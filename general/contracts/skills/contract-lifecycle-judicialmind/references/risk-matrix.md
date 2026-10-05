# Contract Risk Scoring Methodology

## Overview

This document establishes a standardized framework for assessing and scoring contract risk. The methodology enables consistent evaluation across contract types, facilitates prioritization of review resources, and supports data-driven contract management decisions.

---

## Section 1: Risk Scoring Framework

### 1.1 Scoring Scale (1-5)

| Score | Rating | Description | Action Required |
|-------|--------|-------------|-----------------|
| 1 | Minimal | Standard terms, low exposure | Proceed with standard process |
| 2 | Low | Minor deviations, manageable risk | Contract Manager approval |
| 3 | Moderate | Notable concerns, requires mitigation | Senior review required |
| 4 | High | Significant exposure, material risk | Legal escalation required |
| 5 | Critical | Unacceptable risk, potential deal-breaker | Executive approval or rejection |

### 1.2 Overall Risk Calculation

**Weighted Average Method**:
```
Overall Risk Score = Σ (Category Score × Category Weight) / Σ Weights
```

**Category Weights** (adjustable by organization):
| Category | Standard Weight |
|----------|-----------------|
| Financial Risk | 25% |
| Legal Risk | 25% |
| Operational Risk | 20% |
| Strategic Risk | 15% |
| Compliance Risk | 15% |

### 1.3 Risk Threshold Actions

| Overall Score | Risk Level | Required Actions |
|---------------|------------|------------------|
| 1.0 - 1.5 | Green | Standard processing |
| 1.6 - 2.5 | Green-Yellow | Document deviations |
| 2.6 - 3.5 | Yellow | Senior review, mitigation plan |
| 3.6 - 4.0 | Orange | Legal escalation, executive briefing |
| 4.1 - 5.0 | Red | Executive decision required |

---

## Section 2: Financial Risk Factors

### 2.1 Contract Value Risk

| Score | Criteria |
|-------|----------|
| 1 | <$50,000 total contract value |
| 2 | $50,000 - $250,000 |
| 3 | $250,001 - $1,000,000 |
| 4 | $1,000,001 - $5,000,000 |
| 5 | >$5,000,000 or percentage of revenue |

### 2.2 Payment Terms Risk

| Score | Criteria |
|-------|----------|
| 1 | Payment upon delivery/completion; Net 30 |
| 2 | Net 45-60; milestone-based payments |
| 3 | Net 90; advance payment <25% |
| 4 | Advance payment 25-50%; extended terms >90 days |
| 5 | Advance payment >50%; full prepayment required |

### 2.3 Liability Exposure Risk

| Score | Criteria |
|-------|----------|
| 1 | Mutual cap at 12-month fees; consequential damages excluded |
| 2 | Cap at 24-month fees; limited carve-outs |
| 3 | Cap at 36-month fees; multiple carve-outs |
| 4 | Cap exceeds 36-month fees; significant carve-outs |
| 5 | No cap; unlimited liability accepted |

### 2.4 Indemnification Risk

| Score | Criteria |
|-------|----------|
| 1 | Mutual, balanced indemnification; standard scope |
| 2 | Slightly broader indemnification obligations; reasonable caps |
| 3 | One-way indemnification; broad scope with caps |
| 4 | Broad one-way indemnification; limited caps |
| 5 | Unlimited one-way indemnification; defense obligations |

### 2.5 Pricing and Cost Risk

| Score | Criteria |
|-------|----------|
| 1 | Fixed pricing; no adjustment mechanism |
| 2 | CPI adjustment capped at 3% annually |
| 3 | Annual increases up to 5%; volume commitments |
| 4 | Uncapped price increases; minimum commitments |
| 5 | Unilateral pricing power; take-or-pay obligations |

### 2.6 Financial Stability Risk (Counterparty)

| Score | Criteria |
|-------|----------|
| 1 | Public company; investment-grade credit |
| 2 | Established private company; strong financials |
| 3 | Mid-market company; adequate financials |
| 4 | Early-stage company; limited financial history |
| 5 | Startup; financially distressed; high credit risk |

