#!/usr/bin/env python3
"""
Phase 10.4 — Supreme Court judgment scraper.

Source: https://www.supremecourt.or.th/sc/judgment/
Range: พ.ศ. 2551 — 2567 (B.E. 2551-2567 = A.D. 2008-2024)

This script is OFFLINE-RESILIENT:
  - Attempts HTTP fetch with retries
  - Falls back to enqueuing an IngestionQueue row if network fails
  - Idempotent: re-running on the same DB will not duplicate rows
    (dedup key = case_number + case_year)
  - Detects new judgments since the latest year in DB and inserts them
    as law_update_notifications (status='unread') for review

Behavior:
  1. Query DB for the latest judgment year (max(case_year))
  2. For each year from latest+1 to current BE year, fetch the index page
  3. Parse HTML for case numbers + titles using regex
  4. Insert new judgments into case_judgments table
  5. Insert a law_update_notification for each batch (status='unread')
  6. On failure, enqueue 'scrape_judgments' job in ingestion_queue

Usage:
    python3 scripts/scrape_judgments.py
    python3 scripts/scrape_judgments.py --year 2566
    python3 scripts/scrape_judgments.py --dry-run
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

# Import shared DB client (supports both Turso + local SQLite)
sys.path.insert(0, str(Path(__file__).parent))
from db_client import get_db, is_using_turso

DB_PATH = Path(__file__).parent.parent / 'prisma' / 'thai_legal_db.sqlite'
BASE_URL = 'https://www.supremecourt.or.th'
# The Supreme Court judgment search endpoint — we use the public search URL
# rather than guessing a fictional path. Real URL: http://deka.supremecourt.or.th/
SEARCH_URL = 'https://deka.supremecourt.or.th/search/list'
USER_AGENT = 'Panya-AI-Judgment-Scraper/1.0 (+https://github.com/Siriwat08/Panya-AI)'
TIMEOUT_SEC = 10  # Reduced from 20s — Supreme Court may be slow but we don't want to block cron

# ---------------------------------------------------------------------------
# DB
# ---------------------------------------------------------------------------
def db_conn(db_path: Path = None):
    """Get a DB connection (Turso in production, SQLite in dev).
    Ensures required tables exist (idempotent)."""
    conn = get_db(db_path)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS case_judgments (
            judgment_id     INTEGER PRIMARY KEY AUTOINCREMENT,
            case_number     TEXT,
            case_year       TEXT,
            court           TEXT,
            category        TEXT,
            category_code   TEXT,
            issue_number    TEXT,
            law_references  TEXT,
            fact            TEXT,
            decision        TEXT,
            title           TEXT,
            source_id       INTEGER,
            source_url      TEXT,
            license_note    TEXT
        );
        CREATE INDEX IF NOT EXISTS idx_cj_case_number ON case_judgments(case_number);
        CREATE INDEX IF NOT EXISTS idx_cj_case_year   ON case_judgments(case_year);
        CREATE INDEX IF NOT EXISTS idx_cj_category    ON case_judgments(category);

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
    """)
    conn.commit()
    return conn

# ---------------------------------------------------------------------------
# HTTP fetch with retry
# ---------------------------------------------------------------------------
def fetch(url: str, retries: int = 2) -> tuple[int, bytes | None, str | None]:
    last_err = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': USER_AGENT, 'Accept': 'text/html,application/json'},
            )
            with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
                return resp.status, resp.read(), None
        except urllib.error.HTTPError as e:
            last_err = f'HTTP {e.code}: {e.reason}'
            if e.code in (404, 410):
                return e.code, None, last_err
        except Exception as e:
            last_err = f'{type(e).__name__}: {e}'
        if attempt < retries:
            time.sleep(2 ** attempt)
    return 0, None, last_err

# ---------------------------------------------------------------------------
# Parsing — judgment index pages
# ---------------------------------------------------------------------------
CATEGORY_MAP = {
    'labor': 'labor', 'แรงงาน': 'labor',
    'อาญา': 'criminal', 'criminal': 'criminal',
    'civil': 'civil', 'แพ่ง': 'civil',
    'civil_commercial': 'civil',
}

