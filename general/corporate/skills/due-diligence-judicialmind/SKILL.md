---
name: due-diligence-judicialmind
title: Due Diligence
description: Transaction due diligence skill for M&A, investment, and business transactions. Use when the user needs assistance with due diligence checklists, diligence review, risk assessment, diligence reports, or data room organization. Triggers on keywords like "due diligence", "diligence", "data room", "DD checklist", "diligence findings", "risk assessment", "transaction review", "investment review".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/due-diligence
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
sources:
- title: Checklist Templates
  path: references/checklist-templates.md
- title: Report Templates
  path: references/report-templates.md
- title: Risk Matrices
  path: references/risk-matrices.md
---

# Due Diligence

This skill provides expert guidance for conducting comprehensive due diligence in business transactions.

## Core Capabilities

### 1. Diligence Planning
- Scope definition
- Checklist development
- Team coordination
- Timeline management

### 2. Document Review
- Systematic analysis
- Issue identification
- Risk categorization
- Finding documentation

### 3. Risk Assessment
- Material findings
- Deal impact analysis
- Mitigation strategies
- Remediation requirements

### 4. Reporting
- Executive summaries
- Detailed findings
- Risk matrices
- Recommendation memos

## Due Diligence Process

### Diligence Workflow
```
┌─────────────────────────────────────────────────────────────────┐
│                    DUE DILIGENCE PROCESS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Scoping →  Information →  Review →  Analysis →  Reporting      │
│            Request                                               │
│                                                                  │
│    ↓           ↓            ↓          ↓           ↓            │
│                                                                  │
│  - Define    - Send DDL    - Document  - Risk      - Executive  │
│    scope     - Set up       review     assessment   summary     │
│  - Assign     data room   - Expert    - Issue      - Detailed   │
│    teams    - Track         consult    tracking     findings    │
│  - Create    responses    - Follow-up - Mitigation - Risk       │
│    timeline              questions    strategies    matrix      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Team Structure
| Team | Focus Areas |
|------|-------------|
| Legal | Corporate, contracts, litigation, IP, employment |
| Financial | Financials, accounting, tax, working capital |
| Business | Operations, customers, market, strategy |
| Technical | Technology, products, cybersecurity |
| Environmental | Environmental compliance, liabilities |
| HR | Employee matters, benefits, culture |

## Diligence Request Categories

### Corporate/Organizational
```
1. FORMATION DOCUMENTS
   □ Certificate/Articles of Incorporation
   □ Bylaws/Operating Agreement
   □ Amendments
   □ Good standing certificates

2. CAPITALIZATION
   □ Cap table (fully diluted)
   □ Stock ledger
   □ Option/warrant agreements
   □ Convertible instruments

3. GOVERNANCE
   □ Board minutes (3-5 years)
   □ Shareholder minutes
   □ Written consents
   □ Committee minutes

4. EQUITY AGREEMENTS
   □ Shareholder agreements
   □ Voting agreements
   □ Registration rights
   □ ROFR agreements
```

### Contracts & Commercial
```
5. CUSTOMER CONTRACTS
   □ Top 20 customers by revenue
   □ Standard forms
   □ Customer concentration analysis
   □ Pricing arrangements

6. SUPPLIER CONTRACTS
   □ Top 20 suppliers
   □ Single-source suppliers
   □ Key terms and pricing

7. STRATEGIC AGREEMENTS
   □ Joint ventures
   □ Partnerships
   □ Distribution agreements
   □ License agreements

8. REAL ESTATE
   □ Leases
   □ Owned property
   □ Environmental assessments
```

### Financial & Tax
```
9. FINANCIAL STATEMENTS
   □ Audited (3 years)
   □ Interim statements
   □ Management accounts
   □ Audit letters

10. DEBT & FINANCING
    □ Credit agreements
    □ Loan documents
    □ Security agreements
    □ Compliance certificates

11. TAX
    □ Tax returns (3-5 years)
    □ Tax provisions
    □ IRS correspondence
    □ Transfer pricing
```

### Employment & Benefits
```
12. EMPLOYMENT
    □ Employee census
    □ Executive agreements
    □ Offer letter forms
    □ Handbook/policies

13. COMPENSATION
    □ Compensation data
    □ Bonus plans
    □ Equity plans
    □ Commission structures

14. BENEFITS
    □ Benefit plan documents
    □ 401(k) plans
    □ Insurance policies
    □ COBRA compliance
```

### Intellectual Property
```
15. IP PORTFOLIO
    □ Patent list and status
    □ Trademark registrations
    □ Copyright registrations
    □ Domain names

16. IP AGREEMENTS
    □ License agreements (in/out)
    □ Assignment agreements
    □ Development agreements
    □ Open source usage
```

### Litigation & Regulatory
```
17. LITIGATION
    □ Pending matters
    □ Threatened claims
    □ Settlement agreements
    □ Insurance coverage

18. REGULATORY
    □ Permits and licenses
    □ Government correspondence
    □ Compliance certifications
    □ Investigation history
```

## Data Room Organization

### Standard Folder Structure
```
📁 1. Corporate
   📁 1.1 Formation Documents
   📁 1.2 Good Standing
   📁 1.3 Capitalization
   📁 1.4 Board Minutes
   📁 1.5 Shareholder Minutes
   📁 1.6 Equity Agreements

