"""Render HTML, its short chat handoff, or full Markdown from deliverable.json.

Method v2.9 uses the compact record; v2.8 rendering remains for saved records.

Stdlib only. The model writes the structured companion once, including the
plain-English prose fields; this script emits the document in the Step 7
shape so that the shape can never be wrong and nothing is written twice:

    python "<skill root>/scripts/render_brief.py" DELIVERABLE.json --out BRIEF.md

Exit codes: 0 rendered; 1 the companion lacks a field the document needs
(faults on stdout as JSON, nothing written); 2 the file is missing or not
JSON. validate_deliverable.py then binds the rendered brief to the
companion as before.
"""

from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

from brief_sections import (
    PP_CLASSES,
    context,
    holds_detail,
    pp_detail,
    receipt,
    table,
    verdict_line,
)

BRIEF_FIELDS = (
    "position_name",
    "run_date",
    "what_this_is",
    "meaning",
    "summary",
    "document_key",
    "scope_confirmation",
    "established",
    "follows",
)
PP_FIELDS = ("title", "hits", "test_applied", "next_step")


class RenderError(ValueError):
    def __init__(self, faults: list[dict]) -> None:
        self.faults = faults
        super().__init__("; ".join(f["detail"] for f in faults))


def _check(d: dict) -> None:
    faults: list[dict] = []
    brief = d.get("brief")
    if not isinstance(brief, dict):
        faults.append({"code": "missing_brief", "detail": "brief object required"})
    else:
        for field in BRIEF_FIELDS:
            if not brief.get(field):
                faults.append(
                    {"code": "missing_brief_field", "detail": f"brief.{field} required"}
                )
    for f in d.get("findings") or []:
        fid = f.get("id", "?")
        if not str(f.get("title", "")).strip():
            faults.append(
                {"code": "missing_finding_title", "detail": f"{fid}: title required"}
            )
        if f.get("classification") in PP_CLASSES:
            for field in PP_FIELDS:
                if not str(f.get(field, "")).strip():
                    faults.append(
                        {
                            "code": "missing_pressure_point_prose",
                            "detail": f"{fid}: {field} required",
                        }
                    )
    if (
        d.get("verdict") == "incomplete"
        and not str(d.get("incomplete_reason", "")).strip()
    ):
        faults.append(
            {
                "code": "missing_incomplete_reason",
                "detail": "incomplete_reason required",
            }
        )
    if faults:
        raise RenderError(faults)


def render(d: dict, output_format="chat", source_root=None) -> str:
    from result_contract import METHOD_VERSION, presentation_faults

    if output_format not in ("chat", "document", "html", "handoff"):
        raise ValueError("format must be chat, document, html or handoff")
    if d.get("method_version") == METHOD_VERSION:
        from chat_result import render_result

        faults = presentation_faults(d)
        for f in d.get("findings") or []:
            if f.get("classification") in PP_CLASSES:
                for field in PP_FIELDS:
                    if not str(f.get(field, "")).strip():
                        faults.append(
                            {
                                "code": "missing_pressure_point_prose",
                                "detail": f"{f.get('id')}: {field} required",
                            }
                        )
        if faults:
            raise RenderError(faults)
        if output_format in ("html", "handoff"):
            from html_result import render_handoff, render_html

            return (
                render_html(d, source_root)
                if output_format == "html"
                else render_handoff(d)
            )
        return render_result(d, output_format, source_root)
    if output_format in ("html", "handoff"):
        raise RenderError(
            [
                {
                    "code": "legacy_html_unsupported",
                    "detail": "HTML requires v2.9; retain the legacy document export",
                }
            ]
        )
    _check(d)
    findings = list(d.get("findings") or [])
    brief = d["brief"]
    n_docs = len(d.get("coverage", {}).get("reviewed", []))
    lines = [
        f"# Pressure test: {brief['position_name']}",
        "",
        f"{brief['run_date']} · {n_docs} document(s) reviewed · produced by "
        "/pressuretest · machine-proposed, for lawyer review",
        "",
        "## What this document is",
        "",
        brief["what_this_is"],
        "",
        "## The answer",
        "",
        f"**{verdict_line(d, findings)}**",
        "",
        brief["meaning"],
        "",
        brief["summary"],
        "",
        f"**What is established.** {brief['established']}",
        "",
        f"**What currently follows.** {brief['follows']}",
        "",
        *table(d, findings),
        "",
    ]
    if d["verdict"] == "pressure_points":
        lines += pp_detail(findings)
    elif d["verdict"] == "position_holds":
        lines += holds_detail(d, findings)
    lines += context(d, findings)
    lines += receipt(d, findings)
    return "\n".join(lines).rstrip("\n") + "\n"


def main(argv: list[str] | None = None) -> int:
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deliverable")
    parser.add_argument(
        "--out", help="optional output path; otherwise emit native-chat Markdown"
    )
    parser.add_argument(
        "--format", choices=("chat", "document", "html", "handoff"), default="chat"
    )
    parser.add_argument(
        "--source-root", help="selected source root for existing-file links"
    )
    args = parser.parse_args(argv)
    try:
        data = json.loads(Path(args.deliverable).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    try:
        text = render(data, args.format, args.source_root)
    except RenderError as exc:
        json.dump(
            {"status": "contract_fault", "faults": exc.faults}, sys.stdout, indent=1
        )
        print()
        return 1
    if args.out is None:
        sys.stdout.write(text)
        return 0
    try:
        Path(args.out).write_text(text, encoding="utf-8")
    except OSError as exc:
        print(f"output could not be written: {type(exc).__name__}", file=sys.stderr)
        return 2
    json.dump(
        {"status": "rendered", "out": args.out, "lines": text.count("\n")},
        sys.stdout,
        indent=1,
    )
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
