#!/usr/bin/env python3
"""Render the review-setup decision surface as one self-contained HTML file.

Usage:
    python3 render_gate1.py --manifest manifest.json --families families.json \
        --gaps gap-report.json [--read-plan read-plan.json] \
        [--cost-note "estimate for selected worker"] \
        [--review-plan review-plan.json] [--review-cost-note "estimate"] \
        [--readback framework-readback.json] \
        --execution-mode python --assurance-note "named checks pending" \
        --out gate1.html

Inputs follow references/schemas.md. framework-readback.json is minimal:
    {"items": [{"lens": str, "issue_id": str, "question": str,
                "hit_rule": str, "materiality": str, "evidence_required": str}]}

Output is deterministic: same inputs give byte-identical HTML. No external
requests, no timestamps, no random ids. The page records nothing; the
orchestrator records the lawyer's reply as families.confirmed.json.
"""

import argparse
import html
import json
import posixpath
import sys

GATE_SENTENCE = (
    "Approval unlocks the sample run. A bare continue does not advance this gate."
)

GAP_TYPES = ["index-missing", "referenced-absent", "unreadable", "duplicate"]

CSS = """
:root {
  --bg: #f7f6f3;
  --card: #ffffff;
  --ink: #1c1c1a;
  --muted: #6b6b66;
  --line: #d9d7d0;
  --settled: #eef0ea;
  --settled-ink: #3d5238;
  --proposed: #fff3d6;
  --proposed-line: #c98a00;
  --proposed-ink: #7a5300;
  --badge: #e4e2db;
  --accent: #2b4a6f;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #191918;
    --card: #232321;
    --ink: #e8e6e1;
    --muted: #9b9a93;
    --line: #3a3936;
    --settled: #26301f;
    --settled-ink: #a8c49a;
    --proposed: #3a2f12;
    --proposed-line: #e0a11c;
    --proposed-ink: #f0c460;
    --badge: #33322f;
    --accent: #8fb4dd;
  }
  body { background: #191918; }
}
* { box-sizing: border-box; }
body {
  background: #f7f6f3;
  background: var(--bg);
  color: var(--ink);
  font: 15px/1.5 -apple-system, "Segoe UI", system-ui, sans-serif;
  margin: 0;
  padding: 0 16px 48px;
}
main { max-width: 960px; margin: 0 auto; }
header.strip {
  max-width: 960px; margin: 0 auto; padding: 20px 0 12px;
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
.family {
  background: var(--card); border: 1px solid var(--line); border-radius: 6px;
  padding: 14px 16px; margin: 0 0 14px;
}
.doc-id { color: var(--muted); font-family: ui-monospace, Menlo, monospace; font-size: 12px; }
.scroll { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: 14px; }
th, td { text-align: left; padding: 4px 12px 4px 0; border-bottom: 1px solid var(--line); vertical-align: top; }
th { color: var(--muted); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: .03em; }
tr:last-child td { border-bottom: none; }
.role { text-transform: capitalize; }
.edges { list-style: none; margin: 10px 0 0; padding: 0; }
.edge { border-left: 3px solid var(--settled-ink); background: var(--settled);
  color: var(--ink); border-radius: 0 4px 4px 0; padding: 6px 10px; margin: 6px 0; font-size: 14px; }
.edge .prov { font-size: 11px; text-transform: uppercase; letter-spacing: .05em; color: var(--settled-ink); margin-left: 6px; }
.edge.model { border-left: 3px solid var(--proposed-line); background: var(--proposed); }
.edge.model .prov { color: var(--proposed-ink); font-weight: 700; }
.edge blockquote {
  margin: 6px 0 0; padding: 4px 8px; border-left: 2px solid var(--proposed-line);
  font-style: italic; font-size: 13px; color: var(--ink);
}
.rel { font-weight: 600; }
.triage { display: block; margin-top: 10px; font-size: 13px; color: var(--muted); }
.orphans { font-size: 13px; color: var(--muted); }
.orphans ul { margin: 4px 0 0; padding-left: 18px; }
.gap-group { background: var(--card); border: 1px solid var(--line); border-radius: 6px; padding: 12px 16px; margin: 0 0 12px; }
.gap-group h3 .count { margin-left: 8px; }
.gap-group ul { margin: 6px 0 0; padding-left: 18px; }
.gap-group li { margin: 4px 0; }
.evidence { color: var(--muted); font-size: 13px; }
.note { background: var(--card); border: 1px solid var(--line); border-left: 4px solid var(--accent);
  border-radius: 4px; padding: 8px 12px; font-size: 14px; margin: 0 0 12px; }
footer.decide {
  max-width: 960px; margin: 32px auto 0; border-top: 2px solid var(--line); padding-top: 16px;
}
footer.decide p { margin: 6px 0; }
.small { font-size: 13px; color: var(--muted); }
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
        sys.exit(f"render_gate1: cannot read {kind} at {path}: {e}")
    for k in required_keys:
        if k not in data:
            sys.exit(f"render_gate1: {kind} missing key '{k}'")
    return data


def doc_label(doc_id, docs):
    """Display name for a doc id: title if the manifest carries one, else path basename."""
    d = docs.get(doc_id)
    if not d:
        return doc_id
    return d.get("title") or posixpath.basename(d.get("path", doc_id))


def proposed_edge(edge):
    return edge.get("provenance") == "model" or edge.get("evidence_source") in {
        "model-read",
        "image-read-human-confirmed",
    }


def render_family(fam, docs):
    out = []
    base_id = fam["family_id"]
    out.append('<article class="family">')
    out.append(
        f'<h3>{esc(doc_label(base_id, docs))} <span class="doc-id">{esc(base_id)}</span></h3>'
    )
    out.append(
        '<div class="scroll"><table><thead><tr>'
        "<th>Role</th><th>Document</th><th>Date</th><th>ID</th></tr></thead><tbody>"
    )
    members = sorted(
        fam.get("members", []), key=lambda m: (m.get("order", 0), m.get("id", ""))
    )
    for m in members:
        d = docs.get(m["id"], {})
        dated = d.get("dated") or ""
        out.append(
            f'<tr><td class="role">{esc(m.get("role", ""))}</td>'
            f"<td>{esc(doc_label(m['id'], docs))}</td>"
            f"<td>{esc(dated)}</td>"
            f'<td class="doc-id">{esc(m["id"])}</td></tr>'
        )
    out.append("</tbody></table></div>")
    edges = sorted(
        fam.get("edges", []),
        key=lambda e: (e.get("src", ""), e.get("dst", ""), e.get("relation", "")),
    )
    if edges:
        out.append('<ul class="edges">')
        for e in edges:
            proposed = proposed_edge(e)
            cls = "edge model" if proposed else "edge rule"
            origin = e.get("evidence_source") or e.get("provenance", "rule")
            prov = f"PROPOSED ({origin})" if proposed else "rule"
            out.append(
                f'<li class="{cls}">{esc(doc_label(e["src"], docs))} '
                f'<span class="rel">{esc(e["relation"])}</span> '
                f"{esc(doc_label(e['dst'], docs))}"
                f'<span class="prov">{prov}</span>'
            )
            if proposed:
                quote = e.get("quote", "")
                out.append(f"<blockquote>{esc(quote)}</blockquote>")
            out.append("</li>")
        out.append("</ul>")
    # Visual triage only. Checkbox state is not read or saved by anything.
    out.append(
        '<label class="triage"><input type="checkbox"> '
        "Looked at this family (visual aid only, not recorded)</label>"
    )
    out.append("</article>")
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
    out.append(
        '<div class="note">Approval covers the family map above AND these '
        "compiled instructions. Every worker in the run is judged by this table verbatim.</div>"
    )
    out.append(
        '<div class="scroll"><table><thead><tr>'
        "<th>Lens</th><th>Issue</th><th>Question</th><th>Hit rule</th>"
        "<th>Materiality</th><th>Evidence required</th></tr></thead><tbody>"
    )
    for it in items:
        out.append(
            f"<tr><td>{esc(it.get('lens', ''))}</td>"
            f"<td>{esc(it.get('issue_id', ''))}</td>"
            f"<td>{esc(it.get('question', ''))}</td>"
            f"<td>{esc(it.get('hit_rule', ''))}</td>"
            f"<td>{esc(it.get('materiality', ''))}</td>"
            f"<td>{esc(it.get('evidence_required', ''))}</td></tr>"
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
        '<div class="note">This is the frozen metadata read plan. Every planned '
        "ID must resolve through a validated checkpoint, a receipted regex bank, "
        "an explicitly approved deferred-policy lane, or a visible parked reason."
        "</div>"
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
        '<div class="note">This is the prospective issue-review dispatch. '
        "Every row becomes one isolated maker checkpoint and a failed job stays "
        "visible in that lens's parked lane. Approval applies only to this plan ID.</div>",
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


def build_html(
    manifest,
    families,
    gaps,
    readback,
    read_plan=None,
    cost_note=None,
    review_plan=None,
    review_cost_note=None,
    execution_mode=None,
    assurance_note=None,
):
    docs = {d["id"]: d for d in manifest.get("documents", [])}
    fams = sorted(families.get("families", []), key=lambda f: f.get("family_id", ""))
    orphans = sorted(families.get("orphans", []))
    entries = gaps.get("entries", [])
    n_files = manifest.get("counts", {}).get("files", len(docs))
    n_proposed = sum(1 for f in fams for e in f.get("edges", []) if proposed_edge(e))

    counts = [
        (plural(n_files, "file"), False),
        (plural(len(fams), "family").replace("familys", "families"), False),
        (plural(len(orphans), "orphan"), False),
        (plural(len(entries), "gap"), False),
        (
            plural(n_proposed, "proposed edge") + " awaiting confirmation",
            n_proposed > 0,
        ),
    ]
    count_html = "".join(
        f'<span class="count{" warn" if warn else ""}">{esc(c)}</span>'
        for c, warn in counts
    )

    parts = []
    parts.append("<!doctype html>")
    parts.append('<html lang="en"><head><meta charset="utf-8">')
    parts.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    parts.append("<title>Confirm the document-room structure</title>")
    parts.append(f"<style>{CSS}</style></head><body>")

    parts.append('<header class="strip">')
    parts.append(
        f"<h1>Confirm the room structure for {esc(manifest.get('root_label', 'data room'))}</h1>"
    )
    parts.append(f'<div class="counts">{count_html}</div>')
    parts.append(
        f'<p class="small"><b>Execution mode:</b> {esc(execution_mode)}. '
        f"<b>Assurance:</b> {esc(assurance_note)}</p>"
    )
    parts.append(f'<p class="gate-rule">{esc(GATE_SENTENCE)}</p>')
    parts.append("</header><main>")

    section = 0
    if read_plan is not None:
        section += 1
        parts.append('<section id="read-plan">')
        parts.append(f"<h2>{section}. Read plan and receipt</h2>")
        parts.append(render_read_plan(read_plan, cost_note))
        parts.append("</section>")

    if review_plan is not None:
        section += 1
        parts.append('<section id="review-plan">')
        parts.append(f"<h2>{section}. Prospective issue-review plan</h2>")
        parts.append(render_review_plan(review_plan, review_cost_note))
        parts.append("</section>")

    section += 1
    parts.append('<section id="family-map">')
    parts.append(f"<h2>{section}. Family map</h2>")
    parts.append(
        '<p class="small">Pure regex rule edges are grouped. Edges whose '
        "evidence came from a document reader or a model resolver are marked "
        "PROPOSED and show the quote they rest on.</p>"
    )
    for fam in fams:
        parts.append(render_family(fam, docs))
    if orphans:
        parts.append('<div class="orphans"><h3>Orphans (no family)</h3><ul>')
        for o in orphans:
            parts.append(
                f'<li>{esc(doc_label(o, docs))} <span class="doc-id">{esc(o)}</span></li>'
            )
        parts.append("</ul></div>")
    parts.append("</section>")

    section += 1
    parts.append('<section id="gap-report">')
    parts.append(f"<h2>{section}. Gap report</h2>")
    parts.append(render_gaps(entries))
    parts.append("</section>")

    if readback is not None:
        section += 1
        parts.append('<section id="checklist-readback">')
        parts.append(f"<h2>{section}. Checklist read-back</h2>")
        parts.append(render_readback(readback.get("items", [])))
        parts.append("</section>")

    parts.append("</main>")
    parts.append('<footer class="decide">')
    parts.append("<h2>Your decision</h2>")
    parts.append(
        "<p>Decisions are batched on this page. Reply in the conversation with one message that: "
        "confirms the family map as shown or regroups it (say which documents move where), "
        "rules on each PROPOSED edge, approves the checklist read-back, and "
        "approves or rejects the displayed review-plan ID and cost basis.</p>"
    )
    parts.append(
        "<p>Nothing on this page submits or saves anything. The orchestrating agent records "
        "your reply and writes families.confirmed.json; downstream stages read only that file.</p>"
    )
    parts.append(f'<p class="gate-rule">{esc(GATE_SENTENCE)}</p>')
    parts.append("</footer></body></html>")
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser(
        description="Render the review-setup decision surface."
    )
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--families", required=True)
    ap.add_argument("--gaps", required=True)
    ap.add_argument("--read-plan", default=None)
    ap.add_argument("--cost-note", default=None)
    ap.add_argument("--review-plan", default=None)
    ap.add_argument("--review-cost-note", default=None)
    ap.add_argument("--readback", default=None)
    ap.add_argument(
        "--execution-mode", required=True, choices=["python", "portable-fallback"]
    )
    ap.add_argument("--assurance-note", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    manifest = load(args.manifest, "manifest", ["documents", "counts"])
    families = load(args.families, "families", ["families"])
    gaps = load(args.gaps, "gap report", ["entries"])
    read_plan = (
        load(args.read_plan, "read plan", ["documents", "summary"])
        if args.read_plan
        else None
    )
    readback = load(args.readback, "readback", ["items"]) if args.readback else None
    review_plan = (
        load(args.review_plan, "review plan", ["jobs", "plan_id", "summary", "tier"])
        if args.review_plan
        else None
    )

    doc = build_html(
        manifest,
        families,
        gaps,
        readback,
        read_plan,
        args.cost_note,
        review_plan,
        args.review_cost_note,
        args.execution_mode,
        args.assurance_note,
    )
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
