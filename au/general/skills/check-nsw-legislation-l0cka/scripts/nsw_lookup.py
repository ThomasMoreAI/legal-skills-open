#!/usr/bin/env python3
"""Generate official NSW legislation URLs from validated identifiers."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from typing import Any

BASE_URL = "https://legislation.nsw.gov.au"
IDENTIFIER = re.compile(r"^(act|sl|epi)-\d{4}-[0-9a-z]+$")
COLLECTIONS = ("inforce", "repealed")


class LookupInputError(ValueError):
    """Raised when an identifier or date cannot be used safely."""


def validate_identifier(value: str) -> str:
    """Return a normalized NSW identifier or fail closed."""
    normalized = value.strip().lower()
    if not IDENTIFIER.fullmatch(normalized):
        raise LookupInputError(
            "identifier must look like act-1987-015, sl-2024-001 or epi-2021-001"
        )
    return normalized


def validate_as_at(value: str | None) -> str:
    """Return an ISO date or the current selector."""
    if value is None:
        return "current"
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise LookupInputError("--as-at must be a real date in YYYY-MM-DD form") from exc
    if parsed.isoformat() != value:
        raise LookupInputError("--as-at must use exact YYYY-MM-DD form")
    return value


def build_urls(
    identifier: str, collection: str, as_at: str | None = None
) -> dict[str, Any]:
    """Build official navigation URLs without asserting that they resolve."""
    identifier = validate_identifier(identifier)
    if collection not in COLLECTIONS:
        raise LookupInputError("collection must be inforce or repealed")
    selector = validate_as_at(as_at)
    selected_route_collection = collection if selector == "current" else "inforce"
    current_status = f"{BASE_URL}/view/html/{collection}/current/{identifier}"
    selected_status = (
        f"{BASE_URL}/view/html/{selected_route_collection}/{selector}/{identifier}"
    )
    warning = (
        "Generated URLs do not establish identity, version selection, "
        "commencement, currency or authorisation."
    )
    if selector != "current":
        warning += (
            " An explicit-date inforce route does not prove the title operated "
            "on that date."
        )
    warning += " Inspect the official pages."
    return {
        "identifier": identifier,
        "presentCollection": collection,
        "selectedVersionRouteCollection": selected_route_collection,
        "selector": selector,
        "currentTitlePage": current_status,
        "currentLegislativeHistory": f"{current_status}/lh",
        "statusPage": selected_status,
        "wholeHtml": (
            f"{BASE_URL}/view/whole/html/{selected_route_collection}/"
            f"{selector}/{identifier}"
        ),
        "wholePdf": (
            f"{BASE_URL}/view/whole/pdf/{selected_route_collection}/"
            f"{selector}/{identifier}"
        ),
        "legislativeHistory": f"{selected_status}/lh",
        "xml": f"{selected_status}/xml",
        "warning": warning,
    }


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    subparsers = root.add_subparsers(dest="command", required=True)
    urls = subparsers.add_parser("urls", help="generate official URLs")
    urls.add_argument("identifier")
    urls.add_argument(
        "--collection",
        required=True,
        choices=COLLECTIONS,
        help="title's present In force or Repealed collection",
    )
    urls.add_argument("--as-at")
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "urls":
            result = build_urls(args.identifier, args.collection, args.as_at)
        else:  # pragma: no cover - argparse restricts commands
            raise LookupInputError(f"unsupported command: {args.command}")
    except LookupInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
