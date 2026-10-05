---
name: document-review-canhada-labs
title: Document Review Specialist
description: 'Legal document review for discovery, due-diligence, and regulatory

  submissions. Covers first-pass relevance triage, second-pass issue

  review, privilege log discipline, redaction protocols that flatten

  rather than overlay, technology-assisted review (TAR / predictive

  coding / continuous active learning), chain-of-custody tracking from

  collection through production, and production format compliance with

  jurisdiction-specific protocol orders. Handles bulk PII and special-

  category data inherent to discovery-scale review; applies LGPD Art. 11

  and GDPR Art. 9 controls for cross-border matters. Use when: conducting

  e-discovery or paper review in litigation or regulatory proceedings;

  performing due-diligence document review in M&A or financing

  transactions; building or auditing a TAR workflow; reviewing a

  privilege log for completeness; or verifying that a production set

  meets the receiving party''s format protocol order.'
author: Canhada-Labs
author_url: https://github.com/Canhada-Labs/ceo-orchestration/tree/main/.claude/skills/domains/legal/skills/document-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Document Review Specialist

## Cardinal Rule

No document may be withheld from a production set without a privilege log
entry that identifies the document by control number, states the privilege
basis (attorney-client / work-product / common-interest), names the
privilege holder, and documents the redaction or withhold rationale.
Withholding without a log entry is non-defensible under FRCP 26(b)(5) and
equivalent civil procedure rules in Brazilian, EU, and UK jurisdictions.
A privilege log incomplete at the time of production is treated as a
production deficiency, not a minor oversight.

## Fail-Fast Rule

Stop and return a structured failure report when any of the following is
true before or during a review engagement:

- A review protocol document does not exist. Review may not commence
  without a documented protocol specifying scope, issue codes, privilege
  criteria, and quality-control sampling thresholds.
- Redaction has been applied as a visual overlay (e.g. PDF annotation
  layer) rather than as a flattened burn-in. Reversible redactions
  constitute a data breach risk and a privilege waiver risk; the set
  must be reprocessed before delivery.
- PII or special-category data (health, biometric, financial, political
  affiliation) will cross a national border without a documented lawful
  transfer mechanism under LGPD Art. 33 or GDPR Chapter V. The transfer
  is blocked until the mechanism is confirmed.
- A TAR model has been trained on a seed set smaller than the minimum
  statistically defensible threshold defined in the review protocol, or
  the validation sampling plan has not been approved by supervising
  counsel.
- Chain-of-custody documentation has a gap: any hand-off between
  collection, processing, hosting, review, and production that lacks a
  timestamped transfer record must be resolved before production.

## When to Apply

Apply this skill when:

- Conducting e-discovery document review in civil litigation, regulatory
  investigation, or arbitration proceedings.
- Performing due-diligence review of a contract or data-room repository
  in an M&A, financing, or joint-venture transaction.
- Building, validating, or auditing a TAR or predictive-coding workflow
  for a large or recurring review matter.
- Reviewing a privilege log for structural completeness or preparing a
  privilege log for production.
- Verifying that a production set conforms to the receiving party's
  format protocol order (native, TIFF+OCR, PDF, load-file fields).
- Assessing whether a cross-border discovery request implicates LGPD,
  GDPR, or blocking-statute obligations.

Do not apply this skill to contract risk review or transactional
drafting — route those to `domains/legal/skills/contract-counsel`.
Do not apply to client intake or matter-opening workflows — route to
`domains/legal/skills/client-intake`.

## PII Handling

Discovery-scale review is inherently a bulk-PII operation. Every
document corpus contains personal data; many contain special-category
data under LGPD Art. 11 and GDPR Art. 9 (health records, financial
data, biometrics, political and religious affiliation, trade-union
membership). The following controls are mandatory, not advisory.

### Data Minimisation at Collection

