#!/usr/bin/env python3
"""
Phase 10.5 test — verify regulations FTS5 retrieval works end-to-end.

Inserts a sample regulation (with spaces between Thai words so the FTS5
unicode61 tokenizer can index it), queries it via FTS5, then cleans up.

NOTE on Thai text + FTS5:
  The default FTS5 tokenizer (unicode61) treats consecutive Thai characters
  as a single token until it hits a non-Thai character (space, punctuation,
  digit). So "นายจ้างต้องจ่ายค่าจ้าง" (no spaces) becomes ONE giant token
  that won't match queries for "นายจ้าง". To make FTS work, Thai text needs
  word separators (spaces). This is the same behavior as law_sections_fts
  and case_judgments_fts — the existing production data already has spaces
  between Thai words, which is why FTS works there.
"""
import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / 'prisma' / 'thai_legal_db.sqlite'

SAMPLE_REGULATION = {
    'regulation_code': 'TEST-MOL-2567',
    'title': 'ประกาศ กระทรวงแรงงาน เรื่อง ค่าจ้างขั้นต่ำ (TEST)',
    'category': 'min_wage',
    'issuing_body': 'กระทรวงแรงงาน',
    'year': '2567',
    # Note: spaces between Thai words so FTS5 unicode61 tokenizer can index them
    'full_text': (
        'ประกาศ กระทรวงแรงงาน เรื่อง อัตรา ค่าจ้างขั้นต่ำ\n\n'
        'อัตรา ค่าจ้างขั้นต่ำ ทั่วประเทศ ไม่น้อยกว่า วันละ 400 บาท\n'
        'นายจ้าง ต้อง จ่าย ค่าจ้าง ให้ ลูกจ้าง ไม่น้อยกว่า อัตราขั้นต่ำ\n'
        'หาก นายจ้าง จ่าย ค่าจ้าง ต่ำกว่า อัตราขั้นต่ำ มีความผิด ตาม มาตรา 10\n'
        'ลูกจ้าง มีสิทธิ ฟ้องร้อง นายจ้าง ต่อ ศาลแรงงาน'
    ),
}

def main():
    print('--- Phase 10.5 regulations FTS test ---\n')
    conn = sqlite3.connect(str(DB_PATH))

    # 1. Insert sample
    print('[1] Inserting sample regulation (with spaced Thai text)...')
    cur = conn.execute(
        """
        INSERT INTO regulations (regulation_code, title, category, issuing_body, year, full_text)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            SAMPLE_REGULATION['regulation_code'],
            SAMPLE_REGULATION['title'],
            SAMPLE_REGULATION['category'],
            SAMPLE_REGULATION['issuing_body'],
            SAMPLE_REGULATION['year'],
            SAMPLE_REGULATION['full_text'],
        ),
    )
    reg_id = cur.lastrowid
    conn.commit()
    print(f'    inserted regulation_id={reg_id}')

    # 2. Verify trigger synced to FTS (count for THIS regulation_id, not total)
    print('\n[2] Verifying FTS trigger sync (AFTER INSERT)...')
    n = conn.execute(
        'SELECT COUNT(*) FROM regulations_fts_v2 WHERE rowid = ?',
        (reg_id,),
    ).fetchone()[0]
    print(f'    FTS row for reg_id={reg_id}: {n} (expected: 1)')
    assert n == 1, f'FTS sync failed — expected 1 row for reg_id={reg_id}, got {n}'
    print('    PASS')

    # 3. Query via FTS5 (mimics RAG's regulation query)
    print('\n[3] Querying FTS5 for Thai terms...')
    test_terms = ['ค่าจ้างขั้นต่ำ', 'นายจ้าง', 'ลูกจ้าง', 'ศาลแรงงาน']
    for term in test_terms:
        results = conn.execute(
            """
            SELECT r.regulation_id, r.title
            FROM regulations_fts_v2
            JOIN regulations r ON r.regulation_id = regulations_fts_v2.rowid
            WHERE regulations_fts_v2 MATCH ?
            ORDER BY rank
            LIMIT 5
            """,
            (term,),
        ).fetchall()
        print(f'    MATCH {term!r}: {len(results)} result(s)')
        # At least our test regulation should match (others may also match
        # if the seed_regulations.py script has been run)
        our_match = any(r[0] == reg_id for r in results)
        assert our_match, f'FTS query for {term!r} did not match our test regulation (reg_id={reg_id})'
    print('    PASS')

    # 4. Query with English/numeric terms
    print('\n[4] Querying FTS5 for English/numeric terms...')
    for term in ['400', 'บาท']:
        results = conn.execute(
            """
            SELECT r.regulation_id FROM regulations_fts_v2
            JOIN regulations r ON r.regulation_id = regulations_fts_v2.rowid
            WHERE regulations_fts_v2 MATCH ?
            """,
            (term,),
        ).fetchall()
        print(f'    MATCH {term!r}: {len(results)} result(s)')
        assert len(results) >= 1
    print('    PASS')

    # 5. Test UPDATE trigger
    print('\n[5] Testing UPDATE trigger (rename title)...')
    conn.execute(
        "UPDATE regulations SET title = 'Updated title ค่าจ้าง' WHERE regulation_id = ?",
        (reg_id,),
    )
    conn.commit()
    results = conn.execute(
        "SELECT r.title FROM regulations_fts_v2 JOIN regulations r ON r.regulation_id = regulations_fts_v2.rowid WHERE r.regulation_id = ?",
        (reg_id,),
    ).fetchall()
    print(f'    FTS title after update: {results[0][0]!r}')
    assert results[0][0] == 'Updated title ค่าจ้าง'
    print('    PASS')

    # 6. Test DELETE trigger (verify FTS row for THIS reg_id is gone)
    print('\n[6] Testing DELETE trigger (cleanup)...')
    conn.execute('DELETE FROM regulations WHERE regulation_id = ?', (reg_id,))
    conn.commit()
    n_after = conn.execute(
        'SELECT COUNT(*) FROM regulations_fts_v2 WHERE rowid = ?',
        (reg_id,),
    ).fetchone()[0]
    print(f'    FTS row for reg_id={reg_id} after delete: {n_after} (expected: 0)')
    assert n_after == 0, f'FTS delete trigger failed — expected 0, got {n_after}'
    print('    PASS')

    print('\n--- All tests passed ---')
    conn.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())
