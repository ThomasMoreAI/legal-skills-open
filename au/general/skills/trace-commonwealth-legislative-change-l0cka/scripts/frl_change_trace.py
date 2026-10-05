#!/usr/bin/env python3
"""Retrieve a bounded compilation-change interval from the Federal Register API."""

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
    "hasCommencedUnincorporatedAmendments,namePossibleFuture,"
    "statusPossibleFuture,year,number,seriesType"
)
VERSION_FIELDS = (
    "titleId,start,retrospectiveStart,end,retrospectiveEnd,isCurrent,isLatest,"
    "name,status,registerId,registeredAt,compilationNumber,publishComments,"
    "hasUnincorporatedAmendments,reasons"
)


class TraceError(Exception):
    """Raised when the official API cannot supply a safe interval trace."""


def api_get(url: str) -> dict[str, Any]:
    """Return one JSON object from the official API or fail closed."""
    target = urlsplit(url)
    if (
        target.scheme != "https"
        or target.hostname != "api.prod.legislation.gov.au"
        or target.port is not None
        or target.username is not None
        or target.password is not None
    ):
        raise TraceError("refusing a URL outside the Federal Register API")
    request = Request(url, headers={"Accept": "application/json", "User-Agent": USER_AGENT})
    try:
        # nosemgrep
        with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            payload = json.load(response)
    except HTTPError as exc:
        if exc.code == 404:
            raise TraceError("the Federal Register returned no matching record") from exc
        raise TraceError(f"the Federal Register returned HTTP {exc.code}") from exc
    except (URLError, TimeoutError) as exc:
        reason = getattr(exc, "reason", str(exc))
        raise TraceError(f"the Federal Register could not be reached: {reason}") from exc
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise TraceError("the Federal Register returned an unreadable response") from exc
    if not isinstance(payload, dict):
        raise TraceError("the Federal Register returned an unexpected response shape")
    return payload


def validate_title_id(value: str) -> str:
    """Normalize a Federal Register Title ID or reject it."""
    normalized = value.strip().upper()
    if not TITLE_ID.fullmatch(normalized):
        raise TraceError("Title ID must look like C2004A01224 or F2024L00463")
    return normalized


def validate_date(value: str, option: str) -> str:
    """Return an exact ISO date or reject it."""
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise TraceError(f"{option} must be a real date in YYYY-MM-DD format") from exc
    if parsed.isoformat() != value:
        raise TraceError(f"{option} must use exact YYYY-MM-DD format")
    return value


def validate_interval(from_date: str, to_date: str) -> tuple[str, str]:
    """Return a strictly increasing date interval."""
    earlier = validate_date(from_date, "--from")
    later = validate_date(to_date, "--to")
    if earlier >= later:
        raise TraceError("--from must be earlier than --to")
    return earlier, later


def title_url(title_id: str) -> str:
    """Build the bounded title-and-versions API URL."""
    params = urlencode(
        {
            "$select": TITLE_FIELDS,
            "$expand": f"Versions($select={VERSION_FIELDS})",
        }
    )
    return f"{API_ROOT}/Titles('{quote(title_id)}')?{params}"


def point_in_time_url(title_id: str, as_at: str) -> str:
    """Build the official point-in-time lookup URL."""
    return f"{API_ROOT}/versions/find(titleid='{quote(title_id)}',asat={quote(as_at)})"


def timestamp_date(value: Any, field: str) -> str:
    """Extract the ISO date from an API timestamp or fail closed."""
    if not isinstance(value, str) or len(value) < 10:
        raise TraceError(f"a version record has no usable {field}")
    candidate = value[:10]
    try:
        return date.fromisoformat(candidate).isoformat()
    except ValueError as exc:
        raise TraceError(f"a version record has an invalid {field}") from exc


def select_endpoint(versions: list[dict[str, Any]], point_in_time: dict[str, Any]) -> dict[str, Any]:
    """Match a point-in-time response uniquely to expanded version history."""
    register_id = point_in_time.get("registerId")
    start = point_in_time.get("start")
    matches = [
        version for version in versions if version.get("registerId") == register_id and version.get("start") == start
    ]
    if len(matches) != 1:
        raise TraceError("a point-in-time version could not be matched uniquely to the title history")
    return matches[0]


