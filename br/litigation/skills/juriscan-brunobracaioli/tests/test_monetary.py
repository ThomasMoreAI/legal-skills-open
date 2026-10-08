"""Tests for scripts/utils/monetary.py"""

import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from utils.monetary import (
    normalize_brl,
    extract_monetary_values,
    format_brl,
    values_match,
    MonetaryValue,
)


class TestNormalizeBrl:
    def test_standard_format(self):
        assert normalize_brl('R$ 1.234,56') == pytest.approx(1234.56)

    def test_no_cents(self):
        assert normalize_brl('R$ 25.000') == pytest.approx(25000.0)

    def test_simple_value(self):
        assert normalize_brl('R$ 100,00') == pytest.approx(100.0)

    def test_large_value(self):
        assert normalize_brl('R$ 1.234.567,89') == pytest.approx(1234567.89)

    def test_no_spaces(self):
        assert normalize_brl('R$25.000,00') == pytest.approx(25000.0)

    def test_reais_suffix(self):
        assert normalize_brl('1.234,56 reais') == pytest.approx(1234.56)

    def test_multiplier_mil(self):
        assert normalize_brl('R$ 25 mil') == pytest.approx(25000.0)

    def test_multiplier_milhao(self):
        assert normalize_brl('R$ 1,5 milhão') == pytest.approx(1500000.0)

    def test_multiplier_milhoes(self):
        assert normalize_brl('R$ 2 milhões') == pytest.approx(2000000.0)

    def test_empty(self):
        assert normalize_brl('') is None

    def test_none(self):
        assert normalize_brl(None) is None  # type: ignore[arg-type]

    def test_garbage(self):
        assert normalize_brl('not a value') is None


class TestExtractMonetaryValues:
    def test_single_value(self):
        values = extract_monetary_values("O valor é R$ 25.000,00.")
        assert len(values) == 1
        assert values[0].normalized == pytest.approx(25000.0)

    def test_multiple_values(self):
        text = "Danos materiais R$ 18.500,00 e danos morais R$ 30.000,00."
        values = extract_monetary_values(text)
        assert len(values) == 2
        assert values[0].normalized == pytest.approx(18500.0)
        assert values[1].normalized == pytest.approx(30000.0)

    def test_context_captured(self):
        text = "A condenação total foi de R$ 48.500,00 entre materiais e morais."
        values = extract_monetary_values(text)
        assert len(values) == 1
        assert 'R$ 48.500,00' in values[0].context

    def test_multiplier_values(self):
        text = "Valor da causa: R$ 1,5 milhão."
        values = extract_monetary_values(text)
        assert len(values) >= 1
        has_million = any(v.normalized == pytest.approx(1500000.0) for v in values)
        assert has_million

    def test_no_values(self):
        assert extract_monetary_values("Sem valores monetários.") == []


class TestFormatBrl:
    def test_standard(self):
        assert format_brl(1234.56) == 'R$ 1.234,56'

    def test_large(self):
        result = format_brl(2000000.0)
        assert 'milhões' in result or '2.000.000' in result

    def test_zero(self):
        assert format_brl(0.0) == 'R$ 0,00'


class TestValuesMatch:
    def test_equal(self):
        assert values_match(25000.0, 25000.0) is True

    def test_close_enough(self):
        assert values_match(25000.0, 25000.005) is True

    def test_different(self):
        assert values_match(25000.0, 18500.0) is False

    def test_none_values(self):
        assert values_match(None, 25000.0) is False
        assert values_match(25000.0, None) is False
        assert values_match(None, None) is False
