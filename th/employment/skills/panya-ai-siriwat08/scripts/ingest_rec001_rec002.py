#!/usr/bin/env python3
"""
REC-001 + REC-002 — Ingest new laws to Turso production DB.

Adds two missing critical laws identified in the Genspark review:

1. B31 — ประมวลกฎหมายยาเสพติด พ.ศ. 2564 (REC-001)
   Replaces B29 (พ.ร.บ.ยาเสพติดให้โทษ 2522) and B30 (พ.ร.บ.มาตรการปราบปรามฯ 2534)
   which were both repealed when the Narcotics Code came into force on 9 Dec 2024.

2. B32 — พ.ร.บ.คุ้มครองแรงงาน (ฉบับที่ 8) พ.ศ. 2566 — Work from Home (REC-002)
   Adds มาตรา 23/1 on work-from-home rights — critical for modern HR.

The script:
  - Reads the markdown source files from data/
  - Parses YAML frontmatter + section text
  - Inserts into Turso: laws, law_sections, rag_chunks tables
  - Marks B29 + B30 as 'repealed' (does NOT delete — keeps historical record)
  - Idempotent: re-running skips existing rows by law_code

Usage:
    TURSO_URL=https://panya-ai-siriwat08.aws-ap-northeast-1.turso.io \
    TURSO_TOKEN=eyJ... \
    python3 scripts/ingest_rec001_rec002.py
"""
from __future__ import annotations
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / 'data'

TURSO_URL = os.environ.get('TURSO_URL', '').replace('libsql://', 'https://')
TURSO_TOKEN = os.environ.get('TURSO_TOKEN') or os.environ.get('TURSO_AUTH_TOKEN')

