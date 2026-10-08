"""Tests for scripts/enrich_deterministic.py — Phase 2 Step 2.4."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from enrich_deterministic import (  # noqa: E402
    EnrichError,
    _enrich_one,
    enrich,
    make_dialectic_summary,
)


def test_enrich_primary_date_to_iso():
    piece = {
        "chunk_id": "c00",
        "index": 0,
        "tipo_peca": "ACÓRDÃO",
        "primary_date": "18 de março de 2025",
    }
    out = _enrich_one(piece)
    assert out["_enriched"]["primary_date_iso"] == "2025-03-18"
    assert out["_enriched"]["mismatches"] == []


def test_enrich_dates_found_list():
    piece = {
        "chunk_id": "c01",
        "index": 1,
        "tipo_peca": "SENTENÇA",
        "dates_found": ["05/03/2023", "15 de setembro de 2024"],
    }
    out = _enrich_one(piece)
    iso = out["_enriched"]["dates_found_iso"]
    assert "2023-03-05" in iso
    assert "2024-09-15" in iso


def test_enrich_monetary_values():
    piece = {
        "chunk_id": "c02",
        "index": 2,
        "tipo_peca": "SENTENÇA",
        "valores": {
            "causa": "R$ 107.000,00",
            "condenacao": "R$ 87.000,00",
            "outros": [
                {"descricao": "danos materiais", "valor": "R$ 27.000,00"},
                {"descricao": "danos morais", "valor": "R$ 60.000,00"},
            ],
        },
    }
    out = _enrich_one(piece)
    norm = out["_enriched"]["valores_normalized"]
    assert norm["causa"] == 107000.0
    assert norm["condenacao"] == 87000.0
    assert norm["outros"][0]["normalized"] == 27000.0
    assert norm["outros"][1]["normalized"] == 60000.0


def test_enrich_cnj_structural_parse():
    """CNJ must be parsed into sequential/year/court even when check digit fails."""
    piece = {
        "chunk_id": "c00",
        "index": 0,
        "tipo_peca": "PETIÇÃO INICIAL",
        "processo_number": "2000000-22.2023.8.26.0114",
    }
    out = _enrich_one(piece)
    info = out["_enriched"]["processo_number"]
    assert info["year"] == 2023
    assert info["court"] == "TJSP"
    # Synthetic number will fail check digit — we only require parsing worked.
    assert info["normalized"] == "2000000-22.2023.8.26.0114"


def test_enrich_records_mismatch_on_unparseable_date():
    piece = {
        "chunk_id": "c00",
        "index": 0,
        "tipo_peca": "SENTENÇA",
        "primary_date": "not a date",
    }
    out = _enrich_one(piece)
    assert out["_enriched"]["primary_date_iso"] is None
    mismatches = out["_enriched"]["mismatches"]
    assert any(m["field"] == "primary_date" for m in mismatches)


def test_enrich_records_mismatch_on_garbage_money():
    piece = {
        "chunk_id": "c00",
        "index": 0,
        "tipo_peca": "SENTENÇA",
        "valores": {"condenacao": "cem mil dólares canadenses"},
    }
    out = _enrich_one(piece)
    mismatches = out["_enriched"]["mismatches"]
    assert any(m["field"] == "valores.condenacao" for m in mismatches)


def test_enrich_aborts_when_mismatch_rate_too_high():
    """If >10% of monetary mentions fail normalization, enrich raises."""
    pieces = [
        {
            "chunk_id": "c00",
            "index": 0,
            "tipo_peca": "SENTENÇA",
            "valores": {
                "causa": "R$ 100,00",
                "condenacao": "trash",
                "honorarios": "garbage",
            },
        },
    ]
    with pytest.raises(EnrichError) as exc:
        enrich(pieces)
    assert "mismatch rate" in str(exc.value)


def test_enrich_under_threshold_still_succeeds():
    pieces = [
        {
            "chunk_id": f"c{i:02}",
            "index": i,
            "tipo_peca": "SENTENÇA",
            "valores": {"condenacao": f"R$ {i * 1000},00"},
        }
        for i in range(1, 11)  # 10 good mentions
    ]
    # Add one garbage
    pieces.append({
        "chunk_id": "c99",
        "index": 99,
        "tipo_peca": "SENTENÇA",
        "valores": {"condenacao": "junk"},
    })
    # 1/11 ≈ 9% ≤ threshold 10% — should pass
    out = enrich(pieces)
    assert len(out) == 11


def test_enrich_empty_input():
    assert enrich([]) == []


def test_enrich_preserves_other_fields():
    piece = {
        "chunk_id": "c00",
        "index": 0,
        "tipo_peca": "PETIÇÃO INICIAL",
        "primary_date": "10 de maio de 2024",
        "partes": {"autores": ["JOÃO"]},
        "pedidos": ["procedência"],
    }
    out = _enrich_one(piece)
    assert out["partes"] == {"autores": ["JOÃO"]}
    assert out["pedidos"] == ["procedência"]
    assert out["_enriched"]["primary_date_iso"] == "2024-05-10"


# ---------- Phase 7 Step 7.2: dialectic digest ----------

def test_dialectic_summary_drops_raw_text_fields():
    pieces = [{
        "chunk_id": "c00",
        "index": 0,
        "tipo_peca": "SENTENÇA",
        "fatos_relevantes": ["fato 1", "fato 2"],
        "raw_text": "x" * 10000,
        "full_text": "y" * 10000,
        "chunk_file": "chunks/02-sentenca.txt",
    }]
    digest = make_dialectic_summary(pieces)
    assert "raw_text" not in digest[0]
    assert "full_text" not in digest[0]
    assert "chunk_file" not in digest[0]
    assert digest[0]["fatos_relevantes"] == ["fato 1", "fato 2"]


def test_dialectic_summary_propagates_normalized_fields():
    pieces = [{
        "chunk_id": "c00",
        "index": 0,
        "tipo_peca": "SENTENÇA",
        "_enriched": {
            "primary_date_iso": "2024-09-15",
            "valores_normalized": {"condenacao": 87000.0},
            "processo_number": {"valid": False, "court": "TJSP"},
            "mismatches": [{"field": "x"}],
        },
    }]
    digest = make_dialectic_summary(pieces)
    enriched = digest[0]["_enriched"]
    assert enriched["primary_date_iso"] == "2024-09-15"
    assert enriched["valores_normalized"] == {"condenacao": 87000.0}
    assert enriched["processo_number"]["court"] == "TJSP"
    # mismatches must NOT propagate — they're noise for the dialectic layer
    assert "mismatches" not in enriched


def test_dialectic_summary_empty_input():
    assert make_dialectic_summary([]) == []


def test_dialectic_summary_never_mutates_input():
    pieces = [{"chunk_id": "c00", "index": 0, "tipo_peca": "SENTENÇA", "raw_text": "x"}]
    original = dict(pieces[0])
    make_dialectic_summary(pieces)
    assert pieces[0] == original  # untouched
