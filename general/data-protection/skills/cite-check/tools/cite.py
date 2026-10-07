#!/usr/bin/env python3
"""
cite-check — verifiable legal-citation tooling for product counsel reviews.

This is the worker invoked by the cite-check Copilot CLI skill (see SKILL.md
in the same directory). It exposes a small set of subcommands the agent uses
to (a) maintain a local cache of the legal reference library, (b) extract
verbatim text from legal sources and product facts, (c) byte-for-byte verify
quoted spans (the hallucination guard), and (d) build a Word document of
Citation Cards on the user's Desktop.

Modeled on dvelton/eyeball. Every claim that ends up in a card must be
anchored in verbatim text from a real source; this tool refuses to emit a
card that fails verification.

Subcommands:
  setup-check       — confirm Python deps + gh CLI are present
  refresh-corpus    — mirror the cached file allowlist from
                      github/ppl-legal-reference into the local cache and
                      build a section index
  list-corpus       — print the current cache state (file, classification,
                      section count)
  extract-source    — given a citation ref (e.g. "03-reg-eu-gdpr.md#Article 6"
                      or a public URL), print verbatim section text + anchors
  extract-facts     — given a GitHub issue ref (owner/repo#N), print body +
                      comments as a structured fact corpus
  verify            — given a quoted span and a source ref, exit 0 iff the
                      quote appears byte-for-byte in the source
  build             — given a JSON file of Citation Cards, render a Word doc

Cache layout:
  ~/.copilot/skills/cite-check/cache/
    corpus/                  # mirrored markdown files
    index.json               # file → list of (anchor, byte_start, byte_end,
                             #                  classification, source_url)
    fetched/                 # web-fetched provisions (auto [VERIFY] tagged)
    facts/                   # cached fact corpora keyed by issue ref

Exit codes:
  0  success
  1  generic error
  2  verification failed (the hallucination guard tripped)
  3  missing dependency or unconfigured environment
"""
from __future__ import annotations

import argparse
import base64
import calendar
import dataclasses
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Iterable, Optional


# --- paths -------------------------------------------------------------------

TOOLS_DIR = Path(__file__).resolve().parent
TAXONOMY_PATH = TOOLS_DIR / "taxonomy.json"

CACHE_ROOT = Path.home() / ".copilot" / "skills" / "cite-check" / "cache"
CORPUS_DIR = CACHE_ROOT / "corpus"
FETCHED_DIR = CACHE_ROOT / "fetched"
FACTS_DIR = CACHE_ROOT / "facts"
RENDERED_DIR = CACHE_ROOT / "rendered"
AUTH_DIR = CACHE_ROOT / "authoritative"
AUTH_MANIFEST = AUTH_DIR / "manifest.json"
INDEX_PATH = CACHE_ROOT / "index.json"

REFERENCE_REPO = "github/ppl-legal-reference"


# --- small helpers -----------------------------------------------------------

def _ensure_dirs() -> None:
    for p in (CORPUS_DIR, FETCHED_DIR, FACTS_DIR, RENDERED_DIR, AUTH_DIR):
        p.mkdir(parents=True, exist_ok=True)


def _hash_key(*parts: str) -> str:
    h = hashlib.sha256()
    for part in parts:
        h.update(part.encode("utf-8"))
        h.update(b"\x00")
    return h.hexdigest()[:16]


def _load_taxonomy() -> dict[str, Any]:
    with TAXONOMY_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def _have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def _run(cmd: list[str], *, check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        check=check,
        capture_output=capture,
        text=True,
    )


def _classification_for(filename: str) -> str:
    """Map the ppl-legal-reference filename prefix to a source classification.

    Mirrors the prefix taxonomy described in the user's custom instructions:
      01-github-*   → github-public  (ToS, DPA, Privacy Statement, AUP, ...)
      02-internal-* → github-internal  (playbooks, training)
      03-reg-*      → public-law
      04-msft-*     → github-internal  (Microsoft contractual instruments — not
                       posted publicly, only shared with partners; cannot be a
                       primary cite for a legal conclusion)
      05-guidance-* → public-guidance
      06-ip-*       → public-law       (Title 17 + open source licenses)
      07-process-*  → github-internal
      08-caselaw-*  → public-guidance
    """
    base = filename.lower()
    if base.startswith("01-github-"):
        return "github-public"
    if base.startswith("02-internal-"):
        return "github-internal"
    if base.startswith("03-reg-"):
        return "public-law"
    if base.startswith("04-msft-"):
        return "github-internal"
    if base.startswith("05-guidance-"):
        return "public-guidance"
    if base.startswith("06-ip-"):
        return "public-law"
    if base.startswith("07-process-"):
        return "github-internal"
    if base.startswith("08-caselaw-"):
        return "public-guidance"
    return "github-public"


def _normalize_allowlist(taxonomy: dict[str, Any]) -> list[dict[str, Any]]:
    """Return the cached_corpus_allowlist as a list of dicts.

    The taxonomy file may store entries as plain filename strings (legacy v2
    schema) or as objects with `filename` plus authoritative-source metadata
    (v3 schema). Normalize to a uniform list of dicts so callers don't care.
    Each returned dict has at least: filename, authoritative_url (or None),
    authoritative_format (or None), extractor (or None).
    """
    raw = taxonomy.get("cached_corpus_allowlist", []) or []
    out: list[dict[str, Any]] = []
    for entry in raw:
        if isinstance(entry, str):
            out.append({
                "filename": entry,
                "authoritative_url": None,
                "authoritative_format": None,
                "extractor": None,
            })
        elif isinstance(entry, dict) and entry.get("filename"):
            out.append({
                "filename": entry["filename"],
                "authoritative_url": entry.get("authoritative_url"),
                "authoritative_format": entry.get("authoritative_format"),
                "extractor": entry.get("extractor"),
                "_note": entry.get("_note"),
            })
    return out


def _allowlist_filenames(taxonomy: dict[str, Any]) -> list[str]:
    return [e["filename"] for e in _normalize_allowlist(taxonomy)]


def _authoritative_meta_for(filename: str) -> Optional[dict[str, Any]]:
    """Return the authoritative-source metadata for a corpus filename, or None."""
    taxonomy = _load_taxonomy()
    for entry in _normalize_allowlist(taxonomy):
        if entry["filename"] == filename and entry.get("authoritative_url"):
            return entry
    return None


# --- subcommand: setup-check -------------------------------------------------

def cmd_setup_check(_args: argparse.Namespace) -> int:
    print("cite-check setup check")
    print("=" * 40)
    ok = True

    print(f"  python:       {sys.version.split()[0]}")

    for mod in ("docx", "fitz", "PIL", "playwright", "yaml", "requests", "markdown", "bs4", "lxml", "pdfminer"):
        try:
            __import__(mod if mod != "docx" else "docx")
            print(f"  module {mod:<12} ✓")
        except ImportError:
            print(f"  module {mod:<12} ✗  (run setup.sh / setup.ps1)")
            ok = False

    if _have("gh"):
        try:
            who = _run(["gh", "api", "user", "--jq", ".login"]).stdout.strip()
            print(f"  gh CLI        ✓  (authenticated as {who})")
        except subprocess.CalledProcessError:
            print("  gh CLI        ✗  (installed but not authenticated — run `gh auth login`)")
            ok = False
    else:
        print("  gh CLI        ✗  (install from https://cli.github.com/)")
        ok = False

    print(f"  cache root:   {CACHE_ROOT}  ({'exists' if CACHE_ROOT.exists() else 'will be created on first refresh'})")
    if INDEX_PATH.exists():
        idx = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        print(f"  corpus:       {len(idx.get('files', {}))} files indexed")
    else:
        print("  corpus:       not yet built — run `cite.py refresh-corpus`")

    return 0 if ok else 3


# --- subcommand: refresh-corpus ---------------------------------------------

_SECTION_PATTERNS: tuple[tuple[str, "re.Pattern[str]"], ...] = (
    # Markdown headings
    ("md-heading", re.compile(r"^(?P<lvl>#{1,6})\s+(?P<text>.+\S)\s*$", re.MULTILINE)),
    # Regulation chapter / section / annex headers (GDPR, EU AI Act):
    #   "Article 6", "Article 6a", "Article 6(1)", "CHAPTER III", "SECTION 1",
    #   "ANNEX III"
    ("regulation-article", re.compile(
        r"^(?P<text>(?:Article\s+\d+[a-z]?(?:\(\d+\))?"
        r"|CHAPTER\s+[IVXLCDM]+"
        r"|SECTION\s+\d+"
        r"|ANNEX\s+[IVXLCDM]+))\s*$",
        re.MULTILINE,
    )),
    # CCPA-style numbered code sections: "1798.100. Title"
    ("us-code-section", re.compile(
        r"^(?P<text>\d{3,4}\.\d{1,3}\.\s+[A-Z][^\n]{3,160})$",
        re.MULTILINE,
    )),
    # US Code section-sign headings (Title 17, etc.):
    #   "§107 · Limitations on exclusive rights: Fair use"
    # We require the bullet+title because PDF-extracted pages have many bare
    # "§NNN" page-footer occurrences that aren't real section starts.
    ("us-code-section-sign", re.compile(
        r"^(?P<text>§\s?\d{1,4}[A-Z]?\s*·\s*[^\n]{2,200})\s*$",
        re.MULTILINE,
    )),
    # Contract / DPA numbered sections: "1. Definitions.", "9. Subprocessors."
    # Heuristic: digit(s) + dot + space + capital, ending with a period and short
    # title text. Restricted enough to not match every numbered list item.
    ("contract-section", re.compile(
        r"^(?P<text>\d{1,2}\.\s+[A-Z][A-Za-z][A-Za-z0-9 ,.&'/-]{2,80}\.)\s*(?:[A-Z]|$)",
        re.MULTILINE,
    )),
)


