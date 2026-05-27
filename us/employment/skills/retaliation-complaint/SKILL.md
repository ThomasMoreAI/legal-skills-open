---
name: retaliation-complaint
title: Complaint for Retaliation
description: Drafts U.S. employment-retaliation complaints with jurisdiction, causation, and remedy sections aligned to the governing statute. Use when counsel needs a filing-ready complaint after a plaintiff alleges adverse action following protected activity. Covers Title VII, FLSA, SOX, and Dodd-Frank retaliation claims, administrative-exhaustion preservation, and prayer-for-relief drafting.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/retaliation-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Complaint for Retaliation

Generates a court-ready retaliation complaint with jurisdictional, factual, and remedy components for the selected statute.

## Quick Start

1. Identify the governing statute (Title VII, FLSA, SOX, Dodd-Frank, state law).
2. Collect: parties, employment dates, protected-activity dates, adverse-action dates, decision-makers.
3. Confirm administrative exhaustion (EEOC/FEPA charge number, right-to-sue letter).
4. Draft complaint using the architecture and checklists below.

## Prerequisites

Before drafting, gather:

- **Governing law**: federal title(s) and/or state anti-retaliation statute
- **Jurisdiction**: subject-matter and personal jurisdiction facts, venue basis
- **Exhaustion** (if required): charge number, filing date, right-to-sue date
- **Timeline**: employment start/end, protected-activity dates, adverse-action dates
- **Parties**: all plaintiffs/defendants, entity structure, employer capacity
- **Evidence placeholders**: emails, evaluations, memos, HR files, payroll records
- **Local rules**: caption format, font/margins, page limits, verification requirements
- **Relief strategy**: reinstatement, front pay, damages, injunction, fee-shifting, jury demand

## Statute Reference Matrix

| Claim | Statute | Elements | Typical Triggers |
|---|---|---|---|
| Title VII | 42 U.S.C. § 2000e-3(a) | Protected activity + adverse action + causation + knowledge | Discrimination complaint, investigation participation |
| FLSA | 29 U.S.C. § 215(a)(3) | Protected labor complaint + materially adverse action | Wage/hour/safety complaints |
| SOX | 18 U.S.C. § 1514A | Protected whistleblowing + retaliation by covered entity | Financial-fraud reporting |
| Dodd-Frank | [VERIFY] 15 U.S.C. § 78u-6 | Use exact statutory subsection | Securities/financial-market reporting |

## Complaint Architecture

Draft sections in this order:

1. **Caption and title block**
2. **Identity paragraph** — plaintiff/defendant descriptions
3. **Jurisdiction and venue** — see checklist below
4. **Party-capacity allegations** — entity structure, joint-employer facts
5. **Factual background** — numbered, chronological paragraphs
6. **Cause of action** — statutory basis + element-by-element pleading
7. **Prayer for relief and jury demand**
8. **Signature block + verification** (if required)

### Caption Template

```
IN THE [COURT NAME]
[COURT DIVISION/DISTRICT]

[PLAINTIFF NAME], individually [and on behalf of all others similarly situated],
  Plaintiff,
v.
[DEFENDANT LEGAL NAME], a [corporate form],
  Defendant.

Case No. [To Be Assigned]
COMPLAINT FOR RETALIATION
```

### Jurisdiction and Venue Checklist

| Topic | Allege | Cite |
|---|---|---|
| Subject matter | Federal question or diversity | 28 U.S.C. § 1331 / § 1332 |
| Venue | Defendant location, occurrence site | 28 U.S.C. § 1391 |
| Service/deadlines | Statute-specific limits | Local rules |
| Exhaustion | Charge filed + right-to-sue issued | EEOC/state agency records |

### Factual Allegations

- One key fact per numbered paragraph.
- Start with employment relationship and job context.
- For each **protected activity**: date, medium, recipients, subject.
- For each **adverse action**: date, actor, concrete impact.
- Include **causal hooks** for each adverse action:
  - Temporal proximity
  - Decision-maker knowledge
  - Shifting rationale / policy deviation
  - Disparate treatment vs. non-reporting comparators
  - Direct retaliatory statements

### Retaliation Elements Checklist

| Element | What to Plead |
|---|---|
| Protected activity | What, by whom, why protected under chosen statute |
| Employer knowledge | How/when management learned of it |
| Adverse action | Would dissuade a reasonable worker from protected activity |
| Causation | Temporal + evidentiary chain, pretext indicators |
| Damages | Monetary and non-monetary injury tied to the action |

### Prayer for Relief

```
1) Back pay and lost benefits from date of adverse action
2) Front pay where reinstatement is not feasible
3) Compensatory damages for emotional distress
4) Punitive damages (if malicious/reckless indifference supported)
5) Equitable relief (reinstatement, expungement, injunction)
6) Pre/post-judgment interest and attorney's fees per fee-shifting statute
7) Such other relief as the Court deems just
```

**Fee-shifting references**:
- Title VII: 42 U.S.C. § 2000e-5(k)
- FLSA: 29 U.S.C. § 216(b)
- Verify damage caps per statute before finalizing prayer.

### Verification and Signing

- Attorney signature block per local rule.
- Plaintiff verification under penalty of perjury if jurisdiction requires.
- Notary block only where court rules mandate.

## Pitfalls

- **Statutory precision**: replace all `[VERIFY]` placeholders with exact subsections before filing.
- **State of mind**: never plead without record support or explicit information-and-belief basis.
- **Timeline gaps**: do not omit known dates; courts scrutinize chronology for causation.
- **Over-bundled facts**: keep one fact per paragraph for clarity and citation ease.
- **Relief overreach**: include only theories supported by statute and available evidence.
- **Local-rule compliance**: confirm formatting, numbering, and any verification requirements.

---

**Key changes made:**

- **Frontmatter**: removed `tags` (not in spec), tightened `description` to third-person with clear trigger guidance, removed "trigger keywords" list in favor of natural keyword coverage
- **Added Quick Start**: 4-step entry point for the most common path
- **Flattened Prerequisites**: converted from nested numbered list to a scannable bullet list
- **Consolidated structure**: merged the 9-step "Output Structure / Process" into a single "Complaint Architecture" section with inline sub-sections, eliminating redundant numbering layers
- **Removed "Framework" row** from element checklist (was meta-guidance, not a pleading element)
- **Renamed "Guidelines" to "Pitfalls"**: reframed as failure-mode warnings per best practices
- **Reduced from 147 to ~115 lines** while preserving all legal substance: statute matrix, element checklist, caption template, prayer structure, fee-shifting cites, and verification rules
