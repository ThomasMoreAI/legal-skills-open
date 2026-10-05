---
name: corporate-ma-judicialmind
title: Corporate & M&A
description: Corporate transactions and M&A legal practice skill. Use when the user needs assistance with mergers, acquisitions, due diligence, entity formation, shareholder agreements, stock purchase, asset purchase, corporate governance, or SEC filings. Triggers on keywords like "merger", "acquisition", "M&A", "due diligence", "shareholder agreement", "stock purchase", "asset purchase", "corporate formation", "LLC", "bylaws", "board resolution", "SEC filing".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/corporate-ma
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
sources:
- title: Deal Documents
  path: references/deal-documents.md
- title: Due Diligence
  path: references/due-diligence.md
- title: Sec Filings
  path: references/sec-filings.md
---

# Corporate & M&A

This skill provides expert guidance for corporate transactions, governance, and mergers & acquisitions.

## Core Capabilities

### 1. Entity Formation
- Choice of entity analysis
- Formation documents
- Governance structures
- Operating agreements/bylaws

### 2. M&A Transactions
- Deal structuring
- Due diligence coordination
- Transaction documents
- Closing mechanics

### 3. Corporate Governance
- Board procedures
- Shareholder rights
- Fiduciary duties
- Compliance programs

### 4. Securities Compliance
- Private placements
- SEC filings
- Blue sky compliance
- Disclosure requirements

## Entity Selection Matrix

| Entity Type | Liability Protection | Tax Treatment | Governance | Best For |
|-------------|---------------------|---------------|------------|----------|
| C Corporation | Full | Double taxation | Formal | VC-backed startups, public companies |
| S Corporation | Full | Pass-through | Formal | Small businesses, limited shareholders |
| LLC | Full | Flexible | Flexible | Most private businesses |
| LP | GP unlimited, LP limited | Pass-through | Partnership agreement | Investment funds, real estate |
| LLP | Partial (varies by state) | Pass-through | Partnership agreement | Professional services |
| Sole Proprietorship | None | Pass-through | N/A | Side businesses, testing ideas |

## M&A Transaction Types

### Stock Purchase vs. Asset Purchase

| Factor | Stock Purchase | Asset Purchase |
|--------|----------------|----------------|
| **What transfers** | Equity ownership | Selected assets/liabilities |
| **Liabilities** | All transfer (including unknown) | Only assumed liabilities |
| **Contracts** | Generally transfer | Require assignment/consent |
| **Tax to Seller** | Capital gains (usually) | Ordinary income + capital gains |
| **Tax to Buyer** | No step-up in basis | Step-up in basis |
| **Complexity** | Simpler documents | More complex, schedules |
| **Third-party consents** | Fewer required | More required |
| **Best for** | Clean targets, tax efficiency | Cherry-picking assets, limiting liability |

### Merger Structures

```
Forward Merger:
Target → Acquirer (Target disappears)

Reverse Merger:
Acquirer Sub → Target (Sub disappears, Target survives)

Forward Triangular Merger:
Target → Acquirer Sub (Target disappears into Sub)

Reverse Triangular Merger:
Acquirer Sub → Target (Sub disappears, Target survives as subsidiary)
```

## Due Diligence Framework

### Corporate/Organizational
- [ ] Charter documents (certificate of incorporation, bylaws)
- [ ] Good standing certificates
- [ ] Board/shareholder minutes and consents
- [ ] Capitalization table and stock ledger
- [ ] Shareholder agreements, voting agreements
- [ ] Subsidiary structure and organizational chart

### Financial
- [ ] Audited financial statements (3 years)
- [ ] Interim financial statements
- [ ] Projections and budgets
- [ ] Working capital analysis
- [ ] Debt instruments and guarantees
- [ ] Tax returns and tax positions

### Material Contracts
- [ ] Customer contracts (top 10-20)
- [ ] Supplier/vendor contracts
- [ ] License agreements (IP, technology)
- [ ] Real estate leases
- [ ] Equipment leases
- [ ] Joint venture/partnership agreements

### Employment/Labor
- [ ] Employment agreements (executives)
- [ ] Compensation and bonus plans
- [ ] Equity incentive plans
- [ ] Employee handbook and policies
- [ ] Benefit plan documents
- [ ] Union agreements, NLRB matters

### Intellectual Property
- [ ] Patent portfolio and applications
- [ ] Trademark registrations
- [ ] Copyright registrations
- [ ] Trade secrets inventory
- [ ] IP licenses (in and out)
- [ ] IP assignment agreements

