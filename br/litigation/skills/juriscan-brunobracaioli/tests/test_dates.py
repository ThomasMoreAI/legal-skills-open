"""Tests for scripts/utils/dates.py"""

import sys
import os
from datetime import date

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from utils.dates import (
    parse_brazilian_date,
    extract_all_dates,
    find_primary_date,
    validate_chronology,
    format_date_br,
    format_date_iso,
)


class TestParseBrazilianDate:
    def test_numeric_dmy(self):
        assert parse_brazilian_date('05/02/2025') == date(2025, 2, 5)

    def test_numeric_dmy_with_dots(self):
        assert parse_brazilian_date('05.02.2025') == date(2025, 2, 5)

    def test_numeric_dmy_with_dashes(self):
        assert parse_brazilian_date('05-02-2025') == date(2025, 2, 5)

    def test_written_portuguese(self):
        assert parse_brazilian_date('5 de fevereiro de 2025') == date(2025, 2, 5)

    def test_written_portuguese_marco(self):
        # "março" with cedilla and without
        assert parse_brazilian_date('10 de março de 2025') == date(2025, 3, 10)
        assert parse_brazilian_date('10 de marco de 2025') == date(2025, 3, 10)

    def test_iso_format(self):
        assert parse_brazilian_date('2025-02-05') == date(2025, 2, 5)

    def test_invalid_date(self):
        assert parse_brazilian_date('31/02/2025') is None

    def test_empty_string(self):
        assert parse_brazilian_date('') is None

    def test_garbage(self):
        assert parse_brazilian_date('not a date') is None

    def test_date_in_context(self):
        # Should find date even with surrounding text
        assert parse_brazilian_date('São Paulo, 5 de fevereiro de 2025.') == date(2025, 2, 5)

    def test_out_of_range_year(self):
        assert parse_brazilian_date('01/01/1800') is None


class TestExtractAllDates:
    def test_multiple_dates(self):
        text = "Contrato firmado em 15/03/2020. Vazamento em 10/01/2025. Notificação em 25/01/2025."
        dates = extract_all_dates(text)
        assert len(dates) == 3
        assert dates[0]['parsed'] == date(2020, 3, 15)
        assert dates[1]['parsed'] == date(2025, 1, 10)
        assert dates[2]['parsed'] == date(2025, 1, 25)

    def test_mixed_formats(self):
        text = "Em 5 de fevereiro de 2025 e depois em 10/03/2025."
        dates = extract_all_dates(text)
        assert len(dates) == 2

    def test_context_captured(self):
        text = "A sentença foi proferida em 01/07/2025 pelo juiz."
        dates = extract_all_dates(text)
        assert len(dates) == 1
        assert '01/07/2025' in dates[0]['context']

    def test_no_dates(self):
        assert extract_all_dates("Texto sem datas.") == []

    def test_deduplication(self):
        # Same date at different positions should both be captured
        text = "Data: 01/01/2025. Repetindo: 01/01/2025."
        dates = extract_all_dates(text)
        assert len(dates) == 2  # Two occurrences, different positions


class TestFindPrimaryDate:
    def test_sentenca_publique_se(self):
        text = "Publique-se. 01/07/2025\n\nDr. Juiz de Direito"
        result = find_primary_date(text, 'SENTENÇA')
        assert result is not None
        assert result['parsed'] == date(2025, 7, 1)

    def test_acordao_sessao(self):
        text = "Sessão de julgamento realizada em 15/10/2025."
        result = find_primary_date(text, 'ACÓRDÃO')
        assert result is not None
        assert result['parsed'] == date(2025, 10, 15)

    def test_fallback_first_date(self):
        text = "Texto qualquer datado de 05/02/2025. Outra data 10/03/2025."
        result = find_primary_date(text, 'CERTIDÃO')
        assert result is not None
        assert result['parsed'] == date(2025, 2, 5)

    def test_no_dates(self):
        result = find_primary_date("Texto sem data nenhuma.", 'DESPACHO')
        assert result is None


class TestValidateChronology:
    def test_valid_order(self):
        chunks = [
            {'label': 'PETIÇÃO INICIAL', 'primary_date': '05/02/2025'},
            {'label': 'CONTESTAÇÃO', 'primary_date': '10/03/2025'},
            {'label': 'SENTENÇA', 'primary_date': '01/07/2025'},
        ]
        anomalies = validate_chronology(chunks)
        assert anomalies == []

    def test_inverted_order(self):
        chunks = [
            {'label': 'PETIÇÃO INICIAL', 'primary_date': '10/03/2025'},
            {'label': 'CONTESTAÇÃO', 'primary_date': '05/02/2025'},
        ]
        anomalies = validate_chronology(chunks)
        assert len(anomalies) == 1
        assert anomalies[0]['tipo'] == 'DATA_CONFLITANTE'

    def test_missing_dates_skipped(self):
        chunks = [
            {'label': 'PETIÇÃO INICIAL', 'primary_date': '05/02/2025'},
            {'label': 'CONTESTAÇÃO', 'primary_date': None},
            {'label': 'SENTENÇA', 'primary_date': '01/07/2025'},
        ]
        anomalies = validate_chronology(chunks)
        assert anomalies == []


class TestFormatting:
    def test_format_date_br(self):
        assert format_date_br(date(2025, 2, 5)) == '05/02/2025'

    def test_format_date_iso(self):
        assert format_date_iso(date(2025, 2, 5)) == '2025-02-05'
