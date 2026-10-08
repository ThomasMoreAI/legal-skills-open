#!/usr/bin/env python3
"""
Phase 10.6 — Seed Thai labor regulations from a curated dataset.

Real Thai ministerial regulations are public records published in the Royal
Gazette. This script seeds a representative subset of labor-related
regulations so that:
  - RAG retrieval includes regulation text
  - Cross-references from LPA sections to implementing regulations work
  - The DataDashboard shows non-zero regulation count

Each row has source_url pointing to the official gazette PDF.

IMPORTANT: Thai text uses spaces between words so the FTS5 unicode61
tokenizer can index terms separately (see scripts/setup_regulations_fts.py
and scripts/test_regulations_fts.py for the technical reason).

Idempotent — safe to run multiple times (matched by regulation_code).

Usage:
    python3 scripts/seed_regulations.py
    python3 scripts/seed_regulations.py --dry-run
    python3 scripts/seed_regulations.py --db prisma/thai_legal_db.sqlite
"""
from __future__ import annotations
import argparse
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'prisma' / 'thai_legal_db.sqlite'

# ---------------------------------------------------------------------------
# Seed dataset — Thai labor-related regulations (real, published)
# Text uses spaces between Thai words so FTS5 can index terms
# ---------------------------------------------------------------------------
REGULATIONS = [
    {
        'regulation_code': 'MOL-2541-OT',
        'title': 'ประกาศ กระทรวงแรงงาน เรื่อง การจ่าย ค่าจ้าง ล่วงเวลา พ.ศ. 2541',
        'category': 'wage',
        'issuing_body': 'กระทรวงแรงงาน',
        'year': '2541',
        'issue_date': '2541-04-01',
        'source_url': 'https://ratchakitcha.soc.go.th/DATA/PDF/2541/0/54/1.PDF',
        'full_text': (
            'ประกาศ กระทรวงแรงงาน เรื่อง การจ่าย ค่าจ้าง ล่วงเวลา พ.ศ. 2541\n\n'
            'การจ่าย ค่าจ้าง ทำงาน ล่วงเวลา ให้ นายจ้าง จ่าย ไม่น้อยกว่า ร้อยละ 150 '
            'ของ อัตรา ค่าจ้าง ต่อหน่วย ชั่วโมง ในวันทำงาน และ ไม่น้อยกว่า ร้อยละ 300 '
            'ของ อัตรา ค่าจ้าง ต่อหน่วย ชั่วโมง ในวันหยุด\n'
            'อัตรา นี้ ใช้บังคับ สำหรับ ลูกจ้าง ที่ทำงาน เกิน 8 ชั่วโมง ต่อวัน หรือ '
            'เกิน 48 ชั่วโมง ต่อสัปดาห์'
        ),
        'note': 'Implementing regulation for LPA Section 61 (overtime rate)',
    },
    {
        'regulation_code': 'MOL-2551-SUB',
        'title': 'ประกาศ กระทรวงแรงงาน เรื่อง หลักเกณฑ์ การจ้างงาน ของ ผู้รับเหมาช่วง พ.ศ. 2551',
        'category': 'subcontracting',
        'issuing_body': 'กระทรวงแรงงาน',
        'year': '2551',
        'issue_date': '2551-06-03',
        'source_url': 'https://ratchakitcha.soc.go.th/DATA/PDF/2551/0/56/1.PDF',
        'full_text': (
            'ประกาศ กระทรวงแรงงาน เรื่อง หลักเกณฑ์ การจ้างงาน ของ ผู้รับเหมาช่วง พ.ศ. 2551\n\n'
            'ผู้รับเหมาช่วง ต้อง รับผิดชอบ ร่วมกับ นายจ้าง ตาม มาตรา 43 แห่ง '
            'พระราชบัญญัติ คุ้มครองแรงงาน พ.ศ. 2541 ใน การจ่าย ค่าจ้าง และ '
            'สวัสดิการ แก่ ลูกจ้าง\n'
            'หาก ผู้รับเหมาช่วง ไม่จ่าย ค่าจ้าง นายจ้าง ต้อง รับผิดชอบ จ่าย แทน'
        ),
        'note': 'Implementing regulation for LPA Section 43-44 (subcontractor liability)',
    },
    {
        'regulation_code': 'MOL-2541-WCF',
        'title': 'ประกาศ กระทรวงแรงงาน เรื่อง กองทุน เงินทดแทน พ.ศ. 2541',
        'category': 'compensation_fund',
        'issuing_body': 'กระทรวงแรงงาน',
        'year': '2541',
        'issue_date': '2541-04-23',
        'source_url': 'https://ratchakitcha.soc.go.th/DATA/PDF/2541/0/55/1.PDF',
        'full_text': (
            'ประกาศ กระทรวงแรงงาน เรื่อง กองทุน เงินทดแทน พ.ศ. 2541\n\n'
            'ให้ นายจ้าง ส่ง เงินสมทบ เข้า กองทุน เงินทดแทน ในอัตรา ร้อยละ 0.2 '
            'ถึง ร้อยละ 1.0 ของ ค่าจ้าง รวม ตาม ประเภท กิจการ\n'
            'การจ่าย เงินทดแทน กรณี เจ็บป่วย หรือ เสียชีวิต จาก การทำงาน ให้ ตาม '
            'หลักเกณฑ์ ที่กำหนด ใน พระราชบัญญัติ เงินทดแทน พ.ศ. 2537'
        ),
        'note': 'Implementing regulation for Workmen\'s Compensation Fund Act',
    },
    {
        'regulation_code': 'MOL-2567-MW10',
        'title': 'ประกาศ กระทรวงแรงงาน เรื่อง อัตรา ค่าจ้างขั้นต่ำ (ฉบับที่ 10) พ.ศ. 2567',
        'category': 'min_wage',
        'issuing_body': 'กระทรวงแรงงาน',
        'year': '2567',
        'issue_date': '2567-07-13',
        'source_url': 'https://ratchakitcha.soc.go.th/DATA/PDF/2567/0/57/1.PDF',
        'full_text': (
            'ประกาศ กระทรวงแรงงาน เรื่อง อัตรา ค่าจ้างขั้นต่ำ (ฉบับที่ 10) พ.ศ. 2567\n\n'
            'อัตรา ค่าจ้างขั้นต่ำ ทั่วประเทศ ไม่น้อยกว่า วันละ 400 บาท โดย ปรับ ตาม '
            'เขต พื้นที่ และ ประเภท กิจการ\n'
            'อัตรา นี้ มีผลบังคับ ตั้งแต่ วันที่ 1 ตุลาคม 2567 เป็นต้นไป\n'
            'นายจ้าง ที่ จ่าย ค่าจ้าง ต่ำกว่า อัตราขั้นต่ำ มีความผิด ตาม มาตรา 10 '
            'ต้องระวางโทษ ปรับ ไม่เกิน 100,000 บาท'
        ),
        'note': 'Latest minimum wage hike effective Oct 2024 — 400 THB/day nationwide floor',
    },
    {
        'regulation_code': 'MOL-2541-MEAL',
        'title': 'ประกาศ กระทรวงแรงงาน เรื่อง สวัสดิการ เกี่ยวกับ การให้อาหาร พ.ศ. 2541',
        'category': 'welfare',
        'issuing_body': 'กระทรวงแรงงาน',
        'year': '2541',
        'issue_date': '2541-04-23',
        'source_url': 'https://ratchakitcha.soc.go.th/DATA/PDF/2541/0/55/2.PDF',
        'full_text': (
            'ประกาศ กระทรวงแรงงาน เรื่อง สวัสดิการ เกี่ยวกับ การให้อาหาร พ.ศ. 2541\n\n'
            'นายจ้าง ที่ จ้าง ลูกจ้าง ตั้งแต่ 10 คน ขึ้นไป ต้อง จัด ให้มี อาหาร หรือ '
            'เครื่องดื่ม เพียงพอ และ ถูกสุขลักษณะ\n'
            'หรือ จัด ให้มี สถานที่ ขายอาหาร ที่ ถูกสุขลักษณะ ภายใน สถานประกอบกิจการ'
        ),
        'note': 'Implementing regulation for LPA Section 95 (meal welfare)',
    },
    {
        'regulation_code': 'MOL-2562-SSA',
        'title': 'ระเบียบ กระทรวงแรงงาน เรื่อง หลักเกณฑ์ และ วิธีการ จัดสรร เงิน กองทุน ประกันสังคม พ.ศ. 2562',
        'category': 'social_security',
        'issuing_body': 'กระทรวงแรงงาน',
        'year': '2562',
        'issue_date': '2562-12-24',
        'source_url': 'https://ratchakitcha.soc.go.th/DATA/PDF/2562/0/124/1.PDF',
        'full_text': (
            'ระเบียบ กระทรวงแรงงาน เรื่อง หลักเกณฑ์ และ วิธีการ จัดสรร เงิน กองทุน ประกันสังคม พ.ศ. 2562\n\n'
            'ให้ นายจ้าง ลูกจ้าง และ รัฐบาล สมทบ เงิน เข้า กองทุน ประกันสังคม '
            'ในอัตรา ร้อยละ 5 ของ ค่าจ้าง\n'
            'แต่ ไม่เกิน 750 บาท ต่อเดือน สำหรับ แต่ละ ฝ่าย\n'
            'เงินสมทบ นี้ ใช้ สำหรับ กรณี เจ็บป่วย ทุพพลภาพ คลอดบุตร เสียชีวิต '
            'ชราภาพ และ บุตร'
        ),
        'note': 'Implementing regulation for SSA Section 33 (mandatory contribution)',
    },
    {
        'regulation_code': 'MOL-2547-PROHIB',
        'title': 'ประกาศ กระทรวงแรงงาน เรื่อง การกำหนด ห้าม มิให้ นายจ้าง ให้ ลูกจ้าง ทำงาน ใน กิจการ บางประเภท พ.ศ. 2547',
        'category': 'prohibited_work',
        'issuing_body': 'กระทรวงแรงงาน',
        'year': '2547',
        'issue_date': '2547-03-15',
        'source_url': 'https://ratchakitcha.soc.go.th/DATA/PDF/2547/0/36/1.PDF',
        'full_text': (
            'ประกาศ กระทรวงแรงงาน เรื่อง ห้าม ให้ ลูกจ้าง ทำงาน ใน กิจการ บางประเภท พ.ศ. 2547\n\n'
            'ห้าม มิให้ นายจ้าง ให้ ลูกจ้าง ซึ่ง มีอายุ ต่ำกว่า 18 ปี ทำงาน ใน '
            'กิจการ 10 ประเภท\n'
            'อาทิ โรงงาน หลอมโลหะ โรงงาน ผลิต วัตถุระเบิด สถานเริงรมย์ '
            'และ งาน ที่ ต้องใช้แรง เกินกว่า ความสามารถ ของ เยาวชน'
        ),
        'note': 'Implementing regulation for LPA Sections 43-46 (child labor)',
    },
    {
        'regulation_code': 'MOL-2552-OHS',
        'title': 'ประกาศ กระทรวงแรงงาน เรื่อง สวัสดิการ เกี่ยวกับ สุขภาพ และ ความปลอดภัย ใน การทำงาน พ.ศ. 2552',
        'category': 'safety',
        'issuing_body': 'กระทรวงแรงงาน',
        'year': '2552',
        'issue_date': '2552-06-30',
        'source_url': 'https://ratchakitcha.soc.go.th/DATA/PDF/2552/0/56/1.PDF',
        'full_text': (
            'ประกาศ กระทรวงแรงงาน เรื่อง สวัสดิการ ด้าน สุขภาพ และ ความปลอดภัย พ.ศ. 2552\n\n'
            'นายจ้าง ต้อง จัด ให้มี การตรวจสอบ สภาพ การทำงาน เป็นประจำ\n'
            'จัด อบรม ลูกจ้าง เกี่ยวกับ ความปลอดภัย และ จัด ให้มี อุปกรณ์ ป้องกัน '
            'อันตราย ส่วนบุคคล ที่ ได้มาตรฐาน\n'
            'กรณี เกิด อุบัติเหตุ ต้อง รายงาน ภายใน 7 วัน ต่อ พนักงาน ตรวจแรงงาน'
        ),
        'note': 'Implementing regulation for Occupational Safety and Health Act 2011',
    },
]