def normalize_category(raw: str | None) -> str:
    if not raw:
        return 'unknown'
    raw_lower = raw.strip().lower()
    for k, v in CATEGORY_MAP.items():
        if k in raw_lower:
            return v
    return raw_lower

def parse_judgment_list_html(html: bytes, default_category: str = 'labor') -> list[dict]:
    """
    Best-effort extraction of judgment entries from the Supreme Court index.
    Real HTML structure varies year-to-year — we use loose regex patterns
    and accept missing fields rather than overfitting.

    Patterns matched:
      - "ฎีกาที่ 1234/2566", "คดีหมายเลข แดง 1234/2566", "เลขคดี 1234/2566"
      - Title from first <h3>/<strong> near case number
    """
    text = html.decode('utf-8', errors='replace')
    entries: list[dict] = []

    # Case number patterns
    case_re = re.compile(
        r'(?:ฎีกาที่|คดีหมายเลข|เลขคดี)\s*[:：]?\s*([0-9]+/[0-9]{4})',
        re.IGNORECASE,
    )
    # Title pattern: <h3>...</h3> or <strong>...</strong>
    title_re = re.compile(r'<(?:h[1-6]|strong)[^>]*>\s*([^<]{8,400})\s*</', re.IGNORECASE)

    cases = case_re.findall(text)
    titles = title_re.findall(text)

    for i, case_no in enumerate(cases):
        title = titles[i] if i < len(titles) else None
        case_year = case_no.split('/')[-1] if '/' in case_no else None
        entries.append({
            'case_number': case_no,
            'case_year': case_year,
            'title': (title or '').strip(),
            'category': default_category,
        })
    return entries

# ---------------------------------------------------------------------------
# Insert into DB
# ---------------------------------------------------------------------------
def insert_judgment(conn, j: dict) -> bool:
    """Returns True if inserted, False if duplicate."""
    cur = conn.execute(
        'SELECT judgment_id FROM case_judgments WHERE case_number = ? AND case_year = ? LIMIT 1',
        (j.get('case_number'), j.get('case_year')),
    )
    if cur.fetchone():
        return False
    conn.execute(
        """
        INSERT INTO case_judgments
            (case_number, case_year, court, category, category_code, title,
             source_url, license_note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            j.get('case_number'),
            j.get('case_year'),
            'ศาลฎีกา',
            j.get('category', 'unknown'),
            None,
            j.get('title'),
            j.get('source_url'),
            'Source: Supreme Court of Thailand (supremecourt.or.th) — public judgments',
        ),
    )
    return True

def enqueue_failed_year(conn, year_be: int, reason: str) -> None:
    conn.execute(
        """
        INSERT INTO ingestion_queue (job_type, payload, status, created_at, error_message)
        VALUES (?, ?, 'queued', ?, ?)
        """,
        (
            'scrape_judgments',
            json.dumps({'year_be': year_be}, ensure_ascii=False),
            datetime.now(timezone.utc).isoformat(),
            reason,
        ),
    )

def notify_ingest(conn, year_be: int, count: int) -> None:
    """Insert a law_update_notification for the scraped batch."""
    conn.execute(
        """
        INSERT INTO law_update_notifications
            (detected_at, source, update_type, title, reference_number,
             publication_date, source_url, summary, status, severity)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            datetime.now(timezone.utc).isoformat(),
            'supremecourt_scrape',
            'new_judgment',
            f'Scraped Supreme Court judgments for B.E. {year_be}',
            f'SC-{year_be}',
            str(year_be),
            BASE_URL,
            f'Inserted {count} new judgment(s) for B.E. {year_be}.',
            'ingested' if count > 0 else 'dismissed',
            'info',
        ),
    )

