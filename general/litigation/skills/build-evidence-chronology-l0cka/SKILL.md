---
name: build-evidence-chronology-l0cka
title: Build Evidence Chronology
description: Build a source-linked evidence chronology as a .docx file from supplied legal matter documents using a native structured document-review table when available, preserving exact date wording, conflicting accounts, allegations, inferences and evidence gaps for human review. Use for litigation, investigations, regulatory responses, disputes or other matters requiring an auditable sequence of events. Do not use to decide credibility, evidentiary weight, admissibility, legal effect or merits, or to claim completeness beyond the supplied documents.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/legal-evidence-workflows/skills/build-evidence-chronology
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Build Evidence Chronology

Organise supplied evidence into a reviewable sequence without turning disputed
material into an agreed narrative. Keep every material event traceable to the
source set, preserve the source documents unchanged and deliver the chronology
as a Word `.docx` file.

## Workflow

1. Define the review set.
   - Record the matter label, supplied date range and issue focus, if any.
   - Inventory every supplied file with a stable source ID, title, date as
     recorded, document type and readability status.
   - State that the output covers only the supplied and readable documents.
2. Build the source review table.
   - Use the runtime's native review-table or structured document-review feature
     when available. Do not replace an available native table with prose.
   - Treat each document or coherent file group as a source row. Use these
     columns: source ID; document date; document type; author or sender;
     recipients or participants; event candidates; exact date wording;
     supporting passage and pinpoint; evidence character; contradiction or
     uncertainty; and reviewer status.
   - If no native table exists, use the same schema as an internal structured
     extraction and state in the final document that cell verification and
     native source navigation were unavailable.
3. Extract event candidates.
   - Describe only events supported by a cited source passage. Preserve the
     source's exact date and time wording before adding any normalised value.
   - Characterise support as `contemporaneous record`, `reported recollection`,
     `allegation`, `inference` or `unclear`. This is a provenance label, not a
     conclusion about admissibility, truth or weight.
   - Record page, paragraph, section, email timestamp or other usable pinpoint.
     If no pinpoint is available, say so; never invent one.
4. Build the event-level chronology from the source review table.
   - Give each event a stable event ID. Sort unambiguous normalised dates in
     ascending order, but preserve the source wording beside each value.
   - Put ambiguous, approximate, relative and undated events in visibly marked
     positions. Do not invent ordering within the same date or resolve relative
     dates without source support.
   - Consolidate duplicate descriptions only when they concern the same event.
     Preserve every supporting source and pinpoint.
   - Keep inconsistent accounts as separate entries and link them through a
     conflict ID. Do not average, reconcile or silently prefer one account.
5. Create the Word chronology.
   - Create a new `.docx` file. If the user supplies an approved chronology
     template, use a working copy and preserve its styles; otherwise use a
     clean, restrained professional layout suitable for legal review.
   - Include: title and document status; review scope and supplied-source
     limitation; chronology table; conflict register; evidence gaps; source
     register; review record; and limitations.
   - Use a landscape chronology section when needed for readability. Repeat
     table headings across pages, allow rows to expand, keep source pinpoints
     readable and do not shrink text to force the table onto fewer pages.
   - Use these chronology columns: event ID; recorded and normalised date/time;
     event; people or entities; source IDs and pinpoints; evidence character;
     and conflict, qualification or gap.
   - Mark the document `DRAFT - HUMAN REVIEW REQUIRED`. Use reviewer names,
     firm branding or matter identifiers only when supplied or approved.
6. Check traceability, document integrity and gaps.
   - Confirm that every material chronology row points to at least one source
     row and usable pinpoint or an express pinpoint limitation.
   - List unreadable files, missing attachments, broken sequences, unexplained
     date gaps and conflicts requiring human resolution.
   - Mark reviewer corrections separately from extracted source content.
   - Confirm that the output is a valid `.docx`, opens successfully and contains
     the expected sections and chronology rows. Use the runtime's document
     preview or rendering capability when available and inspect every page for
     clipped text, broken tables and unreadable pinpoints. If visual inspection
     is unavailable, state that limitation in the document and result status.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

```text
Review scope: <matter label; supplied date range and issue focus>
Source register: <source ID; title; recorded date; type; readability>
Source review table: <native table reference or structured fallback>
DOCX chronology: <filename; valid and opened; visual QA status>
Chronology table: <event ID; recorded and normalised date/time; event;
  people/entities; source IDs and pinpoints; evidence character;
  conflict, qualification or gap>
Conflict register: <conflict ID; competing entries; source IDs; human question>
Evidence gaps: <missing, unreadable, ambiguous or unexplained material>
Review record: <unreviewed | corrected | verified, with human reviewer details
  only when supplied>
Limitations: <supplied-source boundary; unresolved traceability or ordering>
```

Use `READY FOR HUMAN REVIEW` when the chronology is traceable but has not been
human-verified and a valid `.docx` passed the available document checks. Use
`READY WITH QUALIFICATIONS` when the `.docx` remains useful despite identified
unreadable material, pinpoint limitations, material gaps or unavailable visual
inspection. Use `NOT READY` when source identity or traceability is too weak to
support a reviewable chronology, or the runtime cannot create a valid `.docx`.
Use `OUTSIDE SCOPE` when the request requires a finding about credibility,
weight, admissibility, legal effect or merits.

## Fail closed

Never invent an event, date, time, person, source, quotation, pinpoint or causal
connection. Never convert silence into evidence that an event did not occur.
Never merge conflicting accounts into a single fact, relabel an allegation as
established, or express a view on credibility, weight, admissibility, legal
effect or merits. Do not claim the chronology is complete beyond the supplied
and readable source set. Do not alter, send, file, publish or disclose source
documents or the chronology without separate human authorisation. Do not
substitute Markdown, PDF, a spreadsheet or prose-only output for the required
`.docx` chronology.
