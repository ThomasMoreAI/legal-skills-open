#!/usr/bin/env python3
"""
Rebuild Thai Legal Database — parse all laws that still have 0 sections
- Laws 1, 5, 7, 8, 13, 14: parse from `laws.full_text` (Thai numerals + annotations)
- Laws 2, 3 (Civil/Criminal Code): fix section_number (NULL → extract from text)
- Re-tag labor sections using article_key/text matching
- Add FTS5 virtual table for full-text search
- Build RAG-ready chunks table

Output: /home/z/my-project/data/thai_legal_db.sqlite
"""

import sqlite3
import re
import os
import json
from pathlib import Path

SRC_DB = '/home/z/my-project/upload/extracted/Thai Legal Data Extraction/thai_legal_database.sqlite'
OUT_DB = '/home/z/my-project/data/thai_legal_db.sqlite'
LABOR_JSON = '/home/z/my-project/upload/extracted/Thai Legal Data Extraction/labor_related_sections_in_other_laws.json'

# Thai digits → Arabic
THAI_DIGITS = '๐๑๒๓๔๕๖๗๘๙'
def thai_to_arabic(s: str) -> str:
    out = []
    for ch in s:
        if ch in THAI_DIGITS:
            out.append(str(THAI_DIGITS.index(ch)))
        else:
            out.append(ch)
    return ''.join(out)

def arabic_to_thai(s: str) -> str:
    mapping = {str(i): THAI_DIGITS[i] for i in range(10)}
    return ''.join(mapping.get(c, c) for c in s)

# Section header pattern: "มาตรา ๑" / "มาตรา ๑๒๓" / "มาตรา ๑๒๓/๔" / "มาตรา ๑๒[๑]"
# Match Thai numeral (and slash for sub-sections like 193/34)
SECTION_HEADER_RE = re.compile(
    r'มาตรา\s+([๐-๙]+(?:/[๐-๙]+)?)\s*(\[[^\]]*\])?'
)

def parse_sections_from_full_text(full_text: str):
    """
    Parse full_text into list of (section_number_thai, section_number_arabic, text).
    Handles Thai numerals, sub-sections (193/34), and annotations [1].
    """
    sections = []
    # Find all section header positions
    matches = list(SECTION_HEADER_RE.finditer(full_text))
    if not matches:
        return sections

    for i, m in enumerate(matches):
        section_num_thai = m.group(1)
        section_num_arabic = thai_to_arabic(section_num_thai)
        # Skip if this is inside an annotation like "ตามมาตรา ๑๒๓" - heuristic: only count if it's at line start or after newline
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(full_text)
        # Get text content between this header and the next
        text = full_text[start:end].strip()
        # Clean up: collapse whitespace runs, remove leading/trailing newlines
        text = re.sub(r'\s+', ' ', text).strip()
        # Remove trailing "มาตรา" that might have leaked
        # Limit length
        if len(text) < 3:
            continue
        sections.append({
            'section_number_thai': f'มาตรา {section_num_thai}',
            'section_number': section_num_arabic,
            'section_text': text[:10000],
        })
    return sections

def fix_section_number_from_text(text: str):
    """Extract section number from text that starts with 'มาตรา <thai_num>'."""
    if not text:
        return None, None
    m = SECTION_HEADER_RE.match(text.strip())
    if m:
        num_thai = m.group(1)
        return f'มาตรา {num_thai}', thai_to_arabic(num_thai)
    return None, None

