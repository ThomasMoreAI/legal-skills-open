#!/usr/bin/env python3
"""Search official Hansard sittings, debates and speaker turns."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "lib"))
import nzfetch  # noqa: E402
from hansard_transcript import oral_question_excerpt, parse_listing, parse_transcript  # noqa: E402
from result_contract import result_envelope, utc_now  # noqa: E402

HOME = "https://hansard.parliament.nz/"
ALLOWED = {"hansard.parliament.nz"}
WARNINGS = ["Quote and attribution remain tied to the official transcript.", "Do not infer a speaker's position beyond retrieved words and context."]


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__); commands = root.add_subparsers(dest="command", required=True)
    for name, positional in (("search", "query"), ("speaker", "name"), ("bill", "query")):
        child = commands.add_parser(name); child.add_argument(positional); child.add_argument("--date", dest="sitting_date"); child.add_argument("--sittings", type=int, default=5); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    for name, positional in (("debate", "id"),):
        child = commands.add_parser(name); child.add_argument(positional); child.add_argument("--date", dest="sitting_date"); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    child = commands.add_parser("oral-questions"); child.add_argument("--date", required=True); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    child = commands.add_parser("latest"); child.add_argument("--date", dest="sitting_date"); child.add_argument("--limit", type=int, default=50); child.add_argument("--json", action="store_true")
    return root


def _fetch(url: str) -> str:
    return nzfetch.fetch_text(url, timeout=30, allowed_hosts=ALLOWED, browser_headers=False, headers={"User-Agent": "curl/8.7.1", "Accept": "*/*"})


def parse_input_date(value: str, option: str) -> date:
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise LookupError(f"{option} must be a valid YYYY-MM-DD date") from exc
    if parsed.isoformat() != value:
        raise LookupError(f"{option} must be a valid YYYY-MM-DD date")
    return parsed


def _load_sitting(sitting_date: str, stamp: str) -> tuple[str, dict[str, object]]:
    parse_input_date(sitting_date, "--date")
    url = f"https://hansard.parliament.nz/hansard-transcript/{sitting_date}"
    return url, parse_transcript(_fetch(url), url, stamp)


def _filter_record(command: str, args: argparse.Namespace, record: dict[str, object]) -> list[dict[str, object]]:
    if command == "speaker":
        return [turn for turn in record["turns"] if args.name.casefold() in str(turn.get("speaker_as_published") or turn["speaker"]).casefold()]
    needle = args.query.casefold()
    return [item for item in record["debates"] if needle in json.dumps(item, ensure_ascii=False).casefold()]


def main() -> int:
    args = parser().parse_args(); stamp = utc_now()
    try:
        if not 1 <= args.limit <= 100: raise LookupError("--limit must be between 1 and 100")
        if hasattr(args, "sittings") and not 1 <= args.sittings <= 20: raise LookupError("--sittings must be between 1 and 20")
        chosen = getattr(args, "sitting_date", None) or getattr(args, "date", None)
        if chosen:
            parse_input_date(chosen, "--date")
        debate_id = getattr(args, "id", "") if args.command == "debate" else ""
        if not chosen and debate_id:
            match = re.match(r"^(\d{4}-\d{2}-\d{2})(?:-|$)", debate_id)
            chosen = match.group(1) if match else None
        if not chosen:
            listing = parse_listing(_fetch(HOME), HOME, stamp)
            if args.command == "latest":
                data = listing[:args.limit]; source_url = HOME
                envelope = result_envelope(ok=True, source_name="New Zealand Parliament Hansard", source_url=source_url, retrieved_at=stamp, freshness="listing-dependent", query=vars(args), data=data, warnings=WARNINGS, blocked=False)
                print(json.dumps(envelope if args.json else data, indent=2, ensure_ascii=False)); return 0
            if args.command in {"search", "speaker", "bill"}:
                selected = listing[:args.sittings]
                data = []
                for sitting in selected:
                    _, record = _load_sitting(str(sitting["sitting_date"]), stamp)
                    data.extend(_filter_record(args.command, args, record))
                data = data[:args.limit]
                source_url = HOME
                warnings = WARNINGS + [f"Undated search covered the latest {len(selected)} official sitting(s); use --date for an exact sitting or --sittings to adjust the bounded corpus."]
                envelope = result_envelope(ok=True, source_name="New Zealand Parliament Hansard", source_url=source_url, retrieved_at=stamp, freshness="bounded listing corpus", query=vars(args), data=data, warnings=warnings, blocked=False)
                print(json.dumps(envelope if args.json else data, indent=2, ensure_ascii=False)); return 0
            chosen = str(listing[0]["sitting_date"])
        source_url, record = _load_sitting(chosen, stamp)
        if args.command == "oral-questions": data = oral_question_excerpt(record)[:args.limit]
        elif args.command == "speaker": data = _filter_record(args.command, args, record)[:args.limit]
        elif args.command in {"search", "bill"}:
            data = _filter_record(args.command, args, record)[:args.limit]
        elif args.command == "debate":
            data = [item for item in record["debates"] if item["id"] == debate_id or debate_id == record["id"]][:args.limit]
        else:
            data = record
        envelope = result_envelope(ok=True, source_name="New Zealand Parliament Hansard", source_url=source_url, retrieved_at=stamp, freshness="sitting-dependent", query=vars(args), data=data, warnings=WARNINGS, blocked=False)
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
