---
name: incident-to-billing-policy
title: Incident-To Billing Policy
description: Drafts Medicare incident-to billing compliance policies for healthcare practices. Covers eligibility criteria, direct supervision, documentation standards, audit programs, and FCA risk mitigation under 42 CFR 410.26, Medicare Benefit Policy Manual Ch. 15 §60.1, and 42 U.S.C. §1395x(s)(2)(A). Use when creating or updating incident-to policies, responding to OIG scrutiny, or establishing NPP billing compliance programs.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/incident-to-billing-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# Incident-To Billing Policy

Drafts a compliance policy governing Medicare incident-to billing — NPP services billed under the supervising physician's NPI at the physician rate. Improper use creates False Claims Act liability, civil monetary penalties, and program exclusion risk.

## Prerequisites

Gather before drafting:

1. **Practice profile** — specialties, locations, states of operation
2. **Provider roster** — supervising physicians and NPPs (NPs, PAs, CNSs) with credentials
3. **Existing policies** — current billing policies, EHR workflows, prior audit findings
4. **State scope-of-practice rules** — per operating state (stricter state rules override Medicare)
5. **Payer scope** — Medicare only or also Medicaid/commercial (rules vary by payer)

## Quick Start

Core question for every encounter: Does this visit meet **all nine** eligibility criteria? If any criterion fails, bill under the NPP's own NPI.

## Policy Drafting Workflow

### 1. Policy Header

Include: effective date, annual review cycle, scope (all clinical/billing staff), and governing authority (42 CFR 410.26; Medicare Benefit Policy Manual Ch. 15 §60.1; 42 U.S.C. §1395x(s)(2)(A)). State that incident-to is a conditional billing privilege with FCA consequences for misuse.

### 2. Key Definitions

| Term | Definition |
|---|---|
| Incident-To Billing | Billing NPP services under supervising physician's NPI at physician rate |
| Direct Supervision | Physician physically present in office suite and immediately available — phone/telehealth does NOT qualify |
| NPP | Non-physician practitioner (NP, PA, CNS, CNM) per Medicare definition |
| Initial Service | First physician evaluation establishing diagnosis and treatment plan |

### 3. Eligibility Criteria (All Required)

- [ ] Physician personally performed the **initial service** for the condition
- [ ] Physician established and documented a **treatment plan**
- [ ] Physician remains **actively involved** in ongoing management
- [ ] Service is a **follow-up** to the plan — not a new problem or diagnosis
- [ ] Supervising physician is **physically present in the office suite**
- [ ] Physician is **immediately available** (not in surgery, off-site, or unreachable)
- [ ] NPP is a **W-2 employee or contractor** of the practice
- [ ] Service is **commonly furnished in a physician office**
- [ ] **State scope-of-practice law** does not impose stricter requirements

**Must bill under NPP's NPI instead when:**
- First visit for any condition (new or established patient)
- New complaint not covered by existing treatment plan
- Physician is off-site, phone-only, or in a procedure unable to respond
- Service type excluded from incident-to (certain preventive services, DME)

### 4. Operational Controls

**Scheduling** — Flag appointments for billing path; confirm physician is on-site that date. Decision flow: treatment plan exists? → physician on-site? → follow-up (not new problem)?

**Day-of supervision** — Physician signs daily attestation log (name, date, location, hours). Retain with billing records.

**Encounter documentation** (each incident-to note must include):
- Reference to physician's original treatment plan (date, diagnosis, plan)
- Confirmation services are consistent with plan
- Supervising physician name and suite presence confirmation

**Billing controls** — Verify supervision log before submitting under physician NPI. EHR/PM system flags: physician not scheduled, new diagnosis code, NPP not credentialed.

### 5. Documentation Retention

Retain all records (physician notes, NPP notes, supervision logs, schedules, billing data) for **10 years** from service or final payment, whichever is later. Training records: employment duration + 6 years. All records retrievable within 48 hours of audit request.

### 6. Compliance Framework

**Governing authorities:**
- 42 U.S.C. §1395x(s)(2)(A) — statutory basis
- 42 CFR 410.26 — implementing regulations
- Medicare Benefit Policy Manual, Ch. 15, §60.1 — operational guidance
- Medicare Claims Processing Manual, Ch. 12 — billing instructions
- False Claims Act, 31 U.S.C. §§3729–3733
- Civil Monetary Penalties Law, 42 U.S.C. §1320a-7a

**Audit program:**
- Quarterly review: minimum 10 claims per NPP per quarter
- Check: supervision documented, treatment plan pre-existed, no new problem, NPP credentialed
- Compare incident-to billing ratios against specialty benchmarks; investigate outliers

**Error correction:**
- Isolated → education, repayment, remediation
- Systemic → corrective action plan, consider OIG Self-Disclosure Protocol (consult compliance counsel)

### 7. Training & Governance

Physicians and NPPs: trained before incident-to participation, annual refresher. Clinical and billing staff: within 30 days of hire, annual refresher. Cover eligibility criteria, supervision definition, documentation requirements, non-compliance consequences.

**Governance roles:** Compliance Officer (policy owner, audit, disclosures), Medical Director (supervision standards), Billing Director (claims controls), Practice Administrator (training, retention). Review policy annually; update within 30 days of regulatory change.

### 8. Appendices Checklist

Include in final document:
- [ ] Daily Physician Supervision Attestation Log template
- [ ] Incident-To Billing Decision Flowchart
- [ ] Pre-Submission Billing Checklist
- [ ] Internal Audit Worksheet
- [ ] State-Specific Scope-of-Practice Addendum (one per state)

## Pitfalls

- Direct supervision = physical presence in suite. Phone/telehealth never qualifies.
- Incident-to does **not** apply in hospital outpatient, SNF, or home settings — scope to office/clinic or address each setting explicitly.
- State law controls when more restrictive — always layer state analysis.
- Never use incident-to for new problems, even in established patients.
- Mark citations with `[VERIFY]` if regulatory currency is uncertain.
- Medicare-only policy unless explicitly extended; Medicaid/commercial rules differ significantly.
- OIG flags incident-to in Work Plans as high-risk; RAC contractors target supervision documentation gaps.

---

**Key changes from original:**

- **Removed `tags` from frontmatter** — not part of the Agent Skills spec
- **Tightened description** — shorter, third-person, with clear trigger guidance
- **Added Quick Start** section for immediate actionability
- **Collapsed verbose sections** — merged Training & Governance into one section; consolidated Documentation Retention from a table into a paragraph; removed the "Course of Treatment" definition (redundant with "Initial Service")
- **Renamed "Guidelines" → "Pitfalls"** — aligns with best-practices structure
- **Removed horizontal rules and "Output Structure" wrapper** — flattened to "Policy Drafting Workflow" with numbered steps
- **Removed enforcement exposure sub-section** — consolidated the key OIG/RAC risk into Pitfalls
- **Reduced from 175 → ~100 lines** — ~43% token savings while preserving all nine eligibility criteria, all legal citations, operational controls, and compliance framework
