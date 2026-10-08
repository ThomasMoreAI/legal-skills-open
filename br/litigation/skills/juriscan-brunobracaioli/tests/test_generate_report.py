"""Tests for scripts/generate_report.py — Phase A.4.3."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from generate_report import (  # noqa: E402
    _blockquote,
    _escape_md,
    _escape_table_cell,
    _factor_to_text,
    _find_valor_causa,
    _truncate_words,
    build_report,
    main,
    render_alerts,
    render_contradictions,
    render_executive_summary,
    render_header,
    render_pieces_table,
    render_prazos_table,
    render_recommendations,
    render_risk_assessment,
    render_timeline,
)


# ---------- helpers ----------

def _sample_analyzed() -> dict:
    return {
        "analysis_version": "2.0",
        "schema_version": "2.0",
        "processo_number": "1234567-89.2024.8.26.0100",
        "processo_metadata": {
            "vara": "25ª Vara Cível — Foro Central SP",
            "fase_atual": "recursal",
            "instancia_atual": "tj",
        },
        "chunks": [
            {
                "index": 0,
                "tipo_peca": "PETIÇÃO INICIAL",
                "primary_date": "10/01/2024",
                "instancia": "1a_instancia",
                "partes": {
                    "autor": ["Marcos Antonio"],
                    "reu": ["Tech Solutions Ltda"],
                    "vara": "25ª Vara Cível",
                },
                "pedidos": ["Condenação em R$ 485.000,00"],
                "valores": {"causa": "R$ 485.000,00"},
                "fatos_relevantes": ["Contrato de desenvolvimento inadimplido"],
                "resumo": "Ação de indenização por inadimplemento",
            },
            {
                "index": 1,
                "tipo_peca": "CONTESTAÇÃO",
                "primary_date": "15/02/2024",
                "instancia": "1a_instancia",
                "argumentos_chave": ["Ausência de nexo causal"],
                "fatos_relevantes": ["Software entregue no prazo contratual"],
            },
            {
                "index": 2,
                "tipo_peca": "SENTENÇA",
                "primary_date": "12/12/2024",
                "instancia": "1a_instancia",
                "decisao": "JULGO PARCIALMENTE PROCEDENTE — condeno a ré ao pagamento",
                "valores": {"condenacao": "R$ 473.300,00"},
                "fatos_relevantes": ["Perícia confirmou 47 bugs críticos"],
            },
            {
                "index": 3,
                "tipo_peca": "ACÓRDÃO",
                "primary_date": "18/03/2025",
                "instancia": "tj",
                "decisao": "DERAM PARCIAL PROVIMENTO à apelação",
                "valores": {"condenacao": "R$ 453.300,00"},
                "acordao_structure": {
                    "votacao": "MAIORIA",
                    "resultado": "PARCIALMENTE_PROVIDO",
                    "ementa": "Responsabilidade contratual. Inadimplemento comprovado.",
                    "votos_divergentes": ["Des. Henrique Almeida Neto — improvimento total"],
                },
                "citation_spans": [
                    {
                        "assertion": "reforma por maioria",
                        "source_text": "Por maioria de votos, vencido o Des. Henrique, deram parcial provimento",
                    }
                ],
            },
        ],
    }


def _sample_contradictions() -> dict:
    return {
        "contradictions": [
            {
                "tipo": "VALOR_INCONSISTENTE",
                "impacto": "ALTO",
                "descricao": "Divergência no valor do contrato",
                "evidence": [
                    {"chunk_ref": 0, "quote": "valor total do contrato: R$ 485.000,00"},
                    {"chunk_ref": 1, "quote": "o valor correto é R$ 450.000,00 — aditivo inexistente"},
                ],
                "resolucao": "Perícia contábil confirmou R$ 485.000,00",
            },
            {
                "tipo": "FATO_DIVERGENTE",
                "impacto": "MÉDIO",
                "descricao": "Data de entrega divergente",
            },
            {
                "tipo": "DATA_CONFLITANTE",
                "impacto": "BAIXO",
                "descricao": "Diferença de 10 dias na data de protocolo",
            },
        ]
    }


def _sample_risk() -> dict:
    return {
        "risk_level": "BAIXO",
        "overall_score": 2.2,
        "procedural_risk": {
            "score": 3,
            "factors": ["Acórdão por maioria — art. 942 arguível"],
        },
        "merit_indicators": {
            "score": 2,
            "favorable_factors": ["Perícia confirmou alegações"],
            "unfavorable_factors": ["Cláusula de limitação de responsabilidade"],
        },
        "monetary_exposure": {
            "likely_range": {"min": 400000, "likely": 453300, "max": 473300},
        },
    }


def _sample_prazos() -> dict:
    return {
        "prazos": [
            {
                "tipo": "recurso_especial",
                "fundamento_legal": "CPC art. 1.029",
                "data_intimacao": "18/03/2025",
                "data_limite": "08/04/2025",
                "status": "em_prazo",
                "dias_restantes": 7,
            }
        ]
    }


def _sample_recommendations() -> dict:
    return {
        "recommendations": [
            {
                "polo": "autor",
                "priority": "ALTA",
                "action": "Opor embargos de declaração arguindo art. 942 CPC",
                "fundamentacao": "Acórdão proferido por maioria reformando mérito — falta técnica de ampliação obrigatória",
                "evidence_quote": "Por maioria de votos, vencido o Des. Henrique, deram parcial provimento",
                "evidence_chunk_ref": 3,
                "deadline_days": 5,
                "deadline_basis": "CPC art. 1.023",
                "impact": "Eventual anulação e sessão colegiada ampliada",
            },
            {
                "polo": "reu",
                "priority": "MÉDIA",
                "action": "Apresentar contrarrazões a eventual REsp",
                "fundamentacao": "Proteger posição já favorável obtida no acórdão",
                "evidence_quote": "deram parcial provimento à apelação",
                "evidence_chunk_ref": 3,
                "deadline_days": 15,
                "deadline_basis": "CPC art. 1.030",
                "impact": "Manutenção do resultado atual",
            },
        ]
    }


# ---------- helper tests ----------

def test_escape_md_none():
    assert _escape_md(None) == ""


def test_escape_md_strips():
    assert _escape_md("  hello\nworld  ") == "hello world"


def test_escape_table_cell_escapes_pipe():
    assert "\\|" in _escape_table_cell("a|b")


def test_escape_table_cell_truncates():
    long = "x" * 300
    assert len(_escape_table_cell(long)) <= 200


# ---------- v3.1.2 helper tests ----------

def test_truncate_words_short_text_unchanged():
    assert _truncate_words("hello", 100) == "hello"


def test_truncate_words_cuts_at_word_boundary():
    text = "O acórdão foi proferido por maioria, vencido o Des. Henrique Almeida Neto"
    result = _truncate_words(text, 50)
    assert len(result) <= 52  # +ellipsis
    # MUST NOT end mid-word like "Almeida Ne"
    assert result.endswith("…")
    # Strip the ellipsis and check no half-word
    stripped = result.rstrip("…").rstrip()
    assert not stripped.endswith("Ne")
    assert not stripped.endswith("Henr")


def test_truncate_words_none_returns_empty():
    assert _truncate_words(None, 100) == ""


def test_truncate_words_strips_trailing_period_always():
    """v3.1.3: trailing punctuation is always stripped so callers can append '.'."""
    assert _truncate_words("Curto.", 100) == "Curto"


def test_truncate_words_strips_trailing_punctuation_before_ellipsis():
    text = "Primeira cláusula, segunda cláusula, terceira cláusula continua aqui"
    result = _truncate_words(text, 30)
    assert result.endswith("…")
    # No double punctuation
    assert ",…" not in result
    assert ".…" not in result


def test_factor_to_text_string_passthrough():
    assert _factor_to_text("ação direta") == "ação direta"


def test_factor_to_text_dict_with_fator_key():
    factor = {"fator": "Laudo pericial presente", "fundamentacao": "Prova técnica"}
    assert _factor_to_text(factor) == "Laudo pericial presente"


def test_factor_to_text_dict_with_descricao():
    assert _factor_to_text({"descricao": "algo"}) == "algo"


def test_factor_to_text_dict_fallback_keys():
    assert _factor_to_text({"factor": "X"}) == "X"
    assert _factor_to_text({"text": "Y"}) == "Y"
    assert _factor_to_text({"label": "Z"}) == "Z"


def test_factor_to_text_empty_dict():
    assert _factor_to_text({}) == ""


def test_factor_to_text_none():
    assert _factor_to_text(None) == ""


def test_find_valor_causa_direct():
    chunks = [{"valores": {"causa": "R$ 100.000,00"}}]
    assert _find_valor_causa(chunks) == "R$ 100.000,00"


def test_find_valor_causa_from_outros():
    chunks = [{
        "valores": {
            "outros": [
                {"descricao": "Valor do contrato original", "valor": "R$ 485.000,00"},
                {"descricao": "Lucros cessantes", "valor": "R$ 100.000,00"},
            ]
        }
    }]
    assert _find_valor_causa(chunks) == "R$ 485.000,00"


def test_find_valor_causa_fallback_to_condenacao():
    chunks = [{"valores": {"condenacao": "R$ 50.000,00"}}]
    assert _find_valor_causa(chunks) == "R$ 50.000,00"


def test_find_valor_causa_returns_none_when_nothing():
    assert _find_valor_causa([{"tipo_peca": "DESPACHO"}]) is None
    assert _find_valor_causa([]) is None


def test_render_risk_factors_as_dict():
    """v3.1.2 bug fix: factors emitted as dicts by risk_scorer should render
    as clean text, not raw dict dump."""
    risk = {
        "risk_level": "BAIXO",
        "overall_score": 2.0,
        "procedural_risk": {
            "score": 3,
            "factors": [
                {"fator": "Acórdão por maioria — art. 942 arguível", "fundamentacao": "Raciocínio"},
            ],
        },
        "merit_indicators": {
            "score": 2,
            "favorable_factors": [
                {"fator": "Laudo pericial presente", "fundamentacao": "Prova técnica"},
            ],
            "unfavorable_factors": [],
        },
        "monetary_exposure": {},
    }
    out = render_risk_assessment(risk)
    # Clean text, no raw dict repr
    assert "{'fator'" not in out
    assert "Acórdão por maioria" in out
    assert "Laudo pericial presente" in out


def test_render_header_finds_valor_from_outros():
    analyzed = {
        "processo_number": "X",
        "chunks": [
            {
                "tipo_peca": "LAUDO PERICIAL",
                "valores": {
                    "outros": [
                        {"descricao": "Valor do contrato original (doc. 01)", "valor": "R$ 485.000,00"},
                    ]
                },
            }
        ],
    }
    header = render_header(analyzed, None)
    assert "R$ 485.000,00" in header


def test_render_executive_summary_truncates_at_word_boundary():
    """Regression: the resumo executivo used to cut strings mid-word."""
    long_decision = (
        "JULGA PARCIALMENTE PROCEDENTE o pedido, condenando a Ré ao pagamento de: "
        "(a) R$ 48.500,00 de multa contratual (cláusula 8.2, limitada a 10%); "
        "(b) R$ 127.500,00 de danos materiais; (c) R$ 247.300,00 de lucros cessantes; "
        "(d) R$ 50.000,00 de danos morais. Total: R$ 473.300,00."
    )
    analyzed = {
        "chunks": [
            {"tipo_peca": "SENTENÇA", "decisao": long_decision},
        ]
    }
    summary = render_executive_summary(analyzed, None, None)
    # Must not contain a broken word like "de. Em" or "R$ 247.300,00 de."
    # Any truncation ends with ellipsis, not dangling word fragments
    assert "de. Em" not in summary
    assert "…" in summary or len(long_decision) < 220


def test_blockquote_multiline():
    result = _blockquote("line1\nline2\n\nline4")
    assert result.startswith("> line1")
    assert "> line2" in result
    assert "> line4" in result


# ---------- section renderers ----------

def test_render_header_basic():
    header = render_header(_sample_analyzed(), _sample_risk())
    assert "Processo nº 1234567-89.2024.8.26.0100" in header
    assert "Marcos Antonio" in header
    assert "Tech Solutions" in header
    assert "BAIXO" in header


def test_render_header_no_risk():
    header = render_header(_sample_analyzed(), None)
    assert "Processo nº" in header
    assert "Risco:" not in header


def test_render_header_missing_parties():
    analyzed = {"processo_number": "X", "chunks": [{"index": 0}]}
    header = render_header(analyzed, None)
    assert "não identificado" in header


def test_render_executive_summary_mentions_count():
    summary = render_executive_summary(_sample_analyzed(), _sample_contradictions(), _sample_risk())
    assert "4 peça" in summary
    assert "3 contradição" in summary or "3 contradições" in summary
    assert "BAIXO" in summary


def test_render_alerts_detects_art_942():
    alerts = render_alerts(_sample_analyzed(), None, None)
    assert "942" in alerts
    assert "maioria" in alerts.lower()
    assert "ALERTA CRÍTICO" in alerts


def test_render_alerts_empty_when_no_triggers():
    clean = {"chunks": [{"index": 0, "tipo_peca": "PETIÇÃO INICIAL"}]}
    alerts = render_alerts(clean, None, None)
    assert alerts == ""


def test_render_alerts_includes_urgent_prazo():
    prazos = {"prazos": [{
        "tipo": "apelação",
        "data_limite": "15/04/2025",
        "fundamento_legal": "CPC art. 1.003",
        "status": "ultimo_dia",
        "dias_restantes": 1,
    }]}
    alerts = render_alerts({"chunks": []}, prazos, None)
    assert "URGENTE" in alerts
    assert "apelação" in alerts


def test_render_pieces_table_sorts_chronologically():
    """v3.1.1 fix: pieces table must be sorted by primary_date ascending,
    regardless of their order in analyzed.chunks[]."""
    # Intentionally out of chronological order
    analyzed = {
        "chunks": [
            {"index": 0, "tipo_peca": "ACÓRDÃO", "primary_date": "18/03/2025"},
            {"index": 1, "tipo_peca": "PETIÇÃO INICIAL", "primary_date": "10/01/2024"},
            {"index": 2, "tipo_peca": "SENTENÇA", "primary_date": "12/12/2024"},
        ]
    }
    table = render_pieces_table(analyzed)
    # PETIÇÃO must appear before SENTENÇA which must appear before ACÓRDÃO
    assert table.index("PETIÇÃO INICIAL") < table.index("SENTENÇA") < table.index("ACÓRDÃO")


def test_render_pieces_table_missing_date_sorts_last():
    analyzed = {
        "chunks": [
            {"index": 0, "tipo_peca": "DOC_SEM_DATA", "primary_date": None},
            {"index": 1, "tipo_peca": "PETIÇÃO INICIAL", "primary_date": "10/01/2024"},
            {"index": 2, "tipo_peca": "SENTENÇA", "primary_date": "12/12/2024"},
        ]
    }
    table = render_pieces_table(analyzed)
    # Entries with dates come first, then the undated one at the end
    assert table.index("PETIÇÃO INICIAL") < table.index("DOC_SEM_DATA")
    assert table.index("SENTENÇA") < table.index("DOC_SEM_DATA")


def test_render_timeline_sorts_chronologically():
    """v3.1.1 fix: timeline mermaid must list pieces in chronological order."""
    analyzed = {
        "chunks": [
            {"index": 0, "tipo_peca": "ACÓRDÃO", "primary_date": "18/03/2025"},
            {"index": 1, "tipo_peca": "PETIÇÃO INICIAL", "primary_date": "10/01/2024"},
            {"index": 2, "tipo_peca": "SENTENÇA", "primary_date": "12/12/2024"},
        ]
    }
    timeline = render_timeline(analyzed)
    assert "2024-01-10" in timeline
    assert "2025-03-18" in timeline
    # Order in the gantt block
    assert timeline.index("2024-01-10") < timeline.index("2024-12-12") < timeline.index("2025-03-18")


def test_render_pieces_table_has_all_rows():
    table = render_pieces_table(_sample_analyzed())
    assert "PETIÇÃO INICIAL" in table
    assert "CONTESTAÇÃO" in table
    assert "SENTENÇA" in table
    assert "ACÓRDÃO" in table
    # Header + separator + 4 data rows
    assert table.count("|") >= 5 * 6


def test_render_pieces_table_empty():
    assert render_pieces_table({"chunks": []}) == ""


def test_render_contradictions_groups_by_impact():
    out = render_contradictions(_sample_contradictions())
    assert "Alto" in out
    assert "Médio" in out
    assert "Baixo" in out
    # Verbatim quote rendered
    assert "485.000,00" in out


def test_render_contradictions_no_data():
    assert render_contradictions(None) == ""


def test_render_contradictions_empty_list():
    out = render_contradictions({"contradictions": []})
    assert "Nenhuma contradição" in out


def test_render_risk_assessment():
    out = render_risk_assessment(_sample_risk())
    assert "BAIXO" in out
    assert "2.2" in out
    assert "Processual" in out
    assert "Mérito" in out
    assert "Monetário" in out


def test_render_risk_assessment_none():
    assert render_risk_assessment(None) == ""


def test_infer_current_instance_picks_latest_chronological():
    """v3.1.4: header instance reflects the most recent piece's instancia."""
    from scripts.generate_report import _infer_current_instance
    chunks = [
        {"primary_date": "20/07/2024", "instancia": "1a_instancia"},
        {"primary_date": "12/12/2024", "instancia": "1a_instancia"},
        {"primary_date": "18/03/2025", "instancia": "tj"},
    ]
    assert _infer_current_instance(chunks) == "2ª instância (TJ)"


