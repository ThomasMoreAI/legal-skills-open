---
name: build-document-index-l0cka
title: Build Document Index
description: Build a numbered, source-linked document index as a .docx file from supplied legal matter documents — one row per document or coherent file group with a stable source ID, recorded date, type, author, recipients, description taken from the document itself, page count, readability and duplicate or version links — suitable as a court-book or bundle index and as the source register for a chronology or privilege log. Use for litigation, investigations, regulatory responses, disclosure and brief preparation. Do not use to decide relevance, privilege, admissibility or weight, or to claim the set is complete beyond the supplied documents.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/legal-evidence-workflows/skills/build-document-index
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Build Document Index

Inventory supplied evidence into a stable, reviewable index without deciding
what any document proves. Every row is traceable to one supplied file, the
source documents stay unchanged, and the index is delivered as a Word `.docx`
file so it can become the front of a bundle or the source register of a
chronology.

## Workflow

1. Define the index set.
   - Record the matter label, the supplied set (folder, upload or bundle
     reference) and any practitioner instruction on ordering or numbering.
   - State that the index covers only the supplied and readable documents.
2. Build the source review table.
   - Use the runtime's native review-table or structured document-review feature
     when available. Do not replace an available native table with prose.
   - Treat each document or coherent file group (an email and its attachments,
     a contract and its schedules) as a source row. Use these columns: source
     ID; file name; document date as recorded; document type; author or
     sender; recipients or parties; description; page or item count;
     readability; duplicate, version or attachment relationship; and reviewer
     status.
   - If no native table exists, use the same schema as an internal structured
     extraction and state in the final document that cell verification and
     native source navigation were unavailable.
3. Describe each document from its own text.
   - Take the description from the document's title, heading, subject line or
     opening — quote or closely paraphrase it and give the pinpoint. Never
     summarise what the document proves or invent a title for an untitled file.
   - Preserve the source's exact date wording before adding a normalised
     value. Record an undated document as `undated`; never infer a date from
     file metadata without saying so.
   - Mark duplicates, near-duplicates, drafts and later versions by linking
     source IDs. Do not discard any file; a duplicate stays in the index with
     its link.
4. Number and order the index.
   - Assign stable source IDs in the order supplied unless the practitioner
     instructs chronological or category ordering. Once assigned, an ID never
     changes; a re-ordered index keeps the same IDs.
   - Where a bundle numbering scheme is supplied (tab, volume, page range),
     record it beside the source ID; never renumber the supplied scheme.
5. Create the Word index.
   - Create a new `.docx` file. If the user supplies an approved index or
     court-book template, use a working copy and preserve its styles;
     otherwise use a clean, restrained professional layout suitable for legal
     review.
   - Include: title and document status; index scope and supplied-source
     limitation; the index table; a relationships table (duplicates, versions,
     attachments); unreadable and missing items; review record; and
     limitations.
   - Use a landscape section when needed for readability. Repeat table
     headings across pages, allow rows to expand and do not shrink text to
     force the table onto fewer pages.
   - Mark the document `DRAFT - HUMAN REVIEW REQUIRED`. Use reviewer names,
     firm branding or matter identifiers only when supplied or approved.
6. Check integrity and gaps.
   - Confirm that every supplied file appears exactly once as a row or as a
     linked member of a file group, and that every row points to a supplied
     file.
   - List unreadable, password-protected, corrupt or empty files, missing
     attachments referred to in a document, and broken numbering sequences.
   - Confirm that the output is a valid `.docx`, opens successfully and
     contains the expected sections and rows. Use the runtime's document
     preview when available and inspect every page for clipped text, broken
     tables and unreadable entries. If visual inspection is unavailable, state
     that limitation in the document and result status.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

```text
Index scope: <matter label; supplied set; ordering instruction>
Source review table: <native table reference or structured fallback>
DOCX index: <filename; valid and opened; visual QA status>
Index table: <source ID; bundle reference; file name; recorded and normalised
  date; type; author; recipients; description and pinpoint; pages;
  readability>
Relationships: <duplicates, versions and attachments by source ID>
Unreadable or missing: <file; reason; practitioner action>
Review record: <unreviewed | corrected | verified, with human reviewer details
  only when supplied>
Limitations: <supplied-source boundary; description and dating limits>
```

Use `READY FOR HUMAN REVIEW` when every supplied file is indexed and a valid
`.docx` passed the available document checks. Use `READY WITH QUALIFICATIONS`
when the `.docx` remains useful despite unreadable files, undated items or
unavailable visual inspection. Use `NOT READY` when the supplied set cannot be
identified reliably or the runtime cannot create a valid `.docx`. Use
`OUTSIDE SCOPE` when the request requires a finding about relevance,
privilege, credibility, admissibility, weight or merits.

## Fail closed

Never invent a title, date, author, recipient, page count or relationship.
Never omit a supplied file or merge distinct documents into one row. Never
describe what a document proves, label it relevant or irrelevant, or mark it
privileged — those are practitioner decisions handled in other workflows. Do
not claim the index is complete beyond the supplied and readable set. Do not
alter, send, file, publish or disclose source documents or the index without
separate human authorisation. Do not substitute Markdown, PDF, a spreadsheet
or prose-only output for the required `.docx` index.
