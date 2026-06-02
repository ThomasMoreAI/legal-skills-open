---
name: building-chronologies
title: building-chronologies
description: Use when users say "build a chronology", "make a timeline", "what happened when", "chronology from disclosure", "source the key events", or need legal documents, correspondence, pleadings, witness evidence, or disclosure materials turned into a sourced event chronology.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/building-chronologies
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [chronology, timeline, evidence, disclosure, source-attribution]
---

# building-chronologies

## When to Use

- A lawyer needs a timeline from a bundle, disclosure set, correspondence folder, witness statement set, or case file.
- The user asks "what happened when" or needs chronology support for pleadings, advice, witness prep, mediation, or trial.
- The output must cite each event back to a source document.

Do not use this skill to fill gaps from memory. A chronology is only as reliable as its sources.

## Audience and Work Shape

Audience: litigators, trainees, paralegals, and litigation-support teams building first-pass chronologies for lawyer review.

Work shape: bounded extraction with accretive judgment. The skill extracts dated events from sources, then applies judgment to de-duplicate, flag conflicts, and surface gaps. It does not decide what happened.

## Legal Failure Modes

- Legal support, not legal advice: a chronology is a working evidence map, not merits advice, submissions, or a final statement of facts.
- Privilege/confidentiality: if source material appears privileged or work-product-sensitive, flag it as `privilege_review` and do not include it in an externally shareable chronology without lawyer approval.
- Accountability: the responsible lawyer decides whether a disputed or low-confidence event can be used in pleadings, evidence, settlement material, or submissions.

## Access Modes

This skill works in three modes:

1. **Live source mode** - use browser, web search, MCP, API, or other configured access to retrieve public filings, dockets, emails, storage folders, or document repositories.
2. **User-supplied source mode** - use uploaded or pasted documents, correspondence, pleadings, disclosure exports, witness materials, PDFs, images, or OCR text supplied by the user.
3. **No-source mode** - design the chronology schema and source-request list, but do not create factual chronology entries.

If documents cannot be retrieved or supplied, do not infer events from model memory. Mark missing periods, missing sources, and source requests explicitly.

## How It Works

### 1. Define scope

Confirm:

- Matter or project name.
- Date range.
- Document sources.
- Jurisdiction or forum, if legal deadlines or procedural events will be interpreted.
- Intended output: working chronology, witness-specific chronology, statement-of-facts draft, or issue chronology.

If source coverage is thin, say so before drawing conclusions.

### 2. Extract dated events

For each source, extract only events with a reliable date or date range:

- Email sent or received.
- Letter, notice, pleading, order, filing, or hearing.
- Meeting, call, inspection, delivery, payment, breach, termination, complaint, or admission.
- Document creation date only if it is itself relevant, not merely metadata noise.

Each event should include:

- `date`
- `actor`
- `event`
- `source`
- `source_identifier`, such as Bates number, file name, email metadata, exhibit number, bundle tab, or path
- `quote`
- `confidence`
- `issue_tags`
- `notes`

Use ISO dates where possible. If only month or year is known, preserve that uncertainty.

Distinguish `event_date` from `document_date` and `date_extracted_from`. Do not use file metadata as the event date unless the metadata itself is the fact being recorded.

Use these confidence values:

- `high` - contemporaneous source directly states the event and date.
- `medium` - source supports the event, but date, actor, or context needs checking.
- `low` - event is inferred from incomplete material.
- `date_uncertain` - event happened, but exact date is unclear.
- `source_conflict` - sources disagree materially.

## Confidence Bands

Use the event `confidence` and `date_certainty` together. High confidence requires a contemporaneous source and clear event date. Medium confidence means the event is sourced but date, actor, or context needs checking. Low confidence means the entry is inferred, pleaded-only, or source-limited. `source_conflict` always requires lawyer review before advocacy use.

### 3. De-duplicate and reconcile

When multiple documents describe the same event:

- Group descriptions of the same event under one chronology entry where helpful.
- Keep each material source separately identified.
- Do not decide which account is true. Note why a contemporaneous source may carry more evidential weight, but preserve later inconsistent recollections or pleaded accounts.
- Note conflicts in date, actor, or description.

When sources conflict, classify the entry as `source_conflict` or `needs_lawyer_review`.

### 4. Identify gaps

After extraction, list:

- Missing periods.
- Missing custodians or counterparties.
- Events referenced but not sourced.
- Documents likely to exist but absent, such as notice letters, orders, board minutes, or payment records.

Gaps are part of the work product. Do not hide them.

### 5. Produce the chronology

Recommended table:

| Date | Date Certainty | Actor | Event | Source Identifier | Source Date | Quote | Confidence | Tags | Notes |
|---|---|---|---|---|---|---|---|

Then add:

- Key events.
- Disputed events.
- Source gaps.
- Verification checklist.
- Optional issue-specific or witness-specific extracts.

### 6. Statement-of-facts variant

Only produce a narrative statement of facts after the working chronology is complete. The narrative must:

- Preserve citations.
- Avoid unsourced legal conclusions.
- Exclude or flag disputed entries depending on the user's requested posture.
- Keep verification notes separate from advocacy prose.
- Never convert a disputed chronology entry into advocacy prose unless it is explicitly labelled as disputed or deliberately excluded.

## Out of Scope

- Merits assessment.
- Limitation-period interpretation without supplied rules and facts.
- Court deadline calculation without current rules, orders, and service facts.
- Advice on what facts to plead or omit.
- Public-record supplementation unless the user requests it and source tags are preserved.

## Escalation

Stop and route to the responsible lawyer when there is suspected privilege, irreconcilable source conflict on a key event, an unfamiliar jurisdiction or procedural regime, OCR/source quality too poor to support extraction, or a user asks for merits inference rather than chronology mapping.

## Example

```text
Build a working chronology from this folder of correspondence and pleadings. Cite every event to a source, quote the key words, and list gaps separately.
```

For a compact output pattern, see `examples/output.md`.
For event/date discipline, significance tags, and gap handling, see `references/chronology-model.md`.

## Limitations

- Scanned PDFs and images may need OCR.
- Metadata dates can be misleading.
- Privileged material requires care before export or sharing.
- The skill does not calculate court deadlines unless the controlling rules are supplied or researched separately.
