"""Parse the official New Zealand Government consultation listing."""

from __future__ import annotations

from datetime import datetime
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse


def _classes(attributes: list[tuple[str, str | None]]) -> set[str]:
    value = dict(attributes).get("class") or ""
    return set(value.split())


class _ConsultationParser(HTMLParser):
    def __init__(self, base_url: str, retrieved_at: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.retrieved_at = retrieved_at
        self.depth = 0
        self.item_depth: int | None = None
        self.item: dict[str, object] | None = None
        self.field_stack: list[tuple[int, str]] = []
        self.rows: list[dict[str, object]] = []
        self.anchor_depth: int | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.depth += 1
        classes = _classes(attrs)
        if tag == "div" and "cl-item" in classes and self.item is None:
            self.item_depth = self.depth
            self.item = {"retrieved_at": self.retrieved_at}
        if self.item is None:
            return
        field = next(
            (
                name
                for css, name in (
                    ("cli-title", "title"),
                    ("cli-agencies", "agency"),
                    ("cli-date", "date_text"),
                    ("cli-status", "status"),
                    ("cli-description", "summary"),
                    ("cli-link", "link"),
                )
                if css in classes
            ),
            None,
        )
        if field:
            self.field_stack.append((self.depth, field))
            self.item.setdefault(field, "")
        if tag == "a" and self.item is not None:
            href = dict(attrs).get("href")
            if href:
                self.item.setdefault("_links", [])
                self.item["_links"].append({"url": urljoin(self.base_url, href), "text": ""})
                self.anchor_depth = self.depth

    def handle_data(self, data: str) -> None:
        if self.item is not None and self.anchor_depth is not None and self.item.get("_links"):
            self.item["_links"][-1]["text"] += " " + data
        if self.item is None or not self.field_stack:
            return
        field = self.field_stack[-1][1]
        self.item[field] = str(self.item.get(field, "")) + " " + data

    def handle_endtag(self, tag: str) -> None:
        if self.item is not None:
            if tag == "a" and self.anchor_depth == self.depth:
                self.anchor_depth = None
            while self.field_stack and self.field_stack[-1][0] == self.depth:
                self.field_stack.pop()
            if tag == "div" and self.item_depth == self.depth:
                self._finish_item()
        self.depth -= 1

    def _finish_item(self) -> None:
        assert self.item is not None
        for field in ("title", "agency", "date_text", "status", "summary"):
            self.item[field] = " ".join(str(self.item.get(field, "")).split())
        links = self.item.pop("_links", [])
        for link in links:
            link["text"] = " ".join(str(link.get("text", "")).split())
        submission = next(
            (link["url"] for link in links if any(token in f"{link['text']} {link['url']}".casefold() for token in ("submit", "submission", "have your say", "survey"))),
            None,
        )
        detail = next((link["url"] for link in links if link["url"] != submission), None) or submission
        source_url = str(detail or "")
        if self.item["title"] and source_url:
            slug = urlparse(source_url).path.rstrip("/").split("/")[-1]
            self.item["id"] = slug or source_url
            self.item["status"] = str(self.item["status"]).lower()
            self.item.update(parse_date_range(str(self.item["date_text"])))
            self.item["closing_time_precision"] = "date_only"
            self.item["closing_timezone"] = None
            self.item["detail_url"] = detail
            self.item["submission_url"] = submission
            self.item["source_url"] = source_url
            self.item.pop("link", None)
            self.rows.append(self.item)
        self.item = None
        self.item_depth = None
        self.field_stack.clear()


def parse_date_range(value: str) -> dict[str, str | None]:
    """Parse listing ranges such as ``15 Jun to 28 Jul 2026``."""
    try:
        start_text, end_text = (part.strip() for part in value.split(" to ", 1))
        end = datetime.strptime(end_text, "%d %b %Y").date()
        start = datetime.strptime(f"{start_text} {end.year}", "%d %b %Y").date()
        if start > end:
            start = start.replace(year=start.year - 1)
        return {"opens_on": start.isoformat(), "closes_on": end.isoformat()}
    except (TypeError, ValueError):
        return {"opens_on": None, "closes_on": None}


def parse_consultations(html: str, source_url: str, retrieved_at: str) -> list[dict[str, object]]:
    parser = _ConsultationParser(source_url, retrieved_at)
    parser.feed(html)
    if not parser.rows:
        raise ValueError("Government consultation listing contained no consultation records")
    return parser.rows
