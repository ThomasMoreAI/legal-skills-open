#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import textwrap
import pathlib
import urllib.parse
from datetime import datetime, timezone
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "lib"))
import nzfetch  # noqa: E402


BASE = "https://data.linz.govt.nz/services/api/v1/"
TIMEOUT = 10
UA = "Mozilla/5.0 linz-title-memorials/1.0"
MIN_CELL_SIZE = 6

SOURCES = [
    {
        "resource_type": "layer",
        "id": 50804,
        "path": "layers/50804/",
        "role": "Simplified public title metadata. It excludes ownership and does not include memorial or instrument text.",
        "sensitive_fields": ["title_no"],
    },
    {
        "resource_type": "set",
        "id": 4748,
        "path": "sets/4748/",
        "role": "Public catalogue set for Landonline title memorial tables.",
        "sensitive_fields": [],
    },
    {
        "resource_type": "table",
        "id": 52006,
        "path": "tables/52006/",
        "role": "Title memorial rows. Useful as metadata, but row data includes title numbers and action identifiers.",
        "sensitive_fields": [
            "ttl_title_no",
            "act_id_orig",
            "act_tin_id_orig",
            "act_id_crt",
            "act_tin_id_crt",
            "act_id_ext",
            "act_tin_id_ext",
        ],
    },
    {
        "resource_type": "table",
        "id": 51702,
        "path": "tables/51702/",
        "role": "Landonline action rows. Needed for joins, but not safe to expose as property-level evidence.",
        "sensitive_fields": ["tin_id", "id", "act_id_orig", "act_tin_id_orig", "ste_id"],
    },
    {
        "resource_type": "table",
        "id": 51728,
        "path": "tables/51728/",
        "role": "Small action-type lookup table. Metadata is safe; row lookup is not required for this skill.",
        "sensitive_fields": [],
    },
    {
        "resource_type": "table",
        "id": 52002,
        "path": "tables/52002/",
        "role": "Title-action join table. Row data links title numbers to actions and is not exposed.",
        "sensitive_fields": ["ttl_title_no", "act_tin_id", "act_id"],
    },
    {
        "resource_type": "table",
        "id": 52012,
        "path": "tables/52012/",
        "role": "Title instrument table. Row data includes instrument identifiers and transaction type fields.",
        "sensitive_fields": ["id", "inst_no", "dlg_id", "tin_id_parent"],
    },
    {
        "resource_type": "table",
        "id": 52013,
        "path": "tables/52013/",
        "role": "Instrument-title join table. Row data links instruments to title numbers and is not exposed.",
        "sensitive_fields": ["tin_id", "ttl_title_no"],
    },
    {
        "resource_type": "table",
        "id": 51699,
        "path": "tables/51699/",
        "role": "Statute lookup metadata that may help an official aggregate query classify Building Act records.",
        "sensitive_fields": [],
    },
    {
        "resource_type": "table",
        "id": 51648,
        "path": "tables/51648/",
        "role": "System-code lookup metadata. It may decode memorial or transaction codes in official analysis.",
        "sensitive_fields": [],
    },
]

ALLOWED_GROUPS = {
    "territorial_authority",
    "land_district",
    "hazard_type",
    "year",
    "status",
    "all",
}


class CliError(Exception):
    pass


def get_json(path: str) -> dict[str, Any]:
    url = BASE + path
    try:
        return nzfetch.fetch_json(url, timeout=TIMEOUT, accept="application/json")
    except nzfetch.Blocked as exc:
        raise CliError(f"network failure calling {url}: {exc}") from None
    except nzfetch.FetchError as exc:
        raise CliError(str(exc)) from None


