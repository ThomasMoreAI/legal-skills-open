"""Chunk integrity gate — Phase 1 Step 1.2.

Blocks `analyzed.json` (or `index.json`) outputs whose `chunks[]` entries do
not have a 1:1 correspondence with physical files under `chunks/`. This
prevents the class of bug where a downstream analyzer (Claude or a future
subagent) fabricates chunks that never existed on disk.

Checks performed, in order:
  1. Every chunk in the JSON has an existing physical file.
  2. Every physical `.txt` file under `chunks/` has a JSON entry.
  3. `char_count` on the JSON entry matches `len(file_text)` (±2 for trailing
     newline tolerance), when `char_count` is present.

Usage:
    from integrity_gate import assert_chunks_consistent
    assert_chunks_consistent(Path("analyzed.json"), Path("chunks"))

CLI:
    python3 scripts/integrity_gate.py --input analyzed.json [--chunks-dir chunks]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


class ChunkIntegrityError(Exception):
    """Raised when chunks in JSON do not match files on disk."""


def _load_index(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _resolve_chunk_path(base_dir: Path, chunk_file: str) -> Path:
    p = Path(chunk_file)
    if p.is_absolute():
        return p
    return base_dir / p


def check_chunks(
    index_data: dict,
    base_dir: Path,
    chunks_dir: Path | None = None,
) -> list[str]:
    """Return a list of integrity errors. Empty list means consistent."""
    errors: list[str] = []
    chunks = index_data.get("chunks") or []

    # Resolve the chunks directory.
    if chunks_dir is None:
        chunks_dir = base_dir / "chunks"
    if not chunks_dir.exists():
        errors.append(f"chunks directory does not exist: {chunks_dir}")
        return errors

    physical_files: set[Path] = {
        p.resolve() for p in chunks_dir.iterdir() if p.suffix == ".txt"
    }
    claimed_files: set[Path] = set()

    for i, chunk in enumerate(chunks):
        idx = chunk.get("index", i)
        chunk_file = chunk.get("chunk_file") or chunk.get("source_file") or chunk.get("file")
        if not chunk_file:
            errors.append(f"chunk #{idx}: missing chunk_file/source_file reference")
            continue

        resolved = _resolve_chunk_path(base_dir, chunk_file).resolve()
        if not resolved.exists():
            errors.append(
                f"chunk #{idx}: file not found on disk: {chunk_file}"
            )
            continue
        claimed_files.add(resolved)

        declared_count = chunk.get("char_count")
        if declared_count is not None:
            try:
                actual = len(resolved.read_text(encoding="utf-8"))
            except Exception as e:
                errors.append(f"chunk #{idx}: could not read {chunk_file}: {e}")
                continue
            if abs(actual - int(declared_count)) > 2:
                errors.append(
                    f"chunk #{idx}: char_count mismatch for {chunk_file} "
                    f"(declared={declared_count}, actual={actual})"
                )

    orphans = physical_files - claimed_files
    for orphan in sorted(orphans):
        errors.append(
            f"orphan chunk file on disk has no JSON entry: "
            f"{orphan.relative_to(chunks_dir.parent) if chunks_dir.parent in orphan.parents else orphan}"
        )

    return errors


def assert_chunks_consistent(
    index_path: Path,
    chunks_dir: Path | None = None,
) -> None:
    """Raise ChunkIntegrityError if chunks in `index_path` are inconsistent with disk."""
    data = _load_index(index_path)
    base_dir = index_path.parent
    errors = check_chunks(data, base_dir, chunks_dir)
    if errors:
        joined = "\n  - ".join(errors)
        raise ChunkIntegrityError(
            f"chunk integrity check failed for {index_path}:\n  - {joined}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Chunk integrity gate")
    parser.add_argument("--input", "-i", required=True,
                        help="Path to analyzed.json or index.json")
    parser.add_argument("--chunks-dir", default=None,
                        help="Path to chunks/ dir (default: alongside --input)")
    args = parser.parse_args(argv)

    index_path = Path(args.input)
    chunks_dir = Path(args.chunks_dir) if args.chunks_dir else None
    try:
        assert_chunks_consistent(index_path, chunks_dir)
    except ChunkIntegrityError as e:
        print(str(e), file=sys.stderr)
        return 1
    print(f"[OK] chunk integrity verified: {index_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
