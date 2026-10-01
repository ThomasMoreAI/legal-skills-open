#!/usr/bin/env python3
"""Read-only CLI for FMA warnings and public licensed-provider sources."""
from __future__ import annotations

import argparse
import csv
import html
import io
import json
import pathlib
import re
from datetime import date, datetime, timedelta
import sys
from typing import Any
from urllib.parse import urlencode, urljoin, urlparse, parse_qs, quote_plus

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "lib"))
import nzfetch  # noqa: E402

FMA_BASE = "https://www.fma.govt.nz"
FMA_WARNINGS_LIST_URL = f"{FMA_BASE}/library/warnings-and-alerts/"
FMA_WARNINGS_DOWNLOAD_URL = f"{FMA_BASE}/library/warnings-and-alerts/downloadWarnings/"
FMA_PROVIDER_LIST_URL = f"{FMA_BASE}/business/licensed-providers/"
FMA_FINANCIAL_ADVICE_SERVICE_PAGE = f"{FMA_BASE}/business/services/financial-advice-provider/"
FMA_CROWDFUNDING_PAGE = f"{FMA_BASE}/business/services/crowdfunding/"
FMA_P2P_PAGE = f"{FMA_BASE}/business/services/peer-to-peer-lending-providers/"
FSP_REGISTER_URL = "https://fsp-register.companiesoffice.govt.nz/"
UA = "fma-nz-skill/1.0 (+https://github.com/thecolab-ai/.skills)"
DEFAULT_TIMEOUT = 20
DEFAULT_LIMIT = 20
PAGE_STEP = 15
MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "sept": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}

LIST_ITEM_RE = re.compile(
    r'<li[^>]*class="[^"]*search-results-semantic__result-item[^"]*"[^>]*>(.*?)</li>',
    re.S,
)

TERM_RE = re.compile(
    r'<div[^>]*class="[^"]*result-list__result-term[^"]*"[^>]*>(.*?)</div>',
    re.S,
)

DATE_TEXT_RE = re.compile(r"(\d{1,2})\s+([A-Za-z]+)\s+(20\d{2})")
ISO_DATE_RE = re.compile(r"(20\d{2})-(\d{2})-(\d{2})")

PROVIDER_TYPES = {
    "all": {
        "query": None,
        "labels": ["all"],
        "term_filter": [],
        "source_names": ["FMA licensed provider index"],
        "source_url": FMA_PROVIDER_LIST_URL,
    },
    "crowdfunding": {
        "query": "crowdfunding",
        "labels": ["Crowdfunding providers", "Crowdfunding service providers"],
        "term_filter": ["crowdfunding"],
        "source_names": [
            "FMA Crowdfunding services",
            "FMA licensed provider index",
        ],
        "source_url": FMA_CROWDFUNDING_PAGE,
    },
    "p2p": {
        "query": "peer-to-peer",
        "labels": ["Peer-to-peer lending service providers"],
        "term_filter": ["peer-to-peer"],
        "source_names": [
            "FMA peer-to-peer lending services",
            "FMA licensed provider index",
        ],
        "source_url": FMA_P2P_PAGE,
    },
    "peer_to_peer": {
        "query": "peer-to-peer",
        "labels": ["Peer-to-peer lending service providers"],
        "term_filter": ["peer-to-peer"],
        "source_names": [
            "FMA peer-to-peer lending services",
            "FMA licensed provider index",
        ],
        "source_url": FMA_P2P_PAGE,
    },
    "advice": {
        "query": "financial advice",
        "labels": ["financial advice"],
        "term_filter": [],
        "source_names": [
            "FMA Financial Advice Provider page",
            "Financial Service Providers Register",
        ],
        "source_url": FMA_FINANCIAL_ADVICE_SERVICE_PAGE,
    },
}


class UpstreamUnavailable(RuntimeError):
    pass


class NotFound(RuntimeError):
    pass


def normalize(text: Any) -> str:
    if text is None:
        return ""
    collapsed = re.sub(r"\s+", " ", str(text))
    return html.unescape(collapsed).strip()


def to_slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.strip().lower())


def clean_text(raw: Any) -> str:
    if raw is None:
        return ""
    return normalize(re.sub(r"<[^>]+>", " ", str(raw)))


