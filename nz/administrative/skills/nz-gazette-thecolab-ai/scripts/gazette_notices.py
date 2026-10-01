"""Parsers for the official New Zealand Gazette search and notice pages."""

from __future__ import annotations

import re
from datetime import datetime
from html import unescape
from urllib.parse import urljoin


def _text(value: str) -> str:
    value = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    value = re.sub(r"<(?:script|style)\b.*?</(?:script|style)>", " ", value, flags=re.I | re.S)
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(unescape(value).split())


def _title(value: str) -> str:
    """Use the visible title span, excluding commented previews and controls."""
    cleaned = re.sub(r"<!--.*?-->", " ", value, flags=re.S)
    span = re.search(r"<span\b[^>]*>(.*?)</span>", cleaned, flags=re.I | re.S)
    return _text(span.group(1) if span else cleaned).removesuffix("-->").strip()


def _date(value: str) -> str | None:
    parts = re.findall(r">\s*([^<>]+?)\s*</span>", value, flags=re.S)
    if len(parts) < 3:
        return None
    try:
        return datetime.strptime(" ".join(_text(part) for part in parts[:3]), "%d %b %Y").date().isoformat()
    except ValueError:
        return None


def parse_search(html: str, source_url: str, retrieved_at: str) -> list[dict[str, object]]:
    """Parse a Gazette result table without treating an unexpected blank page as success."""
    rows: list[dict[str, object]] = []
    for body in re.findall(r'<tr\b[^>]*class="[^"]*\bgroup\b[^"]*"[^>]*>(.*?)</tr>', html, flags=re.I | re.S):
        match = re.search(r'href="(/notice/id/([^"/?#]+))"[^>]*>(.*?)</a>', body, flags=re.I | re.S)
        cells = re.findall(r"<td\b[^>]*>(.*?)</td>", body, flags=re.I | re.S)
        if not match or len(cells) < 3:
            continue
        notice_id = unescape(match.group(2)).strip()
        title = _title(match.group(3))
        published_on = _date(cells[0])
        if not notice_id or not title or not published_on:
            continue
        acts = [_text(value) for value in re.findall(r"<span\b[^>]*>(.*?)</span>", cells[3], flags=re.I | re.S)] if len(cells) > 3 else []
        rows.append(
            {
                "id": notice_id,
                "title": title,
                "published_on": published_on,
                "notice_type": _text(cells[2]),
                "acts": [act for act in acts if act],
                "source_url": urljoin(source_url, match.group(1)),
                "retrieved_at": retrieved_at,
                "legal_effect": "not determined by this connector",
            }
        )
    if not rows and not re.search(r"no (notices|results) (were )?found", html, flags=re.I):
        raise ValueError("Gazette search page contained no recognisable result records")
    return rows


def notice_type_codes(html: str) -> dict[str, str]:
    select = re.search(r'<select\b[^>]*id="Form_NoticeSearch_noticeType"[^>]*>(.*?)</select>', html, flags=re.I | re.S)
    if not select:
        raise ValueError("Gazette notice-type selector was not found")
    values: dict[str, str] = {}
    for code, label in re.findall(r'<option\b[^>]*value="([^"]*)"[^>]*>(.*?)</option>', select.group(1), flags=re.I | re.S):
        name = _text(label)
        if code and name:
            values[name.casefold()] = unescape(code)
    return values


def parse_notice(html: str, source_url: str, retrieved_at: str) -> dict[str, object]:
    """Parse a full public notice while preserving official text and provenance."""
    notice = re.search(r'<div\b[^>]*class="[^"]*\bnotice\b[^"]*"[^>]*>(.*?)(?=<footer\b)', html, flags=re.I | re.S)
    title = re.search(r'<h2\b[^>]*class="[^"]*\bci-notice-title\b[^"]*"[^>]*>(.*?)</h2>', html, flags=re.I | re.S)
    ident = re.search(r"Notice Number\s*</h3>\s*</dt>\s*<dd\b[^>]*>(.*?)</dd>", html, flags=re.I | re.S)
    content = re.search(r'<div\b[^>]*class="[^"]*\bcontent\b[^"]*\bfont-serif\b[^"]*"[^>]*>(.*?)</div>', html, flags=re.I | re.S)
    date_block = re.search(r"Publication Date\s*</dt>\s*<dd\b[^>]*>(.*?)</dd>", html, flags=re.I | re.S)
    type_match = re.search(r"Notice Type\s*</dt>\s*<dd\b[^>]*>(.*?)</dd>", html, flags=re.I | re.S)
    if not notice or not title or not ident or not content or not date_block:
        raise ValueError("Gazette notice page did not match the expected public notice schema")
    notice_id = _text(ident.group(1))
    tags_block = re.search(r'<dd\b[^>]*class="[^"]*\btags\b[^"]*"[^>]*>(.*?)</dd>', notice.group(1), flags=re.I | re.S)
    tags = [_text(value) for value in re.findall(r"<a\b[^>]*>(.*?)</a>", tags_block.group(1), flags=re.I | re.S)] if tags_block else []
    pdf = re.search(r'href="([^"]*/notice/id/[^"/]+/pdf)"', html, flags=re.I)
    def meta(label: str) -> str | None:
        match = re.search(rf"{re.escape(label)}\s*</h3>\s*</dt>\s*<dd\b[^>]*>(.*?)</dd>", html, flags=re.I | re.S)
        return _text(match.group(1)) if match else None
    text = _text(content.group(1))
    authority_tags = [
        tag for tag in tags
        if re.search(r"\b(?:Authority|Commission|Ministry|Department|Council|Agency|Board|Registrar|Minister|Police|Office|Service|Corporation)\b", tag, re.I)
    ]
    relationships: list[dict[str, str]] = []
    for sentence in re.split(r"(?<=[.!?])\s+", text):
        relation = next((word for word in ("amends", "amended", "revokes", "revoked", "corrects", "corrected", "replaces", "replaced") if re.search(rf"\b{word}\b", sentence, re.I)), None)
        if not relation:
            continue
        for related_id in re.findall(r"\b\d{4}-[a-z]{2}\d+\b", sentence, re.I):
            if related_id.casefold() != notice_id.casefold():
                relationships.append({"id": related_id, "relationship_text": relation, "context": sentence[:500]})
    return {
        "id": notice_id,
        "title": _text(title.group(1)),
        "published_on": _date(date_block.group(1)),
        "notice_type": _text(type_match.group(1)) if type_match else None,
        "tags": tags,
        "authority_tags": authority_tags,
        "issuing_authority": authority_tags[0] if len(authority_tags) == 1 else None,
        "related_notices": relationships,
        "page_number": meta("Page Number"),
        "issue_number": meta("Issue Number"),
        "text": text,
        "pdf_url": urljoin(source_url, pdf.group(1)) if pdf else None,
        "source_url": source_url,
        "retrieved_at": retrieved_at,
        "legal_effect": "not determined by this connector",
    }
