"""Tests for Phase 6 Step 6.3 — v3 views in scripts/obsidian_export.py.

Legacy v2 vault output is not tested here (pre-existing behavior). These
tests cover the three new views:
  _AUDITORIA.md, _VERIFICAÇÕES.md, _PERSPECTIVAS.md
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from obsidian_export import (  # noqa: E402
    export_vault,
    generate_auditoria_view,
    generate_perspectives_view,
    generate_verificacoes_view,
)


PROCESSO = "2000000-22.2023.8.26.0114"


def test_auditoria_view_empty_when_no_findings():
    assert generate_auditoria_view({}, PROCESSO) == ""


def test_auditoria_view_renders_art_942():
    analysis = {
        "auditor_findings": [
            {
                "tipo": "NULIDADE",
                "fundamento": "CPC art. 942",
                "impacto": "ALTO",
                "peca_ref": "c05",
                "descricao": "Apelação julgada por maioria (2×1) reformando sentença. Ampliação do colegiado omitida.",
                "acao_sugerida": "Arguir nulidade em recurso cabível.",
            },
            {
                "tipo": "OMISSAO",
                "fundamento": "CPC art. 1022",
                "impacto": "MÉDIO",
                "descricao": "Base de honorários não esclarecida",
                "acao_sugerida": "Embargos de declaração",
            },
        ]
    }
    md = generate_auditoria_view(analysis, PROCESSO)
    assert "Auditoria Processual" in md
    assert "CPC art. 942" in md
    assert "NULIDADE" in md
    assert "OMISSAO" in md
    # ALTO must appear before MÉDIO (sort by impact)
    assert md.index("NULIDADE") < md.index("OMISSAO")
    assert "[[_INDEX" in md


def test_verificacoes_view_empty_when_no_verifications():
    assert generate_verificacoes_view({}, PROCESSO) == ""


def test_verificacoes_view_renders_table_and_divergence():
    analysis = {
        "verifications": [
            {
                "tipo": "PRECEDENTE",
                "citacao_original": "REsp 1.234/SP",
                "status": "CONFIRMADO",
                "source_url": "https://stj.jus.br/x",
                "access_date": "2026-04-11",
                "trecho_oficial": "EMENTA: ...",
            },
            {
                "tipo": "SUMULA",
                "citacao_original": "Súmula 999 STJ",
                "status": "NAO_ENCONTRADO",
                "source_url": "https://scon.stj.jus.br/x",
                "access_date": "2026-04-11",
            },
            {
                "tipo": "PRECEDENTE",
                "citacao_original": "REsp 5.555/RJ",
                "status": "DIVERGENTE",
                "source_url": "https://stj.jus.br/y",
                "access_date": "2026-04-11",
                "trecho_oficial": "tese oposta",
                "divergencia": "o acórdão aplicou a tese invertida",
            },
        ],
        "verification_summary": {
            "total_verifications": 3,
            "confirmed": 1,
            "divergent": 1,
            "unverified": 1,
            "no_verification": 0,
        },
    }
    md = generate_verificacoes_view(analysis, PROCESSO)
    assert "| Status | Tipo | Citação" in md
    assert "CONFIRMADO" in md
    assert "NAO_ENCONTRADO" in md
    assert "Divergências" in md
    assert "o acórdão aplicou a tese invertida" in md
    assert "[link](https://stj.jus.br/x)" in md


def test_perspectives_view_empty_when_no_polos():
    assert generate_perspectives_view({}, PROCESSO) == ""


def test_perspectives_view_handles_one_polo_only():
    analysis = {
        "perspectives": {
            "autor": {
                "risk_level": "ALTO",
                "risk_score": 7.5,
                "forcas": [{"titulo": "F1", "descricao": "ok"}],
                "fraquezas": [],
                "recursos_cabiveis": [],
            },
            "reu": None,
        }
    }
    md = generate_perspectives_view(analysis, PROCESSO)
    assert "Autor" in md
    assert "ALTO" in md
    assert "7.5" in md
    assert "sem dados" in md  # reu section


def test_perspectives_view_both_polos():
    analysis = {
        "perspectives": {
            "autor": {"risk_level": "BAIXO", "risk_score": 2.0,
                       "forcas": [], "fraquezas": [], "recursos_cabiveis": []},
            "reu": {"risk_level": "MUITO_ALTO", "risk_score": 9.0,
                     "forcas": [], "fraquezas": [],
                     "recursos_cabiveis": [{"recurso": "Apelação",
                                              "cabimento": "cabível", "prazo_dias": 15}]},
        }
    }
    md = generate_perspectives_view(analysis, PROCESSO)
    assert "BAIXO" in md
    assert "MUITO_ALTO" in md
    assert "Apelação" in md


# ---------- integration: export_vault with v3 fields ----------

def test_export_vault_v3_emits_new_files(tmp_path):
    analysis = {
        "schema_version": "3.0",
        "processo_number": PROCESSO,
        "chunks": [
            {"index": 0, "label": "PETIÇÃO INICIAL", "char_count": 100,
             "dates_found": [], "artigos_lei": [], "jurisprudencia": []},
        ],
        "auditor_findings": [{
            "tipo": "NULIDADE",
            "fundamento": "CPC art. 942",
            "impacto": "ALTO",
            "descricao": "ampliação do colegiado por maioria",
            "acao_sugerida": "apontar em recurso",
        }],
        "verifications": [{
            "tipo": "PRECEDENTE",
            "citacao_original": "REsp 1.234/SP",
            "status": "CONFIRMADO",
            "source_url": "https://stj.jus.br/x",
            "access_date": "2026-04-11",
            "trecho_oficial": "ementa",
        }],
        "perspectives": {
            "autor": {"risk_level": "MÉDIO", "risk_score": 5.0,
                       "forcas": [], "fraquezas": [], "recursos_cabiveis": []},
            "reu": {"risk_level": "ALTO", "risk_score": 7.0,
                     "forcas": [], "fraquezas": [], "recursos_cabiveis": []},
        },
    }
    export_vault(analysis, str(tmp_path))
    files = {p.name for p in tmp_path.iterdir()}
    assert "_AUDITORIA.md" in files
    assert "_VERIFICAÇÕES.md" in files
    assert "_PERSPECTIVAS.md" in files
    # Legacy files still present
    assert "_INDEX.md" in files
    assert "_TIMELINE.md" in files


def test_export_vault_v2_compat_no_new_files(tmp_path):
    """Legacy v2 input must not produce v3 files (backwards compat)."""
    analysis = {
        "analysis_version": "2.0",
        "processo_number": PROCESSO,
        "chunks": [
            {"index": 0, "label": "PETIÇÃO INICIAL", "char_count": 100,
             "dates_found": [], "artigos_lei": [], "jurisprudencia": []},
        ],
    }
    export_vault(analysis, str(tmp_path))
    files = {p.name for p in tmp_path.iterdir()}
    assert "_AUDITORIA.md" not in files
    assert "_VERIFICAÇÕES.md" not in files
    assert "_PERSPECTIVAS.md" not in files
    assert "_INDEX.md" in files
