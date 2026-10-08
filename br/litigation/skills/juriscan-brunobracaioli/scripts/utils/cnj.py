"""
cnj.py — CNJ process number parsing and validation.

Brazilian court process numbers follow the CNJ standard (Res. 65/2008):
NNNNNNN-DD.YYYY.J.TT.OOOO

Where:
- NNNNNNN: sequential number (7 digits)
- DD: check digits (2 digits)
- YYYY: distribution year (4 digits)
- J: justice branch (1 digit)
- TT: court (2 digits)
- OOOO: origin unit (4 digits)
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# CNJ format: 0000000-00.0000.0.00.0000
CNJ_PATTERN = re.compile(r'(\d{7})-(\d{2})\.(\d{4})\.(\d)\.(\d{2})\.(\d{4})')

# Also match without formatting: 00000000000000000000 (20 digits)
CNJ_RAW_PATTERN = re.compile(r'\b(\d{20})\b')

JUSTICE_BRANCHES = {
    1: 'Supremo Tribunal Federal',
    2: 'Conselho Nacional de Justiça',
    3: 'Superior Tribunal de Justiça',
    4: 'Justiça Federal',
    5: 'Justiça do Trabalho',
    6: 'Justiça Eleitoral',
    7: 'Justiça Militar da União',
    8: 'Justiça Estadual',
    9: 'Justiça Militar Estadual',
}

# Major state courts (justice branch 8)
STATE_COURTS = {
    26: 'TJSP', 19: 'TJRJ', 13: 'TJMG', 21: 'TJRS', 16: 'TJPR',
    24: 'TJSC', 5: 'TJBA', 17: 'TJPE', 6: 'TJCE', 9: 'TJGO',
    7: 'TJDF', 8: 'TJES', 10: 'TJMA', 14: 'TJPA', 15: 'TJPB',
    18: 'TJPI', 20: 'TJRN', 25: 'TJSE', 2: 'TJAL', 4: 'TJAM',
    3: 'TJAP', 11: 'TJMT', 12: 'TJMS', 22: 'TJRO', 23: 'TJRR',
    27: 'TJTO', 1: 'TJAC',
}

# Federal courts (justice branch 4)
FEDERAL_COURTS = {
    1: 'TRF1', 2: 'TRF2', 3: 'TRF3', 4: 'TRF4', 5: 'TRF5', 6: 'TRF6',
}


@dataclass
class CNJNumber:
    """Parsed CNJ process number."""
    raw: str
    sequential: str
    check_digits: str
    year: int
    justice_branch: int
    court: int
    origin: int
    branch_name: str
    court_name: str

    @property
    def formatted(self) -> str:
        """Return the formatted CNJ number."""
        return (
            f"{self.sequential}-{self.check_digits}."
            f"{self.year:04d}.{self.justice_branch}.{self.court:02d}.{self.origin:04d}"
        )


def _calculate_check_digits(sequential: int, year: int, branch: int, court: int, origin: int) -> int:
    """Calculate CNJ check digits per Res. 65/2008.

    The check digit algorithm uses modulo 97:
    remainder = NNNNNNN YYYY J TT OOOO 00 mod 97
    DD = 97 - remainder
    """
    # Build the number without check digits, with DD=00
    num = (
        sequential * 10**13
        + year * 10**9
        + branch * 10**8
        + court * 10**6
        + origin * 10**2
    )
    remainder = num % 97
    return 97 - remainder


def parse_cnj(text: str) -> CNJNumber | None:
    """Parse a CNJ process number from text.

    Accepts both formatted (0000000-00.0000.0.00.0000) and raw (20-digit) forms.
    Returns None if no valid CNJ number is found.
    """
    # Try formatted pattern first
    m = CNJ_PATTERN.search(text)
    if m:
        sequential, check, year, branch, court, origin = m.groups()
        branch_int = int(branch)
        court_int = int(court)

        branch_name = JUSTICE_BRANCHES.get(branch_int, f'Justiça {branch_int}')
        if branch_int == 8:
            court_name = STATE_COURTS.get(court_int, f'TJ-{court_int:02d}')
        elif branch_int == 4:
            court_name = FEDERAL_COURTS.get(court_int, f'TRF{court_int}')
        elif branch_int == 5:
            court_name = f'TRT{court_int}'
        else:
            court_name = branch_name

        return CNJNumber(
            raw=m.group(),
            sequential=sequential,
            check_digits=check,
            year=int(year),
            justice_branch=branch_int,
            court=court_int,
            origin=int(origin),
            branch_name=branch_name,
            court_name=court_name,
        )

    return None


def validate_cnj_check_digits(number: CNJNumber) -> bool:
    """Validate the check digits of a parsed CNJ number."""
    expected = _calculate_check_digits(
        int(number.sequential),
        number.year,
        number.justice_branch,
        number.court,
        number.origin,
    )
    return int(number.check_digits) == expected


def extract_cnj_numbers(text: str) -> list[CNJNumber]:
    """Extract all CNJ process numbers from text."""
    results = []
    seen: set[str] = set()
    for m in CNJ_PATTERN.finditer(text):
        cnj = parse_cnj(m.group())
        if cnj and cnj.formatted not in seen:
            seen.add(cnj.formatted)
            results.append(cnj)
    return results