def ordered_versions(versions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return version history in effective-start order."""
    if not versions or not all(isinstance(version, dict) for version in versions):
        raise TraceError("the title response did not include a usable version history")
    return sorted(
        versions,
        key=lambda version: (
            timestamp_date(version.get("start"), "start date"),
            str(version.get("registeredAt") or ""),
            str(version.get("registerId") or ""),
        ),
    )


def endpoint_index(versions: list[dict[str, Any]], endpoint: dict[str, Any]) -> int:
    """Locate a selected endpoint in ordered version history."""
    matches = [
        index
        for index, version in enumerate(versions)
        if version.get("registerId") == endpoint.get("registerId") and version.get("start") == endpoint.get("start")
    ]
    if len(matches) != 1:
        raise TraceError("an endpoint could not be located uniquely in version history")
    return matches[0]


def normalized_reason(reason: Any) -> dict[str, Any]:
    """Expose bounded affecting-title fields without implying provision relevance."""
    if not isinstance(reason, dict):
        return {"warning": "the Register returned an unreadable compilation reason"}
    candidate = reason.get("affectedByTitle") or reason.get("amendedByTitle")
    affecting_title = None
    if isinstance(candidate, dict):
        title_id = candidate.get("titleId")
        affecting_title = {
            "titleId": title_id,
            "name": candidate.get("name"),
            "seriesType": candidate.get("seriesType"),
            "year": candidate.get("year"),
            "number": candidate.get("number"),
            "provisions": candidate.get("provisions"),
            "officialUrl": (
                f"https://www.legislation.gov.au/{title_id}" if isinstance(title_id, str) and title_id else None
            ),
        }
    return {
        "affect": reason.get("affect"),
        "dateChanged": reason.get("dateChanged"),
        "markdown": reason.get("markdown"),
        "affectingTitle": affecting_title,
    }


def normalized_version(version: dict[str, Any], title_id: str) -> dict[str, Any]:
    """Return only fields relevant to a compilation transition."""
    start_date = timestamp_date(version.get("start"), "start date")
    reasons = version.get("reasons")
    if reasons is None:
        reasons = []
    if not isinstance(reasons, list):
        raise TraceError("a version record has an unexpected reasons field")
    return {
        "registerId": version.get("registerId"),
        "compilationNumber": version.get("compilationNumber"),
        "start": version.get("start"),
        "end": version.get("end"),
        "retrospectiveStart": version.get("retrospectiveStart"),
        "retrospectiveEnd": version.get("retrospectiveEnd"),
        "registeredAt": version.get("registeredAt"),
        "status": version.get("status"),
        "hasUnincorporatedAmendments": version.get("hasUnincorporatedAmendments"),
        "reasons": [normalized_reason(reason) for reason in reasons],
        "officialUrl": f"https://www.legislation.gov.au/{title_id}/{start_date}",
    }


def has_retrospective_qualification(version: dict[str, Any]) -> bool:
    """Detect retrospective fields that differ from ordinary effective fields."""
    retrospective_start = version.get("retrospectiveStart")
    retrospective_end = version.get("retrospectiveEnd")
    return bool(
        (retrospective_start and retrospective_start != version.get("start"))
        or (retrospective_end and retrospective_end != version.get("end"))
    )


def trace(title_id: str, from_date: str, to_date: str) -> dict[str, Any]:
    """Return endpoint and intervening compilation metadata for an interval."""
    title = api_get(title_url(title_id))
    title.pop("@odata.context", None)
    raw_versions = title.pop("versions", None)
    versions = ordered_versions(raw_versions) if isinstance(raw_versions, list) else []
    if not versions:
        raise TraceError("the title response did not include a version history")

    from_point = api_get(point_in_time_url(title_id, from_date))
    to_point = api_get(point_in_time_url(title_id, to_date))
    from_version = select_endpoint(versions, from_point)
    to_version = select_endpoint(versions, to_point)
    from_index = endpoint_index(versions, from_version)
    to_index = endpoint_index(versions, to_version)
    if from_index > to_index:
        raise TraceError("the selected endpoint order conflicts with the title version history")

    interval_versions = versions[from_index : to_index + 1]
    transitions = interval_versions[1:]
    same_compilation = from_index == to_index
    all_relevant_versions = [from_version, *transitions]
    retrospective = any(has_retrospective_qualification(version) for version in all_relevant_versions)

    title_summary = {
        key: title.get(key)
        for key in (
            "id",
            "name",
            "collection",
            "subCollection",
            "isPrincipal",
            "isInForce",
            "status",
            "year",
            "number",
            "seriesType",
        )
    }
    return {
        "query": {"titleId": title_id, "from": from_date, "to": to_date},
        "title": title_summary,
        "fromVersion": normalized_version(from_version, title_id),
        "toVersion": normalized_version(to_version, title_id),
        "sameCompilation": same_compilation,
        "transitions": [normalized_version(version, title_id) for version in transitions],
        "currencyFlags": {
            "currentTitleHasCommencedUnincorporatedAmendments": title.get("hasCommencedUnincorporatedAmendments"),
            "fromVersionHasUnincorporatedAmendments": from_version.get("hasUnincorporatedAmendments"),
            "toVersionHasUnincorporatedAmendments": to_version.get("hasUnincorporatedAmendments"),
            "retrospectiveFieldsDiffer": retrospective,
            "knownFutureNameChanges": bool(title.get("namePossibleFuture")),
            "knownFutureStatusChanges": bool(title.get("statusPossibleFuture")),
        },
        "officialUrls": {
            "title": f"https://www.legislation.gov.au/{title_id}",
            "fromPointInTime": f"https://www.legislation.gov.au/{title_id}/{from_date}",
            "toPointInTime": f"https://www.legislation.gov.au/{title_id}/{to_date}",
            "versions": f"https://www.legislation.gov.au/{title_id}/versions",
        },
        "warnings": [
            (
                "Both dates select the same compilation. This shows no compilation "
                "transition, not that legal operation was unchanged."
                if same_compilation
                else "Inspect every listed transition; endpoint comparison can miss a change that later reverted."
            ),
            "Compilation reasons are navigation evidence only. Confirm provision-level relevance from endnotes and amending text.",
            "API metadata does not establish exact text, commencement, incorporation, transitional operation, legal effect or interpretation.",
        ],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    trace_parser = subparsers.add_parser("trace", help="retrieve one bounded compilation-change interval")
    trace_parser.add_argument("title_id", help="Federal Register Title ID")
    trace_parser.add_argument("--from", dest="from_date", required=True, help="YYYY-MM-DD")
    trace_parser.add_argument("--to", dest="to_date", required=True, help="YYYY-MM-DD")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        title_id = validate_title_id(args.title_id)
        from_date, to_date = validate_interval(args.from_date, args.to_date)
        result = trace(title_id, from_date, to_date)
    except TraceError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
