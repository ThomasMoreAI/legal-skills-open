#!/usr/bin/env python3
"""wiki — the wiki engine for the /wiki skill (CODEX for Legal).

The wiki is an OKF v0.2 bundle: markdown notes with YAML frontmatter,
readable in any editor. This script is the deterministic half of the
skill: parsing, validation, history, and receipts. Judgment (distilling,
typing, linking) belongs to the model; this script refuses to guess.

Verbs (grouped; every verb prints a one-line receipt):
  setup · init · wiki-list · wiki-use      configure and find wikis
  check · normalize · version                validate and canonicalize
  land · rename · delete · purge · merge     mutate notes (gated)
  accept · decline · verify-note             markup review
  verify · status · rollback · export-map    history, receipts, map
  gate · denylist-add                        method-not-matter gate
  seed-scan · seed-emit · seed-land          seeding pipeline
  capture · capture-land                     legacy staged-import compatibility
  maintain · tripwire                        maintenance and metrics
Run any verb with --help for its flags.

Conventions: stdlib only; UTF-8; findings to stdout, diagnostics to
stderr. Exit codes: 0 ok, 1 findings or failure, 2 usage/unreadable.
Spec references (§) are to the OKF v0.2 specification; the pinned
excerpts ship in references/okf-profile.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import re
import sys
import tempfile
import time
import uuid
from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

ENGINE_VERSION = "0.1.0"
SCHEMA_VERSION = 1
OKF_VERSION = "0.2"

NOTE_TYPES = ("Legal Insight", "Checklist", "Trap", "Position")
ORIGINS = ("seeded", "auto-built", "accepted")
STATUSES = ("draft", "stable", "disputed", "outdated", "deprecated")
SKIP_REASONS = (
    "routine",
    "no-new-rule",
    "matter-specific",
    "no-boundary-found",
    "unreadable",
    "over-cap",
)
PURGE_REASONS = (
    "matter-data-removal",
    "privacy-remediation",
    "user-requested-erasure",
    "corrupt-content",
)

# Canonical top-level key order: OKF standard keys in spec order, then the
# legal-profile extension keys. Unknown keys keep their source order after
# these (never dropped -- OKF §4.1).
CANONICAL_TOP = (
    "type",
    "title",
    "description",
    "tags",
    "resource",
    "generated",
    "verified",
    "status",
    "stale_after",
    "usage_window",
    "runtime",
    "parameters",
    "computation",
    "executor",
    "attester",
    "sources",
    "practice_area",
    "jurisdiction",
    "document_kind",
    "trigger",
    "origin",
    "pending",
)

# Canonical field order inside known record values.
RECORD_ORDER = {
    "generated": ("by", "at"),
    "verified": ("by", "at"),
    "usage_window": ("from", "to"),
    "executor": ("resource", "receipt"),
    "attester": ("resource",),
    "sources": (
        "id",
        "kind",
        "resource",
        "title",
        "author",
        "pinpoint",
        "support",
        "sha256",
        "last_checked",
        "usage_count",
        "last_modified",
    ),
}

RESERVED_FILENAMES = ("index.md", "log.md")
SIDECAR_DIRNAME = ".wiki"

SEGMENT_RE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9_.\-]*$")
WINDOWS_FORBIDDEN = set(':*?"<>|\\')
KEY_RE = re.compile(r"^([A-Za-z0-9_.\-]+):(.*)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}([T ].*)?$")
NUMERIC_RE = re.compile(r"^-?\d+(\.\d+)?$")
BOOL_NULL_RE = re.compile(r"^(true|false|yes|no|null|~)$", re.IGNORECASE)
DATE_HEADING_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})\s*$")
H2_RE = re.compile(r"^## ")
ROOTED_LINK_RE = re.compile(r"\]\(\s*/[^)]*\)")
MAX_FRONTMATTER_DEPTH = 40


class FrontmatterError(ValueError):
    """A frontmatter block that cannot be parsed under the pinned grammar."""


# ---------------------------------------------------------------------------
# Frontmatter: parsing
# ---------------------------------------------------------------------------


def split_document(text: str) -> tuple[dict | None, str]:
    """Split a note into (frontmatter mapping | None, body).

    A file with no leading fence is all body (upstream behaviour).
    An unterminated fence is an error; guessing would hide corruption.
    """
    lines = text.replace("\r\n", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() in ("---", "..."):
            close = i
            break
    if close is None:
        raise FrontmatterError("unterminated frontmatter fence")
    block = lines[1:close]
    body = "\n".join(lines[close + 1 :])
    mapping, pos = _parse_mapping(block, 0, _first_indent(block), 0)
    rest = _next_content(block, pos)
    if rest is not None:
        raise FrontmatterError(f"unparseable frontmatter near: {block[rest].strip()!r}")
    return mapping, body


def _first_indent(lines: list[str]) -> int:
    i = _next_content(lines, 0)
    return 0 if i is None else _indent_of(lines[i])


def _indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _next_content(lines: list[str], i: int) -> int | None:
    while i < len(lines):
        s = lines[i].strip()
        if s and not s.startswith("#"):
            return i
        i += 1
    return None


def _depth_guard(depth: int) -> None:
    if depth > MAX_FRONTMATTER_DEPTH:
        raise FrontmatterError(
            f"frontmatter nesting exceeds {MAX_FRONTMATTER_DEPTH} levels"
        )


def _parse_mapping(
    lines: list[str], i: int, indent: int, depth: int
) -> tuple[dict, int]:
    _depth_guard(depth)
    out: dict = {}
    while True:
        j = _next_content(lines, i)
        if j is None:
            return out, len(lines)
        line = lines[j]
        cur = _indent_of(line)
        if cur < indent:
            return out, j
        if cur > indent:
            raise FrontmatterError(f"unexpected indent: {line.strip()!r}")
        s = line.strip()
        if s == "-" or s.startswith("- "):
            raise FrontmatterError(f"list item where a key was expected: {s!r}")
        m = KEY_RE.match(s)
        if not m:
            raise FrontmatterError(f"not a key-value line: {s!r}")
        key, rest = m.group(1), m.group(2).strip()
        rest = _strip_inline_comment(rest)
        if rest:
            out[key] = _parse_inline(rest, depth + 1)
            i = j + 1
            continue
        k = _next_content(lines, j + 1)
        if k is None or _indent_of(lines[k]) <= indent:
            out[key] = ""
            i = j + 1
            continue
        child_indent = _indent_of(lines[k])
        child = lines[k].strip()
        if child == "-" or child.startswith("- "):
            out[key], i = _parse_list(lines, k, child_indent, depth + 1)
        else:
            out[key], i = _parse_mapping(lines, k, child_indent, depth + 1)


def _parse_list(lines: list[str], i: int, indent: int, depth: int) -> tuple[list, int]:
    _depth_guard(depth)
    items: list = []
    while True:
        j = _next_content(lines, i)
        if j is None:
            return items, len(lines)
        line = lines[j]
        cur = _indent_of(line)
        if cur < indent:
            return items, j
        s = line.strip()
        if cur > indent or not (s == "-" or s.startswith("- ")):
            raise FrontmatterError(f"expected a list item: {s!r}")
        after = _strip_inline_comment(s[1:].strip())
        key_col = cur + 2
        if not after:
            k = _next_content(lines, j + 1)
            if k is None or _indent_of(lines[k]) <= cur:
                items.append("")
                i = j + 1
                continue
            ci = _indent_of(lines[k])
            child = lines[k].strip()
            if child == "-" or child.startswith("- "):
                value, i = _parse_list(lines, k, ci, depth + 1)
            else:
                value, i = _parse_mapping(lines, k, ci, depth + 1)
            items.append(value)
            continue
        m = KEY_RE.match(after)
        if m and not after.startswith(("{", "[", '"', "'")):
            entry: dict = {}
            first_key, first_rest = m.group(1), m.group(2).strip()
            entry[first_key] = (
                _parse_inline(first_rest, depth + 1) if first_rest else ""
            )
            more, i = _parse_mapping(lines, j + 1, key_col, depth + 1)
            entry.update(more)
            items.append(entry)
            continue
        items.append(_parse_inline(after, depth + 1))
        i = j + 1


def _strip_inline_comment(s: str) -> str:
    if not s or s.startswith(("{", "[", '"', "'")):
        return s
    depth = 0
    for idx in range(len(s)):
        ch = s[idx]
        if ch in "{[":
            depth += 1
        elif ch in "}]":
            depth -= 1
        elif ch == "#" and depth == 0 and idx > 0 and s[idx - 1] == " ":
            return s[:idx].rstrip()
    return s


def _parse_inline(s: str, depth: int = 0):
    _depth_guard(depth)
    s = s.strip()
    if s.startswith("{"):
        return _parse_flow_mapping(s, depth + 1)
    if s.startswith("["):
        return _parse_flow_list(s, depth + 1)
    return _parse_scalar(s)


def _parse_scalar(s: str) -> str:
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return s[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    if len(s) >= 2 and s[0] == "'" and s[-1] == "'":
        return s[1:-1].replace("''", "'")
    return s


def _split_flow(inner: str) -> list[str]:
    parts: list[str] = []
    depth = 0
    quote: str | None = None
    cur: list[str] = []
    for ch in inner:
        if quote:
            cur.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
            cur.append(ch)
        elif ch in "{[":
            depth += 1
            cur.append(ch)
        elif ch in "}]":
            depth -= 1
            cur.append(ch)
        elif ch == "," and depth == 0:
            parts.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    tail = "".join(cur).strip()
    if tail:
        parts.append(tail)
    return parts


def _parse_flow_mapping(s: str, depth: int) -> dict:
    _depth_guard(depth)
    if not s.endswith("}"):
        raise FrontmatterError(f"unterminated flow mapping: {s!r}")
    out: dict = {}
    for part in _split_flow(s[1:-1]):
        m = KEY_RE.match(part)
        if not m:
            raise FrontmatterError(f"bad flow-mapping entry: {part!r}")
        out[m.group(1)] = _parse_inline(m.group(2).strip(), depth + 1)
    return out


def _parse_flow_list(s: str, depth: int) -> list:
    _depth_guard(depth)
    if not s.endswith("]"):
        raise FrontmatterError(f"unterminated flow list: {s!r}")
    return [_parse_inline(p, depth + 1) for p in _split_flow(s[1:-1])]


# ---------------------------------------------------------------------------
# Frontmatter: canonical emission
# ---------------------------------------------------------------------------


def emit_document(fm: dict | None, body: str) -> str:
    if fm is None:
        return body
    out = ["---"]
    out.extend(_emit_mapping(_reorder_top(fm), 0))
    out.append("---")
    text = "\n".join(out)
    return text + "\n" + body if body else text + "\n"


def _reorder_top(fm: dict) -> dict:
    ordered: dict = {}
    for key in CANONICAL_TOP:
        if key in fm:
            ordered[key] = fm[key]
    for key, value in fm.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


def _reorder_record(key: str, record: dict) -> dict:
    order = RECORD_ORDER.get(key, ())
    ordered: dict = {}
    for k in order:
        if k in record:
            ordered[k] = record[k]
    for k, v in record.items():
        if k not in ordered:
            ordered[k] = v
    return ordered


def _emit_mapping(mapping: dict, indent: int) -> list[str]:
    pad = " " * indent
    lines: list[str] = []
    for key, value in mapping.items():
        if isinstance(value, dict):
            if key in ("generated", "verified", "usage_window"):
                lines.append(f"{pad}{key}: {_emit_flow_mapping(key, value)}")
            else:
                lines.append(f"{pad}{key}:")
                lines.extend(_emit_mapping(_reorder_record(key, value), indent + 2))
        elif isinstance(value, list):
            lines.extend(_emit_list(key, value, indent))
        else:
            lines.append(f"{pad}{key}: {_emit_scalar(value)}")
    return lines


def _emit_list(key: str, items: list, indent: int) -> list[str]:
    pad = " " * indent
    if not items:
        return [f"{pad}{key}: []"]
    if all(not isinstance(i, dict | list) for i in items):
        inner = ", ".join(_emit_scalar(i) for i in items)
        return [f"{pad}{key}: [{inner}]"]
    lines = [f"{pad}{key}:"]
    for item in items:
        if isinstance(item, dict):
            if key == "verified":
                lines.append(f"{pad}  - {_emit_flow_mapping(key, item)}")
                continue
            entry = _reorder_record(key, item)
            first = True
            for k, v in entry.items():
                lead = f"{pad}  - " if first else f"{pad}    "
                first = False
                if isinstance(v, dict | list):
                    sub = {k: v}
                    rendered = _emit_mapping(sub, 0)
                    lines.append(lead + rendered[0])
                    lines.extend(f"{pad}    {extra}" for extra in rendered[1:])
                else:
                    lines.append(f"{lead}{k}: {_emit_scalar(v)}")
        elif isinstance(item, list):
            raise FrontmatterError("nested lists are outside the pinned grammar")
        else:
            lines.append(f"{pad}  - {_emit_scalar(item)}")
    return lines


def _emit_flow_mapping(key: str, record: dict) -> str:
    ordered = _reorder_record(key, record)
    inner = ", ".join(f"{k}: {_emit_scalar(v)}" for k, v in ordered.items())
    return "{ " + inner + " }"


def _emit_scalar(value) -> str:
    s = str(value) if not isinstance(value, str) else value
    if isinstance(value, bool):
        s = "true" if value else "false"
    if s == "":
        return '""'
    if DATE_RE.match(s):
        return s
    needs_quote = (
        s != s.strip()
        or ": " in s
        or " #" in s
        or s[0] in "-?:,[]{}#&*!|>'\"%@`"
        or NUMERIC_RE.match(s) is not None
        or (BOOL_NULL_RE.match(s) is not None and s not in ("true", "false"))
    )
    if needs_quote:
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


# ---------------------------------------------------------------------------
# Trust, staleness, identity, digests
# ---------------------------------------------------------------------------


def normalize_verified(raw) -> list[dict]:
    """A bare mapping MUST be treated as a one-element list (§11)."""
    if isinstance(raw, dict):
        return [raw]
    if isinstance(raw, list):
        return [entry for entry in raw if isinstance(entry, dict)]
    return []


def trust_tier(fm: dict) -> str:
    entries = normalize_verified(fm.get("verified"))
    if not entries:
        return "unverified"
    for entry in entries:
        if str(entry.get("by", "")).startswith("human:"):
            return "human-reviewed"
    return "machine-confirmed"


def is_stale(value, today: date | None = None) -> bool:
    """Stale when today >= stale_after; unparseable never hides a note."""
    if value is None:
        return False
    today = today or date.today()
    try:
        parsed = date.fromisoformat(str(value)[:10])
    except ValueError:
        return False
    return today >= parsed


def canonical_json_digest(payload) -> str:
    blob = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def note_dirname(note_path: str) -> str:
    """Version-directory name for a note: first 16 hex of its path hash."""
    return hashlib.sha256(note_path.encode("utf-8")).hexdigest()[:16]


def validate_note_path(rel_path: str) -> list[str]:
    problems: list[str] = []
    if not rel_path or Path(rel_path).is_absolute() or rel_path.startswith(("/", "\\")):
        return ["note path must be bundle-relative"]
    parts = rel_path.split("/")
    for part in parts:
        if part in ("", ".", ".."):
            problems.append(f"segment {part!r} is not allowed")
            continue
        if part.casefold() == SIDECAR_DIRNAME or part.startswith("."):
            problems.append(f"hidden or sidecar segment {part!r} is not allowed")
            continue
        stem = part[:-3] if part.endswith(".md") else part
        bad = set(part) & WINDOWS_FORBIDDEN
        if bad:
            problems.append(f"forbidden character(s) {sorted(bad)} in {part!r}")
            continue
        if not SEGMENT_RE.match(stem):
            problems.append(f"segment {part!r} violates the path grammar")
    if parts and parts[-1].casefold() in RESERVED_FILENAMES:
        problems.append(f"reserved filename {parts[-1]!r} is not a note")
    return problems


def safe_note_path(
    wiki: Path, rel_path: str, *, must_exist: bool = False
) -> tuple[str, Path]:
    """Resolve one canonical note path without permitting a symlink escape."""
    rel = rel_path.replace(os.sep, "/")
    problems = validate_note_path(rel)
    if not rel.endswith(".md"):
        problems.append("note path must end in .md")
    if problems:
        raise WikiError(f"bad note path {rel!r}: {'; '.join(problems)}")

    root = wiki.resolve(strict=True)
    candidate = root.joinpath(*rel.split("/"))
    current = root
    for segment in rel.split("/")[:-1]:
        current = current / segment
        if current.is_symlink():
            raise WikiError(f"note path {rel!r} crosses a symbolic link")
    try:
        candidate.parent.resolve(strict=False).relative_to(root)
    except ValueError as exc:
        raise WikiError(f"note path {rel!r} escapes the wiki") from exc
    if candidate.is_symlink():
        raise WikiError(f"note path {rel!r} is a symbolic link")
    if candidate.exists():
        try:
            candidate.resolve(strict=True).relative_to(root)
        except ValueError as exc:
            raise WikiError(f"note path {rel!r} escapes the wiki") from exc
        if not candidate.is_file():
            raise WikiError(f"note path {rel!r} is not a regular file")
    elif must_exist:
        raise WikiError(f"{rel} does not exist")
    return rel, candidate


def path_has_symlink_component(path: Path) -> bool:
    """Check a lexical path without resolving away a symlinked parent."""
    absolute = Path(os.path.abspath(path))
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def atomic_write_text(path: Path, text: str) -> None:
    """Exclusive random temporary file + atomic replace + durable flush."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent)
    )
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        for attempt in range(5):
            try:
                os.replace(tmp, path)
                return
            except PermissionError:
                if attempt == 4:
                    raise
                time.sleep(0.2 * (attempt + 1))
    finally:
        tmp.unlink(missing_ok=True)


