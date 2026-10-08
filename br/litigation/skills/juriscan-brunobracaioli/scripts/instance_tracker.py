#!/usr/bin/env python3
"""
instance_tracker.py — Multi-instance argument tracking.

Classifies legal pieces by judicial instance and structures data for
Claude's argument evolution analysis across 1ª instância → TJ → STJ → STF.

Usage:
    python3 instance_tracker.py --analysis analyzed.json --output instances.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys


# Instance detection patterns (checked in order, most specific first)
_INSTANCE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ('stf', re.compile(r'(?i)(?:Supremo\s+Tribunal\s+Federal|STF|Plenário\s+do\s+STF)')),
    ('stj', re.compile(r'(?i)(?:Superior\s+Tribunal\s+de\s+Justiça|STJ|Min(?:istro)?\.?\s+\w)')),
    ('tj', re.compile(r'(?i)(?:Des(?:embargador)?\.?\s|Câmara|Turma\s+(?:Cível|Criminal)|Tribunal\s+de\s+Justiça|TRF\d|TRT\d)')),
    ('1a_instancia', re.compile(r'(?i)(?:Vara|Juiz(?:a)?\s+de\s+Direito|Juiz(?:a)?\s+Federal|Foro)')),
]

# Piece types that strongly indicate a specific instance
_PIECE_INSTANCE_MAP: dict[str, str] = {
    'PETIÇÃO INICIAL': '1a_instancia',
    'CONTESTAÇÃO': '1a_instancia',
    'RÉPLICA': '1a_instancia',
    'RECONVENÇÃO': '1a_instancia',
    'ATA DE AUDIÊNCIA': '1a_instancia',
    'LAUDO PERICIAL': '1a_instancia',
    'SENTENÇA': '1a_instancia',
    'CUMPRIMENTO DE SENTENÇA': '1a_instancia',
    'IMPUGNAÇÃO AO CUMPRIMENTO': '1a_instancia',
    'PENHORA': '1a_instancia',
    'ALVARÁ': '1a_instancia',
    'RECURSO ESPECIAL': 'stj',
    'RECURSO EXTRAORDINÁRIO': 'stf',
}


def classify_instance(chunk: dict) -> str:
    """Classify which judicial instance a chunk belongs to.

    Priority:
    1. Explicit piece type mapping (e.g., SENTENÇA → 1a_instancia)
    2. Text-based pattern matching (e.g., "Desembargador" → tj)
    3. Default to '1a_instancia'
    """
    label = chunk.get('label', '')

    # Check piece type map first
    if label in _PIECE_INSTANCE_MAP:
        return _PIECE_INSTANCE_MAP[label]

    # For ACÓRDÃO, APELAÇÃO, AGRAVO, etc. — detect from text
    text = chunk.get('text', '')[:3000]  # Check first 3000 chars
    vara = chunk.get('partes', {}).get('vara', '') or ''
    combined = f"{text} {vara}"

    for instance, pattern in _INSTANCE_PATTERNS:
        if pattern.search(combined):
            return instance

    return '1a_instancia'


def build_instance_flow(chunks: list[dict]) -> dict:
    """Group analyzed chunks by judicial instance.

    Returns:
        {
            '1a_instancia': {'pieces': [...], 'decisao_final': str, 'resultado': str},
            'tj': {'pieces': [...], 'decisao_final': str, 'resultado': str},
            'stj': {...},
            'stf': {...},
        }
    """
    instances: dict[str, dict] = {}

    for chunk in chunks:
        instance = chunk.get('instancia') or classify_instance(chunk)

        if instance not in instances:
            instances[instance] = {
                'pieces': [],
                'decisao_final': None,
                'resultado': None,
            }

        instances[instance]['pieces'].append({
            'index': chunk.get('index'),
            'label': chunk.get('label'),
            'data': chunk.get('primary_date') or chunk.get('data'),
            'resumo': chunk.get('resumo', ''),
        })

        # Track the final decision for each instance
        decisao = chunk.get('decisao')
        if decisao and chunk.get('label') in ('SENTENÇA', 'ACÓRDÃO'):
            instances[instance]['decisao_final'] = decisao
            # Try to extract resultado
            text = decisao.lower()
            if 'improcedente' in text and 'parcialmente' not in text:
                instances[instance]['resultado'] = 'improcedente'
            elif 'parcialmente procedente' in text:
                instances[instance]['resultado'] = 'parcialmente_procedente'
            elif 'procedente' in text:
                instances[instance]['resultado'] = 'procedente'
            elif 'nego provimento' in text or 'desprovido' in text:
                instances[instance]['resultado'] = 'recurso_desprovido'
            elif 'dou provimento' in text or 'provido' in text:
                instances[instance]['resultado'] = 'recurso_provido'

    return instances


def build_argument_tracks(chunks: list[dict]) -> list[dict]:
    """Structure arguments for Claude's cross-instance tracking prompt.

    Groups arguments by polo (ativo/passivo) and instance, preparing
    structured input for the semantic analysis prompt.
    """
    tracks_input: dict[str, list[dict]] = {}

    for chunk in chunks:
        instance = chunk.get('instancia') or classify_instance(chunk)
        args = chunk.get('argumentos_chave', [])
        label = chunk.get('label', '')

        for arg in args:
            # Normalize argument text for grouping
            key = arg.strip().lower()[:100]
            if key not in tracks_input:
                tracks_input[key] = []

            tracks_input[key].append({
                'instancia': instance,
                'peca': label,
                'texto': arg,
                'peca_index': chunk.get('index'),
            })

    # Convert to list format
    result = []
    for key, appearances in tracks_input.items():
        if len(appearances) >= 1:
            result.append({
                'argumento': appearances[0]['texto'],
                'aparicoes': appearances,
                'instancias_presentes': list(set(a['instancia'] for a in appearances)),
            })

    return result


def generate_instance_report(analysis: dict) -> dict:
    """Generate the full instance tracking report."""
    chunks = analysis.get('chunks', [])

    # Classify instances for all chunks
    for chunk in chunks:
        if not chunk.get('instancia'):
            chunk['instancia'] = classify_instance(chunk)

    return {
        'instances': build_instance_flow(chunks),
        'argument_tracks': build_argument_tracks(chunks),
    }


def main():
    parser = argparse.ArgumentParser(description='Multi-instance argument tracker')
    parser.add_argument('--analysis', '-a', required=True, help='Path to analyzed.json')
    parser.add_argument('--output', '-o', help='Output path')
    args = parser.parse_args()

    with open(args.analysis, 'r', encoding='utf-8') as f:
        analysis = json.load(f)

    report = generate_instance_report(analysis)

    output_path = args.output or os.path.join(os.path.dirname(args.analysis), 'instances.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\nInstance Tracking Report:")
    print(f"  Instances: {list(report['instances'].keys())}")
    print(f"  Argument tracks: {len(report['argument_tracks'])}")
    print(f"  Output: {output_path}")


if __name__ == '__main__':
    main()
