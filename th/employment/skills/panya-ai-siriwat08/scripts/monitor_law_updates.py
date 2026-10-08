#!/usr/bin/env python3
"""
Phase 10.3 — Ratchakitcha RSS monitor for new laws & regulations.

Source: Royal Gazette RSS — https://ratchakitcha.soc.go.th/rkssub/rss
Backup feeds (tried in order if primary is unreachable):
  - https://ratchakitcha.soc.go.th/rksrss

Behavior:
  1. Fetch RSS XML feed (with retries + User-Agent header)
  2. Parse <item> entries with <title>, <link>, <pubDate>, <description>
  3. Filter items whose title/description contains labor-related keywords:
        แรงงาน, คุ้มครองแรงงาน, ประกันสังคม, สวัสดิการ,
        ลูกจ้าง, นายจ้าง, ค่าจ้าง, เงินเดือน, โบนัส,
        เลิกจ้าง, ทำงาน, วันหยุด, ลา, ค่าล่วงเวลา,
        กองทุนเงินทดแทน, ความปลอดภัยในการทำงาน,
        labor, labour, employment, wage, social security
  4. For each match, check if (source_url, title) already exists in
     law_update_notifications. If new, INSERT with status='unread'.
  5. Classify update_type (new_law/amendment/repeal/new_regulation) and
     severity (info/warning/critical) based on title keywords.
  6. If fetch fails after retries, enqueue 'fetch_rss' job in
     ingestion_queue for retry on next cron run.

Designed to run via GitHub Actions cron: every weekday at 09:00 ICT.

Usage:
    python3 scripts/monitor_law_updates.py
    python3 scripts/monitor_law_updates.py --dry-run
    python3 scripts/monitor_law_updates.py --db prisma/thai_legal_db.sqlite
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
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

# Import shared DB client (supports both Turso + local SQLite)
sys.path.insert(0, str(Path(__file__).parent))
from db_client import get_db, is_using_turso

DB_PATH = Path(__file__).parent.parent / 'prisma' / 'thai_legal_db.sqlite'

# RSS feeds in priority order
RSS_FEEDS = [
    'https://ratchakitcha.soc.go.th/rkssub/rss',
    'https://ratchakitcha.soc.go.th/rksrss',
]

USER_AGENT = 'Panya-AI-Legal-Monitor/1.0 (+https://github.com/Siriwat08/Panya-AI)'
TIMEOUT_SEC = 25

# Keywords that flag an item as labor-relevant (case-insensitive substring match)
LABOR_KEYWORDS = [
    'แรงงาน', 'คุ้มครองแรงงาน', 'ประกันสังคม', 'สวัสดิการ',
    'ลูกจ้าง', 'นายจ้าง', 'ค่าจ้าง', 'เงินเดือน', 'โบนัส',
    'เลิกจ้าง', 'ทำงาน', 'วันหยุด', 'ลา', 'ค่าล่วงเวลา',
    'กองทุนเงินทดแทน', 'ความปลอดภัยในการทำงาน',
    'labor', 'labour', 'employment', 'wage', 'social security',
]

# ---------------------------------------------------------------------------
# DB
# ---------------------------------------------------------------------------
def db_conn(db_path: Path = None):
    """Get a DB connection (Turso in production, SQLite in dev).
    Ensures required tables exist (idempotent)."""
    conn = get_db(db_path)
    conn.executescript("""
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
# Fetch
# ---------------------------------------------------------------------------
def fetch(url: str, retries: int = 2) -> tuple[int, bytes | None, str | None]:
    """Returns (status_code, body, error_message)."""
    last_err = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    'User-Agent': USER_AGENT,
                    'Accept': 'application/rss+xml, application/xml, text/xml',
                },
            )
            with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
                return resp.status, resp.read(), None
        except urllib.error.HTTPError as e:
            last_err = f'HTTP {e.code}: {e.reason}'
        except Exception as e:
            last_err = f'{type(e).__name__}: {e}'
        if attempt < retries:
            time.sleep(2 ** attempt)
    return 0, None, last_err

# ---------------------------------------------------------------------------
# RSS parsing
# ---------------------------------------------------------------------------
def parse_rss(xml_bytes: bytes) -> list[dict]:
    """Parse RSS 2.0 feed. Returns list of items."""
    items: list[dict] = []
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        print(f'[warn] RSS XML parse error: {e}', file=sys.stderr)
        return items

    # RSS 2.0: rss/channel/item
    for item in root.iter('item'):
        title = (item.findtext('title') or '').strip()
        link = (item.findtext('link') or '').strip()
        pub = (item.findtext('pubDate') or '').strip()
        desc = (item.findtext('description') or '').strip()
        guid = (item.findtext('guid') or '').strip() or link
        items.append({
            'title': title,
            'link': link,
            'pub_date': pub,
            'description': desc,
            'guid': guid,
        })
    return items

def is_labor_related(item: dict) -> bool:
    blob = f"{item['title']} {item['description']}".lower()
    for kw in LABOR_KEYWORDS:
        if kw.lower() in blob:
            return True
    return False

