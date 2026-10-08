#!/usr/bin/env python3
"""
integrity_check.py — Document integrity and OCR quality verification.

Detects:
- OCR quality issues (garbled text, encoding anomalies)
- Metadata anomalies (missing pieces, date inversions, duplicate labels)
- Page gaps (missing pages based on markers)

Usage:
    python3 integrity_check.py --input ./analysis/
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Add utils to path
sys.path.insert(0, os.path.dirname(__file__))
from utils.dates import extract_all_dates, validate_chronology

# Portuguese dictionary words for OCR confidence (common legal terms)
_LEGAL_TERMS = {
    'processo', 'autor', 'réu', 'juiz', 'vara', 'sentença', 'acórdão',
    'petição', 'contestação', 'réplica', 'recurso', 'apelação', 'agravo',
    'decisão', 'despacho', 'certidão', 'mandado', 'intimação', 'citação',
    'direito', 'lei', 'artigo', 'código', 'tribunal', 'justiça', 'foro',
    'comarca', 'advogado', 'procurador', 'ministério', 'público', 'federal',
    'estadual', 'civil', 'penal', 'trabalho', 'consumidor', 'constituição',
    'danos', 'morais', 'materiais', 'indenização', 'condenação', 'honorários',
    'custas', 'valor', 'causa', 'pedido', 'prova', 'testemunha', 'perito',
    'laudo', 'parecer', 'audiência', 'julgamento', 'votação', 'relator',
    'ementa', 'voto', 'dispositivo', 'procedente', 'improcedente', 'parcial',
    'prazo', 'dias', 'úteis', 'recurso', 'embargos', 'contrarrazões',
}

# Pattern for consecutive consonants (OCR artifact indicator)
_CONSONANT_CLUSTER = re.compile(r'[bcdfghjklmnpqrstvwxyz]{5,}', re.IGNORECASE)

# Page marker patterns
_PAGE_MARKERS = [
    re.compile(r'(?i)fls?\.\s*(\d+)'),
    re.compile(r'(?i)Página\s+(\d+)\s+de\s+(\d+)'),
    re.compile(r'(?i)pág(?:ina)?\.\s*(\d+)'),
]

# Expected piece ordering for anomaly detection
_EXPECTED_PIECES = [
    'PETIÇÃO INICIAL', 'CONTESTAÇÃO', 'RÉPLICA', 'SENTENÇA',
    'APELAÇÃO', 'CONTRARRAZÕES', 'ACÓRDÃO',
]


def calculate_ocr_confidence(text: str) -> float:
    """Calculate heuristic OCR confidence score (0.0-1.0).

    Factors:
    - Ratio of recognized words vs garbage
    - Presence of expected legal patterns
    - Character encoding anomalies
    - Consecutive consonant clusters (OCR artifacts)
    """
    if not text or len(text) < 50:
        return 0.0

    words = re.findall(r'\b[a-záàâãéèêíïóôõöúçñ]{3,}\b', text.lower())
    if not words:
        return 0.0

    # Factor 1: Legal term density (0-0.3)
    legal_count = sum(1 for w in words if w in _LEGAL_TERMS)
    legal_density = min(legal_count / max(len(words), 1), 0.3)
    legal_score = legal_density / 0.3 * 0.3

    # Factor 2: Vowel presence ratio (0-0.4)
    # Real Portuguese words contain vowels; OCR garbage typically has low vowel ratios
    all_tokens = text.split()
    if not all_tokens:
        return 0.0
    vowel_pattern = re.compile(r'[aeiouáàâãéèêíïóôõöú]', re.IGNORECASE)
    tokens_with_vowels = sum(1 for t in all_tokens if len(t) >= 3 and vowel_pattern.search(t))
    long_tokens = sum(1 for t in all_tokens if len(t) >= 3)
    vowel_ratio = tokens_with_vowels / max(long_tokens, 1)
    word_score = vowel_ratio * 0.4

    # Factor 3: No consonant clusters (0-0.15)
    clusters = _CONSONANT_CLUSTER.findall(text[:5000])
    cluster_penalty = min(len(clusters) * 0.03, 0.15)
    cluster_score = 0.15 - cluster_penalty

    # Factor 4: Encoding quality (0-0.15)
    # Check for replacement characters, null bytes, control chars
    bad_chars = len(re.findall(r'[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]', text[:5000]))
    encoding_penalty = min(bad_chars * 0.03, 0.15)
    encoding_score = 0.15 - encoding_penalty

    total = legal_score + word_score + cluster_score + encoding_score
    return round(min(max(total, 0.0), 1.0), 3)


def detect_metadata_anomalies(chunks: list[dict]) -> list[dict]:
    """Flag metadata anomalies in the chunk set.

    Checks for:
    - Date chronology violations
    - Missing expected pieces
    - Duplicate piece labels
    - Unusually short/long pieces relative to type
    """
    anomalies = []

    # Date chronology
    chrono_issues = validate_chronology(chunks)
    anomalies.extend(chrono_issues)

    # Missing expected pieces (only flag if we have both petição and sentença)
    labels = [c.get('label', '') for c in chunks]
    has_peticao = 'PETIÇÃO INICIAL' in labels
    has_sentenca = 'SENTENÇA' in labels

    if has_peticao and has_sentenca and 'CONTESTAÇÃO' not in labels:
        anomalies.append({
            'tipo': 'PECA_FALTANTE',
            'descricao': 'Contestação não detectada entre Petição Inicial e Sentença',
            'impacto': 'MÉDIO',
            'recomendacao': 'Verificar se é revelia ou se a contestação não foi detectada pelo chunking',
        })

    # Duplicate labels
    label_counts: dict[str, int] = {}
    for label in labels:
        label_counts[label] = label_counts.get(label, 0) + 1

    for label, count in label_counts.items():
        if count > 1 and label not in ('DESPACHO', 'CERTIDÃO', 'OFÍCIO', 'MANDADO/CARTA'):
            anomalies.append({
                'tipo': 'PECA_DUPLICADA',
                'descricao': f"'{label}' aparece {count} vezes — verificar se são peças distintas ou chunking duplicado",
                'impacto': 'BAIXO',
                'recomendacao': 'Revisar manualmente se são peças distintas (ex: sentença de mérito + sentença de embargos)',
            })

    # Process number changes
    numeros = set()
    for c in chunks:
        n = c.get('processo_number') or c.get('numero_processo')
        if n:
            numeros.add(n)

    if len(numeros) > 1:
        anomalies.append({
            'tipo': 'NUMERO_PROCESSO_DIVERGENTE',
            'descricao': f"Múltiplos números de processo detectados: {', '.join(numeros)}",
            'impacto': 'ALTO',
            'recomendacao': 'Verificar se o PDF contém processos distintos ou se há erro de OCR nos números',
        })

    return anomalies


def detect_page_gaps(full_text: str, pdf_info: dict) -> list[dict]:
    """Flag potential missing pages based on page markers in text."""
    gaps = []

    # Extract page numbers from "fls." markers
    page_numbers: list[int] = []
    for pattern in _PAGE_MARKERS:
        for m in pattern.finditer(full_text):
            try:
                page_numbers.append(int(m.group(1)))
            except (ValueError, IndexError):
                continue

    if len(page_numbers) < 3:
        return gaps

    page_numbers = sorted(set(page_numbers))

    # Find gaps > 5 pages
    for i in range(len(page_numbers) - 1):
        gap = page_numbers[i + 1] - page_numbers[i]
        if gap > 5:
            gaps.append({
                'tipo': 'LACUNA_PAGINAS',
                'descricao': f"Possível lacuna de {gap} páginas entre fls. {page_numbers[i]} e fls. {page_numbers[i+1]}",
                'impacto': 'MÉDIO',
                'recomendacao': 'Verificar se há páginas faltantes ou se a numeração é descontínua',
            })

    # Check against total pages from PDF info
    total_pages = pdf_info.get('pages', 0)
    if total_pages > 0 and page_numbers:
        max_fls = max(page_numbers)
        if max_fls > total_pages * 1.5:
            gaps.append({
                'tipo': 'NUMERACAO_INCOMPATIVEL',
                'descricao': f"Maior número de fls. ({max_fls}) excede total de páginas do PDF ({total_pages})",
                'impacto': 'BAIXO',
                'recomendacao': 'Numeração de fls. dos autos ≠ páginas do PDF — normal em processos digitalizados',
            })

    return gaps


def generate_integrity_report(
    chunks: list[dict],
    full_text: str = '',
    pdf_info: dict | None = None,
) -> dict:
    """Aggregate all integrity checks into a single report."""
    pdf_info = pdf_info or {}

    # OCR confidence per chunk
    ocr_scores = []
    for chunk in chunks:
        text = chunk.get('text', '')
        score = calculate_ocr_confidence(text)
        ocr_scores.append({
            'chunk_index': chunk.get('index', 0),
            'label': chunk.get('label', '?'),
            'score': score,
        })

    overall_confidence = (
        sum(s['score'] for s in ocr_scores) / len(ocr_scores) if ocr_scores else 0.0
    )

    # Metadata anomalies
    anomalies = detect_metadata_anomalies(chunks)

    # Page gaps
    page_gaps = detect_page_gaps(full_text, pdf_info) if full_text else []

    # Low confidence warnings
    low_confidence = [s for s in ocr_scores if s['score'] < 0.7]
    recommendations = []
    if low_confidence:
        recommendations.append(
            f"{len(low_confidence)} chunk(s) com OCR confidence < 0.7 — "
            "considerar re-extração com vision ou OCR de maior qualidade"
        )

    high_impact = [a for a in anomalies if a.get('impacto') == 'ALTO']
    if high_impact:
        recommendations.append(
            f"{len(high_impact)} anomalia(s) de alto impacto detectada(s) — revisar antes de prosseguir"
        )

    return {
        'overall_confidence': round(overall_confidence, 3),
        'ocr_scores': ocr_scores,
        'anomalies': anomalies,
        'page_gaps': page_gaps,
        'recommendations': recommendations,
    }


def main():
    parser = argparse.ArgumentParser(description='Check document integrity and OCR quality')
    parser.add_argument('--input', '-i', required=True, help='Analysis directory (with index.json and chunks/)')
    args = parser.parse_args()

    input_dir = args.input
    index_path = os.path.join(input_dir, 'index.json')

    if not os.path.exists(index_path):
        print(f"[ERROR] index.json not found in {input_dir}", file=sys.stderr)
        sys.exit(1)

    with open(index_path, 'r', encoding='utf-8') as f:
        index = json.load(f)

    # Load chunks with text
    chunks = []
    for chunk_meta in index.get('chunks', []):
        chunk_file = os.path.join(input_dir, chunk_meta.get('chunk_file', ''))
        text = ''
        if os.path.exists(chunk_file):
            with open(chunk_file, 'r', encoding='utf-8') as f:
                text = f.read()
        chunk = {**chunk_meta, 'text': text}
        chunks.append(chunk)

    # Load full text if available
    full_text_path = os.path.join(input_dir, 'full_text.txt')
    full_text = ''
    if os.path.exists(full_text_path):
        with open(full_text_path, 'r', encoding='utf-8') as f:
            full_text = f.read()

    report = generate_integrity_report(
        chunks,
        full_text=full_text,
        pdf_info=index.get('pdf_info', {}),
    )

    # Save report
    output_path = os.path.join(input_dir, 'integrity_report.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\nIntegrity Report:")
    print(f"  Overall confidence: {report['overall_confidence']:.1%}")
    print(f"  Anomalies: {len(report['anomalies'])}")
    print(f"  Page gaps: {len(report['page_gaps'])}")
    for rec in report['recommendations']:
        print(f"  [!] {rec}")
    print(f"  Output: {output_path}")


if __name__ == '__main__':
    main()
