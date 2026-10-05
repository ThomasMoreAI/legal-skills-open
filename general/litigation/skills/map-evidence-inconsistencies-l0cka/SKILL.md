---
name: map-evidence-inconsistencies-l0cka
title: Map Evidence Inconsistencies
description: Map where supplied legal matter documents and accounts agree, diverge or are silent on each material fact, as a .docx file — a fact-by-source matrix with pinpoints, a corroboration register and a divergence register that quotes each competing passage, classifies the divergence (date, amount, sequence, participant, wording, omission) and lists the question a reviewer must resolve — without deciding which account is right. Use after a chronology exists, for witness preparation, cross-examination planning, investigations and regulatory responses. Do not use to assess credibility, reliability, weight or admissibility, to decide that a witness is lying or mistaken, or to draft findings.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/legal-evidence-workflows/skills/map-evidence-inconsistencies
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Map Evidence Inconsistencies

Show, fact by fact, what each source says and where the sources part company,
so a practitioner can decide what to test. The map records agreement,
divergence and silence with pinpoints; it never ranks the accounts. Source
documents stay unchanged and the map is delivered as a Word `.docx` file.

## Workflow

1. Define the mapping set and the material facts.
   - Record the matter label, the supplied documents (or the chronology and
     document index they come from) and the practitioner's list of material
     facts or issues to map. If no list is supplied, derive candidate facts
     from the chronology's conflict register and events, label them
     `candidate` and ask the practitioner to confirm before treating the map as
     complete.
   - State that the map covers only the supplied and readable sources.
2. Build the fact-by-source review table.
   - Use the runtime's native review-table or structured document-review feature
     when available. Do not replace an available native table with prose.
   - Treat each material fact as a row and each source as a column, or each
     fact-source pair as a row when the runtime table is one-dimensional. For
     every pair record: what the source says (quoted or closely paraphrased);
     pinpoint; the source's date and character (`contemporaneous record`,
     `reported recollection`, `allegation`, `inference` or `unclear`); and
     whether it is `consistent`, `divergent` or `silent` relative to the other
     sources on that fact.
   - If no native table exists, use the same schema as an internal structured
     extraction and state in the final document that cell verification and
     native source navigation were unavailable.
3. Classify each divergence.
   - Quote each competing passage with its pinpoint. Classify the divergence
     as `date or time`, `amount or quantity`, `sequence`, `participant`,
     `wording or characterisation`, `omission` or `internal` (one source
     contradicting itself). A divergence may carry more than one class.
   - Record the question a reviewer would need answered — a missing document,
     a witness clarification, a metadata check — rather than an answer.
   - Record silence as silence. A source that does not mention a fact is not
     evidence against it and is not marked divergent.
4. Record corroboration without weighing it.
   - Where two or more sources agree, list them with pinpoints and note
     whether they are independent on their face or appear to derive from the
     same origin (a forwarded email, a copied statement). Note derivation as a
     provenance fact, never as a view on reliability.
5. Create the Word map.
   - Create a new `.docx` file. If the user supplies an approved template, use
     a working copy and preserve its styles; otherwise use a clean, restrained
     professional layout suitable for legal review.
   - Include: title and document status; mapping scope, fact list status and
     supplied-source limitation; the fact-by-source matrix; the divergence
     register; the corroboration register; silences and gaps; review record;
     and limitations.
   - Use a landscape section for the matrix. Repeat table headings across
     pages, allow rows to expand, keep quotations and pinpoints readable and
     do not shrink text to force the table onto fewer pages.
   - Mark the document `DRAFT - HUMAN REVIEW REQUIRED`. Use reviewer names,
     firm branding or matter identifiers only when supplied or approved.
6. Check traceability and gaps.
   - Confirm that every matrix cell other than `silent` points to a source and
     usable pinpoint or an express pinpoint limitation, and that every
     divergence register entry quotes at least two passages.
   - List unreadable files, facts with a single source, facts the practitioner
     listed that no source addresses, and divergences that a missing document
     might resolve.
   - Confirm that the output is a valid `.docx`, opens successfully and
     contains the expected sections and rows. Use the runtime's document
     preview when available and inspect every page. If visual inspection is
     unavailable, state that limitation in the document and result status.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

```text
Mapping scope: <matter label; supplied sources; fact list supplied or candidate>
Fact-by-source table: <native table reference or structured fallback>
DOCX inconsistency map: <filename; valid and opened; visual QA status>
Matrix: <fact ID; per source: statement, pinpoint, character, consistent |
  divergent | silent>
Divergence register: <divergence ID; fact ID; competing passages and
  pinpoints; classes; reviewer question>
Corroboration register: <fact ID; agreeing sources and pinpoints; independent
  on the face | apparently derived>
Silences and gaps: <facts with one or no source; unreadable material; missing
  documents that might resolve a divergence>
Review record: <unreviewed | corrected | verified, with human reviewer details
  only when supplied>
Limitations: <supplied-source boundary; candidate fact list; no view on truth>
```

Use `READY FOR HUMAN REVIEW` when the matrix is traceable, the fact list was
supplied or confirmed and a valid `.docx` passed the available document
checks. Use `READY WITH QUALIFICATIONS` when the `.docx` remains useful
despite a candidate fact list, unreadable material, pinpoint limitations or
unavailable visual inspection. Use `NOT READY` when source identity or
traceability is too weak to support a reviewable map, or the runtime cannot
create a valid `.docx`. Use `OUTSIDE SCOPE` when the request requires a view on
credibility, reliability, weight, admissibility, legal effect or merits, or a
finding about what happened.

## Fail closed

Never decide which account is correct, describe a witness as credible,
unreliable, lying or mistaken, or rank sources. Never invent a statement,
quotation, pinpoint, date or participant, and never paraphrase a passage in a
way that removes or adds a divergence. Never convert silence into evidence
that an event did not occur, and never merge divergent accounts into one
agreed fact. Do not claim the map is complete beyond the supplied and readable
sources or the confirmed fact list. Do not alter, send, file, publish or
disclose source documents or the map without separate human authorisation. Do
not substitute Markdown, PDF, a spreadsheet or prose-only output for the
required `.docx` map.
