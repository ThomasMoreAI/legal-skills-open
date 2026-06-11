---
name: private-placement-memo
title: Private Placement Memorandum (PPM)
description: Drafts a legally compliant Private Placement Memorandum for Regulation D offerings (Rule 506(b)/506(c)), covering full disclosure framework including risk factors, capitalization, securities terms, use of proceeds, and investor qualification requirements. Enforces SEC anti-fraud compliance under Section 10(b)/Rule 10b-5, blue sky law considerations, and accredited investor verification under Rule 501. Use this skill when drafting PPMs, offering memorandums, Reg D disclosure documents, or private offering circulars for issuers raising capital from sophisticated investors. Also trigger when the user mentions private placement disclosure, offering memorandum, Reg D fundraising, or accredited investor verification. Even if the user just says "PPM" or "draft our offering memo," use this skill.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/private-placement-memo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
tags: [corporate, drafting, memo, regulatory, transactional]
---

# Private Placement Memorandum (PPM)

## Why This Skill Exists

A PPM simultaneously serves as disclosure document, liability shield, marketing tool, and compliance record. Deficient disclosure creates rescission rights under Section 12 of the Securities Act and exposes issuers to Rule 10b-5 liability. The challenge is balancing full and fair disclosure of risks with a compelling presentation of the opportunity — every statement must satisfy anti-fraud standards while providing the information a reasonable investor would consider material.

This skill produces a PPM that protects the issuer while meeting Regulation D requirements for the selected exemption.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Offering terms** — security type, total amount, price/valuation, min/max amounts, minimum investment, Rule 506(b) vs. 506(c) election
2. **Corporate documents** — articles of incorporation, cap table, stockholder agreements, option/warrant schedules, prior financing docs
3. **Financial statements** — balance sheet, income statement, cash flow; note audited/reviewed/compiled status
4. **Management bios** — names, titles, education, professional history for officers, directors, and key advisors
5. **Business materials** — pitch deck, business plan, material contracts, IP portfolio, customer/supplier agreements
6. **Transaction documents** — subscription agreement, investor questionnaire, escrow arrangements

**If the user doesn't respond**, apply and clearly label these defaults: Rule 506(b) offering; no general solicitation; equity security; single closing; accredited investors only.

---

## Step 1: Draft Cover Page and Executive Summary

**Cover page** must include three mandatory legends:

1. **Confidentiality** — proprietary info, no reproduction/distribution, return/destroy obligation
2. **Securities law** — not registered under Securities Act of 1933 or state laws; no SEC/state review or approval; criminal offense to represent otherwise
3. **Transfer restrictions** — significant resale limitations; no public market expected; acquire for investment only; prepare to hold indefinitely

**Executive summary** includes: offering terms table, company overview, 3–5 principal risk factors, and intended use of proceeds summary.

---

## Step 2: Draft Risk Factors

Organize by category. Each risk gets a **titled subsection** with description, materiality explanation, and potential consequences.

| Category | Required Topics |
|---|---|
| **Financial** | Operating losses/burn rate, additional capital needs, dilution, debt obligations, limited resources |
| **Business/Operational** | Competition, market acceptance, technology/product development, regulatory compliance, key personnel, IP risks, customer concentration, supply chain, scaling |
| **Investment-Specific** | No public market/illiquidity, transfer restrictions, speculative nature, voting limitations, management discretion over proceeds, subordination, no dividends |

Materiality standard: any fact a reasonable investor would consider important. Disclose both positive developments and risks.

---

## Step 3: Draft Use of Proceeds and Business Description

**Use of proceeds**: Gross proceeds → expenses → net proceeds; specific allocations with strategic rationale; min/max scenarios.

**Business description**: History, products/services, market analysis, competitive landscape, sales/marketing, operations, regulatory environment, IP portfolio.

---

## Step 4: Draft Management, Capitalization, and Securities Terms

**Management & Board**: Bios in reverse-chronological format; board composition and independence; advisory board.

**Capitalization**: Pre-offering and post-offering cap tables (min and max scenarios); fully diluted ownership; option/warrant/convertible schedules.

**Securities terms** — address each applicable term at term-sheet precision:

