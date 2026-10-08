---
name: review-gdpr-readiness-sboghossian
title: GDPR Readiness Review
description: Use when an organization needs a structured GDPR readiness review across the 10 core compliance areas — lawful basis documentation, privacy notice, consent mechanism, Article 30 records of processing, DPIAs, DPO appointment, DSR handling, 72-hour breach notification, international transfer mechanisms, and vendor/processor management. Produces a traffic-light maturity score per area with findings and prioritized recommendations. Relevant for any organization that processes EU personal data, including MENA companies with EU operations or EU customer data flows.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-gdpr-readiness
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR Readiness Review

Structured assessment of an organization's compliance with the General Data Protection Regulation (GDPR) — Regulation (EU) 2016/679 — across the 10 core compliance areas. Applicable to any organization that processes the personal data of EU data subjects, regardless of where the organization is located. For MENA companies, GDPR triggers when EU-based employees, customers, or data subjects are involved.

## When to use this

- Pre-audit preparation: before an internal or external GDPR audit
- Gap assessment: a new business activity is being launched and needs a data-protection review
- Incident post-mortem: a personal data incident has occurred and the organization needs to assess its GDPR position
- M&A due diligence: acquiring a company with EU personal data processing
- Regulatory examination preparation: a supervisory authority (DPA) has initiated an inquiry
- For MENA companies: when processing EU employee data, EU customer data, or data subject to EU adequacy mechanisms

## GDPR applicability to MENA organizations

GDPR applies (Article 3) to:
- Any organization **established** in the EU
- Any organization **not in the EU** that: (a) offers goods or services to EU data subjects, or (b) monitors the behavior of EU data subjects

**MENA implications**: a UAE fintech with EU customers is subject to GDPR. A KSA company employing EU national employees who are subject to EU data protection is subject to GDPR for that processing. An MENA company that receives EU personal data from an EU group parent (intra-group data flows) is subject to GDPR transfer requirements.

## Inputs

| Input | Why it matters |
|-------|---------------|
| Organization description (sector, size, geographic scope) | Determines which GDPR obligations apply at what level (SME exemptions, DPO trigger thresholds) |
| Data flows inventory | What is collected, from whom, for what purpose, where stored, who has access — the foundation of all GDPR compliance |
| Existing policies (privacy notice, retention, security) | Baseline for gap assessment |
| Vendor / processor list | Subprocessors must be identified; DPAs must exist |
| Breach history | Prior incidents reveal process gaps |

If the user provides limited information, the review proceeds as a hypothetical gap assessment (flagging areas of risk) rather than a verified audit.

## Review framework — 10 areas

### Area 1: Lawful Basis

**GDPR requirement**: every processing activity must have a documented lawful basis (Article 6). The six bases: consent; contract performance; legal obligation; vital interests; public task; legitimate interests.

**Review questions**:
- Is there a record mapping each processing activity to its lawful basis?
- For legitimate interests: has a Legitimate Interests Assessment (LIA) been completed?
- For consent: is consent freely given, specific, informed, unambiguous, and withdrawable?
- Are special-category data (health, biometric, religious, political) handled with an Article 9 basis?

**Common MENA gap**: reliance on consent as the sole lawful basis for employee data processing — employee consent is generally not "freely given" under GDPR because of the power imbalance; contract or legal obligation is the appropriate basis for most HR data processing.

### Area 2: Privacy Notice

**GDPR requirement**: Articles 13–14 require privacy information to be provided at or before data collection, covering: controller identity; purposes; legal bases; retention periods; data subject rights; right to complain to a DPA; details of third-party sharing; international transfer safeguards.

**Review questions**:
- Does a privacy notice exist and is it accessible to data subjects at the point of collection?
- Is it written in plain language (not legal jargon)?
- Does it cover all purposes for which data is processed?
- Is there a separate internal privacy notice for employees?
- When was it last updated? (Laws, EDPB guidance, and business activities change)

### Area 3: Consent Mechanism

**Review questions**:
- Where consent is the lawful basis, is it obtained by affirmative action (no pre-ticked boxes)?
- Is consent granular — can data subjects consent to some purposes but not others?
- Can consent be withdrawn as easily as given?
- Is there a record of when consent was obtained and what the data subject consented to?
- For cookies and tracking: does the website / app use a consent management platform (CMP) with a proper opt-in mechanism?

### Area 4: Records of Processing (Article 30)

**GDPR requirement**: controllers with 250+ employees (and smaller controllers in certain circumstances) must maintain a Record of Processing Activities (ROPA) — a written inventory of all processing activities.

**Review questions**:
- Does a ROPA exist? Is it up to date?
- Does it cover: purposes, categories of data, data subjects, recipients, retention periods, international transfers, security measures?
- Is it maintained centrally or distributed?
- SME exemption: organizations with < 250 employees are partially exempt but should maintain records for high-risk processing

### Area 5: Data Protection Impact Assessments (DPIAs)

**GDPR requirement**: Article 35 requires a DPIA before "high-risk processing" — large-scale special-category data; systematic monitoring; automated decision-making with significant effect; new technologies.

**Review questions**:
- Is there a DPIA policy defining the trigger threshold?
- Have DPIAs been completed for high-risk processing activities?
- If a DPIA revealed a high residual risk, was the relevant DPA consulted (Article 36)?
- EDPB guidance lists 9 criteria for "high risk" — is the organization aware of these?

### Area 6: Data Protection Officer (DPO)

**GDPR requirement**: Article 37 requires a DPO for: (a) public authorities; (b) organizations whose core activities require large-scale systematic monitoring of data subjects; (c) organizations whose core activities involve large-scale processing of special-category data.