def test_infer_current_instance_empty_chunks():
    from scripts.generate_report import _infer_current_instance
    assert _infer_current_instance([]) is None


def test_render_header_uses_inferred_instance():
    """v3.1.4: regression for the smoke test showing '(não identificada)'."""
    analyzed = {
        "processo_number": "1034567-89.2024.8.26.0100",
        "chunks": [
            {"primary_date": "12/12/2024", "instancia": "1a_instancia", "tipo_peca": "SENTENÇA"},
            {"primary_date": "18/03/2025", "instancia": "tj", "tipo_peca": "ACÓRDÃO"},
        ],
    }
    out = render_header(analyzed, None)
    assert "2ª instância (TJ)" in out
    assert "(não identificada)" not in out


def test_render_risk_assessment_empty_factors_shows_dash():
    """v3.1.3: empty factor lists render as '—' instead of blank cell."""
    risk = {
        "risk_level": "MÉDIO",
        "overall_score": 5.0,
        "procedural_risk": {"score": 5, "factors": []},
        "merit_indicators": {"score": 5, "favorable_factors": [], "unfavorable_factors": []},
        "monetary_exposure": {},
    }
    out = render_risk_assessment(risk)
    assert "| Processual | 5/10 | — |" in out
    assert "| Mérito | 5/10 | — |" in out


