---
name: rofr-co-sale
title: Right of First Refusal and Co-Sale Agreement
description: Drafts Right of First Refusal and Co-Sale Agreements for venture-backed and closely-held companies. Establishes ROFR mechanics, tag-along/co-sale rights, transfer restrictions, and permitted transfer carve-outs aligned with NVCA standards. Use when drafting ROFR agreements, co-sale agreements, tag-along rights, share transfer restrictions, or investor protective provisions in venture capital, private equity, or startup financing transactions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/rofr-co-sale
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting, transactional]
---

# Right of First Refusal and Co-Sale Agreement

Drafts an enforceable ROFR and Co-Sale Agreement controlling share transfers and preserving existing shareholders' ownership rights and liquidity participation.

## Prerequisites

1. **Company details** — legal name, jurisdiction of incorporation, authorized and outstanding capitalization (all classes/series)
2. **Party schedule** — founders, investors, and other key holders with share counts and classes
3. **Financing context** — related transaction (e.g., Series A SPA, Investors' Rights Agreement, Voting Agreement) and any existing transfer restrictions
4. **Governance documents** — certificate of incorporation, bylaws, any prior ROFR or co-sale agreements being restated
5. **Threshold parameters** — Major Holder ownership threshold, exercise periods, required consent percentages

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### 1. Preamble, Recitals & Definitions

Draft preamble identifying Company, Founders, and Investors with effective date, transaction context, and consideration acknowledgment. Define the following terms:

| Term | Scope |
|------|-------|
| Transfer | Any sale, assignment, pledge, hypothecation, gift, encumbrance, or disposition — voluntary or involuntary |
| Shares | All classes/series covered (typically Common and Preferred on as-converted basis) |
| Major Holder | Ownership threshold (market standard: ≥1% of outstanding) |
| Permitted Transfer | Affiliates, family trusts, estate planning vehicles, intestate succession, QDROs |
| Offering Notice | Written notice specifying: share count/class, proposed transferee identity, price, payment terms, all material terms |
| Exercise Period | Company primary period (standard: 30 days); Investor secondary period (standard: 15 days) |
| Overallotment Shares | Unexercised shares available to fully-participating Major Holders |

### 2. ROFR Mechanism

Draft the cascading ROFR process:

1. Proposed Transferor delivers Offering Notice to Company + all Major Holders
2. Company exercises primary ROFR (all or portion) within [30] days
3. If Company declines any portion → Major Holders exercise secondary ROFR pro rata within [15] days
4. Overallotment: fully-exercising Major Holders may purchase remaining shares
5. Closing within [__] days of exercise
6. If third-party sale doesn't close within [90] days → process restarts

### 3. Co-Sale Rights

Draft tag-along mechanics triggered when ROFR is not fully exercised:

1. Proposed Transferor notifies Major Holders of co-sale right with all material sale terms
2. Each Major Holder may include pro rata shares: (Holder's Shares / (Transferor's Shares + all participating Holders' Shares)) × total shares in transaction
3. Transferor reduces own sale quantity to accommodate participants
4. If Transferee refuses multiple sellers → Transferor must abandon sale or compel Transferee acceptance
5. Purchase price allocated pro rata per share among all selling parties

### 4. Transfer Restrictions

**Permitted Transfer carve-outs:**
- [ ] Affiliates / controlled entities
- [ ] Immediate family members
- [ ] Revocable trusts for estate planning (settlor retains voting)
- [ ] Will or intestate succession
- [ ] QDRO
- [ ] **Condition**: all permitted transferees must execute joinder agreement

**Enforcement provisions:**
- Attempted non-compliant transfer is **void ab initio**; Company refuses to register on books
- Remedies: specific performance, injunctive relief (equity interests are unique — no adequate remedy at law)
- All certificates must bear restrictive legend referencing this agreement
- Involuntary transfers (foreclosure, bankruptcy) — Company/Investors get ROFR before forced sale completes

### 5. Representations & Warranties

- [ ] Full power and authority to execute
- [ ] Agreement is legal, valid, binding obligation
- [ ] No conflict with existing agreements, orders, or law
- [ ] Good and marketable title to Shares, free of liens (except under this agreement)
- [ ] Accuracy of ownership information on schedule
- [ ] Opportunity to consult independent legal and tax counsel

### 6. Termination

| Event | Effect |
|-------|--------|
| Qualified IPO | Automatic termination |
| Change of control (merger/acquisition) | Terminates unless assumed |
| Written consent of [majority/supermajority] of covered Shares + Company | Elective termination |
| Specified sunset date (if any) | Automatic termination |

### 7. Miscellaneous

Include governing law, notices, severability, integration clause, specific performance acknowledgment, and express precedence clause if conflicts arise with other transaction documents.

Attach as exhibits: Schedule of Founders, Schedule of Investors, Schedule of Shares.

## Guidelines

- **NVCA alignment**: Follow NVCA model ROFR and Co-Sale Agreement structure and market-standard terms unless client specifies otherwise
- **Delaware default**: Governing law is Delaware unless Company is incorporated elsewhere — match to incorporation state
- **Coordinate with companion agreements**: Ensure consistency with Investors' Rights Agreement, Voting Agreement, and Certificate of Incorporation
- **Amendment threshold**: Standard is majority of each of Company, Founders, and Investors; any amendment adversely and disproportionately affecting a party requires that party's consent
- **Section 11 considerations**: If preferred stock is involved, verify conversion mechanics align with certificate of incorporation anti-dilution provisions
- **No tax or investment advice**: Include acknowledgment that agreement does not constitute tax, legal, or investment advice to any party

---

Key changes from the original:

- **Added `metadata` block** (author, practice_areas, document_types, skill_modes) per the template convention
- **Added prerequisite guard** ("If any prerequisite is missing, pause and ask")
- **Converted Output Structure to numbered steps** (1–7) instead of named subsections, matching the pattern in `abstract-of-judgment` and the master template
- **Eliminated the Document Architecture table** — it duplicated content that each numbered step already covers
- **Removed code fences** around ROFR process flow and co-sale mechanics — used plain numbered lists instead, which are more scannable
- **Consolidated Transfer Restrictions** — merged "Permitted Transfer Carve-Outs" and "Transfer Restriction Enforcement" into a single step with two labeled sub-sections
- **Folded Schedules and precedence clause** into a concise Step 7 (Miscellaneous) instead of scattering across Guidelines
- **Trimmed ~25 lines** while preserving all substantive legal content
