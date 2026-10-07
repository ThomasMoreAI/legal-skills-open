"""
Fetch + verify a citation against an authoritative legislature source.

The five rules of no-fabrication:

1. URL is built from `authoritative_urls.URL_BUILDERS` — never from a model.
2. Fetched page must contain the section number literally before we cite it
   (anchor check). This catches "section not found" pages that return HTTP 200.
3. Domain in the response must match the expected authoritative domain.
4. Failed fetches return a structured miss with a reason — never a guess.
5. We don't pass anything but the verified text to downstream summarization.

Pure I/O + parsing here. Summarization (which calls a model) lives in summarize.py
so this verifier has no LLM dependency and is easy to unit-test.
"""
from __future__ import annotations

import datetime as dt
import re
import warnings
from typing import Any, Optional
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup

# leginfo serves XHTML; bs4's heuristic warns when an HTML parser sees XML.
# We deliberately want HTML-style get_text() either way.
try:
    from bs4 import XMLParsedAsHTMLWarning
    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
except ImportError:
    pass

from openclaw.skills.citation_format.normalize import parse as parse_citation
from openclaw.skills.web_fallback.authoritative_urls import build_url, supported_codes

# leginfo and several state sites are friendlier to a real-browser UA.
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) SpecterWebFallback/0.1 Safari/605.1.15"
)
DEFAULT_TIMEOUT = 15.0
MIN_TEXT_CHARS = 60   # smell-test: a real statute returns more than this
MAX_TEXT_CHARS = 8000 # cap so we don't ship a whole code chapter to Claude


def _now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def _miss(citation: str, reason: str, **extra: Any) -> dict[str, Any]:
    out: dict[str, Any] = {"verified": False, "citation": citation, "reason": reason}
    out.update(extra)
    return out


def _extract_text(html: str) -> str:
    """Pull the main statute text out of a page. Crude on purpose — we're not
    parsing structure, we're just getting visible text the model can summarize.

    Note: we deliberately do NOT strip <form> elements. leginfo.legislature.ca.gov
    wraps the statute body inside a <form> for JSF reasons; stripping forms loses
    the entire payload.
    """
    soup = BeautifulSoup(html, "lxml")
    # Drop scripts/styles only. Preserve forms (leginfo wraps statute body in one)
    # and headers/nav (some sites embed the statute heading there).
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    # Collapse runs of blank lines.
    text = re.sub(r"\n{2,}", "\n\n", text)
    return text


def _anchor_ok(text: str, section: str) -> bool:
    """
    Anchor check: is the section number literally on the page in a way that
    suggests the page actually rendered the statute (vs the legislature's
    "section not found" shell, which echoes whatever section you asked for
    in the page title)?

    We require the bare section to appear as a whole token. That alone is
    necessary but not sufficient — see _structure_ok for the second check.
    """
    base = section.split("(", 1)[0].strip()
    if not base:
        return False
    pattern = re.compile(rf"(?<!\d){re.escape(base)}(?!\d)")
    return bool(pattern.search(text))


def _structure_ok(html: str, section: str, domain: str = "") -> bool:
    """
    Per-domain structural smell check on the raw HTML.

    leginfo.legislature.ca.gov has a specific "section not found" failure mode
    where the page returns 200 with the section number echoed in the title chrome
    but lacks the actual statute body. The leginfo strict check requires both
    a code-hierarchy heading (DIVISION/CHAPTER/ARTICLE) AND the section number
    in a heading. Other state legislature sites structure their pages
    differently (e.g., flsenate.gov has only generic site headings) and would
    fail that check on real, valid statute pages.

    Strategy:
      * For leginfo: keep the strict check.
      * For everything else: a lighter check — the section number must appear
        somewhere on the page AND the page must have substantive body content.
        The anchor + MIN_TEXT_CHARS checks the caller already runs cover that
        case, so we just return True here.

    If we add per-domain false-positive failure modes for new sources, encode
    them as additional branches here.
    """
    base = section.split("(", 1)[0].strip()

    if "leginfo.legislature.ca.gov" in domain.lower():
        # leginfo strict mode
        headings: list[str] = []
        for m in re.finditer(r"<h\d[^>]*>(.*?)</h\d>", html, re.S | re.I):
            inner = re.sub(r"<[^>]+>", "", m.group(1)).strip()
            if inner:
                headings.append(inner)
        if not headings:
            return True
        has_hierarchy = any(
            re.search(r"\b(DIVISION|CHAPTER|ARTICLE|TITLE|PART|SUBCHAPTER|SUBPART)\b",
                      h, re.I)
            for h in headings
        )
        has_section_heading = any(
            re.search(rf"(?<!\d){re.escape(base)}(?!\d)", h)
            for h in headings
        )
        return has_hierarchy and has_section_heading

    # Default: lighter check. Anchor + body-length already gate the result
    # in the caller; if we got here both passed. Trust them.
    return True


