---
name: vendor-security-assessment
title: Vendor Security Assessment Questionnaire
description: Drafts a Vendor Security Assessment Questionnaire evaluating third-party cybersecurity posture, data handling, and regulatory compliance. Vendor responses become binding contractual representations with executive certification. Use during vendor due diligence, third-party risk management, procurement security review, or subprocessor evaluation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/vendor-security-assessment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Vendor Security Assessment Questionnaire

Generates a pre-contract due-diligence questionnaire for evaluating vendor security controls, data practices, and compliance across GDPR, CCPA, HIPAA, SOX, GLBA, FERPA, and industry frameworks.

## Quick Start

Gather before drafting:
1. **Vendor scope** — data types accessed (PII, PHI, PCI, financial, proprietary), processing activities, data flows
2. **Applicable regulations** — GDPR, CCPA, HIPAA, SOX, GLBA, FERPA, or sector-specific
3. **Risk tolerance** — what constitutes acceptable vs. disqualifying vendor risk
4. **Contract alignment** — security provisions to incorporate by reference

## Document Framework

| Element | Requirement |
|---|---|
| Preamble | Completion mandatory pre-contract; responses are binding representations |
| Executive certification | Senior officer (CISO/CTO/CLO) attests accuracy; signature block required |
| Submission deadline | 10–15 business days |
| Change notification | Vendor notifies within 5 business days of material security changes |
| Confidentiality | Questionnaire and responses treated as confidential business information |

## Assessment Domains

Draft numbered questions per domain. Each question includes a response field and evidence-request field where applicable. Tailor scope to data sensitivity — not every vendor needs every domain.

**1. Information Security Governance**
- Dedicated CISO/equivalent; certifications (CISSP, CISM, CISA)
- Framework alignment (NIST CSF, ISO 27001, CIS Controls, COBIT)
- Policy review cadence; security awareness training (all-staff + specialized)
- Board-level security reporting frequency

**2. Data Classification & Lifecycle**
- Classification taxonomy compatibility with client's scheme
- All data storage/processing locations (primary, DR, backup, cloud regions)
- Cross-border transfer mechanisms (SCCs, adequacy decisions, BCRs)
- Retention post-termination; destruction methods; certificates of destruction
- Backup frequency; encrypted backup media; tested RTO/RPO

**3. Access Control & Privileged Access**
- MFA enforcement across all access; supported factors
- RBAC, least-privilege, segregation of duties
- Privileged access: JIT elevation, session recording, auto-deprovisioning
- Access recertification frequency; anomalous-access alerting

**4. Vulnerability Management & Testing**
- Scanning tools, frequency, and patching SLAs:

| Severity | Patch SLA |
|---|---|
| Critical | ≤ 24–72 hrs |
| High | ≤ 7 days |
| Medium | ≤ 30 days |
| Low | ≤ 90 days |

- Annual third-party pentests (external + internal lateral movement)
- AppSec testing (SAST, DAST, SCA) for custom software
- Bug bounty / responsible disclosure program
- Request most recent pentest summary and remediation status

**5. Incident Response & Business Continuity**
- Documented IR plan with roles, escalation, communication protocols
- IR testing frequency (tabletop, simulations) and recent results
- Notification timeline — must allow client to meet most restrictive regulatory deadline (GDPR 72 hrs, HIPAA 60 days, state breach laws)
- Cooperation with client IR team and legal counsel
- Cyber insurance: policy limits, third-party liability, adequacy for data volume
- BCP/DR: tested RTO/RPO, geographic diversity, multi-scenario resilience

**6. Encryption & Key Management**
- At rest: minimum AES-256; scope includes production, dev/test, backups, portable media
- Database encryption approach (TDE, column-level, application-layer)
- In transit: TLS versions, deprecated protocol status, enforced cipher suites
- In use: confidential computing / secure enclave capabilities (if applicable)
- Key management: HSM/KMS storage, rotation frequency, secure destruction

**7. Network Security & Segmentation**
- Customer isolation; production vs. corporate separation
- Zero-trust architecture status
- Perimeter controls: firewalls, IDS/IPS, WAF, DDoS protection
- Remote access: VPN, NAC/device posture, MFA
- Assessment cadence (external scans, internal pentests, wireless)

**8. Subprocessor Risk Management**
- Complete subprocessor inventory: role, data access, location, assessments conducted
- Flow-down of security requirements (contractually at least as stringent as client's)
- Client notification and approval rights before new subprocessor engagement
- Right to terminate non-compliant subprocessors

**9. Certifications & Compliance**
- SOC 2 Type II: report date, principles, opinion status, scope alignment
- ISO 27001: certificate dates, scope, certification body
- PCI DSS, FedRAMP/StateRAMP, HITRUST, TISAX (as applicable)
- Regulatory compliance confirmation for applicable data types
- Commitment to provide updated reports/certifications annually

**10. Physical Security & Environmental Controls**
- Data center access: MFA, visitor logs, surveillance, security personnel
- Background checks for personnel with physical access
- Environmental: fire suppression, UPS, generators, climate, water detection
- Facility certifications (SSAE 18 SOC 1, Uptime Institute tier)

**11. HR Security & Insider Threat**
- Background checks; periodic re-investigation for sensitive roles
- Security training before access; policy acknowledgment
- Offboarding: access revocation timeline, exit procedures
- Insider threat monitoring; DLP for exfiltration prevention

## Risk Assessment Framework

Score vendor responses after receipt:

| Rating | Criteria |
|---|---|
| Low | Controls meet/exceed requirements; evidence provided |
| Moderate | Minor gaps; addressable via contractual provisions |
| High | Significant gaps; requires remediation plan with deadlines |
| Critical | Fundamental deficiencies; disqualifying absent remediation |

Assessment report must include:
- Per-domain and overall risk rating with justification
- Recommended contractual controls (audit rights, insurance minimums, SLAs)
- Evidence gaps requiring follow-up
- Go/no-go recommendation with conditions
- Flagged inconsistencies between responses and publicly available information

## Checks

- State explicitly in preamble: responses are **contractually binding representations**; incomplete/misleading answers constitute grounds for disqualification or material breach
- Align notification timelines with the **most restrictive applicable breach notification law**
- Mark questions as required vs. conditional based on data type (PCI questions only if payment data involved)
- Flag vendors refusing to disclose subprocessors or share certifications as elevated risk
- All legal citations to specific regulatory provisions must be verified against current law [VERIFY]
