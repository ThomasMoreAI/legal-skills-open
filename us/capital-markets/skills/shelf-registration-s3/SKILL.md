---
name: shelf-registration-s3
title: Shelf Registration Statement (Form S-3)
description: Drafts SEC Form S-3 shelf registration statements for eligible U.S. public companies under the Securities Act of 1933. Verifies issuer eligibility (public float, investment grade, WKSI), structures all disclosure sections, and assembles exhibits for delayed or continuous offerings. Use when drafting Form S-3, shelf registration, securities registration, capital markets filings, or continuous offering documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/shelf-registration-s3
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
tags: [corporate, drafting, regulatory, analysis]
---

# Shelf Registration Statement (Form S-3)

Drafts a Form S-3 shelf registration enabling eligible public companies to register securities for delayed or continuous offerings over a three-year period.

## Prerequisites

1. **Corporate documents** — charter, bylaws, board resolutions authorizing filing
2. **Recent SEC filings** — latest 10-K, subsequent 10-Qs, 8-Ks, prior registration statements
3. **Capital structure** — outstanding shares by class, debt instruments, credit agreements, warrant/option schedules
4. **Public float calculation** — aggregate market value of voting and non-voting common equity held by non-affiliates (within 60 days of filing)
5. **SEC identifiers** — CIK code, file number, reporting history
6. **Offering parameters** — security types, maximum aggregate offering amount, capital raising objectives

## Eligibility Verification

Confirm one pathway before drafting:

| Pathway | Requirements |
|---|---|
| **I.B.1 — Public Float** | US/Canadian org + Section 12(b)/12(g) registered + 12 months reporting + reports current + public float ≥ $75M |
| **I.B.2 — Investment Grade** | Same reporting requirements + non-convertible securities rated investment grade |
| **WKSI** | All I.B.1 + either (a) worldwide public float ≥ $700M or (b) ≥ $1B non-convertible securities issued in registered offerings in prior 3 years |

WKSI: automatic effectiveness upon filing under Rule 462(e).

## Output Structure

### 1. Cover Page

- [ ] Registrant legal name, jurisdiction of incorporation, IRS EIN
- [ ] Principal executive offices address and telephone
- [ ] Agent for service of process with contact details
- [ ] Each security class with precise title (e.g., "Common Stock, par value $0.01 per share")
- [ ] Maximum aggregate offering price (specific or "to be determined from time to time")
- [ ] Fee calculation per Rule 457(o) using current SEC rate
- [ ] Eligibility checkbox referencing applicable General Instruction
- [ ] WKSI checkbox if applicable
- [ ] Incorporation by reference list with titles, dates, file numbers

### 2. Prospectus Summary

1. **Business description** — from 10-K Business section: operations, markets, differentiation
2. **Shelf mechanism** — security types covered, aggregate amount, supplement-based takedowns
3. **Use of proceeds overview** — general capital allocation framework
4. **Key financials** — revenue, net income/loss, total assets, stockholders' equity, trends
5. **Risk factors roadmap** — preview of major categories

### 3. Risk Factors (Item 503(c) Reg S-K)

Organize by category, descending materiality within each:

| Category | Coverage |
|---|---|
| Business/Industry | Competition, concentration, technology obsolescence, key personnel |
| Financial | Cash flow, covenant compliance, interest rate/FX exposure, loss history |
| Legal/Regulatory | Pending litigation, regulatory changes, compliance costs |
| Securities | Market volatility, limited volume, analyst coverage |
| Shelf-Specific | Dilution, timing/pricing uncertainty, management discretion, subordination |

Format each: heading → circumstances → consequences → mitigating factors. Tailor to registrant facts — no generic boilerplate. [VERIFY: SEC routinely comments on generic risk factors]

### 4. Use of Proceeds

- General uses: working capital, capex, R&D, acquisitions, debt repayment, general corporate
- Identified projects with estimated cost ranges and timelines where available
- Debt repayment: identify obligations (principal, rate, maturity, prepayment terms)
- Allocation priority or management discretion statement
- Pending-use policy: short-term, investment-grade instruments
- Specific allocation deferred to prospectus supplements

### 5. Description of Securities

Draft framework descriptions per registered class:

**Common Stock** — voting rights, dividend rights/restrictions, liquidation priority, conversion/preemptive/anti-dilution features; incorporate by reference Section 12 description

