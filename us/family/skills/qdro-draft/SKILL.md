---
name: qdro-draft
title: QDRO Drafting
description: Drafts Qualified Domestic Relations Orders (QDROs) compliant with ERISA §206(d)(3) and IRC §414(p) to divide retirement benefits in divorce. Covers defined benefit pensions, 401(k)s, and defined contribution plans with plan-specific division formulas and alternate payee protections. Use when drafting QDROs, dividing retirement assets post-judgment, or preparing domestic relations orders for plan administrator review.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/qdro-draft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# QDRO Drafting

Produces a court-ready QDRO dividing retirement benefits between participant and alternate payee pursuant to a divorce decree, compliant with ERISA and the specific plan's requirements.

## Prerequisites

Gather before drafting:

- **Divorce decree / MSA** — case number, filing date, retirement benefit provisions
- **Plan documents** — exact IRS-registered plan name, plan number, type (DB/DC/401(k)), administrator contact, any model QDRO language
- **Party info** — full legal names, DOBs, SSNs, current addresses (both parties)
- **Key dates** — marriage, separation, agreed valuation date
- **Division terms** — percentage or dollar amount, method (shared payment vs. separate interest for DB), treatment of earnings/losses between valuation and segregation

## Quick Start

1. Confirm plan type (DB vs. DC) — structures differ fundamentally
2. Obtain plan administrator's model QDRO language if available
3. Draft using the output structure below, matching local court caption rules
4. Submit to plan administrator for pre-approval review before filing

## Output Structure

### 1. Court Caption & Recitals

- Match caption to local court rules of divorce jurisdiction
- Reference divorce decree by exact date and case number
- State order is intended to qualify under ERISA §206(d)(3) and IRC §414(p)
- Include three mandatory ERISA findings:

| Finding | Authority |
|---|---|
| Does not require increased benefits | §206(d)(3)(D)(i) |
| Does not require benefit type/form not provided by plan | §206(d)(3)(D)(ii) |
| Does not require benefits already assigned to another alternate payee | §206(d)(3)(D)(iii) |

### 2. Definitions

Define at minimum: Participant, Alternate Payee, Plan (full legal name + number), Plan Administrator (entity + address), Valuation Date, Accrued Benefit or Account Balance (per plan type).

For DB plans, also define: Marital Coverture Fraction (months married during participation ÷ total participation months), Benefit Commencement Date.

### 3. Division Methodology

**Defined Contribution (401(k), 403(b)):**
- Exact percentage or dollar amount as of valuation date
- Gains/losses from valuation through segregation
- Whether alternate payee directs investments post-segregation

**Defined Benefit (Pension):**
- Method: **shared payment** (% of each payment) or **separate interest** (independent benefit, alternate payee commences separately)
- Coverture fraction formula if dividing marital portion only
- Disposition of early retirement subsidies, COLAs, ancillary benefits
- Form of benefit — must not exceed plan options (no lump sum if plan pays annuity only)

### 4. Alternate Payee Protections

Include provisions for:
- Right to designate own beneficiaries
- Right to receive plan information from administrator
- Pre-retirement survivor benefit rights (specify % if applicable)
- Protection from participant loans/hardship withdrawals against segregated share
- Immediate vesting upon qualification regardless of participant's schedule
- Protection from plan amendments reducing awarded benefits

### 5. Plan Administrator Directives

1. Segregate alternate payee's share as of valuation date
2. Establish separate account (DC) or calculate separate benefit (DB)
3. Grant alternate payee distribution options and investment direction
4. Process distributions per plan terms — QDRO distributions are rollover-eligible and exempt from 10% early withdrawal penalty (IRC §72(t)(2)(C))
5. Provide written notice to both parties upon qualification with segregated balance/benefit amount

### 6. Compliance & Effective Date

- Certify compliance with ERISA §206(d)(3), IRC §414(p), and applicable state law
- Repeat the three mandatory ERISA findings
- Effective date: court signature or plan administrator qualification, whichever is later
- ERISA does **not** permit termination of QDRO rights based on remarriage, regardless of state law

### 7. Signature Block

- Judge signature line (printed name, title, date)
- Court certification of ERISA/IRC compliance
- Check local rules for seal or clerk certification requirements

## Pitfalls

- **Use model language** — deviations from plan administrator's model QDRO are the #1 cause of rejection
- **Never require unavailable benefits** — e.g., lump sum from annuity-only plan
- **Federal plans are not QDROs** — military uses USFSPA court orders; FERS/CSRS uses court orders acceptable for processing; TSP uses retirement benefits court orders per 5 CFR §1653
- **SSN handling** — do not include SSNs in the order body if jurisdiction requires filing under seal or on a confidential information sheet
- **Tax treatment** — alternate payee reports distributions as own income (IRC §402(e)(1)(A)); participant is not taxed on amounts paid under QDRO
- **Flag gaps explicitly** — never assume or omit missing information; incomplete QDROs are routinely rejected

## Key Authorities

- ERISA §206(d)(3)(B) — QDRO definition
- IRC §414(p) — tax code parallel
- 29 CFR §2530.206 — DOL regulations

---

**Key changes made:**
- Removed `tags` from frontmatter (not part of the spec's required fields)
- Added **Quick Start** section for immediate orientation
- Converted the checkbox block to a plain bullet list (more portable)
- Consolidated the Definitions section into prose + conditional additions instead of a full table
- Merged "Compliance Certifications & Effective Date" and "Signature Block" into tighter sections
- Collapsed "Guidelines" into a focused **Pitfalls** section
- Extracted statutory references into a compact **Key Authorities** footer
- Reduced from 109 lines to ~95 while preserving all substantive legal content
