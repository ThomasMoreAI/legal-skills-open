---
name: privacy-compliance-jpeetz
title: Privacy Compliance Agent Skill
description: Comprehensive global privacy compliance agent skill covering GDPR, CCPA/CPRA, HIPAA Privacy Rule, EU AI Act, LGPD, cross-border data transfer mechanisms (SCCs, BCRs, EU-US DPF), PII identification and classification, data minimization, consent management, privacy-by-design patterns, DPIA workflows, data subject access request (DSAR) handling, and breach notification procedures. Provides procedural knowledge for compliance workflows — NOT legal advice. Designed for agentic platforms including Claude Code, Codex, Cursor, Gemini CLI, OpenClaw, GitHub Copilot, Windsurf, and OpenCode.
author: JPeetz
author_url: https://github.com/JPeetz/agent-skills/tree/main/skills/compliance-legal/privacy-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
tags: [privacy, gdpr, ccpa, hipaa, lgpd, eu-ai-act, dpia, compliance, pii, consent-management, privacy-by-design, dsar, cross-border-transfer, data-minimization]
sources:
- title: Privacy Regulations
  path: references/privacy-regulations.md
---

# Privacy Compliance Agent Skill

> **⚠️ IMPORTANT DISCLAIMER: THIS IS NOT LEGAL ADVICE**
>
> This skill provides **procedural knowledge for compliance workflows** —
> checklists, patterns, reference data, and structured analysis frameworks.
> It does **not** provide legal opinions, interpret statutes, or make
> determinations about legal liability. The information herein is educational
> and procedural only. For legal advice, consult a qualified privacy attorney
> licensed in the relevant jurisdiction.
>
> **Never use this skill to make legally binding determinations.** Its output
> is advisory and should be reviewed by qualified legal counsel before any
> compliance decision is finalized.

---

## Quick Reference

| Regulation | Jurisdiction | Key Focus | Enforcement |
|---|---|---|---|
| **GDPR** | EU/EEA | Personal data protection, consent, rights | Fines up to €20M or 4% global turnover |
| **UK GDPR** | United Kingdom | Post-Brexit equivalent to EU GDPR | Fines up to £17.5M or 4% turnover |
| **CCPA/CPRA** | California, USA | Consumer privacy rights, opt-out of sale | $2,500–$7,500 per intentional violation |
| **HIPAA** | USA (Federal) | Protected Health Information (PHI) | $100–$50,000 per violation, up to $1.5M/year |
| **LGPD** | Brazil | Personal data processing, DPO requirement | Fines up to 2% of Brazilian revenue, max R$50M |
| **EU AI Act** | EU/EEA | AI risk classification, prohibited practices | Fines up to €35M or 7% global turnover |

**Workflow Priority Guide:**

| Role / Request | Start With |
|---|---|
| "We're launching in Europe" | → GDPR Compliance Baseline workflow |
| "We process health data" | → HIPAA Privacy Rule Assessment + PII Classification |
| "Users want to delete their data" | → DSAR Handling Procedure |
| "We're building an AI feature" | → EU AI Act Requirements Analysis |
| "Our database was breached" | → Breach Notification Procedure |
| "We use a US-based cloud provider" | → Cross-Border Data Transfer Mechanisms |
| "Review our consent banner" | → Consent Management Review |
| "New feature design review" | → Privacy-by-Design Architecture Review |

---

## When to Use This Skill

Activate this skill when the user asks you to:

- "Check our GDPR compliance" / "Are we GDPR compliant?" / "GDPR audit"
- "Review our privacy policy" / "Review this consent banner"
- "We need a DPIA" / "Conduct a data protection impact assessment"
- "We had a data breach — what do we do?" / "Breach notification steps"
- "Is this CCPA compliant?" / "California privacy check"
- "Does this handle PHI correctly?" / "HIPAA review"
- "What's the EU AI Act require?" / "AI Act compliance"
- "Can we transfer this data to the US?" / "SCCs / BCRs / DPF"
- "How do we handle a DSAR?" / "Data subject access request procedure"
- "Classify this data" / "Identify PII in this dataset"
- "Review our data minimization" / "Are we collecting too much?"
- "Privacy-by-design review" / "Privacy architecture assessment"
- "LGPD requirements" / "Brazilian data protection"
- "Draft a DPA" / "Data processing agreement template"

### Do NOT Activate For

The following are **near-miss negatives** — they touch on privacy-adjacent topics
but are not privacy compliance workflows:

- **General cybersecurity questions**: "How do I set up a firewall?" — infrastructure security, not privacy compliance. Refer to security skills.
- **Encryption implementation**: "How to encrypt a database column?" — cryptography engineering, not compliance. Refer to coding/security skills.
- **Authentication/authorization design**: "Design an OAuth flow" — IAM, not privacy. Refer to auth/security skills.
- **Legal advice requests**: "Is our company liable under Article 82?" — legal opinion, explicitly out of scope. Recommend consulting an attorney.
- **Contract negotiation**: "Negotiate a data processing agreement" — legal services, out of scope.
- **Regulatory filing**: "File a GDPR registration with the ICO" — administrative filing, out of scope.
- **Litigation support**: "Prepare for a GDPR enforcement hearing" — legal proceedings, out of scope.
- **Pure technical infrastructure**: "Set up a logging pipeline" — DevOps, not privacy (even though logging has privacy implications — redirect to privacy-by-design workflow if the user asks about PII in logs).

When in doubt, ask: "Are you asking me to help with a privacy compliance
workflow (which I can do procedurally), or are you asking for legal advice
(which I cannot provide)?"

---

## Common Pitfalls & Anti-Patterns

### ❌ Compliance Anti-Patterns

1. **Treating compliance as a one-time checkbox** — Compliance is continuous. A DPIA from 2022 is not valid if the processing has changed. Flag outdated assessments.

2. **Confusing "legitimate interest" with "convenient interest"** — Legitimate interest requires a genuine, documented balance test. "We want to monetize data" is not a legitimate interest.

3. **Relying on consent for everything** — Consent is only one of six lawful bases under GDPR. Over-reliance on consent (especially for employment data) is a red flag.

4. **"We'll just anonymize it" without understanding anonymization** — True anonymization is irreversible. Pseudonymization is not anonymization. Mislabeling pseudonymized data as anonymous creates false compliance.

5. **Ignoring data in transit vs. at rest distinction** — Encrypting data at rest but sending it plaintext via email is not compliant. Both must be protected.

6. **Collecting data "just in case"** — "We might need it later" violates data minimization. Every data field must have a documented, current purpose.

7. **Cookie banners that make rejection harder than acceptance** — Dark patterns in consent management are explicitly prohibited under GDPR and are actively enforced by DPAs.

8. **Assuming US-based compliance satisfies EU requirements** — CCPA compliance ≠ GDPR compliance. Different legal bases, different rights, different enforcement.

9. **Treating AI Act compliance as optional for non-AI companies** — The EU AI Act applies to deployers, not just providers. Using a third-party AI system can trigger obligations.

10. **Storing breach response plans only as documents** — A breach response plan that hasn't been tested with a tabletop exercise is not reliable. Flag untested plans.

