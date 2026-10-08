---
name: prompt-pack-data-breach-response-plan-sboghossian
title: Data Breach Response Plan
description: 'Use when a company needs to draft an internal Data Breach Response Plan covering incident detection and classification, initial assessment, containment, notification to regulators and affected individuals, documentation, post-incident review, and role assignments. MENA-aware: covers UAE PDPL (72-hour notification), DIFC DP Law, ADGM DP Regs, KSA PDPL, GDPR, and UK GDPR notification requirements with their different timelines and thresholds.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-data-breach-response-plan
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Data Breach Response Plan

A Data Breach Response Plan is a time-sensitive operational document: the first 72 hours after a breach is discovered determine whether regulatory notification deadlines are met, whether liability is mitigated, and whether the company retains or loses control of the narrative. A well-prepared plan enables the response team to act under pressure with confidence.

## When to use this

- A company is implementing a data protection compliance program and needs a formal breach response procedure.
- A regulatory review, ISO 27001 certification, or client audit requires documented incident response procedures.
- A company has suffered a breach and does not have an existing plan — the plan is being drafted in parallel with the response.
- A company has reviewed its existing plan and found it inadequate for the jurisdiction(s) in which it now operates.
- A new data protection law has come into force and the existing plan does not address its specific notification requirements.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company name and jurisdiction(s) of operation | Determines applicable notification frameworks and timelines | Ask the user |
| Types of personal data processed | Scope of potential breach impact; certain data types (health, financial, biometric) trigger enhanced obligations | Ask the user |
| Number of data subjects | Scale of potential breach population | Ask the user |
| Whether a Data Protection Officer (DPO) has been appointed | DPO is the primary coordinator under GDPR; note if one exists | Ask the user |
| Existing incident response or IT security team structure | The plan must integrate with existing security procedures | Ask the user |

## Optional inputs

- Insurance coverage (cyber insurance policy — notify insurer is typically a first-hour obligation).
- Whether the company processes children's data (higher severity under most frameworks).
- Whether the company is a critical infrastructure operator (enhanced obligations in some jurisdictions).
- Existing incident classification matrix (the plan should align with existing IT severity levels).

## Plan structure

### Part 1 — Governance and roles

**1.1 Breach Response Team (BRT)**

| Role | Responsibilities | Typical position |
|---|---|---|
| Incident Lead | Coordinates the response; convenes the BRT; escalation authority | General Counsel / CISO |
| Data Protection Officer (DPO) | Leads regulatory notification decision; advises on obligations; liaises with DPA | DPO / Privacy Counsel |
| IT/Security Lead | Manages technical containment and forensic investigation | CISO / IT Manager |
| Communications Lead | Manages internal and external communications; press statements | Head of Communications / PR |
| Legal Counsel | Provides privilege protection; advises on notification decisions; manages litigation risk | External / In-house counsel |
| Business Lead | Represents affected business unit; operational impact assessment | BU Manager |
| HR (if employee data involved) | Employee communication and employment law compliance | HR Director |

**1.2 Contact directory**
Maintain a current list of all BRT members, their personal mobile numbers, and deputies. Test annually. A breach typically occurs outside business hours.

**1.3 External resources**
- Cyber insurance broker contact.
- External privacy law firm contact.
- Digital forensics firm (pre-contracted or retainer).
- Regulatory authority contacts (DPA / DPO authority) for each jurisdiction.
- Public relations crisis communications firm.

---

### Part 2 — Incident detection and reporting

**2.1 What is a personal data breach?**
A breach is any accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data. This includes:
- External cyberattacks (ransomware, phishing, SQL injection).
- Internal accidental disclosure (email sent to wrong recipient, file shared publicly).
- Internal malicious access (rogue employee).
- Physical loss of device or documents.
- Third-party processor breach that affects company data.

**2.2 Internal reporting obligation**
All employees must report any suspected breach (or near miss) to the IT/Security team and/or DPO immediately (target: within 1 hour of discovery). No employee should decide alone that a security incident is not a breach.

**2.3 Breach log**
Every reported incident, however minor, is logged in the Breach Register with: date reported, date discovered, reporter name, initial description, and outcome. The log is maintained by the DPO.

---

### Part 3 — Initial assessment (Hours 0–4)

**3.1 Classification**
Immediately upon reporting, the IT Lead and DPO assess:

| Factor | Questions |
|---|---|
| Type of breach | Confidentiality / Integrity / Availability |
| Scope | How many data subjects are potentially affected? |
| Data types | Does it include special category data (health, biometric, financial, children's data)? |
| Status | Is the breach ongoing or contained? |
| Cause | External attack / internal error / third-party processor? |

**3.2 Severity classification**

| Severity | Criteria | Response timeline |
|---|---|---|
| Critical | Special category data; large volume; ongoing breach; public authority involved | Immediate; 24/7 BRT activation |
| High | Standard personal data; volume above 1,000 data subjects; breach contained but data exposed | BRT activation within 4 hours |
| Medium | Limited personal data; small volume; breach contained; no evidence of unauthorized access | Assessment within 24 hours |
| Low | Near miss or no data exposure confirmed | Log and review; no notification likely |

**3.3 Containment**
Immediate steps:
- Isolate affected systems (disconnect from network if necessary; balance this against operational impact).
- Revoke compromised credentials.
- Preserve forensic evidence (do not wipe or overwrite affected systems before forensic imaging).
- Take screenshots and logs.

---

### Part 4 — Notification obligations

**This is the most legally critical section. Timelines are strict and missed deadlines can aggravate penalties.**

**4.1 Regulatory notification (to the Data Protection Authority)**

| Jurisdiction | Authority | Deadline | Threshold | Content required |
|---|---|---|---|---|
| EU (GDPR) | Lead Supervisory Authority (Art. 55/56) | 72 hours from discovery | If likely to result in risk to rights and freedoms of individuals | Nature, categories, approx number affected, DPO contact, consequences, measures taken |
| UK (UK GDPR) | ICO | 72 hours | Same as GDPR | Same as GDPR |
| UAE (PDPL) | UAE DPA (TDRA) | 72 hours | If likely to cause serious harm | Same categories as GDPR broadly; specific TDRA guidance to be monitored |
| DIFC | DIFC Commissioner of Data Protection | 72 hours from becoming aware | If likely to result in a risk to rights and freedoms | Nature, approximate number of data subjects, consequences, measures |
| ADGM | ADGM Commissioner of Data Protection | 72 hours | Equivalent to DIFC | Equivalent |
| KSA (PDPL) | Saudi DPA (NDMO) | 72 hours | If breach may result in prejudice to personal data subjects | NDMO implementing regulations govern the content; verify with local counsel |
| Egypt | MCIT (Ministry of Communications) | 72 hours (as per Law No. 151 of 2020) | If serious risk | Confirm with local counsel as implementing regulations are developing |

**The 72-hour clock starts from when the company becomes "aware" — which is when the incident is reported internally, not when the forensic investigation is complete.** A "provisional" or "initial" notification can be filed with a commitment to provide further information. Regulators understand that full information takes time; what they do not forgive is missing the 72-hour deadline entirely.

**4.2 Individual notification (to affected data subjects)**

| Jurisdiction | When required | Timing | Content required |
|---|---|---|---|
| GDPR / UK GDPR | If likely to result in high risk to rights and freedoms | "Without undue delay" | Nature of breach; DPO contact; likely consequences; measures taken; contact point for further information |
| UAE PDPL | If likely to cause serious harm | Without undue delay after regulatory notification | Equivalent content |
| DIFC DP Law | If likely to result in high risk | Without undue delay | Equivalent content |
| KSA PDPL | If harm is likely | Without undue delay | NDMO guidance to be followed |

Individual notification may be waived if: appropriate technical measures render the data unintelligible (e.g., encryption was effective), subsequent measures have removed the high risk, or individual notification would require disproportionate effort (mass public communication as alternative).

---

### Part 5 — Containment and recovery

- Execute the IT security team's technical remediation plan.
- Change all affected credentials and access controls.
- Patch the vulnerability that was exploited.
- Restore from clean backup if data integrity was affected.
- Validate that the breach has been fully contained before restoring normal operations.
- Engage external forensic investigators if the cause is unknown or if litigation is anticipated.

---

### Part 6 — Documentation

Maintain a comprehensive Breach Record including:
- Timeline of events (discovery, assessment, containment, notification).
- All communications (internal and external) related to the breach.
- Regulatory notifications filed (date, content, authority).
- Individual notifications sent (date, method, content, number sent).
- Forensic investigation findings.
- Remediation steps taken.
- Decision log: why each notification decision was made, by whom, and on what information.

The Breach Record must be retained for a minimum of 5 years and must be available for inspection by the relevant DPA.

Privilege: draft the Breach Record with legal counsel to preserve legal privilege where possible. Factual investigation reports may not attract privilege; legal advice on notification and liability should be documented separately under privilege.

---

### Part 7 — Post-incident review

Conduct a post-incident review within 30 days of containment:
1. Root cause analysis: what caused the breach and how was it not prevented?
2. Response quality: was the response plan followed? What worked and what did not?
3. Remediation: are the fixes in place permanent?
4. Lessons learned: update the response plan, security policies, and training programs based on findings.
5. Report to the board or senior management.

---

## Jurisdictional alerts

| Jurisdiction | Specific risk |
|---|---|
| Lebanon | No comprehensive data protection law; apply GDPR as best practice and notify affected individuals as a matter of good practice; cyber insurance claims should be filed promptly |
| Egypt | Law No. 151 of 2020 implementing regulations are still developing; monitor MCIT guidance; 72-hour rule applies |
| KSA | NDMO implementing regulations are evolving; early regulatory engagement is recommended for significant breaches |

## Common mistakes

- Missing the 72-hour regulatory notification deadline because the internal reporting chain was too slow.
- Filing a regulatory notification before containment is confirmed — regulators want to know what the company is doing to protect individuals, not just what happened.
- Insufficient documentation — regulators will ask for the full timeline; gaps suggest inadequate process.
- Notifying individuals before the company has accurate information — incorrect notifications create additional confusion and legal exposure.
- Failure to notify the cyber insurer within the policy's notification window (often 24–48 hours) — this can void coverage.

## Related skills

- [[prompt-pack-data-processing-agreement]]
- [[prompt-pack-data-retention-policy]]
- [[prompt-pack-data-subject-access-request-procedure]]
- [[prompt-pack-cross-border-data-transfer-assessment]]
- [[prompt-pack-cookie-policy]]
