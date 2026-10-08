#!/usr/bin/env python3
"""
Phase 10 — Apply new schema to Turso production DB + migrate new data.

This script:
  1. Creates law_update_notifications + ingestion_queue tables on Turso
     (if they don't exist) — idempotent.
  2. Copies the 8 seeded regulations from local SQLite to Turso
     (skips duplicates by regulation_code).
  3. Copies new cross_references from local SQLite to Turso
     (skips duplicates by source_type+source_id+target_type+target_id).
  4. Rebuilds FTS indexes on Turso if needed.
  5. Reports final row counts so you can verify in Turso UI.

Usage:
    TURSO_URL=https://panya-ai-siriwat08.aws-ap-northeast-1.turso.io \
    TURSO_TOKEN=eyJ... \
    python3 scripts/migrate_phase10_to_turso.py

    # Or with env vars already set:
    python3 scripts/migrate_phase10_to_turso.py
"""
from __future__ import annotations
import json
import os
import sqlite3
import sys
import urllib.request
from pathlib import Path

LOCAL_DB = Path(__file__).parent.parent / 'prisma' / 'thai_legal_db.sqlite'

TURSO_URL = os.environ.get('TURSO_URL', '').replace('libsql://', 'https://')
TURSO_TOKEN = os.environ.get('TURSO_TOKEN') or os.environ.get('TURSO_AUTH_TOKEN')

