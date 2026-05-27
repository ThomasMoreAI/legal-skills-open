---
name: managed-care-contract
title: Managed Care Contract
description: Drafts managed care contracts between MCOs and healthcare providers covering payment methodology (FFS/capitation), credentialing, utilization management, HIPAA compliance, quality assurance (HEDIS/CAHPS), termination, indemnification, and dispute resolution. Ensures compliance with Anti-Kickback Statute, Stark Law, CMS MA/Medicaid guidelines, state insurance laws, and NCQA/URAC standards. Use when establishing provider networks, onboarding providers, updating managed care agreements, or negotiating MCO-provider contracts.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/managed-care-contract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
tags: [agreement, drafting, regulatory]
---

# Managed Care Contract

Drafts the contract governing the legal and operational relationship between a managed care organization (MCO) and a healthcare provider for delivery of services under managed care plans.

## Prerequisites

1. **Party information** — MCO: legal name, entity type, state of incorporation, insurance license number, accreditation (NCQA/URAC/AAAHC). Provider: legal name, entity type, NPI, license numbers, DEA registration, board certifications, practice addresses
2. **Existing agreements** — prior contracts, fee schedules, credentialing materials, provider manual
3. **Payment terms** — FFS rates (% of Medicare or proprietary schedule) or capitation PMPM rates with risk adjustment methodology
4. **Regulatory context** — applicable state managed care statutes; whether contract covers commercial, Medicare Advantage, and/or Medicaid managed care lines of business
5. **Network parameters** — provider participation category (PCP, specialist, hospital, ancillary), geographic service area, panel size limits

## Output Structure

### Article I: Parties & Recitals

| Element | MCO | Provider |
|---|---|---|
| Legal name & DBA | Full name, DBA on member ID cards | Full name, group vs. individual |
| Entity type | State of incorporation | Professional corp, medical group, etc. |
| Identifiers | Tax ID, state insurance license # | Tax ID, NPI, state license #, DEA # |
| Accreditation | NCQA/URAC/AAAHC status | Board certifications, specialties |

- Effective date: execution date, calendar date, or regulatory approval date
- State whether new agreement or amendment/restatement of prior agreement
- Recitals: MCO authority under state insurance law, provider qualifications, mutual intent, regulatory framework

### Article II: Definitions

| Term | Key Elements |
|---|---|
| Covered Services | Enumerated categories; benefit plan reference; prior auth vs. non-auth; conflict hierarchy |
| Capitation | PMPM; scope (global vs. primary care); risk model (full, shared, stop-loss); panel calculation |
| Utilization Review | Prospective, concurrent, retrospective; evidence-based criteria; qualified reviewer; appeal rights |
| Clean Claim | All required data; correct form/format; valid codes; triggers prompt payment clock |
| Member/Enrollee | Subscriber + dependents; eligibility verification method |
| Emergency Services | Prudent layperson standard per federal law; no prior auth required |
| Credentialing | Initial verification + periodic recredentialing of licenses, certifications, training |
| Provider Manual | Incorporated by reference; updatable with reasonable notice |

### Article III: Network Participation & Service Delivery

**Access Standards:**

| Appointment Type | Standard |
|---|---|
| Routine/preventive | Within 4 weeks |
| Urgent/symptomatic | 48–72 hours |
| Emergency | Immediate |
| After-hours | On-call coverage or answering service with triage |

- Define provider participation category, service scope, referral obligations, geographic area, panel limits
- Care coordination: inter-provider communication, referral facilitation, transition coordination

**Credentialing Checklist:**
- [ ] Active, unrestricted state license(s)
- [ ] Board certification (or eligibility with timeline)
- [ ] DEA registration (if prescribing controlled substances)
- [ ] Professional liability insurance: $1M–$3M occurrence / $3M–$5M aggregate; carrier A- or better (A.M. Best); tail coverage if claims-made
- [ ] Notify MCO within 10–30 days of: license restriction/loss, Medicare/Medicaid exclusion, felony conviction, board sanctions, malpractice judgments above threshold

