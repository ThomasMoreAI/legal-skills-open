"""Deterministic provenance, graph, and confirmation validation."""

from __future__ import annotations

import hashlib
from collections import Counter, defaultdict
from typing import Any

from canonical_json import canonical_sha256, packet_sha256
from output_privacy import scan_model_output
from structural_contracts import validate_packet_semantic_boundary, validate_structure

Issue = dict[str, str]
ESSENTIAL = frozenset({"actor", "action", "object", "matter"})
INELIGIBLE_ROLES = frozenset({"quoted", "context", "inline", "suppressed"})


def _fault(out: list[Issue], code: str, path: str) -> None:
    out.append({"code": code, "path": path})


def _duplicates(values: list[Any]) -> set[Any]:
    return {value for value, count in Counter(values).items() if count > 1}


def _packet_units(packet: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], set[str]]:
    units = packet.get("units")
    if not isinstance(units, list):
        return {}, set()
    by_id = {
        row["unitId"]: row
        for row in units
        if isinstance(row, dict) and isinstance(row.get("unitId"), str)
    }
    assessable = {
        unit_id
        for unit_id, row in by_id.items()
        if row.get("coverageDisposition") == "pending"
        and row.get("eligibility") in {"eligible", "requires_confirmation"}
    }
    return by_id, assessable


def _check_packet_identity(
    packet: dict[str, Any], mapping: dict[str, Any], out: list[Issue]
) -> None:
    actual = packet_sha256(packet)
    declared = packet.get("packetDigestSha256")
    if declared != actual:
        _fault(out, "packet_digest_invalid", "$.packetDigestSha256")
    if mapping.get("packetDigest") != declared:
        _fault(out, "map_packet_digest", "$.packetDigest")
    if mapping.get("runId") != packet.get("runId"):
        _fault(out, "run_id_mismatch", "$.runId")


def _check_unique_ids(
    mapping: dict[str, Any], units: dict[str, dict[str, Any]], out: list[Issue]
) -> None:
    seen: set[str] = set(units)
    for field, key in (
        ("unitAssessment", "unitId"),
        ("atoms", "atomId"),
        ("events", "eventId"),
        ("workstreams", "workstreamId"),
        ("clauses", "clauseId"),
    ):
        ids = [row.get(key) for row in mapping[field]]
        if _duplicates(ids):
            _fault(out, "duplicate_id", f"$.{field}")
        if field != "unitAssessment":
            for identifier in ids:
                if identifier in seen:
                    _fault(out, "duplicate_id", f"$.{field}")
                if isinstance(identifier, str):
                    seen.add(identifier)


def _check_assessment(
    mapping: dict[str, Any], assessable: set[str], out: list[Issue]
) -> dict[str, str]:
    rows = mapping["unitAssessment"]
    ids = [row["unitId"] for row in rows]
    if set(ids) != assessable or len(ids) != len(assessable):
        _fault(out, "unit_partition", "$.unitAssessment")
    return {row["unitId"]: row["disposition"] for row in rows}


def _origin_roles(packet: dict[str, Any]) -> dict[str, str]:
    roles: dict[str, str] = {}
    for field, key in (("mimeLeaves", "mimeLeafId"), ("parts", "partId")):
        rows = packet.get(field, [])
        if isinstance(rows, list):
            for row in rows:
                if isinstance(row, dict) and isinstance(row.get(key), str):
                    role = row.get("role")
                    if isinstance(role, str):
                        roles[row[key]] = role
    return roles


