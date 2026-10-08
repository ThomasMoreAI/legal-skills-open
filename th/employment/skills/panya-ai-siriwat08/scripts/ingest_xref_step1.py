"""Step 1: Dump lookups to JSON file."""
import sys, os, json
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)

# Add scripts/ dir to path for shared config import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _db_config import get_turso_config, get_lookup_file

import libsql_experimental as libsql
TURSO_URL, TURSO_TOKEN = get_turso_config()
LOOKUP_FILE = get_lookup_file()

conn = libsql.connect(TURSO_URL, auth_token=TURSO_TOKEN)
cur = conn.cursor()

lookup = {}
print("Loading laws...", flush=True)
cur.execute("SELECT law_id, law_code FROM laws")
lookup['law'] = {r[1]: r[0] for r in cur.fetchall()}
print(f"  {len(lookup['law'])}", flush=True)

print("Loading judgments...", flush=True)
cur.execute("SELECT judgment_id, judgment_code FROM judgments")
lookup['judgment'] = {r[1]: r[0] for r in cur.fetchall()}
print(f"  {len(lookup['judgment'])}", flush=True)

print("Loading regulations...", flush=True)
cur.execute("SELECT regulation_id, regulation_code FROM regulations")
lookup['regulation'] = {r[1]: r[0] for r in cur.fetchall()}
print(f"  {len(lookup['regulation'])}", flush=True)

print("Loading templates...", flush=True)
cur.execute("SELECT template_id, template_code FROM contract_templates")
lookup['contract_template'] = {r[1]: r[0] for r in cur.fetchall()}
print(f"  {len(lookup['contract_template'])}", flush=True)

# Save JSON to a per-user work directory (avoids publicly-writable /tmp)
out_path = LOOKUP_FILE
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(lookup, f, ensure_ascii=False, indent=2)
print(f"\nSaved to {out_path} ({os.path.getsize(out_path)} bytes)", flush=True)

conn.close()
print("DONE", flush=True)