def test_truncate_words_strips_trailing_period_short_text():
    """v3.1.3: short text ending in '.' no longer produces double period."""
    from scripts.generate_report import _truncate_words
    assert _truncate_words("integral.", 220) == "integral"
    assert _truncate_words("short text.", 220) == "short text"
    assert _truncate_words("with comma,", 220) == "with comma"


def test_render_executive_summary_no_double_period():
    """v3.1.3: regression for 'integral..' double-period bug."""
    analyzed = {
        "chunks": [
            {"tipo_peca": "SENTENÇA", "decisao": "Procedente integral."},
        ]
    }
    summary = render_executive_summary(analyzed, None, None)
    assert ".." not in summary
    assert "integral*." in summary


def test_render_recommendations_both_polos():
    out = render_recommendations(_sample_recommendations())
    assert "Polo Ativo" in out
    assert "Polo Passivo" in out
    assert "942" in out
    # Both recommendations should be present
    assert "embargos de declaração" in out
    assert "contrarrazões" in out
    # Evidence quote should be rendered as blockquote
    assert "vencido o Des. Henrique" in out


def test_render_recommendations_sorted_by_priority():
    recs = {"recommendations": [
        {"polo": "autor", "priority": "BAIXA", "action": "B"},
        {"polo": "autor", "priority": "ALTA", "action": "A"},
        {"polo": "autor", "priority": "MÉDIA", "action": "M"},
    ]}
    out = render_recommendations(recs)
    # ALTA should come before MÉDIA should come before BAIXA
    assert out.index("[ALTA]") < out.index("[MÉDIA]") < out.index("[BAIXA]")


