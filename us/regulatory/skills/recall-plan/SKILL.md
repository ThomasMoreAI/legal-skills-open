---
name: recall-plan
title: Recall Plan and Procedure
description: Drafts FDA product recall plans compliant with 21 CFR Part 7, covering Recall Committee governance, health hazard evaluation, recall classification, notification protocols, effectiveness checks, product disposition, and termination procedures. Use when developing recall SOPs, updating recall procedures, drafting recall readiness plans, or preparing FDA-regulated product recall documentation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/recall-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# Recall Plan and Procedure

Drafts the company's official FDA-compliant recall protocol under 21 CFR Part 7 and the FD&C Act.

## Prerequisites

Gather before drafting:
- Company profile — product categories, distribution channels, manufacturing sites
- Existing QMS documents — quality manual, CAPA procedures, complaint handling SOPs
- Regulatory filings — NDC numbers, device ID codes, 510(k)/PMA references
- Organizational chart — key personnel in QA, Regulatory, Legal, Operations, Communications, Executive
- Distribution records — channel structure, geographic scope, sub-distribution
- Prior recall history (if any) — FDA correspondence, lessons learned

## Quick Start

1. Collect prerequisites and confirm product scope
2. Draft each section below in order
3. Flag evolving guidance with `[VERIFY CURRENT GUIDANCE]`
4. Route draft through Legal and Regulatory review

## Core Sections

### 1. Purpose and Scope

State commitment to consumer safety, applicability to all FDA-regulated products, and governing authority (21 CFR Part 7, FD&C Act).

### 2. Recall Committee

Define these roles with named personnel:

| Role | Typical Position | Key Duties |
|------|-----------------|------------|
| Chair | VP Quality+ | Final recall decisions, FDA liaison oversight |
| Regulatory Lead | Head of RA | FDA notifications, classification coordination |
| Legal Counsel | GC / Outside Counsel | Risk assessment, notification review, litigation hold |
| Operations Lead | Head of Mfg/Supply Chain | Retrieval logistics, inventory quarantine |
| Communications Lead | Head of Corp Comms | Press releases, social media, consumer contact |
| Quality Lead | QA Director | HHE, effectiveness checks, CAPA |

**Convening:** Within 4 hours (business) / 12 hours (after-hours). Maintain emergency contact tree with 2 backups per role and documented alternates.

**Decisions:** Consensus preferred; Chair has unilateral emergency authority. Document rationale, attendees, and dissenting views.

### 3. Health Hazard Evaluation (HHE)

Assess these factors in a formal report with supporting data:

- Nature of defect (contamination, mislabeling, malfunction)
- Adverse outcome likelihood (scientific/medical evidence)
- Vulnerable populations (pediatric, immunocompromised, elderly)
- Severity x probability of harm
- Defect prevalence in distributed product

**FDA recall classification:**

| Class | Standard | Examples |
|-------|----------|----------|
| I | Reasonable probability of serious harm or death | Pathogen contamination, wrong active ingredient, life-threatening device failure |
| II | Temporary/reversible consequences; remote serious risk | Minor contamination, labeling errors, device defects causing temporary harm |
| III | Not likely to cause adverse consequences | Minor labeling violations, aesthetic defects |

Company proposes classification; FDA assigns final. Complete HHE proportionate to urgency.

### 4. Recall Strategy

**Depth of recall:**

| Level | Scope | When |
|-------|-------|------|
| Consumer/User | End users; public warnings | Serious hazard + product reached consumers |
| Retail | Retailers/dispensers only | Hazard manageable at retail; product distinguishable |
| Wholesale | Wholesale chain only | Product not yet at retail |

**Public warning required when:** Class I + product reached consumers, product not easily distinguished from safe product, or FDA requests it.

**Document:** Depth justification, public warning plan, timeline, FDA consultation record, adjustment provisions.

### 5. Notification Protocols

#### FDA Notification (21 CFR 7.46)

Submit to jurisdictional FDA district office immediately upon initiating recall; no later than 10 working days.

