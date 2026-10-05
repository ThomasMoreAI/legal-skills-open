#!/usr/bin/env python3
"""Render the plain-language review-setup surface as one self-contained HTML file.

Usage:
    python3 render_dmap.py --manifest manifest.json --messages messages.json \
        --clusters clusters.json --gaps gap-report.json \
        [--read-plan read-plan.json] [--cost-note "selected worker estimate"] \
        [--review-plan review-plan.json] [--review-cost-note "estimate"] \
        [--readback framework-readback.json --framework framework.json] \
        --document-root production --review-copies review-copies.json \
        --execution-mode python --assurance-note "named checks pending" \
        --out dmap.html

Inputs follow references/comms-schemas.md and references/shared/schemas.md.
framework-readback.json is minimal:
    {"items": [{"lens": str, "issue_id": str, "question": str,
                "hit_rule": str, "materiality": str, "evidence_required": str}]}

Output is deterministic: same inputs give byte-identical HTML. No external
requests, timestamps, or random ids. When complete binding inputs are present,
the page exports a deterministic approval receipt for fail-closed ingestion.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import importlib.util
import json
import sys
from pathlib import Path, PurePosixPath
from typing import Any


def load_shared_module(name, filename):
    candidate = Path(__file__).resolve().parent / "shared" / filename
    spec = importlib.util.spec_from_file_location(name, candidate)
    if spec is None or spec.loader is None:
        sys.exit(f"render_dmap: cannot load {filename} from {candidate}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


REVIEW_UI = load_shared_module("lq_setup_review_ui", "review_ui.py")
REVIEW_COPIES = load_shared_module("lq_setup_review_copies", "review_copies.py")
RENDER_READBACK = load_shared_module("lq_setup_render_readback", "render_readback.py")
BRAND_CSS = str(REVIEW_UI.BRAND_CSS)
CONTRACT_ID = str(REVIEW_UI.CONTRACT_ID)
THEME_JS = str(REVIEW_UI.THEME_JS)

APPROVAL_SENTENCE = (
    "Approval authorizes only the displayed test sample. It does not start from "
    "this offline page; return the downloaded receipt to the review task."
)

# Diligence enum plus the two comms types, rendered identically.
GAP_TYPES = [
    "index-missing",
    "referenced-absent",
    "unreadable",
    "duplicate",
    "custodian-gap",
    "thread-gap",
]

# Text-grid heat levels, low to high. Character density, not images.
HEAT_CHARS = ["·", "░", "▒", "▓", "█"]

CSS = """
:root {
  --bg: var(--lq-background);
  --card: var(--lq-surface);
  --ink: var(--lq-foreground);
  --muted: var(--lq-muted-foreground);
  --line: var(--lq-border);
  --settled: var(--lq-success-surface);
  --settled-ink: var(--lq-success);
  --proposed: var(--lq-attention-surface);
  --proposed-line: var(--lq-attention);
  --proposed-ink: var(--lq-attention);
  --badge: var(--lq-surface-muted);
  --accent: var(--lq-primary);
}
* { box-sizing: border-box; }
body {
  background: var(--bg);
  color: var(--ink);
  font: 15px/1.5 var(--lq-font-sans);
  margin: 0;
  padding: 0 0 48px;
}
main { max-width: 960px; margin: 0 auto; padding: 0 16px; }
header.strip {
  max-width: 960px; margin: 0 auto; padding: 20px 16px 12px;
  border-bottom: 2px solid var(--line);
}
h1 { font-size: 20px; margin: 0 0 8px; }
h2 { font-size: 17px; margin: 28px 0 10px; }
h3 { font-size: 15px; margin: 0 0 6px; }
.counts { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 10px; }
.count {
  background: var(--badge); border-radius: 4px; padding: 2px 10px;
  font-size: 13px; white-space: nowrap;
}
.count b { font-size: 14px; }
.count.warn { background: var(--proposed); color: var(--proposed-ink); border: 1px solid var(--proposed-line); }
.gate-rule { font-weight: 600; margin: 0; }
.panel {
  background: var(--card); border: 1px solid var(--line); border-radius: 6px;
  padding: 14px 16px; margin: 0 0 14px;
}
.doc-id { color: var(--muted); font-family: ui-monospace, Menlo, monospace; font-size: 12px; }
.scroll { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: 14px; }
th, td { text-align: left; padding: 4px 12px 4px 0; border-bottom: 1px solid var(--line); vertical-align: top; }
th { color: var(--muted); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: .03em; }
tr:last-child td { border-bottom: none; }
table.heatgrid { width: auto; }
table.heatgrid th, table.heatgrid td { border-bottom: none; padding: 2px 6px 2px 0; }
table.heatgrid th.month { font-size: 11px; }
td.heat {
  font-family: ui-monospace, Menlo, monospace; font-size: 15px;
  text-align: center; min-width: 26px; color: var(--accent);
}
td.heat.gapflag {
  background: var(--proposed); color: var(--proposed-ink);
  border: 1px solid var(--proposed-line); border-radius: 3px; font-weight: 700;
}
td.total { color: var(--muted); font-size: 13px; }
.gapnote { font-size: 13px; color: var(--proposed-ink); background: var(--proposed);
  border: 1px solid var(--proposed-line); border-radius: 4px; display: inline-block;
  padding: 1px 8px; margin: 4px 0 0; }