### ✅ Compliance Quality Checklist

Before publishing your analysis, verify:

- [ ] The specific regulation(s) being assessed are explicitly stated
- [ ] The lawful basis for each processing activity has been identified
- [ ] Data minimization has been evaluated — every field has a purpose
- [ ] Consent mechanisms (if applicable) have been reviewed for validity
- [ ] Cross-border data flows have been mapped and transfer mechanisms identified
- [ ] Data subject rights procedures (access, erasure, portability) have been covered
- [ ] Breach notification timelines per jurisdiction are stated
- [ ] No actual PII was included in the output (see Safety Rules)
- [ ] The disclaimer about this not being legal advice is prominent
- [ ] Any findings have concrete, actionable next steps
- [ ] References to specific regulatory articles are verified against `references/privacy-regulations.md`

---

## Workflows

### Workflow 1: GDPR Compliance Baseline

Use for comprehensive GDPR readiness assessments.

#### Phase 1: Scope Discovery

1. **Identify the data controller and processors.** Who decides the purpose and means of processing? Who processes on behalf of the controller?

2. **Map all personal data flows:**
   - What categories of personal data are collected?
   - From whom? (data subjects, third parties, public sources)
   - For what purpose? (one purpose per data element)
   - Where is it stored? (geographic location of servers/cloud)
   - Who has access? (internal roles, third-party processors)
   - How long is it retained?
   - Where does it flow cross-border?

3. **Identify the lawful basis** for each processing activity:
   - ✓ Consent (freely given, specific, informed, unambiguous)
   - ✓ Contractual necessity
   - ✓ Legal obligation
   - ✓ Vital interests
   - ✓ Public task
   - ✓ Legitimate interests (balance test documented)

   **Critical check:** If processing special category data (Article 9), one of the additional conditions must apply (explicit consent, employment law, vital interests, etc.).

#### Phase 2: Rights & Transparency Review

4. **Privacy notice audit:**
   - Is the privacy notice accessible in plain language?
   - Does it cover: controller identity, purposes, lawful bases, recipients, transfers, retention, and all data subject rights?
   - Is it provided at the point of data collection (not buried)?

5. **Data subject rights verification:**
   - **Right of access (Art. 15):** Is there a documented process for handling access requests? Can you respond within 1 month?
   - **Right to rectification (Art. 16):** Can users correct inaccurate data?
   - **Right to erasure (Art. 17):** Is there a deletion mechanism? Can it cascade to processors?
   - **Right to restriction (Art. 18):** Can you flag and restrict data without deleting it?
   - **Right to data portability (Art. 20):** Can you export data in a structured, machine-readable format?
   - **Right to object (Art. 21):** Can users object to processing (especially direct marketing)?
   - **Automated decision-making (Art. 22):** Are you making decisions with legal/significant effects without human intervention?

#### Phase 3: Technical & Organizational Measures

6. **Security measures assessment:**
   - Encryption at rest and in transit
   - Access controls (least privilege, role-based)
   - Pseudonymization where appropriate
   - Regular testing of security measures
   - Incident response plan

7. **Data Protection Impact Assessment (DPIA) requirement check:**
   A DPIA is required when processing is **"likely to result in high risk"**:
   - Systematic and extensive profiling with legal effects
   - Large-scale processing of special category data
   - Systematic monitoring of publicly accessible areas
   - Processing that involves new technologies at scale

   See **Workflow 2: DPIA Execution** for full procedure.

8. **Data Processing Agreement (DPA) audit:**
   - Do you have DPAs with all processors?
   - Do DPAs include required clauses (Art. 28): subject matter, duration, nature, purpose, type of data, categories of data subjects, controller obligations?
   - Are sub-processors approved and flow-down requirements in place?

#### Phase 4: Breach Preparedness

9. **Breach notification readiness:**
   - Can you detect a personal data breach within 24 hours?
   - Do you have a documented notification procedure?
   - Can you notify the supervisory authority within 72 hours?
   - Can you notify affected data subjects "without undue delay" when there is high risk?
   - See **Workflow 5: Breach Notification Procedure** for full procedure.

#### GDPR Compliance Output Format

```markdown
## GDPR Compliance Assessment

### Scope
- Controller: [entity]
- Processors: [list]
- Processing activities reviewed: N

### Findings

| # | Severity | Finding | Article Reference | Recommendation |
|---|---|---|---|---|
| 1 | 🔴 CRITICAL | No DPIA for high-risk processing | Art. 35 | Execute DPIA immediately |
| 2 | 🟠 HIGH | Consent banner lacks granular opt-out | Art. 7(4) | Redesign consent mechanism |
| 3 | 🟡 MEDIUM | Privacy notice not linked at data collection point | Art. 13 | Add inline privacy notice links |

### Lawful Basis Grid
| Processing Activity | Data Category | Lawful Basis | Special Category? | Condition |
|---|---|---|---|---|
| Account creation | Email, name | Contractual necessity | No | N/A |

### Rights Coverage
| Right | Status | Gap |
|---|---|---|
| Access (Art. 15) | ✅ Implemented | — |
| Erasure (Art. 17) | ⚠️ Partial | No cascade deletion to processor |
| Portability (Art. 20) | ❌ Missing | No export mechanism |

### Recommendation
[Overall assessment with prioritized action items]
```

---

### Workflow 2: DPIA Execution

A Data Protection Impact Assessment is required under GDPR Art. 35 for
processing likely to result in high risk to individuals' rights and freedoms.

#### DPIA Template & Steps

1. **Describe the processing:**
   - Nature: What are you doing with the data?
   - Scope: How much data, how many subjects, how long?
   - Context: What is the relationship with data subjects? Do they expect this?
   - Purposes: Be specific. "Improving user experience" is vague; "Using ML to recommend products based on purchase history" is specific.

2. **Assess necessity and proportionality:**
   - Is the processing necessary to achieve the purpose?
   - Could the purpose be achieved with less intrusive means?
   - Is the data adequate, relevant, and limited (data minimization)?
   - Retention: Is the retention period justified?

3. **Identify and assess risks to individuals:**
   - What could go wrong? (unauthorized access, accidental loss, re-identification)
   - What is the likelihood and severity of harm?
   - Risk matrix: Likelihood × Impact = Risk Level

4. **Identify measures to address risks:**
   - Technical measures (encryption, anonymization, access controls)
   - Organizational measures (staff training, policies, audits)
   - Procedural safeguards (data subject rights procedures)

5. **Record the outcome:**
   - Residual risk after mitigation
   - Whether the residual risk is acceptable
   - Whether prior consultation with the supervisory authority is required (Art. 36)
   - Sign-off from DPO (if appointed)

6. **Integrate outcomes back into the project:**
   - Ensure identified measures are actually implemented
   - Schedule review date (reassess at least every 3 years or when processing changes)

#### DPIA Trigger Checklist

A DPIA is mandatory when the processing involves **two or more** of these indicators (per EDPB guidelines WP 248):

