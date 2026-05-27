---
name: unclaimed-property-policy
title: Escheatment and Unclaimed Property Policy
description: Drafts an enterprise Escheatment and Unclaimed Property Policy covering property identification, dormancy matrices, due diligence notices, NAUPA-format reporting, remittance, recordkeeping, and audit preparedness across all US state jurisdictions. Use when establishing or updating an unclaimed property compliance framework, preparing for state audits, or evaluating voluntary disclosure programs.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/unclaimed-property-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
tags: [drafting, policy, research]
---

# Escheatment and Unclaimed Property Policy

Drafts a governance policy for systematic compliance with all 50 states' unclaimed property (escheat) laws, from identification through remittance and audit defense.

## Prerequisites

1. **Organizational footprint** — states of incorporation, operation, and property-holding
2. **Property type inventory** — all property categories held (deposits, checks, securities, credits, gift cards, etc.)
3. **Existing compliance artifacts** — prior reports, audit correspondence, VDA agreements
4. **Designated policy owner** — CFO, General Counsel, or Compliance Officer with escheat authority
5. **Industry context** — financial services, insurance, utilities, or retail (drives property-type rules)

> **Research step**: Search uploaded org documents for existing policies, prior reports, and audit history before drafting. Supplement with current state statutory requirements for all jurisdictions in the org's footprint.

## Quick Start

1. Gather prerequisites (footprint, property inventory, existing artifacts)
2. Build dormancy period matrix for each state × property type
3. Draft policy sections in order: governance → identification → dormancy → priority rules → due diligence → reporting → recordkeeping → audit preparedness
4. Validate all state-specific periods and thresholds against current statutes
5. Route for CFO/GC approval; schedule annual review cycle

## Core Workflow

### 1. Purpose and Governance

| Element | Content |
|---|---|
| Scope | All 50 states + D.C. + applicable territories; all units holding third-party property |
| Policy owner | Named role with authority to interpret, grant exceptions, coordinate audits |
| Stakeholders | Business units (identify), Accounting (report/remit), Legal (guidance), Internal Audit (verify) |
| Review cycle | Annual minimum; triggered updates on legislative changes |

### 2. Property Identification

| Property Type | Review Freq. | Dormancy Trigger | Notes |
|---|---|---|---|
| Demand/savings accounts | Quarterly | Last owner-initiated contact | Interest credits, fee debits ≠ owner contact |
| Time deposits | Quarterly | Maturity date + dormancy period | — |
| Uncashed checks (payroll) | Monthly | Date of issuance | Often 1–3 yr dormancy |
| Uncashed checks (vendor/refund) | Quarterly | Date of issuance | — |
| Securities / dividends | Quarterly | Last owner activity or uncashed distribution | Includes street name, DRIP, fractional shares |
| Customer credits / overpayments | Quarterly | Date credit created | Includes utility deposits, insurance overpayments |
| Gift cards / stored value | Quarterly | Last redemption activity | CARD Act: no expiration < 5 yrs; state exemptions vary |
| Insurance proceeds | Per policy terms | Date payable or last owner contact | — |
| Safe deposit box contents | Annually | Lease expiration + dormancy period | — |

- **Flag** items within 6 months of dormancy threshold for due diligence prep
- **Exclude** property below de minimis thresholds, property under valid liens, legally exempt instruments

### 3. Dormancy Period Matrix

Maintain a living matrix (update annually): rows = property types, columns = state jurisdictions, cells = dormancy period (years) + statute citation.

| Property Type | Typical Range | Common Period |
|---|---|---|
| Bank accounts | 3–7 yrs | 5 yrs |
| Wages / payroll | 1–3 yrs | 1–2 yrs |
| Uncashed checks | 1–5 yrs | 3 yrs |
| Securities | 3–5 yrs | 3 yrs |
| Insurance proceeds | 3–5 yrs | 3 yrs |
| Gift cards | 1–7 yrs | 5 yrs (many states exempt) |

### 4. Jurisdictional Priority Rules

Apply the Supreme Court priority hierarchy (*Texas v. New Jersey*, 379 U.S. 674 (1965); *Pennsylvania v. New York*, 407 U.S. 206 (1972) [VERIFY citations]):

