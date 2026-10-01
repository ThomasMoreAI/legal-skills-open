#!/usr/bin/env python3
"""Search and retrieve official New Zealand Gazette notices."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "lib"))

import nzfetch  # noqa: E402
from gazette_notices import notice_type_codes, parse_notice, parse_search  # noqa: E402
from result_contract import result_envelope, utc_now  # noqa: E402

SEARCH_URL = "https://gazette.govt.nz/home/search"
ALLOWED_HOSTS = {"gazette.govt.nz"}
WARNINGS = [
    "Notice retrieval is not legal advice and does not determine legal effect.",
    "Check the official record for amendments, revocations and corrected notices.",
]


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)
    for name, positional in (("search", "query"), ("notice", "id"), ("under-act", "act_name"), ("category", "name")):
        child = commands.add_parser(name)
        child.add_argument(positional)
        child.add_argument("--limit", type=int, default=20)
        child.add_argument("--json", action="store_true")
    latest = commands.add_parser("latest")
    latest.add_argument("--limit", type=int, default=20)
    latest.add_argument("--json", action="store_true")
    ranged = commands.add_parser("date")
    ranged.add_argument("--from", dest="from_date", required=True)
    ranged.add_argument("--to", dest="to_date", required=True)
    ranged.add_argument("--limit", type=int, default=20)
    ranged.add_argument("--json", action="store_true")
    return root


def fetch(url: str) -> str:
    return nzfetch.fetch_text(url, timeout=25, allowed_hosts=ALLOWED_HOSTS)


def parse_input_date(value: str, option: str) -> date:
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise LookupError(f"{option} must be a valid YYYY-MM-DD date") from exc
    if parsed.isoformat() != value:
        raise LookupError(f"{option} must be a valid YYYY-MM-DD date")
    return parsed


def main() -> int:
    args = parser().parse_args()
    retrieved_at = utc_now()
    try:
        if not 1 <= args.limit <= 100:
            raise LookupError("--limit must be between 1 and 100")
        if args.command == "date":
            from_date = parse_input_date(args.from_date, "--from")
            to_date = parse_input_date(args.to_date, "--to")
            if from_date > to_date:
                raise LookupError("--from must not be after --to")
        if args.command == "notice":
            ident = args.id.removeprefix("https://gazette.govt.nz/notice/id/").strip("/")
            if not ident or "/" in ident:
                raise LookupError("invalid Gazette notice identifier")
            source_url = f"https://gazette.govt.nz/notice/id/{ident}"
            data: object = parse_notice(fetch(source_url), source_url, retrieved_at)
        else:
            params: dict[str, object] = {"sortField": "publish_date", "sortOrder": "desc"}
            if args.command == "search":
                params["keyword"] = args.query
            elif args.command == "under-act":
                params["act"] = args.act_name
            elif args.command == "category":
                form = fetch(SEARCH_URL)
                codes = notice_type_codes(form)
                needle = args.name.casefold()
                code = codes.get(needle)
                if not code:
                    matches = [value for label, value in codes.items() if needle in label]
                    if len(matches) != 1:
                        raise LookupError("unknown or ambiguous Gazette notice category")
                    code = matches[0]
                params["noticeType[]"] = code
            elif args.command == "date":
                params.update({"dateStart": args.from_date, "dateEnd": args.to_date})
            source_url = f"{SEARCH_URL}?{urlencode(params, doseq=True)}"
            data = parse_search(fetch(source_url), source_url, retrieved_at)[: args.limit]
        envelope = result_envelope(
            ok=True, source_name="New Zealand Gazette", source_url=source_url,
            retrieved_at=retrieved_at, freshness="continuously published", query=vars(args),
            data=data, warnings=WARNINGS, blocked=False,
        )
        if args.json:
            print(json.dumps(envelope, indent=2, ensure_ascii=False))
        elif isinstance(data, list):
            for row in data:
                print(f"{row['published_on']} | {row['id']} | {row['title']}\n  {row['source_url']}")
            if not data:
                print("No matching official Gazette notices.")
        else:
            print(f"{data['published_on']} | {data['id']} | {data['title']}\n{data['text']}\n{data['source_url']}")
        return 0
    except LookupError as exc:
        print(json.dumps({"error": "invalid_input", "message": str(exc)}), file=sys.stderr)
        return 2
    except ValueError as exc:
        print(json.dumps({"error": "invalid_input_or_source_schema", "message": str(exc)}), file=sys.stderr)
        return 6
    except nzfetch.RateLimited as exc:
        print(json.dumps({"error": "rate_limited", "retry_after": exc.retry_after, "message": str(exc)}), file=sys.stderr)
        return 4
    except nzfetch.Blocked as exc:
        print(json.dumps({"error": "blocked", "message": str(exc)}), file=sys.stderr)
        return 4
    except nzfetch.FetchError as exc:
        print(json.dumps({"error": "source_unavailable", "message": str(exc)}), file=sys.stderr)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