**Preferred Stock** — board authority to issue series and fix terms; framework for dividends, liquidation preferences, voting, conversion, redemption, sinking fund; specific terms per supplement

**Debt Securities** — base indenture framework; term-setting: principal, maturity, rate, payment dates, ranking, redemption, covenants, events of default, modification; trustee identification; senior/subordinated, secured/unsecured, convertible/non-convertible per offering

**Warrants / Purchase Contracts / Units** — exercise terms framework, anti-dilution adjustments; specifics per warrant agreements filed with supplements

### 6. Incorporation by Reference

- [ ] Most recent Form 10-K (Sections 13(a) or 15(d))
- [ ] All subsequent Form 10-Qs
- [ ] All subsequent Form 8-Ks (exclude Items 2.02 and 7.01 furnished information)
- [ ] Section 12 registration statement description of common stock

Include forward-incorporation language: future filings under Sections 13(a), 13(c), 14, or 15(d) automatically incorporated from filing date. Later statements supersede earlier ones.

Provide copy-request instructions: investor relations contact, EDGAR URL, company website with non-incorporation disclaimer.

### 7. Undertakings (Item 512 Reg S-K)

Include verbatim regulatory language:

| Item | Substance |
|---|---|
| 512(a)(1) | Post-effective amendments for 10(a)(3) compliance, fundamental changes, material distribution plan changes |
| 512(a)(2) | Each amendment deemed new registration; offering deemed initial bona fide offering |
| 512(a)(3) | Removal of unsold securities at termination |
| 512(a)(5) | (WKSI only) Rule 424(b) prospectus filing and incorporation |
| 512(a)(6) | SEC indemnification policy — indemnification against Securities Act liability unenforceable |
| 512(h) | Respond to incorporation-by-reference requests within one business day |

### 8. Signature Page

- [ ] Registrant signature by authorized officer
- [ ] Principal executive officer, financial officer, controller/accounting officer
- [ ] Majority of board of directors
- [ ] Power of attorney if used — file as Exhibit 24

WKSI automatic shelf: signature date = filing date (effective immediately).

### 9. Exhibits Index (Item 601 Reg S-K)

| Exhibit | Description | Status |
|---|---|---|
| 1 | Underwriting agreement | Filed or to be filed via 8-K per takedown |
| 3.1 | Certificate of incorporation | Filed or incorporated by reference |
| 3.2 | Bylaws | Filed or incorporated by reference |
| 4.x | Security holder rights instruments | Filed herewith or by amendment |
| 5 | Opinion of counsel — legality | Filed herewith |
| 23.1 | Auditor consent | Filed herewith |
| 23.x | Other expert consents | As applicable |
| 24 | Powers of attorney | If applicable |
| 25 | Form T-1 — trustee eligibility | If debt securities |
| 107 | Filing fee table | Filed herewith |

For each: indicate filed herewith, incorporated by reference (cite file number, type, date, exhibit), or to be filed by amendment.

## Checks

- Cross-check all financial data against incorporated filings; verify internal cross-references
- Forward-looking statements must include PSLRA safe harbor language
- EDGAR compliance: HTML tagging, file formats, size limits per Filer Manual
- [VERIFY: current SEC fee rate at filing date]; show computation clearly
- Every risk factor must tie to registrant-specific facts
- Use of proceeds must align with MD&A priorities in incorporated filings
- Verify all exhibit hyperlinks resolve correctly
- Structure aggregate amount and security types for full three-year shelf life
- Base prospectus establishes frameworks only — do not over-specify terms belonging in supplements

---

**Key changes from the original:**

- **Frontmatter**: Dropped `research` tag (not a primary mode), tightened description with trigger keywords
- **Description of Securities**: Collapsed from verbose sub-sections with bullet lists into dense single-paragraph-per-class format — same content, ~40% fewer tokens
- **Signature Page**: Merged officer roles into one checklist item instead of four separate lines
- **Exhibits Index**: Shortened descriptions (e.g., "Auditor consent" vs "Consent of independent registered public accounting firm")
- **Guidelines → Checks**: Renamed to match codebase convention; added `[VERIFY]` markers for attorney-review checkpoints
- **Overall**: Reduced from 175 lines to ~135 lines while preserving all legally substantive content, eligibility thresholds, regulatory citations, and checklist items
