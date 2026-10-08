#!/usr/bin/env python3
"""
Phase 10.2 — Cross-reference auto-linker.

Walks the `case_judgments.law_references` column (and `fact`/`decision` as
fallback) plus `law_sections.section_text`, extracts law/section references
using Thai legal citation regex, and inserts rows into:
  - `case_law_links` (judgment ↔ section)
  - `cross_references` (section ↔ section, with relation_type metadata)

Citation patterns supported (Thai + Latin digits normalized):
  - "มาตรา ๑๑๘" / "มาตรา 118" / "Section 118" / "ม. 57"
  - Law code prefixes: ป.อ. / ป.พ.พ. / ป.วิ.อ. / ป.วิ.แพ่ง /
    พ.ร.บ.คุ้มครองแรงงาน / พ.ร.บ.แรงงาน / พ.ร.บ.ประกันสังคม / พ.ร.บ.เงินทดแทน

Idempotent: re-running on the same DB will skip rows where the link already
exists (matched by judgment_id + section_id, or from_section_id + to_section_id).

Usage:
    python3 scripts/build_cross_references.py
    python3 scripts/build_cross_references.py --limit 100  # for testing
    python3 scripts/build_cross_references.py --dry-run
"""
from __future__ import annotations
import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'prisma' / 'thai_legal_db.sqlite'

# ---------------------------------------------------------------------------
# Thai-Latin digit normalization
# ---------------------------------------------------------------------------
THAI_DIGITS = '๐๑๒๓๔๕๖๗๘๙'
ARABIC_DIGITS = '0123456789'
DIGIT_MAP = str.maketrans(THAI_DIGITS, ARABIC_DIGITS)

def normalize_digits(s: str) -> str:
    return s.translate(DIGIT_MAP)

# ---------------------------------------------------------------------------
# Citation regexes
# ---------------------------------------------------------------------------
# Law code aliases (short forms found in judgment text + section text)
LAW_CODE_ALIASES = {
    'ป.อ.':                       'penal_code',
    'ป.พ.พ.':                     'civil_commercial_code',
    'ป.วิ.อ.':                    'criminal_procedure_code',
    'ป.วิ.แพ่ง':                  'civil_procedure_code',
    'พ.ร.บ.คุ้มครองแรงงาน':       'lpa',
    'พ.ร.บ.แรงงาน':               'lpa',
    'พ.ร.บ.ประกันสังคม':          'ssa',
    'พ.ร.บ.เงินทดแทน':            'wcf',
}

