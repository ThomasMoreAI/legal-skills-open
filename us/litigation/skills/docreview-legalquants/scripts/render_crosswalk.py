#!/usr/bin/env python3
"""Render the offline lawyer review UI for a receiving-side request frame.

Usage:
    python3 render_crosswalk.py --framework framework.json \
        --findings findings.json --manifest manifest.json \
        [--privilege-queue privilege-queue.json] \
        [--document-root source-documents/] \
        [--review-copies review-copies.json] --out review.html

The renderer never changes findings, receipts, or privilege rulings. It binds
browser-exported lawyer feedback to immutable proposal and framework digests.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import importlib.util
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path
from typing import Any, NoReturn, cast

JsonObject = dict[str, Any]

HOLD_REASON = "privilege-candidate-awaiting-lawyer-ruling"
SERIES_PATTERN = re.compile(r"^[A-Z]+$")
PRODUCTION_NUMBER = re.compile(r"^(\d+)")
RULINGS = {"responsive", "not-responsive", "needs-review", "privileged"}
IMAGE_CONFIRMATIONS = {"confirmed", "needs-review"}
IMAGE_CONFIRMATION_KEYS = {
    "confirmation",
    "confirmed_by",
    "doc_id",
    "finding_ids",
    "note",
    "proposal_digest",
}


def load_review_ui() -> Any:
    """Load the shared review primitives from a pack or the source tree."""

    script = Path(__file__).resolve()
    candidates = (script.parent / "shared" / "review_ui.py",)
    for candidate in candidates:
        if not candidate.is_file():
            continue
        spec = importlib.util.spec_from_file_location("lq_shared_review_ui", candidate)
        if spec is None or spec.loader is None:
            continue
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    locations = ", ".join(str(candidate) for candidate in candidates)
    sys.exit(f"render_crosswalk: cannot load shared review UI from {locations}")


def load_review_copies() -> Any:
    """Load the shared review-copy contract from a pack or the source tree."""

    script = Path(__file__).resolve()
    candidates = (script.parent / "shared" / "review_copies.py",)
    for candidate in candidates:
        if not candidate.is_file():
            continue
        spec = importlib.util.spec_from_file_location(
            "lq_shared_review_copies", candidate
        )
        if spec is None or spec.loader is None:
            continue
        module = importlib.util.module_from_spec(spec)
        # dataclasses resolves postponed annotations through sys.modules on
        # Python 3.9, so register the module before executing it.
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    locations = ", ".join(str(candidate) for candidate in candidates)
    sys.exit(f"render_crosswalk: cannot load shared review copies from {locations}")


REVIEW_UI = load_review_ui()
REVIEW_COPIES = load_review_copies()
BRAND_CSS = str(REVIEW_UI.BRAND_CSS)
CONTRACT_ID = str(REVIEW_UI.CONTRACT_ID)
THEME_BUTTON = str(REVIEW_UI.THEME_BUTTON)
THEME_JS = str(REVIEW_UI.THEME_JS)

CSS = r"""
:root{
  --desk:var(--lq-background);--paper:var(--lq-surface);--ink:var(--lq-foreground);
  --muted:var(--lq-muted-foreground);--line:var(--lq-border);--blueback:var(--lq-primary);
  --hilite:var(--lq-attention-surface);--hilite-ink:var(--lq-attention);
  --green:var(--lq-success);--green-bg:var(--lq-success-surface);
  --amber:var(--lq-attention);--amber-bg:var(--lq-attention-surface);
  --red:var(--lq-destructive);--red-bg:var(--lq-destructive-surface);
  --redact:var(--lq-foreground);--focus:var(--lq-ring);
  --serif:var(--lq-font-serif);--sans:var(--lq-font-sans);--mono:var(--lq-font-mono)
}
*{box-sizing:border-box}[hidden]{display:none!important}html{scroll-behavior:smooth}
body{margin:0;background:var(--desk);color:var(--ink);font:400 15px/1.5 var(--sans)}
.skip{position:absolute;left:-9999px;top:4px;background:var(--paper);color:var(--ink);
  padding:6px 10px;z-index:20}.skip:focus{left:4px}
header,main{max-width:1080px;margin:0 auto;padding-left:20px;padding-right:20px}
header{padding-top:20px}.machine-note{display:inline-block;background:var(--amber-bg);
  color:var(--amber);border:1px solid var(--amber);border-radius:3px;
  padding:3px 8px;font-size:12px;font-weight:500;margin-bottom:8px}
h1{font:500 26px/1.2 var(--serif);letter-spacing:.01em;margin:0}
.sub,.small{color:var(--muted);font-size:13px}.sub{margin:3px 0 0}
.caption-rule{border:0;border-top:2px solid var(--ink);margin:12px 0 0}
.caption-rule+.caption-rule{border-top-width:1px;margin:2px 0 12px}
.docket-line{font:16px/1.7 var(--serif);margin:0 0 12px}
.link-button{font:inherit;color:var(--blueback);background:0;border:0;padding:0;
  text-decoration:underline;text-underline-offset:3px;cursor:pointer}
.toolbar,.chips,.ruling,.pills{display:flex;flex-wrap:wrap;gap:7px;align-items:center}
.toolbar{margin-bottom:8px}.toolbar input[type=search]{flex:1;min-width:230px}
input,select,textarea{background:var(--paper);color:var(--ink);border:1px solid var(--line);
  border-radius:4px;padding:7px 9px;font:14px var(--sans)}
.btn{background:var(--blueback);border:0;border-radius:4px;
  padding:8px 13px;font-weight:500;cursor:pointer;color:var(--lq-primary-foreground)}
.tabs{display:flex;border-bottom:2px solid var(--ink);margin:8px 0 11px}
.tab{background:0;border:0;border-bottom:3px solid transparent;color:var(--muted);
  cursor:pointer;font:500 16px var(--serif);margin-bottom:-2px;padding:8px 18px}
.tab[aria-selected=true]{color:var(--ink);border-bottom-color:var(--blueback)}
.chips{margin-bottom:9px}.chip{border:1px solid var(--line);background:var(--paper);
  color:var(--ink);border-radius:14px;padding:4px 11px;font-size:13px;cursor:pointer;
  transition:background-color .12s}
.chip[aria-pressed=true]{background:var(--blueback);border-color:var(--blueback);
  color:var(--lq-primary-foreground)}
.filter-count{color:var(--muted);font-size:12px;margin-left:auto}
.kbd-hint{font-size:12px;color:var(--muted);margin:5px 0 13px}
kbd{background:var(--paper);border:1px solid var(--line);border-radius:3px;
  font:11px var(--mono);padding:0 4px}.group-h{font:12px var(--mono);
  text-transform:uppercase;letter-spacing:.12em;color:var(--muted);margin:20px 0 8px}
.row{background:var(--paper);border:1px solid var(--line);border-left:4px solid var(--line);
  border-radius:2px;margin-bottom:8px;box-shadow:0 1px 2px rgba(0,0,0,.05)}
.row.has-responsive{border-left-color:var(--green)}.row.attention{border-left-color:var(--amber)}
.row.keyboard-focus{outline:2px solid var(--focus);outline-offset:1px}
.rowhead{display:flex;gap:12px;align-items:baseline;width:100%;background:0;border:0;
  color:var(--ink);text-align:left;padding:10px 14px;cursor:pointer;font:inherit}
.reqnum{font:500 15px var(--serif);white-space:nowrap}.preview{flex:1;min-width:0}
.pill,.badge{font-size:12px;border-radius:10px;padding:1px 8px}.pill.responsive,.badge.verified{
  background:var(--green-bg);color:var(--green)}.pill.neutral{background:var(--desk);color:var(--muted)}
.pill.attention,.badge.eyes{background:var(--amber-bg);color:var(--amber)}
.pill.privilege,.badge.privilege{background:var(--red-bg);color:var(--red)}
.rowbody{padding:0 14px 14px;border-top:1px solid var(--line)}
.request-text{font:15.5px var(--serif);border-left:3px solid var(--blueback);
  padding:8px 14px;margin:12px 0;background:var(--desk)}
.request-text .label{font:11px var(--mono);color:var(--muted);text-transform:uppercase;
  letter-spacing:.12em}.doccard{border:1px solid var(--line);border-radius:2px;
  padding:10px 12px;margin:10px 0;background:var(--paper)}
.docname{font-weight:500}.docdesc{color:var(--muted);font-size:13px;margin:2px 0 6px}
.bates{font:500 12px var(--mono);letter-spacing:.08em;border:1.5px solid var(--ink);
  border-radius:2px;padding:1px 7px;white-space:nowrap}
blockquote{font:15.5px var(--serif);margin:8px 0}blockquote mark{background:var(--hilite);
  color:var(--hilite-ink);padding:1px 2px;box-decoration-break:clone;
  -webkit-box-decoration-break:clone}blockquote.unverified mark{background:var(--amber-bg);
  color:var(--amber)}.cite,.receipt{font:11.5px var(--mono);color:var(--muted)}
.characterization{font-size:13.5px;margin:5px 0}.receipt{margin-top:7px}
.receipt summary,.drawer summary,.also summary{cursor:pointer;font-family:var(--sans)}
.ruling{margin-top:8px}.ruling-label{font-size:12px;color:var(--muted)}
.image-confirmation{border:1px solid var(--amber);background:var(--amber-bg);
  border-radius:2px;padding:10px 12px;margin:10px 0}.image-confirmation p{margin:3px 0 8px}
.source-link{color:var(--blueback);
  font-weight:500;text-underline-offset:3px}.original-source{margin:7px 0 12px;color:var(--muted);font-size:13px}