def markdown_text(value: object) -> str:
    """Render untrusted metadata as one inert Markdown text fragment."""
    text = " ".join(str(value).split())
    return re.sub(r"([\\`*_{}\[\]<>()|])", r"\\\1", text)


def markdown_link(label: object, target: object) -> str:
    """Build a Markdown link without letting metadata alter the index shape."""
    safe_target = quote(str(target), safe="/:#?&=@%+~,-._")
    return f"[{markdown_text(label)}]({safe_target})"


# ---------------------------------------------------------------------------
# The conformance checker (OKF pass + legal-profile pass, reported apart)
# ---------------------------------------------------------------------------


@dataclass
class Report:
    conformance: list[str] = field(default_factory=list)
    profile: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.conformance and not self.profile

    def as_dict(self) -> dict:
        return {
            "ok": self.ok,
            "conformance": self.conformance,
            "profile": self.profile,
            "warnings": self.warnings,
        }


def check_wiki(root: Path, today: date | None = None) -> Report:
    report = Report()
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        parts = rel.parts
        if path.is_symlink():
            report.profile.append(f"{rel}: symbolic links are not allowed in a wiki")
            continue
        if SIDECAR_DIRNAME in parts:
            if path.suffix == ".md":
                report.profile.append(
                    f"{rel}: .md file inside the machine sidecar "
                    f"({SIDECAR_DIRNAME}/ holds no markdown, ever)"
                )
            continue
        if any(p.startswith(".") for p in parts):
            continue
        if not path.is_file() or path.suffix != ".md":
            continue
        if path.name == "index.md":
            _check_index(path, rel, is_root=len(parts) == 1, report=report)
        elif path.name == "log.md":
            _check_log(path, rel, report)
        else:
            _check_note(path, rel, report, today)
    root_index = root / "index.md"
    if not root_index.exists():
        report.warnings.append(
            "no root index.md (legal, but the wiki has no front door)"
        )
    return report


def _read(path: Path, rel: Path, report: Report) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        report.conformance.append(f"{rel}: unreadable ({exc.__class__.__name__})")
        return None


def _check_note(path: Path, rel: Path, report: Report, today: date | None) -> None:
    text = _read(path, rel, report)
    if text is None:
        return
    try:
        fm, body = split_document(text)
    except FrontmatterError as exc:
        report.conformance.append(f"{rel}: {exc} (§11 rule 1)")
        return
    if fm is None:
        report.conformance.append(f"{rel}: missing frontmatter block (§11 rule 1)")
        return
    note_type = str(fm.get("type", "") or "").strip()
    if not note_type:
        report.conformance.append(f"{rel}: empty or missing type (§11 rule 2)")
        return
    for problem in validate_note_path(str(rel).replace(os.sep, "/")):
        report.profile.append(f"{rel}: {problem}")
    if note_type not in NOTE_TYPES:
        report.profile.append(
            f"{rel}: type {note_type!r} is not in the legal profile "
            f"(conformant OKF, but not a /wiki note type)"
        )
        return
    _check_profile_keys(fm, rel, note_type, report, today)
    if ROOTED_LINK_RE.search(body):
        report.profile.append(
            f"{rel}: /-rooted body link (profile: body links are document-relative)"
        )


def _check_profile_keys(
    fm: dict, rel: Path, note_type: str, report: Report, today: date | None
) -> None:
    required = {"practice_area"}
    if note_type == "Legal Insight":
        required.add("jurisdiction")
    if note_type in ("Checklist", "Trap"):
        required.update(("document_kind", "trigger"))
    for key in sorted(required):
        if not str(fm.get(key, "") or "").strip():
            report.profile.append(
                f"{rel}: missing required key {key!r} for {note_type}"
            )
    if not str(fm.get("title", "") or "").strip():
        report.profile.append(f"{rel}: missing title")
    description = str(fm.get("description", "") or "")
    if not description.strip():
        report.warnings.append(
            f"{rel}: missing description (index and previews use it)"
        )
    elif re.search(r"[.!?]\s+[A-Z0-9]", description):
        report.warnings.append(f"{rel}: description reads as more than one sentence")
    origin = str(fm.get("origin", "") or "")
    if origin not in ORIGINS:
        report.profile.append(
            f"{rel}: origin {origin!r} missing or not one of {'/'.join(ORIGINS)}"
        )
    generated = fm.get("generated")
    if not isinstance(generated, dict) or not str(generated.get("by", "")).strip():
        report.profile.append(f"{rel}: generated {{by, at}} missing or incomplete")
    status = str(fm.get("status", "") or "")
    if status and status not in STATUSES:
        report.profile.append(f"{rel}: status {status!r} not in {'/'.join(STATUSES)}")
    pending = fm.get("pending")
    if pending is not None:
        truthy = str(pending).strip().lower() == "true"
        if not truthy:
            report.profile.append(f"{rel}: pending must be true or absent")
        elif status != "draft":
            report.profile.append(f"{rel}: pending requires status: draft")
    stale_after = fm.get("stale_after")
    if stale_after is not None:
        try:
            date.fromisoformat(str(stale_after)[:10])
        except ValueError:
            report.profile.append(f"{rel}: stale_after {stale_after!r} is not a date")
        else:
            if is_stale(stale_after, today):
                report.warnings.append(f"{rel}: past stale_after (re-check queued)")
    sources = fm.get("sources", []) or []
    if not isinstance(sources, list):
        report.profile.append(f"{rel}: sources must be a list")
    else:
        pending_draft = (
            status == "draft"
            and str(fm.get("pending", "")).strip().casefold() == "true"
        )
        if note_type in ASSERTION_TYPES and not sources and not pending_draft:
            report.profile.append(
                f"{rel}: {note_type} without sources must be a pending draft"
            )
        for index, source in enumerate(sources, 1):
            if not isinstance(source, dict):
                report.profile.append(f"{rel}: source {index} must be a record")
                continue
            resource = str(source.get("resource", "") or "").strip()
            kind = str(source.get("kind", "") or "").strip()
            if not resource:
                report.warnings.append(
                    f"{rel}: source {index} has no clickable resource"
                )
            elif resource.startswith(("http://", "https://")):
                if kind and kind != "public":
                    report.profile.append(
                        f"{rel}: URL source {index} kind must be public"
                    )
                if _looks_like_matter_reference(
                    resource, str(source.get("title", "") or "")
                ):
                    report.profile.append(
                        f"{rel}: URL source {index} looks matter-specific"
                    )
            elif kind != "authorised-local":
                report.profile.append(
                    f"{rel}: local source {index} requires kind: authorised-local"
                )
            elif resource:
                local = Path(resource).expanduser()
                if path_has_symlink_component(local) or _looks_like_matter_reference(
                    f"{resource} {local.resolve(strict=False)}",
                    str(source.get("title", "") or ""),
                ):
                    report.profile.append(
                        f"{rel}: local source {index} is a link or looks "
                        "matter-specific"
                    )
                elif not local.is_file():
                    report.warnings.append(
                        f"{rel}: local source {index} is unavailable"
                    )
                elif source.get("sha256"):
                    actual = hashlib.sha256(local.read_bytes()).hexdigest()
                    if actual != source.get("sha256"):
                        report.warnings.append(
                            f"{rel}: local source {index} changed since last check"
                        )
            if resource and not source.get("pinpoint"):
                report.warnings.append(f"{rel}: source {index} has no pinpoint")


def _check_index(path: Path, rel: Path, is_root: bool, report: Report) -> None:
    text = _read(path, rel, report)
    if text is None:
        return
    try:
        fm, _body = split_document(text)
    except FrontmatterError as exc:
        report.conformance.append(f"{rel}: {exc} (§8)")
        return
    if fm is None:
        if is_root:
            report.warnings.append(
                f"{rel}: root index.md declares no okf_version (§12)"
            )
        return
    if not is_root:
        report.conformance.append(
            f"{rel}: index.md may not carry frontmatter below the root (§8)"
        )
        return
    extra = set(fm) - {"okf_version"}
    if extra:
        report.conformance.append(
            f"{rel}: root index.md frontmatter may carry only okf_version, "
            f"found {sorted(extra)} (§8/§12)"
        )
    declared = str(fm.get("okf_version", "") or "")
    if declared and declared != OKF_VERSION:
        report.warnings.append(f"{rel}: okf_version {declared!r} != {OKF_VERSION!r}")
    if len(text.split("\n")) > 200 and is_root:
        report.warnings.append(f"{rel}: root index exceeds the 200-line budget")


def _check_log(path: Path, rel: Path, report: Report) -> None:
    text = _read(path, rel, report)
    if text is None:
        return
    try:
        fm, body = split_document(text)
    except FrontmatterError as exc:
        report.conformance.append(f"{rel}: {exc} (§9)")
        return
    if fm is not None:
        report.profile.append(
            f"{rel}: log.md carries frontmatter (profile: the log is prose only)"
        )
        text = body
    dates: list[str] = []
    for line in text.split("\n"):
        if not H2_RE.match(line):
            continue
        m = DATE_HEADING_RE.match(line)
        if not m:
            report.conformance.append(
                f"{rel}: heading {line.strip()!r} is not an ISO date group (§9)"
            )
            continue
        dates.append(m.group(1))
    if dates != sorted(dates, reverse=True):
        report.conformance.append(f"{rel}: date groups are not newest-first (§9)")


# ---------------------------------------------------------------------------
# Wiki state: lock, history chain, versions, regeneration
# ---------------------------------------------------------------------------

LOCK_STALE_SECONDS = 600
DEFAULT_ACTOR = "wiki/engine"
OP_WORDS = {
    "create_note": "Creation",
    "update_note": "Update",
    "rename_note": "Rename",
    "merge_notes": "Merge",
    "delete_note": "Deletion",
    "purge_note": "Purge",
    "accept_suggestion": "Acceptance",
    "decline_suggestion": "Decline",
    "rollback": "Rollback",
    "intake_skip": "Intake",
}


class WikiError(RuntimeError):
    """A wiki operation that must refuse rather than guess."""


def sidecar(wiki: Path) -> Path:
    return wiki / SIDECAR_DIRNAME


def history_path(wiki: Path) -> Path:
    return sidecar(wiki) / "history.jsonl"


def utc_now_iso() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def utc_now_compact() -> str:
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except OSError:
        return True
    return True


class WikiLock:
    """Single-writer O_EXCL lock; stale locks with a dead owner are broken."""

    def __init__(self, wiki: Path):
        self.path = sidecar(wiki) / "lock"
        self.acquired = False
        self.token = uuid.uuid4().hex

    def __enter__(self) -> WikiLock:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        for _attempt in (1, 2):
            try:
                fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            except FileExistsError:
                info = self._read_holder()
                age = time.time() - info.get("epoch", 0)
                same_host = info.get("host") == platform.node()
                dead = same_host and not _pid_alive(int(info.get("pid", 0)))
                if age > LOCK_STALE_SECONDS and (dead or not same_host):
                    print(
                        f"note: breaking stale wiki lock (pid {info.get('pid')} "
                        f"on {info.get('host')}, {int(age)}s old)",
                        file=sys.stderr,
                    )
                    self.path.unlink(missing_ok=True)
                    continue
                raise WikiError(
                    "another /wiki session is writing this wiki "
                    f"(pid {info.get('pid')} on {info.get('host')} since "
                    f"{info.get('ts')}); retry when it finishes"
                ) from None
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                fh.write(
                    json.dumps(
                        {
                            "pid": os.getpid(),
                            "host": platform.node(),
                            "ts": utc_now_iso(),
                            "epoch": time.time(),
                            "token": self.token,
                        }
                    )
                )
            self.acquired = True
            return self
        raise WikiError("could not acquire the wiki lock")

    def _read_holder(self) -> dict:
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}

    def __exit__(self, *_exc) -> None:
        if self.acquired:
            holder = self._read_holder()
            if holder.get("token") == self.token:
                self.path.unlink(missing_ok=True)


def read_history(wiki: Path) -> list[dict]:
    path = history_path(wiki)
    if not path.exists():
        return []
    records = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            records.append({"seq": None, "op": "corrupt", "line": n})
    return records


def chain_digest(record: dict) -> str:
    payload = {k: v for k, v in record.items() if k != "checksum"}
    return canonical_json_digest(payload)


def append_history(
    wiki: Path,
    op: str,
    note: str | None,
    actor: str,
    origin: str | None = None,
    mode: str | None = None,
    content_sha256: str | None = None,
    prior_content_sha256: str | None = None,
    extra: dict | None = None,
) -> dict:
    if op not in OP_WORDS:
        raise WikiError(f"unknown history operation {op!r}")
    extra = extra or {}
    if note:
        safe_note_path(wiki, note)
    if extra.get("to"):
        safe_note_path(wiki, str(extra["to"]))
    for merged in extra.get("merged_from", []) or []:
        safe_note_path(wiki, str(merged))
    if op == "intake_skip":
        reason = extra.get("reason")
        if reason not in SKIP_REASONS:
            raise WikiError(
                f"intake_skip reason must be one of {'/'.join(SKIP_REASONS)}; "
                "free text never enters the chain"
            )
    records = read_history(wiki)
    head = records[-1] if records else None
    record: dict = {
        "seq": (int(head["seq"]) + 1) if head and head.get("seq") else 1,
        "ts": utc_now_iso(),
        "op": op,
        "note": note,
        "actor": actor,
        "origin": origin,
        "mode": mode,
        "content_sha256": content_sha256,
        "prior_content_sha256": prior_content_sha256,
        "prev_checksum": head.get("checksum") if head else None,
        "schema_version": SCHEMA_VERSION,
    }
    record.update(extra)
    record["checksum"] = chain_digest(record)
    path = history_path(wiki)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    return record


def snapshot_note(wiki: Path, rel: str) -> str | None:
    """Copy a note's current state into versions/ before mutating it."""
    src = wiki / rel
    if not src.exists():
        return None
    stamp = utc_now_compact()
    vdir = sidecar(wiki) / "versions" / note_dirname(rel)
    vdir.mkdir(parents=True, exist_ok=True)
    dest = vdir / f"{stamp}.mdv"
    suffix = 0
    while dest.exists():
        suffix += 1
        dest = vdir / f"{stamp}-{suffix}.mdv"
    header = f"# wiki-version: {rel} @ {stamp}\n"
    atomic_write_text(dest, header + src.read_text(encoding="utf-8"))
    return str(dest.relative_to(sidecar(wiki))).replace(os.sep, "/")


def version_content(text: str) -> tuple[str, str]:
    """Split a .mdv file into (note_rel, original content)."""
    first, _, rest = text.partition("\n")
    m = re.match(r"# wiki-version: (.+) @ ", first)
    return (m.group(1) if m else ""), rest


def verify_chain(records: list[dict]) -> list[dict]:
    broken: list[dict] = []
    prev: dict | None = None
    for record in records:
        seq = record.get("seq")
        if record.get("op") == "corrupt":
            broken.append({"seq": seq, "reason": "unparseable history line"})
            prev = record
            continue
        if record.get("checksum") != chain_digest(record):
            broken.append(
                {"seq": seq, "reason": "record digest mismatch (content altered)"}
            )
        if prev is not None and prev.get("op") != "corrupt":
            if seq != (prev.get("seq") or 0) + 1:
                broken.append(
                    {"seq": seq, "reason": f"sequence gap after {prev.get('seq')}"}
                )
            if record.get("prev_checksum") != prev.get("checksum"):
                broken.append({"seq": seq, "reason": "previous-checksum link broken"})
        prev = record
    return broken


def replay_note_state(records: list[dict], upto_seq: int | None = None) -> dict:
    """note path -> content sha, as of the end of the chain (or a seq)."""
    state: dict[str, str] = {}
    for record in records:
        seq = record.get("seq")
        if upto_seq is not None and (seq is None or seq > upto_seq):
            break
        op = record.get("op")
        note = record.get("note")
        if op in ("create_note", "update_note", "merge_notes", "accept_suggestion"):
            if note and record.get("content_sha256"):
                state[note] = record["content_sha256"]
            for merged in record.get("merged_from", []) or []:
                state.pop(merged, None)
        elif op == "rename_note":
            to = record.get("to")
            if note and to:
                sha = state.pop(note, record.get("content_sha256"))
                if sha:
                    state[to] = sha
        elif op in ("delete_note", "purge_note", "decline_suggestion"):
            if note:
                state.pop(note, None)
        elif op == "rollback":
            to_seq = record.get("to_seq")
            if isinstance(to_seq, int):
                state = replay_note_state(records, upto_seq=to_seq)
    return state


