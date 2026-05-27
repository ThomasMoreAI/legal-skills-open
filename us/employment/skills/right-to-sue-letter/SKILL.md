---
name: right-to-sue-letter
title: Notice of Right to Sue Letter
description: Drafts EEOC Notice of Right to Sue letters that close the administrative process and authorize employment discrimination litigation. Ensures compliance with Title VII, ADA, ADEA, GINA, and EPA filing requirements. Use when drafting right-to-sue notices, EEOC closure letters, or administrative exhaustion documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/right-to-sue-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
tags: [drafting, letter, litigation]
---

# Notice of Right to Sue Letter

Drafts the EEOC notice closing the administrative charge and triggering the 90-day window to file an employment discrimination lawsuit in federal or state court.

## Prerequisites

Gather before drafting:

- **Charge file** — charge number, charging party name/address, respondent employer
- **Closure basis** — no cause, insufficient evidence, administrative closure, party request (post-180 days), or failed conciliation
- **Statutory bases** — Title VII, ADA, ADEA, EPA, and/or GINA
- **Issuing office** — address, phone, TTY, authorized signatory name/title

## Quick Start

1. Collect prerequisites above
2. Select closure reason (use verbatim language from Closure Reasons below)
3. Draft letter following Document Layout order
4. Include 90-day deadline paragraph verbatim
5. List all applicable statutes from the original charge
6. Review against Pitfalls checklist

## Document Layout

Draft sections in this order:

| Section | Content |
|---|---|
| Header | EEOC letterhead: agency name, seal, office address, phone, TTY |
| Date | Mailing date, upper-right (90-day clock starts on **receipt**) |
| Reference block | Charge number (bold), party name, mailing address |
| Salutation | "To the Person Aggrieved" |
| Title | **NOTICE OF RIGHT TO SUE** — capitalized, bold |
| Charge ID | Charge number and respondent employer |
| Closure rationale | Verbatim language from Closure Reasons table |
| Merits disclaimer | EEOC determination is not a merits judgment; courts review de novo |
| 90-day deadline | Bold/underlined paragraph (see template below) |
| Applicable statutes | All statutes authorizing suit (see Statute Reference) |
| Legal advisories | Right to counsel, bar referral, pro bono resources |
| EEOC litigation role | Commission intervention status |
| State deferral note | If applicable: notice satisfies state/local prerequisites |
| Signature block | Name, title, "On behalf of the Commission" |
| Enclosures | Original charge copy; position statements if disclosable |

## Closure Reasons

Use the applicable language **verbatim**:

| Reason | Language |
|---|---|
| No cause | "The EEOC has determined that no reasonable cause exists to believe that a violation of the statutes occurred." |
| Insufficient evidence | "The evidence obtained during investigation was insufficient to establish a violation." |
| Administrative closure | "The EEOC has administratively closed the charge and elected to issue this notice." |
| Party request | "Issued at the charging party's written request after the requisite 180-day waiting period." |
| Failed conciliation | "Conciliation efforts did not achieve a voluntary resolution between the parties." |

## 90-Day Deadline Paragraph

Include verbatim:

```
IMPORTANT: Any lawsuit based on this charge MUST be filed in an appropriate
United States District Court or state court of competent jurisdiction WITHIN
90 DAYS of your receipt of this notice. This deadline is strictly enforced.
Failure to file within this period will result in permanent dismissal of
any lawsuit based on this charge, regardless of the merits.
```

## Statute Reference

Include all that apply from the original charge:

| Statute | Protected basis |
|---|---|
| Title VII, Civil Rights Act of 1964 | Race, color, religion, sex, national origin |
| Americans with Disabilities Act (ADA) | Disability |
| Age Discrimination in Employment Act (ADEA) | Age (40+) |
| Equal Pay Act (EPA) | Sex-based wage discrimination |
| Genetic Information Nondiscrimination Act (GINA) | Genetic information |

## Pitfalls

- **90-day clock runs from receipt, not mailing** — state this explicitly; include specific deadline date if receipt date is known
- **De novo review** — always note courts are not bound by EEOC findings, especially after no-cause determinations
- **Neutral tone** — never prejudge merits, discourage filing, or imply EEOC determination is binding
- **All statutes** — list every statute from the original charge to preserve full litigation scope
- **State deferral** — if charge involved state/local FEPA deferral, note this notice satisfies those prerequisites
- **No-cause cases** — clarify the party retains full right to present their case independently
- **Certified mail** — format for certified mail with return receipt; include tracking number in case file

---

**Key changes from the original:**

- **Description** shortened from 3 sentences to 2 while retaining all trigger keywords
- **Added Quick Start** section for the fast-path workflow
- **Flattened structure** — removed the nested `### Output Structure` / `### Document Layout` hierarchy; each reference table is now a top-level `##` section
- **Renamed "Guidelines" to "Pitfalls"** — aligns with the best-practices pattern and signals these are gotchas to check, not general advice
- **Removed the `### Applicable Statute Reference Table` sub-header verbosity** — now just "Statute Reference"
- **Cut redundant prose** — e.g., "Drafts the EEOC notice that closes the administrative process..." was tightened, and the Prerequisites section uses a compact dash-list instead of numbered bold sentences
- **~86 lines → ~95 lines** but with better scanability and a Quick Start that the original lacked
