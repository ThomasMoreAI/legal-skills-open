"""Parse public Courts of New Zealand judgment cards."""

import re
import unicodedata
from datetime import datetime
from html import unescape
from urllib.parse import urljoin, urlparse


def clean(value: str) -> str:
    return " ".join(unescape(re.sub(r"<[^>]+>", " ", value)).split())


def normalised_tokens(value: str):
    folded = unicodedata.normalize("NFKD", value.casefold())
    folded = "".join(char for char in folded if not unicodedata.combining(char))
    return re.findall(r"[a-z0-9]+", folded)


def text_matches_query(text: str, query: str):
    """Require every query token in a source-backed result excerpt/detail."""
    haystack = set(normalised_tokens(text))
    needles = normalised_tokens(query)
    return bool(needles) and all(token in haystack for token in needles)


def judge_match_evidence(text: str, query: str):
    """Return published judge-context evidence, never a bare name hit."""
    tokens = normalised_tokens(query)
    suffixes = {"j", "jj", "cj", "p", "justice", "judge"}
    while tokens and tokens[-1] in suffixes:
        tokens.pop()
    if not tokens:
        return None
    surname = re.escape(tokens[-1])
    folded = unicodedata.normalize("NFKD", unescape(text))
    folded = "".join(char for char in folded if not unicodedata.combining(char))
    patterns = (
        rf"\b{surname}\s+(?:CJ|J|JJ|P)\b",
        rf"\bJustice\s+(?:[A-Z][A-Za-z'’-]+\s+){{0,3}}{surname}\b",
        rf"\b(?:Chief\s+Justice|President)\s+{surname}\b",
    )
    for pattern in patterns:
        match = re.search(pattern, folded, re.I)
        if match:
            start = max(0, match.start() - 80)
            end = min(len(folded), match.end() + 80)
            return " ".join(folded[start:end].split())
    return None


def parse_judgments(html: str, source_url: str, retrieved_at: str, court: str, *, allow_empty: bool = False):
    if re.search(r"captcha|access denied", html, re.I):
        raise ValueError("Courts source returned an access challenge")
    parts = re.split(r'<div\b[^>]*class="judgment"[^>]*>', html, flags=re.I)[1:]
    rows = []
    for part in parts:
        part = part.split('<div class="judgment">', 1)[0]
        link = re.search(
            r'<a\b[^>]*href="([^"]+\.pdf)"[^>]*>.*?<span\b[^>]*class="judgment__text"[^>]*>(.*?)</span>',
            part,
            re.I | re.S,
        )

        def field(label: str):
            match = re.search(
                rf'class="judgment__text"[^>]*>\s*{label}\s*</span>.*?class="judgment__content"[^>]*>\s*<span\b[^>]*class="judgment__text"[^>]*>(.*?)</span>',
                part,
                re.I | re.S,
            )
            return clean(match.group(1)) if match else None

        title = clean(link.group(2)) if link else None
        citation = field("Case number")
        date_text = field("Date of Judgment")
        summary = field("Summary")
        judges = field("Judge") or field("Judges")
        if not title or not citation or not date_text:
            continue
        try:
            published = datetime.strptime(date_text, "%d %B %Y").date().isoformat()
        except ValueError:
            continue
        pdf = urljoin(source_url, link.group(1))
        if urlparse(pdf).hostname != urlparse(source_url).hostname:
            continue
        rows.append(
            {
                "id": citation,
                "case_name": title,
                "citation": citation,
                "court": court,
                "date": published,
                "judges": judges,
                "summary": summary,
                "document_url": pdf,
                "document_format": "pdf",
                "source_url": source_url,
                "retrieved_at": retrieved_at,
                "coverage": "official published-judgment page; coverage varies by court and date",
            }
        )
    if not rows and not allow_empty:
        raise ValueError("Court judgment page contained no recognisable judgment cards")
    return rows