---

## Section 3: Legal Risk Factors

### 3.1 Intellectual Property Risk

| Score | Criteria |
|-------|----------|
| 1 | Customer owns all custom IP; clear license for pre-existing |
| 2 | Joint ownership with clear usage rights |
| 3 | Vendor retains ownership; broad customer license |
| 4 | Vendor ownership; limited license; restrictions on use |
| 5 | No IP rights transferred; vendor retains all rights |

### 3.2 Confidentiality Risk

| Score | Criteria |
|-------|----------|
| 1 | Mutual NDA; standard exceptions; 3-year term |
| 2 | Mutual NDA; extended term (5 years) |
| 3 | One-way confidentiality; broad disclosure rights |
| 4 | Weak confidentiality protections; short duration |
| 5 | No confidentiality obligations; free use of information |

### 3.3 Termination Rights Risk

| Score | Criteria |
|-------|----------|
| 1 | Mutual termination for convenience (30-60 days) |
| 2 | Mutual termination for convenience (90 days) |
| 3 | Termination for cause only; standard cure periods |
| 4 | Limited termination rights; long cure periods |
| 5 | No termination for convenience; limited cause rights |

### 3.4 Governing Law and Venue Risk

| Score | Criteria |
|-------|----------|
| 1 | Customer's preferred jurisdiction (Delaware, New York) |
| 2 | Neutral US jurisdiction |
| 3 | Counterparty's US jurisdiction |
| 4 | Foreign jurisdiction (common law, favorable) |
| 5 | Foreign jurisdiction (unfamiliar, unfavorable) |

### 3.5 Dispute Resolution Risk

| Score | Criteria |
|-------|----------|
| 1 | Litigation in preferred forum; jury trial preserved |
| 2 | Arbitration (AAA/JAMS) in neutral location |
| 3 | Arbitration in counterparty's location |
| 4 | Mandatory arbitration with unfavorable rules |
| 5 | Foreign arbitration; waiver of class action rights |

### 3.6 Assignment and Change of Control Risk

| Score | Criteria |
|-------|----------|
| 1 | Assignment requires consent; change of control termination right |
| 2 | Assignment requires consent; no change of control provision |
| 3 | Assignment permitted to affiliates without consent |
| 4 | Broad assignment rights; limited restrictions |
| 5 | Free assignability; survives change of control |

---

## Section 4: Operational Risk Factors

### 4.1 Performance Dependency Risk

| Score | Criteria |
|-------|----------|
| 1 | Non-critical service; multiple alternatives available |
| 2 | Important service; alternatives exist with transition effort |
| 3 | Significant operational dependency; limited alternatives |
| 4 | High dependency; few alternatives; transition difficulty |
| 5 | Mission-critical; sole source; no practical alternative |

### 4.2 Service Level Risk

| Score | Criteria |
|-------|----------|
| 1 | Comprehensive SLAs with meaningful credits; termination right for persistent failure |
| 2 | Standard SLAs with credits; escalation procedures |
| 3 | Limited SLAs; minimal credits |
| 4 | Best efforts standard; no credits |
| 5 | No service levels; no performance guarantees |

### 4.3 Business Continuity Risk

| Score | Criteria |
|-------|----------|
| 1 | Robust DR/BC plan; tested annually; RTO <4 hours |
| 2 | Documented DR/BC; RTO <24 hours |
| 3 | Basic DR/BC; RTO <72 hours |
| 4 | Minimal DR/BC provisions; extended recovery |
| 5 | No DR/BC requirements; no recovery guarantees |

### 4.4 Transition Risk

| Score | Criteria |
|-------|----------|
| 1 | Comprehensive transition assistance; data return; extended support |
| 2 | Standard transition assistance; reasonable data return |
| 3 | Limited transition assistance; data return at cost |
| 4 | Minimal transition support; data format restrictions |
| 5 | No transition assistance; data retention limitations |

### 4.5 Integration Complexity Risk

