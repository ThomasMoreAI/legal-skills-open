"""Render the lawyer-facing narratives.md from a validated deliverable.

Order: the draft entries first, then anything the lawyer must check, then the
status and scope sentence, then a short record. Headings for entries are
``### <workstreamId>`` and every entry ends with a ``Support:`` line; the
rendered-output rescanner relies on both anchors.
"""

from __future__ import annotations

from typing import Any

import render_language


def _entry_lines(narrative: dict[str, Any]) -> list[str]:
    return [
        "",
        f"### {narrative['workstreamId']}",
        "",
        narrative["text"],
        "",
        render_language.SUPPORT_LINES[narrative["supportClass"]],
    ]


def _question_lines(questions: list[dict[str, Any]]) -> list[str]:
    if not questions:
        return []
    lines = ["", "## Needs your check", ""]
    for question in questions:
        reason = render_language.REASON_LINES.get(
            question["reason"], question["reason"]
        )
        lines.append(f"- {question['source']}: {reason}")
    return lines


def render_markdown(deliverable: dict[str, Any]) -> str:
    exception_count = deliverable["receipt"]["counts"]["exceptionLedgerItems"]
    lines = ["# Time Narratives", "", "## Draft entries"]
    if not deliverable["narratives"]:
        lines += ["", render_language.EMPTY_RESULT_LINE]
    for narrative in deliverable["narratives"]:
        lines += _entry_lines(narrative)
    lines += _question_lines(deliverable["checkQuestions"])
    lines += [
        "",
        render_language.STATUS_LINES[deliverable["status"]],
        "",
        render_language.SCOPE_SENTENCE,
        "",
        "## Record",
        "",
        "Packet scope: expressly selected only",
        "Packet reconciliation: complete",
        "Workday completeness: not assessed",
        "Posting state: unposted draft",
        f"Exceptions recorded: {exception_count}",
    ]
    return "\n".join(lines) + "\n"
