"""Parse official New Zealand Hansard listing and transcript pages."""
from __future__ import annotations

import re
import unicodedata
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse


class _Blocks(HTMLParser):
    BLOCKS = {"h1", "h2", "h3", "h4", "p", "li"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple[str, str]] = []
        self.current_tag: str | None = None
        self.current: list[str] = []
        self.title = ""
        self.in_title = False
        self.links: list[tuple[str, str]] = []
        self.link_href: str | None = None
        self.link_text: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag == "title": self.in_title = True
        classes = set(dict(attrs).get("class", "").split())
        if tag == "span" and "HpsProceedingHeading" in classes:
            tag = "h2"
        elif tag == "span" and "HpsSubjectHeading" in classes:
            tag = "h3"
        if tag in self.BLOCKS:
            self.current_tag, self.current = tag, []
        if tag == "a":
            self.link_href, self.link_text = dict(attrs).get("href"), []

    def handle_endtag(self, tag: str) -> None:
        if tag == "title": self.in_title = False
        if tag == "span" and self.current_tag in {"h2", "h3"}:
            tag = self.current_tag
        if tag == self.current_tag:
            text = " ".join("".join(self.current).split())
            if text: self.blocks.append((tag, text))
            self.current_tag, self.current = None, []
        if tag == "a" and self.link_href:
            self.links.append((self.link_href, " ".join("".join(self.link_text).split())))
            self.link_href, self.link_text = None, []

    def handle_data(self, data: str) -> None:
        if self.in_title: self.title += data
        if self.current_tag: self.current.append(data)
        if self.link_href: self.link_text.append(data)


def _slug(value: str) -> str:
    folded = unicodedata.normalize("NFKD", value.replace("—", "-").replace("–", "-")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", folded).strip("-")[:80]


def parse_listing(html: str, source_url: str, retrieved_at: str) -> list[dict[str, object]]:
    if re.search(r"radware captcha|hcaptcha|captcha page|awswaf", html, re.I):
        raise ValueError("Hansard source returned an access challenge")
    parser = _Blocks(); parser.feed(html)
    rows: dict[str, dict[str, object]] = {}
    for href, title in parser.links:
        match = re.search(r"/hansard-transcript/(\d{4}-\d{2}-\d{2})(?:/|$)", href)
        if not match:
            continue
        url = urljoin(source_url, href)
        if urlparse(url).hostname != "hansard.parliament.nz":
            continue
        rows[url] = {"id": match.group(1), "sitting_date": match.group(1), "title": title or f"Hansard {match.group(1)}", "source_url": url, "retrieved_at": retrieved_at}
    if not rows:
        raise ValueError("Hansard listing contained no transcript links")
    return sorted(rows.values(), key=lambda row: str(row["sitting_date"]), reverse=True)


def _speaker_identity(value: str) -> tuple[str, str | None, str]:
    """Split a published parenthetical role/party from the speaker name."""
    published = value.strip()
    match = re.match(r"^(.*?)\s*\(([^()]*)\)\s*$", published)
    if not match:
        return published, None, published
    return match.group(1).strip(), match.group(2).strip() or None, published


def _speaker_turn(text: str) -> tuple[str, str | None, str, str] | None:
    addressed = re.match(r"^(?:\d+\.\s*)?((?:Rt Hon|Hon|Dr)\s+.+?(?:\([^)]*\))?)\s+to\s+(?:the\s+)?[^:]+:\s+(.+)$", text, re.I)
    if addressed:
        speaker, role, published = _speaker_identity(addressed.group(1))
        return speaker, role, published, addressed.group(2).strip()
    match = re.match(r"^(.{2,100}?):\s+(.+)$", text)
    if not match:
        return None
    speaker, role, published = _speaker_identity(match.group(1))
    if not (speaker.isupper() or re.match(r"^(?:Rt Hon|Hon|Dr)\s+", speaker, re.I) or speaker in {"SPEAKER", "ASSISTANT SPEAKER", "DEPUTY SPEAKER", "CLERK"}):
        return None
    return speaker, role, published, match.group(2).strip()


def parse_transcript(html: str, source_url: str, retrieved_at: str) -> dict[str, object]:
    if re.search(r"radware captcha|hcaptcha|captcha page|awswaf", html, re.I):
        raise ValueError("Hansard source returned an access challenge")
    parser = _Blocks(); parser.feed(html)
    sitting_text = next((m.group(1) for _, text in parser.blocks if (m := re.search(r"Sitting date:\s*(\d{1,2}\s+\w+\s+\d{4})", text, re.I))), None)
    title = next((text for tag, text in parser.blocks if tag == "h1" and re.search(r"\d{4}", text)), None)
    volume = next((m.group(1) for _, text in parser.blocks if (m := re.fullmatch(r"Volume\s+(\d+)", text, re.I))), None)
    url_date = re.search(r"/hansard-transcript/(\d{4}-\d{2}-\d{2})", source_url)
    if not (sitting_text or title) or not url_date:
        raise ValueError("Hansard transcript page lacked sitting metadata")
    sitting_date = url_date.group(1)
    visible = " ".join(text for _, text in parser.blocks)
    if re.search(r'\bclass="[^"]*\bdraft\b', html, re.I) or re.search(r"\bprovisional\b|\bdraft transcript\b", visible, re.I): status = "provisional"
    elif re.search(r"\bcorrected transcript\b|\bcorrection\b", visible, re.I): status = "corrected"
    else: status = "official"

    debates: list[dict[str, object]] = []
    section: str | None = None
    current: dict[str, object] | None = None
    for tag, text in parser.blocks:
        if tag == "h2":
            if current: debates.append(current)
            section = text
            current = None
            continue
        if tag == "h3":
            if current: debates.append(current)
            stable_id = f"{sitting_date}-{_slug(text)}"
            current = {"id": stable_id, "section": section, "title": text, "subheadings": [], "text_blocks": [], "turns": [], "source_url": f"{source_url}#{stable_id}", "transcript_source_url": source_url, "retrieved_at": retrieved_at, "transcript_status": status}
            continue
        if tag == "h4" and current:
            current["subheadings"].append(text)
            continue
        if tag == "p" and current:
            current["text_blocks"].append(text)
            parsed = _speaker_turn(text)
            if parsed:
                speaker, role, published, spoken = parsed
                current["turns"].append({"speaker": speaker, "role_or_party": role, "speaker_as_published": published, "text": spoken, "debate_id": current["id"], "source_url": current["source_url"], "retrieved_at": retrieved_at, "transcript_status": status})
    if current: debates.append(current)
    if not debates:
        raise ValueError("Hansard transcript contained no structured debate/question items")
    for debate in debates:
        debate["text"] = "\n".join(debate.pop("text_blocks"))
    return {
        "id": sitting_date, "title": title or parser.title.strip(), "sitting_date": sitting_date,
        "sitting_date_text": sitting_text, "volume": volume, "debates": debates,
        "headings": [str(item["title"]) for item in debates],
        "turns": [turn for item in debates for turn in item["turns"]],
        "text": "\n\n".join(str(item["text"]) for item in debates),
        "source_url": source_url, "retrieved_at": retrieved_at, "transcript_status": status,
    }


def oral_question_excerpt(record: dict[str, object]) -> list[dict[str, object]]:
    rows = [item for item in record["debates"] if "oral question" in str(item.get("section") or "").casefold()]
    if not rows:
        raise ValueError("No Oral Questions section found in this sitting transcript")
    return rows