| Score | Criteria |
|-------|----------|
| 1 | Standalone solution; no integration required |
| 2 | Standard API integration; documented interfaces |
| 3 | Custom integration; moderate complexity |
| 4 | Deep system integration; significant development |
| 5 | Enterprise-wide integration; transformation required |

---

## Section 5: Strategic Risk Factors

### 5.1 Vendor Concentration Risk

| Score | Criteria |
|-------|----------|
| 1 | <5% of spend with vendor; diversified suppliers |
| 2 | 5-10% of category spend |
| 3 | 10-25% of category spend |
| 4 | 25-50% of category spend |
| 5 | >50% of category spend; single source |

### 5.2 Contract Duration Risk

| Score | Criteria |
|-------|----------|
| 1 | Annual term; mutual renewal |
| 2 | 2-year term; termination for convenience |
| 3 | 3-year term; termination for convenience |
| 4 | 3-5 year term; limited termination rights |
| 5 | >5 years; auto-renewal; difficult exit |

### 5.3 Exclusivity Risk

| Score | Criteria |
|-------|----------|
| 1 | Non-exclusive; full freedom of action |
| 2 | Limited exclusivity (geography or product) |
| 3 | Category exclusivity with exceptions |
| 4 | Broad exclusivity; limited exceptions |
| 5 | Full exclusivity; competitor restrictions |

### 5.4 Competitive Impact Risk

| Score | Criteria |
|-------|----------|
| 1 | No competitive restrictions |
| 2 | Standard non-solicitation of employees |
| 3 | Non-compete for specific products/services |
| 4 | Broad non-compete; significant restrictions |
| 5 | Exclusive dealing; most favored customer denied |

---

## Section 6: Compliance Risk Factors

### 6.1 Data Privacy Risk

| Score | Criteria |
|-------|----------|
| 1 | No personal data processing |
| 2 | Limited PII; standard DPA; domestic processing |
| 3 | Significant PII; compliant DPA; controlled transfers |
| 4 | Sensitive data; complex transfers; subprocessors |
| 5 | Special category data; high-risk processing; cross-border |

### 6.2 Regulatory Compliance Risk

| Score | Criteria |
|-------|----------|
| 1 | Minimal regulatory requirements |
| 2 | Standard industry compliance (SOC 2, ISO 27001) |
| 3 | Specific regulatory requirements (HIPAA, PCI) |
| 4 | Multiple regulatory frameworks; audit requirements |
| 5 | Highly regulated industry; government contracts |

### 6.3 Security Risk

| Score | Criteria |
|-------|----------|
| 1 | No access to systems or data |
| 2 | Limited access; standard security controls |
| 3 | System access; enhanced security requirements |
| 4 | Privileged access; comprehensive security program |
| 5 | Critical infrastructure access; highest security |

### 6.4 Audit Rights Risk

| Score | Criteria |
|-------|----------|
| 1 | Full audit rights; annual certification; SOC reports |
| 2 | Reasonable audit rights; third-party certifications |
| 3 | Limited audit rights; reliance on certifications |
| 4 | Minimal audit rights; limited transparency |
| 5 | No audit rights; no visibility into controls |

### 6.5 Insurance Risk

| Score | Criteria |
|-------|----------|
| 1 | Comprehensive coverage; appropriate limits; named insured |
| 2 | Standard coverage; adequate limits |
| 3 | Basic coverage; minimum limits |
| 4 | Limited coverage; below-standard limits |
| 5 | No insurance requirements; self-insured |

---

## Section 7: Risk Assessment Process

### 7.1 Pre-Assessment Checklist

Before scoring, gather:
- [ ] Draft contract or term sheet
- [ ] Counterparty financial information
- [ ] Business requirements documentation
- [ ] Stakeholder input on criticality
- [ ] Prior dealing history (if any)
- [ ] Industry/market intelligence

### 7.2 Scoring Process

**Step 1**: Score each applicable factor (1-5)
**Step 2**: Calculate category averages
**Step 3**: Apply category weights
**Step 4**: Calculate overall weighted score
**Step 5**: Determine risk level and required actions
**Step 6**: Document rationale for scores 4-5