def output(data: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return

    kind = data.get("kind")
    if kind == "metadata":
        print("LINZ title memorial public metadata boundary")
        print("Row-level records exposed by this command: no")
        print(f"Sources checked: {len(data['sources'])}")
        for source in data["sources"]:
            count = source.get("feature_count")
            count_text = f"{count:,}" if isinstance(count, int) else "n/a"
            print(
                f"- {source['id']} {source['title']} "
                f"({source['resource_type']}, {source['public_access']}, rows: {count_text})"
            )
            if source["sensitive_fields"]:
                print(f"  row identifiers not exposed: {', '.join(source['sensitive_fields'])}")
        print(data["privacy"]["summary"])
    elif kind == "oia_template":
        print(data["template"])
    elif kind in {"blocked", "boundary"}:
        print(data["summary"])
        if data.get("next_step"):
            print(data["next_step"])
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def field_names(raw: dict[str, Any]) -> list[str]:
    return [field.get("name", "") for field in raw.get("data", {}).get("fields", []) if field.get("name")]


def summarise_source(spec: dict[str, Any], raw: dict[str, Any]) -> dict[str, Any]:
    fields = field_names(raw)
    sensitive = [name for name in spec["sensitive_fields"] if name in fields]
    data = raw.get("data") or {}
    return {
        "id": raw.get("id", spec["id"]),
        "resource_type": spec["resource_type"],
        "title": raw.get("title"),
        "public_access": raw.get("public_access"),
        "url_html": raw.get("url_html"),
        "api_url": raw.get("url"),
        "feature_count": data.get("feature_count"),
        "fields": fields,
        "sensitive_fields": sensitive,
        "role": spec["role"],
    }


def metadata_payload() -> dict[str, Any]:
    sources = [summarise_source(spec, get_json(spec["path"])) for spec in SOURCES]
    return {
        "kind": "metadata",
        "source": "linz-data-service",
        "observed_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "sources": sources,
        "privacy": {
            "row_level_records_exposed": False,
            "summary": (
                "This command inspects only public catalogue metadata and field names. "
                "It does not fetch feature samples, downloads, WFS rows, title numbers, "
                "owners, addresses, instrument rows, or parcel/title-level cells."
            ),
            "blocked_outputs": [
                "individual Records of Title",
                "title numbers",
                "owner names",
                "addresses",
                "memorial text",
                "instrument numbers",
                "small cells that could identify a property",
            ],
        },
        "boundary": {
            "public_metadata_found": True,
            "public_row_tables_exist": True,
            "safe_keyless_aggregate_counts_available": False,
            "why_counts_are_not_returned": (
                "Building Act s73/s74 hazard counts require classifying memorials or instruments "
                "and joining row-level Landonline tables that contain title numbers or title/action "
                "links. This skill does not retrieve or expose those rows."
            ),
        },
    }


def parse_groups(raw: str | None) -> list[str]:
    if not raw:
        return ["territorial_authority", "land_district", "year"]
    groups = [part.strip().lower() for part in raw.split(",") if part.strip()]
    if not groups:
        raise CliError("--group-by must include at least one grouping")
    invalid = [group for group in groups if group not in ALLOWED_GROUPS]
    if invalid:
        allowed = ", ".join(sorted(ALLOWED_GROUPS))
        raise CliError(f"unsupported --group-by value(s): {', '.join(invalid)}; allowed: {allowed}")
    if "all" in groups and len(groups) > 1:
        raise CliError("--group-by all cannot be combined with other groupings")
    return groups


def privacy_clause(min_cell_size: int) -> str:
    return (
        "Please provide aggregate counts only. Suppress, combine, or redact any cell smaller "
        f"than {min_cell_size}. Do not include individual Records of Title, title numbers, "
        "owner names, addresses, parcel identifiers, instrument numbers, or memorial text."
    )


def oia_payload(args: argparse.Namespace) -> dict[str, Any]:
    groups = parse_groups(args.group_by)
    if args.min_cell_size < MIN_CELL_SIZE:
        raise CliError(f"--min-cell-size must be at least {MIN_CELL_SIZE}")

    group_text = ", ".join(groups)
    clause = privacy_clause(args.min_cell_size)
    template = f"""Kia ora,

I request aggregate, de-identified information about Building Act 2004 natural-hazard entries on New Zealand Records of Title.

Please provide, for the period {args.from_date} to {args.to_date}:

1. The count of current Records of Title carrying an entry, memorial, notice, or related registration made for Building Act 2004 s73 natural-hazard notification purposes.
2. The count of entries, memorials, notices, or related registrations removed under Building Act 2004 s74(4), by removal year where held.
3. The counts grouped by: {group_text}.
4. Any available split between current and historical entries, and any available hazard category or territorial-authority field used by LINZ or Landonline.
5. The data definitions, Landonline table/field names, memorial or instrument codes, and caveats needed to interpret the counts.

{clause}

If LINZ does not hold one of the requested breakdowns directly, please provide the closest aggregate count held and explain the limitation. Please provide the result as CSV or spreadsheet data where practical.

Nga mihi
"""
    return {
        "kind": "oia_template",
        "agency": args.agency,
        "requested_grouping": groups,
        "period": {"from": args.from_date, "to": args.to_date},
        "min_cell_size": args.min_cell_size,
        "privacy_clause": clause,
        "template": template,
    }


def blocked_payload(command: str, groups: list[str], min_cell_size: int) -> dict[str, Any]:
    return {
        "kind": "blocked",
        "command": command,
        "status": "official_aggregate_required",
        "requested_grouping": groups,
        "min_cell_size": min_cell_size,
        "summary": (
            "Blocked: this keyless skill will not compute Building Act title memorial counts "
            "from row-level Landonline title, memorial, instrument, or action tables."
        ),
        "reason": (
            "The public LDS catalogue exposes relevant table metadata and downloadable row-level "
            "tables, but the joins needed for s73/s74 hazard counts include title numbers, "
            "instrument identifiers, action identifiers, or small cells that can identify properties."
        ),
        "safe_alternative": "Use metadata to inspect public source boundaries, then request official aggregate counts.",
        "next_step": (
            "Run: python3 skills/linz-title-memorials/scripts/cli.py oia-template "
            f"--group-by {','.join(groups)} --min-cell-size {min_cell_size}"
        ),
        "never_outputs": [
            "individual title records",
            "title numbers",
            "owner or address data",
            "memorial text",
            "instrument rows",
            "unsuppressed small cells",
        ],
    }


def boundary_payload() -> dict[str, Any]:
    return {
        "kind": "boundary",
        "summary": (
            "Public LINZ/LDS metadata can identify relevant Landonline title memorial tables, "
            "but this skill returns only aggregate-safe metadata and OIA wording."
        ),
        "safe": [
            "LDS catalogue metadata",
            "field names",
            "public access flags",
            "feature counts",
            "aggregate-only OIA template text",
        ],
        "blocked": [
            "feature samples from title memorial tables",
            "downloads or WFS queries of title/action/instrument joins",
            "individual titles, owners, addresses, parcel identifiers, instrument numbers, or memorial text",
            "cells smaller than the requested suppression threshold",
        ],
        "next_step": "Run metadata --json for live source metadata or oia-template for an aggregate request.",
    }


def cmd_metadata(args: argparse.Namespace) -> int:
    output(metadata_payload(), args.json)
    return 0


def cmd_boundary(args: argparse.Namespace) -> int:
    output(boundary_payload(), args.json)
    return 0


def cmd_oia(args: argparse.Namespace) -> int:
    output(oia_payload(args), args.json)
    return 0


def cmd_blocked_count(args: argparse.Namespace) -> int:
    groups = parse_groups(args.group_by)
    if args.min_cell_size < MIN_CELL_SIZE:
        raise CliError(f"--min-cell-size must be at least {MIN_CELL_SIZE}")
    output(blocked_payload(args.command_name, groups, args.min_cell_size), args.json)
    return 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect aggregate-safe LINZ/Landonline title memorial public-data boundaries"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    metadata = sub.add_parser("metadata", help="fetch public LDS metadata without row data")
    metadata.add_argument("--json", action="store_true", help="print JSON")
    metadata.set_defaults(func=cmd_metadata)

    boundary = sub.add_parser("boundary", help="explain safe and blocked data surfaces")
    boundary.add_argument("--json", action="store_true", help="print JSON")
    boundary.set_defaults(func=cmd_boundary)

    oia = sub.add_parser("oia-template", help="generate an aggregate-only OIA request template")
    oia.add_argument("--agency", default="Toitu Te Whenua Land Information New Zealand")
    oia.add_argument("--from-date", default="31 March 2005")
    oia.add_argument("--to-date", default="present")
    oia.add_argument(
        "--group-by",
        default="territorial_authority,land_district,year",
        help="comma-separated grouping: territorial_authority, land_district, hazard_type, year, status, or all",
    )
    oia.add_argument("--min-cell-size", type=int, default=MIN_CELL_SIZE)
    oia.add_argument("--json", action="store_true", help="print JSON")
    oia.set_defaults(func=cmd_oia)

    for name in (
        "count-building-act-hazard-notices",
        "count-building-act-hazard-removals",
        "list-instrument-types",
    ):
        count = sub.add_parser(name, help="return a structured blocked response for unsafe row-level analysis")
        count.add_argument(
            "--group-by",
            default="territorial_authority,land_district,year",
            help="comma-separated grouping requested for official aggregates",
        )
        count.add_argument("--min-cell-size", type=int, default=MIN_CELL_SIZE)
        count.add_argument("--json", action="store_true", help="print JSON")
        count.set_defaults(func=cmd_blocked_count, command_name=name)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except CliError as exc:
        if getattr(args, "json", False):
            print(
                json.dumps(
                    {
                        "kind": "error",
                        "status": "error",
                        "message": str(exc),
                    },
                    indent=2,
                )
            )
        else:
            wrapped = textwrap.fill(str(exc), width=88)
            print(f"linz-title-memorials: {wrapped}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
