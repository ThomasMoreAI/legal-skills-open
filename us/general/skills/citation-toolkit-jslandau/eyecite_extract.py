#!/usr/bin/env python3
"""
eyecite_extract.py — local citation extraction for the legal-tools skills.

Runs eyecite over a document and emits a JSON array of citations in document
order, with `Id.`/`supra`/short-form references already resolved to their
full-citation antecedents. The output schema is shaped to drop directly into
the structured component schemas defined in citation-toolkit (Cases, Statutes,
etc.) — consuming skills (cite-checking, table-of-authorities, chain-cite)
read this output as authoritative for the citation types eyecite recognizes,
then do a focused manual pass for the known gap categories (administrative
decisions, EU/international cases, popular-name statutes, informal references,
state constitutional provisions).

This is the offline counterpart to the CourtListener MCP's `extract_citations`
tool — both wrap eyecite. Prefer the MCP when it is loaded; reach for this
script when running outside the MCP, or when a skill needs span offsets /
resolution mapping that the MCP wrapper does not expose.

Usage:

    # From a file:
    python3 eyecite_extract.py --input brief.txt

    # From stdin:
    cat brief.txt | python3 eyecite_extract.py

    # With HTML/XML cleaning before extraction:
    python3 eyecite_extract.py --input opinion.html --clean html,inline_whitespace

Output: JSON array on stdout. One object per citation, in document order.
Errors and informational messages go to stderr.

Dependency: `pip install eyecite`. The script imports lazily so `--help` works
without the dependency installed.
"""
import argparse
import json
import sys
from typing import Any


def _load_eyecite():
    try:
        from eyecite import get_citations, resolve_citations, clean_text
        from eyecite.models import (
            FullCaseCitation,
            ShortCaseCitation,
            FullLawCitation,
            FullJournalCitation,
            IdCitation,
            SupraCitation,
            UnknownCitation,
        )
    except ImportError as e:
        sys.stderr.write(
            "ERROR: eyecite is not installed. Install with: pip install eyecite\n"
            f"  (import error: {e})\n"
        )
        sys.exit(2)
    return {
        "get_citations": get_citations,
        "resolve_citations": resolve_citations,
        "clean_text": clean_text,
        "FullCaseCitation": FullCaseCitation,
        "ShortCaseCitation": ShortCaseCitation,
        "FullLawCitation": FullLawCitation,
        "FullJournalCitation": FullJournalCitation,
        "IdCitation": IdCitation,
        "SupraCitation": SupraCitation,
        "UnknownCitation": UnknownCitation,
    }


def _meta(citation, name: str) -> Any:
    md = getattr(citation, "metadata", None)
    if md is None:
        return None
    return getattr(md, name, None)


def _full_case_entry(citation) -> dict:
    g = getattr(citation, "groups", {}) or {}
    return {
        "citation_type": "case",
        "full_citation": citation.matched_text(),
        "source_name": _compose_source_name(_meta(citation, "plaintiff"), _meta(citation, "defendant")),
        "reporter": g.get("reporter"),
        "volume": _to_int(g.get("volume")),
        "start_page": _to_int(g.get("page")),
        "pincite": _split_pin(_meta(citation, "pin_cite")),
        "court": _meta(citation, "court"),
        "year": _to_int(_meta(citation, "year")),
        "parenthetical": _meta(citation, "parenthetical"),
        "span": list(citation.span()),
    }


def _full_law_entry(citation) -> dict:
    g = getattr(citation, "groups", {}) or {}
    return {
        "citation_type": "statute",
        "full_citation": citation.matched_text(),
        "title": _to_int(g.get("title")) or _to_int(g.get("chapter")),
        "code": g.get("reporter"),
        "section": g.get("section"),
        "subsection": g.get("subdivision"),
        "year": _to_int(_meta(citation, "year")),
        "span": list(citation.span()),
    }


def _full_journal_entry(citation) -> dict:
    g = getattr(citation, "groups", {}) or {}
    return {
        "citation_type": "secondary",
        "full_citation": citation.matched_text(),
        "author": _meta(citation, "author"),
        "title": _meta(citation, "title"),
        "journal_or_publisher": g.get("reporter"),
        "volume": _to_int(g.get("volume")),
        "start_page": _to_int(g.get("page")),
        "pincite": _split_pin(_meta(citation, "pin_cite")),
        "year": _to_int(_meta(citation, "year")),
        "span": list(citation.span()),
    }


