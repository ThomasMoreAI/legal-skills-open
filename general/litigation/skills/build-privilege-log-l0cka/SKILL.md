---
name: build-privilege-log-l0cka
title: Build Privilege Log
description: Prepare a draft privilege log as a .docx file from supplied legal matter documents — one row per document or family with the source ID, date, author and recipient roles, the basis the practitioner has instructed or the document's own face suggests (legal advice, litigation, without prejudice, confidential), the facts that support or undercut the claim, third-party circulation and possible waiver flags — with every claim left as a practitioner decision. Use for disclosure and discovery, subpoena and notice-to-produce responses, regulatory productions and privilege reviews. Do not use to decide that privilege exists or is lost, to assert a claim to a court or regulator, or for non-Australian privilege rules unless the practitioner supplies them.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/legal-evidence-workflows/skills/build-privilege-log
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Build Privilege Log

Organise the facts a practitioner needs to decide privilege, document by
document, without deciding it. The log records what each document shows about
who made it, for whom and why, and lists the questions a claim would have to
answer. Every claim remains a practitioner decision, the source documents stay
unchanged and the log is delivered as a Word `.docx` file.

## Workflow

1. Define the log set and the instructed bases.
   - Record the matter label, the supplied set (or the document index it was
     drawn from), the production or disclosure obligation it answers, and the
     practitioner's instructions on the bases to consider.
   - Record the rules the practitioner names — the applicable Evidence Act
     provisions, court rules or common-law principles — as the framework for
     the log. Do not select a framework; if none is supplied, log under
     descriptive bases only and flag the gap.
   - State that the log covers only the supplied and readable documents.
2. Build the source review table.
   - Use the runtime's native review-table or structured document-review feature
     when available. Do not replace an available native table with prose.
   - Treat each document or coherent family (an email chain, an advice and its
     enclosures) as a source row. Use these columns: source ID; document date;
     document type; author and role; recipients and roles; lawyer involvement
     as shown on the face; stated purpose or subject as shown on the face;
     confidentiality markings; third-party circulation; candidate basis;
     supporting facts and pinpoints; facts against the claim; waiver flags;
     and reviewer status.
   - If no native table exists, use the same schema as an internal structured
     extraction and state in the final document that cell verification and
     native source navigation were unavailable.
3. Record the facts bearing on each candidate claim.
   - Take roles, purpose and markings from the document's own face and cite
     the pinpoint. Label a lawyer's involvement as `on the face`, `stated by
     practitioner` or `cannot be determined`; never infer that a copied lawyer
     was giving advice.
   - Record circulation to anyone outside the client and its legal advisers,
     forwarding, quotation in other documents, and any reference to the
     document in a non-privileged document as waiver flags with pinpoints.
     Flag; never decide waiver.
   - Where a family mixes privileged-looking and other content, record the
     part-privilege candidate and the pages or passages involved for
     redaction review.
   - Record a basis as `candidate` only. Use `cannot be determined` where the
     face of the document does not show purpose or roles.
4. Create the Word log.
   - Create a new `.docx` file. If the user supplies an approved privilege-log
     template or a court-prescribed form, use a working copy and preserve its
     styles; otherwise use a clean, restrained professional layout suitable
     for legal review.
   - Include: title and document status; log scope, instructed framework and
     supplied-source limitation; the privilege log table; a waiver-flag
     register; part-privilege and redaction candidates; unreadable items;
     review record; and limitations.
   - Use a landscape section when needed. Repeat table headings across pages,
     allow rows to expand and do not shrink text to force the table onto
     fewer pages.
   - Mark the document `DRAFT - HUMAN REVIEW REQUIRED` and label every basis
     column `candidate`. Use reviewer names, firm branding or matter
     identifiers only when supplied or approved.
5. Check traceability and gaps.
   - Confirm that every row points to a supplied source and usable pinpoint or
     an express pinpoint limitation, and that every candidate basis has at
     least one supporting fact recorded.
   - List unreadable files, missing enclosures, chains with missing earlier
     messages and documents whose author or purpose cannot be determined.
   - Confirm that the output is a valid `.docx`, opens successfully and
     contains the expected sections and rows. Use the runtime's document
     preview when available and inspect every page. If visual inspection is
     unavailable, state that limitation in the document and result status.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

```text
Log scope: <matter label; supplied set; obligation answered; instructed framework>
Source review table: <native table reference or structured fallback>
DOCX privilege log: <filename; valid and opened; visual QA status>
Privilege log table: <source ID; date; type; author and role; recipients and
  roles; lawyer involvement; purpose on the face; markings; circulation;
  candidate basis; supporting facts and pinpoints; facts against; waiver
  flags>
Waiver-flag register: <flag ID; source IDs; circulation or reference; question
  for the practitioner>
Part-privilege candidates: <source ID; pages or passages; reason>
Unreadable or undetermined: <file; reason; practitioner action>
Review record: <unreviewed | corrected | verified, with human reviewer details
  only when supplied>
Limitations: <supplied-source boundary; framework gaps; face-of-document limits>
```

Use `READY FOR HUMAN REVIEW` when every row is traceable, every basis is
labelled candidate and a valid `.docx` passed the available document checks.
Use `READY WITH QUALIFICATIONS` when the `.docx` remains useful despite
unreadable material, undetermined roles or purposes, an unsupplied framework
or unavailable visual inspection. Use `NOT READY` when source identity or
traceability is too weak to support a reviewable log, or the runtime cannot
create a valid `.docx`. Use `OUTSIDE SCOPE` when the request requires a
decision that privilege exists or is lost, an assertion to a court or
regulator, or a non-Australian privilege rule the practitioner has not
supplied.

## Fail closed

Never decide that a document is privileged, not privileged or that privilege
is waived; never state a conclusion on dominant purpose, and never express a
view on credibility, weight, admissibility or merits. Never invent an
author, recipient, role, purpose, marking, date or pinpoint, and never infer
legal advice from a lawyer's name alone. Never omit a supplied document from
the log or merge distinct documents into one row without recording the
family. Do not claim the log is complete beyond the supplied and readable
set. Do not alter, send, file, produce, publish or disclose source documents
or the log without separate human authorisation. Do not substitute Markdown,
PDF, a spreadsheet or prose-only output for the required `.docx` log.