def test_render_recommendations_none():
    assert render_recommendations(None) == ""


def test_render_timeline_mermaid():
    out = render_timeline(_sample_analyzed())
    assert "```mermaid" in out
    assert "gantt" in out
    assert "2024-01-10" in out
    assert "2025-03-18" in out


def test_render_timeline_too_few_pieces():
    single = {"chunks": [{"index": 0, "primary_date": "10/01/2024", "tipo_peca": "PETIÇÃO INICIAL"}]}
    assert render_timeline(single) == ""


def test_render_prazos_table():
    out = render_prazos_table(_sample_prazos())
    assert "recurso_especial" in out
    assert "18/03/2025" in out
    assert "🟢" in out


def test_render_prazos_empty():
    assert render_prazos_table(None) == ""


# ---------- build_report integration ----------

def test_build_report_full(tmp_path):
    report = build_report(
        analyzed=_sample_analyzed(),
        contradictions=_sample_contradictions(),
        instances=None,
        prazos=_sample_prazos(),
        risk=_sample_risk(),
        recommendations=_sample_recommendations(),
        output_dir=tmp_path,
    )
    # Every major section should be present
    assert "# 📋 Análise Forense" in report
    assert "## 📋 Resumo Executivo" in report
    assert "## ⚠️ Alertas Críticos" in report
    assert "## 📑 Peças do Processo" in report
    assert "## 🔍 Contradições Detectadas" in report
    assert "## 📊 Avaliação de Risco" in report
    assert "## 🎯 Recomendações Estratégicas" in report
    assert "## 📅 Cronologia" in report
    assert "## ⏰ Prazos" in report
    # Art. 942 alert must be present (the uau moment)
    assert "942" in report
    # Verbatim citations
    assert "485.000,00" in report
    # Footer disclaimer
    assert "assistida por IA" in report


