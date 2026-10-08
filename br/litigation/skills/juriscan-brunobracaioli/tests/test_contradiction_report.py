"""Tests for scripts/contradiction_report.py — Phase 1 Step 1.3.

Focus: hierarchy-aware detection. A legitimate appellate reform
(sentença → acórdão with reduced condenação) must NOT be flagged as a
VALOR_INCONSISTENTE contradiction.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

import warnings as _warnings

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "legacy"))

with _warnings.catch_warnings():
    _warnings.simplefilter("ignore", DeprecationWarning)
    from contradiction_report import (  # noqa: E402
        _is_legitimate_reform,
        find_value_inconsistencies,
        generate_report,
    )


def test_is_legitimate_reform_true_when_sentenca_and_acordao():
    assert _is_legitimate_reform(["SENTENÇA", "ACÓRDÃO"]) is True


def test_is_legitimate_reform_false_when_only_lower():
    assert _is_legitimate_reform(["SENTENÇA", "SENTENÇA"]) is False


def test_is_legitimate_reform_false_when_only_appellate():
    assert _is_legitimate_reform(["ACÓRDÃO", "ACÓRDÃO"]) is False


def test_is_legitimate_reform_handles_accent_variations():
    assert _is_legitimate_reform(["sentença", "ACORDAO"]) is True


def test_parcial_reform_not_flagged_as_contradiction():
    """Reference case from critical review (fixture 02).

    Sentença condena a R$ 87.000 — acórdão reduz para R$ 57.000.
    This is a legitimate appellate reform and must NOT produce a
    VALOR_INCONSISTENTE. It should produce an instance_tracking note.
    """
    chunks = [
        {
            "label": "SENTENÇA",
            "valores": {"condenacao": "R$ 87.000,00"},
        },
        {
            "label": "ACÓRDÃO",
            "valores": {"condenacao": "R$ 57.000,00"},
        },
    ]
    contradictions, notes = find_value_inconsistencies(chunks)
    assert not any(c["tipo"] == "VALOR_INCONSISTENTE" for c in contradictions), (
        "legitimate appellate reform must not be flagged as contradiction"
    )
    assert len(notes) == 1
    assert notes[0]["tipo"] == "REFORMA_PARCIAL"
    assert notes[0]["impacto"] == "INFO"
    assert "SENTENÇA" in notes[0]["pecas"]
    assert "ACÓRDÃO" in notes[0]["pecas"]


def test_two_sentencas_disagreeing_still_flagged():
    """Not every value divergence is a legitimate reform."""
    chunks = [
        {"label": "SENTENÇA", "valores": {"condenacao": "R$ 50.000,00"}},
        {"label": "SENTENÇA", "valores": {"condenacao": "R$ 70.000,00"}},
    ]
    contradictions, notes = find_value_inconsistencies(chunks)
    assert any(c["tipo"] == "VALOR_INCONSISTENTE" for c in contradictions)
    assert notes == []


def test_causa_values_still_compared():
    """valor_causa divergence is still a contradiction (no hierarchy semantics)."""
    chunks = [
        {"label": "PETIÇÃO INICIAL", "valores": {"causa": "R$ 100.000,00"}},
        {"label": "CONTESTAÇÃO", "valores": {"causa": "R$ 50.000,00"}},
    ]
    contradictions, _ = find_value_inconsistencies(chunks)
    assert any(c["tipo"] == "VALOR_INCONSISTENTE" for c in contradictions)


def test_generate_report_includes_instance_tracking():
    analysis = {
        "chunks": [
            {"label": "SENTENÇA", "valores": {"condenacao": "R$ 87.000,00"}},
            {"label": "ACÓRDÃO", "valores": {"condenacao": "R$ 57.000,00"}},
        ]
    }
    report = generate_report(analysis)
    assert "instance_tracking" in report
    assert len(report["instance_tracking"]) == 1
    assert report["by_type"].get("VALOR_INCONSISTENTE", 0) == 0
