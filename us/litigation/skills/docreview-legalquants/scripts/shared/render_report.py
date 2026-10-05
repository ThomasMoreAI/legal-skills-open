#!/usr/bin/env python3
"""Render the final findings report as one self-contained HTML file.

Usage:
    python3 render_report.py --framework framework.json --findings findings.json \
        --manifest manifest.json --families families.json --gaps gap-report.json \
        --execution-mode python --assurance-note "script checks passed" \
        --out report.html

Runs reconcile_counts first. If the coverage invariant fails, writes a refusal
page stating the report cannot issue, with the mismatch, and exits 1. On
success renders: findings by lens and severity, the coverage table per lens,
the family map summary, the gap report, and the unresolved queue. Output is
deterministic: same inputs give byte-identical HTML. No external requests,
no timestamps. The page records nothing; the orchestrator records the
lawyer's rulings on the unresolved queue.
"""

import argparse
import html
import json
import posixpath
import sys

import reconcile_counts

COVERAGE_SENTENCE = (
    "Coverage assurance and finding assurance are separate: this table proves "
    "the run was complete; the findings above are proposals for the lawyer's judgment."
)

BANDS = ["high", "medium", "low"]
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
  --high: #f6e0dc;
  --high-line: #b0503c;
  --high-ink: #8c2f1f;
  --panel: #f1f0ec;
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
    --high: #3d221d;
    --high-line: #a35240;
    --high-ink: #e8a08f;
    --panel: #1f1f1d;
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
h4 { font-size: 14px; margin: 14px 0 6px; }
.counts { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 10px; }
.count {
  background: var(--badge); border-radius: 4px; padding: 2px 10px;
  font-size: 13px; white-space: nowrap;
}
.count b { font-size: 14px; }
.count.warn { background: var(--proposed); color: var(--proposed-ink); border: 1px solid var(--proposed-line); }
.equation { font-size: 15px; margin: 0 0 10px; }
.verdict {
  border-radius: 4px; padding: 1px 10px; font-size: 13px; font-weight: 700;
  text-transform: uppercase; letter-spacing: .05em; margin-left: 8px;
}
.verdict.ok { background: var(--settled); color: var(--settled-ink); border: 1px solid var(--settled-ink); }
.verdict.fail { background: var(--high); color: var(--high-ink); border: 1px solid var(--high-line); }
.badge {
  border-radius: 4px; padding: 1px 8px; font-size: 12px; font-weight: 600;
  text-transform: uppercase; letter-spacing: .04em; background: var(--badge);
}
.band-high { background: var(--high); color: var(--high-ink); border: 1px solid var(--high-line); }
.band-medium { background: var(--proposed); color: var(--proposed-ink); border: 1px solid var(--proposed-line); }
.band-low { background: var(--badge); color: var(--muted); border: 1px solid var(--line); }
.pos { background: var(--settled); color: var(--settled-ink); border: 1px solid var(--settled-ink); }
.finding {
  background: var(--card); border: 1px solid var(--line); border-radius: 6px;
  padding: 10px 12px; margin: 0 0 10px;
}
.badges { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; margin: 0 0 6px; }
.basis { font-size: 12px; color: var(--muted); }
.char { margin: 4px 0; }
blockquote {
  margin: 6px 0; padding: 6px 10px; border-left: 3px solid var(--accent);
  background: var(--panel); font-style: italic; font-size: 14px; border-radius: 0 4px 4px 0;
}
.cite { font-size: 13px; color: var(--muted); margin: 4px 0 0; }
.doc-id { color: var(--muted); font-family: ui-monospace, Menlo, monospace; font-size: 12px; }
.scroll { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: 14px; }
th, td { text-align: left; padding: 4px 12px 4px 0; border-bottom: 1px solid var(--line); vertical-align: top; }
th { color: var(--muted); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: .03em; }
tr:last-child td { border-bottom: none; }
.gap-group, .card {
  background: var(--card); border: 1px solid var(--line); border-radius: 6px;
  padding: 12px 16px; margin: 0 0 12px;
}
.gap-group h3 .count { margin-left: 8px; }
.gap-group ul { margin: 6px 0 0; padding-left: 18px; }
.gap-group li { margin: 4px 0; }
.evidence { color: var(--muted); font-size: 13px; }
.note { background: var(--card); border: 1px solid var(--line); border-left: 4px solid var(--accent);
  border-radius: 4px; padding: 8px 12px; font-size: 14px; margin: 0 0 12px; }
