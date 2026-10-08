"""
dates.py — Robust Brazilian date parsing and chronology validation.

Handles DD/MM/YYYY, written Portuguese dates, ISO 8601, and piece-type-aware
primary date extraction.
"""

from __future__ import annotations

import re
from datetime import date, datetime

MONTH_NAMES = {
    'janeiro': 1, 'fevereiro': 2, 'março': 3, 'marco': 3, 'abril': 4,
    'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8,
    'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12,
    'jan': 1, 'fev': 2, 'mar': 3, 'abr': 4, 'mai': 5, 'jun': 6,
    'jul': 7, 'ago': 8, 'set': 9, 'out': 10, 'nov': 11, 'dez': 12,
}

# Regex patterns ordered by specificity
_WRITTEN_DATE = re.compile(
    r'(\d{1,2})\s+de\s+(janeiro|fevereiro|março|marco|abril|maio|junho|'
    r'julho|agosto|setembro|outubro|novembro|dezembro)\s+de\s+(\d{4})',
    re.IGNORECASE,
)
_NUMERIC_DMY = re.compile(r'(\d{2})[/.-](\d{2})[/.-](\d{4})')
_ISO_DATE = re.compile(r'(\d{4})-(\d{2})-(\d{2})')

# Piece-type-specific date markers (searched in order of priority)
_PRIMARY_DATE_MARKERS: dict[str, list[str]] = {
    'SENTENÇA': [
        r'(?i)Publique-se[.\s]*(\d{1,2}[/.-]\d{2}[/.-]\d{4})',
        r'(?i)(?:São\s+Paulo|.{3,40}),?\s+(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})',
    ],
    'ACÓRDÃO': [
        r'(?i)(?:Sessão|Julgamento)\s+(?:de|em|realizada?\s+em)\s+(\d{1,2}[/.-]\d{2}[/.-]\d{4})',
        r'(?i)(?:Sessão|Julgamento)\s+(?:de|em)\s+(\d{1,2})\s+de\s+(\w+)\s+de\s+(\d{4})',
    ],
    'PETIÇÃO INICIAL': [
        r'(?i)Protocolo[:\s]+.*?(\d{2}[/.-]\d{2}[/.-]\d{4})',
    ],
}


def parse_brazilian_date(text: str) -> date | None:
    """Parse a single date string in any common Brazilian format.

    Supports:
    - DD/MM/YYYY, DD.MM.YYYY, DD-MM-YYYY
    - 'D de Month de YYYY'
    - YYYY-MM-DD (ISO 8601)

    Returns None if parsing fails or date is invalid.
    """
    text = text.strip()

    # Written Portuguese date
    m = _WRITTEN_DATE.search(text)
    if m:
        day, month_name, year = m.groups()
        month = MONTH_NAMES.get(month_name.lower())
        if month:
            try:
                return date(int(year), month, int(day))
            except ValueError:
                pass

    # Numeric DD/MM/YYYY
    m = _NUMERIC_DMY.search(text)
    if m:
        day, month, year = m.groups()
        try:
            d = date(int(year), int(month), int(day))
            if 1900 <= d.year <= 2100:
                return d
        except ValueError:
            pass

    # ISO 8601
    m = _ISO_DATE.search(text)
    if m:
        year, month, day = m.groups()
        try:
            d = date(int(year), int(month), int(day))
            if 1900 <= d.year <= 2100:
                return d
        except ValueError:
            pass

    return None