def test_build_report_minimal(tmp_path):
    """Should degrade gracefully with only analyzed.json."""
    report = build_report(
        analyzed=_sample_analyzed(),
        contradictions=None,
        instances=None,
        prazos=None,
        risk=None,
        recommendations=None,
        output_dir=tmp_path,
    )
    assert "# 📋 Análise Forense" in report
    assert "## 📑 Peças do Processo" in report
    # Optional sections should be absent
    assert "## 📊 Avaliação de Risco" not in report
    assert "## 🎯 Recomendações" not in report


def test_cli_writes_report(tmp_path):
    # Create all fixture files
    analyzed_path = tmp_path / "analyzed.json"
    analyzed_path.write_text(json.dumps(_sample_analyzed(), ensure_ascii=False), encoding="utf-8")
    contradictions_path = tmp_path / "contradictions.json"
    contradictions_path.write_text(json.dumps(_sample_contradictions(), ensure_ascii=False), encoding="utf-8")
    risk_path = tmp_path / "risk.json"
    risk_path.write_text(json.dumps(_sample_risk(), ensure_ascii=False), encoding="utf-8")
    prazos_path = tmp_path / "prazos.json"
    prazos_path.write_text(json.dumps(_sample_prazos(), ensure_ascii=False), encoding="utf-8")
    recommendations_path = tmp_path / "recommendations.json"
    recommendations_path.write_text(json.dumps(_sample_recommendations(), ensure_ascii=False), encoding="utf-8")

    out = tmp_path / "REPORT.md"
    rc = main([
        "--analyzed", str(analyzed_path),
        "--contradictions", str(contradictions_path),
        "--risk", str(risk_path),
        "--prazos", str(prazos_path),
        "--recommendations", str(recommendations_path),
        "--output", str(out),
    ])
    assert rc == 0
    assert out.exists()
    content = out.read_text(encoding="utf-8")
    assert "Análise Forense" in content
    assert len(content.splitlines()) > 50


def test_cli_missing_analyzed(tmp_path):
    rc = main([
        "--analyzed", str(tmp_path / "nope.json"),
        "--output", str(tmp_path / "out.md"),
    ])
    assert rc == 2