def _index_document(text: str) -> list[dict[str, Any]]:
    """Build a list of section anchors from a corpus document.

    Recognizes four structural conventions used in github/ppl-legal-reference:
      1. Markdown ATX headings (#, ##, ...)
      2. Regulation articles / chapters / annexes (GDPR, EU AI Act): bare lines
         like "Article 6", "CHAPTER III", "ANNEX III", "SECTION 1"
      3. US-code-style sections: "1798.100. Title" (CCPA)
      4. Contract / DPA numbered sections: "9. Subprocessors."

    Each returned section records (anchor, kind, level, byte_start, byte_end).
    The byte range covers from the matched line through the byte before the
    next section start (or end of file).
    """
    raw = text.encode("utf-8")
    if not raw:
        return [{"anchor": "(empty)", "kind": "doc", "level": 0, "byte_start": 0, "byte_end": 0}]

    # Convert character offsets to byte offsets once for the whole doc.
    char_to_byte = []
    cursor = 0
    for ch in text:
        char_to_byte.append(cursor)
        cursor += len(ch.encode("utf-8"))
    char_to_byte.append(len(raw))

    found: list[dict[str, Any]] = []
    seen_starts: set[int] = set()
    for kind, pat in _SECTION_PATTERNS:
        for m in pat.finditer(text):
            start_char = m.start()
            if start_char in seen_starts:
                continue
            seen_starts.add(start_char)
            anchor_text = m.group("text").strip()
            level = len(m.group("lvl")) if "lvl" in m.groupdict() and m.group("lvl") else 2
            found.append({
                "anchor": anchor_text,
                "kind": kind,
                "level": level,
                "_start_char": start_char,
                "byte_start": char_to_byte[start_char],
            })

    if not found:
        return [{
            "anchor": "(whole document)", "kind": "doc", "level": 0,
            "byte_start": 0, "byte_end": len(raw),
        }]

    found.sort(key=lambda s: s["_start_char"])
    sections: list[dict[str, Any]] = []
    for i, s in enumerate(found):
        end = found[i + 1]["byte_start"] if i + 1 < len(found) else len(raw)
        sections.append({
            "anchor": s["anchor"],
            "kind": s["kind"],
            "level": s["level"],
            "byte_start": s["byte_start"],
            "byte_end": end,
        })
    return sections


# Back-compat alias — earlier code (and tests) may reference _index_markdown.
_index_markdown = _index_document


def cmd_refresh_corpus(args: argparse.Namespace) -> int:
    if not _have("gh"):
        print("error: gh CLI not found. Install from https://cli.github.com/", file=sys.stderr)
        return 3

    _ensure_dirs()
    taxonomy = _load_taxonomy()
    allowlist: list[str] = _allowlist_filenames(taxonomy)
    if args.only:
        allowlist = [f for f in allowlist if f in set(args.only)]

    print(f"Refreshing {len(allowlist)} files from {REFERENCE_REPO} into {CORPUS_DIR}")
    # Merge with the existing index so `--only` updates a subset without
    # discarding entries for files we didn't fetch this run.
    if INDEX_PATH.exists() and args.only:
        try:
            index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
            index.setdefault("files", {})
            index["reference_repo"] = REFERENCE_REPO
        except (json.JSONDecodeError, ValueError):
            index = {"reference_repo": REFERENCE_REPO, "files": {}}
    else:
        index = {"reference_repo": REFERENCE_REPO, "files": {}}

    for filename in allowlist:
        api_path = f"repos/{REFERENCE_REPO}/contents/{filename}"
        try:
            raw = _run(["gh", "api", api_path]).stdout
            payload = json.loads(raw)
            content_b64 = payload.get("content", "")
            sha = payload.get("sha", "")
            file_size = payload.get("size", 0)
            encoding = payload.get("encoding", "")
            content = base64.b64decode(content_b64).decode("utf-8") if content_b64 else ""
            # GitHub Contents API returns empty content with encoding="none" for
            # files larger than ~1MB. Fall back to the raw blob endpoint, which
            # streams the full file regardless of size.
            if (not content) and file_size > 0 and encoding in ("none", ""):
                blob_raw = _run([
                    "gh", "api",
                    "-H", "Accept: application/vnd.github.raw",
                    f"repos/{REFERENCE_REPO}/contents/{filename}",
                ]).stdout
                content = blob_raw
        except subprocess.CalledProcessError as e:
            print(f"  ✗ {filename}  (gh api failed — file may not exist yet)")
            print(f"      {e.stderr.strip().splitlines()[0] if e.stderr else ''}")
            continue
        except (json.JSONDecodeError, ValueError) as e:
            print(f"  ✗ {filename}  (decode error: {e})")
            continue

        local = CORPUS_DIR / filename
        local.write_text(content, encoding="utf-8")
        sections = _index_document(content)
        classification = _classification_for(filename)
        index["files"][filename] = {
            "sha": sha,
            "byte_size": len(content.encode("utf-8")),
            "classification": classification,
            "source_url": f"https://github.com/{REFERENCE_REPO}/blob/main/{filename}",
            "sections": sections,
        }
        print(f"  ✓ {filename:<45} {classification:<18} {len(sections):>3} sections")

    INDEX_PATH.write_text(json.dumps(index, indent=2), encoding="utf-8")
    print(f"\nWrote index: {INDEX_PATH}")
    return 0


# --- authoritative-source layer ---------------------------------------------
#
# For every publicly-citable file in the corpus, taxonomy.json maps it to an
# `authoritative_url` published by the regulator / legislature / standards body
# itself (EUR-Lex, leginfo.legislature.ca.gov, gnu.org, docs.github.com, etc.).
# `refresh-authoritative` fetches each URL, normalizes the content to plain
# text, and stores it under cache/authoritative/<filename>.txt with a manifest
# entry. `verify-corpus` then diffs the cached corpus copy against the
# authoritative copy to detect drift (mirror is stale, edited, or incomplete).
# Pressure-test consults the authoritative copy first for byte-for-byte quote
# verification, falling back to the mirror only when the auth source is
# unreachable.

_USER_AGENT = (
    "cite-check/0.2 (legal-citation verifier; "
    "+https://github.com/nkasuku/cite-check)"
)


def _auth_text_path(filename: str) -> Path:
    return AUTH_DIR / (filename.rsplit(".", 1)[0] + ".txt")


def _load_auth_manifest() -> dict[str, Any]:
    if not AUTH_MANIFEST.exists():
        return {"files": {}}
    try:
        return json.loads(AUTH_MANIFEST.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, ValueError):
        return {"files": {}}


def _write_auth_manifest(manifest: dict[str, Any]) -> None:
    AUTH_MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")


def _http_get(url: str, *, accept: str = "text/html,application/xhtml+xml,*/*"):
    """Polite HTTP GET with a stable user agent and reasonable timeout."""
    import requests  # noqa: WPS433 — deferred so setup-check can report missing dep
    return requests.get(
        url,
        headers={"User-Agent": _USER_AGENT, "Accept": accept},
        timeout=45,
        allow_redirects=True,
    )


def _extract_eur_lex(html: str) -> str:
    """EUR-Lex serves XHTML. Take the body text — it includes all recitals,
    articles, and annexes in a single document with no navigation chrome to
    speak of inside <body><div>."""
    import warnings
    from bs4 import XMLParsedAsHTMLWarning  # type: ignore
    warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    body = soup.find("body") or soup
    return body.get_text(separator="\n", strip=True)


def _extract_github_docs(html: str) -> str:
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    el = (
        soup.select_one("div[data-search='article-body']")
        or soup.select_one("div.markdown-body")
        or soup.select_one("article")
        or soup.select_one("main")
    )
    if el is None:
        return ""
    return el.get_text(separator="\n", strip=True)


def _extract_legislation_uk(html: str) -> str:
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    el = (
        soup.select_one("#content")
        or soup.select_one("#viewLegContents")
        or soup.select_one(".LegContent")
        or soup.find("body")
    )
    return el.get_text(separator="\n", strip=True) if el else ""


def _extract_leginfo(html: str) -> str:
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    el = (
        soup.select_one("#manylawsections")
        or soup.select_one("#centerColumn")
        or soup.find("body")
    )
    return el.get_text(separator="\n", strip=True) if el else ""


def _extract_ftc(html: str) -> str:
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    el = (
        soup.select_one("article")
        or soup.select_one("main")
        or soup.find("body")
    )
    return el.get_text(separator="\n", strip=True) if el else ""


def _extract_curia(html: str) -> str:
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    # Curia HTML wraps the judgment text in <div class="C19Centre"> or similar
    # depending on doc; fall back to body text.
    el = (
        soup.select_one("body > div.C19Centre")
        or soup.find("body")
    )
    return el.get_text(separator="\n", strip=True) if el else ""


def _extract_wp29(html: str) -> str:
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    el = soup.select_one("main") or soup.select_one("article") or soup.find("body")
    return el.get_text(separator="\n", strip=True) if el else ""


def _extract_opensource_org(html: str) -> str:
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    el = (
        soup.select_one("article")
        or soup.select_one("main")
        or soup.select_one(".entry-content")
        or soup.find("body")
    )
    return el.get_text(separator="\n", strip=True) if el else ""


def _extract_spdx(html: str) -> str:
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    el = soup.select_one("table") or soup.find("body")
    return el.get_text(separator="\n", strip=True) if el else ""


def _extract_cornell_lii(html: str) -> str:
    from bs4 import BeautifulSoup  # type: ignore
    soup = BeautifulSoup(html, "lxml")
    el = (
        soup.select_one("#main-content")
        or soup.select_one("main")
        or soup.select_one("#content")
        or soup.find("body")
    )
    return el.get_text(separator="\n", strip=True) if el else ""


def _extract_text(text: str) -> str:
    """Identity for plain-text sources (gnu.org, apache.org license files)."""
    return text


def _extract_pdf(pdf_bytes: bytes) -> str:
    """Use pdfminer to pull text out of the PDF."""
    from io import BytesIO
    from pdfminer.high_level import extract_text  # type: ignore
    return extract_text(BytesIO(pdf_bytes))


_EXTRACTORS = {
    "eur_lex": _extract_eur_lex,
    "github_docs": _extract_github_docs,
    "legislation_uk": _extract_legislation_uk,
    "leginfo": _extract_leginfo,
    "ftc": _extract_ftc,
    "curia": _extract_curia,
    "wp29": _extract_wp29,
    "opensource_org": _extract_opensource_org,
    "spdx": _extract_spdx,
    "cornell_lii": _extract_cornell_lii,
    "text": _extract_text,
    "pdf": _extract_pdf,
}


