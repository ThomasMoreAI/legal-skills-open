"""Tests for scripts/integrity_check.py"""

import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from integrity_check import (
    calculate_ocr_confidence,
    detect_metadata_anomalies,
    detect_page_gaps,
    generate_integrity_report,
)


class TestOcrConfidence:
    def test_clean_legal_text(self):
        text = (
            "SENTENÇA. Vistos. O autor ajuizou ação de indenização por danos "
            "morais e materiais em face do réu, alegando que sofreu prejuízo "
            "decorrente de vazamento de dados. A contestação foi apresentada "
            "tempestivamente. O juiz de direito da comarca proferiu decisão."
        )
        score = calculate_ocr_confidence(text)
        assert score >= 0.6

    def test_garbled_text(self):
        text = "xkzq bvnm rthl wcjf plmk sdfg hjkl zxcv bnmq wert yuip asdf ghjk"
        score = calculate_ocr_confidence(text)
        assert score < 0.4

    def test_empty_text(self):
        assert calculate_ocr_confidence('') == 0.0

    def test_short_text(self):
        assert calculate_ocr_confidence('abc') == 0.0

    def test_mixed_quality(self):
        text = (
            "O processo foi distribuído em 2025. xkzqm bvnmt rthlp. "
            "A sentença condenou o réu ao pagamento. wcjfx plmks sdfgy."
        )
        score = calculate_ocr_confidence(text)
        # Should be between garbled and clean
        assert 0.2 < score < 0.8


class TestMetadataAnomalies:
    def test_no_anomalies(self):
        chunks = [
            {'label': 'PETIÇÃO INICIAL', 'primary_date': '05/02/2025'},
            {'label': 'CONTESTAÇÃO', 'primary_date': '10/03/2025'},
            {'label': 'SENTENÇA', 'primary_date': '01/07/2025'},
        ]
        anomalies = detect_metadata_anomalies(chunks)
        assert len(anomalies) == 0

    def test_missing_contestacao(self):
        chunks = [
            {'label': 'PETIÇÃO INICIAL', 'primary_date': '05/02/2025'},
            {'label': 'SENTENÇA', 'primary_date': '01/07/2025'},
        ]
        anomalies = detect_metadata_anomalies(chunks)
        faltante = [a for a in anomalies if a['tipo'] == 'PECA_FALTANTE']
        assert len(faltante) == 1

    def test_duplicate_sentenca(self):
        chunks = [
            {'label': 'PETIÇÃO INICIAL'},
            {'label': 'SENTENÇA'},
            {'label': 'SENTENÇA'},
        ]
        anomalies = detect_metadata_anomalies(chunks)
        dupes = [a for a in anomalies if a['tipo'] == 'PECA_DUPLICADA']
        assert len(dupes) == 1

    def test_duplicate_despacho_ok(self):
        # Multiple DESPACHO is normal
        chunks = [
            {'label': 'DESPACHO'},
            {'label': 'DESPACHO'},
            {'label': 'DESPACHO'},
        ]
        anomalies = detect_metadata_anomalies(chunks)
        dupes = [a for a in anomalies if a['tipo'] == 'PECA_DUPLICADA']
        assert len(dupes) == 0

    def test_multiple_process_numbers(self):
        chunks = [
            {'label': 'PETIÇÃO INICIAL', 'processo_number': '1234567-89.2025.8.26.0100'},
            {'label': 'CONTESTAÇÃO', 'processo_number': '9999999-00.2024.8.19.0001'},
        ]
        anomalies = detect_metadata_anomalies(chunks)
        divergent = [a for a in anomalies if a['tipo'] == 'NUMERO_PROCESSO_DIVERGENTE']
        assert len(divergent) == 1


class TestPageGaps:
    def test_no_gaps(self):
        text = "fls. 1 ... fls. 2 ... fls. 3 ... fls. 4 ... fls. 5"
        gaps = detect_page_gaps(text, {'pages': 10})
        assert len(gaps) == 0

    def test_large_gap(self):
        text = "fls. 1 ... fls. 2 ... fls. 3 ... fls. 50 ... fls. 51"
        gaps = detect_page_gaps(text, {'pages': 60})
        lacunas = [g for g in gaps if g['tipo'] == 'LACUNA_PAGINAS']
        assert len(lacunas) == 1

    def test_incompatible_numbering(self):
        text = "fls. 1 ... fls. 5 ... fls. 10 ... fls. 500"
        gaps = detect_page_gaps(text, {'pages': 50})
        incompat = [g for g in gaps if g['tipo'] == 'NUMERACAO_INCOMPATIVEL']
        assert len(incompat) == 1

    def test_too_few_markers(self):
        text = "fls. 1 ... fls. 100"
        gaps = detect_page_gaps(text, {'pages': 100})
        assert len(gaps) == 0  # Not enough data points


class TestIntegrityReport:
    def test_generates_report(self):
        chunks = [
            {
                'index': 0,
                'label': 'PETIÇÃO INICIAL',
                'text': 'O autor ajuizou ação de indenização por danos morais perante o juiz da vara cível.',
                'primary_date': '05/02/2025',
            },
        ]
        report = generate_integrity_report(chunks)
        assert 'overall_confidence' in report
        assert 'ocr_scores' in report
        assert 'anomalies' in report
        assert 'page_gaps' in report
        assert len(report['ocr_scores']) == 1
