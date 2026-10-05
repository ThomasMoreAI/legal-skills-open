"""Deterministic provenance-DAG and packet arithmetic validation."""

from __future__ import annotations

import hashlib
from collections import Counter
from typing import Any

Issue = dict[str, str]


def _issue(path: str) -> Issue:
    return {"code": "packet_provenance", "path": path}


def _inventory(
    packet: dict[str, Any], field: str, key: str, out: list[Issue]
) -> dict[str, dict[str, Any]]:
    rows = packet[field]
    identifiers = [row[key] for row in rows]
    if len(identifiers) != len(set(identifiers)):
        out.append(_issue(f"$packet.{field}"))
    return {row[key]: row for row in rows}


def _root_and_container_edges(
    roots: dict[str, dict[str, Any]],
    containers: dict[str, dict[str, Any]],
    leaves: dict[str, dict[str, Any]],
    out: list[Issue],
) -> None:
    root_container_ids: list[str] = []
    for root_id, root in roots.items():
        container_id = root["containerId"]
        root_container_ids.append(container_id)
        container = containers.get(container_id)
        if container is None or container["rootId"] != root_id:
            out.append(_issue(f"$packet.roots.{root_id}.containerId"))
        elif container["parentContainerId"] is not None:
            out.append(_issue(f"$packet.containers.{container_id}.parentContainerId"))
    if len(root_container_ids) != len(set(root_container_ids)):
        out.append(_issue("$packet.roots.containerId"))
    child_links = [
        leaf["childContainerId"]
        for leaf in leaves.values()
        if leaf["childContainerId"] is not None
    ]
    derived = [
        identifier
        for identifier, row in containers.items()
        if row["parentContainerId"] is not None
    ]
    if Counter(child_links) != Counter(derived):
        out.append(_issue("$packet.containers.derived"))
    top_level = {
        identifier
        for identifier, row in containers.items()
        if row["parentContainerId"] is None
    }
    if top_level != set(root_container_ids):
        out.append(_issue("$packet.containers.topLevel"))
    for container_id, container in containers.items():
        root_id = container["rootId"]
        if root_id not in roots:
            out.append(_issue(f"$packet.containers.{container_id}.rootId"))
        parent_id = container["parentContainerId"]
        if parent_id is not None:
            parent = containers.get(parent_id)
            if parent is None or parent["rootId"] != root_id:
                out.append(
                    _issue(f"$packet.containers.{container_id}.parentContainerId")
                )
        seen: set[str] = set()
        cursor: str | None = container_id
        while cursor is not None and cursor in containers:
            if cursor in seen:
                out.append(
                    _issue(f"$packet.containers.{container_id}.parentContainerId")
                )
                break
            seen.add(cursor)
            cursor = containers[cursor]["parentContainerId"]


def _mime_edges(
    containers: dict[str, dict[str, Any]],
    leaves: dict[str, dict[str, Any]],
    out: list[Issue],
) -> None:
    for leaf_id, leaf in leaves.items():
        container_id = leaf["containerId"]
        if container_id not in containers:
            out.append(_issue(f"$packet.mimeLeaves.{leaf_id}.containerId"))
        child_id = leaf["childContainerId"]
        child_linked = leaf["disposition"] in {"expanded", "exactDuplicate"}
        if child_linked != (child_id is not None):
            out.append(_issue(f"$packet.mimeLeaves.{leaf_id}.childContainerId"))
        if child_id is not None:
            child = containers.get(child_id)
            if (
                child is None
                or child["parentContainerId"] != container_id
                or child["originLocator"] != leaf["locator"]
            ):
                out.append(_issue(f"$packet.mimeLeaves.{leaf_id}.childContainerId"))


