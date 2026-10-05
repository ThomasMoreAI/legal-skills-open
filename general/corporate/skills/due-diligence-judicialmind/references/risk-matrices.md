# Due Diligence Risk Assessment Matrices

## Overview

This document provides standardized risk assessment matrices for evaluating due diligence findings. The matrices use a red/yellow/green flagging system to quickly communicate risk levels and enable consistent risk assessment across transactions.

---

## 1. Master Risk Assessment Matrix

### 1.1 Risk Scoring Components

**Likelihood Score (L)**
| Score | Rating | Definition | Probability |
|-------|--------|------------|-------------|
| 1 | Remote | Highly unlikely to occur | <10% |
| 2 | Unlikely | Could occur but not expected | 10-25% |
| 3 | Possible | May occur; has occurred elsewhere | 25-50% |
| 4 | Likely | Probably will occur | 50-75% |
| 5 | Almost Certain | Expected to occur | >75% |

**Impact Score (I)**
| Score | Rating | Financial Impact | Operational Impact |
|-------|--------|-----------------|-------------------|
| 1 | Negligible | <$50K | Minor inconvenience |
| 2 | Minor | $50K-$250K | Limited disruption |
| 3 | Moderate | $250K-$1M | Significant disruption |
| 4 | Major | $1M-$5M | Severe disruption |
| 5 | Severe | >$5M | Business-threatening |

**Risk Score Calculation**
```
Risk Score = Likelihood (L) x Impact (I)
Range: 1-25
```

### 1.2 Risk Classification Matrix

```
                           IMPACT
                 1     2     3     4     5
              +-----+-----+-----+-----+-----+
           5  |  5  | 10  | 15  | 20  | 25  |
              +-----+-----+-----+-----+-----+
           4  |  4  |  8  | 12  | 16  | 20  |
L             +-----+-----+-----+-----+-----+
I          3  |  3  |  6  |  9  | 12  | 15  |
K             +-----+-----+-----+-----+-----+
E          2  |  2  |  4  |  6  |  8  | 10  |
L             +-----+-----+-----+-----+-----+
I          1  |  1  |  2  |  3  |  4  |  5  |
H             +-----+-----+-----+-----+-----+
O
O
D

Legend:
[1-4]   = GREEN  (Low Risk - Monitor)
[5-9]   = YELLOW (Moderate Risk - Manage)
[10-14] = ORANGE (High Risk - Mitigate)
[15-25] = RED    (Critical Risk - Escalate/Resolve)
```

### 1.3 Color-Coded Action Requirements

| Color | Score Range | Classification | Required Action |
|-------|-------------|----------------|-----------------|
| GREEN | 1-4 | Low | Document and monitor; no special action |
| YELLOW | 5-9 | Moderate | Active management; include in disclosure schedules |
| ORANGE | 10-14 | High | Mitigation required; consider purchase price adjustment |
| RED | 15-25 | Critical | Must resolve pre-closing or walk away |

---

## 2. Category-Specific Risk Matrices

### 2.1 Corporate/Organizational Risk Matrix

| Risk Factor | Green Flag | Yellow Flag | Red Flag |
|-------------|------------|-------------|----------|
| **Formation Documents** | Current, complete, properly executed | Minor deficiencies; correctable | Missing or defective formation |
| **Good Standing** | Current in all jurisdictions | Lapsed in non-material jurisdictions | Lapsed in key jurisdictions; dissolved |
| **Capitalization** | Clean cap table; all issuances documented | Minor documentation gaps | Disputed ownership; missing issuances |
| **Shareholder Agreements** | Standard provisions; all consents obtainable | Complex provisions; consent uncertainty | Blocking rights; hostile shareholders |
| **Governance** | Regular meetings; proper minutes | Gaps in minutes; informal governance | No governance documentation |
| **Subsidiaries** | All properly formed and maintained | Minor maintenance issues | Unclear ownership; improper formation |
| **Consents Required** | Few consents; all expected to be obtained | Multiple consents; some uncertainty | Material consents unlikely |

### 2.2 Intellectual Property Risk Matrix

