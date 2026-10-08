"""Content quality sanity check for analyzed.json — non-blocking WARN script.

Phase A.3 — Surfaces shallow analyses where the per-chunk semantic
extraction left canonical fields empty. The script does NOT fail the
pipeline (it always exits 0) — it only emits human-readable warnings to
stderr and a structured JSON summary to stdout.

Why this exists
---------------
Real-world legacy runs sometimes produce analyzed.json files where the
orchestrating Claude session took a shortcut (eg. wrote a build_analyzed.py
helper that hardcoded a few enrichments) instead of doing thorough
per-chunk analysis. The schema validator passes because every canonical
field is technically optional, but the result is an empty shell:
`tipo_peca: null` everywhere, `partes: null`, `valores: null`, vault
notes with only frontmatter and a back-link.

This script measures the populated rate of the canonical fields and
flags suspicious ratios so the user (and the running Claude session) can
notice the gap and re-do Step 3 properly.

Usage
-----
    python3 scripts/content_quality_check.py --input analyzed.json
    python3 scripts/content_quality_check.py --input analyzed.json --json
    python3 scripts/content_quality_check.py --input analyzed.json --strict   # exit 1 on warnings

The default exit code is 0 even when warnings exist. Pass `--strict` to
make warnings block (useful in CI or when wiring this into SKILL.md as a
gate).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Fields we expect to see populated when the corresponding piece type is
# present. Keys are canonical tipo_peca values (matching the taxonomy).
# Values are field names that should be non-empty for that piece type.
EXPECTED_FIELDS_BY_TYPE: dict[str, list[str]] = {
    "PETIÇÃO INICIAL": ["pedidos", "fatos_relevantes", "valores"],
    "CONTESTAÇÃO": ["fatos_relevantes"],
    "RÉPLICA": ["fatos_relevantes"],
    "SENTENÇA": ["decisao", "valores"],
    "ACÓRDÃO": ["decisao", "acordao_structure"],
    "DESPACHO": ["decisao"],
    "APELAÇÃO": ["pedidos"],
    "AGRAVO": ["pedidos"],
    "EMBARGOS": [],
    "RECURSO ESPECIAL": ["pedidos"],
    "RECURSO EXTRAORDINÁRIO": ["pedidos"],
    "LAUDO PERICIAL": ["fatos_relevantes"],
}

# Fields whose absence anywhere is suspicious for any pipeline run with
# > 1 chunks (these are the "every analyzed.json should have at least
# *some* of these populated" canonical fields).
GLOBAL_CANONICAL_FIELDS = [
    "tipo_peca",
    "partes",
    "pedidos",
    "valores",
    "fatos_relevantes",
]


def _is_populated(value) -> bool:
    """Treat None, empty string, empty list, empty dict as not populated."""
    if value is None:
        return False
    if isinstance(value, (str, list, dict)) and len(value) == 0:
        return False
    return True


# Tokens that must appear verbatim in citation_spans when an ACÓRDÃO has
# votacao=MAIORIA AND resultado is a reform — this is the art. 942 CPC
# grounding requirement (Phase A.4.7).
ART_942_TOKENS = ("ampliação", "colegiado", "maioria", "vencido")
REFORM_RESULTS = {"PROVIDO", "PARCIALMENTE_PROVIDO"}


def _check_art_942_grounding(chunks: list) -> list[str]:
    """For every ACÓRDÃO chunk proferido por MAIORIA reformando mérito,
    require at least one citation_spans entry containing the verbatim tokens
    that ground the art. 942 CPC detection.

    Returns a list of warnings (one per offending chunk).
    """
    warnings: list[str] = []
    for ch in chunks:
        if (ch.get("tipo_peca") or "").upper() != "ACÓRDÃO":
            continue
        ac = ch.get("acordao_structure") or {}
        if ac.get("votacao") != "MAIORIA":
            continue
        resultado = ac.get("resultado")
        if resultado not in REFORM_RESULTS:
            continue

        spans = ch.get("citation_spans") or []
        grounded = False
        for s in spans:
            src = (s.get("source_text") or "").lower()
            if any(tok in src for tok in ART_942_TOKENS):
                grounded = True
                break
        if not grounded:
            idx = ch.get("index", "?")
            warnings.append(
                f"WARN: chunk[{idx}] ACÓRDÃO por maioria reformando mérito "
                f"(resultado={resultado}) sem citation_spans grounding o art. 942. "
                f"Adicione um trecho verbatim contendo algum de: {ART_942_TOKENS}"
            )
    return warnings


def evaluate(analyzed: dict) -> dict:
    """Evaluate the content quality of an analyzed.json document.

    Returns a dict with:
    - `warnings` — human-readable strings (summary level)
    - `stats` — per-field populated counts
    - `total_chunks` — chunk count
    - `chunks_needing_retry` — list of {index, tipo_peca, chunk_file, missing_fields[]}
      identifying WHICH chunks should be re-analyzed during SKILL.md Step 3b
      retry loop
    """
    chunks = analyzed.get("chunks", []) or []
    total = len(chunks)
    warnings: list[str] = []
    stats: dict[str, dict] = {}
    chunks_needing_retry: list[dict] = []

    if total == 0:
        warnings.append("WARN: analyzed.json has zero chunks — extraction or chunking failed")
        return {
            "warnings": warnings,
            "stats": stats,
            "total_chunks": 0,
            "chunks_needing_retry": [],
        }

    # Count populated rate for each global canonical field across chunks
    for field in GLOBAL_CANONICAL_FIELDS:
        populated = sum(1 for c in chunks if _is_populated(c.get(field)))
        stats[field] = {"populated": populated, "total": total}
        if populated == 0:
            warnings.append(
                f"WARN: 0/{total} chunks têm campo {field!r} populado — "
                f"análise per-chunk pode estar incompleta (SKILL.md Step 3)"
            )
        elif populated < total / 2 and total >= 4:
            warnings.append(
                f"WARN: apenas {populated}/{total} chunks têm campo {field!r} populado"
            )

    # Per-piece-type expected-field check (chunk-level retry plan)
    retry_map: dict[str, dict] = {}
    for i, chunk in enumerate(chunks):
        tipo = chunk.get("tipo_peca")
        if not tipo:
            # Chunk sem tipo_peca é sempre retry
            key = str(chunk.get("index", i))
            retry_map[key] = {
                "index": chunk.get("index", i),
                "tipo_peca": None,
                "chunk_file": chunk.get("chunk_file"),
                "missing_fields": ["tipo_peca"],
            }
            continue
        expected = EXPECTED_FIELDS_BY_TYPE.get(tipo.upper(), [])
        missing: list[str] = []
        for field in expected:
            if not _is_populated(chunk.get(field)):
                missing.append(field)
                warnings.append(
                    f"WARN: chunk[{i}] tipo_peca={tipo!r} sem campo esperado {field!r}"
                )
        if missing:
            key = str(chunk.get("index", i))
            retry_map[key] = {
                "index": chunk.get("index", i),
                "tipo_peca": tipo,
                "chunk_file": chunk.get("chunk_file"),
                "missing_fields": missing,
            }

    chunks_needing_retry = list(retry_map.values())

    # Phase A.4.7 — art. 942 grounding enforcement
    for warning in _check_art_942_grounding(chunks):
        warnings.append(warning)
        # Also add to retry plan so Claude knows which chunk to fix
        import re
        m = re.search(r"chunk\[(\d+)\]", warning)
        if m:
            idx = int(m.group(1))
            key = str(idx)
            if key not in retry_map:
                retry_map[key] = {
                    "index": idx,
                    "tipo_peca": "ACÓRDÃO",
                    "chunk_file": next(
                        (c.get("chunk_file") for c in chunks if c.get("index") == idx),
                        None,
                    ),
                    "missing_fields": ["citation_spans (art. 942 grounding)"],
                }
            else:
                retry_map[key]["missing_fields"].append("citation_spans (art. 942 grounding)")
    chunks_needing_retry = list(retry_map.values())

    # Schema version sanity
    if not analyzed.get("schema_version") and not analyzed.get("analysis_version"):
        warnings.append(
            "WARN: analyzed.json sem schema_version/analysis_version — "
            "marcação de versão recomendada"
        )

    return {
        "warnings": warnings,
        "stats": stats,
        "total_chunks": total,
        "chunks_needing_retry": chunks_needing_retry,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Non-blocking content quality check for analyzed.json",
    )
    parser.add_argument("--input", "-i", required=True, help="Path to analyzed.json")
    parser.add_argument("--json", action="store_true", help="Emit JSON to stdout")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any warning is emitted (default: always exit 0)",
    )
    parser.add_argument(
        "--per-chunk-retry-plan",
        action="store_true",
        help="Print a human-readable retry plan identifying which chunks need "
             "re-analysis and what fields are missing",
    )
    args = parser.parse_args(argv)

    path = Path(args.input)
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    try:
        analyzed = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON: {e}", file=sys.stderr)
        return 2

    result = evaluate(analyzed)

    if args.json:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        if not result["warnings"]:
            print(f"[OK] content quality check passed ({result['total_chunks']} chunks)")
        else:
            print(
                f"[CONTENT QUALITY] {len(result['warnings'])} warning(s) "
                f"in {result['total_chunks']} chunk(s):",
                file=sys.stderr,
            )
            for w in result["warnings"]:
                print(f"  - {w}", file=sys.stderr)

    if args.per_chunk_retry_plan and result.get("chunks_needing_retry"):
        print("\nChunks precisando re-análise:")
        for entry in result["chunks_needing_retry"]:
            idx = entry.get("index")
            tipo = entry.get("tipo_peca") or "(tipo_peca ausente)"
            chunk_file = entry.get("chunk_file") or "(sem chunk_file)"
            missing = ", ".join(entry.get("missing_fields", []))
            print(f"  [{idx}] {tipo} ({chunk_file}) → faltam: {missing}")
        print(
            "\nPara cada entrada acima:\n"
            "  1. Read o chunk_file\n"
            "  2. Re-analise preenchendo os missing_fields\n"
            "  3. Write chunks/<index>.analysis.json atualizado\n"
            "  4. Re-rode merge_chunk_analysis.py + content_quality_check.py"
        )

    # --strict: block on warnings OR on any chunk needing retry
    if args.strict and (result["warnings"] or result.get("chunks_needing_retry")):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
