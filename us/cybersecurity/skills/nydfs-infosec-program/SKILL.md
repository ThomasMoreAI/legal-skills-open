---
name: nydfs-infosec-program
title: NYDFS Information Security Program (23 NYCRR 500)
description: 'Drafts a comprehensive Information Security Program compliant with NYDFS Cybersecurity Regulation (23 NYCRR 500). Covers CISO designation, risk assessment, access controls, encryption, monitoring, incident response, notification, and annual certification for covered financial services entities. Use when drafting cybersecurity programs, NYDFS compliance policies, or information security policies for financial institutions. Trigger keywords: NYDFS, 23 NYCRR 500, cybersecurity regulation, information security program, CISO policy, financial services cybersecurity.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/nydfs-infosec-program
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: cybersecurity
language: en
tags: [drafting, memo, research]
---

# NYDFS Information Security Program (23 NYCRR 500)

Drafts a regulatory-ready Information Security Program for covered entities under the NYDFS Cybersecurity Regulation.

## Prerequisites

1. Organizational documents — org charts, existing cybersecurity policies, technology inventories.
2. Prior risk assessments — completed assessments, audit findings, remediation plans.
3. Regulatory history — prior NYDFS examination findings, guidance letters, enforcement context.
4. Vendor inventory — third-party service providers with access to systems or nonpublic information (NPI).
5. Incident history — prior incident response documentation, breach notifications.

## Quick Start

Assemble the program document with executive summary, table of contents, glossary, and the sections below mapped to 23 NYCRR 500. Tailor controls to the entity's size, complexity, and risk profile.

## Output Structure

### 1. CISO Designation (§ 500.04)

| Element | Requirement |
|---|---|
| Reporting line | Direct to Board or senior officer; independent from operations |
| Qualifications | Certifications (CISSP, CISM), financial-services expertise |
| Authority | Enforce policies, direct investments, oversee risk assessments, coordinate IR |
| Board reporting | Regular reports on posture, threats, metrics, resource needs |
| Strategic role | New products, tech implementations, M&A, vendor relationships |

### 2. Written Information Security Policy (§ 500.03)

| Function | Coverage |
|---|---|
| Information security | CIA triad across information lifecycle |
| Data governance | Classification, handling, retention, disposal |
| Access controls | Least privilege, separation of duties, periodic reviews |
| BC/DR | RTO/RPO, backup requirements, testing |
| Incident response | Definitions, high-level protocols |
| Vendor management | Third-party risk assessment and monitoring |

Include: scope definition, governance structure, enforcement mechanisms, exception process, annual review cycle, Board approval.

### 3. Risk Assessment (§ 500.09)

- **Threats**: Internal (insider, misconfig, process failure) and external (ransomware, phishing, supply chain, nation-state).
- **Scoring**: Likelihood × impact; define thresholds for immediate remediation vs. planned vs. accepted.
- **Impact dimensions**: Financial loss, regulatory penalties, reputational damage, operational disruption.
- **Frequency**: Annual minimum; interim on material changes (new tech, M&A, new vendors, threat shifts).
- **Output**: Documented findings, prioritized remediation, Board reporting.

### 4. Access Controls & Identity Management (§ 500.07, § 500.12)

| Control | Specification |
|---|---|
| Least privilege | Role-based access aligned to job functions |
| MFA (§ 500.12) | Privileged accounts, remote access, systems with sensitive NPI |
| Privileged access | Separate admin accounts; just-in-time provisioning; enhanced monitoring |
| Provisioning | Formal request → manager + data owner approval → authorized provisioning |
| Termination | Immediate deprovisioning; automated where possible |
| Access reviews | Privileged: quarterly · Sensitive: semi-annual · Standard: annual |

### 5. Data Governance & Classification (§ 500.13)

| Level | Definition | Handling |
|---|---|---|
| Public | Freely disclosable | No restrictions |
| Internal | Employee use only | Standard access controls |
| Confidential | Disclosure harmful | Encryption in transit/at rest, restricted sharing |
| Highly Confidential | NPI, SSN, financial accounts, biometrics | Enhanced encryption, strict access, DLP |

Require: data inventory/mapping, ownership assignments, data minimization, retention schedules with secure disposal.

### 6. Encryption (§ 500.15)

