"""Compact v2.9 presentation contract; substantive checks stay in the validator."""

from pathlib import Path

METHOD_VERSION = "lq.pressuretest.method.v2.9"
BRIEF_FIELDS = ("position_name", "run_date", "summary")
CHECKPOINT_STATES = {"confirmed", "amended", "non_interactive", "unanswered"}
CHECKPOINT_LABELS = {
    "confirmed": "The lawyer confirmed the scope before testing.",
    "amended": "The lawyer's scope corrections were incorporated before testing.",
    "non_interactive": (
        "This was a non-interactive run; no live lawyer confirmation was obtained."
    ),
    "unanswered": "The scope check is unanswered; adjudication has not started.",
}


def presentation_faults(data: dict) -> list[dict]:
    faults: list[dict] = []

    def fault(code, detail):
        faults.append({"code": code, "detail": detail})

    brief = data.get("brief")
    if not isinstance(brief, dict):
        fault("missing_brief", "brief object required")
    else:
        for field in BRIEF_FIELDS:
            if not isinstance(brief.get(field), str) or not brief[field].strip():
                fault("missing_brief_field", f"brief.{field} required")
    sources = data.get("sources")
    selected = data.get("coverage", {}).get("selected", [])
    if not isinstance(sources, dict):
        fault("missing_sources", "sources must map selected filenames to names")
        sources = {}
    if set(sources) != set(selected):
        fault(
            "source_inventory_mismatch", "sources must match coverage.selected exactly"
        )
    for filename, meta in sources.items():
        if not isinstance(meta, dict):
            fault("bad_source_metadata", f"sources[{filename}] must be an object")
            continue
        if not isinstance(meta.get("name"), str) or not meta["name"].strip():
            fault("missing_source_name", f"sources[{filename}].name required")
        if "date" not in meta:
            fault("missing_source_date", f"sources[{filename}].date required; use null")
        if meta.get("date") is not None and not isinstance(meta["date"], str):
            fault("bad_source_date", f"sources[{filename}].date must be text or null")
        if set(meta) - {"name", "date"}:
            fault("bad_source_metadata", "source metadata accepts name and date only")
    checkpoint = data.get("checkpoint")
    if not isinstance(checkpoint, dict):
        fault("missing_checkpoint", "checkpoint must be an object")
        checkpoint = {}
    status = checkpoint.get("status")
    if not isinstance(status, str) or status not in CHECKPOINT_STATES:
        fault("bad_checkpoint_status", "checkpoint.status must record the actual reply")
    if status == "unanswered" and data.get("findings"):
        fault(
            "unconfirmed_adjudication",
            "an unanswered map cannot have adjudicated findings",
        )
    anchors = list((data.get("strongest_route") or {}).get("anchors") or [])
    for finding in data.get("findings") or []:
        if isinstance(finding, dict):
            anchors.extend(finding.get("anchors") or [])
    for anchor in anchors:
        if not isinstance(anchor, dict):
            fault("bad_anchor", "anchor must be an object")
            continue
        if not isinstance(anchor.get("locator"), str) or not anchor["locator"].strip():
            fault("missing_anchor_locator", "every anchor needs a visible pinpoint")
        if anchor.get("source") not in sources:
            fault("anchor_source_unknown", "anchor source is missing from sources")
    return faults


def check_result(path: Path, data: dict, output_format: str, root, rep) -> None:
    """Bind all visible content, not merely the verdict and finding IDs."""
    from render_brief import RenderError, render

    try:
        actual = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        rep.fault("result_missing", f"result cannot be read: {type(exc).__name__}")
        return
    try:
        expected = render(data, output_format=output_format, source_root=root)
    except (RenderError, KeyError, TypeError, ValueError) as exc:
        rep.fault("result_unrenderable", f"record cannot render: {type(exc).__name__}")
        return
    if actual.replace("\r\n", "\n") != expected:
        rep.fault(
            "result_record_mismatch",
            "visible result differs from the record; regenerate the result",
        )
    check_language(data, rep)


def check_language(data, rep) -> None:
    """Retain prose rules while excluding quoted evidence and source titles."""
    from validate_deliverable import (
        BANNED_IMPACT,
        BANNED_TELEMETRY,
        MACHINE_TOKENS,
        strip_quoted,
    )

    prose = [
        data["brief"][key]
        for key in (*BRIEF_FIELDS, "established", "follows", "context_items")
        if key in data["brief"]
    ]
    prose.append(data["strongest_route"]["summary"])
    for finding in data["findings"]:
        prose.extend(
            finding[key]
            for key in (
                "title",
                "statement",
                "hits",
                "test_applied",
                "next_step",
                "survives",
                "flip_statement",
                "defect_statement",
                "dispositive_anchor_note",
                "smallest_change",
                "what_would_close",
            )
            if key in finding
        )
    for value in prose:
        for text in value if isinstance(value, list) else [value]:
            if not isinstance(text, str):
                continue
            if MACHINE_TOKENS.search(text):
                rep.fault("result_machine_tokens", "machine vocabulary in result prose")
            if BANNED_TELEMETRY.search(text):
                rep.fault(
                    "result_process_telemetry", "process telemetry in result prose"
                )
            if data["verdict"] == "position_holds" and BANNED_IMPACT.search(
                strip_quoted(text)
            ):
                rep.fault(
                    "result_impact_vocabulary", "impact vocabulary in a sound result"
                )
