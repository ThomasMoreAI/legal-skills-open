#!/usr/bin/env python3
"""Query the official cross-government consultation listing."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "lib"))

import nzfetch  # noqa: E402
from govt_consultations import parse_consultations  # noqa: E402
from result_contract import result_envelope, utc_now  # noqa: E402

SOURCE_URL = "https://www.govt.nz/browse/engaging-with-government/consultations-have-your-say/consultations-listing/"
ALLOWED_HOSTS = {"www.govt.nz"}
WARNINGS = [
    "This connector does not submit consultation responses.",
    "The listing publishes closing dates without an exact time or timezone; verify the linked consultation.",
    "The cross-government listing is not necessarily exhaustive.",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("open", "recently-closed"):
        child = commands.add_parser(command)
        child.add_argument("--limit", type=int, default=50)
        child.add_argument("--json", action="store_true")
    closing = commands.add_parser("closing-soon")
    closing.add_argument("--days", type=int, required=True)
    closing.add_argument("--limit", type=int, default=50)
    closing.add_argument("--json", action="store_true")
    for command, positional in (("agency", "name"), ("topic", "query"), ("consultation", "id")):
        child = commands.add_parser(command)
        child.add_argument(positional)
        child.add_argument("--limit", type=int, default=50)
        child.add_argument("--json", action="store_true")
    return parser


def select(rows: list[dict[str, object]], args: argparse.Namespace) -> list[dict[str, object]]:
    if not 1 <= args.limit <= 100:
        raise ValueError("--limit must be between 1 and 100")
    if args.command == "open":
        selected = [row for row in rows if row["status"] == "open"]
    elif args.command == "recently-closed":
        selected = [row for row in rows if row["status"] == "closed"]
    elif args.command == "closing-soon":
        if not 0 <= args.days <= 366:
            raise ValueError("--days must be between 0 and 366")
        today = date.today()
        try:
            from datetime import datetime

            today = datetime.now(ZoneInfo("Pacific/Auckland")).date()
        except Exception:
            pass
        cutoff = today + timedelta(days=args.days)
        selected = [
            row
            for row in rows
            if row["status"] == "open"
            and row.get("closes_on")
            and today <= date.fromisoformat(str(row["closes_on"])) <= cutoff
        ]
    elif args.command == "agency":
        selected = [row for row in rows if args.name.casefold() in str(row["agency"]).casefold()]
    elif args.command == "topic":
        needle = args.query.casefold()
        selected = [
            row
            for row in rows
            if needle in f"{row['title']} {row['summary']}".casefold()
        ]
    else:
        needle = args.id.casefold()
        selected = [row for row in rows if needle in {str(row["id"]).casefold(), str(row["source_url"]).casefold()}]
    return selected[: args.limit]


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    retrieved_at = utc_now()
    try:
        html = nzfetch.fetch_text(SOURCE_URL, timeout=25, allowed_hosts=ALLOWED_HOSTS)
        data = select(parse_consultations(html, SOURCE_URL, retrieved_at), args)
        envelope = result_envelope(
            ok=True,
            source_name="New Zealand Government consultations",
            source_url=SOURCE_URL,
            retrieved_at=retrieved_at,
            freshness="source-managed; deadlines time-sensitive",
            query=vars(args),
            data=data,
            warnings=WARNINGS,
            blocked=False,
        )
        if args.json:
            print(json.dumps(envelope, indent=2, ensure_ascii=False))
        else:
            for row in data:
                print(f"{row['closes_on'] or 'date unknown'} | {row['agency']} | {row['title']}")
                print(f"  {row['source_url']}")
            if not data:
                print("No matching consultations in the current official listing.")
        return 0
    except ValueError as exc:
        print(json.dumps({"error": "invalid_input_or_source_schema", "message": str(exc)}), file=sys.stderr)
        return 2 if str(exc).startswith("--") else 6
    except nzfetch.RateLimited as exc:
        print(json.dumps({"error": "rate_limited", "message": str(exc), "retry_after": exc.retry_after}), file=sys.stderr)
        return 4
    except nzfetch.Blocked as exc:
        print(json.dumps({"error": "blocked", "message": str(exc)}), file=sys.stderr)
        return 4
    except nzfetch.FetchError as exc:
        print(json.dumps({"error": "source_unavailable", "message": str(exc)}), file=sys.stderr)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
