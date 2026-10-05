"""Consolidate citation-level unit results into a deterministic report.

The preparation manifest owns the complete unit inventory.  A worker result is
one v2 unit receipt: it either reports no citations or carries one row per
citation observed in that unit.  This module deliberately does not reconstruct
a parent citation inventory, bind a citation to a preselected authority, or
run a second model-review contract.

Validation is advisory at the citation level.  The only coverage failures are
missing units and the three defects that prevent a unit result from being
represented at all: non-JSON output, a wrong unit ID, and no salvageable unit
object.  The caller may attach execution receipts after building the report.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections.abc import Callable, Iterable, Mapping, Sequence
from functools import cache
from pathlib import Path
from typing import Any, cast

SCRIPT_PATH = Path(__file__).resolve()
SCRIPTS_DIR = SCRIPT_PATH.parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from common.contracts import (  # noqa: E402
    SCHEMA_DIR,
    RunnerError,
    _load_json,
    validate_schema,
    validate_unit_result,
)
from common.severity import (  # noqa: E402
    SEVERITY_RANK,
    annotate_severity,
    authority_rollup,
    build_triage,
)

MANIFEST_VERSION = "cite-check.manifest.v2"
COVERAGE_VERSION = "cite-check.coverage.v2"
REPORT_VERSION = "cite-check.report.v2"
EXECUTION_FIELDS = ("provider", "surface", "model", "reasoningEffort")
MAX_EXECUTION_VALUE_LENGTH = 160
IDENTIFIER_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,127}$")
RELATIVE_PATH_RE = re.compile(
    r"^(?!/)(?![A-Za-z]:)(?!.*(?:^|/)(?:\.{1,2})(?:/|$))"
    r"(?!.*//)[^\\/\x00-\x1f]+(?:/[^\\/\x00-\x1f]+)*$"
)


class ReportInputError(ValueError):
    """Raised when report input cannot safely enter the report."""


@cache
def _contract_schema(name: str) -> dict[str, Any]:
    try:
        value = _load_json(SCHEMA_DIR / name, name)
    except RunnerError as exc:
        raise ReportInputError(str(exc)) from exc
    if not isinstance(value, dict):
        raise ReportInputError(f"{name} must contain a JSON object schema")
    return value


def _contract_errors(value: Any, name: str, *, path: str = "") -> list[str]:
    return validate_schema(value, _contract_schema(name), path=path)


def _require_contract(value: Any, name: str, label: str) -> None:
    errors = _contract_errors(value, name)
    if errors:
        raise ReportInputError(f"{label} schema invalid: " + "; ".join(errors[:4]))


def _as_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ReportInputError(f"{label} must be an object")
    return cast(dict[str, Any], value)


def _require_keys(value: Mapping[str, Any], keys: Iterable[str], label: str) -> None:
    missing = sorted(set(keys) - set(value))
    if missing:
        raise ReportInputError(
            f"{label} is missing required field(s): {', '.join(missing)}"
        )


def _identifier(value: Any, label: str) -> str:
    if not isinstance(value, str) or IDENTIFIER_RE.fullmatch(value) is None:
        raise ReportInputError(f"{label} is not a safe identifier")
    return value


def _safe_relative_path(value: Any, label: str) -> str:
    if not isinstance(value, str) or RELATIVE_PATH_RE.fullmatch(value) is None:
        raise ReportInputError(f"{label} is not a safe workspace-relative path")
    return value


def _text(value: Any, label: str, *, allow_empty: bool = True) -> str:
    if not isinstance(value, str) or (not allow_empty and not value):
        raise ReportInputError(f"{label} must be a string")
    return value


def _copy_json(value: Any) -> Any:
    try:
        return json.loads(json.dumps(value, ensure_ascii=False))
    except (TypeError, ValueError) as exc:
        raise ReportInputError("report input is not JSON-compatible") from exc


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def _dedupe_objects(values: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    result: list[dict[str, Any]] = []
    for value in values:
        copied = _copy_json(dict(value))
        key = _canonical_json(copied)
        if key not in seen:
            seen.add(key)
            result.append(copied)
    return result


def _safe_normalize_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).split())


def _read_unit_text(
    source_root: Path | None, unit: Mapping[str, Any]
) -> tuple[str | None, str | None]:
    """Read the assigned unit only when the caller supplied a safe run root."""

    if source_root is None:
        return None, None
    root = source_root.resolve()
    candidate = (root / str(unit["path"])).resolve()
    try:
        candidate.relative_to(root)
        text = candidate.read_text(encoding="utf-8")
    except (OSError, UnicodeError, ValueError):
        return None, "unit source is missing or unreadable"
    lines = text.splitlines()
    start = int(unit["lineStart"])
    end = int(unit["lineEnd"])
    if end > len(lines):
        return None, "unit line range is outside its source"
    return "\n".join(lines[start - 1 : end]), None


def _validate_manifest(manifest: Mapping[str, Any]) -> dict[str, Any]:
    _require_contract(manifest, "manifest.schema.json", "manifest")
    _require_keys(
        manifest,
        ("schemaVersion", "runId", "target", "authorities", "units", "limitations"),
        "manifest",
    )
    if manifest["schemaVersion"] != MANIFEST_VERSION:
        raise ReportInputError("manifest has an unsupported schemaVersion")
    run_id = _identifier(manifest["runId"], "manifest.runId")
    target = _as_dict(manifest["target"], "manifest.target")
    _safe_relative_path(target["path"], "manifest.target.path")
    _safe_relative_path(target["fullDocumentRef"], "manifest.target.fullDocumentRef")
    if target["displayName"] is not None:
        _text(target["displayName"], "manifest.target.displayName")

    authorities = manifest["authorities"]
    if not isinstance(authorities, list):
        raise ReportInputError("manifest.authorities must be an array")
    authority_ids: set[str] = set()
    authority_by_id: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(authorities):
        authority = _as_dict(raw, f"manifest.authorities[{index}]")
        source_id = _identifier(
            authority["sourceId"], f"manifest.authorities[{index}].sourceId"
        )
        if source_id in authority_ids:
            raise ReportInputError(f"manifest has duplicate authority ID {source_id}")
        authority_ids.add(source_id)
        _safe_relative_path(authority["path"], f"manifest.authorities[{index}].path")
        _text(
            authority["filename"],
            f"manifest.authorities[{index}].filename",
            allow_empty=False,
        )
        authority_by_id[source_id] = authority

    units = manifest["units"]
    if not isinstance(units, list) or not units:
        raise ReportInputError("manifest.units must be a non-empty array")
    unit_ids: list[str] = []
    unit_by_id: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(units):
        unit = _as_dict(raw, f"manifest.units[{index}]")
        unit_id = _identifier(unit["unitId"], f"manifest.units[{index}].unitId")
        if unit_id in unit_by_id:
            raise ReportInputError(f"manifest has duplicate unit ID {unit_id}")
        if unit["lineStart"] > unit["lineEnd"]:
            raise ReportInputError(f"unit {unit_id} line range is reversed")
        _safe_relative_path(unit["path"], f"manifest.units[{index}].path")
        anchor = unit["footnoteAnchorUnitId"]
        if anchor is not None and not isinstance(anchor, str):
            raise ReportInputError(f"unit {unit_id} footnote anchor is invalid")
        unit_ids.append(unit_id)
        unit_by_id[unit_id] = unit
    unit_id_set = set(unit_ids)
    for unit in unit_by_id.values():
        anchor = unit["footnoteAnchorUnitId"]
        if anchor is not None and anchor not in unit_id_set:
            raise ReportInputError(
                f"unit {unit['unitId']} has an unknown footnote anchor"
            )

    result = _copy_json(dict(manifest))
    result["_runId"] = run_id
    result["_unitIds"] = unit_ids
    result["_unitById"] = unit_by_id
    result["_authorityIds"] = authority_ids
    result["_authorityById"] = authority_by_id
    return result


_AGGREGATOR_CITATION_FIELDS = (
    "validation_flags",
    "severity",
    "severity_bucket",
    "severity_reason",
    "aggregator_flags",
    "aggregator_colliding_source_id",
)
_LEGACY_OPTIONAL_CITATION_FIELDS = (
    "citation_kind",
    "source_resolution",
    "fabrication_indicators",
    "colliding_source_id",
    "existence_check_notes",
)
_SOURCE_RESOLUTION_VALUES = frozenset(
    {
        "matched_supplied_source",
        "not_supplied_confirmed_exists_elsewhere",
        "not_supplied_not_found_potential_hallucination",
        "not_supplied_search_unavailable",
    }
)


def _normalization_input(value: Mapping[str, Any]) -> dict[str, Any]:
    """Return a worker-schema view of a normalized result.

    ``validation_flags`` and aggregator-owned severity fields belong to the
    normalized layer, not to the worker's strict schema.  They are removed only
    for the structural check; the returned report result keeps them intact.
    """

    candidate = _copy_json(dict(value))
    candidate.pop("validation", None)
    candidate.pop("severity", None)
    citations = candidate.get("citations")
    if isinstance(citations, list):
        for citation in citations:
            if isinstance(citation, dict):
                for field in _AGGREGATOR_CITATION_FIELDS:
                    citation.pop(field, None)
    return candidate


def _aggregation_schema() -> dict[str, Any]:
    """Worker schema with new v-next keys optional so legacy rows still load."""

    schema = _copy_json(_contract_schema("cite-check-unit-result.schema.json"))
    citation = schema.get("$defs", {}).get("citation")
    if isinstance(citation, dict) and isinstance(citation.get("required"), list):
        citation["required"] = [
            name
            for name in citation["required"]
            if name not in _LEGACY_OPTIONAL_CITATION_FIELDS
        ]
    return schema


def _add_validation_flag(citation: dict[str, Any], flag: str) -> None:
    flags = citation.get("validation_flags")
    if not isinstance(flags, list):
        flags = []
        citation["validation_flags"] = flags
    if flag not in flags:
        flags.append(flag)


def _sanitize_row_level_evidence(
    candidate: dict[str, Any], authority_ids: set[str]
) -> None:
    """Keep citation rows reportable when evidence fields have bad types/values.

    The worker/runner retains the raw attempt and validator flags.  Aggregation
    may only replace malformed row-level evidence with conservative values so
    the citation remains visible; unit-level shape errors still fail below.
    """

    citations = candidate.get("citations")
    if not isinstance(citations, list):
        return
    for citation in citations:
        if not isinstance(citation, dict):
            continue

        source_id = citation.get("matched_source_id")
        if "matched_source_id" not in citation:
            citation["matched_source_id"] = None
            _add_validation_flag(citation, "malformed_source_id")
            source_id = None
        elif source_id is not None and (
            not isinstance(source_id, str) or not source_id
        ):
            citation["matched_source_id"] = None
            _add_validation_flag(citation, "malformed_source_id")
            source_id = None

        resolution = citation.get("source_resolution")
        if (
            not isinstance(resolution, str)
            or resolution not in _SOURCE_RESOLUTION_VALUES
        ):
            citation["source_resolution"] = (
                "matched_supplied_source"
                if isinstance(source_id, str) and source_id in authority_ids
                else "not_supplied_search_unavailable"
            )
            _add_validation_flag(citation, "malformed_citation")

        indicators = citation.get("fabrication_indicators")
        if "fabrication_indicators" not in citation or not isinstance(indicators, list):
            citation["fabrication_indicators"] = []
            _add_validation_flag(citation, "malformed_citation")
        else:
            valid_indicators = {
                "reporter_coordinates_belong_to_different_supplied_case",
                "not_found_in_external_search",
                "citation_malformed_or_impossible",
            }
            cleaned = [
                item
                for item in indicators
                if isinstance(item, str) and item in valid_indicators
            ]
            deduplicated = list(dict.fromkeys(cleaned))
            if deduplicated != indicators:
                citation["fabrication_indicators"] = deduplicated
                _add_validation_flag(citation, "malformed_citation")

        for field in ("colliding_source_id", "existence_check_notes"):
            if (
                field in citation
                and citation[field] is not None
                and not isinstance(citation[field], str)
            ):
                citation[field] = None
                _add_validation_flag(citation, "malformed_citation")


def _validate_result_shape(
    raw: Any,
    *,
    expected_unit_id: str,
    authority_ids: set[str],
) -> tuple[dict[str, Any] | None, list[dict[str, Any]], str | None]:
    """Normalize one result and return advisory diagnostics plus hard failure."""

    if not isinstance(raw, dict):
        return None, [], "result is not a JSON object"
    normalized = validate_unit_result(
        raw,
        expected_unit_id,
        authority_ids=authority_ids,
    )
    hard_errors = normalized.get("hard_errors")
    if isinstance(hard_errors, list) and hard_errors:
        message = hard_errors[0].get("message", "result is not salvageable")
        return None, hard_errors, str(message)
    candidate = normalized.get("normalized")
    if not isinstance(candidate, dict):
        return None, [], "result did not produce a normalized unit object"
    raw_citations = raw.get("citations")
    normalized_citations = candidate.get("citations")
    if isinstance(raw_citations, list) and isinstance(normalized_citations, list):
        # A runner receipt may already carry validator-owned flags.  Keep them
        # when the report is assembled, while adding any diagnostics discovered
        # during this final structural pass.  Never replace worker-authored
        # citation fields or manufacture a citation row.
        # No strict= on purpose: this ships in the packaged skill and must run
        # on the lawyer's system python3 (3.9); zip(strict=...) needs 3.10+.
        for raw_citation, normalized_citation in zip(  # noqa: B905
            raw_citations, normalized_citations
        ):
            if not isinstance(raw_citation, dict) or not isinstance(
                normalized_citation, dict
            ):
                continue
            previous_flags = raw_citation.get("validation_flags")
            current_flags = normalized_citation.get("validation_flags")
            if isinstance(previous_flags, list) and isinstance(current_flags, list):
                normalized_citation["validation_flags"] = list(
                    dict.fromkeys(
                        flag
                        for flag in [*previous_flags, *current_flags]
                        if isinstance(flag, str)
                    )
                )
    _sanitize_row_level_evidence(candidate, authority_ids)
    schema_errors = validate_schema(
        _normalization_input(candidate), _aggregation_schema()
    )
    if schema_errors:
        return None, [], "result schema invalid: " + "; ".join(schema_errors[:4])
    diagnostics = [
        item
        for item in [
            *(normalized.get("warnings") or []),
            *(normalized.get("potential_issues") or []),
        ]
        if isinstance(item, dict)
    ]
    return candidate, diagnostics, None


def _limitation(
    code: str,
    message: str,
    *,
    unit_id: str | None = None,
    source_id: str | None = None,
    citation_index: int | None = None,
) -> dict[str, Any]:
    value: dict[str, Any] = {"code": code, "message": message}
    if unit_id is not None:
        value["unitId"] = unit_id
    if source_id is not None:
        value["sourceId"] = source_id
    if citation_index is not None:
        value["citationIndex"] = citation_index
    return value


def _source_label(authority: Mapping[str, Any]) -> str:
    identity = authority.get("contentIdentity")
    if isinstance(identity, dict):
        for field in ("caseName", "reporterCitation", "title", "section"):
            value = identity.get(field)
            if isinstance(value, str) and value:
                return value
    return str(authority["filename"])


def _report_contract_errors(report: Mapping[str, Any]) -> list[str]:
    """Check the report's own v2 envelope without a retired report schema."""

    errors: list[str] = []
    required = {
        "schemaVersion",
        "runId",
        "status",
        "target",
        "authoritySources",
        "unitResults",
        "unusedAuthorities",
        "triage",
        "authorityRollup",
        "coverage",
        "limitations",
        "notes",
    }
    missing = sorted(required - set(report))
    errors.extend(f"$: missing required property {name!r}" for name in missing)
    if report.get("schemaVersion") != REPORT_VERSION:
        errors.append("$.schemaVersion: unsupported report schemaVersion")
    if report.get("status") not in {"complete", "incomplete"}:
        errors.append("$.status: invalid report status")
    if not isinstance(report.get("unitResults"), list):
        errors.append("$.unitResults: expected an array")
    if not isinstance(report.get("coverage"), dict):
        errors.append("$.coverage: expected an object")
    elif coverage_errors := _contract_errors(
        report["coverage"], "coverage.schema.json", path="coverage"
    ):
        errors.extend(coverage_errors[:4])
    return errors


