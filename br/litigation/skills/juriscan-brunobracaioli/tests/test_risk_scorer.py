"""Tests for scripts/risk_scorer.py"""

import sys
import os

import pytest

import warnings as _warnings

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts', 'legacy'))
with _warnings.catch_warnings():
    _warnings.simplefilter("ignore", DeprecationWarning)
    from risk_scorer import (  # noqa: E402
        score_procedural_risk,
        score_merit_indicators,
        score_monetary_exposure,
        generate_risk_report,
    )


def _brl_to_float(s: str | None) -> float:
    if s is None:
        return 0.0
    return float(s.replace('R$', '').strip().replace('.', '').replace(',', '.'))


class TestLikelyRangeInvariant:
    """Regression for Phase 1 Step 1.1 — min <= max invariant."""

    def test_outros_larger_than_condenacao_is_clamped(self):
        """Reproduces the field bug: outros (R$485k) > condenação (R$453k).

        Before the fix, likely_range.min was the 'outros' value and
        likely_range.max was the condenação — producing min > max.
        """
        analysis = {
            'chunks': [
                {
                    'label': 'PETIÇÃO INICIAL',
                    'valores': {
                        'causa': 'R$ 500.000,00',
                        'outros': [{'valor': 'R$ 485.000,00', 'descricao': 'pedidos'}],
                    },
                },
                {
                    'label': 'SENTENÇA',
                    'valores': {'condenacao': 'R$ 453.300,00'},
                },
            ],
        }
        result = score_monetary_exposure(analysis)
        rng = result['likely_range']
        assert rng['min'] is not None and rng['max'] is not None
        mn = _brl_to_float(rng['min'])
        mx = _brl_to_float(rng['max'])
        assert mn <= mx, f"invariant violated: min={mn} max={mx}"

    def test_happy_path_min_below_max(self):
        analysis = {
            'chunks': [
                {
                    'label': 'SENTENÇA',
                    'valores': {'condenacao': 'R$ 100.000,00'},
                },
            ],
        }
        result = score_monetary_exposure(analysis)
        mn = _brl_to_float(result['likely_range']['min'])
        mx = _brl_to_float(result['likely_range']['max'])
        assert mn <= mx


class TestProceduralRisk:
    def test_perfect_score(self):
        analysis = {
            'chunks': [
                {'label': 'PETIÇÃO INICIAL'},
                {'label': 'CONTESTAÇÃO'},
                {'label': 'SENTENÇA'},
            ],
            'prazos_calculados': [],
            'integrity_report': {'anomalies': [], 'ocr_scores': []},
        }
        result = score_procedural_risk(analysis)
        assert result['score'] == 10.0
        assert len(result['factors']) == 0

    def test_missing_contestacao(self):
        analysis = {
            'chunks': [
                {'label': 'PETIÇÃO INICIAL'},
                {'label': 'SENTENÇA'},
            ],
        }
        result = score_procedural_risk(analysis)
        assert result['score'] < 10.0
        assert any('Contestação ausente' in f['fator'] for f in result['factors'])

    def test_vencido_prazos(self):
        analysis = {
            'chunks': [],
            'prazos_calculados': [
                {'tipo': 'contestação', 'status': 'vencido'},
            ],
        }
        result = score_procedural_risk(analysis)
        assert result['score'] < 10.0


class TestMeritIndicators:
    def test_neutral_baseline(self):
        analysis = {'chunks': [], 'contradictions': []}
        result = score_merit_indicators(analysis)
        assert result['score'] == 5.0

    def test_high_contradictions_lower_score(self):
        analysis = {
            'chunks': [],
            'contradictions': [
                {'tipo': 'FATO_DIVERGENTE', 'impacto': 'ALTO', 'descricao': 'Divergência grave'},
            ],
        }
        result = score_merit_indicators(analysis)
        assert result['score'] < 5.0

    def test_laudo_pericial_raises_score(self):
        analysis = {
            'chunks': [{'label': 'LAUDO PERICIAL'}],
            'contradictions': [],
        }
        result = score_merit_indicators(analysis)
        assert result['score'] > 5.0

    def test_sentenca_procedente_raises_score(self):
        analysis = {
            'chunks': [
                {'label': 'SENTENÇA', 'decisao': 'JULGO PROCEDENTE a ação'},
            ],
            'contradictions': [],
        }
        result = score_merit_indicators(analysis)
        assert result['score'] > 5.0


class TestMonetaryExposure:
    def test_with_values(self):
        analysis = {
            'chunks': [
                {
                    'label': 'PETIÇÃO INICIAL',
                    'valores': {'causa': 'R$ 75.000,00', 'condenacao': None, 'outros': []},
                },
                {
                    'label': 'SENTENÇA',
                    'valores': {'causa': None, 'condenacao': 'R$ 48.500,00', 'outros': []},
                },
            ],
        }
        result = score_monetary_exposure(analysis)
        assert result['max_exposure'] is not None
        assert '75' in result['max_exposure']

    def test_empty(self):
        analysis = {'chunks': []}
        result = score_monetary_exposure(analysis)
        assert result['max_exposure'] is None


class TestGenerateRiskReport:
    def test_generates_all_sections(self, sample_analyzed):
        report = generate_risk_report(sample_analyzed)
        assert 'risk_level' in report
        assert report['risk_level'] in ('ALTO', 'MÉDIO', 'BAIXO')
        assert 'overall_score' in report
        assert 'procedural_risk' in report
        assert 'merit_indicators' in report
        assert 'monetary_exposure' in report
        assert 'strategic_recommendations' in report
