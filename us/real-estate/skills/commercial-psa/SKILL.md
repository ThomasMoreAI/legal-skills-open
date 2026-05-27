---
name: commercial-psa
title: Purchase and Sale Agreement — Commercial Real Estate
description: Drafts Purchase and Sale Agreements for commercial real estate transactions (office, retail, industrial, multifamily). Triggers when the user needs a commercial PSA, purchase agreement, sale contract, or acquisition agreement. Extracts deal terms from uploaded documents and structures all major provisions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/commercial-psa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [agreement, drafting, transactional]
---

# Purchase and Sale Agreement — Commercial Real Estate

Drafts a litigation-ready PSA for commercial property transfers, ensuring enforceability under applicable state law.

## Quick Start

1. Collect prerequisites (see below). Do NOT draft if deal terms are insufficient — request missing info first.
2. Extract data points from uploaded documents.
3. Draft the PSA following the output structure.
4. Run the final checks.

## Prerequisites

1. **Parties** — exact legal names, entity types, states of formation, addresses
2. **Property** — legal description, address, tax parcel ID, improvements
3. **Deal terms** — purchase price, earnest money, closing timeline, financing
4. **Title commitment** and existing survey (if available)
5. **Lease schedule** — rent roll, all leases/amendments (income-producing properties)
6. **Environmental** — Phase I ESA or known conditions
7. **Service contracts** — management, maintenance, vendor agreements
8. **Client role** — buyer or seller; risk tolerance and priorities

## Document Extraction

Before drafting, extract from uploaded materials:

| Data Point | Source |
|---|---|
| Party names & entity structure | Org docs, term sheet |
| Legal description & address | Deed, title commitment, survey |
| Purchase price & earnest money | Term sheet, LOI |
| Closing timeline & financing | LOI, lender correspondence |
| Lease terms & rent roll | Lease files |
| Environmental conditions | Phase I/II reports |
| Special conditions | Correspondence, LOI |

## Output Structure

### 1. Header & Parties

- Title: "PURCHASE AND SALE AGREEMENT"
- Effective date: date of last signature unless specified otherwise
- Full party ID: legal name, entity type, state of formation, principal + notice address
- Identify parent/guarantor relationships for SPEs or multi-tiered entities

### 2. Property Description & Purchase Price

**Property description:** street address, common name, legal description (Exhibit A), county/state, tax parcel ID, acreage/SF, improvement summary, appurtenant rights, personal property schedule (Exhibit B — conveys as-is without warranty).

**Price structure:**

| Component | Details |
|---|---|
| Total price | Numerical + written form |
| Allocation | Real vs. personal property (must withstand IRS scrutiny) |
| Earnest money | 1–5% typical; wire within 3–5 business days to escrow |
| Additional deposits | Amount, trigger, refundability |
| Cash at closing | Price minus deposits minus financing |
| Financing | Loan amount, type (conventional/SBA/CMBS/mezzanine) |

All closing payments by wire of immediately available federal funds.

### 3. Title Review & Survey

**Title:** Seller delivers commitment within 10–15 days of effective date with all Schedule B exception docs. Buyer review: 10–15 days. Distinguish mandatory cure defects (monetary liens, marketable fee simple issues) from voluntary (easements, CCRs). Seller response: 10–15 days. Buyer election: 5–10 days to accept or terminate. Mandatory cure survives closing.

**Survey:** ALTA/NSPS with Table A items (improvements, zoning/setbacks, parking, utilities, flood zone). Certified to Buyer, lender, title company. Buyer review: 10–15 days. Seller cures encroachments, boundary disputes, zoning violations.

### 4. Due Diligence

**Period:** 30 days (single-tenant) to 60–90 days (complex/multi-tenant/environmental). Time is of the essence.

**Access:** 24–48 hours' notice, business hours. Coordinate tenant access through Seller/PM.

**Scope:** Physical (building systems, structure, utilities) | Environmental (Phase I per ASTM E1527 [VERIFY current edition]; Phase II if RECs) | Financial — income properties (leases, rent rolls, operating statements, capex) | Regulatory (zoning, ADA, COs, permits).

**Buyer obligations:** CGL insurance ≥ $1M/$2M aggregate naming Seller as additional insured; no interference with operations; repair damage; bear all costs.

**Seller cooperation:** Provide all property documents; may require confidentiality; may redact tenant confidential business info (not lease terms).

**Termination:** Buyer may terminate for any/no reason by 5:00 PM (property TZ) on last DD day. On termination: earnest money refunded in 3–5 business days; Buyer delivers third-party reports (retains work product). If NOT terminated: earnest money becomes non-refundable (except Seller default or express contingency failure).

