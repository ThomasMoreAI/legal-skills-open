"""Step 2: Insert cross_references using local JSON lookup."""
import sys, os, csv, json
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)

# Add scripts/ dir to path for shared config import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _db_config import get_turso_config, load_lookup, resolve_source

import libsql_experimental as libsql
TURSO_URL, TURSO_TOKEN = get_turso_config()

# Load lookups (shared helper from _db_config)
lookup = load_lookup()
print(f"Loaded lookups: laws={len(lookup.get('law',{}))}, judgments={len(lookup.get('judgment',{}))}", flush=True)

conn = libsql.connect(TURSO_URL, auth_token=TURSO_TOKEN)
cur = conn.cursor()
print("Connected", flush=True)


# Skip clear (table already empty)
print("Skipping clear (table already empty)", flush=True)

# Process CSV
csv_path = "/home/z/my-project/work/legal_data_v2/panya_ai_legal_data/cross_reference_map.csv"
rows_law = 0
rows_jud = 0
skipped = 0
errors = 0

print("Processing CSV...", flush=True)
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        if i % 100 == 0:
            print(f"  row {i} (law:{rows_law} jud:{rows_jud} skip:{skipped})", flush=True)
        try:
            doc_id = row.get('DocID', '').strip()
            law_id_str = row.get('LawID', '').strip()
            section = row.get('Section', '').strip()
            relevance = row.get('Relevance', '').strip()
            judgment_ids = row.get('JudgmentIDs', '').strip()

            if not doc_id or not law_id_str:
                continue

            source_type, source_id = resolve_source(doc_id, lookup)
            if source_id == 0:
                skipped += 1
                continue

            target_law_id = lookup['law'].get(law_id_str, 0)

            cur.execute(
                "INSERT INTO cross_references (source_type, source_id, source_code, target_type, target_id, target_code, relation_type, section_ref, notes) VALUES (?, ?, ?, 'law', ?, ?, 'related_law', ?, ?)",
                (source_type, source_id, doc_id, target_law_id, law_id_str, section, relevance[:300])
            )
            rows_law += 1

            if judgment_ids:
                for jid in judgment_ids.split():
                    target_jud_id = lookup['judgment'].get(jid, 0)
                    cur.execute(
                        "INSERT INTO cross_references (source_type, source_id, source_code, target_type, target_id, target_code, relation_type, section_ref, notes) VALUES (?, ?, ?, 'judgment', ?, ?, 'cited_by', ?, ?)",
                        (source_type, source_id, doc_id, target_jud_id, jid, section, relevance[:200])
                    )
                    rows_jud += 1
        except Exception as e:
            errors += 1
            if errors < 5:
                print(f"  ERR row {i}: {e}", flush=True)

conn.commit()
print(f"\nInserted: {rows_law} law-section refs + {rows_jud} judgment refs ({skipped} skipped, {errors} errors)", flush=True)

cur.execute("SELECT COUNT(*) FROM cross_references")
print(f"Total cross_references: {cur.fetchone()[0]}", flush=True)

print("\nBy source_type:", flush=True)
cur.execute("SELECT source_type, COUNT(*) FROM cross_references GROUP BY source_type")
for r in cur.fetchall():
    print(f"  {r[0]:25s}: {r[1]}", flush=True)

print("\nBy relation_type:", flush=True)
cur.execute("SELECT relation_type, COUNT(*) FROM cross_references GROUP BY relation_type")
for r in cur.fetchall():
    print(f"  {r[0]:25s}: {r[1]}", flush=True)

conn.close()
print("\nDONE")
