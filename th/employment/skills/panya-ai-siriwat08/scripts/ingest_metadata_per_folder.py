"""Ingest a single folder of law files - invoked by parent process."""
import sys, os, traceback, json
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buffering=1)

# Add scripts/ dir to path for shared config import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _db_config import get_turso_config

import libsql_experimental as libsql
from pathlib import Path
import re

def parse_front_matter(text):
    if not text.startswith('---'):
        return {}
    end_idx = text.find('\n---', 3)
    if end_idx == -1:
        return {}
    yaml_block = text[3:end_idx].strip()
    result = {}
    for line in yaml_block.split('\n'):
        if not line.strip():
            continue
        m = re.match(r'^(\w+):\s?(.*)$', line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            result[key] = val
    return result

TURSO_URL, TURSO_TOKEN = get_turso_config()

folder = sys.argv[1]
update_type = sys.argv[2]  # 'laws' | 'regulations' | 'judgments'

conn = libsql.connect(TURSO_URL, auth_token=TURSO_TOKEN)
cur = conn.cursor()

folder_path = Path(folder)
md_files = sorted(folder_path.glob('*.md'))
print(f"{folder_path.name}: {len(md_files)} files", flush=True)

updated = 0
errors = 0
for md_file in md_files:
    try:
        text = md_file.read_text(encoding='utf-8')
        fm = parse_front_matter(text)
        if not fm or 'id' not in fm:
            continue
        code = fm['id']

        if update_type == 'laws':
            sets = []
            args = []
            for fld in ['krisdika_sysid', 'law_type', 'law_group', 'source_url']:
                if fm.get(fld):
                    sets.append(f'{fld} = ?')
                    args.append(str(fm[fld]))
            if not sets:
                continue
            args.append(code)
            sql = f"UPDATE laws SET {', '.join(sets)} WHERE law_code = ?"
            cur.execute(sql, tuple(args))
            if cur.rowcount > 0:
                updated += 1
        elif update_type == 'regulations':
            is_consolidated = fm.get('is_consolidated', 'false')
            if isinstance(is_consolidated, str):
                is_consolidated = is_consolidated.lower() == 'true'
            repeal_status = 'active' if is_consolidated else 'superseded'
            is_repealed = 0
            group = fm.get('group', '')
            law_type = fm.get('law_type', '')
            source_url = fm.get('source_url', '')
            cur.execute(
                "UPDATE regulations SET repeal_status = ?, is_repealed = ?, category = COALESCE(NULLIF(?, ''), category), issuing_body = COALESCE(NULLIF(?, ''), issuing_body), source_url = COALESCE(NULLIF(?, ''), source_url) WHERE regulation_code = ?",
                (repeal_status, is_repealed, group, law_type, source_url, code)
            )
            if cur.rowcount > 0:
                updated += 1
        elif update_type == 'judgments':
            topics = fm.get('topics', '')
            # topics might be inline list format: ["a", "b"]
            if isinstance(topics, str) and topics.startswith('['):
                import json
                try:
                    topics_list = json.loads(topics)
                    topics_str = json.dumps(topics_list, ensure_ascii=False)
                except (ValueError, TypeError):
                    topics_str = topics
            else:
                topics_str = topics if topics else None

            laws_cited = fm.get('laws_cited', '')
            if isinstance(laws_cited, str) and laws_cited.startswith('['):
                try:
                    laws_list = json.loads(laws_cited)
                    laws_cited_str = json.dumps(laws_list, ensure_ascii=False)
                except (ValueError, TypeError):
                    laws_cited_str = laws_cited
            else:
                laws_cited_str = laws_cited if laws_cited else None

            case_type_group = fm.get('case_type_group', '')
            topic = fm.get('topic', '')

            cur.execute(
                "UPDATE judgments SET topic = COALESCE(NULLIF(?, ''), topic), topics = ?, case_type_group = COALESCE(NULLIF(?, ''), case_type_group), laws_cited = ? WHERE judgment_code = ?",
                (topic, topics_str, case_type_group, laws_cited_str, code)
            )
            if cur.rowcount > 0:
                updated += 1
    except Exception as e:
        print(f"  ERR {md_file.name[:40]}: {e}", flush=True)
        errors += 1

conn.commit()
print(f"  → {updated} updated, {errors} errors", flush=True)
conn.close()
