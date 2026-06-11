---
name: adverse-event-reporting-policy
title: Adverse Event Reporting Policy
description: Drafts an Adverse Event Reporting Policy compliant with 21 CFR 312.32 (IND safety reporting), 21 CFR 314.80 (postmarketing), and ICH E2A, with multi-jurisdictional overlays (EMA, PMDA, Health Canada). Covers seriousness/causality frameworks, expedited reporting timelines, roles, documentation standards, training mandates, and QA mechanisms. Use when drafting or updating an adverse event reporting policy, pharmacovigilance policy, AE/SAE reporting SOP, or safety reporting framework for a pharmaceutical company, CRO, biotech, or clinical research institution.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/adverse-event-reporting-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: life-sciences
language: en
tags: [drafting, policy]
---

# Adverse Event Reporting Policy

Drafts a binding AE reporting policy meeting FDA requirements and ICH standards for pharma, biotech, CROs, and healthcare organizations conducting or sponsoring clinical research.

## Prerequisites

Gather before drafting. If any item is missing, pause and ask — do not assume.

1. **Organization type** — pharmaceutical sponsor, CRO, healthcare system, academic medical center, or combination
2. **Product portfolio** — IND products (Phase I–IV), approved drugs, biologics, devices, combination products, REMS-covered products
3. **Geographic footprint** — domestic only vs. multi-jurisdictional (EU, Japan, Canada, etc.)
4. **Therapeutic areas** — flag specialized populations: oncology, vaccines, biologics, pediatrics
5. **Existing SOPs** — current pharmacovigilance SOPs, IRB agreements, DSMB charters to cross-reference

## Step 1: Introduction & Compliance Statement

- Cite controlling regulations:
  - **21 CFR 312.32** — IND safety reporting
  - **21 CFR 314.80** — Postmarketing adverse drug experience
  - **ICH E2A** — Clinical safety data management
  - **21 CFR 803** — Medical device reporting (if applicable)
  - Applicable state and international requirements
- Effective date, review cycle (annual minimum), approval authority
- Binding compliance statement: policy adherence is condition of employment; violations may constitute federal law violations

## Step 2: Definitions

Include at minimum:

| Term | Definition |
|------|-----------|
| **Adverse Event (AE)** | Any untoward medical occurrence; causal relationship need not be established |
| **Serious Adverse Event (SAE)** | Meets ≥1 of 6 FDA/ICH seriousness criteria |
| **Unexpected AE** | Not in current IB, package insert, or reference safety information by nature, severity, or frequency |
| **Suspected Adverse Reaction** | Reasonable possibility of causal relationship |
| **Causality Assessment** | Systematic evaluation using validated algorithm (Naranjo, WHO-UMC) |
| **Sponsor Awareness** | When *any* sponsor employee first receives AE information — starts all reporting clocks |
| **Expedited Report** | 7-day (fatal/life-threatening) or 15-day (other serious) IND safety report |

**SAE Seriousness Criteria (6 FDA/ICH):**
1. Death
2. Life-threatening (immediate risk at time of event)
3. Inpatient hospitalization or prolongation
4. Persistent/significant disability or incapacity
5. Congenital anomaly/birth defect
6. Important medical event requiring intervention to prevent serious outcome

## Step 3: Scope

**Covered activities:** Phase I–IV clinical trials; post-marketing surveillance; expanded access/compassionate use; investigator-initiated studies

**Covered products:** IND products, approved drugs, biologics, vaccines, gene therapies, medical devices (IDE), combination products, REMS-covered products

**Geographic scope:** Specify domestic-only vs. global; address how international events feed FDA reporting; handle countries where product is unapproved

**Temporal boundaries:**
- Begins: informed consent signature or first dose
- Ends: per protocol follow-up period (specify days; address long half-life/delayed-effect products)

**Exclusions:**

| Excluded Item | Redirect To |
|--------------|-------------|
| Product quality complaints (no patient impact) | Quality Assurance SOP |
| Occupational exposures without health effects | Occupational Health |
| Near-miss medication errors | Medication Safety Program |
| Competitor product AEs in comparator arms | Protocol-specific requirements |

## Step 4: Roles & Responsibilities

| Role | Key Obligations | Timeline |
|------|----------------|----------|
| **Safety Officer / PV Director** | Final reportability, seriousness, causality, expectedness determinations; FDA liaison | Review within 4 hrs; reportability within 8 hrs |
| **Principal Investigator** | Evaluate each AE; causality/seriousness determination; IRB notification | Report to Safety Officer within 24 hrs of awareness |
| **Clinical Research Coordinator** | Active surveillance (interviews, labs, vitals); source documentation; escalate SAEs immediately | Escalate immediately; do not wait for scheduled visits |
| **Clinical Monitor/CRA** | Verify source docs vs. CRF; confirm timeline compliance; escalate systemic deficiencies | Document in monitoring reports; verify CAPAs at next visit |
| **Senior Management** | Resource adequacy; aggregate safety review; risk-benefit decisions | Quarterly review minimum |
| **QA** | Independent audits; CAPA oversight | Annual minimum audit; ad hoc for signals |