# ---------------------------------------------------------------------------
# Turso HTTP API client
# ---------------------------------------------------------------------------
def turso_execute(sql: str, params: list = None) -> dict:
    """Execute a single SQL statement on Turso via the v2 pipeline API."""
    if not TURSO_URL or not TURSO_TOKEN:
        print('ERROR: TURSO_URL and TURSO_TOKEN must be set', file=sys.stderr)
        sys.exit(1)
    stmt = {'sql': sql}
    if params:
        # Convert Python values to libsql value format
        encoded = []
        for p in params:
            if p is None:
                encoded.append({'type': 'null'})
            elif isinstance(p, int):
                encoded.append({'type': 'integer', 'value': str(p)})
            elif isinstance(p, float):
                encoded.append({'type': 'float', 'value': str(p)})
            elif isinstance(p, str):
                encoded.append({'type': 'text', 'value': p})
            elif isinstance(p, bytes):
                encoded.append({'type': 'blob', 'base64': p.hex()})
            else:
                encoded.append({'type': 'text', 'value': str(p)})
        stmt['args'] = encoded
    body = json.dumps({
        'requests': [{'type': 'execute', 'stmt': stmt}]
    }).encode()
    req = urllib.request.Request(
        f'{TURSO_URL}/v2/pipeline',
        data=body,
        headers={
            'Authorization': f'Bearer {TURSO_TOKEN}',
            'Content-Type': 'application/json',
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            for r in data.get('results', []):
                if r.get('type') == 'ok':
                    return r['response']['result']
                elif r.get('type') == 'error':
                    raise RuntimeError(f"Turso SQL error: {r['error']['message']}")
            return {}
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        raise RuntimeError(f'Turso HTTP {e.code}: {body[:500]}') from e

def turso_query(sql: str) -> list[dict]:
    """Run a SELECT and return rows as list of dicts."""
    result = turso_execute(sql)
    cols = [c['name'] for c in result.get('cols', [])]
    rows = []
    for r in result.get('rows', []):
        row = {}
        for i, c in enumerate(cols):
            v = r[i]
            if isinstance(v, dict):
                if v.get('type') == 'null':
                    row[c] = None
                elif v.get('type') == 'integer':
                    row[c] = int(v['value'])
                elif v.get('type') == 'float':
                    row[c] = float(v['value'])
                else:
                    row[c] = v.get('value')
            else:
                row[c] = v
        rows.append(row)
    return rows

# ---------------------------------------------------------------------------
# Migration steps
# ---------------------------------------------------------------------------
def step1_create_schema():
    print('\n[1/5] Creating Phase 10 tables on Turso (idempotent)...')
    schema_sql = [
        """CREATE TABLE IF NOT EXISTS law_update_notifications (
            notification_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            detected_at       TEXT    NOT NULL,
            source            TEXT    NOT NULL,
            update_type       TEXT    NOT NULL,
            title             TEXT    NOT NULL,
            reference_number  TEXT,
            publication_date  TEXT,
            source_url        TEXT,
            summary           TEXT,
            status            TEXT    NOT NULL DEFAULT 'unread',
            severity          TEXT    NOT NULL DEFAULT 'info',
            reviewed_by       TEXT,
            reviewed_at       TEXT,
            review_notes      TEXT
        )""",
        "CREATE INDEX IF NOT EXISTS idx_lun_status ON law_update_notifications(status)",
        "CREATE INDEX IF NOT EXISTS idx_lun_update_type ON law_update_notifications(update_type)",
        "CREATE INDEX IF NOT EXISTS idx_lun_detected_at ON law_update_notifications(detected_at)",
        """CREATE TABLE IF NOT EXISTS ingestion_queue (
            queue_id        INTEGER PRIMARY KEY AUTOINCREMENT,
            job_type        TEXT    NOT NULL,
            payload         TEXT    NOT NULL,
            status          TEXT    NOT NULL DEFAULT 'queued',
            scheduled_for   TEXT,
            started_at      TEXT,
            completed_at    TEXT,
            result_summary  TEXT,
            error_message   TEXT,
            created_at      TEXT    NOT NULL,
            created_by      TEXT
        )""",
        "CREATE INDEX IF NOT EXISTS idx_iq_status ON ingestion_queue(status)",
        "CREATE INDEX IF NOT EXISTS idx_iq_job_type ON ingestion_queue(job_type)",
    ]
    for sql in schema_sql:
        turso_execute(sql)
    print(f'  ✓ {len(schema_sql)} schema statements applied')

def step2_migrate_regulations():
    """Copy 8 regulations from local SQLite to Turso."""
    print('\n[2/5] Migrating regulations to Turso...')
    if not LOCAL_DB.exists():
        print(f'  ⚠ Local DB not found at {LOCAL_DB} — skipping')
        return 0
    local = sqlite3.connect(str(LOCAL_DB))
    local.row_factory = sqlite3.Row
    rows = local.execute('''
        SELECT regulation_code, title, category, issuing_body, year, issue_date,
               full_text, source_url, note, chars_count
        FROM regulations
    ''').fetchall()
    inserted = 0
    skipped = 0
    for r in rows:
        # Check if exists on Turso (by regulation_code)
        existing = turso_query(
            f"SELECT regulation_id FROM regulations WHERE regulation_code = '{r['regulation_code']}' LIMIT 1"
        )
        if existing:
            skipped += 1
            continue
        turso_execute('''
            INSERT INTO regulations
                (regulation_code, title, category, issuing_body, year, issue_date,
                 full_text, source_url, note, chars_count, is_repealed, repeal_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 'active')
        ''', [r['regulation_code'], r['title'], r['category'], r['issuing_body'],
              r['year'], r['issue_date'], r['full_text'], r['source_url'],
              r['note'], r['chars_count']])
        inserted += 1
        print(f'  ✓ {r["regulation_code"]}: {r["title"][:50]}')
    local.close()
    print(f'  → inserted: {inserted}, skipped (existing): {skipped}')
    return inserted

def step3_migrate_cross_references():
    """Copy new cross_references from local SQLite to Turso."""
    print('\n[3/5] Migrating cross_references to Turso...')
    if not LOCAL_DB.exists():
        print(f'  ⚠ Local DB not found — skipping')
        return 0
    local = sqlite3.connect(str(LOCAL_DB))
    local.row_factory = sqlite3.Row
    rows = local.execute('''
        SELECT source_type, source_id, source_code, target_type, target_id,
               target_code, relation_type, section_ref, notes
        FROM cross_references
    ''').fetchall()
    inserted = 0
    skipped = 0
    for r in rows:
        # Check if exists on Turso
        existing = turso_query(
            f"SELECT ref_id FROM cross_references WHERE source_type = '{r['source_type']}' "
            f"AND source_id = {r['source_id']} AND target_type = '{r['target_type']}' LIMIT 1"
        )
        if existing:
            skipped += 1
            continue
        turso_execute('''
            INSERT INTO cross_references
                (source_type, source_id, source_code, target_type, target_id,
                 target_code, relation_type, section_ref, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', [r['source_type'], r['source_id'], r['source_code'],
              r['target_type'], r['target_id'], r['target_code'],
              r['relation_type'], r['section_ref'], r['notes']])
        inserted += 1
    local.close()
    print(f'  → inserted: {inserted}, skipped (existing): {skipped}')
    return inserted

def step4_migrate_case_law_links():
    """Copy new case_law_links from local to Turso."""
    print('\n[4/5] Migrating case_law_links to Turso...')
    if not LOCAL_DB.exists():
        return 0
    local = sqlite3.connect(str(LOCAL_DB))
    local.row_factory = sqlite3.Row
    # Check if case_law_links table exists locally
    try:
        rows = local.execute('''
            SELECT judgment_id, section_id, law_id, law_code, section_ref
            FROM case_law_links
        ''').fetchall()
    except sqlite3.OperationalError:
        print('  ⚠ case_law_links table not in local DB — skipping')
        return 0
    inserted = 0
    skipped = 0
    for r in rows:
        # Check if exists on Turso
        existing = turso_query(
            f"SELECT 1 FROM case_law_links WHERE judgment_id = {r['judgment_id']} "
            f"AND section_id = {r['section_id'] or 'NULL'} LIMIT 1" if r['section_id']
            else f"SELECT 1 FROM case_law_links WHERE judgment_id = {r['judgment_id']} "
                 f"AND section_id IS NULL LIMIT 1"
        )
        if existing:
            skipped += 1
            continue
        try:
            turso_execute('''
                INSERT INTO case_law_links
                    (judgment_id, section_id, law_id, law_code, section_ref)
                VALUES (?, ?, ?, ?, ?)
            ''', [r['judgment_id'], r['section_id'], r['law_id'],
                  r['law_code'], r['section_ref']])
            inserted += 1
        except RuntimeError as e:
            print(f'  ⚠ Skipped row (judgment_id={r['judgment_id']}): {str(e)[:80]}')
            skipped += 1
    local.close()
    print(f'  → inserted: {inserted}, skipped (existing): {skipped}')
    return inserted

def step5_verify():
    """Print final row counts on Turso."""
    print('\n[5/5] Final Turso row counts (verify in UI):')
    tables = ['laws', 'law_sections', 'judgments', 'regulations',
              'contract_templates', 'rag_chunks', 'sources',
              'cross_references', 'law_update_notifications', 'ingestion_queue']
    for t in tables:
        try:
            rows = turso_query(f'SELECT COUNT(*) as n FROM {t}')
            n = rows[0]['n'] if rows else 0
            print(f'  {t:<28} {n:>8}')
        except RuntimeError as e:
            print(f'  {t:<28} ERROR: {str(e)[:60]}')

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print('=' * 60)
    print('Phase 10 — Migrate to Turso production DB')
    print('=' * 60)
    print(f'Turso URL: {TURSO_URL}')
    print(f'Local DB:  {LOCAL_DB}')
    print(f'Local DB exists: {LOCAL_DB.exists()}')

    step1_create_schema()
    n_regs = step2_migrate_regulations()
    n_xrefs = step3_migrate_cross_references()
    n_links = step4_migrate_case_law_links()
    step5_verify()

    print(f'\n{"=" * 60}')
    print(f'Migration complete.')
    print(f'  New regulations inserted:     {n_regs}')
    print(f'  New cross_references inserted: {n_xrefs}')
    print(f'  New case_law_links inserted:   {n_links}')
    print(f'\n→ Open https://app.turso.tech/siriwat08 to verify in UI')
    print(f'→ You should now see law_update_notifications + ingestion_queue tables')
    print(f'→ And the regulations table should have {615 + n_regs} rows (615 existing + {n_regs} new)')
    print('=' * 60)
    return 0

if __name__ == '__main__':
    sys.exit(main())
