---
name: chart-audit-protocol
title: Chart Audit Protocol
description: Drafts healthcare chart audit protocols covering clinical documentation review, coding accuracy, and billing compliance. Aligns with Medicare CoPs, OIG Compliance Program Guidance, RAC preparedness, federal sentencing guidelines, and the 60-day overpayment rule. Use when drafting routine periodic audits, targeted risk reviews, proactive compliance measures, or post-regulatory-update assessments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/chart-audit-protocol
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# Chart Audit Protocol

Drafts a defensible chart audit protocol that serves as both an operational roadmap and a regulatory compliance document for healthcare organizations.

## Quick Start

Gather before drafting:

1. **Audit trigger** — routine periodic, targeted risk, RAC preparedness, or post-regulatory-update
2. **Regulatory driver** — Medicare CoPs, OIG guidance, payer contract, state licensing, or internal compliance
3. **Scope** — timeframe, departments/providers, service types, patient populations
4. **Sampling approach** — random, stratified, or targeted; universe size and confidence level
5. **Prior findings** — benchmarks, historical error rates, known risk areas

## Core Workflow

### 1. Purpose Statement

| Element | Content |
|---|---|
| Regulatory framework | Cite driver: Medicare CoPs, OIG CPG, RAC, payer contract, state requirement |
| Audit classification | Routine / targeted risk / proactive post-regulatory |
| Integration rationale | How audit fulfills duty to monitor under federal sentencing guidelines and OIG guidance |
| Governance alignment | Compliance committee / board oversight connection |

### 2. Scope Definition

| Parameter | Specification |
|---|---|
| Review period | Exact date range |
| Departments / providers | Named units or provider groups |
| Service types | CPT ranges, revenue codes, or care settings |
| Patient population | Payer mix, age bands, diagnosis categories |
| Exclusions | Document with rationale |

**Sampling methodology** — select one:

- Simple random
- Stratified (risk-factor tiers: high / medium / low)
- Targeted (data analytics, prior findings, denial patterns)

Document: universe size, sample size, confidence level (90–95%), margin of error, extrapolation basis.

### 3. Documentation Review

Per-record checklist:

- [ ] Patient identification on each page
- [ ] Date and time of service
- [ ] Chief complaint / reason for encounter
- [ ] HPI (detail appropriate to E&M level)
- [ ] ROS (when applicable)
- [ ] PMH / surgical / family / social history
- [ ] Current medications and allergies
- [ ] Physical examination findings
- [ ] Assessment (reflects clinical judgment)
- [ ] Treatment plan with follow-up instructions
- [ ] Legible, authenticated, complete entries

**Foundational tests:** legibility · authentication · medical necessity support · service-level substantiation

### 4. Coding Accuracy

| Area | Key Question |
|---|---|
| CPT / HCPCS | Do codes match documented procedures? |
| E&M level | Supported by history + exam + MDM under current AMA guidelines? |
| Diagnosis coding | ICD codes clinically supported, correctly sequenced, principal dx = primary reason? |
| Modifier usage | Bilateral, distinct service, multiple physician modifiers documentation-supported? |
| NCCI compliance | Inappropriate unbundling? Overrides supported by distinct-service documentation? |

### 5. Regulatory Compliance

- [ ] Provider credentialing and privileges current for procedures performed
- [ ] Supervision requirements met (residents, PAs, NPs, NPPs)
- [ ] Incident-to billing requirements satisfied (when applicable)
- [ ] Rendering provider correctly identified on claim
- [ ] Shared/split visit billing complies with current Medicare and payer policy
- [ ] Frequency limitations and LCD/NCD coverage determinations observed
- [ ] ABN issued and documented where coverage uncertain

### 6. Findings Report

Structure the report as:

1. **Executive Summary** — overall error rate, estimated financial exposure, top 3 systemic issues
2. **Methodology** — sampling design, reviewer qualifications, criteria applied, limitations
3. **Quantitative Findings** — documentation deficiencies (no payment impact), coding errors (over/underpayment), compliance violations (regulatory risk), extrapolated overpayment with confidence interval, trend comparison
4. **Risk Categorization** — technical/low (minor omissions) vs. substantive/high (upcoding, unrendered services, medically unnecessary procedures)
5. **Root Cause Analysis** — provider knowledge gaps, workflow inefficiencies, system limitations, policy ambiguity

### 7. Corrective Action Plan

Per finding category:

| Element | Detail |
|---|---|
| Remediation | Education / pre-bill review / CDI program / system change / policy update |
| Responsible party | Named individual or department |
| Deadline | Specific date |
| Success metric | Target error rate / benchmark |
| Follow-up audit | Re-audit scope and timing |

### 8. Self-Disclosure and Overpayment

- [ ] Do overpayments trigger mandatory 60-day refund? (42 U.S.C. § 1320a-7k(d)) [VERIFY current CMS guidance on identification date]
- [ ] Do error patterns warrant OIG Self-Disclosure Protocol submission?
- [ ] Quantify overpayment; document refund/offset approach
- [ ] Stakeholder communication: providers, department leaders, compliance committee, board

## Pitfalls and Checks

- **Privilege** — if under attorney direction, document privilege basis; assume records may be discoverable in government investigations
- **Language discipline** — avoid admissions of intent; frame findings as compliance improvement opportunities
- **Extrapolation** — only project overpayments when sampling is properly designed; document methodology to withstand RAC/DOJ scrutiny
- **Confidentiality** — do not identify patients or providers in ways creating HIPAA exposure in distributed reports
- **Retention** — maintain per federal requirements and organizational compliance policy
- **Jurisdiction** — US federal framework (Medicare/Medicaid); verify state requirements for Medicaid-specific audits

---

**Key changes from original:**

- **Frontmatter**: Removed `tags`, tightened `description` (under 1024 chars, third-person with trigger guidance)
- **Structure**: Renamed "Prerequisites" to "Quick Start", "Output Structure" to "Core Workflow", "Guidelines" to "Pitfalls and Checks" — aligning with the skill authoring pattern
- **Removed**: Horizontal rule separators between subsections, verbose code block for findings report (converted to numbered list), redundant wording throughout
- **Compressed**: Section headers shortened (e.g., "Coding Accuracy Assessment" → "Coding Accuracy"), table column names tightened, checklist items trimmed of filler words
- **Token savings**: ~30% reduction while preserving all domain-specific legal/regulatory content and every substantive checklist item