📁 2. Financial
   📁 2.1 Audited Financials
   📁 2.2 Interim Financials
   📁 2.3 Budget & Projections
   📁 2.4 Debt Documents

📁 3. Tax
   📁 3.1 Tax Returns
   📁 3.2 Tax Provisions
   📁 3.3 Correspondence

📁 4. Material Contracts
   📁 4.1 Customer Contracts
   📁 4.2 Supplier Contracts
   📁 4.3 Strategic Agreements
   📁 4.4 Real Estate

📁 5. Intellectual Property
   📁 5.1 Patents
   📁 5.2 Trademarks
   📁 5.3 Licenses
   📁 5.4 Software

📁 6. Employment
   📁 6.1 Agreements
   📁 6.2 Compensation
   📁 6.3 Benefits
   📁 6.4 Policies

📁 7. Litigation
   📁 7.1 Pending
   📁 7.2 Threatened
   📁 7.3 Settled

📁 8. Regulatory
   📁 8.1 Permits
   📁 8.2 Compliance
   📁 8.3 Environmental

📁 9. Insurance

📁 10. IT/Technology
```

### Data Room Best Practices
- Consistent naming conventions
- Version control
- Index with descriptions
- Access logging
- Watermarking (if needed)
- Q&A tracking

## Risk Assessment Framework

### Risk Categories
| Category | Impact | Examples |
|----------|--------|----------|
| Critical | Deal breaker | Fraud, undisclosed litigation, title defects |
| High | Price adjustment | Material contract issues, key employee departure |
| Medium | Post-close item | Compliance gaps, documentation deficiencies |
| Low | Note for file | Minor administrative issues |

### Risk Matrix Template
```
| # | Issue | Category | Risk Level | Deal Impact | Mitigation |
|---|-------|----------|------------|-------------|------------|
| 1 | [Finding] | Corporate | Critical | [Impact] | [Mitigation] |
| 2 | [Finding] | Contracts | High | [Impact] | [Mitigation] |
| 3 | [Finding] | Employment | Medium | [Impact] | [Mitigation] |
```

### Common Red Flags

**Corporate**
- Missing or incomplete records
- Unauthorized equity issuances
- Undocumented related party transactions
- Governance violations

**Contracts**
- Change of control triggers
- Assignment restrictions
- Unusual termination rights
- Missing key contracts

**Financial**
- Unexplained adjustments
- Related party transactions
- Off-balance sheet liabilities
- Revenue recognition issues

**Employment**
- Key person dependency
- Non-compete enforceability
- Misclassification issues
- ERISA violations

**IP**
- Ownership questions
- License restrictions
- Open source contamination
- Infringement claims

**Litigation**
- Undisclosed claims
- Insurance coverage gaps
- Regulatory investigations
- Pattern of disputes

## Due Diligence Report

### Executive Summary Template
```
EXECUTIVE SUMMARY

TRANSACTION OVERVIEW
- Target: [Company]
- Deal Structure: [Stock/Asset Purchase]
- Purchase Price: $[Amount]
- Closing Date: [Anticipated]

DILIGENCE SCOPE
[Description of scope and limitations]

KEY FINDINGS SUMMARY
1. [Critical/High Risk Issue #1]
2. [Critical/High Risk Issue #2]
3. [Material Issue #3]

DEAL IMPACT
[Overall assessment and recommendations]

RECOMMENDED ACTIONS
1. [Pre-closing requirement]
2. [Purchase agreement protection]
3. [Post-closing item]
```

### Detailed Findings Format
```
FINDING: [Title]

Category: [Corporate/Contracts/IP/Employment/Litigation/Tax/Other]
Risk Level: [Critical/High/Medium/Low]

Description:
[Detailed description of finding]

Documents Reviewed:
- [Document 1]
- [Document 2]

Analysis:
[Legal/business analysis of the issue]

Deal Impact:
[How this affects the transaction]

Recommended Mitigation:
[Suggested resolution]

Questions for Seller:
1. [Question]
2. [Question]
```

## Diligence Timeline

### Typical Timeline (Acquisition)
| Phase | Duration | Activities |
|-------|----------|------------|
| Week 1 | Setup | Send DDL, organize team, data room access |
| Week 2-3 | Initial Review | Review priority documents, identify issues |
| Week 4 | Deep Dive | Follow-up questions, expert consultations |
| Week 5 | Analysis | Risk assessment, findings compilation |
| Week 6 | Reporting | Draft report, team review, deliver |

### Milestone Checklist
- [ ] Data room access confirmed
- [ ] Initial document review complete
- [ ] Management meetings conducted
- [ ] Expert consultations complete
- [ ] Follow-up questions answered
- [ ] Risk matrix finalized
- [ ] Draft report circulated
- [ ] Final report delivered

## Integration with Other Skills

- **corporate-ma**: M&A transaction due diligence
- **contract-lifecycle**: Contract analysis
- **intellectual-property**: IP due diligence
- **employment-labor**: Employment matters review
- **environmental-law**: Environmental due diligence

## Reference Files

For detailed guidance:
- `references/checklist-templates.md` - Due diligence request lists
- `references/report-templates.md` - Report format examples
- `references/risk-matrices.md` - Risk assessment frameworks