| Risk Factor | Green Flag | Yellow Flag | Red Flag |
|-------------|------------|-------------|----------|
| **Ownership Chain** | Clear chain of title; all assignments documented | Minor gaps; correctable with confirmatory assignments | Broken chain; disputed ownership |
| **Employee IP Agreements** | All employees signed IP assignment | Most employees covered; key employees signed | Key developers without agreements |
| **Third-Party IP** | Minimal use; properly licensed | Moderate reliance; licenses in place | Heavy reliance; missing licenses |
| **Open Source** | Minimal use; permissive licenses only | Moderate use; compliant with license terms | Copyleft licenses in proprietary code |
| **Patent Portfolio** | Strong portfolio; no challenges | Adequate coverage; minor gaps | Key patents challenged or expiring |
| **Trademark Protection** | Registered in key jurisdictions | Some gaps in registration | Core marks unregistered or challenged |
| **Trade Secrets** | Robust protection program | Adequate protection; some gaps | Inadequate protection; potential exposure |
| **IP Litigation** | No pending or threatened claims | Minor claims; defensible position | Material infringement claims pending |
| **License Compliance** | Full compliance documented | Minor non-compliance; curable | Material breach; termination risk |

### 2.3 Employment Risk Matrix

| Risk Factor | Green Flag | Yellow Flag | Red Flag |
|-------------|------------|-------------|----------|
| **Classification** | All properly classified | Minor misclassification risk | Widespread misclassification |
| **Wage/Hour Compliance** | Full compliance; no claims | Minor issues; limited exposure | Systemic violations; class action risk |
| **Discrimination Claims** | No pending claims; good practices | Isolated claims; adequate response | Pattern of claims; systemic issues |
| **Employee Agreements** | Comprehensive coverage | Gaps in coverage; key employees covered | Key employees without agreements |
| **Non-Competes** | Enforceable; narrowly tailored | Enforceability uncertain | Unenforceable; restricts key hires |
| **Benefits Compliance** | ERISA compliant; proper documentation | Minor compliance issues | Material ERISA violations |
| **Union Relations** | No unions; no organizing activity | Limited union presence; stable relations | Active organizing; contentious relations |
| **Key Person Risk** | Deep bench; retention incentives in place | Some key person dependency | Critical dependency; retention uncertain |
| **WARN Act** | No anticipated issues | Potential triggering; notice period adequate | WARN Act violation likely |
| **Immigration** | All work authorization valid | Minor issues; correctable | Unauthorized workers; compliance gaps |

### 2.4 Litigation Risk Matrix

| Risk Factor | Green Flag | Yellow Flag | Red Flag |
|-------------|------------|-------------|----------|
| **Pending Litigation** | No material pending cases | Cases pending; within insurance coverage | Material uninsured exposure |
| **Threatened Claims** | No known threats | Demand letters; defensible positions | Credible threats; significant exposure |
| **Litigation History** | Clean history; favorable outcomes | Mixed history; average outcomes | Pattern of adverse outcomes |
| **Regulatory Actions** | No pending matters | Minor matters; compliance underway | Major enforcement action pending |
| **Government Investigations** | No known investigations | Inquiry stage; cooperation underway | Active investigation; exposure significant |
| **Product Liability** | No claims; quality program in place | Isolated claims; within insurance | Pattern of claims; recall risk |
| **Securities Litigation** | None (if applicable) | Class action threatened | Active securities class action |
| **Insurance Coverage** | Adequate coverage for risks | Gaps identified; additional coverage available | Material gaps; coverage disputes |

### 2.5 Tax Risk Matrix

| Risk Factor | Green Flag | Yellow Flag | Red Flag |
|-------------|------------|-------------|----------|
| **Federal Returns** | Filed timely; no audits | Minor issues; audits closed favorably | Open audits; material adjustments likely |
| **State/Local Returns** | Full compliance; nexus clear | Some nexus uncertainty | Material nexus exposure; back taxes |
| **Transfer Pricing** | Documentation complete; arm's length | Documentation gaps; reasonable positions | No documentation; aggressive positions |
| **NOL Carryforwards** | Well documented; no 382 issues | Potential 382 limitations | 382 limitations material; NOLs at risk |
| **Tax Positions** | Conservative positions | Uncertain positions properly reserved | Aggressive positions; material risk |
| **Sales Tax** | Full compliance; exemptions documented | Compliance gaps; manageable exposure | Material exposure; audit ongoing |
| **Employment Tax** | Full compliance | Minor classification issues | Significant classification exposure |
| **International** | Compliant structure | Planning reviewed; positions defensible | Aggressive structure; repatriation issues |

### 2.6 Environmental Risk Matrix

