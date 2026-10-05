#!/usr/bin/env python3
"""
lii_fetcher.py — resolve and fetch US statutes and federal regulations from
Cornell's Legal Information Institute (LII).

Companion to eyecite_extract.py. Where eyecite gives a consuming skill the
parsed citations from a brief, this script takes the subset that point at
statutes (U.S.C.) and federal regulations (C.F.R.), fetches the cited section
from LII, and extracts the subsection text the brief actually cites.

Designed to be invoked once per run as a subprocess (one batch in, one batch
out) so consuming skills don't trigger per-citation permission prompts.

Scope:
- 17 U.S.C. § 512 and like citations → https://www.law.cornell.edu/uscode/text/17/512
- 37 C.F.R. § 201.5 and like citations → https://www.law.cornell.edu/cfr/text/37/201.5
- Federal rules (FRCP/FRAP/FRE) are NOT handled here yet; they will fold in once the
  citation_type for rules is wired through. See SKILL.md.

LII has no AI/bot blocking on these pages — a plain GET with a real User-Agent
returns 200. No fallback (Wayback or otherwise) is wired up; if LII is down,
the network is broken and the consuming skill should escalate to the user
rather than paper over it.

Usage:

    # From a file containing the input JSON array:
    python3 lii_fetcher.py --input requests.json

    # From stdin:
    cat requests.json | python3 lii_fetcher.py

Input (JSON array on stdin or via --input). One object per citation:

    [
      {"id": "c1", "type": "statute",    "title": "17", "section": "512", "subsection": "(c)(2)"},
      {"id": "c2", "type": "regulation", "title": "37", "section": "201.5", "subsection": null}
    ]

  - id:         opaque caller-supplied identifier; echoed back in the output.
  - type:       "statute" (U.S.C.) or "regulation" (C.F.R.).
  - title:      title number, as a string or int.
  - section:    section identifier; for C.F.R. include the part (e.g., "201.5").
  - subsection: Bluebook-style subsection (e.g., "(c)(2)", "(b)(1)(A)(i)"),
                already-anchor-form ("c_2"), or null/missing.

Output (JSON array on stdout, one object per input entry, same order):

    [
      {
        "id": "c1",
        "status": "ok",                         # ok | anchor_not_found | not_found | network_error
        "url": "https://www.law.cornell.edu/uscode/text/17/512",
        "anchor": "c_2",
        "anchor_matched": true,
        "section_text": "...full § 512 text, tags stripped...",
        "subsection_text": "...just (c)(2)...",
        "retrieved_at": "2026-05-22T12:34:56Z",
        "flags": []
      }
    ]

Status semantics:
  - "ok":                section fetched and (if a subsection was requested)
                         the anchor was located and its text extracted.
  - "anchor_not_found":  section fetched, but the requested subsection anchor
                         did not appear in the page. section_text is populated;
                         subsection_text is null. Flag `subsection_anchor_not_found`.
  - "not_found":         LII returned 404. The cited section does not exist.
                         Flag `source_not_found`.
  - "network_error":     anything else (timeouts, 5xx, DNS, …). `error` field
                         carries a short description. No retries — the
                         consuming skill decides whether to re-run.

Dependencies: stdlib only. No `pip install` required.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from typing import Any

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
TIMEOUT_SECONDS = 20


# ---------------------------------------------------------------------------
# URL resolution
# ---------------------------------------------------------------------------

def resolve_url(entry: dict) -> str | None:
    """Return the LII URL for a statute or regulation entry, or None if the
    entry doesn't have the components we need."""
    citation_type = entry.get("type")
    title = entry.get("title")
    section = entry.get("section")
    if title is None or section is None:
        return None
    title = str(title).strip()
    section = str(section).strip()
    if not title or not section:
        return None
    if citation_type == "statute":
        return f"https://www.law.cornell.edu/uscode/text/{title}/{section}"
    if citation_type == "regulation":
        return f"https://www.law.cornell.edu/cfr/text/{title}/{section}"
    return None


def anchor_from_subsection(subsection: str | None) -> str | None:
    """Convert a Bluebook-style subsection ("(c)(2)", "(b)(1)(A)(i)") into an
    LII anchor name ("c_2", "b_1_A_i"). Pass through values that already look
    like anchors. Returns None for empty / missing input.

    Case is preserved — LII uses lowercase for first-level and arabic-digit
    levels and uppercase for roman-numeral levels (e.g., "b_2_C_i")."""
    if not subsection:
        return None
    s = str(subsection).strip()
    if not s:
        return None
    # Already in anchor form (no parens, contains underscores or is a single token)
    if "(" not in s and ")" not in s:
        return s
    parts = re.findall(r"\(([^)]+)\)", s)
    parts = [p.strip() for p in parts if p.strip()]
    return "_".join(parts) if parts else None


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------