def _short_or_ref_entry(citation, kind: str, antecedent: dict | None) -> dict:
    return {
        "citation_type": kind,  # "short_case" | "id" | "supra"
        "full_citation": citation.matched_text(),
        "pincite": _split_pin(_meta(citation, "pin_cite")),
        "resolved_to": antecedent,  # antecedent entry from this same array, or None
        "span": list(citation.span()),
    }


def _unknown_entry(citation) -> dict:
    return {
        "citation_type": "unknown",
        "full_citation": citation.matched_text(),
        "span": list(citation.span()),
    }


def _compose_source_name(plaintiff, defendant) -> str | None:
    if plaintiff and defendant:
        return f"{plaintiff} v. {defendant}"
    return plaintiff or defendant or None


def _to_int(value) -> int | None:
    if value is None:
        return None
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def _split_pin(pin_cite) -> list[int]:
    if not pin_cite:
        return []
    pages: list[int] = []
    for chunk in str(pin_cite).replace("–", "-").replace("—", "-").split(","):
        chunk = chunk.strip().lstrip("at ").strip()
        if "-" in chunk:
            chunk = chunk.split("-", 1)[0]
        n = _to_int(chunk)
        if n is not None:
            pages.append(n)
    return pages


def extract(text: str, clean_steps: list[str] | None) -> list[dict]:
    api = _load_eyecite()
    if clean_steps:
        text = api["clean_text"](text, clean_steps)

    citations = api["get_citations"](text)
    citations = sorted(citations, key=lambda c: c.span()[0])

    # Build base entries first so short forms can reference them by index.
    entries: list[dict] = []
    citation_to_index: dict[int, int] = {}
    for idx, c in enumerate(citations):
        citation_to_index[id(c)] = idx
        if isinstance(c, api["FullCaseCitation"]):
            entries.append(_full_case_entry(c))
        elif isinstance(c, api["FullLawCitation"]):
            entries.append(_full_law_entry(c))
        elif isinstance(c, api["FullJournalCitation"]):
            entries.append(_full_journal_entry(c))
        elif isinstance(c, api["ShortCaseCitation"]):
            entries.append(_short_or_ref_entry(c, "short_case", None))
        elif isinstance(c, api["IdCitation"]):
            entries.append(_short_or_ref_entry(c, "id", None))
        elif isinstance(c, api["SupraCitation"]):
            entries.append(_short_or_ref_entry(c, "supra", None))
        elif isinstance(c, api["UnknownCitation"]):
            entries.append(_unknown_entry(c))
        else:
            entries.append({
                "citation_type": "other",
                "full_citation": c.matched_text(),
                "class": type(c).__name__,
                "span": list(c.span()),
            })

    # Resolve short forms / Id / supra to their antecedents.
    resolved = api["resolve_citations"](citations)
    # resolve_citations returns {Resource: [citations...]}. Invert to per-citation antecedent.
    for resource, group in resolved.items():
        # The resource's anchor citation is the earliest FullCase/Law/Journal cite in the group.
        anchor = None
        for c in group:
            if isinstance(c, (api["FullCaseCitation"], api["FullLawCitation"], api["FullJournalCitation"])):
                anchor = c
                break
        if anchor is None:
            continue
        anchor_idx = citation_to_index.get(id(anchor))
        if anchor_idx is None:
            continue
        for c in group:
            if c is anchor:
                continue
            i = citation_to_index.get(id(c))
            if i is None:
                continue
            entry = entries[i]
            # Surface a compact pointer rather than nesting the full antecedent.
            entry["resolved_to"] = {
                "index": anchor_idx,
                "full_citation": entries[anchor_idx]["full_citation"],
            }

    # Flag unresolved short forms so consuming skills see the toolkit's flag vocabulary.
    for entry in entries:
        if entry["citation_type"] in ("short_case", "id", "supra") and not entry.get("resolved_to"):
            entry.setdefault("flags", []).append("unresolved_short_form")

    return entries


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Extract legal citations from text using eyecite. "
                    "Emits a JSON array of toolkit-shaped citation entries on stdout.",
    )
    parser.add_argument("--input", help="Path to input text file. If omitted, read stdin.")
    parser.add_argument(
        "--clean",
        default="",
        help="Comma-separated eyecite cleaners to apply before extraction. "
             "Valid: html, inline_whitespace, all_whitespace, underscores. "
             "Example: --clean html,inline_whitespace",
    )
    args = parser.parse_args(argv)

    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    clean_steps = [s.strip() for s in args.clean.split(",") if s.strip()] or None
    entries = extract(text, clean_steps)
    json.dump(entries, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
