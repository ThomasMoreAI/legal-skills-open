#!/usr/bin/env python3
# ruff: noqa: E501 -- self-contained HTML and CSS literals stay readable.
"""Render the lawyer-facing factual test review as one self-contained HTML file.

Usage:
    python3 render_sample.py --framework framework.json --findings findings.json \
        --manifest manifest.json --out sample.html

Shows factual sample results grouped by lens then issue, each beside the schema
fields that governed it, so a reaction maps to a specific field edit.
Unresolved findings render in their own strip with the rule that routed them
there. Output is deterministic: same inputs give byte-identical HTML. No
external requests, no timestamps. The page records nothing; the orchestrator
records the lawyer's reply and recompiles the framework.
"""

import argparse
import hashlib
import html
import importlib.util
import json
import sys
from pathlib import Path

_REVIEW_UI_SPEC = importlib.util.spec_from_file_location(
    "diligence_review_ui", Path(__file__).with_name("review_ui.py")
)
if _REVIEW_UI_SPEC is None or _REVIEW_UI_SPEC.loader is None:
    raise RuntimeError("cannot load sibling review_ui.py")
review_ui = importlib.util.module_from_spec(_REVIEW_UI_SPEC)
_REVIEW_UI_SPEC.loader.exec_module(review_ui)
BRAND_CSS = review_ui.BRAND_CSS
CONTRACT_ID = review_ui.CONTRACT_ID
THEME_JS = review_ui.THEME_JS
masthead = review_ui.masthead

_REVIEW_COPIES_SPEC = importlib.util.spec_from_file_location(
    "diligence_review_copies", Path(__file__).with_name("review_copies.py")
)
if _REVIEW_COPIES_SPEC is None or _REVIEW_COPIES_SPEC.loader is None:
    raise RuntimeError("cannot load sibling review_copies.py")
review_copies = importlib.util.module_from_spec(_REVIEW_COPIES_SPEC)
sys.modules[_REVIEW_COPIES_SPEC.name] = review_copies
_REVIEW_COPIES_SPEC.loader.exec_module(review_copies)

BAND_ORDER = {"high": 0, "medium": 1, "low": 2}
STATUS_LABELS = {
    "present": "Found",
    "absent": "Not found",
    "unresolved": "Needs a decision",
}