- [ ] Evaluation or scoring (profiling, credit scoring)
- [ ] Automated decision-making with legal or similar significant effect
- [ ] Systematic monitoring (CCTV, employee monitoring, tracking)
- [ ] Sensitive data or highly personal data (special categories, criminal data, financial data)
- [ ] Data processed on a large scale (volume, duration, geographic extent, number of subjects)
- [ ] Matching or combining datasets from different sources
- [ ] Data concerning vulnerable data subjects (children, employees, patients)
- [ ] Innovative use of technological or organizational solutions (AI, IoT, biometrics)
- [ ] Data transfer across borders outside the EU
- [ ] Processing that prevents data subjects from exercising a right or using a service

---

### Workflow 3: DPA Agreement Drafting

Data Processing Agreements (Art. 28 GDPR) are required between controllers
and processors.

#### DPA Required Clauses Checklist

Every DPA must include (Art. 28(3)):

- [ ] **Subject matter and duration** of processing
- [ ] **Nature and purpose** of processing
- [ ] **Type of personal data** and categories of data subjects
- [ ] **Controller obligations and rights**
- [ ] **Processor obligations:**
  - [ ] Process only on documented instructions from controller
  - [ ] Ensure persons authorized to process are under confidentiality
  - [ ] Implement appropriate technical and organizational measures (Art. 32)
  - [ ] Do not engage sub-processors without prior authorization
  - [ ] Assist controller with data subject rights requests
  - [ ] Assist controller with security, breach notification, DPIA
  - [ ] Delete or return all personal data at end of contract
  - [ ] Make available all information to demonstrate compliance
  - [ ] Allow and contribute to audits and inspections
- [ ] **Sub-processor provisions:**
  - [ ] General written authorization requirement
  - [ ] Equivalent data protection obligations flow-down
  - [ ] Processor liability for sub-processor failures
- [ ] **International transfer provisions** (if applicable):
  - [ ] Specify transfer mechanism (SCCs, BCRs, adequacy decision, DPF)
  - [ ] Include supplementary measures if needed
- [ ] **Liability and indemnification** clauses
- [ ] **Termination provisions** (data deletion/return certification)

#### DPA Review Checklist

When reviewing an existing DPA:

1. Is the processor named specifically, or is it a broad "any processor" clause?
2. Are sub-processor approval mechanisms clear (general vs. specific authorization)?
3. Does the DPA cover cross-border transfers if the processor uses non-EU infrastructure?
4. Are security measures specific or just "industry standard" (too vague)?
5. Is there a clear deletion timeline and certification requirement?
6. Does the DPA reference the processor's obligation to notify the controller of breaches?
7. Is there an audit right? Is it practical or illusory?

---

### Workflow 4: CCPA/CPRA Compliance

The California Consumer Privacy Act as amended by the CPRA (effective Jan 1, 2023)
extends GDPR-like rights to California residents.

#### CCPA/CPRA Applicability Threshold

A business must comply if it meets **any one** of these thresholds AND does
business in California:

- Annual gross revenue > $25 million
- Buys, sells, or shares personal information of 100,000+ consumers/households
- Derives 50%+ of annual revenue from selling or sharing personal information

#### Consumer Rights Under CCPA/CPRA

| Right | CCPA Original | CPRA Enhancement |
|---|---|---|
| **Right to Know** | Categories and specific pieces of PI collected | Extended to PI collected beyond 12 months |
| **Right to Delete** | Delete PI collected from consumer | Must notify third parties to delete |
| **Right to Opt-Out** | Opt out of sale of PI | + opt out of sharing for cross-context behavioral advertising |
| **Right to Correct** | — | New: correct inaccurate PI |
| **Right to Limit** | — | New: limit use of sensitive PI |
| **Right to Non-Discrimination** | No discrimination for exercising rights | Strengthened |
| **Right to Data Portability** | Accessible format | Expanded scope |
| **Automated Decision-Making** | — | New: access to info about ADM and opt-out option |

#### CCPA/CPRA Compliance Checklist

1. **Notice at Collection:**
   - [ ] Provided at or before the point of collection
   - [ ] Lists categories of PI collected and purposes
   - [ ] Includes "Do Not Sell/Share My Personal Information" link (if applicable)

2. **Privacy Policy Requirements:**
   - [ ] Categories of PI collected in past 12 months
   - [ ] Categories of sources
   - [ ] Business/commercial purpose for collection
   - [ ] Categories of third parties with whom PI is shared
   - [ ] Consumer rights disclosures
   - [ ] Updated at least every 12 months

3. **Opt-Out Mechanisms:**
   - [ ] "Do Not Sell or Share My Personal Information" link on homepage
   - [ ] Opt-out preference signals honored (GPC — Global Privacy Control)
   - [ ] No re-request to opt-in for 12 months after opt-out
   - [ ] Opt-in consent required for minors 13–16; parental consent <13

4. **Sensitive Personal Information:**
   - [ ] "Limit the Use of My Sensitive Personal Information" link
   - [ ] Opt-in consent for secondary uses of sensitive PI
   - [ ] Sensitive PI categories: SSN, financial account, precise geolocation, race/ethnicity, contents of communications, genetic data, biometric data, health, sex life/orientation

5. **Data Retention:**
   - [ ] Retention periods disclosed
   - [ ] PI not retained longer than reasonably necessary

6. **Contracts:**
   - [ ] Contracts with service providers and contractors include CPRA-required terms
   - [ ] Contracts with third parties for sale/sharing include CPRA terms

7. **Risk Assessments:**
   - [ ] Cybersecurity audits conducted
   - [ ] Risk assessments for processing sensitive PI

8. **Employee Training:**
   - [ ] Staff handling consumer requests are trained
   - [ ] Annual training requirement met

#### CCPA vs GDPR Key Differences

| Aspect | CCPA/CPRA | GDPR |
|---|---|---|
| **Scope** | For-profit businesses meeting thresholds | Any entity processing personal data |
| **Lawful basis** | No lawful basis requirement (rights-based) | Six lawful bases required |
| **Opt-in for sensitive data** | Opt-out default; opt-in for sensitive + minors | Opt-in required for most processing |
| **Private right of action** | Limited to data breaches | Broader damage claims |
| **DPO requirement** | Not required | Required in specific circumstances |
| **DPIAs** | Risk assessments (narrower scope) | DPIAs (broader scope) |
| **Fines** | Statutory damages ($100–$750 per incident) | Administrative fines (up to 4% global turnover) |

---

### Workflow 5: Breach Notification Procedure

#### Multi-Jurisdiction Breach Response

When a personal data breach occurs, different regulations impose different
notification requirements. Time is critical.

#### Step-by-Step Breach Response

1. **Contain and Assess (Immediate — Hour 0):**
   - Contain the breach (revoke access, isolate systems, patch vulnerability)
   - Preserve evidence (logs, access records, system snapshots)
   - Assemble incident response team
   - Document: What happened? What data? How many subjects? What risk level?

