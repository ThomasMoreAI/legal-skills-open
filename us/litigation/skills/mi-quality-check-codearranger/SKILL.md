---
name: mi-quality-check-codearranger
title: Michigan Pre-Filing Quality Check
description: 'Use to QC, review, or validate a Michigan court document before filing. Triggers include "quality check Michigan filing", "is my Michigan motion ready to file", "MCR 1.109 compliance", "pre-filing review Michigan", "QC this Michigan document", "validate this Michigan affidavit". Runs two-pass check: (1) format pass — MCR 1.109 document format and signature, MCR 2.113 caption and pleading form, MCR 2.107 proof of service, line numbering + footer + "Page X of Y", redaction of protected personal info (MCR 1.109(D)); (2) content pass — citations resolvability, affirmative defenses separately stated (MCR 2.111(F)), required-component completeness, attachments, packet consistency. Lighter than `mi-fact-check`; defers evidentiary citations to that skill.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Michigan Pre-Filing Quality Check

> **NOT LEGAL ADVICE.** This skill detects errors in form and
> structural completeness. It does not assess substantive legal
> sufficiency. Verify against current Michigan Court Rules and the
> filing court's local administrative orders before filing.

Use this skill as the **last step** before filing any Michigan court
document. Two passes, plus a packet-consistency sweep.

## A note on Michigan format authority

Form of pleadings and motions in Michigan is governed statewide by:

- **MCR 1.109** — document format (paper size, margins, legibility),
  signature requirement (MCR 1.109(E)), and protected-personal-
  identifying-information rules (MCR 1.109(D))
- **MCR 2.113** — form of pleadings, including the caption
  (MCR 2.113(C)), paragraph and count structure, and adoption by
  reference
- **MCR 2.107** — manner and proof of service

Page limits and chambers-copy practice are largely set by **local
administrative orders** of the filing circuit/district court. This
skill checks the statewide MCR components and **flags page-limit and
local-practice items as WARN — confirm with the venue.**

## Pass 1 — Format

For a generated filing, run `scripts/format-check.py` first:

```
python3 plugins/mi-court-docs/scripts/format-check.py path/to/filing.docx
```

The format-check script validates the marketplace common-practice
defaults (US Letter, conventional margins, 12-point body, double or
1.5x spacing, footer with **document title + "Page X of Y"**
pagination) against the MCR 1.109 / MCR 2.113 baseline. Where a value
is a local-administrative-order matter, the script emits **WARN**
(not FAIL) — resolve those by checking the venue's local rules.

Resolve any **FAIL** from the format check before continuing.

### Format pass — non-`.docx` (markdown / text drafts)

Verify manually:

