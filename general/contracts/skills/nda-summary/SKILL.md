---
name: nda-summary
title: NDA Summary
description: Generates structured summaries of Non-Disclosure Agreements, extracting parties, confidential information scope, permitted disclosures, term/survival, breach remedies, and risk flags. Use when summarizing NDAs, reviewing confidentiality agreements, distilling NDA obligations, or onboarding stakeholders to NDA terms.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/nda-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# NDA Summary

Distills an NDA into a structured, scannable reference covering material terms, obligations, and risk areas.

## Prerequisites

- Complete NDA (executed or near-final draft)
- Any amendments or side letters modifying original terms

## Quick Start

1. Read the full NDA and any amendments
2. Extract terms into each section below, citing section numbers
3. Flag gaps, ambiguities, and non-market terms in Risk Flags
4. Mark silent topics as **[NOT ADDRESSED]** and uncertain citations as **[VERIFY]**

## Output Sections

### 1. Overview

Extract: parties (full legal names, Disclosing/Receiving/Mutual roles), effective date, purpose/context, agreement type (unilateral/mutual), governing law and venue.

### 2. Confidential Information

Extract:
- **Definition** — quote or paraphrase with scope
- **Categories** — listed categories from agreement
- **Exclusions** — publicly available, independently developed, prior knowledge, authorized disclosure
- **Standard of care** — same-as-own / reasonable care / heightened
- **Marking requirements** — written marking, oral designation follow-up

### 3. Disclosure Parameters

Extract:
- **Permitted recipients** — employees, contractors, advisors, affiliates; note need-to-know or binding requirements
- **Permitted uses** — evaluation, due diligence, project scope
- **Prohibited uses** — reverse engineering, competitive use, etc.
- **Compelled disclosure** — legal process / regulatory; note advance-notice and protective-order rights

### 4. Term and Survival

Extract: agreement duration, survival period post-termination, return/destruction requirements and certification obligations.

### 5. Breach Remedies

For each, note whether present (Y/N) and details:
- **Injunctive relief** — bond waiver?
- **Liquidated damages** — amount/formula
- **Indemnification** — scope, legal fees
- **Liability cap** — amount, exclusions (consequential, punitive)
- **Dispute resolution** — arbitration, mediation, forum

### 6. Additional Terms

Extract if present: non-solicitation/non-compete, IP ownership or licensing, representations re authority to disclose, assignment restrictions, third-party beneficiary provisions.

### 7. Risk Flags

- [ ] **Unusual terms** — deviations from market-standard NDAs
- [ ] **Onerous obligations** — asymmetric burdens, broad definitions, long survival
- [ ] **Ambiguities** — vague definitions, internal inconsistencies
- [ ] **Gaps** — missing standard of care, survival period, return/destruction, compelled-disclosure carve-out
- [ ] **Enforceability concerns** — overbroad scope, unreasonable duration

## Pitfalls

- **Silent topics**: Always flag missing standard of care, survival period, and return/destruction — these are the most commonly omitted
- **Quoting vs. paraphrasing**: Quote definitions and key obligations exactly; paraphrase elsewhere for brevity
- **No legal advice**: Flag issues for attorney review — do not opine on enforceability
- **Section citations**: Every extracted term must reference a section number or page
- **Length**: Target 1–3 pages depending on NDA complexity