def _unit_result_sort_key(
    result: Mapping[str, Any], ordinals: Mapping[str, int]
) -> tuple[int, int, str]:
    unit_id = str(result.get("unitId", ""))
    rank = SEVERITY_RANK.get(str(result.get("severity")), len(SEVERITY_RANK))
    return rank, ordinals.get(unit_id, 2**31 - 1), unit_id


def _sense_check(
    manifest: Mapping[str, Any],
    report: Mapping[str, Any],
    *,
    source_root: Path | None,
) -> dict[str, Any]:
    """Run one deterministic, bounded post-render consistency pass.

    This is deliberately a report check, not a second citation selector.  It
    records anomalies for a caller that can perform one targeted retry through
    the runner.  The report itself remains deliverable when an anomaly cannot
    be repaired, and the check never iterates until the data changes.
    """

    issues: list[dict[str, Any]] = []
    expected_ids = [unit["unitId"] for unit in manifest["units"]]
    states = report.get("coverage", {}).get("unitStates", [])
    observed_ids = [item.get("unitId") for item in states if isinstance(item, Mapping)]
    if observed_ids != expected_ids:
        issues.append(
            _limitation(
                "sense_check_appendix_mismatch",
                (
                    "The coverage appendix does not account for the prepared "
                    "units in source order."
                ),
            )
        )

    result_by_id = {
        item.get("unitId"): item
        for item in report.get("unitResults", [])
        if isinstance(item, Mapping) and isinstance(item.get("unitId"), str)
    }
    for unit in manifest["units"]:
        unit_id = unit["unitId"]
        result = result_by_id.get(unit_id)
        if result is not None and result.get("disposition") != "no_citations_found":
            continue
        if source_root is None:
            continue
        text, error = _read_unit_text(source_root, unit)
        if error is not None or text is None:
            continue
        # This is only a conservative anomaly signal for the final check.  It
        # does not select review work or decide whether a unit has a citation.
        citation_dense = re.search(
            r"(?:"
            r"\b\d+\s+(?:U\.S\.|F\.[0-9]|S\. Ct\.|F\. Supp\.)"
            r"|\b\d+\s+U\.S\.C\.\s*§+"
            r"|\b(?:Fed\.\s*R\.|[A-Z][A-Za-z]+\s+R\.)\s*(?:Civ\.\s*P\.|App\.\s*P\.|Evid\.|Crim\.\s*P\.)"
            r"|\b(?:Cal\.|N\.Y\.|Mass\.|Tex\.|Ill\.|Pa\.|Wash\.)\s*(?:App\.|[23]d|[0-9]+)"
            r"|\b\d+\s+(?:A\.D\.|N\.Y\.S\.|S\.E\.|S\.W\.|N\.E\.|So\.|P\.)[23]d\s+\d+\b"
            r"|\b(?:Aplt\.\s+)?Appx\.\s*(?:at\s+)?\d+\b"
            r"|\b(?:R\.|Tr\.|App\.|Hr'g|Dep\.)\s*\d+"
            r"|https?://\S+"
            r"|\bId\.|\bsupra\b"
            r")",
            text,
        )
        if citation_dense is not None:
            issues.append(
                _limitation(
                    "sense_check_citation_gap",
                    "A citation-shaped passage has no citation rows in the report.",
                    unit_id=unit_id,
                )
            )

    # A unit may contain distinct proposition rows for the same written cite,
    # so only compare rows with the same proposition.  Contradictory worker
    # labels are a report anomaly, not a reason to discard either citation.
    for result in report.get("unitResults", []):
        if not isinstance(result, Mapping):
            continue
        rows_by_key: dict[tuple[str, str | None], list[Mapping[str, Any]]] = {}
        for row in result.get("citations", []):
            if not isinstance(row, Mapping):
                continue
            written = row.get("citation_as_written_in_unit")
            if not isinstance(written, str):
                continue
            proposition = row.get("proposition")
            rows_by_key.setdefault((written, proposition), []).append(row)
        for (written, proposition), rows in rows_by_key.items():
            if len(rows) < 2:
                continue
            checks = (
                (
                    "accuracy_of_source_characterization",
                    "confirmed_fair_characterization_of_source",
                    "objectively_false_or_unreasonable_characterization_of_source",
                    "source_characterization",
                ),
                (
                    "pincite_accuracy",
                    "pincite_confirmed_accurate",
                    "pincite_inaccurate",
                    "pincite",
                ),
                (
                    "accuracy_of_direct_quotation",
                    "quotation_confirmed_accurate_and_fair",
                    "quotation_objectively_inaccurate",
                    "quotation",
                ),
            )
            for field, positive, negative, label in checks:
                values = {row.get(field) for row in rows}
                if positive in values and negative in values:
                    issue = _limitation(
                        "sense_check_face_contradiction",
                        (
                            f"Rows for the same written citation and proposition "
                            f"have contradictory {label} labels: {positive} and "
                            f"{negative}."
                        ),
                        unit_id=str(result["unitId"]),
                    )
                    issue["citation"] = written
                    if proposition is not None:
                        issue["proposition"] = proposition
                    issues.append(issue)
    return {
        "performed": True,
        "passCount": 1,
        "maxRetryRoundCount": 1,
        "maxTargetedRepairCount": 1,
        "retryRoundCount": 0,
        "targetedRepairCount": 0,
        "issues": issues,
        "unresolvedIssueCount": len(issues),
    }