### 5. Representations & Warranties

**Seller reps** (true as of effective date and closing): authority/organization | good and marketable fee simple title | no pending/threatened litigation or condemnation | environmental compliance (knowledge-qualified) | zoning/code compliance (knowledge-qualified) | leases: rent roll accurate, no defaults, deposits held per law | financial statements accurate | all contracts/options disclosed.

**Knowledge qualifier:** "To Seller's actual knowledge without independent investigation" for environmental and compliance reps.

**Buyer reps:** Authority/capacity | as-is acknowledgment based on own investigation (does NOT limit remedies for breach of express reps or fraud).

**Survival & caps:** 12–18 months | de minimis threshold $10K–$25K | aggregate cap 5–10% of price | fraud: unlimited, no caps.

### 6. Closing

**Date:** Date certain or formula (e.g., 30 days post-DD). Time is of the essence; 15–30 day extension for title cure.

**Seller delivers:** Special warranty deed | bill of sale (Exhibit B, as-is) | FIRPTA certificate (15% withholding if foreign [VERIFY rate under IRC §1445]) | owner's affidavit | assignment of leases (with Buyer assumption) | tenant estoppels | assignment of contracts/warranties | keys/codes | updated certified rent roll | licenses/permits/COs | settlement statement | entity authority docs | transfer tax declarations.

**Buyer delivers:** Purchase price (wire, net of deposits/financing ± prorations) | entity authority docs | assumption agreements | lender-required docs.

### 7. Prorations & Adjustments

Prorate as of 11:59 PM day before closing:

- **Taxes** — most recent bill; true-up within 30 days of actual bill
- **Rent** (income properties) — collected (not accrued); post-closing collections: current first, then delinquent
- **Security deposits** — transfer or credit; Buyer assumes return obligations
- **Operating expenses** — utilities, insurance, CAM, management fees (prepaid/accrued)
- **TI/leasing commissions** — Seller responsible for pre-closing lease obligations; holdback if incomplete
- **Special assessments** — allocate per agreement

Post-closing adjustment period: 90–120 days.

### 8. Default & Remedies

**Seller default — Buyer elects:** (a) Terminate: full earnest money refund + reasonable OOP expenses (cap $25K–$50K); OR (b) Specific performance (may record lis pendens).

**Buyer default — Seller's sole remedy:** Terminate and retain earnest money as liquidated damages. Include enforceability language (reasonable pre-estimate, not a penalty). Escrow agent: notice, cure period, interpleader if disputed.

**General:** Written notice + 5–10 business day cure. No cure period for failure to close, repudiation, or fraud. Prevailing party fees optional (advise client it cuts both ways).

### 9. General Provisions

- **Notices:** Personal delivery, overnight courier, email (with confirmation), certified mail RRR. Deemed delivered: same day / next business day / 3 business days (certified)
- **Assignment:** Affiliate assignment without consent if assignor remains liable; unaffiliated requires consent (not unreasonably withheld); §1031 exchange cooperation permitted
- **Governing law:** Property state, no conflicts-of-law principles
- **Disputes:** Mandatory mediation first (30–60 days); exclusive jurisdiction in property county
- **Jury waiver:** Mutual, knowing, voluntary (separately initialed if required)
- **Standard:** Integration, written amendments only, severability, counterparts, e-signatures

## Exhibits

- **A** — Legal description
- **B** — Personal property schedule
- **C** — Form of deed (optional)
- **D** — Form of bill of sale (optional)
- **E** — Assignment and assumption of leases (income properties)
- **F** — Tenant estoppel certificate (income properties)

## Final Checks

- **Jurisdiction:** Verify state-specific transfer tax rates, mandatory disclosures (lead-based paint if pre-1978 residential component), recording requirements
- **Property type adjustments:** Office (parking, TI) | Retail (exclusive use, percentage rent) | Industrial (environmental, zoning) | Multifamily (rent control, deposit regs)
- **FIRPTA:** 15% withholding for foreign sellers [VERIFY current rate under IRC §1445]
- **§1031 exchange:** Include cooperation clause; cooperating party bears no additional cost/liability
- **Entity verification:** Confirm legal names against secretary of state records
- **Timeline validation:** Calculate all deadlines effective date through closing; flag conflicts
- **Cross-references:** Verify exhibit references, defined terms, section cross-references, dollar amounts
- Mark uncertain statutory citations with [VERIFY]
