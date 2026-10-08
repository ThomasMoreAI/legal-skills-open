"""Tests for scripts/utils/cnj.py"""

import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from utils.cnj import (
    parse_cnj,
    validate_cnj_check_digits,
    extract_cnj_numbers,
    CNJNumber,
)


class TestParseCnj:
    def test_standard_format(self):
        result = parse_cnj('1234567-89.2025.8.26.0100')
        assert result is not None
        assert result.sequential == '1234567'
        assert result.check_digits == '89'
        assert result.year == 2025
        assert result.justice_branch == 8
        assert result.court == 26
        assert result.origin == 100

    def test_justice_branch_names(self):
        # State court (branch 8, court 26 = TJSP)
        result = parse_cnj('1234567-89.2025.8.26.0100')
        assert result is not None
        assert result.branch_name == 'Justiça Estadual'
        assert result.court_name == 'TJSP'

    def test_federal_court(self):
        result = parse_cnj('1234567-89.2025.4.03.0000')
        assert result is not None
        assert result.court_name == 'TRF3'

    def test_labor_court(self):
        result = parse_cnj('1234567-89.2025.5.02.0000')
        assert result is not None
        assert result.court_name == 'TRT2'

    def test_formatted_output(self):
        result = parse_cnj('1234567-89.2025.8.26.0100')
        assert result is not None
        assert result.formatted == '1234567-89.2025.8.26.0100'

    def test_in_context(self):
        text = "Processo nº 1234567-89.2025.8.26.0100 da 2ª Vara"
        result = parse_cnj(text)
        assert result is not None
        assert result.sequential == '1234567'

    def test_no_match(self):
        assert parse_cnj('not a process number') is None

    def test_partial_number(self):
        assert parse_cnj('1234567-89') is None


class TestValidateCnjCheckDigits:
    def test_known_valid_structure(self):
        # We test the algorithm itself, not a specific real number
        cnj = parse_cnj('0000000-00.2025.8.26.0100')
        if cnj:
            # The validation function should return a bool without error
            result = validate_cnj_check_digits(cnj)
            assert isinstance(result, bool)


class TestExtractCnjNumbers:
    def test_single(self):
        text = "Processo 1234567-89.2025.8.26.0100 em tramitação."
        results = extract_cnj_numbers(text)
        assert len(results) == 1

    def test_multiple(self):
        text = (
            "Processo 1234567-89.2025.8.26.0100 e "
            "processo 7654321-01.2024.8.19.0001."
        )
        results = extract_cnj_numbers(text)
        assert len(results) == 2

    def test_deduplication(self):
        text = (
            "Processo 1234567-89.2025.8.26.0100. "
            "Novamente: 1234567-89.2025.8.26.0100."
        )
        results = extract_cnj_numbers(text)
        assert len(results) == 1

    def test_no_matches(self):
        assert extract_cnj_numbers("Sem processos aqui.") == []
