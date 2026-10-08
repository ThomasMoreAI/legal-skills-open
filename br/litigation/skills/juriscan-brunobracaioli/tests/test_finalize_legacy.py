"""Tests for scripts/finalize_legacy.py — Phase A.4.5."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from finalize_legacy import (  # noqa: E402
    _extract_condemnation_from_chunk,
    compute_recalculations,
    find_recalculation_candidates,
    main,
)


def _analyzed_with_sentenca_2023(value: str = "R$ 100.000,00") -> dict:
    return {
        "analysis_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "PETIÇÃO INICIAL",
                "primary_date": "10/01/2023",
            },
            {
                "index": 1,
                "tipo_peca": "SENTENÇA",
                "primary_date": "12/12/2023",
                "valores": {"condenacao": value},
                "decisao": "JULGO PROCEDENTE",
            },
        ],
    }


def _analyzed_with_sentenca_2025() -> dict:
    return {
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "SENTENÇA",
                "primary_date": "01/03/2025",
                "valores": {"condenacao": "R$ 500.000,00"},
            }
        ]
    }


def _analyzed_no_condemnation() -> dict:
    return {
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "SENTENÇA",
                "primary_date": "10/01/2024",
                "valores": {"causa": "R$ 100.000,00"},
                "decisao": "JULGO IMPROCEDENTE",
            }
        ]
    }


# ---------- extraction ----------

def test_extract_condemnation_valid():
    chunk = {
        "index": 0,
        "tipo_peca": "SENTENÇA",
        "primary_date": "10/05/2023",
        "valores": {"condenacao": "R$ 50.000,00"},
    }
    result = _extract_condemnation_from_chunk(chunk)
    assert result is not None
    raw, iso = result
    assert raw == "R$ 50.000,00"
    assert iso == "2023-05-10"


def test_extract_no_condemnation():
    chunk = {"tipo_peca": "SENTENÇA", "primary_date": "10/05/2023", "valores": {}}
    assert _extract_condemnation_from_chunk(chunk) is None


def test_extract_no_date():
    chunk = {
        "tipo_peca": "SENTENÇA",
        "valores": {"condenacao": "R$ 50.000,00"},
    }
    assert _extract_condemnation_from_chunk(chunk) is None


def test_extract_empty_condemnation():
    chunk = {
        "tipo_peca": "SENTENÇA",
        "primary_date": "10/05/2023",
        "valores": {"condenacao": ""},
    }
    assert _extract_condemnation_from_chunk(chunk) is None


# ---------- candidate discovery ----------

def test_find_candidates_includes_sentenca():
    candidates = find_recalculation_candidates(_analyzed_with_sentenca_2023())
    assert len(candidates) == 1
    assert candidates[0]["chunk_index"] == 1
    assert candidates[0]["tipo_peca"] == "SENTENÇA"


def test_find_candidates_skips_peticao_inicial():
    analyzed = {
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "PETIÇÃO INICIAL",
                "primary_date": "10/01/2023",
                "valores": {"condenacao": "R$ 100.000,00"},
            }
        ]
    }
    assert find_recalculation_candidates(analyzed) == []


def test_find_candidates_empty_analyzed():
    assert find_recalculation_candidates({"chunks": []}) == []


# ---------- compute_recalculations ----------

def test_recalc_crosses_cutover_produces_split():
    """SENTENÇA 2023 → data_fim 2026 must cross 2024-08-30 and produce split."""
    recalcs = compute_recalculations(
        _analyzed_with_sentenca_2023(), data_fim=date(2026, 1, 1)
    )
    assert len(recalcs) == 1
    r = recalcs[0]
    assert r["tipo"] == "JUROS_LEI_14905"
    assert len(r["periods"]) == 2
    # Period 1 is pre-cutover with concrete numbers
    p1 = r["periods"][0]
    assert p1["juros"] is not None
    assert "1%" in p1["taxa"]
    # Period 2 is post-cutover with null juros
    p2 = r["periods"][1]
    assert p2["juros"] is None
    assert "SELIC" in p2["taxa"]


def test_recalc_fully_after_cutover():
    """SENTENÇA 2025 → fully post-cutover."""
    recalcs = compute_recalculations(
        _analyzed_with_sentenca_2025(), data_fim=date(2026, 1, 1)
    )
    assert len(recalcs) == 1
    assert len(recalcs[0]["periods"]) == 1
    assert "SELIC" in recalcs[0]["periods"][0]["taxa"]


def test_recalc_skips_when_no_condemnation():
    recalcs = compute_recalculations(
        _analyzed_no_condemnation(), data_fim=date(2026, 1, 1)
    )
    assert recalcs == []


def test_recalc_preserves_chunk_reference():
    recalcs = compute_recalculations(
        _analyzed_with_sentenca_2023(), data_fim=date(2026, 1, 1)
    )
    assert recalcs[0]["chunk_index"] == 1
    assert recalcs[0]["tipo_peca_source"] == "SENTENÇA"
    assert recalcs[0]["base"] == "R$ 100.000,00"


# ---------- CLI ----------

def test_cli_inplace(tmp_path):
    path = tmp_path / "analyzed.json"
    path.write_text(
        json.dumps(_analyzed_with_sentenca_2023()), encoding="utf-8"
    )

    rc = main([
        "--input", str(path),
        "--inplace",
        "--data-fim", "2026-01-01",
    ])
    assert rc == 0

    data = json.loads(path.read_text(encoding="utf-8"))
    assert "monetary_recalculations" in data
    assert len(data["monetary_recalculations"]) == 1


def test_cli_output_separate(tmp_path):
    inp = tmp_path / "analyzed.json"
    inp.write_text(json.dumps(_analyzed_with_sentenca_2023()), encoding="utf-8")
    out = tmp_path / "final.json"

    rc = main([
        "--input", str(inp),
        "--output", str(out),
        "--data-fim", "2026-01-01",
    ])
    assert rc == 0
    assert out.exists()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert "monetary_recalculations" in data


def test_cli_no_condemnation_produces_no_recalc(tmp_path):
    inp = tmp_path / "analyzed.json"
    inp.write_text(json.dumps(_analyzed_no_condemnation()), encoding="utf-8")
    out = tmp_path / "final.json"

    rc = main(["--input", str(inp), "--output", str(out)])
    assert rc == 0
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data.get("monetary_recalculations") in (None, [])


def test_cli_missing_input(tmp_path):
    rc = main(["--input", str(tmp_path / "nope.json"), "--inplace"])
    assert rc == 2


def test_cli_invalid_date_format(tmp_path):
    inp = tmp_path / "analyzed.json"
    inp.write_text("{}", encoding="utf-8")
    rc = main([
        "--input", str(inp),
        "--inplace",
        "--data-fim", "bad-date",
    ])
    assert rc == 2
