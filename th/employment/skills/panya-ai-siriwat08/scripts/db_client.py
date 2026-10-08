#!/usr/bin/env python3
"""
Shared Turso HTTP API client for Phase 10 scripts.

Provides a drop-in replacement for sqlite3.Connection that routes queries
to Turso via the v2 pipeline HTTP API when TURSO_URL + TURSO_TOKEN env
vars are set. Falls back to local SQLite when they're not set (dev mode).

Usage:
    from db_client import get_db
    db = get_db()
    db.execute("INSERT INTO ... VALUES (?, ?)", [val1, val2])
    db.commit()
    rows = db.execute("SELECT * FROM ...").fetchall()
    db.close()

Env vars (production):
    TURSO_URL — libsql:// or https:// URL of the Turso DB
    TURSO_TOKEN or TURSO_AUTH_TOKEN — auth token from Turso dashboard

When env vars are not set, falls back to local SQLite at:
    prisma/thai_legal_db.sqlite (relative to project root)
"""
from __future__ import annotations
import json
import os
import sqlite3
import sys
import urllib.request
import urllib.error
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
LOCAL_DB_PATH = Path(__file__).parent.parent / 'prisma' / 'thai_legal_db.sqlite'

TURSO_URL = (
    os.environ.get('TURSO_URL', '')
    or os.environ.get('TURSO_DATABASE_URL', '')
    or os.environ.get('DATABASE_URL', '')
).strip()  # Strip whitespace/newlines that may come from secret copy-paste
# Normalize libsql:// to https:// for HTTP API
if TURSO_URL.startswith('libsql://'):
    TURSO_URL = 'https://' + TURSO_URL[len('libsql://'):]

TURSO_TOKEN = (
    os.environ.get('TURSO_TOKEN')
    or os.environ.get('TURSO_AUTH_TOKEN')
    or ''
).strip()  # Strip whitespace/newlines — critical for HTTP header validity

USE_TURSO = bool(TURSO_URL and TURSO_TOKEN)

# Validate token format (must be ASCII, no control chars)
if USE_TURSO:
    try:
        TURSO_TOKEN.encode('ascii')
    except UnicodeEncodeError:
        print(f'[db_client] ERROR: TURSO_TOKEN contains non-ASCII characters', file=sys.stderr)
        USE_TURSO = False
    # Check for control characters (newlines, tabs, etc.)
    if any(ord(c) < 32 or ord(c) == 127 for c in TURSO_TOKEN):
        print(f'[db_client] ERROR: TURSO_TOKEN contains control characters (newline/tab)', file=sys.stderr)
        USE_TURSO = False

# ---------------------------------------------------------------------------
# Turso HTTP API client
# ---------------------------------------------------------------------------
class TursoCursor:
    """Mimics sqlite3.Cursor — buffers rows from execute() for fetchall()."""
    def __init__(self, conn: 'TursoConnection'):
        self.conn = conn
        self._rows: list[dict] = []
        self._cols: list[str] = []

    def execute(self, sql: str, params: list | None = None) -> 'TursoCursor':
        self._rows, self._cols = self.conn._execute(sql, params)
        return self

    def fetchall(self) -> list[dict]:
        return self._rows

    def fetchone(self) -> dict | None:
        return self._rows[0] if self._rows else None

    def close(self) -> None:
        self._rows = []
        self._cols = []