2. **Risk Assessment (Hours 0–24):**
   - Classify the breach:
     - **Confidentiality breach:** Unauthorized access/disclosure
     - **Integrity breach:** Unauthorized alteration
     - **Availability breach:** Unauthorized loss/destruction (ransomware can be all three)
   - Assess risk to individuals: likelihood × severity of impact
   - **If no risk to individuals:** Document internally, no notification required
   - **If risk to individuals:** Proceed to notification
   - **If high risk to individuals:** Expedited notification to data subjects

3. **Notification Timelines by Jurisdiction:**

| Jurisdiction | Supervisory Authority | Data Subjects | Trigger |
|---|---|---|---|
| **GDPR** | Within 72 hours of awareness | Without undue delay | Risk to individuals (SA); High risk (subjects) |
| **UK GDPR** | Within 72 hours | Without undue delay | Same as GDPR |
| **CCPA/CPRA** | No SA notification requirement | "In the most expedient time possible, without unreasonable delay" | Unencrypted/unredacted PI breach |
| **HIPAA** | Within 60 days (<500: annual; ≥500: concurrent) | Within 60 days | Breach of unsecured PHI |
| **LGPD** | Within a reasonable time | Must be communicated | Relevant risk or harm |

4. **Notify the Supervisory Authority (as applicable):**
   - **GDPR notification minimum content:**
     - Nature of the breach (categories, approximate number of data subjects and records)
     - DPO contact details
     - Likely consequences
     - Measures taken or proposed (mitigation, prevention)
   - If notification is after 72 hours, include reasons for delay

5. **Notify Data Subjects (as applicable):**
   - Clear, plain language communication
   - Name and contact of DPO
   - Description of likely consequences
   - Measures taken and recommended steps for subjects (e.g., change passwords)
   - Do NOT include: detailed technical forensic data, raw PII of other subjects, speculative causes

6. **Document Everything:**
   - Breach log per Art. 33(5) GDPR: facts, effects, remedial action
   - CCPA: maintain records of breach response for 24 months
   - HIPAA: maintain documentation for 6 years

#### Breach Notification Decision Tree

```
Personal Data Breach Detected
│
├──→ CONTAIN + PRESERVE EVIDENCE (Immediate)
│
├──→ RISK ASSESSMENT
│
├── No risk to individuals?
│   └──→ DOCUMENT internally only. No external notification.
│
├── Risk to individuals?
│   ├── GDPR: Notify SA within 72h ✓
│   ├── UK GDPR: Notify ICO within 72h ✓
│   └── LGPD: Notify ANPD within reasonable time ✓
│
├── High risk to individuals?
│   ├── GDPR: Notify data subjects without undue delay ✓
│   ├── UK GDPR: Same ✓
│   └── CCPA: Notify if unencrypted/unredacted PI ✓
│
├── PHI involved (USA)?
│   └── HIPAA: Notify HHS (60 days), notify individuals (60 days) ✓
│
└──→ DOCUMENT ALL STEPS, DECISIONS, AND TIMELINES
```

---

### Workflow 6: HIPAA Privacy Rule Assessment

The HIPAA Privacy Rule (45 CFR Part 160 and Part 164) protects the privacy of
individually identifiable health information (Protected Health Information / PHI).

#### HIPAA Applicability

**Covered Entities:**
- Health plans (insurers, HMOs, government health programs)
- Health care clearinghouses
- Health care providers who transmit health information electronically

**Business Associates:**
- Entities that create, receive, maintain, or transmit PHI on behalf of covered entities
- Must have Business Associate Agreements (BAAs) in place

#### PHI Identification — The 18 Identifiers

Under HIPAA, PHI is health information that contains **any** of these 18 identifiers:

1. Names
2. Geographic subdivisions smaller than a State
3. Dates (except year) related to an individual
4. Telephone numbers
5. Fax numbers
6. Email addresses
7. Social Security numbers
8. Medical record numbers
9. Health plan beneficiary numbers
10. Account numbers
11. Certificate/license numbers
12. Vehicle identifiers and serial numbers
13. Device identifiers and serial numbers
14. Web URLs
15. IP addresses
16. Biometric identifiers (fingerprints, voice prints)
17. Full-face photographs and comparable images
18. Any other unique identifying number, characteristic, or code

**De-identification safe harbor:** Remove all 18 identifiers + no actual knowledge that remaining information could identify the individual.

#### HIPAA Privacy Rule Assessment Checklist

**1. Notice of Privacy Practices:**
- [ ] Provided to all patients/plan members
- [ ] Acknowledgment of receipt documented (good faith effort)
- [ ] Posted prominently in facility and on website

**2. Uses and Disclosures of PHI:**
- [ ] Permitted uses: Treatment, Payment, Health Care Operations (TPO) — no authorization required
- [ ] Authorization required for: marketing, sale of PHI, psychotherapy notes, research (with exceptions)
- [ ] Minimum necessary standard: Is access limited to the minimum necessary PHI?
- [ ] Facility directories: Patient opt-out honored?
- [ ] Fundraising communications: Opt-out provided?

**3. Individual Rights:**
- [ ] Right to Access: PHI provided within 30 days
- [ ] Right to Amend: Process for requesting corrections
- [ ] Right to Accounting of Disclosures: Records of disclosures (6 years)
- [ ] Right to Request Restrictions: Especially self-pay restrictions
- [ ] Right to Confidential Communications: Alternative contacts honored

**4. Administrative Safeguards:**
- [ ] Privacy Official designated
- [ ] Workforce training (within reasonable time of hire, annually for changes)
- [ ] Sanctions policy for privacy violations
- [ ] Complaint process (no retaliation for filing complaints)
- [ ] Mitigation procedures for breaches
- [ ] Data safeguards (no intimidating/retaliatory acts)

**5. Business Associate Agreements:**
- [ ] BAAs in place with all business associates
- [ ] BAAs require: permitted uses, reporting breaches, subcontractor flow-down, termination provisions

#### HIPAA vs GDPR: Quick Comparison

| Aspect | HIPAA | GDPR |
|---|---|---|
| **Scope** | Health data specific | All personal data |
| **Legal basis for processing** | TPO + authorization | 6 lawful bases |
| **Consent requirement** | Authorization for non-TPO uses | Consent is one of 6 bases |
| **Data subject access** | 30 days (one 30-day extension) | 1 month (two-month extension possible) |
| **Breach threshold** | Compromised unsecured PHI | Any personal data breach with risk |
| **Private right of action** | No | Yes (Art. 82) |

---

### Workflow 7: EU AI Act Requirements

The EU AI Act (Regulation 2024/1689) classifies AI systems into risk
categories and imposes obligations accordingly.

#### AI Act Risk Classification

| Risk Level | Definition | Requirements | Examples |
|---|---|---|---|
| **🔴 Unacceptable** | Prohibited entirely | Cannot be placed on market or used | Social scoring by governments, real-time remote biometric identification in public spaces (with limited exceptions), emotion recognition in workplace/schools, predictive policing based on profiling, untargeted scraping of facial images |
| **🟠 High Risk** | Significant impact on health, safety, fundamental rights | Conformity assessment, risk management, data governance, transparency, human oversight, accuracy, robustness | Medical device AI, recruitment/filtering systems, credit scoring, biometric categorization, critical infrastructure, education/vocational access, law enforcement, migration, justice |
| **🟡 Limited Risk** | Interaction with natural persons | Transparency obligations only | Chatbots (must disclose AI nature), emotion recognition systems, deepfake generation (must label) |
| **⚪ Minimal Risk** | Most AI systems | Voluntary codes of conduct | AI-powered video games, spam filters, inventory management |