def build_report(
    manifest: Mapping[str, Any],
    unit_results: Sequence[Any],
    *,
    execution: Mapping[str, Any] | None = None,
    target_context: Mapping[str, Any] | None = None,
    generated_at: str | None = None,
    source_root: Path | None = None,
) -> dict[str, Any]:
    """Build a v2 report from the complete prepared-unit inventory."""
    checked = _validate_manifest(manifest)
    run_id = checked["_runId"]
    units = checked["_unitById"]
    unit_ids = checked["_unitIds"]
    authority_ids = checked["_authorityIds"]

    valid_results: dict[str, dict[str, Any]] = {}
    duplicate_ids: set[str] = set()
    failed: dict[str, str] = {}
    limitations: list[dict[str, Any]] = []
    for _index, raw in enumerate(unit_results):
        raw_unit_id = raw.get("unitId") if isinstance(raw, dict) else None
        if not isinstance(raw_unit_id, str) or raw_unit_id not in units:
            limitations.append(
                _limitation(
                    "out_of_scope_result",
                    "A result was supplied for a unit outside the prepared inventory.",
                )
            )
            continue
        unit_id = raw_unit_id
        if unit_id in valid_results:
            duplicate_ids.add(unit_id)
            limitations.append(
                _limitation(
                    "duplicate_result",
                    "More than one terminal result was supplied for this unit; "
                    "the first normalized result is retained and coverage remains "
                    "incomplete.",
                    unit_id=unit_id,
                )
            )
            continue
        normalized, diagnostics, error = _validate_result_shape(
            raw,
            expected_unit_id=unit_id,
            authority_ids=authority_ids,
        )
        if error is not None or normalized is None:
            failed[unit_id] = error or "result could not be normalized"
            limitations.append(_limitation("failed", failed[unit_id], unit_id=unit_id))
            continue
        valid_results[unit_id] = normalized
        for diagnostic in diagnostics:
            code = diagnostic.get("code")
            message = diagnostic.get("message")
            if isinstance(code, str) and isinstance(message, str):
                limitations.append(
                    _limitation(
                        code,
                        message,
                        unit_id=unit_id,
                        citation_index=diagnostic.get("citationIndex")
                        if isinstance(diagnostic.get("citationIndex"), int)
                        else None,
                    )
                )

    unit_states: list[dict[str, str]] = []
    unit_texts: dict[str, str] = {}
    for unit_id in unit_ids:
        unit = units[unit_id]
        unit_text, read_error = _read_unit_text(source_root, unit)
        if unit_text is not None:
            unit_texts[unit_id] = unit_text
        if read_error is not None:
            limitations.append(
                _limitation("source_unavailable", read_error, unit_id=unit_id)
            )
        result = valid_results.get(unit_id)
        state = (
            "failed"
            if unit_id in failed or unit_id in duplicate_ids
            else "still_missing"
            if result is None
            else result["disposition"]
        )
        if state == "citations_found":
            state = "complete"
        unit_states.append({"unitId": unit_id, "state": state})

    coverage_complete = all(
        item["state"] in {"no_citations_found", "complete"} for item in unit_states
    )
    coverage = {
        "schemaVersion": COVERAGE_VERSION,
        "runId": run_id,
        "phase": "final",
        "unitStates": unit_states,
        "retriedUnitIds": [],
        "status": "complete" if coverage_complete else "incomplete",
        "isComplete": coverage_complete,
    }

    context = dict(target_context or {})
    target = {
        "path": checked["target"]["path"],
        "displayName": checked["target"].get("displayName"),
        **{
            key: context.get(key)
            for key in (
                "intendedUse",
                "tribunal",
                "jurisdiction",
                "proceduralPosture",
                "asOfDate",
            )
        },
    }
    for key, value in target.items():
        if value is not None and not isinstance(value, str):
            raise ReportInputError(f"report target {key} must be a string or null")

    authority_sources = [
        {
            "sourceId": authority["sourceId"],
            "path": authority["path"],
            "identityLabel": _source_label(authority),
            "readability": authority["readability"],
        }
        for authority in checked["authorities"]
    ]
    execution_data = {
        # A report can be assembled by a host-native worker or by a caller
        # that does not have execution metadata.  Do not infer a provider from
        # the packaged Codex runner: callers must supply observed execution
        # metadata when they want Codex-specific attribution.
        "provider": "unknown",
        "surface": "unknown",
        "model": "unknown",
        "reasoningEffort": "unknown",
    }
    if execution is not None:
        supplied_execution = dict(execution)
        for key in EXECUTION_FIELDS:
            value = supplied_execution.get(key)
            if value is None:
                continue
            if not isinstance(value, str):
                raise ReportInputError(f"report execution.{key} must be a string")
            if len(value) > MAX_EXECUTION_VALUE_LENGTH:
                raise ReportInputError(
                    f"report execution.{key} exceeds the bounded length"
                )
            if any(character in value for character in "\r\n"):
                raise ReportInputError(
                    f"report execution.{key} must not contain line breaks"
                )
            execution_data[key] = value
    for key in EXECUTION_FIELDS:
        if not isinstance(execution_data.get(key), str):
            raise ReportInputError(f"report execution.{key} must be a string")

    notes: list[str] = []
    if not coverage_complete:
        notes.append("Coverage is incomplete; unresolved units remain in the appendix.")
    if duplicate_ids:
        notes.append(
            "Duplicate unit results were not merged or used to invent citation rows."
        )

    results_sorted: list[dict[str, Any]] = []
    for result in valid_results.values():
        copied = _copy_json(result)
        unit_text = unit_texts.get(copied["unitId"])
        if unit_text is not None:
            copied["unitText"] = unit_text
        results_sorted.append(copied)
    unused_authorities = annotate_severity(results_sorted, checked["authorities"])
    triage = build_triage(results_sorted)
    rollup = authority_rollup(
        results_sorted, checked["authorities"], unused_authorities
    )
    ordinals = {unit_id: index for index, unit_id in enumerate(unit_ids)}
    results_sorted.sort(key=lambda item: _unit_result_sort_key(item, ordinals))

    report: dict[str, Any] = {
        "schemaVersion": REPORT_VERSION,
        "runId": run_id,
        "status": "complete" if coverage_complete else "incomplete",
        "target": target,
        "authoritySources": authority_sources,
        "execution": execution_data,
        "unitResults": results_sorted,
        "unusedAuthorities": unused_authorities,
        "triage": triage,
        "authorityRollup": rollup,
        "coverage": coverage,
        "limitations": _dedupe_objects(limitations),
        "generatedAt": generated_at,
        "notes": sorted(set(notes)),
    }
    sense_check = _sense_check(manifest, report, source_root=source_root)
    report["senseCheck"] = sense_check
    report["limitations"] = _dedupe_objects(
        [*report["limitations"], *sense_check["issues"]]
    )
    errors = _report_contract_errors(report)
    if errors:
        raise ReportInputError("report contract invalid: " + "; ".join(errors[:4]))
    return cast(dict[str, Any], _copy_json(report))


