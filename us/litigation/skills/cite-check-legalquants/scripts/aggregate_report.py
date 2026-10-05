#!/usr/bin/env python3
"""Compatibility CLI for deterministic cite-check report generation.

The report core owns contract validation and reconciliation, while the render
module owns the two deterministic projections.  This file intentionally keeps
the historical direct-import and command-line surface stable for native hosts.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from collections.abc import Sequence
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
if str(SCRIPT_PATH.parent) not in sys.path:
    sys.path.insert(0, str(SCRIPT_PATH.parent))

from common.contracts import (  # noqa: E402
    RunnerError,
    _ensure_output_parent,
    _lexical_absolute,
)
from common.contracts import _load_json as _contract_load_json  # noqa: E402
from common.report_core import (  # noqa: E402
    ReportInputError,
    _as_dict,
    _canonical_json,
    _report_contract_errors,
    build_report,
)
from common.report_render import (  # noqa: E402
    render_html,
    render_summary,
)

__all__ = [
    "ReportInputError",
    "build_report",
    "ingest_receipts",
    "load_worker_results",
    "main",
    "render_html",
    "render_summary",
    "write_artifacts",
]


# Receipt data is execution metadata, not evidence.  Keep its projection
# deliberately small so a malformed or over-helpful runtime receipt cannot
# smuggle source text, machine paths, or arbitrary JSON into the lawyer-facing
# report.  The limits also keep a failed large run from making the report
# itself unbounded.
RECEIPT_MAX_IDS = 4096
RECEIPT_MAX_UNITS = 4096
RECEIPT_MAX_ATTEMPTS_PER_UNIT = 32
RECEIPT_MAX_TEXT = 240
RECEIPT_ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]{0,127}$")
RECEIPT_STATUS_VALUES = {
    "accepted",
    "failed",
    "rejected",
    "cancelled",
    "missing",
    "unknown",
}
RECEIPT_PHASE_VALUES = {"initial", "final"}
RECEIPT_PREFLIGHT_STATUS_VALUES = {"passed", "failed", "not_run", "unavailable"}


def _relative_manifest_source(root: Path, value: Any, label: str) -> Path:
    """Resolve a manifest-declared input path so it can be protected on write.

    The aggregator never deletes anything; the run directory persists for
    audit.  This exists only so an artifact path cannot silently overwrite the
    prepared brief or a supplied authority file.
    """

    if not isinstance(value, str) or not value:
        raise ReportInputError(f"manifest {label} path is invalid")
    relative = Path(value)
    if relative.is_absolute() or relative.drive or ".." in relative.parts:
        raise ReportInputError(f"manifest {label} path is unsafe")
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ReportInputError(f"manifest {label} path is unsafe") from exc
    return candidate


def _load_json(path: Path) -> Any:
    """Load JSON while keeping error messages free of local path details."""

    try:
        return _contract_load_json(path, path.name)
    except RunnerError as exc:
        raise ReportInputError(str(exc)) from exc


def _receipt_text(value: Any) -> str | None:
    """Return a short runtime label without preserving local paths.

    Runtime receipts are allowed to carry human-readable diagnostics, but the
    report must not become a second client-document store.  Reject path-like
    values rather than trying to reconstruct a safe-looking version of them.
    """

    if not isinstance(value, str) or not value:
        return None
    compact = " ".join(value.split())
    if not compact or "/" in compact or "\\" in compact:
        return "local path or machine detail redacted"
    if len(compact) > RECEIPT_MAX_TEXT:
        compact = compact[: RECEIPT_MAX_TEXT - 1].rstrip() + "…"
    return compact


def _receipt_id(value: Any) -> str | None:
    if not isinstance(value, str) or RECEIPT_ID_RE.fullmatch(value) is None:
        return None
    return value


def _receipt_ids(value: Any, *, limit: int = RECEIPT_MAX_IDS) -> list[str]:
    if not isinstance(value, list):
        return []
    result = sorted(
        {
            identifier
            for identifier in (_receipt_id(item) for item in value)
            if identifier is not None
        }
    )
    return result[:limit]


def _receipt_object(value: Any, label: str) -> Any:
    """Load one optional receipt while keeping failures non-fatal.

    The caller records the returned diagnostic in the report.  Optional
    runtime telemetry should never make a valid worker result disappear.
    """

    if isinstance(value, Path):
        try:
            return _load_json(value)
        except (OSError, ReportInputError):
            return None
    if isinstance(value, (dict, list)):
        return _copy_receipt_json(value)
    return None


def _copy_receipt_json(value: Any) -> Any:
    """Copy only JSON-compatible receipt values; never retain caller objects."""

    try:
        return json.loads(json.dumps(value, ensure_ascii=False))
    except (TypeError, ValueError):
        return None


def _load_receipt_collection(value: Any) -> list[dict[str, Any]]:
    """Load bounded per-unit JSON receipts from a file, JSONL, or directory."""

    values: list[Any] = []
    if isinstance(value, Path):
        if not value.exists():
            return []
        if value.is_dir():
            for child in sorted(value.glob("*.json")):
                loaded = _receipt_object(child, child.name)
                if loaded is not None:
                    values.append(loaded)
        elif value.suffix.lower() == ".jsonl":
            try:
                lines = value.read_text(encoding="utf-8").splitlines()
            except OSError:
                return []
            for line in lines[:RECEIPT_MAX_UNITS]:
                if not line.strip():
                    continue
                try:
                    loaded = json.loads(line)
                except json.JSONDecodeError:
                    continue
                values.append(loaded)
        else:
            loaded = _receipt_object(value, value.name)
            if loaded is not None:
                values.append(loaded)
    else:
        loaded = _copy_receipt_json(value)
        if loaded is not None:
            values.append(loaded)

    flattened: list[dict[str, Any]] = []
    for raw in values[:RECEIPT_MAX_UNITS]:
        if isinstance(raw, dict):
            if isinstance(raw.get("results"), list):
                flattened.extend(
                    item for item in raw["results"] if isinstance(item, dict)
                )
            elif isinstance(raw.get("unitId"), str):
                flattened.append(raw)
            else:
                # A convenient mapping form {"P0001": {...}} is accepted for
                # native hosts that do not write one file per unit.
                for unit_id, item in raw.items():
                    if isinstance(item, dict):
                        copied = dict(item)
                        copied.setdefault("unitId", unit_id)
                        flattened.append(copied)
        elif isinstance(raw, list):
            flattened.extend(item for item in raw if isinstance(item, dict))
    return flattened[:RECEIPT_MAX_UNITS]


def _summarize_coverage_receipt(
    value: Any, *, run_id: str
) -> tuple[dict[str, Any] | None, str | None]:
    if isinstance(value, dict) and isinstance(value.get("coverage"), dict):
        value = value["coverage"]
    if not isinstance(value, dict):
        return None, "final coverage receipt was not an object"
    if value.get("runId") != run_id:
        return None, "final coverage receipt runId did not match the report"
    if value.get("schemaVersion") == "cite-check.coverage.v2":
        raw_states = value.get("unitStates")
        if not isinstance(raw_states, list):
            return None, "v2 coverage receipt unitStates was not an array"
        states: list[dict[str, str]] = []
        for item in raw_states[:RECEIPT_MAX_UNITS]:
            if not isinstance(item, dict):
                continue
            unit_id = _receipt_id(item.get("unitId"))
            state = item.get("state")
            if unit_id is not None and state in {
                "no_citations_found",
                "complete",
                "failed",
                "still_missing",
            }:
                states.append({"unitId": unit_id, "state": state})
        phase = value.get("phase")
        status = value.get("status")
        if phase not in RECEIPT_PHASE_VALUES or status not in {
            "complete",
            "incomplete",
        }:
            return None, "v2 coverage receipt had an invalid phase or status"
        return {
            "schemaVersion": "cite-check.coverage.v2",
            "runId": run_id,
            "phase": phase,
            "unitStates": states,
            "retriedUnitIds": _receipt_ids(value.get("retriedUnitIds")),
            "status": status,
            "isComplete": value.get("isComplete") is True,
        }, None
    return None, "coverage receipt schemaVersion is unsupported"


def _summarize_preflight(value: Any) -> dict[str, str] | None:
    if not isinstance(value, dict):
        return None
    status = value.get("status")
    if status not in RECEIPT_PREFLIGHT_STATUS_VALUES:
        return None
    summary = {"status": status}
    reason = _receipt_text(value.get("reason"))
    if reason is not None:
        summary["reason"] = reason
    return summary


def _summarize_capability(value: Any) -> tuple[dict[str, Any] | None, str | None]:
    if isinstance(value, dict) and isinstance(value.get("capability"), dict):
        value = value["capability"]
    if not isinstance(value, dict):
        return None, "capability receipt was not an object"
    # Capability receipts are also emitted by host-native and provider-neutral
    # paths.  Keep the provider observed in the receipt instead of silently
    # dropping every non-Codex run from the audit trail.  A missing or
    # malformed provider remains non-actionable and is ignored below.
    provider = _receipt_text(value.get("provider"))
    if provider is None:
        return None, "capability receipt did not identify a provider"

    observed_version = value.get("schemaVersion")
    if observed_version not in {
        "cite-check.runner-capability.v1",
        "cite-check.runner-capability.v2",
    }:
        observed_version = "cite-check.runner-capability.v2"
    summary: dict[str, Any] = {
        "schemaVersion": observed_version,
        "provider": provider,
    }
    for source_key, output_key in (
        ("requestedModel", "requestedModel"),
        ("requestedReasoningEffort", "requestedReasoningEffort"),
        ("observedModel", "observedModel"),
        ("observedReasoningEffort", "observedReasoningEffort"),
        ("selectedRuntime", "selectedRuntime"),
        ("runtime", "selectedRuntime"),
    ):
        text = _receipt_text(value.get(source_key))
        if text is not None and output_key not in summary:
            summary[output_key] = text
    for key in ("fallback", "substitution"):
        text = _receipt_text(value.get(key))
        if text is not None:
            summary[key] = text
    for key in ("sdk", "cli"):
        raw = value.get(key)
        if not isinstance(raw, dict):
            continue
        item: dict[str, Any] = {}
        if isinstance(raw.get("available"), bool):
            item["available"] = raw["available"]
        if isinstance(raw.get("executable"), bool):
            item["executable"] = raw["executable"]
        reason = _receipt_text(raw.get("reason"))
        if reason is not None:
            item["reason"] = reason
        if item:
            summary[key] = item
    for key in ("preflight", "fallbackPreflight"):
        preflight = _summarize_preflight(value.get(key))
        if preflight is not None:
            summary[key] = preflight
    telemetry = value.get("cacheTelemetry")
    if isinstance(telemetry, dict):
        cache: dict[str, Any] = {}
        for key in ("inputTokens", "cachedInputTokens", "cacheWriteInputTokens"):
            number = telemetry.get(key)
            if isinstance(number, int) and not isinstance(number, bool) and number >= 0:
                cache[key] = number
        status = telemetry.get("status")
        if status in {"observed", "unavailable"}:
            cache["status"] = status
        if cache:
            summary["cacheTelemetry"] = cache
    return summary, None


def _summarize_attempts(value: Any) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for raw in _load_receipt_collection(value):
        unit_id = _receipt_id(raw.get("unitId"))
        raw_attempts = raw.get("attempts")
        if unit_id is None or not isinstance(raw_attempts, list):
            continue
        attempts: list[dict[str, Any]] = []
        for attempt in raw_attempts[:RECEIPT_MAX_ATTEMPTS_PER_UNIT]:
            if not isinstance(attempt, dict):
                continue
            item: dict[str, Any] = {}
            number = attempt.get("attempt")
            if isinstance(number, int) and not isinstance(number, bool) and number >= 1:
                item["attempt"] = number
            status = attempt.get("status")
            item["status"] = status if status in RECEIPT_STATUS_VALUES else "unknown"
            code = _receipt_id(attempt.get("code"))
            if code is not None:
                item["reason"] = code
            if isinstance(attempt.get("retryable"), bool):
                item["retryable"] = attempt["retryable"]
            if isinstance(attempt.get("cancelled"), bool):
                item["cancelled"] = attempt["cancelled"]
            for key in (
                "requestedModel",
                "requestedReasoningEffort",
                "observedModel",
                "observedReasoningEffort",
            ):
                value = _receipt_text(attempt.get(key))
                if value is not None:
                    item[key] = value
            attempts.append(item)
        if not attempts:
            continue
        failure_reasons = sorted(
            {item["reason"] for item in attempts if "reason" in item}
        )
        summaries.append(
            {
                "unitId": unit_id,
                "attemptCount": len(attempts),
                "retryCount": max(0, len(attempts) - 1),
                "statuses": [item["status"] for item in attempts],
                "failureReasons": failure_reasons,
                "attempts": attempts,
            }
        )
    summaries.sort(key=lambda item: item["unitId"])
    return summaries[:RECEIPT_MAX_UNITS]


def _summarize_failures(value: Any) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for raw in _load_receipt_collection(value):
        unit_id = _receipt_id(raw.get("unitId"))
        reason = _receipt_id(raw.get("code")) or _receipt_id(raw.get("reason"))
        if unit_id is None or reason is None:
            continue
        item: dict[str, Any] = {"unitId": unit_id, "reason": reason}
        for key in ("retryable", "cancelled"):
            if isinstance(raw.get(key), bool):
                item[key] = raw[key]
        summaries.append(item)
    summaries.sort(key=lambda item: (item["unitId"], item["reason"]))
    return summaries[:RECEIPT_MAX_UNITS]


def ingest_receipts(
    report: dict[str, Any],
    *,
    coverage: Any = None,
    capability: Any = None,
    attempts: Any = None,
    failures: Any = None,
) -> dict[str, Any]:
    """Attach bounded execution telemetry without changing report truth.

    The report core's worker reconciliation remains the only source of
    completeness.  These optional receipts explain how the run got there:
    runtime selection/preflight, retries, failures, and cache observations.
    A receipt that claims complete coverage is displayed as telemetry only and
    cannot upgrade ``report.status`` or ``report.coverage``.
    """

    run_id = report.get("runId")
    if not isinstance(run_id, str):
        raise ReportInputError("report.runId is required before receipt ingestion")
    receipts: dict[str, Any] = {
        "coverage": None,
        "capability": None,
        "attempts": [],
        "failures": [],
    }
    receipt_notes: list[str] = []
    if coverage is not None:
        summary, error = _summarize_coverage_receipt(
            _receipt_object(coverage, "coverage"), run_id=run_id
        )
        if summary is not None:
            receipts["coverage"] = summary
            receipt_notes.append(
                "Execution coverage receipt was ingested for audit only; it "
                "cannot change report completeness."
            )
        elif error is not None:
            receipt_notes.append(f"Execution coverage receipt was ignored: {error}.")
    if capability is not None:
        summary, error = _summarize_capability(
            _receipt_object(capability, "capability")
        )
        if summary is not None:
            receipts["capability"] = summary
        elif error is not None:
            receipt_notes.append(f"Capability receipt was ignored: {error}.")
    if attempts is not None:
        receipts["attempts"] = _summarize_attempts(attempts)
    if failures is not None:
        receipts["failures"] = _summarize_failures(failures)
    report["receipts"] = receipts
    if receipts["attempts"]:
        receipt_notes.append(
            f"Attempt receipts record retries for {len(receipts['attempts'])} unit(s)."
        )
    if receipts["failures"]:
        receipt_notes.append(
            f"Failure receipts record unresolved runtime failures for "
            f"{len(receipts['failures'])} unit(s)."
        )
    report["notes"] = sorted(set([*report.get("notes", []), *receipt_notes]))
    errors = _report_contract_errors(report)
    if errors:
        raise ReportInputError(
            "report schema invalid after receipt ingestion: " + "; ".join(errors[:4])
        )
    return report


def load_worker_results(path: Path) -> list[Any]:
    """Load a JSON array/object, JSONL file, or sorted JSON directory."""

    if path.is_dir():
        results: list[Any] = []
        for child in sorted(path.glob("*.json")):
            value = _load_json(child)
            results.extend(_flatten_results(value))
        return results
    if path.suffix.lower() == ".jsonl":
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            raise ReportInputError(f"cannot read {path.name}: {exc}") from exc
        results = []
        for line_number, line in enumerate(lines, start=1):
            if not line.strip():
                continue
            try:
                results.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ReportInputError(
                    f"invalid JSONL at {path.name}:{line_number}: {exc}"
                ) from exc
        return results
    return _flatten_results(_load_json(path))


def _flatten_results(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        for key in ("results",):
            if isinstance(value.get(key), list):
                return value[key]
        return [value]
    raise ReportInputError("worker result input must be an object or array")


def _write_artifact(path: Path, value: str, output_root: Path) -> None:
    """Atomically replace one artifact without following directory symlinks."""

    try:
        path = _ensure_output_parent(path, output_root)
    except RunnerError as exc:
        raise ReportInputError(str(exc)) from exc
    temporary: Path | None = None
    try:
        descriptor, name = tempfile.mkstemp(
            prefix=f".{path.name}.tmp-", dir=str(path.parent)
        )
        temporary = Path(name)
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(value)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            try:
                temporary.unlink()
            except FileNotFoundError:
                pass


def write_artifacts(
    report: dict[str, Any] | Any,
    output_dir: Path,
    *,
    group_by_authority: bool = False,
    protected_paths: Sequence[Path] = (),
) -> dict[str, Path]:
    """Write the canonical JSON and its deterministic Markdown/HTML views."""

    output_dir = _lexical_absolute(output_dir)
    if output_dir.is_symlink() or output_dir.parent.is_symlink():
        raise ReportInputError("output path contains a symlinked directory")
    artifacts = {
        "json": output_dir / "cite-check-results.json",
        "markdown": output_dir / "cite-check-summary.md",
        "html": output_dir / "cite-check-report.html",
    }
    normalized_inputs = {_lexical_absolute(path) for path in protected_paths}
    if any(_lexical_absolute(path) in normalized_inputs for path in artifacts.values()):
        raise ReportInputError("report artifact path overlaps an input file")
    output_dir.mkdir(parents=True, exist_ok=True)
    if output_dir.is_symlink() or not output_dir.is_dir():
        raise ReportInputError("output path contains a symlinked directory")
    _write_artifact(artifacts["json"], _canonical_json(report), output_dir)
    _write_artifact(
        artifacts["markdown"],
        render_summary(report, group_by_authority=group_by_authority),
        output_dir,
    )
    _write_artifact(artifacts["html"], render_html(report), output_dir)
    return artifacts


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Aggregate cite-check worker results into offline report artifacts."
    )
    parser.add_argument(
        "--manifest", type=Path, required=True, help="Preparation manifest JSON"
    )
    parser.add_argument(
        "--results",
        type=Path,
        required=True,
        help="Result JSON, JSONL, or directory of result JSON files",
    )
    parser.add_argument(
        "--output-dir", type=Path, required=True, help="Directory for report artifacts"
    )
    parser.add_argument(
        "--execution-json", type=Path, help="Optional execution receipt JSON object"
    )
    parser.add_argument(
        "--coverage-receipt",
        "--coverage-json",
        dest="coverage_receipt",
        type=Path,
        help=(
            "Optional final coverage receipt. If omitted, the aggregator looks "
            "for coverage.json beside a results directory."
        ),
    )
    parser.add_argument(
        "--capability-receipt",
        "--capability-json",
        dest="capability_receipt",
        type=Path,
        help=(
            "Optional runtime capability receipt. If omitted, the "
            "aggregator looks for capability.json beside a results directory."
        ),
    )
    parser.add_argument(
        "--attempts-receipt",
        "--attempts",
        dest="attempts_receipt",
        type=Path,
        help=(
            "Optional per-unit attempt receipt file or directory. If omitted, "
            "the aggregator looks for attempts/ beside a results directory."
        ),
    )
    parser.add_argument(
        "--failures-receipt",
        "--failures",
        dest="failures_receipt",
        type=Path,
        help=(
            "Optional per-unit failure receipt file or directory. If omitted, "
            "the aggregator looks for failures/ beside a results directory."
        ),
    )
    parser.add_argument(
        "--receipt-dir",
        type=Path,
        help=(
            "Optional directory containing coverage.json, capability.json, "
            "attempts/, and failures/."
        ),
    )
    parser.add_argument(
        "--group-by-authority",
        action="store_true",
        help="Group the Markdown findings by primary authority",
    )
    parser.add_argument("--intended-use")
    parser.add_argument("--tribunal")
    parser.add_argument("--jurisdiction")
    parser.add_argument("--procedural-posture")
    parser.add_argument("--as-of-date")
    parser.add_argument(
        "--generated-at",
        help="Optional stable generation timestamp; omitted by default",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        manifest = _load_json(args.manifest)
        worker_results = load_worker_results(args.results)
        execution = _load_json(args.execution_json) if args.execution_json else None
        results_root = args.results if args.results.is_dir() else args.results.parent
        receipt_root = args.receipt_dir or results_root

        def discover(explicit: Path | None, name: str) -> Path | None:
            if explicit is not None:
                return explicit
            candidate = receipt_root / name
            return candidate if candidate.exists() else None

        coverage_receipt = discover(args.coverage_receipt, "coverage.json")
        capability_receipt = discover(args.capability_receipt, "capability.json")
        attempts_receipt = discover(args.attempts_receipt, "attempts")
        failures_receipt = discover(args.failures_receipt, "failures")
        context = {
            "intendedUse": args.intended_use,
            "tribunal": args.tribunal,
            "jurisdiction": args.jurisdiction,
            "proceduralPosture": args.procedural_posture,
            "asOfDate": args.as_of_date,
        }
        report = build_report(
            _as_dict(manifest, "manifest"),
            worker_results,
            execution=_as_dict(execution, "execution")
            if execution is not None
            else None,
            target_context=context,
            generated_at=args.generated_at,
            source_root=args.manifest.parent,
        )
        if any(
            receipt is not None
            for receipt in (
                coverage_receipt,
                capability_receipt,
                attempts_receipt,
                failures_receipt,
            )
        ):
            report = ingest_receipts(
                report,
                coverage=coverage_receipt,
                capability=capability_receipt,
                attempts=attempts_receipt,
                failures=failures_receipt,
            )
        protected_paths = {args.manifest}
        protected_paths.update(
            args.results.glob("*.json") if args.results.is_dir() else (args.results,)
        )
        for optional_input in (
            args.execution_json,
            coverage_receipt,
            capability_receipt,
            attempts_receipt,
            failures_receipt,
        ):
            if optional_input is None:
                continue
            protected_paths.update(
                optional_input.glob("*.json")
                if optional_input.is_dir()
                else (optional_input,)
            )
        target = manifest.get("target") if isinstance(manifest, dict) else None
        if isinstance(target, dict):
            for name in ("path", "fullDocumentRef"):
                if isinstance(target.get(name), str):
                    protected_paths.add(
                        _relative_manifest_source(
                            args.manifest.parent.resolve(),
                            target[name],
                            f"target {name}",
                        )
                    )
        authorities = (
            manifest.get("authorities") if isinstance(manifest, dict) else None
        )
        if isinstance(authorities, list):
            for authority in authorities:
                if isinstance(authority, dict) and isinstance(
                    authority.get("path"), str
                ):
                    protected_paths.add(
                        _relative_manifest_source(
                            args.manifest.parent.resolve(),
                            authority["path"],
                            "authority",
                        )
                    )
        artifacts = write_artifacts(
            report,
            args.output_dir,
            group_by_authority=args.group_by_authority,
            protected_paths=tuple(protected_paths),
        )
    except (OSError, ReportInputError) as exc:
        print(f"cite-check aggregation failed: {exc}", file=sys.stderr)
        return 2
    for label, path in artifacts.items():
        # Keep the CLI receipt portable and confidentiality-safe.  The caller
        # already knows the selected output directory; echoing an absolute
        # ``Path`` here would disclose a local workspace location in logs.
        print(f"{label}: {path.name}")
    # The run directory persists for audit.  Deleting prepared copies,
    # receipts, or attempts is the lawyer's manual decision, so this tool
    # never removes anything it did not write.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