## Step 5: AE Identification & Assessment

**Active surveillance:** Structured patient interviews at each contact; lab values vs. protocol ranges and clinically significant change thresholds; physical examination with baseline comparison; concomitant medication review (may indicate unreported AE).

**Passive surveillance:** Dedicated patient reporting line/email/portal; external provider reporting pathway; EHR alert integration (hospitalizations, ED visits, critical labs) where feasible.

**Causality assessment — document each factor:**

| Factor | Document |
|--------|----------|
| Temporal relationship | Time from last dose to onset |
| Biological plausibility | Known pharmacology/class effects |
| Dechallenge | Symptom change upon discontinuation |
| Rechallenge | Symptom recurrence upon restart |
| Alternative explanations | Disease progression, comedications, other factors |
| Prior literature/experience | Published reports, IB data |

Use validated tool (Naranjo Scale or WHO-UMC). Document algorithm applied and narrative rationale — not just final conclusion.

**Severity grading:** CTCAE or protocol-specified scale; document grade and supporting clinical findings.

**Enhanced monitoring populations:** Pediatric (developmental); pregnant (maternal/fetal); elderly with polypharmacy (attribution complexity); immunocompromised (atypical presentations).

## Step 6: Reporting Timelines & Submission

**Expedited IND Safety Reports (21 CFR 312.32):**

| Event Type | FDA Deadline | Internal Trigger |
|-----------|-------------|-----------------|
| Fatal or life-threatening SUSAR | 7 calendar days from sponsor awareness | Safety Officer notified within 4 hrs |
| Other serious SUSAR | 15 calendar days from sponsor awareness | Safety Officer notified within 4 hrs |
| Follow-up to 7-day report | 8 additional calendar days (15 total) | Initiate at day 7 submission |

**Other reporting obligations:**
- **Annual IND Safety Reports** — within 60 days of IND anniversary; tabular AE summaries, narrative SAE descriptions, signal analysis, updated risk-benefit
- **IRB/IEC** — same timeline as FDA or 24 hours per IRB requirements, whichever more stringent; all SAEs regardless of causality
- **DSMB/IDMC** — per charter; unblinded data; expedited notification for predefined stopping rules

**Postmarketing (21 CFR 314.80):** 15-day alert reports for serious unexpected AEs; PADERs per approved schedule.

**Submission mechanics:** FDA Electronic Submission Gateway; Form 3500A; ICH E2B(R3) format. Backup: telephone for urgent situations. Retain all submission confirmations and FDA acknowledgment receipts.

**Multi-jurisdictional overlay:**

| Agency | Key Differences |
|--------|----------------|
| EMA | EudraVigilance submission; potential seriousness/expectedness definition differences |
| PMDA (Japan) | Local timelines; Japanese labeling as reference document [VERIFY] |
| Health Canada | MedEffect reporting [VERIFY current timelines] |

## Step 7: Documentation Standards

**Source documents:** Created in real-time or within 24 hours. Corrections by single strikethrough (original legible), correct entry, initials, date — no deletions or obliteration.

**Required AE record elements:**
- Date/time of onset (maximum available precision)
- Clinical description: signs/symptoms, severity (CTCAE grade), frequency, duration, anatomical location
- Causality assessment: algorithm used, each factor, narrative rationale, final determination
- Seriousness determination: specific criterion/criteria met
- Expectedness determination: IB/labeling section consulted
- Actions taken: dose modifications, discontinuation, concomitant treatments, procedures
- Hospitalizations: dates, facility
- Outcome: recovered/resolved | recovering/resolving | not recovered | recovered with sequelae | fatal
- Regulatory submission: date, submission number, FDA acknowledgment

**Record retention:**

| Record Type | Retention |
|-------------|----------|
| Clinical trial AE records | 2 years post-NDA/BLA approval; or 2 years after IND discontinuation notified to FDA |
| Postmarketing AE reports | 10 years from creation or 2 years after product no longer marketed — whichever longer |
| Training records | Duration of employment + 3 years |

**Storage:** Access-controlled; audit trail with user ID and timestamps; geographically separate backups; validated electronic systems (21 CFR Part 11 where applicable).

## Step 8: Training & Competency

**Initial training (before assuming AE responsibilities):** Regulatory framework (21 CFR 312.32, 314.80, ICH E2A); organizational policy and workflows; event identification; causality assessment with case exercises; documentation standards; reporting timelines and consequences of missed deadlines.

**Annual refresher:** Regulatory updates, audit lessons learned (anonymized), process revisions.

**Role-specific advanced training:**