def _check_atoms(
    packet: dict[str, Any],
    mapping: dict[str, Any],
    units: dict[str, dict[str, Any]],
    assessment: dict[str, str],
    out: list[Issue],
) -> dict[str, dict[str, Any]]:
    atoms = {row["atomId"]: row for row in mapping["atoms"]}
    roles = _origin_roles(packet)
    for index, atom in enumerate(mapping["atoms"]):
        path = f"$.atoms[{index}]"
        unit = units.get(atom["unitId"])
        if unit is None:
            _fault(out, "unresolved_atom_unit", f"{path}.unitId")
            continue
        origin_role = roles.get(unit.get("originId", ""))
        confirmable_note = (
            unit.get("kind") == "user_note"
            and unit.get("sourceClass") == "user_attested"
            and unit.get("eligibility") == "requires_confirmation"
            and unit.get("assertedByActorId") == packet.get("actor", {}).get("id")
        )
        if (
            (unit.get("eligibility") != "eligible" and not confirmable_note)
            or unit.get("role") in INELIGIBLE_ROLES
            or origin_role in INELIGIBLE_ROLES
        ):
            _fault(out, "ineligible_atom_unit", f"{path}.unitId")
        if assessment.get(atom["unitId"]) != "used":
            _fault(out, "atom_unit_not_used", f"{path}.unitId")
        text = unit.get("canonicalText")
        if not isinstance(text, str):
            _fault(out, "unit_text_missing", f"$packet.units.{atom['unitId']}")
            continue
        raw = text.encode("utf-8")
        start, end = atom["startByte"], atom["endByte"]
        if not 0 <= start < end <= len(raw):
            _fault(out, "atom_span_bounds", path)
            continue
        span = raw[start:end]
        try:
            span.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            _fault(out, "atom_utf8_boundary", path)
        if hashlib.sha256(span).hexdigest() != atom["spanSha256"]:
            _fault(out, "atom_span_hash", f"{path}.spanSha256")
    return atoms


def _check_events(
    packet: dict[str, Any],
    mapping: dict[str, Any],
    units: dict[str, dict[str, Any]],
    atoms: dict[str, dict[str, Any]],
    out: list[Issue],
) -> tuple[dict[str, str], set[str]]:
    actor = packet.get("actor", {})
    matter = packet.get("matter", {})
    workstream_ids = {row["workstreamId"] for row in mapping["workstreams"]}
    support: dict[str, str] = {}
    used_atoms: set[str] = set()
    spans: dict[str, list[tuple[int, int, str]]] = defaultdict(list)
    for index, event in enumerate(mapping["events"]):
        path = f"$.events[{index}]"
        if event["workstreamId"] not in workstream_ids:
            _fault(out, "unresolved_workstream", f"{path}.workstreamId")
        if event["performedByActorId"] != actor.get("id"):
            _fault(out, "wrong_performed_actor", f"{path}.performedByActorId")
        if event["namedTimekeeperActorId"] != actor.get("id"):
            _fault(out, "wrong_named_timekeeper", f"{path}.namedTimekeeperActorId")
        if event["matterId"] != matter.get("id"):
            _fault(out, "wrong_matter", f"{path}.matterId")
        event_atoms: list[dict[str, Any]] = []
        for atom_id in event["atomIds"]:
            atom = atoms.get(atom_id)
            if atom is None:
                _fault(out, "unresolved_atom", f"{path}.atomIds")
                continue
            if atom_id in used_atoms:
                _fault(out, "atom_reused", f"{path}.atomIds")
            used_atoms.add(atom_id)
            event_atoms.append(atom)
            spans[atom["unitId"]].append(
                (atom["startByte"], atom["endByte"], event["eventId"])
            )
        covered = {
            component for atom in event_atoms for component in atom["components"]
        }
        if not ESSENTIAL <= covered:
            _fault(out, "missing_event_limb", path)
        # A self-authored record with no parseable author metadata may establish
        # actor and action through its own anchored text. Contradictory parsed
        # author metadata still disqualifies the unit for these limbs.
        asserted_components = {
            component
            for atom in event_atoms
            if atom["unitId"] in units
            and units[atom["unitId"]].get("sourceAuthor") in (event["assertedBy"], None)
            for component in atom["components"]
        }
        if not {"actor", "action"} <= asserted_components:
            _fault(out, "asserted_by_not_source_bound", f"{path}.assertedBy")
        classes = {
            units[atom["unitId"]].get("sourceClass")
            for atom in event_atoms
            if atom["unitId"] in units
        }
        if not classes <= {"documentary_supported", "user_attested"}:
            _fault(out, "invalid_source_class", path)
        support[event["eventId"]] = (
            "user_attested" if "user_attested" in classes else "documentary_supported"
        )
    _check_overlaps(spans, out)
    return support, used_atoms


def _check_overlaps(
    spans: dict[str, list[tuple[int, int, str]]], out: list[Issue]
) -> None:
    for unit_id, values in spans.items():
        ordered = sorted(values)
        for left, right in zip(ordered, ordered[1:], strict=False):
            if left[1] > right[0] and left[2] != right[2]:
                _fault(out, "overlapping_event_atoms", f"$packet.units.{unit_id}")


