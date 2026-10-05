#!/usr/bin/env python3
"""Retrieve bounded metadata from the Federal Register of Legislation API."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import Request, urlopen

API_ROOT = "https://api.prod.legislation.gov.au/v1"
TITLE_ID = re.compile(r"^[A-Z][0-9]{4}[A-Z][0-9]{5}$")
USER_AGENT = "legal-skills/australian-legal-research/0.1.0"
TIMEOUT_SECONDS = 20

TITLE_FIELDS = (
    "id,name,collection,subCollection,isPrincipal,isInForce,status,"
    "hasCommencedUnincorporatedAmendments,nameHistory,namePossibleFuture,"
    "statusHistory,statusPossibleFuture,makingDate,asMadeRegisteredAt,"
    "optionalSeriesNumber,year,number,seriesType"
)
VERSION_FIELDS = (
    "titleId,start,retrospectiveStart,end,retrospectiveEnd,isCurrent,isLatest,"
    "name,status,registerId,registeredAt,compilationNumber,publishComments,"
    "hasUnincorporatedAmendments,reasons"
)


class LookupError(Exception):
    """Raised when the official API cannot supply an unambiguous result."""


def api_get(url: str) -> dict[str, Any]:
    target = urlsplit(url)
    if (
        target.scheme != "https"
        or target.hostname != "api.prod.legislation.gov.au"
        or target.port is not None
        or target.username is not None
        or target.password is not None
    ):
        raise LookupError("refusing a URL outside the Federal Register API")
    request = Request(url, headers={"Accept": "application/json", "User-Agent": USER_AGENT})
    try:
        # nosemgrep
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            payload = json.load(response)
    except HTTPError as exc:
        if exc.code == 404:
            raise LookupError("the Federal Register returned no matching record") from exc
        raise LookupError(f"the Federal Register returned HTTP {exc.code}") from exc
    except (URLError, TimeoutError) as exc:
        reason = getattr(exc, "reason", str(exc))
        raise LookupError(f"the Federal Register could not be reached: {reason}") from exc
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise LookupError("the Federal Register returned an unreadable response") from exc
    if not isinstance(payload, dict):
        raise LookupError("the Federal Register returned an unexpected response shape")
    return payload


def validate_title_id(value: str) -> str:
    value = value.strip().upper()
    if not TITLE_ID.fullmatch(value):
        raise LookupError("Title ID must look like C2004A01224 or F2024L00463")
    return value


def validate_as_at(value: str) -> str:
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError as exc:
        raise LookupError("--as-at must be a real date in YYYY-MM-DD format") from exc


def search_url(query: str, limit: int) -> str:
    normalized = " ".join(query.split())
    if not normalized or len(normalized) > 200:
        raise LookupError("search text must contain 1 to 200 characters")
    escaped = normalized.lower().replace("'", "''")
    params = urlencode(
        {
            "$filter": f"contains(tolower(name),'{escaped}')",
            "$select": "id,name,collection,isPrincipal,isInForce,status,year,number,seriesType",
            "$top": limit,
        }
    )
    return f"{API_ROOT}/Titles?{params}"


def title_url(title_id: str) -> str:
    params = urlencode(
        {
            "$select": TITLE_FIELDS,
            "$expand": f"Versions($select={VERSION_FIELDS})",
        }
    )
    return f"{API_ROOT}/Titles('{quote(title_id)}')?{params}"


def point_in_time_url(title_id: str, as_at: str) -> str:
    return f"{API_ROOT}/versions/find(titleid='{quote(title_id)}',asat={quote(as_at)})"


def candidate_list(payload: dict[str, Any]) -> list[dict[str, Any]]:
    candidates = payload.get("value", payload)
    if not isinstance(candidates, list):
        raise LookupError("the Federal Register search returned an unexpected response shape")
    return [candidate for candidate in candidates if isinstance(candidate, dict)]


def select_expanded_version(versions: list[dict[str, Any]], point_in_time: dict[str, Any]) -> dict[str, Any]:
    register_id = point_in_time.get("registerId")
    start = point_in_time.get("start")
    matches = [
        version for version in versions if version.get("registerId") == register_id and version.get("start") == start
    ]
    if len(matches) != 1:
        raise LookupError("the point-in-time version could not be matched uniquely to the title history")
    return matches[0]


def search(query: str, limit: int) -> dict[str, Any]:
    candidates = candidate_list(api_get(search_url(query, limit)))
    return {
        "query": query,
        "candidateCount": len(candidates),
        "candidates": [
            {
                **candidate,
                "officialUrl": f"https://www.legislation.gov.au/{candidate.get('id')}",
            }
            for candidate in candidates
        ],
        "warning": "Candidates require identity review; search rank does not establish the correct title.",
    }


def check(title_id: str, as_at: str) -> dict[str, Any]:
    title = api_get(title_url(title_id))
    title.pop("@odata.context", None)
    versions = title.pop("versions", None)
    if not isinstance(versions, list):
        raise LookupError("the title response did not include a version history")
    point_in_time = api_get(point_in_time_url(title_id, as_at))
    version = select_expanded_version(versions, point_in_time)
    return {
        "query": {"titleId": title_id, "asAt": as_at},
        "title": title,
        "version": version,
        "currencyFlags": {
            "currentTitleHasCommencedUnincorporatedAmendments": title.get("hasCommencedUnincorporatedAmendments"),
            "versionHasUnincorporatedAmendments": version.get("hasUnincorporatedAmendments"),
            "knownFutureNameChanges": bool(title.get("namePossibleFuture")),
            "knownFutureStatusChanges": bool(title.get("statusPossibleFuture")),
        },
        "officialUrls": {
            "title": f"https://www.legislation.gov.au/{title_id}",
            "pointInTime": f"https://www.legislation.gov.au/{title_id}/{as_at}",
            "versions": f"https://www.legislation.gov.au/{title_id}/versions",
        },
        "warning": (
            "API metadata does not establish commencement of every provision, "
            "authorised-PDF status, legal effect or interpretation. Inspect the official pages."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Retrieve bounded metadata from the official Federal Register API.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    search_parser = subparsers.add_parser("search", help="Find candidate title records")
    search_parser.add_argument("query", help="Part of the official title")
    search_parser.add_argument("--limit", type=int, default=10, choices=range(1, 21))

    check_parser = subparsers.add_parser("check", help="Retrieve one point-in-time record")
    check_parser.add_argument("title_id", help="Federal Register Title ID")
    check_parser.add_argument("--as-at", required=True, help="YYYY-MM-DD")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "search":
            result = search(args.query, args.limit)
        else:
            result = check(validate_title_id(args.title_id), validate_as_at(args.as_at))
    except LookupError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