#### High-Risk AI System Requirements Checklist

For each requirement, assess the AI system:

1. **Risk Management System (Art. 9):**
   - [ ] Continuous, iterative process throughout lifecycle
   - [ ] Identification of reasonably foreseeable risks
   - [ ] Estimation and evaluation of risks
   - [ ] Adoption of risk management measures
   - [ ] Testing to ensure measures are appropriate

2. **Data Governance (Art. 10):**
   - [ ] Training, validation, and testing datasets meet quality criteria
   - [ ] Data governance practices address: design choices, data collection, preparation, assumptions
   - [ ] Examination for biases that could affect health/safety or fundamental rights
   - [ ] Documentation of datasets used

3. **Technical Documentation (Art. 11):**
   - [ ] General description of the AI system
   - [ ] Detailed description of elements and development process
   - [ ] Monitoring, functioning, and control details
   - [ ] Risk management system description
   - [ ] Any changes to the system documented

4. **Record-Keeping / Logging (Art. 12):**
   - [ ] Automatic logging of events during operation
   - [ ] Logging sufficient for traceability throughout lifecycle

5. **Transparency and Information (Art. 13):**
   - [ ] Clear and adequate information to deployers
   - [ ] Instructions for use including: identity of provider, characteristics/capabilities/limitations, changes, human oversight measures, expected lifetime, and maintenance

6. **Human Oversight (Art. 14):**
   - [ ] Built-in human-machine interface tools
   - [ ] Human overseers can: understand system capacity/limitations, detect automation bias, interpret output correctly, override or disregard output, intervene to stop operation

7. **Accuracy, Robustness, Cybersecurity (Art. 15):**
   - [ ] Appropriate level of accuracy declared
   - [ ] Resilience to errors, faults, inconsistencies
   - [ ] Robustness against manipulation of training data (data poisoning)
   - [ ] Cybersecurity measures against adversarial attacks

#### AI Act Applicability Timeline

| Date | Obligation |
|---|---|
| Feb 2, 2025 | Prohibitions on unacceptable risk AI practices take effect |
| Aug 2, 2025 | GPAI model rules take effect (notifying GPAI with systemic risk, etc.) |
| Aug 2, 2026 | Full AI Act applies (except Art. 6(1) and corresponding obligations) |
| Aug 2, 2027 | Art. 6(1) — classification rules for high-risk AI systems |

#### GPAI (General Purpose AI) Obligations

If using or providing General Purpose AI models:
- [ ] Technical documentation of the model (training, testing, evaluation)
- [ ] Information and documentation to downstream providers
- [ ] Copyright policy and training data summary
- [ ] **Systemic risk GPAI** (trained with >10^25 FLOPs): additional obligations — model evaluations, adversarial testing, incident reporting, cybersecurity

---

### Workflow 8: Cross-Border Data Transfer Mechanisms

International data transfers require specific safeguards. Different mechanisms
apply to different jurisdictions.

#### EU/EEA Transfer Mechanisms

**Adequacy Decisions (Art. 45 GDPR):**
The European Commission has determined these countries provide adequate protection:
Andorra, Argentina, Canada (commercial), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jersey, New Zealand, Republic of Korea, Switzerland, United Kingdom, Uruguay.

**With adequate protection for specific frameworks:** EU-US Data Privacy Framework (certified entities only).

**Without adequacy decision — use these safeguards:**

1. **Standard Contractual Clauses (SCCs):**
   - Modular approach: Controller-to-Controller, Controller-to-Processor, Processor-to-Processor, Processor-to-Controller
   - Must conduct a Transfer Impact Assessment (TIA) before relying on SCCs
   - Cannot be modified (may add supplementary clauses, but cannot contradict SCCs)
   - Most common mechanism for transfers to the US and other non-adequate countries

2. **Binding Corporate Rules (BCRs):**
   - Legally binding internal rules for multinational groups
   - Must be approved by a competent supervisory authority
   - Covers all transfers within the corporate group
   - Complex and time-consuming to establish (6–18 months)
   - Best for large multinationals with frequent intra-group transfers

3. **Derogations (Art. 49 — exceptional use only):**
   - Explicit consent (informed of risks with no adequacy/safeguards)
   - Necessary for contract performance
   - Important reasons of public interest
   - Legal claims
   - Vital interests
   - Public register consultation
   - **Limitation:** Cannot be used for repetitive, systematic transfers

#### Transfer Impact Assessment (TIA) Steps

Per EDPB Recommendations 01/2020 (post-Schrems II):

1. **Map the transfer:** What data, to where, under what mechanism?
2. **Assess the law of the destination country:** Does local law allow authorities access to the data in ways disproportionate to EU standards?
3. **Assess the transfer tool:** Do SCCs provide sufficient protection against the assessed risks?
4. **Identify supplementary measures:** If needed:
   - Technical: End-to-end encryption with key held outside destination jurisdiction, pseudonymization, split processing
   - Organizational: Policies, transparency reports, warrant canary
   - Contractual: Enhanced rights for data subjects
5. **Procedural steps:** Document the TIA, adopt supplementary measures, re-assess periodically
6. **If insufficient protection after supplementary measures:** Suspend or terminate the transfer

#### EU-US Data Privacy Framework (DPF)

- Replaced Privacy Shield (invalidated by Schrems II)
- Adequacy decision adopted July 10, 2023
- **Only available for US entities certified under the DPF**
- Check certification at: https://www.dataprivacyframework.gov/
- Does NOT cover all US companies — only DPF-certified entities
- For non-certified entities: SCCs + TIA still required

#### UK Transfer Mechanisms

The UK has its own adequacy regulations and transfer mechanisms post-Brexit:

- **UK Adequacy Regulations:** Similar list to EU, with some differences
- **UK International Data Transfer Agreement (IDTA):** Replaces EU SCCs for UK-restricted transfers
- **UK Addendum to EU SCCs:** An alternative that adds UK provisions to EU SCCs
- **UK-US Data Bridge:** UK extension of the EU-US DPF (effective October 12, 2023)

#### Cross-Border Transfer Decision Flowchart

```
Is data leaving [jurisdiction]?
│
├──→ NO: No transfer mechanism needed ✓
│
├──→ YES: Is the destination covered by an adequacy decision?
│   ├──→ YES: Transfer proceeds — document adequacy reliance ✓
│   └──→ NO: Proceed to safeguards ↓
│
├──→ Is the recipient DPF-certified (EU→US)?
│   ├──→ YES: Transfer under DPF — document certification ✓
│   └──→ NO: Proceed to SCCs/BCRs ↓
│
├──→ Are SCCs appropriate?
│   ├──→ YES: Execute SCCs + conduct TIA ✓
│   └──→ NO: BCRs for intra-group transfers? ✓
│
├──→ Can a derogation apply (Art. 49)?
│   ├──→ YES: Strictly limited — document justification ⚠️
│   └──→ NO: Transfer cannot proceed ❌
│
└──→ DOCUMENT: TIA, mechanism, supplementary measures, periodic review
```