| Risk Factor | Green Flag | Yellow Flag | Red Flag |
|-------------|------------|-------------|----------|
| **Phase I Assessment** | REC-free; no further action | RECs identified; Phase II recommended | Significant contamination identified |
| **Phase II Assessment** | Contamination below thresholds | Contamination present; manageable cost | Extensive contamination; significant cost |
| **Permits** | All permits current; full compliance | Minor permit gaps; obtainable | Missing material permits; violations |
| **Compliance History** | Clean compliance record | Minor violations; corrected | Pattern of violations; enforcement |
| **Hazardous Materials** | Minimal use; proper handling | Moderate use; compliant handling | Significant use; handling concerns |
| **Underground Storage Tanks** | None or properly managed | USTs present; no known releases | Known releases; remediation needed |
| **Superfund Exposure** | No known exposure | De minimis exposure | Named PRP; material liability |
| **Asbestos/Lead** | None identified | Present but managed | Present; abatement required |
| **Wetlands/Protected Areas** | None on property | Minor encroachment; permit obtainable | Significant issues; development limited |

### 2.7 Contract Risk Matrix

| Risk Factor | Green Flag | Yellow Flag | Red Flag |
|-------------|------------|-------------|----------|
| **Customer Concentration** | No customer >10% of revenue | One customer >15% | One customer >25% or top 3 >50% |
| **Contract Assignability** | Assignable or consent likely | Consent required; cooperation expected | Anti-assignment clauses; consent uncertain |
| **Change of Control** | No adverse provisions | Provisions exist; waiver likely | Termination rights likely to be exercised |
| **Most Favored Customer** | No MFC clauses | Limited MFC clauses | Broad MFC clauses affecting pricing |
| **Exclusivity** | No exclusivity | Limited exclusivity | Broad exclusivity limiting buyer |
| **Minimum Commitments** | None or easily met | Moderate commitments; manageable | Material commitments; shortfall risk |
| **Termination Rights** | Long-term; limited termination | Standard termination provisions | Short-term; termination at will |
| **Price Protections** | Prices locked or buyer-favorable | Annual increase caps | Unilateral price increase rights |
| **Warranty Obligations** | Standard warranties | Extended warranties; manageable | Unusual warranties; significant exposure |
| **Indemnification** | Balanced provisions | Asymmetric but limited | Unlimited indemnification obligations |

### 2.8 Real Estate Risk Matrix

| Risk Factor | Green Flag | Yellow Flag | Red Flag |
|-------------|------------|-------------|----------|
| **Title** | Clear title; title insurance in place | Minor defects; curative available | Material title defects; clouds |
| **Survey** | Survey current; no encroachments | Minor survey issues | Material encroachments or disputes |
| **Zoning** | Fully compliant; permits in place | Non-conforming use; grandfathered | Zoning violations; variance needed |
| **Lease Terms** | Favorable terms; long-term | Standard terms; renewal options | Short-term; landlord termination rights |
| **Rent Levels** | Below market or at market | At market | Above market; reversion risk |
| **Lease Assignability** | Freely assignable | Consent required; not unreasonably withheld | Consent required; withheld possible |
| **Maintenance Condition** | Good condition; recent upgrades | Adequate condition; normal wear | Deferred maintenance; capital needed |
| **Environmental** | Phase I clean | Phase I with RECs; no material issues | Environmental contamination |

---

## 3. Aggregate Risk Dashboard

### 3.1 Category Summary Template

```
================================================================================
                     DUE DILIGENCE RISK DASHBOARD
================================================================================

Transaction: [Target Name]
Date: [Date]
Status: [Draft/Final]

--------------------------------------------------------------------------------
                         RISK SUMMARY BY CATEGORY
--------------------------------------------------------------------------------

Category              | GREEN | YELLOW | ORANGE | RED | Overall Rating
----------------------|-------|--------|--------|-----|---------------
Corporate             |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
Intellectual Property |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
Employment            |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
Litigation            |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
Tax                   |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
Environmental         |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
Contracts             |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
Real Estate           |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
Compliance            |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
Financial             |  [#]  |  [#]   |  [#]   | [#] | [GREEN/YELLOW/ORANGE/RED]
----------------------|-------|--------|--------|-----|---------------
TOTAL                 |  [#]  |  [#]   |  [#]   | [#] |
----------------------|-------|--------|--------|-----|---------------
OVERALL TRANSACTION RATING:                            [GREEN/YELLOW/ORANGE/RED]
================================================================================
```

