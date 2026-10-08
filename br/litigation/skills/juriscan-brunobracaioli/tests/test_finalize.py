"""Tests for scripts/finalize.py — Phase 5 Step 5.3."""

from __future__ import annotations

import sys
from decimal import Decimal
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from finalize import (  # noqa: E402
    FinalizeError,
    apply_recalculations,
    recalcular_honorarios,
    recalcular_juros_lei_14905,
)


# ---------- Lei 14.905 ----------

def test_juros_fully_before_cutover():
    r = recalcular_juros_lei_14905(
        base_value="R$ 100.000,00",
        data_inicio="2023-01-01",
        data_fim="2024-01-01",
    )
    assert len(r["periods"]) == 1
    p = r["periods"][0]
    # 12 meses × 1% × 100k = 12k juros
    assert p["juros"] == "12000.00"
    assert p["valor_com_juros"] == "112000.00"
    assert "1%" in p["taxa"]


def test_juros_fully_after_cutover():
    r = recalcular_juros_lei_14905(
        base_value=50000,
        data_inicio="2024-09-01",
        data_fim="2025-03-01",
    )
    assert len(r["periods"]) == 1
    p = r["periods"][0]
    assert p["juros"] is None
    assert p["valor_com_juros"] is None
    assert "SELIC" in p["taxa"]


def test_juros_straddling_cutover_splits():
    r = recalcular_juros_lei_14905(
        base_value=100000,
        data_inicio="2024-02-29",
        data_fim="2025-02-28",
    )
    assert len(r["periods"]) == 2
    p1, p2 = r["periods"]
    assert p1["ate"] == "2024-08-30"
    assert p2["de"] == "2024-08-30"
    # Period 1 must be fully computed (1% a.m.)
    assert p1["juros"] is not None
    assert Decimal(p1["juros"]) > 0
    # Period 2 must be structurally present but not computed
    assert p2["juros"] is None
    assert "SELIC" in p2["taxa"]
    # Period 2 base must equal period 1 closing amount
    assert p2["base"] == p1["valor_com_juros"]


def test_juros_rejects_inverted_dates():
    with pytest.raises(FinalizeError):
        recalcular_juros_lei_14905(1000, "2025-01-01", "2024-01-01")


def test_juros_rejects_negative_base():
    with pytest.raises(FinalizeError):
        recalcular_juros_lei_14905(-100, "2023-01-01", "2024-01-01")


# ---------- honorários ----------

def test_honorarios_both_bases():
    r = recalcular_honorarios(
        percentual=15,
        base_original="R$ 87.000,00",
        base_reformada="R$ 57.000,00",
    )
    assert r["honorarios_sobre_base_original"] == "13050.00"
    assert r["honorarios_sobre_base_reformada"] == "8550.00"
    assert r["delta"] == "4500.00"
    assert "omiss" in r["note"].lower()


def test_honorarios_accepts_decimal_percentage():
    r = recalcular_honorarios(
        percentual=0.15,
        base_original=100000,
        base_reformada=60000,
    )
    assert r["honorarios_sobre_base_original"] == "15000.00"
    assert r["honorarios_sobre_base_reformada"] == "9000.00"


def test_honorarios_no_rounding_drift():
    """Decimal arithmetic must not introduce binary float errors."""
    r = recalcular_honorarios(
        percentual=10,
        base_original="R$ 1.234,56",
        base_reformada="R$ 1.234,56",
    )
    assert r["honorarios_sobre_base_original"] == "123.46"


# ---------- apply_recalculations integration ----------

def test_apply_recalculations_handles_multiple_findings():
    analysis = {
        "auditor_findings": [
            {
                "tipo": "NULIDADE",
                "fundamento": "CPC art. 942",
                "descricao": "...",
                "acao_sugerida": "...",
                "impacto": "ALTO",
            },
            {
                "tipo": "RECALCULO_NECESSARIO",
                "fundamento": "Lei 14.905/2024",
                "impacto": "MÉDIO",
                "descricao": "juros mistos",
                "acao_sugerida": "recalcular",
                "payload": {
                    "base": "R$ 87.000,00",
                    "data_inicio": "2024-05-01",
                    "data_fim": "2025-02-01",
                },
            },
            {
                "tipo": "RECALCULO_NECESSARIO",
                "fundamento": "Honorários pós-reforma (CPC art. 1022)",
                "impacto": "MÉDIO",
                "descricao": "base ambígua",
                "acao_sugerida": "embargos",
                "payload": {
                    "percentual": 15,
                    "base_original": 87000,
                    "base_reformada": 57000,
                },
            },
        ]
    }
    apply_recalculations(analysis)
    recalcs = analysis["monetary_recalculations"]
    assert len(recalcs) == 2
    assert recalcs[0]["tipo"] == "JUROS_LEI_14905"
    assert recalcs[1]["tipo"] == "HONORARIOS_APOS_REFORMA"


def test_apply_recalculations_empty_when_no_findings():
    analysis = {"auditor_findings": []}
    apply_recalculations(analysis)
    assert analysis["monetary_recalculations"] == []


def test_apply_recalculations_ignores_non_recalculo_findings():
    analysis = {
        "auditor_findings": [
            {"tipo": "NULIDADE", "fundamento": "x", "impacto": "ALTO",
             "descricao": "...", "acao_sugerida": "..."}
        ]
    }
    apply_recalculations(analysis)
    assert analysis["monetary_recalculations"] == []


def test_apply_recalculations_records_errors_inline():
    analysis = {
        "auditor_findings": [
            {
                "tipo": "RECALCULO_NECESSARIO",
                "fundamento": "Lei 14.905/2024",
                "impacto": "MÉDIO",
                "descricao": "...",
                "acao_sugerida": "...",
                "payload": {
                    "base": "R$ 100,00",
                    "data_inicio": "2025-01-01",
                    "data_fim": "2024-01-01",  # inverted
                },
            }
        ]
    }
    apply_recalculations(analysis)
    assert len(analysis["monetary_recalculations"]) == 1
    assert analysis["monetary_recalculations"][0]["tipo"] == "ERROR"
