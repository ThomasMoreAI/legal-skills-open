#!/usr/bin/env python3
"""
read_version.py — establish which version of an instrument you actually fetched,
from the publisher's own markers, without a model in the loop.

This is the step the whole skill turns on. Publishers do say which version they
are serving; they say it quietly, beside the text rather than in it, and a
reader who came for Article 6 does not look. EUR-Lex will hand you the original
Official Journal text at the instrument's own canonical address while noting, in
a sidebar, that a consolidated version exists. legislation.gov.uk will tell you
a statute is up to date "on or before" a date that moves daily, and list
elsewhere the amendments not yet written into the words you are reading.

So the markers are read mechanically, from the bytes fetch_source.py saved, using
patterns the jurisdiction registry carries. A model reading a page can miss a
banner; a regex cannot. When a marker says the text is superseded or incomplete,
this exits non-zero, and the run stops rather than quoting.

Severities:
  superseded  the fetched text is not the operative version — stop and refetch
  incomplete  the version is right but known changes are not written into it
  info        a fact the note must carry (revision date, language regime)

Usage:
    python3 read_version.py <source.html> --jurisdiction EU --json version.json
    python3 read_version.py <source.html> --jurisdiction UK --json version.json \
        --historical-effective 2024-01-01 --research-date 2024-06-01

Stdlib only. Exit 0 only when the version is confirmed, or when a superseded
text was explicitly selected for a dated question. Unresolved blocks too.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

from integrity import (
    CONFIRMED,
    HISTORICAL_SELECTED,
    RELIANCE_STATES,
    IntegrityError,
    validate_extraction_input,
    version_state,
)

REGISTRY = Path(__file__).resolve().parent.parent / "references" / "jurisdictions"

DROP_ELEMENTS = re.compile(r"(?is)<(script|style)\b.*?</\1\s*>")
TAG = re.compile(r"(?s)<[^>]+>")
WHITESPACE = re.compile(r"\s+")

STOP_SEVERITIES = {"superseded", "incomplete"}


def load_registry(code: str) -> dict:
    path = REGISTRY / f"{code.lower()}.md"
    if not path.exists():
        available = sorted(
            p.stem.upper() for p in REGISTRY.glob("*.md") if not p.stem.startswith("_")
        )
        sys.exit(
            f"No registry entry for {code.upper()}.\n"
            f"  mapped: {', '.join(available) or 'none'}\n"
            f"  Read {REGISTRY / '_unmapped.md'} and follow it. "
            "Do not guess a publisher."
        )
    fence = re.search(
        r"```json\s*(\{.*?\})\s*```", path.read_text(encoding="utf-8"), re.S
    )
    if not fence:
        sys.exit(f"{path} has no ```json metadata block.")
    return json.loads(fence.group(1))


def to_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() in {".html", ".htm", ".xhtml"}:
        raw = DROP_ELEMENTS.sub(" ", raw)
        raw = TAG.sub(" ", raw)
        raw = html.unescape(raw)
    return WHITESPACE.sub(" ", raw).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("source", type=Path)
    parser.add_argument("--jurisdiction", required=True)
    parser.add_argument(
        "--json", type=Path, required=True, help="write the bound version receipt"
    )
    parser.add_argument(
        "--provenance",
        type=Path,
        help="fetch directory; defaults to the source directory",
    )
    parser.add_argument(
        "--historical-effective",
        help="effective date of intentionally selected historical text",
    )
    parser.add_argument(
        "--research-date", help="dated question for which historical text was selected"
    )
    args = parser.parse_args()

    if not args.source.exists():
        sys.exit(f"No such file: {args.source}")
    if bool(args.historical_effective) != bool(args.research_date):
        sys.exit(
            "Historical selection requires both "
            "--historical-effective and --research-date."
        )
    try:
        chain = validate_extraction_input(
            args.provenance or args.source.parent, args.source
        )
    except IntegrityError as error:
        sys.exit(str(error))
    if chain["instrument"]["jurisdiction"] != args.jurisdiction.strip().upper():
        sys.exit(
            "The requested jurisdiction does not match the saved instrument identity."
        )

    registry = load_registry(args.jurisdiction)
    text = to_text(args.source)

    findings = []
    for marker in registry.get("markers", []):
        match = re.search(marker["pattern"], text, re.I)
        if not match:
            continue
        findings.append(
            {
                "marker": marker["name"],
                "severity": marker["severity"],
                "captured": [g for g in match.groups() if g],
                "matched": WHITESPACE.sub(" ", match.group(0))[:200],
                "note": marker.get("note", ""),
            }
        )

    stopped = [f for f in findings if f["severity"] in STOP_SEVERITIES]
    try:
        state = version_state(findings, args.historical_effective, args.research_date)
    except IntegrityError as error:
        sys.exit(str(error))

    print(f"{registry['name']} — {registry['publisher']}")
    print(f"consolidated text: {registry.get('consolidated_text', 'unknown')}")
    print(
        f"authentic language(s): {', '.join(registry.get('authentic_languages', []))}\n"
    )

    if not findings:
        print("No version markers matched.")
        print(
            "  That is not a clean bill of health — it means this page did not "
            "carry the\n  markers the registry expects. Establish the version by "
            "hand before quoting."
        )
    for finding in findings:
        captured = (
            f"  -> {', '.join(finding['captured'])}" if finding["captured"] else ""
        )
        print(f"[{finding['severity']}] {finding['marker']}{captured}")
        if finding["note"]:
            print(f"    {finding['note']}")

    if args.json.exists():
        sys.exit(f"Refusing to overwrite existing version receipt: {args.json.name}")
    receipt = {
        "jurisdiction": registry["code"],
        "source": args.source.name,
        "state": state,
        "effective_date": args.historical_effective,
        "research_date": args.research_date,
        "findings": findings,
        "integrity": {
            key: chain[key]
            for key in (
                "schema",
                "instrument",
                "publisher_bytes_sha256",
                "extraction_input_sha256",
            )
        },
    }
    args.json.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    if state == HISTORICAL_SELECTED:
        print(
            f"\nUsing historical text effective {args.historical_effective} because "
            f"this research concerns {args.research_date}."
        )
    elif state == CONFIRMED:
        print("\nUsing official text with a confirmed publisher version marker.")
    elif stopped:
        print(
            f"\nSTOP. {len(stopped)} marker(s) say this text is not what you should "
            "be quoting.\nRefetch the version the marker names, or state the gap in "
            "the note. Do not quote\nfrom this file as though it were operative."
        )
    else:
        print("\nI could not confirm the operative text, so I have not relied on it.")
    return 0 if state in RELIANCE_STATES else 1


if __name__ == "__main__":
    raise SystemExit(main())