| Term | Key Elements |
|---|---|
| Dividends | Rate, cumulative vs. non-cumulative, participation |
| Liquidation preference | Amount, participating vs. non-participating, deemed liquidation events |
| Conversion | Ratio/price, adjustments, optional vs. mandatory vs. auto-convert triggers |
| Voting | Votes per share, as-converted basis, protective provisions (enumerate veto rights) |
| Redemption | Company vs. investor rights, triggers, pricing, subordination to debt |
| Transfer restrictions | Lock-ups, ROFR, co-sale/tag-along, drag-along, permitted transfers |
| Registration rights | Demand, piggyback, S-3, expense allocation, cutback provisions |
| Anti-dilution | Weighted average vs. full ratchet; preemptive rights and exceptions |
| Information rights | Financial statement frequency, budget access, inspection rights |
| Board rights | Designation rights, observer rights, committee assignments |

---

## Step 5: Draft Plan of Distribution and Investor Qualifications

**Plan of distribution**: Offering mechanics, timeline, subscription procedures, escrow, accredited investor verification method.

**Subscription procedure** must include:
1. Review PPM and all exhibits
2. Execute subscription agreement
3. Complete investor questionnaire (KYC/AML)
4. Provide accredited investor verification per Rule 501 [VERIFY current thresholds]
5. Submit payment with wire/check instructions
6. Await acceptance (company reserves right to reject)

**Investor qualifications**: Accredited investor definitions per Rule 501 (include professional certification category from 2020 amendments [VERIFY]); suitability requirements; verification procedures — tailor to 506(b) self-certification vs. 506(c) reasonable verification steps.

**Legal matters**: Counsel identification, auditor identification, forward-looking statement disclaimers.

---

## Step 6: Produce Final Document

Assemble all sections into a single integrated PPM:

| # | Section |
|---|---|
| 1 | Cover Page (with three legends) |
| 2 | Executive Summary |
| 3 | Risk Factors |
| 4 | Use of Proceeds |
| 5 | Business Description |
| 6 | Management & Board |
| 7 | Capitalization |
| 8 | Securities Terms |
| 9 | Plan of Distribution |
| 10 | Legal Matters |
| 11 | Investor Qualifications |

### Mandatory Front Matter

Include **Assumptions and Open Items** listing every `[COMPANY TO PROVIDE]` and `[VERIFY]` item with what needs confirmation, where to confirm it, and who is responsible.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial PPM, ask:

1. Are all offering terms accurately reflected across sections (cap table, use of proceeds, executive summary)?
2. Are there additional risk factors specific to the company's industry or stage?
3. Should local Blue Sky counsel be engaged for any specific states?
4. Are financial statements audited, reviewed, or compiled — and does the PPM reflect the correct status?

---

## Quality Audit

Before finalizing, verify:

- All figures (cap table, use of proceeds, offering terms) internally consistent across sections
- Risk factors cover all three categories with company-specific risks included
- Securities terms match the actual term sheet or charter provisions
- 506(b): no general solicitation language appears anywhere in the document
- 506(c): reasonable verification steps documented for accredited investors
- Financial statements correctly labeled as audited/reviewed/compiled
- Forward-looking statements marked with cautionary language
- All three cover page legends present and complete
- Form D filing obligation noted (15 days after first sale [VERIFY])
- Every information gap flagged with `[COMPANY TO PROVIDE: specific item]`
- Assumptions and open items listed prominently
- No unsubstantiated claims in business description

---

## Guidelines

- **Anti-fraud compliance**: Every statement must satisfy Section 10(b) / Rule 10b-5 — no material misstatements or omissions
- **506(b) vs. 506(c)**: If 506(b), ensure no general solicitation language appears. If 506(c), document reasonable verification steps for accredited investors
- **State blue sky**: Flag state filing requirements; Rule 506 preempts state registration but not notice filing or fee requirements
- **Financial statements**: Clearly label audit status. If unaudited, add prominent disclaimer
- **Information gaps**: Flag with `[COMPANY TO PROVIDE: specific item needed]` and explain the disclosure obligation
- **No promotional overreach**: Business description may be compelling but never unsubstantiated; maintain factual, balanced tone
- **Date sensitivity**: PPM is accurate only as of its date; flag obligation to supplement if material changes occur during offering period
- **Consistency check**: Cross-reference all figures across sections — a plaintiff will exploit any inconsistency
- **Anti-hallucination**: Do not fabricate SEC guidance, CDI references, or Rule 501 thresholds. Mark unverified items with `[VERIFY]`
- **Attorney review required**: All output is draft guidance requiring review by licensed counsel before use, distribution to investors, or reliance for filings
