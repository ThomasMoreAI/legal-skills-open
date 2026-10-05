#!/usr/bin/env python3
"""Render the offline lawyer decision surface for possible privileged documents.

The renderer never decides privilege and never changes the queue. It provides
plain-language candidate explanations, source-document access, and a
deterministic ``privilege-rulings.json`` export bound to the exact queue and
manifest. ``ingest_privilege_rulings.py`` is the only consumer that may create
a ruled queue copy.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import importlib.util
import json
import os
import sys
import urllib.parse
from pathlib import Path
from typing import Any

RULING_LABELS = {
    "privileged": "Privileged",
    "not-privileged": "Not privileged",
    "needs-review": "Need more review",
}
SIGNAL_EXPLANATIONS = {
    "attorney-domain": "A sender or recipient address may belong to a lawyer.",
    "counsel-name": "A person named in the document may be a lawyer.",
    "legal-advice-content": "The document appears to contain legal analysis or a request for legal advice.",
    "legend": "The document carries a confidentiality label. A confidentiality label alone does not establish privilege.",
}
HOLD_SENTENCE = "No finding that references these documents enters the review results until you rule."


def load_review_ui() -> Any:
    """Load the self-contained lawyer-review brand primitives."""

    candidate = Path(__file__).resolve().parent / "shared" / "review_ui.py"
    spec = importlib.util.spec_from_file_location("lq_privilege_review_ui", candidate)
    if spec is None or spec.loader is None:
        sys.exit(
            f"render_privilege_queue: cannot load shared review UI from {candidate}"
        )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_review_copies() -> Any:
    """Load the self-contained hash-bound review-copy contract."""

    candidate = Path(__file__).resolve().parent / "shared" / "review_copies.py"
    spec = importlib.util.spec_from_file_location(
        "lq_privilege_review_copies", candidate
    )
    if spec is None or spec.loader is None:
        sys.exit(
            f"render_privilege_queue: cannot load shared review copies from {candidate}"
        )
    module = importlib.util.module_from_spec(spec)
    # dataclasses resolves postponed annotations through sys.modules on
    # Python 3.9, so register the module before executing it.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


REVIEW_UI = load_review_ui()
REVIEW_COPIES = load_review_copies()
BRAND_CSS = str(REVIEW_UI.BRAND_CSS)
CONTRACT_ID = str(REVIEW_UI.CONTRACT_ID)
THEME_BUTTON = str(REVIEW_UI.THEME_BUTTON)
THEME_JS = str(REVIEW_UI.THEME_JS)


CSS = r"""
:root{--desk:var(--lq-background);--paper:var(--lq-surface);--ink:var(--lq-foreground);
  --muted:var(--lq-muted-foreground);--line:var(--lq-border);--blue:var(--lq-primary);
  --green:var(--lq-success);--green-bg:var(--lq-success-surface);
  --amber:var(--lq-attention);--amber-bg:var(--lq-attention-surface);
  --red:var(--lq-destructive);--red-bg:var(--lq-destructive-surface);
  --focus:var(--lq-ring);--serif:var(--lq-font-serif);--sans:var(--lq-font-sans);
  --mono:var(--lq-font-mono)}
*{box-sizing:border-box}[hidden]{display:none!important}body{margin:0;background:var(--desk);
  color:var(--ink);font:15px/1.5 var(--sans)}.skip{position:absolute;left:-9999px;top:4px;
  background:var(--paper);color:var(--ink);padding:6px 10px;z-index:20}.skip:focus{left:4px}
