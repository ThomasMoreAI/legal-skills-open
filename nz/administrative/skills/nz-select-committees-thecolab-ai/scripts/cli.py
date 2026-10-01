#!/usr/bin/env python3
"""Track official select committees, submissions, evidence and reports."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "lib"))
import nzfetch  # noqa: E402
from result_contract import result_envelope, utc_now  # noqa: E402
from select_committees import parse_detail, parse_listing  # noqa: E402

BASE = "https://www3.parliament.nz/en/pb/sc"
ALLOWED = {"www3.parliament.nz", "www.parliament.nz"}
WARNINGS = ["This connector never submits on a user's behalf.", "Verify the exact closing time and timezone on the linked official item.", "Public evidence can contain personal information; retain official context."]


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__); commands = root.add_subparsers(dest="command", required=True)
    for name in ("committees", "open-submissions"):
        child = commands.add_parser(name); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    child = commands.add_parser("closing-soon"); child.add_argument("--days", type=int, required=True); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    child = commands.add_parser("business"); child.add_argument("--committee", required=True); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    child = commands.add_parser("evidence"); child.add_argument("item_id"); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    child = commands.add_parser("reports"); child.add_argument("--since", required=True); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    child = commands.add_parser("item"); child.add_argument("id"); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    return root


def _enrich(rows: list[dict[str, object]], retrieved_at: str, limit: int) -> list[dict[str, object]]:
    enriched = []
    for row in rows[:limit]:
        url = str(row["source_url"])
        detail = parse_detail(nzfetch.fetch_text(url, timeout=25, allowed_hosts=ALLOWED), url, retrieved_at)
        enriched.append({**row, **{key: value for key, value in detail.items() if value not in (None, [], "")}})
    return enriched


def parse_input_date(value: str, option: str) -> date:
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise LookupError(f"{option} must be a valid YYYY-MM-DD date") from exc
    if parsed.isoformat() != value:
        raise LookupError(f"{option} must be a valid YYYY-MM-DD date")
    return parsed


def main() -> int:
    args = parser().parse_args(); stamp = utc_now()
    try:
        if not 1 <= args.limit <= 100: raise LookupError("--limit must be between 1 and 100")
        if args.command == "closing-soon" and not 0 <= args.days <= 366: raise LookupError("--days must be between 0 and 366")
        since = parse_input_date(args.since, "--since") if args.command == "reports" else None
        paths = {"committees": "scl", "open-submissions": "make-a-submission/open", "closing-soon": "make-a-submission/open", "business": "business-before-committees", "evidence": "evidence-submissions", "reports": "reports/all", "item": "business-before-committees"}
        source_url = f"{BASE}/{paths[args.command]}/"
        rows = parse_listing(nzfetch.fetch_text(source_url, timeout=30, allowed_hosts=ALLOWED), source_url, stamp)
        if args.command == "closing-soon":
            end = date.today() + timedelta(days=args.days)
            rows = [row for row in rows if row["closing_date"] and date.today() <= date.fromisoformat(str(row["closing_date"])) <= end]
            data = _enrich(rows, stamp, args.limit)
        elif args.command == "business":
            rows = [row for row in rows if args.committee.casefold() in f"{row['committee']} {row['context']}".casefold()]
            data = _enrich(rows, stamp, args.limit)
        elif args.command == "evidence":
            rows = [row for row in rows if args.item_id.casefold() in f"{row['id']} {row['title']} {row['context']}".casefold()]
            data = [{**item, "evidence": item.get("evidence", [])} for item in _enrich(rows, stamp, args.limit)]
        elif args.command == "reports":
            data = [row for row in rows if row["date"] and date.fromisoformat(str(row["date"])) >= since][:args.limit]
        elif args.command == "item":
            rows = [row for row in rows if args.id.casefold() in f"{row['id']} {row['title']}".casefold()]
            data = _enrich(rows, stamp, args.limit)
        elif args.command in {"committees", "open-submissions"}:
            data = _enrich(rows, stamp, args.limit)
        else:
            data = rows[:args.limit]
        envelope = result_envelope(ok=True, source_name="New Zealand Parliament select committees", source_url=source_url, retrieved_at=stamp, freshness="source-managed; deadlines time-sensitive", query=vars(args), data=data, warnings=WARNINGS, blocked=False)
        print(json.dumps(envelope if args.json else data, indent=2, ensure_ascii=False))
        return 0
    except LookupError as exc:
        print(json.dumps({"error": "invalid_input", "message": str(exc)}), file=sys.stderr); return 2
    except nzfetch.RateLimited as exc:
        print(json.dumps({"error": "rate_limited", "retry_after": exc.retry_after, "message": str(exc)}), file=sys.stderr); return 4
    except nzfetch.Blocked as exc:
        print(json.dumps({"error": "blocked", "message": str(exc)}), file=sys.stderr); return 4
    except nzfetch.FetchError as exc:
        print(json.dumps({"error": "source_unavailable", "message": str(exc)}), file=sys.stderr); return 5
    except (ValueError, KeyError) as exc:
        print(json.dumps({"error": "source_schema_failure", "message": str(exc)}), file=sys.stderr); return 6


if __name__ == "__main__":
    raise SystemExit(main())
