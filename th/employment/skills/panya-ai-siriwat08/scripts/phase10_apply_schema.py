#!/usr/bin/env python3
"""
Phase 10.1 — Apply LawUpdateNotification + IngestionQueue tables to the local DB.

The production Prisma schema (prisma/schema.prisma) has been updated with these
models, but the actual local DB uses an older schema (Phase 1-8 era). Rather
than run `prisma db push` (which would try to reconcile the entire schema and
risk data loss), we apply just the two new tables directly via raw SQL.

This is idempotent — safe to run multiple times.
"""
import os
import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'prisma' / 'thai_legal_db.sqlite'

SCHEMA_SQL = """
-- Phase 10.1: LawUpdateNotification — RSS / scraper detection log
CREATE TABLE IF NOT EXISTS law_update_notifications (
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
);
CREATE INDEX IF NOT EXISTS idx_lun_status      ON law_update_notifications(status);
CREATE INDEX IF NOT EXISTS idx_lun_update_type ON law_update_notifications(update_type);
CREATE INDEX IF NOT EXISTS idx_lun_detected_at ON law_update_notifications(detected_at);

-- Phase 10.1: IngestionQueue — retry mechanism for failed scrapers / monitors
CREATE TABLE IF NOT EXISTS ingestion_queue (
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
);
CREATE INDEX IF NOT EXISTS idx_iq_status   ON ingestion_queue(status);
CREATE INDEX IF NOT EXISTS idx_iq_job_type ON ingestion_queue(job_type);
"""

def main() -> int:
    if not DB_PATH.exists():
        print(f"ERROR: DB not found at {DB_PATH}", file=sys.stderr)
        return 1

    print(f"Applying Phase 10.1 schema to: {DB_PATH}")
    conn = sqlite3.connect(str(DB_PATH))
    try:
        conn.executescript(SCHEMA_SQL)
        conn.commit()
        # Verify
        cur = conn.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name IN ('law_update_notifications', 'ingestion_queue')
        """)
        tables = [r[0] for r in cur.fetchall()]
        print(f"  ✓ Tables present: {tables}")

        cur2 = conn.execute("""
            SELECT name FROM sqlite_master
            WHERE type='index' AND name LIKE 'idx_lun_%' OR name LIKE 'idx_iq_%'
            ORDER BY name
        """)
        indexes = [r[0] for r in cur2.fetchall()]
        print(f"  ✓ Indexes present: {len(indexes)} ({', '.join(indexes)})")
    finally:
        conn.close()

    print("\nDone. Phase 10.1 schema applied successfully.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
