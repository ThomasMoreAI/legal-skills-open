"""Deterministic projections of the citation-level cite-check report."""

from __future__ import annotations

import sys
from collections.abc import Mapping
from html import escape
from pathlib import Path
from typing import Any

SCRIPT_PATH = Path(__file__).resolve()
SCRIPTS_DIR = SCRIPT_PATH.parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from common.report_core import ReportInputError, _canonical_json  # noqa: E402

TEMPLATE_PATH = SCRIPT_PATH.parents[2] / "assets" / "report-template.html"


def _markdown_quote(value: Any) -> str:
    text = str(value if value is not None else "")
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("\n", "\n> ")
    )


def _display(value: Any, fallback: str = "not supplied") -> str:
    return fallback if value is None or value == "" else str(value)


def _citation_source_label(citation: Mapping[str, Any]) -> tuple[str, str]:
    value = citation.get("matched_source_id")
    flags = citation.get("validation_flags")
    if isinstance(flags, list) and "source_not_in_authority_universe" in flags:
        return (
            "Untrusted out-of-universe source claim",
            value if isinstance(value, str) else "not supplied",
        )
    return ("Matched source", value if isinstance(value, str) else "not matched")


def _citation_status(citation: Mapping[str, Any]) -> str:
    labels = {
        "red": "do not file as-is",
        "amber": "cannot verify",
        "yellow": "fix before filing",
        "green": "verified",
    }
    severity = citation.get("severity")
    if isinstance(severity, str) and severity in labels:
        return labels[severity]
    flags = citation.get("validation_flags")
    if isinstance(flags, list) and flags:
        return "claimed but unverified"
    return "reported"


def _citation_lines(citation: Mapping[str, Any]) -> list[str]:
    written = _markdown_quote(citation.get("citation_as_written_in_unit"))
    matched = _markdown_quote(citation.get("matched_citation"))
    proposition = citation.get("proposition")
    source_label, source_value = _citation_source_label(citation)
    source = _markdown_quote(source_value)
    excerpt = citation.get("source_excerpt")
    locator = citation.get("source_locator")
    flags = citation.get("validation_flags")
    lines = [
        f"- **{written}** — {_citation_status(citation)}",
        f"  - Matched citation: `{matched}`",
        f"  - Proposition: {_markdown_quote(_display(proposition, 'not supplied'))}",
        f"  - {source_label}: `{source}`",
    ]
    if excerpt is not None:
        lines.append(f"  - Source excerpt: {_markdown_quote(excerpt)}")
    if locator is not None:
        lines.append(f"  - Source locator: `{_markdown_quote(locator)}`")
    if isinstance(flags, list) and flags:
        lines.append(
            "  - Validation flags: "
            + ", ".join(f"`{_markdown_quote(flag)}`" for flag in flags)
        )
    recommended = citation.get("recommended_changes")
    if recommended is not None:
        lines.append(f"  - Recommended changes: {_markdown_quote(recommended)}")
    return lines


def _render_citation_units(report: Mapping[str, Any]) -> list[str]:
    lines = ["## Citation-level results", ""]
    results = report.get("unitResults", [])
    if not results:
        lines.append("No completed review entries were available.")
        return lines
    for result in results:
        unit_id = result["unitId"]
        lines.extend(
            [
                f"### {_markdown_quote(unit_id)}",
                "",
                f"**Disposition:** `{_markdown_quote(result['disposition'])}`",
            ]
        )
        citations = result.get("citations", [])
        if citations:
            lines.extend(["", "**Citations:**"])
            for citation in citations:
                if isinstance(citation, Mapping):
                    lines.extend(_citation_lines(citation))
        validation = result.get("validation")
        if isinstance(validation, Mapping):
            warnings = validation.get("warnings", [])
            issues = validation.get("potential_issues", [])
            if warnings or issues:
                lines.append("")
                lines.append("**Review notes:**")
                for item in [*warnings, *issues]:
                    if isinstance(item, Mapping):
                        lines.append(f"- {_markdown_quote(item.get('message'))}")
        lines.append("")
    return lines


def _render_authority_groups(report: Mapping[str, Any]) -> list[str]:
    lines = ["## Results by authority", ""]
    rows_by_source: dict[str | None, list[Mapping[str, Any]]] = {}
    for result in report.get("unitResults", []):
        if not isinstance(result, Mapping):
            continue
        for citation in result.get("citations", []):
            if not isinstance(citation, Mapping):
                continue
            source_id = citation.get("matched_source_id")
            if not isinstance(source_id, str) or not source_id:
                source_id = None
            rows_by_source.setdefault(source_id, []).append(citation)

    rollup = report.get("authorityRollup")
    if not isinstance(rollup, list) or not rollup:
        lines.append("No authority rollup was available.")
        return lines
    for item in rollup:
        if not isinstance(item, Mapping):
            continue
        source_id = item.get("sourceId")
        label = item.get("identityLabel") or source_id or "unknown"
        lines.append(f"### `{_markdown_quote(source_id)}` — {_markdown_quote(label)}")
        lines.append(
            f"- Kind: {_markdown_quote(item.get('citation_kind', 'other'))}; "
            f"worst: `{_markdown_quote(item.get('worst', 'green'))}`; "
            f"times cited: {item.get('timesCited', 0)}"
        )
        if item.get("unused"):
            note = item.get("collisionNote") or "Supplied but never cited"
            lines.append(f"- {_markdown_quote(note)}")
        elif isinstance(source_id, str):
            for citation in rows_by_source.get(source_id, []):
                lines.extend(_citation_lines(citation))
        lines.append("")

    unmatched = rows_by_source.get(None) or []
    if unmatched:
        lines.extend(["### Unmatched citations", ""])
        for citation in unmatched:
            lines.extend(_citation_lines(citation))
        lines.append("")
    return lines