# ---------------------------------------------------------------------------
# Turso HTTP API client
# ---------------------------------------------------------------------------
def turso_execute(sql: str, params: list = None) -> dict:
    if not TURSO_URL or not TURSO_TOKEN:
        print('ERROR: TURSO_URL and TURSO_TOKEN must be set', file=sys.stderr)
        sys.exit(1)
    stmt = {'sql': sql}
    if params:
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
            else:
                encoded.append({'type': 'text', 'value': str(p)})
        stmt['args'] = encoded
    body = json.dumps({'requests': [{'type': 'execute', 'stmt': stmt}]}).encode()
    req = urllib.request.Request(
        f'{TURSO_URL}/v2/pipeline',
        data=body,
        headers={'Authorization': f'Bearer {TURSO_TOKEN}', 'Content-Type': 'application/json'},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
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
# Markdown parser
# ---------------------------------------------------------------------------
def parse_markdown_with_frontmatter(filepath: Path) -> tuple[dict, str]:
    """Parse a markdown file with YAML frontmatter. Returns (metadata, body)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.startswith('---'):
        return {}, content
    # Find end of frontmatter
    end_idx = content.find('\n---', 3)
    if end_idx == -1:
        return {}, content
    frontmatter = content[3:end_idx].strip()
    body = content[end_idx + 4:].strip()
    # Parse simple YAML (key: value)
    metadata = {}
    for line in frontmatter.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if ':' in line:
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip()
            # Strip quotes
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            metadata[key] = value
    return metadata, body

def extract_sections(body: str) -> list[dict]:
    """Extract law sections from markdown body using มาตรา N as delimiter."""
    # Pattern: มาตรา followed by number (Thai or Arabic digits)
    THAI_DIGITS = '๐๑๒๓๔๕๖๗๘๙'
    ARABIC_DIGITS = '0123456789'
    DIGIT_MAP = str.maketrans(THAI_DIGITS, ARABIC_DIGITS)
    # Normalize digits in body for matching, but keep original for storage
    normalized = body.translate(DIGIT_MAP)
    # Find all "มาตรา N" positions
    pattern = re.compile(r'^มาตรา\s+(\d+)', re.MULTILINE)
    matches = list(pattern.finditer(normalized))
    if not matches:
        return []
    sections = []
    for i, m in enumerate(matches):
        section_num = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        # Get text from original body (preserve Thai digits)
        section_text = body[start:end].strip()
        sections.append({
            'section_number': section_num,
            'section_text': section_text,
        })
    return sections

# ---------------------------------------------------------------------------
# Ingestion
# ---------------------------------------------------------------------------
def get_next_law_id() -> int:
    """Get the next available law_id (max + 1)."""
    rows = turso_query('SELECT MAX(law_id) as max_id FROM laws')
    max_id = rows[0].get('max_id') if rows else 0
    return (max_id or 0) + 1

def get_next_section_id() -> int:
    """Get the next available section_id (max + 1)."""
    rows = turso_query('SELECT MAX(section_id) as max_id FROM law_sections')
    max_id = rows[0].get('max_id') if rows else 0
    return (max_id or 0) + 1

def get_next_chunk_id() -> int:
    """Get the next available chunk_id (max + 1)."""
    rows = turso_query('SELECT MAX(chunk_id) as max_id FROM rag_chunks')
    max_id = rows[0].get('max_id') if rows else 0
    return (max_id or 0) + 1

def law_exists(law_code: str) -> int | None:
    """Check if a law with the given law_code already exists. Returns law_id or None."""
    rows = turso_query(f"SELECT law_id FROM laws WHERE law_code = '{law_code}' LIMIT 1")
    return rows[0].get('law_id') if rows else None

def mark_law_as_repealed(law_code: str, replaced_by: str) -> None:
    """Mark a law as repealed (status update, does NOT delete)."""
    rows = turso_query(f"SELECT law_id FROM laws WHERE law_code = '{law_code}' LIMIT 1")
    if not rows:
        print(f'  ⚠️  Law {law_code} not found — cannot mark as repealed')
        return
    law_id = rows[0]['law_id']
    turso_execute(
        "UPDATE laws SET status = 'repealed', note = COALESCE(note, '') || ? WHERE law_id = ?",
        [f'\n\n[Repealed] This law was repealed and replaced by {replaced_by} on 9 Dec 2024. Kept for historical reference only.', law_id]
    )
    print(f'  ✓ Marked {law_code} (law_id={law_id}) as repealed, replaced by {replaced_by}')

def ingest_law(law_code: str, title: str, year: str, category: str,
               law_group: str, law_type: str, krisdika_sysid: str,
               source_url: str, full_text: str, sections_count: int,
               chars_count: int) -> int:
    """Insert a new law. Returns the law_id."""
    law_id = get_next_law_id()
    turso_execute('''
        INSERT INTO laws (law_id, law_code, title, category, law_group, law_type, year,
                          krisdika_sysid, source_url, full_text, sections_count,
                          chars_count, status, note)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'complete', ?)
    ''', [law_id, law_code, title, category, law_group, law_type, year,
          krisdika_sysid, source_url, full_text, sections_count, chars_count,
          f'Ingested by ingest_rec001_rec002.py at {datetime.now(timezone.utc).isoformat()}'])
    return law_id

def ingest_section(law_id: int, section_id: int, section_number: str,
                   section_text: str, is_labor_related: int = 0) -> None:
    """Insert a law section."""
    turso_execute('''
        INSERT INTO law_sections (section_id, law_id, section_number, section_text,
                                  is_labor_related)
        VALUES (?, ?, ?, ?, ?)
    ''', [section_id, law_id, section_number, section_text, is_labor_related])

def ingest_rag_chunk(chunk_id: int, source_type: str, source_id: int,
                     source_code: str, chunk_text: str) -> None:
    """Insert a RAG chunk."""
    turso_execute('''
        INSERT INTO rag_chunks (chunk_id, source_type, source_id, source_code, chunk_text)
        VALUES (?, ?, ?, ?, ?)
    ''', [chunk_id, source_type, source_id, source_code, chunk_text])

# ---------------------------------------------------------------------------
# Main ingestion
# ---------------------------------------------------------------------------
def ingest_narcotics_code():
    """REC-001: Ingest ประมวลกฎหมายยาเสพติด พ.ศ. 2564."""
    print('\n[REC-001] Ingesting ประมวลกฎหมายยาเสพติด พ.ศ. 2564 (B31)...')
    filepath = DATA_DIR / 'B31_ประมวลกฎหมายยาเสพติด_พ.ศ.2564.md'
    if not filepath.exists():
        print(f'  ✗ Source file not found: {filepath}')
        return False
    metadata, body = parse_markdown_with_frontmatter(filepath)
    sections = extract_sections(body)
    print(f'  Parsed: {len(sections)} sections, {len(body)} chars')

    # Check if already ingested
    existing = law_exists('B31')
    if existing:
        print(f'  ⏭️  B31 already exists (law_id={existing}) — skipping')
        return True

    # Insert law
    law_id = ingest_law(
        law_code='B31',
        title=metadata.get('title', 'ประมวลกฎหมายยาเสพติด พ.ศ. 2564'),
        year='2564',
        category='criminal',
        law_group='สาธารณสุข',
        law_type='ประมวลกฎหมาย',
        krisdika_sysid=metadata.get('krisdika_sysid', '780849'),
        source_url=metadata.get('source_url', 'https://www.ratchakitcha.soc.go.th/DATA/PDF/2564/A/073/T_0001.PDF'),
        full_text=body,
        sections_count=len(sections),
        chars_count=len(body),
    )
    print(f'  ✓ Inserted law B31 (law_id={law_id})')

    # Insert sections
    next_section_id = get_next_section_id()
    next_chunk_id = get_next_chunk_id()
    for i, section in enumerate(sections):
        section_id = next_section_id + i
        ingest_section(law_id, section_id, section['section_number'],
                       section['section_text'], is_labor_related=0)
        # Also insert as RAG chunk
        chunk_id = next_chunk_id + i
        ingest_rag_chunk(chunk_id, 'law_section', section_id, 'B31',
                         section['section_text'])
    print(f'  ✓ Inserted {len(sections)} sections + {len(sections)} RAG chunks')

    # Mark B29 and B30 as repealed
    print('\n  Marking old laws as repealed (keeping for historical reference):')
    mark_law_as_repealed('B29', 'B31 (ประมวลกฎหมายยาเสพติด พ.ศ. 2564)')
    mark_law_as_repealed('B30', 'B31 (ประมวลกฎหมายยาเสพติด พ.ศ. 2564)')
    return True

def ingest_work_from_home():
    """REC-002: Ingest พ.ร.บ.คุ้มครองแรงงาน (ฉบับที่ 8) พ.ศ. 2566 — Work from Home."""
    print('\n[REC-002] Ingesting พ.ร.บ.คุ้มครองแรงงาน (ฉบับที่ 8) Work from Home (B32)...')
    filepath = DATA_DIR / 'B32_พระราชบัญญัติคุ้มครองแรงงานฉบับที่8_พ.ศ.2566.md'
    if not filepath.exists():
        print(f'  ✗ Source file not found: {filepath}')
        return False
    metadata, body = parse_markdown_with_frontmatter(filepath)
    sections = extract_sections(body)
    print(f'  Parsed: {len(sections)} sections, {len(body)} chars')

    # Check if already ingested
    existing = law_exists('B32')
    if existing:
        print(f'  ⏭️  B32 already exists (law_id={existing}) — skipping')
        return True

    # Insert law
    law_id = ingest_law(
        law_code='B32',
        title=metadata.get('title', 'พระราชบัญญัติคุ้มครองแรงงาน (ฉบับที่ 8) พ.ศ. 2566 — Work from Home'),
        year='2566',
        category='labor',
        law_group='แรงงาน',
        law_type='พระราชบัญญัติ',
        krisdika_sysid=metadata.get('krisdika_sysid', ''),
        source_url=metadata.get('source_url', 'https://www.ratchakitcha.soc.go.th/DATA/PDF/2566/A/053/T_0001.PDF'),
        full_text=body,
        sections_count=len(sections),
        chars_count=len(body),
    )
    print(f'  ✓ Inserted law B32 (law_id={law_id})')

    # Insert sections
    next_section_id = get_next_section_id()
    next_chunk_id = get_next_chunk_id()
    for i, section in enumerate(sections):
        section_id = next_section_id + i
        # Mark as labor-related (this is a labor law amendment)
        ingest_section(law_id, section_id, section['section_number'],
                       section['section_text'], is_labor_related=1)
        # Also insert as RAG chunk
        chunk_id = next_chunk_id + i
        ingest_rag_chunk(chunk_id, 'law_section', section_id, 'B32',
                         section['section_text'])
    print(f'  ✓ Inserted {len(sections)} sections + {len(sections)} RAG chunks')
    return True

def verify_final_counts():
    """Print final Turso row counts."""
    print('\n=== Final Turso row counts ===')
    tables = ['laws', 'law_sections', 'rag_chunks']
    for t in tables:
        rows = turso_query(f'SELECT COUNT(*) as n FROM {t}')
        n = rows[0].get('n', 0) if rows else 0
        print(f'  {t:<20} {n:>8}')
    # Show repealed laws
    print('\n  Repealed laws (status = repealed):')
    rows = turso_query("SELECT law_code, title FROM laws WHERE status = 'repealed' ORDER BY law_code")
    for r in rows:
        print(f'    {r["law_code"]}: {r["title"][:60]}')

def main():
    print('=' * 60)
    print('REC-001 + REC-002 — Ingest new laws to Turso')
    print('=' * 60)
    print(f'Turso URL: {TURSO_URL}')

    ok1 = ingest_narcotics_code()
    ok2 = ingest_work_from_home()
    verify_final_counts()

    print(f'\n{"=" * 60}')
    if ok1 and ok2:
        print('✓ Done. Both laws ingested successfully.')
    else:
        print('⚠️  Some ingestion steps failed — check output above.')
    print('=' * 60)
    return 0 if (ok1 and ok2) else 1

if __name__ == '__main__':
    sys.exit(main())
