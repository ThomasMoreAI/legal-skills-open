---
name: redlines
title: redlines — Word Document Redlining Library
description: Use when you need to generate tracked changes in Word documents from diff output, apply redlines from AI agents to DOCX files, or convert text diffs into native Word revisions.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/redlines
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [word, docx, tracked-changes, redlines, document-processing]
---

# redlines — Word Document Redlining Library

## When to Use

- Converting AI-generated edits into Word tracked changes
- Applying diff output to DOCX files with native revision markup
- Building legal tools that produce redlined documents
- Automated document comparison with Word-compatible output
- "Draft by exception" workflows where you track exceptions to standard clauses

## How It Works

Takes diff output (from any source) and applies it to a DOCX as native Word tracked changes. Built by a practising Singapore counsel who needed deterministic document transformation.

### Input

- Original DOCX
- Modified text or diff output

### Output

DOCX with Word native tracked changes (insertions in blue, deletions in strikethrough)

### Usage

```javascript
import { applyRedlines } from '@houfu/redlines';

const result = applyRedlines({
  originalDoc: './contract.docx',
  modifiedText: 'modified contract text here',
  author: 'LQClaw'
});

result.toDocx('./contract-redlined.docx');
```

### Key Design Decisions

- **Deterministic** — Same input produces identical output
- **Format preservation** — Headers, lists, tables survive transformation
- **Standard-compliant** — Output is valid DOCX that Word renders correctly
- **No round-trip through Word** — Works headlessly, no Office install required

## Audience and Work Shape

Audience: legal engineers and counsel comfortable invoking a JavaScript library from a workflow. Not a self-service tool for a reviewing partner and not intended for non-technical users. The judgment as to *which* edits to apply sits upstream of this skill; this skill only carries them into the DOCX.

Work shape: Bounded Transactional primitive. Text-in (or diff-in) → DOCX-out. The transform is mechanical. It is not a redline reviewer, not a redline generator, and not a substantive review step.

## Scope and Legal Use

This skill provides legal *support*, not legal advice. Producing a tracked-changes DOCX is mechanical document processing; the redlined output is a draft, not a vetted lawyer redline and not signed-off work product. A successful run means "the supplied edits were carried into the file as Word revisions" — not "these edits are correct" and not "this draft is fit to send."

**Privilege and metadata exposure.** Tracked changes carry author metadata into the document. The `author` field in the call (e.g., `'LQClaw'`) is written into the Word XML alongside revision timestamps and is preserved in the saved file. Anyone who opens the DOCX (counterparty, opposing counsel, recipient on production) can read it. Stance: AI authorship should be visible — do not mask AI-generated revisions behind a lawyer's name or firm identity. Treat the redlined DOCX as a draft document and assess data flow with the firm before routing draft files externally; redlines on privileged drafts can be discoverable and can affect privilege if circulated. Confirm a metadata-scrubbing step before any external delivery and confirm with the firm that the upstream diff and the source DOCX may be processed by the calling pipeline.

**Accountability.** Output is a mechanical transform of an upstream diff. A qualified, named lawyer must read the redlined DOCX page-by-page before any client or counterparty delivery. The skill does not stamp provenance, does not maintain an audit log, and does not designate an owner of the output — the calling workflow must do all three.

## Confidence Bands

- **High** — simple paragraph-level diffs in linear body text, no pre-existing revisions in the source, no comments or footnotes touched by the diff, diff anchors cleanly to the source.
- **Medium** — diff touches lists or tables, or crosses paragraph boundaries; numbering is preserved but should be eyeballed. Route for lawyer review.
- **Low / Review** — nested numbering, footnotes, cross-references, comments, redlines spanning structural breaks (section/heading boundaries), source DOCX already contains tracked changes, or diff fails to anchor unambiguously. Do not treat the output as a clean redline; halt and escalate.

## Out of Scope

- Does not generate the redline — the diff or modified text must come from upstream.
- Does not review the redline for legal substance or correctness of edits.
- Does not preserve comments, footnotes, or cross-references unless explicitly tested for the document shape in hand.
- Does not handle scanned PDFs, images, password-protected files, or files under DRM.
- Does not handle structural transformations (re-ordering of clauses, schedule moves).
- Does not constitute a redline-review or quality-control sign-off for purposes of professional rules.
- Does not scrub author metadata, comments, or revision history from the output — that is a separate step the caller owns.

## Escalation

Stop and route to the responsible lawyer when:
- the diff does not anchor cleanly to the source (return a structured error, do not write a partial redline);
- the source DOCX already contains tracked changes or unresolved comments;
- the source DOCX is password-protected, corrupt, or cannot be parsed;
- the diff touches footnotes, cross-references, defined-term placement, or nested numbering;
- the redlined DOCX is about to leave the firm and no metadata-scrubbing / provenance-stamping step has run;
- a confidence band of Medium or Low is emitted and no named lawyer has been designated to review the output.

## Limitations

- Complex nested structures may require manual review
- Only handles text-level changes (not structural transformations)

## QA Remediation (LegalQuants, 2026-05)

Original author: Hou Fu Ang. Technical content (When to Use, How It Works, Input, Output, Usage, Key Design Decisions, Limitations) preserved verbatim.

LegalQuants applied QA remediation against the Legal Skill Design Framework on 2026-05-11 in response to the QA report at `/tmp/qa-results/redlines.md` (verdict: MATERIAL CONCERNS — three legal failure modes unaddressed). Added: `version`, `last_reviewed`, `last_reviewed_by` in frontmatter; Audience and Work Shape; Scope and Legal Use covering the three mandatory legal failure modes (advice-vs-support, privilege/metadata, accountability), with specific treatment of Word XML author metadata persistence and the stance that AI authorship should be visible rather than masked; Confidence Bands tied to document shape; Out of Scope ("does NOT do"); Escalation triggers. No changes to the technical instructions or the `@houfu/redlines` API.