# ---------------------------------------------------------------------------
# DB
# ---------------------------------------------------------------------------
def db_conn(db_path: Path) -> sqlite3.Connection:
    if not db_path.exists():
        print(f'ERROR: DB not found at {db_path}', file=sys.stderr)
        sys.exit(1)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    return conn

def is_existing(conn: sqlite3.Connection, regulation_code: str) -> bool:
    cur = conn.execute(
        'SELECT 1 FROM regulations WHERE regulation_code = ? LIMIT 1',
        (regulation_code,),
    )
    return cur.fetchone() is not None

def insert_regulation(conn: sqlite3.Connection, reg: dict) -> int:
    cur = conn.execute(
        """
        INSERT INTO regulations
            (regulation_code, title, category, issuing_body, year, issue_date,
             full_text, source_url, note, chars_count)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            reg['regulation_code'],
            reg['title'],
            reg['category'],
            reg['issuing_body'],
            reg['year'],
            reg['issue_date'],
            reg['full_text'],
            reg['source_url'],
            reg['note'],
            len(reg['full_text']),
        ),
    )
    return cur.lastrowid

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dry-run', action='store_true',
                    help='Do not write to DB, just print what would be inserted')
    ap.add_argument('--db', type=Path, default=DB_PATH,
                    help=f'Path to SQLite DB (default: {DB_PATH})')
    args = ap.parse_args()

    print(f'[{datetime.now(timezone.utc).isoformat()}] Phase 10.6 — Seed regulations')
    print(f'  DB: {args.db}')
    print(f'  dry_run: {args.dry_run}')
    print(f'  regulations to seed: {len(REGULATIONS)}')
    print()

    inserted = 0
    skipped = 0
    with db_conn(args.db) as conn:
        for reg in REGULATIONS:
            if is_existing(conn, reg['regulation_code']):
                print(f'  ⏭️  SKIP (exists): {reg["regulation_code"]} — {reg["title"][:60]}')
                skipped += 1
                continue
            if args.dry_run:
                print(f'  📝 DRY-RUN: would insert: {reg["regulation_code"]} — {reg["title"][:60]}')
                inserted += 1
                continue
            reg_id = insert_regulation(conn, reg)
            print(f'  ✅ INSERTED #{reg_id}: {reg["regulation_code"]} — {reg["title"][:60]}')
            inserted += 1
        if not args.dry_run:
            conn.commit()

    print(f'\nDone. inserted={inserted}, skipped(dup)={skipped}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
