"""Initialize analyzed.json skeleton from index.json — Phase A.4.1.

This script creates the starting point for per-chunk analysis. It reads the
index.json produced by extract_and_chunk.py and produces an analyzed.json
that contains all the technical fields (index, label, char_count, chunk_file,
primary_date, dates_found, page_range, ocr_confidence) but with semantic
fields marked as pending via `_pending_analysis: true`.

The SKILL.md Step 3 workflow then uses Write to create one analysis file per
chunk (chunks/NN.analysis.json), and merge_chunk_analysis.py consolidates
those back into analyzed.json.

Usage:
    python3 scripts/analyzed_init.py --index output/index.json --output output/analyzed.json

Output is a valid skeleton — the integrity gate in schema_validator.py
passes (chunks are 1:1 with physical files), but content_quality_check.py
will flag it as empty until semantic enrichment happens.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

TECHNICAL_FIELDS = [
    "index",
    "label",
    "char_count",
    "primary_date",
    "dates_found",
    "page_range",
    "ocr_confidence",
    "chunk_file",
    "processo_number",
]


def build_skeleton(index: dict) -> dict:
    """Build analyzed.json skeleton preserving technical fields from index.json."""
    chunks = index.get("chunks", []) or []
    skeleton_chunks = []
    for ch in chunks:
        entry = {k: ch.get(k) for k in TECHNICAL_FIELDS if k in ch}
        entry["_pending_analysis"] = True
        skeleton_chunks.append(entry)

    return {
        "analysis_version": "2.0",
        "schema_version": "2.0",
        "generated_at": index.get("generated_at"),
        "source_file": index.get("source_file"),
        "pdf_info": index.get("pdf_info"),
        "processo_number": index.get("processo_number"),
        "total_characters": index.get("total_characters"),
        "total_chunks": index.get("total_chunks", len(skeleton_chunks)),
        "chunks": skeleton_chunks,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Initialize analyzed.json skeleton from index.json",
    )
    parser.add_argument("--index", "-i", required=True, help="Path to index.json")
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="Path to analyzed.json (will be overwritten)",
    )
    args = parser.parse_args(argv)

    index_path = Path(args.index)
    if not index_path.exists():
        print(f"ERROR: index file not found: {index_path}", file=sys.stderr)
        return 2

    try:
        index = json.loads(index_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON in {index_path}: {e}", file=sys.stderr)
        return 2

    skeleton = build_skeleton(index)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(skeleton, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    n = len(skeleton["chunks"])
    print(
        f"[analyzed_init] skeleton written with {n} pending chunk(s) → {out_path}"
    )
    print(
        "Next step: Read each chunks/NN-*.txt, analyze it, and Write chunks/NN.analysis.json"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