def fetch_text(url: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    try:
        return nzfetch.fetch_text(
            url,
            timeout=timeout,
            accept="text/html,text/csv,*/*;q=0.8",
            headers={"Accept-Language": "en-NZ,en;q=0.8"},
        )
    except nzfetch.Blocked as exc:
        # Transient bot-block (IP reputation / challenge) — treat as upstream
        # unavailable so the smoke test SKIPs (returncode 2) rather than failing.
        raise UpstreamUnavailable(f"network error while calling {url}: {exc}")
    except nzfetch.FetchError as exc:
        if "HTTP 404" in str(exc):
            raise NotFound(f"HTTP 404 from {url}")
        raise UpstreamUnavailable(f"HTTP error from {url}: {exc}")


def to_abs_url(value: str, base: str) -> str:
    if not value:
        return ""
    value = value.strip()
    if value.startswith("http://") or value.startswith("https://"):
        return value
    if value.startswith("/"):
        return FMA_BASE + value
    return urljoin(base, value)


def parse_list_item(block: str, base_url: str) -> dict[str, Any] | None:
    link = re.search(
        r'<h3>\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>\s*</h3>',
        block,
        re.S,
    )
    if not link:
        return None

    href = to_abs_url(link.group(1), base_url)
    title = clean_text(link.group(2))
    slug = urlparse(href).path.rstrip("/").split("/")[-1]
    if not title:
        return None

    summary_match = re.search(r"<p>(.*?)</p>", block, re.S)
    summary = clean_text(summary_match.group(1)) if summary_match else ""

    date_match = re.search(
        r'<span[^>]*class="[^"]*search-results-semantic__date[^"]*"[^>]*>(.*?)</span>',
        block,
        re.S,
    )
    date_text = clean_text(date_match.group(1)) if date_match else ""

    terms = [clean_text(term) for term in TERM_RE.findall(block)]

    return {
        "id": slug,
        "title": title,
        "url": href,
        "summary": summary,
        "date_text": date_text,
        "date": parse_display_date(date_text),
        "terms": terms,
    }


def parse_display_date(value: str) -> str | None:
    if not value:
        return None

    cleaned = value.strip()
    m = ISO_DATE_RE.fullmatch(cleaned)
    if m:
        try:
            return date(int(m.group(1)), int(m.group(2)), int(m.group(3))).isoformat()
        except ValueError:
            return None

    m = DATE_TEXT_RE.search(cleaned)
    if not m:
        return None
    day = int(m.group(1))
    month_name = m.group(2).strip().lower()
    year = int(m.group(3))
    month = MONTHS.get(month_name)
    if not month:
        month_name = month_name[:3]
        month = MONTHS.get(month_name)
    if not month:
        return None
    try:
        return date(year, month, day).isoformat()
    except ValueError:
        return None


def parse_list_items(html_text: str, base_url: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for block in LIST_ITEM_RE.findall(html_text):
        item = parse_list_item(block, base_url)
        if item:
            out.append(item)
    return out


def build_search_url(base_url: str, query: str | None, start: int | None = None) -> str:
    params: dict[str, str] = {}
    if query:
        params["BasicSearch"] = query
    if start and start > 0:
        params["start"] = str(start)
    if not params:
        return base_url
    return f"{base_url}?{urlencode(params)}"


def parse_date_range(value: str | None) -> date | None:
    if not value:
        return None
    value = value.strip()
    if re.fullmatch(r"\d{4}", value):
        return date(int(value), 1, 1)
    if re.fullmatch(r"20\d{2}-\d{2}-\d{2}", value):
        return datetime.strptime(value, "%Y-%m-%d").date()
    if re.fullmatch(r"\d{2}/\d{2}/20\d{2}", value):
        return datetime.strptime(value, "%d/%m/%Y").date()
    raise ValueError("--since/--until must be YYYY or YYYY-MM-DD")


def within_range(item_date: str | None, since: date | None, until: date | None) -> bool:
    if not item_date:
        return True
    parsed = parse_display_date(item_date)
    if not parsed:
        return True
    d = datetime.fromisoformat(parsed).date()
    if since and d < since:
        return False
    if until and d > until:
        return False
    return True


def warning_list_items(args: argparse.Namespace) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    scanned = 0
    start = 0
    since = parse_date_range(args.since)
    until = parse_date_range(args.until)

    while True:
        query = args.query
        url = build_search_url(FMA_WARNINGS_LIST_URL, query, start)
        html_text = fetch_text(url, timeout=args.timeout)
        items = parse_list_items(html_text, FMA_WARNINGS_LIST_URL)
        if not items:
            break
        scanned += len(items)

        stop_by_since = False
        for item in items:
            if not within_range(item["date"], since, until):
                if since and item.get("date"):
                    if parse_display_date(item["date"]) and datetime.fromisoformat(item["date"]).date() < since:
                        stop_by_since = True
                continue

            records.append(
                {
                    "id": item["id"],
                    "title": item["title"],
                    "summary": item["summary"],
                    "source_url": item["url"],
                    "published_date": item["date"],
                    "published_date_text": item["date_text"],
                }
            )
            if len(records) >= args.limit:
                break

        if len(records) >= args.limit or stop_by_since:
            break

        if len(items) < PAGE_STEP:
            break
        start += PAGE_STEP

    return [
        {
            "records": records,
            "scanned_pages": max(start // PAGE_STEP + 1, 1),
            "matched": len(records),
            "returned": len(records[: args.limit]),
            "scanned": scanned,
        }
    ][0]


def warning_detail(payload_url: str, timeout: int) -> dict[str, Any]:
    html_text = fetch_text(payload_url, timeout=timeout)

    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_text, re.S)
    title = clean_text(title_match.group(1)) if title_match else ""

    desc_match = re.search(
        r'<meta\s+name="description"[^>]+content="([^"]+)"',
        html_text,
        re.I,
    )
    description = desc_match.group(1).strip() if desc_match else ""

    published_match = re.search(
        r'class="[^"]*published__text[^"]*"[^>]*>(.*?)</span>',
        html_text,
        re.I | re.S,
    )
    published = parse_display_date(clean_text(published_match.group(1))) if published_match else None

    if not published:
        m = re.search(r'Warning first published\s+((?:\d{1,2}\s+[A-Za-z]+\s+20\d{2}))', html_text)
        published = parse_display_date(m.group(1)) if m else None

    body_summary_match = re.search(
        r'<div[^>]*class="[^"]*content-element__content[^"]*"[^>]*>(.*?)</div>\s*</div>\s*</article>',
        html_text,
        re.S,
    )
    body_summary = ""
    if body_summary_match:
        p = re.search(r'<p>(.*?)</p>', body_summary_match.group(1), re.S)
        if p:
            body_summary = clean_text(p.group(1))

    return {
        "title": title,
        "description": description,
        "summary": body_summary,
        "source_url": payload_url,
        "published_date": published,
        "published_date_text": clean_text(published_match.group(1)) if published_match else "",
    }


def fetch_provider_page(url: str, timeout: int) -> dict[str, Any]:
    html_text = fetch_text(url, timeout=timeout)

    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_text, re.S)
    title = clean_text(title_match.group(1)) if title_match else ""

    desc_match = re.search(
        r'<meta\s+name="description"[^>]+content="([^"]+)"',
        html_text,
        re.I,
    )
    description = desc_match.group(1).strip() if desc_match else ""

    # Typical page includes one phrase like: "is licensed ... to provide ..."
    license_class = ""
    m = re.search(r"is (?:a|an)\s+([^\.]+)\.?,", description, re.I)
    if not m:
        m = re.search(r"is (?:a|an)\s+([^\.]+)", description, re.I)
    if m:
        license_class = clean_text(m.group(1))

    fsp = re.search(r"(FSP\d+)", description or title, re.I)

    slug = urlparse(url).path.rstrip("/").split("/")[-1]

    return {
        "name": title,
        "slug": slug,
        "source_url": url,
        "description": description,
        "license_class": license_class,
        "fsp_number": fsp.group(1) if fsp else "",
        "url": url,
    }


def provider_search_items(
    query: str | None,
    provider_type: str,
    limit: int,
    timeout: int,
) -> tuple[list[dict[str, Any]], int, int]:
    records: list[dict[str, Any]] = []
    scanned = 0
    start = 0
    type_key = provider_type if provider_type in PROVIDER_TYPES else "all"
    cfg = PROVIDER_TYPES[type_key]

    query_to_use = query
    if not query_to_use and cfg["query"]:
        query_to_use = cfg["query"]

    while len(records) < limit:
        url = build_search_url(FMA_PROVIDER_LIST_URL, query_to_use, start)
        page_html = fetch_text(url, timeout=timeout)
        items = parse_list_items(page_html, FMA_PROVIDER_LIST_URL)
        if not items:
            break
        scanned += len(items)

        for item in items:
            if cfg["term_filter"]:
                tag_text = [t.lower() for t in item.get("terms", [])]
                if query is None:
                    if not any(any(k in t for t in tag_text) for k in cfg["term_filter"]):
                        continue
            records.append(
                {
                    "id": item["id"],
                    "name": item["title"],
                    "source_url": item["url"],
                    "summary": item["summary"],
                    "terms": item["terms"],
                }
            )
            if len(records) >= limit:
                break

        if len(items) < PAGE_STEP:
            break
        start += PAGE_STEP

    return records, scanned, len(records)


def provider_sources(provider_type: str) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    normalized = provider_type if provider_type in PROVIDER_TYPES else "all"
    cfg = PROVIDER_TYPES[normalized]

    result.append(
        {
            "name": cfg["source_names"][0],
            "url": cfg["source_url"],
            "notes": "Primary source for licensed-provider entries in public HTML",
        }
    )

    if normalized in {"advice", "all"}:
        result.append(
            {
                "name": "Financial Service Providers Register",
                "url": FSP_REGISTER_URL,
                "notes": "Public search is JS/login-fronted and not mirrored in this skill",
            }
        )

    if normalized == "all":
        result.append(
            {
                "name": "FMA Crowdfunding services",
                "url": FMA_CROWDFUNDING_PAGE,
                "notes": "Service details and eligibility guidance",
            }
        )
        result.append(
            {
                "name": "FMA Peer-to-peer lending services",
                "url": FMA_P2P_PAGE,
                "notes": "Service details and eligibility guidance",
            }
        )

    return result


def output_json(payload: dict[str, Any], json_mode: bool) -> None:
    if json_mode:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        if payload.get("kind"):
            print(f"[{payload['kind']}]")
        for line in (payload.get("rows") or []):
            print(line)


def output_error(err: Exception, command: str, json_mode: bool, source_url: str | None = None) -> None:
    code = 1
    payload: dict[str, Any] = {
        "error": "error",
        "kind": command,
        "message": str(err),
        "meta": {
            "source_url": source_url,
            "source": "FMA",
            "at": datetime.utcnow().isoformat() + "Z",
        },
    }

    if isinstance(err, UpstreamUnavailable):
        payload["error"] = "upstream_unavailable"
        code = 2
    elif isinstance(err, NotFound):
        payload["error"] = "not_found"

    if json_mode:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(payload["message"], file=sys.stderr)
    raise SystemExit(code)


def command_warning_list(args: argparse.Namespace) -> int:
    try:
        data = warning_list_items(args)
    except (UpstreamUnavailable, NotFound, ValueError) as exc:
        output_error(
            exc,
            command="fma_warnings_list",
            json_mode=args.json,
            source_url=FMA_WARNINGS_LIST_URL,
        )

    payload = {
        "kind": "fma_warnings_search",
        "query": args.query,
        "since": args.since,
        "until": args.until,
        "meta": {
            "source": "FMA warnings",
            "source_url": FMA_WARNINGS_LIST_URL,
            "scanned": data["scanned"],
            "scanned_pages": data["scanned_pages"],
            "returned": len(data["records"]),
            "matched": data["matched"],
        },
        "records": data["records"],
    }

    if args.json:
        output_json(payload, True)
        return 0

    print(f"Warnings: {payload['meta']['returned']} rows")
    for row in payload["records"]:
        print(f"- {row['title']}")
        if row.get("published_date"):
            print(f"  date: {row['published_date']}")
        print(f"  url: {row['source_url']}")
    return 0


def command_warning_get(args: argparse.Namespace) -> int:
    source_url = args.slug
    if not re.match(r"^https?://", source_url):
        if source_url.startswith("/"):
            source_url = to_abs_url(source_url, FMA_WARNINGS_LIST_URL)
        else:
            source_url = f"{FMA_WARNINGS_LIST_URL.rstrip('/')}/{source_url.strip('/')}/"

    try:
        record = warning_detail(source_url, args.timeout)
    except (UpstreamUnavailable, NotFound) as exc:
        output_error(exc, command="fma_warning_get", json_mode=args.json, source_url=source_url)

    payload = {
        "kind": "fma_warning_detail",
        "meta": {
            "source": "FMA warnings",
            "source_url": source_url,
            "at": datetime.utcnow().isoformat() + "Z",
        },
        "record": record,
    }
    if args.json:
        output_json(payload, True)
        return 0

    print(record.get("title") or "(unknown)")
    if record.get("published_date"):
        print(f"published: {record['published_date']}")
    if record.get("description"):
        print(f"description: {record['description']}")
    print(record.get("source_url"))
    if record.get("summary"):
        print(f"summary: {record['summary'][:200]}")
    return 0


def command_warning_download(args: argparse.Namespace) -> int:
    start = parse_date_range(args.date_from)
    end = parse_date_range(args.date_to)

    if not start or not end:
        raise ValueError("--date-from and --date-to are required")

    if end < start:
        raise ValueError("--date-to must be after --date-from")

    if args.limit is None:
        args.limit = 5

    try:
        url = (
            f"{FMA_WARNINGS_DOWNLOAD_URL}?"
            f"DateFrom={start.isoformat()}&DateTo={end.isoformat()}"
        )
        payload = fetch_text(url, timeout=args.timeout)
        csv_rows = list(csv.reader(io.StringIO(payload)))
    except (UpstreamUnavailable, NotFound, ValueError) as exc:
        output_error(
            exc,
            command="fma_warnings_download",
            json_mode=args.json,
            source_url=f"{FMA_WARNINGS_DOWNLOAD_URL}?DateFrom={start.isoformat()}&DateTo={end.isoformat()}",
        )

    header = csv_rows[0] if csv_rows else []
    records = []
    if len(csv_rows) > 1:
        records = [dict(zip(header, row)) for row in csv_rows[1:] if len(row) == len(header)]

    preview = records[: args.limit]

    payload = {
        "kind": "fma_warnings_download",
        "meta": {
            "source": "FMA warnings",
            "source_url": f"{FMA_WARNINGS_DOWNLOAD_URL}?DateFrom={start.isoformat()}&DateTo={end.isoformat()}",
            "from": start.isoformat(),
            "to": end.isoformat(),
            "total_rows": len(records),
            "returned": len(preview),
        },
        "records": preview,
    }

    if args.json:
        output_json(payload, True)
        return 0

    print(f"Rows downloaded: {payload['meta']['total_rows']} from {payload['meta']['from']} to {payload['meta']['to']}")
    for row in preview:
        title = row.get("Content") or ""
        print(f"- {title[:100]}")
    return 0


def resolve_provider_url(ref: str) -> str:
    ref = ref.strip()
    if re.match(r"^https?://", ref):
        return ref
    if ref.startswith("/"):
        return to_abs_url(ref, FMA_PROVIDER_LIST_URL)
    if "/" in ref:
        return ref if ref.startswith("http") else to_abs_url(ref, FMA_PROVIDER_LIST_URL)

    if re.fullmatch(r"\d+", ref) or ref.upper().startswith("FSP"):
        # Try to resolve by search in the public list first.
        return resolve_provider_from_query(ref)

    return f"{FMA_PROVIDER_LIST_URL.rstrip('/')}/{ref.strip('/')}/"


def resolve_provider_from_query(provider_ref: str) -> str:
    entries, _, _ = provider_search_items(provider_ref, "all", 5, DEFAULT_TIMEOUT)
    slug_target = to_slug(provider_ref)
    for item in entries:
        if slug_target in to_slug(item["id"]) or slug_target in to_slug(item["name"]):
            return item["source_url"]
        if provider_ref.upper().startswith("FSP") and provider_ref.upper() in (item.get("summary", "") + item.get("name", "")).upper():
            return item["source_url"]
    if not entries:
        raise NotFound(f"no matching FMA provider record found for {provider_ref}")
    return entries[0]["source_url"]


def command_provider_list(args: argparse.Namespace) -> int:
    p_type = args.type
    if p_type == "all":
        query = args.query
    else:
        query = args.query

    try:
        records, scanned, _ = provider_search_items(
            query=query,
            provider_type=p_type,
            limit=args.limit,
            timeout=args.timeout,
        )
    except (UpstreamUnavailable, NotFound) as exc:
        output_error(
            exc,
            command="fma_provider_list",
            json_mode=args.json,
            source_url=FMA_PROVIDER_LIST_URL,
        )

    type_label = p_type if p_type != "all" else "all"

    payload = {
        "kind": "fma_provider_search",
        "type": type_label,
        "query": args.query,
        "meta": {
            "source": "FMA licensed providers",
            "source_url": FMA_PROVIDER_LIST_URL,
            "scanned": scanned,
            "returned": len(records),
            "limit": args.limit,
        },
        "records": records,
    }

    if args.json:
        if args.type == "advice":
            payload["advice_register"] = {
                "source_url": FSP_REGISTER_URL,
                "notes": "advice providers are primarily maintained on the FSP Register; full query flow is JS-dependent",
            }
        output_json(payload, True)
        return 0

    print(f"Providers (type={type_label})" )
    print(f"returned: {len(records)}")
    for row in records:
        print(f"- {row['name']}")
        print(f"  url: {row['source_url']}")
        if row.get("terms"):
            print(f"  terms: {', '.join(row['terms'])}")

    if args.type == "advice":
        print("Note: advice providers search is source-limited; use sources for FSP register guidance.")
    return 0


def command_provider_get(args: argparse.Namespace) -> int:
    try:
        provider_url = resolve_provider_url(args.provider_id)
        record = fetch_provider_page(provider_url, args.timeout)
    except (UpstreamUnavailable, NotFound) as exc:
        output_error(
            exc,
            command="fma_provider_get",
            json_mode=args.json,
            source_url=provider_url if "provider_url" in locals() else None,
        )

    payload = {
        "kind": "fma_provider_detail",
        "meta": {
            "source": "FMA licensed providers",
            "source_url": record["source_url"],
            "at": datetime.utcnow().isoformat() + "Z",
        },
        "record": record,
        "sources": provider_sources("advice" if args.include_advice_sources else "all"),
    }
    if args.json:
        output_json(payload, True)
        return 0

    print(record["name"])
    if record.get("fsp_number"):
        print(f"fsp_number: {record['fsp_number']}")
    if record.get("license_class"):
        print(f"license_class: {record['license_class']}")
    print(record["source_url"])
    if record.get("description"):
        print(record["description"])
    return 0


def command_provider_sources(args: argparse.Namespace) -> int:
    payload = {
        "kind": "fma_provider_sources",
        "type": args.type,
        "sources": provider_sources(args.type),
    }

    if args.json:
        output_json(payload, True)
        return 0

    print(f"Provider sources for type={args.type}")
    for src in payload["sources"]:
        print(f"- {src['name']}: {src['url']}")
        if src.get("notes"):
            print(f"  notes: {src['notes']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", help="emit JSON output")

    parser = argparse.ArgumentParser(
        prog="skills/fma-nz/scripts/cli.py",
        description="Query FMA warnings and public licensed-provider source pages.",
    )
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="network timeout seconds")

    sub = parser.add_subparsers(dest="command", required=True)

    warnings = sub.add_parser("warnings", help="Search and fetch warning records", parents=[common])
    warnings_sub = warnings.add_subparsers(dest="warnings_command", required=True)

    warnings_list = warnings_sub.add_parser("list", help="list/search warnings", parents=[common])
    warnings_list.add_argument("--query", "-q", default=None, help="keyword search")
    warnings_list.add_argument("--since", default=None, help="only include rows on/after YYYY or YYYY-MM-DD")
    warnings_list.add_argument("--until", default=None, help="only include rows on/before YYYY or YYYY-MM-DD")
    warnings_list.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="max rows")
    warnings_list.set_defaults(func=command_warning_list)

    warnings_get = warnings_sub.add_parser("get", help="get one warning by slug or URL", parents=[common])
    warnings_get.add_argument("slug", help="warning slug or full URL")
    warnings_get.set_defaults(func=command_warning_get)

    warnings_download = warnings_sub.add_parser(
        "download", help="download warnings CSV by date range", parents=[common]
    )
    warnings_download.add_argument("--date-from", required=True, help="start date YYYY-MM-DD")
    warnings_download.add_argument("--date-to", required=True, help="end date YYYY-MM-DD")
    warnings_download.add_argument("--limit", type=int, default=5, help="max preview rows")
    warnings_download.set_defaults(func=command_warning_download)

    providers = sub.add_parser(
        "providers",
        help="Search and inspect licensed provider pages",
        parents=[common],
    )
    providers_sub = providers.add_subparsers(dest="providers_command", required=True)

    providers_list = providers_sub.add_parser("list", help="list providers by type", parents=[common])
    providers_list.add_argument("--type", choices=["all", "crowdfunding", "p2p", "peer_to_peer", "advice"], default="all")
    providers_list.add_argument("--query", "-q", default=None, help="keyword search")
    providers_list.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="max rows")
    providers_list.set_defaults(func=command_provider_list)

    providers_get = providers_sub.add_parser("get", help="get provider details", parents=[common])
    providers_get.add_argument("provider_id", help="provider slug, URL, or FSP number")
    providers_get.add_argument(
        "--include-advice-sources",
        action="store_true",
        help="include FSP register advice source in output",
    )
    providers_get.set_defaults(func=command_provider_get)

    providers_sources = providers_sub.add_parser(
        "sources", help="show curated source URLs", parents=[common]
    )
    providers_sources.add_argument("--type", choices=["all", "crowdfunding", "p2p", "peer_to_peer", "advice"], default="all")
    providers_sources.set_defaults(func=command_provider_sources)

    alias_platforms = sub.add_parser(
        "crowdfunding-platforms",
        help="Convenience alias for crowdfunding provider list",
        parents=[common],
    )
    alias_platforms.add_argument("--query", "-q", default=None)
    alias_platforms.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    alias_platforms.set_defaults(
        func=lambda a: command_provider_list(
            argparse.Namespace(
                type="crowdfunding",
                query=a.query,
                limit=a.limit,
                json=a.json,
                timeout=a.timeout,
            )
        )
    )

    alias_advice = sub.add_parser(
        "advice-providers",
        help="Convenience alias for advice provider discovery",
        parents=[common],
    )
    alias_advice.add_argument("--query", "-q", default=None)
    alias_advice.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    alias_advice.set_defaults(
        func=lambda a: command_provider_list(
            argparse.Namespace(
                type="advice",
                query=a.query,
                limit=a.limit,
                json=a.json,
                timeout=a.timeout,
            )
        )
    )

    alias_search = sub.add_parser(
        "provider-search", help="Convenience wrapper for provider search", parents=[common]
    )
    alias_search.add_argument("query")
    alias_search.add_argument("--type", choices=["all", "crowdfunding", "p2p", "peer_to_peer", "advice"], default="all")
    alias_search.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    alias_search.set_defaults(
        func=lambda a: command_provider_list(
            argparse.Namespace(
                type=a.type,
                query=a.query,
                limit=a.limit,
                json=a.json,
                timeout=a.timeout,
            )
        )
    )

    providers_get_by_fsp = sub.add_parser(
        "provider", help="Fetch by fsp number or provider slug", parents=[common]
    )
    providers_get_by_fsp.add_argument("provider", help="provider slug, URL, or FSP number")
    providers_get_by_fsp.set_defaults(
        func=lambda a: command_provider_get(
            argparse.Namespace(
                provider_id=a.provider,
                include_advice_sources=False,
                json=a.json,
                timeout=a.timeout,
            )
        )
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if not getattr(args, "func", None):
        parser.print_help()
        return 1
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
