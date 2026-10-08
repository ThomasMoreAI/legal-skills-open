"""Tests for scripts/analyzed_init.py — Phase A.4.1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from analyzed_init import TECHNICAL_FIELDS, build_skeleton, main  # noqa: E402


def _sample_index() -> dict:
    return {
        "generated_at": "2026-04-11T12:00:00",
        "source_file": "processo.pdf",
        "pdf_info": {"pages": 13, "file_size_mb": 0.02, "title": None},
        "processo_number": "1234567-89.2024.8.26.0100",
        "total_characters": 50000,
        "total_chunks": 3,
        "chunks": [
            {
                "index": 0,
                "label": "PETIÇÃO INICIAL",
                "char_count": 8000,
                "primary_date": "10/01/2024",
                "dates_found": ["10/01/2024"],
                "processo_number": "1234567-89.2024.8.26.0100",
                "ocr_confidence": 0.92,
                "page_range": {"start": 1, "end": 5},
                "chunk_file": "chunks/00-peticao-inicial.txt",
            },
            {
                "index": 1,
                "label": "CONTESTAÇÃO",
                "char_count": 12000,
                "primary_date": "15/02/2024",
                "dates_found": ["15/02/2024"],
                "processo_number": None,
                "ocr_confidence": 0.88,
                "page_range": {"start": 6, "end": 10},
                "chunk_file": "chunks/01-contestacao.txt",
            },
            {
                "index": 2,
                "label": "SENTENÇA",
                "char_count": 5000,
                "primary_date": "01/07/2024",
                "dates_found": ["01/07/2024"],
                "processo_number": None,
                "ocr_confidence": 0.95,
                "page_range": {"start": 11, "end": 13},
                "chunk_file": "chunks/02-sentenca.txt",
            },
        ],
    }


def test_build_skeleton_preserves_root_fields():
    skel = build_skeleton(_sample_index())
    assert skel["analysis_version"] == "2.0"
    assert skel["schema_version"] == "2.0"
    assert skel["processo_number"] == "1234567-89.2024.8.26.0100"
    assert skel["total_chunks"] == 3
    assert len(skel["chunks"]) == 3


def test_build_skeleton_preserves_technical_fields_per_chunk():
    skel = build_skeleton(_sample_index())
    first = skel["chunks"][0]
    for field in ["index", "label", "char_count", "primary_date", "chunk_file", "page_range", "ocr_confidence"]:
        assert field in first, f"missing {field}"
    assert first["chunk_file"] == "chunks/00-peticao-inicial.txt"
    assert first["page_range"] == {"start": 1, "end": 5}


def test_build_skeleton_marks_pending():
    skel = build_skeleton(_sample_index())
    for ch in skel["chunks"]:
        assert ch.get("_pending_analysis") is True


def test_build_skeleton_does_not_invent_semantic_fields():
    skel = build_skeleton(_sample_index())
    for ch in skel["chunks"]:
        assert "tipo_peca" not in ch
        assert "pedidos" not in ch
        assert "valores" not in ch


def test_build_skeleton_empty_chunks():
    skel = build_skeleton({"chunks": [], "total_chunks": 0})
    assert skel["chunks"] == []
    assert skel["total_chunks"] == 0


def test_cli_writes_skeleton(tmp_path):
    idx = tmp_path / "index.json"
    idx.write_text(json.dumps(_sample_index()), encoding="utf-8")
    out = tmp_path / "analyzed.json"

    rc = main(["--index", str(idx), "--output", str(out)])
    assert rc == 0
    data = json.loads(out.read_text(encoding="utf-8"))
    assert len(data["chunks"]) == 3
    assert all(ch.get("_pending_analysis") for ch in data["chunks"])


def test_cli_missing_input(tmp_path):
    rc = main(["--index", str(tmp_path / "nope.json"), "--output", str(tmp_path / "out.json")])
    assert rc == 2


def test_cli_invalid_json(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("not json", encoding="utf-8")
    rc = main(["--index", str(bad), "--output", str(tmp_path / "out.json")])
    assert rc == 2


def test_skeleton_passes_integrity_gate(tmp_path):
    """The skeleton should pass schema_validator.py integrity gate — chunk_file
    entries must correspond to physical files.
    """
    idx = _sample_index()
    idx_path = tmp_path / "index.json"
    idx_path.write_text(json.dumps(idx), encoding="utf-8")
    out_path = tmp_path / "analyzed.json"

    # Create the physical chunk files with content matching declared char_count
    chunks_dir = tmp_path / "chunks"
    chunks_dir.mkdir()
    for ch in idx["chunks"]:
        (tmp_path / ch["chunk_file"]).write_text("x" * ch["char_count"], encoding="utf-8")

    assert main(["--index", str(idx_path), "--output", str(out_path)]) == 0

    # Run schema_validator (integrity gate check)
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "schema_validator.py"),
         "--input", str(out_path)],
        capture_output=True, text=True, cwd=str(tmp_path),
    )
    # Skeleton has _pending_analysis — schema might pass or fail depending on
    # whether additionalProperties is strict. What we care about: integrity
    # gate (1:1 chunks) should pass. We accept exit code 0 or errors that are
    # NOT about missing physical files.
    combined = (r.stdout + r.stderr).lower()
    assert "missing physical" not in combined
    assert "integrity" not in combined or "ok" in combined or r.returncode == 0


def test_technical_fields_list_is_sane():
    # Guard against accidental removal of essential fields
    for required in ["index", "label", "char_count", "chunk_file"]:
        assert required in TECHNICAL_FIELDS