class TursoConnection:
    """Mimics sqlite3.Connection — routes queries to Turso HTTP API."""

    def __init__(self, url: str, token: str):
        self.url = url.rstrip('/')
        self.token = token
        # Set row_factory to None for parity with sqlite3 — we return dicts
        self.row_factory = None

    def _encode_value(self, v: Any) -> dict:
        if v is None:
            return {'type': 'null'}
        if isinstance(v, bool):
            return {'type': 'integer', 'value': '1' if v else '0'}
        if isinstance(v, int):
            return {'type': 'integer', 'value': str(v)}
        if isinstance(v, float):
            return {'type': 'float', 'value': str(v)}
        if isinstance(v, str):
            return {'type': 'text', 'value': v}
        if isinstance(v, bytes):
            return {'type': 'blob', 'base64': v.hex()}
        return {'type': 'text', 'value': str(v)}

    def _execute(self, sql: str, params: list | None = None) -> tuple[list[dict], list[str]]:
        stmt = {'sql': sql}
        if params:
            stmt['args'] = [self._encode_value(p) for p in params]
        body = json.dumps({'requests': [{'type': 'execute', 'stmt': stmt}]}).encode()
        req = urllib.request.Request(
            f'{self.url}/v2/pipeline',
            data=body,
            headers={
                'Authorization': f'Bearer {self.token}',
                'Content-Type': 'application/json',
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read())
                for r in data.get('results', []):
                    if r.get('type') == 'ok':
                        result = r['response']['result']
                        cols = [c['name'] for c in result.get('cols', [])]
                        rows = []
                        for row in result.get('rows', []):
                            d = {}
                            for i, c in enumerate(cols):
                                v = row[i] if i < len(row) else None
                                if isinstance(v, dict):
                                    if v.get('type') == 'null':
                                        d[c] = None
                                    elif v.get('type') == 'integer':
                                        d[c] = int(v['value'])
                                    elif v.get('type') == 'float':
                                        d[c] = float(v['value'])
                                    else:
                                        d[c] = v.get('value')
                                else:
                                    d[c] = v
                            rows.append(d)
                        return rows, cols
                    elif r.get('type') == 'error':
                        raise RuntimeError(f"Turso SQL error: {r['error']['message']}")
                return [], []
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', errors='replace')
            raise RuntimeError(f'Turso HTTP {e.code}: {body[:500]}') from e

    def execute(self, sql: str, params: list | None = None) -> TursoCursor:
        # For DDL/DML statements (CREATE TABLE, INSERT, UPDATE, etc.)
        # we use executescript-like behavior — execute and return empty cursor
        cursor = TursoCursor(self)
        cursor.execute(sql, params)
        return cursor

    def executescript(self, script: str) -> None:
        # Split on semicolons (naive — works for our schema scripts)
        # Each statement is executed separately
        # Filter out empty statements and comments
        statements = []
        current = []
        for line in script.split('\n'):
            line = line.strip()
            if not line or line.startswith('--'):
                continue
            current.append(line)
            if line.endswith(';'):
                statements.append(' '.join(current))
                current = []
        if current:
            statements.append(' '.join(current))

        for stmt in statements:
            stmt = stmt.rstrip(';').strip()
            if stmt:
                self._execute(stmt)

    def commit(self) -> None:
        # Turso auto-commits each statement — no-op for parity
        pass

    def close(self) -> None:
        pass


# ---------------------------------------------------------------------------
# SQLite fallback (for local dev)
# ---------------------------------------------------------------------------
class SQLiteCursor:
    """Wraps sqlite3.Cursor to return dict rows (parity with TursoCursor)."""
    def __init__(self, cursor: sqlite3.Cursor):
        self._cursor = cursor

    def execute(self, sql: str, params: list | None = None) -> 'SQLiteCursor':
        if params:
            self._cursor.execute(sql, params)
        else:
            self._cursor.execute(sql)
        return self

    def fetchall(self) -> list[dict]:
        rows = self._cursor.fetchall()
        if not rows:
            return []
        cols = [d[0] for d in self._cursor.description]
        return [dict(zip(cols, row)) for row in rows]

    def fetchone(self) -> dict | None:
        row = self._cursor.fetchone()
        if not row:
            return None
        cols = [d[0] for d in self._cursor.description]
        return dict(zip(cols, row))

    def close(self) -> None:
        self._cursor.close()


class SQLiteConnection:
    """Wraps sqlite3.Connection to provide the same interface as TursoConnection."""
    def __init__(self, path: Path):
        self._conn = sqlite3.connect(str(path))
        self._conn.row_factory = sqlite3.Row  # for dict-like access
        self.row_factory = None

    def execute(self, sql: str, params: list | None = None) -> SQLiteCursor:
        cursor = self._conn.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        return SQLiteCursor(cursor)

    def executescript(self, script: str) -> None:
        self._conn.executescript(script)

    def commit(self) -> None:
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def get_db(db_path: Path | None = None) -> TursoConnection | SQLiteConnection:
    """
    Get a database connection.

    Returns TursoConnection when TURSO_URL + TURSO_TOKEN env vars are set
    (production). Otherwise returns SQLiteConnection to the local DB file
    at prisma/thai_legal_db.sqlite (dev mode).

    Both return the same interface: execute(), executescript(), commit(), close()
    """
    if USE_TURSO:
        print(f'[db_client] Using Turso: {TURSO_URL}', file=sys.stderr)
        return TursoConnection(TURSO_URL, TURSO_TOKEN)
    else:
        path = db_path or LOCAL_DB_PATH
        if not path.exists():
            print(f'[db_client] WARNING: Local DB not found at {path}', file=sys.stderr)
        else:
            print(f'[db_client] Using local SQLite: {path}', file=sys.stderr)
        return SQLiteConnection(path)


def is_using_turso() -> bool:
    """Returns True if the connection will go to Turso, False for local SQLite."""
    return USE_TURSO
