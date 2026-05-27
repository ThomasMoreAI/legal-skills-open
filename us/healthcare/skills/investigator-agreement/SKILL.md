---
name: investigator-agreement
title: Investigator Agreement
description: Drafts Investigator Agreements for FDA-regulated clinical trials between sponsors and principal investigators. Covers 21 CFR Parts 50, 56, 312/812, ICH GCP E6(R2), IRB governance, data integrity, IP, indemnification, financial terms, and termination. Use when preparing clinical trial investigator agreements, site agreements, PI agreements, or sponsor-investigator contracts for drug, biologic, or device studies.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/investigator-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# Investigator Agreement

Drafts a legally enforceable agreement governing the sponsor–principal investigator relationship for FDA-regulated clinical research.

## Prerequisites

Gather before drafting:

1. **Protocol** — number, version, phase, design, investigational product, indication, enrollment target, endpoints, special populations
2. **Parties** — sponsor type (pharma/biotech/device/academic/government), CRO if any, PI credentials, institution legal name and type, governing state
3. **Contracting structure** — PI individually, institution as primary with PI signatory, or joint
4. **Site personnel** — sub-investigators, coordinators, specialists
5. **Prior agreements/templates** — mandatory provisions, indemnification policies, payment processing
6. **Budget** — per-subject, per-procedure, or hybrid; fair market value basis
7. **Single-site vs. multi-center** — affects publication rights, data ownership, oversight

## Quick Start

1. Collect all prerequisites above
2. Draft each section below, adapting to institutional type and study specifics
3. Replace all bracketed `[X]` placeholders with client-specific values
4. Run through the Drafting Checks at the end
5. For detailed regulatory tables and reference material, see [references/REGULATORY.md](references/REGULATORY.md)

## Agreement Sections

### 1. Recitals & Definitions

- Full legal names and roles for all parties
- Define: Protocol, Investigational Product, Study Site, Confidential Information, Study Data, Serious Adverse Event, Effective Date, Study Completion

### 2. Investigator Obligations

Key regulatory obligations to address:

| Obligation | Regulatory Basis | Core Requirement |
|---|---|---|
| Protocol compliance | 21 CFR 312.60 / 812.110 | Absolute; deviations only for immediate hazard; report within 24 hrs |
| Delegation | ICH E6(R2) §4.2 | Signed delegation log; PI retains ultimate responsibility |
| IP accountability | 21 CFR 312.62 / 812.140 | Receipt, storage, dispensing, return/destruction records |
| Informed consent | 21 CFR 50; ICH E6(R2) §4.8 | Written consent before any study procedure; current IRB-approved form |
| Vulnerable populations | 45 CFR 46 Subparts B/C/D | Additional protections; immediate notification for status changes |
| HIPAA | 45 CFR 164 | PHI authorization; coded CRF identifiers; breach reporting |

### 3. IRB Governance

- **Initial submission**: Complete package before any subject contact
- **Continuing review**: Per IRB schedule with enrollment counts, AE summary, deviations
- **Amendments**: IRB + sponsor approval before implementation; exception for immediate hazard (document, notify within 24 hrs)
- **Reporting**: SAEs (unexpected + possibly related), unanticipated problems, deviations increasing risk
- **Lapse**: Cease all activities; exception for enrolled subject safety monitoring
- **Document flow**: IRB submissions/correspondence to sponsor within 5 business days

### 4. Data Integrity & Documentation

- Apply **ALCOA+ principles** (Attributable, Legible, Contemporaneous, Original, Accurate + Available, Consistent, Enduring, Traceable)
- All CRF entries verifiable against source documents
- Corrections: single line-through (paper) or audit trail (EDC); date, initial, reason
- Essential documents per ICH E6(R2) §8 — FDA 1572, financial disclosures, IRB correspondence, signed ICFs, delegation log, IP records, protocol versions, lab certifications
- **Retention**: longest of — 2 years post-marketing approval (or 2 years post-discontinuation + FDA notification), institutional policy, or state law; notify sponsor before destruction

### 5. Adverse Event Reporting

| Category | Timeline | Recipient |
|---|---|---|
| All AEs | Document regardless of severity/causality | Study file |
| SAEs | Within 24 hours of awareness | Sponsor |
| Unanticipated problems involving risk | Per IRB policy | IRB |
| Sponsor safety reports | Review + submit per IRB policy | IRB |

### 6. Monitoring & Inspection

- **Sponsor monitoring**: Business hours; ≥1 week notice (except urgent); direct source document access; PI responds promptly to findings
- **Regulatory inspections**: Notify sponsor within 24 hours of FDA/authority contact; cooperate fully; provide copies of FDA 483, EIR, warning letters within 5 business days
- **Corrective actions**: Collaborative development with sponsor; document implementation

### 7. Confidentiality & IP

