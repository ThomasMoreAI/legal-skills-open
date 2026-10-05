"""Section builders for the exported pressure-test brief (method v2.8).

Imported by render_brief.py. Every function returns markdown lines; none
writes machine vocabulary, so the rendered document passes the validator's
token ban by construction.
"""

from __future__ import annotations

PP_CLASSES = ("breaks_position", "internal_defect")
VERDICT_LINES = {
    "pressure_points_breaks": (
        "Verdict: the position does not hold as stated — pressure points found."
    ),
    "pressure_points_internal": (
        "Verdict: the conclusion survives on the supplied documents, but the "
        "position as drafted contradicts itself — pressure points found."
    ),
    "position_holds": "Verdict: the position holds on the supplied documents.",
    "incomplete": "Verdict: this review is incomplete.",
}
PLAIN_CLASS = {
    "defeated": "defeated — the documents answer it",
    "weakens_route": "weakens one route only — the conclusion still stands",
    "proof_gap": "evidence to watch",
    "context": "context",
}
CLOSING = (
    "This review can only test the routes it identified — anything it did not "
    "identify remains untested. It does not verify cited authorities or certify "
    "the position."
)
HANDOFF = (
    "Cited authorities were not checked; run /cite-check on this document "
    "before it leaves the building."
)
REVIEW = "Review status: proposed by the machine — not yet reviewed by a lawyer."
FULL_DETAIL_LIMIT = 5


def cell(text) -> str:
    """One table cell: collapse whitespace, never let a pipe break the row."""
    return " ".join(str(text).split()).replace("|", "/")


def where(anchors) -> str:
    return "; ".join(a.get("locator") or a.get("source", "?") for a in anchors)


def passages(anchors) -> list[str]:
    """One blockquote per passage, blank-line separated so they never merge."""
    lines: list[str] = []
    for a in anchors:
        if lines:
            lines.append("")
        lines.append(f'> "{cell(a["quote"])}" ({a.get("locator") or a["source"]})')
    return lines


def pressure_points(findings: list) -> list:
    """Position-breaking entries first, then contradictions, source order within."""
    breaks = [f for f in findings if f["classification"] == "breaks_position"]
    contradictions = [f for f in findings if f["classification"] == "internal_defect"]
    return breaks + contradictions


def verdict_line(d: dict, findings: list) -> str:
    verdict = d["verdict"]
    if verdict == "pressure_points":
        breaks = any(f["classification"] == "breaks_position" for f in findings)
        key = "pressure_points_breaks" if breaks else "pressure_points_internal"
        return VERDICT_LINES[key]
    return VERDICT_LINES[verdict]


def table(d: dict, findings: list) -> list[str]:
    verdict = d["verdict"]
    lines: list[str] = []
    if verdict == "pressure_points":
        lines += [
            "| # | Finding | Whose case it hits | How serious | Where |",
            "|---|---|---|---|---|",
        ]
        for f in pressure_points(findings):
            serious = (
                "Breaks the position"
                if f["classification"] == "breaks_position"
                else "Contradiction as drafted"
            )
            lines.append(
                f"| {f['id']} | {cell(f['title'])} | {cell(f['hits'])} "
                f"| {serious} | {cell(where(f['anchors']))} |"
            )
    elif verdict == "position_holds":
        lines += [
            "| # | Attack tested | Outcome | Answered by |",
            "|---|---|---|---|",
        ]
        for f in findings:
            answered = f.get("dispositive_anchor_note") or where(f["anchors"])
            outcome = PLAIN_CLASS.get(f["classification"], "context")
            lines.append(
                f"| {f['id']} | {cell(f['title'])} | {outcome} | {cell(answered)} |"
            )
    else:
        lines += ["## What is missing", "", f"- {d['incomplete_reason']}"]
        for name in d.get("coverage", {}).get("parked", []):
            lines.append(f"- {name} was set aside unread.")
    key = d["brief"]["document_key"]
    lines += ["", " · ".join(f"{k} = {v}" for k, v in key.items())]
    return lines


def _pp_full(f: dict) -> list[str]:
    internal = f["classification"] == "internal_defect"
    lands = f["defect_statement"] if internal else f["flip_statement"]
    lines = [
        f"## {f['id']} — {cell(f['title'])}",
        "",
        f"**Whose case it hits.** {f['hits']}",
        "",
        f"**If this lands.** {lands}",
        "",
        "**The passages.**",
        "",
        *passages(f["anchors"]),
        "",
        f"**The test applied.** {f['test_applied']}",
        "",
        f"**What survives.** {f['survives']}",
        "",
    ]
    if f.get("smallest_change"):
        lines += [
            "**Smallest change of fact that would change the result.** "
            f"{f['smallest_change']}",
            "",
        ]
    lines += [f"**Next step.** {f['next_step']}", "", f"*{REVIEW}*", ""]
    return lines