def _part_and_unit_edges(
    containers: dict[str, dict[str, Any]],
    leaves: dict[str, dict[str, Any]],
    parts: dict[str, dict[str, Any]],
    units: dict[str, dict[str, Any]],
    out: list[Issue],
) -> None:
    for part_id, part in parts.items():
        if part["containerId"] not in containers:
            out.append(_issue(f"$packet.parts.{part_id}.containerId"))
        actual = [
            unit_id for unit_id, unit in units.items() if unit["originId"] == part_id
        ]
        if Counter(part["unitIds"]) != Counter(actual):
            out.append(_issue(f"$packet.parts.{part_id}.unitIds"))
    for unit_id, unit in units.items():
        container_id = unit["containerId"]
        if container_id not in containers:
            out.append(_issue(f"$packet.units.{unit_id}.containerId"))
        origin_id = unit["originId"]
        if origin_id == container_id:
            continue
        origin = leaves.get(origin_id) or parts.get(origin_id)
        if origin is None or origin["containerId"] != container_id:
            out.append(_issue(f"$packet.units.{unit_id}.originId"))
    _docx_unit_edges(containers, parts, units, out)


def _docx_unit_edges(
    containers: dict[str, dict[str, Any]],
    parts: dict[str, dict[str, Any]],
    units: dict[str, dict[str, Any]],
    out: list[Issue],
) -> None:
    for unit_id, unit in units.items():
        kind = unit.get("kind")
        is_docx_kind = isinstance(kind, str) and kind.startswith("docx_")
        container = containers.get(unit.get("containerId"))
        is_docx_container = (
            container is not None and container.get("sourceType") == "docx"
        )
        if not is_docx_container:
            continue
        path = f"$packet.units.{unit_id}"
        if not is_docx_kind:
            out.append(_issue(f"{path}.kind"))
        part = parts.get(unit.get("originId"))
        if (
            part is None
            or part.get("containerId") != unit.get("containerId")
            or part.get("unitIds", []).count(unit_id) != 1
        ):
            out.append(_issue(f"{path}.originId"))
            continue
        if part.get("role") != "story":
            out.append(_issue(f"$packet.parts.{part['partId']}.role"))
        if part.get("disposition") != "ready":
            out.append(_issue(f"$packet.parts.{part['partId']}.disposition"))
        part_locator = part.get("locator")
        if not isinstance(part_locator, str) or not part_locator.startswith("docx:"):
            out.append(_issue(f"$packet.parts.{part['partId']}.locator"))
            continue
        part_name = part_locator.removeprefix("docx:")
        metadata = unit.get("metadata")
        if not isinstance(metadata, dict) or metadata.get("partName") != part_name:
            out.append(_issue(f"{path}.metadata.partName"))
        locator = unit.get("locator")
        if not isinstance(locator, str) or not locator.startswith(f"{part_locator}#"):
            out.append(_issue(f"{path}.locator"))


def _text_and_budget(
    packet: dict[str, Any], units: dict[str, dict[str, Any]], out: list[Issue]
) -> None:
    total = 0
    for unit_id, unit in units.items():
        encoded = unit["canonicalText"].encode("utf-8")
        total += len(encoded)
        if hashlib.sha256(encoded).hexdigest() != unit["canonicalUtf8Sha256"]:
            out.append(_issue(f"$packet.units.{unit_id}.canonicalUtf8Sha256"))
        if unit["utf8End"] - unit["utf8Start"] != len(encoded):
            out.append(_issue(f"$packet.units.{unit_id}.utf8End"))
    budget = packet["budget"]
    limit = packet["limits"]["modelVisibleUtf8Bytes"]
    if budget["modelVisibleUtf8Bytes"] != total:
        out.append(_issue("$packet.budget.modelVisibleUtf8Bytes"))
    if budget["modelVisibleUtf8Limit"] != limit:
        out.append(_issue("$packet.budget.modelVisibleUtf8Limit"))
    if budget["withinLimit"] != (total <= limit):
        out.append(_issue("$packet.budget.withinLimit"))


def validate_packet_edges(packet: dict[str, Any]) -> list[Issue]:
    out: list[Issue] = []
    roots = _inventory(packet, "roots", "rootId", out)
    containers = _inventory(packet, "containers", "containerId", out)
    leaves = _inventory(packet, "mimeLeaves", "mimeLeafId", out)
    parts = _inventory(packet, "parts", "partId", out)
    units = _inventory(packet, "units", "unitId", out)
    _root_and_container_edges(roots, containers, leaves, out)
    _mime_edges(containers, leaves, out)
    _part_and_unit_edges(containers, leaves, parts, units, out)
    _text_and_budget(packet, units, out)
    unique = {(issue["code"], issue["path"]): issue for issue in out}
    return [unique[key] for key in sorted(unique)]