def _fetch_authoritative(entry: dict[str, Any]) -> dict[str, Any]:
    """Fetch + extract one authoritative source. Returns a manifest record:
        {filename, url, fetched_at, http_status, content_length, content_hash,
         etag (if any), error (if any)}.
    Writes the extracted text to cache/authoritative/<filename>.txt on success.
    """
    filename = entry["filename"]
    url = entry["authoritative_url"]
    fmt = entry.get("authoritative_format") or "html"
    extractor_name = entry.get("extractor") or "html"
    record: dict[str, Any] = {
        "filename": filename,
        "url": url,
        "format": fmt,
        "extractor": extractor_name,
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "http_status": None,
        "content_length": 0,
        "content_hash": None,
        "etag": None,
        "error": None,
    }
    try:
        accept = "application/pdf" if fmt == "pdf" else "text/html,application/xhtml+xml,*/*"
        resp = _http_get(url, accept=accept)
        record["http_status"] = resp.status_code
        record["etag"] = resp.headers.get("ETag")
        if resp.status_code != 200:
            record["error"] = f"HTTP {resp.status_code}"
            return record
        extractor = _EXTRACTORS.get(extractor_name)
        if extractor is None:
            record["error"] = f"unknown extractor {extractor_name!r}"
            return record
        if fmt == "pdf":
            text = extractor(resp.content)
        elif fmt == "text":
            text = extractor(resp.text)
        else:
            text = extractor(resp.text)
    except Exception as e:  # noqa: BLE001 — refresh must never crash on one bad source
        record["error"] = f"{type(e).__name__}: {e}"
        return record

    if not text or not text.strip():
        record["error"] = "extractor returned empty text"
        return record

    record["content_length"] = len(text)
    record["content_hash"] = hashlib.sha256(text.encode("utf-8")).hexdigest()
    _auth_text_path(filename).write_text(text, encoding="utf-8")
    return record


def _load_auth_text(filename: str) -> Optional[str]:
    """Return the cached authoritative text for a corpus filename, or None."""
    p = _auth_text_path(filename)
    if not p.exists():
        return None
    try:
        return p.read_text(encoding="utf-8")
    except OSError:
        return None


def _auth_age_days(filename: str) -> Optional[float]:
    """Return how many days old the cached authoritative copy is, or None.

    Reads the manifest's `fetched_at` ISO timestamp first; falls back to the
    on-disk mtime if the manifest is missing or unparseable. Returns None when
    the file isn't cached at all.
    """
    if not _auth_text_path(filename).exists():
        return None
    manifest = _load_auth_manifest()
    record = manifest.get("files", {}).get(filename) or {}
    fetched_at = record.get("fetched_at")
    if fetched_at:
        try:
            t = time.strptime(fetched_at, "%Y-%m-%dT%H:%M:%SZ")
            fetched_epoch = calendar.timegm(t)
            return max(0.0, (time.time() - fetched_epoch) / 86400.0)
        except (ValueError, TypeError):
            pass
    try:
        mtime = _auth_text_path(filename).stat().st_mtime
        return max(0.0, (time.time() - mtime) / 86400.0)
    except OSError:
        return None


# --- subcommand: refresh-authoritative --------------------------------------

