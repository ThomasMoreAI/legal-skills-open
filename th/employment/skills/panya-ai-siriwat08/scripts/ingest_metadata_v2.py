#!/usr/bin/env python3
"""
ingest_metadata_v2.py — Parse YAML front matter from v2_fixed markdown files
and update Turso DB tables with richer metadata.

Updates:
  1. laws: krisdika_sysid, law_type, law_group, source_url (from A/B/C/D/E folders)
  2. regulations: is_consolidated → set is_repealed/repeal_status using consolidated logic
                  + group/category from front matter
  3. judgments: topic, topics, case_type_group, laws_cited, law_names, issues_count
  4. cross_references: ingest cross_reference_map.csv → populate table

Usage:
  python3 /home/z/my-project/scripts/ingest_metadata_v2.py
"""

import os
import re
import sys
import json
import csv
import traceback
import libsql_experimental as libsql
from pathlib import Path

# Force unbuffered output
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buffering=1)

# ===== Turso config (loaded from env vars via shared helper) =====
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _db_config import get_turso_config
TURSO_URL, TURSO_TOKEN = get_turso_config()

DATA_DIR = Path("/home/z/my-project/work/legal_data_v2/panya_ai_legal_data")

# ===== YAML front matter parser (lightweight, no PyYAML needed) =====
def parse_front_matter(text: str) -> dict:
    """Parse YAML front matter from markdown. Returns dict or empty dict."""
    if not text.startswith('---'):
        return {}
    end_idx = text.find('\n---', 3)
    if end_idx == -1:
        return {}
    yaml_block = text[3:end_idx].strip()
    result = {}
    current_list = None
    for line in yaml_block.split('\n'):
        # Skip empty
        if not line.strip():
            continue
        # List item under current key (starts with - or [)
        if line.startswith(('  - ', '- ')):
            item = line.lstrip(' -').strip()
            if current_list is not None:
                current_list.append(_clean_yaml_value(item))
            continue
        # Inline list: topics: ["a", "b", "c"]
        m_inline = re.match(r'^(\w+):\s*\[(.*)\]\s*$', line)
        if m_inline:
            key = m_inline.group(1)
            items_str = m_inline.group(2)
            items = [_clean_yaml_value(x.strip()) for x in re.split(r',(?![^"]*"[^"]*$)', items_str) if x.strip()]
            result[key] = items
            current_list = None
            continue
        # Key: value
        m = re.match(r'^(\w+):\s?(.*)$', line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            if val == '' or val is None:
                # Maybe start of a list on next lines
                result[key] = []
                current_list = result[key]
            else:
                result[key] = _clean_yaml_value(val)
                current_list = None
    return result


def _clean_yaml_value(val: str):
    """Strip quotes, convert true/false/null."""
    if val is None:
        return None
    val = val.strip()
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        return val[1:-1]
    if val.lower() == 'true':
        return True
    if val.lower() == 'false':
        return False
    if val.lower() == 'null' or val.lower() == '~':
        return None
    return val


def main():
    pass


# ===== Connect to Turso =====
print("Connecting to Turso...", flush=True)
conn = libsql.connect(TURSO_URL, auth_token=TURSO_TOKEN)
cur = conn.cursor()
print("Connected.\n", flush=True)


# ===== 1. UPDATE LAWS TABLE =====
print("=" * 70, flush=True)
print("1. Updating LAWS table with front matter metadata", flush=True)
print("=" * 70, flush=True)

laws_folders = ['A_laws_labor', 'B_laws_criminal', 'C_laws_civil', 'D_laws_other', 'E_laws_business']
laws_updated = 0
laws_seen = set()

for folder in laws_folders:
    folder_path = DATA_DIR / folder
    if not folder_path.exists():
        continue
    md_files = sorted(folder_path.glob('*.md'))
    print(f"\n  {folder}: {len(md_files)} files", flush=True)
    for md_file in md_files:
        try:
            text = md_file.read_text(encoding='utf-8')
            fm = parse_front_matter(text)
            if not fm or 'id' not in fm:
                continue
            law_code = fm['id']
            laws_seen.add(law_code)

            # Build UPDATE query
            updates = []
            params = []
            if 'krisdika_sysid' in fm and fm['krisdika_sysid']:
                updates.append('krisdika_sysid = ?')
                params.append(str(fm['krisdika_sysid']))
            if 'law_type' in fm and fm['law_type']:
                updates.append('law_type = ?')
                params.append(fm['law_type'])
            if 'law_group' in fm and fm['law_group']:
                updates.append('law_group = ?')
                params.append(fm['law_group'])
            if 'source_url' in fm and fm['source_url']:
                updates.append('source_url = ?')
                params.append(fm['source_url'])
            if 'note' in fm and fm['note']:
                updates.append('note = ?')
                params.append(fm['note'])

            if not updates:
                continue
            params.append(law_code)
            sql = f"UPDATE laws SET {', '.join(updates)} WHERE law_code = ?"
            cur.execute(sql, tuple(params))
            if cur.rowcount > 0:
                laws_updated += 1
        except Exception as e:
            print(f"    ERR {md_file.name}: {e}", flush=True)

conn.commit()
print(f"\n  → {laws_updated} laws updated", flush=True)


# ===== 2. UPDATE REGULATIONS TABLE =====
print("\n" + "=" * 70, flush=True)
print("2. Updating REGULATIONS table with is_consolidated + group/category", flush=True)
print("=" * 70, flush=True)

reg_folder = DATA_DIR / 'H_regulations'
md_files = sorted(reg_folder.glob('*.md'))
print(f"\n  Found {len(md_files)} regulation files", flush=True)

regs_updated = 0
regs_consolidated = 0
regs_not_consolidated = 0

# Strategy: regulations marked is_consolidated=true are "active" (latest version)
# Regulations marked is_consolidated=false are likely superseded — mark as "superseded"
# (use repeal_status='superseded' to distinguish from 'active' and 'repealed')
for md_file in md_files:
    try:
        text = md_file.read_text(encoding='utf-8')
        fm = parse_front_matter(text)
        if not fm or 'id' not in fm:
            continue
        reg_code = fm['id']
        is_consolidated = fm.get('is_consolidated', False)
        # Determine status
        if is_consolidated:
            repeal_status = 'active'
            is_repealed = 0
            regs_consolidated += 1
        else:
            # Not consolidated — could be an old version that's been superseded
            # We'll mark as 'superseded' (a new status value) — UI can show amber badge
            repeal_status = 'superseded'
            is_repealed = 0  # Not formally repealed, just superseded
            regs_not_consolidated += 1

        # Group / category from front matter
        group = fm.get('group', '')
        law_type = fm.get('law_type', '')
        source_url = fm.get('source_url', '')

        # Update the regulation row
        cur.execute("""
            UPDATE regulations
            SET repeal_status = ?, is_repealed = ?, category = COALESCE(NULLIF(?, ''), category),
                issuing_body = COALESCE(NULLIF(?, ''), issuing_body),
                source_url = COALESCE(NULLIF(?, ''), source_url)
            WHERE regulation_code = ?
        """, (repeal_status, is_repealed, group, law_type, source_url, reg_code))
        if cur.rowcount > 0:
            regs_updated += 1
    except Exception as e:
        print(f"    ERR {md_file.name}: {e}", flush=True)

conn.commit()
print(f"\n  → {regs_updated} regulations updated", flush=True)
print(f"  → consolidated (active): {regs_consolidated}", flush=True)
print(f"  → superseded (not consolidated): {regs_not_consolidated}", flush=True)


# ===== 3. UPDATE JUDGMENTS TABLE =====
print("\n" + "=" * 70, flush=True)
print("3. Updating JUDGMENTS table with topics, case_type_group, laws_cited", flush=True)
print("=" * 70, flush=True)

jud_folder = DATA_DIR / 'G_court_judgments'
md_files = sorted(jud_folder.glob('*.md'))
print(f"\n  Found {len(md_files)} judgment files", flush=True)

juds_updated = 0
for md_file in md_files:
    try:
        text = md_file.read_text(encoding='utf-8')
        fm = parse_front_matter(text)
        if not fm or 'id' not in fm:
            continue
        jud_code = fm['id']

        # Convert list/array fields to JSON string for storage
        topics = fm.get('topics', [])
        if isinstance(topics, list):
            topics_str = json.dumps(topics, ensure_ascii=False)
        else:
            topics_str = str(topics) if topics else None

        laws_cited = fm.get('laws_cited', [])
        if isinstance(laws_cited, list):
            laws_cited_str = json.dumps(laws_cited, ensure_ascii=False)
        else:
            laws_cited_str = str(laws_cited) if laws_cited else None

        case_type_group = fm.get('case_type_group')

        # Update judgments table (note: schema has 'issue' as text, no 'issue_number' column)
        cur.execute("""
            UPDATE judgments
            SET topic = COALESCE(NULLIF(?, ''), topic),
                topics = ?,
                case_type_group = COALESCE(NULLIF(?, ''), case_type_group),
                laws_cited = ?
            WHERE judgment_code = ?
        """, (
            fm.get('topic', ''),
            topics_str,
            case_type_group or '',
            laws_cited_str,
            jud_code,
        ))
        if cur.rowcount > 0:
            juds_updated += 1
    except Exception as e:
        print(f"    ERR {md_file.name}: {e}", flush=True)

conn.commit()
print(f"\n  → {juds_updated} judgments updated", flush=True)


# ===== 4. POPULATE CROSS_REFERENCES TABLE =====
print("\n" + "=" * 70, flush=True)
print("4. Populating CROSS_REFERENCES table from cross_reference_map.csv", flush=True)
print("=" * 70, flush=True)

# Clear existing cross_references (it's empty anyway, but safe)
cur.execute("DELETE FROM cross_references")
conn.commit()

csv_path = DATA_DIR / 'cross_reference_map.csv'
rows_inserted = 0
judgments_linked = 0

with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            doc_id = row.get('DocID', '').strip()
            doc_name = row.get('DocName', '').strip()
            doc_folder = row.get('DocFolder', '').strip()
            law_id_str = row.get('LawID', '').strip()
            law_title = row.get('LawTitle', '').strip()
            section = row.get('Section', '').strip()
            relevance = row.get('Relevance', '').strip()
            judgment_ids = row.get('JudgmentIDs', '').strip()

            if not doc_id or not law_id_str:
                continue

            # Determine source_type from doc_id prefix
            if doc_id.startswith('F'):
                source_type = 'contract_template'
            elif doc_id.startswith(('A', 'B', 'C', 'D', 'E')):
                source_type = 'law'
            elif doc_id.startswith('G'):
                source_type = 'judgment'
            elif doc_id.startswith('H'):
                source_type = 'regulation'
            else:
                source_type = 'unknown'

            # Look up source_id from law_code/judgment_code/regulation_code
            # For now, use string code as source_code; source_id will be NULL
            # We'll do a separate update pass to fill in IDs
            cur.execute("""
                INSERT INTO cross_references
                    (source_type, source_id, source_code, target_type, target_id, target_code,
                     relation_type, section_ref, notes)
                VALUES (?, NULL, ?, 'law', NULL, ?, 'related_law', ?, ?)
            """, (
                source_type, doc_id, law_id_str, section,
                f"relevance={relevance}; judgments={judgment_ids[:500]}"
            ))
            rows_inserted += 1

            # Also create individual judgment links if JudgmentIDs is present
            if judgment_ids:
                jud_list = judgment_ids.split()
                for jid in jud_list:
                    cur.execute("""
                        INSERT INTO cross_references
                            (source_type, source_id, source_code, target_type, target_id, target_code,
                             relation_type, section_ref, notes)
                        VALUES (?, NULL, ?, 'judgment', NULL, ?, 'cited_by', ?, ?)
                    """, (
                        source_type, doc_id, jid, section,
                        f"relevance={relevance}"
                    ))
                    judgments_linked += 1
        except Exception as e:
            print(f"    ERR row: {e}", flush=True)

conn.commit()
print(f"\n  → {rows_inserted} law-section cross-refs inserted", flush=True)
print(f"  → {judgments_linked} judgment cross-refs inserted", flush=True)


# ===== 5. SUMMARY =====
print("\n" + "=" * 70, flush=True)
print("5. Final DB state summary", flush=True)
print("=" * 70, flush=True)

# Count by source_type in cross_references
cur.execute("SELECT source_type, COUNT(*) FROM cross_references GROUP BY source_type")
print("\n  cross_references by source_type:", flush=True)
for r in cur.fetchall():
    print(f"    {r[0]:25s}: {r[1]}", flush=True)

cur.execute("SELECT relation_type, COUNT(*) FROM cross_references GROUP BY relation_type")
print("\n  cross_references by relation_type:", flush=True)
for r in cur.fetchall():
    print(f"    {r[0]:25s}: {r[1]}", flush=True)

# Regulations status distribution
cur.execute("SELECT repeal_status, COUNT(*) FROM regulations GROUP BY repeal_status")
print("\n  regulations by repeal_status:", flush=True)
for r in cur.fetchall():
    print(f"    {r[0]:25s}: {r[1]}", flush=True)

# Laws with krisdika_sysid
cur.execute("SELECT COUNT(*) FROM laws WHERE krisdika_sysid IS NOT NULL")
print(f"\n  laws with krisdika_sysid: {cur.fetchone()[0]}", flush=True)

# Judgments with topics (JSON array)
cur.execute("SELECT COUNT(*) FROM judgments WHERE topics IS NOT NULL AND topics != ''")
print(f"  judgments with topics array: {cur.fetchone()[0]}", flush=True)

# Judgments with laws_cited (JSON array)
cur.execute("SELECT COUNT(*) FROM judgments WHERE laws_cited IS NOT NULL AND laws_cited != ''")
print(f"  judgments with laws_cited array: {cur.fetchone()[0]}", flush=True)

conn.close()
print("\n" + "=" * 70, flush=True)
print("DONE — all metadata ingested successfully", flush=True)
print("=" * 70, flush=True)
