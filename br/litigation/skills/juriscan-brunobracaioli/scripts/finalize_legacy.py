"""Standalone Lei 14.905/2024 monetary recalculation for legacy pipeline — Phase A.4.5.

The agents-pipeline `scripts/finalize.py` requires `auditor_findings` to
drive its recalculations. The legacy pipeline doesn't produce that field,
so this script scans `chunks[].valores.condenacao` directly and generates
`monetary_recalculations[]` for any condemnation whose period crosses the
Lei 14.905/2024 cutover (2024-08-30).

Reuses the core Decimal math from scripts/finalize.py to avoid duplication.

Heuristic (conservative):
- Only recalculates when there is a SENTENÇA or ACÓRDÃO chunk with BOTH:
  - valores.condenacao populated (has a BRL value)
  - primary_date populated (has a date)
- Uses the date of the first piece with a condemnation as data_inicio
- Uses the date of the most recent chunk (or today) as data_fim
- Skips silently when data cannot be inferred — does not invent values

Usage:
    python3 scripts/finalize_legacy.py --input analyzed.json --inplace
    python3 scripts/finalize_legacy.py --input analyzed.json --output final.json
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from finalize import (  # noqa: E402
    FinalizeError,
    LEI_14905_CUTOVER,
    _to_decimal,
    recalcular_juros_lei_14905,
)
from utils.dates import parse_brazilian_date  # noqa: E402
from utils.monetary import normalize_brl  # noqa: E402


DECISION_TYPES = {"SENTENÇA", "ACÓRDÃO"}


def _extract_condemnation_from_chunk(chunk: dict) -> tuple[str, str] | None:
    """Return (raw_value_str, iso_date) if the chunk has a valid condemnation
    with a parseable date. None otherwise."""
    valores = chunk.get("valores") or {}
    raw = valores.get("condenacao")
    if not raw or not isinstance(raw, str):
        return None

    # Sanity: must contain a number
    if normalize_brl(raw) in (None, 0):
        return None

    # Primary date — must parse
    primary = chunk.get("primary_date")
    if not primary:
        return None
    try:
        parsed = parse_brazilian_date(primary)
    except Exception:
        parsed = None
    if parsed is None:
        return None

    iso = parsed.isoformat() if isinstance(parsed, (date, datetime)) else None
    if iso is None:
        return None

    return raw, iso


def find_recalculation_candidates(analyzed: dict) -> list[dict]:
    """Walk analyzed.chunks[] looking for condemnations whose period straddles
    the Lei 14.905 cutover. Returns a list of recalc input dicts."""
    chunks = analyzed.get("chunks") or []
    candidates: list[dict] = []

    for ch in chunks:
        tipo = (ch.get("tipo_peca") or "").upper()
        if tipo not in DECISION_TYPES:
            continue
        extracted = _extract_condemnation_from_chunk(ch)
        if extracted is None:
            continue
        raw_value, iso_date = extracted

        # Try to parse the numeric value
        try:
            base = _to_decimal(raw_value)
        except FinalizeError:
            continue
        if base <= 0:
            continue

        candidates.append({
            "chunk_index": ch.get("index"),
            "tipo_peca": tipo,
            "base_raw": raw_value,
            "base_decimal": base,
            "data_inicio": iso_date,
            "chunk_date_obj": date.fromisoformat(iso_date),
        })

    return candidates


def compute_recalculations(analyzed: dict, data_fim: date | None = None) -> list[dict]:
    """For each candidate, generate a monetary_recalculation entry.

    data_fim defaults to today. Only recalculations whose period actually
    crosses the cutover are returned — we don't spam the output with
    no-op entries for purely pre- or post-cutover periods unless the
    period reaches the cutover itself.
    """
    if data_fim is None:
        data_fim = date.today()

    candidates = find_recalculation_candidates(analyzed)
    out: list[dict] = []

    for cand in candidates:
        start = cand["chunk_date_obj"]
        if start >= data_fim:
            continue

        # Does the update period cross or reach the cutover?
        crosses = start < LEI_14905_CUTOVER <= data_fim
        fully_before = data_fim <= LEI_14905_CUTOVER
        fully_after = start >= LEI_14905_CUTOVER

        # Only generate entries when there is something interesting to show
        if not (crosses or fully_before or fully_after):
            continue

        try:
            recalc = recalcular_juros_lei_14905(
                cand["base_decimal"],
                start,
                data_fim,
            )
        except FinalizeError as e:
            out.append({
                "tipo": "JUROS_LEI_14905",
                "chunk_index": cand["chunk_index"],
                "error": str(e),
            })
            continue

        recalc["chunk_index"] = cand["chunk_index"]
        recalc["tipo_peca_source"] = cand["tipo_peca"]
        recalc["base"] = cand["base_raw"]  # preserve original display string
        out.append(recalc)

    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Standalone Lei 14.905/2024 recalculation for legacy pipeline",
    )
    parser.add_argument("--input", "-i", required=True, help="Path to analyzed.json")
    parser.add_argument(
        "--output",
        "-o",
        help="Output path (default: same as input when --inplace)",
    )
    parser.add_argument(
        "--inplace",
        action="store_true",
        help="Write back to --input (ignores --output)",
    )
    parser.add_argument(
        "--data-fim",
        help="Reference end date in ISO YYYY-MM-DD (default: today)",
    )
    args = parser.parse_args(argv)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: input not found: {input_path}", file=sys.stderr)
        return 2

    try:
        analyzed = json.loads(input_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON: {e}", file=sys.stderr)
        return 2

    data_fim: date | None = None
    if args.data_fim:
        try:
            data_fim = date.fromisoformat(args.data_fim)
        except ValueError:
            print(f"ERROR: --data-fim must be ISO YYYY-MM-DD, got {args.data_fim!r}", file=sys.stderr)
            return 2

    recalcs = compute_recalculations(analyzed, data_fim=data_fim)

    if recalcs:
        existing = analyzed.get("monetary_recalculations") or []
        analyzed["monetary_recalculations"] = existing + recalcs
        print(
            f"[finalize_legacy] {len(recalcs)} recalculation(s) appended to monetary_recalculations[]",
            file=sys.stderr,
        )
    else:
        print(
            "[finalize_legacy] no monetary recalculations applicable "
            "(no SENTENÇA/ACÓRDÃO with condenação + date crossing Lei 14.905 cutover)",
            file=sys.stderr,
        )

    if args.inplace:
        out_path = input_path
    elif args.output:
        out_path = Path(args.output)
    else:
        print("ERROR: must pass --inplace or --output", file=sys.stderr)
        return 2

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(analyzed, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
