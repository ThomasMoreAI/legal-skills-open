"""Parse official New Zealand Parliament select-committee pages."""
from __future__ import annotations

import re
from datetime import datetime
from html import unescape
from urllib.parse import urljoin, urlparse
from zoneinfo import ZoneInfo

HOSTS = {"www.parliament.nz", "www3.parliament.nz"}


def _listing_kind(source_path: str) -> str:
    if "/make-a-submission/" in source_path:
        return "submissions"
    if "/business-before-committees" in source_path:
        return "business"
    if "/evidence-submissions" in source_path:
        return "evidence"
    if "/reports/" in source_path:
        return "reports"
    if source_path.rstrip("/").endswith("/scl"):
        return "committees"
    return "unknown"


def _is_record_path(kind: str, path: str) -> bool:
    path = path.rstrip("/")
    prefixes = {
        "submissions": ("/en/pb/sc/make-a-submission/document/",),
        "business": ("/en/pb/sc/business-before-committees/",),
        "evidence": ("/en/pb/sc/evidence-submissions/", "/en/pb/sc/submissions-and-advice/"),
        "reports": ("/en/pb/sc/reports/",),
        "committees": ("/en/pb/sc/scl/",),
    }.get(kind, ())
    return any(path.startswith(prefix) and len(path) > len(prefix.rstrip("/")) for prefix in prefixes)


def clean(value: str) -> str:
    value = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    return " ".join(unescape(re.sub(r"<[^>]+>", " ", value)).replace("\xa0", " ").split())


def parse_deadline(text: str) -> tuple[str | None, str | None, str | None]:
    closing = re.search(r"(?:close|closing)[^\d]{0,80}(\d{1,2}\s+[A-Za-z]+\s+\d{4}(?:\s+(?:at\s+)?\d{1,2}(?:[.:]\d{2})?\s*(?:am|pm))?)", text, re.I)
    candidate = closing.group(1) if closing else text
    match = re.search(r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})(?:\s+(?:at\s+)?(\d{1,2})(?:[.:](\d{2}))?\s*(am|pm))?", candidate, re.I)
    if not match:
        return None, None, None
    try:
        day = datetime.strptime(" ".join(match.group(i) for i in (1, 2, 3)), "%d %B %Y")
    except ValueError:
        return None, None, None
    date_value = day.date().isoformat()
    if not match.group(4):
        return date_value, None, None
    hour = int(match.group(4)) % 12 + (12 if match.group(6).casefold() == "pm" else 0)
    minute = int(match.group(5) or 0)
    local = day.replace(hour=hour, minute=minute, tzinfo=ZoneInfo("Pacific/Auckland"))
    return date_value, local.isoformat(), "Pacific/Auckland"


def parse_listing(html: str, source_url: str, retrieved_at: str) -> list[dict[str, object]]:
    if re.search(r"radware|captcha page|hcaptcha|awswaf", html, re.I):
        raise ValueError("Parliament source returned an access challenge")
    host = urlparse(source_url).hostname
    kind = _listing_kind(urlparse(source_url).path)
    if kind == "unknown":
        raise ValueError("Parliament listing URL was not a supported select-committee route")
    rows: list[dict[str, object]] = []
    blocks = re.findall(r"<(tr|li|article)\b[^>]*>(.*?)</\1>", html, re.I | re.S)
    for _, block in blocks:
        link = re.search(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', block, re.I | re.S)
        if not link: continue
        url = urljoin(source_url, unescape(link.group(1)))
        if urlparse(url).hostname not in HOSTS | {host}: continue
        if not _is_record_path(kind, urlparse(url).path): continue
        title, context = clean(link.group(2)), clean(block)
        if not title or title.casefold() in {"rss", "next", "previous", "view all"}: continue
        cells = [clean(value) for value in re.findall(r"<td\b[^>]*>(.*?)</td>", block, re.I | re.S)]
        closing_date, closing_at, timezone = parse_deadline(context)
        if kind == "submissions" and (len(cells) < 2 or not closing_date or "submission" not in context.casefold()):
            continue
        if kind == "reports" and not closing_date:
            continue
        rows.append({
            "id": urlparse(url).path.rstrip("/").split("/")[-1], "title": title,
            "committee": cells[1] if len(cells) > 2 else None,
            "date": closing_date, "closing_date": closing_date, "closing_at": closing_at, "timezone": timezone,
            "status": "open" if "submissions are now being invited" in context.casefold() else None,
            "context": context[:1200], "source_url": url, "retrieved_at": retrieved_at,
        })
    dedup = {str(row["source_url"]): row for row in rows}
    if not dedup and not re.search(r"No items were found|Displaying 0", html, re.I):
        raise ValueError("Parliament listing contained no recognisable records")
    return list(dedup.values())


def parse_detail(html: str, source_url: str, retrieved_at: str) -> dict[str, object]:
    if re.search(r"radware|captcha page|hcaptcha|awswaf", html, re.I):
        raise ValueError("Parliament source returned an access challenge")
    heading = re.search(r"<h1\b[^>]*>(.*?)</h1>", html, re.I | re.S) or re.search(r"<h2\b[^>]*>(.*?)</h2>", html, re.I | re.S)
    if not heading:
        raise ValueError("Parliament detail page contained no item title")
    plain = clean(html)
    closing_date, closing_at, timezone = parse_deadline(plain)
    membership: list[dict[str, str]] = []
    membership_block = re.search(r"(?:Committee membership|Current membership|Members)(.*?)(?=<h[1-3]\b|$)", html, re.I | re.S)
    if membership_block:
        for item in re.findall(r"<li\b[^>]*>(.*?)</li>", membership_block.group(1), re.I | re.S):
            value = clean(item)
            if value:
                role = next((name for name in ("Chairperson", "Deputy Chairperson", "Member") if name.casefold() in value.casefold()), None)
                membership.append({"name": re.sub(r"\s*[-–—,:]?\s*(?:Chairperson|Deputy Chairperson|Member)\s*$", "", value, flags=re.I), "role": role or "Member"})
    evidence: list[dict[str, str]] = []
    for href, label in re.findall(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.I | re.S):
        url = urljoin(source_url, unescape(href))
        title = clean(label)
        if urlparse(url).hostname not in HOSTS or not title:
            continue
        if re.search(r"evidence|submission|transcript|briefing", f"{title} {url}", re.I) or urlparse(url).path.lower().endswith((".pdf", ".doc", ".docx")):
            evidence.append({"title": title, "url": url})
    return {
        "id": urlparse(source_url).path.rstrip("/").split("/")[-1], "title": clean(heading.group(1)),
        "closing_date": closing_date, "closing_at": closing_at, "timezone": timezone,
        "membership": membership, "evidence": list({item["url"]: item for item in evidence}.values()),
        "source_url": source_url, "retrieved_at": retrieved_at,
    }