def repair_report_once(
    report: dict[str, Any],
    manifest: Mapping[str, Any],
    repair: Callable[[tuple[str, ...]], Mapping[str, Any] | None],
    *,
    source_root: Path | None = None,
) -> dict[str, Any]:
    """Apply at most one sense-check retry and one targeted receipt repair.

    ``repair`` is a host-provided step-3 operation.  It receives only the
    affected unit IDs and may return replacement raw unit results keyed by ID.
    The callback is invoked at most once, and the post-repair check is one
    fixed second pass; this function never loops over the report.
    """

    sense = report.get("senseCheck")
    if not isinstance(sense, dict) or not sense.get("issues"):
        return report
    if sense.get("retryRoundCount", 0) >= sense.get("maxRetryRoundCount", 1):
        return report

    issue_unit_ids = tuple(
        sorted(
            {
                item["unitId"]
                for item in sense["issues"]
                if isinstance(item, Mapping) and isinstance(item.get("unitId"), str)
            }
        )
    )
    sense["retryRoundCount"] = 1
    original_issues = list(sense["issues"])
    try:
        replacements = repair(issue_unit_ids)
    except Exception as exc:  # pragma: no cover - host callback boundary
        replacements = None
        sense["issues"] = [
            *original_issues,
            _limitation(
                "sense_check_repair_failed",
                "The bounded sense-check repair could not run: "
                f"{exc.__class__.__name__}.",
            ),
        ]
    if not isinstance(replacements, Mapping):
        sense["unresolvedIssueCount"] = len(sense["issues"])
        report["limitations"] = _dedupe_objects(
            [
                item
                for item in report.get("limitations", [])
                if item not in original_issues
            ]
            + list(sense["issues"])
        )
        return report

    checked = _validate_manifest(manifest)
    authority_ids = checked["_authorityIds"]
    unit_ids = set(checked["_unitIds"])
    current = {
        item["unitId"]: item
        for item in report.get("unitResults", [])
        if isinstance(item, Mapping) and isinstance(item.get("unitId"), str)
    }
    repaired = False
    for unit_id, raw in replacements.items():
        if not isinstance(unit_id, str) or unit_id not in unit_ids:
            continue
        normalized, _diagnostics, error = _validate_result_shape(
            raw,
            expected_unit_id=unit_id,
            authority_ids=authority_ids,
        )
        if error is not None or normalized is None:
            continue
        if source_root is not None:
            unit_text, _read_error = _read_unit_text(
                source_root, checked["_unitById"][unit_id]
            )
            if unit_text is not None:
                normalized["unitText"] = unit_text
        current[unit_id] = normalized
        repaired = True

    if repaired:
        sense["targetedRepairCount"] = 1
        repaired_results = list(current.values())
        unused = annotate_severity(repaired_results, checked["authorities"])
        report["unusedAuthorities"] = unused
        report["triage"] = build_triage(repaired_results)
        report["authorityRollup"] = authority_rollup(
            repaired_results, checked["authorities"], unused
        )
        ordinals = {unit_id: index for index, unit_id in enumerate(checked["_unitIds"])}
        report["unitResults"] = sorted(
            repaired_results, key=lambda item: _unit_result_sort_key(item, ordinals)
        )
        states = []
        for unit_id in checked["_unitIds"]:
            result = current.get(unit_id)
            state = (
                "still_missing"
                if result is None
                else "complete"
                if result.get("disposition") == "citations_found"
                else "no_citations_found"
            )
            states.append({"unitId": unit_id, "state": state})
        report["coverage"]["unitStates"] = states
        report["coverage"]["status"] = (
            "complete"
            if all(
                item["state"] in {"complete", "no_citations_found"} for item in states
            )
            else "incomplete"
        )
        report["coverage"]["isComplete"] = report["coverage"]["status"] == "complete"
        report["status"] = report["coverage"]["status"]

    checked_report = _sense_check(manifest, report, source_root=source_root)
    sense["issues"] = checked_report["issues"]
    sense["unresolvedIssueCount"] = len(sense["issues"])
    report["limitations"] = _dedupe_objects(
        [item for item in report.get("limitations", []) if item not in original_issues]
        + list(sense["issues"])
    )
    errors = _report_contract_errors(report)
    if errors:
        raise ReportInputError(
            "report contract invalid after repair: " + "; ".join(errors[:4])
        )
    return report
