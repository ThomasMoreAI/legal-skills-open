"""Tests for scripts/persist_chunks.py — Phase 2 Step 2.2."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from persist_chunks import PersistError, persist  # noqa: E402


SAMPLE_TEXT = (
    "PETIÇÃO INICIAL\n"
    "João da Silva propõe ação contra Empresa X.\n"
    "Dá-se à causa o valor de R$ 10.000,00.\n"
    "\f"
    "SENTENÇA\n"
    "JULGO PROCEDENTE o pedido e condeno a ré ao pagamento de R$ 10.000,00.\n"
)


def _write_raw(tmp: Path, text: str = SAMPLE_TEXT) -> Path:
    raw = tmp / "raw_text.txt"
    raw.write_text(text, encoding="utf-8")
    return raw


def _segmenter_output(raw_text: str, chunks: list[dict]) -> dict:
    return {
        "schema_version": "1.0",
        "raw_text_length": len(raw_text),
        "chunks": chunks,
    }


def _default_chunks(raw_text: str) -> list[dict]:
    boundary = raw_text.index("SENTENÇA")
    return [
        {
            "id": "c00",
            "start_char": 0,
            "end_char": boundary,
            "tipo_provavel": "PETIÇÃO INICIAL",
            "confianca": 0.95,
            "evidencia": "PETIÇÃO INICIAL",
        },
        {
            "id": "c01",
            "start_char": boundary,
            "end_char": len(raw_text),
            "tipo_provavel": "SENTENÇA",
            "confianca": 0.92,
            "evidencia": "SENTENÇA",
        },
    ]


def _write_seg(tmp: Path, doc: dict) -> Path:
    p = tmp / "segmenter.json"
    p.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    return p


# ---------- happy path ----------

def test_persist_happy_path(tmp_path):
    raw = _write_raw(tmp_path)
    seg = _write_seg(tmp_path, _segmenter_output(SAMPLE_TEXT, _default_chunks(SAMPLE_TEXT)))
    out = tmp_path / "output"
    index_path = persist(seg, raw, out)
    assert index_path == out / "index.json"
    idx = json.loads(index_path.read_text())
    assert idx["total_chunks"] == 2
    files = sorted((out / "chunks").iterdir())
    assert len(files) == 2
    assert files[0].name.startswith("00-peticao-inicial")
    assert files[1].name.startswith("01-sentenca")
    # Concatenation round-trip
    concatenated = "".join(f.read_text() for f in files)
    assert concatenated == SAMPLE_TEXT


def test_persist_removes_stale_chunks(tmp_path):
    """A previous run's orphan chunks must be removed, not left alongside."""
    raw = _write_raw(tmp_path)
    out = tmp_path / "output"
    (out / "chunks").mkdir(parents=True)
    (out / "chunks" / "99-ghost.txt").write_text("from previous run")

    seg = _write_seg(tmp_path, _segmenter_output(SAMPLE_TEXT, _default_chunks(SAMPLE_TEXT)))
    persist(seg, raw, out)
    files = {p.name for p in (out / "chunks").iterdir()}
    assert "99-ghost.txt" not in files


def test_persist_preserves_unicode(tmp_path):
    raw = _write_raw(tmp_path)
    seg = _write_seg(tmp_path, _segmenter_output(SAMPLE_TEXT, _default_chunks(SAMPLE_TEXT)))
    out = tmp_path / "output"
    persist(seg, raw, out)
    peticao = (out / "chunks" / "00-peticao-inicial.txt").read_text(encoding="utf-8")
    assert "PETIÇÃO" in peticao  # accents preserved


# ---------- failure modes ----------

def test_persist_rejects_gap(tmp_path):
    raw = _write_raw(tmp_path)
    boundary = SAMPLE_TEXT.index("SENTENÇA")
    chunks = [
        {"id": "c00", "start_char": 0, "end_char": boundary - 5,
         "tipo_provavel": "PETIÇÃO INICIAL", "confianca": 0.9},
        {"id": "c01", "start_char": boundary, "end_char": len(SAMPLE_TEXT),
         "tipo_provavel": "SENTENÇA", "confianca": 0.9},
    ]
    seg = _write_seg(tmp_path, _segmenter_output(SAMPLE_TEXT, chunks))
    with pytest.raises(PersistError) as exc:
        persist(seg, raw, tmp_path / "output")
    assert "gap/overlap" in str(exc.value)


def test_persist_rejects_overlap(tmp_path):
    raw = _write_raw(tmp_path)
    boundary = SAMPLE_TEXT.index("SENTENÇA")
    chunks = [
        {"id": "c00", "start_char": 0, "end_char": boundary + 5,
         "tipo_provavel": "PETIÇÃO INICIAL", "confianca": 0.9},
        {"id": "c01", "start_char": boundary, "end_char": len(SAMPLE_TEXT),
         "tipo_provavel": "SENTENÇA", "confianca": 0.9},
    ]
    seg = _write_seg(tmp_path, _segmenter_output(SAMPLE_TEXT, chunks))
    with pytest.raises(PersistError):
        persist(seg, raw, tmp_path / "output")


def test_persist_rejects_not_starting_at_zero(tmp_path):
    raw = _write_raw(tmp_path)
    chunks = [
        {"id": "c00", "start_char": 5, "end_char": len(SAMPLE_TEXT),
         "tipo_provavel": "DESCONHECIDO", "confianca": 0.4},
    ]
    seg = _write_seg(tmp_path, _segmenter_output(SAMPLE_TEXT, chunks))
    with pytest.raises(PersistError) as exc:
        persist(seg, raw, tmp_path / "output")
    assert "start at 0" in str(exc.value)


def test_persist_rejects_not_ending_at_end(tmp_path):
    raw = _write_raw(tmp_path)
    chunks = [
        {"id": "c00", "start_char": 0, "end_char": len(SAMPLE_TEXT) - 10,
         "tipo_provavel": "DESCONHECIDO", "confianca": 0.4},
    ]
    seg = _write_seg(tmp_path, _segmenter_output(SAMPLE_TEXT, chunks))
    with pytest.raises(PersistError):
        persist(seg, raw, tmp_path / "output")


def test_persist_rejects_stale_raw_len(tmp_path):
    raw = _write_raw(tmp_path)
    seg_doc = _segmenter_output(SAMPLE_TEXT, _default_chunks(SAMPLE_TEXT))
    seg_doc["raw_text_length"] = len(SAMPLE_TEXT) + 100
    seg = _write_seg(tmp_path, seg_doc)
    with pytest.raises(PersistError) as exc:
        persist(seg, raw, tmp_path / "output")
    assert "stale" in str(exc.value).lower() or "mismatch" in str(exc.value).lower()


def test_persist_rejects_invalid_schema(tmp_path):
    raw = _write_raw(tmp_path)
    # Missing required `id` field
    chunks = [
        {"start_char": 0, "end_char": len(SAMPLE_TEXT),
         "tipo_provavel": "SENTENÇA", "confianca": 0.8},
    ]
    seg = _write_seg(tmp_path, _segmenter_output(SAMPLE_TEXT, chunks))
    with pytest.raises(PersistError) as exc:
        persist(seg, raw, tmp_path / "output")
    assert "schema validation" in str(exc.value).lower()