CSS = (
    BRAND_CSS
    + r"""
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
  --high: var(--lq-destructive-surface);
  --high-line: var(--lq-destructive);
  --high-ink: var(--lq-destructive);
  --panel: var(--lq-surface-muted);
  --serif: var(--lq-font-serif);
}
* { box-sizing: border-box; }
.skip { position: absolute; left: -9999px; top: 4px; background: var(--card); color: var(--ink); padding: 6px 10px; z-index: 20; }
.skip:focus { left: 4px; }
body {
  background: #f7f6f3;
  background: var(--bg);
  color: var(--ink);
  font: 15px/1.5 var(--lq-font-sans);
  margin: 0;
  padding: 0 16px 48px;
}
main { max-width: 1080px; margin: 0 auto; }
header.strip {
  max-width: 1080px; margin: 0 auto; padding: 20px 0 12px;
  border-bottom: 2px solid var(--line);
}
h1 { font: 500 27px/1.2 var(--serif); margin: 0 0 8px; }
h2 { font-size: 17px; margin: 28px 0 10px; }
h3 { font-size: 15px; margin: 0 0 6px; }
.eyebrow { color: var(--accent); font-size: 13px; font-weight: 500; margin: 0 0 5px; }
.lede { color: var(--muted); font-size: 15px; max-width: 760px; margin: 5px 0 14px; }
.counts { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 10px; }
.count {
  background: var(--badge); border-radius: 4px; padding: 2px 10px;
  font-size: 13px; white-space: nowrap;
}
.count b { font-size: 14px; }
.count.warn { background: var(--proposed); color: var(--proposed-ink); border: 1px solid var(--proposed-line); }
.gate-rule { font-weight: 500; margin: 0; }
.issue {
  background: var(--card); border: 1px solid var(--line); border-radius: 6px;
  padding: 14px 16px; margin: 0 0 14px;
}
.issue-grid { display: grid; grid-template-columns: minmax(0, 1fr) 320px; gap: 16px; }
@media (max-width: 820px) { .issue-grid { grid-template-columns: minmax(0, 1fr); } }
.finding { border: 1px solid var(--line); border-radius: 6px; padding: 10px 12px; margin: 0 0 10px; }
.badges { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; margin: 0 0 6px; }
.badge {
  border-radius: 4px; padding: 1px 8px; font-size: 12px; font-weight: 500;
  text-transform: uppercase; letter-spacing: .04em; background: var(--badge);
}
.status-present { background: var(--settled); color: var(--settled-ink); border: 1px solid var(--settled-ink); }
.status-absent { background: var(--badge); color: var(--muted); border: 1px solid var(--line); }
.status-unresolved { background: var(--proposed); color: var(--proposed-ink); border: 1px solid var(--proposed-line); }
.band-high { background: var(--high); color: var(--high-ink); border: 1px solid var(--high-line); }
.band-medium { background: var(--badge); color: var(--muted); border: 1px solid var(--line); }
.band-low { background: var(--badge); color: var(--muted); border: 1px solid var(--line); }
.basis { font-size: 12px; color: var(--muted); }
.char { margin: 4px 0; }
blockquote {
  margin: 6px 0; padding: 6px 10px; border-left: 3px solid var(--accent);
  background: var(--panel); font-style: italic; font-size: 14px; border-radius: 0 4px 4px 0;
}
.cite { font-size: 13px; color: var(--muted); margin: 4px 0 0; }
.doc-id { color: var(--muted); font-family: ui-monospace, Menlo, monospace; font-size: 12px; }
details.schema {
  background: var(--panel); border: 1px solid var(--line); border-radius: 6px;
  padding: 10px 12px; font-size: 13px; align-self: start;
}
details.schema summary { cursor: pointer; color: var(--accent); font-weight: 500; }
details.schema h4 {
  margin: 0 0 6px; font-size: 12px; text-transform: uppercase;
  letter-spacing: .04em; color: var(--muted);
}
details.schema dl { margin: 8px 0 0; }
details.schema dt { font-weight: 500; margin-top: 6px; }
details.schema dd { margin: 0; color: var(--muted); overflow-wrap: break-word; }
details.schema ul { margin: 2px 0 0; padding-left: 16px; }
.strip-unresolved {
  background: var(--proposed); border: 1px solid var(--proposed-line); border-radius: 6px;
  padding: 12px 16px; margin: 0 0 14px;
}
.strip-unresolved .finding { background: var(--card); }
.rule-hit { font-size: 13px; color: var(--proposed-ink); margin: 4px 0 0; }
.note { background: var(--card); border: 1px solid var(--line); border-left: 4px solid var(--accent);
  border-radius: 4px; padding: 8px 12px; font-size: 14px; margin: 0 0 12px; }
.small { font-size: 13px; color: var(--muted); }
.scroll { overflow-x: auto; }
.review-copy-alert { background: var(--proposed); color: var(--proposed-ink); border: 1px solid var(--proposed-line); padding: 12px 14px; margin: 14px 0; }
.source-review-item { margin: 14px 0; padding: 14px; border: 1px solid var(--line); background: var(--panel); }
.source-review-item:target { outline: 3px solid var(--accent); outline-offset: 3px; }
.lq-review-copy h3 { margin-bottom: 6px; }
.lq-review-copy-receipt { color: var(--muted); font-size: 12px; overflow-wrap: anywhere; }
.lq-review-copy-frame, .lq-review-copy-pdf { display: block; width: 100%; min-height: 430px; border: 1px solid var(--line); background: var(--card); }
.lq-review-copy-image { display: block; max-width: 100%; height: auto; margin: 8px auto; border: 1px solid var(--line); }
.lq-needs-rendering { padding: 12px 14px; background: var(--proposed); color: var(--proposed-ink); border-left: 4px solid var(--proposed-line); }
.original-file { margin: 9px 0 0; font-size: 13px; }
footer.decide {
  max-width: 1080px; margin: 32px auto 0; border-top: 2px solid var(--line); padding-top: 16px;
}
footer.decide p { margin: 6px 0; }
#technical-receipts { max-width: 1080px; margin: 24px auto 0; border-top: 1px solid var(--line); padding-top: 12px; }
#technical-receipts summary { cursor: pointer; color: var(--accent); font-weight: 500; }
a { color: var(--accent); text-underline-offset: 3px; }
button:focus-visible, a:focus-visible, summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (max-width: 680px) { body { padding-left: 10px; padding-right: 10px; } h1 { font-size: 23px; } }
"""
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
        sys.exit(f"render_sample: cannot read {kind} at {path}: {e}")
    for k in required_keys:
        if k not in data:
            sys.exit(f"render_sample: {kind} missing key '{k}'")
    return data


def gate_sentence(_version):
    return (
        "Your feedback changes the review rules and reruns this test when needed. "
        "Approval authorizes the same questions for the full collection."
    )


def doc_path(doc_id, docs):
    d = docs.get(doc_id)
    return d.get("path", doc_id) if d else doc_id


def document_anchor(document):
    path_digest = hashlib.sha256(document.get("path", "").encode("utf-8")).hexdigest()[
        :8
    ]
    doc_id = str(document.get("id", "document")).removeprefix("sha256:")
    return f"review-document-{doc_id}-{path_digest}"


def source_href(prefix, path):
    try:
        return review_ui.source_href(prefix, path, link_without_prefix=False)
    except ValueError as error:
        sys.exit(f"render_sample: {error}")


def validate_review_copy_inputs(sidecar, manifest, document_root, output):
    if sidecar.parent.resolve() != output.parent.resolve():
        sys.exit(
            "render_sample: review-copies sidecar and HTML output must share a directory"
        )
    validation = review_copies.revalidate_review_copies(
        sidecar, manifest, document_root
    )
    if not validation.integrity_ok:
        detail = "; ".join(validation.errors)
        sys.exit(f"render_sample: review-copy validation failed: {detail}")
    return validation


def render_review_document(document, source_prefix, validation):
    title = (
        document.get("title") or Path(str(document.get("path", ""))).name or "Document"
    )
    href = source_href(source_prefix, document.get("path", ""))
    original = (
        f'<a href="{esc(href)}" target="_blank" rel="noopener">Open original file ↗</a>'
        if href
        else "Original-file link not supplied"
    )
    component = review_copies.render_review_copy_component(
        validation,
        document.get("id", ""),
        path=document.get("path", ""),
        title=title,
    )
    return (
        f'<article id="{esc(document_anchor(document))}" class="source-review-item" '
        'data-review-document="true" tabindex="-1">'
        f'{component}<p class="original-file">{original}</p></article>'
    )


def render_finding(f, docs, source_prefix):
    out = ['<article class="finding">', '<div class="badges">']
    status = f.get("status", "")
    out.append(
        f'<span class="badge status-{esc(status)}">'
        f"{esc(STATUS_LABELS.get(status, status))}</span>"
    )
    band = f.get("band")
    if band:
        out.append(f'<span class="badge band-{esc(band)}">{esc(band)}</span>')
    basis = f.get("band_basis")
    if basis:
        out.append(f'<span class="basis">band basis: {esc(basis)}</span>')
    if f.get("current_position"):
        out.append('<span class="badge band-medium">current position</span>')
    out.append("</div>")
    if f.get("characterization"):
        out.append(f'<p class="char">{esc(f["characterization"])}</p>')
    if (f.get("quote") or "").strip():
        out.append(f"<blockquote>{esc(f['quote'])}</blockquote>")
    section = f.get("section")
    cite = f"Section {esc(section)}, " if section else ""
    path = doc_path(f.get("doc_id", ""), docs)
    document = docs.get(f.get("doc_id", ""))
    link = (
        f'<a href="#{esc(document_anchor(document))}">Review document on this page ↓</a>'
        if document
        else "Review copy not supplied"
    )
    out.append(f'<p class="cite">{cite}{esc(path)} · {link}</p>')
    out.append("</article>")
    return "\n".join(out)


def render_schema_panel(item):
    """The calibration knobs for one issue; a reaction to a finding edits one of these."""
    mat = item.get("materiality", {})
    bands = mat.get("bands", [])
    out = [
        '<details class="schema">',
        "<summary>How this question was tested</summary>",
        "<dl>",
    ]
    out.append(f"<dt>A match means</dt><dd>{esc(item.get('hit_rule', ''))}</dd>")
    excl = item.get("exclusions", [])
    if excl:
        out.append("<dt>What does not count</dt><dd><ul>")
        out.extend(f"<li>{esc(x)}</li>" for x in excl)
        out.append("</ul></dd>")
    else:
        out.append("<dt>What does not count</dt><dd>Nothing separately excluded</dd>")
    if mat:
        out.append(f"<dt>Priority rule</dt><dd>default: {esc(mat.get('default', ''))}")
    else:
        out.append("<dt>Priority rule</dt><dd>No ranking was requested")
    if bands:
        out.append("<ul>")
        out.extend(
            f"<li>{esc(b.get('band', ''))} when {esc(b.get('when', ''))}</li>"
            for b in bands
        )
        out.append("</ul>")
    out.append("</dd>")
    out.append(
        "<dt>When the result needs review</dt>"
        f"<dd>{esc(item.get('evidence', {}).get('unresolved_when', ''))}</dd>"
    )
    out.append("</dl></details>")
    return "\n".join(out)


def build_html(framework, findings, manifest, source_prefix, review_validation):
    docs = {d["id"]: d for d in manifest.get("documents", [])}
    version = framework.get("framework_version")
    sentence = gate_sentence(version)

    by_issue = {}
    for f in findings.get("findings", []):
        by_issue.setdefault(f.get("issue_id", ""), []).append(f)
    for fl in by_issue.values():
        fl.sort(key=lambda f: f.get("finding_id", ""))

    all_findings = findings.get("findings", [])
    unresolved = sorted(
        (f for f in all_findings if f.get("status") == "unresolved"),
        key=lambda f: f.get("finding_id", ""),
    )
    unresolved_label = f"{len(unresolved)} result{'s' if len(unresolved) != 1 else ''} needing a decision"
    n_lenses = len(framework.get("lenses", []))

    parts = []
    parts.append("<!doctype html>")
    parts.append(
        f'<html lang="en" data-lq-review-ui="{CONTRACT_ID}"><head><meta charset="utf-8">'
    )
    parts.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    parts.append("<title>Review the test results</title>")
    parts.append(f"<style>{CSS}</style></head><body>")

    parts.append('<a class="skip" href="#sample-results">Skip to test results</a>')
    parts.append(masthead("Test results"))
    parts.append('<header class="strip">')
    parts.append('<p class="eyebrow">Test review</p>')
    parts.append("<h1>Review the test results</h1>")
    parts.append(
        '<p class="lede">This small test shows how the approved questions are being applied before the rest of the collection is reviewed.</p>'
    )
    counts = [
        (plural(len(all_findings), "sample finding"), False),
        (plural(n_lenses, "lens").replace("lenss", "lenses"), False),
        (unresolved_label + " below", len(unresolved) > 0),
    ]
    parts.append(
        '<div class="counts">'
        + "".join(
            f'<span class="count{" warn" if warn else ""}">{esc(c)}</span>'
            for c, warn in counts
        )
        + "</div>"
    )
    parts.append(f'<p class="gate-rule">{esc(sentence)}</p>')
    parts.append('</header><main id="sample-results">')

    blockers = [
        row
        for row in review_validation.sidecar.get("documents", [])
        if row.get("status") != "ready"
    ]
    if blockers:
        label = (
            "One file needs rendering"
            if len(blockers) == 1
            else f"{len(blockers)} files need rendering"
        )
        parts.append(
            f'<div class="review-copy-alert" role="alert"><b>{esc(label)}.</b> '
            "Those results are not ready for approval until a verified in-page copy is available.</div>"
        )

    parts.append(
        '<div class="note"><b>What the result labels mean.</b> “Found” includes the supporting quote. '
        "“Not found” means only that the supplied agreement text did not match the question. "
        "“Needs a decision” means the available text was incomplete or could not support a reliable answer.</div>"
    )

    sec = 0
    for lens in framework.get("lenses", []):
        sec += 1
        parts.append(
            f"<h2>{sec}. {esc(lens.get('name', lens.get('lens_id', '')))}</h2>"
        )
        for item in lens.get("items", []):
            issue_id = item.get("issue_id", "")
            parts.append('<article class="issue">')
            parts.append(f"<h3>{esc(item.get('question', ''))}</h3>")
            parts.append('<div class="issue-grid"><div class="findings">')
            shown = [
                f for f in by_issue.get(issue_id, []) if f.get("status") != "unresolved"
            ]
            if shown:
                for f in shown:
                    parts.append(render_finding(f, docs, source_prefix))
            else:
                parts.append(
                    '<p class="small">No resolved sample findings for this item.</p>'
                )
            hidden = len(by_issue.get(issue_id, [])) - len(shown)
            if hidden:
                hidden_label = (
                    f"{hidden} result{'s' if hidden != 1 else ''} needing a decision"
                )
                parts.append(
                    f'<p class="small">{hidden_label} for this item below.</p>'
                )
            parts.append("</div>")
            parts.append(render_schema_panel(item))
            parts.append("</div></article>")

    parts.append('<section id="unresolved-strip">')
    parts.append("<h2>Needs a decision</h2>")
    if unresolved:
        parts.append('<div class="strip-unresolved">')
        parts.append(
            '<p class="small">The available text did not support a reliable answer. Each result shows the approved reason it was sent for review.</p>'
        )
        rules = {
            item.get("issue_id", ""): item.get("evidence", {}).get(
                "unresolved_when", ""
            )
            for lens in framework.get("lenses", [])
            for item in lens.get("items", [])
        }
        for f in unresolved:
            parts.append(render_finding(f, docs, source_prefix))
            rule = rules.get(f.get("issue_id", ""), "")
            parts.append(f'<p class="rule-hit">Why it needs review: {esc(rule)}</p>')
        parts.append("</div>")
    else:
        parts.append('<p class="small">No needs-review results in this sample.</p>')
    parts.append("</section>")

    parts.append('<section id="source-review" aria-labelledby="source-review-title">')
    parts.append('<h2 id="source-review-title">Review the source documents</h2>')
    parts.append(
        '<p class="small">Each source appears once. Review copies are hash-bound to the manifest; the original file remains available as a secondary provenance link.</p>'
    )
    for document in sorted(
        manifest.get("documents", []),
        key=lambda row: (row.get("path", ""), row.get("id", "")),
    ):
        parts.append(render_review_document(document, source_prefix, review_validation))
    parts.append("</section>")

    parts.append("</main>")
    parts.append('<footer class="decide">')
    if review_validation.ready:
        parts.append("<h2>Are these the results you expected?</h2>")
        parts.append(
            "<p>Reply with approval, or identify the review question and explain what should count differently. The test will be rerun when that change could affect the results.</p>"
        )
    else:
        parts.append("<h2>Review is not ready for approval</h2>")
        parts.append(
            '<p role="alert">One or more source files still needs rendering. '
            "Resolve every item marked Needs rendering before approving the test.</p>"
        )
    parts.append(
        "<p>Nothing on this offline page records approval or starts the full review.</p>"
    )
    parts.append(f'<p class="gate-rule">{esc(sentence)}</p>')
    parts.append("</footer>")
    parts.append(
        '<details id="technical-receipts"><summary>Technical receipts and reproducibility details</summary>'
    )
    parts.append(
        f'<p class="small">Internal control: test sample · framework version {esc(version)}.</p><ul>'
    )
    parts.append(
        f'<li class="doc-id">Review-copy receipt {esc(review_validation.sidecar.get("digest"))} · status {esc(review_validation.sidecar.get("status"))}</li>'
    )
    for lens in framework.get("lenses", []):
        for item in lens.get("items", []):
            parts.append(
                f'<li class="doc-id">issue_id {esc(item.get("issue_id", ""))} · hit_rule {esc(item.get("hit_rule", ""))} · unresolved_when {esc(item.get("evidence", {}).get("unresolved_when", ""))}</li>'
            )
    parts.append("</ul></details>")
    parts.append(f"<script>{THEME_JS}</script></body></html>")
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser(
        description="Render the lawyer-facing factual test review."
    )
    ap.add_argument("--framework", required=True)
    ap.add_argument("--findings", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--source-prefix", default=None)
    ap.add_argument("--review-copies", required=True, type=Path)
    ap.add_argument("--document-root", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    output_path = args.out.expanduser().absolute().resolve()
    input_paths = {
        Path(value).expanduser().absolute().resolve()
        for value in (
            args.framework,
            args.findings,
            args.manifest,
            args.review_copies,
        )
    }
    if output_path in input_paths:
        sys.exit("render_sample: --out must be a distinct new artifact path")

    framework = load(args.framework, "framework", ["framework_version", "lenses"])
    findings = load(args.findings, "findings", ["findings"])
    manifest = load(args.manifest, "manifest", ["documents", "counts"])

    document_root = args.document_root.expanduser().resolve()
    for document in manifest.get("documents", []):
        raw_path = document.get("path") if isinstance(document, dict) else None
        if not isinstance(raw_path, str) or not raw_path:
            continue
        relative = Path(raw_path)
        if relative.is_absolute():
            sys.exit(
                f"render_sample: manifest document path must be relative: {raw_path}"
            )
        source = (document_root / relative).resolve()
        try:
            source.relative_to(document_root)
        except ValueError:
            sys.exit(f"render_sample: manifest document path escapes root: {raw_path}")
        if source == output_path:
            sys.exit(
                "render_sample: --out must not overwrite a manifest source document"
            )

    for document in manifest.get("documents", []):
        source_href(args.source_prefix, document.get("path", ""))
    review_validation = validate_review_copy_inputs(
        args.review_copies, Path(args.manifest), args.document_root, args.out
    )

    doc = build_html(
        framework, findings, manifest, args.source_prefix, review_validation
    )
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
