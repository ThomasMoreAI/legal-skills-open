---
name: real-estate-judicialmind
title: Real Estate
description: Real estate law skill for property transactions, leases, and land use. Use when the user needs assistance with real estate closings, lease agreements, title review, zoning, easements, or property disputes. Triggers on keywords like "real estate", "property", "lease", "landlord", "tenant", "title", "deed", "mortgage", "closing", "zoning", "easement", "commercial lease".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/real-estate
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
sources:
- title: Closing Checklist
  path: references/closing-checklist.md
- title: Lease Forms
  path: references/lease-forms.md
- title: Title Review
  path: references/title-review.md
---

# Real Estate

This skill provides expert guidance for real estate transactions, leasing, and property law matters.

## Core Capabilities

### 1. Transactions
- Purchase and sale agreements
- Title review and insurance
- Due diligence
- Closings

### 2. Commercial Leasing
- Lease negotiation
- Lease abstraction
- Tenant improvements
- Lease administration

### 3. Financing
- Mortgage documentation
- Loan agreements
- Security instruments

### 4. Land Use
- Zoning analysis
- Permitting
- Entitlements
- Environmental compliance

## Purchase and Sale Transactions

### Transaction Timeline
```
LOI → PSA Negotiation → Due Diligence → Title Review →
Financing → Survey → Closing → Post-Closing
```

### Purchase Agreement Key Terms

| Section | Key Issues |
|---------|------------|
| **Purchase Price** | Amount, earnest money, adjustments |
| **Due Diligence** | Period, scope, termination rights |
| **Title** | Commitment review, permitted exceptions |
| **Survey** | Requirements, objection process |
| **Representations** | Environmental, litigation, leases, compliance |
| **Conditions** | Financing, tenant estoppels, approvals |
| **Closing** | Date, location, deliverables |
| **Prorations** | Taxes, rents, operating expenses |
| **Default** | Remedies, liquidated damages, specific performance |

### Due Diligence Checklist

**Physical**
- [ ] Property condition assessment
- [ ] Environmental (Phase I, Phase II if needed)
- [ ] Building systems review
- [ ] ADA compliance assessment
- [ ] Deferred maintenance analysis
- [ ] Capital expenditure projections

**Financial**
- [ ] Rent roll verification
- [ ] Operating expense history (3 years)
- [ ] Utility bills
- [ ] Service contracts
- [ ] Insurance costs
- [ ] Tax assessment review
- [ ] CAM reconciliation history

**Legal**
- [ ] Title commitment review
- [ ] Survey review
- [ ] Lease abstracts
- [ ] Tenant estoppels
- [ ] SNDAs
- [ ] Existing loan documents
- [ ] Property management agreements
- [ ] Reciprocal easement agreements
- [ ] CC&Rs

**Governmental**
- [ ] Zoning verification
- [ ] Certificate of occupancy
- [ ] Building permits
- [ ] Compliance certificates
- [ ] Pending assessments
- [ ] Litigation/condemnation

## Title Review

### Standard Exceptions to Remove
1. Rights of parties in possession
2. Survey matters
3. Mechanic's liens
4. Taxes not yet due
5. Special assessments

### Common Title Issues
| Issue | Resolution |
|-------|------------|
| Mortgage liens | Pay off and record satisfaction |
| Judgment liens | Obtain release or pay |
| Tax liens | Pay and obtain certificate |
| Easements | Analyze impact, may be acceptable |
| Restrictive covenants | Review for conflicts with intended use |
| Gaps in chain | Obtain affidavits, quiet title |

### Title Insurance
**Owner's Policy**: Protects buyer's ownership interest
**Lender's Policy**: Protects mortgagee's security interest

**Common Endorsements**:
- Access
- Survey/location
- Zoning
- Contiguity
- Restrictions
- Tax parcel

## Commercial Lease Structure

### Lease Types by Expense Allocation

| Lease Type | Tenant Pays |
|------------|-------------|
| Gross | Base rent only |
| Modified Gross | Base rent + some expenses |
| Triple Net (NNN) | Base rent + taxes + insurance + CAM |
| Absolute Net | Everything including structural |

### Key Lease Provisions

**Business Terms**
```
- Premises description and measurement
- Lease term (commencement, expiration)
- Rent (base, escalations, percentage)
- Security deposit
- Permitted use
```

