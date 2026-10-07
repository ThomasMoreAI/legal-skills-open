#!/usr/bin/env python3
"""Helper script for the firmvault-search Claude Code skill.

The SKILL.md primarily calls the ``firmvault_search`` console-script directly,
but this script is shipped for offline / non-uv environments where the
console-script wrapper is not on PATH. It imports ``query_firmvault`` from
the installed package and emits JSON to stdout.

Usage:
    python scripts/query.py "<text>" [--scope all|case|<slug>] [--category ...] ...
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="firmvault-search",
        description="Search the FirmVault case corpus.",
    )
    p.add_argument("text", help="Free-text query.")
    p.add_argument("--scope", default=None, help="all | case | <slug>")
    p.add_argument(
        "--category",
        default=None,
        help="medical | legal | insurance | communication",
    )
    p.add_argument("--case", default=None, help="Filter by case_slug.")
    p.add_argument("--date", default=None, help="Exact document_date.")
    p.add_argument(
        "--date-range",
        dest="date_range",
        default=None,
        help="Inclusive YYYY-MM-DD..YYYY-MM-DD range.",
    )
    p.add_argument(
        "--provider",
        default=None,
        help="Substring match on provider/sender/recipient (case-insensitive).",
    )
    p.add_argument("--limit", type=int, default=10, help="Max hits.")
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        from firmvault_pipeline.ops.search import query_firmvault
    except ImportError as e:
        sys.stderr.write(f"firmvault-search: cannot import package ({e})\n")
        return 2

    hits = query_firmvault(
        text=args.text,
        scope=args.scope,
        category=args.category,
        case_slug=args.case,
        date=args.date,
        date_range=args.date_range,
        provider=args.provider,
        limit=args.limit,
        cwd=Path.cwd(),
    )
    json.dump([h.model_dump() for h in hits], sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
