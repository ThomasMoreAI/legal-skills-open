"""Persist segmenter output to disk as physical chunk files + index.json.

Phase 2 Step 2.2. Consumes a validated segmenter output JSON + the raw text
used as its input, slices the text by (start_char, end_char), writes one
`chunks/NN-<slug>.txt` file per chunk, and emits an index.json that matches
the legacy extract_and_chunk.py shape (index, label, char_count, chunk_file,
primary_date placeholder) so downstream legacy steps keep working during the
transition.

Invariants enforced at write time (raises PersistError):
  - segmenter output schema valid (delegated to agent_io.validate)
  - raw_text length matches raw_text_length declared by segmenter
  - chunks cover the entire raw_text without gaps or overlap
  - persisted chunks pass integrity_gate.assert_chunks_consistent
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

from agent_io import validate_agent_output  # noqa: E402
from integrity_gate import assert_chunks_consistent  # noqa: E402


class PersistError(Exception):
    """Raised when the segmenter output cannot be persisted safely."""


def _slug(label: str) -> str:
    norm = unicodedata.normalize("NFKD", label)
    norm = norm.encode("ascii", "ignore").decode("ascii")
    norm = re.sub(r"[^a-zA-Z0-9]+", "-", norm).strip("-").lower()
    return norm or "peca"


def _verify_coverage(chunks: list[dict], raw_len: int) -> None:
    if not chunks:
        raise PersistError("segmenter returned zero chunks")
    if chunks[0]["start_char"] != 0:
        raise PersistError(
            f"first chunk does not start at 0: start_char={chunks[0]['start_char']}"
        )
    if chunks[-1]["end_char"] != raw_len:
        raise PersistError(
            f"last chunk does not end at raw_len: "
            f"end_char={chunks[-1]['end_char']}, raw_len={raw_len}"
        )
    for i, ch in enumerate(chunks):
        if ch["end_char"] <= ch["start_char"]:
            raise PersistError(
                f"chunk {ch['id']} has non-positive length: "
                f"{ch['start_char']}..{ch['end_char']}"
            )
        if i > 0 and ch["start_char"] != chunks[i - 1]["end_char"]:
            raise PersistError(
                f"gap/overlap between chunk {chunks[i-1]['id']} "
                f"(end={chunks[i-1]['end_char']}) and {ch['id']} "
                f"(start={ch['start_char']})"
            )


def persist(
    segmenter_output_path: Path,
    raw_text_path: Path,
    output_dir: Path,
    *,
    skip_validate: bool = False,
) -> Path:
    """Materialize chunks on disk. Returns path to the written index.json."""
    # 1. Validate the segmenter JSON against its schema.
    if not skip_validate:
        ok, errors = validate_agent_output("segmenter", segmenter_output_path)
        if not ok:
            raise PersistError(
                "segmenter output failed schema validation:\n  - "
                + "\n  - ".join(errors)
            )

    seg = json.loads(segmenter_output_path.read_text(encoding="utf-8"))
    raw_text = raw_text_path.read_text(encoding="utf-8")
    raw_len = len(raw_text)

    declared_len = seg["raw_text_length"]
    if declared_len != raw_len:
        raise PersistError(
            f"raw_text_length mismatch: segmenter declared {declared_len}, "
            f"file has {raw_len} chars (stale input?)"
        )

    chunks = seg["chunks"]
    _verify_coverage(chunks, raw_len)

    chunks_dir = output_dir / "chunks"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    # Remove any stale *.txt in chunks/ to avoid orphans from previous runs.
    for stale in chunks_dir.glob("*.txt"):
        stale.unlink()

    index_chunks: list[dict] = []
    for i, ch in enumerate(chunks):
        start, end = ch["start_char"], ch["end_char"]
        text_slice = raw_text[start:end]
        slug = _slug(ch["tipo_provavel"])
        filename = f"{i:02d}-{slug}.txt"
        file_path = chunks_dir / filename
        file_path.write_text(text_slice, encoding="utf-8")

        index_chunks.append({
            "index": i,
            "id": ch["id"],
            "label": ch["tipo_provavel"],
            "char_count": len(text_slice),
            "chunk_file": f"chunks/{filename}",
            "start_char": start,
            "end_char": end,
            "confianca": ch["confianca"],
            "evidencia": ch.get("evidencia"),
            "page_range": ch.get("page_range"),
        })

    index = {
        "generated_at": None,
        "source": "juriscan-segmenter",
        "schema_version": seg["schema_version"],
        "segmenter_notes": seg.get("notes"),
        "raw_text_length": raw_len,
        "total_chunks": len(index_chunks),
        "chunks": index_chunks,
    }
    index_path = output_dir / "index.json"
    index_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 4. Final check: integrity gate (defense in depth).
    assert_chunks_consistent(index_path)
    return index_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Persist juriscan-segmenter output to disk as chunks/*.txt + index.json"
    )
    parser.add_argument("--segmenter-output", required=True,
                        help="Path to the JSON produced by juriscan-segmenter")
    parser.add_argument("--raw-text", required=True,
                        help="Path to the raw_text.txt the segmenter saw")
    parser.add_argument("--output-dir", required=True,
                        help="Directory where chunks/ and index.json will be written")
    parser.add_argument("--skip-validate", action="store_true",
                        help="Skip jsonschema validation of the segmenter output")
    args = parser.parse_args(argv)

    try:
        index_path = persist(
            Path(args.segmenter_output),
            Path(args.raw_text),
            Path(args.output_dir),
            skip_validate=args.skip_validate,
        )
    except PersistError as e:
        print(f"[FAIL] persist_chunks: {e}", file=sys.stderr)
        return 1
    print(f"[OK] wrote {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
