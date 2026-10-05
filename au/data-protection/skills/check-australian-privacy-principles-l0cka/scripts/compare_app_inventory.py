#!/usr/bin/env python3
"""Schema-check and compare provenance-bound APP framework inventories."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

PRIVACY_ACT_TITLE_ID = "C2004A03712"
REGISTER_ID = re.compile(r"^C\d{4}C\d{5}$")
DIGEST = re.compile(r"^[0-9a-f]{64}$")

SCHEMA_VALID = "INVENTORY SCHEMA VALID"
TEXT_UNCHANGED = "APP TEXT AND TRACKED LAYERS UNCHANGED – INDEPENDENT LEGAL VERIFICATION REQUIRED"
CHANGE_DETECTED = "APP FRAMEWORK CHANGE DETECTED – LEGAL CONTENT REVIEW REQUIRED"
APPLICATION_REVIEW = "APP TEXT UNCHANGED – APPLICATION LAW REVIEW REQUIRED"
GUIDANCE_REFRESH = "GUIDANCE REFRESH REQUIRED"
NOT_VERIFIED = "APP FRAMEWORK NOT VERIFIED – DO NOT RELY"

AUTOMATED_DECISION_AMENDMENT = {
    "id": "C2024A00128-schedule-1-part-15-items-87-89",
    "source_title_id": "C2024A00128",
    "commencement": "2026-12-10",
    "application": (
        "Applies to decisions after commencement even if the arrangement, "
        "information use or acquisition occurred earlier."
    ),
}


class InventoryError(ValueError):
    """Raised when an inventory is unsafe to compare."""


def normalize_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFC", value).split())


def require_string(data: dict[str, Any], key: str, location: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise InventoryError(f"{location}.{key}: required non-empty string")
    return value.strip()


def validate_date(value: str, location: str) -> str:
    try:
        date.fromisoformat(value)
    except ValueError as exc:
        raise InventoryError(f"{location}: expected YYYY-MM-DD") from exc
    return value


def validate_timestamp(value: str, location: str) -> str:
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise InventoryError(f"{location}: expected ISO 8601 timestamp") from exc
    return value


def validate_digest(value: str, location: str) -> str:
    if not DIGEST.fullmatch(value):
        raise InventoryError(f"{location}: expected lowercase SHA-256 digest")
    return value


def validate_url(value: str, location: str, title_id: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme != "https" or parsed.hostname not in {
        "legislation.gov.au",
        "www.legislation.gov.au",
    }:
        raise InventoryError(f"{location}: expected an HTTPS Federal Register URL")
    path_parts = {part for part in parsed.path.split("/") if part}
    if title_id not in path_parts:
        raise InventoryError(f"{location}: URL path is not bound to {title_id}")
    return value


def validate_source(data: Any, title_id: str, compilation_id: str, as_at: str) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise InventoryError("inventory.source: expected object")
    canonical_url = validate_url(
        require_string(data, "canonical_url", "inventory.source"),
        "inventory.source.canonical_url",
        title_id,
    )
    final_url = validate_url(
        require_string(data, "final_url", "inventory.source"),
        "inventory.source.final_url",
        title_id,
    )
    if urlparse(canonical_url).path != urlparse(final_url).path:
        raise InventoryError("inventory.source.final_url: redirect changed canonical path")
    version_token = urlparse(canonical_url).path.rstrip("/").split("/")[-1]
    if version_token not in {compilation_id, require_string(data, "effective_from", "inventory.source")}:
        raise InventoryError(
            "inventory.source.canonical_url: final path must identify the compilation ID or effective-from date"
        )
    effective_from = validate_date(
        require_string(data, "effective_from", "inventory.source"),
        "inventory.source.effective_from",
    )
    effective_to_value = data.get("effective_to")
    if effective_to_value is not None:
        if not isinstance(effective_to_value, str):
            raise InventoryError("inventory.source.effective_to: expected date or null")
        effective_to = validate_date(effective_to_value, "inventory.source.effective_to")
    else:
        effective_to = None
    if as_at < effective_from or (effective_to is not None and as_at > effective_to):
        raise InventoryError("inventory.as_at: outside verified compilation effective period")
    return {
        "canonical_url": canonical_url,
        "final_url": final_url,
        "retrieved_at": validate_timestamp(
            require_string(data, "retrieved_at", "inventory.source"),
            "inventory.source.retrieved_at",
        ),
        "raw_sha256": validate_digest(
            require_string(data, "raw_sha256", "inventory.source"),
            "inventory.source.raw_sha256",
        ),
        "effective_from": effective_from,
        "effective_to": effective_to,
    }


def validate_layer(data: Any, name: str) -> dict[str, Any]:
    location = f"inventory.framework_layers.{name}"
    if not isinstance(data, dict):
        raise InventoryError(f"{location}: expected object")
    sources = data.get("sources")
    if (
        not isinstance(sources, list)
        or not sources
        or not all(isinstance(item, str) and item.strip() for item in sources)
    ):
        raise InventoryError(f"{location}.sources: expected non-empty string array")
    return {
        "sha256": validate_digest(require_string(data, "sha256", location), f"{location}.sha256"),
        "sources": sources,
    }


def validate_inventory(data: Any) -> dict[str, Any]:
    """Return a sanitized schema-valid inventory; never claim legal verification."""
    if not isinstance(data, dict):
        raise InventoryError("inventory root: expected object")
    title_id = require_string(data, "title_id", "inventory")
    if title_id != PRIVACY_ACT_TITLE_ID:
        raise InventoryError(f"inventory.title_id: expected {PRIVACY_ACT_TITLE_ID}")
    compilation_id = require_string(data, "compilation_id", "inventory")
    if not REGISTER_ID.fullmatch(compilation_id):
        raise InventoryError("inventory.compilation_id: expected Federal Register compilation ID")
    as_at = validate_date(require_string(data, "as_at", "inventory"), "inventory.as_at")
    source = validate_source(data.get("source"), title_id, compilation_id, as_at)

    coverage = data.get("coverage")
    if not isinstance(coverage, dict):
        raise InventoryError("inventory.coverage: expected object")
    complete = coverage.get("complete")
    if coverage.get("schedule") != "Schedule 1" or not isinstance(complete, bool) or not complete:
        raise InventoryError("inventory.coverage: complete Schedule 1 required")
    method = require_string(coverage, "method", "inventory.coverage")

    principles = data.get("principles")
    if not isinstance(principles, list) or not principles:
        raise InventoryError("inventory.principles: expected non-empty array")
    sanitized: list[dict[str, str]] = []
    seen: set[str] = set()
    for index, principle in enumerate(principles):
        location = f"inventory.principles[{index}]"
        if not isinstance(principle, dict):
            raise InventoryError(f"{location}: expected object")
        identifier = normalize_text(require_string(principle, "identifier", location))
        if identifier in seen:
            raise InventoryError(f"{location}.identifier: duplicate {identifier!r}")
        seen.add(identifier)
        text = normalize_text(require_string(principle, "text", location))
        clause_range = principle.get("clause_range", "")
        if not isinstance(clause_range, str):
            raise InventoryError(f"{location}.clause_range: expected string")
        sanitized.append(
            {
                "identifier": identifier,
                "heading": normalize_text(require_string(principle, "heading", location)),
                "clause_range": normalize_text(clause_range),
                "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            }
        )

    layers = data.get("framework_layers")
    if not isinstance(layers, dict):
        raise InventoryError("inventory.framework_layers: expected object")
    validated_layers = {
        name: validate_layer(layers.get(name), name) for name in ("application_perimeter", "applicable_instruments")
    }
    guidance = validate_layer(layers.get("guidance"), "guidance")

    return {
        "title_id": title_id,
        "compilation_id": compilation_id,
        "as_at": as_at,
        "source": source,
        "coverage": {"schedule": "Schedule 1", "complete": True, "method": method},
        "principles": sanitized,
        "framework_layers": {**validated_layers, "guidance": guidance},
    }


def compare_inventories(earlier: Any, later: Any, horizon: str | None = None) -> dict[str, Any]:
    before = validate_inventory(earlier)
    after = validate_inventory(later)
    if before["as_at"] > after["as_at"]:
        raise InventoryError("comparison chronology: earlier inventory is later than later inventory")

    before_by_id = {item["identifier"]: item for item in before["principles"]}
    after_by_id = {item["identifier"]: item for item in after["principles"]}
    added = [after_by_id[item_id] for item_id in after_by_id.keys() - before_by_id.keys()]
    removed = [before_by_id[item_id] for item_id in before_by_id.keys() - after_by_id.keys()]
    modified = []
    for item_id in before_by_id.keys() & after_by_id.keys():
        fields = [
            field
            for field in ("heading", "clause_range", "text_sha256")
            if before_by_id[item_id][field] != after_by_id[item_id][field]
        ]
        if fields:
            modified.append({"identifier": item_id, "changed_fields": fields})
    before_order = [item["identifier"] for item in before["principles"] if item["identifier"] in after_by_id]
    after_order = [item["identifier"] for item in after["principles"] if item["identifier"] in before_by_id]
    reordered = before_order != after_order
    app_text_changed = bool(added or removed or modified or reordered)

    if before["compilation_id"] == after["compilation_id"]:
        if app_text_changed or before["source"]["raw_sha256"] != after["source"]["raw_sha256"]:
            raise InventoryError("same compilation ID has inconsistent official-document or APP content")

    layer_changes = {
        name: before["framework_layers"][name]["sha256"] != after["framework_layers"][name]["sha256"]
        for name in ("application_perimeter", "applicable_instruments", "guidance")
    }
    statutory_change = (
        app_text_changed or layer_changes["application_perimeter"] or layer_changes["applicable_instruments"]
    )
    guidance_changed = layer_changes["guidance"]

    known_future = []
    if horizon is not None:
        horizon = validate_date(horizon, "horizon")
        if after["as_at"] < AUTOMATED_DECISION_AMENDMENT["commencement"] <= horizon:
            known_future.append(AUTOMATED_DECISION_AMENDMENT)

    if statutory_change:
        status = CHANGE_DETECTED
    elif known_future:
        status = APPLICATION_REVIEW
    else:
        status = TEXT_UNCHANGED

    return {
        "status": status,
        "app_text_status": CHANGE_DETECTED if app_text_changed else "APP TEXT UNCHANGED",
        "application_law_status": APPLICATION_REVIEW
        if any(layer_changes[name] for name in ("application_perimeter", "applicable_instruments")) or known_future
        else "TRACKED APPLICATION LAW UNCHANGED",
        "guidance_status": GUIDANCE_REFRESH if guidance_changed else "TRACKED GUIDANCE UNCHANGED",
        "comparison": {
            "earlier": {"compilation_id": before["compilation_id"], "as_at": before["as_at"]},
            "later": {"compilation_id": after["compilation_id"], "as_at": after["as_at"]},
            "compilation_changed": before["compilation_id"] != after["compilation_id"],
        },
        "changes": {
            "added": sorted(added, key=lambda item: item["identifier"]),
            "removed": sorted(removed, key=lambda item: item["identifier"]),
            "modified": sorted(modified, key=lambda item: item["identifier"]),
            "reordered": reordered,
            "framework_layers": layer_changes,
        },
        "known_future_amendments": known_future,
        "warning": (
            "Schema and digest comparison cannot independently prove that supplied content is official. "
            "Use legislation skills and inspected official source metadata before any legal verification claim."
        ),
    }


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise InventoryError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise InventoryError(f"invalid JSON in {path}:{exc.lineno}:{exc.colno}: {exc.msg}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("inventory", type=Path)
    compare_parser = subparsers.add_parser("compare")
    compare_parser.add_argument("earlier", type=Path)
    compare_parser.add_argument("later", type=Path)
    compare_parser.add_argument("--horizon")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate":
            result = {
                "status": SCHEMA_VALID,
                "inventory": validate_inventory(load_json(args.inventory)),
                "warning": "Schema validation is not authoritative-source or legal verification.",
            }
        else:
            result = compare_inventories(load_json(args.earlier), load_json(args.later), args.horizon)
    except (OSError, InventoryError) as exc:
        print(json.dumps({"status": NOT_VERIFIED, "error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