### 7.3 Risk Assessment Template

```
CONTRACT RISK ASSESSMENT

Contract: _________________________
Counterparty: _____________________
Value: ___________________________
Assessor: ________________________
Date: ____________________________

FINANCIAL RISK (25%)
Contract Value:           [1-5] ___
Payment Terms:            [1-5] ___
Liability Exposure:       [1-5] ___
Indemnification:          [1-5] ___
Pricing Risk:             [1-5] ___
Counterparty Financial:   [1-5] ___
CATEGORY AVERAGE:         [   ] ___

LEGAL RISK (25%)
IP Risk:                  [1-5] ___
Confidentiality:          [1-5] ___
Termination Rights:       [1-5] ___
Governing Law:            [1-5] ___
Dispute Resolution:       [1-5] ___
Assignment:               [1-5] ___
CATEGORY AVERAGE:         [   ] ___

OPERATIONAL RISK (20%)
Performance Dependency:   [1-5] ___
Service Levels:           [1-5] ___
Business Continuity:      [1-5] ___
Transition:               [1-5] ___
Integration Complexity:   [1-5] ___
CATEGORY AVERAGE:         [   ] ___

STRATEGIC RISK (15%)
Vendor Concentration:     [1-5] ___
Contract Duration:        [1-5] ___
Exclusivity:              [1-5] ___
Competitive Impact:       [1-5] ___
CATEGORY AVERAGE:         [   ] ___

COMPLIANCE RISK (15%)
Data Privacy:             [1-5] ___
Regulatory Compliance:    [1-5] ___
Security:                 [1-5] ___
Audit Rights:             [1-5] ___
Insurance:                [1-5] ___
CATEGORY AVERAGE:         [   ] ___

OVERALL WEIGHTED SCORE:   [   ] ___
RISK LEVEL:               [   ] ___

HIGH-RISK FACTORS (Score 4-5):
_________________________________
_________________________________
_________________________________

MITIGATION RECOMMENDATIONS:
_________________________________
_________________________________
_________________________________

APPROVAL REQUIRED:
[ ] Contract Manager
[ ] Senior Counsel
[ ] General Counsel
[ ] Executive
```

---

## Section 8: Risk Mitigation Strategies

### 8.1 Financial Risk Mitigation
- Negotiate liability caps
- Require performance bonds or letters of credit
- Structure milestone payments
- Include audit rights for cost-plus contracts
- Require parent guarantees for subsidiaries

### 8.2 Legal Risk Mitigation
- Negotiate balanced IP provisions
- Strengthen confidentiality protections
- Add termination for convenience rights
- Include change of control provisions
- Negotiate favorable dispute resolution

### 8.3 Operational Risk Mitigation
- Define comprehensive SLAs with credits
- Require business continuity plans
- Include transition assistance obligations
- Establish governance and escalation procedures
- Require regular performance reporting

### 8.4 Strategic Risk Mitigation
- Avoid exclusivity where possible
- Limit contract duration
- Include benchmarking rights
- Reserve right to use competitors
- Build in exit ramps

### 8.5 Compliance Risk Mitigation
- Require appropriate certifications
- Include robust data protection provisions
- Establish audit and inspection rights
- Require insurance with appropriate limits
- Include regulatory change provisions

---

## Section 9: Reporting and Analytics

### 9.1 Portfolio Risk Dashboard
- Overall portfolio risk score
- Distribution by risk level (Green/Yellow/Orange/Red)
- Trend analysis over time
- High-risk contracts requiring attention
- Upcoming renewals by risk level

### 9.2 Key Risk Indicators (KRIs)
- Percentage of contracts above risk threshold
- Average time to resolve high-risk issues
- Number of exceptions approved by level
- Concentration risk metrics
- Compliance incident rate

### 9.3 Management Reporting
- Quarterly risk summary for leadership
- Exception reports for audit committee
- Trend analysis and recommendations
- Benchmarking against industry standards
