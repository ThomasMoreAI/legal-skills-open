---
name: adoption-petition
title: Petition for Adoption
description: Drafts a Petition for Adoption for U.S. family law courts (stepparent, relative, agency, independent). Use when drafting adoption petitions, initiating adoption proceedings, or preparing pre-filing adoption pleadings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/adoption-petition
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
tags: [drafting, litigation, pleading]
---

# Petition for Adoption

Produces a court-ready Petition for Adoption satisfying statutory requirements and presenting a best-interests case for finalization.

## Quick Start

1. Classify adoption type (stepparent / relative / agency / independent) — this drives consent rules, waiting periods, and eligibility
2. Collect party information: full legal names, DOBs, addresses for petitioner(s), child, biological parents
3. Identify governing statute: state adoption code sections, local court rules, mandatory judicial council forms
4. Determine consent / TPR status: executed consents with dates, termination orders, or facts supporting statutory exceptions
5. Gather supporting documents: home study, background checks, birth certificate, marriage/divorce decrees, financial affidavits

## Document Structure

| Section | Content |
|---|---|
| Caption | Court name (county + judicial district), case number placeholder, "In the Matter of the Adoption of [Child's Full Legal Name]" |
| Introduction | Petitioner(s) by name; nature of petition; adoption type |
| Party Identification | Numbered paragraphs per party |
| Jurisdictional Allegations | Residency facts, statutory authority, personal jurisdiction |
| Relationship & Caregiving History | Placement date, circumstances, bond narrative |
| Eligibility & Fitness | Statutory criteria, background checks, home study, financial adequacy |
| Consent / TPR Status | Consent details, termination orders, or exception facts |
| Best Interests Analysis | Evidence-based argument per framework below |
| Prayer for Relief | Specific requests |
| Verification & Execution | Oath, signature blocks, notary acknowledgment |
| Exhibit List | Labeled attachments referenced in body |

## Core Workflow

### 1. Party Identification

**Each Petitioner:** Full legal name, DOB, address, marital status, relationship to child, duration of residency in jurisdiction.

**Child:** Current legal name, DOB, residence, duration in petitioners' care, proposed new name (if any — state both current and proposed).

**Biological Parents / Legal Guardians:** Full legal names, last known addresses, status of parental rights (intact / voluntarily relinquished / involuntarily terminated).

### 2. Jurisdictional Allegations

- Cite exact state adoption code sections for this adoption type
- Allege residency with specific dates meeting statutory minimum (typically 6–12 months; confirm for jurisdiction)
- Cite Uniform Adoption Act provisions if applicable
- Address personal jurisdiction over any party whose consent or TPR is at issue

### 3. Consent & Termination Framework

| Scenario | Required Allegations |
|---|---|
| Written consent obtained | Date, consenting party, manner of execution (witnessed / acknowledged before judicial officer), statutory sufficiency |
| Prior TPR order | Case number, issuing court, date, grounds |
| Consent exception claimed | Statutory provision + particularized facts (abandonment period, failure to support, unfitness) |
| TPR pending | Case number, court, status, anticipated timeline |
| Waiting period | Elapsed time since consent/TPR meets statutory minimum |

### 4. Best Interests Analysis

Address each factor with specific, concrete facts:

- Emotional/psychological benefits of permanency
- Stability of home environment
- Educational opportunities and progress
- Medical/developmental needs and petitioners' capacity to meet them
- Quality of attachment (reference professional observations if available)
- Sibling relationships and preservation plan
- Child's preference (if age-appropriate; typically 12+ but varies by state)
- Integration into extended family and community
- Home study conclusions and professional recommendations

### 5. Prayer for Relief

1. Grant petition; enter final decree establishing legal parent-child relationship
2. Order name change from [current name] to [proposed name] (if applicable)
3. Direct state registrar to issue new birth certificate reflecting adoptive parents
4. Seal adoption records per state law
5. Such other relief as the court deems just and proper

### 6. Verification & Execution Block

Include perjury declaration under state law, dated signature lines for each petitioner, and notary acknowledgment block with commission expiration and seal.

### 7. Exhibit List

Standard exhibits: (A) birth certificate, (B) marriage certificate, (C) divorce decree(s), (D) written consent(s), (E) TPR order(s), (F) home study report, (G) criminal background checks, (H) child abuse registry clearances, (I) financial affidavit, (J) medical/health assessments, (K) educational records. Add jurisdiction-specific exhibits as needed.

## Pitfalls & Checks

- **Adoption type controls procedure** — verify which consent, waiting period, and eligibility rules apply before drafting
- **Residency requirements vary** — confirm exact statutory minimum; do not assume 6 months
- **Consent execution defects are fatal** — verify witnessing/acknowledgment requirements precisely; a deficient consent can void proceedings
- **ICPC compliance** — if child crosses state lines, Interstate Compact on the Placement of Children must be satisfied before placement; flag if applicable
- **ICWA screening** — if the child is or may be eligible for membership in an Indian tribe, the Indian Child Welfare Act (25 U.S.C. §§ 1901–1963) imposes heightened notice, active efforts, and expert testimony requirements; screen early `[VERIFY current ICWA regulations]`
- **Bracketed placeholders** — use `[INSERT CASE NUMBER WHEN ASSIGNED]`, `[ATTACH EXHIBIT _]` for missing information
- **Never fabricate** consent dates, court order numbers, or statutory citations; use `[VERIFY]` for uncertain citations
- **Format per local rules** — margins, line numbering, font, pagination as required by jurisdiction