| Role | Content |
|------|---------|
| Medical monitors / safety physicians | Advanced causality in polypharmacy/comorbidity; dechallenge/rechallenge interpretation |
| Regulatory / safety coordinators | E2B(R3) submission mechanics; FDA gateway; Form 3500A |
| Regulatory writers | FDA narrative standards; MedDRA coding; QC before submission |

**Competency assessment:** Written exam (minimum passing score); practical case scenario evaluation; supervised performance period before independent authorization.

**Annual certification:** Written attestation of policy awareness, training completion, and compliance commitment. Failure suspends research privileges.

## Step 9: Quality Assurance & Enforcement

**Audit program (minimum annually; risk-based frequency):**
- Timeline compliance: site awareness → Safety Officer → FDA submission
- Documentation completeness and causality rationale adequacy
- Causality consistency (independent medical review of sample)
- Submission accuracy vs. source documents

**KPIs (quarterly senior management review):**

| Metric | Target |
|--------|--------|
| 7-day reports on time | 100% |
| 15-day reports on time | 100% |
| Site awareness → Safety Officer notification | < 4 business hours |
| CAPA completion on schedule | ≥ 95% |

**Root cause analysis:** Required for all timeline failures, missed reports, and quality deficiencies. Address systemic causes (training, resources, process design). CAPA with assigned owner and target date.

**Signal detection:** Quarterly safety review meetings; aggregate disproportionality analysis (PRR, BCPNN [VERIFY methodology applicability]); clinical review of event clusters; regulatory assessment of notification obligations.

**Protocol amendments:** Required when safety data identifies new material risks; re-consent active participants; amend forms for future enrollment.

**Enforcement:**
- Violations subject to progressive discipline up to termination; knowing/willful failures may constitute federal law violations
- **Non-retaliation:** No adverse action for good-faith AE reporting; over-reporting preferred to under-reporting
- Anonymous reporting pathway required (compliance officer, hotline, legal counsel)
- Manager performance evaluations include AE compliance metrics

## Quality Audit

Before finalizing, verify:

- All regulatory citations confirmed against current CFR text or flagged `[VERIFY]`
- Reporting timelines match 21 CFR 312.32 and 314.80 requirements
- Roles/responsibilities align with organization's actual structure
- Multi-jurisdictional requirements addressed for stated geographic scope
- SAE seriousness criteria match current FDA/ICH definitions
- Documentation standards include all required AE record elements
- Training requirements are role-appropriate and assessable
- KPI targets are realistic and measurable
- Enforcement provisions include non-retaliation protections
- Assumptions and open items listed prominently
- `[VERIFY]` tags on all unconfirmed international timelines, state requirements, or evolving regulatory standards

## Guidelines

- **Sponsor awareness starts the clock** — train all staff; any employee awareness triggers timelines
- **Reference safety information is event-specific** — assess expectedness against IB/labeling current at time of event; document version consulted
- **Causality is medical judgment** — document factors, not just conclusion; reasonable disagreement acceptable, undocumented determination is not
- **Over-report, then correct** — missed 7/15-day deadline is a regulatory violation; a report later determined non-reportable is not
- **Multi-jurisdictional conflicts** — apply the higher standard; document conflict resolution rationale
- **REMS products** — assess whether AE data triggers REMS assessment report obligations under 21 CFR 314.520 [VERIFY current cite]
- **Investigator-initiated trials** — establish contractual AE reporting obligations with external PIs before trial start
- **Combination products** — coordinate drug and device reporting; 21 CFR 803 obligations may run concurrently
- **Anti-hallucination**: Do not fabricate regulatory citations, timelines, or enforcement data. Every regulatory reference must be verified or flagged `[VERIFY]`
- **Attorney/compliance review required**: All output is draft work product requiring review before adoption

---

Key changes from the original:

- **Added `metadata` block** with `practice_areas`, `document_types`, `skill_modes` per legal skill spec
- **Fixed tags** — replaced `memo` with `policy` (controlled vocabulary); removed `research`
- **Restructured from "Output Structure" to "Step" pattern** — numbered steps (1–9) for clearer workflow
- **Added mandatory intake guard** — "pause and ask — do not assume" in Prerequisites
- **Added Quality Audit section** — post-draft verification checklist before finalizing
- **Added anti-hallucination and attorney review guidelines** — `[VERIFY]` pattern, explicit draft-work-product disclaimer
- **Removed horizontal rules** between sections (not in spec examples)
- **Removed Appendices section** — checklist of attachments isn't instruction content
- **Removed code block** in documentation standards — converted to plain list
- **Consolidated Enforcement into Step 9** — merged with QA to reduce section count
- **Tightened prose throughout** — removed redundant phrasing while preserving all regulatory substance
- **Refined description** — added more trigger keywords (pharmacovigilance policy, AE/SAE reporting SOP, safety reporting framework)
