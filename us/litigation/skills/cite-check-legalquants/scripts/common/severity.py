"""Derived legal-severity rollup for cite-check reports.

Workers never author a severity tier. The aggregator computes a worst-of
red/amber/yellow/green value from worker enums, fabrication indicators, and a
deterministic reporter-collision cross-check against supplied-authority
identity metadata.
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

SEVERITY_RANK = {"red": 0, "amber": 1, "yellow": 2, "green": 3}
REFERENCE_MATERIAL_KINDS = frozenset({"statute", "rule", "regulation"})
RED_RESOLUTIONS = frozenset({"not_supplied_not_found_potential_hallucination"})
AMBER_RESOLUTIONS = frozenset(
    {
        "not_supplied_confirmed_exists_elsewhere",
        "not_supplied_search_unavailable",
    }
)
COLLISION_FLAG = "reporter_collision_with_supplied_authority"
REFERENCE_BUCKET = "reference_material_not_checked"
EVIDENCE_VALIDATION_FLAGS = frozenset(
    {
        "source_not_in_authority_universe",
        "source_not_found",
        "missing_excerpt",
        "missing_locator",
        "malformed_citation",
        "malformed_source_id",
        "source_resolution_inconsistent",
        "source_resolution_indicator_inconsistent",
    }
)

_NEUTRAL_RE = re.compile(r"\b(\d{4}-[A-Za-z]+-\d+)\b")
_REPORTER_RE = re.compile(
    r"\b(\d+)\s+"
    r"("
    r"F\.\s*Supp\.\s*(?:2d|3d)|"
    r"F\.\s*\d+th|"
    r"F\.\s*App['’]?x|"
    r"F\.\s*3d|"
    r"F\.\s*2d|"
    r"U\.S\.|"
    r"S\.\s*Ct\.|"
    r"Ohio\s+App\.3d|"
    r"Ohio\s+St\.3d|"
    r"Cal\.\d+th|"
    r"[A-Z][A-Za-z.']+(?:\s+[A-Z][A-Za-z.']+){0,2}"
    r")\s+"
    r"(\d+)\b"
)


def _normalize_cite_text(value: str) -> str:
    text = unicodedata.normalize("NFKC", value).replace("’", "'")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\b(St|App)\.\s+(\d+d)\b", r"\1.\2", text, flags=re.I)
    text = re.sub(r"\bF\.\s+Supp\.\s+", "F. Supp. ", text, flags=re.I)
    text = re.sub(r"\bF\.\s+App'?x\b", "F. App'x", text, flags=re.I)
    return text


def _canonical_reporter(reporter: str) -> str:
    reporter = re.sub(r"\s+", " ", reporter).strip()
    reporter = re.sub(r"\b(St|App)\.\s+(\d+d)\b", r"\1.\2", reporter, flags=re.I)
    reporter = re.sub(r"\bF\.\s+App'?x\b", "F. App'x", reporter, flags=re.I)
    if re.fullmatch(r"Ohio\s+App\.3d", reporter, flags=re.I):
        return "Ohio App.3d"
    if re.fullmatch(r"Ohio\s+St\.3d", reporter, flags=re.I):
        return "Ohio St.3d"
    if re.fullmatch(r"F\.\s*App'x", reporter, flags=re.I):
        return "F. App'x"
    if re.fullmatch(r"F\.\s*Supp\.\s*(2d|3d)", reporter, flags=re.I):
        edition = re.search(r"(2d|3d)", reporter, flags=re.I)
        return f"F. Supp. {edition.group(1).lower()}" if edition else reporter
    if re.fullmatch(r"F\.\s*\d+th", reporter, flags=re.I):
        number = re.search(r"\d+", reporter)
        return f"F.{number.group(0)}th" if number else reporter
    if re.fullmatch(r"F\.\s*3d", reporter, flags=re.I):
        return "F.3d"
    if re.fullmatch(r"F\.\s*2d", reporter, flags=re.I):
        return "F.2d"
    if re.fullmatch(r"Cal\.\d+th", reporter, flags=re.I):
        number = re.search(r"\d+", reporter)
        return f"Cal.{number.group(0)}th" if number else reporter
    return reporter


def parse_reporter_coordinates(text: Any) -> set[str]:
    """Return canonical reporter/neutral coordinates found in *text*."""

    if not isinstance(text, str) or not text:
        return set()
    normalized = _normalize_cite_text(text)
    found: set[str] = set()
    for match in _NEUTRAL_RE.finditer(normalized):
        found.add(match.group(1))
    for match in _REPORTER_RE.finditer(normalized):
        volume, reporter, page = match.groups()
        found.add(f"{volume} {_canonical_reporter(reporter)} {page}")
    return found


_KIND_VALUES = frozenset({"case", "statute", "rule", "regulation", "record", "other"})


def infer_citation_kind(row: Mapping[str, Any]) -> str:
    """Classify a legacy row from its written cite. Worker-authored kinds win."""

    existing = row.get("citation_kind")
    if existing in _KIND_VALUES:
        return existing
    text = " ".join(
        part
        for part in (
            row.get("citation_as_written_in_unit"),
            row.get("matched_citation"),
        )
        if isinstance(part, str)
    )
    if re.search(r"\bC\.?F\.?R\.?\b|\bCFR\b", text, flags=re.I):
        return "regulation"
    if re.search(
        r"\b(?:Fed\.\s*R\.|[A-Z][A-Za-z]+\s+R\.)|\bRule\s+\d+",
        text,
        flags=re.I,
    ):
        return "rule"
    if re.search(r"\bU\.S\.C\.\b|§\s*\d+", text):
        return "statute"
    if parse_reporter_coordinates(text) or re.search(r"\bv\.\s", text):
        return "case"
    return "other"


def citation_severity(
    row: Mapping[str, Any],
    *,
    collision: bool = False,
) -> tuple[str, str | None]:
    """Return ``(tier, bucket)`` for one citation row.

    ``quotation_technically_accurate_but_misleading_or_unfair`` stays yellow
    until the product policy determines whether a dispositive misleading
    quotation should escalate to red.
    """

    indicators = row.get("fabrication_indicators")
    has_indicators = isinstance(indicators, list) and any(
        isinstance(item, str) and item for item in indicators
    )
    resolution = row.get("source_resolution")
    if collision:
        return "red", None
    validation_flags = row.get("validation_flags")
    if isinstance(validation_flags, list) and (
        "source_resolution_indicator_inconsistent" in validation_flags
    ):
        # Conflicting fields are an amber evidence defect until repaired. The
        # declared unavailable/confirmed search outcome remains readable below.
        if resolution not in AMBER_RESOLUTIONS:
            return "amber", None
    if resolution in AMBER_RESOLUTIONS:
        kind = row.get("citation_kind") or "other"
        not_supplied = (
            row.get("matched_source_id") is None
            or resolution in AMBER_RESOLUTIONS | RED_RESOLUTIONS
        )
        bucket = (
            REFERENCE_BUCKET
            if kind in REFERENCE_MATERIAL_KINDS and not_supplied
            else None
        )
        return "amber", bucket
    if has_indicators:
        return "red", None
    if resolution in RED_RESOLUTIONS:
        return "red", None
    if (
        row.get("accuracy_of_source_characterization")
        == "objectively_false_or_unreasonable_characterization_of_source"
    ):
        return "red", None
    if row.get("accuracy_of_direct_quotation") == "quotation_objectively_inaccurate":
        return "red", None

    accuracy_values = (
        row.get("accuracy_of_source_characterization"),
        row.get("pincite_accuracy"),
        row.get("accuracy_of_direct_quotation"),
    )
    source_not_found = any(
        isinstance(value, str) and value.startswith("source_not_found_")
        for value in accuracy_values
    )
    if source_not_found:
        kind = row.get("citation_kind") or "other"
        not_supplied = (
            row.get("matched_source_id") is None
            or row.get("source_resolution") in AMBER_RESOLUTIONS | RED_RESOLUTIONS
        )
        bucket = (
            REFERENCE_BUCKET
            if kind in REFERENCE_MATERIAL_KINDS and not_supplied
            else None
        )
        return "amber", bucket

    if row.get("pincite_accuracy") == "pincite_inaccurate":
        return "yellow", None
    if (
        row.get("accuracy_of_source_characterization")
        == "potentially_unfair_or_unreasonable_characterization_of_source"
    ):
        return "yellow", None
    if (
        row.get("accuracy_of_direct_quotation")
        == "quotation_technically_accurate_but_misleading_or_unfair"
    ):
        return "yellow", None

    # Validation is an evidence-completeness gate, not a replacement for the
    # worker's legal judgment.  Preserve substantive red/yellow findings above;
    # only prevent a row with unusable evidence from presenting as verified.
    validation_flags = row.get("validation_flags")
    if isinstance(validation_flags, list) and any(
        flag in EVIDENCE_VALIDATION_FLAGS for flag in validation_flags
    ):
        return "amber", None
    return "green", None


def _authority_coordinates(authority: Mapping[str, Any]) -> set[str]:
    identity = authority.get("contentIdentity")
    parts: list[str] = []
    if isinstance(identity, Mapping):
        for field in ("caseName", "reporterCitation", "title"):
            value = identity.get(field)
            if isinstance(value, str) and value:
                parts.append(value)
    return parse_reporter_coordinates(" ".join(parts))


def _source_label(authority: Mapping[str, Any]) -> str:
    identity = authority.get("contentIdentity")
    if isinstance(identity, Mapping):
        for field in ("caseName", "reporterCitation", "title"):
            value = identity.get(field)
            if isinstance(value, str) and value:
                return value
    filename = authority.get("filename")
    if isinstance(filename, str) and filename:
        return filename
    return str(authority.get("sourceId", ""))


def annotate_severity(
    results: Sequence[dict[str, Any]],
    authorities: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """Attach aggregator-owned severity fields. Do not rewrite worker values."""

    authority_index = [
        (
            str(authority["sourceId"]),
            _authority_coordinates(authority),
            _source_label(authority),
        )
        for authority in authorities
        if isinstance(authority, Mapping) and "sourceId" in authority
    ]
    matched_ids: set[str] = set()
    collisions_by_source: dict[str, list[dict[str, str]]] = {}

    for result in results:
        citations = result.get("citations")
        if not isinstance(citations, list):
            result["severity"] = "green"
            continue
        worst = "green"
        for row in citations:
            if not isinstance(row, Mapping):
                continue
            if "citation_kind" not in row:
                row["citation_kind"] = infer_citation_kind(row)
            source_id = row.get("matched_source_id")
            if isinstance(source_id, str) and source_id:
                matched_ids.add(source_id)
            colliding_id: str | None = None
            flags: list[str] = []
            if source_id is None:
                cite_coords = parse_reporter_coordinates(
                    " ".join(
                        part
                        for part in (
                            row.get("citation_as_written_in_unit"),
                            row.get("matched_citation"),
                        )
                        if isinstance(part, str)
                    )
                )
                for candidate_id, auth_coords, _label in authority_index:
                    if cite_coords and cite_coords & auth_coords:
                        colliding_id = candidate_id
                        flags.append(COLLISION_FLAG)
                        collisions_by_source.setdefault(candidate_id, []).append(
                            {
                                "unitId": str(result.get("unitId", "")),
                                "citation": str(
                                    row.get("citation_as_written_in_unit") or ""
                                ),
                            }
                        )
                        break
            tier, bucket = citation_severity(row, collision=colliding_id is not None)
            row["severity"] = tier
            if bucket is not None:
                row["severity_bucket"] = bucket
            row["aggregator_flags"] = flags
            if colliding_id is not None:
                row["aggregator_colliding_source_id"] = colliding_id
            row["severity_reason"] = severity_reason(row)
            if SEVERITY_RANK[tier] < SEVERITY_RANK[worst]:
                worst = tier
        result["severity"] = worst if citations else "green"

    unused: list[dict[str, Any]] = []
    for source_id, _coords, label in authority_index:
        if source_id in matched_ids:
            continue
        item: dict[str, Any] = {
            "sourceId": source_id,
            "identityLabel": label,
        }
        if source_id in collisions_by_source:
            item["collisions"] = collisions_by_source[source_id]
        unused.append(item)
    return unused


def _case_name(row: Mapping[str, Any]) -> str:
    text = row.get("citation_as_written_in_unit") or row.get("matched_citation") or ""
    if not isinstance(text, str) or not text.strip():
        return "an unnamed citation"
    return text.split(",", 1)[0].strip()


def severity_reason(row: Mapping[str, Any]) -> str:
    colliding = row.get("aggregator_colliding_source_id")
    if colliding:
        return f"The reporter citation belongs to a different case ({colliding})"
    indicators = row.get("fabrication_indicators") or []
    resolution = row.get("source_resolution")
    if resolution == "not_supplied_search_unavailable":
        return "The environment could not search"
    if resolution == "not_supplied_confirmed_exists_elsewhere":
        return "Case found but not supplied for substantive checking"
    validation_flags = row.get("validation_flags")
    if isinstance(validation_flags, list) and (
        "source_resolution_indicator_inconsistent" in validation_flags
    ):
        return "Search outcome fields conflict — could not verify"
    if isinstance(indicators, list):
        if "citation_malformed_or_impossible" in indicators:
            return "Citation is malformed or impossible"
        if "not_found_in_external_search" in indicators:
            return "Search did not find the case — it may be hallucinated"
        if "reporter_coordinates_belong_to_different_supplied_case" in indicators:
            worker_id = row.get("colliding_source_id")
            if isinstance(worker_id, str) and worker_id:
                return (
                    f"The reporter citation belongs to a different case ({worker_id})"
                )
            return "The reporter citation belongs to a different supplied case"
    if resolution in RED_RESOLUTIONS:
        return "Search did not find the case — it may be hallucinated"
    if (
        row.get("accuracy_of_source_characterization")
        == "objectively_false_or_unreasonable_characterization_of_source"
    ):
        return "Contradicts the cited source"
    if row.get("accuracy_of_direct_quotation") == "quotation_objectively_inaccurate":
        return "Quotation does not appear in the source as written"
    if row.get("pincite_accuracy") == "pincite_inaccurate":
        return "Wrong page or paragraph cited"
    if (
        row.get("accuracy_of_source_characterization")
        == "potentially_unfair_or_unreasonable_characterization_of_source"
    ):
        return "Overstates the source or omits a material qualification"
    if (
        row.get("accuracy_of_direct_quotation")
        == "quotation_technically_accurate_but_misleading_or_unfair"
    ):
        return "Quotation accurate but used misleadingly"
    if isinstance(validation_flags, list) and any(
        flag in EVIDENCE_VALIDATION_FLAGS for flag in validation_flags
    ):
        return "Evidence is incomplete — could not verify against supplied source"
    if row.get("severity") == "amber":
        return "Source not supplied — could not verify"
    return "Supported by the supplied source"


def build_triage(
    results: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    """Lawyer-facing rollup consumed by the report template."""

    cards: list[dict[str, Any]] = []
    counts = {"red": 0, "amber": 0, "yellow": 0, "green": 0}
    reference_count = 0
    for result in results:
        citations = result.get("citations")
        if not isinstance(citations, list):
            continue
        for row in citations:
            if not isinstance(row, Mapping):
                continue
            tier = str(row.get("severity") or "green")
            if tier not in counts:
                tier = "green"
            counts[tier] += 1
            if row.get("severity_bucket") == REFERENCE_BUCKET:
                reference_count += 1
            cards.append(
                {
                    "unitId": str(result.get("unitId") or ""),
                    "citation": str(row.get("citation_as_written_in_unit") or ""),
                    "caseName": _case_name(row),
                    "severity": tier,
                    "reason": severity_reason(row),
                    "recommended_changes": row.get("recommended_changes"),
                    "aggregator_colliding_source_id": row.get(
                        "aggregator_colliding_source_id"
                    ),
                    "citation_kind": row.get("citation_kind") or "other",
                    "source_resolution": row.get("source_resolution"),
                }
            )

    fabricated = [
        card
        for card in cards
        if card["severity"] == "red"
        and (
            card.get("aggregator_colliding_source_id")
            or card.get("source_resolution") in RED_RESOLUTIONS
            or "fabricated" in card["reason"].lower()
            or "hallucinated" in card["reason"].lower()
            or "not found" in card["reason"].lower()
            or "different case" in card["reason"].lower()
        )
    ]
    contradicted = [
        card for card in cards if card["severity"] == "red" and card not in fabricated
    ]
    parts: list[str] = []
    if fabricated:
        names = "; ".join(card["caseName"] for card in fabricated)
        parts.append(
            f"{len(fabricated)} "
            f"{'citation' if len(fabricated) == 1 else 'citations'} "
            f"may be fabricated — {names}."
        )
    if contradicted:
        parts.append(
            f"{len(contradicted)} "
            f"{'citation' if len(contradicted) == 1 else 'citations'} "
            f"contradict their cited sources."
        )
    if not parts and counts["yellow"]:
        parts.append(
            f"{counts['yellow']} "
            f"{'citation needs' if counts['yellow'] == 1 else 'citations need'} "
            "correction before filing."
        )
    if not parts:
        total = sum(counts.values())
        if counts["amber"]:
            amber_text = (
                f"{counts['amber']} "
                f"{'citation could' if counts['amber'] == 1 else 'citations could'} "
                "not be verified"
            )
            if counts["green"]:
                parts.append(
                    f"{counts['green']} "
                    f"{'citation is' if counts['green'] == 1 else 'citations are'} "
                    f"supported by supplied sources; {amber_text}."
                )
            else:
                parts.append(amber_text.capitalize() + ".")
        elif total:
            parts.append(f"All {total} citations are supported by supplied sources.")
        else:
            parts.append("No citations were reported.")

    return {
        "worst": worst_severity(tier for tier, count in counts.items() if count)
        if sum(counts.values())
        else "green",
        "headline": " ".join(parts),
        "counts": counts,
        "referenceMaterialCount": reference_count,
        "findings": [card for card in cards if card["severity"] in {"red", "yellow"}],
    }


def authority_rollup(
    results: Sequence[Mapping[str, Any]],
    authorities: Sequence[Mapping[str, Any]],
    unused: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """One row per resolved authority plus unused supplied authorities."""

    by_id: dict[str, dict[str, Any]] = {}
    for result in results:
        unit_id = str(result.get("unitId") or "")
        for row in result.get("citations") or []:
            if not isinstance(row, Mapping):
                continue
            source_id = row.get("matched_source_id")
            if not isinstance(source_id, str) or not source_id:
                continue
            item = by_id.setdefault(
                source_id,
                {
                    "sourceId": source_id,
                    "identityLabel": source_id,
                    "citation_kind": row.get("citation_kind") or "other",
                    "worst": "green",
                    "timesCited": 0,
                    "unitIds": [],
                },
            )
            item["timesCited"] += 1
            if unit_id and unit_id not in item["unitIds"]:
                item["unitIds"].append(unit_id)
            item["worst"] = worst_severity(
                (item["worst"], str(row.get("severity") or "green"))
            )
            kind = row.get("citation_kind")
            if isinstance(kind, str) and kind:
                item["citation_kind"] = kind

    for authority in authorities:
        source_id = str(authority.get("sourceId") or "")
        if source_id in by_id:
            by_id[source_id]["identityLabel"] = _source_label(authority)

    rows = list(by_id.values())
    for item in unused:
        source_id = str(item.get("sourceId") or "")
        collisions = item.get("collisions") or []
        note = ""
        if collisions:
            first = collisions[0]
            note = (
                f"{source_id} — its citation appears in the brief attributed to "
                f"{first.get('citation', '')} ({first.get('unitId', '')})"
            )
        rows.append(
            {
                "sourceId": source_id,
                "identityLabel": item.get("identityLabel") or source_id,
                "citation_kind": "other",
                "worst": "red" if collisions else "green",
                "timesCited": 0,
                "unitIds": [],
                "unused": True,
                "collisionNote": note,
                "collisions": collisions,
            }
        )
    rows.sort(
        key=lambda item: (
            SEVERITY_RANK.get(str(item.get("worst")), 99),
            0 if item.get("unused") else 1,
            str(item.get("sourceId") or ""),
        )
    )
    return rows


def worst_severity(values: Iterable[str]) -> str:
    worst = "green"
    for value in values:
        if value in SEVERITY_RANK and SEVERITY_RANK[value] < SEVERITY_RANK[worst]:
            worst = value
    return worst
