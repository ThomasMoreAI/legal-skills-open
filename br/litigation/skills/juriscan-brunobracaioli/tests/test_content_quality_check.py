"""Tests for scripts/content_quality_check.py — Phase A.3."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from content_quality_check import (  # noqa: E402
    _is_populated,
    evaluate,
    main,
)


# ---------- _is_populated helper ----------

def test_is_populated_none():
    assert _is_populated(None) is False


def test_is_populated_empty_string():
    assert _is_populated("") is False


def test_is_populated_empty_list():
    assert _is_populated([]) is False


def test_is_populated_empty_dict():
    assert _is_populated({}) is False


def test_is_populated_string():
    assert _is_populated("hello") is True


def test_is_populated_list():
    assert _is_populated([1]) is True


def test_is_populated_dict():
    assert _is_populated({"a": 1}) is True


def test_is_populated_zero_int_is_populated():
    # Numeric zero is a real value, not "missing"
    assert _is_populated(0) is True


# ---------- evaluate() core ----------

def test_evaluate_zero_chunks():
    r = evaluate({"chunks": []})
    assert r["total_chunks"] == 0
    assert any("zero chunks" in w for w in r["warnings"])


def test_evaluate_all_empty_chunks_flags_every_global_field():
    analyzed = {"chunks": [{}, {}, {}, {}]}
    r = evaluate(analyzed)
    # Every global canonical field should fire a 0/N warning
    for field in ["tipo_peca", "partes", "pedidos", "valores", "fatos_relevantes"]:
        assert any(f"0/4 chunks têm campo {field!r}" in w for w in r["warnings"])


def test_evaluate_well_populated_chunks_no_global_warnings():
    analyzed = {
        "schema_version": "2.0",
        "chunks": [
            {
                "tipo_peca": "PETIÇÃO INICIAL",
                "partes": {"autor": "X", "reu": "Y"},
                "pedidos": ["p1"],
                "valores": {"causa": "1000"},
                "fatos_relevantes": ["f1"],
            },
            {
                "tipo_peca": "SENTENÇA",
                "partes": {"autor": "X", "reu": "Y"},
                "pedidos": [],  # not expected for sentence
                "valores": {"condenacao": "500"},
                "fatos_relevantes": ["f2"],
                "decisao": "JULGO PROCEDENTE",
            },
        ],
    }
    r = evaluate(analyzed)
    # No 0/N warnings for global fields
    for field in ["tipo_peca", "partes", "valores", "fatos_relevantes"]:
        assert not any(f"0/2 chunks têm campo {field!r}" in w for w in r["warnings"])


def test_evaluate_per_type_expected_field_violation():
    analyzed = {
        "chunks": [{
            "tipo_peca": "SENTENÇA",
            "partes": {"x": 1},
            "pedidos": ["x"],
            "valores": {"condenacao": "100"},
            "fatos_relevantes": ["x"],
            # decisao MISSING — expected field for SENTENÇA
        }],
    }
    r = evaluate(analyzed)
    assert any("SENTENÇA" in w and "'decisao'" in w for w in r["warnings"])


def test_evaluate_partial_population_under_half():
    # 4 chunks, only 1 has fatos_relevantes — flag the partial fill
    analyzed = {
        "chunks": [
            {"tipo_peca": "PETIÇÃO INICIAL", "fatos_relevantes": ["f1"],
             "partes": {}, "pedidos": [], "valores": {}},
            {"tipo_peca": "CONTESTAÇÃO"},
            {"tipo_peca": "RÉPLICA"},
            {"tipo_peca": "SENTENÇA"},
        ],
    }
    r = evaluate(analyzed)
    assert any("1/4" in w and "'fatos_relevantes'" in w for w in r["warnings"])


def test_evaluate_schema_version_warning():
    analyzed = {"chunks": [{"tipo_peca": "PETIÇÃO INICIAL", "fatos_relevantes": ["x"],
                            "partes": {"a": 1}, "pedidos": ["x"], "valores": {"causa": "1"}}]}
    r = evaluate(analyzed)
    assert any("schema_version" in w for w in r["warnings"])


def test_evaluate_with_schema_version_no_warning_about_version():
    analyzed = {
        "schema_version": "3.0",
        "chunks": [{"tipo_peca": "PETIÇÃO INICIAL", "fatos_relevantes": ["x"],
                    "partes": {"a": 1}, "pedidos": ["x"], "valores": {"causa": "1"}}],
    }
    r = evaluate(analyzed)
    assert not any("schema_version" in w for w in r["warnings"])


def test_evaluate_analysis_version_v2_legacy_no_warning():
    analyzed = {
        "analysis_version": "2.0",
        "chunks": [{"tipo_peca": "PETIÇÃO INICIAL", "fatos_relevantes": ["x"],
                    "partes": {"a": 1}, "pedidos": ["x"], "valores": {"causa": "1"}}],
    }
    r = evaluate(analyzed)
    assert not any("schema_version" in w for w in r["warnings"])


# ---------- CLI integration ----------

def test_cli_default_exit_zero_on_warnings(tmp_path):
    analyzed = tmp_path / "analyzed.json"
    analyzed.write_text(json.dumps({"chunks": [{}, {}]}), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "content_quality_check.py"),
         "--input", str(analyzed)],
        capture_output=True, text=True,
    )
    # Default: warnings do NOT fail the run
    assert r.returncode == 0
    assert "WARN" in r.stderr


def test_cli_strict_exit_one_on_warnings(tmp_path):
    analyzed = tmp_path / "analyzed.json"
    analyzed.write_text(json.dumps({"chunks": [{}, {}]}), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "content_quality_check.py"),
         "--input", str(analyzed), "--strict"],
        capture_output=True, text=True,
    )
    assert r.returncode == 1


def test_cli_json_output(tmp_path):
    analyzed = tmp_path / "analyzed.json"
    analyzed.write_text(json.dumps({"chunks": [{}, {}, {}]}), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "content_quality_check.py"),
         "--input", str(analyzed), "--json"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0
    data = json.loads(r.stdout)
    assert data["total_chunks"] == 3
    assert len(data["warnings"]) >= 5  # one per global canonical field


def test_cli_missing_file_exit_2(tmp_path):
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "content_quality_check.py"),
         "--input", str(tmp_path / "does_not_exist.json")],
        capture_output=True, text=True,
    )
    assert r.returncode == 2
    assert "not found" in r.stderr


def test_cli_invalid_json_exit_2(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("not json{{", encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "content_quality_check.py"),
         "--input", str(bad)],
        capture_output=True, text=True,
    )
    assert r.returncode == 2


# ---------- A.4.2: chunks_needing_retry per-chunk feedback ----------

def test_evaluate_returns_chunks_needing_retry_key():
    r = evaluate({"chunks": []})
    assert "chunks_needing_retry" in r


def test_chunks_needing_retry_lists_missing_fields_per_type():
    analyzed = {
        "schema_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "PETIÇÃO INICIAL",
                "chunk_file": "chunks/00-peticao.txt",
                # Missing: pedidos, fatos_relevantes, valores
                "partes": {"autor": ["X"]},
            },
            {
                "index": 1,
                "tipo_peca": "SENTENÇA",
                "chunk_file": "chunks/01-sentenca.txt",
                # Missing: decisao, valores
                "fatos_relevantes": ["fact"],
            },
        ],
    }
    r = evaluate(analyzed)
    retry = r["chunks_needing_retry"]
    assert len(retry) == 2

    by_idx = {entry["index"]: entry for entry in retry}
    assert 0 in by_idx
    assert 1 in by_idx

    p0 = by_idx[0]
    assert p0["tipo_peca"] == "PETIÇÃO INICIAL"
    assert p0["chunk_file"] == "chunks/00-peticao.txt"
    assert "pedidos" in p0["missing_fields"]
    assert "fatos_relevantes" in p0["missing_fields"]
    assert "valores" in p0["missing_fields"]

    p1 = by_idx[1]
    assert "decisao" in p1["missing_fields"]
    assert "valores" in p1["missing_fields"]


def test_chunks_needing_retry_flags_missing_tipo_peca():
    analyzed = {
        "schema_version": "2.0",
        "chunks": [{"index": 0, "chunk_file": "chunks/00.txt"}],
    }
    r = evaluate(analyzed)
    retry = r["chunks_needing_retry"]
    assert len(retry) == 1
    assert retry[0]["missing_fields"] == ["tipo_peca"]


def test_chunks_needing_retry_empty_when_all_complete():
    analyzed = {
        "schema_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "PETIÇÃO INICIAL",
                "chunk_file": "chunks/00.txt",
                "partes": {"autor": ["X"]},
                "pedidos": ["p"],
                "fatos_relevantes": ["f"],
                "valores": {"causa": "R$ 1.000,00"},
            },
            {
                "index": 1,
                "tipo_peca": "SENTENÇA",
                "chunk_file": "chunks/01.txt",
                "decisao": "JULGO PROCEDENTE",
                "valores": {"condenacao": "R$ 500,00"},
                "fatos_relevantes": ["f"],
            },
        ],
    }
    r = evaluate(analyzed)
    assert r["chunks_needing_retry"] == []


def test_cli_strict_fails_on_retry_needed(tmp_path):
    """--strict should fail when chunks_needing_retry is non-empty, even if
    there are no global warnings."""
    analyzed = tmp_path / "analyzed.json"
    analyzed.write_text(json.dumps({
        "schema_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "SENTENÇA",
                "chunk_file": "chunks/00.txt",
                # Missing decisao — triggers retry
            }
        ],
    }), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "content_quality_check.py"),
         "--input", str(analyzed), "--strict"],
        capture_output=True, text=True,
    )
    assert r.returncode == 1


def test_cli_per_chunk_retry_plan_prints_plan(tmp_path):
    analyzed = tmp_path / "analyzed.json"
    analyzed.write_text(json.dumps({
        "schema_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "PETIÇÃO INICIAL",
                "chunk_file": "chunks/00-peticao.txt",
            }
        ],
    }), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "content_quality_check.py"),
         "--input", str(analyzed), "--per-chunk-retry-plan"],
        capture_output=True, text=True,
    )
    assert "PETIÇÃO INICIAL" in r.stdout
    assert "chunks/00-peticao.txt" in r.stdout
    assert "faltam:" in r.stdout


def test_art_942_grounding_required_for_maioria_reform():
    """ACÓRDÃO by maioria reforming merit must have citation_spans grounding
    the art. 942 finding with verbatim tokens."""
    analyzed = {
        "schema_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "ACÓRDÃO",
                "chunk_file": "chunks/00-acordao.txt",
                "decisao": "DERAM PARCIAL PROVIMENTO",
                "valores": {"condenacao": "R$ 100.000,00"},
                "fatos_relevantes": ["f"],
                "acordao_structure": {
                    "votacao": "MAIORIA",
                    "resultado": "PARCIALMENTE_PROVIDO",
                },
                # Missing citation_spans with the verbatim tokens
                "citation_spans": [],
            }
        ],
    }
    r = evaluate(analyzed)
    assert any("942" in w for w in r["warnings"])
    assert any(
        "citation_spans" in ", ".join(e.get("missing_fields", []))
        for e in r["chunks_needing_retry"]
    )


def test_art_942_grounding_satisfied_with_verbatim_token():
    analyzed = {
        "schema_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "ACÓRDÃO",
                "chunk_file": "chunks/00.txt",
                "decisao": "DERAM PARCIAL PROVIMENTO",
                "valores": {"condenacao": "R$ 100.000,00"},
                "fatos_relevantes": ["f"],
                "acordao_structure": {
                    "votacao": "MAIORIA",
                    "resultado": "PARCIALMENTE_PROVIDO",
                },
                "citation_spans": [
                    {
                        "assertion": "reforma por maioria",
                        "source_text": "Por maioria de votos, vencido o Des. X, deram parcial provimento",
                    }
                ],
            }
        ],
    }
    r = evaluate(analyzed)
    assert not any("942" in w for w in r["warnings"])


def test_art_942_grounding_not_required_when_unanime():
    analyzed = {
        "schema_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "ACÓRDÃO",
                "chunk_file": "chunks/00.txt",
                "decisao": "DERAM PROVIMENTO",
                "valores": {"condenacao": "R$ 100.000,00"},
                "fatos_relevantes": ["f"],
                "acordao_structure": {
                    "votacao": "UNÂNIME",
                    "resultado": "PROVIDO",
                },
                "citation_spans": [],
            }
        ],
    }
    r = evaluate(analyzed)
    assert not any("942" in w for w in r["warnings"])


def test_art_942_grounding_not_required_when_not_reform():
    analyzed = {
        "schema_version": "2.0",
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "ACÓRDÃO",
                "chunk_file": "chunks/00.txt",
                "decisao": "NEGARAM PROVIMENTO",
                "valores": {"condenacao": "R$ 100.000,00"},
                "fatos_relevantes": ["f"],
                "acordao_structure": {
                    "votacao": "MAIORIA",
                    "resultado": "DESPROVIDO",
                },
                "citation_spans": [],
            }
        ],
    }
    r = evaluate(analyzed)
    assert not any("942" in w for w in r["warnings"])


def test_cli_json_output_includes_chunks_needing_retry(tmp_path):
    analyzed = tmp_path / "analyzed.json"
    analyzed.write_text(json.dumps({
        "chunks": [{"index": 0, "tipo_peca": "SENTENÇA"}],
    }), encoding="utf-8")
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "content_quality_check.py"),
         "--input", str(analyzed), "--json"],
        capture_output=True, text=True,
    )
    data = json.loads(r.stdout)
    assert "chunks_needing_retry" in data
    assert len(data["chunks_needing_retry"]) == 1
