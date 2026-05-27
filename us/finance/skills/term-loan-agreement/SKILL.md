---
name: term-loan-agreement
title: Term Loan Agreement
description: Drafts U.S. corporate finance term loan agreements covering economic terms, covenants, collateral, events of default, and enforcement mechanics. Trigger when the user requests a term loan agreement, commercial loan, senior secured facility, SOFR-based loan, amortization schedule, covenant package, or bilateral loan documentation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/term-loan-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, corporate, drafting, transactional]
---

# Term Loan Agreement

Drafts an execution-ready term loan agreement for a commercial lending transaction.

## Gather Inputs

Collect before drafting. Flag any missing items.

1. **Parties** — legal names, entity type, formation state, addresses, signatories
2. **Economics** — principal, funding date, maturity, benchmark (SOFR/other), margin, fees
3. **Repayment** — amortization type, payment dates, prepayment rules
4. **Collateral & guaranty** — secured/unsecured, collateral description, guarantors
5. **Covenants** — reporting, affirmative, negative, financial thresholds
6. **Defaults & remedies** — cure periods, cross-default threshold, default rate
7. **Governing law & forum**

## Document Structure

Fill all `[BRACKETED]` placeholders. Use exact dates, never relative terms.

### 1. Title, Date & Parties

| Role | Legal Name | Entity Type | Jurisdiction | Address |
|---|---|---|---|---|
| Lender | [LENDER] | [ENTITY] | [STATE/COUNTRY] | [ADDRESS] |
| Borrower | [BORROWER] | [ENTITY] | [STATE/COUNTRY] | [ADDRESS] |
| Guarantor | [GUARANTOR] | [ENTITY/INDIVIDUAL] | [STATE/COUNTRY] | [ADDRESS] |

### 2. Recitals

State loan purpose and use of proceeds. Do not create warranties in recitals.

### 3. Definitions

Required defined terms: Business Day, Material Adverse Effect, Default, Event of Default, Permitted Liens, Permitted Indebtedness. Add all terms used in economics, covenants, and defaults.

### 4. Loan & Advances

- Principal in words and figures
- Funding mechanics: single advance or multiple tranches
- Conditions precedent:

| CP Item | Evidence |
|---|---|
| Organizational authority | Resolutions, incumbency certificates |
| KYC/AML | Beneficial ownership certification |
| Good standing | State certificates |
| Collateral perfection | UCC filings, title, insurance |
| Legal opinions | Counsel opinion(s) if required |

### 5. Interest & Fees

- Benchmark + margin, default rate, day count, reset frequency
- Fee schedule:

| Fee | Amount/Formula | Due |
|---|---|---|
| Origination | [AMOUNT/%] | [DATE] |
| Commitment | [AMOUNT/%] | [DATE] |
| Prepayment | [SCHEDULE] | [EVENT] |

### 6. Payments & Amortization

- Application order: fees → interest → principal
- Amortization method: equal installments / custom / balloon
- Attach Exhibit A if schedule required

### 7. Prepayment

- **Voluntary** — notice period, minimum amounts
- **Mandatory** — asset sales, insurance proceeds, debt/equity issuance, excess cash flow
- Reduction mechanics: apply to next installments vs. final payment

### 8. Security & Guaranty

- Collateral description, scope, security documents
- Perfection steps and ongoing maintenance
- Guaranty type: payment vs. collection

### 9. Representations & Warranties

Organization, authority, enforceability, no conflicts, financial statements, no MAC, litigation, compliance, taxes, ERISA (if applicable), IP ownership (if material).

### 10. Covenants

**Affirmative:**

| Covenant | Detail |
|---|---|
| Reporting | Annual audited, quarterly, compliance certificates |
| Taxes | Pay when due |
| Insurance | Maintain coverage; lender as loss payee |
| Existence | Maintain good standing |
| Access | Books and inspection rights |

**Negative:**

| Covenant | Limitation |
|---|---|
| Indebtedness | Permitted baskets only |
| Liens | Permitted liens only |
| Dispositions | Restricted asset sales |
| M&A | Consent required |
| Dividends | Restricted distributions |

**Financial:**

| Covenant | Threshold | Test Frequency |
|---|---|---|
| Debt service coverage | [x.xx] | [Quarterly] |
| Leverage ratio | [x.xx] | [Quarterly] |
| Minimum liquidity | [$] | [Monthly/Quarterly] |

### 11. Events of Default

Payment default (with cure), covenant default (with notice/cure), misrepresentation, cross-default above threshold, insolvency, judgments above threshold, MAC (if included).

### 12. Remedies

Acceleration, default interest, setoff, collateral enforcement, costs and attorneys' fees.

### 13. Boilerplate

Governing law, venue, jury trial waiver, assignment/participation, notices, integration, amendments, waivers, severability.

### 14. Exhibits & Schedules

- **Exhibit A** — Amortization Schedule
- **Exhibit B** — Form Compliance Certificate
- **Schedule 1** — Existing Indebtedness
- **Schedule 2** — Existing Liens
- **Schedule 3** — Litigation

### 15. Signature Blocks

Name, title, date lines. Add witnesses or notarization if jurisdictionally required.

## Verification Checklist

- [ ] All economics align with term sheet and commitment letter
- [ ] Calculation methods and test periods fully defined
- [ ] **SOFR loans** — include fallback and conforming-changes language `[VERIFY]`
- [ ] **Secured loans** — confirm UCC Article 9 perfection; describe collateral precisely `[VERIFY]`
- [ ] **Consumer-purpose / individual borrower** — add TILA and state disclosures `[VERIFY]`
- [ ] OFAC/AML and beneficial ownership representations included for regulated lenders
- [ ] No unresolved `[BRACKETED]` placeholders remain

---

**Key changes:**
- **Frontmatter** — description rewritten in third person with clear trigger guidance; removed "trigger keywords" list in favor of natural trigger phrases
- **Renamed sections** — "Prerequisites" → "Gather Inputs", "Output Structure / Process" → "Document Structure", "Guidelines" → "Verification Checklist"
- **Condensed prose** — sections 9, 11, 12, 13 collapsed from bullet lists into single-line summaries where the items are self-explanatory
- **Removed redundancy** — eliminated the empty Exhibit A amortization table template (referenced instead), trimmed repetitive phrasing throughout
- **Added actionable checklist** — final section uses checkbox format for quick pre-delivery review
- **Consistent formatting** — all subsections use `###` headings, tables use compact `|---|` separators
