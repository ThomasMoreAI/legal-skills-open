#!/usr/bin/env python3
"""Discover current official NZ regulatory-analysis publications."""
from __future__ import annotations

import argparse
import html
import json
import re
import socket
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlencode, urljoin, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

SCHEMA_VERSION = "1"
USER_AGENT = "thecolab-nz-regulatory-analysis/1.0 (+https://github.com/thecolab-ai/.skills)"
TIMEOUT = 10
MAX_BYTES = 2_000_000
MAX_REDIRECTS = 3
MAX_REGULATION_PAGES = 10
MAX_DECODE_PASSES = 5
REGULATION_ROOT = "https://www.regulation.govt.nz"
REGULATION_INDEX = REGULATION_ROOT + "/publications-and-resources/regulatory-analysis-summaries/"
ENVIRONMENT_ROOT = "https://environment.govt.nz"
ENVIRONMENT_INDEX = ENVIRONMENT_ROOT + "/what-government-is-doing/cabinet-papers-and-regulatory-impact-statements/"
ALLOWED_HOSTS = {"www.regulation.govt.nz", "environment.govt.nz"}
ALLOWED_PREFIXES = {
    "www.regulation.govt.nz": ("/publications-and-resources/regulatory-analysis-summaries/", "/assets/"),
    "environment.govt.nz": ("/what-government-is-doing/cabinet-papers-and-regulatory-impact-statements/", "/assets/"),
}
SPACE_RE = re.compile(r"\s+")
BLOCK_RE = re.compile(r"captcha|verify you are human|access denied|request unsuccessful|cf-chl-|challenge-platform|incapsula", re.I)


class CliError(Exception):
    def __init__(self, message: str, code: int, *, blocked: bool = False):
        super().__init__(message)
        self.code = code
        self.blocked = blocked


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        return None


def clean(value: str | None) -> str | None:
    if value is None:
        return None
    result = SPACE_RE.sub(" ", html.unescape(value)).strip()
    return result or None


def classify_document(title: str, url: str = "") -> str:
    # Use visible text and the document filename, never unrelated parent directories.
    filename = unquote(urlsplit(url).path.rsplit("/", 1)[-1]) if url else ""
    text = clean(f"{title} {filename}") or ""
    folded = text.casefold().replace("_", " ").replace("-", " ")
    if re.search(r"\b(independent|external)\b.*\bquality (?:assurance|assessment|review)\b|\bquality (?:assurance|assessment|review)\b.*\b(independent|external)\b", folded):
        return "independent_quality_assessment"
    if re.search(r"\b(department|departmental|agency|panel)\b.*\bquality (?:assurance|assessment|review)\b|\bquality (?:assurance|assessment|review)\b.*\b(department|departmental|agency|panel)\b", folded):
        return "agency_quality_assessment"
    if re.search(r"\bquality (?:assurance|assessment|review)\b|\bqa (?:statement|assessment|review)\b", folded):
        return "quality_assessment"
    if "supplementary analysis report" in folded:
        return "supplementary_analysis_report"
    if "cost recovery impact statement" in folded:
        return "cost_recovery_impact_statement"
    if re.search(r"\bregulatory impact assessment\b|\bria\b", folded):
        return "regulatory_impact_assessment"
    if re.search(r"\bregulatory impact statement\b|\bris\b", folded):
        return "regulatory_impact_statement"
    if re.search(r"\bregulatory analysis summary\b|\bras\b", folded):
        return "regulatory_analysis_summary"
    if "cabinet minute" in folded:
        return "cabinet_minute"
    if "cabinet paper" in folded:
        return "cabinet_paper"
    if "briefing" in folded:
        return "briefing"
    if urlsplit(url).path.casefold().endswith(".pdf"):
        return "other_pdf"
    return "publication_page"


def canonical_official_url(url: str, base: str | None = None, required_host: str | None = None) -> str | None:
    absolute = urljoin(base, url) if base else url
    parts = urlsplit(absolute)
    host = (parts.hostname or "").casefold()
    decoded_path = parts.path
    for _ in range(MAX_DECODE_PASSES):
        next_path = unquote(decoded_path)
        if next_path == decoded_path:
            break
        decoded_path = next_path
    else:
        if unquote(decoded_path) != decoded_path:
            return None
    try:
        port = parts.port
    except ValueError:
        return None
    if parts.scheme != "https" or parts.username or parts.password or port not in (None, 443):
        return None
    if "\\" in decoded_path or any(ord(char) < 32 for char in decoded_path) or any(segment in {".", ".."} for segment in decoded_path.split("/")):
        return None
    if host not in ALLOWED_HOSTS or (required_host and host != required_host) or not any(decoded_path.startswith(p) for p in ALLOWED_PREFIXES[host]):
        return None
    canonical_path = quote(decoded_path, safe="/!$&'()*+,-.:;=@_~")
    return urlunsplit(("https", host, canonical_path, parts.query, ""))


