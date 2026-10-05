"""Contracts, validation, and safe file helpers for the cite-check runner."""

from __future__ import annotations

import json
import os
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any

PACKAGE_DIR = Path(__file__).resolve().parents[2]
SCHEMA_DIR = PACKAGE_DIR / "schemas"


class RunnerError(Exception):
    """A user-actionable runner error whose message contains no document text."""


class ManifestError(RunnerError):
    """The input manifest is invalid or unsafe."""


class RuntimeUnavailable(RunnerError):
    """A requested local runtime cannot be used in this environment."""


# These are deliberately the only validator findings that make a unit
# unreportable.  A source-quality problem belongs to one citation row and is
# represented in the normalized layer instead of turning the whole unit into a
# failed worker receipt.
HARD_ERROR_CODES = frozenset({"not_json", "wrong_unit_id", "nothing_salvageable"})


def _issue(
    code: str,
    message: str,
    *,
    unit_id: str | None = None,
    citation_index: int | None = None,
    repairable: bool = True,
) -> dict[str, Any]:
    value: dict[str, Any] = {
        "code": code,
        "message": message,
        "repairable": repairable,
    }
    if unit_id is not None:
        value["unitId"] = unit_id
    if citation_index is not None:
        value["citationIndex"] = citation_index
    return value


def _parse_worker_output(value: Any) -> tuple[Any, dict[str, Any] | None]:
    """Decode a runtime payload without guessing at non-JSON worker prose."""

    if isinstance(value, (dict, list)):
        return value, None
    if isinstance(value, str):
        try:
            return json.loads(value), None
        except json.JSONDecodeError:
            return None, _issue(
                "not_json",
                "The worker response is not JSON; repair or retry this unit.",
            )
    return None, _issue(
        "nothing_salvageable",
        "The worker response has no salvageable JSON result; retry this unit.",
    )


def _is_source_not_found(value: Any) -> bool:
    return isinstance(value, str) and value.startswith("source_not_found_")