```
- [ ] Product identity (NDC/device ID, lot numbers)
- [ ] Reason for recall — specific defect
- [ ] HHE and proposed classification
- [ ] Quantity produced and time span
- [ ] Quantity in distribution
- [ ] Distribution pattern (geography, customer types)
- [ ] Proposed strategy (depth, warnings, effectiveness level)
```

#### Trade Notifications

Legal + Regulatory must approve before distribution.

```
- [ ] Prominent "RECALL NOTICE" header
- [ ] Product ID with lot numbers and visual aids
- [ ] Plain-language recall reason
- [ ] Instructions for identifying affected inventory
- [ ] Required actions (quarantine, return, destroy)
- [ ] Lot verification procedure
- [ ] Contact information
- [ ] Request for written confirmation
```

#### Public/Consumer Notifications

Coordinate press releases with FDA. Use social media for rapid dissemination. Contact consumers directly when registry data available.

**Record all notifications:** date/time, recipients, method, copies, responses.

### 6. Effectiveness Checks

| Level | Typical Class | Requirement |
|-------|--------------|-------------|
| A | I | Contact 100% of direct accounts |
| B | II | Contact representative sample |
| C | III | Confirm notification receipt |

**Collect per check:** notification receipt confirmation, product identified, quarantine confirmed, quantity reconciliation, sub-distribution info.

**Report to FDA:** At 2-week, 4-week, and 8-week intervals (or as directed).

**Non-responsive escalation:** Repeated contact → certified mail with return receipt → personal visit → notify FDA.

### 7. Product Disposition

| Option | When | Requirements |
|--------|------|-------------|
| Destruction | Contamination, fundamental defects (default) | Witnessed, certificate (date/method/qty/lots), photo/video for high-value |
| Reconditioning | Correctable defect; FDA pre-approval | Detailed proposal, QC verification per unit, batch records |
| Relabeling | Labeling-only; FDA pre-approval | Proposal, per-unit verification, records |
| Return to mfg | Evaluation/rework | Full chain of custody |

**Storage:** Segregated, restricted access, conspicuously marked, full inventory controls.

**Accountability:** Periodic reconciliation of distributed vs. returned vs. disposed quantities. Investigate discrepancies. Prevent unauthorized re-entry into distribution.

### 8. Recall Termination

**FDA decides termination, not the company.** Never unilaterally declare completion or make public statements suggesting recall has concluded without written FDA agreement.

```
- [ ] Final effectiveness check results (% accounted for)
- [ ] Quantity reconciliation with explanations for gaps
- [ ] Complete disposition records
- [ ] All recall notifications/communications
- [ ] Outcome summary with lessons learned
- [ ] Formal termination request
```

### 9. Post-Recall Review

**Monitoring:** Handle recalled product surfacing after termination; notify FDA if significant quantities found.

**Retention:** Complete recall file minimum 2 years beyond termination (longer per litigation holds).

**Review checklist:**

```
- [ ] Timeliness of initial HHE
- [ ] Adequacy of recall strategy and mid-course adjustments
- [ ] Effectiveness of notifications
- [ ] Efficiency of recovery and disposition
- [ ] Resource and personnel adequacy
- [ ] Plan gaps identified
- [ ] Root cause / systemic quality issues
```

Produce written report with CAPA recommendations tracked through QMS.

## Pitfalls

- **Never self-terminate:** Only FDA can authorize recall completion
- **Classification is FDA's call:** Company proposes; FDA assigns final classification
- **Reconditioning/relabeling require pre-approval:** Do not proceed without FDA authorization
- **Guidance evolves:** Flag sections with `[VERIFY CURRENT GUIDANCE]` where FDA guidance may have changed
- **Cross-reference requirements:** Medical devices — MDR reporting (21 CFR Part 803) `[VERIFY]`; Drugs/biologics — field alert reporting (21 CFR 314.81) `[VERIFY]`
- **International distribution:** Coordinate with foreign regulatory authorities if distributing outside the US
- **Dual audience:** Maintain legal precision for counsel while keeping operational sections accessible to non-legal staff