---

### Workflow 9: PII Identification and Classification

Personally Identifiable Information (PII) is any data that can be used to
identify a specific individual. Different jurisdictions define it differently.

#### PII Classification Taxonomy

| Category | Definition | Examples | Risk Level |
|---|---|---|---|
| **Direct Identifiers** | Uniquely identify an individual without additional data | Full name, SSN, passport number, email address, phone number, biometric data, national ID number | 🔴 HIGH |
| **Indirect Identifiers** | Can identify when combined with other data | Date of birth, postal code, gender, IP address, device ID, cookie ID, vehicle plate number | 🟠 MEDIUM |
| **Sensitive PII** | Special categories with enhanced protection | Race/ethnicity, political opinions, religious beliefs, trade union membership, genetic data, biometric data (for ID), health data, sex life/orientation, criminal records, precise geolocation | 🔴 VERY HIGH |
| **Pseudonymous Data** | PII with identifiers replaced, but re-identifiable with a key | Hashed email, tokenized user ID, pseudonymized medical record | 🟡 MEDIUM (if key is secure) |
| **Anonymous Data** | Irreversibly de-identified — no reasonable means of re-identification | Aggregated statistics, fully anonymized datasets (rare) | ⚪ LOW |
| **Non-PII** | Cannot be used to identify an individual | Aggregated temperature data, anonymous survey responses, page view counts (without identifiers) | ⚪ NONE |

#### PII Detection Framework

When reviewing code, data schemas, or documentation for PII:

1. **Data Inventory Scan:**
   - Search for known PII field patterns: `email`, `phone`, `ssn`, `passport`, `dob`, `birth_date`, `address`, `ip_address`, `device_id`, `biometric`, `health`, `medical`, `national_id`, `tax_id`
   - Search for PII in unstructured data: free-text fields, comments, logs, error messages, debug output
   - Check data at all layers: database schemas, API payloads, log files, analytics events, URL parameters, client-side storage

2. **Context Assessment:**
   - Does the data element alone identify an individual?
   - What happens when combined with other available data?
   - Is the data necessary for the stated purpose?
   - Would a reasonable person consider this data personal?

3. **Data Flow Mapping:**
   - Where does PII enter the system? (User input, API, third-party integration, device sensor)
   - Where is PII stored? (Database, cache, logs, file system, cloud storage)
   - Where does PII travel? (Network calls, API responses, data exports, analytics, emails)
   - Where does PII leave the system? (Third-party integrations, backups, exports, deletions)

4. **Classification Output:**

```markdown
## PII Inventory: [System/Feature Name]

| Field Name | Data Type | PII Category | Sensitivity | Storage Location | Retention | Cross-Border? | Access Control |
|---|---|---|---|---|---|---|---|
| user_email | STRING | Direct Identifier | HIGH | PostgreSQL `users` table | Account lifecycle | No (EU-only) | Role: admin, self |
| ip_address | STRING | Indirect Identifier | MEDIUM | Access logs (S3) | 30 days | No (EU-only) | Role: security_team |
| medical_condition | TEXT | Sensitive PII | VERY HIGH | Encrypted column `health_records` | 10 years (legal req) | No (EU-only) | Role: medical_staff |
```

#### Data Minimization Audit

For each PII field in the inventory, answer:

1. **Purpose:** What specific business purpose does this field serve?
2. **Necessity:** Could this purpose be achieved without collecting this field?
3. **Alternatives:** Could a less identifying alternative serve the same purpose? (e.g., age range instead of DOB, country instead of full address)
4. **Retention:** Is the retention period proportionate to the purpose?
5. **Verdict:** Keep ✓ | Minimize ⚠️ (use alternative) | Remove ❌ (no valid purpose)

---

### Workflow 10: Consent Management Review

Consent under GDPR must be freely given, specific, informed, and unambiguous.
Under CCPA, the focus is on opt-out rights (with opt-in for sensitive data and minors).

#### GDPR Consent Validity Checklist

For each consent collection point, verify:

1. **Freely Given (Art. 7(4)):**
   - [ ] Is consent optional — not a condition of service unless strictly necessary?
   - [ ] Can the user decline without negative consequences? (No cookie walls, no degradation)
   - [ ] Is there no power imbalance? (Employment consent requires extra scrutiny)
   - [ ] Is consent granular — separate for different purposes?

2. **Specific (Art. 6(1)(a), Recital 32):**
   - [ ] Each purpose has its own consent option
   - [ ] No bundled consent ("by signing up you agree to marketing + analytics + sharing")
   - [ ] Purposes are described specifically, not vaguely ("improve services" is too vague)

3. **Informed (Art. 7(2), Art. 13):**
   - [ ] Controller identity is stated
   - [ ] Each purpose is explained in plain language
   - [ ] Third-party data recipients are identified (by name or category)
   - [ ] Data retention periods are disclosed
   - [ ] Data subject rights are explained
   - [ ] Cross-border transfers (if any) are disclosed

4. **Unambiguous (Art. 4(11), Recital 32):**
   - [ ] Affirmative action required (pre-ticked boxes are invalid under GDPR)
   - [ ] Clear "Accept" / "Reject" options (equal prominence)
   - [ ] Silence or inactivity is NOT consent
   - [ ] Consent is demonstrable — records kept

5. **Easily Withdrawn (Art. 7(3)):**
   - [ ] Withdrawing consent is as easy as giving it
   - [ ] Consent withdrawal mechanism is accessible (not buried in account settings)
   - [ ] User is informed of the right to withdraw before giving consent

#### Consent Dark Pattern Detection

Flag these anti-patterns:

| Dark Pattern | Description | Regulation Violated |
|---|---|---|
| **Cookie walls** | Access to content conditional on accepting all cookies | GDPR (free consent), CNIL guidelines |
| **Deceptive button hierarchy** | "Accept All" is prominent; "Reject All" is a tiny link | GDPR (equal prominence) |
| **Pre-ticked boxes** | Consent pre-selected | GDPR Art. 4(11), 7 |
| **Legitimate interest bypass** | Cookies set under "legitimate interest" with no opt-out | GDPR (must be genuine LI, must offer opt-out) |
| **Repeated consent requests** | Nagging user who rejected until they accept | GDPR (harassment undermines free consent) |
| **Hidden reject** | "Manage settings" requires multiple clicks to reject all | GDPR, ePrivacy Directive |
| **Time pressure** | "Offer expires in 5 minutes — accept now!" | GDPR (free consent — coercion) |
| **Confusing language** | Legalese or deliberately misleading descriptions | GDPR Art. 7(2) (clear and plain language) |

#### Consent Record-Keeping

Per Art. 7(1), the controller must demonstrate that consent was obtained.
Records should include:

- **Who:** Identity of the data subject (or unique identifier)
- **When:** Timestamp of consent
- **What:** The specific consent text/statement shown at the time
- **How:** Method of consent (checkbox, button, signature)
- **Context:** Which page/form, what was presented
- **Scope:** Specific purposes consented to
- **Version:** Privacy notice/consent form version

---

### Workflow 11: Privacy-by-Design Architecture Review

Privacy-by-design means embedding data protection into the system architecture
from the ground up, not bolting it on afterward (Art. 25 GDPR).

#### Privacy-by-Design Principles

1. **Proactive, not reactive — Preventative, not remedial**
2. **Privacy as the default setting** — No action required to protect privacy
3. **Privacy embedded into design** — Integral part of the system
4. **Full functionality — positive-sum, not zero-sum** — Privacy AND utility
5. **End-to-end security — full lifecycle protection**
6. **Visibility and transparency** — Keep it open to data subjects
7. **Respect for user privacy** — Keep it user-centric

#### Architecture Review Dimensions

**1. Data Collection Layer:**
- [ ] Are data fields explicitly enumerated? No catch-all "additional info" fields.
- [ ] Is collection minimized to what's strictly necessary?
- [ ] Are defaults privacy-preserving? (Opt-out by default, minimal data sharing)
- [ ] Is sensitive data collection flagged for special handling?
- [ ] Are data collection points documented with purpose specifications?

**2. Data Storage Layer:**
- [ ] Is PII encrypted at rest? (AES-256 minimum for PII, separate key management)
- [ ] Is PII stored separately from non-PII? (segregation of sensitive data)
- [ ] Are database backups encrypted and access-controlled?
- [ ] Is data pseudonymized/anonymized where possible?
- [ ] Is there a clear data retention and automated deletion mechanism?
- [ ] Is test data sanitized? No production PII in dev/staging environments.

**3. Data Processing Layer:**
- [ ] Is processing limited to documented purposes? (purpose limitation)
- [ ] Are processors identified and DPAs in place?
- [ ] Is access control enforced at the application layer (not just database)?
- [ ] Are there audit logs for all PII access?
- [ ] Is PII minimized in memory (not cached unnecessarily)?
- [ ] Is PII excluded from error messages and debug logs?

**4. Data Transmission Layer:**
- [ ] Is TLS 1.2+ enforced for all data in transit?
- [ ] Are API responses filtered to exclude unnecessary PII fields?
- [ ] Is PII excluded from URL query parameters?
- [ ] Are third-party integrations reviewed for PII transmission?
- [ ] Is client-side storage of PII (localStorage, cookies) reviewed and justified?

**5. User-Facing Layer:**
- [ ] Is the privacy notice accessible at the point of data collection?
- [ ] Are consent mechanisms compliant (per Consent Management Review workflow)?
- [ ] Are DSAR self-service tools available (data download, account deletion)?
- [ ] Is PII masked or hidden by default in UI (e.g., masked email in user lists)?
- [ ] Are third-party trackers disclosed and consented to?

**6. Operational Layer:**
- [ ] Is employee access to PII on a need-to-know basis?
- [ ] Are access reviews conducted regularly?
- [ ] Is there a data breach detection mechanism in place?
- [ ] Is there a documented breach response plan?
- [ ] Are third-party vendor privacy practices assessed?
- [ ] Is privacy training documented for all relevant personnel?

#### Privacy-by-Design Pattern Library

| Pattern | Description | When to Use |
|---|---|---|
| **Data Minimization by Design** | Collect only what's needed, when it's needed, for as long as needed | Default for all new development |
| **Purpose-Based Access Control** | Access controls tied to specific processing purposes, not just roles | Multi-purpose systems |
| **Just-in-Time Consent** | Request consent at the moment of data collection, not at signup | Features collecting sensitive data |
| **Client-Side Processing** | Process data on-device, never transmit raw PII to server | Analytics, personalization |
| **Differential Privacy** | Add calibrated noise to aggregate outputs to protect individuals | Analytics, ML training |
| **Encrypted Processing** | Homomorphic encryption, secure enclaves for processing sensitive data | Highly sensitive data processing |
| **Data Tokenization** | Replace PII with tokens, store mapping separately | Payment systems, multi-system integrations |
| **Automated Data Lifecycle** | Cron-driven deletion of expired data per retention policy | All PII storage |
| **Privacy-Preserving Analytics** | Aggregate-only analytics, no per-user tracking | Web analytics, product metrics |

---

### Workflow 12: Data Subject Access Request (DSAR) Handling

#### Multi-Regulation DSAR Rights Summary

| Right | GDPR | CCPA/CPRA | HIPAA | LGPD |
|---|---|---|---|---|
| **Access** | Art. 15 — Confirm processing + copy of data | Right to Know — categories + specific pieces | Right to Access — designated record set | Art. 18 — Confirmation + access |
| **Rectification** | Art. 16 | Right to Correct (CPRA) | Right to Amend | Art. 18 |
| **Erasure** | Art. 17 — "Right to be forgotten" | Right to Delete | Limited (amendment preferred) | Art. 18 |
| **Portability** | Art. 20 | Right to Data Portability (CPRA) | Right to Direct to Third Party | Art. 18 |
| **Restriction** | Art. 18 | — | Right to Request Restrictions | Blocking (Art. 18 §6) |
| **Objection** | Art. 21 — Object to processing | Opt-Out of Sale/Sharing | — | Opposition (Art. 18 §2) |
| **Automated Decisions** | Art. 22 — Human review of ADM | CPRA: Access + opt-out option | — | Review of ADM (Art. 20) |

#### DSAR Handling Procedure

**Phase 1: Receipt & Validation (Day 1–5)**

1. **Log the request** — timestamp, channel (email, web form, phone, mail), request type
2. **Verify the requester's identity:**
   - Authenticated user in your system → verify session/account ownership
   - Non-authenticated user → request additional verification (ID document, email verification)
   - **Be cautious:** Do not request excessive ID verification (disproportionate under GDPR)
3. **Clarify the scope** — What specifically is the user requesting? All data? Specific processing? Deletion of specific data?
4. **Confirm the request is valid** — Is it excessive or manifestly unfounded? (If so, you may charge a reasonable fee or refuse — but document the justification)

**Phase 2: Data Collection (Day 5–15)**

5. **Identify all data stores:**
   - Primary databases (user tables, profile stores)
   - Analytics systems (Mixpanel, Amplitude, etc.)
   - Customer support systems (Zendesk, Intercom)
   - Marketing systems (email platforms, CRM)
   - Logs and backups (may be impractical — document)
   - Third-party processors (must assist per DPA)