1. **First priority**: State of owner's last known address
2. **Second priority**: State of holder's incorporation (intangible) or state where property is held (tangible) — applies when no address known, address outside US, or address invalid

| Scenario | Rule |
|---|---|
| Wages | Employee's last known address state |
| Insurance proceeds | Insured's last known address state |
| Business entity owner | Entity's state of incorporation or principal place of business |
| Unknown/foreign address | Holder's state of incorporation |
| Multi-state claims | Follow priority hierarchy; document analysis; escalate to legal |

### 5. Due Diligence

**Notice thresholds** (verify per state):

| Threshold | Typical Requirement |
|---|---|
| ≥ $50 | Some states require notice |
| $50–$250 | Most states require written notice |
| All amounts | Some states (e.g., California [VERIFY]) require notice regardless |

**Timing**: 60–120 days before report due date (some states require up to 240 days).

**Notice must include**: statement of held property; property description (account, type, value); claim instructions; response deadline; org contact info; plain language tone.

**Retain**: copies of notices, mailing dates/addresses, returned mail with USPS notations, owner responses, reunification records.

**Returned mail**: Use address verification services, review other org records, search public databases. Document all attempts.

### 6. Reporting and Remittance

**Compliance calendar** (work backward from each state deadline):

| Milestone | Timing |
|---|---|
| Property identification complete | 180 days before deadline |
| Due diligence notices sent | 60–240 days before (state-specific) |
| Report compilation & reconciliation | 45 days before |
| Internal review & approval | 30 days before |
| Submission & remittance | On or before deadline |

**Filing deadlines**: Most states March 1 – November 1 annually. Maintain per-state calendar.

**Report checklist**: property aggregated by state per priority rules; categorized per state property-type codes; owner data complete (name, address, type, last contact, value, SSN/TIN); NAUPA II format (or state-specific portal); interest calculated where required; reconciled to accounting records; CFO/GC sign-off obtained.

**Remittance**: EFT (cash), DTC/certificate (securities), physical delivery (tangible). Retain confirmations and state acknowledgments.

**Amended reports**: File promptly on discovering material errors; document basis; obtain same approval as original.

**Voluntary disclosure**: When prior-year non-compliance found, engage counsel to evaluate VDA options (reduced look-back, penalty/interest waivers) before self-reporting.

### 7. Recordkeeping

| Record Category | Retention | Notes |
|---|---|---|
| Property records | 10 yrs from report date | Some states audit 10+ yrs back |
| Due diligence documentation | 10 yrs from report date | Notices, responses, reunifications |
| Filed reports & remittances | 10 yrs from report date | Include state acknowledgments |
| Audit correspondence & settlements | Permanent | — |

Ensure electronic records remain accessible through system migrations with backup copies and audit trails.

### 8. Audit Preparedness

| Role | Responsibility |
|---|---|
| Audit Coordinator | Primary state contact; document coordination; strategy |
| Legal Counsel | Privilege review; assessment challenges; settlement negotiation |
| Business Unit Managers | Produce records on request |
| Senior Management | Approve settlement positions |

**Audit lifecycle**: scoping (establish privilege boundaries) → document production (log all productions) → conferences (document communications) → work paper review (challenge unsupported findings) → assessment negotiation → appeal (evaluate for strong grounds).

### 9. Continuous Improvement

- Annual compliance review: error rates, audit findings, late filings
- Monitor proposed legislation in key jurisdictions
- Train personnel on policy updates within 30 days of material changes
- Update dormancy matrix and compliance calendar annually

## Pitfalls and Checks

- **Always verify** current dormancy periods and notice requirements against state statutes — this policy is a framework, not a substitute for jurisdiction-specific legal review
- **Priority rules govern**: Apply *Texas v. New Jersey* hierarchy every time; never default to holder's state
- **Owner-initiated contact only**: Bank fees, interest credits, and automated statements do not reset dormancy
- **VDA before audit**: Evaluate voluntary disclosure before a state-initiated audit forecloses the option
- **10-year retention floor**: Some high-risk states may warrant longer
- **CARD Act**: Gift card provisions must comply with federal law (no expiration < 5 yrs) and state exemptions
- **Industry-specific rules**: Financial services holders must verify special rules for securities, insurance, and custody property per state
- **[VERIFY]**: Confirm all statutory and case citations against current law before finalizing
