"""Tests for scripts/confidence_rules.py — Phase 3 Step 3.4 + Phase 4 Step 4.3."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from confidence_rules import (  # noqa: E402
    ConfidenceRuleError,
    apply_downgrade,
    assert_preservation,
    run,
)


def _finding(tipo: str = "NULIDADE", fundamento: str = "CPC art. 942") -> dict:
    return {
        "tipo": tipo,
        "fundamento": fundamento,
        "impacto": "ALTO",
        "descricao": "x" * 30,
        "acao_sugerida": "y" * 20,
    }


# ---------- preservation invariant ----------

def test_preservation_holds_when_sizes_equal():
    auditor = {"auditor_findings": [_finding(), _finding()]}
    synth = {"auditor_findings": [_finding(), _finding()]}
    assert_preservation(synth, auditor)  # no raise


def test_preservation_holds_when_synthesizer_adds():
    auditor = {"auditor_findings": [_finding()]}
    synth = {"auditor_findings": [_finding(), _finding()]}  # added one
    assert_preservation(synth, auditor)


def test_preservation_raises_when_synthesizer_drops():
    auditor = {"auditor_findings": [_finding(), _finding(), _finding()]}
    synth = {"auditor_findings": [_finding()]}
    with pytest.raises(ConfidenceRuleError) as exc:
        assert_preservation(synth, auditor)
    assert "preservation" in str(exc.value).lower()
    assert "3" in str(exc.value)
    assert "1" in str(exc.value)


def test_preservation_handles_missing_auditor_findings():
    auditor = {}
    synth = {"auditor_findings": [_finding()]}
    assert_preservation(synth, auditor)  # no input = no constraint


# ---------- downgrade rules ----------

def _synthesis_with_arguments(citations: list[str]) -> dict:
    return {
        "perspectives": {
            "autor": {
                "forcas": [
                    {"titulo": "f", "descricao": "d", "peca_refs": ["c00"],
                     "citacao_juridica": c}
                    for c in citations
                ],
                "fraquezas": [],
                "recursos_cabiveis": [],
            },
            "reu": {"forcas": [], "fraquezas": [], "recursos_cabiveis": []},
        },
        "auditor_findings": [],
    }


def test_downgrade_confirmed_leaves_argument_clean():
    synth = _synthesis_with_arguments(["REsp 1.234/SP"])
    verifs = [{"citacao_original": "REsp 1.234/SP", "status": "CONFIRMADO"}]
    apply_downgrade(synth, verifs)
    arg = synth["perspectives"]["autor"]["forcas"][0]
    assert "confidence_flag" not in arg
    assert synth["verification_summary"]["confirmed"] == 1


def test_downgrade_divergent_marks_argument():
    synth = _synthesis_with_arguments(["REsp 1.234/SP"])
    verifs = [{
        "citacao_original": "REsp 1.234/SP",
        "status": "DIVERGENTE",
        "divergencia": "acórdão cita caso análogo mas a tese é oposta",
    }]
    apply_downgrade(synth, verifs)
    arg = synth["perspectives"]["autor"]["forcas"][0]
    assert arg["confidence_flag"] == "DIVERGENT"
    assert "divergencia" in arg
    assert synth["verification_summary"]["divergent"] == 1


def test_downgrade_not_found_marks_unverified():
    synth = _synthesis_with_arguments(["REsp 9.999.999/ZZ"])
    verifs = [{"citacao_original": "REsp 9.999.999/ZZ", "status": "NAO_ENCONTRADO"}]
    apply_downgrade(synth, verifs)
    arg = synth["perspectives"]["autor"]["forcas"][0]
    assert arg["confidence_flag"] == "UNVERIFIED"
    assert synth["verification_summary"]["unverified"] == 1


def test_downgrade_citation_without_verification():
    synth = _synthesis_with_arguments(["REsp 7.777/SP"])
    apply_downgrade(synth, [])
    # With empty verifications list, no verification summary entries
    assert synth["verification_summary"]["total_verifications"] == 0


def test_downgrade_citation_match_is_case_insensitive():
    synth = _synthesis_with_arguments(["  REsp 1.234/SP  "])
    verifs = [{"citacao_original": "resp 1.234/sp", "status": "CONFIRMADO"}]
    apply_downgrade(synth, verifs)
    assert synth["verification_summary"]["confirmed"] == 1


# ---------- run (full pipeline) ----------

def test_run_happy_path_with_phase3_only():
    auditor = {"auditor_findings": [_finding()]}
    synth = {
        "perspectives": {
            "autor": {"forcas": [], "fraquezas": [], "recursos_cabiveis": []},
            "reu": {"forcas": [], "fraquezas": [], "recursos_cabiveis": []},
        },
        "auditor_findings": [_finding()],
    }
    out = run(synth, auditor, verifications=None)
    assert out["verification_summary"]["total_verifications"] == 0


def test_run_aborts_on_preservation_violation():
    auditor = {"auditor_findings": [_finding(), _finding()]}
    synth = {"auditor_findings": []}
    with pytest.raises(ConfidenceRuleError):
        run(synth, auditor, verifications=None)
