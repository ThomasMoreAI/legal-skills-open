#!/usr/bin/env python3
"""fetch_zefix.py (notaire-cantonal) — Canton-specific Registre du Commerce (RC) wrapper.

Wraps the central ZEFIX lookup and post-filters by canton for notarial workflows
(e.g. constitution de société, modification statutaire). ZEFIX returns the cantonal
RC reference (`cantonalExcerptWeb`) which can be deep-linked.

Legal reference: ORC (RS 221.411); cantonal RC offices remain the authoritative registrars
(art. 927 CO). ZEFIX is the consolidated federal portal (OFJ).

External deps: `requests` (only).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# Re-use the central implementation.
SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from fetch_zefix import fetch_zefix  # type: ignore  # noqa: E402


def fetch_by_uid_for_canton(uid: str, canton: str | None = None) -> dict[str, Any]:
    """Fetch ZEFIX record and surface the cantonal RC excerpt link."""
    data = fetch_zefix(uid)
    record = data[0] if isinstance(data, list) and data else data
    if canton and isinstance(record, dict):
        rc_canton = (record.get("canton") or "").upper()
        if rc_canton and rc_canton != canton.upper():
            return {"warning": f"company registered in {rc_canton}, not {canton}", "record": record}
    return {"record": record}


def main() -> int:
    p = argparse.ArgumentParser(description="Canton-specific ZEFIX lookup wrapper for notaires.")
    p.add_argument("uid")
    p.add_argument("--canton", help="Expected canton code (GE, VD, ZH, ...) — warns if mismatch.")
    args = p.parse_args()
    try:
        out = fetch_by_uid_for_canton(args.uid, args.canton)
    except Exception as exc:  # noqa: BLE001
        print(f"error: {exc}", file=sys.stderr)
        return 1
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
