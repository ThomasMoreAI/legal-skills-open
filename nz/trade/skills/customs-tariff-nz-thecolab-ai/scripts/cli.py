#!/usr/bin/env python3
"""Read-only CLI for current New Zealand Customs tariff source records."""
from __future__ import annotations

import argparse
import json
import sys
from typing import Any, NoReturn

from customs_tariff import (
    ARCHIVE_URL,
    DEFAULT_TIMEOUT,
    LANDING_URL,
    SkillError,
    fetch_archive,
    formula_records,
    lookup_records,
    normalise_code,
    parse_as_of,
    search_records,
    utc_now,
    validate_formula_code,
    validate_search_query,
)

COMMON_WARNINGS = [
    "Source records support research only; they are not legal or customs advice.",
    "Do not treat these fields as a definitive duty, levy, GST or landed-cost calculation.",
    "Confirm consequential classifications and charges with New Zealand Customs or a qualified customs broker.",
]


class CliArgumentParser(argparse.ArgumentParser):
    """Raise a typed error so JSON callers receive the normal envelope."""

    def error(self, message: str) -> NoReturn:
        raise SkillError(message, exit_code=2, kind="invalid_input")


def positive_limit(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("limit must be an integer") from exc
    if not 1 <= number <= 100:
        raise argparse.ArgumentTypeError("limit must be between 1 and 100")
    return number


def bounded_timeout(value: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("timeout must be an integer") from exc
    if not 1 <= number <= DEFAULT_TIMEOUT:
        raise argparse.ArgumentTypeError("timeout must be between 1 and 10 seconds")
    return number


def source_payload(archive: Any) -> dict[str, Any]:
    return {
        "name": "New Zealand Customs Service CusMod Tariff Data",
        "url": archive.source_url,
        "landing_page": LANDING_URL,
        "retrieved_at": archive.retrieved_at,
        "timestamp": archive.source_timestamp,
        "http_last_modified": archive.http_last_modified,
    }


def envelope(archive: Any, command: str, query: dict[str, Any], data: Any, warnings: list[str]) -> dict[str, Any]:
    return {
        "schema_version": "1",
        "ok": True,
        "blocked": False,
        "command": command,
        "source": source_payload(archive),
        "query": query,
        "data": data,
        "warnings": warnings,
    }


def print_human(payload: dict[str, Any]) -> None:
    source = payload["source"]
    print(f"Source timestamp: {source['timestamp']}")
    print(f"Source: {source['url']}")
    data = payload["data"]
    if payload["command"] == "search":
        print(f"Matches: {len(data)}")
        for record in data:
            letter = record.get("check_letter") or ""
            print(f"- {record['display_code']}{letter} — {record['description']}")
    elif payload["command"] == "formula":
        print(f"Levy formulas: {len(data)}")
        for record in data:
            print(f"- {record['formula_code']}: {record['formula_rate']}")
    else:
        classification = data.get("classification")
        if classification:
            print(f"{data['display_code']}{classification.get('check_letter') or ''} — {classification['description']}")
        else:
            print(f"No active classification found for {data['display_code']} on {data['as_of']}.")
        print(f"Rates: {len(data['rates'])}; levies: {len(data['levies'])}")
        for rate in data["rates"]:
            print(f"- rate {rate['rate_group']}: formula {rate['formula_code']}, factors {rate['factors']}")
        for levy in data["levies"]:
            print(f"- levy {levy['levy_type_code']}: formula {levy['formula_code']}, coefficient {levy['formula_rate']}")
    print("Caveats:")
    for warning in payload["warnings"]:
        print(f"- {warning}")


def add_common(parser: argparse.ArgumentParser, *, as_of: bool = False, limit: bool = False) -> None:
    if as_of:
        parser.add_argument("--as-of", help="active-record date (YYYY-MM-DD; default: archive timestamp date)")
    if limit:
        parser.add_argument("--limit", type=positive_limit, default=20, help="maximum records, 1-100 (default: 20)")
    parser.add_argument("--timeout", type=bounded_timeout, default=DEFAULT_TIMEOUT, help="request timeout, 1-10 seconds (default: 10)")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")


def build_parser() -> argparse.ArgumentParser:
    parser = CliArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)

    search = subcommands.add_parser("search", help="search active classifications by text or tariff-code prefix")
    search.add_argument("query", help="description words or a 1-to-10 digit code prefix")
    add_common(search, as_of=True, limit=True)

    lookup = subcommands.add_parser("lookup", help="join active classification, rate, levy and formula records")
    lookup.add_argument("tariff_code", help="10-digit tariff item, with optional separators")
    add_common(lookup, as_of=True)

    formula = subcommands.add_parser("formula", help="inspect raw levy-formula coefficients")
    formula.add_argument("code", nargs="?", default="", help="optional exact formula code")
    formula.add_argument("--prefix", action="store_true", help="treat code as a prefix instead of an exact value")
    add_common(formula, limit=True)
    return parser


def run(args: argparse.Namespace) -> dict[str, Any]:
    if args.command == "search":
        validate_search_query(args.query)
        if args.as_of:
            parse_as_of(args.as_of)
    elif args.command == "lookup":
        normalise_code(args.tariff_code, exact=True)
        if args.as_of:
            parse_as_of(args.as_of)
    else:
        validate_formula_code(args.code)
        if args.prefix and not args.code:
            raise SkillError("--prefix requires a formula code", exit_code=2, kind="invalid_input")
    archive = fetch_archive(args.timeout)
    if args.command == "search":
        as_of = args.as_of or archive.source_timestamp[:10]
        data = search_records(archive, args.query, as_of, args.limit)
        return envelope(
            archive,
            "search",
            {"query": args.query, "as_of": as_of, "limit": args.limit},
            data,
            [*COMMON_WARNINGS, "Search results include active classification rows, not a classification decision."],
        )
    if args.command == "lookup":
        as_of = args.as_of or archive.source_timestamp[:10]
        data = lookup_records(archive, args.tariff_code, as_of)
        warnings = [
            *COMMON_WARNINGS,
            "Rate formula codes and Factors A-F are published inputs only; this command does not execute duty formulas.",
            "The separate concessions dataset and origin-based preferences are outside this result.",
        ]
        if data["classification"] is None:
            warnings.append("No active classification matched the exact code and date; verify the item and source date.")
        return envelope(archive, "lookup", {"tariff_code": args.tariff_code, "as_of": as_of}, data, warnings)
    data = formula_records(archive, args.code, args.limit, prefix=args.prefix)
    return envelope(
        archive,
        "formula",
        {
            "code": args.code,
            "match": "all" if not args.code else ("prefix" if args.prefix else "exact"),
            "limit": args.limit,
        },
        data,
        [*COMMON_WARNINGS, "Formula rates are raw levy coefficients; their units and payable treatment depend on the levy and declaration context."],
    )


def main() -> int:
    try:
        parser = build_parser()
        args = parser.parse_args()
        payload = run(args)
    except SkillError as exc:
        if "--json" in sys.argv[1:]:
            error_payload = {
                "schema_version": "1",
                "ok": False,
                "blocked": exc.exit_code == 4,
                "source": {
                    "name": "New Zealand Customs Service CusMod Tariff Data",
                    "url": ARCHIVE_URL,
                    "retrieved_at": utc_now(),
                },
                "query": {"argv": sys.argv[1:]},
                "data": None,
                "warnings": [],
                "error": {"code": exc.exit_code, "kind": exc.kind, "message": str(exc)},
            }
            print(json.dumps(error_payload, indent=2, sort_keys=True))
        else:
            print(f"Error: {exc}", file=sys.stderr)
        return exc.exit_code
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print_human(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
