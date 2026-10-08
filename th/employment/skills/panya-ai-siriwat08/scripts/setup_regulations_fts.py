#!/usr/bin/env python3
"""
Phase 10.5 — Set up regulations table + FTS5 index for RAG retrieval.

The production RAG code (src/lib/rag.ts) queries `regulations_fts_v2` to
retrieve regulation text alongside law sections and judgments. This script
creates the underlying `regulations` table (if missing) and the FTS5 index.

Idempotent — safe to run multiple times.

Usage:
    python3 scripts/setup_regulations_fts.py
    python3 scripts/setup_regulations_fts.py --db prisma/thai_legal_db.sqlite
"""
from __future__ import annotations
import argparse
import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'prisma' / 'thai_legal_db.sqlite'

SCHEMA_SQL = """
-- =========================================================================
-- regulations table — ministerial regulations, announcements, rules
-- =========================================================================
CREATE TABLE IF NOT EXISTS regulations (
    regulation_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    regulation_code   TEXT    NOT NULL,
    title             TEXT    NOT NULL,
    category          TEXT,
    issuing_body      TEXT,
    year              TEXT,
    issue_date        TEXT,
    full_text         TEXT,
    source_url        TEXT,
    source_id         INTEGER,
    chars_count       INTEGER DEFAULT 0,
    note              TEXT,
    is_repealed       INTEGER DEFAULT 0,
    repeal_status     TEXT    DEFAULT 'active'
);
CREATE INDEX IF NOT EXISTS idx_regulations_category     ON regulations(category);
CREATE INDEX IF NOT EXISTS idx_regulations_is_repealed  ON regulations(is_repealed);
CREATE INDEX IF NOT EXISTS idx_regulations_repeal_status ON regulations(repeal_status);

-- =========================================================================
-- regulations_fts_v2 — FTS5 full-text index on regulations
-- =========================================================================
CREATE VIRTUAL TABLE IF NOT EXISTS regulations_fts_v2 USING fts5(
    title, full_text, regulation_code,
    content='regulations', content_rowid='regulation_id',
    tokenize='unicode61'
);

-- Trigger: keep FTS in sync on INSERT
CREATE TRIGGER IF NOT EXISTS regulations_fts_v2_ai AFTER INSERT ON regulations BEGIN
    INSERT INTO regulations_fts_v2(rowid, title, full_text, regulation_code)
    VALUES (new.regulation_id, new.title, new.full_text, new.regulation_code);
END;

-- Trigger: keep FTS in sync on DELETE
-- Note: 'delete' is the FTS5 special-row command (not a string literal)
CREATE TRIGGER IF NOT EXISTS regulations_fts_v2_ad AFTER DELETE ON regulations BEGIN
    INSERT INTO regulations_fts_v2(regulations_fts_v2, rowid, title, full_text, regulation_code)
    VALUES ('delete', old.regulation_id, old.title, old.full_text, old.regulation_code);
END;

-- Trigger: keep FTS in sync on UPDATE
CREATE TRIGGER IF NOT EXISTS regulations_fts_v2_au AFTER UPDATE ON regulations BEGIN
    INSERT INTO regulations_fts_v2(regulations_fts_v2, rowid, title, full_text, regulation_code)
    VALUES ('delete', old.regulation_id, old.title, old.full_text, old.regulation_code);
    INSERT INTO regulations_fts_v2(rowid, title, full_text, regulation_code)
    VALUES (new.regulation_id, new.title, new.full_text, new.regulation_code);
END;
"""

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--db', type=Path, default=DB_PATH,
                    help=f'Path to SQLite DB (default: {DB_PATH})')
    args = ap.parse_args()

    if not args.db.exists():
        print(f'ERROR: DB not found at {args.db}', file=sys.stderr)
        return 1

    print(f'[{__file__}] Setting up regulations table + FTS5 index...')
    print(f'  DB: {args.db}')
    conn = sqlite3.connect(str(args.db))
    try:
        conn.executescript(SCHEMA_SQL)
        conn.commit()

        # Verify
        cur = conn.execute("""
            SELECT name, type FROM sqlite_master
            WHERE name IN ('regulations', 'regulations_fts_v2',
                           'regulations_fts_v2_ai', 'regulations_fts_v2_ad',
                           'regulations_fts_v2_au')
            ORDER BY name
        """)
        print('\n  Created/verified objects:')
        for r in cur.fetchall():
            print(f'    {r[1]:>10} {r[0]}')

        # Count existing regulations
        n = conn.execute('SELECT COUNT(*) FROM regulations').fetchone()[0]
        print(f'\n  regulations count: {n}')
        n_fts = conn.execute('SELECT COUNT(*) FROM regulations_fts_v2').fetchone()[0]
        print(f'  regulations_fts_v2 count: {n_fts}')
    finally:
        conn.close()

    print('\nDone. Phase 10.5 schema applied successfully.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
