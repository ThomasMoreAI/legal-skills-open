"""One complete reading view for native chat and optional document export."""

import re
from pathlib import Path
from urllib.parse import quote

from brief_sections import (
    CLOSING,
    PP_CLASSES,
    REVIEW,
    pressure_points,
)
from result_contract import CHECKPOINT_LABELS

ASSESSMENTS = {
    "breaks_position": "Problem with the position",
    "internal_defect": "Contradiction to correct",
    "defeated": "The documents answer this objection",
    "weakens_route": "One argument fails; another still supports the conclusion",
    "proof_gap": "Evidence still needed",
    "context": "Practical point or qualification",
}
READING_GUIDE = (
    "Potential issues are tested against the supplied documents. Problems, "
    "evidence gaps and practical corrections need attention; objections answered "
    "by the documents show which parts of the argument remain supported. "
    "An answered objection is not an additional problem or proof that the whole "
    "position is correct."
)


def overview(data, findings) -> list[str]:
    if data["verdict"] == "incomplete":
        verdict = "Verdict: this review is incomplete."
    elif data["verdict"] == "position_holds":
        verdict = "The position withstands the objections tested on these documents."
    elif any(f["classification"] == "breaks_position" for f in findings):
        verdict = "The position is not supported in full by the supplied documents."
    else:
        verdict = (
            "The conclusion remains supported, but the draft contains "
            "contradictions that need correction."
        )
    lines = ["## Summary", "", f"**{verdict}**", "", data["brief"]["summary"], ""]
    if data["verdict"] == "incomplete" and data.get("incomplete_reason"):
        lines += [data["incomplete_reason"], ""]
    lines += [f"**How to read this review:** {READING_GUIDE}", ""]
    attention = pressure_points(findings) + [
        f for f in findings if f["classification"] in ("proof_gap", "context")
    ]
    if attention:
        lines += ["### Issues requiring attention", ""]
        lines += [
            f"- **{ASSESSMENTS[f['classification']]}:** {f['title']}" for f in attention
        ]
        lines += [""]
    return lines


def plain(value) -> str:
    """Escape inline source metadata as text, never authored Markdown links."""
    return re.sub(r"([\\`*_[\]<>])", r"\\\1", " ".join(str(value).split()))


def source_name(data, filename, root=None) -> str:
    meta = data["sources"][filename]
    label = plain(meta["name"])
    if meta.get("date"):
        label += f", {plain(meta['date'])}"
    if root is not None:
        base = Path(root).resolve()
        path = (base / filename).resolve()
        if (
            not Path(filename).is_absolute()
            and path.is_relative_to(base)
            and path.is_file()
        ):
            target = quote(path.as_posix(), safe="/:")
            return f"[{label}](<{target}>)"
    return label


def passages(data, anchors, root) -> list[str]:
    lines: list[str] = []
    for anchor in anchors:
        lines += [
            f"**{source_name(data, anchor['source'], root)} — "
            f"{plain(anchor['locator'])}**",
            "",
            *[f"> {line}" for line in anchor["quote"].splitlines()],
            "",
        ]
    return lines


def finding_detail(data, finding, number, root) -> list[str]:
    f = finding
    answer_label = (
        "Why this objection is answered"
        if f["classification"] == "defeated"
        else "Why the conclusion remains supported"
    )
    lines = [f"### {number}. {f['title']}", "", f["statement"], ""]
    if f["classification"] in PP_CLASSES:
        severity = (
            "The conclusion is not supported in full"
            if f["classification"] == "breaks_position"
            else "Contradiction as drafted"
        )
        lines += [f"**Affects:** {f['hits']}. {severity}.", ""]
    else:
        lines += [f"**Assessment:** {ASSESSMENTS[f['classification']]}.", ""]
    lines += passages(data, f["anchors"], root)
    for field, label in (
        ("test_applied", "Assessment"),
        ("dispositive_anchor_note", answer_label),
        ("flip_statement", "Consequence if accepted"),
        ("defect_statement", "Consequence if accepted"),
        ("survives", "What remains supported"),
        ("smallest_change", "What would change this result"),
        ("what_would_close", "Evidence needed"),
        ("next_step", "Next action"),
    ):
        if f.get(field):
            lines += [f"**{label}:** {f[field]}", ""]
    return lines