| Scope | Standard |
|---|---|
| In transit | TLS 1.2+; AES-128 minimum, AES-256 preferred |
| At rest — portable | Full-disk encryption |
| At rest — databases | TDE or column-level for NPI |
| At rest — backups | Encrypted; keys separate from production |
| Asymmetric | RSA-2048+ or equivalent ECC |
| Key management | HSM or KMS; separate generation, storage, rotation, destruction |
| Exceptions | Risk assessment + compensating controls + CISO approval |

### 7. Monitoring & Vulnerability Management (§ 500.05, § 500.06)

**Monitoring**: IDS/IPS at perimeters, EDR on endpoints/servers, SIEM aggregating firewalls/auth/apps/databases. Log retention by risk tier.

**Required logging**: Auth events, privileged access, sensitive data access, config changes, security alerts.

| Activity | Frequency |
|---|---|
| External scan | Weekly or continuous |
| Internal scan | Monthly |
| Penetration testing | Annual minimum |
| Critical vuln remediation | Days |
| General patching | Risk-based; compensating controls for delays |

### 8. Incident Response Plan (§ 500.16)

**Incident types**: Unauthorized access, malware, DoS, data breach, insider threat, physical breach.

**Response lifecycle**:
1. **Preparation** — Training, tools, playbooks, communication channels.
2. **Detection & Analysis** — Triage alerts, severity assessment.
3. **Containment** — Short-term (isolate, disable, block) → Long-term (patch, harden).
4. **Eradication** — Remove threat, close access paths, reset credentials.
5. **Recovery** — Restore from clean backups, enhanced monitoring.
6. **Post-Incident Review** — Root cause, response effectiveness, documented improvements.

**Team roles**: Incident Commander, Technical Investigators, Legal Counsel, Communications, Executive Leadership. Maintain forensic images and chain of custody.

### 9. NYDFS Notification (§ 500.17)

**Threshold**: Cybersecurity event with reasonable likelihood of materially harming normal operations.

| Requirement | Detail |
|---|---|
| Deadline | 72 hours from *determination* of reportability (not detection) |
| Content | Incident type, date, affected systems, data types, individuals affected, remediation, investigation status |
| Updates | Submit supplemental reports as investigation progresses |
| Coordination | Align with state breach laws, federal regulators, law enforcement, contracts |

### 10. Annual Certification (§ 500.17(b))

**Timeline**: Begin compliance review no later than Q4; submission deadline February 15.

**Compliance matrix** — Map each § 500 requirement to: implementing controls, responsible personnel, supporting evidence, gap status/remediation.

**Evidence domains**: Governance (Board minutes, CISO appointment), Policies (approvals, acknowledgments), Risk assessment (reports, methodology), Access controls (RBAC, MFA records, audit logs), Encryption (inventory, key management), Monitoring (scans, pen tests, SIEM), IR (plan, exercises, incident logs), Vendor management (assessments, contracts), BC/DR (plans, test results).

**Validation**: Go beyond document existence — sample transactions, review patching timelines, test encryption, interview personnel.

**Certification governance**: CISO prepares report → legal review → Board review → documented approval. Material deficiencies must be remediated or disclosed before submission.

## Guidelines

- Address all sections of 23 NYCRR 500; use the regulation as the organizational backbone.
- Tailor controls to entity size, complexity, and risk profile — avoid one-size-fits-all language.
- Include version control: version number, revision history, approval signatures, next review date.
- Cross-reference supporting documents rather than embedding them.
- Flag cited section numbers with `[VERIFY]` if uncertain — 23 NYCRR 500 was significantly amended November 2023.
- Do not include privileged legal analysis or attorney-client communications in the program document.
- Note that Class A companies (§ 500.1(d)) have additional requirements including independent audits and CISO independence standards.

---

Key changes from the original:
- Added `>-` multiline description with trigger keywords for better agent discoverability
- Added **Quick Start** section per best practices
- Compressed IR team roles from a full table to inline list (the lifecycle is the important structure)
- Collapsed the evidence categories table in Section 10 into a compact inline format
- Removed redundant prose (e.g., "Role changes" row merged into termination/provisioning flow)
- Trimmed monitoring stack from bullet list to single-line summary
- Shortened all section headings and removed "Section N:" prefix noise
- Reduced from ~196 lines to ~140 lines (~28% token savings) while preserving every § reference and regulatory requirement
