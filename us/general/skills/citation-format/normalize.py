"""
Normalize messy citation strings to canonical form.

Hackathon-scope: focused on motor-vehicle statutes (state vehicle codes).
We handle the common variants users / judges will type. Not a full Bluebook.

Canonical form:
    Cal. Veh. Code § 23152(a)
    Tex. Transp. Code § 545.351
    N.Y. Veh. & Traf. Law § 1192(2)

Strategy:
1. Detect the jurisdiction prefix (or accept that the input gives only a section).
2. Pull out the section + subsection.
3. Reassemble in canonical form.

Returns the input unchanged if it can't be confidently normalized — better to
let the Harvester miss than to silently rewrite into the wrong canonical form.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

SECTION_SIGN = "\u00a7"  # §

# Map of (lowercase user-input prefix) → canonical code prefix.
# Order matters: longer/more specific patterns first.
PREFIX_MAP: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bcal(?:\.|ifornia)?\s*veh(?:\.|icle)?\s*(?:code)?\b", re.I),  "Cal. Veh. Code"),
    (re.compile(r"\bcvc\b", re.I),                                          "Cal. Veh. Code"),
    (re.compile(r"\btex(?:\.|as)?\s*transp(?:\.|ortation)?\s*code\b", re.I), "Tex. Transp. Code"),
    (re.compile(r"\bttc\b", re.I),                                          "Tex. Transp. Code"),
    (re.compile(r"\bn\.?y\.?\s*veh(?:\.|icle)?\s*&?\s*traf(?:\.|fic)?\s*law\b", re.I),
                                                                            "N.Y. Veh. & Traf. Law"),
    (re.compile(r"\bfla?\.?(?:orida)?\s*stat(?:\.|utes?)?\b", re.I),        "Fla. Stat."),
    (re.compile(r"\b625\s*ilcs\b", re.I),                                   "625 ILCS"),  # Illinois Vehicle Code
]


@dataclass
class ParsedCitation:
    code_prefix: Optional[str]   # e.g. "Cal. Veh. Code" — None if unknown / ambiguous
    section: str                 # e.g. "23152(a)"
    raw: str

    def canonical(self) -> Optional[str]:
        if not self.code_prefix:
            return None
        return f"{self.code_prefix} {SECTION_SIGN} {self.section}"


def _extract_section(s: str) -> Optional[str]:
    """
    Pull out the section + optional subsections from a citation string.

    Accepts:
        "23152(a)"          → "23152(a)"
        "23152 a"           → "23152(a)"
        "23152a"            → "23152(a)"
        "545.351"           → "545.351"
        "1192(2)(b)"        → "1192(2)(b)"
    Returns None if no sane section can be extracted.
    """
    # Find a number (with optional dots), then capture trailing subsection markers.
    m = re.search(
        r"""
        (\d+(?:\.\d+)*)                       # base section (with dotted numerics)
        (                                     # optional subsection cluster
            (?:                               # one or more of:
                \s*\(\s*[a-z0-9]+\s*\)        #   "(a)" / "(2)"
                |
                \s*[a-z]                      #   bare trailing letter (e.g. "23152a")
            )+
        )?
        """,
        s,
        re.I | re.X,
    )
    if not m:
        return None

    base = m.group(1)
    tail = (m.group(2) or "").strip()
    if not tail:
        return base

    # Convert bare-letter form to (letter): "23152a" → "23152(a)"
    parts = re.findall(r"\(\s*([a-z0-9]+)\s*\)|([a-z])", tail, re.I)
    pieces: list[str] = []
    for paren, bare in parts:
        token = (paren or bare).strip().lower()
        if token:
            pieces.append(f"({token})")
    return base + "".join(pieces)


def parse(citation: str) -> ParsedCitation:
    """Best-effort parse. Always returns a ParsedCitation; .canonical() is None on miss."""
    raw = citation.strip()

    # Strip a section sign if present, plus the word "section"/"sec."
    cleaned = raw.replace(SECTION_SIGN, " ")
    cleaned = re.sub(r"\bsec(?:t(?:ion)?)?\.?\b", " ", cleaned, flags=re.I)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()

    # Detect a known prefix
    code_prefix: Optional[str] = None
    for pat, canonical in PREFIX_MAP:
        if pat.search(cleaned):
            code_prefix = canonical
            cleaned = pat.sub("", cleaned, count=1).strip()
            break

    section = _extract_section(cleaned)
    if not section:
        return ParsedCitation(code_prefix=code_prefix, section="", raw=raw)

    return ParsedCitation(code_prefix=code_prefix, section=section, raw=raw)


def normalize(citation: str, *, default_jurisdiction: Optional[str] = None) -> str:
    """
    Normalize a citation to canonical form. Idempotent.

    If `default_jurisdiction` is provided (e.g. "California") and the input has
    no detectable code prefix, we'll fill it in. Otherwise the section-only
    input is returned unchanged — caller should ask the user for jurisdiction.
    """
    parsed = parse(citation)

    # Already canonical with a known prefix — use it as-is.
    canonical = parsed.canonical()
    if canonical:
        return canonical

    # No prefix detected. Fall back to default if given.
    if not parsed.code_prefix and default_jurisdiction and parsed.section:
        prefix_for_default = _DEFAULTS.get(default_jurisdiction.lower())
        if prefix_for_default:
            return f"{prefix_for_default} {SECTION_SIGN} {parsed.section}"

    # Couldn't safely normalize — return input unchanged.
    return citation.strip()


_DEFAULTS: dict[str, str] = {
    "california": "Cal. Veh. Code",
    "ca": "Cal. Veh. Code",
    "texas": "Tex. Transp. Code",
    "tx": "Tex. Transp. Code",
    "new york": "N.Y. Veh. & Traf. Law",
    "ny": "N.Y. Veh. & Traf. Law",
    "florida": "Fla. Stat.",
    "fl": "Fla. Stat.",
    "illinois": "625 ILCS",
    "il": "625 ILCS",
}


if __name__ == "__main__":
    import sys
    samples = sys.argv[1:] or [
        "Cal. Veh. Code § 23152(a)",
        "CVC 23152(a)",
        "CVC 23152a",
        "California Vehicle Code Section 23152(a)",
        "cal veh § 23152(a)",
        "Tex. Transp. Code § 545.351",
        "TTC 545.351",
        "23152(a)",
    ]
    for s in samples:
        print(f"{s!r:50} → {normalize(s)!r}")
