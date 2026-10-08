"""Remove audit trail files older than a retention window (default: 90 days).

Usage:
    python scripts/cleanup_audit.py               # delete files > 90 days
    python scripts/cleanup_audit.py --dry-run     # list what would be removed
    python scripts/cleanup_audit.py --days 30     # custom TTL
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from audit import DEFAULT_AUDIT_ROOT


def find_stale(root: Path, max_age_days: int, now: float | None = None) -> list[Path]:
    if not root.exists():
        return []
    cutoff = (now if now is not None else time.time()) - max_age_days * 86400
    stale: list[Path] = []
    for entry in sorted(root.iterdir()):
        if not entry.is_file() or entry.suffix != ".jsonl":
            continue
        if entry.stat().st_mtime < cutoff:
            stale.append(entry)
    return stale


def cleanup(root: Path, max_age_days: int, dry_run: bool) -> tuple[int, int]:
    stale = find_stale(root, max_age_days)
    removed = 0
    for entry in stale:
        if dry_run:
            print(f"[dry-run] would remove: {entry}")
        else:
            entry.unlink()
            print(f"removed: {entry}")
            removed += 1
    return removed, len(stale)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(DEFAULT_AUDIT_ROOT), help="Audit root directory")
    parser.add_argument("--days", type=int, default=90, help="Retention window in days")
    parser.add_argument("--dry-run", action="store_true", help="Do not delete, only list")
    args = parser.parse_args(argv)

    removed, total = cleanup(Path(args.root), args.days, args.dry_run)
    suffix = "would be removed" if args.dry_run else "removed"
    print(f"{removed if not args.dry_run else total} file(s) {suffix} (retention: {args.days} days)")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    raise SystemExit(main())