def setup_schema(conn):
    """Create tables (drop existing for fresh build)."""
    conn.executescript("""
        DROP TABLE IF EXISTS sources;
        DROP TABLE IF EXISTS laws;
        DROP TABLE IF EXISTS law_sections;
        DROP TABLE IF EXISTS case_judgments;
        DROP TABLE IF EXISTS case_law_links;
        DROP TABLE IF EXISTS ingestion_log;
        DROP TABLE IF EXISTS rag_chunks;
        DROP TABLE IF EXISTS laws_fts;
        DROP TABLE IF EXISTS law_sections_fts;
        DROP TABLE IF EXISTS case_judgments_fts;

        CREATE TABLE sources (
            source_id INTEGER PRIMARY KEY,
            source_name TEXT NOT NULL,
            source_type TEXT,
            source_url TEXT,
            description TEXT,
            license TEXT
        );

        CREATE TABLE laws (
            law_id INTEGER PRIMARY KEY,
            law_name_th TEXT NOT NULL,
            law_name_en TEXT,
            year TEXT,
            krisdika_sysid TEXT,
            law_go_th_id TEXT,
            source_url TEXT,
            status TEXT DEFAULT 'pending',
            full_text TEXT,
            notes TEXT,
            category TEXT,
            is_labor_law INTEGER DEFAULT 0
        );

        CREATE TABLE law_sections (
            section_id INTEGER PRIMARY KEY AUTOINCREMENT,
            law_id INTEGER NOT NULL,
            article_key TEXT,
            section_number TEXT,
            section_text TEXT NOT NULL,
            notes TEXT,
            is_cancelled INTEGER DEFAULT 0,
            chapter TEXT,
            is_labor_related INTEGER DEFAULT 0,
            FOREIGN KEY (law_id) REFERENCES laws(law_id)
        );

        CREATE TABLE case_judgments (
            judgment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_number TEXT,
            case_year TEXT,
            court TEXT,
            category TEXT,
            category_code TEXT,
            issue_number TEXT,
            law_references TEXT,
            fact TEXT,
            decision TEXT,
            title TEXT,
            source_id INTEGER,
            source_url TEXT,
            license_note TEXT,
            FOREIGN KEY (source_id) REFERENCES sources(source_id)
        );

        CREATE TABLE case_law_links (
            link_id INTEGER PRIMARY KEY AUTOINCREMENT,
            judgment_id INTEGER,
            section_id INTEGER,
            law_id INTEGER,
            law_code TEXT,
            section_ref TEXT,
            FOREIGN KEY (judgment_id) REFERENCES case_judgments(judgment_id),
            FOREIGN KEY (section_id) REFERENCES law_sections(section_id),
            FOREIGN KEY (law_id) REFERENCES laws(law_id)
        );

        CREATE TABLE ingestion_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_name TEXT,
            record_count INTEGER,
            source_file TEXT,
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE rag_chunks (
            chunk_id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type TEXT,  -- 'law_section' or 'judgment'
            source_id INTEGER,
            law_id INTEGER,
            section_id INTEGER,
            judgment_id INTEGER,
            chunk_text TEXT,
            chunk_metadata TEXT  -- JSON
        );

        CREATE INDEX idx_sections_law ON law_sections(law_id);
        CREATE INDEX idx_sections_number ON law_sections(section_number);
        CREATE INDEX idx_sections_labor ON law_sections(is_labor_related);
        CREATE INDEX idx_judgments_category ON case_judgments(category);
        CREATE INDEX idx_links_judgment ON case_law_links(judgment_id);
        CREATE INDEX idx_links_section ON case_law_links(section_id);
        CREATE INDEX idx_chunks_type ON rag_chunks(source_type);
    """)
    conn.commit()

def log_ingest(conn, table, count, source, notes=''):
    conn.execute(
        "INSERT INTO ingestion_log (table_name, record_count, source_file, notes) VALUES (?, ?, ?, ?)",
        (table, count, source, notes)
    )
    conn.commit()

