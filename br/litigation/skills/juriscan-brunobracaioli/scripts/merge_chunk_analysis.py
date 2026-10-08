"""Merge per-chunk analysis files into analyzed.json — Phase A.4.1.

This script consolidates the per-chunk semantic analysis files produced
during SKILL.md Step 3b (chunks/NN.analysis.json — one per chunk) into the
single analyzed.json skeleton produced by analyzed_init.py.

Workflow:
    1. analyzed_init.py → analyzed.json skeleton with _pending_analysis markers
    2. Claude reads each chunks/NN-*.txt and Writes chunks/NN.analysis.json
    3. merge_chunk_analysis.py (this script) → validates each analysis file
       against references/chunk_analysis_schema.json and merges semantic
       fields into the corresponding entry of analyzed.chunks[]

Split-semantic support:
    When the chunker groups multiple pieces in a single physical file, the
    user can produce multiple analysis files (chunks/02a.analysis.json,
    chunks/02b.analysis.json) for the same physical chunk. Each entry must
    set `chunk_file_override` to the original chunk_file path. The merged
    analyzed.chunks[] will contain N entries all pointing to the same
    physical file, satisfying the integrity gate.

Error modes:
    - Missing chunks/NN.analysis.json for a pending index → exit 1 with list
    - Schema validation failure → exit 1 with details
    - Detected helper-script pattern (chunks/build_analyzed.py etc.) → warns
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "references" / "chunk_analysis_schema.json"

SEMANTIC_FIELDS = [
    "tipo_peca",
    "partes",
    "pedidos",
    "argumentos_chave",
    "valores",
    "fatos_relevantes",
    "decisao",
    "resumo",
    "acordao_structure",
    "artigos_lei",
    "jurisprudencia",
    "binding_precedents",
    "prazos",
    "citation_spans",
    "instancia",
    # v3.1.2: primary_date and dates_found can be overridden per-piece
    # (critical for split-semantic where each piece has its own date)
    "primary_date",
    "dates_found",
]

# Filename pattern: 00.analysis.json, 02a.analysis.json, etc.
ANALYSIS_FILE_RE = re.compile(r"^(?P<idx>[0-9]+[a-z]?)\.analysis\.json$")

HELPER_SCRIPT_PATTERNS = [
    "build_analyzed.py",
    "build_analysis.py",
    "populate_analyzed.py",
    "fix_analyzed.py",
]


def _load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _looks_post_merged(analyzed: dict) -> bool:
    """Detect if analyzed.json is already in a merged state.

    After a successful merge, chunks have semantic fields populated,
    no `_pending_analysis` markers, and may have been renumbered (the
    number of chunks may exceed the original physical chunk count due
    to split-semantic). If we re-run merge against such a file, the
    loop will try to match renumbered indices (4, 5, 6) against
    non-existent chunks/04.analysis.json files. Re-initialize from
    index.json instead.
    """
    chunks = analyzed.get("chunks") or []
    if not chunks:
        return False
    has_pending = any(ch.get("_pending_analysis") for ch in chunks)
    if has_pending:
        return False
    # Post-merge state markers: original_index set, or semantic fields present
    for ch in chunks:
        if "original_index" in ch:
            return True
        if ch.get("tipo_peca") or ch.get("resumo") or ch.get("decisao"):
            return True
    return False


def _validate(data: dict, schema: dict, source: str) -> list[str]:
    """Validate a per-chunk analysis file against the schema. Returns errors."""
    try:
        import jsonschema
    except ImportError:
        return [f"{source}: jsonschema package not available"]

    validator = jsonschema.Draft7Validator(schema)
    errors = []
    for err in validator.iter_errors(data):
        path = ".".join(str(p) for p in err.absolute_path)
        loc = f" at {path}" if path else ""
        errors.append(f"{source}{loc}: {err.message}")
    return errors


def discover_analysis_files(chunks_dir: Path) -> dict[str, Path]:
    """Find all chunks/NN.analysis.json files and index them by string index."""
    found: dict[str, Path] = {}
    if not chunks_dir.exists():
        return found
    for p in sorted(chunks_dir.iterdir()):
        m = ANALYSIS_FILE_RE.match(p.name)
        if m:
            found[m.group("idx")] = p
    return found


def check_helper_scripts(chunks_dir: Path, output_dir: Path) -> list[str]:
    """Warn if the user wrote a helper Python script to hardcode enrichments."""
    warnings = []
    for d in [chunks_dir, output_dir, output_dir.parent]:
        if not d.exists():
            continue
        for pattern in HELPER_SCRIPT_PATTERNS:
            matches = list(d.glob(pattern))
            if matches:
                warnings.append(
                    f"WARN: detected helper script {matches[0]} — "
                    f"this is the anti-pattern from v3.0.1. Prefer one "
                    f"chunks/NN.analysis.json Write per chunk."
                )
    return warnings


def merge(
    analyzed: dict, analysis_files: dict[str, Path], schema: dict
) -> tuple[dict, list[str]]:
    """Merge analysis files into analyzed.chunks[]. Returns (analyzed, errors).

    Ordering (Phase A.4.1 + v3.1.1 fix):
    1. Process numeric chunks in skeleton order.
    2. Immediately after each parent chunk, insert its suffixed children
       (01a, 01b, ...) in alphabetical order. This produces a natural
       chronological flow when split-semantic is used (the split pieces
       stay next to their physical parent).
    3. After all merging, RENUMBER every entry to a sequential integer
       index starting at 0. This guarantees the output satisfies
       output_schema_v2.json (which requires integer indices) regardless
       of what string indices the per-chunk files used. The original
       user-facing index (e.g. "2a") is preserved in `original_index`
       for debugging.
    """
    errors: list[str] = []
    chunks = analyzed.get("chunks", []) or []

    # Map pending chunks by int index for fast lookup
    pending_by_int_idx = {int(ch["index"]): ch for ch in chunks if "index" in ch}

    # Partition keys into numeric vs suffixed, and group suffixed by parent
    numeric_keys = [k for k in analysis_files if k.isdigit()]
    suffixed_keys = [k for k in analysis_files if not k.isdigit()]
    suffixed_by_parent: dict[int, list[str]] = {}
    for key in suffixed_keys:
        m = re.match(r"^(\d+)", key)
        if not m:
            errors.append(
                f"ERROR: {analysis_files[key]}: suffixed index {key!r} has no numeric prefix"
            )
            continue
        parent_idx = int(m.group(1))
        suffixed_by_parent.setdefault(parent_idx, []).append(key)
    for parent_idx in suffixed_by_parent:
        suffixed_by_parent[parent_idx].sort()

    def _load_and_validate(key: str) -> dict | None:
        """Load analysis file and validate against chunk_analysis schema.
        Returns None on error (errors are appended to the outer list)."""
        path = analysis_files[key]
        try:
            analysis = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"ERROR: {path}: invalid JSON: {e}")
            return None
        schema_errors = _validate(analysis, schema, str(path))
        if schema_errors:
            errors.extend(schema_errors)
            return None
        return analysis

    def _build_suffixed_entry(key: str, analysis: dict, parent: dict) -> dict:
        """Build a new chunk entry for a suffixed (split-semantic) analysis.

        Technical fields (char_count, chunk_file, page_range, ocr_confidence,
        primary_date, dates_found) are inherited from the parent chunk by
        default. The per-chunk file can override any of them by including
        the field explicitly — most important is primary_date, since each
        split-semantic piece typically has its own date that differs from
        the parent's.
        """
        new_entry = {
            k: parent.get(k)
            for k in [
                "char_count",
                "chunk_file",
                "page_range",
                "ocr_confidence",
                "primary_date",
                "dates_found",
            ]
            if k in parent
        }
        # Preserve the user-facing string index for debugging
        new_entry["original_index"] = analysis.get("index", key)
        new_entry["label"] = analysis.get("tipo_peca", parent.get("label"))
        # Allow override of chunk_file (split-semantic typically reuses parent's file)
        if "chunk_file_override" in analysis:
            new_entry["chunk_file"] = analysis["chunk_file_override"]
        # Semantic fields override the inherited technical fields
        # (primary_date and dates_found are in SEMANTIC_FIELDS since v3.1.2)
        for field in SEMANTIC_FIELDS:
            if field in analysis and field != "chunk_file_override":
                new_entry[field] = analysis[field]
        return new_entry

    merged_chunks: list[dict] = []

    # Process each parent chunk, then immediately its suffixed children
    for ch in chunks:
        idx = int(ch["index"])
        # Find the matching numeric analysis file
        key = None
        for candidate in [f"{idx:02d}", str(idx)]:
            if candidate in numeric_keys:
                key = candidate
                break

        if key is None:
            errors.append(
                f"ERROR: chunk[{idx}] ({ch.get('label', '?')}) has no matching "
                f"chunks/{idx:02d}.analysis.json file. Produce one via Write."
            )
            merged_chunks.append(ch)  # Keep skeleton
        else:
            analysis = _load_and_validate(key)
            if analysis is None:
                merged_chunks.append(ch)
            else:
                merged = dict(ch)
                merged.pop("_pending_analysis", None)
                for field in SEMANTIC_FIELDS:
                    if field in analysis:
                        merged[field] = analysis[field]
                if "tipo_peca" in analysis and analysis["tipo_peca"]:
                    merged["tipo_peca"] = analysis["tipo_peca"]
                # Preserve original numeric index as string for reference
                merged["original_index"] = idx
                merged_chunks.append(merged)

        # Insert suffixed children immediately after their parent
        for sk in suffixed_by_parent.get(idx, []):
            analysis = _load_and_validate(sk)
            if analysis is None:
                continue
            parent = ch  # Technical fields come from the skeleton parent
            merged_chunks.append(_build_suffixed_entry(sk, analysis, parent))

    # Renumber every entry to sequential integer index — this satisfies
    # output_schema_v2.json (which requires integer) and keeps downstream
    # scripts (contradiction_report, instance_tracker) happy.
    for new_idx, entry in enumerate(merged_chunks):
        entry["index"] = new_idx
        entry.pop("_pending_analysis", None)

    analyzed["chunks"] = merged_chunks
    analyzed["total_chunks"] = len(merged_chunks)

    return analyzed, errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Merge per-chunk analysis files into analyzed.json",
    )
    parser.add_argument(
        "--analyzed",
        "-a",
        required=True,
        help="Path to analyzed.json skeleton (produced by analyzed_init.py)",
    )
    parser.add_argument(
        "--chunks-dir",
        "-c",
        required=True,
        help="Directory containing chunks/NN.analysis.json files",
    )
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="Path to write merged analyzed.json",
    )
    parser.add_argument(
        "--allow-missing",
        action="store_true",
        help="Continue even if some chunks have no analysis file (exit 0 with warnings)",
    )
    args = parser.parse_args(argv)

    analyzed_path = Path(args.analyzed)
    chunks_dir = Path(args.chunks_dir)

    if not analyzed_path.exists():
        print(f"ERROR: analyzed file not found: {analyzed_path}", file=sys.stderr)
        return 2

    try:
        analyzed = json.loads(analyzed_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON in {analyzed_path}: {e}", file=sys.stderr)
        return 2

    # v3.1.4: idempotency — if analyzed.json is already in post-merged state
    # (chunks without _pending_analysis markers, possibly renumbered), rebuild
    # the skeleton from index.json in the same directory. This lets the retry
    # loop in SKILL.md Step 4 re-run merge without needing a manual reset.
    if _looks_post_merged(analyzed):
        index_path = analyzed_path.parent / "index.json"
        if index_path.exists():
            print(
                f"[merge_chunk_analysis] detected post-merged state — "
                f"rebuilding skeleton from {index_path.name}",
                file=sys.stderr,
            )
            try:
                from analyzed_init import build_skeleton  # type: ignore
            except ImportError:
                sys.path.insert(0, str(Path(__file__).parent))
                from analyzed_init import build_skeleton  # type: ignore
            index_data = json.loads(index_path.read_text(encoding="utf-8"))
            analyzed = build_skeleton(index_data)
        else:
            print(
                f"WARN: analyzed.json appears post-merged but {index_path} "
                f"not found — matching by chunk_file basename as fallback",
                file=sys.stderr,
            )

    try:
        schema = _load_schema()
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR: cannot load schema at {SCHEMA_PATH}: {e}", file=sys.stderr)
        return 2

    # Warn about helper scripts
    for w in check_helper_scripts(chunks_dir, analyzed_path.parent):
        print(w, file=sys.stderr)

    analysis_files = discover_analysis_files(chunks_dir)
    if not analysis_files:
        print(
            f"ERROR: no chunks/NN.analysis.json files found in {chunks_dir}. "
            f"Run Step 3b: for each chunk, Read the source and Write "
            f"chunks/NN.analysis.json with the semantic analysis.",
            file=sys.stderr,
        )
        return 1

    merged, errors = merge(analyzed, analysis_files, schema)

    if errors:
        print(f"[merge_chunk_analysis] {len(errors)} error(s):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        if not args.allow_missing:
            return 1

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    n = len(merged.get("chunks", []))
    print(f"[merge_chunk_analysis] merged {n} chunk(s) → {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