def _read_response(response: Any) -> tuple[bytes, str]:
    content_type = response.headers.get_content_type()
    if content_type not in {"text/html", "application/xhtml+xml"}:
        raise CliError(f"unexpected upstream content type: {content_type}", 6)
    declared = response.headers.get("Content-Length")
    if declared and declared.isdigit() and int(declared) > MAX_BYTES:
        raise CliError("upstream page exceeds the 2 MB response limit", 5)
    body = response.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise CliError("upstream page exceeds the 2 MB response limit", 5)
    text = body.decode("utf-8", errors="replace")
    if BLOCK_RE.search(text[:200_000]):
        raise CliError("official source returned an access challenge", 4, blocked=True)
    return body, response.geturl()


def fetch_html(url: str) -> tuple[str, str]:
    current = canonical_official_url(url)
    if not current:
        raise CliError("URL is outside the supported official publication paths", 2)
    required_host = urlsplit(current).hostname
    opener = build_opener(NoRedirect)
    for _ in range(MAX_REDIRECTS + 1):
        request = Request(current, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml", "Accept-Encoding": "identity"})
        try:
            with opener.open(request, timeout=TIMEOUT) as response:
                body, final_url = _read_response(response)
                canonical = canonical_official_url(final_url, required_host=required_host)
                if not canonical:
                    raise CliError("official source redirected outside the allowlist", 4, blocked=True)
                return body.decode("utf-8", errors="replace"), canonical
        except HTTPError as exc:
            if exc.code in {301, 302, 303, 307, 308}:
                location = exc.headers.get("Location")
                target = canonical_official_url(location or "", current, required_host)
                if not target:
                    raise CliError("official source redirected outside the allowlist", 4, blocked=True) from exc
                current = target
                continue
            if exc.code in {401, 403, 429, 451}:
                raise CliError(f"official source blocked the request (HTTP {exc.code})", 4, blocked=True) from exc
            if exc.code == 404:
                raise CliError("official publication page was not found", 5) from exc
            raise CliError(f"official source returned HTTP {exc.code}", 5) from exc
        except (URLError, TimeoutError, socket.timeout) as exc:
            raise CliError(f"official source unavailable: {getattr(exc, 'reason', exc)}", 5) from exc
    raise CliError("too many redirects from official source", 4, blocked=True)


class RegulationSearchParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.records: list[dict[str, Any]] = []
        self.item: dict[str, Any] | None = None
        self.depth = 0
        self.field: str | None = None
        self.buf: list[str] = []
        self.saw_results_container = False
        self.saw_no_results = False
        self.next_href: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        classes = set((a.get("class") or "").split())
        if "search__results" in classes:
            self.saw_results_container = True
        if "search__results-no-results" in classes:
            self.saw_no_results = True
        if tag == "a" and "pagination__link--arrow" in classes and (a.get("aria-label") or "").casefold() == "navigate to next page":
            self.next_href = a.get("href")
        if tag == "li" and "search-result__wrapper" in classes:
            self.item, self.depth = {}, 1
        elif self.item is not None:
            self.depth += 1
            if tag == "a" and "search-result__link" in classes:
                self.field, self.buf = "title", []
                self.item["href"] = a.get("href")
            elif "search-result__date" in classes:
                self.field, self.buf = "date", []
            elif "search-result__authors" in classes:
                self.field, self.buf = "author", []

    def handle_data(self, data: str) -> None:
        if self.item is not None and self.field:
            self.buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.item is None:
            return
        if self.field and tag in {"a", "span"}:
            self.item[self.field] = clean("".join(self.buf))
            self.field, self.buf = None, []
        self.depth -= 1
        if self.depth == 0:
            self.records.append(self.item)
            self.item = None


class EnvironmentListingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.listings: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "listing-results-container":
            return
        value = dict(attrs).get(":id")
        if not value:
            return
        try:
            listing, end = json.JSONDecoder().raw_decode(value)
        except (json.JSONDecodeError, TypeError) as exc:
            raise ValueError("invalid embedded listing JSON") from exc
        suffix = value[end:].strip()
        if suffix not in {"", "['id']", "['results']", "['total']"} or not isinstance(listing, dict):
            raise ValueError("unsupported embedded listing expression")
        results = listing.get("results")
        total = listing.get("total")
        if not isinstance(results, list) or isinstance(total, bool) or not isinstance(total, int) or total < 0 or total < len(results):
            raise ValueError("embedded listing is missing results or total")
        self.listings.append(listing)


class DetailParser(HTMLParser):
    def __init__(self, page_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        self.title: str | None = None
        self.updated: str | None = None
        self._in_h1 = False
        self._h1: list[str] = []
        self._anchor: dict[str, Any] | None = None
        self.documents: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag == "meta":
            key = (a.get("property") or a.get("name") or "").casefold()
            if key in {"article:modified_time", "dcterms.modified", "dcterms.date"} and a.get("content"):
                self.updated = clean(a["content"])
        elif tag == "h1":
            self._in_h1, self._h1 = True, []
        elif tag == "a" and a.get("href"):
            self._anchor = {"href": a["href"], "text": []}

    def handle_data(self, data: str) -> None:
        if self._in_h1:
            self._h1.append(data)
        if self._anchor is not None:
            self._anchor["text"].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1" and self._in_h1:
            self.title, self._in_h1 = clean("".join(self._h1)), False
        elif tag == "a" and self._anchor is not None:
            href = canonical_official_url(self._anchor["href"], self.page_url, urlsplit(self.page_url).hostname)
            label = clean("".join(self._anchor["text"])) or "Untitled document"
            if href and urlsplit(href).path.casefold().endswith(".pdf"):
                self.documents.append({"title": label, "url": href, "document_type": classify_document(label, href)})
            self._anchor = None


def parse_regulation_page(text: str, page_url: str = REGULATION_INDEX) -> tuple[list[dict[str, Any]], str | None]:
    parser = RegulationSearchParser()
    parser.feed(text)
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for raw in parser.records:
        url = canonical_official_url(raw.get("href") or "", REGULATION_INDEX, "www.regulation.govt.nz")
        title = clean(raw.get("title"))
        if not url or not title or url in seen:
            continue
        seen.add(url)
        date = clean(re.sub(r"^Publication Date:\s*", "", raw.get("date") or "", flags=re.I))
        author = clean(re.sub(r"^Author:\s*", "", raw.get("author") or "", flags=re.I))
        records.append({"title": title, "url": url, "published": date, "author": author, "document_type": classify_document(title, url), "publisher": "Ministry for Regulation"})
    if not parser.saw_results_container or (not records and not parser.saw_no_results):
        raise CliError("official regulation search result structure is missing or invalid", 6)
    next_url = canonical_official_url(parser.next_href or "", page_url, "www.regulation.govt.nz") if parser.next_href else None
    if parser.next_href and (not next_url or urlsplit(next_url).path != urlsplit(REGULATION_INDEX).path):
        raise CliError("official regulation pagination URL is outside the search index", 6)
    return records, next_url


def parse_regulation_search(text: str) -> list[dict[str, Any]]:
    records, _ = parse_regulation_page(text)
    return records


def parse_environment_search(text: str) -> tuple[list[dict[str, Any]], int]:
    parser = EnvironmentListingParser()
    try:
        parser.feed(text)
    except ValueError as exc:
        raise CliError(str(exc), 6) from exc
    if len(parser.listings) != 1:
        raise CliError("expected one official environment publication listing", 6)
    listing = parser.listings[0]
    records: list[dict[str, Any]] = []
    for raw in listing["results"]:
        if not isinstance(raw, dict):
            raise CliError("environment listing contains a non-record result", 6)
        url = canonical_official_url(str(raw.get("href") or ""), ENVIRONMENT_INDEX, "environment.govt.nz")
        title = clean(str(raw.get("title") or ""))
        if not url or not title:
            raise CliError("environment listing result is missing an official URL or title", 6)
        tags = [clean(str(tag.get("title") or "")) for tag in raw.get("tags", []) if isinstance(tag, dict)]
        clean_tags = [x for x in tags if x]
        document_types = list(dict.fromkeys(classify_document(tag) for tag in clean_tags if classify_document(tag) != "publication_page"))
        page_type = document_types[0] if len(document_types) == 1 else ("publication_package" if document_types else classify_document(title))
        records.append({"title": title, "url": url, "published": clean(str(raw.get("dateReadable") or raw.get("date") or "")), "tags": clean_tags, "document_type": page_type, "document_types": document_types, "publisher": "Ministry for the Environment"})
    return records, listing["total"]


def parse_detail(text: str, page_url: str) -> dict[str, Any]:
    parser = DetailParser(page_url)
    parser.feed(text)
    if not parser.title:
        raise CliError("official publication page has no readable title", 6)
    unique: list[dict[str, str]] = []
    seen: set[str] = set()
    for document in parser.documents:
        if document["url"] not in seen:
            unique.append(document)
            seen.add(document["url"])
    return {"kind": "regulatory_analysis_publication", "title": parser.title, "document_type": classify_document(parser.title), "page_url": page_url, "page_updated": parser.updated, "documents": unique, "document_count": len(unique)}


def source_url(source: str, query: str) -> str:
    index = REGULATION_INDEX if source == "regulation" else ENVIRONMENT_INDEX
    return index + "?" + urlencode({"query" if source == "regulation" else "keyword": query})


def run_search(query: str, source: str, limit: int) -> tuple[dict[str, Any], str]:
    sources = [source] if source != "all" else ["regulation", "environment"]
    results: list[dict[str, Any]] = []
    urls: list[str] = []
    totals: dict[str, int] = {}
    for selected in sources:
        if selected == "regulation":
            found: list[dict[str, Any]] = []
            seen_records: set[str] = set()
            seen_pages: set[str] = set()
            next_url: str | None = source_url(selected, query)
            for _ in range(MAX_REGULATION_PAGES):
                if not next_url or next_url in seen_pages:
                    if next_url:
                        raise CliError("official regulation pagination contains a cycle", 6)
                    break
                seen_pages.add(next_url)
                text, final_url = fetch_html(next_url)
                if final_url in urls:
                    raise CliError("official regulation pagination repeated a fetched page", 6)
                urls.append(final_url)
                page_records, next_url = parse_regulation_page(text, final_url)
                for record in page_records:
                    if record["url"] not in seen_records:
                        seen_records.add(record["url"])
                        found.append(record)
            else:
                if next_url:
                    raise CliError(f"regulation search exceeds the {MAX_REGULATION_PAGES}-page safety limit; narrow the query", 6)
            totals[selected] = len(found)
        else:
            text, final_url = fetch_html(source_url(selected, query))
            urls.append(final_url)
            found, total = parse_environment_search(text)
            totals[selected] = total
        results.extend(found[:limit])
    return {
        "kind": "regulatory_analysis_search",
        "results": results[:limit],
        "returned": len(results[:limit]),
        "source_totals": totals,
        "source_urls": urls,
    }, urls[0]


def envelope(ok: bool, source: str, query: dict[str, Any], data: Any, *, warnings: list[str] | None = None, blocked: bool = False, error: str | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {"schema_version": SCHEMA_VERSION, "ok": ok, "source": {"name": "New Zealand official regulatory-analysis publications", "url": source, "retrieved_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")}, "query": query, "data": data, "warnings": warnings or [], "blocked": blocked}
    if error:
        payload["error"] = error
    return payload


def print_human(payload: dict[str, Any]) -> None:
    data = payload["data"]
    if data["kind"] == "regulatory_analysis_search":
        if not data["results"]:
            print("No matching current publications found.")
        for item in data["results"]:
            print(f"{item['title']}\n  {item['document_type']} | {item.get('published') or 'date not shown'}\n  {item['url']}")
    else:
        print(f"{data['title']}\nType: {data['document_type']}\nUpdated: {data['page_updated'] or 'not shown'}\nDocuments: {data['document_count']}")
        for doc in data["documents"]:
            print(f"- {doc['title']} [{doc['document_type']}]\n  {doc['url']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Discover current official NZ regulatory-analysis publications")
    sub = parser.add_subparsers(dest="command", required=True)
    search = sub.add_parser("search", help="search official regulatory-analysis publication indexes")
    search.add_argument("query", help="words to search for")
    search.add_argument("--source", choices=("all", "regulation", "environment"), default="all")
    search.add_argument("--limit", type=int, choices=range(1, 26), default=10, metavar="1-25")
    search.add_argument("--json", action="store_true", help="emit the versioned JSON result envelope")
    inspect = sub.add_parser("inspect", help="inspect one official publication page and its linked PDFs")
    inspect.add_argument("url", help="official regulation.govt.nz or environment.govt.nz publication URL")
    inspect.add_argument("--json", action="store_true", help="emit the versioned JSON result envelope")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    query: dict[str, Any]
    try:
        if args.command == "search":
            if not args.query.strip():
                raise CliError("query must not be empty", 2)
            query = {"command": "search", "text": args.query, "source": args.source, "limit": args.limit}
            data, used_url = run_search(args.query, args.source, args.limit)
        else:
            official_url = canonical_official_url(args.url)
            if not official_url or urlsplit(official_url).path.casefold().endswith(".pdf"):
                raise CliError("inspect requires a supported official HTML publication URL", 2)
            query = {"command": "inspect", "url": official_url}
            text, used_url = fetch_html(official_url)
            data = parse_detail(text, used_url)
        payload = envelope(True, used_url, query, data, warnings=["Search results and publication pages can change; cite the returned official URL and retrieval time."])
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print_human(payload)
        return 0
    except CliError as exc:
        query = {"command": args.command}
        if getattr(args, "json", False):
            print(json.dumps(envelope(False, "", query, None, blocked=exc.blocked, error=str(exc)), ensure_ascii=False, indent=2))
        else:
            print(f"Error: {exc}", file=sys.stderr)
        return exc.code


if __name__ == "__main__":
    raise SystemExit(main())