def main():
    os.makedirs(os.path.dirname(OUT_DB), exist_ok=True)
    if os.path.exists(OUT_DB):
        os.remove(OUT_DB)

    src = sqlite3.connect(SRC_DB)
    src.row_factory = sqlite3.Row
    out = sqlite3.connect(OUT_DB)
    out.row_factory = sqlite3.Row

    print('=== Setting up schema ===')
    setup_schema(out)

    # 1. Copy sources + add license column data
    print('=== Copying sources ===')
    PD_THAI_GOV = 'Public domain (Thai government)'
    PD_PYTHAINLP = 'Public domain (PyThaiNLP)'
    OPEN_DATA = 'Open data — verify per document'
    source_license_map = {
        1: PD_THAI_GOV,
        2: PD_PYTHAINLP,
        3: PD_PYTHAINLP,
        4: 'Academic use only — NOT for commercial use',
        5: PD_THAI_GOV,
        6: PD_THAI_GOV,
        7: OPEN_DATA,
        8: OPEN_DATA,
        9: 'Public domain (ThaiDeka — verify)',
    }
    src_sources = src.execute('SELECT * FROM sources').fetchall()
    for s in src_sources:
        out.execute(
            'INSERT INTO sources (source_id, source_name, source_type, source_url, description, license) VALUES (?, ?, ?, ?, ?, ?)',
            (s['source_id'], s['source_name'], s['source_type'], s['source_url'], s['description'],
             source_license_map.get(s['source_id'], 'Unknown'))
        )
    log_ingest(out, 'sources', len(src_sources), SRC_DB, 'Copied from source DB')

    # 2. Copy laws with new columns
    print('=== Copying laws ===')
    labor_law_ids = {1, 4, 5, 6, 7, 8}  # 6 dedicated labor laws
    # Source DB has: law_id, law_name_th, law_type (en), law_year (int),
    # source_id, source_url, krisdika_sysid, latest_version, status,
    # full_text, text_length, category, notes, law_go_th_id (int)
    # Map source category → our category if source's is empty
    law_category_map = {
        1: 'labor', 4: 'labor', 5: 'labor', 6: 'labor', 7: 'labor', 8: 'labor',
        2: 'civil', 3: 'criminal', 9: 'civil_procedure', 10: 'land',
        11: 'rent', 12: 'criminal_procedure', 13: 'narcotics', 14: 'traffic',
    }
    src_laws = src.execute('SELECT * FROM laws').fetchall()
    for l in src_laws:
        out.execute('''
            INSERT INTO laws (law_id, law_name_th, law_name_en, year, krisdika_sysid,
                              law_go_th_id, source_url, status, full_text, notes,
                              category, is_labor_law)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            l['law_id'], l['law_name_th'], l['law_type'],
            str(l['law_year']) if l['law_year'] else None,
            l['krisdika_sysid'],
            str(l['law_go_th_id']) if l['law_go_th_id'] else None,
            l['source_url'], l['status'],
            l['full_text'], l['notes'],
            l['category'] if l['category'] else law_category_map.get(l['law_id'], 'other'),
            1 if l['law_id'] in labor_law_ids else 0
        ))
    log_ingest(out, 'laws', len(src_laws), SRC_DB, 'Copied + added is_labor_law')

    # 3. Re-parse sections for laws that have 0 sections but have full_text
    print('\n=== Parsing sections from full_text (laws 1, 5, 7, 8, 13, 14) ===')
    laws_to_reparse = [1, 5, 7, 8, 13, 14]
    total_new_sections = 0
    for law_id in laws_to_reparse:
        law = out.execute('SELECT law_name_th, full_text FROM laws WHERE law_id=?', (law_id,)).fetchone()
        if not law or not law['full_text']:
            print(f'  Law #{law_id}: no full_text, skipping')
            continue
        sections = parse_sections_from_full_text(law['full_text'])
        # Dedupe by section_number (keep first occurrence)
        seen = set()
        unique = []
        for s in sections:
            if s['section_number'] in seen:
                continue
            seen.add(s['section_number'])
            unique.append(s)
        for s in unique:
            out.execute('''
                INSERT INTO law_sections (law_id, article_key, section_number, section_text, notes, is_cancelled, is_labor_related)
                VALUES (?, ?, ?, ?, NULL, 0, ?)
            ''', (
                law_id, s['section_number_thai'], s['section_number'], s['section_text'],
                1 if law_id in labor_law_ids else 0
            ))
        out.execute("UPDATE laws SET status='available' WHERE law_id=?", (law_id,))
        print(f'  Law #{law_id} {law["law_name_th"][:40]}: {len(unique)} sections parsed')
        total_new_sections += len(unique)
    log_ingest(out, 'law_sections', total_new_sections, 'full_text parser', 'Re-parsed laws 1,5,7,8,13,14')

    # 4. Copy existing parsed sections for laws 2,3,4,6,9,10,11,12 + fix section_number
    print('\n=== Copying existing sections + fixing section_number ===')
    fixed_count = 0
    copied_count = 0
    for law_id in [2, 3, 4, 6, 9, 10, 11, 12]:
        src_sections = src.execute('SELECT * FROM law_sections WHERE law_id=? ORDER BY section_id', (law_id,)).fetchall()
        for s in src_sections:
            # If section_number is NULL or empty, try to extract from section_text
            sec_num = s['section_number']
            article_key = s['article_key']
            if not sec_num or sec_num == 'None':
                ak, sn = fix_section_number_from_text(s['section_text'])
                if ak:
                    article_key = ak
                    sec_num = sn
                    fixed_count += 1
            # If article_key looks like "intro-1" replace with proper "มาตรา X"
            if article_key and article_key.startswith('intro-'):
                ak, sn = fix_section_number_from_text(s['section_text'])
                if ak:
                    article_key = ak
                    sec_num = sn
                    fixed_count += 1
            is_labor = 1 if law_id in labor_law_ids else 0
            out.execute('''
                INSERT INTO law_sections (law_id, article_key, section_number, section_text, notes, is_cancelled, chapter, is_labor_related)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                law_id, article_key, sec_num, s['section_text'], s['notes'],
                s['is_cancelled'] if s['is_cancelled'] is not None else 0,
                s['chapter'], is_labor
            ))
            copied_count += 1
        print(f'  Law #{law_id}: {len(src_sections)} sections copied')
    print(f'  Fixed section_number for {fixed_count} rows')
    log_ingest(out, 'law_sections', copied_count, SRC_DB, f'Copied existing + fixed {fixed_count} NULL section_numbers')

    # 5. Tag labor-related sections in ป.พ.พ. (law_id=2) and ป.อ. (law_id=3)
    print('\n=== Tagging labor-related sections ===')
    with open(LABOR_JSON, 'r', encoding='utf-8') as f:
        labor_data = json.load(f)

    # Civil Code labor sections (law_id=2)
    civil_labor_count = 0
    for section in labor_data.get('civil_code_labor_sections', []):
        article_num = section['article_key']  # e.g. "27" or "193/34"
        # Try Arabic and Thai numeral variants
        variants = [article_num, arabic_to_thai(article_num)]
        for v in variants:
            cur = out.execute('''
                UPDATE law_sections SET is_labor_related=1,
                    notes = COALESCE(notes || ' | ', '') || 'labor-related'
                WHERE law_id=2 AND (section_number=? OR article_key=?)
            ''', (v, f'มาตรา {v}'))
            civil_labor_count += cur.rowcount
    print(f'  Civil Code labor sections tagged: {civil_labor_count} rows')

    # Criminal Code labor sections (law_id=3)
    crim_labor_count = 0
    for section in labor_data.get('criminal_code_labor_sections', []):
        article_num = section['article_key']
        variants = [article_num, arabic_to_thai(article_num)]
        for v in variants:
            cur = out.execute('''
                UPDATE law_sections SET is_labor_related=1,
                    notes = COALESCE(notes || ' | ', '') || 'labor-related'
                WHERE law_id=3 AND (section_number=? OR article_key=?)
            ''', (v, f'มาตรา {v}'))
            crim_labor_count += cur.rowcount
    print(f'  Criminal Code labor sections tagged: {crim_labor_count} rows')

    # Also tag any section whose text contains labor keywords (as a safety net)
    print('  Tagging by keyword scan (safety net)...')
    labor_keywords = ['ลูกจ้าง', 'นายจ้าง', 'ค่าจ้าง', 'สัญญาจ้าง', 'แรงงาน', 'การจ้าง', 'เลิกจ้าง', 'ค่าชดเชย', 'สวัสดิการ']
    kw_count = 0
    for kw in labor_keywords:
        cur = out.execute('''
            UPDATE law_sections SET is_labor_related=1,
                notes = CASE WHEN notes IS NULL THEN 'kw:' || ? ELSE notes || ' | kw:' || ? END
            WHERE law_id IN (2, 3) AND section_text LIKE ?
              AND is_labor_related=0
        ''', (kw, kw, f'%{kw}%'))
        kw_count += cur.rowcount
    print(f'  Keyword-tagged additional: {kw_count} rows')

    # 6. Copy case_judgments + add license_note + derive title
    print('\n=== Copying case_judgments ===')
    src_judgments = src.execute('SELECT * FROM case_judgments ORDER BY judgment_id').fetchall()
    judgment_count = 0
    for j in src_judgments:
        # Determine license note based on category/source
        license_note = 'Public domain (Thai Supreme Court)'
        if j['category'] == 'criminal':
            license_note = 'TSCC Dataset — Academic use only, NOT for commercial use. Use via RAG only.'
        elif j['category'] == 'labor' and j['source_id'] == 9:
            license_note = 'ThaiDeka — verify terms before redistribution'
        # For labor judgments, the `decision` field actually stores the case TITLE
        # (from build script: j.get('title','') was inserted into `decision` column)
        # So we derive: title = old decision for labor; for criminal title = first 80 chars of fact
        title = None
        fact = j['fact']
        decision = j['decision']
        if j['category'] == 'labor':
            title = decision  # labor's `decision` was actually the title
            decision = None   # no real decision text
        else:
            # Criminal (TSCC): both fact and decision exist as actual text
            if fact:
                title = (fact[:80] + '...') if len(fact) > 80 else fact
        out.execute('''
            INSERT INTO case_judgments (judgment_id, case_number, case_year, court, category, category_code,
                                        issue_number, law_references, fact, decision, title, source_id, source_url, license_note)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            j['judgment_id'], j['case_number'],
            str(j['case_year']) if j['case_year'] else None,
            j['court'], j['category'], j['category_code'],
            str(j['issue_number']) if j['issue_number'] is not None else None,
            j['law_references'],
            fact, decision, title, j['source_id'], j['source_url'], license_note
        ))
        judgment_count += 1
    log_ingest(out, 'case_judgments', judgment_count, SRC_DB, 'Copied + added license_note + derived title')

    # 7. Skip source case_law_links (TSCC-style codes like "CC-288-00" not mapped to real sections)
    # We'll derive ALL links fresh from law_references in step 8 below
    print('\n=== Skipping source case_law_links (will re-derive from law_references) ===')

    # 8. Re-link case_law_links by parsing law_references (e.g. "พ.ร.บ.คุ้มครองแรงงาน ม.119; ป.พ.พ. ม.577")
    print('\n=== Re-linking case_law_links from law_references ===')
    law_name_keywords = {
        1: ['คุ้มครองแรงงาน', 'พรบคุ้มครองแรงงาน'],
        2: ['ปพพ', 'ป.พ.พ.', 'แพ่งและพาณิชย์'],
        3: ['ปอ', 'ป.อ.', 'อาญา'],
        4: ['ประกันสังคม'],
        5: ['เงินทดแทน'],
        6: ['แรงงานสัมพันธ์'],
        7: ['ผู้รับงานไปทำที่บ้าน', 'คุ้มครองผู้รับงาน'],
        8: ['จัดหางาน', 'คนหางาน'],
        9: ['วิธีพิจารณาความแพ่ง', 'วิธีพิจารณาความแพ่ง'],
        10: ['ที่ดิน', 'ประมวลกฎหมายที่ดิน'],
        11: ['เช่าเคหะ', 'ควบคุมการเช่า'],
        12: ['วิธีพิจารณาความอาญา'],
        13: ['ยาเสพติด'],
        14: ['จราจร'],
    }
    # Build pattern: find "ม.XX" or "มาตรา XX" inside law_references
    # Use \d instead of [0-9] for conciseness (SonarCloud S6353)
    section_ref_re = re.compile(r'มาตรา\s*([๐-๙]+(?:/[๐-๙]+)?|\d+(?:/\d+)?)|ม\.?\s*([๐-๙]+(?:/[๐-๙]+)?|\d+(?:/\d+)?)')

    judgments = out.execute('SELECT judgment_id, law_references FROM case_judgments WHERE law_references IS NOT NULL AND law_references != ""').fetchall()
    new_links_count = 0
    for j in judgments:
        refs = j['law_references']
        # Split by ; or ,
        parts = re.split(r'[;,]', refs)
        for part in parts:
            part = part.strip()
            if not part:
                continue
            # Find which law this part refers to
            matched_law_id = None
            for lid, kws in law_name_keywords.items():
                for kw in kws:
                    if kw in part:
                        matched_law_id = lid
                        break
                if matched_law_id:
                    break
            if not matched_law_id:
                continue
            # Find section number
            m = section_ref_re.search(part)
            if not m:
                continue
            sec_thai = m.group(1) or m.group(2)
            sec_arabic = thai_to_arabic(sec_thai) if sec_thai[0] in THAI_DIGITS else sec_thai
            # Find section_id
            sec_row = out.execute(
                'SELECT section_id FROM law_sections WHERE law_id=? AND (section_number=? OR article_key=?) LIMIT 1',
                (matched_law_id, sec_arabic, f'มาตรา {sec_thai}')
            ).fetchone()
            if sec_row:
                out.execute('''
                    INSERT INTO case_law_links (judgment_id, section_id, law_id, law_code, section_ref)
                    VALUES (?, ?, ?, ?, ?)
                ''', (j['judgment_id'], sec_row['section_id'], matched_law_id, f'L{matched_law_id}', sec_arabic))
                new_links_count += 1
    print(f'  Re-linked {new_links_count} judgment→section links from law_references')
    log_ingest(out, 'case_law_links', new_links_count, 'law_references parser', 'Re-derived from judgment.law_references')

    # 9. Build RAG chunks
    print('\n=== Building RAG chunks ===')
    chunk_count = 0
    # Law sections → 1 chunk each (sections are already self-contained)
    sections = out.execute('SELECT section_id, law_id, section_number, article_key, section_text FROM law_sections').fetchall()
    for s in sections:
        if not s['section_text'] or len(s['section_text']) < 10:
            continue
        meta = json.dumps({
            'law_id': s['law_id'],
            'section_id': s['section_id'],
            'section_number': s['section_number'],
            'article_key': s['article_key'],
        }, ensure_ascii=False)
        out.execute('''
            INSERT INTO rag_chunks (source_type, source_id, law_id, section_id, chunk_text, chunk_metadata)
            VALUES ('law_section', ?, ?, ?, ?, ?)
        ''', (s['section_id'], s['law_id'], s['section_id'], s['section_text'], meta))
        chunk_count += 1
    # Judgments → 1 chunk each (fact + decision)
    judgments = out.execute('SELECT judgment_id, case_number, case_year, category, fact, decision FROM case_judgments').fetchall()
    for j in judgments:
        text = (j['fact'] or '') + '\n\nคำพิพากษา: ' + (j['decision'] or '')
        if len(text.strip()) < 20:
            continue
        meta = json.dumps({
            'judgment_id': j['judgment_id'],
            'case_number': j['case_number'],
            'case_year': j['case_year'],
            'category': j['category'],
        }, ensure_ascii=False)
        out.execute('''
            INSERT INTO rag_chunks (source_type, source_id, judgment_id, chunk_text, chunk_metadata)
            VALUES ('judgment', ?, ?, ?, ?)
        ''', (j['judgment_id'], j['judgment_id'], text, meta))
        chunk_count += 1
    print(f'  RAG chunks: {chunk_count}')
    log_ingest(out, 'rag_chunks', chunk_count, 'db build', '1 chunk per section + 1 per judgment')

    # 10. Build FTS5 virtual tables
    print('\n=== Building FTS5 indexes ===')
    try:
        out.executescript('''
            CREATE VIRTUAL TABLE law_sections_fts USING fts5(
                section_text, article_key, law_id UNINDEXED, section_id UNINDEXED,
                content='law_sections', content_rowid='section_id'
            );
            INSERT INTO law_sections_fts(section_text, article_key, law_id, section_id)
                SELECT section_text, COALESCE(article_key, ''), law_id, section_id FROM law_sections;
        ''')
        print('  law_sections_fts created')
    except Exception as e:
        print(f'  FTS5 law_sections failed: {e}')

    try:
        out.executescript('''
            CREATE VIRTUAL TABLE case_judgments_fts USING fts5(
                fact, decision, case_number, judgment_id UNINDEXED, category UNINDEXED,
                content='case_judgments', content_rowid='judgment_id'
            );
            INSERT INTO case_judgments_fts(fact, decision, case_number, judgment_id, category)
                SELECT COALESCE(fact,''), COALESCE(decision,''), COALESCE(case_number,''), judgment_id, COALESCE(category,'')
                FROM case_judgments;
        ''')
        print('  case_judgments_fts created')
    except Exception as e:
        print(f'  FTS5 judgments failed: {e}')

    out.commit()

    # Final stats
    print('\n=== FINAL STATS ===')
    for q in [
        ('Laws', 'SELECT COUNT(*) FROM laws'),
        ('Laws available', "SELECT COUNT(*) FROM laws WHERE status='available'"),
        ('Sections total', 'SELECT COUNT(*) FROM law_sections'),
        ('Sections labor-related', 'SELECT COUNT(*) FROM law_sections WHERE is_labor_related=1'),
        ('Sections in labor laws', 'SELECT COUNT(*) FROM law_sections WHERE law_id IN (1,4,5,6,7,8)'),
        ('Judgments total', 'SELECT COUNT(*) FROM case_judgments'),
        ('Judgments labor', "SELECT COUNT(*) FROM case_judgments WHERE category='labor'"),
        ('Judgments criminal', "SELECT COUNT(*) FROM case_judgments WHERE category='criminal'"),
        ('Case law links', 'SELECT COUNT(*) FROM case_law_links'),
        ('RAG chunks', 'SELECT COUNT(*) FROM rag_chunks'),
    ]:
        n = out.execute(q[1]).fetchone()[0]
        print(f'  {q[0]:30s} {n:>8,}')

    # Sections per law
    print('\n=== SECTIONS PER LAW ===')
    for r in out.execute('SELECT l.law_id, l.law_name_th, l.is_labor_law, COUNT(s.section_id), length(l.full_text) FROM laws l LEFT JOIN law_sections s ON l.law_id = s.law_id GROUP BY l.law_id ORDER BY l.law_id'):
        flag = '[L]' if r[2] else '   '
        print(f'  {flag} #{r[0]:2d}  {r[3]:5d} sections  full_text={r[4] or 0:6d}b  {r[1][:45]}')

    # DB size
    out.close()
    src.close()
    size_mb = os.path.getsize(OUT_DB) / 1024 / 1024
    print(f'\n=== Output DB: {OUT_DB} ({size_mb:.2f} MB) ===')
    print('Done!')

if __name__ == '__main__':
    main()