**Review questions**:
- Has the organization assessed whether a DPO is required?
- If required and appointed: is the DPO independent? Are they resourced adequately? Are they integrated into decision-making processes?
- If not required: has that assessment been documented?
- DPO contact details: published on the privacy notice and registered with the relevant DPA?

### Area 7: Data Subject Rights (DSR) Handling

**GDPR requirements**: data subjects have the right to access (Art. 15), rectification (Art. 16), erasure (Art. 17), restriction (Art. 18), portability (Art. 20), objection (Art. 21), and not to be subject to automated decisions (Art. 22). All must generally be responded to within **1 calendar month** (extendable by 2 months for complex requests, with notice).

**Review questions**:
- Is there a documented process for receiving and triaging DSR requests?
- Can the organization fulfill access requests (identify all data held about a data subject) within 1 month?
- Is there a process for erasure requests that also deletes data held by processors and subprocessors?
- Are requests responded to in the correct format (electronic if requested electronically)?
- Is there a log of DSRs received and how they were handled?

### Area 8: Breach Response (72-hour notification)

**GDPR requirement**: Article 33 requires notification to the supervisory DPA within **72 hours** of becoming aware of a personal data breach (unless the breach is unlikely to result in risk to individuals). Article 34 requires notification to affected data subjects "without undue delay" for high-risk breaches.

**Review questions**:
- Is there a written incident response plan that covers personal data breaches?
- Does the organization have the technical capability to detect breaches within the 72-hour window?
- Is the relevant DPA's breach notification portal known and tested?
- Is there a breach log (records of all breaches, even those not notified, are required under Article 33(5))?
- Post-breach review process: are lessons learned and controls improved?

**MENA organizations**: for a company with no EU establishment, the "lead supervisory authority" under GDPR's one-stop-shop mechanism may not apply; the relevant DPA is that of the EU member state where the breach affects data subjects.

### Area 9: International Transfers

**GDPR requirement**: Articles 44–49 restrict transfers of EU personal data outside the EEA to third countries (including UAE, KSA, Lebanon) unless a transfer mechanism is in place:
- **Adequacy decision**: the destination country has GDPR-equivalent protections (UK, Japan, Israel, Canada (commercial) have adequacy; UAE, KSA, Lebanon do not)
- **Standard Contractual Clauses (SCCs)**: EU Commission approved SCCs (new 2021 versions); must be supplemented with a Transfer Impact Assessment (TIA) for high-risk destinations
- **Binding Corporate Rules (BCRs)**: for intra-group transfers in large multinationals; requires DPA approval
- **Derogations** (Art. 49): limited use cases (explicit consent, contract performance, legal claims, vital interests)

**MENA-specific**: UAE, KSA, and Lebanon are not adequacy-list countries. EU-to-UAE and EU-to-KSA transfers require SCCs + TIA. The UAE PDPL (2021) and KSA PDPL (2021) are new and their implementation is still developing; SCCs remain the standard mechanism.

### Area 10: Vendor / Processor Management

**GDPR requirement**: controllers must use only processors that provide sufficient guarantees (Article 28). A Data Processing Agreement (DPA) must be in place with all processors. Sub-processors: the DPA must specify whether the processor can engage sub-processors and the sub-processor approval mechanism.

**Review questions**:
- Is there a vendor inventory listing all processors and sub-processors?
- Does every processor have a signed DPA (Article 28 compliant)?
- Do DPAs contain all required terms: processing instructions, security measures, sub-processor approval, breach notification, audit rights, deletion/return of data on termination?
- For cloud providers (AWS, Azure, Google Cloud): are the standard DPAs adequate, or do they need supplemental terms for GDPR compliance?
- Is there a process for approving new sub-processors?

## Output format

### Per area assessment

For each of the 10 areas:

```
## Area [N]: [Name]

Status: 🟢 Compliant | 🟡 Partially Compliant | 🔴 Non-Compliant | ⚪ Not Assessed

Findings:
- [Specific finding 1]
- [Specific finding 2]

Recommendations:
- [Specific action to achieve compliance]

Timeline: [30 days / 90 days / next cycle]
```

### Maturity score

```
Overall GDPR Readiness: [X/10 areas at 🟢]

🟢 Compliant areas: [list]
🟡 Partially compliant areas: [list]
🔴 Non-compliant areas: [list]

Priority actions (next 30 days): [top 3 red items]
```

### Risk prioritization

- 🔴 = Active regulatory and reputational risk; remediate within 30 days; consider self-reporting to DPA if a breach has already occurred and notification was missed
- 🟡 = Improvement needed; 90-day remediation plan; document the gap and your plan to close it
- 🟢 = Maintain and monitor; confirm during next annual review

## Limits and escalation

- This skill reviews against the GDPR standard; it does not review compliance with national GDPR implementing legislation, which may add requirements (e.g., Germany's BDSG, France's CNIL requirements, UK GDPR post-Brexit)
- For organizations in UAE, KSA, or other MENA jurisdictions with their own data protection laws, a separate compliance assessment against UAE PDPL / KSA PDPL is required — see [[review-compliance-gap-analysis]]
- For high-risk processing (health data, financial data, location tracking), engage a qualified data protection specialist for DPIA review
- This skill produces analysis, not legal advice. GDPR compliance decisions require a qualified data protection lawyer or DPO

## Related skills

- [[review-compliance-gap-analysis]]
- [[research-regulation-lookup]]
- [[research-regulator-guidance-lookup]]
- [[kb-data-privacy-gdpr]]
