#!/usr/bin/env python3
"""Query official New Zealand legislation sources.

The keyless path uses legislation.govt.nz HTML/XML format URLs. The PCO
developer API is supported for search when LEGISLATION_NZ_API_KEY is set.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import pathlib
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "lib"))
import nzfetch  # noqa: E402

BASE_URL = "https://www.legislation.govt.nz"
API_BASE_URL = "https://api.legislation.govt.nz"
UA = "thecolab-ai/legislation-nz-skill (+https://github.com/thecolab-ai/.skills)"
DEFAULT_TIMEOUT = 10
DEFAULT_LIMIT = 10
MAX_LIMIT = 100
ALLOWED_HOSTS = {
    "api.legislation.govt.nz",
    "catalogue.data.govt.nz",
    "www.legislation.govt.nz",
}

TYPE_ALIASES = {
    "act": "act",
    "acts": "act",
    "bill": "bill",
    "bills": "bill",
    "regulation": "secondary-legislation",
    "regulations": "secondary-legislation",
    "secondary": "secondary-legislation",
    "secondary-legislation": "secondary-legislation",
    "secondary_legislation": "secondary-legislation",
}

API_TYPE = {
    "act": "act",
    "bill": "bill",
    "secondary-legislation": "secondary_legislation",
}


class CliError(RuntimeError):
    def __init__(self, message: str, *, code: str = "error", source_url: str | None = None):
        super().__init__(message)
        self.code = code
        self.source_url = source_url


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def normalise_text(value: Any) -> str:
    text = html.unescape(str(value or "")).replace("\xa0", " ")
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def to_absolute(url_or_path: str) -> str:
    return urllib.parse.urljoin(BASE_URL, html.unescape(url_or_path))


def clamp_limit(limit: int) -> int:
    if limit < 1:
        return 1
    return min(limit, MAX_LIMIT)


def parse_iso_or_none(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        return dt.datetime.fromisoformat(value)
    except ValueError:
        return None


def nz_date_to_iso(value: str | None) -> str | None:
    if not value:
        return None
    clean = normalise_text(value)
    clean = re.sub(r"\s*\(.*?\)\s*$", "", clean)
    for fmt in ("%d %B %Y", "%d %b %Y"):
        try:
            return dt.datetime.strptime(clean, fmt).date().isoformat()
        except ValueError:
            pass
    return None


def fetch_bytes(
    url: str,
    *,
    timeout: int = DEFAULT_TIMEOUT,
    accept: str = "text/html,application/xml,application/json,*/*;q=0.8",
    method: str = "GET",
    extra_headers: dict[str, str] | None = None,
) -> tuple[bytes, str, str]:
    headers = {"Accept-Language": "en-NZ,en;q=0.9"}
    if extra_headers:
        headers.update(extra_headers)
    try:
        body, content_type, final_url = nzfetch.fetch_bytes(
            url,
            timeout=timeout,
            accept=accept,
            headers=headers,
            method=method,
            allowed_hosts=ALLOWED_HOSTS,
        )
        return body, final_url, content_type
    except nzfetch.Blocked as exc:
        text = str(exc).lower()
        code = "upstream_bot_protection" if ("robot" in text or "incapsula" in text or "challenge" in text) else "upstream_blocked"
        raise CliError(f"network error contacting upstream. {exc}", code=code, source_url=url) from exc
    except nzfetch.FetchError as exc:
        text = str(exc)
        if "401" in text and "api.legislation.govt.nz" in url:
            raise CliError(
                "PCO developer API key is required; set LEGISLATION_NZ_API_KEY or use --source web where supported",
                code="api_key_required",
                source_url=url,
            ) from exc
        if "429" in text:
            raise CliError("upstream rate limit returned HTTP 429", code="upstream_rate_limited", source_url=url) from exc
        raise CliError(f"upstream fetch failed. {exc}", code="upstream_http", source_url=url) from exc


def fetch_text(url: str, *, timeout: int = DEFAULT_TIMEOUT, accept: str = "text/html,*/*;q=0.8") -> tuple[str, str]:
    body, final_url, _ = fetch_bytes(url, timeout=timeout, accept=accept)
    return body.decode("utf-8", errors="replace"), final_url


def fetch_json(
    url: str,
    *,
    timeout: int = DEFAULT_TIMEOUT,
    method: str = "GET",
    extra_headers: dict[str, str] | None = None,
) -> tuple[dict[str, Any], str]:
    body, final_url, _ = fetch_bytes(
        url,
        timeout=timeout,
        accept="application/json,*/*;q=0.8",
        method=method,
        extra_headers=extra_headers,
    )
    try:
        return json.loads(body.decode("utf-8")), final_url
    except json.JSONDecodeError as exc:
        raise CliError("upstream returned non-JSON data", code="upstream_parse_error", source_url=final_url) from exc


def type_from_user(value: str | None) -> str | None:
    if not value:
        return None
    key = value.strip().lower().replace("_", "-")
    if key not in TYPE_ALIASES:
        raise CliError(f"unsupported legislation type: {value}", code="bad_input")
    return TYPE_ALIASES[key]


def split_legislation_path(url_or_path: str) -> dict[str, str] | None:
    parsed = urllib.parse.urlsplit(url_or_path)
    path = parsed.path if parsed.scheme else url_or_path
    parts = [urllib.parse.unquote(p) for p in path.strip("/").split("/") if p]
    if len(parts) < 4 or parts[0] not in {"act", "bill", "secondary-legislation", "amendment-paper"}:
        return None

    version = "latest"
    language = "en"
    if len(parts) >= 6 and parts[4] == "en":
        language = parts[4]
        version = parts[5]
    elif len(parts) >= 5:
        version = parts[4]

    version = re.sub(r"\.(xml|html|pdf)$", "", version)
    return {
        "type": parts[0],
        "subtype": parts[1],
        "year": parts[2],
        "number": parts[3],
        "language": language,
        "version": version or "latest",
    }


def parse_ref(raw: str, *, default_type: str = "act", default_subtype: str = "public") -> dict[str, str]:
    raw = raw.strip()
    from_path = split_legislation_path(raw)
    if from_path:
        return from_path

    work_match = re.match(
        r"^(act|bill|secondary-legislation|amendment-paper)_([^_]+)_([^_]+)_([^_]+)(?:_en_([^_]+))?$",
        raw,
    )
    if work_match:
        return {
            "type": work_match.group(1),
            "subtype": work_match.group(2),
            "year": work_match.group(3),
            "number": work_match.group(4),
            "language": "en",
            "version": work_match.group(5) or "latest",
        }

    year_number = re.match(r"^(~?\d{4})/([~\w-]+)$", raw)
    if year_number:
        return {
            "type": default_type,
            "subtype": default_subtype,
            "year": year_number.group(1),
            "number": year_number.group(2),
            "language": "en",
            "version": "latest",
        }

    raise CliError(
        "legislation reference must be a year/number pair, work_id, version_id, or legislation.govt.nz URL",
        code="bad_input",
    )


def work_id(ref: dict[str, str]) -> str:
    return f"{ref['type']}_{ref['subtype']}_{ref['year']}_{ref['number']}"


def version_id(ref: dict[str, str], as_at: str | None = None) -> str | None:
    version = as_at or ref.get("version")
    if not version or version == "latest":
        return None
    return f"{work_id(ref)}_{ref.get('language', 'en')}_{version}"


def canonical_url(ref: dict[str, str], *, version: str | None = None, fmt: str = "html") -> str:
    version = version or ref.get("version") or "latest"
    base = f"{BASE_URL}/{ref['type']}/{ref['subtype']}/{ref['year']}/{ref['number']}/{ref.get('language', 'en')}"
    if fmt == "xml":
        return f"{base}/{version}.xml/"
    if fmt == "pdf":
        return f"{base}/{version}.pdf"
    return f"{base}/{version}/"


def ref_from_url(url: str) -> dict[str, str] | None:
    return split_legislation_path(url)


def load_xml(raw_ref: str, *, version: str | None, timeout: int) -> tuple[ET.Element, dict[str, str], str]:
    ref = parse_ref(raw_ref)
    if version:
        ref["version"] = version
    url = canonical_url(ref, fmt="xml")
    body, final_url, content_type = fetch_bytes(url, timeout=timeout, accept="application/xml,text/xml,*/*;q=0.8")
    if "html" in content_type and b"<act" not in body[:1000].lower():
        raise CliError(
            "upstream returned HTML instead of legislation XML; this may be a bot-protection or not-found page",
            code="upstream_unexpected_html",
            source_url=final_url,
        )
    try:
        root = ET.fromstring(body)
    except ET.ParseError as exc:
        raise CliError("could not parse legislation XML", code="upstream_parse_error", source_url=final_url) from exc
    return root, ref, final_url


def child_text(element: ET.Element, tag: str) -> str | None:
    child = element.find(tag)
    if child is None:
        return None
    return normalise_text(" ".join(child.itertext()))


def element_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return normalise_text(" ".join(element.itertext()))


def act_metadata(root: ET.Element, ref: dict[str, str], xml_url: str) -> dict[str, Any]:
    as_at = root.attrib.get("date.as.at")
    title = child_text(root, "cover/title") or child_text(root, "cover/cover.title") or child_text(root, "title")
    admin = None
    admin_el = root.find(".//admin-office")
    if admin_el is not None:
        admin = element_text(admin_el)

    resolved_version = as_at if as_at and as_at != "nulldate" else ref.get("version")
    return {
        "title": title,
        "work_id": work_id(ref),
        "version_id": version_id(ref, resolved_version),
        "type": ref["type"],
        "subtype": ref["subtype"],
        "year": root.attrib.get("year") or ref["year"].lstrip("~"),
        "number": root.attrib.get("act.no") or root.attrib.get("reg.no") or root.attrib.get("number") or ref["number"].lstrip("~"),
        "as_at": as_at if as_at and as_at != "nulldate" else None,
        "assent": root.attrib.get("date.assent"),
        "terminated": None if root.attrib.get("date.terminated") == "nulldate" else root.attrib.get("date.terminated"),
        "administered_by": admin,
        "source_url": canonical_url(ref, version=ref.get("version", "latest"), fmt="html"),
        "xml_url": xml_url,
        "pdf_url": canonical_url(ref, version=resolved_version or ref.get("version", "latest"), fmt="pdf"),
    }


def section_rows(root: ET.Element, *, limit: int | None = None) -> tuple[list[dict[str, Any]], int]:
    rows: list[dict[str, Any]] = []
    for prov in root.findall(".//prov"):
        label = child_text(prov, "label")
        heading = child_text(prov, "heading")
        if not label and not heading:
            continue
        rows.append(
            {
                "label": label,
                "heading": heading,
                "xml_id": prov.attrib.get("id"),
            }
        )
    total = len(rows)
    if limit is not None:
        rows = rows[:limit]
    return rows, total


SCHEDULE_QUERY_RE = re.compile(
    r"^(?:schedule|sched|sch)\.?\s*([0-9A-Za-z]+)"
    r"(?:\s*(?:clause|cl|c)\.?\s*([0-9A-Za-z()]+))?$",
    flags=re.I,
)


def _norm_label(value: str | None) -> str | None:
    if not value:
        return None
    return re.sub(r"\s+", "", value).lower()


def find_schedule(root: ET.Element, wanted: str) -> ET.Element | None:
    for sched in root.iter("schedule"):
        if _norm_label(child_text(sched, "label")) == wanted:
            return sched
    return None


def find_section(root: ET.Element, section: str) -> ET.Element | None:
    """Resolve a section, a schedule, or a clause within a schedule.

    Schedules live in a separate <schedule> tree, not under <prov>, so a bare
    ``.//prov`` walk silently misses them (e.g. Schedule 7 of the Companies
    Act 1993). Explicit "Schedule N" queries resolve against schedules only;
    bare labels prefer body sections, then fall back to schedules.
    """
    raw = section.strip()
    wanted = _norm_label(raw)
    if not wanted:
        return None

    sched_match = SCHEDULE_QUERY_RE.match(raw)
    if sched_match:
        sched = find_schedule(root, _norm_label(sched_match.group(1)))
        if sched is None:
            return None
        clause = _norm_label(sched_match.group(2))
        if not clause:
            return sched
        for prov in sched.iter("prov"):
            if _norm_label(child_text(prov, "label")) == clause:
                return prov
        return None

    # Body sections take precedence over identically-labelled schedule clauses.
    schedule_provs = {id(prov) for sched in root.iter("schedule") for prov in sched.iter("prov")}
    fallback = None
    for prov in root.findall(".//prov"):
        if _norm_label(child_text(prov, "label")) != wanted:
            continue
        if id(prov) not in schedule_provs:
            return prov
        fallback = fallback or prov
    return fallback or find_schedule(root, wanted)


def owning_schedule(root: ET.Element | None, prov: ET.Element) -> ET.Element | None:
    """Return the <schedule> containing ``prov``, if any."""
    if root is None or prov.tag == "schedule":
        return None
    for sched in root.iter("schedule"):
        for child in sched.iter("prov"):
            if child is prov:
                return sched
    return None


def section_payload(
    prov: ET.Element, act: dict[str, Any], root: ET.Element | None = None
) -> dict[str, Any]:
    label = child_text(prov, "label")
    heading = child_text(prov, "heading")
    schedule_label = None
    if prov.tag == "schedule":
        body = prov.find("schedule.provisions")
        kind = "schedule"
        schedule_label = f"Schedule {label}" if label else "Schedule"
        label = schedule_label
    else:
        body = prov.find("prov.body")
        sched = owning_schedule(root, prov)
        if sched is not None:
            # A clause inside a schedule is NOT a body section; labelling it
            # "section" is how duplicate labels end up misattributed.
            kind = "schedule-clause"
            sched_label = child_text(sched, "label")
            schedule_label = f"Schedule {sched_label}" if sched_label else "Schedule"
            label = f"{schedule_label} clause {label}" if label else schedule_label
        else:
            kind = "section"
    text = element_text(body if body is not None else prov)
    history = [element_text(note) for note in prov.findall(".//history-note")]
    xml_id = prov.attrib.get("id")
    source_url = act["source_url"] + (f"#{xml_id}" if xml_id else "")
    payload = {
        "label": label,
        "kind": kind,
        "heading": heading,
        "xml_id": xml_id,
        "text": text,
        "history_notes": history,
        "source_url": source_url,
    }
    if kind == "schedule-clause":
        payload["schedule"] = schedule_label
    return payload


def parse_total(html_text: str) -> int | None:
    match = re.search(r"has returned\s+([\d,]+)\s+results?", html_text, flags=re.I)
    if not match:
        return None
    return int(match.group(1).replace(",", ""))


def href_to_item(href: str, title: str, block: str) -> dict[str, Any]:
    url = to_absolute(href)
    ref = ref_from_url(url)
    kind = ref["type"] if ref else None
    as_at_match = re.search(r"as at\s+([0-9]{1,2}\s+[A-Za-z]+\s+[0-9]{4}(?:\s+\([^)]*\))?)", block)
    as_at = nz_date_to_iso(as_at_match.group(1)) if as_at_match else None
    block_text = normalise_text(block)
    status: list[str] = []
    for label in ("Latest version", "Previous version", "In force", "Not in force", "Current", "Enacted", "Terminated"):
        if re.search(rf"\b{re.escape(label)}\b", block_text, flags=re.I):
            status.append(label.lower().replace(" ", "_"))
    return {
        "title": normalise_text(title),
        "url": url,
        "work_id": work_id(ref) if ref else None,
        "type": kind,
        "subtype": ref["subtype"] if ref else None,
        "year": ref["year"] if ref else None,
        "number": ref["number"] if ref else None,
        "as_at": as_at,
        "status": status,
    }


def parse_search_cards(html_text: str, *, limit: int) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    seen: set[str] = set()
    anchor_re = re.compile(
        r'<a[^>]+class="[^"]*\blink-visited-style\b[^"]*"[^>]+href="([^"]+)"[^>]*>\s*'
        r'<h3[^>]*class="[^"]*\blegislation-card__title\b[^"]*"[^>]*>(.*?)</h3>',
        flags=re.I | re.S,
    )
    for match in anchor_re.finditer(html_text):
        href = html.unescape(match.group(1))
        if not href.startswith(("/act/", "/bill/", "/secondary-legislation/", "https://www.legislation.govt.nz/")):
            continue
        title = match.group(2)
        card_start = html_text.rfind('<div class="legislation-card card', 0, match.start())
        next_card = html_text.find('<div class="legislation-card card', match.end())
        card_end = next_card if next_card != -1 else min(len(html_text), match.end() + 2500)
        block = html_text[card_start:card_end] if card_start != -1 else html_text[match.start() : card_end]
        item = href_to_item(href, title, block)
        if item["url"] in seen:
            continue
        seen.add(item["url"])
        results.append(item)
        if len(results) >= limit:
            break
    return results


def web_search(
    *,
    query: str | None,
    legislation_type: str | None,
    search_field: str,
    bill_status: str | None,
    sort_by: str | None,
    limit: int,
    timeout: int,
) -> dict[str, Any]:
    params: dict[str, str] = {
        "per_page": str(clamp_limit(limit)),
        "search_field": search_field,
    }
    if query:
        params["search_term"] = query
    if legislation_type:
        params["legislation_type"] = legislation_type
        if legislation_type == "bill":
            params["search_for"] = "bill"
    if bill_status:
        params["bill_status"] = bill_status
    if sort_by:
        params["sort_by"] = sort_by

    url = BASE_URL + "/items/?" + urllib.parse.urlencode(params)
    html_text, final_url = fetch_text(url, timeout=timeout)
    return {
        "source": "legislation.govt.nz web search",
        "source_url": final_url,
        "total": parse_total(html_text),
        "results": parse_search_cards(html_text, limit=limit),
    }


def api_key() -> str | None:
    return os.environ.get("LEGISLATION_NZ_API_KEY") or os.environ.get("PCO_API_KEY")


def api_search(
    *,
    query: str | None,
    legislation_type: str | None,
    search_field: str,
    sort_by: str | None,
    limit: int,
    timeout: int,
) -> dict[str, Any]:
    key = api_key()
    if not key:
        raise CliError(
            "PCO developer API key is required; request one from contact@pco.govt.nz and set LEGISLATION_NZ_API_KEY",
            code="api_key_required",
            source_url=f"{API_BASE_URL}/v0/works/",
        )
    params: dict[str, str] = {
        "per_page": str(clamp_limit(limit)),
        "search_field": search_field,
    }
    if query:
        params["search_term"] = query
    if legislation_type:
        params["legislation_type"] = API_TYPE[legislation_type]
    if sort_by:
        params["sort_by"] = sort_by
    url = f"{API_BASE_URL}/v0/works/?" + urllib.parse.urlencode(params)
    data, final_url = fetch_json(url, timeout=timeout, extra_headers={"X-Api-Key": key})
    rows = []
    for item in data.get("results", [])[:limit]:
        latest = item.get("latest_matching_version") or {}
        formats = latest.get("formats") or []
        rows.append(
            {
                "title": latest.get("title"),
                "url": next((f.get("url") for f in formats if f.get("type") == "html"), None),
                "work_id": item.get("work_id"),
                "version_id": latest.get("version_id"),
                "type": item.get("legislation_type"),
                "status": item.get("legislation_status"),
                "is_latest_version": latest.get("is_latest_version"),
                "formats": formats,
            }
        )
    return {
        "source": "api.legislation.govt.nz v0 works",
        "source_url": final_url,
        "total": data.get("total"),
        "results": rows,
    }


def parse_version_cards(html_text: str, *, limit: int) -> list[dict[str, Any]]:
    versions: list[dict[str, Any]] = []
    starts = [m.start() for m in re.finditer(r'<div class="card mb-3 version-card[^"]*" id="version-[^"]+">', html_text)]
    for index, start in enumerate(starts[:limit]):
        end = starts[index + 1] if index + 1 < len(starts) else min(len(html_text), start + 7000)
        block = html_text[start:end]
        id_match = re.search(r'id="version-([^"]+)"', block)
        anchor = re.search(
            r'<a[^>]+class="[^"]*\blink-visited-style\b[^"]*"[^>]+href="([^"]+)"[^>]*>\s*'
            r'<h3[^>]*class="[^"]*\blegislation-card__title\b[^"]*"[^>]*>(.*?)</h3>',
            block,
            flags=re.I | re.S,
        )
        date_value = id_match.group(1) if id_match else None
        status = "latest" if "Latest version" in normalise_text(block) else "previous"
        amendments = []
        for amendment in re.findall(
            r'<div[^>]+class="[^"]*\bincorporated-amendments?\b[^"]*"[^>]*>(.*?)</div>',
            block,
            flags=re.I | re.S,
        ):
            text = normalise_text(amendment)
            if text:
                amendments.append(text)
        versions.append(
            {
                "as_at": date_value,
                "title": normalise_text(anchor.group(2)) if anchor else None,
                "url": to_absolute(anchor.group(1)) if anchor else None,
                "status": status,
                "pdf_url": to_absolute(re.search(r'href="([^"]+\.pdf)"', block).group(1))
                if re.search(r'href="([^"]+\.pdf)"', block)
                else None,
                "incorporated_amendments": amendments,
            }
        )
    return versions


def version_list_url(ref: dict[str, str], root: ET.Element, *, limit: int) -> str:
    as_at = root.attrib.get("date.as.at") or ref.get("version")
    if not as_at or as_at == "latest" or as_at == "nulldate":
        as_at = ref.get("version", "latest")
    per_page = min(max(limit, 1), 50)
    base = canonical_url(ref, version=as_at, fmt="html").rstrip("/")
    return f"{base}/versions/?per_page={per_page}"


def rss_feed(params: dict[str, str], *, timeout: int) -> tuple[str, bytes | None]:
    url = BASE_URL + "/api_keys/?" + urllib.parse.urlencode(params)
    body, final_url, content_type = fetch_bytes(
        url,
        timeout=timeout,
        accept="application/json,application/atom+xml,application/xml,text/xml,*/*;q=0.8",
        method="POST",
    )
    if "xml" in content_type or body.lstrip().startswith(b"<?xml"):
        return final_url, body
    try:
        data = json.loads(body.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise CliError("official RSS generator returned neither JSON nor XML", code="upstream_parse_error", source_url=final_url) from exc
    feed_url = data.get("url")
    if not feed_url:
        raise CliError("official RSS generator did not return a feed URL", code="upstream_parse_error", source_url=url)
    return feed_url, None


def parse_atom_feed(xml_text: bytes) -> list[dict[str, Any]]:
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise CliError("could not parse official RSS/Atom feed", code="upstream_parse_error") from exc
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entries: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", ns):
        link = entry.find("atom:link", ns)
        url = link.attrib.get("href") if link is not None else entry.findtext("atom:id", default="", namespaces=ns)
        published = entry.findtext("atom:published", default=None, namespaces=ns)
        updated = entry.findtext("atom:updated", default=None, namespaces=ns)
        content = entry.findtext("atom:content", default="", namespaces=ns)
        ref = ref_from_url(url or "")
        entries.append(
            {
                "title": normalise_text(entry.findtext("atom:title", default="", namespaces=ns)),
                "url": url,
                "work_id": work_id(ref) if ref else None,
                "type": ref["type"] if ref else None,
                "published": published,
                "updated": updated,
                "summary": normalise_text(content),
            }
        )
    return entries


def output(data: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    command = data.get("command")
    if command == "get-act":
        act = data["act"]
        print(f"{act.get('title')} ({act.get('year')} No {act.get('number')})")
        print(f"as at: {act.get('as_at') or '-'} | source: {act.get('source_url')}")
        print(f"sections shown: {len(data.get('sections', []))} of {data.get('sections_total', 0)}")
        for row in data.get("sections", [])[:20]:
            label = row.get("label") or "-"
            heading = row.get("heading") or ""
            print(f"- {label}: {heading}")
    elif command == "get-section":
        act = data["act"]
        section = data["section"]
        print(f"{act.get('title')} section {section.get('label')}: {section.get('heading')}")
        print(section.get("text") or "")
        print(f"source: {section.get('source_url')}")
    elif command in {"search", "list-bills", "updates"}:
        print(f"{command}: {data.get('total', len(data.get('results', [])))} result(s)")
        for item in data.get("results", [])[: data.get("limit", DEFAULT_LIMIT)]:
            date = item.get("as_at") or item.get("published") or item.get("updated") or "-"
            print(f"- {item.get('title')} [{date}]")
            if item.get("url"):
                print(f"  {item['url']}")
    elif command == "versions":
        act = data["act"]
        print(f"{act.get('title')}: {len(data.get('versions', []))} version(s)")
        for item in data.get("versions", []):
            print(f"- {item.get('as_at')}: {item.get('status')} {item.get('url') or ''}")
    elif command == "sources":
        print("legislation-nz official sources:")
        for item in data["sources"]:
            print(f"- {item['name']}: {item['url']}")
            print(f"  {item['note']}")
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def output_error(exc: CliError, args: argparse.Namespace) -> None:
    if getattr(args, "json", False):
        print(
            json.dumps(
                {
                    "command": getattr(args, "command", None),
                    "status": "error",
                    "error": exc.code,
                    "message": str(exc),
                    "source_url": exc.source_url,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
        return

    detail = f"legislation-nz: {exc.code}: {exc}"
    if exc.source_url:
        detail += f" (source: {exc.source_url})"
    print(detail, file=sys.stderr)


def cmd_get_act(args: argparse.Namespace) -> None:
    root, ref, xml_url = load_xml(args.act_id, version=args.version, timeout=args.timeout)
    act = act_metadata(root, ref, xml_url)
    section_limit = None if args.all_sections else args.sections_limit
    sections, total = section_rows(root, limit=section_limit)
    output(
        {
            "command": "get-act",
            "status": "ok",
            "retrieved_at": now_iso(),
            "source": "legislation.govt.nz XML format",
            "act": act,
            "sections_total": total,
            "sections_truncated": section_limit is not None and total > len(sections),
            "sections": sections,
        },
        args.json,
    )


def cmd_get_section(args: argparse.Namespace) -> None:
    root, ref, xml_url = load_xml(args.act_id, version=args.version, timeout=args.timeout)
    act = act_metadata(root, ref, xml_url)
    prov = find_section(root, args.section)
    if prov is None:
        raise CliError(f"section {args.section} not found in {act.get('title') or args.act_id}", code="not_found", source_url=act["source_url"])
    output(
        {
            "command": "get-section",
            "status": "ok",
            "retrieved_at": now_iso(),
            "source": "legislation.govt.nz XML format",
            "act": act,
            "section": section_payload(prov, act, root),
        },
        args.json,
    )


def cmd_search(args: argparse.Namespace) -> None:
    legislation_type = type_from_user(args.type)
    source = args.source
    if source == "auto":
        source = "api" if api_key() else "web"
    if source == "api":
        data = api_search(
            query=args.query,
            legislation_type=legislation_type,
            search_field=args.field,
            sort_by=args.sort,
            limit=args.limit,
            timeout=args.timeout,
        )
    else:
        data = web_search(
            query=args.query,
            legislation_type=legislation_type,
            search_field=args.field,
            bill_status=None,
            sort_by=args.sort,
            limit=args.limit,
            timeout=args.timeout,
        )
    output(
        {
            "command": "search",
            "status": "ok",
            "retrieved_at": now_iso(),
            "query": args.query,
            "type": legislation_type,
            "field": args.field,
            "limit": args.limit,
            **data,
        },
        args.json,
    )


def cmd_versions(args: argparse.Namespace) -> None:
    root, ref, xml_url = load_xml(args.act_id, version=args.version, timeout=args.timeout)
    act = act_metadata(root, ref, xml_url)
    url = version_list_url(ref, root, limit=args.limit)
    html_text, final_url = fetch_text(url, timeout=args.timeout)
    versions = parse_version_cards(html_text, limit=args.limit)
    output(
        {
            "command": "versions",
            "status": "ok",
            "retrieved_at": now_iso(),
            "source": "legislation.govt.nz versions page",
            "source_url": final_url,
            "act": act,
            "limit": args.limit,
            "versions": versions,
        },
        args.json,
    )


def cmd_updates(args: argparse.Namespace) -> None:
    since_dt = parse_iso_or_none(args.since)
    if since_dt is None:
        raise CliError("--since must be an ISO date or datetime, for example 2026-07-01", code="bad_input")
    if since_dt.tzinfo is None:
        since_dt = since_dt.replace(tzinfo=dt.timezone.utc)

    params = {"id": "search"}
    legislation_type = type_from_user(args.type)
    if legislation_type:
        params["legislation_type"] = legislation_type
    feed_url, body = rss_feed(params, timeout=args.timeout)
    final_url = feed_url
    if body is None:
        body, final_url, _ = fetch_bytes(feed_url, timeout=args.timeout, accept="application/atom+xml,application/xml,text/xml,*/*;q=0.8")
    entries = parse_atom_feed(body)
    filtered = []
    for entry in entries:
        updated = parse_iso_or_none(entry.get("updated")) or parse_iso_or_none(entry.get("published"))
        if updated and updated >= since_dt:
            filtered.append(entry)
        if len(filtered) >= args.limit:
            break
    output(
        {
            "command": "updates",
            "status": "ok",
            "retrieved_at": now_iso(),
            "source": "legislation.govt.nz generated Atom feed",
            "source_url": final_url,
            "since": args.since,
            "type": legislation_type,
            "limit": args.limit,
            "total": len(filtered),
            "results": filtered,
        },
        args.json,
    )


def cmd_list_bills(args: argparse.Namespace) -> None:
    data = web_search(
        query=args.query,
        legislation_type="bill",
        search_field="title",
        bill_status="current" if args.current else None,
        sort_by=args.sort,
        limit=args.limit,
        timeout=args.timeout,
    )
    output(
        {
            "command": "list-bills",
            "status": "ok",
            "retrieved_at": now_iso(),
            "current_only": args.current,
            "query": args.query,
            "limit": args.limit,
            **data,
        },
        args.json,
    )


def cmd_sources(args: argparse.Namespace) -> None:
    output(
        {
            "command": "sources",
            "status": "ok",
            "retrieved_at": now_iso(),
            "sources": [
                {
                    "name": "New Zealand Legislation website",
                    "url": BASE_URL,
                    "note": "Official home for New Zealand Acts, Bills, and secondary legislation; keyless HTML and XML format URLs are used by this skill.",
                },
                {
                    "name": "PCO developer API",
                    "url": f"{API_BASE_URL}/docs/",
                    "note": "Supported API with /v0/works, /v0/works/{work_id}/versions, and /v0/versions/{version_id}; requires a free API key requested from contact@pco.govt.nz.",
                },
                {
                    "name": "Official web feeds",
                    "url": f"{BASE_URL}/learn-more/find-and-use-legislation/keep-up-to-date-with-legislation/",
                    "note": "Official generated Atom feeds for updates; this skill requests a feed URL through the public website endpoint.",
                },
                {
                    "name": "Bulk XML dataset catalogue",
                    "url": "https://catalogue.data.govt.nz/dataset/new-zealand-legislation",
                    "note": "Catalogue entry for the whole-corpus XML directory and related resources; availability may be affected by bot protection.",
                },
            ],
        },
        args.json,
    )


def add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="network timeout in seconds (default: 10)")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query official New Zealand legislation sources")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("get-act", help="fetch Act metadata and section headings from official XML")
    p.add_argument("act_id", help="year/number, work_id, version_id, or legislation.govt.nz URL")
    p.add_argument("--version", default=None, help="version date YYYY-MM-DD, or latest")
    p.add_argument("--sections-limit", type=int, default=200, help="maximum section headings to include")
    p.add_argument("--all-sections", action="store_true", help="include all section headings")
    add_common(p)
    p.set_defaults(func=cmd_get_act)

    p = sub.add_parser("get-section", help="fetch one section from official XML")
    p.add_argument("act_id", help="year/number, work_id, version_id, or legislation.govt.nz URL")
    p.add_argument("section", help="section label, for example 5 or 83ZE")
    p.add_argument("--version", default=None, help="version date YYYY-MM-DD, or latest")
    add_common(p)
    p.set_defaults(func=cmd_get_section)

    p = sub.add_parser("search", help="search official legislation records")
    p.add_argument("query", help="search keywords")
    p.add_argument("--type", choices=["act", "bill", "regulation", "secondary-legislation"], default=None)
    p.add_argument("--field", choices=["title", "content"], default="title")
    p.add_argument("--sort", choices=["relevance", "title_asc", "title_desc", "year_asc", "year_desc", "most_recently_updated"], default=None)
    p.add_argument("--source", choices=["auto", "web", "api"], default="auto", help="auto uses API when LEGISLATION_NZ_API_KEY is set, otherwise web")
    p.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    add_common(p)
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("versions", help="list point-in-time versions for a work")
    p.add_argument("act_id", help="year/number, work_id, version_id, or legislation.govt.nz URL")
    p.add_argument("--version", default=None, help="starting version date, or latest")
    p.add_argument("--limit", type=int, default=25)
    add_common(p)
    p.set_defaults(func=cmd_versions)

    p = sub.add_parser("updates", help="list official feed updates since a date")
    p.add_argument("--since", required=True, help="ISO date/datetime, for example 2026-07-01")
    p.add_argument("--type", choices=["act", "bill", "regulation", "secondary-legislation"], default=None)
    p.add_argument("--limit", type=int, default=20)
    add_common(p)
    p.set_defaults(func=cmd_updates)

    p = sub.add_parser("list-bills", help="list Bills currently before Parliament")
    p.add_argument("query", nargs="?", default=None, help="optional title search")
    p.add_argument("--all-statuses", dest="current", action="store_false", help="include enacted and terminated Bills too")
    p.add_argument("--sort", choices=["relevance", "title_asc", "title_desc", "year_asc", "year_desc", "most_recently_updated"], default="most_recently_updated")
    p.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    add_common(p)
    p.set_defaults(func=cmd_list_bills, current=True)

    p = sub.add_parser("sources", aliases=["datasets"], help="describe official data sources and caveats")
    add_common(p)
    p.set_defaults(func=cmd_sources)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except CliError as exc:
        output_error(exc, args)
        raise SystemExit(1)
    except KeyboardInterrupt:
        print("legislation-nz: interrupted", file=sys.stderr)
        raise SystemExit(130)


if __name__ == "__main__":
    main()
