---
name: prospectus-draft
title: SEC Prospectus Draft
description: Drafts SEC-compliant prospectuses for securities offerings, structuring company data, financials, risk factors, and offering terms into a regulatory disclosure document. Use when preparing prospectuses, S-1 registration statements, offering memoranda, or primary disclosure documents for public or private issuances.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/prospectus-draft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: securities
language: en
---

# SEC Prospectus Draft

Produces a securities offering prospectus satisfying SEC disclosure requirements. Balances factual disclosure with investor protection — never promotional tone.

## Quick Start

Gather before drafting:

1. **Corporate docs** — articles, bylaws, cap table
2. **Financials** — audited GAAP statements, interim results, projections
3. **Offering terms** — term sheet or preliminary parameters
4. **Management bios** — officers/directors, compensation, ownership %
5. **Risk inventory** — litigation, regulatory matters, operational vulnerabilities
6. **Business plan** — revenue model, competitive landscape, IP portfolio

## Prospectus Sections

Draft each section in order. Flag gaps with `[INFORMATION NEEDED: description]` and privilege-sensitive items with `[LEGAL REVIEW]`.

### 1. Cover Page

Include: full legal issuer name, securities type/amount/price, prospectus date, SEC disclaimer legend ("Neither the SEC nor any state securities commission has approved..."), and risk warning. Add red herring language per Rule 430 if preliminary [VERIFY].

### 2. Executive Summary

Company value proposition, offering type, high-level use of proceeds. Substantiate every claim with later disclosures. No promotional language — Section 10(b) applies.

### 3. Risk Factors

Order: (1) offering-specific → (2) company-specific → (3) industry → (4) market/economic.

- Every risk must be company-tailored, not generic boilerplate
- Describe potential impact with specificity
- Cross-reference SEC comment letter trends for the industry
- Follow Regulation S-K Item 105 [VERIFY]

### 4. Use of Proceeds

Tabulate categories (working capital, capex, debt repayment, R&D, acquisitions, general corporate) with amounts, percentages, and timelines. Disclose material assumptions and whether management retains reallocation discretion.

### 5. Business Description

Cover: company history, revenue model/unit economics, products and target markets, customer concentration, distribution channels, competitive positioning, IP portfolio, regulatory compliance, supply chain dependencies, seasonal factors. Reference Regulation S-K Items 101-103 [VERIFY].

### 6. Management & Governance

For each officer/director: name, title, age, 5-year professional background, education, board committee roles, independence status. Also disclose: compensation arrangements, major shareholders (>5%), related-party transactions, family relationships.

### 7. Financial Information

Required GAAP statements: balance sheet, income, cash flow, stockholders' equity, notes.

- [ ] Audited financials for required periods per Regulation S-X [VERIFY]
- [ ] Interim results with comparative periods
- [ ] Non-GAAP measures reconciled to GAAP with justification
- [ ] Forward-looking statements include PSLRA safe harbor language
- [ ] MD&A covering trends, liquidity, capital resources

### 8. Legal Proceedings

For each material proceeding: parties, nature of claims, forum, procedural status, management's liability assessment. Apply Regulation S-K Item 103 materiality threshold [VERIFY]. Balance transparency with privilege preservation.

### 9. Terms of the Offering

- [ ] Security type and pricing mechanism
- [ ] Underwriting arrangements and commissions
- [ ] Plan of distribution and closing conditions
- [ ] Dilution analysis (pre/post-offering ownership)
- [ ] Lock-up agreements — parties, duration, exceptions
- [ ] Registration rights and transfer restrictions

### 10. Signature Pages

Signatures from CEO, CFO, principal accounting officer, and majority of directors. SOX certifications (Sections 302, 906) if applicable [VERIFY]. Verify signing authority against bylaws and board resolutions.

## Drafting Rules

- **Materiality**: disclose anything a reasonable investor would consider important (TSC Industries v. Northway, 426 U.S. 438 (1976) [VERIFY])
- **Forward-looking statements**: must include meaningful cautionary language identifying specific risk factors
- **Cross-references**: link related sections for navigability; define key terms at first use
- **Jurisdiction**: default U.S. federal securities law (Securities Act of 1933, Exchange Act of 1934); flag state blue sky issues as needing separate analysis
- **EDGAR**: note formatting requirements if filing electronically
- **Privilege**: never include privileged analysis in prospectus text — use `[LEGAL REVIEW]` markers
- **Gaps**: use `[INFORMATION NEEDED: description]` — never fabricate details

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec; discovery relies on `description` keywords
- **Trimmed description** — tightened to essential trigger guidance, removed redundant phrases
- **Eliminated verbose tables** — cover page, management, and legal proceedings tables replaced with dense inline lists that convey the same requirements in fewer tokens
- **Removed ASCII template** — the use-of-proceeds table template was replaced with a one-line instruction
- **Consolidated guidelines into "Drafting Rules"** — compressed 9 bullet points of prose into 7 terse rules
- **Reduced from 175 → ~85 lines** — roughly 50% token savings while preserving all legal substance, section structure, `[VERIFY]` markers, and the `[LEGAL REVIEW]`/`[INFORMATION NEEDED]` conventions
