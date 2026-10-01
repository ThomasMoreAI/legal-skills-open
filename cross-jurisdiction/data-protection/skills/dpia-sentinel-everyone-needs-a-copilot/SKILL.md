---
name: dpia-sentinel-everyone-needs-a-copilot
title: DPIA-Sentinel Skill
description: Data Protection Impact Assessment support for GDPR-style necessity, proportionality, risk identification, mitigation, and residual-risk review. Use for privacy impact assessments, DPIAs, sensitive data processing, and legal-privacy analysis.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/dpia-sentinel
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# DPIA-Sentinel Skill

A Data Protection Impact Assessment identifies privacy risks before processing begins. The goal is not to prevent data processing: it is to ensure that processing is done in a way that minimizes risk to the people whose data is involved.

---

## When a DPIA Is Required

**GDPR Article 35 (mandatory when):**
- Systematic profiling with legal or similarly significant effects on individuals
- Large-scale processing of special categories of data (health, race, religion, biometric, etc.)
- Systematic monitoring of publicly accessible areas

**Colorado Privacy Act (CPA) analog: data protection assessment required when:**
- Processing data for targeted advertising
- Processing sensitive data (health, financial, biometric, race, sexual orientation, citizenship status)
- Selling personal data
- Profiling in a way that produces legal or similarly significant effects

**ENAC best practice: conduct a DPIA whenever:**
- An engagement involves interview data, employee data, or organizational assessment data
- AI tools are used to process personal information about individuals
- A new technology or vendor is introduced that will process client or third-party data

---

## DPIA Process: Five Steps

### Step 1: Necessity and Proportionality Assessment

**Questions to answer:**
1. What personal data will be processed?
2. What is the purpose of processing?
3. Is processing necessary to achieve the purpose, or can the purpose be achieved without processing personal data?
4. Is processing proportionate to the risk (i.e., is the amount of data collected the minimum necessary)?
5. What is the legal basis for processing?

**ENAC-specific considerations:**
- Interview transcripts: necessary for qualitative assessment; apply data minimization (use themes, not named individuals, in deliverables)
- Employee survey responses: necessary for engagement; anonymize or aggregate before analysis where possible
- Organizational structure data: necessary; limit access to engagement team only
- AI processing: what AI tool is used, and is it necessary for this step? Could a less data-intensive approach achieve the same result?

**Output of Step 1:** Processing is necessary and proportionate: YES / NO / CONDITIONALLY
- If YES: continue to Step 2
- If NO: redesign the processing approach before proceeding
- If CONDITIONALLY: document the conditions (e.g., anonymize before AI processing)

---

### Step 2: Risk Identification

**Identify data subjects:** Who are the individuals whose data is being processed?
- Client employees (named, identifiable)
- Client customers or stakeholders (identifiable from context)
- Government officials or elected representatives (public figures)
- Anonymous/aggregated respondents (lower risk)

**Identify processing activities:** For each processing activity, document:
- Data type (name, email, job title, performance data, salary, health status, etc.)
- Processing method (collection, analysis, AI processing, storage, transmission, deletion)
- Tool or system used
- Who has access

**Identify threat scenarios:** For each data subject group × processing activity, what could go wrong?

| Threat | Example |
|--------|---------|
| Unauthorized disclosure | Interview transcript shared with wrong party via email error |
| Unauthorized access | AI vendor processes data for model training without consent |
| Re-identification | Anonymized survey data re-identified from context clues |
| Data breach | Cloud storage with interview transcripts is breached |
| CORA exposure | Materials submitted to Adams County are disclosed via public records request |
| Scope creep | Client uses interview data for purposes beyond the engagement |
| Retention violation | Data not destroyed after engagement ends |

---

### Step 3: Risk Evaluation

Rate each identified threat on two dimensions:

**Likelihood:** How likely is this threat to materialize?
- High: Regularly occurs without specific controls
- Medium: Could occur without attention
- Low: Unlikely with standard precautions

**Severity:** How bad would the impact be on affected individuals?
- High: Significant harm: discrimination, financial loss, professional damage, safety risk
- Medium: Meaningful harm: embarrassment, unwanted attention, limited professional impact
- Low: Minimal harm: minor inconvenience, no lasting effect

**Risk matrix:**

| | Severity: Low | Severity: Medium | Severity: High |
|-|--------------|----------------|----------------|
| **Likelihood: High** | Medium risk | High risk | Critical risk |
| **Likelihood: Medium** | Low risk | Medium risk | High risk |
| **Likelihood: Low** | Acceptable | Low risk | Medium risk |

---

### Step 4: Risk Mitigation Measures

For each identified risk, define mitigation measures:

**Technical measures:**
- Anonymization or pseudonymization before AI processing
- Access controls: limit who can view identified data
- Encryption at rest and in transit
- Audit logging of data access
- Secure deletion protocol after engagement

**Organizational measures:**
- Data handling training for engagement team
- Need-to-know access policy
- Confidentiality agreements with all personnel (NDAs)
- Clear retention and disposal schedule communicated at engagement start
- CORA marking: all materials marked "Confidential: Trade Secret"

**Contractual measures:**
- Data processing agreement with AI vendors
- Confidentiality clause with the client covering ENAC's handling of their data
- Sub-processor controls: same standards flow to any subcontractors handling personal data

**Colorado-specific measures:**
- CORA notice and protective order rights negotiated in PSA (see `@legal-privacy`)
- Trade secret marking on all materials
- Annual PII certification per C.R.S. § 24-74-105 (calendar renewal date)

---

### Step 5: Residual Risk Acceptance

After mitigation measures are applied:

1. **Recalculate the risk**: What is the likelihood and severity after controls?
2. **Is residual risk acceptable?**: Accept if Medium or below after mitigation
3. **If High or Critical residual risk remains:** Escalate to human counsel before proceeding; consider whether the processing is necessary
4. **If risk is unacceptable and cannot be mitigated:** Do not proceed with this processing activity; redesign the engagement

**For GDPR:** If residual risk remains high, prior consultation with the supervisory authority (Data Protection Authority) may be required.

---

## ENAC-Specific DPIA Template

For each engagement involving personal data, complete this assessment and store in the engagement file:

```
Engagement: [Name]
Date: [Date]
Assessor: [Name]

1. NECESSITY AND PROPORTIONALITY
Personal data types: [list]
Processing purpose: [description]
Legal basis (CPA): [legitimate business purpose / contract / legal obligation]
Minimum necessary confirmed: [Yes/No/Conditionally: describe conditions]

2. RISK IDENTIFICATION
Data subjects: [employees / stakeholders / public officials / other]
Threat scenarios identified: [list]

3. RISK EVALUATION
[For each threat: likelihood / severity / risk level]

4. MITIGATION MEASURES
Technical: [list]
Organizational: [list]
Contractual: [list]

5. RESIDUAL RISK
[For each threat: residual likelihood / residual severity / residual risk level]
Overall residual risk: [Acceptable / Requires escalation]

6. DECISION
[Proceed / Proceed with conditions / Escalate / Do not proceed]
Conditions: [if applicable]
Annual review date: [date]
```

---

## Anti-Generic Rules

- NEVER skip Step 1 (necessity): if processing is not necessary, no mitigation makes it appropriate
- NEVER assess risk without identifying specific threats: "general privacy risk" is not a risk
- NEVER accept "we have a confidentiality clause" as a complete mitigation for CORA exposure
- NEVER process health, financial, or sensitive data without a completed DPIA
- NEVER use an AI tool with government client data without verifying the vendor's data processing terms and including it in Step 4 mitigation