def extract_all_dates(text: str) -> list[dict]:
    """Extract ALL dates from the entire text.

    Returns list of:
        {raw: str, parsed: date, char_position: int, context: str}

    Context includes 40 chars before and after for grounding.
    """
    results = []
    seen_positions: set[int] = set()

    # Written dates
    for m in _WRITTEN_DATE.finditer(text):
        day, month_name, year = m.groups()
        month = MONTH_NAMES.get(month_name.lower())
        if not month:
            continue
        try:
            d = date(int(year), month, int(day))
        except ValueError:
            continue
        if 1900 <= d.year <= 2100 and m.start() not in seen_positions:
            seen_positions.add(m.start())
            ctx_start = max(0, m.start() - 40)
            ctx_end = min(len(text), m.end() + 40)
            results.append({
                'raw': m.group(),
                'parsed': d,
                'char_position': m.start(),
                'context': text[ctx_start:ctx_end].replace('\n', ' ').strip(),
            })

    # Numeric DD/MM/YYYY
    for m in _NUMERIC_DMY.finditer(text):
        if m.start() in seen_positions:
            continue
        day, month, year = m.groups()
        try:
            d = date(int(year), int(month), int(day))
        except ValueError:
            continue
        if 1900 <= d.year <= 2100:
            seen_positions.add(m.start())
            ctx_start = max(0, m.start() - 40)
            ctx_end = min(len(text), m.end() + 40)
            results.append({
                'raw': m.group(),
                'parsed': d,
                'char_position': m.start(),
                'context': text[ctx_start:ctx_end].replace('\n', ' ').strip(),
            })

    results.sort(key=lambda x: x['char_position'])
    return results


def find_primary_date(text: str, piece_type: str) -> dict | None:
    """Extract the most relevant date for a given piece type.

    Uses piece-type-specific markers first, then falls back to the first date
    found in the text.
    """
    # Try type-specific markers
    markers = _PRIMARY_DATE_MARKERS.get(piece_type, [])
    for pattern in markers:
        m = re.search(pattern, text[:5000])
        if m:
            groups = m.groups()
            # Single-group patterns capture a numeric date
            if len(groups) == 1:
                d = parse_brazilian_date(groups[0])
                if d:
                    return {'parsed': d, 'raw': groups[0], 'source': 'marker'}
            # Three-group patterns capture day/month_name/year
            elif len(groups) == 3:
                raw = f"{groups[0]} de {groups[1]} de {groups[2]}"
                d = parse_brazilian_date(raw)
                if d:
                    return {'parsed': d, 'raw': raw, 'source': 'marker'}

    # Fallback: first date in the text
    all_dates = extract_all_dates(text[:5000])
    if all_dates:
        first = all_dates[0]
        return {'parsed': first['parsed'], 'raw': first['raw'], 'source': 'first_in_text'}

    return None


def validate_chronology(chunks: list[dict]) -> list[dict]:
    """Check that piece dates follow logical procedural order.

    Returns list of anomalies found.
    """
    # Expected order: pieces that should come before others
    ORDER_RULES = [
        ('PETIÇÃO INICIAL', 'CONTESTAÇÃO', 'Contestação datada antes da Petição Inicial'),
        ('CONTESTAÇÃO', 'RÉPLICA', 'Réplica datada antes da Contestação'),
        ('RÉPLICA', 'SENTENÇA', 'Sentença datada antes da Réplica'),
        ('SENTENÇA', 'APELAÇÃO', 'Apelação datada antes da Sentença'),
        ('APELAÇÃO', 'CONTRARRAZÕES', 'Contrarrazões datadas antes da Apelação'),
        ('APELAÇÃO', 'ACÓRDÃO', 'Acórdão datado antes da Apelação'),
        ('SENTENÇA', 'EMBARGOS', 'Embargos datados antes da Sentença'),
        ('SENTENÇA', 'CUMPRIMENTO DE SENTENÇA', 'Cumprimento datado antes da Sentença'),
    ]

    # Build date map from chunks
    chunk_dates: dict[str, date] = {}
    for c in chunks:
        label = c.get('label', '')
        primary = c.get('primary_date')
        if primary:
            if isinstance(primary, str):
                d = parse_brazilian_date(primary)
            elif isinstance(primary, date):
                d = primary
            else:
                continue
            if d:
                chunk_dates[label] = d

    anomalies = []
    for before_label, after_label, description in ORDER_RULES:
        d_before = chunk_dates.get(before_label)
        d_after = chunk_dates.get(after_label)
        if d_before and d_after and d_after < d_before:
            anomalies.append({
                'tipo': 'DATA_CONFLITANTE',
                'pecas': [before_label, after_label],
                'descricao': description,
                'data_antes': d_before.isoformat(),
                'data_depois': d_after.isoformat(),
            })

    return anomalies


def format_date_br(d: date) -> str:
    """Format date as DD/MM/YYYY for display."""
    return d.strftime('%d/%m/%Y')


def format_date_iso(d: date) -> str:
    """Format date as ISO 8601."""
    return d.isoformat()
