---
name: case-viability-report
title: Case Viability & Conflict Check Report
description: Produces internal case viability and conflict check memos for personal injury litigation intake. Screens conflicts, assesses liability and damages, checks statute of limitations, and outputs an accept/decline recommendation. Use when evaluating new PI intake, running conflict checks, assessing case merit pre-filing, or preparing acceptance memos.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/case-viability-report
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Case Viability & Conflict Check Report

Internal privileged memo evaluating a prospective PI matter for case acceptance, conflict clearance, and resource commitment.

## Prerequisites

- **Intake summary** — client name, adverse parties, incident date, injuries, objectives
- **Supporting documents** — police reports, medical records, photos, insurance info
- **Firm conflict database** — current/former clients, pending matters
- **Fee parameters** — contingency rates, cost-advance policy, minimum case value thresholds

## Quick Start

1. Gather intake summary and supporting documents
2. Run conflict screen against all parties and entities
3. Assess legal viability: claims, defenses, SOL, procedural bars
4. Project damages and calculate cost-benefit
5. Issue recommendation: ACCEPT / ACCEPT WITH CONDITIONS / DECLINE / DEFER
6. Draft executive summary with privilege designation

## Memo Sections

### 1. Factual Summary

- Chronological narrative of key events
- All parties identified (client, adverse parties, insurers, witnesses, related entities)
- Client's stated objectives
- Gap analysis:

| Missing Information | Impact (H/M/L) | Resolution Path |
|---|---|---|
| {item} | {level} | {method} |

### 2. Conflict of Interest Analysis

Screen every person/entity against firm databases.

**Check:** prospective client + affiliates, all adverse parties (named and anticipated), insurers/adjusters, key witnesses, subject matter overlap.

**For each conflict found:**

| Factor | Analysis |
|---|---|
| Type | Direct (Rule 1.7) / Former client (Rule 1.9) / Imputed (Rule 1.10) / Prospective (Rule 1.18) |
| Affected matter | {identify specifically} |
| Waivable? | Yes — informed written consent / No — {reason} |
| Proposed cure | Screening wall / Client consent / Decline |

If clear: state affirmatively with search date range and scope. Flag jurisdiction-specific RPC variations with [VERIFY].

### 3. Legal Viability

**A. Causes of Action** — For each claim, table elements vs. supporting/undermining facts and available evidence.

**B. Anticipated Defenses** — For each defense (comparative negligence, assumption of risk, etc.), assess likelihood, impact, and mitigation strategy.

**C. Statute of Limitations**

- Applicable statute with citation
- Accrual date and basis
- Tolling doctrines (discovery rule, minority, incapacity)
- **Filing deadline: {exact date}**
- Urgency: > 6 months / < 6 months / < 90 days / EXPIRED

**D. Procedural Requirements**

- [ ] Subject matter and personal jurisdiction
- [ ] Venue proper
- [ ] Administrative exhaustion (if applicable)
- [ ] Pre-suit notice requirements (e.g., government tort claims)
- [ ] Mandatory arbitration clauses
- [ ] Standing confirmed

**E. Red Flags**

- [ ] Client credibility concerns
- [ ] Prior claims / litigation history
- [ ] Social media contradicting injury claims
- [ ] Pre-existing conditions overlapping claimed injuries
- [ ] Adverse precedent in controlling jurisdiction
- [ ] Uncooperative or unreachable client
- [ ] Criminal exposure or parallel proceedings
- [ ] Gaps in medical treatment

### 4. Financial Viability

**Damages projection** — estimate low/mid/high for: past medical specials, future medical, lost wages, loss of earning capacity, pain & suffering, punitive (if applicable).

**Cost-benefit analysis** — projected attorney hours, fee arrangement, hard costs (filing, depositions, experts), total firm investment, expected recovery × probability of success, ROI ratio.

**Collectability** — assess insurance coverage, defendant assets, judgment-proofing concerns.

**Resource check:**

- [ ] Firm has subject-matter expertise
- [ ] Staffing capacity available
- [ ] Co-counsel needed? (if so, identified)
- [ ] Strategic value beyond fees (reputation, referral source, precedent)

### 5. Recommendation

One of:

- **ACCEPT** — conditions listed
- **ACCEPT WITH CONDITIONS** — specify prerequisites (waivers, retainer, investigation)
- **DECLINE** — specific reasons + referral suggestions
- **DEFER** — specify information needed + decision deadline

Rationale: synthesize conflict status, legal merit, financial viability, and strategic alignment in 2-3 paragraphs.

### 6. Executive Summary

- 3-5 bullet key findings
- One-sentence recommendation
- Report date, preparing attorney, contributors
- Sources consulted and search scope
- Time-sensitive deadlines flagged
- Privilege designation: *Attorney-Client Privileged / Work Product*

## Pitfalls & Rules

- **Candor** — internal document; sugar-coating risks harms the firm
- **SOL precision** — calculate deadlines exactly; flag < 90 days as urgent
- **Collectability** — never assume; verify insurance and assets
- **Ethics rules** — apply Model Rules of Professional Conduct; mark jurisdiction-specific variations with [VERIFY]
- **Minimum case value** — for contingency fees, apply firm threshold before recommending acceptance
- **Citations** — mark any unverifiable legal citation with [VERIFY]
- **Privilege** — state "Attorney-Client Privileged / Work Product" explicitly in output
