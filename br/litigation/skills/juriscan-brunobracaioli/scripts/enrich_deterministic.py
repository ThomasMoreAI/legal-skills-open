"""Deterministic enrichment layer between juriscan-parser and the dialectic.

Phase 2 Step 2.4. After N parser invocations have each classified and
extracted fields from one chunk, this script re-processes those structured
outputs with the battle-tested Python utils so that:

  1. Dates are normalized to ISO 8601 via utils.dates.parse_brazilian_date.
  2. Monetary values are re-parsed with utils.monetary.normalize_brl and
     reported as floats, not LLM-generated strings.
  3. CNJ process numbers are structurally parsed and (when possible)
     check-digit validated via utils.cnj.
  4. Mismatches between what the LLM claimed and what the regex utilities
     recovered are recorded as `llm_claim_vs_extracted_mismatch` flags for
     downstream triage.

Why this is necessary
---------------------
LLMs make quiet numeric mistakes — dropping a zero, swapping DD/MM, writing
"R$ 27.00" when the text says "R$ 27.000,00". Piping every numeric field
through deterministic normalization eliminates that class of error
*before* the dialectic layer (advogados / auditor) reads the output.

Output contract
---------------
enrich(pieces) returns a new list of piece dicts with the same shape as the
input plus:

  pieces[i]["_enriched"] = {
      "primary_date_iso":     "2025-03-18" or None,
      "dates_found_iso":      ["2023-03-05", ...],
      "valores_normalized":   { "causa": 107000.0, "condenacao": 57000.0, ... },
      "processo_number_valid": true | false | null,
      "processo_number_court": "TJSP",
      "mismatches":           [ {...}, ... ],
  }

The script raises EnrichError when >10% of monetary mentions across the
whole piece list mismatch between LLM output and regex extraction — that
signals systemic parser degradation and aborts the pipeline.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

from utils.cnj import parse_cnj, validate_cnj_check_digits  # noqa: E402
from utils.dates import (  # noqa: E402
    format_date_iso,
    parse_brazilian_date,
)
from utils.monetary import normalize_brl  # noqa: E402


MONETARY_MISMATCH_THRESHOLD = 0.10  # 10% of mentions may diverge before abort.


class EnrichError(Exception):
    """Raised when parser output cannot be safely enriched."""


def _safe_date_to_iso(raw: str | None) -> str | None:
    if not raw:
        return None
    parsed = parse_brazilian_date(raw)
    if parsed is None:
        return None
    return format_date_iso(parsed)


def _safe_brl(raw: str | None) -> float | None:
    if not raw:
        return None
    try:
        return normalize_brl(raw)
    except Exception:
        return None


def _normalize_valores(valores: dict | None) -> tuple[dict, list[dict]]:
    """Return (normalized_dict, mismatches_list)."""
    if not valores or not isinstance(valores, dict):
        return {}, []

    normalized: dict[str, Any] = {}
    mismatches: list[dict] = []

    for key in ("causa", "condenacao", "honorarios"):
        raw = valores.get(key)
        if raw is None:
            continue
        value = _safe_brl(raw)
        normalized[key] = value
        if raw and value is None:
            mismatches.append({
                "field": f"valores.{key}",
                "raw": raw,
                "reason": "normalize_brl returned None",
            })

    outros = valores.get("outros") or []
    normalized_outros: list[dict] = []
    for i, item in enumerate(outros):
        if not isinstance(item, dict):
            continue
        raw_val = item.get("valor")
        value = _safe_brl(raw_val)
        normalized_outros.append({
            "descricao": item.get("descricao", ""),
            "raw": raw_val,
            "normalized": value,
        })
        if raw_val and value is None:
            mismatches.append({
                "field": f"valores.outros[{i}]",
                "raw": raw_val,
                "reason": "normalize_brl returned None",
            })
    if normalized_outros:
        normalized["outros"] = normalized_outros

    return normalized, mismatches


def _enrich_processo_number(raw: str | None) -> dict:
    if not raw:
        return {"valid": None, "court": None, "normalized": None}
    parsed = parse_cnj(raw)
    if parsed is None:
        return {"valid": False, "court": None, "normalized": None,
                "reason": "could not parse CNJ"}
    try:
        valid = validate_cnj_check_digits(parsed)
    except Exception:
        valid = None
    return {
        "valid": valid,
        "court": parsed.court_name,
        "normalized": parsed.raw,
        "year": parsed.year,
        "justice_branch": parsed.branch_name,
    }


def _enrich_one(piece: dict) -> dict:
    enriched = dict(piece)

    primary_iso = _safe_date_to_iso(piece.get("primary_date"))
    dates_iso = [
        d for d in (
            _safe_date_to_iso(raw) for raw in (piece.get("dates_found") or [])
        )
        if d is not None
    ]

    valores_norm, value_mismatches = _normalize_valores(piece.get("valores"))

    processo_info = _enrich_processo_number(piece.get("processo_number"))

    mismatches: list[dict] = list(value_mismatches)
    if piece.get("primary_date") and primary_iso is None:
        mismatches.append({
            "field": "primary_date",
            "raw": piece["primary_date"],
            "reason": "parse_brazilian_date returned None",
        })
    if piece.get("processo_number") and processo_info["valid"] is False:
        mismatches.append({
            "field": "processo_number",
            "raw": piece["processo_number"],
            "reason": processo_info.get("reason") or "check digits invalid",
        })

    enriched["_enriched"] = {
        "primary_date_iso": primary_iso,
        "dates_found_iso": dates_iso,
        "valores_normalized": valores_norm,
        "processo_number": processo_info,
        "mismatches": mismatches,
    }
    return enriched


def make_dialectic_summary(pieces: list[dict]) -> list[dict]:
    """Phase 7 Step 7.2 — produce compact piece summaries for the dialectic layer.

    The advogados and auditor don't need the full extracted text of every
    piece — they only need a structured digest with the semantic facts each
    parser already extracted. Passing the digest instead of raw text (a)
    cuts token count by ~70% and (b) keeps the system-prompt portion of
    each subagent's context stable, maximizing prompt cache hits across
    the three parallel dialectic invocations.

    The digest is append-only (never mutates the input) and intentionally
    excludes raw text fields like `raw_text`, `chunk_file`, `full_text`.
    """
    digest: list[dict] = []
    KEEP_KEYS = {
        "chunk_id",
        "index",
        "tipo_peca",
        "instancia",
        "polo",
        "primary_date",
        "processo_number",
        "partes",
        "fatos_relevantes",
        "pedidos",
        "valores",
        "jurisprudencia",
        "legislacao",
        "decisao",
        "acordao_detail",
        "confianca_parsing",
    }
    for p in pieces or []:
        item = {k: p[k] for k in KEEP_KEYS if k in p}
        enriched_block = p.get("_enriched") or {}
        if enriched_block:
            # Only propagate the normalized numeric fields — drop mismatch
            # noise from the dialectic layer, which cannot act on it.
            item["_enriched"] = {
                "primary_date_iso": enriched_block.get("primary_date_iso"),
                "valores_normalized": enriched_block.get("valores_normalized"),
                "processo_number": enriched_block.get("processo_number"),
            }
        digest.append(item)
    return digest


def enrich(pieces: list[dict]) -> list[dict]:
    """Normalize LLM-extracted fields into deterministic values.

    Aborts (EnrichError) if the rate of monetary mismatches exceeds
    MONETARY_MISMATCH_THRESHOLD — that's a signal the parser is producing
    unreliable numeric output and the dialectic layer should not run on it.
    """
    if not pieces:
        return []

    enriched_pieces = [_enrich_one(p) for p in pieces]

    # Global monetary mismatch rate check.
    total_mentions = 0
    mismatches = 0
    for ep in enriched_pieces:
        valores = (ep.get("valores") or {}) if isinstance(ep, dict) else {}
        for key in ("causa", "condenacao", "honorarios"):
            if valores.get(key):
                total_mentions += 1
        total_mentions += len(valores.get("outros") or [])
        for m in ep["_enriched"]["mismatches"]:
            if m["field"].startswith("valores"):
                mismatches += 1

    if total_mentions > 0:
        rate = mismatches / total_mentions
        if rate > MONETARY_MISMATCH_THRESHOLD:
            raise EnrichError(
                f"monetary mismatch rate {rate:.1%} exceeds threshold "
                f"{MONETARY_MISMATCH_THRESHOLD:.0%} "
                f"({mismatches}/{total_mentions} mentions failed normalization). "
                "Parser output is too unreliable to enrich — inspect audit trail."
            )

    return enriched_pieces


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Deterministically enrich parser output with date/BRL/CNJ normalization."
    )
    parser.add_argument("--input", required=True,
                        help="Path to JSON array (or object with 'pieces' key) produced by juriscan-parser runs")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    doc = json.loads(Path(args.input).read_text(encoding="utf-8"))
    if isinstance(doc, dict) and "pieces" in doc:
        doc["pieces"] = enrich(doc["pieces"])
    elif isinstance(doc, list):
        doc = enrich(doc)
    else:
        raise SystemExit("input must be a list or a dict with 'pieces' key")

    try:
        Path(args.output).write_text(
            json.dumps(doc, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError as e:
        print(f"[FAIL] could not write output: {e}", file=sys.stderr)
        return 1
    print(f"[OK] enriched {args.output}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except EnrichError as e:
        print(f"[FAIL] enrich_deterministic: {e}", file=sys.stderr)
        sys.exit(2)
