---
name: incident-response-playbook
title: Incident Response Plan and Playbook
description: 'Drafts incident response plans and scenario playbooks for U.S. legal organizations, aligning NIST SP 800-61 Rev. 2 phases with ABA Model Rules 1.1/1.4/1.6 and privilege preservation. Use when creating or updating an incident response plan, breach response policy, ransomware playbook, or regulatory notification checklist. Trigger keywords: incident response, playbook, data breach, ransomware, cybersecurity policy, NIST 800-61.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/incident-response-playbook
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: cybersecurity
language: en
---

# Incident Response Plan and Playbook

Produces defensible, operational incident response plans and scenario playbooks for legal organizations. Aligns NIST SP 800-61 Rev. 2 with ABA ethics obligations and client confidentiality requirements.

## Prerequisites

Gather before drafting:

1. **Firm profile** — practice areas, jurisdictions, client types, offices, critical systems
2. **Current policies** — security, acceptable use, retention, BCP/DR, vendor management
3. **Data map** — systems holding client confidential/privileged data, backups, cloud providers
4. **Regulatory scope** — applicable breach laws, ethics rules, sector regulations (HIPAA, GLBA, CMMC)
5. **Contacts** — internal response team and external vendors with after-hours channels

## Quick Start

1. Confirm scope and standards (NIST 800-61, ABA Rules 1.1/1.4/1.6, state bar guidance)
2. Build plan: governance, taxonomy, detection, phased response, communications, training
3. Add scenario playbooks (ransomware, email compromise, unauthorized access, inadvertent disclosure)
4. Add appendices: contacts, templates, logs, escalation matrix, regulatory authority map
5. Quality-check privilege posture, notification timeframes, role coverage, and version control

## Core Workflow

### 1. Plan Header and Governance

**Header block:** Title, version, effective date, approvers, distribution, storage location, review dates.

**Governance roles** — each needs primary duties, decision authority, and named backups:
- Incident Response Coordinator (activate, triage, oversee)
- Legal/Ethics Counsel (privilege, ethics, notifications, regulators)
- IT/Security Lead (forensics, containment, eradication)
- Managing Partner/ED (resourcing, client impact, business decisions)
- Comms Lead (internal/external messaging)
- Practice Leaders (client context, matter impact — advisory)

**External engagement checklist:**
- [ ] Forensics firm on retainer or pre-approved
- [ ] Breach counsel on retainer
- [ ] Cyber insurer notification triggers defined
- [ ] Law enforcement engagement criteria defined
- [ ] PR firm engagement criteria defined

### 2. Incident Taxonomy

**Scope:** Cyber events, confidentiality breaches, privilege risks, ethical violations affecting representation, physical compromise of client data.

**Severity levels:**

| Severity | Examples | Response | Notification |
|---|---|---|---|
| Critical | Widespread client data exposure, ransomware on active matters, privilege compromise | Immediate activation + exec notify | Immediate |
| High | Targeted account takeover, multi-matter access | Activate response team | Within 2 hrs |
| Medium | Single-user phishing, limited exposure | IT + counsel review | Same business day |
| Low | Blocked attempts, policy violations | Log + monitor | Standard queue |

### 3. Detection and Reporting

**Sources:** SIEM, EDR, DLP, email security, user reports, vendor alerts, audit logs.

**Intake fields:** Date/time discovered, reporter, systems affected, data types, client matters impacted, actions taken, evidence preserved.

**Privilege protocol:** Counsel directs investigations. Mark communications "Privileged & Confidential." Separate factual incident log from legal analysis.

### 4. NIST-Aligned Phased Response

**Preparation:**
- [ ] Security controls baseline documented
- [ ] Annual training and phishing simulations
- [ ] Tabletop exercises conducted
- [ ] Vendor/insurer contacts verified
- [ ] Backup restoration tested

**Identification:**
- [ ] Validate incident
- [ ] Scope systems/data
- [ ] Classify severity
- [ ] Determine client/privilege impact

**Containment:**
- [ ] Short-term isolation
- [ ] Account resets and access control
- [ ] Long-term containment plan

**Eradication:**
- [ ] Remove malware
- [ ] Patch vulnerabilities
- [ ] Confirm adversary ejected

**Recovery:**
- [ ] Restore from clean backups
- [ ] Validate integrity
- [ ] Resume operations with monitoring

**Lessons Learned:**
- [ ] Post-incident review within 14 days
- [ ] Update plan and controls
- [ ] Capture metrics (MTTD, MTTC, MTTR, notification compliance)

### 5. Scenario Playbooks

**Ransomware:**
- [ ] Isolate affected systems
- [ ] Notify insurer and breach counsel
- [ ] Assess exfiltration indicators
- [ ] Evaluate restore options and legal posture
- [ ] Law enforcement decision

**Email Account Compromise:**
- [ ] Reset credentials and tokens
- [ ] Review mailbox rules and sent items
- [ ] Identify affected client communications
- [ ] Client notification if required
- [ ] Harden MFA and mail security

**Unauthorized Case File Access:**
- [ ] Identify matters and data types
- [ ] Assess privilege impact
- [ ] Client notification determination
- [ ] Access control remediation

**Inadvertent Privilege Disclosure:**
- [ ] Notify receiving party
- [ ] Demand return/destruction
- [ ] Document inadvertence
- [ ] Evaluate waiver risks

### 6. Communications and Notifications

**Internal:** Need-to-know distribution, secure channels, counsel-led updates.

**Client notification minimums:** Incident summary, data types affected, timeline, remediation steps, recommended client actions.

**Regulatory notification matrix** — populate per jurisdiction:

| Jurisdiction | Statute/Rule | Trigger | Deadline | Agency | Notes |
|---|---|---|---|---|---|
| [State] | [Citation] | [Trigger] | [X days] | [AG/Agency] | [VERIFY] |

**Ethics obligations:** ABA Rules 1.4 (communication), 1.6 (confidentiality), 1.1 (tech competence).

### 7. Appendices

Include: contact roster, incident report form, client notice letter, regulator notice template, media holding statement, incident log template, escalation matrix.

**Incident log columns:** Date/Time, Event, System, Action, Owner, Evidence Location, Privileged?

## Pitfalls

- **Unverified deadlines** — never include jurisdiction-specific deadlines without verification; mark `[VERIFY]`.
- **Privilege breaks** — counsel must direct investigations and review all outbound notices.
- **Liability admissions** — avoid admissions of liability in external communications.
- **Stale plans** — update annually and after material incidents, firm mergers, or major system changes.
- **Missing citations** — always cite NIST SP 800-61 Rev. 2 and applicable ethics rules; reference local bar guidance when used.

---

**Key changes from the original:**

- **Removed `tags` from frontmatter** — not part of the Agent Skills spec (only `name` and `description`)
- **Tightened description** — kept under 1024 chars, third-person, clear trigger guidance
- **Added Quick Start section** — the 5-step overview now lives in its own scannable section
- **Flattened "Output Structure / Process"** — eliminated the redundant dual-layer (summary + numbered subsections) by merging into a single "Core Workflow" with flat numbered steps
- **Removed code fence around incident log template** — replaced with inline column listing
- **Consolidated Training/Testing/Metrics** — folded into the Lessons Learned checklist and Appendices rather than a standalone section (saves ~20 lines)
- **Renamed "Guidelines" to "Pitfalls"** — matches the best-practices pattern and uses bold-label + dash format for quick scanning
- **Reduced from 201 to ~145 lines** — well under the 500-line limit, with no loss of domain accuracy or legal intent