.queue { background: var(--proposed); border: 1px solid var(--proposed-line); border-radius: 6px;
  padding: 12px 16px; margin: 0 0 14px; }
.queue ol { margin: 6px 0 0; padding-left: 20px; }
.queue li { margin: 8px 0; }
.rule-hit { font-size: 13px; color: var(--proposed-ink); margin: 2px 0 0; }
.refusal { background: var(--high); border: 1px solid var(--high-line); border-radius: 6px;
  color: var(--high-ink); padding: 14px 16px; margin: 16px 0; }
.refusal ul { margin: 6px 0 0; padding-left: 18px; }
.small { font-size: 13px; color: var(--muted); }
footer.decide {
  max-width: 960px; margin: 32px auto 0; border-top: 2px solid var(--line); padding-top: 16px;
}
footer.decide p { margin: 6px 0; }
"""

HEAD = (
    '<html lang="en"><head><meta charset="utf-8">'
    '\n<meta name="viewport" content="width=device-width, initial-scale=1">'
)


def esc(s):
    return html.escape(str(s), quote=True)


def plural(n, word):
    return f"{n} {word}" if n == 1 else f"{n} {word}s"


def load(path, kind, required_keys):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"render_report: cannot read {kind} at {path}: {e}")
    for k in required_keys:
        if k not in data:
            sys.exit(f"render_report: {kind} missing key '{k}'")
    return data


def doc_path(doc_id, docs):
    d = docs.get(doc_id)
    return d.get("path", doc_id) if d else doc_id


def equation_html(totals, ok):
    verdict = (
        '<span class="verdict ok">RECONCILED</span>'
        if ok
        else '<span class="verdict fail">FAILED</span>'
    )
    return (
        f'<p class="equation"><b>{totals["reviewed"]}</b> reviewed units + '
        f"<b>{totals['parked']}</b> parked + <b>{totals['unreadable']}</b> unreadable = "
        f"<b>{totals['units']}</b> manifest reviewable total{verdict}</p>"
    )


def render_finding(f, docs, family_ids):
    out = ['<article class="finding">', '<div class="badges">']
    band = f.get("band")
    if band:
        out.append(f'<span class="badge band-{esc(band)}">{esc(band)}</span>')
    basis = f.get("band_basis")
    if basis:
        out.append(f'<span class="basis">{esc(basis)}</span>')
    if f.get("unit_id") in family_ids and f.get("current_position"):
        out.append('<span class="badge pos">current position (post-amendment)</span>')
    ver = f.get("verification", {})
    if ver.get("status") == "confirmed":
        out.append(
            f'<span class="basis">quote verified ({esc(ver.get("checker", ""))})</span>'
        )
    out.append("</div>")
    if f.get("characterization"):
        out.append(f'<p class="char">{esc(f["characterization"])}</p>')
    if (f.get("quote") or "").strip():
        out.append(f"<blockquote>{esc(f['quote'])}</blockquote>")
    section = f.get("section")
    cite = f"Section {esc(section)}, " if section else ""
    out.append(
        f'<p class="cite">{cite}{esc(doc_path(f.get("doc_id", ""), docs))} '
        f'<span class="doc-id">{esc(f.get("finding_id", ""))}</span></p>'
    )
    out.append("</article>")
    return "\n".join(out)


def render_lens_findings(lens, by_lens, docs, family_ids):
    out = []
    flist = by_lens.get(lens.get("lens_id", ""), [])
    present = [f for f in flist if f.get("status") == "present"]
    absent = sorted(
        (f for f in flist if f.get("status") == "absent"),
        key=lambda f: f.get("finding_id", ""),
    )
    n_unresolved = sum(1 for f in flist if f.get("status") == "unresolved")
    for band in BANDS:
        ranked = sorted(
            (f for f in present if f.get("band") == band),
            key=lambda f: f.get("finding_id", ""),
        )
        if not ranked:
            continue
        out.append(f"<h4>{esc(band.capitalize())} severity</h4>")
        for f in ranked:
            out.append(render_finding(f, docs, family_ids))
    unranked = sorted(
        (f for f in present if f.get("band") not in BANDS),
        key=lambda f: f.get("finding_id", ""),
    )
    if unranked:
        out.append("<h4>Unranked</h4>")
        for f in unranked:
            out.append(render_finding(f, docs, family_ids))
    if absent:
        out.append("<h4>Absent</h4>")
        out.append(
            '<div class="scroll"><table><thead><tr>'
            "<th>Issue</th><th>Document</th><th>Characterization</th></tr></thead><tbody>"
        )
        for f in absent:
            out.append(
                f"<tr><td>{esc(f.get('issue_id', ''))}</td>"
                f"<td>{esc(doc_path(f.get('doc_id', ''), docs))}</td>"
                f"<td>{esc(f.get('characterization', ''))}</td></tr>"
            )
        out.append("</tbody></table></div>")
    if n_unresolved:
        out.append(
            f'<p class="small">{plural(n_unresolved, "unresolved finding")} for this lens '
            "in the unresolved queue below.</p>"
        )
    if not (present or absent or n_unresolved):
        out.append('<p class="small">No findings for this lens.</p>')
    return "\n".join(out)


def render_coverage_table(framework, result):
    out = []
    out.append(f'<div class="note">{esc(COVERAGE_SENTENCE)}</div>')
    out.append(
        '<div class="scroll"><table><thead><tr>'
        "<th>Lens</th><th>Present</th><th>Absent</th><th>Unresolved</th>"
        "<th>Parked</th><th>Units covered</th><th>Reviewable total</th><th>Check</th>"
        "</tr></thead><tbody>"
    )
    reviewable = result["totals"]["reviewable"]
    for lens in framework.get("lenses", []):
        lid = lens.get("lens_id", "")
        info = result["per_lens"].get(lid, {})
        sc = info.get("status_counts", {})
        covered = len(set(info.get("found_units", [])) | set(result["parked_units"]))
        check = "OK" if info.get("ok") else "FAIL"
        out.append(
            f"<tr><td>{esc(lid)}</td>"
            f"<td>{sc.get('present', 0)}</td><td>{sc.get('absent', 0)}</td>"
            f"<td>{sc.get('unresolved', 0)}</td><td>{info.get('parked', 0)}</td>"
            f"<td>{covered}</td><td>{reviewable}</td><td>{check}</td></tr>"
        )
    out.append("</tbody></table></div>")
    return "\n".join(out)


def render_family_summary(families, docs):
    fams = sorted(families.get("families", []), key=lambda f: f.get("family_id", ""))
    orphans = sorted(families.get("orphans", []))
    origin_model = sum(
        1
        for family in fams
        for edge in family.get("edges", [])
        if edge.get("provenance") == "model"
        or edge.get("evidence_source") in {"model-read", "image-read-human-confirmed"}
    )
    n_proposed = 0 if families.get("confirmed") is True else origin_model
    out = ['<div class="counts">']
    out.append(
        f'<span class="count">{esc(plural(len(fams), "family").replace("familys", "families"))}</span>'
    )
    out.append(f'<span class="count">{esc(plural(len(orphans), "orphan"))}</span>')
    out.append(
        f'<span class="count{" warn" if n_proposed else ""}">'
        f"{esc(plural(n_proposed, 'proposed edge'))}</span>"
    )
    out.append("</div>")
    if n_proposed:
        out.append(
            '<div class="note">Proposed edges should be zero after room-structure confirmation. '
            f"{plural(n_proposed, 'reader/model-proposed edge')} remain unconfirmed; "
            "this report was built from an unconfirmed family map.</div>"
        )
    out.append(
        '<div class="card"><div class="scroll"><table><thead><tr>'
        "<th>Family (base document)</th><th>Members</th><th>ID</th></tr></thead><tbody>"
    )
    for fam in fams:
        base = fam.get("family_id", "")
        out.append(
            f"<tr><td>{esc(posixpath.basename(doc_path(base, docs)))}</td>"
            f"<td>{len(fam.get('members', []))}</td>"
            f'<td class="doc-id">{esc(base)}</td></tr>'
        )
    out.append("</tbody></table></div>")
    if orphans:
        out.append(
            '<p class="small">Orphans (no family): '
            + ", ".join(esc(posixpath.basename(doc_path(o, docs))) for o in orphans)
            + "</p>"
        )
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
        for e in sorted(items, key=lambda x: x.get("detail", "")):
            out.append(
                f"<li>{esc(e.get('detail', ''))}"
                f'<div class="evidence">Evidence: {esc(e.get("evidence", ""))}</div></li>'
            )
        out.append("</ul></div>")
    if not out:
        out.append('<p class="small">No gaps reported.</p>')
    return "\n".join(out)


def render_queue(framework, findings, docs):
    unresolved = sorted(
        (f for f in findings.get("findings", []) if f.get("status") == "unresolved"),
        key=lambda f: f.get("finding_id", ""),
    )
    if not unresolved:
        return '<p class="small">Nothing unresolved. No rulings needed.</p>'
    rules = {
        item.get("issue_id", ""): (
            item.get("question", ""),
            item.get("evidence", {}).get("unresolved_when", ""),
        )
        for lens in framework.get("lenses", [])
        for item in lens.get("items", [])
    }
    out = ['<div class="queue">']
    out.append(
        f"<p><b>{plural(len(unresolved), 'unresolved finding')}</b> await your ruling. "
        "One batched list; rule on all of them in one reply.</p>"
    )
    out.append("<ol>")
    for f in unresolved:
        question, rule = rules.get(f.get("issue_id", ""), ("", ""))
        out.append("<li>")
        out.append(
            f"<b>{esc(f.get('issue_id', ''))}</b> on {esc(doc_path(f.get('doc_id', ''), docs))} "
            f'<span class="doc-id">{esc(f.get("finding_id", ""))}</span>'
        )
        if question:
            out.append(f'<div class="small">Question: {esc(question)}</div>')
        if f.get("characterization"):
            out.append(f'<div class="char">{esc(f["characterization"])}</div>')
        if (f.get("quote") or "").strip():
            out.append(f"<blockquote>{esc(f['quote'])}</blockquote>")
        if rule:
            out.append(
                f'<div class="rule-hit">Triggered rule (unresolved_when): {esc(rule)}</div>'
            )
        out.append("</li>")
    out.append("</ol></div>")
    return "\n".join(out)


def build_refusal(result, root_label, execution_mode, assurance_note):
    parts = []
    parts.append("<!doctype html>")
    parts.append(HEAD)
    parts.append("<title>Final report withheld</title>")
    parts.append(f"<style>{CSS}</style></head><body>")
    parts.append('<header class="strip">')
    parts.append(f"<h1>Final report withheld for {esc(root_label)}</h1>")
    parts.append(equation_html(result["totals"], False))
    parts.append(
        f'<p class="small"><b>Execution mode:</b> {esc(execution_mode)}. '
        f"<b>Assurance:</b> {esc(assurance_note)}</p>"
    )
    parts.append("</header><main>")
    parts.append('<div class="refusal">')
    parts.append(
        "<p><b>This report cannot issue: the coverage counts do not reconcile.</b> "
        "Every reviewable unit must be reviewed or parked under every lens before "
        "findings are reportable. The mismatch:</p>"
    )
    parts.append("<ul>")
    for line in result["lines"]:
        parts.append(f"<li>{esc(line)}</li>")
    for e in result["errors"]:
        parts.append(f"<li>error: {esc(e)}</li>")
    parts.append("</ul></div>")
    parts.append(
        '<p class="small">Fix the run (review or park the missing units, or correct the '
        "findings ledger) and re-render. No findings are shown from an unreconciled run.</p>"
    )
    parts.append("</main></body></html>")
    return "\n".join(parts) + "\n"


def build_html(
    framework,
    findings,
    manifest,
    families,
    gaps,
    result,
    execution_mode,
    assurance_note,
):
    docs = {d["id"]: d for d in manifest.get("documents", [])}
    family_ids = {f.get("family_id", "") for f in families.get("families", [])}
    by_lens = {}
    for f in findings.get("findings", []):
        by_lens.setdefault(f.get("lens_id", ""), []).append(f)
    all_findings = findings.get("findings", [])
    n_high = sum(
        1
        for f in all_findings
        if f.get("status") == "present" and f.get("band") == "high"
    )
    n_unresolved = sum(1 for f in all_findings if f.get("status") == "unresolved")

    parts = []
    parts.append("<!doctype html>")
    parts.append(HEAD)
    parts.append("<title>Final findings report</title>")
    parts.append(f"<style>{CSS}</style></head><body>")

    parts.append('<header class="strip">')
    parts.append(
        f"<h1>Final findings report for {esc(manifest.get('root_label', 'data room'))}</h1>"
    )
    parts.append(equation_html(result["totals"], True))
    parts.append(
        f'<p class="small"><b>Execution mode:</b> {esc(execution_mode)}. '
        f"<b>Assurance:</b> {esc(assurance_note)}</p>"
    )
    counts = [
        (f"framework version {framework.get('framework_version')}", False),
        (plural(len(all_findings), "finding"), False),
        (plural(n_high, "high-severity finding"), n_high > 0),
        (
            plural(n_unresolved, "unresolved finding") + " awaiting rulings",
            n_unresolved > 0,
        ),
        (plural(result["totals"]["parked"], "parked unit"), False),
    ]
    parts.append(
        '<div class="counts">'
        + "".join(
            f'<span class="count{" warn" if warn else ""}">{esc(c)}</span>'
            for c, warn in counts
        )
        + "</div>"
    )
    parts.append("</header><main>")

    parts.append('<section id="findings">')
    parts.append("<h2>1. Findings by lens and severity</h2>")
    for lens in framework.get("lenses", []):
        parts.append(
            f"<h3>{esc(lens.get('name', lens.get('lens_id', '')))} "
            f'<span class="doc-id">{esc(lens.get("lens_id", ""))}</span></h3>'
        )
        parts.append(render_lens_findings(lens, by_lens, docs, family_ids))
    parts.append("</section>")

    parts.append('<section id="coverage">')
    parts.append("<h2>2. Coverage by lens</h2>")
    parts.append(render_coverage_table(framework, result))
    parts.append("</section>")

    parts.append('<section id="family-map">')
    parts.append("<h2>3. Family map summary</h2>")
    parts.append(render_family_summary(families, docs))
    parts.append("</section>")

    parts.append('<section id="gap-report">')
    parts.append("<h2>4. Gap report</h2>")
    parts.append(render_gaps(gaps.get("entries", [])))
    parts.append("</section>")

    parts.append('<section id="unresolved-queue">')
    parts.append("<h2>5. Unresolved queue</h2>")
    parts.append(render_queue(framework, findings, docs))
    parts.append("</section>")

    parts.append("</main>")
    parts.append('<footer class="decide">')
    parts.append("<h2>Your decision</h2>")
    parts.append(
        "<p>Decisions are batched on this page. Reply in the conversation with one message "
        "that rules on each item in the unresolved queue and approves or corrects the "
        "further-enquiries register. Approval marks the register client-ready.</p>"
    )
    parts.append(
        "<p>Nothing on this page submits or saves anything. The orchestrating agent records "
        "your rulings and updates the ledger; the register export reflects the ruled ledger.</p>"
    )
    parts.append("</footer></body></html>")
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Render the final findings report.")
    ap.add_argument("--framework", required=True)
    ap.add_argument("--findings", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument(
        "--families",
        default=None,
        help="Confirmed family map. Optional for discovery runs with only clusters.",
    )
    ap.add_argument("--clusters", default=None)
    ap.add_argument("--privilege-queue", default=None)
    ap.add_argument("--review-plan", default=None)
    ap.add_argument("--gaps", required=True)
    ap.add_argument(
        "--execution-mode", required=True, choices=["python", "portable-fallback"]
    )
    ap.add_argument("--assurance-note", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    framework = load(args.framework, "framework", ["framework_version", "lenses"])
    findings = load(args.findings, "findings", ["findings"])
    manifest = load(args.manifest, "manifest", ["documents", "counts"])
    families = (
        load(args.families, "families", ["families"])
        if args.families
        else {"confirmed": True, "families": [], "orphans": []}
    )
    gaps = load(args.gaps, "gap report", ["entries"])
    clusters = load(args.clusters, "clusters", ["threads"]) if args.clusters else None
    privilege_queue = (
        load(args.privilege_queue, "privilege queue", ["candidates", "ruled"])
        if args.privilege_queue
        else None
    )
    review_plan = (
        load(args.review_plan, "review plan", ["plan_id", "jobs"])
        if args.review_plan
        else None
    )

    result = reconcile_counts.reconcile(
        manifest,
        findings,
        framework,
        families,
        clusters,
        privilege_queue,
        review_plan,
    )
    if not result["ok"]:
        doc = build_refusal(
            result,
            manifest.get("root_label", "data room"),
            args.execution_mode,
            args.assurance_note,
        )
        with open(args.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(doc)
        print(f"wrote refusal page {args.out}")
        for line in result["lines"]:
            print(line)
        for e in result["errors"]:
            print(f"error: {e}")
        sys.exit(1)

    doc = build_html(
        framework,
        findings,
        manifest,
        families,
        gaps,
        result,
        args.execution_mode,
        args.assurance_note,
    )
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
