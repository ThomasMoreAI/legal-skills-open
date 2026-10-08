"""Tests for scripts/integrity_gate.py — Phase 1 Step 1.2."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from integrity_gate import (  # noqa: E402
    ChunkIntegrityError,
    assert_chunks_consistent,
    check_chunks,
)


def _make_fixture(tmp_path: Path, chunks: list[dict], files: dict[str, str]) -> Path:
    chunks_dir = tmp_path / "chunks"
    chunks_dir.mkdir()
    for name, content in files.items():
        (chunks_dir / name).write_text(content, encoding="utf-8")
    index = {"chunks": chunks}
    idx_path = tmp_path / "index.json"
    idx_path.write_text(json.dumps(index), encoding="utf-8")
    return idx_path


def test_consistent_passes(tmp_path):
    files = {"00-a.txt": "hello world", "01-b.txt": "second piece"}
    chunks = [
        {"index": 0, "chunk_file": "chunks/00-a.txt", "char_count": len(files["00-a.txt"])},
        {"index": 1, "chunk_file": "chunks/01-b.txt", "char_count": len(files["01-b.txt"])},
    ]
    idx = _make_fixture(tmp_path, chunks, files)
    assert_chunks_consistent(idx)


def test_missing_physical_file_fails(tmp_path):
    files = {"00-a.txt": "hello"}
    chunks = [
        {"index": 0, "chunk_file": "chunks/00-a.txt", "char_count": 5},
        {"index": 1, "chunk_file": "chunks/99-phantom.txt", "char_count": 10},
    ]
    idx = _make_fixture(tmp_path, chunks, files)
    with pytest.raises(ChunkIntegrityError) as exc:
        assert_chunks_consistent(idx)
    assert "99-phantom.txt" in str(exc.value)
    assert "chunk #1" in str(exc.value)


def test_orphan_file_fails(tmp_path):
    files = {"00-a.txt": "hello", "01-b.txt": "orphaned"}
    chunks = [
        {"index": 0, "chunk_file": "chunks/00-a.txt", "char_count": 5},
    ]
    idx = _make_fixture(tmp_path, chunks, files)
    with pytest.raises(ChunkIntegrityError) as exc:
        assert_chunks_consistent(idx)
    assert "orphan" in str(exc.value).lower()
    assert "01-b.txt" in str(exc.value)


def test_char_count_mismatch_fails(tmp_path):
    files = {"00-a.txt": "hello world"}
    chunks = [
        {"index": 0, "chunk_file": "chunks/00-a.txt", "char_count": 999},
    ]
    idx = _make_fixture(tmp_path, chunks, files)
    with pytest.raises(ChunkIntegrityError) as exc:
        assert_chunks_consistent(idx)
    assert "char_count mismatch" in str(exc.value)


def test_missing_chunk_file_reference_fails(tmp_path):
    files = {"00-a.txt": "hi"}
    chunks = [{"index": 0, "char_count": 2}]
    idx = _make_fixture(tmp_path, chunks, files)
    with pytest.raises(ChunkIntegrityError) as exc:
        assert_chunks_consistent(idx)
    assert "missing chunk_file" in str(exc.value)


def test_check_chunks_returns_errors_list(tmp_path):
    files = {"00-a.txt": "hi"}
    chunks = [{"index": 0, "chunk_file": "chunks/ghost.txt", "char_count": 2}]
    idx = _make_fixture(tmp_path, chunks, files)
    data = json.loads(idx.read_text())
    errors = check_chunks(data, idx.parent)
    assert len(errors) >= 1


def test_real_extraction_is_consistent(tmp_path):
    """Sanity: the legacy extractor produces a consistent layout."""
    import subprocess
    out = tmp_path / "real"
    out.mkdir()
    pdf = REPO_ROOT / "tests" / "golden" / "processo_01_sintetico_simples" / "input.pdf"
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "extract_and_chunk.py"),
         "--input", str(pdf), "--output", str(out)],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    assert_chunks_consistent(out / "index.json")