def pp_detail(findings: list) -> list[str]:
    pps = pressure_points(findings)
    lines: list[str] = []
    for f in pps[:FULL_DETAIL_LIMIT]:
        lines += _pp_full(f)
    rest = pps[FULL_DETAIL_LIMIT:]
    if rest:
        lines += ["## Further points, in brief", ""]
        for f in rest:
            lines.append(
                f"- **{f['id']}** — {cell(f['title'])}: {f['statement']} "
                f"Hits {f['hits']}. {REVIEW}"
            )
        lines.append("")
    survived = [f for f in findings if f["classification"] not in PP_CLASSES]
    if survived:
        lines += ["## Other attacks tested", ""]
        for f in survived:
            outcome = PLAIN_CLASS.get(f["classification"], "context")
            answered = f.get("dispositive_anchor_note") or where(f["anchors"])
            lines.append(
                f"- **{f['id']}** — {cell(f['title'])}: {outcome}. "
                f"Answered by {answered}"
            )
        lines.append("")
    return lines


def holds_detail(d: dict, findings: list) -> list[str]:
    route = d["strongest_route"]
    lines = [
        "## The route that holds",
        "",
        route["summary"],
        "",
        *passages(route["anchors"]),
        "",
        "## Attack register",
        "",
    ]
    for f in findings:
        outcome = PLAIN_CLASS.get(f["classification"], "context")
        lines += [
            f"### {f['id']} — {cell(f['title'])}",
            "",
            f"**Outcome.** {outcome}.",
            "",
            f["statement"],
            "",
        ]
        if f.get("dispositive_anchor_note"):
            lines += [f"**Answered by.** {f['dispositive_anchor_note']}", ""]
        lines += [*passages(f["anchors"]), "", f"*{REVIEW}*", ""]
    watch = [f for f in findings if f["classification"] == "proof_gap"]
    if watch:
        lines += ["## Watch items", ""]
        for f in watch:
            closer = (
                f" What would close it: {f['what_would_close']}"
                if f.get("what_would_close")
                else ""
            )
            lines.append(f"- **{f['id']}** — {f['statement']}{closer}")
        lines.append("")
    return lines


def context(d: dict, findings: list) -> list[str]:
    items = list(d["brief"].get("context_items") or [])
    items += [
        f"{f['id']} — {f['statement']}"
        for f in findings
        if f["classification"] == "context"
    ]
    if not items:
        return []
    return ["## Context, not findings", "", *[f"- {item}" for item in items], ""]


def receipt(d: dict, findings: list) -> list[str]:
    cov = d.get("coverage", {})
    aside = list(cov.get("excluded", [])) + list(cov.get("unreadable", []))
    lines = [
        "## How this review was done",
        "",
        "| | |",
        "|---|---|",
        f"| Documents reviewed | {len(cov.get('reviewed', []))} |",
        f"| Set aside or unreadable | {len(aside)} |",
        f"| Lines of attack tested | {len(findings)} |",
        "",
    ]
    if aside:
        lines += ["Not relied on: " + ", ".join(aside) + ".", ""]
    lines += [
        d["brief"]["scope_confirmation"],
        "",
        *_map_basis(d),
        HANDOFF,
        "",
        CLOSING,
        "",
    ]
    return lines


def _map_basis(d: dict) -> list[str]:
    """Disclose what the map rested on when the lawyer saw it."""
    checkpoint = d.get("checkpoint") or {}
    read = list(checkpoint.get("map_read") or [])
    total = len(d.get("coverage", {}).get("selected", []))
    if not read:
        return []
    if len(read) >= total:
        sentence = f"The map was shown after reading all {total} documents."
    else:
        sentence = (
            f"The map was shown after reading {len(read)} of {total} documents "
            f"({', '.join(read)}); the rest were read while the lawyer "
            "considered it."
        )
    lines = [sentence, ""]
    if checkpoint.get("map_changed_after_full_read") and checkpoint.get("change_note"):
        lines += [
            f"The map changed after the full read: {checkpoint['change_note']}",
            "",
        ]
    return lines
