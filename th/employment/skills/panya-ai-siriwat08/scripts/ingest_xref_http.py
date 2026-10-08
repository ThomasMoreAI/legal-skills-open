"""Step 3: Insert cross_references using HTTP API (libsql Python crashes)."""
import sys, os, csv, json, requests, time
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)

# Add scripts/ dir to path for shared config import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _db_config import get_http_config, load_lookup, resolve_source

PIPELINE_URL, HTTP_HEADERS = get_http_config()


def execute_batch(statements: list):
    """Execute multiple SQL statements in one HTTP request."""
    if not statements:
        return []
    requests_body = []
    for sql, args in statements:
        req = {
            "type": "execute",
            "stmt": {
                "sql": sql,
                "args": [
                    {"type": "integer" if isinstance(a, int) else "text", "value": str(a)}
                    for a in args
                ]
            }
        }
        requests_body.append(req)
    requests_body.append({"type": "close"})

    resp = requests.post(
        PIPELINE_URL,
        headers=HTTP_HEADERS,
        json={"requests": requests_body},
        timeout=60,
    )
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code}: {resp.text[:500]}")
    return resp.json().get("results", [])


# Load lookups (shared helper from _db_config)
lookup = load_lookup()
print(f"Loaded lookups: laws={len(lookup.get('law',{}))}, judgments={len(lookup.get('judgment',{}))}", flush=True)


# Process CSV — collect all insert statements, then execute in batches of 50
csv_path = "/home/z/my-project/work/legal_data_v2/panya_ai_legal_data/cross_reference_map.csv"

INSERT_SQL = "INSERT INTO cross_references (source_type, source_id, source_code, target_type, target_id, target_code, relation_type, section_ref, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

batch = []
batch_size = 10  # small to avoid HTTP request size limits
total_law = 0
total_jud = 0
skipped = 0
errors = 0
flushed = 0

print("Processing CSV...", flush=True)
# Resume from row 350 (skip the rows we already processed)
START_ROW = 650  # set higher to resume
with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        if i < START_ROW:
            continue
        if i % 25 == 0:
            print(f"  row {i} (law:{total_law} jud:{total_jud} skip:{skipped} errs:{errors} flushed:{flushed})", flush=True)

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

            # Law-section ref
            batch.append((INSERT_SQL, (
                source_type, source_id, doc_id,
                'law', target_law_id, law_id_str,
                'related_law', section, relevance[:300]
            )))
            total_law += 1

            # Judgment refs
            if judgment_ids:
                for jid in judgment_ids.split():
                    target_jud_id = lookup['judgment'].get(jid, 0)
                    batch.append((INSERT_SQL, (
                        source_type, source_id, doc_id,
                        'judgment', target_jud_id, jid,
                        'cited_by', section, relevance[:200]
                    )))
                    total_jud += 1

            # Flush batch
            if len(batch) >= batch_size:
                try:
                    execute_batch(batch)
                    flushed += 1
                    # Small delay to avoid connection issues
                    if flushed % 20 == 0:
                        time.sleep(1)
                except Exception as e:
                    errors += 1
                    print(f"  flush ERR at row {i}: {e}", flush=True)
                    # On error, try smaller sub-batches
                    for single_stmt in batch:
                        try:
                            execute_batch([single_stmt])
                        except Exception as e2:
                            errors += 1
                batch = []
        except Exception as e:
            errors += 1
            if errors < 5:
                print(f"  ERR row {i}: {e}", flush=True)

# Flush remaining
if batch:
    try:
        execute_batch(batch)
    except Exception as e:
        print(f"  Final flush ERR: {e}", flush=True)
        errors += 1

print(f"\nInserted: {total_law} law-section refs + {total_jud} judgment refs ({skipped} skipped, {errors} errors)", flush=True)

# Verify
print("\nVerifying...", flush=True)
result = execute_batch([("SELECT source_type, COUNT(*) FROM cross_references GROUP BY source_type", [])])
print("By source_type:", flush=True)
try:
    rows = result[0]['response']['result']['rows']
    for r in rows:
        print(f"  {r[0]['value']:25s}: {r[1]['value']}", flush=True)
except Exception as e:
    print(f"  verify error: {e}", flush=True)

result = execute_batch([("SELECT COUNT(*) FROM cross_references", [])])
try:
    rows = result[0]['response']['result']['rows']
    print(f"\nTotal cross_references: {rows[0][0]['value']}", flush=True)
except Exception as e:
    print(f"  count error: {e}", flush=True)

print("\nDONE")