def classify_update_type(title: str) -> tuple[str, str]:
    """Returns (update_type, severity)."""
    t = title.lower() if title else ''
    if any(k in title for k in ['ยกเลิก', 'เลิก']) or 'repeal' in t:
        return ('repeal', 'critical')
    if any(k in title for k in ['แก้ไข', 'เพิ่มเติม', 'ฉบับที่ ๒']) or 'amend' in t:
        return ('amendment', 'warning')
    if 'ระเบียบ' in title or 'ข้อบังคับ' in title or 'ประกาศ' in title:
        return ('new_regulation', 'warning')
    return ('new_law', 'info')

def extract_reference_number(title: str, description: str) -> str | None:
    """Extract patterns like 'พ.ศ. 2567', 'ร.33', 'ป.52', '1234/2567'."""
    text = title + ' ' + description
    m = re.search(r'(พ\.ศ\.\s?\d{4}|\d+/\d{4}|[A-Zก-ฮ]\.\d+)', text)
    return m.group(1) if m else None

def normalize_pub_date(pub_date: str) -> str:
    if not pub_date:
        return datetime.now(timezone.utc).isoformat()
    try:
        dt = parsedate_to_datetime(pub_date)
        return dt.isoformat()
    except Exception:
        return pub_date

# ---------------------------------------------------------------------------
# Insert
# ---------------------------------------------------------------------------
def is_duplicate(conn, source_url: str, title: str) -> bool:
    cur = conn.execute(
        'SELECT 1 FROM law_update_notifications WHERE source_url = ? OR title = ? LIMIT 1',
        [source_url, title],
    )
    return cur.fetchone() is not None

def insert_notification(conn, item: dict) -> bool:
    """Returns True if inserted, False if duplicate."""
    if not item['title']:
        return False
    if is_duplicate(conn, item['link'] or item['guid'], item['title']):
        return False
    update_type, severity = classify_update_type(item['title'])
    ref_no = extract_reference_number(item['title'], item['description'])
    conn.execute(
        """
        INSERT INTO law_update_notifications
            (detected_at, source, update_type, title, reference_number,
             publication_date, source_url, summary, status, severity)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'unread', ?)
        """,
        [
            datetime.now(timezone.utc).isoformat(),
            'ratchakitcha_rss',
            update_type,
            item['title'][:500],
            ref_no,
            normalize_pub_date(item['pub_date']),
            item['link'] or item['guid'],
            item['description'][:1000] if item['description'] else None,
            severity,
        ],
    )
    return True

def enqueue_failed_fetch(conn, reason: str) -> None:
    conn.execute(
        """
        INSERT INTO ingestion_queue (job_type, payload, status, created_at, error_message)
        VALUES (?, ?, 'queued', ?, ?)
        """,
        [
            'fetch_rss',
            json.dumps({'feeds': RSS_FEEDS}, ensure_ascii=False),
            datetime.now(timezone.utc).isoformat(),
            reason,
        ],
    )

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dry-run', action='store_true',
                    help='Do not write to DB, just print what would be inserted')
    ap.add_argument('--db', type=Path, default=DB_PATH,
                    help=f'Path to SQLite DB (default: {DB_PATH}, ignored when TURSO_URL is set)')
    args = ap.parse_args()

    print(f"[{datetime.now(timezone.utc).isoformat()}] Phase 10.3 — RSS monitor")
    target = 'Turso (production)' if is_using_turso() else f'local SQLite: {args.db}'
    print(f"  DB target: {target}")
    print(f"  dry_run: {args.dry_run}")
    print()

    print("Fetching RSS feeds...")
    items: list[dict] = []
    fetch_error = None
    for url in RSS_FEEDS:
        status, body, err = fetch(url)
        if status == 200 and body:
            print(f"  ✓ fetched {url} ({len(body)} bytes)")
            items = parse_rss(body)
            if items:
                break
        else:
            print(f"  ✗ failed {url}: {err}", file=sys.stderr)
            fetch_error = err

    if not items:
        print(f"\n[warn] no items parsed. last error: {fetch_error}")
        if not args.dry_run:
            conn = db_conn(args.db)
            enqueue_failed_fetch(conn, fetch_error or 'no items')
            conn.commit()
            conn.close()
            print("  → enqueued 'fetch_rss' job for retry on next cron run")
        # Exit 0 — this is NOT a hard failure. The RSS feed may be temporarily
        # unavailable (403 from data center IPs is common). The retry job is
        # queued and will be picked up on the next cron run.
        return 0

    labor_items = [it for it in items if is_labor_related(it)]
    print(f"\n  → {len(items)} total items, {len(labor_items)} labor-related")

    if args.dry_run:
        print("\nDry-run — would insert:")
        for it in labor_items:
            update_type, severity = classify_update_type(it['title'])
            print(f"  [{severity:>8}] [{update_type:>14}] {it['title'][:80]}")
            print(f"             {it['link']}")
        return 0

    inserted = 0
    conn = db_conn(args.db)
    for it in labor_items:
        if insert_notification(conn, it):
            inserted += 1
    conn.commit()
    conn.close()

    print(f"\n  ✓ inserted {inserted} new notification(s)")
    if inserted == 0:
        print("  (all items were already in DB — duplicates skipped)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