The collection scope must be documented and defensible. Overly broad
collection that harvests personal data beyond the matter's scope
constitutes unnecessary processing under LGPD Art. 6(III) and GDPR
Art. 5(1)(c). Collection parameters (custodians, date ranges, search
terms) must be preserved as part of the chain-of-custody record.

### Redaction Discipline

Redaction of PII that is not responsive or that is outside the
production scope must be applied as a flattened operation. Tools that
produce annotation-layer or translucent-box redactions are prohibited
for productions containing personal data. After redaction, OCR must
be re-verified on the redacted output: text extracted from the
underlying layer before flattening has been the mechanism of multiple
inadvertent-disclosure incidents.

Metadata scrubbing is required for native productions. Hidden text,
revision history, author fields, embedded objects, and custom
properties must be stripped or confirmed absent before delivery.

### Cross-Border Data Sovereignty

When discovery involves documents that will be processed or hosted
outside Brazil or the EU, confirm the applicable transfer mechanism
before processing begins. LGPD Art. 33 permits international transfer
to jurisdictions with adequate protection, via standard contractual
clauses, or under other listed bases. GDPR Chapter V equivalents
apply for EU-domiciled data subjects. Blocking statutes in France,
Germany, and Switzerland impose criminal penalties for compliance with
foreign discovery orders without prior authorization; flag cross-border
requests touching these jurisdictions for counsel review before
responding.

### Special Categories

LGPD Art. 11 and GDPR Art. 9 impose heightened processing restrictions
on health, biometric, genetic, religious, political, trade-union, and
sexual-orientation data. Documents containing these categories must be
identified and tagged separately. Production of special-category data
requires explicit legal basis documentation beyond the general lawful
basis used for ordinary personal data.

Cross-link: `core/compliance-lgpd` for LGPD legal-basis matrix,
data-subject rights, breach notification timelines, and ANPD
registration requirements.

## Review Protocol Architecture

A review protocol document must exist and be approved by supervising
counsel before the first document is coded. The protocol defines:

- **Matter scope** — custodians, date range, collection sources,
  responsive subject-matter definition.
- **Issue code taxonomy** — exhaustive list of issue codes with
  definitions; no code may be applied outside the taxonomy.
- **Privilege criteria** — which communications qualify for
  attorney-client privilege, work-product protection, or
  common-interest doctrine in the governing jurisdiction; how
  to handle dual-purpose documents; treatment of in-house counsel.
- **QC sampling methodology** — random sample rate (floor and ceiling),
  targeted sample triggers (high-error reviewers, late-breaking
  responsive categories), and acceptance/rejection thresholds.
- **TAR parameters** — if TAR is used, seed-set size, validation
  sampling plan, elusion-testing protocol, and the criterion for
  declaring the model production-ready.

First-pass review focuses on relevance and responsiveness. Second-pass
review applies issue codes and identifies privilege claims. A third
quality-control pass by senior reviewers samples the first- and
second-pass outputs and measures error rates against protocol thresholds.

```
REVIEW PROTOCOL REGISTER
─────────────────────────────────────────
Matter:              [Matter name / ID]
Protocol Version:    [vN — date]
Approved By:         [Supervising counsel — name / role]
Scope Custodians:    [List]
Date Range:          [Start — End]
Responsive Scope:    [Subject-matter definition]
Issue Codes:         [Taxonomy ref — see §Appendix A]
Privilege Criteria:  [AC / WP / CI definitions — see §Appendix B]
QC Sample Rate:      [Random: N%; Targeted triggers: see §4]
TAR Parameters:      [Seed set: N docs; Validation: N%; Elusion: N%]
Protocol Status:     [DRAFT / APPROVED / SUPERSEDED]
─────────────────────────────────────────
```

## Privilege Logging

Every document withheld in full or redacted for privilege requires a
log entry. Common log fields aligned to federal and state court
expectations:

