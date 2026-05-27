---
name: record-designation
title: Record Designation on Appeal
description: Drafts a Record Designation on Appeal identifying trial court materials for transmission to the appellate court. Covers appellant designations and appellee counter-designations with transcript requests, exhibit lists, cost allocation, and compliance guidance. Use when filing a designation of record, counter-designation, transcript designation, or preparing the appellate record after a notice of appeal.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/record-designation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Record Designation on Appeal

Drafts a designation identifying all trial court materials to be transmitted to the appellate court, organized for completeness against each appellate issue.

## Prerequisites

1. **Notice of Appeal** — filed and served; appellate case number if assigned
2. **Trial court docket** — chronological docket with filing dates and entry numbers
3. **Case documents** — pleadings, motions, orders, jury instructions, verdict forms
4. **Trial exhibits** — exhibit numbers, descriptions, and admission status
5. **Hearing/trial dates** — dates, judges, subject matter, witness lists
6. **Appellate issues** — identified errors or rulings being challenged
7. **Applicable rules** — jurisdiction-specific deadlines and format requirements
8. **Party role** — appellant (initial designation) or appellee (counter-designation)

## Output Structure

### 1. Caption

| Element | Requirement |
|---|---|
| Court | Full appellate court name |
| Case numbers | Appellate case no. + trial court case no. |
| Parties | Full names with appellate designations (Appellant/Appellee or Petitioner/Respondent) |
| Title | "Designation of Record on Appeal" or jurisdiction-specific variant |

### 2. Organization

Choose based on case complexity:

- **Chronological** — simple cases; all items by filing/occurrence date
- **Categorical** — complex cases; group by type with chronological sub-ordering

### 3. Foundational Documents

- Notice of Appeal
- Final judgment or appealable order
- Post-judgment motions (JNOV, new trial, reconsideration)

> For each item: exact docket title, filing date, docket entry number.

### 4. Pleadings

- Complaint/petition (and amendments)
- Answers, responsive pleadings
- Counterclaims, cross-claims (if relevant to appellate issues)

### 5. Motions & Briefing

For each challenged ruling, designate the complete motion package:

| Component | Details |
|---|---|
| Motion | Title, filing date, docket no. |
| Supporting briefs | All opposition and reply briefs |
| Declarations/affidavits | Each declarant identified |
| Documentary evidence | Attached or filed in support |
| Hearing transcript | Date and subject |
| Written order | Granting/denying |

### 6. Transcripts

Format each designation:

```
Transcript of [Proceeding Type] held on [Date],
before Judge [Name], regarding [Subject Matter].
[If partial]: Limited to: (1) testimony of [Witness];
(2) sidebar conference at p. [X] regarding Exhibit [Y];
(3) [other specific portions].
```

Identify by: date, proceeding type, judge, subject matter, witnesses, exhibit discussions. Err toward completeness — omitted portions cannot be reviewed on appeal.

### 7. Exhibits

Format each entry:

```
[Party]'s Exhibit [No.]: [Description], dated [Date] — [Admitted/Excluded/Limited Purpose]
```

- Use trial numbering/lettering system
- Designate specific pages/sections for voluminous exhibits if only portions are relevant, but include full exhibit when context matters

### 8. Orders & Rulings

- Interlocutory orders on dispositive motions
- Discovery rulings affecting available evidence
- Evidentiary rulings (in limine, trial objections)
- Directed verdict / JMOL rulings
- Jury instructions — given AND refused
- Special verdict forms
- Post-trial motion orders

### 9. Counter-Designation Additions (Appellee Only)

When drafting a counter-designation, also include:

- Direct examination context for appellant's cross-exam excerpts
- Colloquy showing court's reasoning or party concessions
- Evidence supporting affirmance / substantial evidence for findings
- Record showing opponent's failure to preserve issues
- Statement re cost responsibility for additional materials

### 10. Closing Components

| Component | Requirement |
|---|---|
| Cost allocation | Appellant acknowledges preparation/transmission costs; appellee addresses costs for counter-designated additions |
| Certification | Accuracy and completeness after reasonable inquiry |
| Certificate of service | All parties, trial court clerk, court reporters per local rules |
| Signature block | Counsel name, bar number, firm, address, phone, email |

## Guidelines

- **Deadlines are often jurisdictional** — verify filing window (typically 10–30 days post-notice for appellant; shorter for counter-designation) [VERIFY for jurisdiction]
- **Cross-reference against appellate issues** — every challenged ruling must have its complete supporting record designated
- **Incomplete designation risk** — materials not designated may be permanently excluded from appellate review
- **Partial transcript caution** — if appellant designates less than full transcript, appellee may designate additional portions at appellant's cost
- **Format compliance** — check local rules for required organization, numbering, and filing method
- **When in doubt, include it** — over-designation costs money; under-designation loses issues