def fetch(url: str) -> tuple[str | None, str, str | None]:
    """Fetch `url` and return (html, status, error_message).

    status is one of: "ok", "not_found", "network_error".
    On status != "ok", html is None."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            if resp.status >= 400:
                if resp.status == 404:
                    return None, "not_found", f"HTTP {resp.status}"
                return None, "network_error", f"HTTP {resp.status}"
            raw = resp.read()
            charset = resp.headers.get_content_charset() or "utf-8"
            return raw.decode(charset, errors="replace"), "ok", None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, "not_found", f"HTTP {e.code}"
        return None, "network_error", f"HTTP {e.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return None, "network_error", f"{type(e).__name__}: {e}"


# ---------------------------------------------------------------------------
# HTML parsing — pull section text and, optionally, a single subsection
# ---------------------------------------------------------------------------

class _SectionExtractor(HTMLParser):
    """Parse an LII section page. Capture:
      - the text inside `<div class="section">` (LII's main content wrapper for
        both U.S.C. and C.F.R.), with tags stripped and whitespace collapsed,
        as `section_text`;
      - the text of a specific subsection anchor's enclosing container, as
        `subsection_text`, when `target_anchor` is provided.

    Anchor markup differs by source type:
      - U.S.C.: `<a name="X"></a>` followed by a `<div class="subsection|paragraph indentN">` container.
      - C.F.R.: `<span class="enumxml" id="X">(X)</span>` inside a `<p class="psection-N">` container.

    Both anchor schemes use the same X token format (`a`, `b_1`, `b_2_C_i`), so
    `anchor_from_subsection` is shared.
    """

    _CONTAINER_TAGS = ("div", "p")
    _CONTAINER_CLASS_TOKENS = ("subsection", "paragraph", "psection")

    def __init__(self, target_anchor: str | None):
        super().__init__(convert_charrefs=True)
        self.target_anchor = target_anchor
        self._section_depth = 0  # nesting of <div class="section"> (1+ means we're inside)
        self._inside_section_at_depth: int | None = None  # depth at which the outer section div opened
        # Stack of (tag, class) for every container-eligible tag open inside the section.
        self._container_stack: list[tuple[str, str | None]] = []
        self._section_chars: list[str] = []
        self._subsection_chars: list[str] | None = None
        # The container-stack length at which capture started; capture ends when
        # the stack drops back to (or below) this length.
        self._capture_start_len: int | None = None
        self.anchor_matched = False

    # --- helpers
    @staticmethod
    def _attr(attrs, name):
        for k, v in attrs:
            if k == name:
                return v
        return None

    @classmethod
    def _is_container_class(cls, cls_value: str | None) -> bool:
        if not cls_value:
            return False
        return any(token in cls_value for token in cls._CONTAINER_CLASS_TOKENS)

    def _in_section(self) -> bool:
        return self._inside_section_at_depth is not None

    def _check_anchor_hit(self, anchor_value: str | None):
        if not self.target_anchor or self.anchor_matched:
            return
        if anchor_value != self.target_anchor:
            return
        # Find the nearest enclosing container-class entry in the stack; capture
        # everything until that container closes. If no container-class entry
        # exists, fall back to capturing until the section wrapper closes.
        start_len = 0  # default: capture everything to end of section
        for i in range(len(self._container_stack) - 1, -1, -1):
            tag, cls = self._container_stack[i]
            if self._is_container_class(cls):
                start_len = i  # capture while stack length > i (i.e., this container is open)
                break
        self._capture_start_len = start_len
        self._subsection_chars = []
        self.anchor_matched = True

    # --- handlers
    def handle_starttag(self, tag, attrs):
        # Track entry into <div class="section">.
        if tag == "div":
            cls = self._attr(attrs, "class")
            if not self._in_section() and cls and "section" in cls.split():
                self._inside_section_at_depth = 0  # marker; depth tracked via container stack
                self._container_stack.append((tag, cls))
                return
        # Outside the section wrapper, ignore.
        if not self._in_section():
            return
        # Container-eligible tags: push onto stack.
        if tag in self._CONTAINER_TAGS:
            cls = self._attr(attrs, "class")
            self._container_stack.append((tag, cls))
            return
        # Anchor types:
        # U.S.C. — <a name="X"></a>
        if tag == "a":
            self._check_anchor_hit(self._attr(attrs, "name"))
            return
        # C.F.R. — <span class="enumxml" id="X">
        if tag == "span":
            cls = self._attr(attrs, "class") or ""
            if "enumxml" in cls.split():
                self._check_anchor_hit(self._attr(attrs, "id"))
            return

    def handle_endtag(self, tag):
        if not self._in_section():
            return
        if tag in self._CONTAINER_TAGS and self._container_stack:
            # Closing a container. Finalize a pending capture if we're popping
            # back to (or below) its start.
            popped_index = len(self._container_stack) - 1
            self._container_stack.pop()
            if (
                self._capture_start_len is not None
                and popped_index <= self._capture_start_len
            ):
                self._capture_start_len = None
            # If the stack is now empty, we've closed the section wrapper.
            if not self._container_stack:
                self._inside_section_at_depth = None

    def handle_data(self, data):
        if self._in_section():
            self._section_chars.append(data)
            if self._capture_start_len is not None and self._subsection_chars is not None:
                self._subsection_chars.append(data)

    # --- output
    @staticmethod
    def _normalize(chars: list[str]) -> str:
        return re.sub(r"\s+", " ", "".join(chars)).strip()

    def section_text(self) -> str:
        return self._normalize(self._section_chars)

    def subsection_text(self) -> str | None:
        if self._subsection_chars is None:
            return None
        return self._normalize(self._subsection_chars)


def extract_section(html: str, anchor: str | None) -> tuple[str, str | None, bool]:
    """Return (section_text, subsection_text, anchor_matched).

    If `anchor` is None, subsection_text is None and anchor_matched is False.
    If `anchor` is provided but not located in the page, subsection_text is
    None and anchor_matched is False — the caller surfaces this as
    `anchor_not_found`."""
    parser = _SectionExtractor(target_anchor=anchor)
    parser.feed(html)
    parser.close()
    return parser.section_text(), parser.subsection_text(), parser.anchor_matched


# ---------------------------------------------------------------------------
# Top-level processing
# ---------------------------------------------------------------------------

def process(entries: list[dict]) -> list[dict]:
    now = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    results: list[dict] = []
    for entry in entries:
        result: dict[str, Any] = {"id": entry.get("id"), "retrieved_at": now, "flags": []}
        url = resolve_url(entry)
        if url is None:
            result.update(
                status="network_error",
                url=None,
                anchor=None,
                anchor_matched=False,
                section_text=None,
                subsection_text=None,
                error="unsupported_or_incomplete_entry",
            )
            results.append(result)
            continue
        anchor = anchor_from_subsection(entry.get("subsection"))
        result["url"] = url
        result["anchor"] = anchor
        html, status, error = fetch(url)
        if status != "ok":
            result.update(
                status=status,
                anchor_matched=False,
                section_text=None,
                subsection_text=None,
                error=error,
            )
            if status == "not_found":
                result["flags"].append("source_not_found")
            results.append(result)
            continue
        section_text, subsection_text, anchor_matched = extract_section(html or "", anchor)
        # LII sometimes serves HTTP 200 for sections it doesn't actually have
        # (the page renders with chrome but no body). Treat that as not_found
        # so the consuming skill can escalate uniformly with real 404s.
        if not section_text or len(section_text) < 80:
            result.update(
                status="not_found",
                anchor_matched=False,
                section_text=None,
                subsection_text=None,
                error="empty_section_body",
            )
            result["flags"].append("source_not_found")
            results.append(result)
            continue
        if anchor and not anchor_matched:
            result.update(
                status="anchor_not_found",
                anchor_matched=False,
                section_text=section_text,
                subsection_text=None,
            )
            result["flags"].append("subsection_anchor_not_found")
        else:
            result.update(
                status="ok",
                anchor_matched=bool(anchor and anchor_matched),
                section_text=section_text,
                subsection_text=subsection_text,
            )
        results.append(result)
    return results


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Fetch US statutes and CFR sections from Cornell LII. "
                    "Reads a JSON array of citation requests; writes a JSON "
                    "array of results to stdout.",
    )
    parser.add_argument("--input", help="Path to input JSON file. If omitted, read stdin.")
    args = parser.parse_args(argv)

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            payload = f.read()
    else:
        payload = sys.stdin.read()

    try:
        entries = json.loads(payload)
    except json.JSONDecodeError as e:
        sys.stderr.write(f"ERROR: input is not valid JSON: {e}\n")
        return 2
    if not isinstance(entries, list):
        sys.stderr.write("ERROR: input JSON must be an array of request objects.\n")
        return 2

    results = process(entries)
    json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