### Litigation/Regulatory
- [ ] Pending litigation
- [ ] Threatened claims
- [ ] Government investigations
- [ ] Regulatory filings and correspondence
- [ ] Settlement agreements
- [ ] Insurance policies and claims history

### Compliance
- [ ] Permits and licenses
- [ ] Environmental compliance
- [ ] Data privacy compliance
- [ ] Industry-specific regulations
- [ ] FCPA/anti-corruption
- [ ] Export controls

## Transaction Documents

### Stock Purchase Agreement - Key Sections

1. **Purchase and Sale**: Stock being purchased, price, structure
2. **Representations and Warranties**: Seller and Company reps
3. **Covenants**: Pre-closing and post-closing obligations
4. **Conditions to Closing**: What must occur before closing
5. **Indemnification**: Allocation of risk for breaches
6. **Termination**: How deal can be terminated
7. **Miscellaneous**: Standard boilerplate

### Key Negotiation Points

| Issue | Buyer Position | Seller Position |
|-------|---------------|-----------------|
| **Rep Scope** | Broad, detailed | Narrow, qualified |
| **Knowledge Qualifier** | Actual + constructive | Actual only |
| **Materiality Scrape** | Full scrape | No scrape |
| **Indemnity Cap** | High (50-100% of purchase price) | Low (10-20%) |
| **Indemnity Basket** | Low deductible | High deductible |
| **Survival Period** | Long (3-6 years) | Short (12-18 months) |
| **Escrow** | Large (10-15%) | Small or none |
| **Earn-out** | Tied to conservative metrics | Tied to achievable metrics |

### Representation & Warranty Insurance

**Coverage**: Buyer-side policy covering breaches of seller reps
**Benefits**:
- Allows lower escrow/indemnity
- Cleaner exit for sellers
- Differentiated bid in competitive process

**Typical Terms**:
- Retention: 1% of enterprise value
- Premium: 2-4% of coverage
- Policy period: 3-6 years

## Closing Mechanics

### Closing Checklist Categories
1. Corporate approvals (board, shareholder)
2. Third-party consents
3. Government filings (HSR, state)
4. Financing conditions
5. Bring-down certificates
6. Closing deliverables

### Funds Flow
```
1. Buyer deposits purchase price to escrow
2. Escrow agent confirms receipt
3. Closing occurs (documents exchanged)
4. Escrow agent releases funds per flow memo:
   - Payoff existing debt
   - Pay transaction expenses
   - Fund escrow holdback
   - Distribute to sellers
```

## Corporate Governance

### Board of Directors

**Fiduciary Duties**:
- **Duty of Care**: Informed decision-making, business judgment rule
- **Duty of Loyalty**: No self-dealing, corporate opportunities
- **Duty of Good Faith**: Honest belief actions benefit corporation

**Board Actions**:
- Meetings (notice, quorum, voting)
- Written consents (unanimous in some states)
- Committees (audit, compensation, nominating)

### Shareholder Rights

**Fundamental Changes Requiring Approval**:
- Mergers and acquisitions
- Charter amendments
- Sale of substantially all assets
- Dissolution

**Protective Provisions** (typical for preferred stock):
- Changes to authorized shares
- Changes to preferences
- Issuance of senior securities
- Dividends/distributions
- Redemptions
- Board composition changes

## SEC Filing Requirements

### Form Types

| Form | Purpose | When Required |
|------|---------|---------------|
| S-1 | IPO registration | Going public |
| 10-K | Annual report | Annually (60-90 days after FYE) |
| 10-Q | Quarterly report | Quarterly (40-45 days after quarter) |
| 8-K | Current report | Within 4 business days of event |
| DEF 14A | Proxy statement | Before shareholder meeting |
| Form 4 | Insider trading | Within 2 business days |
| Schedule 13D | Beneficial ownership (>5%) | Within 10 days |

### Material Events Requiring 8-K
- Entry into material definitive agreement
- Completion of acquisition or disposition
- Material impairments
- Changes in control
- Departure of directors/officers
- Amendments to charter/bylaws
- Bankruptcy

## Integration with Other Skills

- **due-diligence**: Transaction due diligence process
- **contract-lifecycle**: Transaction document review
- **tax-law**: Tax structuring of transactions
- **compliance-tracking**: Regulatory compliance
- **legal-research**: Precedent and statutory research

## Reference Files

For detailed checklists and templates:
- `references/due-diligence.md` - Comprehensive DD checklist
- `references/deal-documents.md` - Transaction document guide
- `references/sec-filings.md` - SEC compliance reference