.legend { font-size: 12px; color: var(--muted); margin: 8px 0 0; }
.legend .heatchar { font-family: ui-monospace, Menlo, monospace; color: var(--accent); }
.gap-group { background: var(--card); border: 1px solid var(--line); border-radius: 6px; padding: 12px 16px; margin: 0 0 12px; }
.gap-group h3 .count { margin-left: 8px; }
.gap-group ul { margin: 6px 0 0; padding-left: 18px; }
.gap-group li { margin: 4px 0; }
.evidence { color: var(--muted); font-size: 13px; }
.note { background: var(--card); border: 1px solid var(--line); border-left: 4px solid var(--accent);
  border-radius: 4px; padding: 8px 12px; font-size: 14px; margin: 0 0 12px; }
.broken { border-left: 3px solid var(--proposed-line); background: var(--proposed);
  color: var(--ink); border-radius: 0 4px 4px 0; padding: 6px 10px; margin: 6px 0; font-size: 14px;
  list-style: none; }
.broken .prov { font-size: 11px; text-transform: uppercase; letter-spacing: .05em;
  color: var(--proposed-ink); font-weight: 700; margin-left: 6px; }
ul.brokens { margin: 10px 0 0; padding: 0; }
footer.decide {
  max-width: 960px; margin: 32px auto 0; border-top: 2px solid var(--line); padding-top: 16px;
}
footer.decide p { margin: 6px 0; }
.small { font-size: 13px; color: var(--muted); }
.eyebrow { color: var(--accent); font-size: 13px; font-weight: 700; margin: 0 0 5px; }
.lede { color: var(--muted); font-size: 16px; max-width: 720px; margin: 8px 0 18px; }
.flow { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--line); border: 1px solid var(--line); margin: 16px 0 20px; }
.flow div { background: var(--card); color: var(--muted); padding: 10px 12px; }
.flow div:first-child { box-shadow: inset 0 3px 0 var(--accent); color: var(--ink); }
.flow b { display: block; }
.decision { background: var(--card); border: 1px solid var(--line); border-radius: 6px; margin: 14px 0; padding: 16px; }
.decision h2 { margin: 0 0 4px; }
.decision-label { color: var(--accent); font-size: 12px; font-weight: 700; margin: 0 0 3px; text-transform: uppercase; letter-spacing: .04em; }
.question-list { margin: 12px 0 0; padding-left: 22px; }
.question-list li { margin: 10px 0; padding-left: 4px; }
.question-list details { margin-top: 4px; }
summary { cursor: pointer; color: var(--accent); font-weight: 600; }
.metrics { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin: 14px 0; }
.metric { background: var(--settled); padding: 10px 12px; }
.metric b { display: block; font-size: 18px; }
.warning { background: var(--proposed); border: 1px solid var(--proposed-line); color: var(--proposed-ink); padding: 10px 12px; margin: 12px 0; }
.sample-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 12px; }
.sample-grid ul { margin: 0; padding-left: 20px; }
.scope-box { background: var(--settled); padding: 12px; }
.scope-box b { display: block; margin-bottom: 3px; }
.approve-box { border: 2px solid var(--accent); background: var(--card); border-radius: 6px; padding: 16px; margin: 18px 0; }
.approve-box h2 { margin: 0 0 6px; }
.confirm-row { display: flex; gap: 9px; align-items: flex-start; margin: 14px 0; }
.confirm-row input { margin-top: 4px; }
button { border: 1px solid var(--accent); border-radius: 4px; background: var(--accent); color: var(--lq-primary-foreground); cursor: pointer; font: inherit; font-weight: 500; padding: 9px 13px; }
button:disabled { cursor: not-allowed; opacity: .45; }
.approval-result { color: var(--settled-ink); font-weight: 600; margin: 10px 0 0; }
button:focus-visible,input:focus-visible,summary:focus-visible { outline: 2px solid var(--lq-ring); outline-offset: 2px; }
#technical-receipts { border-top: 1px solid var(--line); margin-top: 24px; padding-top: 14px; }
#technical-receipts > summary { font-size: 15px; }
@media (max-width: 680px) {
  .flow, .metrics, .sample-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 420px) {
  body { padding-left: 10px; padding-right: 10px; }
  .flow, .metrics, .sample-grid { grid-template-columns: 1fr; }
  .decision, .approve-box { padding: 13px; }
}
"""


def esc(s):
    return html.escape(str(s), quote=True)


def plural(n, word):
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def load(path, kind, required_keys):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"render_dmap: cannot read {kind} at {path}: {e}")
    for k in required_keys:
        if k not in data:
            sys.exit(f"render_dmap: {kind} missing key '{k}'")
    return data


def canonical_digest(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def approval_bindings(manifest, framework, clusters, read_plan, review_plan):
    jobs = review_plan.get("jobs", [])
    issue_ids = sorted(
        {
            issue_id
            for job in jobs
            for issue_id in job.get("issue_ids", [])
            if isinstance(issue_id, str)
        }
    )
    unit_ids = sorted(
        {job.get("unit_id") for job in jobs if isinstance(job.get("unit_id"), str)}
    )
    return {
        "approval_source": "offline-export",
        "approved_by": "lawyer",
        "artifact": "review-setup-approval",
        "authorization": "sample-only",
        "clusters_digest": canonical_digest(clusters),
        "corpus_id": manifest.get("corpus_id"),
        "decisions": {
            "collection_coverage_confirmed": True,
            "metadata_policy_confirmed": True,
            "review_questions_confirmed": True,
            "sample_confirmed": True,
        },
        "framework_digest": canonical_digest(framework),
        "issue_ids": issue_ids,
        "manifest_digest": canonical_digest(manifest),
        "read_plan_digest": canonical_digest(read_plan),
        "read_plan_id": read_plan.get("plan_id"),
        "review_plan_digest": canonical_digest(review_plan),
        "review_plan_id": review_plan.get("plan_id"),
        "unit_ids": unit_ids,
        "version": 1,
    }


def heat_char(count, top):
    """Density character for a count against the custodian's busiest month."""
    if count <= 0:
        return HEAT_CHARS[0]
    if top <= 0:
        return HEAT_CHARS[-1]
    idx = 1 + min(3, (count * 4 - 1) // top)  # buckets 1..4 for counts 1..top
    return HEAT_CHARS[idx]


def custodian_gap_months(custodian, months, entries):
    """Zero-count months this custodian is named for in a custodian-gap entry.

    The entry detail names custodian and month; neighboring months appear in
    the detail too, so only months with a zero count qualify (the contract
    defines a custodian-gap as a zero month between populated neighbors).
    """
    flagged = set()
    for e in entries:
        if e.get("type") != "custodian-gap":
            continue
        detail = e.get("detail", "")
        if custodian in detail:
            for tok in detail.replace(";", " ").replace(",", " ").split():
                tok = tok.strip(".")
                if (
                    len(tok) == 7
                    and tok[4] == "-"
                    and tok[:4].isdigit()
                    and tok[5:].isdigit()
                    and months.get(tok, 0) == 0
                ):
                    flagged.add(tok)
    return flagged


def render_custodians(custodian_months, entries):
    out = []
    all_months = sorted({m for months in custodian_months.values() for m in months})
    out.append('<div class="panel"><div class="scroll">')
    out.append('<table class="heatgrid"><thead><tr><th>Custodian</th>')
    for m in all_months:
        out.append(f'<th class="month">{esc(m)}</th>')
    out.append("<th>Total</th></tr></thead><tbody>")
    for cust in sorted(custodian_months):
        months = custodian_months[cust]
        top = max(months.values(), default=0)
        gaps = custodian_gap_months(cust, months, entries)
        cells = []
        for m in all_months:
            n = months.get(m, 0)
            if m in gaps:
                cells.append(
                    f'<td class="heat gapflag" title="{esc(cust)} {esc(m)}: '
                    f'{n} messages (custodian-gap)">0</td>'
                )
            else:
                cells.append(
                    f'<td class="heat" title="{esc(cust)} {esc(m)}: '
                    f'{n} messages">{heat_char(n, top)}</td>'
                )
        total = sum(months.values())
        row = f"<tr><td>{esc(cust)}</td>{''.join(cells)}<td class='total'>{total}</td></tr>"
        out.append(row)
        if gaps:
            span = len(all_months) + 2
            flags = ", ".join(f"{m} (custodian-gap)" for m in sorted(gaps))
            out.append(
                f'<tr><td colspan="{span}"><span class="gapnote">'
                f"{esc(cust)} gap months: {esc(flags)}</span></td></tr>"
            )
    out.append("</tbody></table></div>")
    scale = " ".join(f'<span class="heatchar">{c}</span>' for c in HEAT_CHARS)
    out.append(
        f'<p class="legend">Scale per custodian row, zero to busiest month: {scale}. '
        "Highlighted cells are custodian-gap months from the gap report. "
        "Hover any cell for the exact count.</p></div>"
    )
    return "\n".join(out)


def channel_span(channel, messages):
    dates = sorted(
        messages[member]["date"][:10]
        for member in channel.get("members", [])
        if member in messages and isinstance(messages[member].get("date"), str)
    )
    if not dates:
        return ""
    return dates[0] if dates[0] == dates[-1] else f"{dates[0]} to {dates[-1]}"


def render_channels(channels, messages):
    out = []
    out.append(
        '<div class="panel"><div class="scroll"><table><thead><tr>'
        "<th>Channel</th><th>Participants</th><th>Count</th><th>Date span</th>"
        "</tr></thead><tbody>"
    )
    ordered = sorted(
        channels,
        key=lambda channel: (
            -(channel.get("basis") or {}).get("occurrences", 0),
            channel.get("cluster_id", ""),
        ),
    )
    for c in ordered:
        basis = c.get("basis") or {}
        parts = ", ".join(sorted(basis.get("participants", [])))
        out.append(
            f'<tr><td class="doc-id">{esc(c.get("cluster_id", ""))}</td>'
            f"<td>{esc(parts)}</td>"
            f"<td>{basis.get('occurrences', len(c.get('members', [])))}</td>"
            f"<td>{esc(channel_span(c, messages))}</td></tr>"
        )
    out.append("</tbody></table></div></div>")
    return "\n".join(out)


def render_threads(threads, entries):
    out = []
    broken = [e for e in entries if e.get("type") == "thread-gap"]
    out.append('<div class="panel">')
    out.append(
        f"<p>{esc(plural(len(threads), 'thread'))} assembled; "
        f"{esc(plural(len(broken), 'broken thread'))}.</p>"
    )
    if broken:
        out.append('<ul class="brokens">')
        for e in sorted(broken, key=lambda x: x.get("detail", "")):
            out.append(
                f'<li class="broken">{esc(e.get("detail", ""))}'
                '<span class="prov">thread-gap</span>'
                f'<div class="evidence">Evidence: {esc(e.get("evidence", ""))}</div></li>'
            )
        out.append("</ul>")
    else:
        out.append('<p class="small">No broken threads.</p>')
    out.append("</div>")
    return "\n".join(out)


def render_gaps(entries):
    out = []
    grouped = {}
    for e in entries:
        grouped.setdefault(e.get("type", "other"), []).append(e)
    order = GAP_TYPES + sorted(k for k in grouped if k not in GAP_TYPES)
    for t in order:
        items = grouped.get(t, [])
        if not items:
            continue
        out.append('<div class="gap-group">')
        out.append(f'<h3>{esc(t)}<span class="count"><b>{len(items)}</b></span></h3>')
        out.append("<ul>")
        for e in items:
            out.append(
                f"<li>{esc(e.get('detail', ''))}"
                f'<div class="evidence">Evidence: {esc(e.get("evidence", ""))}</div></li>'
            )
        out.append("</ul></div>")
    if not out:
        out.append('<p class="small">No gaps reported.</p>')
    return "\n".join(out)


def render_readback(items):
    out = []
    has_targets = any("target" in item for item in items)
    out.append(
        '<div class="note">These are the exact instructions retained in the '
        "audit record for the sample review.</div>"
    )
    out.append(
        '<div class="scroll"><table><thead><tr>'
        "<th>Lens</th><th>Issue</th>"
        + ("<th>Target</th>" if has_targets else "")
        + "<th>Question</th><th>Hit rule</th>"
        "<th>Materiality</th><th>Evidence required</th></tr></thead><tbody>"
    )
    for it in items:
        out.append(
            f"<tr><td>{esc(it.get('lens', ''))}</td>"
            f"<td>{esc(it.get('issue_id', ''))}</td>"
            + (f"<td>{esc(it.get('target', ''))}</td>" if has_targets else "")
            + f"<td>{esc(it.get('question', ''))}</td>"
            f"<td>{esc(it.get('hit_rule', ''))}</td>"
            f"<td>{esc(it.get('materiality', ''))}</td>"
            f"<td>{esc(it.get('evidence_required', ''))}</td></tr>"
        )
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render_instrument_coverage(readback):
    coverage = readback.get("instrument_coverage", [])
    totals = readback.get("census_totals", {})
    out = [
        '<div class="counts">',
        f'<span class="count"><b>{esc(totals.get("elements", 0))}</b> elements</span>',
        f'<span class="count"><b>{esc(totals.get("covered", 0))}</b> covered</span>',
        f'<span class="count"><b>{esc(totals.get("staged_elements", 0))}</b> staged</span>',
        "</div>",
    ]
    by_kind = totals.get("by_kind", {})
    if by_kind:
        out.append(
            '<p class="small">Per-kind totals: '
            + "; ".join(
                f"{esc(kind.upper())} {esc(by_kind[kind])}" for kind in sorted(by_kind)
            )
            + ".</p>"
        )
    out.append(
        '<div class="scroll"><table><thead><tr><th>Kind</th><th>Instrument</th>'
        "<th>Label</th><th>Elements</th><th>Items covering</th><th>State</th>"
        "</tr></thead><tbody>"
    )
    for row in coverage:
        out.append(
            f"<tr><td>{esc(str(row.get('kind', '')).upper())}</td>"
            f'<td class="doc-id">{esc(row.get("instrument_id", ""))}</td>'
            f"<td>{esc(row.get('label', ''))}</td>"
            f"<td>{esc(row.get('element_count', 0))}</td>"
            f"<td>{esc(row.get('covered', 0))}</td>"
            f"<td>{'staged' if row.get('staged') else 'compiled'}</td></tr>"
        )
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render_read_plan(read_plan, cost_note):
    summary = read_plan.get("summary", {})
    dispositions = summary.get("dispositions", {})
    estimate = summary.get("estimated_input_tokens")
    if not isinstance(estimate, int):
        chars = summary.get("estimated_text_chars", 0)
        estimate = (chars + 3) // 4 if isinstance(chars, int) else 0
    rows = [
        ("Fresh isolated readers", dispositions.get("reader-required", 0)),
        ("Regex audit readers", dispositions.get("regex-audit", 0)),
        ("Receipted regex bank", dispositions.get("regex-banked", 0)),
        ("Deferred to review", dispositions.get("deferred-to-review", 0)),
        ("Parked unreadable", dispositions.get("parked-unreadable", 0)),
    ]
    out = [
        '<div class="note">Non-message documents use the shared isolated '
        "reader loop. Every planned ID must resolve through a validated checkpoint, "
        "a receipted regex bank, an explicitly approved deferred-policy lane, or a "
        "visible parked reason.</div>"
    ]
    out.append(
        '<div class="scroll"><table><thead><tr><th>Lane</th><th>Documents</th>'
        "</tr></thead><tbody>"
    )
    for label, count in rows:
        out.append(f"<tr><td>{esc(label)}</td><td>{esc(count)}</td></tr>")
    out.append("</tbody></table></div>")
    if dispositions.get("deferred-to-review", 0):
        out.append(
            '<p class="small">Deferred documents get no standalone metadata '
            "read or canonical titles/parties/dates inventory; each is read in full "
            "by the frame-aware review pass. Review coverage and privilege discipline "
            "are unchanged, and metadata reads can be ordered later by rerunning prep "
            "without deferral. Approving this surface approves the deferral.</p>"
        )
    out.append(
        f'<p class="small">Estimated metadata-reader input: about '
        f"{estimate:,} tokens from extracted text, before instructions and output. "
        "This is not the later issue-review cost.</p>"
    )
    out.append(
        f'<p class="small">Stable metadata plan ID: '
        f"{esc(read_plan.get('plan_id', 'not recorded'))}</p>"
    )
    default_cost = (
        "not calculated until the lawyer or host selects the worker model "
        "and current pricing"
    )
    out.append(f'<p class="small">Cost basis: {esc(cost_note or default_cost)}</p>')
    return "\n".join(out)


def render_review_plan(review_plan, cost_note):
    summary = review_plan.get("summary", {})
    rows = [
        ("Tier", review_plan.get("tier", "")),
        ("Stable plan ID", review_plan.get("plan_id", "")),
        ("Fresh unit/lens makers", summary.get("jobs", 0)),
        ("Unique units", summary.get("unique_units", 0)),
        ("Parked before dispatch", summary.get("parked_units", 0)),
        ("Estimated text input tokens", summary.get("estimated_input_tokens", 0)),
        ("Estimated image pages", summary.get("estimated_image_pages", 0)),
        (
            "Image documents with unknown pages",
            summary.get("unknown_image_documents", 0),
        ),
    ]
    out = [
        '<div class="note">This prospective issue-review dispatch creates one '
        "isolated maker checkpoint per unit and lens. Approval applies only to "
        "the displayed plan ID.</div>",
        '<div class="scroll"><table><thead><tr><th>Review plan</th><th>Value</th>'
        "</tr></thead><tbody>",
    ]
    for label, value in rows:
        out.append(f"<tr><td>{esc(label)}</td><td>{esc(value)}</td></tr>")
    out.append("</tbody></table></div>")
    default_cost = (
        "not calculated until the lawyer or host selects the worker model "
        "and current pricing"
    )
    out.append(
        f'<p class="small">Issue-review cost basis: {esc(cost_note or default_cost)}</p>'
    )
    out.append(
        '<p class="small">Current receipt: '
        + (
            "lawyer-approved"
            if review_plan.get("approved") is True
            else "not yet approved"
        )
        + ".</p>"
    )
    return "\n".join(out)


def render_questions(items):
    if not items:
        return '<p class="small">No review questions were supplied.</p>'
    out = ['<ol class="question-list">']
    for item in items:
        target = item.get("target") or item.get("issue_id", "")
        materiality = str(item.get("materiality", "")).replace(
            "tune during sample review", "can be adjusted after the sample"
        )
        out.append(f"<li><b>{esc(target)}</b>: {esc(item.get('question', ''))}")
        out.append("<details><summary>What counts as a match</summary>")
        out.append(
            f"<p><b>Match rule:</b> {esc(item.get('hit_rule', ''))}<br>"
            f"<b>Importance:</b> {esc(materiality)}<br>"
            f"<b>Proof required:</b> {esc(item.get('evidence_required', ''))}</p>"
        )
        out.append("</details></li>")
    out.append("</ol>")
    return "\n".join(out)


def message_date_span(messages):
    dates = sorted(
        value[:10]
        for message in messages.values()
        for value in [message.get("date_local") or message.get("date")]
        if isinstance(value, str) and len(value) >= 10
    )
    if not dates:
        return "Not available"
    return dates[0] if dates[0] == dates[-1] else f"{dates[0]} to {dates[-1]}"


def unit_labels(review_plan, manifest, messages, clusters):
    if review_plan is None:
        return []
    docs = {}
    for document in sorted(
        manifest.get("documents", []),
        key=lambda item: (item.get("id", ""), item.get("path", "")),
    ):
        docs.setdefault(document.get("id"), document)
    threads = {
        thread.get("cluster_id"): thread
        for thread in clusters.get("threads", [])
        if isinstance(thread.get("cluster_id"), str)
    }
    labels = []
    seen = set()
    for job in sorted(
        review_plan.get("jobs", []), key=lambda item: item.get("unit_id", "")
    ):
        unit_id = job.get("unit_id")
        if not isinstance(unit_id, str) or unit_id in seen:
            continue
        seen.add(unit_id)
        subjects = []
        member_ids = job.get("member_ids", [])
        if unit_id in threads:
            member_ids = threads[unit_id].get("members", member_ids)
        for doc_id in member_ids:
            subject = messages.get(doc_id, {}).get("subject")
            if isinstance(subject, str) and subject.strip() and subject not in subjects:
                subjects.append(subject.strip())
        if subjects:
            label = subjects[0] if len(subjects) == 1 else f"{subjects[0]} conversation"
        else:
            paths = [
                docs[doc_id].get("path", "") for doc_id in member_ids if doc_id in docs
            ]
            label = PurePosixPath(paths[0]).name if paths else unit_id
        labels.append((unit_id, label))
    return labels


def render_review_copy_status(review_validation):
    documents = review_validation.sidecar["documents"]
    blocked = [item for item in documents if item["status"] != "ready"]
    ready = len(documents) - len(blocked)
    out = [
        '<section class="decision" id="review-copy-status">',
        "<h2>Are the documents ready to review?</h2>",
        f'<p class="small"><b>{ready} of {len(documents)}</b> source files have '
        "verified in-page review copies.</p>",
    ]
    if blocked:
        out.append(
            '<div class="warning" role="alert"><b>Approval is locked.</b> Every '
            "document in this collection needs a verified review copy before the "
            "test can be approved.</div><ul>"
        )
        for item in blocked:
            out.append(
                f"<li><b>{esc(item['path'])}</b> — Needs rendering: "
                f"{esc(item['reason'])}</li>"
            )
        out.append("</ul>")
    else:
        out.append(
            '<p class="small">Every source is covered by the current hash-bound '
            "review-copy receipt.</p>"
        )
    out.append("</section>")
    return "".join(out)


def build_html(
    manifest,
    framework,
    messages_doc,
    clusters,
    gaps,
    readback,
    read_plan=None,
    cost_note=None,
    review_plan=None,
    review_cost_note=None,
    execution_mode=None,
    assurance_note=None,
    review_validation: Any = None,
):
    if review_validation is None or review_validation.sidecar is None:
        raise ValueError("review-copy validation receipt is required")
    messages = messages_doc.get("messages", {})
    entries = gaps.get("entries", [])
    threads = clusters.get("threads", [])
    channels = clusters.get("channels", [])
    custodian_months = clusters.get("custodian_months", {})
    n_files = manifest.get("counts", {}).get(
        "files", len(manifest.get("documents", []))
    )
    unique_records = len({doc.get("id") for doc in manifest.get("documents", [])})
    duplicates = sum(1 for entry in entries if entry.get("type") == "duplicate")
    unreadable = sum(1 for entry in entries if entry.get("type") == "unreadable")
    actionable_gaps = sum(1 for entry in entries if entry.get("type") != "duplicate")
    readback_items = readback.get("items", []) if readback is not None else []
    sample_labels = unit_labels(review_plan, manifest, messages, clusters)
    actionable = all(
        value is not None for value in (framework, read_plan, review_plan, readback)
    )
    review_ready = review_validation.ready
    bindings = (
        approval_bindings(manifest, framework, clusters, read_plan, review_plan)
        if actionable and review_ready
        else None
    )

    parts = []
    parts.append("<!doctype html>")
    parts.append(
        f'<html lang="en" data-review-ui-contract="{esc(CONTRACT_ID)}"><head><meta charset="utf-8">'
    )
    parts.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    parts.append("<title>Confirm your review setup</title>")
    parts.append(f"<style>{BRAND_CSS}{CSS}</style></head><body>")
    parts.append(REVIEW_UI.masthead(esc("Review setup")))

    parts.append('<header class="strip">')
    parts.append('<p class="eyebrow">Set up the review</p>')
    parts.append("<h1>Confirm what we should look for</h1>")
    parts.append(
        '<p class="lede">Before any document review begins, check the review '
        "questions, the collection we received, and the small test sample. You can "
        "change any of them now.</p>"
    )
    parts.append(
        '<nav class="flow" aria-label="Review progress">'
        "<div><b>1 · Set up</b>Confirm the rules</div>"
        "<div><b>2 · Test sample</b>Review a small set</div>"
        "<div><b>3 · Full review</b>Only after approval</div>"
        "<div><b>4 · Final decisions</b>Lawyer rulings</div></nav>"
    )
    parts.append("</header><main>")
    parts.append(render_review_copy_status(review_validation))

    if unreadable:
        parts.append(
            f'<div class="warning" role="alert"><b>{esc(plural(unreadable, "file"))} '
            "could not be read.</b> It will remain in Needs attention and will not "
            "be treated as nonresponsive. Approval stays locked until it is rendered "
            "or repaired.</div>"
        )

    parts.append('<section class="decision" id="review-questions">')
    parts.append('<p class="decision-label">Decision 1 of 3</p>')
    parts.append("<h2>Are these the right review questions?</h2>")
    parts.append(
        '<p class="small">Every document in the test will be checked against each '
        "question below.</p>"
    )
    parts.append(render_questions(readback_items))
    parts.append("</section>")

    parts.append('<section class="decision" id="collection-coverage">')
    parts.append('<p class="decision-label">Decision 2 of 3</p>')
    parts.append("<h2>Does this look like the collection you expected?</h2>")
    parts.append(
        '<p class="small">You are confirming the visible coverage for this test, '
        "not certifying that the legal collection is complete.</p>"
    )
    parts.append('<div class="metrics">')
    parts.append(f'<div class="metric"><b>{n_files}</b>source files</div>')
    parts.append(f'<div class="metric"><b>{unique_records}</b>unique records</div>')
    parts.append(f'<div class="metric"><b>{len(custodian_months)}</b>custodians</div>')
    parts.append(
        f'<div class="metric"><b>{esc(message_date_span(messages))}</b>message dates</div>'
    )
    parts.append("</div>")
    parts.append(
        f"<p>{esc(plural(duplicates, 'duplicate'))} accounted for; "
        f"{esc(plural(actionable_gaps, 'item'))} may need attention.</p>"
    )
    if read_plan is not None:
        dispositions = read_plan.get("summary", {}).get("dispositions", {})
        deferred = dispositions.get("deferred-to-review", 0)
        if deferred:
            parts.append(
                f"<p><b>{esc(plural(deferred, 'standalone file'))} will be read "
                "during the legal review rather than in a separate metadata pass.</b> "
                "This avoids a duplicate read; review coverage and privilege handling "
                "do not change.</p>"
            )
    parts.append(
        "<details><summary>Review custodians, dates, and missing areas</summary>"
    )
    parts.append(render_custodians(custodian_months, entries))
    parts.append(render_gaps(entries))
    parts.append("</details>")
    parts.append(
        "<details><summary>How email conversations were grouped</summary>"
        '<p class="small">Related messages were grouped using subjects and reply '
        "headers. Recurring participant groups are supporting context; you are not "
        "being asked to approve an algorithm.</p>"
    )
    parts.append(render_threads(threads, entries))
    parts.append(render_channels(channels, messages))
    parts.append("</details></section>")

    parts.append('<section class="decision" id="sample-selection">')
    parts.append('<p class="decision-label">Decision 3 of 3</p>')
    parts.append("<h2>Is this a useful test sample?</h2>")
    parts.append(
        '<p class="small">The test is intended to expose obvious matches, overlap, '
        "ambiguous material, and possible privilege before any full review.</p>"
    )
    parts.append('<div class="sample-grid"><ul>')
    if sample_labels:
        for _unit_id, label in sample_labels:
            parts.append(f"<li>{esc(label)}</li>")
    else:
        parts.append("<li>No sample has been selected.</li>")
    parts.append('</ul><div class="scope-box">')
    parts.append(
        "<b>What approving this does</b>Authorizes review of only the listed test "
        "groups against the questions above."
    )
    parts.append(
        "<br><br><b>What it does not do</b>It does not approve the full review, "
        "responsiveness decisions, privilege rulings, production, or anything sent "
        "to opposing counsel."
    )
    parts.append("</div></div></section>")

    if actionable:
        parts.append('<section class="approve-box" aria-labelledby="approve-title">')
        parts.append('<h2 id="approve-title">Ready to run the test?</h2>')
        parts.append(
            '<p class="small">This offline page will download a bound approval receipt. '
            "Return that file to the review task to begin; clicking here does not "
            "itself start model review.</p>"
        )
        parts.append('<div class="confirm-row">')
        approval_disabled = ' disabled aria-disabled="true"' if not review_ready else ""
        parts.append(
            f'<input id="approval-confirm" type="checkbox"{approval_disabled}>'
        )
        parts.append(
            '<label for="approval-confirm">I confirm the review questions, collection '
            "coverage, standalone-file handling, and test sample are appropriate for "
            "this sample-only run.</label></div>"
        )
        parts.append(
            '<button id="download-approval" type="button" disabled aria-disabled="true">'
            "Approve and download run instructions</button>"
        )
        if not review_ready:
            parts.append(
                '<p class="warning" role="alert">Approval remains unavailable until '
                "every source has a verified review copy.</p>"
            )
        parts.append(
            '<p id="approval-result" class="approval-result" aria-live="polite"></p>'
        )
        parts.append(f'<p class="small">{esc(APPROVAL_SENTENCE)}</p></section>')

    parts.append('<details id="technical-receipts">')
    parts.append("<summary>Technical receipts and reproducibility details</summary>")
    parts.append(
        f'<p class="small"><b>Execution mode:</b> {esc(execution_mode)}. '
        f"<b>Assurance:</b> {esc(assurance_note)}. "
        f"<b>Corpus:</b> {esc(manifest.get('corpus_id', 'not recorded'))}</p>"
    )
    parts.append(
        f'<p class="small"><b>Review-copy receipt:</b> {esc(review_validation.sidecar["digest"])}. '
        f"<b>Status:</b> {esc(review_validation.sidecar['status'])}.</p>"
    )
    if read_plan is not None:
        parts.append('<section id="read-plan">')
        parts.append("<h2>Metadata handling receipt</h2>")
        parts.append(render_read_plan(read_plan, cost_note))
        parts.append("</section>")
    if review_plan is not None:
        parts.append('<section id="review-plan">')
        parts.append("<h2>Sample dispatch receipt</h2>")
        parts.append(render_review_plan(review_plan, review_cost_note))
        parts.append("</section>")
    if readback is not None and readback.get("instrument_coverage") is not None:
        parts.append('<section id="instrument-coverage">')
        parts.append("<h2>Instrument census &amp; coverage</h2>")
        parts.append(render_instrument_coverage(readback))
        parts.append("</section>")
    if readback is not None:
        parts.append('<section id="framework-readback">')
        parts.append("<h2>Exact review-instruction receipt</h2>")
        parts.append(render_readback(readback_items))
        parts.append("</section>")
    parts.append("</details></main>")

    if bindings is not None:
        payload = json.dumps(bindings, sort_keys=True, separators=(",", ":"))
        parts.append("<script>")
        parts.append(f"const REVIEW_SETUP_APPROVAL={payload};")
        parts.append(
            "const approvalConfirm=document.getElementById('approval-confirm');"
            "const approvalButton=document.getElementById('download-approval');"
            "const approvalResult=document.getElementById('approval-result');"
            "approvalConfirm.addEventListener('change',()=>{"
            "approvalButton.disabled=!approvalConfirm.checked;"
            "approvalResult.textContent='';});"
            "approvalButton.addEventListener('click',()=>{"
            "const body=JSON.stringify(REVIEW_SETUP_APPROVAL,null,2)+'\\n';"
            "const url=URL.createObjectURL(new Blob([body],{type:'application/json'}));"
            "const link=document.createElement('a');link.href=url;"
            "link.download='review-setup-approval.json';link.click();"
            "URL.revokeObjectURL(url);"
            "approvalResult.textContent='Approval file downloaded. Return it to the review task to begin. No review has started from this page.';});"
        )
        parts.append("</script>")
    parts.append(f"<script>{THEME_JS}</script>")
    parts.append("</body></html>")
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Render the disclosure map HTML surface.")
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--messages", required=True)
    ap.add_argument("--clusters", required=True)
    ap.add_argument("--gaps", required=True)
    ap.add_argument("--read-plan", default=None)
    ap.add_argument("--cost-note", default=None)
    ap.add_argument("--review-plan", default=None)
    ap.add_argument("--review-cost-note", default=None)
    ap.add_argument("--readback", default=None)
    ap.add_argument(
        "--framework",
        default=None,
        help="validated framework that the displayed readback must exactly derive from",
    )
    ap.add_argument(
        "--document-root",
        required=True,
        help="root containing the source paths listed in the manifest",
    )
    ap.add_argument(
        "--review-copies",
        required=True,
        help="hash-bound review-copy sidecar alongside --out",
    )
    ap.add_argument(
        "--execution-mode", required=True, choices=["python", "portable-fallback"]
    )
    ap.add_argument("--assurance-note", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    output_path = Path(args.out).expanduser().absolute().resolve()
    input_paths = {
        Path(value).expanduser().absolute().resolve()
        for value in (
            args.manifest,
            args.messages,
            args.clusters,
            args.gaps,
            args.read_plan,
            args.review_plan,
            args.readback,
            args.framework,
            args.review_copies,
        )
        if value
    }
    if output_path in input_paths:
        sys.exit("render_dmap: --out must be a distinct new artifact path")
    sidecar_path = Path(args.review_copies).expanduser().absolute()
    if sidecar_path.parent.resolve() != output_path.parent:
        sys.exit(
            "render_dmap: --review-copies must be alongside --out so relative "
            "review-copy links stay valid"
        )
    review_validation = REVIEW_COPIES.revalidate_review_copies(
        sidecar_path,
        args.manifest,
        args.document_root,
    )
    if not review_validation.integrity_ok:
        detail = "; ".join(review_validation.errors[:4])
        sys.exit(f"render_dmap: review-copy validation failed: {detail}")

    manifest = load(args.manifest, "manifest", ["documents", "counts"])
    document_root = Path(args.document_root).expanduser().resolve()
    for row in manifest["documents"]:
        raw_path = row.get("path") if isinstance(row, dict) else None
        if not isinstance(raw_path, str) or not raw_path:
            continue
        relative = Path(raw_path)
        if relative.is_absolute():
            sys.exit(
                f"render_dmap: manifest document path must be relative: {raw_path}"
            )
        source = (document_root / relative).resolve()
        try:
            source.relative_to(document_root)
        except ValueError:
            sys.exit(f"render_dmap: manifest document path escapes root: {raw_path}")
        if source == output_path:
            sys.exit("render_dmap: --out must not overwrite a manifest source document")
    messages_doc = load(args.messages, "messages", ["messages"])
    clusters = load(
        args.clusters, "clusters", ["threads", "channels", "custodian_months"]
    )
    gaps = load(args.gaps, "gap report", ["entries"])
    read_plan = (
        load(args.read_plan, "read plan", ["documents", "summary"])
        if args.read_plan
        else None
    )
    readback = load(args.readback, "readback", ["items"]) if args.readback else None
    framework = (
        load(
            args.framework,
            "framework",
            ["framework_version", "approved", "source_inputs", "lenses"],
        )
        if args.framework
        else None
    )
    review_plan = (
        load(args.review_plan, "review plan", ["jobs", "plan_id", "summary", "tier"])
        if args.review_plan
        else None
    )
    if (readback is not None or review_plan is not None) and framework is None:
        sys.exit(
            "render_dmap: --framework is required with --readback or --review-plan"
        )
    if framework is not None:
        schema = RENDER_READBACK.validate_framework.load_json(
            RENDER_READBACK.validate_framework.DEFAULT_SCHEMA,
            "schema",
        )
        errors, _unknown = RENDER_READBACK.validate_framework.validate(
            framework,
            schema,
            allow_approved=True,
        )
        if errors:
            sys.exit("render_dmap: framework is invalid: " + "; ".join(errors[:4]))
        if readback is not None and readback != RENDER_READBACK.build_readback(
            framework
        ):
            sys.exit(
                "render_dmap: framework readback drift; regenerate it from the "
                "current framework"
            )
        if review_plan is not None:
            framework_digest = canonical_digest(framework)
            if review_plan.get("framework_digest") != framework_digest:
                sys.exit("render_dmap: review plan framework digest drift")
            if review_plan.get("framework_version") != framework.get(
                "framework_version"
            ):
                sys.exit("render_dmap: review plan framework version drift")

    doc = build_html(
        manifest,
        framework,
        messages_doc,
        clusters,
        gaps,
        readback,
        read_plan,
        args.cost_note,
        review_plan,
        args.review_cost_note,
        args.execution_mode,
        args.assurance_note,
        review_validation,
    )
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