**Clinical Standards:**
- Comply with MCO clinical practice guidelines — guidelines inform but do not override independent medical judgment
- Medical records: HIPAA-compliant; MCO access for UM/QA/audit; retain 6–10 years per state law

### Article IV: Payment & Claims

**Fee-for-Service:**
- Fee schedule as exhibit — specify basis (e.g., "[X]% of Medicare PFS")
- Annual update mechanism: Medicare rate changes, new CPT/HCPCS codes, renegotiated rates

**Capitation:**
- PMPM rates by age band, gender, geography, or HCC risk scores
- Panel assignment: prospective (member selection) vs. retrospective (plurality of care)
- Mid-month enrollment: pro-rated or monthly reconciliation

**Claims Submission:**
- Forms: CMS-1500/837P (professional); UB-04/837I (institutional)
- Timely filing: 90–180 days from date of service (exceptions for retroactive eligibility, COB)

**Payment Timelines:**
- Clean claims paid within 30–45 days per state prompt payment law
- Late payment interest: 10%–18% APR per state statute
- Specify whether additional information requests suspend prompt payment clock

**COB & Adjustments:**
- Provider bills primary payers first (Medicare for dual-eligibles, commercial, auto/workers' comp)
- Recoupment procedures for overpayments, duplicates, ineligible members

**Payment Disputes:**
- Remittance with standard CARC/RARC codes; dispute window 30–90 days
- Escalation: medical director review → executive review → formal dispute resolution
- Address retroactive eligibility termination liability

**Balance Billing:**
- Prohibited for covered services (except copay/coinsurance/deductible)
- Permitted for non-covered services only with advance written member consent

### Article V: Quality Assurance & Utilization Management

**Quality Program:** HEDIS measure reporting; CAHPS survey participation; clinical outcome tracking; peer review under state protection statutes.

**Prior Authorization:** Required for elective inpatient, outpatient surgical, advanced imaging, specialty medications, DME, out-of-network referrals.

| Request Type | Decision Deadline |
|---|---|
| Urgent | 24–72 hours |
| Non-urgent | 14 days (or per state regulation) |

- Denials by physicians/licensed practitioners using MCG, InterQual, or MCO medical policies
- Appeal: 30–60 days to submit; expedited within 72 hours for urgent; external IRO review per ACA/state law
- Provider assumes financial responsibility for services rendered without required prior authorization

**Audits:** On-site with 10–30 days notice; provider cooperates (records, facility, staff); findings may trigger corrective action or recoupment.

### Article VI: Term, Renewal & Termination

**Term:** 1–3 years initial; auto-renewal for 1-year terms unless 90–180 days written non-renewal notice.

**Without Cause:** 90–180 days written notice; MCO notifies affected members.

**For Cause (30 days or immediate):** License loss/suspension; Medicare/Medicaid exclusion (Section 1128 SSA); uncured material breach; fraud/misrepresentation; failure to maintain insurance; felony conviction; conduct threatening member safety.

**Automatic Termination:** Provider death/disability (individual); dissolution/bankruptcy; MCO loss of state insurance license; mutual agreement.

**Post-Termination:**
- Transitional care: 90 days active treatment; through delivery + postpartum; extended for life-threatening conditions
- Claims deadline: 60–90 days post-termination
- Return MCO property; surviving obligations: payment, record retention, PHI confidentiality

### Article VII: HIPAA & Data Protection

- PHI exchange permitted for treatment, payment, healthcare operations without patient authorization; minimum necessary standard applies
- Both parties execute BAAs with subcontractors per HIPAA Omnibus Rule
- Breach notification within 24–72 hours; risk assessment per HIPAA 4-factor test; breaching party bears costs
- Security safeguards: administrative, physical, technical per HIPAA Security Rule; encryption at rest and in transit
- Data retention: 6–10 years per state law; return/destroy PHI on termination (except legally required retention)

### Article VIII: Indemnification & Insurance

**Mutual Indemnification:** Each party indemnifies for its negligence, willful misconduct, breach, or legal violations; includes duty to defend.

**Scope Distinction:**
- Provider: malpractice, negligent treatment, failure to obtain informed consent, improper PHI disclosure — applies even if MCO UM decisions also alleged, provided provider conduct was proximate cause
- MCO: UM decisions, coverage determinations, payment denials, credentialing decisions, network termination

**Insurance Minimums:**

| Party | Coverage | Limits |
|---|---|---|
| Provider (physician) | Professional liability | $1M/$3M (higher for OB, neurosurgery, ortho) |
| Provider (hospital) | Professional + general liability | $10M–$25M+ |
| MCO | General, professional (UM/CM), E&O, cyber | Appropriate to size/scope |

Carrier A- or better; claims-made require tail coverage; MCO as additional insured; insurance minimums do not cap indemnification.

### Article IX: Dispute Resolution

| Step | Timeframe | Process |
|---|---|---|
| Negotiation | 15–30 days | Designated reps with settlement authority |
| Mediation | 30 days (complete within 60) | AAA/JAMS neutral mediator; costs shared |
| Binding Arbitration | If mediation fails | AAA/JAMS rules; healthcare law expertise required |

- Exceptions: injunctive relief for irreparable harm; medical necessity disputes via UM appeals; small claims below threshold
- Governing law: state where provider practices or MCO domicile
- Member rights to external review, regulatory complaints, and court claims preserved regardless of contract ADR

### Article X: General Provisions

- **Amendments:** Written, signed by both authorized representatives
- **Assignment:** Prohibited without consent (not unreasonably withheld); exception for mergers where successor assumes all obligations
- **Notices:** Written; certified mail, overnight courier, or personal delivery
- **Independent Contractor:** No employment, partnership, or agency; each responsible for own employees and taxes
- **Entire Agreement:** Contract + exhibits + provider manual; hierarchy: main contract > exhibits > provider manual
- **Survival:** Indemnification for statute of limitations period; confidentiality 3–5 years; payment until resolved

**Regulatory Compliance:**
- Anti-Kickback Statute (42 U.S.C. § 1320a-7b) [VERIFY]
- Stark Law (42 U.S.C. § 1395nn) [VERIFY]
- False Claims Act (31 U.S.C. §§ 3729–3733) [VERIFY]
- ACA prohibition on provider gag clauses
- State insurance laws (network adequacy, prompt payment, UM, provider termination)

### Execution

- Signature blocks with authority representation; electronic signatures valid per E-SIGN/UETA
- Attach exhibits: fee schedule, covered services list, credentialing requirements, prior authorization forms

## Guidelines

1. **Jurisdiction-specific**: Verify state managed care statutes, prompt payment laws, and insurance filing requirements — timelines and interest rates vary by state
2. **Line of business**: For Medicare Advantage, incorporate 42 CFR Part 422 [VERIFY]; for Medicaid managed care, 42 CFR Part 438 [VERIFY] and state Medicaid agency requirements
3. **Accreditation alignment**: Ensure contract terms satisfy NCQA/URAC standards if MCO holds or seeks accreditation
4. **Anti-Kickback safe harbors**: Structure payment to fit personal services safe harbor (42 CFR § 1001.952(d)) [VERIFY] — fair market value, commercially reasonable, written, specifying services
5. **Do not** include specific payment rates without client instructions — use placeholders
6. **Do not** draft as if representing both parties — maintain drafter's perspective
7. **Balance billing prohibition** must be explicit and unambiguous — required by most state laws and CMS for government programs
8. **Transitional care** obligations are often statutorily mandated — verify minimum periods under applicable state law