def _domain_ok(url: str, expected_domain: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return host.endswith(expected_domain.lower())


def verify(citation: str, *, timeout: float = DEFAULT_TIMEOUT) -> dict[str, Any]:
    """
    Verify a citation against an authoritative source.

    Returns a dict with at minimum:
        verified: bool
        citation: str
        reason:   str (only when verified is False)
        url:      str (only when verified is True)
        section:  str (only when verified is True)
        text:     str (only when verified is True; cropped to MAX_TEXT_CHARS)
        fetched_at: ISO-8601 timestamp (only when verified is True)
        domain:   str (only when verified is True)
    """
    parsed = parse_citation(citation)
    if not parsed.code_prefix:
        return _miss(
            citation,
            "no detectable jurisdiction in citation; "
            f"supported codes: {', '.join(supported_codes())}",
        )

    if not parsed.section:
        return _miss(citation, "no section number could be extracted from citation")

    built = build_url(parsed.code_prefix, parsed.section)
    if not built:
        return _miss(
            citation,
            f"no authoritative URL pattern for {parsed.code_prefix!r}",
            supported_codes=supported_codes(),
        )

    url, expected_domain = built

    try:
        with httpx.Client(
            headers={"User-Agent": USER_AGENT},
            timeout=timeout,
            follow_redirects=True,
        ) as c:
            resp = c.get(url)
    except httpx.HTTPError as e:
        return _miss(citation, f"transport error fetching {url}: {type(e).__name__}: {e}", url=url)

    if resp.status_code != 200:
        return _miss(citation, f"HTTP {resp.status_code} from {url}", url=url)

    final_url = str(resp.url)
    if not _domain_ok(final_url, expected_domain):
        return _miss(
            citation,
            f"redirected off authoritative domain: expected {expected_domain}, got {urlparse(final_url).hostname}",
            url=final_url,
        )

    text = _extract_text(resp.text)
    if len(text) < MIN_TEXT_CHARS:
        return _miss(citation, f"page returned suspiciously short text ({len(text)} chars)", url=final_url)

    if not _anchor_ok(text, parsed.section):
        return _miss(
            citation,
            f"section number {parsed.section.split('(', 1)[0]!r} not found on fetched page (anchor check failed)",
            url=final_url,
        )

    if not _structure_ok(resp.text, parsed.section, domain=expected_domain):
        return _miss(
            citation,
            f"page lacks code-hierarchy headings or section heading for {parsed.section.split('(', 1)[0]!r} "
            f"(structural check failed; likely a 'section not found' shell)",
            url=final_url,
        )

    return {
        "verified": True,
        "citation": citation,
        "code_prefix": parsed.code_prefix,
        "section": parsed.section,
        "url": final_url,
        "domain": expected_domain,
        "text": text[:MAX_TEXT_CHARS],
        "text_truncated": len(text) > MAX_TEXT_CHARS,
        "fetched_at": _now_iso(),
    }


# CLI:
#   python -m openclaw.skills.web_fallback.verify "Cal. Veh. Code § 22350"
if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) < 2:
        print("usage: python -m openclaw.skills.web_fallback.verify '<citation>'", file=sys.stderr)
        sys.exit(2)
    res = verify(" ".join(sys.argv[1:]))
    # Trim text in CLI output so it fits a terminal — full text is in the dict.
    if res.get("verified"):
        snippet = res["text"][:200].replace("\n", " ")
        res_print = {**res, "text_preview": snippet + ("…" if len(res["text"]) > 200 else "")}
        del res_print["text"]
        print(json.dumps(res_print, indent=2))
    else:
        print(json.dumps(res, indent=2))
