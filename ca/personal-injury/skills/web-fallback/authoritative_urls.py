"""
Authoritative-source URL builders, per jurisdiction.

Each entry maps a code prefix (matching the canonical form from
openclaw.skills.citation_format.normalize) to:
- a `build` callable: section-string → URL
- a `domain`: the expected domain on a successful fetch (used in result reporting)

ONLY government / legislature domains. No SEO blogs, no Wikipedia, no aggregators.

Adding a new jurisdiction:
1. Find the official legislature site for the state's vehicle code.
2. Inspect a real section URL — note the pattern.
3. Add an entry below.
4. Add a smoke test in tests/test_web_fallback.py (optional).

Failure mode: if a citation comes in with a code prefix we don't have,
verify() returns {"verified": false, "reason": "no authoritative URL pattern for <code>"}.
That's the correct behavior — refusing is better than fabricating.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass(frozen=True)
class UrlBuilder:
    domain: str
    build: Callable[[str], str]


def _ca_veh_code(section: str) -> str:
    # Examples:
    #   "22350"      -> .../sectionNum=22350.
    #   "23152(a)"   -> .../sectionNum=23152.
    base = section.split("(", 1)[0].strip()
    return (
        "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml"
        f"?lawCode=VEH&sectionNum={base}."
    )


def _tx_transp_code(section: str) -> str:
    # Texas uses chapter-then-section. e.g. "545.351" -> chapter 545.
    chapter = section.split(".", 1)[0].strip()
    return f"https://statutes.capitol.texas.gov/Docs/TN/htm/TN.{chapter}.htm"


def _ny_veh_traf(section: str) -> str:
    # NY VAT lookup by section.
    base = section.split("(", 1)[0].strip()
    return f"https://www.nysenate.gov/legislation/laws/VAT/{base}"


def _fl_stat(section: str) -> str:
    # Florida statutes. flsenate.gov serves clean per-section pages with
    # the section number echoed throughout the body. The legacy
    # leg.state.fl.us cfm URL returns a shell page that fails the anchor
    # check.
    base = section.split("(", 1)[0].strip()
    return f"https://www.flsenate.gov/Laws/Statutes/2024/{base}"


def _il_625_ilcs(section: str) -> str:
    # 625 ILCS 5/<section>. The user-facing form is usually "625 ILCS 5/11-501".
    # We don't try to parse the chapter/article split — point the user at the search.
    return f"https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=062500050K{section.strip()}"


# Canonical code prefix -> URL builder.
# Keys must match the canonical form produced by citation_format.normalize.
URL_BUILDERS: dict[str, UrlBuilder] = {
    "Cal. Veh. Code":         UrlBuilder("leginfo.legislature.ca.gov",  _ca_veh_code),
    "Tex. Transp. Code":      UrlBuilder("statutes.capitol.texas.gov",  _tx_transp_code),
    "N.Y. Veh. & Traf. Law":  UrlBuilder("nysenate.gov",                _ny_veh_traf),
    "Fla. Stat.":             UrlBuilder("flsenate.gov",                _fl_stat),
    "625 ILCS":               UrlBuilder("ilga.gov",                    _il_625_ilcs),
}


def build_url(code_prefix: str, section: str) -> Optional[tuple[str, str]]:
    """
    Returns (url, domain) for a known code prefix, or None if unsupported.
    """
    builder = URL_BUILDERS.get(code_prefix)
    if not builder:
        return None
    return builder.build(section), builder.domain


def supported_codes() -> list[str]:
    return sorted(URL_BUILDERS.keys())