- **Caption (MCR 2.113(C))** — court and county
  (e.g., "STATE OF MICHIGAN / IN THE CIRCUIT COURT FOR THE COUNTY OF
  WAYNE"), party names with designations, **case number** and assigned
  judge, and the document title
- **Title** — identifying the document (e.g., "MOTION FOR SUMMARY
  DISPOSITION")
- **Numbered paragraphs (MCR 2.113(C)(2))** — sequential, each
  averment limited to a single set of circumstances; separate counts
  where required
- **Signature block (MCR 1.109(E))** — name, address, telephone,
  email, and **P-number (State Bar of Michigan attorney number)** if
  an attorney, or the **"In Pro Per" / "Self-Represented"**
  designation if not; the MCR 1.109(E) signature certifies the filing
- **Proof of Service (MCR 2.107)** — date, manner of service, and
  each recipient
- **Line numbering + footer present** with **"Page X of Y"** (WARN —
  line numbering is a marketplace convention, not an MCR requirement;
  confirm the venue does not prohibit it)
- **Protected personal identifying information** restricted/redacted
  per **MCR 1.109(D)** (full SSNs, financial-account numbers, minors'
  identifying data) — use the separate protected-data form where the
  rule requires it

## Pass 2 — Content

The content check applies the pro-se drafting framework. Citation
resolution is delegated to **mi-fact-check**; this pass confirms the
component is structurally complete.

### For a motion / brief:

- [ ] **Relief stated clearly** in the opening paragraph
- [ ] **Rule or statute citation** that grants the relief (e.g.,
      MCR 2.116(C) summary disposition; MCR 2.119 motion practice;
      MCL § ___)
- [ ] **Numbered factual paragraphs** with record cites (affidavit ¶,
      complaint ¶, exhibit, admission)
- [ ] **Application of controlling authority** — case law applied to
      the facts, not merely strung together (citations verified by
      `mi-fact-check`)
- [ ] **Counter-arguments addressed**
- [ ] **Specific conclusion** — what exactly should the court do?
- [ ] **Proposed order attached / referenced** per the MCR 2.602
      seven-day rule practice
- [ ] **Notice of Hearing** prepared and timely served under
      MCR 2.119(C) (motion and supporting brief served at least 9 days
      before hearing if served by mail, 7 days if served other than by
      mail — verify the current rule)

### For an affidavit:

- [ ] **Personal-knowledge foundation** in the opening paragraph
- [ ] **Numbered factual paragraphs** — facts only, no argument
- [ ] **Exhibit references** match the attached exhibits
- [ ] **Jurat** — sworn before a notary (a verified statement or
      declaration is permitted only where the rule or statute allows
      one — verify)
- [ ] **Date and place** of execution
- [ ] For a **business-records** affidavit, the custodian /
      qualified-witness foundation under MRE 803(6)

### For a proposed order:

- [ ] **Caption identical** to the underlying motion (MCR 2.113(C))
- [ ] **Findings (if any) separate from the ordering clause**
- [ ] **Ordering clause mirrors** the motion's prayer for relief
- [ ] **Specific dates / amounts** filled in or bracketed for the
      judge
- [ ] **Judge signature line** at the foot; entry consistent with the
      MCR 2.602(B) procedure (see `mi-submit-order`)

### For an answer:

- [ ] **Each allegation of the complaint addressed** (admit / deny /
      lack of knowledge — no skipping) per MCR 2.111(C)/(D)
- [ ] **Affirmative defenses separately stated** under
      **MCR 2.111(F)** (statute of limitations, payment, lack of
      standing, etc.) — defenses not stated may be waived
- [ ] **Compulsory counterclaims** stated (MCR 2.203)
- [ ] **Timeliness** — answer due **21 days** after personal service
      (28 days if served by mail or outside Michigan) under
      MCR 2.108(A) — verify against the proof of service

## Pass 3 — Packet consistency

If filing a packet (motion + affidavit + proposed order + proof of
service):

- [ ] **Same caption** across all documents — court (Circuit /
      District), county, party names, case number, assigned judge
- [ ] **Same document title** referenced in the proof of service and
      the proposed order
- [ ] **Dates align** — proof-of-service date matches the signature
      date on the motion; affidavit jurat date is consistent
- [ ] **Relief sought matches** between motion prayer and proposed
      order ordering clause (item by item)
- [ ] **All referenced exhibits** attached

## Pre-flight checklist

| Check | Done |
|-------|------|
| `scripts/format-check.py` run; no FAIL (WARN items confirmed against local rules) | ☐ |
| Caption shows correct court, county, party names, case number, judge (MCR 2.113(C)) | ☐ |
| Numbered paragraphs sequential (MCR 2.113(C)(2)) | ☐ |
| Signature block has P-number (attorney) or "In Pro Per" designation (MCR 1.109(E)) | ☐ |
| Proof of Service shows manner, date, recipients (MCR 2.107) | ☐ |
| Protected personal identifying information restricted/redacted (MCR 1.109(D)) | ☐ |
| Footer carries document title + "Page X of Y" | ☐ |
| Affirmative defenses separately stated (MCR 2.111(F)) | ☐ |
| Proposed Order drafted as a separate document | ☐ |
| Notice of Hearing prepared; MCR 2.119(C) service window met | ☐ |
| Local-rule page limit / chambers-copy practice confirmed for the venue | ☐ |
| `mi-fact-check` deep audit run (if high-stakes filing) | ☐ |

## Common Michigan pre-filing failures

1. **Missing P-number or in-pro-per designation** in the MCR 1.109(E)
   signature block.
2. **Affirmative defenses not separately stated** — MCR 2.111(F)
   requires defenses be set forth; omitted defenses can be waived.
3. **Motion served too late.** MCR 2.119(C) sets the service window
   ahead of the hearing; a short notice gets the hearing adjourned.
4. **Protected personal identifying information left in the body**
   rather than restricted per MCR 1.109(D).
5. **Caption missing the case number or assigned judge** required by
   MCR 2.113(C).
6. **Affidavit not actually sworn** — an un-notarized "affidavit"
   carries no evidentiary weight unless a verified/declared form is
   permitted.

## Composition

- For the deep evidentiary-citation and sworn-vs-argued review:
  `mi-fact-check`
- For format generation and the MCR 1.109 / 2.113 / 2.107 baseline:
  `mi-statewide-format`
- For drafting each component: `mi-draft-motion`,
  `mi-draft-declaration`, `mi-draft-order`, `mi-draft-note`
- For deadline arithmetic (MCR 1.108 computation; MCR 2.108
  response windows): `mi-deadlines`
- For court-specific local-rule overlay: `mi-wayne`, `mi-oakland`,
  `mi-circuit-courts`, `mi-district-courts`, `mi-36th-district`
- For the final filing step: `mi-file-packet`

## References

- `mi-statewide-format` for the MCR 1.109 / MCR 2.113 / MCR 2.107
  baseline and the local-administrative-order page-limit caveat
- `mi-law-references` for canonical MCR and MRE text
- Always confirm the current local administrative orders of the
  filing court — this skill checks statewide components and flags
  local-practice items as WARN.
