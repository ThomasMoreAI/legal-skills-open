"""Offline HTML reading view of the validated v2.9 record; no model pass."""

import re
from html import escape
from pathlib import Path

from brief_sections import CLOSING, PP_CLASSES
from chat_result import ASSESSMENTS, READING_GUIDE, overview, review_limits

ASSETS = Path(__file__).resolve().parent.parent / "assets"
GROUPS = (
    ("breaks_position", "Problems with the position"),
    ("internal_defect", "Contradictions to correct"),
    ("proof_gap", "Evidence still needed"),
    ("context", "Practical points and qualifications"),
    ("defeated", "Objections the documents answer"),
    ("weakens_route", "Arguments that fail without changing the conclusion"),
)


def text(value):
    """Treat source and model text as text, allowing only bold emphasis."""
    return re.sub(r"\*\*([^*\n]+)\*\*", r"<strong>\1</strong>", escape(str(value)))


def paragraph(value, label=None):
    prefix = f"<strong>{escape(label)}:</strong> " if label else ""
    return f"<p>{prefix}{text(value)}</p>"


def source(data, filename, root):
    meta = data["sources"][filename]
    label = escape(meta["name"])
    if meta.get("date"):
        label += ", " + escape(meta["date"])
    if root is not None:
        base = Path(root).resolve()
        path = (base / filename).resolve()
        if (
            not Path(filename).is_absolute()
            and path.is_relative_to(base)
            and path.is_file()
        ):
            return f'<a href="{escape(path.as_uri(), quote=True)}">{label}</a>'
    return label


def passages(data, anchors, root):
    return "".join(
        '<figure class="evidence"><figcaption>'
        + source(data, a["source"], root)
        + " — "
        + escape(a["locator"])
        + "</figcaption><blockquote>"
        + escape(a["quote"])
        + "</blockquote></figure>"
        for a in anchors
    )


def finding(data, item, number, root):
    cls = item["classification"]
    opened = " open" if cls in PP_CLASSES else ""
    parts = [
        f'<details class="finding {cls}" id="finding-{number}"{opened}>',
        f'<summary><span class="number">{number:02}</span><span>',
        f'<span class="finding-title">{text(item["title"])}</span>',
        f'<span class="status">{ASSESSMENTS[cls]}</span></span></summary>',
        '<div class="finding-body">',
        paragraph(item["statement"]),
    ]
    if cls in PP_CLASSES:
        parts.append(paragraph(item["hits"], "Affects"))
    parts.append(passages(data, item["anchors"], root))
    answer = (
        "Why this objection is answered"
        if cls == "defeated"
        else "Why the conclusion remains supported"
    )
    for field, label in (
        ("test_applied", "Assessment"),
        ("dispositive_anchor_note", answer),
        ("flip_statement", "Consequence if accepted"),
        ("defect_statement", "Consequence if accepted"),
        ("survives", "What remains supported"),
        ("smallest_change", "What would change this result"),
        ("what_would_close", "Evidence needed"),
        ("next_step", "Next action"),
    ):
        if item.get(field):
            parts.append(paragraph(item[field], label))
    parts.append("</div></details>")
    return "".join(parts)


def render_html(data, source_root=None):
    brief = data["brief"]
    findings = data["findings"]
    # Use the same verdict wording as the complete chat reading view.
    verdict = overview(data, findings)[2].strip("*")
    parts = [
        '<header><p class="eyebrow">PRESSURETEST · FOR LAWYER REVIEW</p>',
        f"<h1>{text(brief['position_name'])}</h1>",
        paragraph(brief["run_date"]),
        "</header>",
        '<section class="summary" id="summary"><h2>Summary</h2>',
        paragraph(verdict, "Assessment"),
        paragraph(brief["summary"]),
        paragraph(READING_GUIDE, "How to read this review"),
    ]
    if data["verdict"] == "incomplete":
        parts.append(paragraph(data["incomplete_reason"], "Unfinished review"))
    for field, label in (
        ("established", "What is established"),
        ("follows", "What currently follows"),
    ):
        if brief.get(field):
            parts.append(paragraph(brief[field], label))
    parts += ["</section><section><h2>Position tested</h2>"]
    for position in data["positions"]:
        parts.append(paragraph(position["conclusion"], position["owner"]))
    ordered = [f for cls, _ in GROUPS for f in findings if f["classification"] == cls]
    attention = [
        (n, f)
        for n, f in enumerate(ordered, 1)
        if f["classification"] not in ("defeated", "weakens_route")
    ]
    if attention:
        parts += ['<h2>Issues requiring attention</h2><ul class="attention">']
        for n, f in attention:
            parts.append(
                f'<li><a href="#finding-{n}">{text(f["title"])}</a> — '
                f"{ASSESSMENTS[f['classification']]}</li>"
            )
        parts.append("</ul>")
    parts += ['</section><nav aria-label="Report sections">']
    for cls, title in GROUPS:
        if any(f["classification"] == cls for f in findings):
            parts.append(f'<a href="#{cls}">{title}</a>')
    parts += [
        '<a href="#sources">Sources and limits</a></nav>',
        '<div class="controls" hidden><button type="button" id="expand">'
        "Expand all findings</button>",
        '<button type="button" id="collapse">Collapse all findings</button>',
        '<button type="button" id="print">Print / save PDF</button></div>',
    ]
    number = 0
    for cls, title in GROUPS:
        if cls == "defeated":
            route_title = (
                "Why the conclusion remains supported"
                if data["verdict"] == "position_holds"
                else "The strongest argument supporting the position"
            )
            parts += [
                f"<section><h2>{route_title}</h2>",
                paragraph(data["strongest_route"]["summary"]),
                passages(data, data["strongest_route"]["anchors"], source_root),
                "</section>",
            ]
        group = [f for f in findings if f["classification"] == cls]
        if group:
            parts.append(f'<section id="{cls}"><h2>{title}</h2>')
            for item in group:
                number += 1
                parts.append(finding(data, item, number, source_root))
            parts.append("</section>")
    parts.append('<section id="sources">')
    for value in brief.get("context_items") or []:
        parts.append(paragraph(value))
    for line in review_limits(data):
        if line.startswith("## "):
            parts.append(f"<h2>{text(line[3:])}</h2>")
        elif line.strip():
            parts.append(paragraph(line.removeprefix("- ")))
    parts.append("<h2>Sources reviewed</h2><ul>")
    for filename in data["coverage"]["selected"]:
        state = next(
            k
            for k in ("reviewed", "parked", "excluded", "unreadable")
            if filename in data["coverage"][k]
        )
        parts.append(
            f"<li>{source(data, filename, source_root)} — "
            f"{'unread' if state == 'parked' else state}</li>"
        )
    parts += ["</ul></section><footer>", paragraph(CLOSING), "</footer>"]
    template = (ASSETS / "report-template.html").read_text(encoding="utf-8")
    replacements = {
        "TITLE": escape(brief["position_name"]),
        "CONTENT": "\n".join(parts),
    }
    return re.sub(r"\{\{(TITLE|CONTENT)\}\}", lambda m: replacements[m[1]], template)


def render_handoff(data):
    """Short native-chat handoff; the host appends the real artifact link."""
    parts = overview(data, data["findings"])
    parts += [
        "The full HTML report contains every finding, supporting passage, "
        "next action and review limit. Open the report linked below.",
        "",
    ]
    return "\n".join(parts).rstrip() + "\n"