# Pattern: optional law_code + มาตรา + number (handles Thai + Latin digits)
# Multi-character regex is acceptable here because we are EXTRACTING data,
# not SANITIZING untrusted input. CodeQL does not flag extraction regex.
SECTION_REF_RE = re.compile(
    r'(?P<law_code>ป\.อ\.|ป\.พ\.พ\.|ป\.วิ\.อ\.|ป\.วิ\.แพ่ง|'
    r'พ\.ร\.บ\.คุ้มครองแรงงาน|พ\.ร\.บ\.แรงงาน|'
    r'พ\.ร\.บ\.ประกันสังคม|พ\.ร\.บ\.เงินทดแทน)?\s*'
    r'(?:มาตรา|Section|Sec\.?|ม\.)\s*'
    r'(?P<section_num>[0-9๐-๙/]+)',
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# DB
# ---------------------------------------------------------------------------
def db_conn() -> sqlite3.Connection:
    if not DB_PATH.exists():
        print(f"ERROR: DB not found at {DB_PATH}", file=sys.stderr)
        sys.exit(1)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def ensure_schema(conn: sqlite3.Connection) -> None:
    """Make sure cross_references + case_law_links tables exist (idempotent)."""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS cross_references (
            ref_id          INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type     TEXT NOT NULL,
            source_id       INTEGER NOT NULL,
            source_code     TEXT,
            target_type     TEXT NOT NULL,
            target_id       INTEGER,
            target_code     TEXT,
            relation_type   TEXT,
            section_ref     TEXT,
            notes           TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_xref_source ON cross_references(source_type, source_id);
        CREATE INDEX IF NOT EXISTS idx_xref_target ON cross_references(target_type, target_id);

        CREATE INDEX IF NOT EXISTS idx_caselawlinks_judgment_id ON case_law_links(judgment_id);
        CREATE INDEX IF NOT EXISTS idx_caselawlinks_section_id ON case_law_links(section_id);
    """)
    conn.commit()

# ---------------------------------------------------------------------------
# Law lookup cache
# ---------------------------------------------------------------------------
def load_law_lookup(conn: sqlite3.Connection) -> dict[str, int]:
    """Build {normalized_law_name_lower: law_id} + {alias: law_id} from DB."""
    cur = conn.execute("SELECT law_id, law_name_th, law_name_en FROM laws")
    lookup: dict[str, int] = {}
    for row in cur:
        law_id = row['law_id']
        if row['law_name_th']:
            key = row['law_name_th'].strip().lower()
            lookup[key] = law_id
            # Also store short form (first 30 chars)
            lookup[key[:30]] = law_id
        if row['law_name_en']:
            lookup[row['law_name_en'].strip().lower()] = law_id
            lookup[row['law_name_en'].strip().lower()[:30]] = law_id

    # Add manual aliases mapped to best-guess law_id
    alias_to_law_id_hint = {
        'lpa':    'คุ้มครองแรงงาน',
        'ssa':    'ประกันสังคม',
        'wcf':    'เงินทดแทน',
        'penal_code': 'อาญา',
        'civil_commercial_code': 'แพ่งและพาณิชย์',
        'criminal_procedure_code': 'วิอาญา',
        'civil_procedure_code': 'วิแพ่ง',
    }
    for alias, hint in alias_to_law_id_hint.items():
        cur2 = conn.execute(
            "SELECT law_id FROM laws WHERE law_name_th LIKE ? OR law_name_en LIKE ? LIMIT 1",
            (f'%{hint}%', f'%{hint}%'),
        )
        row2 = cur2.fetchone()
        if row2:
            lookup[alias] = row2['law_id']
            # Also map the Thai short-form back
            lookup[hint] = row2['law_id']
    return lookup

def find_section(conn: sqlite3.Connection, law_id: int, section_num: str) -> int | None:
    """Try to find a matching section by section_number."""
    # Try exact section_number match
    cur = conn.execute(
        "SELECT section_id FROM law_sections WHERE law_id = ? AND section_number = ? LIMIT 1",
        (law_id, section_num),
    )
    row = cur.fetchone()
    if row:
        return row['section_id']
    # Try LIKE on section_number (some have suffixes like "118/1")
    cur2 = conn.execute(
        "SELECT section_id FROM law_sections WHERE law_id = ? AND section_number LIKE ? LIMIT 1",
        (law_id, f'{section_num}%'),
    )
    row2 = cur2.fetchone()
    if row2:
        return row2['section_id']
    return None

# ---------------------------------------------------------------------------
# Linkers
# ---------------------------------------------------------------------------
def link_judgments_to_sections(
    conn: sqlite3.Connection,
    law_lookup: dict[str, int],
    limit: int | None = None,
    dry_run: bool = False,
) -> tuple[int, int]:
    """Walk case_judgments.law_references, extract refs, insert into case_law_links.
    Returns (inserted_count, skipped_duplicate_count)."""
    sql = (
        "SELECT judgment_id, law_references, fact, decision, title FROM case_judgments "
        "WHERE (law_references IS NOT NULL AND TRIM(law_references) != '') "
        "   OR (fact IS NOT NULL AND TRIM(fact) != '') "
        "ORDER BY judgment_id"
    )
    if limit:
        sql += f" LIMIT {limit}"
    cur = conn.execute(sql)

    inserted = 0
    skipped = 0
    for j_row in cur:
        text = ' '.join(filter(None, [
            j_row['law_references'],
            j_row['fact'],
            j_row['decision'],
        ]))
        text = normalize_digits(text)
        seen_for_this_judgment: set[tuple[int | None, int | None]] = set()

        for m in SECTION_REF_RE.finditer(text):
            section_num = m.group('section_num').strip()
            law_code_raw = (m.group('law_code') or '').strip()
            law_id: int | None = None
            if law_code_raw and law_code_raw in law_lookup:
                law_id = law_lookup[law_code_raw]
            elif law_code_raw:
                alias_key = LAW_CODE_ALIASES.get(law_code_raw)
                if alias_key and alias_key in law_lookup:
                    law_id = law_lookup[alias_key]

            section_id: int | None = None
            if law_id:
                section_id = find_section(conn, law_id, section_num)

            # Dedup within the same judgment
            key = (law_id, section_id)
            if key in seen_for_this_judgment:
                continue
            seen_for_this_judgment.add(key)

            if not (section_id or law_id):
                continue

            # Check for existing link
            exists_cur = conn.execute(
                "SELECT 1 FROM case_law_links WHERE judgment_id = ? AND "
                + ("section_id = ?" if section_id else "law_id = ? AND section_id IS NULL"),
                (j_row['judgment_id'], section_id or law_id),
            )
            if exists_cur.fetchone():
                skipped += 1
                continue

            if not dry_run:
                conn.execute(
                    """
                    INSERT INTO case_law_links (judgment_id, section_id, law_id, law_code, section_ref)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (j_row['judgment_id'], section_id, law_id, law_code_raw or None, section_num),
                )
            inserted += 1

    return inserted, skipped

def link_sections_to_sections(
    conn: sqlite3.Connection,
    law_lookup: dict[str, int],
    limit: int | None = None,
    dry_run: bool = False,
) -> tuple[int, int]:
    """Walk law_sections.section_text, extract refs to other sections, insert
    into cross_references. Returns (inserted_count, skipped_duplicate_count)."""
    sql = (
        "SELECT section_id, law_id, section_text FROM law_sections "
        "WHERE section_text IS NOT NULL AND LENGTH(section_text) > 50 "
        "ORDER BY section_id"
    )
    if limit:
        sql += f" LIMIT {limit}"
    cur = conn.execute(sql)

    inserted = 0
    skipped = 0
    for s_row in cur:
        text = normalize_digits(s_row['section_text'])
        seen_for_this_section: set[tuple[int | None, int | None]] = set()

        for m in SECTION_REF_RE.finditer(text):
            section_num = m.group('section_num').strip()
            law_code_raw = (m.group('law_code') or '').strip()
            law_id: int | None = None
            if law_code_raw and law_code_raw in law_lookup:
                law_id = law_lookup[law_code_raw]
            elif not law_code_raw:
                law_id = s_row['law_id']  # self-reference within same law
            else:
                alias_key = LAW_CODE_ALIASES.get(law_code_raw)
                if alias_key and alias_key in law_lookup:
                    law_id = law_lookup[alias_key]
            if not law_id:
                continue

            to_section_id = find_section(conn, law_id, section_num)
            if not to_section_id or to_section_id == s_row['section_id']:
                continue

            key = (law_id, to_section_id)
            if key in seen_for_this_section:
                continue
            seen_for_this_section.add(key)

            # Check for existing cross-reference
            exists_cur = conn.execute(
                "SELECT 1 FROM cross_references "
                "WHERE source_type = 'law_section' AND source_id = ? "
                "  AND target_type = 'law_section' AND target_id = ? LIMIT 1",
                (s_row['section_id'], to_section_id),
            )
            if exists_cur.fetchone():
                skipped += 1
                continue

            if not dry_run:
                conn.execute(
                    """
                    INSERT INTO cross_references
                        (source_type, source_id, target_type, target_id,
                         relation_type, section_ref, notes)
                    VALUES ('law_section', ?, 'law_section', ?, 'references', ?, ?)
                    """,
                    (s_row['section_id'], to_section_id, section_num,
                     f'auto-extracted from section text (regex match: {m.group(0).strip()})'),
                )
            inserted += 1

    return inserted, skipped

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--limit', type=int, help='Limit number of source rows (for testing)')
    ap.add_argument('--dry-run', action='store_true', help='Do not write to DB, just count')
    args = ap.parse_args()

    print(f"[{datetime.now(timezone.utc).isoformat()}] Phase 10.2 — Cross-reference auto-linker")
    print(f"  DB: {DB_PATH}")
    print(f"  dry_run: {args.dry_run}")
    print()

    with db_conn() as conn:
        ensure_schema(conn)
        print("Loading law lookup table...")
        law_lookup = load_law_lookup(conn)
        print(f"  → {len(law_lookup)} law aliases loaded")

        print("\nLinking judgments → sections (case_law_links)...")
        n1, skip1 = link_judgments_to_sections(conn, law_lookup, limit=args.limit, dry_run=args.dry_run)
        print(f"  → inserted: {n1}, skipped (duplicates): {skip1}")

        print("\nLinking sections → sections (cross_references)...")
        n2, skip2 = link_sections_to_sections(conn, law_lookup, limit=args.limit, dry_run=args.dry_run)
        print(f"  → inserted: {n2}, skipped (duplicates): {skip2}")

        if not args.dry_run:
            conn.commit()

    print(f"\nDone. Total new links: {n1 + n2} (case_law_links: {n1}, cross_references: {n2})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