| Field | Required | Notes |
|---|---|---|
| Control number | Yes | Unique document identifier from processing |
| Privilege basis | Yes | AC / WP / CI — may be multiple |
| Privilege holder | Yes | Client entity; never the law firm alone |
| Author | Yes | Name and role |
| Recipients | Yes | All To / CC / BCC with roles |
| Date | Yes | Document date, not processing date |
| Document type | Yes | Email / memo / draft / report |
| Subject / description | Yes | Non-privileged description of general topic |
| Redacted vs. withheld | Yes | Partial redaction or full withhold |
| Redaction rationale | Yes | Specific basis for each redacted portion |

Attorney-client privilege requires: (1) a communication, (2) between
attorney and client (or agents of either), (3) for the dominant purpose
of legal advice, (4) maintained in confidence. Work-product protection
covers documents prepared in anticipation of litigation. Common-interest
doctrine extends privilege to communications among parties sharing a
common legal interest. Dual-purpose documents require analysis of
dominant purpose; the protocol must specify the governing standard.

Never log a document as privileged based on the presence of an attorney
as a recipient alone. Business advice communicated by in-house counsel
is not privileged. The privilege log must reflect an affirmative analysis
of each withheld document, not a blanket designation.

## Redaction Discipline

The following sequence is required for every redaction workflow:

1. Apply redaction using a tool that produces a burned-in, flattened
   output — not an annotation layer. Approved tools include those that
   produce TIFF images from rendered page content or PDF outputs verified
   by the tool vendor to flatten annotations before saving.
2. Verify that the redacted output does not expose underlying text via
   copy-paste, select-all, or text-extraction from any layer.
3. Re-run OCR on the redacted output. OCR extracted before flattening
   may have indexed the now-redacted text; the index must be rebuilt
   from the post-redaction image.
4. Strip metadata from the output file: author, revision history,
   hidden text, custom properties, embedded objects, tracked changes.
5. Document the redaction rationale in the privilege log (for privilege
   redactions) or in the processing log (for PII-minimisation redactions).

Redaction that can be reversed — including PDF annotation layers visible
to PDF-editing software, highlight-over-white-background renders, and
redactions applied only to the display layer of a document viewer — must
be reprocessed before any delivery. Inadvertent disclosure of redacted
content constitutes a potential privilege waiver and a data-breach event.

## Technology-Assisted Review

TAR (predictive coding / continuous active learning) is a defensible
supplement to human review, not a replacement for human judgment on
privilege decisions. The following constraints apply:

- **Privilege decisions are human-only.** A TAR model may not make final
  privilege calls. It may flag documents for privilege review; a
  qualified human reviewer must review and code each flagged document.
- **Seed set defensibility.** The seed set must be large enough and
  diverse enough to train a model representative of the corpus. The
  protocol must specify the minimum seed set size with statistical
  justification. A seed set composed only of documents retrieved by
  keyword search introduces selection bias.
- **Validation sampling.** Random sampling of the model's non-responsive
  predictions (elusion testing) measures the recall rate. The protocol
  must specify the acceptable elusion threshold. Crossing the threshold
  requires either additional active-learning rounds or supplemental
  manual review.
- **Model versioning.** Each retrained model version must be logged with
  the training date, seed-set composition, and validation results. A
  production decision based on a superseded model version is not
  defensible.
- **Transparency.** If opposing counsel requests disclosure of the TAR
  methodology, the process log must be sufficient to reconstruct the
  training history. Withholding TAR methodology details that are
  required by court order or stipulated protocol is non-compliance.

## Chain of Custody

A defensible production requires an unbroken chain of custody from
original collection through final delivery. Each hand-off must be
logged with a timestamp, the identity of both transferring and receiving
parties, and a hash-verification record confirming file integrity.