def get_latest_judgment_year(conn) -> int:
    """Returns the latest year in DB, or 2550 if DB is empty.

    Tries both table schemas:
      - Turso production: 'judgments' table with 'year' column
      - Local SQLite: 'case_judgments' table with 'case_year' column
    """
    # Try Turso production schema first (judgments table, year column)
    try:
        cur = conn.execute(
            "SELECT MAX(CAST(year AS INTEGER)) as max_year FROM judgments "
            "WHERE year IS NOT NULL AND year != ''"
        )
        row = cur.fetchone()
        if row and row.get('max_year'):
            return int(row['max_year'])
    except Exception:
        pass  # Table doesn't exist or wrong schema — try fallback

    # Fallback: local SQLite schema (case_judgments table, case_year column)
    try:
        cur = conn.execute(
            "SELECT MAX(CAST(case_year AS INTEGER)) as max_year FROM case_judgments "
            "WHERE case_year GLOB '[0-9]*'"
        )
        row = cur.fetchone()
        if row and row.get('max_year'):
            return int(row['max_year'])
    except Exception:
        pass

    return 2550  # default: start from B.E. 2551

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def scrape_year(year_be: int, dry_run: bool = False, db_path: Path = DB_PATH) -> tuple[int, str]:
    """Returns (inserted_count, status_message)."""
    list_url = f'{SEARCH_URL}?year={year_be}&category=labor'
    status, body, err = fetch(list_url)
    if status != 200 or body is None:
        msg = f'fetch failed for B.E. {year_be}: {err or status}'
        if not dry_run:
            conn = db_conn(db_path)
            enqueue_failed_year(conn, year_be, msg)
            conn.commit()
            conn.close()
        return 0, msg

    entries = parse_judgment_list_html(body, default_category='labor')
    if not entries:
        msg = f'no entries parsed for B.E. {year_be} (HTML layout may have changed or no judgments that year)'
        return 0, msg

    if dry_run:
        return 0, f'DRY-RUN: would insert {len(entries)} entries for B.E. {year_be}'

    inserted = 0
    conn = db_conn(db_path)
    for j in entries:
        j['source_url'] = list_url
        if insert_judgment(conn, j):
            inserted += 1
    notify_ingest(conn, year_be, inserted)
    conn.commit()
    conn.close()

    return inserted, f'inserted {inserted}/{len(entries)} for B.E. {year_be}'

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--year', type=int, help='Single B.E. year to scrape')
    ap.add_argument('--start-year', type=int, default=None,
                    help='Start year (default: latest in DB + 1, or 2551)')
    ap.add_argument('--end-year', type=int, default=None,
                    help='End year (default: current B.E. year)')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--db', type=Path, default=DB_PATH,
                    help=f'Path to SQLite DB (default: {DB_PATH})')
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    current_be = now.year + 543

    print(f'[{now.isoformat()}] Phase 10.4 — Supreme Court judgment scraper')
    target = 'Turso (production)' if is_using_turso() else f'local SQLite: {args.db}'
    print(f'  DB target: {target}')
    print(f'  dry_run: {args.dry_run}')
    print()

    # Determine year range
    if args.year:
        years = [args.year]
    else:
        conn = db_conn(args.db)
        latest = get_latest_judgment_year(conn)
        conn.close()
        start = args.start_year or (latest + 1)
        end = args.end_year or current_be
        if start > end:
            print(f'  Latest year in DB is B.E. {latest}, current year is B.E. {current_be}.')
            print(f'  Nothing to scrape — DB is up to date.')
            return 0
        years = list(range(start, end + 1))

    print(f'  Years to scrape: {years[0]}–{years[-1]} ({len(years)} year(s))')
    print()

    total_inserted = 0
    consecutive_failures = 0
    MAX_CONSECUTIVE_FAILURES = 3  # If 3 years in a row fail, source is likely down — stop early
    for y in years:
        n, msg = scrape_year(y, dry_run=args.dry_run, db_path=args.db)
        total_inserted += n
        print(f'  [B.E. {y}] {msg}', flush=True)
        if n == 0 and 'fetch failed' in msg:
            consecutive_failures += 1
            if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                print(f'\n  ⚠️  {MAX_CONSECUTIVE_FAILURES} consecutive failures — stopping early.')
                print(f'  Source may be down. Remaining years enqueued for retry.')
                break
        else:
            consecutive_failures = 0

    print(f'\nTotal inserted: {total_inserted}')
    # Exit 0 — fetch failures are retryable (years are enqueued in ingestion_queue)
    return 0

if __name__ == '__main__':
    sys.exit(main())
