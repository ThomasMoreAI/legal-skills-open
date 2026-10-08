#!/usr/bin/env python3
"""
prazo_calculator.py — CPC-compliant procedural deadline calculator.

Implements CPC Art. 219-232 rules:
- Business day counting (Art. 219)
- Start/end rules (Art. 224)
- Court holidays (forense) + state holidays
- Recesso forense (Art. 220): Dec 20 - Jan 20
- Suspension ranges

Usage:
    python3 prazo_calculator.py --analysis analyzed.json --output prazos.json
    python3 prazo_calculator.py --date 2025-03-15 --tipo contestação --state SP
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import unicodedata
from datetime import date, timedelta
from typing import Literal


def _strip_accents(s: str) -> str:
    """Remove diacritics from a string while preserving the base characters."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.combining(c) == 0
    )

REFERENCES_DIR = os.path.join(os.path.dirname(__file__), '..', 'references')


def _easter(year: int) -> date:
    """Calculate Easter Sunday using Butcher/Meeus algorithm."""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return date(year, month, day)


def load_feriados(state: str | None = None, year: int | None = None) -> set[date]:
    """Load court holidays for a given year (defaults to current year).

    Includes: national fixed + mobile (Easter-based) + optional state holidays.
    """
    if year is None:
        year = date.today().year

    feriados_path = os.path.join(REFERENCES_DIR, 'feriados_forenses.json')
    with open(feriados_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    holidays: set[date] = set()

    # National fixed holidays
    for h in data.get('nacionais_fixos', []):
        try:
            holidays.add(date(year, h['mes'], h['dia']))
        except ValueError:
            continue

    # Mobile holidays (Easter-based)
    easter = _easter(year)
    offsets = data.get('moveis', {}).get('offsets_from_easter', {})
    for name, offset in offsets.items():
        holidays.add(easter + timedelta(days=offset))

    # State holidays
    if state:
        state_holidays = data.get('estaduais', {}).get(state.upper(), [])
        for h in state_holidays:
            try:
                holidays.add(date(year, h['mes'], h['dia']))
            except ValueError:
                continue

    return holidays


def is_recesso(d: date) -> bool:
    """Check if a date falls within the recesso forense (CPC Art. 220).

    Recesso: Dec 20 to Jan 20 (inclusive).
    """
    if d.month == 12 and d.day >= 20:
        return True
    if d.month == 1 and d.day <= 20:
        return True
    return False


def is_business_day(d: date, feriados: set[date]) -> bool:
    """Check if a date is a business day (dia útil forense)."""
    if d.weekday() >= 5:  # Saturday or Sunday
        return False
    if d in feriados:
        return False
    if is_recesso(d):
        return False
    return True


def next_business_day(d: date, feriados: set[date]) -> date:
    """Find the next business day on or after the given date.

    CPC Art. 224 §1: if deadline falls on non-business day, extends to next business day.
    """
    while not is_business_day(d, feriados):
        d += timedelta(days=1)
    return d


def calculate_prazo(
    start_date: date,
    days: int,
    unit: Literal['úteis', 'corridos'] = 'úteis',
    feriados: set[date] | None = None,
    suspended_ranges: list[tuple[date, date]] | None = None,
) -> date:
    """Calculate procedural deadline per CPC rules.

    CPC Art. 224: Exclude start day, include end day.
    CPC Art. 219: Count only business days (for 'úteis').
    CPC Art. 224 §1: If deadline falls on non-business day, extend to next business day.

    Args:
        start_date: Date of intimation/publication (dia do começo — excluded).
        days: Number of days for the deadline.
        unit: 'úteis' (business days) or 'corridos' (calendar days).
        feriados: Set of holiday dates.
        suspended_ranges: List of (start, end) suspension periods.
    """
    if feriados is None:
        feriados = set()

    def is_suspended(d: date) -> bool:
        if suspended_ranges:
            return any(start <= d <= end for start, end in suspended_ranges)
        return False

    current = start_date
    counted = 0

    if unit == 'úteis':
        while counted < days:
            current += timedelta(days=1)
            if is_suspended(current):
                continue
            if is_business_day(current, feriados):
                counted += 1
    else:  # corridos
        while counted < days:
            current += timedelta(days=1)
            if is_suspended(current):
                continue
            counted += 1
        # Even for corridos, deadline must end on business day
        current = next_business_day(current, feriados)

    return current


def get_standard_prazo(tipo: str) -> dict | None:
    """Look up the standard CPC deadline for a procedural act."""
    prazos_path = os.path.join(REFERENCES_DIR, 'cpc_prazos.json')
    with open(prazos_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tipo_normalized = _strip_accents(tipo.lower().strip().replace(' ', '_'))

    for prazo in data.get('prazos_legais', []):
        if _strip_accents(prazo['ato']) == tipo_normalized:
            return prazo

    # Fuzzy match
    for prazo in data.get('prazos_legais', []):
        ato_normalized = _strip_accents(prazo['ato'])
        if tipo_normalized in ato_normalized or ato_normalized in tipo_normalized:
            return prazo

    return None


VALID_PROCESS_STATES = {
    "ativo",
    "transito_em_julgado",
    "suspenso",
    "arquivado",
    "desconhecido",
}

# Phase 5 Step 5.2 — state-aware behaviour
# When the process has already transited in rem judicatam, recursal deadlines
# are meaningless; only the voluntary compliance deadline (CPC art. 523) is
# relevant. When the process is suspended, all deadlines are frozen. When it
# is archived, nothing is computed.

_CUMPRIMENTO_VOLUNTARIO = {
    "dias": 15,
    "unidade": "dias úteis",
    "fundamento": "CPC art. 523 — cumprimento voluntário da sentença",
    "tipo": "cumprimento voluntário",
}


def check_prazo_status(
    intimation_date: date,
    prazo_type: str,
    current_date: date | None = None,
    state: str | None = None,
    process_state: str | None = None,
) -> dict | None:
    """Check the status of a procedural deadline.

    Returns dict with deadline, days_remaining, and status.

    Phase 5 Step 5.2: when ``process_state`` is provided, recursal deadlines
    are computed only when the process is 'ativo' or 'desconhecido'. For
    'transito_em_julgado', only the voluntary compliance deadline (CPC
    art. 523) is computed regardless of ``prazo_type``. For 'suspenso' all
    deadlines are marked suspended. For 'arquivado' nothing is returned.
    """
    if current_date is None:
        current_date = date.today()

    # --- Phase 5.2 gate ---
    if process_state is not None:
        if process_state not in VALID_PROCESS_STATES:
            raise ValueError(
                f"invalid process_state: {process_state!r} "
                f"(expected one of {sorted(VALID_PROCESS_STATES)})"
            )
        if process_state == "arquivado":
            return None
        if process_state == "suspenso":
            return {
                "tipo": prazo_type,
                "status": "suspenso",
                "data_intimacao": intimation_date.isoformat(),
                "fundamento_legal": "processo suspenso — prazos paralisados",
                "process_state": process_state,
            }
        if process_state == "transito_em_julgado":
            # Recursal deadlines are no longer valid; switch to CPC 523.
            feriados = load_feriados(state, intimation_date.year)
            if intimation_date.year != current_date.year:
                feriados |= load_feriados(state, current_date.year)
            deadline = calculate_prazo(
                start_date=intimation_date,
                days=_CUMPRIMENTO_VOLUNTARIO["dias"],
                unit=_CUMPRIMENTO_VOLUNTARIO["unidade"],
                feriados=feriados,
            )
            if current_date > deadline:
                status = "vencido"
            elif current_date == deadline:
                status = "ultimo_dia"
            else:
                status = "em_prazo"
            return {
                "tipo": _CUMPRIMENTO_VOLUNTARIO["tipo"],
                "fundamento_legal": _CUMPRIMENTO_VOLUNTARIO["fundamento"],
                "data_intimacao": intimation_date.isoformat(),
                "data_limite": deadline.isoformat(),
                "dias": _CUMPRIMENTO_VOLUNTARIO["dias"],
                "unidade": _CUMPRIMENTO_VOLUNTARIO["unidade"],
                "status": status,
                "process_state": process_state,
                "note": (
                    f"prazo recursal {prazo_type!r} ignorado porque o processo "
                    f"já transitou em julgado; computado apenas o prazo de "
                    f"cumprimento voluntário (CPC art. 523)."
                ),
            }
        # "ativo" or "desconhecido" -> fall through to normal calculation

    prazo_info = get_standard_prazo(prazo_type)
    if not prazo_info:
        return None

    # Load holidays for both the intimation year and deadline year
    feriados = load_feriados(state, intimation_date.year)
    if intimation_date.year != current_date.year:
        feriados |= load_feriados(state, current_date.year)

    deadline = calculate_prazo(
        start_date=intimation_date,
        days=prazo_info['dias'],
        unit=prazo_info['unidade'],
        feriados=feriados,
    )

    days_remaining = None
    if current_date <= deadline:
        # Count business days remaining
        d = current_date
        count = 0
        while d < deadline:
            d += timedelta(days=1)
            if is_business_day(d, feriados):
                count += 1
        days_remaining = count

    if current_date > deadline:
        status = 'vencido'
    elif current_date == deadline:
        status = 'ultimo_dia'
    else:
        status = 'em_prazo'

    result = {
        'tipo': prazo_type,
        'fundamento_legal': prazo_info['fundamento'],
        'data_intimacao': intimation_date.isoformat(),
        'data_limite': deadline.isoformat(),
        'dias': prazo_info['dias'],
        'unidade': prazo_info['unidade'],
        'status': status,
        'dias_restantes': days_remaining,
    }
    if process_state is not None:
        result['process_state'] = process_state
    return result


def main():
    parser = argparse.ArgumentParser(description='CPC Prazo Calculator')
    parser.add_argument('--date', '-d', help='Intimation date (YYYY-MM-DD)')
    parser.add_argument('--tipo', '-t', help='Prazo type (e.g., contestação, apelação)')
    parser.add_argument('--state', '-s', help='State for holidays (e.g., SP, RJ)')
    parser.add_argument('--analysis', '-a', help='Path to analyzed.json for batch calculation')
    parser.add_argument('--output', '-o', help='Output path for prazos.json')
    args = parser.parse_args()

    if args.date and args.tipo:
        # Single calculation mode
        intimation = date.fromisoformat(args.date)
        result = check_prazo_status(intimation, args.tipo, state=args.state)
        if result:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"[ERROR] Unknown prazo type: {args.tipo}", file=sys.stderr)
            sys.exit(1)
    elif args.analysis:
        # Batch mode from analyzed.json
        with open(args.analysis, 'r', encoding='utf-8') as f:
            analysis = json.load(f)

        from utils.dates import parse_brazilian_date

        prazos = []
        unknown_tipo = 0
        unparseable_date = 0
        missing_start = 0
        seen_any = False
        for ci, chunk in enumerate(analysis.get('chunks', [])):
            for pj, prazo in enumerate(chunk.get('prazos', [])):
                seen_any = True
                tipo = prazo.get('tipo', '')
                start = prazo.get('data_inicio')
                if not start:
                    missing_start += 1
                    print(
                        f"WARN: chunk[{ci}].prazos[{pj}] tipo={tipo!r} sem data_inicio — pulando",
                        file=sys.stderr,
                    )
                    continue
                d = parse_brazilian_date(start)
                if not d:
                    unparseable_date += 1
                    print(
                        f"WARN: chunk[{ci}].prazos[{pj}] data_inicio={start!r} não parseável — pulando",
                        file=sys.stderr,
                    )
                    continue
                result = check_prazo_status(d, tipo, state=args.state)
                if result is None:
                    unknown_tipo += 1
                    print(
                        f"WARN: chunk[{ci}].prazos[{pj}] tipo={tipo!r} não reconhecido — pulando",
                        file=sys.stderr,
                    )
                    continue
                prazos.append(result)

        output_path = args.output or os.path.join(os.path.dirname(args.analysis), 'prazos.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(prazos, f, ensure_ascii=False, indent=2)

        dropped = unknown_tipo + unparseable_date + missing_start
        if dropped > 0:
            print(
                f"WARN: {dropped} prazo(s) descartado(s) "
                f"(tipo desconhecido: {unknown_tipo}, "
                f"data não parseável: {unparseable_date}, "
                f"sem data_inicio: {missing_start})",
                file=sys.stderr,
            )
        print(f"Calculated {len(prazos)} deadline(s). Output: {output_path}")

        if seen_any and len(prazos) == 0:
            # Input had prazos but everything was dropped — likely upstream bug
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