def cmd_refresh_authoritative(args: argparse.Namespace) -> int:
    """Fetch every file's authoritative URL, extract clean text, cache it, and
    write a manifest. Files without an authoritative_url (intentionally:
    internal docs) are skipped with a clear note."""
    _ensure_dirs()
    taxonomy = _load_taxonomy()
    entries = _normalize_allowlist(taxonomy)
    selected = set(args.only or [])
    if selected:
        entries = [e for e in entries if e["filename"] in selected]

    manifest = _load_auth_manifest()
    files_section: dict[str, Any] = manifest.setdefault("files", {})

    fetched = skipped = failed = 0
    print(f"Refreshing authoritative sources ({len(entries)} entries)…")
    for entry in entries:
        filename = entry["filename"]
        url = entry.get("authoritative_url")
        if not url:
            note = entry.get("_note") or "no authoritative URL configured"
            print(f"  - {filename:<48} skipped — {note[:80]}")
            skipped += 1
            continue
        if not args.force and filename in files_section and files_section[filename].get("content_hash"):
            existing_text = _load_auth_text(filename)
            if existing_text is not None:
                print(f"  ⤳ {filename:<48} cached ({files_section[filename].get('content_length', 0)} chars) — pass --force to re-fetch")
                continue

        record = _fetch_authoritative(entry)
        files_section[filename] = record
        if record["error"]:
            print(f"  ✗ {filename:<48} {record['error']}")
            failed += 1
        else:
            print(f"  ✓ {filename:<48} {record['content_length']:>7} chars  hash={record['content_hash'][:12]}")
            fetched += 1
        time.sleep(args.delay)

    manifest["files"] = files_section
    manifest["last_refreshed"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    _write_auth_manifest(manifest)
    print()
    print(f"Authoritative manifest: {AUTH_MANIFEST}")
    print(f"  fetched: {fetched}   cached: {len(entries) - fetched - skipped - failed}   skipped: {skipped}   failed: {failed}")
    return 1 if failed else 0


# --- subcommand: verify-corpus ----------------------------------------------

_MIRROR_ARTIFACT_PATTERNS = (
    re.compile(r"^#{1,6}\s"),                    # markdown headers added by mirror
    re.compile(r"^\*Extracted from:"),           # provenance line added by mirror
    re.compile(r"^<!--\s*Page\s+\d+\s*-->$"),    # page-break markers from PDF extraction
    re.compile(r"^<!--\s*end of page"),
    re.compile(r"^---+$"),                        # horizontal rules
    re.compile(r"^=+$"),
    re.compile(r"^In this article$"),             # docs.github.com TOC label
    re.compile(r"^\*?\(?\d+\)?\*?$"),             # footnote markers like "(1)" or "1."
)


def _is_mirror_artifact(line: str) -> bool:
    line = line.strip()
    if not line:
        return True
    return any(p.match(line) for p in _MIRROR_ARTIFACT_PATTERNS)


def _drift_summary(corpus_text: str, auth_text: str) -> dict[str, Any]:
    """Compare the corpus mirror against the authoritative source.

    Comparison is done on `_normalize_for_match`-normalized text so that
    cosmetic mirror reformatting (line wraps, smart quotes) doesn't register
    as drift. Mirror-side wrapper artifacts (markdown headers added by the
    mirror, PDF page-break markers, provenance lines like "*Extracted from:
    ...*", footnote-marker-only lines) are excluded from the comparison —
    they can't be drift because the authoritative source never had them.

    Returns:
      - in_sync: True iff every legally-meaningful normalized line in the
        corpus appears in the authoritative text.
      - corpus_lines: count of normalized non-empty corpus lines compared
      - matched_lines, missing_count, missing_examples (first 5)
      - artifact_lines: count of mirror artifacts excluded from comparison
    """
    auth_norm = _normalize_for_match(auth_text)
    matched = 0
    missing: list[str] = []
    artifacts = 0
    compared = 0
    for raw_line in corpus_text.splitlines():
        if _is_mirror_artifact(raw_line):
            artifacts += 1
            continue
        ln = _normalize_for_match(raw_line)
        if not ln:
            continue
        compared += 1
        # Skip very short lines (likely "(a)" / "1." / numbered list markers
        # that survived after mirror-artifact filtering).
        if len(ln) < 12:
            matched += 1
            continue
        if ln in auth_norm:
            matched += 1
        else:
            missing.append(ln)
    return {
        "corpus_lines": compared,
        "matched_lines": matched,
        "missing_count": len(missing),
        "missing_examples": missing[:5],
        "artifact_lines_excluded": artifacts,
        "in_sync": len(missing) == 0,
    }


def cmd_verify_corpus(args: argparse.Namespace) -> int:
    """For each corpus file with an authoritative source, check whether the
    mirror is still in sync. Emits a markdown report (or JSON) and exits 1 if
    any drift was detected."""
    _ensure_dirs()
    taxonomy = _load_taxonomy()
    entries = _normalize_allowlist(taxonomy)
    if args.only:
        entries = [e for e in entries if e["filename"] in set(args.only)]

    manifest = _load_auth_manifest()
    rows: list[dict[str, Any]] = []
    drift_seen = False
    for entry in entries:
        filename = entry["filename"]
        url = entry.get("authoritative_url")
        row: dict[str, Any] = {
            "filename": filename,
            "url": url,
            "status": None,
            "detail": None,
        }
        if not url:
            row["status"] = "no-auth-source"
            row["detail"] = entry.get("_note") or "no authoritative URL configured (intentional for internal documents)"
            rows.append(row)
            continue

        corpus_path = CORPUS_DIR / filename
        auth_text = _load_auth_text(filename)
        manifest_record = manifest.get("files", {}).get(filename) or {}
        if auth_text is None:
            row["status"] = "auth-not-fetched"
            err = manifest_record.get("error")
            row["detail"] = f"authoritative source not yet cached — run refresh-authoritative" + (f" (last error: {err})" if err else "")
            drift_seen = True
            rows.append(row)
            continue
        if not corpus_path.exists():
            row["status"] = "corpus-missing"
            row["detail"] = f"corpus mirror not present — run refresh-corpus"
            drift_seen = True
            rows.append(row)
            continue
        corpus_text = corpus_path.read_text(encoding="utf-8")
        diff = _drift_summary(corpus_text, auth_text)
        row["drift"] = diff
        if diff["in_sync"]:
            row["status"] = "in-sync"
            row["detail"] = f"{diff['matched_lines']} / {diff['corpus_lines']} normalized lines match"
        else:
            row["status"] = "drift"
            row["detail"] = (
                f"{diff['missing_count']} normalized line(s) in mirror not present in authoritative source"
            )
            drift_seen = True
        rows.append(row)

    if args.json:
        print(json.dumps({"rows": rows, "drift_detected": drift_seen}, indent=2))
        return 1 if drift_seen else 0

    print(f"# verify-corpus report ({len(rows)} files)\n")
    for row in rows:
        sym = {
            "in-sync": "✓",
            "drift": "✗",
            "auth-not-fetched": "?",
            "corpus-missing": "?",
            "no-auth-source": "—",
        }.get(row["status"], "?")
        print(f"{sym} {row['filename']:<48} {row['status']:<18} {row['detail']}")
        if row["status"] == "drift":
            for ex in row.get("drift", {}).get("missing_examples", []):
                print(f"     missing: {ex[:120]}{'…' if len(ex) > 120 else ''}")
    print()
    print(f"Authoritative manifest: {AUTH_MANIFEST}")
    if drift_seen:
        print("⚠ at least one file is out of sync with its authoritative source.")
    else:
        print("✓ every cached corpus file with an authoritative source is in sync.")
    return 1 if drift_seen else 0


# --- subcommand: list-corpus -------------------------------------------------

def cmd_list_corpus(args: argparse.Namespace) -> int:
    if not INDEX_PATH.exists():
        print("No corpus indexed yet. Run: cite.py refresh-corpus", file=sys.stderr)
        return 1
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    print(f"Reference repo: {index.get('reference_repo')}")
    print(f"Cache:          {CORPUS_DIR}\n")
    files = index.get("files", {})
    target = getattr(args, "file", None)
    if target:
        meta = files.get(target)
        if not meta:
            print(f"{target} not in cached corpus.", file=sys.stderr)
            print("Available files:", file=sys.stderr)
            for f in sorted(files):
                print(f"  {f}", file=sys.stderr)
            return 1
        print(
            f"  {target:<45} {meta['classification']:<18} "
            f"{meta['byte_size']:>7} bytes  {len(meta['sections']):>3} sections\n"
        )
        for s in meta["sections"]:
            kind = s.get("kind", "md-heading")
            print(f"    [{kind}] {s['anchor']}")
        return 0

    for filename, meta in sorted(files.items()):
        print(
            f"  {filename:<45} {meta['classification']:<18} "
            f"{meta['byte_size']:>7} bytes  {len(meta['sections']):>3} sections"
        )
    return 0


# --- subcommand: extract-source ---------------------------------------------

def _resolve_corpus_section(filename: str, anchor: str | None) -> dict[str, Any]:
    if not INDEX_PATH.exists():
        raise FileNotFoundError("Corpus index missing. Run refresh-corpus first.")
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    file_meta = index.get("files", {}).get(filename)
    if not file_meta:
        raise KeyError(f"{filename} not in cached corpus. Add to taxonomy.cached_corpus_allowlist and refresh.")
    local = CORPUS_DIR / filename
    if not local.exists():
        raise FileNotFoundError(f"Local copy missing: {local}. Run refresh-corpus.")
    raw_bytes = local.read_bytes()

    if not anchor:
        return {
            "filename": filename,
            "anchor": "(whole document)",
            "classification": file_meta["classification"],
            "source_url": file_meta["source_url"],
            "text": raw_bytes.decode("utf-8"),
            "byte_start": 0,
            "byte_end": len(raw_bytes),
        }

    matches = [s for s in file_meta["sections"] if s["anchor"].lower() == anchor.lower()]
    if not matches:
        matches = [s for s in file_meta["sections"] if anchor.lower() in s["anchor"].lower()]
    if not matches:
        raise KeyError(
            f"Anchor '{anchor}' not found in {filename}. "
            f"Available headings (first 20): {[s['anchor'] for s in file_meta['sections'][:20]]}"
        )
    section = matches[0]
    text = raw_bytes[section["byte_start"]: section["byte_end"]].decode("utf-8")
    return {
        "filename": filename,
        "anchor": section["anchor"],
        "classification": file_meta["classification"],
        "source_url": file_meta["source_url"],
        "text": text,
        "byte_start": section["byte_start"],
        "byte_end": section["byte_end"],
    }


def _fetch_web_source(url: str) -> dict[str, Any]:
    """Fetch a web source and cache it under fetched/. Auto-tagged [VERIFY]."""
    import requests  # noqa: WPS433 (deferred import keeps setup-check informative)

    cache_key = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
    target = FETCHED_DIR / f"{cache_key}.txt"
    meta_target = FETCHED_DIR / f"{cache_key}.meta.json"
    if not target.exists():
        resp = requests.get(url, timeout=30, headers={"User-Agent": "cite-check/0.1"})
        resp.raise_for_status()
        target.write_text(resp.text, encoding="utf-8")
        meta_target.write_text(json.dumps({"url": url}), encoding="utf-8")
    return {
        "filename": str(target),
        "anchor": "(web)",
        "classification": "verify-required",
        "source_url": url,
        "text": target.read_text(encoding="utf-8"),
        "byte_start": 0,
        "byte_end": target.stat().st_size,
        "verify_tag": True,
    }


def _resolve_source_text(ref: str) -> dict[str, Any]:
    """Single dispatcher used by extract-source, verify, and screenshot to
    obtain the verbatim text of a source.

    Recognized source-ref shapes:
      * http(s):// URL                    → web fetch, classification verify-required
      * <owner>/<repo>#<N>               → GitHub issue body
      * <owner>/<repo>#<N>::comment_<id> → a single GitHub issue comment
      * <filename>.md                    → whole cached corpus file
      * <filename>.md#<anchor>           → one section of a cached corpus file

    Returns the same dict shape produced by `_resolve_corpus_section` /
    `_fetch_web_source` so verify can do byte-for-byte matching uniformly.
    """
    ref = ref.strip()
    if ref.startswith(("http://", "https://")):
        return _fetch_web_source(ref)

    cm = _COMMENT_REF_RE.match(ref)
    if cm:
        owner, repo, num = cm.group("owner"), cm.group("repo"), cm.group("num")
        comment_id = cm.group("cid")
        facts = _load_facts(f"{owner}/{repo}#{num}")
        if comment_id:
            comment = next(
                (c for c in facts.get("comments", []) if str(c.get("id")) == comment_id),
                None,
            )
            if not comment:
                raise KeyError(f"Comment {comment_id} not found in {ref}")
            text = comment.get("body", "") or ""
            anchor = f"comment by @{comment.get('author', '(unknown)')} on {comment.get('created_at', '')[:10]}"
            url = comment.get("url", facts.get("url"))
        else:
            text = facts.get("body", "") or ""
            anchor = f"issue body by @{facts.get('author', '(unknown)')}"
            url = facts.get("url")
        return {
            "filename": ref,
            "anchor": anchor,
            "classification": "github-public",
            "source_url": url,
            "text": text,
            "byte_start": 0,
            "byte_end": len(text.encode("utf-8")),
        }

    if "#" in ref:
        filename, anchor = ref.split("#", 1)
        return _resolve_corpus_section(filename.strip(), anchor.strip())
    return _resolve_corpus_section(ref, None)


def cmd_extract_source(args: argparse.Namespace) -> int:
    ref: str = args.ref.strip()
    try:
        result = _resolve_source_text(ref)
    except (KeyError, FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Source:         {result['source_url']}")
        print(f"Anchor:         {result['anchor']}")
        print(f"Classification: {result['classification']}")
        if result.get("verify_tag"):
            print("Tag:            [VERIFY] (web-fetched)")
        print(f"Bytes:          {result['byte_start']}–{result['byte_end']}")
        print("-" * 60)
        print(result["text"])
    return 0


# --- subcommand: extract-facts ----------------------------------------------

_ISSUE_RE = re.compile(r"^(?P<owner>[^/]+)/(?P<repo>[^#]+)#(?P<num>\d+)$")


def _load_facts(issue_ref: str) -> dict[str, Any]:
    """Load (and cache) a GitHub issue's body + comments. Reusable by build/screenshot."""
    if not _have("gh"):
        raise RuntimeError("gh CLI not found.")
    m = _ISSUE_RE.match(issue_ref.strip())
    if not m:
        raise ValueError("issue ref must look like 'owner/repo#123'")
    owner, repo, num = m.group("owner"), m.group("repo"), m.group("num")
    _ensure_dirs()
    cached = FACTS_DIR / f"{owner}__{repo}__{num}.json"
    if cached.exists():
        return json.loads(cached.read_text(encoding="utf-8"))

    api_path = f"repos/{owner}/{repo}/issues/{num}"
    issue = json.loads(_run(["gh", "api", api_path]).stdout)
    comments = json.loads(_run(["gh", "api", f"{api_path}/comments"]).stdout)
    facts = {
        "ref": f"{owner}/{repo}#{num}",
        "url": issue.get("html_url"),
        "title": issue.get("title"),
        "author": issue.get("user", {}).get("login"),
        "created_at": issue.get("created_at"),
        "state": issue.get("state"),
        "labels": [lbl.get("name") for lbl in issue.get("labels", [])],
        "body": issue.get("body") or "",
        "comments": [
            {
                "id": c.get("id"),
                "author": c.get("user", {}).get("login"),
                "created_at": c.get("created_at"),
                "url": c.get("html_url"),
                "body": c.get("body") or "",
            }
            for c in comments
        ],
    }
    cached.write_text(json.dumps(facts, indent=2), encoding="utf-8")
    return facts


def cmd_extract_facts(args: argparse.Namespace) -> int:
    try:
        facts = _load_facts(args.issue)
    except (RuntimeError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 3 if "gh CLI" in str(e) else 1
    except subprocess.CalledProcessError as e:
        print(f"error: gh api failed — {e.stderr.strip()}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(facts, indent=2))
    else:
        print(f"Issue:    {facts['ref']}  ({facts['url']})")
        print(f"Title:    {facts['title']}")
        print(f"Author:   {facts['author']}  ({facts['created_at']})")
        print(f"Labels:   {', '.join(facts['labels']) or '(none)'}")
        print(f"Comments: {len(facts['comments'])}")
        m = _ISSUE_RE.match(args.issue.strip())
        if m:
            owner, repo, num = m.group("owner"), m.group("repo"), m.group("num")
            print(f"Cached:   {FACTS_DIR / f'{owner}__{repo}__{num}.json'}")
    return 0


# --- subcommand: verify ------------------------------------------------------

def _normalize_for_match(s: str) -> str:
    """Light normalization to absorb whitespace differences without weakening
    the byte-for-byte intent. Collapses runs of whitespace; keeps everything
    else untouched. Tightens to true byte-for-byte if --strict is passed."""
    return re.sub(r"\s+", " ", s).strip()


def cmd_verify(args: argparse.Namespace) -> int:
    quote: str = args.quote
    ref: str = args.source.strip()

    try:
        source = _resolve_source_text(ref)
    except (KeyError, FileNotFoundError, ValueError, RuntimeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    haystack = source["text"]
    if args.strict:
        ok = quote in haystack
    else:
        ok = _normalize_for_match(quote) in _normalize_for_match(haystack)

    payload = {
        "ok": ok,
        "quote_sha256": hashlib.sha256(quote.encode("utf-8")).hexdigest(),
        "source": source["source_url"],
        "anchor": source["anchor"],
        "classification": source["classification"],
        "verify_required": bool(source.get("verify_tag")),
        "mode": "strict" if args.strict else "whitespace-normalized",
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    elif ok:
        print(f"✓ verified  ({payload['mode']})  {source['source_url']} :: {source['anchor']}")
        if payload["verify_required"]:
            print("  note: source was web-fetched — append [VERIFY] tag in the citation card.")
    else:
        print(f"✗ NOT FOUND in source  ({payload['mode']})")
        print(f"  source:   {source['source_url']}")
        print(f"  anchor:   {source['anchor']}")
        print(f"  quote:    {quote[:120]}{'...' if len(quote) > 120 else ''}")
        print("  refusal:  cite-check will not emit a card with an unverified quote.")
    return 0 if ok else 2


# --- screenshot rendering ---------------------------------------------------
#
# eyeball-style: render the source to PDF (Playwright headless Chromium),
# search the rendered PDF for the verbatim quote with fitz.search_for, crop a
# region around the hit with padding, draw a yellow highlight rectangle, and
# emit a PNG. Two source types are supported:
#
#   1. cached corpus markdown — converted to HTML with print-friendly CSS
#      so headings, tables, and lists render legibly in the PDF.
#   2. product facts (issue body or a single comment) — wrapped in a
#      GitHub-like comment card so the screenshot is recognizably "an issue
#      comment from @author on date X".
#
# Rendered PDFs are cached under ~/.copilot/skills/cite-check/cache/rendered/
# keyed by a hash of (renderer_kind, source_ref, content_hash).

_DOC_HTML = """<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<style>
  body {{ font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
          font-size: 11pt; line-height: 1.55; color: #1f2328;
          padding: 24px 8px; max-width: 760px; }}
  h1, h2, h3, h4, h5, h6 {{ font-weight: 600; line-height: 1.25; }}
  h1 {{ font-size: 22pt; padding-bottom: 6px; border-bottom: 1px solid #d0d7de; }}
  h2 {{ font-size: 17pt; padding-bottom: 4px; border-bottom: 1px solid #d0d7de; margin-top: 22pt; }}
  h3 {{ font-size: 14pt; margin-top: 16pt; }}
  h4, h5, h6 {{ font-size: 12pt; margin-top: 12pt; }}
  p, li {{ margin: 0 0 0.6em 0; }}
  pre, code {{ font-family: "SF Mono", Menlo, Consolas, monospace; font-size: 9.5pt; }}
  pre {{ background: #f6f8fa; padding: 10px; border-radius: 6px; overflow-x: auto; }}
  blockquote {{ margin: 0 0 1em 0; padding: 0 1em; color: #57606a; border-left: 3px solid #d0d7de; }}
  table {{ border-collapse: collapse; }}
  td, th {{ border: 1px solid #d0d7de; padding: 4px 8px; }}
  .source-banner {{ background: #ddf4ff; border: 1px solid #54aeff; border-radius: 6px;
                    padding: 8px 12px; margin-bottom: 16px; font-size: 9.5pt; color: #0969da; }}
</style></head><body>
{banner}
{content}
</body></html>"""

_COMMENT_HTML = """<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<style>
  body {{ font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
          font-size: 11pt; line-height: 1.55; color: #1f2328;
          padding: 24px 8px; max-width: 760px; }}
  .issue-banner {{ background: #ddf4ff; border: 1px solid #54aeff; border-radius: 6px;
                   padding: 10px 14px; margin-bottom: 16px; }}
  .issue-banner .title {{ font-weight: 600; font-size: 13pt; color: #1f2328; }}
  .issue-banner .meta {{ font-size: 9.5pt; color: #0969da; margin-top: 4px; }}
  .comment {{ border: 1px solid #d0d7de; border-radius: 6px; margin-bottom: 16px; }}
  .comment-header {{ background: #f6f8fa; padding: 10px 14px;
                     border-bottom: 1px solid #d0d7de; font-size: 10pt; color: #57606a; }}
  .comment-author {{ color: #0969da; font-weight: 600; }}
  .comment-body {{ padding: 14px; }}
  .comment-body p, .comment-body li {{ margin: 0 0 0.6em 0; }}
  pre, code {{ font-family: "SF Mono", Menlo, Consolas, monospace; font-size: 9.5pt; }}
  pre {{ background: #f6f8fa; padding: 10px; border-radius: 6px; }}
</style></head><body>
{banner}
{content}
</body></html>"""


def _markdown_to_html(md_text: str) -> str:
    try:
        import markdown
    except ImportError:
        from html import escape
        return f"<pre>{escape(md_text)}</pre>"
    return markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "sane_lists"],
    )


def _render_html_to_pdf(html: str, pdf_path: Path) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise RuntimeError(
            "Playwright not installed. Run setup.sh / setup.ps1, then "
            "`python3 -m playwright install chromium`."
        )
    import tempfile
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", suffix=".html", delete=False, encoding="utf-8") as tf:
        tf.write(html)
        html_path = Path(tf.name)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            try:
                page = browser.new_page()
                page.goto(f"file://{html_path}", wait_until="load", timeout=30000)
                page.pdf(
                    path=str(pdf_path),
                    format="Letter",
                    print_background=True,
                    margin={"top": "0.5in", "bottom": "0.5in", "left": "0.6in", "right": "0.6in"},
                )
            finally:
                browser.close()
    finally:
        html_path.unlink(missing_ok=True)


def _render_url_to_pdf(url: str, pdf_path: Path) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise RuntimeError(
            "Playwright not installed. Run setup.sh / setup.ps1, then "
            "`python3 -m playwright install chromium`."
        )
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.goto(url, wait_until="networkidle", timeout=45000)
            page.evaluate(
                "document.querySelectorAll("
                "'header, footer, nav, .header, .footer, .nav, "
                "[data-testid=\"header\"], [data-testid=\"footer\"], "
                ".cookie-banner, .cookie-consent').forEach(el => el.remove());"
            )
            page.pdf(
                path=str(pdf_path),
                format="Letter",
                print_background=True,
                margin={"top": "0.5in", "bottom": "0.5in", "left": "0.6in", "right": "0.6in"},
            )
        finally:
            browser.close()


def _render_corpus_section_pdf(filename: str, anchor: str | None) -> tuple[Path, dict[str, Any]]:
    section = _resolve_corpus_section(filename, anchor)
    key = _hash_key(
        "corpus", filename, section["anchor"],
        str(section["byte_start"]), str(section["byte_end"]),
    )
    pdf_path = RENDERED_DIR / f"{key}.pdf"
    if not pdf_path.exists():
        banner = (
            f'<div class="source-banner">📄 <strong>{filename}</strong> · '
            f'{section["anchor"]} · classification: {section["classification"]}</div>'
        )
        content = _markdown_to_html(section["text"])
        html = _DOC_HTML.format(
            title=f"{filename} — {section['anchor']}",
            banner=banner, content=content,
        )
        _render_html_to_pdf(html, pdf_path)
    return pdf_path, section


def _render_url_pdf(url: str) -> tuple[Path, dict[str, Any]]:
    key = _hash_key("url", url)
    pdf_path = RENDERED_DIR / f"{key}.pdf"
    if not pdf_path.exists():
        _render_url_to_pdf(url, pdf_path)
    return pdf_path, {"source_url": url, "classification": "verify-required"}


_COMMENT_REF_RE = re.compile(r"^(?P<owner>[^/]+)/(?P<repo>[^#]+)#(?P<num>\d+)(?:::comment_(?P<cid>\d+))?$")


def _render_issue_comment_pdf(source_ref: str) -> tuple[Path, dict[str, Any]]:
    m = _COMMENT_REF_RE.match(source_ref.strip())
    if not m:
        raise ValueError(f"Unrecognized issue source ref: {source_ref}")
    owner, repo, num, comment_id = m.group("owner"), m.group("repo"), m.group("num"), m.group("cid")
    facts = _load_facts(f"{owner}/{repo}#{num}")

    if comment_id:
        comment = next(
            (c for c in facts.get("comments", []) if str(c.get("id")) == comment_id),
            None,
        )
        if not comment:
            raise KeyError(f"Comment {comment_id} not found in {source_ref}")
        body_md = comment.get("body", "")
        author = comment.get("author", "(unknown)")
        timestamp = comment.get("created_at", "")
        item_url = comment.get("url", facts.get("url"))
        item_label = "Comment"
    else:
        body_md = facts.get("body", "") or ""
        author = facts.get("author", "(unknown)")
        timestamp = facts.get("created_at", "")
        item_url = facts.get("url")
        item_label = "Issue body"

    body_hash = hashlib.sha256(body_md.encode("utf-8")).hexdigest()
    key = _hash_key("issue", source_ref, body_hash)
    pdf_path = RENDERED_DIR / f"{key}.pdf"

    if not pdf_path.exists():
        banner_html = (
            f'<div class="issue-banner">'
            f'<div class="title">{facts.get("title", "")}</div>'
            f'<div class="meta">{facts["ref"]} · {item_label} · {timestamp}<br>'
            f'<a href="{item_url}">{item_url}</a></div>'
            f'</div>'
        )
        content_html = (
            f'<div class="comment">'
            f'<div class="comment-header"><span class="comment-author">@{author}</span> '
            f'commented on {timestamp}</div>'
            f'<div class="comment-body">{_markdown_to_html(body_md)}</div>'
            f'</div>'
        )
        html = _COMMENT_HTML.format(title=source_ref, banner=banner_html, content=content_html)
        _render_html_to_pdf(html, pdf_path)

    return pdf_path, {
        "source_url": item_url,
        "classification": "github-public",
        "ref": source_ref,
    }


def _render_source_pdf(source_ref: str) -> tuple[Path, dict[str, Any]]:
    """Dispatcher: chooses the right renderer based on source_ref shape."""
    ref = source_ref.strip()
    if ref.startswith(("http://", "https://")):
        return _render_url_pdf(ref)
    if _COMMENT_REF_RE.match(ref):
        return _render_issue_comment_pdf(ref)
    if "#" in ref:
        filename, anchor = ref.split("#", 1)
        return _render_corpus_section_pdf(filename.strip(), anchor.strip())
    if ref.endswith(".md"):
        return _render_corpus_section_pdf(ref, None)
    if ref.startswith("manual:"):
        raise ValueError(
            "manual: source refs cannot be screenshotted yet — "
            "save the raw text to a markdown file in the corpus and refresh-corpus."
        )
    raise ValueError(f"Unrecognized source_ref shape: {ref}")


def _quote_search_candidates(quote: str) -> list[str]:
    """Progressively shorter search strings — falls back when the full quote
    doesn't match because of soft hyphens, smart quotes, or wrapping."""
    quote = quote.strip()
    candidates = [quote]
    sentences = [s.strip() for s in re.split(r"(?<=[.;])\s+", quote) if len(s.strip()) > 20]
    candidates.extend(sentences)
    if len(quote) > 80:
        head = quote[:80].rsplit(" ", 1)[0]
        if head and head not in candidates:
            candidates.append(head)
    seen: set[str] = set()
    out: list[str] = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return out


def _render_pdf_region(doc, pg_idx: int, hits: list, context_padding: int, zoom: float):
    import fitz
    from PIL import Image, ImageDraw
    page = doc[pg_idx]
    page_rect = page.rect
    all_rects = [h for _, h in hits]
    min_y = min(r.y0 for r in all_rects)
    max_y = max(r.y1 for r in all_rects)
    crop_rect = fitz.Rect(
        page_rect.x0 + 12,
        max(page_rect.y0, min_y - context_padding),
        page_rect.x1 - 12,
        min(page_rect.y1, max_y + context_padding),
    )
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=crop_rect)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    draw = ImageDraw.Draw(img, "RGBA")
    pad = max(2, round(2 * zoom))
    for _anchor, rect in hits:
        if rect.y0 >= crop_rect.y0 - 5 and rect.y1 <= crop_rect.y1 + 5:
            x0 = (rect.x0 - crop_rect.x0) * zoom
            y0 = (rect.y0 - crop_rect.y0) * zoom
            x1 = (rect.x1 - crop_rect.x0) * zoom
            y1 = (rect.y1 - crop_rect.y0) * zoom
            draw.rectangle([x0 - pad, y0 - pad, x1 + pad, y1 + pad], fill=(255, 255, 0, 110))
    ImageDraw.Draw(img).rectangle(
        [0, 0, img.width - 1, img.height - 1], outline=(160, 160, 160), width=2,
    )
    return img


def _screenshot_quote(pdf_path: Path, quote: str, png_path: Path,
                      context_padding: int = 30, dpi: int = 200) -> dict[str, Any]:
    """Find the verbatim quote in the rendered PDF and write a highlighted PNG."""
    try:
        import fitz
        from PIL import Image, ImageDraw
    except ImportError:
        return {"ok": False, "reason": "pymupdf or pillow not installed (run setup.sh)"}

    doc = fitz.open(str(pdf_path))
    try:
        candidates = _quote_search_candidates(quote)
        page_hits: dict[int, list] = {}
        anchor_used: str | None = None
        tried: list[str] = []
        for anchor in candidates:
            tried.append(anchor[:80])
            for pg_idx in range(doc.page_count):
                page = doc[pg_idx]
                hits = page.search_for(anchor)
                if hits:
                    page_hits.setdefault(pg_idx, []).extend([(anchor, h) for h in hits])
            if page_hits:
                anchor_used = anchor
                break

        if not page_hits:
            return {
                "ok": False,
                "reason": "quote text not found in rendered source",
                "anchors_tried": tried[:5],
            }

        zoom = dpi / 72
        pages_used = sorted(page_hits.keys())
        images = [
            _render_pdf_region(doc, pg, page_hits[pg], context_padding, zoom)
            for pg in pages_used
        ]
        if len(images) == 1:
            final_img = images[0]
        else:
            total_h = sum(im.height for im in images) + 6 * (len(images) - 1)
            max_w = max(im.width for im in images)
            final_img = Image.new("RGB", (max_w, total_h), (255, 255, 255))
            y = 0
            for im in images:
                final_img.paste(im, (0, y))
                y += im.height + 6
            ImageDraw.Draw(final_img).rectangle(
                [0, 0, final_img.width - 1, final_img.height - 1],
                outline=(160, 160, 160), width=2,
            )
        png_path.parent.mkdir(parents=True, exist_ok=True)
        final_img.save(png_path, format="PNG")
        return {
            "ok": True,
            "png": str(png_path),
            "pages": [p + 1 for p in pages_used],
            "anchor_used": anchor_used[:80] if anchor_used else None,
            "size": list(final_img.size),
        }
    finally:
        doc.close()


def _screenshot_for_quote(quote: str, source_ref: str, png_path: Path) -> dict[str, Any]:
    """End-to-end: render source PDF (cached), then crop+highlight PNG for quote."""
    pdf_path, meta = _render_source_pdf(source_ref)
    result = _screenshot_quote(pdf_path, quote, png_path)
    result["source_pdf"] = str(pdf_path)
    result["source_meta"] = meta
    return result


# --- subcommand: screenshot --------------------------------------------------

def cmd_screenshot(args: argparse.Namespace) -> int:
    out = Path(args.output).expanduser().resolve()
    try:
        result = _screenshot_for_quote(args.quote, args.source, out)
    except (ValueError, KeyError, FileNotFoundError, RuntimeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, indent=2))
    elif result.get("ok"):
        print(f"✓ Wrote {out}  (pages: {result.get('pages')}, size: {result.get('size')})")
    else:
        print(f"✗ {result.get('reason')}", file=sys.stderr)
        if "anchors_tried" in result:
            for a in result["anchors_tried"]:
                print(f"    tried: {a!r}", file=sys.stderr)
    return 0 if result.get("ok") else 2


# --- subcommand: build -------------------------------------------------------

@dataclasses.dataclass
class CardQuote:
    label: str          # e.g. "LEGAL PROVISION", "GITHUB COMMITMENT", "PRODUCT FACT"
    quote: str          # verbatim text
    source_ref: str     # filename.md#Anchor or URL or owner/repo#N::comment_id
    classification: str  # public-law | public-guidance | github-public | github-internal | verify-required
    verified: bool      # set true only after cmd_verify succeeded


def _risk_emoji(tier: str) -> str:
    return {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(tier.lower(), "⚪")


def cmd_build(args: argparse.Namespace) -> int:
    try:
        from docx import Document
        from docx.shared import Pt, Inches, RGBColor
        from docx.enum.text import WD_ALIGN_PARAGRAPH
    except ImportError:
        print("error: python-docx not installed. Run setup.sh / setup.ps1.", file=sys.stderr)
        return 3

    cards_path = Path(args.cards).expanduser().resolve()
    if not cards_path.exists():
        print(f"error: cards file not found: {cards_path}", file=sys.stderr)
        return 1
    cards = json.loads(cards_path.read_text(encoding="utf-8"))

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    doc = Document()
    title = doc.add_heading(cards.get("title", "Citation Cards"), level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    if subtitle := cards.get("subtitle"):
        para = doc.add_paragraph(subtitle)
        para.runs[0].italic = True

    doc.add_paragraph(
        "This document was generated by cite-check. Each Citation Card anchors a "
        "flagged risk in verbatim quotes from the cited legal source(s) and the "
        "product fact. Quotes shown were byte-for-byte verified against their "
        "sources before this document was written, then captured from the rendered "
        "source with the cited language highlighted in yellow. Quotes tagged "
        "[VERIFY] were fetched from the public web and should be confirmed against "
        "the canonical source. This is a drafting aid — not final legal advice."
    )
    doc.add_paragraph()

    risks = cards.get("risks") or []
    refusals: list[str] = []
    render_failures: list[str] = []
    no_screenshot = bool(args.no_screenshots)
    img_width = Inches(float(args.image_width)) if args.image_width else Inches(6.0)

    for i, risk in enumerate(risks, start=1):
        tier = risk.get("tier", "medium")
        heading = doc.add_heading(
            f"{_risk_emoji(tier)} RISK {i} of {len(risks)} — {risk.get('summary', 'Untitled risk')}",
            level=1,
        )
        heading.runs[0].font.color.rgb = RGBColor(0x20, 0x20, 0x20)

        for q in risk.get("quotes", []):
            if not q.get("verified"):
                refusals.append(
                    f"Risk {i} ({risk.get('summary', '')}) — quote labeled '{q.get('label')}' "
                    f"is not marked verified. Run `cite.py verify` first and set verified=true."
                )
                continue

            block = doc.add_paragraph()
            run = block.add_run(f"[{q.get('label', 'SOURCE').upper()}]")
            run.bold = True
            run.font.size = Pt(10)

            tag_bits = []
            if q.get("classification") == "verify-required":
                tag_bits.append("[VERIFY]")
            if q.get("classification") == "github-internal":
                tag_bits.append("[INTERNAL CONTEXT — background only]")
            if tag_bits:
                tag_run = block.add_run("   " + "  ".join(tag_bits))
                tag_run.italic = True
                tag_run.font.size = Pt(9)

            screenshot_ok = False
            source_ref = q.get("source_ref", "")
            if not no_screenshot and source_ref:
                png_path = RENDERED_DIR / "shots" / f"risk{i}_{_hash_key(source_ref, q.get('quote',''))}.png"
                try:
                    print(f"  rendering screenshot: risk {i} · {q.get('label','')} · {source_ref[:60]}", file=sys.stderr)
                    shot = _screenshot_for_quote(q.get("quote", ""), source_ref, png_path)
                    if shot.get("ok"):
                        pic_para = doc.add_paragraph()
                        pic_para.add_run().add_picture(str(png_path), width=img_width)
                        screenshot_ok = True
                    else:
                        render_failures.append(
                            f"Risk {i} · {q.get('label','')} · {source_ref}: {shot.get('reason')}"
                        )
                except Exception as e:  # noqa: BLE001 — render failure must not abort the whole build
                    render_failures.append(
                        f"Risk {i} · {q.get('label','')} · {source_ref}: {type(e).__name__}: {e}"
                    )

            if not screenshot_ok:
                quote_para = doc.add_paragraph(style="Intense Quote")
                quote_para.add_run(q.get("quote", "").strip())
                if not no_screenshot and source_ref:
                    note = doc.add_paragraph()
                    note_run = note.add_run("(screenshot unavailable — verbatim text shown above)")
                    note_run.italic = True
                    note_run.font.size = Pt(8)
            else:
                # Always print the verbatim text below the screenshot for searchability
                vt = doc.add_paragraph()
                vt_label = vt.add_run("Verbatim quote: ")
                vt_label.bold = True
                vt_label.font.size = Pt(9)
                vt_text = vt.add_run(q.get("quote", "").strip())
                vt_text.font.size = Pt(9)

            src_para = doc.add_paragraph()
            src_run = src_para.add_run(f"Source: {source_ref or '(unknown)'}")
            src_run.italic = True
            src_run.font.size = Pt(9)

        if nexus := risk.get("nexus"):
            p = doc.add_paragraph()
            p.add_run("[NEXUS] ").bold = True
            p.add_run(nexus)

        if action := risk.get("action"):
            p = doc.add_paragraph()
            p.add_run("[RECOMMENDED ACTION] ").bold = True
            p.add_run(action)

        doc.add_paragraph()
        doc.add_paragraph("─" * 60)

    if refusals or render_failures:
        doc.add_page_break()
        if refusals:
            doc.add_heading("Refusals (verification not satisfied)", level=1)
            for r in refusals:
                doc.add_paragraph(r, style="List Bullet")
        if render_failures:
            doc.add_heading("Screenshot render notes", level=1)
            for r in render_failures:
                doc.add_paragraph(r, style="List Bullet")
        if refusals:
            print("warning: some quotes were not verified — see Refusals page in the output document.", file=sys.stderr)
            if args.strict:
                print("strict mode: refusing to write output with unverified quotes.", file=sys.stderr)
                return 2

    doc.save(output)
    print(f"✓ Wrote {output}")
    print(f"  risks: {len(risks)}, refusals: {len(refusals)}, render notes: {len(render_failures)}")
    return 0


# --- subcommand: pressure-test ----------------------------------------------
#
# Pressure-test mode is the inverse of build:
#   build      — agent assembles a Citation Card from scratch
#   pressure-test — agent has ALREADY done a review and wants to validate that
#                   each flagged risk is actually backed by (a) verbatim legal
#                   text from a public source, (b) verbatim product facts from
#                   the issue, and (c) sources that are publicly citable
#                   under the product-counsel agent's "public sources only"
#                   constraint (so internal-only refs are flagged).
#
# Input is a small JSON spec the agent assembles by reading its own in-session
# review output. Schema:
#
#   {
#     "review_target": "github/product-and-privacy-legal#2398",
#     "review_summary": "<optional one-line summary of the review>",
#     "risks": [
#       {
#         "id": "2.1",
#         "label": "Cross-border data transfers",
#         "tier": "medium",
#         "claim": "<the risk statement from the review>",
#         "asserted_legal_sources": [
#           {"label": "GDPR Art. 46", "ref": "03-reg-gdpr.md#Article 46",
#            "quote": "<verbatim text the review relies on, OPTIONAL>"}
#         ],
#         "asserted_product_facts": [
#           {"label": "kayreiman comment", "ref": "owner/repo#N::comment_<id>",
#            "quote": "<verbatim quote the review relies on>"}
#         ]
#       }
#     ]
#   }
#
# A source is allowed as a primary citation only if its classification is one
# of {public-law, public-guidance, github-public, verify-required}.
# `github-internal` refs (02-internal-* and 07-process-* and any unknown
# repo-internal source) are downgraded to "background only" with a ⚠ flag.

_PUBLIC_PRIMARY_CLASSES = {"public-law", "public-guidance", "github-public", "verify-required"}

# Default freshness window for the cached authoritative-source copies. When a
# pressure-test run consults a cached auth source older than this, it surfaces
# a warning ("authoritative source is N days old; consider running
# refresh-authoritative") so reviewers know they're verifying against
# potentially stale data — without blocking the run.
_AUTH_FRESHNESS_DAYS_DEFAULT = 30.0


def _classify_ref_for_pressure_test(ref: str) -> str:
    """Return the classification cite-check would assign to this ref, for
    the public-source policy check. Mirrors the dispatcher used by
    _resolve_source_text but doesn't fetch — it just tells us the class."""
    ref = ref.strip()
    if ref.startswith(("http://", "https://")):
        return "verify-required"
    if _COMMENT_REF_RE.match(ref):
        return "github-public"
    filename = ref.split("#", 1)[0].strip() if "#" in ref else ref
    return _classification_for(filename)


def _check_one_quote(
    ref: str,
    quote: Optional[str],
    *,
    auth_freshness_days: float = _AUTH_FRESHNESS_DAYS_DEFAULT,
) -> dict[str, Any]:
    """Resolve one source ref and (optionally) verify a quote against it.

    Verification is *authoritative-first*: when the ref points to a corpus
    file that has an authoritative public source cached locally (via
    `refresh-authoritative`), the quote is verified against that source. The
    cached corpus mirror is consulted only when no authoritative copy is
    available.

    Returns a dict with: ref, classification, source_url, resolved (bool),
    error (if any), quote_provided (bool), quote_verified (bool|None),
    authoritative_url (str|None), authoritative_verified (bool|None),
    verified_against ('authoritative' | 'mirror' | None),
    auth_age_days (float|None), auth_stale (bool).
    """
    out: dict[str, Any] = {
        "ref": ref,
        "classification": _classify_ref_for_pressure_test(ref),
        "source_url": None,
        "resolved": False,
        "error": None,
        "quote_provided": bool(quote and quote.strip()),
        "quote_verified": None,
        "authoritative_url": None,
        "authoritative_verified": None,
        "verified_against": None,
        "auth_age_days": None,
        "auth_stale": False,
    }
    try:
        source = _resolve_source_text(ref)
    except Exception as e:  # noqa: BLE001 — pressure-test must never crash on a bad ref
        out["error"] = f"{type(e).__name__}: {e}"
        msg = str(e).lower()
        if ref.startswith("https://github.com/") and ("404" in msg or "not found" in msg):
            out["classification"] = "github-internal"
            out["error"] = (
                f"{type(e).__name__}: not reachable unauthenticated — likely "
                f"a private or internal GitHub resource"
            )
        return out
    out["resolved"] = True
    out["source_url"] = source["source_url"]
    out["classification"] = source["classification"]

    auth_text: Optional[str] = None
    auth_meta: Optional[dict[str, Any]] = None
    corpus_filename = ref.split("#", 1)[0] if not ref.startswith("http") and "::" not in ref else None
    if corpus_filename:
        auth_meta = _authoritative_meta_for(corpus_filename)
        if auth_meta:
            out["authoritative_url"] = auth_meta.get("authoritative_url")
            auth_text = _load_auth_text(corpus_filename)
            age = _auth_age_days(corpus_filename)
            if age is not None:
                out["auth_age_days"] = round(age, 1)
                if age > auth_freshness_days:
                    out["auth_stale"] = True

    if quote and quote.strip():
        q_norm = _normalize_for_match(quote)
        mirror_match = q_norm in _normalize_for_match(source["text"])
        if auth_text is not None:
            auth_match = q_norm in _normalize_for_match(auth_text)
            out["authoritative_verified"] = auth_match
            out["quote_verified"] = auth_match
            out["verified_against"] = "authoritative"
            if not auth_match and mirror_match:
                out["error"] = (
                    "quote present in cached mirror but NOT in authoritative source — "
                    "either the mirror has drifted or the quote was paraphrased"
                )
        else:
            out["quote_verified"] = mirror_match
            out["verified_against"] = "mirror"
            if auth_meta and auth_meta.get("authoritative_url"):
                out["error"] = (
                    "verified against cached mirror only — authoritative source "
                    "not yet fetched (run `cite.py refresh-authoritative`)"
                )
    return out


def _pressure_test_one_risk(
    risk: dict[str, Any],
    *,
    auth_freshness_days: float = _AUTH_FRESHNESS_DAYS_DEFAULT,
) -> dict[str, Any]:
    legal = risk.get("asserted_legal_sources") or []
    facts = risk.get("asserted_product_facts") or []

    legal_results = [
        _check_one_quote(r.get("ref", ""), r.get("quote"), auth_freshness_days=auth_freshness_days)
        for r in legal
    ]
    fact_results = [
        _check_one_quote(r.get("ref", ""), r.get("quote"), auth_freshness_days=auth_freshness_days)
        for r in facts
    ]

    # Compute per-dimension status
    legal_status, legal_notes = _grade_dimension(
        legal_results,
        legal,
        category="legal",
        require_verified_quote=True,
        auth_freshness_days=auth_freshness_days,
    )
    fact_status, fact_notes = _grade_dimension(
        fact_results,
        facts,
        category="fact",
        require_verified_quote=True,
        auth_freshness_days=auth_freshness_days,
    )
    public_status, public_notes = _grade_public_sources(legal_results + fact_results, legal, facts)

    overall = "PASS"
    if legal_status == "fail" or fact_status == "fail":
        overall = "FAIL"
    elif legal_status == "warn" or fact_status == "warn" or public_status == "warn":
        overall = "WARN"

    return {
        "id": risk.get("id"),
        "label": risk.get("label"),
        "tier": risk.get("tier"),
        "claim": risk.get("claim"),
        "overall": overall,
        "legal": {"status": legal_status, "notes": legal_notes, "results": legal_results},
        "fact": {"status": fact_status, "notes": fact_notes, "results": fact_results},
        "public_sources": {"status": public_status, "notes": public_notes},
    }


def _grade_dimension(
    results: list[dict[str, Any]],
    spec: list[dict[str, Any]],
    *,
    category: str,
    require_verified_quote: bool,
    auth_freshness_days: float = _AUTH_FRESHNESS_DAYS_DEFAULT,
) -> tuple[str, list[str]]:
    """Return (status, notes) for the legal or fact dimension.

    status ∈ {"pass", "warn", "fail"}.

    Verification badges:
      ✓✓  quote verified against the authoritative public source
      ✓   quote verified against the cached mirror only (no auth source, or
          auth source unreachable; this is the legitimate state for facts and
          for github-public docs that are themselves the authoritative source)
      ⚠   quote present in the mirror but NOT in the authoritative source
          (corpus drift) — graded as warn, not fail, but flagged loudly
    """
    notes: list[str] = []
    if not spec:
        notes.append(f"no {category} sources cited in the review")
        return "fail", notes

    has_unresolved = False
    has_unverified = False
    has_no_quote = False
    has_corpus_drift = False
    has_stale_auth = False
    for r, s in zip(results, spec):
        label = s.get("label") or r["ref"]
        if not r["resolved"]:
            has_unresolved = True
            notes.append(f"✗ {label} — could not resolve ref `{r['ref']}` ({r['error']})")
            continue
        if not r["quote_provided"]:
            if require_verified_quote:
                has_no_quote = True
                notes.append(
                    f"⚠ {label} — ref resolves but no verbatim quote provided; "
                    f"the reviewer is relying on the source generically"
                )
            else:
                notes.append(f"✓ {label} — ref resolves at {r['source_url']}")
            continue

        verified_against = r.get("verified_against")
        auth_url = r.get("authoritative_url")
        if r["quote_verified"]:
            if verified_against == "authoritative":
                notes.append(
                    f"✓✓ {label} — verbatim quote verified against authoritative source ({auth_url})"
                )
                if r.get("auth_stale"):
                    has_stale_auth = True
                    age = r.get("auth_age_days")
                    age_str = f"{age:.1f}d" if isinstance(age, (int, float)) else "unknown"
                    corpus_filename = r.get("ref", "").split("#", 1)[0]
                    notes.append(
                        f"  ⚠ authoritative copy is {age_str} old (threshold: {auth_freshness_days:g}d) — "
                        f"re-fetch with `cite.py refresh-authoritative --only {corpus_filename} --force` "
                        f"to confirm the publisher hasn't amended the source since"
                    )
            else:
                # mirror-only verification
                if auth_url:
                    has_no_quote = True  # treat as warn so reviewer knows to refresh-authoritative
                    notes.append(
                        f"⚠ {label} — quote verified against cached mirror only; "
                        f"authoritative source not yet fetched (run `cite.py refresh-authoritative`). "
                        f"Source: {r['source_url']}"
                    )
                else:
                    notes.append(
                        f"✓ {label} — verbatim quote present in {r['source_url']} "
                        f"(no authoritative source applies — this ref *is* the publisher copy)"
                    )
        else:
            # quote was not verified
            if verified_against == "authoritative" and r.get("error", "").startswith("quote present in cached mirror"):
                # corpus drift: mirror has it, authoritative doesn't
                has_corpus_drift = True
                notes.append(
                    f"⚠ {label} — quote is in the cached mirror but NOT in the authoritative "
                    f"source ({auth_url}). This is corpus drift: the mirror may be stale or the "
                    f"quote may have been paraphrased. Run `cite.py verify-corpus` for details."
                )
            else:
                has_unverified = True
                notes.append(
                    f"✗ {label} — quote NOT found verbatim in source "
                    f"({r['source_url']}); reviewer may be paraphrasing or misciting"
                )

    if has_unresolved or has_unverified:
        return "fail", notes
    if has_no_quote or has_corpus_drift or has_stale_auth:
        return "warn", notes
    return "pass", notes


def _grade_public_sources(
    all_results: list[dict[str, Any]],
    legal_spec: list[dict[str, Any]],
    fact_spec: list[dict[str, Any]],
) -> tuple[str, list[str]]:
    """Apply the product-counsel "public sources only" policy.

    Operates on the *legal* spec results only — facts can come from internal
    GitHub sources (the issue itself) without violating the policy. For each
    legal anchor, classify by the resolved classification when available, or
    by the heuristic in `_check_one_quote` when the source couldn't be reached.
    """
    notes: list[str] = []
    has_warn = False
    legal_specs_with_results = list(zip(legal_spec, all_results[: len(legal_spec)]))
    for spec, r in legal_specs_with_results:
        cls = r["classification"]
        label = spec.get("label") or r["ref"]
        if cls not in _PUBLIC_PRIMARY_CLASSES:
            has_warn = True
            reachable = "" if r["resolved"] else " (also unreachable: " + (r["error"] or "") + ")"
            notes.append(
                f"⚠ Legal anchor `{label}` is `{cls}`{reachable} — "
                f"may be used only as background context, NOT as the basis for the "
                f"legal conclusion (per product-counsel agent constraint)"
            )
        elif cls == "verify-required":
            notes.append(
                f"ℹ Legal anchor `{label}` is web-fetched (`verify-required`) — "
                f"append [VERIFY] tag in the final review text"
            )
    if not notes:
        notes.append("✓ all primary legal sources are publicly citable")
    return ("warn" if has_warn else "pass"), notes


def _format_pressure_test_report(report: dict[str, Any]) -> str:
    lines: list[str] = []
    target = report.get("review_target", "(unspecified)")
    lines.append(f"# Pressure-test report — {target}\n")
    if report.get("review_summary"):
        lines.append(f"_Review summary:_ {report['review_summary']}\n")

    summary_pass = sum(1 for r in report["risks"] if r["overall"] == "PASS")
    summary_warn = sum(1 for r in report["risks"] if r["overall"] == "WARN")
    summary_fail = sum(1 for r in report["risks"] if r["overall"] == "FAIL")
    total = len(report["risks"])
    lines.append(
        f"**{total} risks tested** · ✓ {summary_pass} hold up · "
        f"⚠ {summary_warn} with warnings · ✗ {summary_fail} with gaps\n"
    )

    for risk in report["risks"]:
        glyph = {"PASS": "✓", "WARN": "⚠", "FAIL": "✗"}[risk["overall"]]
        tier = (risk.get("tier") or "").upper()
        lines.append(f"## {glyph} RISK {risk.get('id') or ''} — {risk.get('label') or '(unlabeled)'} ({tier})  →  {risk['overall']}")
        if risk.get("claim"):
            lines.append(f"_Claim:_ {risk['claim']}\n")

        for dim_name, dim in (("Legal anchor", risk["legal"]),
                              ("Product fact", risk["fact"]),
                              ("Public-source policy", risk["public_sources"])):
            badge = {"pass": "✓", "warn": "⚠", "fail": "✗"}[dim["status"]]
            lines.append(f"  - **{badge} {dim_name}** ({dim['status']})")
            for note in dim["notes"]:
                lines.append(f"    - {note}")
        lines.append("")

    fails = [r for r in report["risks"] if r["overall"] == "FAIL"]
    warns = [r for r in report["risks"] if r["overall"] == "WARN"]
    if fails or warns:
        lines.append("## Suggested follow-ups")
        for r in fails:
            lines.append(f"- Risk {r.get('id') or ''} ({r.get('label') or ''}): resolve the ✗ items above before relying on this risk in the final review.")
        for r in warns:
            lines.append(f"- Risk {r.get('id') or ''} ({r.get('label') or ''}): pin a verbatim quote for any ⚠ items, and confirm the public-source classification of any background refs.")
    else:
        lines.append("All flagged risks are anchored by verbatim, publicly-citable text on both the legal and factual sides. The review holds up.")

    return "\n".join(lines)


def cmd_pressure_test(args: argparse.Namespace) -> int:
    spec_path = Path(args.spec).expanduser()
    if not spec_path.exists():
        print(f"error: spec file not found: {spec_path}", file=sys.stderr)
        return 1
    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"error: spec is not valid JSON: {e}", file=sys.stderr)
        return 1

    risks_in = spec.get("risks") or []
    if not risks_in:
        print("error: spec has no `risks` to test", file=sys.stderr)
        return 1

    # Optional filter by --risk-id (one or many)
    if args.risk_id:
        wanted = set(args.risk_id)
        risks_in = [r for r in risks_in if r.get("id") in wanted]
        if not risks_in:
            print(f"error: no risks in spec match --risk-id {sorted(wanted)}", file=sys.stderr)
            return 1

    auth_freshness_days = getattr(args, "auth_freshness_days", _AUTH_FRESHNESS_DAYS_DEFAULT)
    report = {
        "review_target": spec.get("review_target"),
        "review_summary": spec.get("review_summary"),
        "auth_freshness_days": auth_freshness_days,
        "risks": [
            _pressure_test_one_risk(r, auth_freshness_days=auth_freshness_days)
            for r in risks_in
        ],
    }

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(_format_pressure_test_report(report))

    # Exit code reflects the worst outcome:
    #   0 = all PASS
    #   1 = at least one WARN, no FAIL
    #   2 = at least one FAIL
    if any(r["overall"] == "FAIL" for r in report["risks"]):
        return 2
    if any(r["overall"] == "WARN" for r in report["risks"]):
        return 1
    return 0


# --- entrypoint --------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cite", description=__doc__.strip().splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("setup-check", help="verify Python deps and gh CLI")
    sp.set_defaults(func=cmd_setup_check)

    sp = sub.add_parser("refresh-corpus", help="mirror the legal reference library into the local cache")
    sp.add_argument("--only", nargs="*", help="optional subset of filenames to refresh")
    sp.set_defaults(func=cmd_refresh_corpus)

    sp = sub.add_parser(
        "refresh-authoritative",
        help="fetch the official public source for every cached file and store it for verification",
    )
    sp.add_argument("--only", nargs="*", help="optional subset of filenames to refresh")
    sp.add_argument("--force", action="store_true", help="re-fetch even if a cached copy already exists")
    sp.add_argument("--delay", type=float, default=1.0, help="seconds to sleep between requests (default: 1.0)")
    sp.set_defaults(func=cmd_refresh_authoritative)

    sp = sub.add_parser(
        "verify-corpus",
        help="diff every cached corpus file against its authoritative public source; exit 1 on drift",
    )
    sp.add_argument("--only", nargs="*", help="optional subset of filenames to check")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_verify_corpus)

    sp = sub.add_parser("list-corpus", help="show the current cache state")
    sp.add_argument("--file", help="show every section anchor in this cached file")
    sp.set_defaults(func=cmd_list_corpus)

    sp = sub.add_parser("extract-source", help="resolve a citation reference to verbatim text")
    sp.add_argument("--ref", required=True, help="e.g. '03-reg-eu-gdpr.md#Article 6' or a public URL")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_extract_source)

    sp = sub.add_parser("extract-facts", help="pull a GitHub issue (body + comments) into a structured fact corpus")
    sp.add_argument("--issue", required=True, help="owner/repo#N")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_extract_facts)

    sp = sub.add_parser("verify", help="byte-for-byte check that a quote appears in a source (exit 2 if not)")
    sp.add_argument("--quote", required=True)
    sp.add_argument("--source", required=True, help="filename.md#Anchor or URL")
    sp.add_argument("--strict", action="store_true", help="exact byte match (default: whitespace-normalized)")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_verify)

    sp = sub.add_parser("screenshot", help="render one quote → highlighted PNG (for testing/debugging)")
    sp.add_argument("--quote", required=True)
    sp.add_argument("--source", required=True, help="filename.md#Anchor, owner/repo#N[::comment_<id>], or URL")
    sp.add_argument("--output", required=True, help="output .png path")
    sp.add_argument("--json", action="store_true")
    sp.set_defaults(func=cmd_screenshot)

    sp = sub.add_parser("build", help="render Citation Cards to a Word document")
    sp.add_argument("--cards", required=True, help="path to a JSON cards file (see SKILL.md for schema)")
    sp.add_argument("--output", required=True, help="output .docx path")
    sp.add_argument("--strict", action="store_true", help="refuse to write output if any quotes are unverified")
    sp.add_argument("--no-screenshots", action="store_true", help="skip screenshot rendering; emit text-only quote blocks")
    sp.add_argument("--image-width", type=float, default=6.0, help="screenshot width in inches (default: 6.0)")
    sp.set_defaults(func=cmd_build)

    sp = sub.add_parser(
        "pressure-test",
        help="validate an existing review: byte-check the cited law and product facts, "
             "and surface gaps in the legal/factual anchoring",
    )
    sp.add_argument("--spec", required=True, help="path to a JSON pressure-test spec (see SKILL.md schema)")
    sp.add_argument("--risk-id", action="append",
                    help="optional: only test these risk ids (can be repeated)")
    sp.add_argument(
        "--auth-freshness-days",
        type=float,
        default=_AUTH_FRESHNESS_DAYS_DEFAULT,
        help=(
            "warn (do not block) when a cited file's authoritative-source cache is "
            f"older than this many days (default: {_AUTH_FRESHNESS_DAYS_DEFAULT:g}). "
            "Use a larger value to silence freshness warnings; use 0 to flag every cite."
        ),
    )
    sp.add_argument("--json", action="store_true", help="emit machine-readable JSON instead of the markdown report")
    sp.set_defaults(func=cmd_pressure_test)

    return p


def main(argv: Optional[list[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args) or 0)
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