### 3.2 Visual Risk Heat Map

```
================================================================================
                           RISK HEAT MAP
================================================================================

              IMPACT
              Low -------- Medium -------- High
           +----------------------------------+
    High   |    [Y]    |    [O]    |   [R]   |
           |           |           |         |
LIKELIHOOD |----------------------------------+
           |    [G]    |    [Y]    |   [O]   |
    Medium |           |           |         |
           |----------------------------------+
           |    [G]    |    [G]    |   [Y]   |
    Low    |           |           |         |
           +----------------------------------+

Issue Distribution:
- Quadrant [G]: [#] issues
- Quadrant [Y]: [#] issues
- Quadrant [O]: [#] issues
- Quadrant [R]: [#] issues

================================================================================
```

---

## 4. Issue Flagging Guidelines

### 4.1 Red Flags (Immediate Escalation Required)

**Corporate Red Flags**
- Disputed ownership of target company
- Invalid or missing formation documents
- Unauthorized issuances of equity
- Blocking shareholders opposing transaction
- Target not in good standing in state of incorporation

**IP Red Flags**
- Core technology owned by third party or former employee
- Pending patent infringement litigation on key products
- GPL or similar copyleft code in proprietary software
- Trade secrets disclosed without NDA protection
- Key patents invalid or expiring

**Employment Red Flags**
- Pending class action for wage/hour violations
- Pattern of discrimination claims
- Key employees without non-compete agreements (where enforceable)
- Imminent union organizing campaign
- WARN Act violation exposure

**Litigation Red Flags**
- Material uninsured litigation exposure
- Government investigation with criminal exposure
- Injunction risk affecting core business
- Multi-district litigation or mass tort claims
- Fraud allegations by customers or regulators

**Tax Red Flags**
- Open IRS audit with material exposure
- Undisclosed tax liabilities
- Transfer pricing adjustments likely
- Section 382 limitations on NOLs
- State nexus exposure in multiple jurisdictions

**Environmental Red Flags**
- Superfund PRP status with joint/several liability
- Known contamination requiring remediation
- Operating without required permits
- History of significant violations
- Asbestos or hazardous materials requiring abatement

**Contract Red Flags**
- Key contracts non-assignable without consent
- Change of control termination clauses likely to be exercised
- Customer accounting for >25% of revenue at risk
- Material breach of contract claims pending
- Long-term below-market commitments

### 4.2 Yellow Flags (Requires Management Attention)

- Documentation gaps that are curable
- Minor compliance issues with clear remediation path
- Pending matters with adequate reserves
- Consent requirements expected to be obtained
- Limited customer/supplier concentration
- Expiring contracts with renewal expectation
- Standard litigation within insurance coverage
- Known liabilities properly disclosed and reserved

### 4.3 Green Flags (Standard Documentation)

- Clean organizational records
- All IP properly documented and owned
- Standard employee agreements in place
- No material pending litigation
- Clean tax compliance history
- Clean environmental record
- Diversified customer and supplier base
- Standard contract terms

---

## 5. Risk Mitigation Tracking

### 5.1 Mitigation Plan Template

| Issue ID | Category | Risk Level | Mitigation Action | Owner | Due Date | Status | Residual Risk |
|----------|----------|------------|-------------------|-------|----------|--------|---------------|
| [ID] | [Cat] | [R/O/Y] | [Action] | [Name] | [Date] | [Status] | [R/O/Y/G] |

### 5.2 Status Definitions

- **Open**: Issue identified, mitigation not started
- **In Progress**: Mitigation underway
- **Pending Verification**: Mitigation complete, awaiting confirmation
- **Resolved**: Issue mitigated to acceptable level
- **Accepted**: Risk accepted without further mitigation
- **Escalated**: Elevated for senior decision

### 5.3 Pre-Closing Verification Checklist

- [ ] All RED issues resolved or walk-away decision made
- [ ] All ORANGE issues mitigated or reflected in deal terms
- [ ] Disclosure schedules updated with all YELLOW and above issues
- [ ] Special indemnities drafted for material issues
- [ ] Escrow/holdback amounts determined
- [ ] Bring-down conditions satisfied
- [ ] Third-party consents obtained
- [ ] Regulatory approvals received
- [ ] Final risk assessment approved by deal team