def parse_search_results(html: str, source_url: str, retrieved_at: str, query: str):
    """Parse judgment hits from the Courts site's official full-text search.

    The global search also returns judges' profiles, speeches and other site
    content. Only results with both a canonical ``/cases/`` page and an
    official ``/assets/cases/`` judgment PDF are returned here.
    """
    if re.search(r"captcha|access denied", html, re.I):
        raise ValueError("Courts search returned an access challenge")
    if not (
        re.search(r'<h1\b[^>]*class="[^"]*\bpage__title\b[^"]*"[^>]*>\s*Search Results\s*</h1>', html, re.I | re.S)
        and 'id="SearchForm_Firesphere_SolrSearch_Forms_SearchForm"' in html
        and re.search(r'<div\b[^>]*class="[^"]*\bsearch__results\b[^"]*"', html, re.I)
    ):
        raise ValueError("Courts search page omitted its recognised results structure")
    rows = []
    for article in re.findall(
        r'<article\b[^>]*class="[^"]*\bresult\b[^"]*"[^>]*>(.*?)</article>',
        html,
        re.I | re.S,
    ):
        page_match = re.search(
            r'<a\b[^>]*class="[^"]*\bresult__link\b[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
            article,
            re.I | re.S,
        )
        pdf_match = re.search(
            r'<a\b[^>]*href="([^"]*/assets/cases/[^"]+\.pdf)"[^>]*>\s*(\[[0-9]{4}\]\s+NZ[A-Z]+\s+[0-9]+)',
            article,
            re.I | re.S,
        )
        if not page_match or not pdf_match:
            continue
        page_url = urljoin(source_url, unescape(page_match.group(1)))
        pdf_url = urljoin(source_url, unescape(pdf_match.group(1)))
        if urlparse(page_url).hostname != urlparse(source_url).hostname:
            continue
        if not urlparse(page_url).path.startswith("/cases/"):
            continue
        if urlparse(pdf_url).hostname != urlparse(source_url).hostname:
            continue
        citation = clean(pdf_match.group(2))
        court_match = re.search(r"\]\s+(NZ[A-Z]+)\s+", citation)
        if not court_match:
            continue
        # Remove heading/footer navigation while retaining the indexed excerpt
        # that explains why the official search returned the judgment.
        excerpt_html = re.sub(r"<header\b.*?</header>|<footer\b.*?</footer>", " ", article, flags=re.I | re.S)
        search_excerpt = clean(excerpt_html)
        rows.append(
            {
                "id": citation,
                "case_name": clean(page_match.group(2)),
                "citation": citation,
                "court": court_match.group(1).upper(),
                "date": None,
                "judges": None,
                "summary": search_excerpt,
                "document_url": pdf_url,
                "document_format": "pdf",
                "case_page_url": page_url,
                "source_url": page_url,
                "search_source_url": source_url,
                "search_query": query,
                "search_match_basis": "official Courts full-text search index",
                "search_excerpt": search_excerpt,
                "retrieved_at": retrieved_at,
                "coverage": "official site-search judgment hit; verify judge attribution in the linked judgment",
            }
        )
    return list({row["citation"].casefold(): row for row in rows}.values())


def parse_case_page(html: str, source_url: str, retrieved_at: str):
    """Parse the canonical Courts case page linked by a search result."""
    if re.search(r"captcha|access denied", html, re.I):
        raise ValueError("Courts case page returned an access challenge")
    heading_match = re.search(
        r'<h1\b[^>]*class="[^"]*\bcase__title\b[^"]*"[^>]*>(.*?)</h1>',
        html,
        re.I | re.S,
    )
    date_match = re.search(
        r'<p\b[^>]*class="[^"]*\bcase__date\b[^"]*"[^>]*>(.*?)</p>',
        html,
        re.I | re.S,
    )
    pdf_match = re.search(
        r'<p\b[^>]*class="[^"]*\bcase__decision\b[^"]*"[^>]*>.*?<a\b[^>]*href="([^"]+\.pdf)"',
        html,
        re.I | re.S,
    )
    if not heading_match or not date_match or not pdf_match:
        raise ValueError("Courts case page contained no recognisable judgment metadata")
    heading = clean(heading_match.group(1))
    citation_match = re.search(r"\[[0-9]{4}\]\s+NZ[A-Z]+\s+[0-9]+", heading)
    if not citation_match:
        raise ValueError("Courts case page omitted its neutral citation")
    citation = citation_match.group(0)
    try:
        published = datetime.strptime(clean(date_match.group(1)), "%d %B %Y").date().isoformat()
    except ValueError as exc:
        raise ValueError("Courts case page used an unrecognised judgment date") from exc
    summary_match = re.search(
        r'<div\b[^>]*class="[^"]*\bcase__summary\b[^"]*"[^>]*>(.*?)(?:</div>\s*</div>|<h2\b|<footer\b)',
        html,
        re.I | re.S,
    )
    pdf_url = urljoin(source_url, unescape(pdf_match.group(1)))
    if urlparse(pdf_url).hostname != urlparse(source_url).hostname:
        raise ValueError("Courts case page linked a judgment on an unexpected host")
    court_match = re.search(r"\]\s+(NZ[A-Z]+)\s+", citation)
    return {
        "id": citation,
        "case_name": heading[: citation_match.start()].rstrip(" -"),
        "citation": citation,
        "court": court_match.group(1).upper() if court_match else None,
        "date": published,
        "judges": None,
        "summary": clean(summary_match.group(1)) if summary_match else None,
        "document_url": pdf_url,
        "document_format": "pdf",
        "case_page_url": source_url,
        "source_url": source_url,
        "retrieved_at": retrieved_at,
        "coverage": "official canonical case page; judge panel is not a structured page field",
    }
