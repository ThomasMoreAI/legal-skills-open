---
name: incident-response-plan
title: Incident Response Plan and Playbook
description: Drafts incident response plans and playbooks for legal organizations, adapting NIST SP 800-61 to law firm contexts including privilege preservation, ethics obligations, and state breach notification compliance. Use when creating IR plans, cybersecurity playbooks, breach response policies, or data incident procedures for law firms or legal departments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/incident-response-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: cybersecurity
language: en
---

# Incident Response Plan and Playbook

Drafts legally defensible IR plans for law firms and legal departments covering cybersecurity incidents, data breaches, privilege preservation, and professional responsibility compliance.

## Prerequisites

Gather before drafting:

1. **Organization profile** — firm structure, practice areas, office locations, operating jurisdictions
2. **Existing policies** — infosec policies, business continuity plans, professional responsibility guidelines
3. **Regulatory landscape** — state breach notification statutes, sector overlays (HIPAA, GLBA, CMMC)
4. **Technology environment** — case management systems, DMS, email, backup infrastructure
5. **Insurance coverage** — cyber insurance policy, carrier contact, claim procedures

## Quick Start

1. Map jurisdictions and applicable breach statutes
2. Classify incident types by severity tier
3. Define governance roles and escalation chains
4. Draft phased response procedures (NIST 800-61 adapted)
5. Build scenario-specific playbooks
6. Set communication protocols and notification templates
7. Establish training/testing cadence

## Output Sections

### 1. Jurisdictional Analysis

Map per operating jurisdiction:

- **Breach notification statutes** — triggers, timeframes (typically 30–90 days), AG notification
- **Professional conduct rules** — ABA Model Rules 1.1 (tech competence), 1.4 (communication), 1.6 (confidentiality)
- **Sector overlays** — HIPAA, GLBA, CMMC, SEC as applicable
- **Ethics opinions** — relevant state bar opinions on cybersecurity duties

### 2. Incident Taxonomy

Four severity tiers:

| Tier | Criteria | Response Time |
|------|----------|---------------|
| **Critical** | Widespread client data compromise; privilege breach; mandatory reporting triggered | Immediate (24/7) |
| **High** | Multi-matter exposure; attorney email compromise | ≤2 hours |
| **Medium** | Isolated access attempts; contained inadvertent disclosure | ≤4 hours |
| **Low** | Blocked attempts; policy violations without data exposure | Next business day |

Legal-specific incident types: inadvertent privilege disclosure, case management unauthorized access, conflicts data exposure, attorney email compromise, DMS ransomware, physical file breach.

### 3. Governance Structure

| Role | Function | Key Authority |
|------|----------|---------------|
| IR Coordinator | Activates plan, convenes team | Isolate systems, engage external resources |
| General Counsel / Ethics Counsel | Legal/ethical analysis, privilege protection | Direct privileged investigation, approve notifications |
| CISO / IT Director | Technical response, forensics | Evidence preservation, restoration |
| Managing Partner | Strategic decisions | Expenditures, client relationship decisions |
| Communications Director | Internal/external messaging | Media responses (with counsel approval) |

Include after-hours contact roster and escalation chain for unavailable contacts.

### 4. Phased Response (NIST 800-61 Adapted)

**Phase 1 — Preparation**
- Preventive controls inventory
- Annual security awareness training + tabletop exercises
- External expert relationships (forensics, breach counsel, PR)

**Phase 2 — Identification**
- [ ] Validate incident; preliminary scope assessment
- [ ] Determine if privileged or client-confidential materials involved
- [ ] Assign severity tier; activate response team
- [ ] Initiate investigation under counsel direction to preserve privilege

**Phase 3 — Containment**
- [ ] Isolate systems; disable compromised accounts; block malicious IPs
- [ ] Enhanced monitoring; emergency patches; migrate to backups if needed

**Phase 4 — Eradication**
- [ ] Remove malware/unauthorized access; close vulnerabilities
- [ ] Verify no persistent backdoors

**Phase 5 — Recovery**
- [ ] Restore from verified clean backups
- [ ] System integrity testing; gradual return with heightened monitoring

**Phase 6 — Lessons Learned** (within 14 days)
- [ ] Post-incident review; document timeline and findings
- [ ] Update IR plan; implement preventive measures

### 5. Scenario Playbooks

**Ransomware on DMS:**
1. Isolate systems → notify cyber insurance carrier
2. Assess backup integrity; evaluate exfiltration indicators (double extortion)
3. Determine client notification obligations per jurisdiction
4. Consider law enforcement (FBI IC3); document all decisions under privilege

**Attorney Email Compromise:**
1. Reset credentials; revoke sessions; review forwarding/mailbox rules
2. Identify accessed client communications; assess privilege implications
3. Notify affected clients per Rule 1.4; implement MFA

**Inadvertent Privilege Disclosure:**
1. Notify opposing counsel per FRE 502(b) `[VERIFY]`; request return/destruction
2. Document inadvertence; assess waiver risk under applicable law
3. File clawback motion if necessary

### 6. Communication Protocols

| Audience | Trigger | Timing | Approval |
|----------|---------|--------|----------|
| IR Team | Any confirmed incident | Immediate | IR Coordinator |
| Senior Leadership | High/Critical | Within 1 hour | IR Coordinator |
| Affected Clients | Client data compromised | Per statute + "prompt" ethics notice | GC + Managing Partner |
| State AG / Regulators | Statutory threshold met | Per state (30–90 days) | General Counsel |
| Law Enforcement | Criminal activity; ransomware | Case-by-case | General Counsel |
| Media | Public exposure/inquiry | Reactive only | GC + Communications |

Mark all investigation communications "Privileged & Confidential — Attorney Work Product." Client notifications must satisfy both breach statutes and professional conduct rules.

### 7. Training and Testing

| Activity | Frequency |
|----------|-----------|
| Security awareness training | Annual (all personnel) |
| IR team specialized training | Annual |
| Tabletop exercises | Annual minimum |
| Phishing simulations | Quarterly |
| Backup restoration tests | Semi-annual |
| Plan review and update | Annual + post-incident |

Track: time to detect, contain, eradicate, recover; notification compliance rate.

### 8. Appendices

- [ ] Contact roster (internal + external)
- [ ] Incident reporting form template
- [ ] Client notification letter templates (per jurisdiction)
- [ ] Regulatory filing templates
- [ ] Escalation matrix by severity
- [ ] Evidence preservation checklist
- [ ] Breach notification quick-reference table
- [ ] Version control and approval log

## Pitfalls and Checks

- **Privilege preservation** — all investigation activities directed by counsel; mark work product accordingly
- **Jurisdiction specificity** — map each state's breach notification statute; never rely on generic summaries
- **Dual obligation** — every notification must satisfy both statutory AND ethics requirements
- **Cite authority** — reference specific statutes, ABA Model Rules, ethics opinions; mark uncertain citations `[VERIFY]`
- **Defensibility** — the plan itself evidences reasonable security measures under Rule 1.1 competence duty
- **Internal only** — this plan governs firm response; separate client advisory communications