- **Scope**: Protocol, IB, CRFs, study data, product formulation, regulatory strategy, all non-public sponsor information
- **Duration**: Study term + [3–5] years post-termination or until publicly available
- **Permitted disclosures**: IRB, regulators, study personnel (bound by equivalent obligations), legal counsel
- **Return/destruction**: Upon request or termination; retain one regulatory copy; certify electronic deletion
- **Data ownership**: Sponsor owns all data, results, discoveries, inventions; survives termination
- **Biological samples**: Sponsor-owned; subject to institutional policies on genetic testing/destruction

### 8. Publication Rights

- Eligible after study completion + database lock + primary analyses
- **Review period**: Submit to sponsor [45–60] days before submission/presentation
- **Sponsor rights**: Remove confidential information; delay [60–90] days for patent filing; request accuracy modifications
- **Anti-suppression**: Sponsor may not suppress legitimate scientific findings; independent expert dispute resolution
- **Authorship**: Per ICMJE guidelines

### 9. Financial Terms

- **Compensation**: Per-subject/per-procedure/hybrid; attach itemized budget as exhibit
- **Fair market value**: Based on time, effort, complexity, qualifications, local rates; Anti-Kickback Statute compliant
- **Invoicing**: [Monthly/quarterly]; payment within [30–45] days of compliant invoice
- **Adjustments**: Screen failures at [specified rate]; early withdrawals pro rata; no payment for unusable data from PI non-compliance
- **Reimbursable costs**: Protocol-required labs/imaging, pharmacy fees, IP storage, subject stipends/travel; pre-approval above [threshold]
- **Financial disclosure**: Per 21 CFR 54 — equity >$50K, prior-year compensation >$25K (excluding study payments), proprietary interests; update during study

### 10. Indemnification & Insurance

**Sponsor indemnifies for**: protocol design, IP formulation/manufacture/defects, product-related injuries when used per protocol.

**Exceptions**: PI negligence/willful misconduct, failure to follow informed consent, unauthorized deviations, agreement breach, regulatory non-compliance.

**Insurance minimums**:

| Party | Per Occurrence | Aggregate |
|---|---|---|
| Sponsor (clinical trial liability) | $[1–5]M | $[2–10]M |
| PI/Institution (professional liability) | $[1–3]M | $[3–5]M |

- Certificates of insurance required; 10-day claims notice; indemnifying party controls defense
- Academic/public institutions typically cannot indemnify — rely on professional liability insurance with specified minimums instead

### 11. Term & Termination

| Trigger | Notice | Effect |
|---|---|---|
| Study completion | N/A | Ends after closeout complete |
| Sponsor convenience | [30–60] days written | Payment through termination + wind-down costs |
| Sponsor for cause | Immediate | May seek damages; may report to FDA/ORI |
| PI — sponsor breach | 30-day cure period | Effective after cure period |
| PI — sponsor insurance lapse | Written notice | Effective upon notice |

**Wind-down**: PI ceases enrollment, notifies subjects, completes CRFs, returns IP/confidential info, submits final IRB report. Sponsor pays for completed services and reasonable wind-down costs.

### 12. Governing Law & Disputes

- Governing law: [Sponsor's state] for contract; site jurisdiction for research conduct/malpractice
- Escalation: project managers → institutional/sponsor executives → mediation (shared costs) → litigation
- Consider arbitration based on party preferences

### 13. Representations & Warranties

- **Sponsor**: Authority to contract; effective IND/IDE; IB contains all known safety information; will maintain insurance; IP manufactured per regulations
- **PI**: Authority to contract; qualified and licensed; disclosed all financial interests; adequate facilities/personnel; not debarred from clinical research
- **Disclaimer**: No implied warranties; investigational product is experimental

### 14. Compliance Provisions

- **Anti-corruption**: FCPA/UK Bribery Act; if PI is government official, institutional compliance review; immediate termination for violation
- **Export controls/sanctions**: PI not on OFAC/SDN lists; no export of IP to restricted parties
- **Healthcare compliance**: Anti-Kickback Statute, False Claims Act, Sunshine Act; compensation = FMV

### 15. Execution & Exhibits

- **Signature blocks**: Authorized institutional official (not just PI) for institutional agreements; PI signature for personal obligations
- **Startup timeline**: Allow [6–12] weeks for institutional review
- **Exhibits**: A: Protocol, B: Budget, C: Personnel List, D: PI CV, E: Financial Disclosures, F: Institutional Policies
- **Amendments**: Material changes require written amendment signed by both parties

## Drafting Checks

- [ ] All `[X]` placeholders replaced with client-specific values
- [ ] Contracting structure and indemnification adapted to institutional type (academic centers typically cannot indemnify)
- [ ] For device studies, 21 CFR 812 substituted for Part 312 references throughout
- [ ] Publication terms include ICMJE-compliant authorship and anti-suppression language
- [ ] Financial terms withstand fair market value scrutiny under Anti-Kickback Statute
- [ ] Multi-center provisions address publication timing and data consistency coordination
- [ ] State-specific requirements checked (informed consent, medical records retention)
- [ ] All regulatory citations verified against current CFR versions
