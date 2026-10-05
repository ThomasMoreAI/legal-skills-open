#!/usr/bin/env python3
"""Read or check an approved stored wording block without rewriting its text."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import wiki


def read_block(root: Path, note: str, block_id: str) -> dict:
    wiki.load_manifest(root)
    _, path = wiki.safe_note_path(root, note)
    raw = path.read_bytes().decode("utf-8")
    if "\r" in raw:
        raise wiki.WikiError(
            "Review line endings before using the exact wording block."
        )
    fm, body = wiki.split_document(raw)
    if not fm or str(fm.get("pending", "")).casefold() == "true":
        raise wiki.WikiError("This note awaits review.")
    if fm.get("status", "stable") != "stable" or wiki.is_stale(fm.get("stale_after")):
        raise wiki.WikiError("Review this note's status before using its wording.")
    if wiki.trust_tier(fm) != "human-reviewed":
        raise wiki.WikiError("This note awaits human review.")
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", block_id):
        raise wiki.WikiError("Use the stored block identifier.")
    records = fm.get("wording", [])
    if not isinstance(records, list):
        raise wiki.WikiError("Review the wording records.")
    matches = [r for r in records if isinstance(r, dict) and r.get("id") == block_id]
    if len(matches) != 1:
        raise wiki.WikiError("No unique stored wording block with this identifier.")
    record = matches[0]
    try:
        datetime.fromisoformat(str(record.get("approved_at", "")))
    except ValueError as exc:
        raise wiki.WikiError("This wording needs a valid approval date.") from exc
    approver = str(record.get("approved_by", ""))
    if (
        record.get("status") != "approved"
        or not approver.startswith("human:")
        or not approver.removeprefix("human:").strip()
    ):
        raise wiki.WikiError("This wording awaits explicit approval.")
    escaped = re.escape(block_id)
    pattern = (
        rf"^<!-- wiki-wording:{escaped} -->\n(.*?)"
        rf"^<!-- /wiki-wording:{escaped} -->$"
    )
    blocks = re.findall(pattern, body, re.M | re.S)
    if len(blocks) != 1:
        raise wiki.WikiError("No unique delimited wording block found.")
    text = blocks[0]
    if wiki.text_sha256(text) != record.get("sha256"):
        raise wiki.WikiError("Stored wording changed since approval; review it again.")
    source_records = fm.get("sources", [])
    if not isinstance(source_records, list):
        raise wiki.WikiError("Review the source records.")
    sources = [
        s
        for s in source_records
        if isinstance(s, dict) and s.get("id") == record.get("source_id")
    ]
    if len(sources) != 1:
        raise wiki.WikiError("This wording needs a unique source reference.")
    return {
        "id": block_id,
        "note": note,
        "text": text,
        "source": sources[0],
        "approval": {
            k: record.get(k) for k in ("status", "approved_by", "approved_at")
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wiki", required=True, type=Path)
    parser.add_argument("--note", required=True)
    parser.add_argument("--block", required=True)
    parser.add_argument(
        "--check", type=Path, help="compare a UTF-8 plain-text answer block exactly"
    )
    args = parser.parse_args()
    try:
        result = read_block(args.wiki, args.note, args.block)
        if args.check:
            if args.check.read_bytes() != result["text"].encode("utf-8"):
                raise wiki.WikiError(
                    "The answer differs from the approved stored block."
                )
            print("Exact stored wording confirmed.")
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, wiki.WikiError) as exc:
        print(f"Wording unavailable: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
