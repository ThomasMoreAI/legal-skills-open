# Reviewer Markup Model

Use this reference when the task involves multiple marked-up DOCX drafts, exported Word comments, or non-Word reviewer feedback.

## Core Doctrine

This workflow compiles a lawyer-controlled resolution checklist. It is not a redliner, merger, or auto-acceptance tool.

The master document remains the working source of truth. The lawyer edits the master in Word after reviewing each item. This matters for court-facing and client-facing documents because automatic DOCX merging can break numbering, cross-references, styles, tracked-change XML, footnotes, tables, and paragraph order.

## Resolution Unit

Each actionable item is a separate resolution unit:

| Source | Resolution Unit | Typical ID |
|---|---|---|
| Word comment | comment text plus anchor | `comment-{id}` |
| Word insertion | inserted text and local context | `revision-{id}` |
| Word deletion | deleted text and local context | `revision-{id}` |
| Replacement | paired deletion/insertion where confidently paired | `replacement-{id}` |
| Whole paragraph insertion/deletion | paragraph-level status | `paragraph-{index}` |
| Email/call/chat note | manual reviewer note | `manual-{id}` |

Resolution states:

- `unresolved` - not yet reviewed.
- `accepted` - lawyer has decided to make the change in the master.
- `rejected` - lawyer has decided not to make the change.
- `deferred` - lawyer needs instructions, source check, or strategic decision.
- `needs_manual_review` - extraction/location is unreliable.

Do not infer a resolution from seniority, tone, repetition, or apparent correctness.

## Item Taxonomy

Use these item types consistently:

- `comment` - reviewer comment without text change.
- `insertion` - proposed added text.
- `deletion` - proposed removed text.
- `replacement` - deletion and insertion that appear paired.
- `whole-paragraph-insertion` - entire paragraph added.
- `whole-paragraph-deletion` - entire paragraph deleted.
- `manual-note` - feedback from email, call, chat, conference, or notes.
- `formatting-risk` - formatting-only change that may hide substantive impact.
- `needs_manual_review` - unreliable extraction or location.

## Conflict Semantics

Use `conflict` narrowly. A conflict is not "two comments on the same topic." It means reviewer inputs create incompatible instructions or competing edits that cannot both be implemented.

Examples:

- One reviewer deletes a clause; another expands it.
- One reviewer changes a date; another comment says the date is not agreed.
- Two track-change authors alter the same paragraph in incompatible ways.

Keep possible but unproven conflicts as `potential_conflict` until the lawyer reviews.

## Paragraph Matching Risk

When collating multiple versions of a document, paragraph matching is approximate. It is useful for grouping review items, not proof that the item belongs exactly there.

Mark `location_confidence`:

- `exact` - comment anchor or revision context maps directly to the master.
- `approximate` - similar paragraph matched, but wording differs.
- `location_uncertain` - probable section known, exact anchor unclear.
- `manual_review` - table, footnote, text box, field, or heavy restructure prevents reliable mapping.

Heavy restructures, duplicate clauses, repeated definitions, schedules, tables, and numbering changes require spot-checking.

## Privacy and Source Handling

If the workflow is browser-local, local-file, or user-supplied, state that mode precisely. Do not overclaim "no network" unless runtime evidence proves it. For confidential drafts, preserve source filenames and reviewer names only where appropriate for the audience.

## Deliverables

Preferred outputs:

- Resolution checklist grouped in document order.
- Conflicts and potential conflicts.
- Manual-review items.
- High-risk legal drafting items: citations, pleaded relief/remedies, dates, figures, defined terms, signature blocks, limitation dates, privilege-sensitive wording.
- Optional JSON/CSV/HTML report for audit.

The report is a decision log. It is not the revised document.
