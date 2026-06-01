---
name: collating-reviewer-feedback
title: collating-reviewer-feedback
description: Use when users say "collate comments", "combine reviewer markups", "compile tracked changes", "make a resolution checklist", or have multiple DOCX drafts, Word comments, redlines, partner/client markups, or external feedback to review without auto-merging.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/collating-reviewer-feedback
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [docx, comments, track-changes, litigation, drafting, review-workflow]
---

# collating-reviewer-feedback

## When to Use

- Multiple reviewers returned Word documents with comments or tracked changes.
- The team needs to see every proposed edit, comment, and conflict in one place.
- The master document is court-facing, client-facing, or otherwise too risky to auto-merge.
- Feedback arrived outside Word, such as email, Teams, WhatsApp, phone notes, or conference comments, and needs to be added to the same resolution list.

Do not use this skill to automatically accept, reject, or merge changes into the master document. The output is a review checklist. The lawyer makes every document edit.

## Audience and Work Shape

Audience: drafting and litigation lawyers, trainees, and paralegals who own or support the master document and understand Word comments/track changes.

Work shape: pattern-matched review with bounded extraction. The skill compiles, groups, and classifies reviewer inputs; it does not decide the legal or drafting outcome.

## Legal Failure Modes

- Legal support, not legal advice: the checklist is a review aid. The responsible lawyer decides whether and how to amend the master.
- Privilege/confidentiality: privileged or confidential drafts must be processed only in an approved environment. Uploading drafts or extracted comments to an unapproved third-party AI surface may affect privilege or confidentiality.
- Accountability: every item defaults to `open` or `unresolved`; a lawyer owns each accept/reject/defer decision.

## Access Modes

This skill works in two practical modes:

1. **File mode** - use uploaded or accessible DOCX files, reviewer versions, exports, or extracted Word markup.
2. **User-supplied text mode** - use pasted comments, exported revision tables, screenshots, email notes, or manually supplied feedback.

If reviewer files or extracted markup are unavailable, prepare an intake checklist and do not claim to have collated Word comments or track changes.

## How It Works

### 1. Establish the master and reviewer set

Identify:

- The master draft the lawyer will edit.
- Each reviewer version and reviewer name.
- Whether each file is a full draft, partial draft, or external notes.
- Any deadline or filing constraint that affects how conservative the review should be.

If the master is unclear, stop and ask. A checklist built against the wrong base document is not reliable.

### 2. Extract review items

For each reviewer version, extract:

- Word comments, including author, date, anchor text, and comment text.
- Track changes, including insertions, deletions, moved text where detectable, and paragraph-level insertions or deletions.
- Nearby paragraph text so the lawyer can locate the issue in the master.
- External comments added manually, with source and date.

Preserve reviewer identity and original proposed wording exactly. Do not collapse two reviewers into one anonymous note unless the user asks for anonymization. If a table, text box, footnote, field, or other complex Word structure cannot be extracted reliably, create a `needs_manual_review` item rather than omitting it.

### 3. Group without pretending to merge

Group items by likely paragraph or clause. Use approximate matching only to organize the review. If matching is uncertain, mark the item as `location_uncertain`.

Within each group, classify:

- `comment` - reviewer comment without text change.
- `insertion` - proposed added text.
- `deletion` - proposed removed text.
- `replacement` - deletion and insertion that appear paired.
- `whole-paragraph-change` - inserted or deleted paragraph.
- `external-note` - manually added feedback.
- `conflict` - reviewers propose incompatible outcomes.

### 4. Produce the checklist

Output a resolution checklist with one row per item:

| Field | Meaning |
|---|---|
| `id` | Stable item id |
| `source_file` | reviewer file or external note source |
| `source_item_id` | Word comment id, revision id, or external note id where available |
| `source_timestamp` | comment/revision/note date where available |
| `location` | paragraph, heading, clause, or best available anchor |
| `location_confidence` | `exact`, `approximate`, `location_uncertain`, or `manual_review` |
| `reviewer` | source reviewer or external source |
| `type` | classification above |
| `proposal` | exact proposed text or comment |
| `context` | nearby master text |
| `status` | `open`, `accepted`, `rejected`, or `deferred` |
| `notes` | lawyer's resolution note |

Keep the default status `open`. Do not infer acceptance from reviewer seniority.

## Confidence Bands

Use `location_confidence` as the operative confidence band: `exact`, `approximate`, `location_uncertain`, or `manual_review`. Anything affecting tables, footnotes, text boxes, numbering, duplicated clauses, or heavily reworked paragraphs should default down to `location_uncertain` or `manual_review`.

### 5. Call out conflicts and high-risk items

Surface separately:

- Direct conflicts between reviewers.
- Comments anchored to text that cannot be found in the master.
- Whole-paragraph deletions or insertions.
- Formatting-only changes that may hide substantive changes.
- Items affecting citations, pleadings, defined terms, relief/remedies sought, signature blocks, dates, or numbers.

### 6. Export for lawyer action

Recommended outputs:

- A human-readable checklist for review.
- A JSON or CSV export for re-import or audit.
- A printable report grouped by document order.

The final step is always: the lawyer edits the master document in Word and checks off the resolution list.

## Escalation

Stop and route to the responsible lawyer when a conflict turns on legal substance, including privilege waiver, settlement strategy, regulatory exposure, pleaded relief/remedies, limitation, admissions, or client instructions. Do not classify these as ordinary drafting conflicts.

## Example

User: "I have partner, client, and associate comments on the same draft. Can you combine them?"

Response pattern:

1. Confirm the master draft.
2. Read each reviewer version.
3. Produce a grouped checklist.
4. Flag conflicts and uncertain anchors.
5. Remind the user that no merged document has been produced.

For a compact output pattern, see `examples/output.md`.
For the detailed item taxonomy, conflict semantics, and paragraph-matching model, see `references/reviewer-markup-model.md`.

## Limitations

- Approximate paragraph matching can be wrong when drafts have diverged heavily.
- Complex nested track changes, tables, text boxes, and footnotes may need manual review.
- The skill does not produce a clean merged DOCX.
- Privileged or confidential drafts should be processed only in an environment approved for the matter.