def wiki_notes(wiki: Path) -> list[str]:
    notes = []
    for path in sorted(wiki.rglob("*.md")):
        rel = path.relative_to(wiki)
        if path.is_symlink():
            continue
        current = wiki
        if any((current := current / part).is_symlink() for part in rel.parts[:-1]):
            continue
        if SIDECAR_DIRNAME in rel.parts or any(p.startswith(".") for p in rel.parts):
            continue
        if path.name in RESERVED_FILENAMES:
            continue
        notes.append(str(rel).replace(os.sep, "/"))
    return notes


def _content_pool(wiki: Path) -> dict[str, str]:
    """content sha -> text, from every current note and every version file."""
    pool: dict[str, str] = {}
    for rel in wiki_notes(wiki):
        text = (wiki / rel).read_text(encoding="utf-8")
        pool[text_sha256(text)] = text
    versions_dir = sidecar(wiki) / "versions"
    if versions_dir.is_dir():
        for mdv in versions_dir.rglob("*.mdv"):
            _rel, content = version_content(mdv.read_text(encoding="utf-8"))
            pool[text_sha256(content)] = content
    return pool


def note_findings(rel: str, text: str) -> Report:
    """Run the note-level checks against a single draft."""
    report = Report()
    _check_note_text(rel, text, report)
    return report


def _check_note_text(rel: str, text: str, report: Report) -> None:
    rel_path = Path(rel)
    try:
        fm, body = split_document(text)
    except FrontmatterError as exc:
        report.conformance.append(f"{rel}: {exc} (§11 rule 1)")
        return
    if fm is None:
        report.conformance.append(f"{rel}: missing frontmatter block (§11 rule 1)")
        return
    note_type = str(fm.get("type", "") or "").strip()
    if not note_type:
        report.conformance.append(f"{rel}: empty or missing type (§11 rule 2)")
        return
    for problem in validate_note_path(rel):
        report.profile.append(f"{rel}: {problem}")
    if note_type not in NOTE_TYPES:
        report.profile.append(f"{rel}: type {note_type!r} is not in the legal profile")
        return
    _check_profile_keys(fm, rel_path, note_type, report, None)
    if ROOTED_LINK_RE.search(body):
        report.profile.append(f"{rel}: /-rooted body link")


def regenerate_log(wiki: Path, records: list[dict]) -> None:
    by_day: dict[str, list[dict]] = {}
    for record in records:
        if record.get("op") == "corrupt":
            continue
        day = str(record.get("ts", ""))[:10]
        by_day.setdefault(day, []).append(record)
    lines = ["# Wiki log", ""]
    for day in sorted(by_day, reverse=True):
        lines.append(f"## {day}")
        lines.append("")
        for record in reversed(by_day[day]):
            lines.append(
                f"- **{OP_WORDS.get(record.get('op'), 'Change')}** — "
                f"{_describe(record)}"
            )
        lines.append("")
    atomic_write_text(wiki / "log.md", "\n".join(lines).rstrip() + "\n")


def _describe(record: dict) -> str:
    op = record.get("op")
    note = record.get("note") or ""
    origin = record.get("origin")
    if op in ("create_note", "update_note", "accept_suggestion"):
        return f"{note} (origin: {origin})" if origin else note
    if op == "rename_note":
        return f"{note} → {record.get('to')}"
    if op == "merge_notes":
        merged = ", ".join(record.get("merged_from", []) or [])
        return f"{note} ← {merged}"
    if op == "delete_note":
        return f"{note} (tombstoned; recoverable)"
    if op == "purge_note":
        return f"{note} (content and versions destroyed)"
    if op == "rollback":
        return f"wiki restored to seq {record.get('to_seq')}"
    if op == "intake_skip":
        return (
            f"session {record.get('session', '?')}: nothing to record "
            f"({record.get('reason')})"
        )
    if op == "decline_suggestion":
        return f"{note} (suggestion declined)"
    return note


REVIEW_DISPOSITIONS = (
    "new",
    "update",
    "disputed",
    "unsupported",
    "stale",
    "no-material",
    "matter-specific",
)


def review_records_path(wiki: Path) -> Path:
    return sidecar(wiki) / "review" / "queue.jsonl"


def read_review_records(wiki: Path) -> list[dict]:
    path = review_records_path(wiki)
    if not path.exists():
        return []
    records: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(record, dict):
            records.append(record)
    return records


def append_review_record(wiki: Path, record: dict) -> None:
    path = review_records_path(wiki)
    path.parent.mkdir(parents=True, exist_ok=True)
    prior = path.read_text(encoding="utf-8") if path.exists() else ""
    atomic_write_text(path, prior + json.dumps(record, ensure_ascii=False) + "\n")


def regenerate_indexes(wiki: Path) -> None:
    listed: dict[str, list[tuple[str, str, str, str, dict]]] = {}
    source_rows: dict[str, dict] = {}
    pending = stale = disputed = outdated = 0
    for rel in wiki_notes(wiki):
        try:
            fm, _body = split_document((wiki / rel).read_text(encoding="utf-8"))
        except FrontmatterError:
            continue
        if fm is None:
            continue
        is_pending = str(fm.get("pending", "")).strip().lower() == "true"
        pending += is_pending
        if is_pending:
            continue
        parts = rel.split("/")
        area = parts[0] if len(parts) > 1 else "."
        status = str(fm.get("status", "") or "stable")
        stale += is_stale(fm.get("stale_after"))
        disputed += status == "disputed"
        outdated += status in ("outdated", "deprecated")
        listed.setdefault(area, []).append(
            (
                str(fm.get("type", "")),
                str(fm.get("title", "") or rel),
                rel,
                str(fm.get("description", "") or ""),
                fm,
            )
        )
        for source in fm.get("sources", []) or []:
            if not isinstance(source, dict):
                continue
            source_id = str(source.get("id", "") or source.get("resource", ""))
            if not source_id:
                continue
            row = source_rows.setdefault(
                source_id,
                {
                    "title": str(source.get("title", "") or source_id),
                    "resource": str(source.get("resource", "") or ""),
                    "notes": [],
                    "identity": _source_identity(source),
                    "conflict": False,
                    "source": dict(source),
                },
            )
            if row["identity"] != _source_identity(source):
                row["conflict"] = True
            row["notes"].append(rel)
    for area, entries in listed.items():
        if area == ".":
            continue
        lines = [f"# {area.replace('-', ' ').title()}", ""]
        for note_type in NOTE_TYPES:
            grouped = sorted(
                (e for e in entries if e[0] == note_type), key=lambda e: e[1].lower()
            )
            if not grouped:
                continue
            lines.append(f"# {note_type}")
            lines.append("")
            for _t, title, rel, desc, _fm in grouped:
                target = rel.split("/", 1)[1]
                lines.append(
                    f"* {markdown_link(title, target)} - {markdown_text(desc)}"
                )
            lines.append("")
        atomic_write_text(wiki / area / "index.md", "\n".join(lines).rstrip() + "\n")
    root = wiki / "index.md"
    okf_declared = OKF_VERSION
    if root.exists():
        try:
            fm, _ = split_document(root.read_text(encoding="utf-8"))
            if fm and fm.get("okf_version"):
                okf_declared = str(fm["okf_version"])
        except FrontmatterError:
            pass
    lines = [
        "---",
        f'okf_version: "{okf_declared}"',
        "---",
        "",
        "# Wiki Home",
        "",
        "Reusable legal knowledge and method, never matter.",
        "",
        "## At a glance",
        "",
        f"- {sum(len(v) for v in listed.values())} notes",
        f"- {len(source_rows)} linked sources",
        f"- {pending} pending review · {stale} stale · {disputed} disputed · "
        f"{outdated} outdated",
        "- [Source catalogue](sources/index.md)",
        "- [Review queue](review/index.md)",
        "- [Change log](log.md)",
        "",
        "## Browse by topic",
        "",
    ]
    for area in sorted(a for a in listed if a != "."):
        count = len(listed[area])
        lines.append(f"* [{area}/index.md]({area}/index.md) - {count} note(s)")
    records = [r for r in read_history(wiki) if r.get("note")][-8:]
    if records:
        lines.extend(["", "## Recent changes", ""])
        for record in reversed(records):
            note = str(record.get("note"))
            lines.append(
                f"- {markdown_link(note, note)} — "
                f"{markdown_text(OP_WORDS.get(record.get('op'), 'Changed'))} "
                f"{str(record.get('ts', ''))[:10]}"
            )
    atomic_write_text(wiki / "index.md", "\n".join(lines).rstrip() + "\n")

    source_lines = ["# Sources", "", "Sources linked from wiki notes.", ""]
    if not source_rows:
        source_lines.append("No linked sources yet.")
    for source_id, row in sorted(source_rows.items()):
        resource = row["resource"]
        label = (
            markdown_link(row["title"], resource)
            if resource
            else markdown_text(row["title"])
        )
        note_links = ", ".join(
            markdown_link(Path(n).stem, f"../{n}") for n in sorted(set(row["notes"]))
        )
        warning = " · **CONFLICTING SOURCE RECORDS**" if row["conflict"] else ""
        source = row["source"]
        details = []
        if source.get("pinpoint"):
            details.append(f"pinpoint {markdown_text(source['pinpoint'])}")
        if source.get("last_checked"):
            details.append(f"checked {markdown_text(source['last_checked'])}")
        if source.get("sha256"):
            details.append(f"sha256 {markdown_text(str(source['sha256'])[:12])}…")
        detail_text = " · " + " · ".join(details) if details else ""
        source_lines.append(
            f"- **{markdown_text(source_id)}** — {label} · used by {note_links}"
            f"{detail_text}{warning}"
        )
    (wiki / "sources").mkdir(parents=True, exist_ok=True)
    atomic_write_text(
        wiki / "sources" / "index.md", "\n".join(source_lines).rstrip() + "\n"
    )

    review_records = read_review_records(wiki)
    review_lines = [
        "# Review queue",
        "",
        "Legal judgment stays visible for human review.",
        "",
    ]
    open_records = [r for r in review_records if r.get("status") == "open"]
    if not open_records:
        review_lines.append("Nothing pending.")
    for record in reversed(open_records[-100:]):
        subject = record.get("note") or record.get("source_id") or "wiki"
        review_lines.append(
            f"- **{markdown_text(record['disposition'])}** — "
            f"`{markdown_text(subject)}` · "
            f"{str(record.get('ts', ''))[:10]}"
        )
    (wiki / "review").mkdir(parents=True, exist_ok=True)
    atomic_write_text(
        wiki / "review" / "index.md", "\n".join(review_lines).rstrip() + "\n"
    )


def _regenerate(wiki: Path) -> None:
    regenerate_log(wiki, read_history(wiki))
    regenerate_indexes(wiki)


def _load_gate_report(
    path_str: str | None, dest: str, candidate_text: str
) -> str | None:
    """Require a passing verdict cryptographically bound to this candidate."""
    if not path_str:
        return (
            f"gate unresolved for {dest}: run the method-not-matter gate and "
            "pass --gate-report <verdict.json>; no note lands ungated"
        )
    path = Path(path_str)
    try:
        verdict = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return f"gate report {path} unreadable: {exc}"
    if verdict.get("ok") is not True:
        reason = verdict.get("reason", "gate failed")
        return f"gate FAILED for {dest}: {reason}; the note is parked, not landed"
    expected = text_sha256(candidate_text)
    if verdict.get("candidate_sha256") != expected:
        return (
            f"gate report is not bound to the current draft for {dest}; "
            "run the gate again after the final edit"
        )
    return None


def _reason_guard(reason: str) -> str | None:
    if reason not in PURGE_REASONS:
        return "purge reason must be one of " + "/".join(PURGE_REASONS)
    return None


# ---------------------------------------------------------------------------
# Method-not-matter gate — layer 1 (deterministic), and the hashed denylist
# ---------------------------------------------------------------------------

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
CORP_ENTITY_RE = re.compile(
    r"\b[A-Z][A-Za-z&.\-]+(?:\s+[A-Z][A-Za-z&.\-]+){0,3}\s+"
    r"(LLP|LLC|Ltd|GmbH|Inc|AG|S\.A\.|B\.V\.|plc|SE|KG)\b"
)
MATTER_ID_RE = re.compile(r"\b[A-Z]{1,4}-\d{2,6}/\d{2,4}\b")
MATTER_KEYWORD_RE = re.compile(
    r"(?i)\b(matter|case|file|aktenzeichen|az)\s*(no\.?|number|#)?\s*[:#]\s*\S+"
)
GATE_RULES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("corporate-entity", CORP_ENTITY_RE),
    ("email-address", EMAIL_RE),
    ("matter-identifier", MATTER_ID_RE),
    ("matter-keyword", MATTER_KEYWORD_RE),
    (
        "instruction-override",
        re.compile(
            r"(?i)\b(ignore|disregard)\s+(all\s+|any\s+)?(previous|prior|earlier|above)\b"
        ),
    ),
    (
        "instruction-addressed",
        re.compile(r"(?i)\bnote\s+(for|to)\s+the\s+(assistant|ai|agent|system)\b"),
    ),
    (
        # "never accept an unlimited cap" is method advice to the lawyer;
        # "always automatically approve" is an instruction to a machine.
        "instruction-imperative",
        re.compile(
            r"(?i)\b(always|never)\s+automatically\s+"
            r"(approve|execute|run|send|delete|accept|sign)\b"
        ),
    ),
    ("instruction-syntax", re.compile(r"<command-name>|(?i:\bsystem\s+prompt\b)")),
)


