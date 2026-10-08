"""Tests for scripts/migrate_v2_to_v3.py and schema dispatcher — Phase 6.1+6.2."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from migrate_v2_to_v3 import migrate, V3_DEFAULTS  # noqa: E402
from schema_validator import (  # noqa: E402
    load_schema,
    pick_schema_for,
    validate_analysis,
)


def _v2_sample() -> dict:
    return {
        "analysis_version": "2.0",
        "processo_number": "1234567-89.2024.8.26.0100",
        "chunks": [
            {"index": 0, "label": "PETIÇÃO INICIAL", "char_count": 100},
            {"index": 1, "label": "SENTENÇA", "char_count": 200},
        ],
    }


# ---------- migrate() ----------

def test_migrate_adds_all_v3_defaults():
    v2 = _v2_sample()
    v3 = migrate(v2)
    for key in V3_DEFAULTS:
        assert key in v3


def test_migrate_sets_schema_version_3():
    v3 = migrate(_v2_sample())
    assert v3["schema_version"] == "3.0"
    assert v3["pipeline_mode"] == "legacy"
    assert v3["run_id"] is None


def test_migrate_does_not_overwrite_existing_fields():
    v2 = _v2_sample()
    v2["auditor_findings"] = [{"tipo": "NULIDADE", "fundamento": "x"}]
    v3 = migrate(v2)
    assert v3["auditor_findings"] == [{"tipo": "NULIDADE", "fundamento": "x"}]


def test_migrate_preserves_chunks_verbatim():
    v2 = _v2_sample()
    v3 = migrate(v2)
    assert v3["chunks"] == v2["chunks"]


def test_migrate_preserves_processo_number():
    v2 = _v2_sample()
    v3 = migrate(v2)
    assert v3["processo_number"] == v2["processo_number"]


def test_migrate_with_empty_input():
    v3 = migrate({})
    assert v3["schema_version"] == "3.0"
    assert v3["perspectives"] == {"autor": None, "reu": None}


# ---------- schema dispatch ----------

def test_pick_schema_for_v3():
    assert "v3" in pick_schema_for({"schema_version": "3.0"})


def test_pick_schema_for_v2_implicit():
    assert "v2" in pick_schema_for({"analysis_version": "2.0"})


def test_pick_schema_for_unknown_defaults_to_v2():
    assert "v2" in pick_schema_for({})


# ---------- validation round-trip ----------

def test_migrated_doc_validates_against_v3_schema():
    v2 = _v2_sample()
    v3 = migrate(v2)
    schema = load_schema(pick_schema_for(v3))
    valid, errors = validate_analysis(v3, schema)
    assert valid, errors


def test_v2_doc_does_not_claim_v3():
    v2 = _v2_sample()
    # v2 doc routed to v2 schema
    picked = pick_schema_for(v2)
    assert "v2" in picked


def test_full_v3_doc_with_agents_fields_validates():
    doc = migrate(_v2_sample())
    doc["pipeline_mode"] = "agents"
    doc["run_id"] = "abc-123"
    doc["process_state"] = "ativo"
    doc["perspectives"] = {
        "autor": {"risk_level": "MÉDIO", "risk_score": 5.0,
                   "forcas": [], "fraquezas": [], "recursos_cabiveis": []},
        "reu": {"risk_level": "ALTO", "risk_score": 7.0,
                 "forcas": [], "fraquezas": [], "recursos_cabiveis": []},
    }
    doc["auditor_findings"] = [{
        "tipo": "NULIDADE",
        "fundamento": "CPC art. 942",
        "impacto": "ALTO",
        "descricao": "ampliação do colegiado por maioria",
        "acao_sugerida": "apontar em RE/REsp",
    }]
    schema = load_schema(pick_schema_for(doc))
    valid, errors = validate_analysis(doc, schema)
    assert valid, errors


# ---------- CLI ----------

def test_cli_dry_run(tmp_path):
    src = tmp_path / "v2.json"
    src.write_text(json.dumps(_v2_sample()), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "migrate_v2_to_v3.py"),
         "--input", str(src), "--dry-run"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    out = json.loads(r.stdout)
    assert out["schema_version"] == "3.0"


def test_cli_writes_output_file(tmp_path):
    src = tmp_path / "v2.json"
    dst = tmp_path / "v3.json"
    src.write_text(json.dumps(_v2_sample()), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "migrate_v2_to_v3.py"),
         "--input", str(src), "--output", str(dst)],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    assert dst.exists()
    out = json.loads(dst.read_text())
    assert out["schema_version"] == "3.0"
