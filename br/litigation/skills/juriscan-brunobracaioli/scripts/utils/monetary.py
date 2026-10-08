"""
monetary.py — Brazilian Real (BRL) monetary value extraction and normalization.

Handles:
- R$ 1.234,56
- 1.234,56 reais
- Written forms: "cem mil reais", "1 milhão"
- Comparison and normalization for contradiction detection
"""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class MonetaryValue:
    """A parsed monetary value with its original text."""
    raw: str
    normalized: float | None
    char_position: int = 0
    context: str = ''

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MonetaryValue):
            return NotImplemented
        if self.normalized is None or other.normalized is None:
            return False
        return abs(self.normalized - other.normalized) < 0.01

    def __repr__(self) -> str:
        return f"MonetaryValue(raw={self.raw!r}, normalized={self.normalized})"


# Patterns for monetary value extraction
_BRL_PATTERNS = [
    # R$ 1.234.567,89 or R$1234,56
    re.compile(r'R\$\s*[\d]+(?:\.[\d]{3})*(?:,[\d]{1,2})?'),
    # 1.234,56 reais (requires "reais" suffix)
    re.compile(r'[\d]+(?:\.[\d]{3})*,[\d]{2}\s*reais', re.IGNORECASE),
]

# Multiplier words
_MULTIPLIERS = {
    'mil': 1_000,
    'milhão': 1_000_000,
    'milhões': 1_000_000,
    'bilhão': 1_000_000_000,
    'bilhões': 1_000_000_000,
}

_MULTIPLIER_PATTERN = re.compile(
    r'R\$\s*([\d]+(?:[.,]\d+)?)\s*(bilhões|bilhão|milhões|milhão|mil)',
    re.IGNORECASE,
)


def normalize_brl(value_str: str) -> float | None:
    """Normalize a BRL monetary string to a float.

    Handles Brazilian number format: dots as thousands separator, comma as decimal.
    Examples:
        "R$ 1.234,56" -> 1234.56
        "R$ 100.000,00" -> 100000.0
        "R$1234" -> 1234.0
        "1.234,56 reais" -> 1234.56
    """
    if not value_str:
        return None

    # Check for multiplier pattern first: "R$ 1,5 milhão"
    m = _MULTIPLIER_PATTERN.search(value_str)
    if m:
        num_str, mult_word = m.groups()
        num_str = num_str.replace(',', '.')
        try:
            base = float(num_str)
            multiplier = _MULTIPLIERS.get(mult_word.lower(), 1)
            return base * multiplier
        except ValueError:
            pass

    # Strip currency symbol, whitespace
    cleaned = re.sub(r'[R$\s]', '', value_str)
    cleaned = re.sub(r'\s*reais\s*$', '', cleaned, flags=re.IGNORECASE)

    if not cleaned:
        return None

    # Brazilian format: 1.234.567,89
    # Remove dots (thousands separator), replace comma (decimal)
    if ',' in cleaned:
        cleaned = cleaned.replace('.', '').replace(',', '.')
    else:
        # No comma: might be "1.234.567" (integer with thousands) or "1234567"
        # If dots are present and pattern is thousands-style, remove them
        parts = cleaned.split('.')
        if len(parts) > 1 and all(len(p) == 3 for p in parts[1:]):
            cleaned = cleaned.replace('.', '')

    try:
        return float(cleaned)
    except ValueError:
        return None


def extract_monetary_values(text: str) -> list[MonetaryValue]:
    """Extract all monetary values from text.

    Returns list of MonetaryValue with position and context for grounding.
    """
    results: list[MonetaryValue] = []
    seen_positions: set[int] = set()

    # Multiplier patterns first (more specific)
    for m in _MULTIPLIER_PATTERN.finditer(text):
        if m.start() in seen_positions:
            continue
        seen_positions.add(m.start())
        raw = m.group().strip()
        ctx_start = max(0, m.start() - 40)
        ctx_end = min(len(text), m.end() + 40)
        results.append(MonetaryValue(
            raw=raw,
            normalized=normalize_brl(raw),
            char_position=m.start(),
            context=text[ctx_start:ctx_end].replace('\n', ' ').strip(),
        ))

    # Standard patterns
    for pattern in _BRL_PATTERNS:
        for m in pattern.finditer(text):
            if m.start() in seen_positions:
                continue
            seen_positions.add(m.start())
            raw = m.group().strip()
            ctx_start = max(0, m.start() - 40)
            ctx_end = min(len(text), m.end() + 40)
            results.append(MonetaryValue(
                raw=raw,
                normalized=normalize_brl(raw),
                char_position=m.start(),
                context=text[ctx_start:ctx_end].replace('\n', ' ').strip(),
            ))

    results.sort(key=lambda x: x.char_position)
    return results


def format_brl(value: float) -> str:
    """Format a float as BRL display string: R$ 1.234,56"""
    if value >= 1_000_000_000:
        return f"R$ {value / 1_000_000_000:,.2f} bilhões".replace(',', 'X').replace('.', ',').replace('X', '.')
    if value >= 1_000_000:
        return f"R$ {value / 1_000_000:,.2f} milhões".replace(',', 'X').replace('.', ',').replace('X', '.')

    # Standard format
    formatted = f"{value:,.2f}"
    # Swap . and , for Brazilian format
    formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
    return f"R$ {formatted}"


def values_match(a: float | None, b: float | None, tolerance: float = 0.01) -> bool:
    """Check if two monetary values are effectively equal."""
    if a is None or b is None:
        return False
    return abs(a - b) < tolerance
