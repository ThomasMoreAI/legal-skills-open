#!/usr/bin/env python3
"""
sync_index.py — Reconcile matters.json with journal.md files on disk.

Scans one level deep for */journal.md, extracts header metadata,
and updates matters.json to match reality. Stdlib only.

Usage:
    python sync_index.py /path/to/legal-matters-folder
"""

import json
import re
import sys
from pathlib import Path
from datetime import date


def extract_header(journal_path: Path) -> dict:
    """Parse the YAML-ish header from a journal.md file."""
    text = journal_path.read_text(encoding="utf-8")
    meta = {}

    # Matter name from H1
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        meta["matter_name"] = m.group(1).strip()

    # Key-value fields
    patterns = {
        "client": r"\*\*Client:\*\*\s*([^|*\n]+)",
        "matter_id": r"\*\*Matter ID:\*\*\s*(\S+)",
        "status": r"\*\*Status:\*\*\s*(\w+)",
        "matter_type": r"\*\*Matter Type:\*\*\s*(.+?)(?:\n|\*\*)",
    }
    for key, pattern in patterns.items():
        m = re.search(pattern, text)
        if m:
            meta[key] = m.group(1).strip()

    return meta


def find_last_log_date(journal_path: Path) -> str | None:
    """Find the most recent ### YYYY-MM-DD header in the log."""
    text = journal_path.read_text(encoding="utf-8")
    dates = re.findall(r"^###\s+(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
    return dates[-1] if dates else None


def load_index(index_path: Path) -> list[dict]:
    """Load matters.json, returning empty list if missing."""
    if not index_path.exists():
        return []
    return json.loads(index_path.read_text(encoding="utf-8"))


def save_index(index_path: Path, matters: list[dict]):
    """Write matters.json with pretty formatting."""
    index_path.write_text(
        json.dumps(matters, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def next_matter_id(matters: list[dict]) -> str:
    """Find highest M-XXX and increment."""
    max_num = 0
    for m in matters:
        match = re.match(r"M-(\d+)", m.get("id", ""))
        if match:
            max_num = max(max_num, int(match.group(1)))
    return f"M-{max_num + 1:03d}"


def sync(root: Path):
    """Main reconciliation logic."""
    index_path = root / "matters.json"
    matters = load_index(index_path)

    # Build lookup by folder name
    by_folder = {m["folder"]: m for m in matters}

    # Scan for journal.md files one level deep
    journals_found = set()
    for journal_path in sorted(root.glob("*/journal.md")):
        folder_name = journal_path.parent.name
        journals_found.add(folder_name)
        header = extract_header(journal_path)
        last_date = find_last_log_date(journal_path)

        if folder_name in by_folder:
            # Update existing entry if metadata differs
            entry = by_folder[folder_name]
            changed = False
            for key in ("client", "matter_name", "matter_type", "status"):
                if key in header and header[key] != entry.get(key):
                    entry[key] = header[key]
                    changed = True
            if last_date and last_date != entry.get("last_session"):
                entry["last_session"] = last_date
                changed = True
            if changed:
                print(f"  Updated: {folder_name}")
        else:
            # New journal without index entry — add it
            new_entry = {
                "id": next_matter_id(matters),
                "folder": folder_name,
                "client": header.get("client", "Unknown"),
                "matter_name": header.get("matter_name", folder_name),
                "matter_type": header.get("matter_type", "unknown"),
                "aliases": [],
                "parties": [],
                "status": header.get("status", "active").lower(),
                "created": last_date or str(date.today()),
                "last_session": last_date or str(date.today()),
            }
            matters.append(new_entry)
            print(f"  Added: {folder_name} as {new_entry['id']}")

    # Mark orphaned entries (index entry but no journal on disk)
    for m in matters:
        if m["folder"] not in journals_found:
            if m.get("status") != "orphaned":
                m["status"] = "orphaned"
                print(f"  Orphaned: {m['folder']} ({m['id']})")

    save_index(index_path, matters)
    print(f"Index synced: {len(matters)} matters, {len(journals_found)} journals on disk.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sync_index.py <legal-matters-folder>")
        sys.exit(1)
    root = Path(sys.argv[1])
    if not root.is_dir():
        print(f"Error: {root} is not a directory")
        sys.exit(1)
    sync(root)