```
CHAIN-OF-CUSTODY LOG
─────────────────────────────────────────
Step        From              To                Date       Hash-Verified
─────────────────────────────────────────
Collection  Custodian device  Collection agent  YYYY-MM-DD Yes / No
Processing  Collection agent  Review platform   YYYY-MM-DD Yes / No
Hosting     Processing vendor Review counsel    YYYY-MM-DD Yes / No
Review      Review platform   QC supervisor     YYYY-MM-DD Yes / No
Production  Review counsel    Receiving party   YYYY-MM-DD Yes / No
─────────────────────────────────────────
Gap flag:   [Any step with missing log entry — STOP before production]
```

Federal Rules of Evidence Rule 901(b)(9) requires that a process or
system that produces an accurate result be described and the result shown
to be produced by that process. FRCP 26(b) requires disclosure of
sources of electronically stored information. Gaps in the custody chain
create authentication vulnerability and may expose production to
admissibility challenges.

## Production Format Compliance

Every production must conform to the receiving party's format protocol
order or, absent a protocol order, to the format specified in the
applicable procedural rules. Key dimensions:

- **Format** — native (original file format), TIFF+OCR (page images
  with extracted text), or PDF. The protocol order governs; absent an
  order, negotiate before processing.
- **Load file** — Concordance DAT, Relativity CSV, or equivalent.
  Field names, delimiters, and encoding must match the receiving
  party's specification exactly. Mismatched delimiters cause import
  failures that delay review.
- **Metadata fields** — standard fields (BegBates, EndBates, BegAttach,
  EndAttach, Custodian, Date Sent, Author, Subject, FileType) plus
  matter-specific fields specified in the protocol. Omitted fields
  cannot be added after production without re-production.
- **Bates numbering** — sequential, unique, and per-document. Duplicate
  or non-sequential Bates numbers require re-production.
- **Image resolution** — minimum 300 DPI for TIFF productions; OCR
  accuracy degrades below this threshold.

## Anti-Patterns

| Anti-Pattern | Risk | Correct Approach |
|---|---|---|
| Annotation-layer redaction | Reversible; constitutes data breach risk and privilege waiver risk | Flatten to burned-in image; verify with text-extraction test |
| Privilege log absent or incomplete | Non-defensible; adverse inference risk; sanctions exposure | Every withheld or redacted-for-privilege document gets a complete log entry before production |
| Review commenced without a protocol document | Inconsistent coding; QC has no baseline; court-challenge vulnerability | Draft and approve protocol before first document is coded |
| TAR model used for privilege decisions without human review | Unacceptable; privilege is a legal determination requiring human judgment | TAR flags for review; human reviewer makes each privilege call |
| Chain-of-custody gap unresolved before production | Authentication vulnerability; admissibility challenge | Identify and document resolution for every gap; do not produce until chain is complete |
| Metadata not stripped from native productions | Hidden personal data; hidden revision history; potential inadvertent disclosure | Run metadata scrub and verify output before delivery |
| Cross-border transfer without documented lawful basis | LGPD Art. 33 / GDPR Ch. V violation; regulatory penalty exposure | Confirm transfer mechanism before data leaves originating jurisdiction |
| Elusion testing omitted from TAR workflow | Unknown recall; non-defensible completeness representation | Include elusion testing in validation plan; document results |

## Cross-References

- `core/compliance-lgpd` — LGPD legal-basis matrix, data-subject
  rights, breach notification timelines, ANPD registration requirements,
  cross-border transfer mechanisms under Art. 33.
- `domains/legal/skills/client-intake` — matter-opening, conflict
  check, engagement letter, and initial data-assessment workflows
  that precede document review.
- `core/security-and-auth` — data-at-rest encryption, access-control
  requirements for review platforms, and audit-log standards applicable
  to review-platform access events.

## ADR Anchors

- **ADR-058** — Bulk creative authoring strategy governing structural
  inspiration from upstream agency-agents corpus. This skill's content
  is an original ceo-orchestration composition; `inspired_by:` records
  the upstream file used as a structural reference only.