def render_summary(
    report: Mapping[str, Any], *, group_by_authority: bool = False
) -> str:
    """Render the v2 report without interpreting citation rows as findings."""

    coverage = report["coverage"]
    lines = [
        "# Cite-check report",
        "",
        "**Scope:** Checks citations against the sources supplied for this run; it "
        "does not check later case history or replace full legal research.",
        "",
        "## Review context",
        "",
        f"- Sources supplied: {len(report['authoritySources'])}",
        f"- Document reviewed: {_markdown_quote(report['target']['path'])}",
        "- Intended use: "
        f"{_markdown_quote(_display(report['target'].get('intendedUse')))}",
        f"- Tribunal: {_markdown_quote(_display(report['target'].get('tribunal')))}",
        "- Jurisdiction: "
        f"{_markdown_quote(_display(report['target'].get('jurisdiction')))}",
        "- Procedural posture: "
        f"{_markdown_quote(_display(report['target'].get('proceduralPosture')))}",
        f"- As-of date: {_markdown_quote(_display(report['target'].get('asOfDate')))}",
    ]
    lines.extend(
        [
            "",
            "## Authority set",
            "",
        ]
    )
    if report["authoritySources"]:
        lines.extend(
            f"- `{_markdown_quote(source['sourceId'])}` — "
            f"{_markdown_quote(source['identityLabel'])}; "
            f"readability `{_markdown_quote(source['readability'])}`; "
            f"path `{_markdown_quote(source['path'])}`"
            for source in report["authoritySources"]
        )
    else:
        lines.append("- No authority files were supplied.")
    terminal_count = sum(
        item["state"] in {"complete", "no_citations_found"}
        for item in coverage["unitStates"]
    )
    lines.extend(
        [
            "",
            "## Review completeness",
            "",
            f"- Selected passages: {len(coverage['unitStates'])}",
            f"- Passages reviewed: {terminal_count}",
            "",
        ]
    )
    not_reviewed = [
        state
        for state in coverage["unitStates"]
        if state["state"] not in {"complete", "no_citations_found"}
    ]
    if not_reviewed:
        lines.append("Passages needing review:")
        lines.extend(f"- {_markdown_quote(state['unitId'])}" for state in not_reviewed)
    else:
        lines.append("All selected passages have a review result.")
    lines.append("")
    if group_by_authority:
        lines.extend(_render_authority_groups(report))
    else:
        lines.extend(_render_citation_units(report))
    lines.extend(["## Caveats / Issues", ""])
    sense_check = report.get("senseCheck")
    unresolved_sense_issues = (
        sense_check.get("unresolvedIssueCount", 0)
        if isinstance(sense_check, Mapping)
        else 0
    )
    if report.get("limitations"):
        for limitation in report["limitations"]:
            scope = ""
            if limitation.get("unitId"):
                scope += f" unit `{_markdown_quote(limitation['unitId'])}`"
            if limitation.get("citationIndex") is not None:
                scope += f" citation {limitation['citationIndex']}"
            lines.append(
                f"- `{_markdown_quote(limitation['code'])}`{scope}: "
                f"{_markdown_quote(limitation['message'])}"
            )
        lines.append("")
    if unresolved_sense_issues:
        lines.append(
            f"- Sense check found {unresolved_sense_issues} unresolved "
            f"{'issue' if unresolved_sense_issues == 1 else 'issues'}."
        )
        lines.append("")
    if not report.get("limitations") and not unresolved_sense_issues:
        lines.append("No unresolved caveats or issues were recorded.")
        lines.append("")
    lines.extend(["## Notes", ""])
    lines.extend(f"- {_markdown_quote(note)}" for note in report["notes"])
    lines.append("")
    return "\n".join(lines)


def _html_layer_summary(report: Mapping[str, Any]) -> str:
    coverage = report.get("coverage")
    if not isinstance(coverage, Mapping):
        return ""
    states = coverage.get("unitStates")
    count = len(states) if isinstance(states, list) else 0
    terminal = (
        sum(
            item.get("state") in {"complete", "no_citations_found"}
            for item in states
            if isinstance(item, Mapping)
        )
        if isinstance(states, list)
        else 0
    )
    return (
        '<section class="panel" id="audit-layers" aria-label="Review layers">'
        "<h2>Review completeness</h2>"
        f'<div class="warning"><strong>{escape(str(terminal))} of '
        f"{escape(str(count))} selected passages have a review result.</strong></div>"
        "</section>"
    )


def render_html(report: Mapping[str, Any], *, template_path: Path | None = None) -> str:
    """Render the offline lawyer-facing template with the v2 report payload."""

    template = (template_path or TEMPLATE_PATH).read_text(encoding="utf-8")
    payload = _canonical_json(report)
    payload = (
        payload.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("/", "\\u002f")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    marker = "{{REPORT_JSON}}"
    if marker not in template:
        raise ReportInputError(f"report template does not contain {marker}")
    rendered = template.replace(marker, payload)
    scope_marker = '<section class="panel" id="scope"></section>'
    if scope_marker in rendered:
        rendered = rendered.replace(
            scope_marker, _html_layer_summary(report) + scope_marker, 1
        )
    return rendered