def _citation_flags(
    citation: Any,
    index: int,
    *,
    unit_id: str,
    authority_ids: set[str],
) -> tuple[list[str], list[dict[str, Any]], list[dict[str, Any]]]:
    """Return validator-owned flags without changing worker-authored values."""

    flags: list[str] = []
    warnings: list[dict[str, Any]] = []
    potential_issues: list[dict[str, Any]] = []
    if not isinstance(citation, dict):
        return (
            ["malformed_citation"],
            [],
            [
                _issue(
                    "malformed_citation",
                    "This citation row is not an object; repair the row if possible.",
                    unit_id=unit_id,
                    citation_index=index,
                )
            ],
        )

    required = ("citation_as_written_in_unit", "matched_citation")
    if any(
        not isinstance(citation.get(name), str) or not citation[name]
        for name in required
    ):
        flags.append("malformed_citation")
        potential_issues.append(
            _issue(
                "malformed_citation",
                (
                    "This citation row is missing its written or matched citation; "
                    "repair it if possible."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )

    source_id = citation.get("matched_source_id")
    if "matched_source_id" not in citation:
        flags.append("malformed_source_id")
        potential_issues.append(
            _issue(
                "malformed_source_id",
                (
                    "The matched source identifier is missing; use a supplied "
                    "source ID or null."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )
    source_id_present = isinstance(source_id, str) and bool(source_id)
    resolution = citation.get("source_resolution")
    if "source_resolution" not in citation:
        flags.append("malformed_citation")
        warnings.append(
            _issue(
                "malformed_citation",
                "The source-resolution outcome is missing; repair the evidence fields.",
                unit_id=unit_id,
                citation_index=index,
            )
        )
    if resolution is not None and source_id_present != (
        resolution == "matched_supplied_source"
    ):
        flags.append("source_resolution_inconsistent")
        warnings.append(
            _issue(
                "source_resolution_inconsistent",
                (
                    "matched_source_id must be non-null exactly when "
                    "source_resolution is matched_supplied_source; consider "
                    "repairing the source receipt."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )
    indicators = citation.get("fabrication_indicators")
    if "fabrication_indicators" not in citation:
        flags.append("malformed_citation")
        warnings.append(
            _issue(
                "malformed_citation",
                (
                    "The fabrication-indicator list is missing; repair the "
                    "evidence fields."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )
    if (
        isinstance(indicators, list)
        and "not_found_in_external_search" in indicators
        and resolution != "not_supplied_not_found_potential_hallucination"
    ):
        flags.append("source_resolution_indicator_inconsistent")
        potential_issues.append(
            _issue(
                "source_resolution_indicator_inconsistent",
                (
                    "The external-search indicator conflicts with the declared "
                    "source resolution; repair the search outcome fields."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )
    if source_id is not None and (not isinstance(source_id, str) or not source_id):
        flags.append("malformed_source_id")
        potential_issues.append(
            _issue(
                "malformed_source_id",
                "The matched source identifier is not usable; repair it if possible.",
                unit_id=unit_id,
                citation_index=index,
            )
        )
    source_in_universe = isinstance(source_id, str) and source_id in authority_ids
    if isinstance(source_id, str) and source_id not in authority_ids:
        flags.append("source_not_in_authority_universe")
        flags.append("source_not_found")
        warnings.append(
            _issue(
                "source_not_in_authority_universe",
                (
                    "The worker named a source outside the supplied authority "
                    "universe; consider repairing the source match."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )

    characterization = citation.get("accuracy_of_source_characterization")
    pincite = citation.get("pincite_accuracy")
    quotation = citation.get("accuracy_of_direct_quotation")
    source_claimed_found = (
        source_in_universe
        and not _is_source_not_found(characterization)
        and not _is_source_not_found(pincite)
        and not _is_source_not_found(quotation)
    )
    if source_claimed_found:
        if (
            not isinstance(citation.get("source_excerpt"), str)
            or not citation["source_excerpt"].strip()
        ):
            flags.append("missing_excerpt")
            warnings.append(
                _issue(
                    "missing_excerpt",
                    (
                        "The source was reported as found but no excerpt was "
                        "supplied; consider repairing the receipt before relying "
                        "on it."
                    ),
                    unit_id=unit_id,
                    citation_index=index,
                )
            )
        if (
            not isinstance(citation.get("source_locator"), str)
            or not citation["source_locator"].strip()
        ):
            flags.append("missing_locator")
            warnings.append(
                _issue(
                    "missing_locator",
                    (
                        "The source was reported as found but no stable locator "
                        "was supplied; consider repairing the receipt before "
                        "relying on it."
                    ),
                    unit_id=unit_id,
                    citation_index=index,
                )
            )
    elif (
        source_id is None
        or not authority_ids
        or _is_source_not_found(characterization)
        or _is_source_not_found(pincite)
        or _is_source_not_found(quotation)
    ):
        flags.append("source_not_found")
        warnings.append(
            _issue(
                "source_not_found",
                (
                    "The source could not be verified from the supplied authority "
                    "universe; consider repairing the source receipt or leave it "
                    "claimed but unverified."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )

    if pincite == "pincite_inaccurate":
        flags.append("pincite_inaccurate")
        potential_issues.append(
            _issue(
                "pincite_inaccurate",
                (
                    "The worker marked the pinpoint inaccurate; consider repairing "
                    "the citation or confirm the warning with the source."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )
    if characterization in {
        "potentially_unfair_or_unreasonable_characterization_of_source",
        "objectively_false_or_unreasonable_characterization_of_source",
    }:
        flags.append("characterization_issue")
        potential_issues.append(
            _issue(
                "characterization_issue",
                (
                    "The worker identified a potentially unfair or objectively "
                    "unreasonable source characterization; consider repairing or "
                    "escalating this citation."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )
    if quotation in {
        "quotation_technically_accurate_but_misleading_or_unfair",
        "quotation_objectively_inaccurate",
    }:
        flags.append("quotation_issue")
        potential_issues.append(
            _issue(
                "quotation_issue",
                (
                    "The worker identified a quotation accuracy or fairness "
                    "problem; consider repairing or escalating this citation."
                ),
                unit_id=unit_id,
                citation_index=index,
            )
        )
    return list(dict.fromkeys(flags)), warnings, potential_issues


def normalize_unit_result(
    value: Any,
    expected_unit_id: str,
    *,
    authority_ids: set[str] | None = None,
) -> dict[str, Any] | None:
    """Build the report-facing copy while preserving every worker field.

    The returned object preserves the worker result at the top level while
    citation rows carry only validator-owned ``validation_flags`` in addition
    to the worker's original fields.  No worker value is corrected or silently
    replaced; raw attempts are retained by the orchestration receipt layer.
    """

    candidate, parse_error = _parse_worker_output(value)
    if parse_error is not None or not isinstance(candidate, dict):
        return None
    if candidate.get("unitId") != expected_unit_id:
        return None
    raw_citations = candidate.get("citations")
    if raw_citations is None and candidate.get("disposition") == "no_citations_found":
        raw_citations = []
    if not isinstance(raw_citations, list):
        return None
    citations: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    potential_issues: list[dict[str, Any]] = []
    authority_ids = authority_ids or set()
    for index, citation in enumerate(raw_citations):
        if isinstance(citation, dict):
            row = deepcopy(citation)
        else:
            row = {"worker_value": deepcopy(citation)}
        flags, row_warnings, row_issues = _citation_flags(
            citation,
            index,
            unit_id=expected_unit_id,
            authority_ids=authority_ids,
        )
        row["validation_flags"] = flags
        citations.append(row)
        warnings.extend(row_warnings)
        potential_issues.extend(row_issues)
    disposition = candidate.get("disposition")
    if disposition not in {"no_citations_found", "citations_found"}:
        disposition = "citations_found" if citations else "no_citations_found"
        warnings.append(
            _issue(
                "wrapper_repair_disposition",
                (
                    "The worker disposition was not usable; the normalized "
                    "wrapper derived it from the citation rows and recorded the "
                    "repair."
                ),
                unit_id=expected_unit_id,
            )
        )
    if disposition == "no_citations_found" and citations:
        disposition = "citations_found"
        warnings.append(
            _issue(
                "wrapper_repair_disposition",
                (
                    "The worker reported no citations while returning citation "
                    "rows; the normalized wrapper retained the rows and recorded "
                    "the repair."
                ),
                unit_id=expected_unit_id,
            )
        )
    if disposition == "citations_found" and not citations:
        warnings.append(
            _issue(
                "empty_citation_rows",
                (
                    "The worker reported citations but returned no rows; consider "
                    "a targeted receipt repair."
                ),
                unit_id=expected_unit_id,
            )
        )
    normalized = deepcopy(candidate)
    normalized["unitId"] = expected_unit_id
    normalized["disposition"] = disposition
    normalized["citations"] = citations
    normalized["validation"] = {
        "warnings": warnings,
        "potential_issues": potential_issues,
        "hard_errors": [],
    }
    return normalized


def validate_unit_result(
    value: Any,
    expected_unit_id: str,
    *,
    authority_ids: set[str] | None = None,
) -> dict[str, Any]:
    """Return advisory validation and the three report-blocking hard errors."""

    candidate, parse_error = _parse_worker_output(value)
    hard_errors: list[dict[str, Any]] = []
    if parse_error is not None:
        hard_errors.append(parse_error)
    elif not isinstance(candidate, dict):
        hard_errors.append(
            _issue(
                "nothing_salvageable",
                "The worker response has no salvageable unit result; retry this unit.",
            )
        )
    elif candidate.get("unitId") != expected_unit_id:
        hard_errors.append(
            _issue(
                "wrong_unit_id",
                (
                    "The worker returned a different unit ID; retry this unit "
                    "with the original assignment."
                ),
                unit_id=expected_unit_id,
            )
        )
    else:
        citations = candidate.get("citations")
        salvageable = isinstance(citations, list) and (
            bool(citations) or candidate.get("disposition") == "no_citations_found"
        )
        if not salvageable:
            hard_errors.append(
                _issue(
                    "nothing_salvageable",
                    (
                        "The worker object does not contain salvageable citation "
                        "rows or a citation-free disposition; retry this unit."
                    ),
                    unit_id=expected_unit_id,
                )
            )
    normalized = (
        normalize_unit_result(
            candidate,
            expected_unit_id,
            authority_ids=authority_ids,
        )
        if not hard_errors
        else None
    )
    validation = (
        normalized["validation"]
        if normalized is not None
        else {
            "warnings": [],
            "potential_issues": [],
            "hard_errors": hard_errors,
        }
    )
    validation["hard_errors"] = hard_errors
    return {
        "normalized": normalized,
        "warnings": list(validation["warnings"]),
        "potential_issues": list(validation["potential_issues"]),
        "hard_errors": hard_errors,
        "retryable": bool(hard_errors),
        "salvageable": normalized is not None,
    }


def _load_json(path: Path, label: str) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RunnerError(f"cannot read {label}: {exc.__class__.__name__}") from exc
    except json.JSONDecodeError as exc:
        raise RunnerError(f"invalid JSON in {label} at line {exc.lineno}") from exc


def _schema_error(path: str, message: str) -> str:
    return f"{path or '$'}: {message}"


def _resolve_schema_ref(schema: dict[str, Any], reference: str) -> dict[str, Any]:
    if reference.startswith("#/$defs/"):
        name = reference.removeprefix("#/$defs/")
        value = schema.get("$defs", {}).get(name)
        if isinstance(value, dict):
            return value
    raise ValueError(f"unsupported schema reference {reference}")


def _load_external_schema(reference: str) -> dict[str, Any]:
    """Load one sibling packaged schema referenced by a contract."""

    path = Path(reference)
    if (
        path.name != reference
        or path.suffix != ".json"
        or not reference.endswith(".schema.json")
    ):
        raise ValueError(f"unsupported schema reference {reference}")
    value = _load_json(SCHEMA_DIR / reference, reference)
    if not isinstance(value, dict):
        raise ValueError(f"schema reference {reference} is not an object")
    return value


def _json_unique(items: list[Any]) -> bool:
    try:
        keys = [
            json.dumps(item, sort_keys=True, separators=(",", ":")) for item in items
        ]
    except (TypeError, ValueError):
        return False
    return len(keys) == len(set(keys))


def validate_schema(
    instance: Any,
    schema: dict[str, Any],
    *,
    root: dict[str, Any] | None = None,
    path: str = "",
) -> list[str]:
    """Validate the strict JSON Schema subset used by packaged contracts."""

    root = schema if root is None else root
    if "$ref" in schema:
        reference = schema["$ref"]
        if not isinstance(reference, str):
            return [_schema_error(path, "schema reference must be a string")]
        if not reference.startswith("#/"):
            try:
                external = _load_external_schema(reference)
            except (RunnerError, ValueError) as exc:
                return [_schema_error(path, str(exc))]
            return validate_schema(instance, external, root=external, path=path)
        try:
            return validate_schema(
                instance,
                _resolve_schema_ref(root, reference),
                root=root,
                path=path,
            )
        except ValueError as exc:
            return [_schema_error(path, str(exc))]
    errors: list[str] = []
    if "const" in schema and instance != schema["const"]:
        errors.append(_schema_error(path, f"expected {schema['const']!r}"))
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(_schema_error(path, "value is not an allowed enum member"))
    if "type" in schema:
        expected = schema["type"]
        types = expected if isinstance(expected, list) else [expected]
        valid_type = any(
            (kind == "object" and isinstance(instance, dict))
            or (kind == "array" and isinstance(instance, list))
            or (kind == "string" and isinstance(instance, str))
            or (kind == "boolean" and isinstance(instance, bool))
            or (kind == "null" and instance is None)
            or (
                kind == "integer"
                and isinstance(instance, int)
                and not isinstance(instance, bool)
            )
            or (
                kind == "number"
                and isinstance(instance, (int, float))
                and not isinstance(instance, bool)
            )
            for kind in types
        )
        if not valid_type:
            errors.append(_schema_error(path, f"expected type {expected!r}"))
            return errors
    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            errors.append(_schema_error(path, "string is shorter than minLength"))
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errors.append(_schema_error(path, "string is longer than maxLength"))
        if "pattern" in schema:
            try:
                if re.search(schema["pattern"], instance) is None:
                    errors.append(_schema_error(path, "string does not match pattern"))
            except re.error:
                errors.append(_schema_error(path, "schema pattern is invalid"))
    if (
        isinstance(instance, (int, float))
        and not isinstance(instance, bool)
        and "minimum" in schema
        and instance < schema["minimum"]
    ):
        errors.append(_schema_error(path, "number is below minimum"))
    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(_schema_error(path, "array is shorter than minItems"))
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(_schema_error(path, "array is longer than maxItems"))
        if schema.get("uniqueItems") and not _json_unique(instance):
            errors.append(_schema_error(path, "array items must be unique"))
        if isinstance(schema.get("items"), dict):
            for index, item in enumerate(instance):
                errors.extend(
                    validate_schema(
                        item, schema["items"], root=root, path=f"{path}[{index}]"
                    )
                )
    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        for name in schema.get("required", []):
            if name not in instance:
                errors.append(
                    _schema_error(path, f"missing required property {name!r}")
                )
        if schema.get("additionalProperties") is False:
            unknown = sorted(set(instance) - set(properties))
            errors.extend(
                _schema_error(path, f"unknown property {name!r}") for name in unknown
            )
        for name, child_schema in properties.items():
            if name in instance:
                errors.extend(
                    validate_schema(
                        instance[name], child_schema, root=root, path=f"{path}.{name}"
                    )
                )
    if "anyOf" in schema:
        alternatives = [
            validate_schema(instance, option, root=root, path=path)
            for option in schema["anyOf"]
        ]
        if not any(not option_errors for option_errors in alternatives):
            errors.append(_schema_error(path, "does not satisfy anyOf"))
    if "allOf" in schema:
        for option in schema["allOf"]:
            errors.extend(validate_schema(instance, option, root=root, path=path))
    return errors


def _safe_relative(root: Path, value: Any, label: str) -> Path:
    if (
        not isinstance(value, str)
        or not value
        or Path(value).is_absolute()
        or Path(value).drive
    ):
        raise ManifestError(f"unsafe {label} path")
    candidate = (root / value).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ManifestError(f"unsafe {label} path") from exc
    return candidate


def _manifest_paths(manifest: dict[str, Any], root: Path) -> set[Path]:
    path_labels = [
        (manifest["target"]["path"], "target"),
        (manifest["target"]["fullDocumentRef"], "target document"),
    ]
    path_labels.extend(
        (authority["path"], "authority") for authority in manifest["authorities"]
    )
    path_labels.extend(
        (unit["path"], f"unit {unit['unitId']}") for unit in manifest["units"]
    )
    paths: set[Path] = set()
    for value, label in path_labels:
        candidate = _safe_relative(root, value, label)
        try:
            readable = candidate.is_file() and os.access(candidate, os.R_OK)
        except OSError:
            readable = False
        if not readable:
            raise ManifestError(f"{label} source file is missing or unreadable")
        paths.add(candidate)
    return paths


def _validate_manifest(manifest: Any, root: Path) -> dict[str, Any]:
    schema = _load_json(SCHEMA_DIR / "manifest.schema.json", "manifest schema")
    errors = validate_schema(manifest, schema)
    if errors:
        raise ManifestError("manifest schema invalid: " + "; ".join(errors[:4]))
    assert isinstance(manifest, dict)
    _manifest_paths(manifest, root)
    units = manifest["units"]
    authorities = manifest["authorities"]
    unit_ids = [unit["unitId"] for unit in units]
    if len(unit_ids) != len(set(unit_ids)):
        raise ManifestError("manifest contains duplicate unit IDs")
    if not unit_ids:
        raise ManifestError("manifest contains no prepared units")
    unit_id_set = set(unit_ids)
    for unit in units:
        if unit["lineStart"] > unit["lineEnd"]:
            raise ManifestError(f"unit {unit['unitId']} line range is reversed")
        anchor_id = unit.get("footnoteAnchorUnitId")
        if anchor_id is not None and anchor_id not in unit_id_set:
            raise ManifestError(f"unit {unit['unitId']} has an unknown footnote anchor")
    source_ids = [authority["sourceId"] for authority in authorities]
    if len(source_ids) != len(set(source_ids)):
        raise ManifestError("manifest contains duplicate authority IDs")
    return manifest


def _lexical_absolute(path: Path) -> Path:
    """Normalize a path without following any filesystem symlink."""

    return Path(os.path.abspath(os.fspath(path)))


def _ensure_output_parent(path: Path, output_root: Path) -> Path:
    """Create a receipt parent while rejecting symlinked directories."""

    lexical_path = _lexical_absolute(path)
    lexical_root = _lexical_absolute(output_root)
    try:
        relative_parent = lexical_path.parent.relative_to(lexical_root)
    except ValueError as exc:
        raise RunnerError(
            "output path must stay inside the approved output root"
        ) from exc

    current = lexical_root
    if current.is_symlink():
        raise RunnerError("output path contains a symlinked directory")
    for component in relative_parent.parts:
        current /= component
        if current.is_symlink():
            raise RunnerError("output path contains a symlinked directory")
        current.mkdir(exist_ok=True)
        if not current.is_dir():
            raise RunnerError("output path parent is not a directory")

    try:
        lexical_path.parent.resolve().relative_to(lexical_root.resolve())
    except ValueError as exc:
        raise RunnerError(
            "output path resolves outside the approved output root"
        ) from exc
    return lexical_path


def _write_json(
    path: Path,
    value: Any,
    source_paths: set[Path],
    *,
    output_root: Path | None = None,
) -> None:
    """Atomically write JSON without traversing nested output symlinks."""

    lexical_path = _lexical_absolute(path)
    root = output_root or lexical_path.parent
    path = _ensure_output_parent(lexical_path, root)
    if path in {_lexical_absolute(source) for source in source_paths}:
        raise RunnerError("output path overlaps a supplied source")
    temporary: Path | None = None
    try:
        descriptor, name = tempfile.mkstemp(
            prefix=f".{path.name}.tmp-", dir=str(path.parent)
        )
        temporary = Path(name)
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass
