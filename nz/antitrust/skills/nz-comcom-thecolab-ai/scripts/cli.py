#!/usr/bin/env python3
"""Search NZ Commerce Commission data, cases, news, and reports.

Source: the public comcom.govt.nz website (SilverStripe CMS, server-rendered).
Keyless, read-only; no login. The whole site uses one repeated "card" component
for listings, so `search`, `cases`, and `news` share a card parser; `page` reads
any comcom page and extracts its summary and linked documents/reports (PDFs).
"""
from __future__ import annotations

import argparse
import html as htmllib
import json
import pathlib
import re
import ssl
import sys
import urllib.parse
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "lib"))
import nzfetch  # noqa: E402

BASE = "https://www.comcom.govt.nz"
DOC_EXT_RE = re.compile(r"\.(pdf|docx?|xlsx?|pptx?|csv)$", re.I)


class ApiError(RuntimeError):
    """Upstream/network failure with a clean human message."""


def fetch(url: str, timeout: int = 20) -> str:
    ctx = ssl.create_default_context()
    try:
        return nzfetch.fetch_text(
            url, timeout=timeout, accept="text/html,*/*",
            context=ctx,
        )
    except nzfetch.Blocked as e:
        raise ApiError(f"network error contacting comcom.govt.nz: {e}") from e
    except nzfetch.FetchError as e:
        raise ApiError(str(e)) from e


def clean(text: str) -> str:
    return htmllib.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text))).strip()


def absolute(href: str) -> str:
    if href.startswith("http"):
        return href
    return BASE + href if href.startswith("/") else f"{BASE}/{href}"


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

_LINK_RE = re.compile(r'class="card__link"\s+href="([^"]+)"[^>]*>(.*?)</a>', re.S)
_STATUS_RE = re.compile(r'card__status[^"]*">(.*?)</div>', re.S)
_SUMMARY_RE = re.compile(r'card__summary">(.*?)</div>', re.S)
_INFO_RE = re.compile(r'card__info">(.*?)</div>', re.S)


def parse_cards(html: str, limit: int) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    # Listings share the `card--has-link` component; the leading class varies by
    # page (e.g. `card card--media-release-page card--has-link`), so split on the
    # common token rather than the full class string.
    for chunk in html.split('card--has-link')[1:]:
        chunk = chunk[:2000]  # a card block is small; cap to avoid bleeding into the next
        link = _LINK_RE.search(chunk)
        if not link:
            continue
        href, title = link.group(1), clean(link.group(2))
        if not title:
            continue
        status = _STATUS_RE.search(chunk)
        summary = _SUMMARY_RE.search(chunk)
        info = _INFO_RE.search(chunk)
        card = {
            "title": title,
            "url": absolute(href),
            "status": clean(status.group(1)) if status else None,
            "summary": clean(summary.group(1)) if summary else None,
            "meta": clean(info.group(1)) if info else None,
        }
        cards.append(card)
        if len(cards) >= limit:
            break
    return cards


def parse_detail(html: str, url: str) -> dict[str, Any]:
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    title_tag = re.search(r"<title>(.*?)</title>", html, re.S)
    desc = re.search(r'<meta name="description" content="([^"]*)"', html)
    # Documents/reports: links to files or the CMS asset store.
    docs: list[dict[str, str]] = []
    seen: set[str] = set()
    for href, text in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html, re.S):
        if "/assets/" in href or "/__data/" in href or "dmsdocument" in href or DOC_EXT_RE.search(href):
            full = absolute(href)
            if full in seen:
                continue
            seen.add(full)
            label = clean(text) or full.rsplit("/", 1)[-1]
            docs.append({"name": label, "url": full})
    return {
        "title": clean(h1.group(1)) if h1 else (clean(title_tag.group(1)) if title_tag else None),
        "url": url,
        "summary": clean(desc.group(1)) if desc else None,
        "documents": docs,
    }


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_search(args: argparse.Namespace) -> int:
    url = f"{BASE}/search/?q=" + urllib.parse.quote(args.query)
    cards = parse_cards(fetch(url), args.limit)
    payload = {"query": args.query, "source": url, "count": len(cards), "results": cards}
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"Commerce Commission search for {args.query!r} ({len(cards)})")
        for c in cards:
            print(f"\n  {c['title']}")
            if c.get("summary"):
                print(f"    {c['summary'][:140]}")
            print(f"    {c['url']}")
    return 0


def cmd_cases(args: argparse.Namespace) -> int:
    if args.keyword:
        url = f"{BASE}/search/?q=" + urllib.parse.quote(args.keyword)
        cards = [c for c in parse_cards(fetch(url), 50) if "/case-register/" in c["url"]][: args.limit]
        source = url
    else:
        source = f"{BASE}/case-register/case-register-entries/"
        cards = parse_cards(fetch(source), args.limit)
    payload = {"keyword": args.keyword, "source": source, "count": len(cards), "results": cards}
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        kw = f" matching {args.keyword!r}" if args.keyword else ""
        print(f"Commerce Commission case register{kw} ({len(cards)})")
        for c in cards:
            status = f"[{c['status']}] " if c.get("status") else ""
            meta = f" — {c['meta']}" if c.get("meta") else ""
            print(f"\n  {status}{c['title']}{meta}")
            print(f"    {c['url']}")
    return 0


def cmd_news(args: argparse.Namespace) -> int:
    source = f"{BASE}/news-and-media/news-and-events/"
    if args.year:
        source += f"{args.year}/"
    cards = parse_cards(fetch(source), args.limit)
    payload = {"year": args.year, "source": source, "count": len(cards), "results": cards}
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"Commerce Commission news & media ({len(cards)})")
        for c in cards:
            print(f"\n  {c['title']}")
            if c.get("summary"):
                print(f"    {c['summary'][:140]}")
            print(f"    {c['url']}")
    return 0


def cmd_page(args: argparse.Namespace) -> int:
    ref = args.url
    url = ref if ref.startswith("http") else absolute(ref if ref.startswith("/") else "/" + ref)
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or (parsed.hostname or "").lower() != "www.comcom.govt.nz":
        raise ApiError("page only fetches comcom.govt.nz URLs")
    detail = parse_detail(fetch(url), url)
    if args.json:
        print(json.dumps(detail, indent=2, ensure_ascii=False))
    else:
        print(detail.get("title") or url)
        print(f"  {url}")
        if detail.get("summary"):
            print(f"\n  {detail['summary']}")
        if detail.get("documents"):
            print(f"\n  Documents ({len(detail['documents'])}):")
            for d in detail["documents"][: args.limit]:
                print(f"    {d['name']}")
                print(f"      {d['url']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        description="Search NZ Commerce Commission cases, news, and reports (comcom.govt.nz)."
    )
    sub = ap.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="site-wide search across cases, decisions, reports, guidelines")
    p_search.add_argument("query", help="search terms, e.g. 'grocery market study'")
    p_search.add_argument("--limit", type=int, default=20, help="max results (default 20)")
    p_search.add_argument("--json", action="store_true", help="emit JSON")
    p_search.set_defaults(func=cmd_search)

    p_cases = sub.add_parser("cases", help="case register entries (recent, or filtered by keyword)")
    p_cases.add_argument("-k", "--keyword", help="filter case register by keyword")
    p_cases.add_argument("--limit", type=int, default=20, help="max entries (default 20)")
    p_cases.add_argument("--json", action="store_true", help="emit JSON")
    p_cases.set_defaults(func=cmd_cases)

    p_news = sub.add_parser("news", help="news, media releases, and report announcements")
    p_news.add_argument("--year", type=int, help="filter to a calendar year, e.g. 2026")
    p_news.add_argument("--limit", type=int, default=20, help="max items (default 20)")
    p_news.add_argument("--json", action="store_true", help="emit JSON")
    p_news.set_defaults(func=cmd_news)

    p_page = sub.add_parser("page", help="fetch a comcom page/case and list its documents (reports/PDFs)")
    p_page.add_argument("url", help="comcom.govt.nz URL or path, e.g. /case-register/case-register-entries/asb-bank-ltd/")
    p_page.add_argument("--limit", type=int, default=50, help="max documents to list (default 50)")
    p_page.add_argument("--json", action="store_true", help="emit JSON")
    p_page.set_defaults(func=cmd_page)

    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args)
    except ApiError as e:
        if getattr(args, "json", False):
            print(json.dumps({"error": "upstream_error", "message": str(e)}, indent=2), file=sys.stderr)
        else:
            print(f"nz-comcom: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