def review_limits(data) -> list[str]:
    cov = data["coverage"]
    lines = ["## Outstanding evidence and review limits", ""]
    if data.get("incomplete_reason") and data["verdict"] == "incomplete":
        lines += [data["incomplete_reason"], ""]
    for key, label in (
        ("parked", "Unread"),
        ("excluded", "Excluded"),
        ("unreadable", "Unreadable"),
    ):
        for filename in cov.get(key, []):
            lines.append(f"- {label}: {source_name(data, filename)}.")
    for key in ("parked", "indeterminate"):
        for route in data["routes"].get(key, []):
            lines.append(f"- Unfinished route ({key}): {plain(route)}.")
    for test in data["tests"].get("parked", []):
        lines.append(f"- Unperformed test: {plain(test)}.")
    checkpoint = data["checkpoint"]
    lines += ["", CHECKPOINT_LABELS[checkpoint["status"]], ""]
    read = checkpoint["map_read"]
    lines += [
        f"The initial map followed reading {len(read)} of "
        f"{len(cov['selected'])} selected documents: "
        + "; ".join(source_name(data, filename) for filename in read)
        + ".",
        "",
    ]
    if checkpoint.get("map_changed_after_full_read"):
        lines += [
            f"The map changed after the full read: {checkpoint['change_note']}",
            "",
        ]
    lines += [
        f"Reviewed {len(cov['reviewed'])} of {len(cov['selected'])} "
        "selected documents; "
        f"assessed {len(data['findings'])} potential objections or issues.",
        "",
        "This tests logic and consistency in the supplied documents. "
        "Quote checks, where available, establish normalised text occurrence only; "
        "pinpoint accuracy, contextual meaning and legal correctness require review. "
        "See the actual validation result for what was checked.",
        "",
        REVIEW,
        "",
        "Cited authorities were not checked; run /cite-check on this result "
        "before it leaves the building.",
        "",
    ]
    return lines


def render_result(data: dict, output_format="chat", source_root=None) -> str:
    brief = data["brief"]
    findings = data["findings"]
    lines: list[str] = []
    if output_format == "document":
        lines += [
            f"# Pressure test: {brief['position_name']}",
            "",
            brief["run_date"],
            "",
            "A review of the stated positions against the selected sources, "
            "for lawyer review.",
            "",
        ]
    lines += overview(data, findings)
    for field, label in (
        ("established", "What is established"),
        ("follows", "What currently follows"),
    ):
        if brief.get(field):
            lines += [f"**{label}:** {brief[field]}", ""]
    lines += [
        "**Position tested:** "
        + "; ".join(f"{p['owner']}: {p['conclusion']}" for p in data["positions"]),
        "",
    ]
    route_heading = (
        "Why the conclusion remains supported"
        if data["verdict"] == "position_holds"
        else "The strongest argument supporting the position"
    )
    groups = [
        (
            "Problems with the position",
            [f for f in findings if f["classification"] == "breaks_position"],
        ),
        (
            "Contradictions to correct",
            [f for f in findings if f["classification"] == "internal_defect"],
        ),
        (
            "Evidence still needed",
            [f for f in findings if f["classification"] == "proof_gap"],
        ),
        (
            "Practical points and qualifications",
            [f for f in findings if f["classification"] == "context"],
        ),
        (
            "Objections the documents answer",
            [f for f in findings if f["classification"] == "defeated"],
        ),
        (
            "Arguments that fail without changing the conclusion",
            [f for f in findings if f["classification"] == "weakens_route"],
        ),
    ]
    number = 0
    for title, group in groups:
        if title == "Objections the documents answer":
            lines += [f"## {route_heading}", "", data["strongest_route"]["summary"], ""]
            lines += passages(data, data["strongest_route"]["anchors"], source_root)
        if group:
            lines += [f"## {title}", ""]
        for finding in group:
            number += 1
            lines += finding_detail(data, finding, number, source_root)
    for item in brief.get("context_items") or []:
        lines += [item, ""]
    lines += review_limits(data)
    lines += ["## Sources reviewed", ""]
    for filename in data["coverage"]["selected"]:
        status = next(
            key
            for key in ("reviewed", "parked", "excluded", "unreadable")
            if filename in data["coverage"][key]
        )
        status = "unread" if status == "parked" else status
        lines.append(f"- {source_name(data, filename, source_root)} — {status}.")
    lines += ["", CLOSING, ""]
    return "\n".join(lines).rstrip("\n") + "\n"
