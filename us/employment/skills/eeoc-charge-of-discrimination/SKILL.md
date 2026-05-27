---
name: eeoc-charge-of-discrimination
title: EEOC Charge of Discrimination
description: Drafts an EEOC Charge of Discrimination (Form 5) for federal administrative complaints under Title VII, ADEA, ADA, GINA, and EPA. Verifies jurisdiction and timeliness, builds a prima facie narrative from uploaded documents, and structures relief. Use when drafting employment discrimination, harassment, retaliation, failure-to-accommodate, or hostile work environment charges requiring EEOC filing before federal litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/eeoc-charge-of-discrimination
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# EEOC Charge of Discrimination

Drafts a jurisdictionally sufficient EEOC charge that satisfies administrative exhaustion and preserves the right to sue.

## Prerequisites

Collect before drafting:

1. **Complainant** — name, address, phone, email, job title, hire/termination dates
2. **Respondent** — legal entity name, address, employee count, HR/legal contact
3. **Timeline docs** — adverse action notices, performance reviews, disciplinary records, communications
4. **Protected class basis** — race, sex, age, disability, etc. with supporting facts
5. **Comparators/witnesses** — names, titles, treatment differentials
6. **Filing deadline** — date of last discriminatory act

## Quick Start

1. Run jurisdiction and timeliness check
2. Complete complainant and respondent sections
3. Identify statutory basis and adverse actions with exact dates
4. Draft chronological factual narrative
5. Specify relief requested with applicable damage caps
6. Add verification block per 29 C.F.R. § 1601.12

## Core Workflow

### 1. Jurisdiction & Timeliness

| Factor | Rule |
|--------|------|
| Title VII / ADA / GINA | ≥ 15 employees (payroll method, 20+ calendar weeks) |
| ADEA | ≥ 20 employees; complainant ≥ 40 at time of adverse action |
| Filing — non-deferral state | 180 days from discriminatory act |
| Filing — deferral state | 300 days (FEPA worksharing agreement) |
| Continuing violation | Use final incident date for hostile environment claims |

Flag whether dual-filing with state FEPA is appropriate to preserve state claims and extend the deadline to 300 days.

### 2. Complainant Section

- Full legal name, address, phone, email
- Employment status (current / former / applicant), job title, department, supervisor, hire and separation dates
- Protected class membership — stated as fact, not legal conclusion
- Prior EEOC/FEPA charge number if applicable

### 3. Respondent Section

- Legal entity name (not trade name/DBA), principal address, phone
- HR director or registered agent, employee count, coverage statute(s)
- FEIN if available; parent/subsidiary or joint employer relationships if relevant

### 4. Basis of Discrimination

| Statute | Basis |
|---------|-------|
| Title VII | Race, color, religion, sex (including pregnancy, sexual orientation, gender identity), national origin |
| Title VII | Sexual harassment — quid pro quo or hostile environment |
| ADEA | Age (≥ 40) |
| ADA | Actual disability, record of impairment, or regarded-as; treatment, accommodation, or harassment |
| GINA | Genetic information |
| EPA | Sex-based wage discrimination |
| Retaliation | Prior charge, opposition, or participation in investigation |

### 5. Adverse Actions

List each discrete act with exact date: termination, demotion, failure to promote, denial of transfer/training/benefits, retaliatory action, harassing conduct (date of each significant incident).

### 6. Factual Narrative

Structure chronologically:

1. **Background** — hire date, role, performance baseline
2. **Protected class/activity** — how and when respondent knew
3. **Discriminatory conduct** — specific acts, direct quotes, dates, actor names
4. **Comparators** — name, title, protected class, preferential treatment
5. **Employer knowledge** — complaints made, to whom, date, outcome
6. **Adverse action** — decision-maker, stated reason, pretext evidence
7. **Harm** — economic losses, emotional distress, dates

**Claim-specific elements:**
- **Harassment** — severity/pervasiveness, unwelcomeness, employer knowledge, failure to remediate
- **Accommodation** — request, interactive process (or failure), employer response, reasonableness
- **Retaliation** — protected activity → employer knowledge → adverse action with temporal proximity

### 7. Relief

- Back pay (with prejudgment interest), front pay, reinstatement
- Compensatory damages (out-of-pocket, emotional distress)
- Punitive damages — Civil Rights Act of 1991 caps:

| Employer size | Cap |
|---------------|-----|
| 15–100 | $50,000 |
| 101–200 | $100,000 |
| 201–500 | $200,000 |
| 500+ | $300,000 |

- Injunctive relief, attorney's fees, costs, and other relief the Commission deems proper

### 8. Verification

Per 29 C.F.R. § 1601.12:

> "I have read the above charge and it is true to the best of my knowledge, information, and belief."

Include signature block: charging party name, date, and (if represented) attorney name, bar number, firm, address, phone, email.

## Pitfalls & Checks

- **Preserve all bases** — omitted protected characteristics cannot be added post-charge without amendment
- **No legal conclusions** in the narrative — state facts only
- **Continuing violation** — expressly argue if any acts fall outside the filing window
- **Dual-file** with state FEPA where available
- **Witness safety** — use descriptive identifiers instead of names when safety is a concern
- **Government employers** — punitive damages unavailable under Title VII [VERIFY state equivalents]
- **ADEA remedies** — no compensatory/punitive damages; liquidated damages (double back pay) for willful violations [VERIFY]
- **File via Form 5 or EEOC Public Portal** — retain proof of filing

---

**Key changes from the original:**

- Removed `tags` from frontmatter (not in the Agent Skills spec)
- Tightened `description` to stay focused while preserving all trigger keywords
- Added **Quick Start** section for at-a-glance workflow
- Restructured body under a single **Core Workflow** heading with numbered subsections
- Collapsed the Title VII sex-basis rows into one line to reduce table sprawl
- Condensed the ADA note inline into the basis table
- Merged harassment/accommodation/retaliation narrative guidance into a compact **Claim-specific elements** block instead of three separate paragraphs
- Compressed the Relief section — removed redundant parentheticals while keeping damage caps table
- Renamed "Guidelines" to **Pitfalls & Checks** and tightened each item to one line
- Reduced from 134 lines to ~105 lines (~22% token savings) with no loss of legal substance
