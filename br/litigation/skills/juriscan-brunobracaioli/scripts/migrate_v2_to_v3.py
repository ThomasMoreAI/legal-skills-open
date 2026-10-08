"""Migrate legacy v2 analyzed.json outputs to schema v3.

Phase 6 Step 6.2. Additive only — nothing is removed. Adds:

  - schema_version = "3.0"
  - run_id = null (legacy pipeline did not track one)
  - pipeline_mode = "legacy"
  - perspectives = { autor: null, reu: null }
  - auditor_findings = []
  - verifications = []
  - monetary_recalculations = []
  - dissensos = []

Keys that already exist in the input are NEVER overwritten.

Usage:
    python3 scripts/migrate_v2_to_v3.py --input analyzed.json --output analyzed_v3.json
    python3 scripts/migrate_v2_to_v3.py --input analyzed.json --in-place --dry-run
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


V3_DEFAULTS: dict = {
    "schema_version": "3.0",
    "run_id": None,
    "pipeline_mode": "legacy",
    "perspectives": {"autor": None, "reu": None},
    "auditor_findings": [],
    "verifications": [],
    "verification_summary": {
        "total_verifications": 0,
        "confirmed": 0,
        "divergent": 0,
        "unverified": 0,
        "no_verification": 0,
    },
    "monetary_recalculations": [],
    "dissensos": [],
}


def migrate(doc: dict) -> dict:
    """Return a new dict with v3 keys added (v2 values preserved)."""
    out = dict(doc)
    for key, default in V3_DEFAULTS.items():
        out.setdefault(key, default)
    # Normalize: if the input had schema_version already, prefer the input's value
    # unless it was the v2 legacy marker — in which case upgrade.
    if doc.get("schema_version") and doc["schema_version"] not in ("2.0", "3.0"):
        out["schema_version"] = doc["schema_version"]  # keep as-is
    elif doc.get("schema_version") == "2.0":
        out["schema_version"] = "3.0"
    # Preserve analysis_version for audit.
    if "analysis_version" in doc and "analysis_version" not in out:
        out["analysis_version"] = doc["analysis_version"]
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Migrate analyzed.json from schema v2 to v3")
    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--output", "-o", help="Output path (required unless --in-place)")
    parser.add_argument("--in-place", action="store_true",
                        help="Overwrite --input after migration")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the migrated JSON to stdout instead of writing")
    args = parser.parse_args(argv)

    src = Path(args.input)
    doc = json.loads(src.read_text(encoding="utf-8"))
    migrated = migrate(doc)

    if args.dry_run:
        json.dump(migrated, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0

    dst = src if args.in_place else (Path(args.output) if args.output else None)
    if dst is None:
        print("ERROR: either --output or --in-place is required", file=sys.stderr)
        return 2
    dst.write_text(json.dumps(migrated, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] migrated v2 → v3: {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
