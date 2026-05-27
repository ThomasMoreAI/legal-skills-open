---
name: order-modification
title: Request for Order Modification
description: Drafts post-judgment motions to modify existing family law court orders based on material changes in circumstances. Structures changed-circumstances arguments with jurisdictional compliance, factual chronologies, and precise relief specifications. Use when drafting modification motions, changed-circumstances motions, post-judgment family law motions, or petitions to modify custody, support, or visitation orders.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/order-modification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Request for Order Modification

Drafts a post-judgment motion to modify an existing family law court order based on material changes in circumstances.

## Prerequisites

Collect before drafting:

1. **Original order** — full text, entry date, issuing judge, provisions at issue
2. **Changed-circumstances evidence** — financial, medical, employment, school, or incident records
3. **Baseline declarations** — prior financial disclosures and conditions at time of original order
4. **Jurisdiction** — state/county, applicable modification statute, local court rules
5. **Modification history** — any prior modification attempts and outcomes

## Quick Start

1. Identify modification type and governing legal standard
2. Verify statutory authority, burden of proof, and procedural prerequisites
3. Draft motion with structured changed-circumstances argument
4. Prepare supporting declaration and exhibits
5. Run review checklist before finalizing

## Workflow

### Step 1: Jurisdiction & Standard Research

Identify the governing standard by modification type:

| Type | Standard | Authority |
|---|---|---|
| Child support | Material change; income threshold | State family code; support guidelines |
| Spousal support | Changed circumstances; cohabitation; retirement | State family code; appellate law |
| Custody/visitation | Best interests + changed circumstances | State family code; custody factors |
| Property division | Fraud, mistake, newly discovered assets (rare) | State family code; FRCP 60(b) analogs |

Verify:
- [ ] Statutory authority for this modification type
- [ ] Burden of proof (moving party's burden)
- [ ] Threshold showing required before evidentiary hearing
- [ ] Meet-and-confer or ADR prerequisite
- [ ] Filing deadlines or waiting periods

### Step 2: Caption & Formatting

- [ ] Full court name with department/division
- [ ] Exact case number
- [ ] Party designations (Petitioner/Respondent)
- [ ] Document title per local rules ("Request for Order," "Motion to Modify," "Order to Show Cause")
- [ ] Local formatting rules (font, margins, spacing, page numbers)
- [ ] Required companion filings (proposed order, income/expense declaration, notice of motion)

### Step 3: Draft the Motion

Structure the motion as follows:

**1. INTRODUCTION** — Moving party identity, original order (title, date, judicial officer), provisions to modify (cite paragraph/section numbers), summary of relief, one-sentence changed-circumstances statement.

**2. PROCEDURAL HISTORY** — Timeline from original order through present motion. Note prior modifications or attempts and distinguish current facts. Address compliance history.

**3. STATEMENT OF FACTS** — Chronological narrative:
- Baseline conditions at time of original order
- Specific changes with dates, quantified data, concrete details
- Each fact tied to admissible evidence (cite exhibit)
- Address foreseeability — why changes were unanticipated
- Preempt counterarguments (temporary vs. enduring; foreseeable vs. new)

**4. LEGAL ARGUMENT** — Cite governing statute with quoted language. State elements the court must consider. Apply each element to specific facts. Cite controlling appellate authority [VERIFY all citations]. Distinguish unfavorable authority if applicable.

**5. REQUESTED RELIEF** — Specific modifications in adoptable order language:
- Dollar amounts, effective dates, payment mechanisms
- Detailed schedules (days, times, holidays, vacations)
- Step-down/termination provisions if applicable
- Alternative relief if primary request denied
- "Such other and further relief as the Court deems just and proper"

**6. CONCLUSION** — Restate each modification concisely. Prayer for relief.

### Step 4: Supporting Documents

**Moving Party Declaration:**
- First person, paragraph-per-fact structure
- Establish personal knowledge for each assertion
- Authenticate all referenced exhibits
- Quantified data and specific incidents — no conclusory statements

**Exhibit Organization:** Sequential lettering (A, B, C...). Each exhibit referenced by authenticating paragraph in the declaration.

| Exhibit | Description | Authenticating ¶ |
|---|---|---|
| A | Original order | Dec. ¶ __ |
| B | Financial records / pay stubs / tax returns | Dec. ¶ __ |
| C | Medical / school / incident records | Dec. ¶ __ |

**Procedural Filings:**
- [ ] Meet-and-confer declaration (if required)
- [ ] Income and expense declaration (if financial modification)
- [ ] Proof of service (documents, date, method, address, server identity)
- [ ] Proposed order in court-required format
- [ ] Cover sheets or fee waiver requests

### Step 5: Review Checklist

- [ ] Cross-references accurate (exhibit letters, paragraph numbers)
- [ ] Legal citations current and Bluebook-formatted [VERIFY each]
- [ ] Every factual assertion supported by cited evidence
- [ ] Proposed order language specific enough for direct adoption
- [ ] Signature block complete (attorney name, bar number, firm, address, phone, email)
- [ ] Word count/page limit compliance
- [ ] Service timeline meets statutory minimum notice period

## Pitfalls

- **Accuracy over advocacy** — every assertion must be verifiable from the record; credibility is dispositive in discretionary rulings
- **Quantify everything** — dollar amounts, dates, percentages, schedule times; never use vague language
- **Distinguish prior attempts** — if earlier modifications were denied, explicitly differentiate current facts
- **FRE 408** — do not reference settlement discussions or mediation offers unless an exception applies
- **Child-focused framing** — for custody/visitation, anchor every argument to the child's best interests, not parental preference
- **Local rule compliance** — rules vary significantly; always verify required forms, filing fees, and hearing procedures
- **Mark unverified citations** — use [VERIFY] for any citation not confirmed against source material

---

**Key changes from the original:**

- Removed `tags` from frontmatter (not part of the Agent Skills spec — only `name` and `description`)
- Added **Quick Start** section for immediate orientation
- Renamed "Process" phases to numbered **Steps** for clarity
- Collapsed the draft structure from a code block into inline bold headings — more scannable and ~30% fewer tokens
- Compressed the jurisdiction table by trimming redundant wording
- Consolidated the "Guidelines" section into a tighter **Pitfalls** section
- Trimmed repeated explanatory text throughout while preserving every substantive legal instruction
- Reduced from 137 lines to ~105 lines, well under the 500-line limit