6. **Collect and collate the data:**
   - Export in structured, machine-readable format (JSON, CSV)
   - Include metadata: source, purpose of processing, recipients, retention period
   - Redact third-party PII (do not disclose another person's data)
   - Translate codes/IDs where necessary (user ID → meaningful context)

**Phase 3: Review & Redaction**

7. **Before releasing, review for:**
   - Third-party personal data (must not be disclosed)
   - Legally privileged information
   - Confidential commercial information (trade secrets)
   - Information that would adversely affect the rights and freedoms of others
   - Security-sensitive information (internal security procedures)

8. **Document your redactions** — What was redacted, why, under what legal basis.

**Phase 4: Response (by Day 30)**

9. **Provide the response:**
   - **Access request:** Copy of all personal data + Art. 15(1) and (2) information (purposes, categories, recipients, retention, rights, source, automated decision-making)
   - **Erasure request:** Confirmation of deletion + scope of what was deleted + where deletion might be incomplete (backups, legal holds) + timeline for completion
   - **Portability request:** Data in structured, commonly used, machine-readable format

10. **Timeline management:**
    - GDPR: Respond within 1 month (can extend by 2 months for complex requests — notify within first month)
    - CCPA: Respond within 45 days (can extend by 45 days — notify within first 45 days)
    - HIPAA: Respond within 30 days (one 30-day extension)
    - LGPD: Within 15 days (confirmation of processing), rest within reasonable time

**Phase 5: Closure & Documentation**

11. **Document everything:**
    - Request log (date, type, requester, scope)
    - Identity verification method
    - Data sources searched
    - Redactions and justifications
    - Response provided and date
    - Any extensions and justifications
    - Time to complete

12. **Metrics tracking (for accountability):**
    - Number of DSARs received per month
    - Average response time
    - Most common request types
    - Extension rate (should be low)

#### DSAR Refusal Grounds

Valid grounds to refuse or charge a fee (document thoroughly):

| Ground | GDPR | CCPA |
|---|---|---|
| Manifestly unfounded | Art. 12(5) — refuse or charge | Must respond (no unfounded exception for access) |
| Excessive (repetitive) | Art. 12(5) — refuse or charge | 2 requests per 12 months; charge for additional |
| Cannot verify identity | Art. 12(6) — can refuse until verified | Can refuse if cannot verify |
| Adversely affects rights of others | Art. 15(4) — can refuse/redact | Must provide (redact third-party PI) |
| Legal privilege | Recital 73 | Attorney-client privilege |

---

## Safety Rules

**ABSOLUTE RULES — never violate these:**

1. **Never expose actual PII in outputs.** When referencing data in examples,
   use synthetic, obviously fake values (e.g., `user@example.com`,
   `John Doe`, `123-45-6789 (synthetic)`). Never echo real PII from the
   user's systems. If real PII appears in your analysis context, redact it.

2. **This is NOT legal advice. Ever.** Do not offer legal opinions, interpret
   statutes authoritatively, or tell users whether they are "compliant" or
   "non-compliant." Say: "This analysis identifies areas that should be
   reviewed by qualified legal counsel." Frame findings as "This may not
   meet [regulation] requirements" not "You are in violation of [regulation]."

3. **Do not draft legal documents for execution.** You can provide templates
   and checklists, but flag that every DPA, privacy notice, and consent
   form must be reviewed by legal counsel before use. Do not present
   templates as "ready to sign."

4. **Do not make determinations about fines or penalties.** You can cite the
   regulatory maximums, but do not estimate or predict an organization's
   financial exposure. That requires legal analysis by a qualified attorney.

5. **Acknowledge jurisdictional complexity.** Privacy law is fragmented.
   What satisfies the CCPA may not satisfy the GDPR, and vice versa. Always
   identify which jurisdiction(s) apply and note conflicts between regimes.

6. **Respect the limits of the skill.** This skill covers GDPR, CCPA/CPRA,
   HIPAA, LGPD, and the EU AI Act. If the user asks about regulations not
   covered here (e.g., PIPEDA, POPIA, China's PIPL), state that the skill
   does not cover that regulation and recommend consulting subject-matter
   expertise.

7. **Be transparent about model limitations.** AI can process procedural
   checklists but cannot exercise legal judgment. Say: "This is a procedural
   analysis based on my training data. Regulatory interpretations evolve
   through guidance and case law. Always verify with current regulatory
   guidance and qualified legal counsel."

8. **Never recommend avoiding or circumventing regulations.** If a user asks
   "How can we avoid GDPR by moving servers to country X?", do not provide
   a workaround. Explain that territorial scope is determined by the data
   subject's location and the targeting of the EU market, not server location.

---

## Platform Compatibility Notes

| Platform | Notes |
|---|---|
| **Claude Code** | Use for document review and checklist generation. Works well with files in workspace. Use web search for current regulatory guidance. |
| **Codex (OpenAI)** | Strong at structured analysis. Provide clear workflow selection. Good for DPIA templates and gap analysis. |
| **Cursor** | Can read codebases for privacy-by-design reviews. Use to scan for PII in database schemas, API definitions, and code. |
| **Gemini CLI** | Large context for processing privacy policies and DPAs. Use for multi-document analysis. |
| **OpenClaw** | Full workflow execution. Use `exec` for regex PII scanning. Use web search for regulatory updates. Compatible with all referenced workflows. |
| **GitHub Copilot** | Best for inline privacy-by-design suggestions. Flag PII patterns in code as they're written. |
| **Windsurf** | Can scan entire codebase for PII and compliance gaps. Use for architecture reviews. |
| **OpenCode** | Terminal-based. Use for quick PII scans and checklist generation. |

### Platform-Specific Adjustments

- **For Discord/Slack delivery:** Use bullet lists, not markdown tables.
  Wrap multiple links in `<>` to suppress embeds. Keep findings concise.
- **For web search access:** Verify current regulatory guidance. DPAs issue
  new guidance frequently. Check `references/privacy-regulations.md` for
  baseline knowledge, then supplement with web search for recent updates.
- **If output length is limited:** Prioritize CRITICAL and HIGH findings.
  Reference workflows by name rather than embedding full procedure text.
- **For codebase scanning:** Use regex patterns from Workflow 9 (PII
  Identification). Focus on `email`, `phone`, `ssn`, `health`, `biometric`,
  `address` field patterns.

---

## References

- `references/privacy-regulations.md` — Quick-reference guide to major privacy regulations, key articles, enforcement bodies, and fine structures.
- External:
  - [GDPR Full Text](https://gdpr-info.eu/) — Official GDPR text with article navigation
  - [EDPB Guidelines](https://edpb.europa.eu/our-work-tools/general-guidance/gdpr-guidelines-recommendations-best-practices_en) — Official EDPB guidance
  - [ICO Guidance (UK)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/) — UK ICO guidance
  - [CPPA Regulations](https://cppa.ca.gov/regulations/) — California Privacy Protection Agency
  - [HHS HIPAA for Professionals](https://www.hhs.gov/hipaa/for-professionals/index.html) — HIPAA Privacy Rule guidance
  - [EU AI Act](https://artificialintelligenceact.eu/) — EU AI Act text and resources
  - [EU-US DPF](https://www.dataprivacyframework.gov/) — Official DPF list and certification verification
  - [EDPB Recommendations 01/2020](https://edpb.europa.eu/our-work-tools/our-documents/recommendations/recommendations-012020-measures-supplement-transfer_en) — Supplementary measures for cross-border transfers
  - [LGPD English Translation](https://iapp.org/resources/article/brazils-general-data-protection-law-official-english-translation/) — IAPP translation of Brazil's LGPD
