"""Advisory unit validation and retry receipts for cite-check orchestration.

This module is the small seam between a host runtime and the provider-neutral
contracts. It deliberately does not perform citation matching, compare worker
rows with a parent inventory, or reinterpret parent-owned assignment metadata.
Those are outside the citation-level contract.
"""

from __future__ import annotations

import re
from copy import deepcopy
from typing import Any

from common.contracts import (
    HARD_ERROR_CODES,
    PACKAGE_DIR,
    _load_json,
    validate_schema,
    validate_unit_result,
)

_SOURCE_RESOLUTION_VALUES = frozenset(
    {
        "matched_supplied_source",
        "not_supplied_confirmed_exists_elsewhere",
        "not_supplied_not_found_potential_hallucination",
        "not_supplied_search_unavailable",
    }
)
_FABRICATION_INDICATOR_VALUES = frozenset(
    {
        "reporter_coordinates_belong_to_different_supplied_case",
        "not_found_in_external_search",
        "citation_malformed_or_impossible",
    }
)


def _add_validation_flag(citation: dict[str, Any], flag: str) -> None:
    flags = citation.get("validation_flags")
    if not isinstance(flags, list):
        flags = []
        citation["validation_flags"] = flags
    if flag not in flags:
        flags.append(flag)


def _annotate_allowed_evidence_defects(validation: dict[str, Any]) -> None:
    """Mark only allowed evidence-link defects for the one targeted retry."""

    normalized = validation.get("normalized")
    if not isinstance(normalized, dict):
        return
    citations = normalized.get("citations")
    if not isinstance(citations, list):
        return
    for citation in citations:
        if not isinstance(citation, dict):
            continue

        source_id = citation.get("matched_source_id")
        if "matched_source_id" not in citation or (
            source_id is not None and (not isinstance(source_id, str) or not source_id)
        ):
            _add_validation_flag(citation, "malformed_source_id")

        resolution = citation.get("source_resolution")
        if (
            "source_resolution" not in citation
            or not isinstance(resolution, str)
            or resolution not in _SOURCE_RESOLUTION_VALUES
        ):
            _add_validation_flag(citation, "malformed_citation")

        indicators = citation.get("fabrication_indicators")
        invalid_indicators = "fabrication_indicators" not in citation or not isinstance(
            indicators, list
        )
        if not invalid_indicators:
            invalid_indicators = any(
                not isinstance(item, str) or item not in _FABRICATION_INDICATOR_VALUES
                for item in indicators
            )
        if not invalid_indicators:
            invalid_indicators = len(indicators) != len(set(indicators))
        if invalid_indicators:
            _add_validation_flag(citation, "malformed_citation")

        for field in ("colliding_source_id", "existence_check_notes"):
            if (
                field in citation
                and citation[field] is not None
                and not isinstance(citation[field], str)
            ):
                _add_validation_flag(citation, "malformed_citation")


def _worker_schema_view(value: dict[str, Any]) -> dict[str, Any]:
    """Remove validator-owned fields before checking the worker contract."""

    candidate = deepcopy(value)
    candidate.pop("validation", None)
    citations = candidate.get("citations")
    if isinstance(citations, list):
        for citation in citations:
            if isinstance(citation, dict):
                citation.pop("validation_flags", None)
    return candidate


def validate_attempt(
    value: Any,
    expected_unit_id: str,
    *,
    authority_ids: set[str] | None = None,
) -> dict[str, Any]:
    """Validate one worker attempt as advisory diagnostics plus normalization."""

    validation = validate_unit_result(
        value,
        expected_unit_id,
        authority_ids=authority_ids,
    )
    _annotate_allowed_evidence_defects(validation)
    return validation


def should_retry(validation: dict[str, Any], attempts_remaining: int) -> bool:
    """Retry only report-blocking defects, and only within the caller's budget."""

    hard_errors = validation.get("hard_errors", [])
    return (
        attempts_remaining > 0
        and isinstance(hard_errors, list)
        and any(
            isinstance(item, dict) and item.get("code") in HARD_ERROR_CODES
            for item in hard_errors
        )
    )


