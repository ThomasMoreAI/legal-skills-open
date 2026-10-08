#!/usr/bin/env python3
"""Extract all tables from a SQLite database and output as JSON.

Used by migrate_to_turso.ts — invoked via execFileSync with absolute python3 path.
Reads the DB path from PANYA_LOCAL_DB environment variable (no shell interpolation).

Usage:
  PANYA_LOCAL_DB=/path/to/db.db python3 _extract_sqlite.py
"""

import sqlite3
import json
import sys
import os


def main():
    db_path = os.environ.get('PANYA_LOCAL_DB', '')
    if not db_path:
        print('ERROR: PANYA_LOCAL_DB environment variable not set', file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    tables = [
        'sources', 'laws', 'law_sections', 'case_judgments',
        'case_law_links', 'ingestion_log', 'rag_chunks'
    ]

    out = {}
    for t in tables:
        try:
            cur = conn.execute(f'SELECT * FROM {t}')
            cols = [d[0] for d in cur.description]
            rows = [dict(zip(cols, r)) for r in cur.fetchall()]
            out[t] = {'columns': cols, 'rows': rows}
            print(f'  {t}: {len(rows)} rows', file=sys.stderr)
        except Exception as e:
            out[t] = {'error': str(e)}
            print(f'  {t}: ERROR {e}', file=sys.stderr)

    conn.close()
    print(json.dumps(out, default=str, ensure_ascii=False))


if __name__ == '__main__':
    main()