def _check_clauses(
    packet: dict[str, Any], mapping: dict[str, Any], out: list[Issue]
) -> None:
    actor_id = packet.get("actor", {}).get("id")
    events = {row["eventId"]: row for row in mapping["events"]}
    workstreams = {row["workstreamId"] for row in mapping["workstreams"]}
    ws_counts = Counter(row["workstreamId"] for row in mapping["clauses"])
    event_counts = Counter(
        event_id for row in mapping["clauses"] for event_id in row["eventIds"]
    )
    for workstream_id in workstreams:
        if ws_counts[workstream_id] != 1:
            _fault(out, "workstream_clause_count", f"$.workstreams.{workstream_id}")
    for event_id in events:
        if event_counts[event_id] != 1:
            _fault(out, "event_clause_count", f"$.events.{event_id}")
    for index, clause in enumerate(mapping["clauses"]):
        path = f"$.clauses[{index}]"
        if clause["workstreamId"] not in workstreams:
            _fault(out, "unresolved_workstream", f"{path}.workstreamId")
        if clause["clauseOwnerActorId"] != actor_id:
            _fault(out, "wrong_clause_owner", f"{path}.clauseOwnerActorId")
        for event_id in clause["eventIds"]:
            event = events.get(event_id)
            if event is None:
                _fault(out, "unresolved_event", f"{path}.eventIds")
            elif event["workstreamId"] != clause["workstreamId"]:
                _fault(out, "event_workstream_mismatch", f"{path}.eventIds")


def validate_map(packet: dict[str, Any], mapping: dict[str, Any]) -> dict[str, Any]:
    faults = validate_structure("map", mapping)
    if faults:
        return {
            "faults": faults,
            "eventSupport": {},
            "mapDigest": canonical_sha256(mapping),
        }
    packet_faults = validate_packet_semantic_boundary(packet)
    if packet_faults:
        return {
            "faults": packet_faults,
            "eventSupport": {},
            "mapDigest": canonical_sha256(mapping),
        }
    faults.extend(scan_model_output(mapping, packet))
    _check_packet_identity(packet, mapping, faults)
    units, assessable = _packet_units(packet)
    _check_unique_ids(mapping, units, faults)
    assessment = _check_assessment(mapping, assessable, faults)
    atoms = _check_atoms(packet, mapping, units, assessment, faults)
    support, used_atoms = _check_events(packet, mapping, units, atoms, faults)
    if used_atoms != set(atoms):
        _fault(faults, "orphan_atom", "$.atoms")
    used_units = {
        atom["unitId"] for atom in atoms.values() if atom["atomId"] in used_atoms
    }
    assessed_used = {
        unit_id for unit_id, state in assessment.items() if state == "used"
    }
    if used_units != assessed_used:
        _fault(faults, "used_unit_mismatch", "$.unitAssessment")
    _check_clauses(packet, mapping, faults)
    return {
        "faults": faults,
        "eventSupport": support,
        "mapDigest": canonical_sha256(mapping),
    }


def validate_confirmation(
    packet: dict[str, Any], mapping: dict[str, Any], confirmation: dict[str, Any]
) -> dict[str, Any]:
    faults = validate_structure("confirmation", confirmation)
    actual_packet = packet_sha256(packet)
    declared_packet = packet.get("packetDigestSha256")
    actual_map = canonical_sha256(mapping)
    if (
        declared_packet != actual_packet
        or confirmation.get("packetDigest") != declared_packet
    ):
        _fault(faults, "stale_packet_confirmation", "$.packetDigest")
    if mapping.get("packetDigest") != declared_packet:
        _fault(faults, "stale_packet_confirmation", "$map.packetDigest")
    if confirmation.get("mapDigest") != actual_map:
        _fault(faults, "stale_map_confirmation", "$.mapDigest")
    if confirmation.get("confirmationToken") != f"TN-{actual_map[:16]}":
        _fault(faults, "confirmation_token", "$.confirmationToken")
    if confirmation.get("runId") != packet.get("runId") or mapping.get(
        "runId"
    ) != packet.get("runId"):
        _fault(faults, "confirmation_run_id", "$.runId")
    return {"faults": faults, "mapDigest": actual_map}