def attempt_receipt(
    attempt_number: int,
    raw_value: Any,
    validation: dict[str, Any],
    *,
    elapsed_ms: int | None = None,
    runtime_failure: dict[str, Any] | None = None,
    requested_model: str = "unknown",
    requested_effort: str = "unknown",
    observed_model: str = "unknown",
    observed_effort: str = "unknown",
) -> dict[str, Any]:
    """Build an audit receipt retaining the raw attempt and normalized outcome."""

    hard_errors = validation.get("hard_errors", [])
    receipt: dict[str, Any] = {
        "attempt": attempt_number,
        "status": (
            "failed"
            if runtime_failure is not None
            else "accepted"
            if not hard_errors
            else "rejected"
        ),
        "rawResult": deepcopy(raw_value),
        "warnings": deepcopy(validation.get("warnings", [])),
        "potentialIssues": deepcopy(validation.get("potential_issues", [])),
        "hardErrors": deepcopy(hard_errors),
        "requestedModel": requested_model,
        "requestedReasoningEffort": requested_effort,
        "observedModel": observed_model,
        "observedReasoningEffort": observed_effort,
    }
    normalized = validation.get("normalized")
    if normalized is not None:
        receipt["normalizedResult"] = deepcopy(normalized)
    if runtime_failure is not None:
        receipt["runtimeFailure"] = deepcopy(runtime_failure)
    if isinstance(elapsed_ms, int) and not isinstance(elapsed_ms, bool):
        receipt["elapsedMs"] = max(0, elapsed_ms)
    return receipt


def normalized_report_result(validation: dict[str, Any]) -> dict[str, Any] | None:
    """Return the normalized result, retaining the advisory layer separately."""

    value = validation.get("normalized")
    return value if isinstance(value, dict) else None


def strict_normalized_report_result(
    validation: dict[str, Any],
) -> dict[str, Any] | None:
    """Return a normalized result only when it passes the worker schema.

    Advisory validation deliberately preserves citation-level warnings, but a
    resume receipt is terminal only when its underlying worker result is also
    structurally valid.  Keeping that check here makes fresh results and
    same-run resume use the same acceptance boundary.
    """

    normalized = normalized_report_result(validation)
    if normalized is None or validation.get("hard_errors"):
        return None
    if terminal_schema_errors(validation):
        return None
    return normalized


def strict_schema_errors(validation: dict[str, Any]) -> list[str]:
    """Return structural worker-schema errors for an advisory validation."""

    normalized = normalized_report_result(validation)
    if normalized is None or validation.get("hard_errors"):
        return []
    schema = _load_json(
        PACKAGE_DIR / "schemas" / "cite-check-unit-result.schema.json",
        "unit result schema",
    )
    if not isinstance(schema, dict):
        return ["unit result schema is not an object"]
    return validate_schema(_worker_schema_view(normalized), schema)


_ROW_EVIDENCE_ERROR = re.compile(
    r"^\$?\.citations\[\d+\]\.(?:matched_source_id|source_resolution|"
    r"fabrication_indicators(?:\[\d+\])?|colliding_source_id|"
    r"existence_check_notes)$"
)
_MISSING_ROW_EVIDENCE_ERROR = re.compile(
    r"^\$?\.citations\[\d+\]: missing required property "
    r"'(?:matched_source_id|source_resolution|fabrication_indicators)'$"
)


def _is_row_evidence_error(error: str) -> bool:
    path = error.split(":", 1)[0]
    return bool(
        _ROW_EVIDENCE_ERROR.match(path) or _MISSING_ROW_EVIDENCE_ERROR.match(error)
    )


def terminal_schema_errors(validation: dict[str, Any]) -> list[str]:
    """Return schema errors that make a whole unit unreportable.

    The worker schema is intentionally strict, but malformed evidence values
    belong to a citation row. The validator preserves those raw values, marks
    the row amber, and may request one mechanical repair. They must not make
    the entire prepared unit disappear from the report. Wrapper errors,
    unknown properties, and malformed legal-judgment fields remain terminal.
    """

    return [
        error
        for error in strict_schema_errors(validation)
        if not _is_row_evidence_error(error)
    ]
