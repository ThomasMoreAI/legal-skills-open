"""Shared config for ingest scripts — loads Turso credentials from env vars.

Usage:
  from _db_config import get_turso_config, get_work_dir
  url, token = get_turso_config()
  work_dir = get_work_dir()  # safe per-user dir instead of /tmp

Or for HTTP API:
  from _db_config import get_http_config
  pipeline_url, headers = get_http_config()
"""

import os
import sys
import tempfile
from pathlib import Path


def _load_env_file():
    """Load .env file from project root or scripts/ directory.

    Looks for .env in:
      1. Current working directory
      2. Project root (parent of scripts/)
      3. /home/z/my-project/work/Panya-AI-final/

    Note: .env file values take precedence over shell env vars — this is
    intentional for ingest scripts that need the Turso DB URL, not whatever
    might be in the shell environment.
    """
    candidates = [
        Path.cwd() / '.env',
        Path(__file__).parent.parent / '.env',
        Path('/home/z/my-project/work/Panya-AI-final/.env'),
    ]
    for env_path in candidates:
        if not env_path.exists():
            continue
        try:
            with open(env_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#') or '=' not in line:
                        continue
                    key, _, value = line.partition('=')
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    # .env file takes precedence over shell env for ingest scripts
                    if key:
                        os.environ[key] = value
            return
        except OSError:
            continue


# Load .env on import
_load_env_file()


def get_turso_config():
    """Returns (url, token) tuple. Exits with error if not set."""
    url = os.environ.get('DATABASE_URL') or os.environ.get('TURSO_URL')
    token = os.environ.get('TURSO_AUTH_TOKEN') or os.environ.get('TURSO_TOKEN')

    if not url or not url.startswith('libsql://'):
        print('ERROR: DATABASE_URL or TURSO_URL must be set to a libsql:// URL', file=sys.stderr)
        print('Create a .env file with:', file=sys.stderr)
        print('  DATABASE_URL=libsql://your-db.turso.io', file=sys.stderr)
        print('  TURSO_AUTH_TOKEN=your-token-here', file=sys.stderr)
        sys.exit(1)

    if not token:
        print('ERROR: TURSO_AUTH_TOKEN or TURSO_TOKEN must be set', file=sys.stderr)
        print('Create a .env file with:', file=sys.stderr)
        print('  TURSO_AUTH_TOKEN=your-token-here', file=sys.stderr)
        sys.exit(1)

    return url, token


def get_http_config():
    """Returns (pipeline_url, headers_dict) for Turso HTTP API."""
    url, token = get_turso_config()
    # Convert libsql:// to https:// for HTTP API
    http_url = url.replace('libsql://', 'https://')
    pipeline_url = f"{http_url}/v2/pipeline"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    return pipeline_url, headers


def get_work_dir() -> Path:
    """Return a per-user working directory for intermediate files.

    Uses tempfile.gettempdir() + 'panya-ai-<uid>' instead of writing directly
    to /tmp — this avoids the S5443 (publicly writable directory) warning
    while still keeping files in a known location across runs.

    The directory is created with mode 0700 (owner-only) and returned as
    a Path object. Files written here are only readable by the current user.
    """
    uid = os.getuid() if hasattr(os, 'getuid') else 0
    base = Path(tempfile.gettempdir()) / f'panya-ai-{uid}'
    base.mkdir(mode=0o700, exist_ok=True)
    # Ensure restrictive permissions even if dir already existed
    try:
        os.chmod(base, 0o700)
    except OSError:
        pass
    return base


def get_lookup_file() -> Path:
    """Return the path to the code_lookup.json file in the safe work dir."""
    return get_work_dir() / 'code_lookup.json'


def load_lookup() -> dict:
    """Load the code lookup JSON file. Returns dict with keys:
    'law', 'judgment', 'regulation', 'contract_template'.
    Each maps code string → numeric ID.
    """
    import json
    lookup_path = get_lookup_file()
    if not lookup_path.exists():
        print(f'ERROR: lookup file not found at {lookup_path}', file=sys.stderr)
        print('Run ingest_xref_step1.py first to generate it.', file=sys.stderr)
        sys.exit(1)
    with open(lookup_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def resolve_source(doc_id: str, lookup: dict):
    """Resolve a document ID prefix to (source_type, source_id).

    Convention:
      F*  → contract_template
      A-E → law
      G*  → judgment
      H*  → regulation
    """
    if not doc_id:
        return ('unknown', 0)
    if doc_id.startswith('F'):
        return ('contract_template', lookup.get('contract_template', {}).get(doc_id, 0))
    if doc_id[0] in 'ABCDE':
        return ('law', lookup.get('law', {}).get(doc_id, 0))
    if doc_id.startswith('G'):
        return ('judgment', lookup.get('judgment', {}).get(doc_id, 0))
    if doc_id.startswith('H'):
        return ('regulation', lookup.get('regulation', {}).get(doc_id, 0))
    return ('unknown', 0)