.review-copy-wrap{border-top:1px solid var(--line);margin:10px 0;padding-top:10px;scroll-margin-top:12px}
.lq-review-copy{margin:0 0 10px}.lq-review-copy h3{font:500 16px/1.3 var(--serif);margin:0 0 5px}
.lq-review-copy-receipt{color:var(--muted);font:11px/1.4 var(--mono);overflow-wrap:anywhere}
.lq-review-copy-frame,.lq-review-copy-pdf{display:block;width:100%;height:min(68vh,720px);
  border:1px solid var(--line);background:var(--paper)}.lq-review-copy-image{display:block;max-width:100%;
  max-height:70vh;width:auto;height:auto;margin:8px auto;border:1px solid var(--line);background:#fff;object-fit:contain}
.lq-needs-rendering{border:1px solid var(--amber);background:var(--amber-bg);color:var(--amber);padding:10px 12px}
.document-jump{display:inline-block;margin-top:5px}.image-confirmation-blocked{border:1px solid var(--amber);
  background:var(--amber-bg);color:var(--amber);border-radius:2px;padding:10px 12px;margin:10px 0}
.rbtn{border:1px solid var(--line);background:var(--paper);color:var(--ink);
  border-radius:4px;padding:3px 9px;font-size:13px;cursor:pointer}
.rbtn[aria-pressed=true]{background:var(--blueback);border-color:var(--blueback);
  color:var(--lq-primary-foreground)}.rbtn[data-ruling=privileged][aria-pressed=true]{background:var(--redact);
  border-color:var(--redact);color:#fff}.note{width:100%;margin-top:7px}
.redaction .bar{display:block;background:var(--redact);color:transparent;
  border-radius:1px;padding:6px 12px;user-select:none;font:15.5px var(--serif)}
.redaction .why{display:block;color:var(--red);font:11px var(--mono);
  text-transform:uppercase;letter-spacing:.12em;margin-top:3px}
.also{margin-top:9px}.also-list{list-style:none;padding:0;margin:7px 0}
.banner{border-radius:2px;padding:8px 12px;font-size:13.5px;margin:8px 0}
.banner.attention{background:var(--amber-bg);color:var(--amber)}
.banner.privilege{background:var(--red-bg);color:var(--red)}
.drawers{margin:22px 0}.drawer{background:var(--paper);border:1px solid var(--line);
  border-radius:2px;padding:9px 12px;margin:8px 0}.drawer>summary{font-weight:500}
.drawer-list{list-style:none;margin:8px 0 0;padding:0}.drawer-list li{border-top:1px dashed var(--line);
  padding:7px 0}.staged{border:1px dashed var(--line);padding:9px 12px;margin:14px 0}
.exportbox{margin:14px 0 40px}.exportbox textarea{width:100%;height:190px;
  font:12px/1.4 var(--mono)}.status{min-height:1.5em;color:var(--muted);font-size:13px}
button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,
summary:focus-visible{outline:2px solid var(--focus);outline-offset:2px}
@media (prefers-reduced-motion: reduce){*{transition:none!important;scroll-behavior:auto!important}}
@media (max-width:640px){header,main{padding-left:12px;padding-right:12px}h1{font-size:22px}
  .rowhead{flex-wrap:wrap}.pills{width:100%}.toolbar select{max-width:100%}}
"""

JS = r"""
"use strict";
const DATA=JSON.parse(document.getElementById("review-data").textContent);
const BINDINGS=DATA.bindings;
const REVIEW_READY=DATA.review_ready;
const REVIEW_LOCK_REASON=DATA.review_lock_reason||"Decisions and export are locked until every displayed document has a verified review copy.";
const FINDINGS=new Map(DATA.findings.map(row=>[row.finding_id,row]));
const IMAGE_SUBJECTS=new Map(DATA.image_confirmation_subjects.map(row=>[row.doc_id,row]));
const state={tab:"requests",focus:0,search:"",instrument:"all",
  filters:{responsiveOnly:true,empty:false,eyes:false,unread:false,privilege:false},rulings:{},imageConfirmations:{}};
for(const row of DATA.findings){if(row.lawyer_ruling){state.rulings[row.finding_id]={
  ruling:row.lawyer_ruling.ruling,note:row.lawyer_ruling.note||""};}}
for(const row of DATA.image_confirmations){state.imageConfirmations[row.doc_id]={
  confirmation:row.confirmation,note:row.note||""};}
const $=selector=>document.querySelector(selector);
const $$=selector=>Array.from(document.querySelectorAll(selector));
function visibleRows(){return $$(`[data-row]:not([hidden])`).filter(row=>!row.closest("[hidden]"));}
function setStatus(message){$("#review-status").textContent=message;}
function setTab(name){state.tab=name;state.focus=0;
  for(const button of $$("[role=tab]")){const on=button.dataset.tab===name;
    button.setAttribute("aria-selected",String(on));button.tabIndex=on?0:-1;}
  $("#panel-requests").hidden=name!=="requests";$("#panel-documents").hidden=name!=="documents";
  $("#sort-select").innerHTML=name==="requests"?
    '<option value="order">Request order</option><option value="matches">Most responsive first</option><option value="unruled">Unruled first</option>':
    '<option value="order">Production order</option><option value="matches">Most requests matched</option><option value="attention">Needs attention first</option>';
  $("#sort-select").value="order";sortRows("order");applyFilters();}
function cardVisible(card){const status=card.dataset.status;
  if(state.filters.eyes&&!card.dataset.needsEyes)return false;
  if(state.filters.privilege&&!card.dataset.privilege)return false;
  const categoryOverride=state.filters.empty||state.filters.eyes||state.filters.unread||state.filters.privilege;
  return status==="present"||!state.filters.responsiveOnly||categoryOverride;}
function applyFilters(){const query=state.search.toLowerCase();
  for(const row of $$("#panel-requests .request-row")){let show=!query||row.dataset.search.toLowerCase().includes(query);
    if(state.instrument!=="all"&&row.dataset.instrument!==state.instrument)show=false;
    const categoryOverride=state.filters.empty||state.filters.eyes||state.filters.unread||state.filters.privilege;
    if(state.filters.responsiveOnly&&!categoryOverride&&row.dataset.hasResponsive!=="true")show=false;
    if(state.filters.empty&&row.dataset.empty!=="true")show=false;if(state.filters.eyes&&row.dataset.needsEyes!=="true")show=false;
    if(state.filters.unread&&row.dataset.unread!=="true")show=false;if(state.filters.privilege&&row.dataset.privilege!=="true")show=false;
    row.hidden=!show;for(const card of row.querySelectorAll("[data-finding-card]"))card.hidden=!cardVisible(card);}
  for(const row of $$("#panel-documents .document-row")){let show=!query||row.dataset.search.toLowerCase().includes(query);
    const categoryOverride=state.filters.empty||state.filters.eyes||state.filters.unread||state.filters.privilege;
    if(state.filters.responsiveOnly&&!categoryOverride&&row.dataset.hasResponsive!=="true")show=false;
    if(state.filters.empty&&row.dataset.empty!=="true")show=false;if(state.filters.eyes&&row.dataset.needsEyes!=="true")show=false;
    if(state.filters.unread&&row.dataset.unread!=="true")show=false;if(state.filters.privilege&&row.dataset.privilege!=="true")show=false;row.hidden=!show;}
  for(const chip of $$("[data-filter]")){chip.setAttribute("aria-pressed",String(state.filters[chip.dataset.filter]));}
  const panel=state.tab==="requests"?$("#panel-requests"):$("#panel-documents"),selector=state.tab==="requests"?".request-row":".document-row";
  const rows=Array.from(panel.querySelectorAll(selector)),shown=rows.filter(row=>!row.hidden).length,noun=state.tab==="requests"?"requests":"documents";
  $("#filter-count").textContent=`Showing ${shown} of ${rows.length} ${noun}.`;applyFocus();}
function applyFocus(){const rows=visibleRows();if(state.focus>=rows.length)state.focus=Math.max(0,rows.length-1);
  rows.forEach((row,index)=>row.classList.toggle("keyboard-focus",index===state.focus));}
function syncRuling(findingId){const current=state.rulings[findingId]||null;
  for(const card of $$(`[data-finding-card][data-finding-id="${CSS.escape(findingId)}"]`)){card.dataset.existingRuling=current?current.ruling:"";
    for(const button of card.querySelectorAll("[data-ruling]"))button.setAttribute("aria-pressed",String(!!current&&current.ruling===button.dataset.ruling));
    const note=card.querySelector("[data-ruling-note]");if(note){note.hidden=!current;note.value=current?current.note:"";}
    const normal=card.querySelector("[data-quote-normal]"),redaction=card.querySelector("[data-redaction]");
    const privileged=!!current&&current.ruling==="privileged";if(normal)normal.hidden=privileged;if(redaction)redaction.hidden=!privileged;}}
function setRuling(findingId,ruling){const current=state.rulings[findingId];
  if(!REVIEW_READY){setStatus(REVIEW_LOCK_REASON);return;}
  if(current&&current.ruling===ruling)delete state.rulings[findingId];else state.rulings[findingId]={ruling,note:current?current.note:""};syncRuling(findingId);}
function syncImageConfirmation(docId){const current=state.imageConfirmations[docId]||null;
  for(const box of $$(`[data-image-confirmation-subject="${CSS.escape(docId)}"]`)){box.dataset.existingImageConfirmation=current?current.confirmation:"";
    for(const button of box.querySelectorAll("[data-image-confirmation]"))button.setAttribute("aria-pressed",String(!!current&&current.confirmation===button.dataset.imageConfirmation));
    const note=box.querySelector("[data-image-confirmation-note]");if(note){note.hidden=!current;note.value=current?current.note:"";}
    const status=box.querySelector("[data-image-confirmation-status]");if(status)status.textContent=!current?"Page review not finished":current.confirmation==="confirmed"?"Page review complete":"Page review needs more work";}}
function setImageConfirmation(docId,confirmation){const current=state.imageConfirmations[docId];
  if(!REVIEW_READY){setStatus(REVIEW_LOCK_REASON);return;}
  if(current&&current.confirmation===confirmation)delete state.imageConfirmations[docId];else state.imageConfirmations[docId]={confirmation,note:current?current.note:""};syncImageConfirmation(docId);}
function acceptRequest(issueId){if(!REVIEW_READY){setStatus(REVIEW_LOCK_REASON);return;}
  for(const row of DATA.findings.filter(item=>item.issue_id===issueId)){
  const ruling=row.status==="present"?"responsive":row.status==="absent"?"not-responsive":"needs-review";
  state.rulings[row.finding_id]={ruling,note:""};syncRuling(row.finding_id);}setStatus("Machine findings copied into your explicit rulings for this request.");}
function buildExport(){const rulings=Object.keys(state.rulings).sort().map(findingId=>{const row=FINDINGS.get(findingId),choice=state.rulings[findingId];
  return {finding_id:findingId,issue_id:row.issue_id,doc_id:row.doc_id,machine_status:row.status,ruling:choice.ruling,note:choice.note||"",ruled_by:"lawyer"};});
  const image_confirmations=Object.keys(state.imageConfirmations).sort().map(docId=>{const subject=IMAGE_SUBJECTS.get(docId),choice=state.imageConfirmations[docId];
    return {confirmation:choice.confirmation,confirmed_by:"lawyer",doc_id:docId,finding_ids:subject.finding_ids,note:choice.note||"",proposal_digest:subject.proposal_digest};});
  return JSON.stringify({artifact:"review-feedback",version:1,review_plan_id:BINDINGS.review_plan_id,
    framework_version:BINDINGS.framework_version,framework_digest:BINDINGS.framework_digest,frame_id:BINDINGS.frame_id,
    corpus_id:BINDINGS.corpus_id,ledger_digest:BINDINGS.ledger_digest,source:BINDINGS.source,image_confirmations,rulings},null,2)+"\n";}
function exportFeedback(){if(!REVIEW_READY){setStatus(REVIEW_LOCK_REASON);return;}
  const value=buildExport(),box=$("#export-box"),area=$("#export-text");box.hidden=false;area.value=value;area.focus();area.select();
  try{const blob=new Blob([value],{type:"application/json"}),url=URL.createObjectURL(blob),link=document.createElement("a");link.href=url;link.download="review-feedback.json";link.click();setTimeout(()=>URL.revokeObjectURL(url),0);}catch(error){}
  setStatus(`Prepared ${Object.keys(state.rulings).length} lawyer ruling(s) and ${Object.keys(state.imageConfirmations).length} scanned-file review decision(s).`);}
function sortRows(value){const panel=state.tab==="requests"?$("#panel-requests"):$("#panel-documents");
  const containers=state.tab==="requests"?Array.from(panel.querySelectorAll(".request-group")):[panel];for(const container of containers){
  const rows=Array.from(container.children).filter(child=>child.classList.contains(state.tab==="requests"?"request-row":"document-row"));rows.sort((a,b)=>{
    if(value==="matches")return Number(b.dataset.matches)-Number(a.dataset.matches)||a.dataset.order.localeCompare(b.dataset.order);
    if(value==="unruled")return Number(a.dataset.ruled)-Number(b.dataset.ruled)||a.dataset.order.localeCompare(b.dataset.order);
    if(value==="attention")return Number(b.dataset.attention)-Number(a.dataset.attention)||a.dataset.order.localeCompare(b.dataset.order);
    return a.dataset.order.localeCompare(b.dataset.order);});for(const row of rows)container.appendChild(row);}applyFocus();}
document.addEventListener("click",event=>{const target=event.target instanceof Element?event.target:event.target.parentElement;
  const jump=target?target.closest("[data-document-jump]"):null;if(jump){event.preventDefault();state.search="";$("#search").value="";for(const key of Object.keys(state.filters))state.filters[key]=false;setTab("documents");
    const row=document.getElementById(jump.dataset.documentJump);if(row){const toggle=row.querySelector("[data-toggle=document]"),body=toggle?document.getElementById(toggle.getAttribute("aria-controls")):null;
      if(toggle&&body){body.hidden=false;toggle.setAttribute("aria-expanded","true");}row.scrollIntoView({block:"start"});}return;}
  const button=target?target.closest("button"):null;if(!button)return;
  if(button.dataset.tab){setTab(button.dataset.tab);return;}if(button.dataset.toggle){const body=document.getElementById(button.getAttribute("aria-controls"));body.hidden=!body.hidden;button.setAttribute("aria-expanded",String(!body.hidden));return;}
  if(button.dataset.filter){const key=button.dataset.filter,next=!state.filters[key];
    for(const name of Object.keys(state.filters))state.filters[name]=false;state.filters[key]=next;
    if(["eyes","unread","privilege"].includes(key))setTab("documents");else applyFilters();return;}
  if(button.dataset.summaryFilter){for(const key of Object.keys(state.filters))state.filters[key]=false;const key=button.dataset.summaryFilter;state.filters[key]=true;
    if(key==="unread")$("#attention-drawer").open=true;if(key==="privilege")$("#privilege-drawer").open=true;
    setTab(["eyes","unread","privilege"].includes(key)?"documents":"requests");return;}
  if(button.dataset.ruling){setRuling(button.dataset.findingId,button.dataset.ruling);return;}if(button.dataset.acceptRequest){acceptRequest(button.dataset.acceptRequest);return;}
  if(button.dataset.imageConfirmation){setImageConfirmation(button.dataset.docId,button.dataset.imageConfirmation);return;}
  if(button.id==="export-button")exportFeedback();});
document.addEventListener("input",event=>{if(event.target.id==="search"){state.search=event.target.value;applyFilters();}
  if(event.target.dataset.rulingNote){const id=event.target.dataset.rulingNote;if(state.rulings[id])state.rulings[id].note=event.target.value;}
  if(event.target.dataset.imageConfirmationNote){const id=event.target.dataset.imageConfirmationNote;if(state.imageConfirmations[id])state.imageConfirmations[id].note=event.target.value;}});
document.addEventListener("change",event=>{if(event.target.id==="instrument-select"){state.instrument=event.target.value;applyFilters();}
  if(event.target.id==="sort-select")sortRows(event.target.value);});
document.addEventListener("keydown",event=>{if(event.target.matches("[role=tab]")&&["ArrowLeft","ArrowRight","Home","End"].includes(event.key)){
  event.preventDefault();const tabs=$$("[role=tab]"),index=tabs.indexOf(event.target),next=event.key==="Home"?0:event.key==="End"?tabs.length-1:(index+(event.key==="ArrowRight"?1:-1)+tabs.length)%tabs.length;
  setTab(tabs[next].dataset.tab);tabs[next].focus();return;}
  if(event.target.matches("input,textarea,select")){if(event.key==="Escape")event.target.blur();return;}
  const rows=visibleRows();if(event.key==="j"||event.key==="k"){event.preventDefault();state.focus=Math.max(0,Math.min(rows.length-1,state.focus+(event.key==="j"?1:-1)));applyFocus();rows[state.focus]?.scrollIntoView({block:"nearest"});}
  else if(event.key==="Enter"||event.key==="o"){rows[state.focus]?.querySelector("[data-toggle]")?.click();}else if(event.key==="/"){event.preventDefault();$("#search").focus();}
  else if(event.key==="e")exportFeedback();else if(event.key==="[")setTab("requests");else if(event.key==="]")setTab("documents");
  else if(["1","2","3","4"].includes(event.key)){const card=rows[state.focus]?.querySelector("[data-finding-card]:not([hidden])");if(card)setRuling(card.dataset.findingId,["responsive","not-responsive","needs-review","privileged"][Number(event.key)-1]);}});
for(const id of Object.keys(state.rulings))syncRuling(id);for(const id of IMAGE_SUBJECTS.keys())syncImageConfirmation(id);setTab("requests");
if(!REVIEW_READY){for(const button of $$('[data-ruling],[data-accept-request],[data-image-confirmation],#export-button')){button.disabled=true;button.setAttribute("aria-disabled","true");}
  setStatus(REVIEW_LOCK_REASON);}
"""


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def review_masthead(context: object) -> str:
    """Return the shared review masthead with DocReview-specific identity."""

    return (
        '<div class="lq-masthead" role="banner">'
        '<div class="lq-brand">LQ · Document Review</div>'
        f'<div class="lq-context"><span>{esc(context)}</span>{THEME_BUTTON}</div></div>'
    )


def fail(message: str) -> NoReturn:
    sys.exit(f"render_crosswalk: {message}")


def load(path: str, kind: str, required: tuple[str, ...]) -> JsonObject:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot read {kind} at {path}: {error}")
    if not isinstance(value, dict):
        fail(f"{kind} must be an object")
    for key in required:
        if key not in value:
            fail(f"{kind} missing key {key!r}")
    return cast(JsonObject, value)


def canonical_digest(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(raw.encode()).hexdigest()


def proposal_ledger(findings: dict) -> dict:
    proposal = json.loads(json.dumps(findings))
    proposal.pop("image_confirmations", None)
    for row in proposal.get("findings", []):
        if isinstance(row, dict):
            row.pop("lawyer_ruling", None)
    return proposal


def safe_json(value: object) -> str:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"))
        .replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
    )


def target_key(target: dict) -> tuple[str, str | None, int]:
    return (target["instrument_id"], target.get("series"), target["element"])


def target_sort_key(key: tuple[str, str | None, int]) -> tuple[str, str, int]:
    return (key[0], key[1] or "", key[2])


def designator(target: dict) -> str:
    series = target.get("series")
    return f"{series}-{target['element']}" if series else str(target["element"])


def instrument_display(instrument: dict) -> str:
    raw_kind = str(instrument.get("kind", "request"))
    kind = "Issues List" if raw_kind == "issues-list" else raw_kind.upper()
    words = re.sub(r"[_-]+", " ", Path(str(instrument.get("label", ""))).stem).strip()
    upper = words.upper()
    if upper.startswith(raw_kind.upper() + " "):
        return f"{kind} to {words.split(' ', 1)[1].strip().title()}"
    if upper.endswith(" " + raw_kind.upper()):
        return f"{kind} — {words.rsplit(' ', 1)[0].strip().title()}"
    return f"{kind} — {words.title()}" if words else kind


def request_label(issue: dict) -> str:
    return f"{issue['instrument_label']}, No. {designator(issue['target'])}"


def framework_index(framework: JsonObject):
    raw_frame = framework.get("frame")
    if not isinstance(raw_frame, dict) or raw_frame.get("kind") != "requests":
        fail("framework must have frame.kind 'requests'")
    frame = cast(JsonObject, raw_frame)
    instruments = frame.get("instruments")
    lenses = framework.get("lenses")
    if not isinstance(instruments, list) or not isinstance(lenses, list):
        fail("requests framework has invalid instruments or lenses")
    by_instrument: dict[str, JsonObject] = {}
    staged: list[JsonObject] = []
    for raw_instrument in cast(list[Any], instruments):
        if not isinstance(raw_instrument, dict):
            fail("frame instrument must be an object")
        instrument = cast(JsonObject, raw_instrument)
        instrument_id = instrument.get("instrument_id")
        if not isinstance(instrument_id, str) or instrument_id in by_instrument:
            fail("frame instrument IDs are missing or duplicated")
        if not isinstance(instrument.get("element_count"), int):
            fail(f"instrument {instrument_id!r} has invalid element_count")
        normalized = dict(instrument)
        normalized["display"] = instrument_display(instrument)
        by_instrument[instrument_id] = normalized
        if instrument.get("staged") is True:
            staged.append(normalized)
    issues: dict[str, JsonObject] = {}
    lens_issues: dict[str, list[str]] = {}
    seen_targets: set[tuple[str, str | None, int]] = set()
    for raw_lens in cast(list[Any], lenses):
        lens_id = raw_lens.get("lens_id") if isinstance(raw_lens, dict) else None
        if not isinstance(lens_id, str) or lens_id in lens_issues:
            fail("framework lens is invalid or duplicated")
        lens = cast(JsonObject, raw_lens)
        lens_issues[lens_id] = []
        items = lens.get("items")
        if not isinstance(items, list):
            fail(f"lens {lens_id!r} has no items array")
        for raw_item in cast(list[Any], items):
            issue_id = raw_item.get("issue_id") if isinstance(raw_item, dict) else None
            raw_target = (
                raw_item.get("target_ref") if isinstance(raw_item, dict) else None
            )
            if not isinstance(issue_id, str) or issue_id in issues:
                fail(f"lens {lens_id!r} has an invalid or repeated issue")
            if not isinstance(raw_target, dict):
                fail(f"requests item {issue_id!r} has no target_ref")
            item = cast(JsonObject, raw_item)
            target = cast(JsonObject, raw_target)
            instrument_id = target.get("instrument_id")
            element = target.get("element")
            series = target.get("series")
            instrument = by_instrument.get(instrument_id)
            if instrument is None or instrument.get("staged") is True:
                fail(
                    f"requests item {issue_id!r} targets an unknown or staged instrument"
                )
            if not isinstance(element, int) or isinstance(element, bool) or element < 1:
                fail(f"requests item {issue_id!r} has an invalid target element")
            if "series" in target and not (
                isinstance(series, str) and SERIES_PATTERN.fullmatch(series)
            ):
                fail(f"requests item {issue_id!r} has an invalid target series")
            normalized_target = {"instrument_id": instrument_id, "element": element}
            if series is not None:
                normalized_target["series"] = series
            key = target_key(normalized_target)
            if key in seen_targets:
                fail(f"target {key!r} is covered more than once")
            seen_targets.add(key)
            issues[issue_id] = {
                "instrument": instrument,
                "instrument_label": instrument["display"],
                "issue_id": issue_id,
                "lens_id": lens_id,
                "question": item.get("question", ""),
                "target": normalized_target,
            }
            lens_issues[lens_id].append(issue_id)
    for instrument_id, instrument in by_instrument.items():
        if instrument.get("staged") is not True:
            covered = sum(
                1
                for issue in issues.values()
                if issue["target"]["instrument_id"] == instrument_id
            )
            if covered != instrument["element_count"]:
                fail(
                    f"instrument {instrument_id!r} has {covered} targets, expected {instrument['element_count']}"
                )
    return frame, issues, lens_issues, by_instrument, staged


def manifest_index(manifest: JsonObject) -> dict[str, JsonObject]:
    rows = manifest.get("documents")
    if not isinstance(rows, list):
        fail("manifest documents must be an array")
    documents: dict[str, JsonObject] = {}
    normalized_rows = []
    for raw_row in cast(list[Any], rows):
        doc_id = raw_row.get("id") if isinstance(raw_row, dict) else None
        path = raw_row.get("path") if isinstance(raw_row, dict) else None
        if not isinstance(doc_id, str) or not isinstance(path, str):
            fail("manifest document IDs or paths are invalid")
        normalized_rows.append(cast(JsonObject, raw_row))
    for row in sorted(normalized_rows, key=lambda item: (item["id"], item["path"])):
        # A content-addressed manifest can contain the same bytes at more than
        # one production path. Show one stable representative, matching the
        # deterministic source selection used by the findings merger.
        documents.setdefault(cast(str, row["id"]), row)
    return documents


def privilege_index(queue: JsonObject | None, documents: dict[str, JsonObject]):
    if queue is None:
        return set(), {}
    candidates = queue.get("candidates")
    ruled = queue.get("ruled")
    if not isinstance(candidates, list) or not isinstance(ruled, list):
        fail("privilege queue candidates and ruled must be arrays")
    by_doc: dict[str, list[JsonObject]] = {}
    rulings: dict[str, Any] = {}
    for raw_row in cast(list[Any], ruled):
        doc_id = raw_row.get("doc_id") if isinstance(raw_row, dict) else None
        if not isinstance(doc_id, str) or doc_id not in documents:
            fail("privilege ruling references an unknown document")
        row = cast(JsonObject, raw_row)
        rulings[doc_id] = row.get("ruling")
        by_doc.setdefault(doc_id, []).append({**row, "queue_state": "ruled"})
    held: set[str] = set()
    for raw_row in cast(list[Any], candidates):
        doc_id = raw_row.get("doc_id") if isinstance(raw_row, dict) else None
        if not isinstance(doc_id, str) or doc_id not in documents:
            fail("privilege candidate references an unknown document")
        row = cast(JsonObject, raw_row)
        by_doc.setdefault(doc_id, []).append({**row, "queue_state": "candidate"})
        if rulings.get(doc_id) != "not-privileged":
            held.add(doc_id)
    held.update(
        doc_id
        for doc_id, ruling in rulings.items()
        if ruling in {"privileged", "needs-review"}
    )
    return held, by_doc


def compile_rows(
    findings: JsonObject,
    issues: dict[str, JsonObject],
    lens_issues: dict[str, list[str]],
    documents: dict[str, JsonObject],
    queue_held: set[str],
):
    rows = findings.get("findings")
    parked = findings.get("parked", [])
    if not isinstance(rows, list) or not isinstance(parked, list):
        fail("findings and parked must be arrays")
    by_issue: dict[str, dict[str, Any]] = {
        issue_id: {
            "present": [],
            "absent": [],
            "unresolved": [],
            "held": set(),
            "parked": {},
        }
        for issue_id in issues
    }
    by_doc: dict[str, dict[str, Any]] = {
        doc_id: {
            "present": [],
            "absent": [],
            "unresolved": [],
            "held_issues": set(),
            "parked_issues": {},
        }
        for doc_id in documents
    }
    seen: set[str] = set()
    reviewed_docs: set[str] = set()
    for raw_row in cast(list[Any], rows):
        if not isinstance(raw_row, dict):
            fail("finding row must be an object")
        row = cast(JsonObject, raw_row)
        issue_id, doc_id, status = (
            row.get("issue_id"),
            row.get("doc_id"),
            row.get("status"),
        )
        finding_id = row.get("finding_id")
        if not isinstance(issue_id, str) or issue_id not in issues:
            fail(f"finding references unknown issue_id {issue_id!r}")
        if not isinstance(doc_id, str) or doc_id not in documents:
            fail(f"finding references document absent from manifest: {doc_id!r}")
        if not isinstance(status, str) or status not in {
            "present",
            "absent",
            "unresolved",
        }:
            fail(f"finding for {issue_id!r} has invalid status {status!r}")
        expected_id = f"{issue_id}/{doc_id}"
        if not isinstance(finding_id, str) or not finding_id:
            fail(f"finding for {issue_id!r} is missing its stable finding_id")
        if finding_id != expected_id or finding_id in seen:
            fail(f"finding has invalid or repeated stable ID {finding_id!r}")
        seen.add(finding_id)
        overlay = row.get("lawyer_ruling")
        if overlay is not None and (
            not isinstance(overlay, dict)
            or set(overlay) != {"note", "ruled_by", "ruling"}
            or overlay.get("ruling") not in RULINGS
            or overlay.get("ruled_by") != "lawyer"
            or not isinstance(overlay.get("note"), str)
        ):
            fail(f"finding {finding_id!r} has an invalid lawyer_ruling overlay")
        reviewed_docs.add(doc_id)
        if doc_id in queue_held:
            by_issue[issue_id]["held"].add(doc_id)
            by_doc[doc_id]["held_issues"].add(issue_id)
            continue
        by_issue[issue_id][status].append(row)
        by_doc[doc_id][status].append(row)
    for raw_row in cast(list[Any], parked):
        if not isinstance(raw_row, dict):
            fail("parked entry must be an object")
        row = cast(JsonObject, raw_row)
        lens_id, members, reason = (
            row.get("lens_id"),
            row.get("member_ids"),
            row.get("reason"),
        )
        if (
            not isinstance(lens_id, str)
            or lens_id not in lens_issues
            or not isinstance(members, list)
            or not isinstance(reason, str)
            or not reason
        ):
            fail("parked entry is invalid")
        for doc_id in cast(list[Any], members):
            if not isinstance(doc_id, str) or doc_id not in documents:
                fail(f"parked entry references unknown document {doc_id!r}")
            reviewed_docs.add(doc_id)
            for issue_id in lens_issues[lens_id]:
                if reason == HOLD_REASON:
                    by_issue[issue_id]["held"].add(doc_id)
                    by_doc[doc_id]["held_issues"].add(issue_id)
                else:
                    by_issue[issue_id]["parked"].setdefault(doc_id, set()).add(reason)
                    by_doc[doc_id]["parked_issues"].setdefault(issue_id, set()).add(
                        reason
                    )
    for buckets in by_issue.values():
        for status in ("present", "absent", "unresolved"):
            buckets[status].sort(
                key=lambda row: (
                    documents[row["doc_id"]].get("path", ""),
                    row["finding_id"],
                )
            )
    return by_issue, by_doc, reviewed_docs


def matter_label(manifest: dict, frame: dict) -> str:
    root = re.sub(r"[_-]+", " ", str(manifest.get("root_label", ""))).strip()
    if root and root.lower() not in {"room", "production", "documents"}:
        return root
    frame_id = str(frame.get("frame_id", "production"))
    base = re.sub(r"-(?:rfp|rfa|srog|requests?)-(?:audit|review)$", "", frame_id)
    base = re.sub(r"[_-]+", " ", base).strip().title()
    return f"{base} production" if base else "Production"


def production_number(document: dict) -> str:
    match = PRODUCTION_NUMBER.match(Path(str(document.get("path", ""))).name)
    return match.group(1) if match else "—"


def document_sort(document: dict):
    number = production_number(document)
    return (
        (0, int(number), str(document.get("path", "")))
        if number.isdigit()
        else (1, number, str(document.get("path", "")))
    )


def document_type(document: dict) -> str:
    ext = str(
        document.get("ext") or Path(str(document.get("path", ""))).suffix.lstrip(".")
    ).upper()
    readability, pages = str(document.get("readability", "")), document.get("pages")
    if readability == "scanned" and ext in {"PNG", "JPG", "JPEG", "TIFF", "TIF"}:
        phrase = f"{ext} image"
    elif readability == "scanned":
        phrase = f"Scanned {ext or 'document'}"
    elif readability == "native":
        phrase = f"Native {ext or 'document'}"
    else:
        phrase = ext or "File"
    if isinstance(pages, int):
        phrase += f", {pages} page" + ("s" if pages != 1 else "")
    return phrase


def document_source_index(
    documents: dict[str, JsonObject],
    document_root: Path | None,
    required: set[str],
    output_parent: Path,
) -> dict[str, JsonObject]:
    if document_root is None:
        if required:
            fail(
                "image-review documents require --document-root so the lawyer can inspect the source before confirming"
            )
        return {}
    root = document_root.expanduser().resolve()
    if not root.is_dir():
        fail(f"document root is not a directory: {document_root}")
    sources: dict[str, JsonObject] = {}
    for doc_id, document in documents.items():
        raw_path = document.get("path")
        if not isinstance(raw_path, str) or not raw_path:
            if doc_id in required:
                fail(f"image-review document {doc_id!r} has no source path")
            continue
        relative = Path(raw_path)
        if relative.is_absolute():
            fail(
                f"manifest document path must be relative to --document-root: {raw_path}"
            )
        candidate = (root / relative).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            fail(f"manifest document path escapes --document-root: {raw_path}")
        if not candidate.is_file():
            if doc_id in required:
                fail(f"image-review source document does not exist: {raw_path}")
            continue
        sources[doc_id] = {
            "href": urllib.parse.quote(
                Path(os.path.relpath(candidate, output_parent)).as_posix(), safe="/"
            ),
        }
    return sources


def reject_source_output_alias(
    manifest: JsonObject, document_root: Path | None, output_path: Path
) -> None:
    if document_root is None:
        return
    root = document_root.expanduser().resolve()
    rows = manifest.get("documents", [])
    if not isinstance(rows, list):
        fail("manifest documents must be an array")
    for row in cast(list[Any], rows):
        raw_path = row.get("path") if isinstance(row, dict) else None
        if not isinstance(raw_path, str) or not raw_path:
            continue
        relative = Path(raw_path)
        if relative.is_absolute():
            fail(f"manifest document path must be relative: {raw_path}")
        candidate = (root / relative).resolve()
        try:
            candidate.relative_to(root)
        except ValueError:
            fail(f"manifest document path escapes --document-root: {raw_path}")
        if candidate == output_path:
            fail("--out must not overwrite a manifest source document")


def source_link_html(document: JsonObject, source: JsonObject) -> str:
    path = str(document.get("path", "document"))
    return (
        f'<a class="source-link" href="{esc(source["href"])}" target="_blank" rel="noopener" '
        f'aria-label="Open source document: {esc(path)}">Open source document ↗</a>'
    )


def document_anchor(doc_id: str) -> str:
    return f"document-card-{hashlib.sha256(doc_id.encode()).hexdigest()[:12]}"


def document_jump_link_html(document: JsonObject, doc_id: str) -> str:
    anchor = document_anchor(doc_id)
    path = str(document.get("path", "document"))
    return (
        f'<a class="source-link document-jump" href="#{anchor}" '
        f'data-document-jump="{anchor}" aria-label="Review document in this page: {esc(path)}">'
        "Review document in this page →</a>"
    )


def review_copy_entry(
    validation: Any | None, doc_id: str, path: str
) -> JsonObject | None:
    if validation is None or not validation.integrity_ok or validation.sidecar is None:
        return None
    matches = [
        row
        for row in validation.sidecar["documents"]
        if row.get("doc_id") == doc_id and row.get("path") == path
    ]
    return cast(JsonObject, matches[0]) if len(matches) == 1 else None


def review_copy_ready(validation: Any | None, doc_id: str, path: str) -> bool:
    entry = review_copy_entry(validation, doc_id, path)
    return bool(entry and entry.get("status") == "ready")


def blocked_review_copy_ids(
    validation: Any | None, documents: dict[str, JsonObject]
) -> set[str]:
    """Return every content ID with any missing or unready manifest path."""

    if validation is None or not validation.integrity_ok or validation.sidecar is None:
        return set(documents)
    blocked = {
        str(row.get("doc_id"))
        for row in validation.sidecar["documents"]
        if row.get("status") != "ready"
    }
    blocked.update(
        doc_id
        for doc_id, document in documents.items()
        if not review_copy_ready(validation, doc_id, str(document.get("path", "")))
    )
    return blocked


def review_copy_html(validation: Any | None, doc_id: str, document: JsonObject) -> str:
    path = str(document.get("path", ""))
    if validation is None:
        return (
            '<div class="lq-review-copy lq-needs-rendering" role="alert">'
            "<strong>Needs rendering</strong> No verified review-copy sidecar was supplied."
            "</div>"
        )
    return str(
        REVIEW_COPIES.render_review_copy_component(
            validation,
            doc_id,
            path=path,
            title=Path(path).name or "Document review copy",
        )
    )


def needs_image_review(row: dict) -> bool:
    verification = row.get("quote_verification")
    reason = row.get("human_review_reason")
    return bool(
        row.get("receipt_mode") == "image-transcription"
        or (isinstance(reason, str) and "image" in reason.lower())
        or (
            isinstance(verification, dict)
            and verification.get("status") == "human-required"
            and "image" in str(verification.get("reason", "")).lower()
        )
    )


def needs_eyes(row: dict) -> bool:
    verification = row.get("quote_verification")
    return bool(
        row.get("status") == "present"
        and (
            row.get("receipt_mode") == "image-transcription"
            or (
                isinstance(verification, dict)
                and verification.get("status") == "human-required"
            )
        )
    )


def image_confirmation_subjects(findings: JsonObject) -> dict[str, JsonObject]:
    proposal = proposal_ledger(findings)
    grouped: dict[str, list[JsonObject]] = {}
    for raw_row in cast(list[Any], proposal.get("findings", [])):
        if not isinstance(raw_row, dict):
            fail("findings ledger contains a non-object finding")
        row = cast(JsonObject, raw_row)
        if not needs_image_review(row):
            continue
        doc_id = row.get("doc_id")
        finding_id = row.get("finding_id")
        if not isinstance(doc_id, str) or not isinstance(finding_id, str):
            fail("image-review finding has an invalid subject")
        grouped.setdefault(doc_id, []).append(row)
    subjects: dict[str, JsonObject] = {}
    for doc_id, rows in grouped.items():
        ordered = sorted(rows, key=lambda row: row["finding_id"])
        subjects[doc_id] = {
            "doc_id": doc_id,
            "finding_ids": [row["finding_id"] for row in ordered],
            "proposal_digest": canonical_digest(ordered),
        }
    return subjects


def image_confirmation_index(
    findings: JsonObject, subjects: dict[str, JsonObject]
) -> dict[str, JsonObject]:
    raw_rows = findings.get("image_confirmations", [])
    if not isinstance(raw_rows, list):
        fail("findings image_confirmations overlay must be an array")
    indexed: dict[str, JsonObject] = {}
    for index, raw_row in enumerate(cast(list[Any], raw_rows)):
        if not isinstance(raw_row, dict) or set(raw_row) != IMAGE_CONFIRMATION_KEYS:
            fail(f"image confirmation overlay {index} has invalid shape")
        row = cast(JsonObject, raw_row)
        doc_id = row.get("doc_id")
        if not isinstance(doc_id, str) or doc_id in indexed:
            fail(f"image confirmation overlay {index} has invalid document identity")
        subject = subjects.get(doc_id)
        if subject is None:
            fail(f"image confirmation references non-image document {doc_id!r}")
        if row.get("confirmation") not in IMAGE_CONFIRMATIONS:
            fail(f"image confirmation for {doc_id!r} is invalid")
        if row.get("confirmed_by") != "lawyer":
            fail(f"image confirmation for {doc_id!r} is not lawyer-authored")
        if not isinstance(row.get("note"), str):
            fail(f"image confirmation for {doc_id!r} has an invalid note")
        if row.get("finding_ids") != subject["finding_ids"]:
            fail(f"image confirmation for {doc_id!r} has stale finding IDs")
        if row.get("proposal_digest") != subject["proposal_digest"]:
            fail(f"image confirmation for {doc_id!r} has a stale proposal digest")
        indexed[doc_id] = row
    return indexed


def image_confirmation_controls(
    subject: JsonObject,
    existing: JsonObject | None,
) -> str:
    doc_id = str(subject["doc_id"])
    current = str(existing.get("confirmation", "")) if existing else ""
    note = str(existing.get("note", "")) if existing else ""
    count = len(cast(list[Any], subject["finding_ids"]))
    status = (
        "Page review complete"
        if current == "confirmed"
        else "Page review needs more work"
        if current == "needs-review"
        else "Page review not finished"
    )
    return (
        f'<section class="image-confirmation" data-image-confirmation-subject="{esc(doc_id)}" '
        f'data-existing-image-confirmation="{esc(current)}">'
        '<div class="docname">Confirm this scanned file was reviewed completely</div>'
        "<p>This file was read from page images rather than searchable text. "
        "Open the review copy, inspect every page, and compare it with the results "
        "listed below. Mark the page review complete only if no responsive request "
        "was missed.</p>"
        f'<details class="receipt"><summary>What this confirmation covers</summary>This file was compared with {count} request'
        f"{'s' if count != 1 else ''}. Confirming records your review without changing the machine results.</details>"
        '<div class="ruling" role="group" aria-label="Scanned-file page review">'
        f'<button class="rbtn" type="button" data-image-confirmation="confirmed" data-doc-id="{esc(doc_id)}" aria-pressed="{str(current == "confirmed").lower()}">Page review complete</button>'
        f'<button class="rbtn" type="button" data-image-confirmation="needs-review" data-doc-id="{esc(doc_id)}" aria-pressed="{str(current == "needs-review").lower()}">Something is missing</button>'
        f'<span class="ruling-label" data-image-confirmation-status="">{esc(status)}</span></div>'
        f'<input class="note" type="text" maxlength="500" data-image-confirmation-note="{esc(doc_id)}" value="{esc(note)}" placeholder="Optional page-review note" aria-label="Optional page-review note"'
        f"{'' if existing else ' hidden'}></section>"
    )


def blocked_image_confirmation_controls(
    subject: JsonObject, existing: JsonObject | None
) -> str:
    doc_id = str(subject["doc_id"])
    current = str(existing.get("confirmation", "")) if existing else ""
    return (
        f'<section class="image-confirmation-blocked" role="alert" '
        f'data-image-confirmation-subject="{esc(doc_id)}" '
        f'data-existing-image-confirmation="{esc(current)}">'
        '<div class="docname">Page review is unavailable</div>'
        "<p>The verified in-page copy must be available before you can confirm "
        "that every page was reviewed. Rebuild the review copies, then rerender this page.</p>"
        "</section>"
    )


def unresolved_document_notice(doc_rows: dict[str, Any]) -> str:
    if doc_rows["present"] or doc_rows["absent"]:
        return (
            "The review could not determine whether this file responds to one or "
            "more requests. Open the file and review the questions listed below."
        )
    return (
        "The review could not confidently match this file to any request. Open "
        "the file and review the machine explanation before deciding."
    )


def identity_excerpt(doc_rows: dict):
    confirmed, unverified = [], []
    for row in doc_rows["present"]:
        quote = row.get("quote")
        if not isinstance(quote, str) or not quote:
            continue
        verification = row.get("quote_verification") or {}
        (confirmed if verification.get("status") == "confirmed" else unverified).append(
            quote
        )
    choices = confirmed or unverified
    if not choices:
        return None, False
    choices.sort(key=lambda value: (-len(value), value))
    return choices[0], not bool(confirmed)


def receipt_html(row: dict) -> str:
    parts = [
        f"finding {esc(row['finding_id'])}",
        f"document {esc(row['doc_id'])}",
        f"machine status {esc(row['status'])}",
    ]
    if row.get("receipt_mode"):
        parts.append(f"receipt {esc(row['receipt_mode'])}")
    return (
        '<details class="receipt"><summary>Receipt</summary>'
        + " · ".join(parts)
        + "</details>"
    )


def ruling_controls(row: dict, *, enabled: bool) -> str:
    existing = row.get("lawyer_ruling") or {}
    current = existing.get("ruling", "")
    labels = (
        ("responsive", "Responsive"),
        ("not-responsive", "Not responsive"),
        ("needs-review", "Needs review"),
        ("privileged", "Privileged"),
    )
    buttons = []
    disabled = "" if enabled else ' disabled aria-disabled="true"'
    for index, (value, label) in enumerate(labels, 1):
        buttons.append(
            '<button class="rbtn" type="button" data-ruling="{}" data-finding-id="{}" aria-pressed="{}" title="Keyboard {}"{}>{}</button>'.format(
                value,
                esc(row["finding_id"]),
                str(current == value).lower(),
                index,
                disabled,
                label,
            )
        )
    hidden = "" if current else " hidden"
    return (
        '<div class="ruling" role="group" aria-label="Your ruling"><span class="ruling-label">Your ruling:</span>'
        + "".join(buttons)
        + f'</div><input class="note" type="text" maxlength="500" data-ruling-note="{esc(row["finding_id"])}" '
        f'value="{esc(existing.get("note", ""))}" placeholder="Optional note" aria-label="Optional ruling note"{disabled}{hidden}>'
    )


def finding_card(
    row: dict,
    document: dict,
    label: str,
    question: str,
    *,
    decision_enabled: bool,
    default_visible: bool = False,
    show_document: bool = True,
) -> str:
    eye = needs_eyes(row)
    existing = row.get("lawyer_ruling") or {}
    privileged = existing.get("ruling") == "privileged"
    status = row["status"]
    status_label = {
        "present": "Responsive",
        "absent": "Nothing found",
        "unresolved": "Needs a decision",
    }[status]
    path = str(document.get("path", ""))
    search = " ".join(
        str(value or "")
        for value in (
            label,
            question,
            path,
            row.get("quote"),
            row.get("characterization"),
        )
    )
    attrs = [
        'class="doccard"',
        'data-finding-card=""',
        f'data-finding-id="{esc(row["finding_id"])}"',
        f'data-status="{esc(status)}"',
        f'data-existing-ruling="{esc(existing.get("ruling", ""))}"',
        f'data-search="{esc(search.lower())}"',
    ]
    if default_visible:
        attrs.append('data-default-visible="true"')
    if eye:
        attrs.append('data-needs-eyes="true"')
    if privileged:
        attrs.append('data-privilege="true"')
    parts = [f"<article {' '.join(attrs)}>"]
    if show_document:
        jump = document_jump_link_html(document, str(row["doc_id"]))
        parts.append(
            f'<div class="docname"><span class="bates">NO. {esc(production_number(document))}</span> {esc(path)}</div>'
            f'<div class="docdesc">{esc(document_type(document))}</div>{jump}'
        )
    parts.append(
        f'<span class="pill {"responsive" if status == "present" else "neutral"}">Machine: {status_label}</span>'
    )
    if status == "present":
        quote, section, page = (
            str(row.get("quote") or ""),
            row.get("section"),
            row.get("page"),
        )
        verified = (row.get("quote_verification") or {}).get("status") == "confirmed"
        cite = []
        if page is not None:
            cite.append(f"Page {esc(page)}")
        if section:
            cite.append(esc(section))
        badge = (
            '<span class="badge verified">Quote verified against document text ✓</span>'
            if verified
            else '<span class="badge eyes">Confirm against the page image</span>'
        )
        parts.append(
            f'<div data-quote-normal=""{" hidden" if privileged else ""}><blockquote class="{"" if verified else "unverified"}"><mark>“{esc(quote)}”</mark></blockquote>'
            f'<div class="cite">{" · ".join(cite)} {badge}</div></div>'
        )
        parts.append(
            f'<div class="redaction" data-redaction=""{"" if privileged else " hidden"}><span class="bar" aria-hidden="true">{esc(quote)}</span>'
            '<span class="why">Redacted — your privilege ruling</span></div>'
        )
    if row.get("characterization"):
        parts.append(f'<p class="characterization">{esc(row["characterization"])}</p>')
    parts.extend(
        [
            receipt_html(row),
            ruling_controls(row, enabled=decision_enabled),
            "</article>",
        ]
    )
    return "".join(parts)


def render(
    framework: dict,
    findings: dict,
    manifest: dict,
    queue: dict | None,
    source_name: str = "findings.json",
    document_root: Path | None = None,
    review_validation: Any | None = None,
    output_parent: Path | None = None,
    review_warning: str | None = None,
) -> str:
    frame, issues, lens_issues, instruments, staged = framework_index(framework)
    documents = manifest_index(manifest)
    queue_held, privilege_rows = privilege_index(queue, documents)
    by_issue, by_doc, reviewed_docs = compile_rows(
        findings, issues, lens_issues, documents, queue_held
    )
    interactive_findings = sorted(
        (
            row
            for rows in by_issue.values()
            for status in ("present", "absent", "unresolved")
            for row in rows[status]
        ),
        key=lambda row: row["finding_id"],
    )
    corpus_id = manifest.get("corpus_id") or frame.get("corpus_id")
    if not isinstance(corpus_id, str) or not corpus_id:
        fail("manifest or framework must carry corpus_id")
    if manifest.get("corpus_id") and frame.get("corpus_id") != manifest.get(
        "corpus_id"
    ):
        fail("framework and manifest corpus IDs differ")
    if findings.get("framework_version") != framework.get("framework_version"):
        fail("findings and framework versions differ")
    label = matter_label(manifest, frame)
    issue_order = sorted(
        issues,
        key=lambda issue_id: target_sort_key(target_key(issues[issue_id]["target"])),
    )
    present_requests = sum(bool(by_issue[issue_id]["present"]) for issue_id in issues)
    empty_requests = sum(
        bool(rows["absent"])
        and not rows["present"]
        and not rows["unresolved"]
        and not rows["held"]
        and not rows["parked"]
        for rows in by_issue.values()
    )
    unresolved_doc_ids = sorted(
        (doc_id for doc_id, rows in by_doc.items() if rows["unresolved"]),
        key=lambda doc_id: document_sort(documents[doc_id]),
    )
    parked_doc_ids = sorted(
        (doc_id for doc_id, rows in by_doc.items() if rows["parked_issues"]),
        key=lambda doc_id: document_sort(documents[doc_id]),
    )
    image_subjects = {
        doc_id: subject
        for doc_id, subject in image_confirmation_subjects(findings).items()
        if doc_id not in queue_held
    }
    resolved_output_parent = (output_parent or Path.cwd()).resolve()
    document_sources = document_source_index(
        documents, document_root, set(image_subjects), resolved_output_parent
    )
    review_copy_needs_set = blocked_review_copy_ids(review_validation, documents)
    review_copy_needs_ids = sorted(
        review_copy_needs_set,
        key=lambda doc_id: document_sort(documents[doc_id]),
    )
    review_ready = bool(
        review_validation
        and review_validation.integrity_ok
        and review_validation.ready
        and not review_copy_needs_set
        and not review_warning
    )
    review_lock_reason = (
        "Decisions and export are locked because this pass failed calibration."
        if review_warning
        else "Decisions and export are locked until every displayed document has a verified review copy."
    )
    image_confirmations = image_confirmation_index(findings, image_subjects)
    image_review_doc_ids = sorted(
        image_subjects,
        key=lambda doc_id: document_sort(documents[doc_id]),
    )
    pending_image_review_doc_ids = [
        doc_id
        for doc_id in image_review_doc_ids
        if image_confirmations.get(doc_id, {}).get("confirmation") != "confirmed"
    ]
    pending_image_review_doc_set = set(pending_image_review_doc_ids)
    eyes_rows = sorted(
        (
            row
            for rows in by_issue.values()
            for row in rows["present"] + rows["absent"]
            if needs_eyes(row) and row["doc_id"] in pending_image_review_doc_set
        ),
        key=lambda row: row["finding_id"],
    )
    privilege_doc_ids = sorted(
        privilege_rows, key=lambda doc_id: document_sort(documents[doc_id])
    )
    held_doc_ids = {doc_id for rows in by_issue.values() for doc_id in rows["held"]}
    outside_doc_ids = sorted(
        set(documents) - reviewed_docs - held_doc_ids,
        key=lambda doc_id: document_sort(documents[doc_id]),
    )
    bindings = {
        "corpus_id": corpus_id,
        "frame_id": frame.get("frame_id"),
        "framework_digest": canonical_digest(framework),
        "framework_version": framework.get("framework_version"),
        "ledger_digest": canonical_digest(proposal_ledger(findings)),
        "review_plan_id": findings.get("review_plan_id"),
        "source": source_name,
    }
    data = {
        "bindings": bindings,
        "findings": interactive_findings,
        "image_confirmation_subjects": [
            image_subjects[doc_id] for doc_id in sorted(image_subjects)
        ],
        "image_confirmations": [
            image_confirmations[doc_id] for doc_id in sorted(image_confirmations)
        ],
        "review_ready": review_ready,
        "review_lock_reason": review_lock_reason,
    }
    decision_disabled = ' disabled aria-disabled="true"' if not review_ready else ""
    parts = [
        "<!doctype html>",
        '<html lang="en"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>Production review — {esc(label)}</title><style>{BRAND_CSS}{CSS}</style></head>",
        f'<body data-lq-review-ui="{esc(CONTRACT_ID)}" data-default-filter="responsive-only">',
        '<a class="skip" href="#panel-requests">Skip to review</a>',
        review_masthead(label),
        "<header>",
        '<div class="machine-note">Machine first pass — verify before relying</div>',
        f"<h1>Production review — {esc(label)}</h1>",
        f'<p class="sub">Their production, mapped to your requests · corpus {esc(corpus_id)}</p>',
        '<hr class="caption-rule"><hr class="caption-rule">',
        '<p class="docket-line">',
        f"Of <b>{len(issues)} requests</b> checked, ",
        f'<button class="link-button" type="button" data-summary-filter="responsiveOnly">{present_requests} have responsive documents</button> and ',
        f'<button class="link-button" type="button" data-summary-filter="empty">{empty_requests} have no matching document identified</button>. ',
        f'<button class="link-button" type="button" data-summary-filter="unread">{len(unresolved_doc_ids)} file',
        "s" if len(unresolved_doc_ids) != 1 else "",
        " has" if len(unresolved_doc_ids) == 1 else " have",
        " questions that still need a decision</button>, ",
        f"<b>{len(parked_doc_ids)} file",
        "s" if len(parked_doc_ids) != 1 else "",
        " did not complete review</b>, ",
        f'<button class="link-button" type="button" data-summary-filter="eyes">{len(pending_image_review_doc_ids)} image file',
        "s" if len(pending_image_review_doc_ids) != 1 else "",
        " need" if len(pending_image_review_doc_ids) != 1 else " needs",
        " a complete page review</button>; ",
        f"<b>{len(review_copy_needs_ids)} document review cop",
        "ies need" if len(review_copy_needs_ids) != 1 else "y needs",
        " rendering</b>; and ",
        f'<button class="link-button" type="button" data-summary-filter="privilege">{len(privilege_doc_ids)} privilege flag',
        "s" if len(privilege_doc_ids) != 1 else "",
        "</button>.</p>",
        '<div class="toolbar"><input type="search" id="search" aria-label="Search review" placeholder="Search requests, files, or quoted text…  ( / )">',
        '<select id="sort-select" aria-label="Sort review"><option value="order">Request order</option><option value="matches">Most responsive first</option><option value="unruled">Unruled first</option></select>',
        f'<button class="btn" id="export-button" type="button" title="Keyboard e"{decision_disabled}>Download rulings (JSON)</button></div>',
        '<div class="tabs" role="tablist" aria-label="Review orientation"><button class="tab" id="tab-requests" role="tab" type="button" data-tab="requests" aria-selected="true" aria-controls="panel-requests">Requests</button>',
        '<button class="tab" id="tab-documents" role="tab" type="button" data-tab="documents" aria-selected="false" aria-controls="panel-documents" tabindex="-1">Documents</button></div>',
        '<div class="chips"><button class="chip" type="button" data-filter="responsiveOnly" aria-pressed="true">Responsive only</button>',
        '<button class="chip" type="button" data-filter="empty" aria-pressed="false">No match identified</button>',
        '<button class="chip" type="button" data-filter="eyes" aria-pressed="false">Needs page review</button>',
        '<button class="chip" type="button" data-filter="unread" aria-pressed="false">Needs a decision</button>',
        '<button class="chip" type="button" data-filter="privilege" aria-pressed="false">Privilege flags</button>',
        '<select id="instrument-select" aria-label="Instrument"><option value="all">All requests</option>',
    ]
    for instrument in sorted(
        (row for row in instruments.values() if row.get("staged") is not True),
        key=lambda row: row["display"],
    ):
        parts.append(
            f'<option value="{esc(instrument["instrument_id"])}">{esc(instrument["display"])}</option>'
        )
    parts.append(
        '</select><span class="filter-count" id="filter-count" aria-live="polite"></span>'
    )
    if review_warning:
        parts.append(
            '<div class="banner attention" role="alert"><b>Review decisions are locked. '
            f"Do not rely on this first pass yet.</b> {esc(review_warning)}</div>"
        )
    if review_copy_needs_ids:
        parts.append(
            '<div class="banner attention" role="alert"><b>Review decisions are locked.</b> '
            "Every displayed document needs a verified in-page review copy before "
            "you can rule or export feedback.</div>"
        )
    parts.extend(
        [
            "</div>",
            '<div class="kbd-hint"><kbd>j</kbd>/<kbd>k</kbd> move · <kbd>Enter</kbd> expand · <kbd>1</kbd>–<kbd>4</kbd> rule · <kbd>[</kbd>/<kbd>]</kbd> switch tabs · <kbd>/</kbd> search · <kbd>e</kbd> export</div></header><main>',
            '<section id="panel-requests" role="tabpanel" aria-labelledby="tab-requests">',
        ]
    )
    last_instrument = None
    for order, issue_id in enumerate(issue_order):
        issue, rows = issues[issue_id], by_issue[issue_id]
        instrument_id = issue["target"]["instrument_id"]
        if instrument_id != last_instrument:
            if last_instrument is not None:
                parts.append("</div>")
            parts.append(
                f'<div class="request-group" data-request-group="{esc(instrument_id)}">'
            )
            parts.append(f'<div class="group-h">{esc(issue["instrument_label"])}</div>')
            last_instrument = instrument_id
        present, absent, unresolved, held, parked = (
            rows["present"],
            rows["absent"],
            rows["unresolved"],
            rows["held"],
            rows["parked"],
        )
        eye_count = sum(
            needs_eyes(row) and row["doc_id"] in pending_image_review_doc_set
            for row in present + absent
        )
        all_absent = (
            bool(absent) and not present and not unresolved and not held and not parked
        )
        empty = all_absent
        attention = bool(unresolved or eye_count or held or parked)
        existing_count = sum(
            bool(row.get("lawyer_ruling")) for row in present + absent + unresolved
        )
        request_search = " ".join(
            [
                issue["instrument_label"],
                designator(issue["target"]),
                str(issue["question"]),
            ]
            + [
                " ".join(
                    str(value or "")
                    for value in (
                        documents[row["doc_id"]].get("path"),
                        row.get("quote"),
                        row.get("characterization"),
                    )
                )
                for row in present + absent
            ]
            + [
                " ".join([str(documents[doc_id].get("path", "")), *sorted(reasons)])
                for doc_id, reasons in parked.items()
            ]
        ).lower()
        row_id = f"request-{hashlib.sha256(issue_id.encode()).hexdigest()[:12]}"
        classes = "row request-row" + (
            " has-responsive" if present else " attention" if attention else ""
        )
        parts.append(
            f'<article class="{classes}" data-row="" data-request="{esc(issue_id)}" data-instrument="{esc(instrument_id)}" '
            f'data-has-responsive="{str(bool(present)).lower()}" data-empty="{str(empty).lower()}" data-needs-eyes="{str(bool(eye_count)).lower()}" data-unread="{str(bool(unresolved or parked)).lower()}" '
            f'data-privilege="{str(bool(held)).lower()}" data-matches="{len(present)}" data-ruled="{existing_count}" data-order="{order:06d}" data-search="{esc(request_search)}">'
        )
        preview = str(issue["question"])
        preview = preview[:140].rstrip() + "…" if len(preview) > 140 else preview
        pills = (
            f'<span class="pill responsive">● {len(present)} responsive</span>'
            if present
            else '<span class="pill neutral">No matching document identified</span>'
            if all_absent
            else '<span class="pill neutral">No responsive document found</span>'
        )
        if eye_count:
            pills += (
                f'<span class="pill attention">{eye_count} image-based match'
                f"{'s' if eye_count != 1 else ''} "
                f"{'need' if eye_count != 1 else 'needs'} review</span>"
            )
        if unresolved:
            unresolved_count = len({row["doc_id"] for row in unresolved})
            pills += (
                f'<span class="pill attention">{unresolved_count} decision'
                f"{'s' if unresolved_count != 1 else ''} needed</span>"
            )
        if held:
            pills += '<span class="pill privilege">Needs a privilege ruling</span>'
        if parked:
            pills += '<span class="pill attention">Review incomplete</span>'
        parts.append(
            f'<button class="rowhead" type="button" data-toggle="request" aria-expanded="false" aria-controls="{row_id}"><span class="reqnum">No. {esc(designator(issue["target"]))}</span>'
            f'<span class="preview">{esc(preview)}</span><span class="pills">{pills}</span></button><div class="rowbody" id="{row_id}" hidden>'
            f'<div class="request-text"><div class="label">What the request asks for</div>{esc(issue["question"])}</div>'
            f'<button class="link-button" type="button" data-accept-request="{esc(issue_id)}"{decision_disabled}>Accept all machine findings for this request</button>'
        )
        for row in present:
            parts.append(
                finding_card(
                    row,
                    documents[row["doc_id"]],
                    request_label(issue),
                    str(issue["question"]),
                    decision_enabled=review_ready,
                    default_visible=True,
                )
            )
        if absent:
            parts.append(
                f'<details class="also"><summary>Also checked: {len(absent)} document{"s" if len(absent) != 1 else ""} with nothing found</summary>'
            )
            for row in absent:
                parts.append(
                    finding_card(
                        row,
                        documents[row["doc_id"]],
                        request_label(issue),
                        str(issue["question"]),
                        decision_enabled=review_ready,
                    )
                )
            parts.append("</details>")
        if unresolved:
            count = len({row["doc_id"] for row in unresolved})
            notice = (
                "The machine could not decide whether one document answers this request. "
                "Open the document and review the explanation under Needs attention."
                if count == 1
                else f"The machine could not decide whether {count} documents answer this request. "
                "Open each document and review the explanations under Needs attention."
            )
            parts.append(f'<div class="banner attention">{notice}</div>')
        if held:
            parts.append(
                '<div class="banner privilege">Privilege flag — this request has material held for a lawyer ruling.</div>'
            )
        if parked:
            reasons = sorted(
                {
                    reason
                    for parked_reasons in parked.values()
                    for reason in parked_reasons
                }
            )
            parts.append(
                '<div class="banner attention"><b>Review incomplete.</b> '
                f"{len(parked)} document{'s' if len(parked) != 1 else ''} "
                "could not complete this request, so no absence conclusion was made. "
                f"{esc('; '.join(reasons))}</div>"
            )
        parts.append("</div></article>")
    if last_instrument is not None:
        parts.append("</div>")
    if staged:
        parts.append(
            '<div class="staged"><b>Scope of this page</b><p>This page compares the production only with the requests shown above. '
            "The following separate discovery sets are listed for completeness and were not part of this document-to-request review:</p><ul>"
        )
        for row in sorted(staged, key=lambda item: item["display"]):
            parts.append(
                f"<li>{esc(row['display'])} — {row['element_count']} requests</li>"
            )
        parts.append(
            "</ul><p>No positive or negative result was made for those separate sets.</p></div>"
        )
    parts.append(
        '</section><section id="panel-documents" role="tabpanel" aria-labelledby="tab-documents" hidden>'
    )
    for order, doc_id in enumerate(
        sorted(documents, key=lambda value: document_sort(documents[value]))
    ):
        document, doc_rows = documents[doc_id], by_doc[doc_id]
        present, unread, outside, held, parked = (
            doc_rows["present"],
            bool(doc_rows["unresolved"]),
            doc_id in outside_doc_ids,
            bool(doc_rows["held_issues"]),
            bool(doc_rows["parked_issues"]),
        )
        image_subject = image_subjects.get(doc_id)
        image_confirmation = image_confirmations.get(doc_id)
        eye = doc_id in pending_image_review_doc_set
        copy_ready = doc_id not in review_copy_needs_set
        privilege = doc_id in privilege_rows or any(
            (row.get("lawyer_ruling") or {}).get("ruling") == "privileged"
            for row in present + doc_rows["absent"]
        )
        identity, identity_unverified = identity_excerpt(doc_rows)
        search = " ".join(
            [str(document.get("path", "")), document_type(document), identity or ""]
            + [
                str(issues[row["issue_id"]]["question"])
                + " "
                + str(row.get("quote") or "")
                for row in present
            ]
        ).lower()
        row_id = f"document-{hashlib.sha256(doc_id.encode()).hexdigest()[:12]}"
        anchor_id = document_anchor(doc_id)
        parts.append(
            f'<article id="{anchor_id}" class="row document-row{" has-responsive" if present else " attention" if unread or held or parked or not copy_ready else ""}" data-row="" '
            f'data-has-responsive="{str(bool(present)).lower()}" data-empty="{str(doc_id in reviewed_docs and not present and not unread and not held and not parked).lower()}" '
            f'data-needs-eyes="{str(eye).lower()}" data-unread="{str(unread or parked).lower()}" data-privilege="{str(privilege or held).lower()}" '
            f'data-matches="{len(present)}" data-attention="{int(unread or eye or held or parked or not copy_ready)}" data-order="{order:06d}" data-search="{esc(search)}">'
        )
        if present:
            pill = f'<span class="pill responsive">Matches {len(present)} of your requests</span>'
            if unread:
                pill += '<span class="pill attention">Needs a decision</span>'
        elif unread:
            pill = '<span class="pill attention">Needs a decision</span>'
        elif held:
            pill = '<span class="pill privilege">Needs a privilege ruling</span>'
        elif parked:
            pill = '<span class="pill attention">Review incomplete</span>'
        elif outside:
            pill = '<span class="pill neutral">Not reviewed in this tier</span>'
        else:
            pill = '<span class="pill neutral">No request match identified</span>'
        if image_confirmation and image_confirmation["confirmation"] == "confirmed":
            pill += '<span class="pill responsive">Page review complete</span>'
        elif eye:
            pill += '<span class="pill attention">Needs page review</span>'
        if not copy_ready:
            pill += '<span class="pill attention">Needs rendering</span>'
        identity_line = (
            f" — “{esc(identity[:100])}{'…' if len(identity) > 100 else ''}”"
            if identity
            else ""
        )
        parts.append(
            f'<button class="rowhead" type="button" data-toggle="document" aria-expanded="false" aria-controls="{row_id}"><span class="bates">NO. {esc(production_number(document))}</span>'
            f'<span class="preview"><span class="docname">{esc(document.get("path", ""))}</span><br><span class="docdesc">{esc(document_type(document))}{identity_line}</span></span>'
            f'<span class="pills">{pill}</span></button><div class="rowbody" id="{row_id}" hidden>'
        )
        if unread:
            parts.append(
                f'<div class="banner attention">{esc(unresolved_document_notice(doc_rows))}</div>'
            )
        if held:
            parts.append(
                '<div class="banner privilege">Privilege flag — held until the lawyer rules.</div>'
            )
        if parked:
            reasons = sorted(
                {
                    reason
                    for parked_reasons in doc_rows["parked_issues"].values()
                    for reason in parked_reasons
                }
            )
            parts.append(
                '<div class="banner attention"><b>Review incomplete.</b> No absence '
                f"conclusion was made. {esc('; '.join(reasons))}</div>"
            )
        parts.append(
            f'<div class="review-copy-wrap" data-review-document="{esc(doc_id)}">'
            f"{review_copy_html(review_validation, doc_id, document)}"
        )
        if doc_id in document_sources:
            parts.append(
                '<p class="original-source">Need the native file? '
                + source_link_html(document, document_sources[doc_id])
                + "</p>"
            )
        parts.append("</div>")
        if image_subject:
            if copy_ready:
                parts.append(
                    image_confirmation_controls(
                        image_subject,
                        image_confirmation,
                    )
                )
            else:
                parts.append(
                    blocked_image_confirmation_controls(
                        image_subject,
                        image_confirmation,
                    )
                )
        if identity:
            parts.append(
                f'<blockquote class="{"unverified" if identity_unverified else ""}"><mark>“{esc(identity)}”</mark></blockquote>'
                f'<div class="cite">Identity excerpt · {"read from page image — confirm against the file" if identity_unverified else "verified text"}</div>'
            )
        if present:
            parts.append('<div class="group-h">Responsive to</div>')
            for row in present:
                issue = issues[row["issue_id"]]
                parts.append(f'<div class="docname">{esc(request_label(issue))}</div>')
                parts.append(
                    finding_card(
                        row,
                        document,
                        request_label(issue),
                        str(issue["question"]),
                        decision_enabled=review_ready,
                        show_document=False,
                    )
                )
        if doc_rows["unresolved"]:
            parts.append('<div class="group-h">Needs a decision</div>')
            for row in doc_rows["unresolved"]:
                issue = issues[row["issue_id"]]
                parts.append(f'<div class="docname">{esc(request_label(issue))}</div>')
                parts.append(
                    finding_card(
                        row,
                        document,
                        request_label(issue),
                        str(issue["question"]),
                        decision_enabled=review_ready,
                        show_document=False,
                    )
                )
        elif not unread and not held and not parked:
            parts.append(
                '<p class="characterization">'
                + (
                    "Not reviewed in this tier; no responsiveness decision was made."
                    if outside
                    else "The machine did not identify a request match in this review."
                )
                + "</p>"
            )
        parts.append("</div></article>")
    parts.append(
        '</section><section class="drawers" aria-label="Supporting review queues">'
    )
    parts.append(
        f'<details class="drawer" id="attention-drawer"><summary>Needs attention — {len(unresolved_doc_ids)} file'
        f"{'s' if len(unresolved_doc_ids) != 1 else ''} with questions still needing a decision; "
        f"{len(pending_image_review_doc_ids)} scanned file{'s' if len(pending_image_review_doc_ids) != 1 else ''} "
        f"{'need' if len(pending_image_review_doc_ids) != 1 else 'needs'} complete page review; "
        f"{len(eyes_rows)} proposed image-based match{'es' if len(eyes_rows) != 1 else ''} "
        f"{'need' if len(eyes_rows) != 1 else 'needs'} confirmation; "
        f"{len(parked_doc_ids)} file{'s' if len(parked_doc_ids) != 1 else ''} did not complete review; "
        f"{len(review_copy_needs_ids)} document review cop"
        f"{'ies need' if len(review_copy_needs_ids) != 1 else 'y needs'} rendering</summary>"
    )
    if (
        not unresolved_doc_ids
        and not parked_doc_ids
        and not pending_image_review_doc_ids
        and not eyes_rows
        and not review_copy_needs_ids
    ):
        parts.append('<p class="small">No file needs separate attention.</p>')
    for doc_id in unresolved_doc_ids:
        review_link = "<br>" + document_jump_link_html(documents[doc_id], doc_id)
        parts.append(
            f'<article class="banner attention" data-unresolved-document="{esc(doc_id)}"><b>{esc(documents[doc_id].get("path", ""))}</b><br>'
            f"{esc(unresolved_document_notice(by_doc[doc_id]))}{review_link}</article>"
        )
    for doc_id in parked_doc_ids:
        reasons = sorted(
            {
                reason
                for parked_reasons in by_doc[doc_id]["parked_issues"].values()
                for reason in parked_reasons
            }
        )
        parts.append(
            f'<article class="banner attention" data-parked-document="{esc(doc_id)}">'
            f"<b>{esc(documents[doc_id].get('path', ''))}</b><br>Review incomplete; "
            f"no absence conclusion was made. {esc('; '.join(reasons))}<br>"
            f"{document_jump_link_html(documents[doc_id], doc_id)}</article>"
        )
    for doc_id in pending_image_review_doc_ids:
        doc_rows = by_doc[doc_id]
        responsive = len(doc_rows["present"])
        no_match = len(doc_rows["absent"])
        unresolved = len(doc_rows["unresolved"])
        review_link = document_jump_link_html(documents[doc_id], doc_id)
        parts.append(
            f'<article class="banner attention" data-image-review-document="{esc(doc_id)}"><b>{esc(documents[doc_id].get("path", ""))}</b><br>'
            f"Scanned-file review: the machine proposed {responsive} match{'es' if responsive != 1 else ''}, "
            f"{no_match} non-match{'es' if no_match != 1 else ''}, and "
            f"{unresolved} question{'s' if unresolved != 1 else ''} still needing a decision. "
            "Review every page and the listed results before marking this file complete."
            f"<br>{review_link}</article>"
        )
    for doc_id in review_copy_needs_ids:
        parts.append(
            f'<article class="banner attention" data-review-copy-needed="{esc(doc_id)}">'
            f"<b>{esc(documents[doc_id].get('path', ''))}</b><br>"
            "A verified in-page review copy is not ready. "
            f"{document_jump_link_html(documents[doc_id], doc_id)}</article>"
        )
    for row in eyes_rows:
        issue = issues[row["issue_id"]]
        parts.append(
            finding_card(
                row,
                documents[row["doc_id"]],
                request_label(issue),
                str(issue["question"]),
                decision_enabled=review_ready,
            )
        )
    parts.append("</details>")
    parts.append(
        f'<details class="drawer" id="privilege-drawer"><summary>Privilege flags — {len(privilege_doc_ids)}</summary><ul class="drawer-list">'
    )
    if not privilege_doc_ids:
        parts.append("<li>No privilege flag is pending or recorded.</li>")
    for doc_id in privilege_doc_ids:
        for row in privilege_rows[doc_id]:
            state = (
                "Needs a privilege ruling"
                if row.get("queue_state") == "candidate"
                else "Privilege reviewed — not privileged"
                if row.get("ruling") == "not-privileged"
                else "Privilege reviewed — " + str(row.get("ruling")).replace("-", " ")
            )
            parts.append(
                f'<li><b>Privilege flag — {esc(documents[doc_id].get("path", ""))}</b> <span class="badge privilege">{esc(state)}</span><br>{esc(row.get("reason", ""))}'
                f'<details class="receipt"><summary>Privilege receipt</summary>{esc(row.get("quote", ""))} · document {esc(doc_id)}</details></li>'
            )
    parts.append("</ul></details>")
    parts.append(
        f'<details class="drawer" id="outside-drawer"><summary>Not reviewed in this tier — {len(outside_doc_ids)} files</summary><ul class="drawer-list">'
    )
    for doc_id in outside_doc_ids:
        parts.append(f"<li>{esc(documents[doc_id].get('path', ''))}</li>")
    parts.extend(
        [
            "</ul></details></section>",
            '<div class="exportbox" id="export-box" hidden><p class="sub">review-feedback.json — deterministic and bound to this proposal ledger and framework.</p>'
            '<textarea id="export-text" readonly aria-label="Exported lawyer rulings"></textarea></div>',
            '<p class="status" id="review-status" aria-live="polite"></p></main>',
            f'<script id="review-data" type="application/json">{safe_json(data)}</script>',
            f"<script>{THEME_JS}</script><script>{JS}</script></body></html>\n",
        ]
    )
    return "".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--framework", required=True)
    parser.add_argument("--findings", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--privilege-queue")
    parser.add_argument(
        "--document-root",
        help="root directory containing manifest document paths; required for image review",
    )
    parser.add_argument(
        "--review-copies",
        help=(
            "hash-bound review-copy sidecar; it must be alongside --out and "
            "requires --document-root"
        ),
    )
    parser.add_argument("--out", required=True)
    parser.add_argument(
        "--review-warning",
        help="plain-language warning shown near the top of the review page",
    )
    args = parser.parse_args()
    output_path = Path(args.out).expanduser().absolute().resolve()
    input_paths = {
        Path(value).expanduser().absolute().resolve()
        for value in (
            args.framework,
            args.findings,
            args.manifest,
            args.privilege_queue,
            args.review_copies,
        )
        if value
    }
    if output_path in input_paths:
        fail("--out must be a distinct new artifact path")
    framework = load(
        args.framework,
        "framework",
        ("framework_version", "approved", "source_inputs", "lenses"),
    )
    findings = load(
        args.findings, "findings", ("framework_version", "review_plan_id", "findings")
    )
    manifest = load(args.manifest, "manifest", ("documents",))
    reject_source_output_alias(
        manifest,
        Path(args.document_root) if args.document_root else None,
        output_path,
    )
    queue = (
        load(args.privilege_queue, "privilege queue", ("candidates", "ruled"))
        if args.privilege_queue
        else None
    )
    output_parent = output_path.parent
    review_validation = None
    if args.review_copies:
        if not args.document_root:
            fail("--review-copies requires --document-root for source revalidation")
        sidecar_path = Path(args.review_copies).expanduser().absolute()
        if sidecar_path.parent.resolve() != output_parent:
            fail(
                "--review-copies must be alongside --out so relative review-copy links stay valid"
            )
        review_validation = REVIEW_COPIES.revalidate_review_copies(
            sidecar_path,
            args.manifest,
            args.document_root,
        )
        if not review_validation.integrity_ok:
            detail = "; ".join(review_validation.errors[:4])
            fail(f"review-copy validation failed: {detail}")
    output = render(
        framework,
        findings,
        manifest,
        queue,
        Path(args.findings).name,
        Path(args.document_root) if args.document_root else None,
        review_validation,
        output_parent,
        args.review_warning,
    )
    try:
        with open(args.out, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(output)
    except OSError as error:
        fail(f"cannot write {args.out}: {error}")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
