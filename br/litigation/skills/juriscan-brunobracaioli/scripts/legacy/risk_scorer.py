#!/usr/bin/env python3
"""
risk_scorer.py — Litigation risk scoring.

DEPRECATED (Phase 5 Step 5.1, 2026-04-11): moved to scripts/legacy/. Still
consumed by SKILL.md when `--pipeline=legacy` is explicit. The agents
pipeline uses juriscan-advogado-autor + juriscan-advogado-reu (two-polo
perspectives) instead. Removal scheduled 3 releases after Phase 6.4 flip.

Computes structural risk indicators from the analysis JSON.
Strategic analysis (Claude-dependent) is handled via prompt templates.

Usage:
    python3 risk_scorer.py --analysis analyzed.json --output risk.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import warnings as _warnings

_warnings.warn(
    "scripts.legacy.risk_scorer is deprecated; prefer perspectives.autor / "
    "perspectives.reu from the agents pipeline.",
    DeprecationWarning,
    stacklevel=2,
)

sys.path.insert(0, os.path.dirname(__file__))
# risk_scorer previously imported from scripts/utils — after the move to
# scripts/legacy/, point to the parent scripts/ so utils.monetary still works.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.monetary import normalize_brl


def score_procedural_risk(analysis: dict) -> dict:
    """Score procedural risk based on structural indicators.

    Checks:
    - Missing expected pieces
    - Prazo compliance (from prazos_calculados if available)
    - Integrity anomalies
    - Chronological consistency
    """
    score = 10.0  # Start perfect, deduct
    factors = []
    chunks = analysis.get('chunks', [])
    labels = [c.get('label', '') for c in chunks]

    # Missing contestação when petição + sentença exist
    if 'PETIÇÃO INICIAL' in labels and 'SENTENÇA' in labels and 'CONTESTAÇÃO' not in labels:
        score -= 2.0
        factors.append({
            'fator': 'Contestação ausente — possível revelia',
            'impacto': -2.0,
            'peca_fonte': 'Análise de peças',
        })

    # Prazo violations
    prazos = analysis.get('prazos_calculados', [])
    vencidos = [p for p in prazos if p.get('status') == 'vencido']
    if vencidos:
        penalty = min(len(vencidos) * 2.0, 5.0)
        score -= penalty
        factors.append({
            'fator': f'{len(vencidos)} prazo(s) vencido(s)',
            'impacto': -penalty,
            'peca_fonte': 'Cálculo de prazos',
        })

    # Integrity issues
    integrity = analysis.get('integrity_report', {})
    anomalies = integrity.get('anomalies', [])
    high_impact = [a for a in anomalies if a.get('impacto') == 'ALTO']
    if high_impact:
        penalty = min(len(high_impact) * 1.5, 3.0)
        score -= penalty
        factors.append({
            'fator': f'{len(high_impact)} anomalia(s) de alto impacto na integridade documental',
            'impacto': -penalty,
            'peca_fonte': 'Relatório de integridade',
        })

    # Low OCR confidence
    ocr_scores = integrity.get('ocr_scores', [])
    low_ocr = [s for s in ocr_scores if s.get('score', 1) < 0.5]
    if low_ocr:
        score -= 1.0
        factors.append({
            'fator': f'{len(low_ocr)} chunk(s) com OCR confidence < 50%',
            'impacto': -1.0,
            'peca_fonte': 'Relatório de integridade',
        })

    return {
        'score': round(max(score, 0.0), 1),
        'factors': factors,
    }


def score_merit_indicators(analysis: dict) -> dict:
    """Score merit indicators from structural data.

    Analyzes: contradiction count/severity, evidence presence, jurisprudence alignment.
    """
    score = 5.0  # Neutral start
    favorable = []
    unfavorable = []
    chunks = analysis.get('chunks', [])

    # Contradictions analysis
    contradictions = analysis.get('contradictions', [])
    high_contradictions = [c for c in contradictions if c.get('impacto') == 'ALTO']
    if high_contradictions:
        score -= 1.5
        unfavorable.append({
            'fator': f'{len(high_contradictions)} contradição(ões) de alto impacto',
            'fundamentacao': '; '.join(c.get('descricao', '')[:100] for c in high_contradictions[:3]),
        })

    # Evidence: laudo pericial present?
    has_laudo = any(c.get('label') == 'LAUDO PERICIAL' for c in chunks)
    if has_laudo:
        score += 1.0
        favorable.append({
            'fator': 'Laudo pericial presente no processo',
            'fundamentacao': 'Prova técnica disponível para fundamentação',
        })

    # Evidence: ata de audiência (witnesses)
    has_audiencia = any(c.get('label') == 'ATA DE AUDIÊNCIA' for c in chunks)
    if has_audiencia:
        score += 0.5
        favorable.append({
            'fator': 'Audiência de instrução realizada',
            'fundamentacao': 'Prova oral produzida',
        })

    # Jurisprudence: binding precedents
    all_binding = []
    for c in chunks:
        all_binding.extend(c.get('binding_precedents', []))

    favoraveis = [b for b in all_binding if b.get('alinhamento') == 'FAVORAVEL_AUTOR']
    desfavoraveis = [b for b in all_binding if b.get('alinhamento') == 'FAVORAVEL_REU']

    if favoraveis:
        score += min(len(favoraveis) * 0.5, 2.0)
        favorable.append({
            'fator': f'{len(favoraveis)} precedente(s) vinculante(s) favorável(is)',
            'fundamentacao': ', '.join(b.get('numero', '?') for b in favoraveis[:3]),
        })

    if desfavoraveis:
        score -= min(len(desfavoraveis) * 0.5, 2.0)
        unfavorable.append({
            'fator': f'{len(desfavoraveis)} precedente(s) vinculante(s) desfavorável(is)',
            'fundamentacao': ', '.join(b.get('numero', '?') for b in desfavoraveis[:3]),
        })

    # Sentença result (if available)
    for c in chunks:
        if c.get('label') == 'SENTENÇA' and c.get('decisao'):
            decisao = c['decisao'].lower()
            if 'procedente' in decisao and 'improcedente' not in decisao:
                score += 1.5
                favorable.append({
                    'fator': 'Sentença procedente (total ou parcial)',
                    'fundamentacao': c['decisao'][:150],
                    'peca_fonte': 'SENTENÇA',
                })

    return {
        'score': round(max(min(score, 10.0), 0.0), 1),
        'favorable_factors': favorable,
        'unfavorable_factors': unfavorable,
    }


def score_monetary_exposure(analysis: dict) -> dict:
    """Calculate monetary exposure from available data."""
    chunks = analysis.get('chunks', [])

    max_exposure = 0.0
    likely_value = 0.0
    min_value = 0.0

    for c in chunks:
        valores = c.get('valores', {})

        # Maximum: valor da causa or sum of pedidos
        causa = normalize_brl(valores.get('causa', '') or '')
        if causa and causa > max_exposure:
            max_exposure = causa

        # Likely: condenação value (from sentença/acórdão)
        cond = normalize_brl(valores.get('condenacao', '') or '')
        if cond and c.get('label') in ('SENTENÇA', 'ACÓRDÃO'):
            likely_value = cond

        # Values from "outros"
        for outro in valores.get('outros', []):
            val = normalize_brl(outro.get('valor', '') or '')
            if val:
                if val > min_value:
                    min_value = val

    # If no condenação, estimate likely as 60% of max
    if not likely_value and max_exposure:
        likely_value = max_exposure * 0.6

    # Min is the smallest acknowledged value or 30% of likely
    if not min_value:
        min_value = likely_value * 0.3 if likely_value else 0.0

    # Costs estimation
    honorarios = likely_value * 0.15 if likely_value else max_exposure * 0.10
    custas = max_exposure * 0.01 if max_exposure else 0.0

    # Ensure invariant: likely_range.min <= likely_range.max.
    # Previously min_value could exceed likely_value when "outros" valores
    # (e.g. aggregated pedidos) were larger than the actual condenação,
    # producing a nonsense range with min > max.
    range_min, range_max = sorted([min_value, likely_value])
    assert range_min <= range_max, (
        f"likely_range invariant violated: min={range_min}, max={range_max}"
    )

    def fmt(v: float) -> str | None:
        if v <= 0:
            return None
        return f"R$ {v:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    return {
        'max_exposure': fmt(max_exposure),
        'likely_range': {
            'min': fmt(range_min),
            'max': fmt(range_max),
        },
        'costs': {
            'custas_estimadas': fmt(custas),
            'honorarios_sucumbencia': fmt(honorarios),
        },
    }


def generate_risk_report(analysis: dict) -> dict:
    """Generate composite risk report."""
    procedural = score_procedural_risk(analysis)
    merit = score_merit_indicators(analysis)
    monetary = score_monetary_exposure(analysis)

    # Weighted composite score (from author's perspective)
    overall = procedural['score'] * 0.3 + merit['score'] * 0.5 + (procedural['score'] * 0.2)
    overall = round(overall, 1)

    if overall < 4.0:
        level = 'ALTO'
    elif overall < 7.0:
        level = 'MÉDIO'
    else:
        level = 'BAIXO'

    return {
        'risk_level': level,
        'overall_score': overall,
        'procedural_risk': procedural,
        'merit_indicators': merit,
        'monetary_exposure': monetary,
        'strategic_recommendations': [],  # Populated by Claude via prompt
    }


def main():
    parser = argparse.ArgumentParser(description='Litigation risk scorer')
    parser.add_argument('--analysis', '-a', required=True, help='Path to analyzed.json')
    parser.add_argument('--output', '-o', help='Output path')
    args = parser.parse_args()

    with open(args.analysis, 'r', encoding='utf-8') as f:
        analysis = json.load(f)

    report = generate_risk_report(analysis)

    output_path = args.output or os.path.join(os.path.dirname(args.analysis), 'risk.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\nRisk Assessment:")
    print(f"  Level: {report['risk_level']}")
    print(f"  Score: {report['overall_score']}/10")
    print(f"  Procedural: {report['procedural_risk']['score']}/10")
    print(f"  Merit: {report['merit_indicators']['score']}/10")
    print(f"  Output: {output_path}")


if __name__ == '__main__':
    main()