**Operating Provisions**
```
- Operating expense pass-throughs
- CAM calculation methodology
- Expense caps and exclusions
- Audit rights
- Gross-up provisions
```

**Construction/Improvements**
```
- Tenant improvement allowance
- Work letter
- Plans and specifications
- Change orders
- Substantial completion
```

**Tenant Rights**
```
- Renewal options
- Expansion rights
- Right of first offer/refusal
- Exclusivity
- Co-tenancy
- Relocation rights
- Termination rights
```

**Landlord Protections**
```
- Use restrictions
- Assignment/subletting controls
- Continuous operation
- Radius restrictions
- Recapture rights
- Financial reporting requirements
```

### Lease Abstraction Template
```
LEASE ABSTRACT

BASIC INFORMATION
Tenant:
Landlord:
Premises:
Lease Date:
Commencement:
Expiration:
Square Footage:

RENT
Base Rent: $____ PSF / $____ per month
Escalations:
Percentage Rent:

ADDITIONAL RENT
CAM:
Taxes:
Insurance:
Base Year/Stop:

OPTIONS
Renewal:
Expansion:
ROFR/ROFO:
Termination:

KEY DATES
Rent Commencement:
Option Notice Deadlines:
Lease Expiration:

SPECIAL PROVISIONS
Exclusivity:
Co-Tenancy:
Kick-Out Rights:

TENANT IMPROVEMENTS
Allowance: $____ PSF
Delivery Condition:
```

## Financing Documents

### Loan Document Checklist
- [ ] Loan Agreement/Note
- [ ] Mortgage/Deed of Trust
- [ ] Assignment of Leases and Rents
- [ ] Security Agreement
- [ ] Environmental Indemnity
- [ ] Guaranty (if applicable)
- [ ] UCC Financing Statements
- [ ] Subordination agreements

### Key Loan Terms
| Term | Description |
|------|-------------|
| LTV | Loan-to-value ratio |
| DSCR | Debt service coverage ratio |
| Interest Rate | Fixed, floating, caps |
| Prepayment | Penalty, yield maintenance, defeasance |
| Reserves | Taxes, insurance, TI/LC, capital |
| Recourse | Full, partial (carve-outs), non-recourse |
| Financial Covenants | Ongoing requirements |

### Carve-Out Guaranty Triggers
- Fraud
- Misappropriation of funds
- Voluntary bankruptcy
- Environmental liability
- Waste
- Prohibited transfers
- SPE covenant violations

## Zoning and Land Use

### Zoning Analysis
1. Verify current zoning classification
2. Check permitted uses
3. Review dimensional requirements
4. Identify variance/special permit needs
5. Check overlay districts
6. Review comprehensive plan

### Common Zoning Requirements
- Setbacks (front, side, rear)
- Height limitations
- Floor area ratio (FAR)
- Lot coverage
- Parking requirements
- Signage regulations
- Landscaping requirements

### Entitlement Process
```
Pre-Application → Application → Staff Review →
Public Hearing → Planning Commission →
City Council/Board → Permits
```

## Closing Process

### Seller Deliverables
- [ ] Deed (warranty, special warranty, quitclaim)
- [ ] Bill of sale
- [ ] Assignment of leases
- [ ] Assignment of contracts
- [ ] Tenant estoppels
- [ ] SNDA (if required)
- [ ] FIRPTA affidavit
- [ ] Authority documents
- [ ] Title affidavit
- [ ] Gap indemnity

### Buyer Deliverables
- [ ] Purchase price (wire)
- [ ] Authority documents
- [ ] Assumption agreements

### Closing Statement Items
- Purchase price
- Earnest money credit
- Prorations (taxes, rents, CAM)
- Title insurance premiums
- Recording fees
- Transfer taxes
- Attorney fees
- Escrow fees

## Integration with Other Skills

- **contract-lifecycle**: Lease and PSA review
- **due-diligence**: Transaction due diligence
- **environmental-law**: Environmental compliance
- **corporate-ma**: Real estate in M&A
- **tax-law**: 1031 exchanges, REIT issues

## Reference Files

For detailed guidance:
- `references/lease-forms.md` - Commercial lease templates
- `references/closing-checklist.md` - Transaction closing guide
- `references/title-review.md` - Title examination procedures