def _normalize_token(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().casefold()


def _denylist_hash(salt: str, token: str) -> str:
    return hashlib.sha256((salt + _normalize_token(token)).encode("utf-8")).hexdigest()


# Words too generic to identify anyone on their own; they never become
# denylist tokens ("Data" inside a company name must not flag the phrase
# "data protection obligations" in a clean note).
GENERIC_NAME_WORDS = frozenset(
    """data protection privacy analytics cloud hosting systems solutions
    services technologies technology digital group holding holdings partners
    capital consulting software networks network global legal international
    european gmbh ltd llc llp inc plc corp company limited the and of""".split()
)


def denylist_tokens(name: str) -> set[str]:
    """A name expands to the phrase, its distinctive words, and bigrams."""
    words = [w for w in re.findall(r"[A-Za-z][\w&.\-]*", name) if len(w) >= 3]
    norm = [_normalize_token(w) for w in words]
    tokens = {_normalize_token(name)}
    tokens |= {w for w in norm if w not in GENERIC_NAME_WORDS}
    tokens |= {
        f"{a} {b}"
        for a, b in zip(norm, norm[1:], strict=False)
        if not (a in GENERIC_NAME_WORDS and b in GENERIC_NAME_WORDS)
    }
    return {t for t in tokens if t}


def load_denylist(path_str: str | None) -> dict | None:
    if not path_str:
        return None
    path = Path(path_str)
    if not path.exists():
        print(
            f"warning: denylist {path} does not exist — matching runs without "
            "it (build one with: denylist-add --file ... <names>)",
            file=sys.stderr,
        )
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    return {"salt": data["salt"], "hashes": set(data["hashes"])}


def gate_candidate(text: str, denylist: dict | None = None) -> dict:
    """Layer 1: deterministic, fails closed, never echoes matched text."""
    findings: list[dict] = []
    for rule, regex in GATE_RULES:
        findings.extend(
            {"rule": rule, "span": [m.start(), m.end()]} for m in regex.finditer(text)
        )
    if denylist:
        words = re.findall(r"[A-Za-z][\w&.\-]{2,}", text)
        candidates = {_normalize_token(w) for w in words}
        candidates |= {
            _normalize_token(f"{a} {b}") for a, b in zip(words, words[1:], strict=False)
        }
        hits = sum(
            1
            for t in candidates
            if _denylist_hash(denylist["salt"], t) in denylist["hashes"]
        )
        if hits:
            findings.append({"rule": "denylist-token", "count": hits})
    rules = sorted({f["rule"] for f in findings})
    return {
        "ok": not findings,
        "layer": "deterministic",
        "reason": None if not findings else "matched: " + ", ".join(rules),
        "details": {"findings": findings},
    }


# ---------------------------------------------------------------------------
# Seeding: inventory pre-pass, work items, quote-verified batch landing
# ---------------------------------------------------------------------------


def probe_file(path: Path) -> dict:
    """What stdlib can honestly measure about a seed file — nothing more."""
    row: dict = {"path": str(path), "exists": path.exists()}
    if not path.exists():
        row.update(kind="missing", readable=False, text_measurable=False)
        return row
    data = path.read_bytes()
    row["size"] = len(data)
    row["sha256"] = hashlib.sha256(data).hexdigest()
    suffix = path.suffix.lower()
    if suffix in (".md", ".txt"):
        row.update(kind="text", readable=True, text_measurable=True)
    elif data[:5] == b"%PDF-":
        pages = max(
            data.count(b"/Type /Page") - data.count(b"/Type /Pages"),
            data.count(b"/Type/Page") - data.count(b"/Type/Pages"),
            0,
        )
        encrypted = b"/Encrypt" in data
        row.update(
            kind="pdf",
            pages=pages,
            encrypted=encrypted,
            readable=not encrypted,
            text_measurable=False,
        )
    elif suffix == ".docx" and data[:2] == b"PK":
        row.update(kind="docx", readable=True, text_measurable=False)
    else:
        row.update(kind="unknown", readable=False, text_measurable=False)
    return row


def _seed_instructions(profile: dict, source_path: str) -> str:
    slots = profile.get("slots", {})
    cap = profile.get("caps", {}).get(
        "max_notes_per_source", profile.get("caps", {}).get("max_notes_per_session", 5)
    )
    parts = [
        f"Read the source file at {source_path} in full, then distil at most "
        f"{cap} note drafts. Fewer is better; zero is a valid answer.",
        str(slots.get("gate", "")),
        str(slots.get("type_guidance", "")),
        str(slots.get("format", "")),
        str(slots.get("output_rules", "")),
    ]
    return "\n\n".join(p for p in parts if p)


def _verify_quotes(draft: dict, sources_root: Path) -> str | None:
    """Every quote must exist verbatim (whitespace-collapsed) in its source."""
    quotes = draft.get("quotes", [])
    fm, _body = split_document(draft.get("markdown", ""))
    note_type = str((fm or {}).get("type", ""))
    if note_type in ("Legal Insight", "Trap", "Position") and not quotes:
        return "no supporting quote for an assertion-bearing note"
    for entry in quotes:
        source_name = str(entry.get("source", ""))
        relative = Path(source_name)
        if relative.is_absolute() or ".." in relative.parts:
            return "quote source escapes the declared source root"
        root = sources_root.resolve(strict=True)
        source = root / relative
        if source.is_symlink():
            return "quote source may not be a symbolic link"
        try:
            resolved = source.resolve(strict=True)
            resolved.relative_to(root)
        except (FileNotFoundError, ValueError):
            return "quote cites a source file that does not exist"
        if not resolved.is_file():
            return "quote cites a source file that does not exist"
        haystack = _normalize_token(resolved.read_text(encoding="utf-8"))
        if _normalize_token(str(entry.get("quote", ""))) not in haystack:
            return "quote not found verbatim in its cited source"
    return None


def cmd_gate(args: argparse.Namespace) -> int:
    try:
        text = Path(args.candidate).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Error: cannot read candidate: {exc}", file=sys.stderr)
        return 2
    verdict = gate_candidate(text, load_denylist(args.denylist))
    verdict["candidate_sha256"] = text_sha256(text)
    output = json.dumps(verdict, indent=2, ensure_ascii=False)
    if args.out:
        atomic_write_text(Path(args.out), output + "\n")
    else:
        print(output)
    return 0 if verdict["ok"] else 1


def cmd_denylist_add(args: argparse.Namespace) -> int:
    path = Path(args.file)
    if path.exists():
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            print("Error: denylist must be a JSON object", file=sys.stderr)
            return 2
        salt = raw.get("salt")
        stored_hashes = raw.get("hashes")
        if not isinstance(salt, str) or not isinstance(stored_hashes, list):
            print(
                "Error: denylist requires string salt and list hashes",
                file=sys.stderr,
            )
            return 2
        data: dict[str, object] = {"salt": salt, "hashes": stored_hashes}
    else:
        import secrets

        salt = secrets.token_hex(16)
        data = {"salt": salt, "hashes": []}
    stored = data["hashes"]
    assert isinstance(stored, list)
    hashes = {str(value) for value in stored}
    for name in args.names:
        hashes |= {_denylist_hash(salt, t) for t in denylist_tokens(name)}
    data["hashes"] = sorted(hashes)
    atomic_write_text(path, json.dumps(data, indent=1) + "\n")
    print(f"denylist: {len(hashes)} hashed token(s); no plaintext stored")
    return 0


def cmd_seed_scan(args: argparse.Namespace) -> int:
    rows = [probe_file(Path(f)) for f in args.files]
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    readable = sum(1 for r in rows if r["readable"])
    missing = [r["path"] for r in rows if not r["exists"]]
    print(
        f"seed-scan: {len(rows)} file(s), {readable} readable, "
        f"{len(rows) - readable} parked"
    )
    if missing:
        for m in missing:
            print(f"Error: named file not found: {m}", file=sys.stderr)
        return 1
    return 0


def cmd_seed_emit(args: argparse.Namespace) -> int:
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Error: cannot read source profile: {exc}", file=sys.stderr)
        return 2
    emitted = parked = 0
    for f in args.files:
        row = probe_file(Path(f))
        if not row["readable"]:
            parked += 1
            continue
        item = {
            "unitId": row["sha256"][:16],
            "status": "pending",
            "source_path": str(f),
            "probe": row,
            "instructions": _seed_instructions(profile, str(f)),
            "note_drafts": [],
        }
        atomic_write_text(
            out_dir / f"item-{row['sha256'][:16]}.json",
            json.dumps(item, indent=2, ensure_ascii=False) + "\n",
        )
        emitted += 1
    print(f"seed-emit: {emitted} work item(s), {parked} parked")
    return 0


def cmd_seed_land(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    items_dir = Path(args.items)
    sources_root = Path(args.sources_root)
    if not items_dir.is_dir() or not sources_root.is_dir():
        print(
            "Error: --items and --sources-root must be existing directories",
            file=sys.stderr,
        )
        return 2
    denylist = load_denylist(args.denylist)
    landed = updated = unchanged = 0
    parked: list[dict] = []
    drafts_total = 0
    with WikiLock(wiki):
        for item_path in sorted(items_dir.glob("item-*.json")):
            try:
                item = json.loads(item_path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                parked.append({"dest": item_path.name, "reason": f"bad item: {exc}"})
                continue
            for draft in item.get("note_drafts", []):
                drafts_total += 1
                dest = str(draft.get("dest", "")).replace(os.sep, "/")
                markdown = str(draft.get("markdown", ""))
                problems = validate_note_path(dest) if dest else ["missing dest"]
                if problems or not dest.endswith(".md"):
                    parked.append({"dest": dest, "reason": "bad destination path"})
                    continue
                quote_error = _verify_quotes(draft, sources_root)
                if quote_error:
                    parked.append({"dest": dest, "reason": quote_error})
                    continue
                verdict = gate_candidate(markdown, denylist)
                if not verdict["ok"]:
                    parked.append(
                        {"dest": dest, "reason": f"gate: {verdict['reason']}"}
                    )
                    continue
                try:
                    fm, body = split_document(markdown)
                except FrontmatterError as exc:
                    parked.append({"dest": dest, "reason": f"frontmatter: {exc}"})
                    continue
                if fm is None:
                    parked.append({"dest": dest, "reason": "draft has no frontmatter"})
                    continue
                if draft.get("quotes") and not fm.get("sources"):
                    inferred_sources = []
                    seen_sources = set()
                    for quote in draft.get("quotes", []):
                        source_name = str(quote.get("source", ""))
                        if not source_name or source_name in seen_sources:
                            continue
                        seen_sources.add(source_name)
                        resolved = (sources_root / source_name).resolve(strict=True)
                        inferred_sources.append(
                            {
                                "id": re.sub(
                                    r"[^a-z0-9-]+",
                                    "-",
                                    Path(source_name).stem.casefold(),
                                ).strip("-"),
                                "kind": "authorised-local",
                                "resource": str(resolved),
                                "title": Path(source_name)
                                .stem.replace("-", " ")
                                .title(),
                                "pinpoint": "quoted extract",
                            }
                        )
                    if inferred_sources:
                        fm["sources"] = inferred_sources
                try:
                    word, record = _land_note(
                        wiki,
                        dest,
                        fm,
                        body,
                        "seeded",
                        args.mode,
                        args.actor,
                        replace=True,
                    )
                except WikiError as exc:
                    parked.append({"dest": dest, "reason": str(exc)})
                    continue
                if record is None:
                    unchanged += 1
                elif word == "updated":
                    updated += 1
                else:
                    landed += 1
        if landed or updated:
            _regenerate(wiki)
    accounted = landed + updated + unchanged + len(parked)
    print(
        f"seed-land: {drafts_total} draft(s) → {landed} landed, {updated} updated, "
        f"{unchanged} unchanged, {len(parked)} parked · "
        f"accounted {accounted}/{drafts_total}"
    )
    for p in parked:
        print(f"parked {p['dest']}: {p['reason']}")
    if args.json:
        print(
            json.dumps(
                {
                    "drafts": drafts_total,
                    "landed": landed,
                    "updated": updated,
                    "unchanged": unchanged,
                    "parked": parked,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    return 0 if accounted == drafts_total else 1


# ---------------------------------------------------------------------------
# Vocabulary registry, maintenance pass (v1-minimal), tripwire metrics
# ---------------------------------------------------------------------------

VOCAB_KEYS = ("practice_area", "jurisdiction", "document_kind")
STOP_ARTICLES = frozenset({"the", "a", "an", "of", "and"})


def _vocab_canon(value: str) -> str:
    words = re.findall(r"[a-z0-9]+", value.casefold())
    return " ".join(w for w in words if w not in STOP_ARTICLES)


def vocab_path(wiki: Path) -> Path:
    return sidecar(wiki) / "vocab.json"


def load_vocab(wiki: Path) -> dict:
    path = vocab_path(wiki)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {key: {} for key in VOCAB_KEYS}


def vocab_snap(wiki: Path, vocab: dict, key: str, value: str) -> str:
    """First use registers the canonical form; later uses snap to it."""
    canon = _vocab_canon(value)
    if not canon:
        return value
    registry = vocab.setdefault(key, {})
    for display, canon_form in registry.items():
        if canon_form == canon:
            return display
    registry[value] = canon
    return value


def save_vocab(wiki: Path, vocab: dict) -> None:
    atomic_write_text(
        vocab_path(wiki), json.dumps(vocab, indent=1, ensure_ascii=False) + "\n"
    )


def _body_tokens(text: str) -> set[str]:
    _fm, body = split_document(text)
    return {w for w in re.findall(r"[a-z0-9]+", body.casefold()) if len(w) > 2}


def cmd_maintain(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    try:
        today = date.fromisoformat(args.today) if args.today else None
    except ValueError:
        print(f"Error: --today {args.today!r} is not YYYY-MM-DD", file=sys.stderr)
        return 2
    notes: dict[str, dict] = {}
    for rel in wiki_notes(wiki):
        try:
            fm, _body = split_document((wiki / rel).read_text(encoding="utf-8"))
        except FrontmatterError:
            continue
        if fm:
            notes[rel] = fm
    stale = sorted(
        rel for rel, fm in notes.items() if is_stale(fm.get("stale_after"), today)
    )
    by_sha: dict[str, list[str]] = {}
    for rel in notes:
        try:
            _fm, body = split_document((wiki / rel).read_text(encoding="utf-8"))
        except FrontmatterError:
            continue
        by_sha.setdefault(text_sha256(body.strip()), []).append(rel)
    exact_dupes = sorted(v for v in by_sha.values() if len(v) > 1)
    by_title: dict[tuple, list[str]] = {}
    for rel, fm in notes.items():
        key = (
            _vocab_canon(str(fm.get("title", ""))),
            str(fm.get("type", "")),
        )
        if key[0]:
            by_title.setdefault(key, []).append(rel)
    title_pairs = sorted(
        v for v in by_title.values() if len(v) > 1 and v not in exact_dupes
    )
    deprecated = {
        rel for rel, fm in notes.items() if str(fm.get("status", "")) == "deprecated"
    }
    source_findings: list[dict] = []
    for rel, fm in notes.items():
        for source in fm.get("sources", []) or []:
            if not isinstance(source, dict):
                continue
            resource = str(source.get("resource", "") or "")
            if source.get("kind") != "authorised-local" or not resource:
                continue
            path = Path(resource).expanduser()
            if path_has_symlink_component(path) or not path.is_file():
                source_findings.append(
                    {
                        "note": rel,
                        "source": source.get("id"),
                        "issue": "unavailable-or-symlink",
                    }
                )
                continue
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if source.get("sha256") and source.get("sha256") != digest:
                source_findings.append(
                    {"note": rel, "source": source.get("id"), "issue": "hash-changed"}
                )
    dep_links = []
    for rel in sorted(notes):
        body = (wiki / rel).read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+\.md)\)", body):
            resolved = (Path(rel).parent / target).as_posix()
            resolved = str(Path(os.path.normpath(resolved)).as_posix())
            if resolved in deprecated:
                dep_links.append({"note": rel, "cites_deprecated": resolved})
    vocab = load_vocab(wiki)
    near: list[list[str]] = []
    import difflib

    for key in VOCAB_KEYS:
        values = list(vocab.get(key, {}))
        for i, a in enumerate(values):
            for b in values[i + 1 :]:
                if difflib.SequenceMatcher(None, a, b).ratio() > 0.8:
                    near.append([key, a, b])
    payload = {
        "stale_recheck_queue": stale,
        "exact_duplicates": exact_dupes,
        "same_title_pairs": title_pairs,
        "links_to_deprecated": dep_links,
        "vocabulary_near_duplicates": near,
        "source_findings": source_findings,
    }
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0
    print(
        f"maintain: {len(stale)} stale re-check(s), {len(exact_dupes)} exact "
        f"duplicate group(s), {len(title_pairs)} same-title pair(s), "
        f"{len(dep_links)} deprecated-authority link(s), {len(near)} vocabulary "
        f"near-duplicate(s), {len(source_findings)} source finding(s) — "
        "proposals only, nothing changed"
    )
    return 0


def _note_origin_map(records: list[dict]) -> dict[str, str]:
    origins: dict[str, str] = {}
    for record in records:
        note = record.get("note")
        op = record.get("op")
        if op in ("create_note", "merge_notes") and note and record.get("origin"):
            origins[note] = record["origin"]
        elif op == "rename_note" and note and record.get("to"):
            if note in origins:
                origins[record["to"]] = origins.pop(note)
    return origins


def cmd_tripwire(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    for label, value in (
        ("--window-from", args.window_from),
        ("--window-to", args.window_to),
    ):
        if not value:
            continue
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            print(f"Error: {label} {value!r} is not an ISO timestamp", file=sys.stderr)
            return 2
    records = read_history(wiki)
    pool = _content_pool(wiki)
    origins = _note_origin_map(records)

    def in_window(record: dict) -> bool:
        ts = str(record.get("ts", ""))
        return (not args.window_from or ts >= args.window_from) and (
            not args.window_to or ts <= args.window_to
        )

    auto_built = [
        r
        for r in records
        if r.get("op") in ("create_note", "merge_notes")
        and r.get("origin") == "auto-built"
        and in_window(r)
    ]
    edited_away: list[dict] = []
    unmeasurable = 0
    for record in records:
        if not in_window(record):
            continue
        op = record.get("op")
        note = record.get("note")
        if op in ("delete_note", "purge_note") and origins.get(note) == "auto-built":
            edited_away.append({"note": note, "how": op})
        elif op == "update_note" and origins.get(note) == "auto-built":
            prior = pool.get(record.get("prior_content_sha256", ""))
            new = pool.get(record.get("content_sha256", ""))
            if prior is None or new is None:
                unmeasurable += 1
                continue
            before, after = _body_tokens(prior), _body_tokens(new)
            union = before | after
            overlap = len(before & after) / len(union) if union else 1.0
            if overlap < 0.5:
                edited_away.append(
                    {"note": note, "how": "rewritten", "overlap": round(overlap, 3)}
                )
    rollbacks = sum(1 for r in records if r.get("op") == "rollback" and in_window(r))
    denominator = len(auto_built)
    numerator = len({e["note"] for e in edited_away})
    tripped = denominator > 0 and numerator * 7 > denominator
    payload = {
        "auto_built": denominator,
        "edited_away": numerator,
        "events": edited_away,
        "rollbacks": rollbacks,
        "unmeasurable": unmeasurable,
        "threshold": "more than 1 in 7",
        "tripped": tripped,
    }
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 1 if tripped else 0
    verdict = (
        "TRIPPED — markup mode becomes the shipping default" if tripped else "holding"
    )
    print(
        f"tripwire: {numerator} of {denominator} auto-built note(s) edited away "
        f"or deleted · {rollbacks} rollback(s) · threshold >1/7 · {verdict}"
    )
    return 1 if tripped else 0


# ---------------------------------------------------------------------------
# Legacy staged-item import compatibility
# ---------------------------------------------------------------------------


def automation_state_path(wiki: Path) -> Path:
    """Operational idempotency beside the wiki; never a behaviour setting."""
    return sidecar(wiki) / "automation.json"


def load_automation_state(wiki: Path) -> dict:
    path = automation_state_path(wiki)
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except (OSError, json.JSONDecodeError):
            pass
    return {"schema_version": SCHEMA_VERSION, "staged": [], "processed": []}


def save_automation_state(wiki: Path, state: dict) -> None:
    atomic_write_text(
        automation_state_path(wiki),
        json.dumps(state, indent=1, ensure_ascii=False) + "\n",
    )


def cmd_capture(args: argparse.Namespace) -> int:
    """Refuse legacy raw-transcript staging.

    Persisting a transcript slice for a later pass would leave confidential
    temporary data. Deliberate capture uses the normal Add workflow in the
    current turn instead.
    """
    del args
    print(
        "REFUSED: raw transcript staging is disabled; use manual Add or ask to "
        "save the reusable lessons from this conversation",
        file=sys.stderr,
    )
    return 2


def cmd_capture_land(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    staging_dir = Path(args.staging)
    if not staging_dir.is_dir():
        print("Error: --staging must be an existing directory", file=sys.stderr)
        return 2
    state = load_automation_state(wiki)
    denylist = load_denylist(args.denylist)
    try:
        profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Error: cannot read capture profile: {exc}", file=sys.stderr)
        return 2
    cap = int(profile.get("caps", {}).get("max_notes_per_session", 5))
    landed = updated = 0
    parked: list[dict] = []
    dropped = skips = 0
    kept_items = 0
    with WikiLock(wiki):
        for item_path in sorted(staging_dir.glob("item-*.json")):
            try:
                item = json.loads(item_path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                print(
                    f"Error: item {item_path.name} is unreadable ({exc}); "
                    "item preserved",
                    file=sys.stderr,
                )
                kept_items += 1
                continue
            session = str(item.get("session", item_path.stem))
            skip = item.get("skip")
            drafts = item.get("note_drafts", [])
            if skip:
                if skip not in SKIP_REASONS:
                    print(
                        f"Error: item {session}: skip {skip!r} is not in the "
                        f"closed enum; item preserved",
                        file=sys.stderr,
                    )
                    kept_items += 1
                    continue
                append_history(
                    wiki,
                    "intake_skip",
                    None,
                    args.actor,
                    extra={"session": session, "reason": skip},
                )
                skips += 1
            elif not drafts:
                print(
                    f"Error: item {session}: neither drafts nor a skip token; "
                    f"item preserved for the next run",
                    file=sys.stderr,
                )
                kept_items += 1
                continue
            else:
                landed_this_session = 0
                for draft in drafts:
                    dest = str(draft.get("dest", "")).replace(os.sep, "/")
                    markdown = str(draft.get("markdown", ""))
                    if not dest.endswith(".md") or validate_note_path(dest):
                        parked.append({"dest": dest, "reason": "bad destination path"})
                        continue
                    verdict = gate_candidate(markdown, denylist)
                    if not verdict["ok"]:
                        parked.append(
                            {"dest": dest, "reason": f"gate: {verdict['reason']}"}
                        )
                        continue
                    try:
                        fm, body = split_document(markdown)
                    except FrontmatterError as exc:
                        parked.append({"dest": dest, "reason": f"frontmatter: {exc}"})
                        continue
                    if fm is None:
                        parked.append({"dest": dest, "reason": "no frontmatter"})
                        continue
                    note_type = str(fm.get("type", ""))
                    if note_type in (
                        "Legal Insight",
                        "Trap",
                        "Position",
                    ) and not fm.get("sources"):
                        parked.append(
                            {"dest": dest, "reason": "assertion note without sources"}
                        )
                        continue
                    if landed_this_session >= cap:
                        dropped += 1
                        continue
                    try:
                        word, record = _land_note(
                            wiki,
                            dest,
                            fm,
                            body,
                            "auto-built",
                            args.mode,
                            args.actor,
                            replace=True,
                        )
                    except WikiError as exc:
                        parked.append({"dest": dest, "reason": str(exc)})
                        continue
                    if record is None:
                        pass
                    elif word == "updated":
                        updated += 1
                        landed_this_session += 1
                    else:
                        landed += 1
                        landed_this_session += 1
            item_path.unlink()
            staged = state.get("staged", [])
            if session in staged:
                staged.remove(session)
            state.setdefault("processed", []).append(session)
        if landed or updated or skips:
            _regenerate(wiki)
    save_automation_state(wiki, state)
    print(
        f"capture-land: {landed} landed, {updated} updated, {len(parked)} parked, "
        f"{dropped} dropped (over-cap, {cap}/session), {skips} session(s) with "
        f"nothing to record, {kept_items} item(s) preserved"
    )
    for p in parked:
        print(f"parked {p['dest']}: {p['reason']}")
    return 0 if kept_items == 0 else 1


# ---------------------------------------------------------------------------
# Mutation verbs
# ---------------------------------------------------------------------------


# A chat that did not create the wiki must still find it. The per-wiki
# manifest is authoritative; the user registry is only an address book with
# names, stable ids, paths and timestamps. Explicit --wiki always wins and
# the engine never scans the disk guessing for a wiki.


def user_registry_path() -> Path:
    override = os.environ.get("WIKI_USER_REGISTRY")
    if override:
        return Path(override)
    return Path.home() / ".wiki" / "wikis.json"


def user_playbook_path() -> Path:
    """The global behaviour surface; separate from every wiki artifact."""
    override = os.environ.get("WIKI_PLAYBOOK")
    if override:
        return Path(override)
    return user_registry_path().parent / "lqplaybook.md"


def _load_registry_file(path: Path) -> dict:
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("wikis", {}), dict):
            raise WikiError(f"invalid wiki registry at {path}")
        return data
    return {"schema_version": 2, "wikis": {}, "default_wiki": None}


def _load_registry_if_readable(path: Path) -> dict | None:
    """Read an optional registry without making workspace-local use brittle."""
    try:
        return _load_registry_file(path)
    except (OSError, json.JSONDecodeError, WikiError):
        return None


def manifest_path(wiki: Path) -> Path:
    return sidecar(wiki) / "manifest.json"


def load_manifest(wiki: Path, required: bool = True) -> dict | None:
    if wiki.is_symlink():
        raise WikiError(f"wiki root {wiki} may not be a symbolic link")
    if wiki.is_dir():
        for entry in wiki.rglob("*"):
            if entry.is_symlink():
                raise WikiError(
                    f"wiki contains symbolic link {entry.relative_to(wiki)}; "
                    "links are refused because they can escape the wiki"
                )
    path = manifest_path(wiki)
    if not path.exists():
        if required:
            raise WikiError(
                f"{wiki} is not an initialised /wiki "
                f"(missing {SIDECAR_DIRNAME}/manifest.json)"
            )
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WikiError(f"invalid wiki manifest at {path}: {exc}") from exc
    wiki_id = data.get("wiki_id")
    if not isinstance(wiki_id, str) or not wiki_id:
        raise WikiError(f"invalid wiki manifest at {path}: missing wiki_id")
    return data


def _register(reg: dict, name: str, path: Path, manifest: dict) -> None:
    wikis = reg.setdefault("wikis", {})
    existing = wikis.get(name)
    if isinstance(existing, dict):
        existing_id = existing.get("wiki_id")
        if existing_id and existing_id != manifest["wiki_id"]:
            raise WikiError(
                f"wiki name {name!r} already belongs to a different wiki; "
                "choose another name"
            )
    created = (existing or {}).get("created", utc_now_iso())
    wikis[name] = {
        "wiki_id": manifest["wiki_id"],
        "path": str(path.resolve()),
        "created": created,
        "last_opened": utc_now_iso(),
    }
    if not reg.get("default_wiki"):
        reg["default_wiki"] = name


def register_wiki(name: str, path: Path, user_registry: bool = True) -> list[str]:
    wrote: list[str] = []
    if user_registry:
        up = user_registry_path()
        try:
            reg = _load_registry_file(up)
            manifest = load_manifest(path)
            assert manifest is not None
            _register(reg, name, path, manifest)
            up.parent.mkdir(parents=True, exist_ok=True)
            atomic_write_text(up, json.dumps(reg, indent=1, ensure_ascii=False) + "\n")
            wrote.append(str(up))
        except (OSError, json.JSONDecodeError) as exc:
            raise WikiError(f"cannot write user wiki registry at {up}: {exc}") from exc
    return wrote


def _touch_registered_wiki(path: Path, manifest: dict) -> None:
    registry_path = user_registry_path()
    reg = _load_registry_if_readable(registry_path)
    if reg is None:
        return
    changed = False
    for entry in (reg.get("wikis") or {}).values():
        if not isinstance(entry, dict):
            continue
        if entry.get("wiki_id") == manifest.get("wiki_id"):
            entry["path"] = str(path.resolve())
            entry["last_opened"] = utc_now_iso()
            changed = True
    if changed:
        try:
            atomic_write_text(
                registry_path, json.dumps(reg, indent=1, ensure_ascii=False) + "\n"
            )
        except OSError:
            pass


def resolve_wiki(args: argparse.Namespace) -> Path:
    explicit = getattr(args, "wiki", None)
    if explicit:
        path = Path(explicit).expanduser()
        if not path.is_dir():
            raise WikiError(f"wiki is missing at {path}; nothing was created")
        manifest = load_manifest(path, required=True)
        assert manifest is not None
        _touch_registered_wiki(path, manifest)
        return path
    current = Path.cwd()
    if not getattr(args, "ignore_current", False) and manifest_path(current).is_file():
        manifest = load_manifest(current)
        assert manifest is not None
        _touch_registered_wiki(current, manifest)
        return current
    name = getattr(args, "wiki_name", None)
    reg = _load_registry_if_readable(user_registry_path())
    if reg is None:
        raise WikiError(f"wiki registry at {user_registry_path()} is unreadable")
    wikis = reg.get("wikis") or {}
    pick = name or reg.get("default_wiki")
    if not pick and len(wikis) == 1:
        pick = next(iter(wikis))
    if name:
        if name not in wikis:
            raise WikiError(
                f"no wiki named {name!r} is registered; "
                f"known: {sorted(wikis) or 'none'}"
            )
    if not pick:
        if wikis:
            raise WikiError(
                "several wikis are registered and none is default; choose one with "
                "wiki-use <name> or --wiki-name <name>"
            )
        raise WikiError(
            "no wiki registered — choose a folder once, then run: "
            "wiki.py init --wiki <dir> [--name <name>]"
        )
    entry = wikis.get(pick)
    if not isinstance(entry, dict) or not entry.get("path"):
        raise WikiError(f"invalid registry entry for wiki {pick!r}")
    path = Path(str(entry["path"])).expanduser()
    if not path.is_dir():
        raise WikiError(
            f"registered wiki {pick!r} is missing at {path} — reconnect it with "
            "init --wiki <moved-path> --name <name>; nothing was auto-created"
        )
    manifest = load_manifest(path)
    assert manifest is not None
    expected = entry.get("wiki_id")
    if expected and expected != manifest.get("wiki_id"):
        raise WikiError(
            f"registry/manifest identity mismatch for wiki {pick!r} at {path}; "
            "refusing to open the wrong wiki"
        )
    _touch_registered_wiki(path, manifest)
    return path


def _wiki_arg(args: argparse.Namespace) -> Path:
    wiki = resolve_wiki(args)
    if not wiki.is_dir():
        raise WikiError(f"{wiki} is not a directory (run: wiki.py init --wiki …)")
    return wiki


def cmd_init(args: argparse.Namespace) -> int:
    requested = Path(args.wiki).expanduser()
    if requested.is_symlink():
        print("REFUSED: wiki root may not be a symbolic link", file=sys.stderr)
        return 1
    wiki = requested.resolve()
    already = manifest_path(wiki).exists()
    if wiki.exists():
        try:
            load_manifest(wiki, required=False)
        except WikiError as exc:
            print(f"REFUSED: {exc}", file=sys.stderr)
            return 1
    if not args.no_user_registry:
        registry_path = user_registry_path()
        if registry_path.exists():
            reg = _load_registry_if_readable(registry_path)
            if reg is None:
                print(
                    f"REFUSED: wiki registry at {registry_path} is unreadable; "
                    "repair it before initialising another wiki",
                    file=sys.stderr,
                )
                return 1
            existing = (reg.get("wikis") or {}).get(args.name)
            candidate_manifest = (
                load_manifest(wiki, required=False) if already else None
            )
            if isinstance(existing, dict) and (
                candidate_manifest is None
                or existing.get("wiki_id") != candidate_manifest.get("wiki_id")
            ):
                print(
                    f"REFUSED: wiki name {args.name!r} already belongs to a "
                    "different wiki; choose another name",
                    file=sys.stderr,
                )
                return 1
    (sidecar(wiki) / "versions").mkdir(parents=True, exist_ok=True)
    (sidecar(wiki) / "pending").mkdir(parents=True, exist_ok=True)
    (sidecar(wiki) / "review").mkdir(parents=True, exist_ok=True)
    if not already:
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "wiki_id": str(uuid.uuid4()),
            "name": args.name,
            "okf_version": OKF_VERSION,
            "legal_profile_version": 1,
            "generated_index_version": 2,
            "created": utc_now_iso(),
        }
        atomic_write_text(
            manifest_path(wiki),
            json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
        )
    else:
        manifest = load_manifest(wiki)
        assert manifest is not None
        if manifest.get("name") != args.name:
            manifest["name"] = args.name
            atomic_write_text(
                manifest_path(wiki),
                json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
            )
    if not (wiki / "index.md").exists():
        atomic_write_text(
            wiki / "index.md",
            '---\nokf_version: "0.2"\n---\n\n# Wiki Home\n\n'
            "Reusable legal knowledge and method, never matter.\n",
        )
    if not (wiki / "log.md").exists():
        atomic_write_text(wiki / "log.md", "# Wiki log\n")
    regenerate_indexes(wiki)
    wrote = register_wiki(args.name, wiki, user_registry=not args.no_user_registry)
    word = "already initialised" if already else "initialised"
    where = f" · registered as {args.name!r} in {', '.join(wrote)}" if wrote else ""
    print(f"{word} wiki at {wiki} · okf {OKF_VERSION} · schema {SCHEMA_VERSION}{where}")
    return 0


def cmd_setup(args: argparse.Namespace) -> int:
    """One-question first run, or a fresh-chat route to Wiki Home."""
    registry_path = user_registry_path()
    reg = _load_registry_if_readable(registry_path)
    if reg is None and registry_path.exists():
        print(
            f"REFUSED: wiki registry at {registry_path} is unreadable; repair or "
            "restore it before setup",
            file=sys.stderr,
        )
        return 1
    reg = reg or {"wikis": {}, "default_wiki": None}
    wikis: dict = dict(reg.get("wikis") or {})
    configured = bool(wikis)
    default = reg.get("default_wiki") or (
        next(iter(wikis)) if len(wikis) == 1 else None
    )
    if args.json:
        print(
            json.dumps(
                {
                    "configured": configured,
                    "wikis": wikis,
                    "default_wiki": default,
                    "needs_choice": len(wikis) > 1 and not default,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
        return 0
    print("LegalQuants · CODEX for Legal — /wiki")
    if not configured:
        print(
            "\nWhere should your wiki live? Choose an existing wiki folder or a new "
            "folder you own. Optionally give it a short name. Then run:\n"
            "  init --wiki <dir> [--name <name>]\n\n"
            "Its name and path are saved in ~/.wiki/wikis.json, so a new chat "
            "finds it without asking again."
        )
        return 0
    print("\nWikis:")
    for name, entry in wikis.items():
        mark = " (default)" if name == default else ""
        missing = "" if Path(entry["path"]).is_dir() else " [MISSING]"
        print(f"  wiki {name!r} → {entry['path']}{mark}{missing}")
    if default and default in wikis and Path(wikis[default]["path"]).is_dir():
        print(f"  open: {Path(wikis[default]['path']) / 'index.md'}")
    elif default and default in wikis:
        print(
            f"  reconnect {default!r}: move or restore its folder, then run "
            f"init --wiki <moved-path> --name {default}"
        )
    elif len(wikis) > 1:
        print("  choose one: wiki-use <name>")
    return 0


def cmd_wiki_list(args: argparse.Namespace) -> int:
    rows: list[dict] = []
    seen: set[tuple[str, str]] = set()
    user_registry = _load_registry_if_readable(user_registry_path())
    sources = [("user", user_registry)] if user_registry else []
    for label, reg in sources:
        default = reg.get("default_wiki")
        for name, entry in (reg.get("wikis") or {}).items():
            key = (name, entry["path"])
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "name": name,
                    "path": entry["path"],
                    "default": name == default,
                    "source": label,
                    "exists": Path(entry["path"]).is_dir(),
                    "wiki_id": entry.get("wiki_id"),
                }
            )
    if args.json:
        print(json.dumps({"wikis": rows}, indent=2, ensure_ascii=False))
        return 0
    if not rows:
        print("no wikis registered — run: wiki.py init --wiki <dir>")
        return 0
    for row in rows:
        marks = (" (default)" if row["default"] else "") + (
            "" if row["exists"] else " [MISSING]"
        )
        print(f"{row['name']} → {row['path']}{marks} [{row['source']}]")
    return 0


def cmd_wiki_use(args: argparse.Namespace) -> int:
    up = user_registry_path()
    changed = []
    if up.exists():
        reg = _load_registry_if_readable(up)
        if reg is not None and args.name in (reg.get("wikis") or {}):
            reg["default_wiki"] = args.name
            atomic_write_text(up, json.dumps(reg, indent=1, ensure_ascii=False) + "\n")
            changed.append(str(up))
    if not changed:
        print(f"Error: no wiki named {args.name!r} is registered", file=sys.stderr)
        return 1
    print(f"default wiki is now {args.name!r} ({', '.join(changed)})")
    return 0


def cmd_land(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    dest = args.dest.replace(os.sep, "/")
    try:
        dest, target = safe_note_path(wiki, dest)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    try:
        draft = Path(args.file).read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Error: cannot read draft: {exc}", file=sys.stderr)
        return 2
    gate_error = _load_gate_report(args.gate_report, dest, draft)
    if gate_error:
        print(f"REFUSED: {gate_error}", file=sys.stderr)
        return 1
    try:
        fm, body = split_document(draft)
    except FrontmatterError as exc:
        print(f"Error: draft frontmatter: {exc}", file=sys.stderr)
        return 2
    if fm is None:
        print("Error: draft has no frontmatter", file=sys.stderr)
        return 2
    if args.dry_run:
        word = "update" if target.exists() else "create"
        print(f"dry-run: would {word} {dest} (origin {args.origin}, {args.mode})")
        return 0
    try:
        with WikiLock(wiki):
            word, record = _land_note(
                wiki,
                dest,
                fm,
                body,
                args.origin,
                args.mode,
                args.actor,
                replace=args.replace,
            )
            if record is not None:
                _regenerate(wiki)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    if record is None:
        print(f"unchanged: {dest} — placed 0 new")
        return 0
    print(f"{word} {dest} ({args.origin}, {args.mode}) · seq {record['seq']}")
    return 0


def _land_note(
    wiki: Path,
    dest: str,
    fm: dict,
    body: str,
    origin: str,
    mode: str,
    actor: str,
    replace: bool,
) -> tuple[str, dict | None]:
    """The one landing path (caller holds the lock). Refuses via WikiError."""
    fm["origin"] = origin
    title = str(fm.get("title", "") or "")
    if _looks_like_matter_reference(dest) or any(
        term in title.casefold() for term in MATTER_DOCUMENT_TERMS
    ):
        raise WikiError("note destination or title looks matter-specific")
    _prepare_and_validate_sources(fm)
    _validate_source_ids(wiki, dest, fm)
    dest, target = safe_note_path(wiki, dest)
    exists = target.exists()
    if mode == "markup" and not exists:
        fm["status"] = "draft"
        fm["pending"] = True
    _enforce_grounding(fm)
    normalized = emit_document(fm, body)
    findings = note_findings(dest, normalized)
    if not findings.ok:
        raise WikiError("; ".join(findings.conformance + findings.profile))
    vocab = load_vocab(wiki)
    touched = False
    for key in VOCAB_KEYS:
        value = fm.get(key)
        if isinstance(value, str) and value.strip():
            fm[key] = vocab_snap(wiki, vocab, key, value)
            touched = True
    normalized = emit_document(fm, body)
    if exists and not replace:
        raise WikiError(f"{dest} exists; pass --replace to update it")
    prior_sha = None
    if exists:
        prior_text = target.read_text(encoding="utf-8")
        prior_sha = text_sha256(prior_text)
        if prior_text == normalized:
            return "unchanged", None
    version_file = snapshot_note(wiki, dest)
    target.parent.mkdir(parents=True, exist_ok=True)
    atomic_write_text(target, normalized)
    record = append_history(
        wiki,
        "update_note" if exists else "create_note",
        dest,
        actor,
        origin=origin,
        mode=mode,
        content_sha256=text_sha256(normalized),
        prior_content_sha256=prior_sha,
        extra={"version_file": version_file} if version_file else None,
    )
    if touched:
        save_vocab(wiki, vocab)
    return ("updated" if exists else "landed"), record


MATTER_PATH_SEGMENTS = {
    "matter",
    "matters",
    "client",
    "clients",
    "case-files",
    "casefiles",
    "deals",
}
MATTER_DOCUMENT_TERMS = (
    "statement of claim",
    "statement of defence",
    "statement of defense",
    "pleading",
    "client correspondence",
    "witness statement",
)
ASSERTION_TYPES = ("Legal Insight", "Trap", "Position")


def _looks_like_matter_reference(resource: str, title: str = "") -> bool:
    decoded = unquote(f"{resource} {title}")
    folded = decoded.casefold()
    path_parts = {
        part.casefold() for part in re.split(r"[/\\?#]+", unquote(resource)) if part
    }
    identifier_like = bool(re.search(r"\b[A-Z][A-Z0-9]{1,20}[-_/]\d{2,6}\b", decoded))
    return bool(
        path_parts & MATTER_PATH_SEGMENTS
        or any(term in folded for term in MATTER_DOCUMENT_TERMS)
        or identifier_like
    )


def _source_identity(source: dict) -> tuple[str, str, str, str]:
    return (
        str(source.get("kind", "") or "").strip(),
        str(source.get("resource", "") or "").strip(),
        str(source.get("title", "") or "").strip(),
        str(source.get("sha256", "") or "").strip(),
    )


def _validate_source_ids(wiki: Path, dest: str, fm: dict) -> None:
    known: dict[str, tuple[str, str, str, str]] = {}
    for rel in wiki_notes(wiki):
        if rel == dest:
            continue
        try:
            other, _body = split_document((wiki / rel).read_text(encoding="utf-8"))
        except (OSError, FrontmatterError):
            continue
        for source in (other or {}).get("sources", []) or []:
            if isinstance(source, dict) and source.get("id"):
                known[str(source["id"])] = _source_identity(source)
    for source in fm.get("sources", []) or []:
        source_id = str(source.get("id", "") or "").strip()
        if not source_id:
            continue
        existing = known.get(source_id)
        if existing is not None and existing != _source_identity(source):
            raise WikiError(
                f"source id {source_id!r} conflicts with an existing source record"
            )


def _enforce_grounding(fm: dict) -> None:
    note_type = str(fm.get("type", "") or "")
    if note_type not in ASSERTION_TYPES or fm.get("sources"):
        return
    pending = str(fm.get("pending", "")).strip().casefold() == "true"
    if str(fm.get("status", "") or "stable") != "draft" or not pending:
        raise WikiError(
            f"{note_type} without sources must remain a pending draft; "
            "it cannot land as reusable authority"
        )


def _prepare_and_validate_sources(fm: dict) -> None:
    """Classify explicit sources and refuse obvious matter-document resolvers."""
    sources = fm.get("sources", []) or []
    if not isinstance(sources, list):
        raise WikiError("sources must be a list")
    for index, source in enumerate(sources, 1):
        if not isinstance(source, dict):
            raise WikiError(f"source {index} must be a record")
        resource = str(source.get("resource", "") or "").strip()
        title = str(source.get("title", "") or "").strip()
        if not resource:
            continue
        if resource.startswith(("http://", "https://")):
            parsed = urlsplit(resource)
            if not parsed.netloc:
                raise WikiError(f"public source {index} is not a valid absolute URL")
            if _looks_like_matter_reference(resource, title):
                raise WikiError(
                    f"source {index} looks like a matter document; its URL and "
                    "title cannot be persisted in the wiki"
                )
            source.setdefault("kind", "public")
            if source.get("kind") != "public":
                raise WikiError(f"URL source {index} kind must be public")
            continue
        local = Path(resource).expanduser()
        if source.get("kind") != "authorised-local":
            raise WikiError(
                f"local source {index} requires explicit kind: authorised-local"
            )
        if path_has_symlink_component(local):
            raise WikiError(f"local source {index} may not use a symbolic-link path")
        if not local.is_file():
            raise WikiError(f"local source {index} is unavailable at {local}")
        resolved = local.resolve(strict=True)
        if _looks_like_matter_reference(f"{resource} {resolved}", title):
            raise WikiError(
                f"source {index} looks like a matter document; its path and title "
                "cannot be persisted in the wiki"
            )
        digest = hashlib.sha256()
        with resolved.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        actual_sha = digest.hexdigest()
        if source.get("sha256") and source.get("sha256") != actual_sha:
            raise WikiError(f"local source {index} changed since its recorded hash")
        source["sha256"] = actual_sha
        source.setdefault("last_checked", date.today().isoformat())


def cmd_rename(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    try:
        src, src_path = safe_note_path(wiki, args.src, must_exist=True)
        dst, dst_path = safe_note_path(wiki, args.dest)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    if dst_path.exists():
        print(f"Error: {dst} already exists", file=sys.stderr)
        return 1
    if args.dry_run:
        print(f"dry-run: would rename {src} → {dst}")
        return 0
    with WikiLock(wiki):
        version_file = snapshot_note(wiki, src)
        text = src_path.read_text(encoding="utf-8")
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_text(dst_path, text)
        src_path.unlink()
        record = append_history(
            wiki,
            "rename_note",
            src,
            args.actor,
            content_sha256=text_sha256(text),
            extra={"to": dst, "version_file": version_file},
        )
        _regenerate(wiki)
    inbound = 0
    for rel in wiki_notes(wiki):
        if rel != dst and Path(src).name in (wiki / rel).read_text(encoding="utf-8"):
            inbound += 1
    print(f"renamed {src} → {dst} · seq {record['seq']}")
    if inbound:
        print(f"note: {inbound} note(s) may still link to the old name")
    return 0


def cmd_delete(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    try:
        rel, target = safe_note_path(wiki, args.note, must_exist=True)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    if args.dry_run:
        print(f"dry-run: would tombstone {rel} (recoverable from versions)")
        return 0
    with WikiLock(wiki):
        text = target.read_text(encoding="utf-8")
        version_file = snapshot_note(wiki, rel)
        target.unlink()
        record = append_history(
            wiki,
            "delete_note",
            rel,
            args.actor,
            prior_content_sha256=text_sha256(text),
            extra={"version_file": version_file},
        )
        _regenerate(wiki)
    print(f"tombstoned {rel} · seq {record['seq']} · recoverable from versions")
    return 0


def cmd_purge(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    try:
        rel, target = safe_note_path(wiki, args.note, must_exist=True)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    guard = _reason_guard(args.reason)
    if guard:
        print(f"REFUSED: {guard}", file=sys.stderr)
        return 1
    if not args.yes:
        print(
            "REFUSED: purge destroys content AND versions; re-run with --yes",
            file=sys.stderr,
        )
        return 1
    with WikiLock(wiki):
        prior_sha = None
        if target.exists():
            prior_sha = text_sha256(target.read_text(encoding="utf-8"))
            target.unlink()
        vdir = sidecar(wiki) / "versions" / note_dirname(rel)
        removed_versions = 0
        if vdir.is_dir():
            for mdv in vdir.iterdir():
                mdv.unlink()
                removed_versions += 1
            vdir.rmdir()
        record = append_history(
            wiki,
            "purge_note",
            rel,
            args.actor,
            prior_content_sha256=prior_sha,
            extra={"reason": args.reason},
        )
        _regenerate(wiki)
    print(
        f"purged {rel} · seq {record['seq']} · {removed_versions} version(s) destroyed"
    )
    return 0


def cmd_merge(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    try:
        into, into_path = safe_note_path(wiki, args.into, must_exist=True)
        from_pairs = [
            safe_note_path(wiki, rel, must_exist=True) for rel in args.from_notes
        ]
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    froms = [rel for rel, _path in from_pairs]
    try:
        merged_draft = Path(args.file).read_text(encoding="utf-8")
        fm, body = split_document(merged_draft)
    except (OSError, FrontmatterError) as exc:
        print(f"Error: merged draft: {exc}", file=sys.stderr)
        return 2
    gate_error = _load_gate_report(args.gate_report, into, merged_draft)
    if gate_error:
        print(f"REFUSED: {gate_error}", file=sys.stderr)
        return 1
    if fm is None:
        print("Error: merged draft has no frontmatter", file=sys.stderr)
        return 2
    fm["merged_from"] = sorted(froms)
    try:
        _prepare_and_validate_sources(fm)
        _validate_source_ids(wiki, into, fm)
        _enforce_grounding(fm)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    normalized = emit_document(fm, body)
    findings = note_findings(into, normalized)
    if not findings.ok:
        for f in findings.conformance + findings.profile:
            print(f"REFUSED: {f}", file=sys.stderr)
        return 1
    with WikiLock(wiki):
        prior_sha = text_sha256(into_path.read_text(encoding="utf-8"))
        version_file = snapshot_note(wiki, into)
        from_versions = []
        for rel, from_path in from_pairs:
            from_versions.append(snapshot_note(wiki, rel))
            from_path.unlink()
        atomic_write_text(into_path, normalized)
        record = append_history(
            wiki,
            "merge_notes",
            into,
            args.actor,
            origin=str(fm.get("origin") or "") or None,
            content_sha256=text_sha256(normalized),
            prior_content_sha256=prior_sha,
            extra={
                "merged_from": sorted(froms),
                "version_file": version_file,
                "from_versions": from_versions,
            },
        )
        _regenerate(wiki)
    print(f"merged {', '.join(froms)} into {into} · seq {record['seq']}")
    return 0


def _stamp_verified(fm: dict, by: str) -> None:
    entries = normalize_verified(fm.get("verified"))
    entries.append({"by": by, "at": utc_now_iso()})
    fm["verified"] = entries[0] if len(entries) == 1 else entries


def cmd_accept(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    try:
        rel, target = safe_note_path(wiki, args.note, must_exist=True)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    if not args.by.startswith("human:"):
        print(
            "Error: --by must be a human:<id> actor (a human accepts)", file=sys.stderr
        )
        return 2
    try:
        fm, body = split_document(target.read_text(encoding="utf-8"))
    except (OSError, FrontmatterError) as exc:
        print(f"Error: {rel}: {exc}", file=sys.stderr)
        return 2
    if not fm or str(fm.get("pending", "")).strip().lower() != "true":
        print(f"Error: {rel} carries no pending suggestion", file=sys.stderr)
        return 1
    fm.pop("pending", None)
    if str(fm.get("status", "")) == "draft":
        fm["status"] = "stable"
    try:
        _enforce_grounding(fm)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    _stamp_verified(fm, args.by)
    normalized = emit_document(fm, body)
    with WikiLock(wiki):
        version_file = snapshot_note(wiki, rel)
        prior_sha = text_sha256(target.read_text(encoding="utf-8"))
        atomic_write_text(target, normalized)
        record = append_history(
            wiki,
            "accept_suggestion",
            rel,
            args.by,
            origin=str(fm.get("origin") or "") or None,
            content_sha256=text_sha256(normalized),
            prior_content_sha256=prior_sha,
            extra={"version_file": version_file},
        )
        _regenerate(wiki)
    print(f"accepted {rel} · now human-reviewed · seq {record['seq']}")
    return 0


def cmd_decline(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    try:
        rel, target = safe_note_path(wiki, args.note, must_exist=True)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    try:
        fm, _body = split_document(target.read_text(encoding="utf-8"))
    except (OSError, FrontmatterError) as exc:
        print(f"Error: {rel}: {exc}", file=sys.stderr)
        return 2
    if not fm or str(fm.get("pending", "")).strip().lower() != "true":
        print(f"Error: {rel} carries no pending suggestion", file=sys.stderr)
        return 1
    with WikiLock(wiki):
        prior_sha = text_sha256(target.read_text(encoding="utf-8"))
        version_file = snapshot_note(wiki, rel)
        target.unlink()
        record = append_history(
            wiki,
            "decline_suggestion",
            rel,
            args.actor,
            prior_content_sha256=prior_sha,
            extra={"version_file": version_file},
        )
        _regenerate(wiki)
    print(f"declined {rel} · seq {record['seq']} · recoverable from versions")
    return 0


def cmd_verify_note(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    try:
        rel, target = safe_note_path(wiki, args.note, must_exist=True)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    if not args.by.startswith("human:"):
        print("Error: --by must be a human:<id> actor", file=sys.stderr)
        return 2
    try:
        fm, body = split_document(target.read_text(encoding="utf-8"))
    except (OSError, FrontmatterError) as exc:
        print(f"Error: {rel}: {exc}", file=sys.stderr)
        return 2
    if fm is None:
        print(f"Error: {rel} has no frontmatter", file=sys.stderr)
        return 2
    try:
        _enforce_grounding(fm)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    _stamp_verified(fm, args.by)
    normalized = emit_document(fm, body)
    with WikiLock(wiki):
        version_file = snapshot_note(wiki, rel)
        prior_sha = text_sha256(target.read_text(encoding="utf-8"))
        atomic_write_text(target, normalized)
        record = append_history(
            wiki,
            "update_note",
            rel,
            args.by,
            origin=str(fm.get("origin") or "") or None,
            content_sha256=text_sha256(normalized),
            prior_content_sha256=prior_sha,
            extra={"version_file": version_file},
        )
        _regenerate(wiki)
    print(f"verified {rel} · now human-reviewed · seq {record['seq']}")
    return 0


def _browser_payload(
    wiki: Path, *, selected_note: str | None = None, topic: str | None = None
) -> dict:
    """Return display-safe, full-content knowledge for a reader view."""
    wanted_note = None
    if selected_note:
        wanted_note, _target = safe_note_path(wiki, selected_note, must_exist=True)
    topic_folded = topic.casefold().strip() if topic else ""
    notes: list[dict] = []
    for rel in wiki_notes(wiki):
        if wanted_note and rel != wanted_note:
            continue
        try:
            fm, body = split_document((wiki / rel).read_text(encoding="utf-8"))
        except (OSError, FrontmatterError):
            continue
        if not fm:
            continue
        note_type = str(fm.get("type", "") or "")
        status = str(fm.get("status", "") or "stable")
        pending = str(fm.get("pending", "")).strip().casefold() == "true"
        if note_type == "Position" or pending or status == "deprecated":
            continue
        tags = [str(tag) for tag in fm.get("tags", []) or []]
        topic_fields = (
            rel,
            str(fm.get("title", "") or ""),
            str(fm.get("practice_area", "") or ""),
            str(fm.get("jurisdiction", "") or ""),
            note_type,
            " ".join(tags),
        )
        if topic_folded and topic_folded not in " ".join(topic_fields).casefold():
            continue
        sources = []
        for source in fm.get("sources", []) or []:
            if not isinstance(source, dict):
                continue
            display_source = {
                key: str(source.get(key, "") or "").strip()
                for key in ("id", "title", "resource", "pinpoint")
                if source.get(key)
            }
            if display_source:
                sources.append(display_source)
        related = []
        for target in re.findall(r"\]\(([^)]+)\)", body):
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if (
                not clean.endswith(".md")
                or Path(clean).is_absolute()
                or urlsplit(clean).scheme
            ):
                continue
            resolved = (Path(rel).parent / clean).as_posix()
            related.append(Path(os.path.normpath(resolved)).as_posix())
        notices = []
        if status in ("disputed", "outdated"):
            notices.append(status)
        if is_stale(fm.get("stale_after")):
            notices.append("stale")
        if trust_tier(fm) != "human-reviewed":
            notices.append("unverified")
        notes.append(
            {
                "id": rel,
                "title": str(fm.get("title", "") or rel),
                "type": note_type,
                "topic": str(fm.get("practice_area", "") or ""),
                "jurisdiction": str(fm.get("jurisdiction", "") or ""),
                "body": body.strip(),
                "sources": sources,
                "related": sorted(set(related)),
                "notices": notices,
            }
        )
    notes.sort(key=lambda note: (note["topic"].casefold(), note["title"].casefold()))
    included = {note["id"] for note in notes}
    for note in notes:
        note["related"] = [rel for rel in note["related"] if rel in included]
    manifest = load_manifest(wiki, required=False) or {}
    return {
        "schema": 1,
        "title": str(manifest.get("name", "") or "Legal wiki"),
        "scope": {"note": wanted_note, "topic": topic or None},
        "coverage": {
            "scope": "selected" if wanted_note or topic else "all-eligible",
            "note_count": len(notes),
            "note_ids": [note["id"] for note in notes],
        },
        "notes": notes,
    }


def cmd_browse(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    try:
        payload = _browser_payload(
            wiki,
            selected_note=getattr(args, "note", None),
            topic=getattr(args, "topic", None),
        )
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0
    notes = payload["notes"]
    if not notes:
        print("No reusable knowledge found in this browse scope.")
        return 0
    print(f"# {markdown_text(payload['title'])}")
    for note in notes:
        print(f"\n## {markdown_text(note['title'])}\n")
        if note["notices"]:
            warning = ", ".join(str(value) for value in note["notices"])
            print(f"**Check before relying:** {markdown_text(warning)}\n")
        print(note["body"] or "_No note body._")
        if note["sources"]:
            print("\n### Sources\n")
            for source in note["sources"]:
                label = source.get("title") or source.get("id") or "Source"
                resource = source.get("resource")
                rendered = (
                    markdown_link(label, resource) if resource else markdown_text(label)
                )
                pinpoint = source.get("pinpoint")
                suffix = f" — {markdown_text(pinpoint)}" if pinpoint else ""
                print(f"- {rendered}{suffix}")
    return 0


def _ask_tokens(text: str) -> set[str]:
    return {
        token[:-1] if token.endswith("s") and len(token) > 3 else token
        for token in re.findall(r"[a-z0-9][a-z0-9-]{2,}", text.casefold())
    }


def cmd_ask(args: argparse.Namespace) -> int:
    """Manual, read-only deterministic search. The model writes the answer."""
    wiki = _wiki_arg(args)
    if args.limit <= 0:
        print("Error: --limit must be a positive integer", file=sys.stderr)
        return 2
    query = _ask_tokens(args.query)
    matches: list[tuple[float, dict]] = []
    for rel in wiki_notes(wiki):
        try:
            fm, body = split_document((wiki / rel).read_text(encoding="utf-8"))
        except (OSError, FrontmatterError):
            continue
        if not fm or str(fm.get("pending", "")).casefold() == "true":
            continue
        status = str(fm.get("status", "") or "stable")
        if status == "deprecated":
            continue
        title = str(fm.get("title", "") or rel)
        tags = [str(v) for v in fm.get("tags", []) or []]
        source_text = " ".join(
            " ".join(
                str(source.get(key, "") or "") for key in ("id", "title", "resource")
            )
            for source in (fm.get("sources", []) or [])
            if isinstance(source, dict)
        )
        haystack = " ".join(
            [
                title,
                str(fm.get("description", "") or ""),
                str(fm.get("trigger", "") or ""),
                " ".join(tags),
                source_text,
                body,
            ]
        )
        tokens = _ask_tokens(haystack)
        if not query or not tokens:
            score = 0.0
        else:
            overlap = query & tokens
            score = len(overlap) / len(query)
            if query & _ask_tokens(title):
                score += 0.5
            if query & _ask_tokens(" ".join(tags)):
                score += 0.25
            if query & _ask_tokens(source_text):
                score += 0.25
        if score <= 0:
            continue
        sources = []
        for source in fm.get("sources", []) or []:
            if isinstance(source, dict):
                sources.append(
                    {
                        "id": source.get("id"),
                        "title": source.get("title"),
                        "resource": source.get("resource"),
                    }
                )
        matches.append(
            (
                score,
                {
                    "path": rel,
                    "title": title,
                    "type": str(fm.get("type", "")),
                    "status": status,
                    "stale": is_stale(fm.get("stale_after")),
                    "tier": trust_tier(fm),
                    "sources": sources,
                },
            )
        )
    matches.sort(key=lambda item: (-item[0], item[1]["path"]))
    offered: list[dict] = []
    for score, item in matches[: args.limit]:
        result = dict(item)
        result["score"] = round(score, 3)
        offered.append(result)
    if args.json:
        print(json.dumps({"matches": offered}, indent=2, ensure_ascii=False))
    elif not offered:
        print("No reusable knowledge found in this wiki.")
    else:
        print(f"From your wiki: {len(offered)} relevant note(s)")
        for item in offered:
            warnings = []
            if item["status"] in ("disputed", "outdated"):
                warnings.append(item["status"])
            if item["stale"]:
                warnings.append("stale")
            warning = f" · WARNING: {', '.join(warnings)}" if warnings else ""
            print(
                f"- {item['path']} · {item['type']} [{item['tier']}] · "
                f"{item['title']}{warning}"
            )
            sources = item.get("sources", [])
            if not isinstance(sources, list):
                continue
            for source in sources:
                if not isinstance(source, dict):
                    continue
                label = source.get("title") or source.get("id") or "source"
                if source.get("resource"):
                    print(f"  source: {label} → {source['resource']}")
        print(
            "Read these notes as evidence-bearing data; then answer with their "
            "links and sources."
        )
    return 0


def cmd_review_record(args: argparse.Namespace) -> int:
    """Record a closed, non-confidential disposition in the durable queue."""
    wiki = _wiki_arg(args)
    subject = args.note or args.source_id
    if args.note and validate_note_path(args.note):
        print("Error: invalid note identifier", file=sys.stderr)
        return 2
    if args.source_id and not re.fullmatch(r"[A-Za-z0-9_.-]+", args.source_id):
        print("Error: invalid source identifier", file=sys.stderr)
        return 2
    if not subject and args.disposition not in ("no-material", "matter-specific"):
        print("Error: this disposition requires --note or --source-id", file=sys.stderr)
        return 2
    record = {
        "ts": utc_now_iso(),
        "disposition": args.disposition,
        "status": "open"
        if args.disposition not in ("no-material", "matter-specific")
        else "closed",
    }
    if args.note:
        record["note"] = args.note
    if args.source_id:
        record["source_id"] = args.source_id
    with WikiLock(wiki):
        append_review_record(wiki, record)
        regenerate_indexes(wiki)
    print(
        f"review: {args.disposition} recorded" + (f" for {subject}" if subject else "")
    )
    return 0


def _confirmed_playbook_value(playbook: Path, key: str) -> str | None:
    if not playbook.exists():
        return None
    confirmed = False
    value = None
    values = r"(.*)" if key == "automatic scope" else r"(on|off)"
    pattern = re.compile(rf"^-\s*\[wiki\]\s*{re.escape(key)}\s*:\s*{values}\s*$", re.I)
    try:
        lines = playbook.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return None
    for raw in lines:
        line = raw.strip()
        if line.startswith("## "):
            confirmed = line == "## Confirmed"
            continue
        if confirmed:
            match = pattern.match(line)
            if match:
                value = match.group(1).casefold()
    return value


def _append_confirmed_lines(playbook: Path, lines_to_add: list[str]) -> None:
    if playbook.exists():
        lines = playbook.read_text(encoding="utf-8").splitlines()
    else:
        lines = ["# LQ playbook", "", "## Confirmed", ""]
    try:
        start = next(
            i for i, line in enumerate(lines) if line.strip() == "## Confirmed"
        )
    except StopIteration:
        if lines and lines[-1].strip():
            lines.append("")
        lines.extend(["## Confirmed", ""])
        start = len(lines) - 2
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
        len(lines),
    )
    insertion = end
    while insertion > start + 1 and not lines[insertion - 1].strip():
        insertion -= 1
    lines[insertion:insertion] = lines_to_add + [""]
    atomic_write_text(playbook, "\n".join(lines).rstrip() + "\n")


def automation_scope() -> tuple[str, list[str]]:
    """Only a confirmed scope selects immutable operational project metadata.

    Missing scope preserves previously enabled global settings. New enablement
    must choose a scope. Project paths never enter the playbook or the wiki.
    """
    selection = _confirmed_playbook_value(user_playbook_path(), "automatic scope")
    if selection is None or selection == "all":
        return "all", []
    if not re.fullmatch(r"projects:[a-f0-9]{64}", selection):
        return "unavailable", []
    digest = selection.partition(":")[2]
    path = user_registry_path().parent / "automation-scopes" / f"{digest}.json"
    try:
        policy = json.loads(path.read_text(encoding="utf-8"))
        roots = policy["roots"]
        if (
            canonical_json_digest(policy) != digest
            or policy.get("schema") != 1
            or not isinstance(roots, list)
            or any(
                not isinstance(root, str) or not Path(root).is_absolute()
                for root in roots
            )
        ):
            return "unavailable", []
        return "projects", roots
    except (OSError, ValueError, KeyError, TypeError):
        return "unavailable", []


def automation_scope_allows(cwd: object) -> bool:
    scope, roots = automation_scope()
    if scope == "all":
        return True
    if scope != "projects" or not isinstance(cwd, str) or not cwd:
        return False
    try:
        current = Path(cwd)
        if not current.is_absolute() or not current.is_dir():
            return False
        current = current.resolve(strict=True)
        for root in roots:
            saved = Path(root)
            # A root moved or redirected by a symlink needs selecting again.
            if saved.is_dir() and saved.resolve(strict=True) == saved:
                if current.is_relative_to(saved):
                    return True
    except (OSError, ValueError, RuntimeError):
        return False
    return False


def cmd_automation(args: argparse.Namespace) -> int:
    """Preview and confirm automatic retrieval within an explicit scope."""
    _wiki_arg(args)
    playbook = user_playbook_path()
    current_retrieval = (
        _confirmed_playbook_value(playbook, "automatic retrieval") or "off"
    )
    if args.intake == "on":
        raise WikiError(
            "automatic intake is unavailable; ask Wiki to save the reusable "
            "lessons from this conversation"
        )
    scope, roots = automation_scope()
    requested = []
    policy = None
    scope_choice = getattr(args, "scope", None)
    additions = getattr(args, "project", None) or []
    removals = getattr(args, "remove_project", None) or []
    if scope_choice == "all" and (additions or removals):
        raise WikiError("choose All projects or selected project folders")
    if scope_choice == "projects" or additions or removals:
        if scope != "projects":
            roots = []
        for value in additions:
            root = Path(value).expanduser().resolve()
            if not root.is_dir():
                raise WikiError("select an existing project folder")
            roots.append(str(root))
        removed = {str(Path(value).expanduser().resolve()) for value in removals}
        roots = sorted(set(roots) - removed)
        if not roots and (
            not removals or (args.retrieval or current_retrieval) != "off"
        ):
            raise WikiError("select at least one project, or turn retrieval off")
        policy = {"schema": 1, "roots": roots}
        scope = "projects"
        requested.append(
            f"- [wiki] automatic scope: projects:{canonical_json_digest(policy)}"
        )
    elif scope_choice == "all":
        scope, roots = "all", []
        requested.append("- [wiki] automatic scope: all")
    # Preserve a cleanup path for installations that previously saved this
    # setting. The current hook overlay never reads it.
    if args.intake == "off":
        requested.append("- [wiki] automatic intake: off")
    if args.retrieval:
        requested.append(f"- [wiki] automatic retrieval: {args.retrieval}")
    enabling = args.retrieval == "on"
    if enabling and not scope_choice and not additions and not removals:
        if _confirmed_playbook_value(playbook, "automatic scope") is None:
            raise WikiError("choose Selected projects or All projects with --scope")
    if enabling and (scope == "unavailable" or (scope == "projects" and not roots)):
        raise WikiError("select the project folders again to enable automation")
    label = (
        "All projects"
        if scope == "all"
        else "Selected projects"
        if scope == "projects"
        else "Select project folders again"
    )
    print(f"Wiki automation · {label}")
    for root in roots:
        print(f"  {root} (including subfolders)")
    print(f"Bring in relevant notes: {args.retrieval or current_retrieval}")
    print("Save new knowledge: on request · Manual Add/Ask/Browse/Check available.")
    if not requested:
        return 0
    if not args.yes:
        print(
            "Preview only. Confirm this scope and retrieval setting to save the change."
        )
        # Exact preference lines are reviewable without storing project paths here.
        for line in requested:
            print(line)
        return 0
    if policy is not None:
        path = (
            user_registry_path().parent
            / "automation-scopes"
            / f"{canonical_json_digest(policy)}.json"
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_text(path, json.dumps(policy, indent=2) + "\n")
    _append_confirmed_lines(playbook, requested)
    print("Wiki automation settings saved.")
    return 0


def cmd_export_map(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    nodes = []
    for rel in wiki_notes(wiki):
        try:
            fm, body = split_document((wiki / rel).read_text(encoding="utf-8"))
        except FrontmatterError:
            continue
        if not fm:
            continue
        note_type = str(fm.get("type", ""))
        if note_type == "Position" and not args.include_positions:
            continue  # Positions stay local; they never leave the machine
        links = []
        for target in re.findall(r"\]\(([^)]+\.md)\)", body):
            resolved = (Path(rel).parent / target).as_posix()
            links.append(str(Path(os.path.normpath(resolved)).as_posix()))
        nodes.append(
            {
                "id": rel,
                "title": str(fm.get("title", "") or rel),
                "type": note_type,
                "tier": trust_tier(fm),
                "status": str(fm.get("status", "") or "stable"),
                "pending": str(fm.get("pending", "")).strip().lower() == "true",
                "stale": is_stale(fm.get("stale_after")),
                "tags": [str(t) for t in fm.get("tags", []) or []],
                "practice_area": str(fm.get("practice_area", "") or ""),
                "document_kind": str(fm.get("document_kind", "") or ""),
                "links": sorted(links),
                "sources": [
                    {
                        "id": source.get("id"),
                        "title": source.get("title"),
                        "resource": source.get("resource"),
                    }
                    for source in (fm.get("sources", []) or [])
                    if isinstance(source, dict)
                ],
            }
        )
    review = read_review_records(wiki)
    payload = {
        "schema": 2,
        "wiki": load_manifest(wiki, required=False),
        "summary": {
            "notes": len(nodes),
            "pending": sum(1 for n in nodes if n["pending"]),
            "stale": sum(1 for n in nodes if n["stale"]),
            "disputed": sum(1 for n in nodes if n["status"] == "disputed"),
            "open_review": sum(1 for r in review if r.get("status") == "open"),
        },
        "nodes": nodes,
    }
    output = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.out:
        atomic_write_text(Path(args.out), output + "\n")
        print(f"export-map: {len(nodes)} node(s) → {args.out}")
    else:
        print(output)
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    records = read_history(wiki)
    broken = verify_chain(records)
    state = replay_note_state(records)
    drift: list[str] = []
    on_disk = set(wiki_notes(wiki))
    for note, sha in state.items():
        if note not in on_disk:
            drift.append(f"{note}: recorded in history but missing on disk")
        elif text_sha256((wiki / note).read_text(encoding="utf-8")) != sha:
            drift.append(f"{note}: changed on disk since last recorded state")
    for note in sorted(on_disk - set(state)):
        drift.append(f"{note}: on disk but never recorded in history")
    if args.json:
        print(
            json.dumps(
                {
                    "ok": not broken and not drift,
                    "broken_links": broken,
                    "drift": drift,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        for b in broken:
            print(f"BROKEN seq {b['seq']}: {b['reason']}")
        for d in drift:
            print(f"DRIFT {d}")
        verdict = "PASS" if not broken and not drift else "FAIL"
        print(
            f"verify: {len(records)} record(s), {len(broken)} broken link(s), "
            f"{len(drift)} drift note(s) — {verdict}"
        )
    return 0 if not broken and not drift else 1


def cmd_status(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    records = read_history(wiki)
    broken = verify_chain(records)
    if broken:
        print(
            "REFUSED: history chain is broken; repair it before rollback",
            file=sys.stderr,
        )
        return 1
    notes = wiki_notes(wiki)
    pending = deprecated = stale = disputed = outdated = 0
    for rel in notes:
        try:
            fm, _ = split_document((wiki / rel).read_text(encoding="utf-8"))
        except FrontmatterError:
            continue
        if not fm:
            continue
        if str(fm.get("pending", "")).strip().lower() == "true":
            pending += 1
        if str(fm.get("status", "")) == "deprecated":
            deprecated += 1
        if str(fm.get("status", "")) == "disputed":
            disputed += 1
        if str(fm.get("status", "")) == "outdated":
            outdated += 1
        if is_stale(fm.get("stale_after")):
            stale += 1
    declined = sum(1 for r in records if r.get("op") == "decline_suggestion")
    state = replay_note_state(records)
    drift = sum(
        1
        for note, sha in state.items()
        if (wiki / note).exists()
        and text_sha256((wiki / note).read_text(encoding="utf-8")) != sha
    )
    review = read_review_records(wiki)
    open_review = sum(1 for r in review if r.get("status") == "open")
    sources: set[str] = set()
    for rel in notes:
        try:
            fm, _ = split_document((wiki / rel).read_text(encoding="utf-8"))
        except FrontmatterError:
            continue
        if fm:
            for source in fm.get("sources", []) or []:
                if isinstance(source, dict):
                    source_id = source.get("id") or source.get("resource")
                    if source_id:
                        sources.add(str(source_id))
    print(
        f"notes {len(notes)} · pending {pending} · declined {declined} · "
        f"disputed {disputed} · outdated {outdated} · deprecated {deprecated} · "
        f"stale {stale} · sources {len(sources)} · review {open_review} open · "
        f"unreviewed disk changes {drift}"
    )
    return 0


def cmd_rollback(args: argparse.Namespace) -> int:
    wiki = _wiki_arg(args)
    if not args.yes:
        print(
            "REFUSED: rollback protection active — re-run with --yes to restore "
            f"the wiki to seq {args.to}",
            file=sys.stderr,
        )
        return 1
    records = read_history(wiki)
    seqs: list[int] = [
        seq for r in records if isinstance((seq := r.get("seq")), int) and seq > 0
    ]
    if not seqs or args.to < 0 or args.to > max(seqs):
        print(
            f"Error: --to {args.to} is outside the chain (1..{max(seqs or [0])})",
            file=sys.stderr,
        )
        return 2
    target_state = replay_note_state(records, upto_seq=args.to)
    try:
        safe_targets = {note: safe_note_path(wiki, note)[1] for note in target_state}
    except WikiError as exc:
        print(f"REFUSED: unsafe history path: {exc}", file=sys.stderr)
        return 1
    pool = _content_pool(wiki)
    restored, removed, unrecoverable = [], [], []
    with WikiLock(wiki):
        on_disk = set(wiki_notes(wiki))
        for note, sha in target_state.items():
            target = safe_targets[note]
            current = target if target.exists() else None
            if current and text_sha256(current.read_text(encoding="utf-8")) == sha:
                continue
            text = pool.get(sha)
            if text is None:
                unrecoverable.append(note)
                continue
            snapshot_note(wiki, note)
            target.parent.mkdir(parents=True, exist_ok=True)
            atomic_write_text(target, text)
            restored.append(note)
        for note in sorted(on_disk - set(target_state)):
            _rel, target = safe_note_path(wiki, note, must_exist=True)
            snapshot_note(wiki, note)
            target.unlink()
            removed.append(note)
        append_history(wiki, "rollback", None, args.actor, extra={"to_seq": args.to})
        _regenerate(wiki)
    print(
        f"rolled back to seq {args.to}: {len(restored)} restored, "
        f"{len(removed)} removed, {len(unrecoverable)} unrecoverable"
    )
    for note in unrecoverable:
        print(f"cannot restore {note}: content was purged", file=sys.stderr)
    return 0 if not unrecoverable else 1


# ---------------------------------------------------------------------------
# Verbs
# ---------------------------------------------------------------------------


def cmd_check(args: argparse.Namespace) -> int:
    root = Path(args.path)
    if not root.is_dir():
        print(f"Error: {root} is not a directory", file=sys.stderr)
        return 2
    today = None
    if args.today:
        try:
            today = date.fromisoformat(args.today)
        except ValueError:
            print(f"Error: --today {args.today!r} is not YYYY-MM-DD", file=sys.stderr)
            return 2
    report = check_wiki(root, today)
    if args.json:
        print(json.dumps(report.as_dict(), indent=2, ensure_ascii=False))
    else:
        for finding in report.conformance:
            print(f"CONFORMANCE FAIL {finding}")
        for finding in report.profile:
            print(f"PROFILE FAIL {finding}")
        for finding in report.warnings:
            print(f"WARN {finding}")
        verdict = "PASS" if report.ok else "FAIL"
        print(
            f"check: {len(report.conformance)} conformance, "
            f"{len(report.profile)} profile, {len(report.warnings)} warnings "
            f"— {verdict}"
        )
    return 0 if report.ok else 1


def cmd_normalize(args: argparse.Namespace) -> int:
    path = Path(args.file)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Error: cannot read {path}: {exc}", file=sys.stderr)
        return 2
    try:
        fm, body = split_document(text)
    except FrontmatterError as exc:
        print(f"Error: {path}: {exc}", file=sys.stderr)
        return 2
    sys.stdout.write(emit_document(fm, body))
    return 0


def cmd_version(_args: argparse.Namespace) -> int:
    print(
        f"wiki engine {ENGINE_VERSION} · state schema {SCHEMA_VERSION} "
        f"· okf {OKF_VERSION}"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wiki.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="verb", required=True)

    p_check = sub.add_parser("check", help="validate a wiki directory")
    p_check.add_argument("path", help="wiki root directory")
    p_check.add_argument("--json", action="store_true", help="machine-readable report")
    p_check.add_argument("--today", help="override today (YYYY-MM-DD) for staleness")
    p_check.set_defaults(func=cmd_check)

    p_norm = sub.add_parser("normalize", help="print a note's canonical form")
    p_norm.add_argument("file", help="markdown note file")
    p_norm.set_defaults(func=cmd_normalize)

    p_ver = sub.add_parser("version", help="print engine and schema versions")
    p_ver.set_defaults(func=cmd_version)

    def wikied(name: str, help_text: str) -> argparse.ArgumentParser:
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--wiki", help="wiki root directory (wins over any registry)")
        p.add_argument("--wiki-name", help="pick a registered wiki by name")
        p.add_argument("--actor", default=DEFAULT_ACTOR, help="who is acting")
        return p

    p_init = sub.add_parser("init", help="initialise and register a wiki")
    p_init.add_argument("--wiki", required=True)
    p_init.add_argument("--name", default="main", help="registry name for this wiki")
    p_init.add_argument(
        "--no-user-registry",
        action="store_true",
        help="do not record this wiki in the user-level registry",
    )
    p_init.set_defaults(func=cmd_init)

    p_setup = sub.add_parser("setup", help="first-run welcome / current config")
    p_setup.add_argument("--json", action="store_true")
    p_setup.set_defaults(func=cmd_setup)

    p_vl = sub.add_parser("wiki-list", help="list registered wikis")
    p_vl.add_argument("--json", action="store_true")
    p_vl.set_defaults(func=cmd_wiki_list)

    p_vu = sub.add_parser("wiki-use", help="set the default wiki by name")
    p_vu.add_argument("name")
    p_vu.set_defaults(func=cmd_wiki_use)

    p_land = wikied("land", "land a gated note draft into the wiki")
    p_land.add_argument("--file", required=True, help="the draft note file")
    p_land.add_argument("--dest", required=True, help="wiki-relative destination")
    p_land.add_argument("--origin", required=True, choices=ORIGINS)
    p_land.add_argument("--mode", default="auto", choices=("auto", "markup"))
    p_land.add_argument("--gate-report", help="JSON verdict from the gate")
    p_land.add_argument(
        "--replace", action="store_true", help="update an existing note"
    )
    p_land.add_argument("--dry-run", action="store_true")
    p_land.set_defaults(func=cmd_land)

    p_rn = wikied("rename", "rename a note; history keeps everything")
    p_rn.add_argument("src")
    p_rn.add_argument("dest")
    p_rn.add_argument("--dry-run", action="store_true")
    p_rn.set_defaults(func=cmd_rename)

    p_del = wikied("delete", "tombstone a note (recoverable)")
    p_del.add_argument("note")
    p_del.add_argument("--dry-run", action="store_true")
    p_del.set_defaults(func=cmd_delete)

    p_purge = wikied("purge", "destroy a note AND its versions (leak remedy)")
    p_purge.add_argument("note")
    p_purge.add_argument("--reason", required=True, choices=PURGE_REASONS)
    p_purge.add_argument("--yes", action="store_true")
    p_purge.set_defaults(func=cmd_purge)

    p_merge = wikied("merge", "replace a note with a merged draft, retiring sources")
    p_merge.add_argument("--into", required=True)
    p_merge.add_argument("--from", dest="from_notes", action="append", required=True)
    p_merge.add_argument("--file", required=True, help="the merged draft")
    p_merge.add_argument("--gate-report", help="JSON verdict from the gate")
    p_merge.set_defaults(func=cmd_merge)

    p_vfy = wikied("verify", "verify the tamper-evident history chain")
    p_vfy.add_argument("--json", action="store_true")
    p_vfy.set_defaults(func=cmd_verify)

    p_st = wikied("status", "print the wiki receipt")
    p_st.set_defaults(func=cmd_status)

    p_rb = wikied("rollback", "restore the wiki to a prior chain state")
    p_rb.add_argument("--to", required=True, type=int, help="target seq")
    p_rb.add_argument("--yes", action="store_true")
    p_rb.set_defaults(func=cmd_rollback)

    p_gate = sub.add_parser("gate", help="deterministic method-not-matter gate")
    p_gate.add_argument("--candidate", required=True, help="candidate note file")
    p_gate.add_argument("--denylist", help="hashed denylist JSON")
    p_gate.add_argument("--out", help="write the verdict JSON here")
    p_gate.set_defaults(func=cmd_gate)

    p_dl = sub.add_parser("denylist-add", help="hash names into a denylist")
    p_dl.add_argument("--file", required=True, help="denylist JSON (created if absent)")
    p_dl.add_argument("names", nargs="+", help="names to hash (never stored as text)")
    p_dl.set_defaults(func=cmd_denylist_add)

    p_scan = sub.add_parser("seed-scan", help="deterministic seed-file inventory")
    p_scan.add_argument("files", nargs="+")
    p_scan.add_argument("--json", action="store_true")
    p_scan.set_defaults(func=cmd_seed_scan)

    p_emit = sub.add_parser("seed-emit", help="emit seed work items for the model")
    p_emit.add_argument("files", nargs="+")
    p_emit.add_argument("--out-dir", required=True)
    p_emit.add_argument(
        "--profile",
        default=str(
            Path(__file__).parent.parent / "references" / "source_profile.json"
        ),
    )
    p_emit.set_defaults(func=cmd_seed_emit)

    p_sland = wikied("seed-land", "verify, gate, and land filled seed items")
    p_sland.add_argument("--items", required=True, help="directory of item-*.json")
    p_sland.add_argument("--sources-root", required=True)
    p_sland.add_argument("--denylist")
    p_sland.add_argument("--mode", default="auto", choices=("auto", "markup"))
    p_sland.add_argument("--json", action="store_true")
    p_sland.set_defaults(func=cmd_seed_land)

    default_profile = str(
        Path(__file__).parent.parent / "references" / "source_profile.json"
    )

    p_cap = wikied("capture", "legacy raw-transcript staging (safely refused)")
    p_cap.add_argument("--staging", required=True, help="pre-gate staging dir")
    p_cap.add_argument("--session-dirs", nargs="+", help=argparse.SUPPRESS)
    p_cap.add_argument(
        "--transcript",
        help=argparse.SUPPRESS,
    )
    p_cap.add_argument("--profile", default=default_profile)
    p_cap.set_defaults(func=cmd_capture)

    p_cland = wikied("capture-land", "legacy import of prepared items (manual only)")
    p_cland.add_argument("--staging", required=True)
    p_cland.add_argument("--denylist")
    p_cland.add_argument("--mode", default="auto", choices=("auto", "markup"))
    p_cland.add_argument("--profile", default=default_profile)
    p_cland.set_defaults(func=cmd_capture_land)

    p_browse = wikied("browse", "read full wiki knowledge without frontmatter")
    p_browse.add_argument("--json", action="store_true")
    p_browse.add_argument("--note", help="show one bundle-relative note in full")
    p_browse.add_argument("--topic", help="show every matching topic note in full")
    p_browse.set_defaults(func=cmd_browse)

    p_ask = wikied("ask", "manual read-only search of the selected wiki")
    p_ask.add_argument("query")
    p_ask.add_argument("--limit", type=int, default=5)
    p_ask.add_argument("--json", action="store_true")
    p_ask.set_defaults(func=cmd_ask)

    p_review = wikied("review-record", "record a closed review disposition")
    p_review.add_argument("disposition", choices=REVIEW_DISPOSITIONS)
    p_review.add_argument("--note")
    p_review.add_argument("--source-id")
    p_review.set_defaults(func=cmd_review_record)

    p_auto = wikied("automation", "advanced optional lifecycle automation")
    p_auto.add_argument("--intake", choices=("on", "off"), help=argparse.SUPPRESS)
    p_auto.add_argument("--retrieval", choices=("on", "off"))
    p_auto.add_argument("--scope", choices=("all", "projects"))
    p_auto.add_argument(
        "--project", action="append", help="add a project folder and its subfolders"
    )
    p_auto.add_argument(
        "--remove-project", action="append", help="remove a selected project folder"
    )
    p_auto.add_argument("--yes", action="store_true")
    p_auto.set_defaults(func=cmd_automation)

    p_mt = wikied("maintain", "propose merges, flag staleness and contradictions")
    p_mt.add_argument("--json", action="store_true")
    p_mt.add_argument("--today", help="override today (YYYY-MM-DD) for staleness")
    p_mt.set_defaults(func=cmd_maintain)

    p_tw = wikied("tripwire", "auto-build quality metrics from the history")
    p_tw.add_argument("--window-from", help="ISO timestamp lower bound")
    p_tw.add_argument("--window-to", help="ISO timestamp upper bound")
    p_tw.add_argument("--json", action="store_true")
    p_tw.set_defaults(func=cmd_tripwire)

    p_acc = wikied("accept", "accept a pending suggestion (human-reviewed)")
    p_acc.add_argument("note")
    p_acc.add_argument("--by", required=True, help="human:<id> actor")
    p_acc.set_defaults(func=cmd_accept)

    p_dec = wikied("decline", "decline a pending suggestion (recoverable)")
    p_dec.add_argument("note")
    p_dec.set_defaults(func=cmd_decline)

    p_vn = wikied("verify-note", "confirm any note as human-reviewed")
    p_vn.add_argument("note")
    p_vn.add_argument("--by", required=True, help="human:<id> actor")
    p_vn.set_defaults(func=cmd_verify_note)

    p_map = wikied("export-map", "deterministic wiki-structure JSON")
    p_map.add_argument("--out", help="write here instead of stdout")
    p_map.add_argument(
        "--include-positions",
        action="store_true",
        help="include Position notes (they stay local by default)",
    )
    p_map.set_defaults(func=cmd_export_map)
    return parser


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv[1:])
    try:
        return args.func(args)
    except WikiError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