header,main{max-width:980px;margin:0 auto;padding-left:20px;padding-right:20px}header{padding-top:20px}
.eyebrow{color:var(--blue);font-size:13px;font-weight:700;margin:0 0 5px}h1{font:600 27px/1.2 var(--serif);margin:0}
.sub,.small{color:var(--muted);font-size:13px}.sub{font-size:15px;max-width:760px;margin:7px 0 13px}
.caption-rule{border:0;border-top:2px solid var(--ink);margin:12px 0 0}.caption-rule+.caption-rule{border-top-width:1px;margin:2px 0 12px}
.counts{display:flex;flex-wrap:wrap;gap:7px;margin:0 0 12px}.pill{border-radius:12px;padding:2px 9px;font-size:12px;background:var(--paper);border:1px solid var(--line)}
.pill.attention{background:var(--amber-bg);color:var(--amber);border-color:var(--amber)}.hold{background:var(--amber-bg);color:var(--amber);padding:9px 12px;margin:0 0 16px}
.candidate{background:var(--paper);border:1px solid var(--line);border-left:4px solid var(--amber);border-radius:2px;margin:0 0 12px;padding:14px 16px}
.candidate h2{font:600 19px/1.3 var(--serif);margin:0}.fileline{font:12px var(--mono);color:var(--muted);overflow-wrap:anywhere;margin-top:2px}
.why{background:var(--desk);border-left:3px solid var(--blue);padding:9px 12px;margin:12px 0}.why strong{display:block;margin-bottom:3px}
blockquote{font:15.5px var(--serif);margin:10px 0;padding-left:13px;border-left:2px solid var(--line)}
.meta{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px;margin:10px 0}.meta div{min-width:0}.meta b{display:block;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.source{margin:10px 0}.source a{color:var(--blue);font-weight:650;text-underline-offset:3px}.decision{border-top:1px solid var(--line);margin-top:12px;padding-top:12px}
.review-copy-wrap{border-top:1px solid var(--line);margin:12px 0;padding-top:12px}.lq-review-copy{margin:0 0 10px}
.lq-review-copy h3{font:500 16px/1.3 var(--serif);margin:0 0 5px}.lq-review-copy-receipt{color:var(--muted);font:11px/1.4 var(--mono);overflow-wrap:anywhere}
.lq-review-copy-frame,.lq-review-copy-pdf{display:block;width:100%;height:min(68vh,720px);border:1px solid var(--line);background:var(--paper)}
.lq-review-copy-image{display:block;max-width:100%;max-height:70vh;width:auto;height:auto;margin:8px auto;border:1px solid var(--line);background:#fff;object-fit:contain}
.lq-needs-rendering{border:1px solid var(--amber);background:var(--amber-bg);color:var(--amber);padding:10px 12px}
.decision-label{display:block;color:var(--muted);font-size:12px;margin-bottom:6px}.choices{display:flex;flex-wrap:wrap;gap:7px}
.choice{border:1px solid var(--line);background:var(--paper);color:var(--ink);border-radius:4px;padding:6px 10px;cursor:pointer}
.choice[aria-pressed=true]{background:var(--blue);border-color:var(--blue);color:var(--paper)}
.choice[data-ruling=privileged][aria-pressed=true]{background:var(--red);border-color:var(--red);color:#fff}
.note{width:100%;margin-top:8px;padding:7px 9px;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:4px;font:14px var(--sans)}
.export{background:var(--paper);border:2px solid var(--blue);padding:15px 16px;margin:18px 0}.export h2{font:600 19px var(--serif);margin:0 0 5px}.btn{border:0;border-radius:4px;background:var(--blue);color:var(--paper);padding:9px 13px;font-weight:650;cursor:pointer}.btn:disabled{cursor:not-allowed;opacity:.45}
.status{min-height:1.5em;color:var(--muted);font-size:13px}.ruled{background:var(--paper);border:1px solid var(--line);padding:10px 12px;margin:10px 0}.ruled summary,details summary{cursor:pointer;font-weight:650}
#technical-receipts{border-top:1px solid var(--line);margin:22px 0 40px;padding-top:12px}.receipt-list{font:12px/1.5 var(--mono);overflow-wrap:anywhere}
button:focus-visible,textarea:focus-visible,a:focus-visible,summary:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
@media(prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
@media (max-width: 680px){header,main{padding-left:12px;padding-right:12px}.meta{grid-template-columns:1fr 1fr}.choices{display:grid;grid-template-columns:1fr}.choice{width:100%;text-align:left}}
"""


JS = r"""
"use strict";
const DATA=JSON.parse(document.getElementById("privilege-data").textContent);
const state={};
const candidates=[...document.querySelectorAll("[data-candidate]")];
const exportButton=document.getElementById("download-rulings");
const status=document.getElementById("ruling-status");
function update(){const complete=candidates.length>0&&candidates.every(card=>state[card.dataset.docId]);
  exportButton.disabled=!complete;status.textContent=complete?"All documents have a ruling. The export is ready.":
  `${Object.keys(state).length} of ${candidates.length} documents ruled.`;}
for(const card of candidates){for(const button of card.querySelectorAll("[data-ruling]")){button.addEventListener("click",()=>{
  const docId=card.dataset.docId;state[docId]=button.dataset.ruling;
  for(const peer of card.querySelectorAll("[data-ruling]")){peer.setAttribute("aria-pressed",String(peer===button));}update();});}}
function receipt(){return {artifact:"privilege-rulings",candidate_doc_ids:DATA.bindings.candidate_doc_ids,
  manifest_digest:DATA.bindings.manifest_digest,queue_digest:DATA.bindings.queue_digest,ruled_by:"lawyer",
  ruling_source:"offline-export",rulings:candidates.map(card=>({doc_id:card.dataset.docId,
  note:card.querySelector("textarea").value.trim(),ruling:state[card.dataset.docId]})).sort((a,b)=>a.doc_id.localeCompare(b.doc_id)),version:1};}
exportButton.addEventListener("click",()=>{const body=JSON.stringify(receipt(),null,2)+"\n";
  const link=document.createElement("a");link.href=URL.createObjectURL(new Blob([body],{type:"application/json"}));
  link.download="privilege-rulings.json";document.body.appendChild(link);link.click();link.remove();URL.revokeObjectURL(link.href);
  status.textContent="Downloaded privilege-rulings.json. Return it to the review task to apply these rulings.";});
update();
"""


def fail(message: str) -> None:
    print(f"render_privilege_queue: {message}", file=sys.stderr)
    raise SystemExit(1)


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def load(path: str, kind: str, required: tuple[str, ...]) -> dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot read {kind} at {path}: {error}")
    if not isinstance(value, dict):
        fail(f"{kind} must be an object")
    for key in required:
        if key not in value:
            fail(f"{kind} missing key {key!r}")
    return value


def digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def source_index(
    manifest: dict[str, Any], document_root: str | None, output_path: Path
) -> dict[str, dict[str, str]]:
    if document_root is None:
        return {}
    root = Path(document_root).expanduser().resolve()
    if not root.is_dir():
        fail(f"document root is not a directory: {document_root}")
    sources: dict[str, dict[str, str]] = {}
    rows = sorted(
        (row for row in manifest.get("documents", []) if isinstance(row, dict)),
        key=lambda row: (str(row.get("id", "")), str(row.get("path", ""))),
    )
    for document in rows:
        doc_id, raw_path = document.get("id"), document.get("path")
        if not isinstance(doc_id, str) or not isinstance(raw_path, str) or not raw_path:
            continue
        relative = Path(raw_path)
        if relative.is_absolute():
            fail(f"manifest document path must be relative: {raw_path}")
        candidate = (root / relative).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            fail(f"manifest document path escapes document root: {raw_path}")
        if candidate == output_path:
            fail("--out must not overwrite a manifest source document")
        if candidate.is_file():
            relative_href = Path(
                os.path.relpath(candidate, output_path.parent)
            ).as_posix()
            sources.setdefault(
                doc_id,
                {
                    "href": urllib.parse.quote(relative_href, safe="/"),
                    "path": raw_path,
                },
            )
    return sources


def explanation(candidate: dict[str, Any]) -> str:
    signals = candidate.get("signals", [])
    phrases = [
        SIGNAL_EXPLANATIONS[item] for item in signals if item in SIGNAL_EXPLANATIONS
    ]
    return (
        " ".join(phrases)
        or "The review detected a possible privilege indicator that requires a lawyer's decision."
    )


def review_copy_html(
    validation: Any,
    doc_id: str,
    document: dict[str, Any],
    title: str,
) -> str:
    """Return a verified component or refuse to expose a ruling control."""

    path = document.get("path")
    if not isinstance(path, str) or not path:
        fail(f"manifest document has no usable path: {doc_id}")
    if not validation.integrity_ok or validation.sidecar is None:
        detail = "; ".join(validation.errors[:3]) or "receipt validation failed"
        fail(f"review-copy integrity failed: {detail}")
    matches = [
        row
        for row in validation.sidecar["documents"]
        if row["doc_id"] == doc_id and row["path"] == path
    ]
    if len(matches) != 1:
        fail(f"review-copy receipt does not uniquely bind {doc_id} at {path}")
    entry = matches[0]
    if entry["status"] != "ready":
        fail(
            f"review copy is not ready for {doc_id}: "
            f"{entry.get('reason') or 'rendering required'}"
        )
    return str(
        REVIEW_COPIES.render_review_copy_component(
            validation,
            doc_id,
            path=path,
            title=title,
        )
    )


def candidate_html(
    candidate: dict[str, Any],
    messages: dict[str, Any],
    sources: dict[str, dict[str, str]],
    documents: dict[str, dict[str, Any]],
    review_validation: Any,
) -> str:
    doc_id = candidate.get("doc_id", "")
    message = messages.get(doc_id, {})
    source = sources.get(doc_id)
    title = message.get("subject") or (
        Path(source["path"]).name if source else "Document requiring review"
    )
    path = source["path"] if source else "Source path unavailable"
    metadata = ""
    if message:
        metadata = (
            '<div class="meta">'
            f"<div><b>From</b>{esc(message.get('from', 'Not stated'))}</div>"
            f"<div><b>To</b>{esc(', '.join(message.get('to', [])) or 'Not stated')}</div>"
            f"<div><b>Date</b>{esc(message.get('date', 'Not stated'))}</div>"
            f"<div><b>Subject</b>{esc(message.get('subject', 'Not stated'))}</div></div>"
        )
    source_html = (
        f'<p class="source"><a href="{esc(source["href"])}" target="_blank" rel="noopener" '
        f'aria-label="Open source document: {esc(path)}">Open source document ↗</a></p>'
        if source
        else '<p class="small">The source document is not linked from this copy. Do not rule until it is available.</p>'
    )
    review_html = review_copy_html(
        review_validation,
        str(doc_id),
        documents[str(doc_id)],
        str(title),
    )
    buttons = "".join(
        f'<button class="choice" type="button" data-ruling="{esc(value)}" aria-pressed="false">{esc(label)}</button>'
        for value, label in RULING_LABELS.items()
    )
    return (
        f'<article class="candidate" data-candidate data-doc-id="{esc(doc_id)}">'
        f'<h2>{esc(title)}</h2><div class="fileline">{esc(path)}</div>'
        f'<div class="why"><strong>Why this needs your decision</strong>{esc(explanation(candidate))}</div>'
        f"<blockquote>“{esc(candidate.get('quote', ''))}”</blockquote>{metadata}{source_html}"
        f'<div class="review-copy-wrap">{review_html}</div>'
        '<div class="decision"><span class="decision-label">Your privilege ruling</span>'
        f'<div class="choices" role="group" aria-label="Privilege ruling for {esc(title)}">{buttons}</div>'
        f'<textarea class="note" rows="2" aria-label="Optional note for {esc(title)}" placeholder="Optional note"></textarea>'
        "</div></article>"
    )


def build_html(
    queue: dict[str, Any],
    messages_doc: dict[str, Any],
    manifest: dict[str, Any],
    document_root: str | None,
    output_path: Path,
    review_validation: Any,
) -> str:
    candidates = sorted(
        queue.get("candidates", []), key=lambda item: item.get("doc_id", "")
    )
    ruled = sorted(queue.get("ruled", []), key=lambda item: item.get("doc_id", ""))
    if not isinstance(queue.get("candidates"), list) or not isinstance(
        queue.get("ruled"), list
    ):
        fail("candidates and ruled must be arrays")
    document_rows = sorted(
        (
            item
            for item in manifest.get("documents", [])
            if isinstance(item, dict)
            and isinstance(item.get("id"), str)
            and isinstance(item.get("path"), str)
        ),
        key=lambda item: (item["id"], item["path"]),
    )
    documents: dict[str, dict[str, Any]] = {}
    for item in document_rows:
        documents.setdefault(item["id"], item)
    for candidate in candidates:
        if candidate.get("doc_id") not in documents:
            fail(
                f"candidate references document absent from manifest: {candidate.get('doc_id')}"
            )
    sources = source_index(manifest, document_root, output_path)
    messages = messages_doc.get("messages", {})
    bindings = {
        "candidate_doc_ids": [item["doc_id"] for item in candidates],
        "manifest_digest": digest(manifest),
        "queue_digest": digest(queue),
    }
    data = json.dumps(
        {"bindings": bindings}, sort_keys=True, separators=(",", ":")
    ).replace("<", "\\u003c")
    cards = "".join(
        candidate_html(item, messages, sources, documents, review_validation)
        for item in candidates
    )
    if not cards:
        cards = '<p class="small">No document is waiting for a privilege ruling.</p>'
    ruled_html = (
        "".join(
            f"<li><b>{esc(item.get('doc_id', ''))}</b> — {esc(RULING_LABELS.get(item.get('ruling'), item.get('ruling', '')))}</li>"
            for item in ruled
        )
        or "<li>No prior rulings are recorded.</li>"
    )
    receipts = "".join(
        f"<li><code>{esc(item.get('doc_id', ''))}</code> · signals: {esc(', '.join(item.get('signals', [])))} · "
        f"candidate reason: {esc(item.get('reason', ''))}</li>"
        for item in candidates
    )
    label = manifest.get("root_label", "Production")
    return "".join(
        [
            f'<!doctype html><html lang="en" data-review-ui-contract="{esc(CONTRACT_ID)}"><head><meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            "<title>Review possible privileged documents</title>",
            f"<style>{BRAND_CSS}{CSS}</style></head><body>",
            '<a class="skip" href="#candidates">Skip to documents</a>',
            '<div class="lq-masthead" role="banner"><div class="lq-brand">LQ · Document Review</div>',
            f'<div class="lq-context"><span>Privilege review</span>{THEME_BUTTON}</div></div><header>',
            '<p class="eyebrow">Privilege review</p><h1>Review possible privileged documents</h1>',
            '<p class="sub">Before the review results can include these documents, decide whether each should remain protected. A flag is not a privilege determination.</p>',
            '<hr class="caption-rule"><hr class="caption-rule">',
            f'<div class="counts"><span class="pill attention">{len(candidates)} awaiting your ruling</span><span class="pill">{len(ruled)} already ruled</span></div>',
            f'<p class="hold" role="alert">{esc(HOLD_SENTENCE)}</p></header><main id="candidates">',
            cards,
            '<section class="export" aria-labelledby="export-title"><h2 id="export-title">Save these privilege rulings</h2>',
            '<p class="small">Rule every document, then download the receipt and return it to the review task. Nothing on this offline page changes the review by itself.</p>',
            '<button class="btn" id="download-rulings" type="button" disabled>Download privilege rulings</button>',
            '<p class="small"><code>privilege-rulings.json</code></p><p class="status" id="ruling-status" aria-live="polite"></p></section>',
            f'<details class="ruled"><summary>Already ruled documents ({len(ruled)})</summary><ul>{ruled_html}</ul></details>',
            '<details id="technical-receipts"><summary>Technical receipts and reproducibility details</summary>',
            f'<p class="small">Matter: {esc(label)}. Queue digest <code>{bindings["queue_digest"]}</code>. Manifest digest <code>{bindings["manifest_digest"]}</code>.</p>',
            f'<ul class="receipt-list">{receipts}</ul></details>',
            f'<script id="privilege-data" type="application/json">{data}</script><script>{THEME_JS}{JS}</script></main></body></html>\n',
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--queue", required=True)
    parser.add_argument("--messages", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument(
        "--document-root",
        help="root containing manifest source paths; required when candidates exist",
    )
    parser.add_argument(
        "--review-copies",
        help=(
            "hash-bound review-copy sidecar; required for pending candidates and "
            "must be alongside --out"
        ),
    )
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    queue = load(args.queue, "queue", ("candidates", "ruled"))
    messages = load(args.messages, "messages", ("messages",))
    manifest = load(args.manifest, "manifest", ("documents",))
    output_path = Path(args.out).expanduser().absolute().resolve()
    input_paths = {
        Path(value).expanduser().absolute().resolve()
        for value in (args.queue, args.messages, args.manifest, args.review_copies)
        if value
    }
    if output_path in input_paths:
        fail("--out must be a distinct new artifact path")
    candidates = queue.get("candidates")
    if not isinstance(candidates, list):
        fail("candidates must be an array")
    review_validation: Any = None
    if candidates:
        if not args.document_root or not args.review_copies:
            fail(
                "pending candidates require --document-root and --review-copies; "
                "a source link alone is not a lawyer-reviewable document"
            )
        output_parent = output_path.parent
        sidecar_path = Path(args.review_copies).expanduser().absolute()
        if sidecar_path.parent.resolve() != output_parent:
            fail(
                "--review-copies must be alongside --out so relative review-copy "
                "links stay valid"
            )
        review_validation = REVIEW_COPIES.revalidate_review_copies(
            sidecar_path,
            args.manifest,
            args.document_root,
        )
        if not review_validation.integrity_ok:
            detail = "; ".join(review_validation.errors[:3])
            fail(f"review-copy integrity failed: {detail}")
    rendered = build_html(
        queue,
        messages,
        manifest,
        args.document_root,
        output_path,
        review_validation,
    )
    try:
        Path(args.out).write_text(rendered, encoding="utf-8")
    except OSError as error:
        fail(f"cannot write {args.out}: {error}")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
