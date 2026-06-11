---
name: information-security-policy
title: Information Security Policy
description: Drafts a board-approvable Information Security Policy covering data classification, access controls, encryption, incident response, breach notification, and enforcement. Tailored by industry and regulatory environment (HIPAA, GDPR, CCPA, GLBA, FERPA, PCI DSS). Use when drafting or overhauling an organization's foundational information security governance framework or cybersecurity policy.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/information-security-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: cybersecurity
language: en
tags: [drafting, policy, regulatory, research]
---

# Information Security Policy

Drafts a formal Information Security Policy satisfying multi-framework regulatory requirements with enforceable operational guidance.

## Prerequisites

1. **Org profile** — industry sector, employee count, jurisdictions of operation
2. **Regulatory triggers** — applicable frameworks (HIPAA, GDPR, CCPA, GLBA, FERPA, PCI DSS, SOC 2, ISO 27001, NIST CSF)
3. **Existing governance docs** — current policies, data classification schemes, incident response plans
4. **Data inventory** — sensitive data categories handled (PHI, PII, payment card data, student records, trade secrets)
5. **Approving authority** — CEO, Board, CISO, General Counsel signature blocks needed

## Output Structure

### Document Control Block

| Field | Content |
|-------|---------|
| Policy Title | Information Security Policy |
| Version / Effective Date | [#] / [Date] |
| Approved By / Owner | [Title] / CISO or equivalent |
| Next Review | [Date + 1 year] |
| Supersedes | [Prior version or N/A] |

### Section Outline

**1. Purpose & Authority**
- Business rationale (financial, reputational, regulatory risk)
- Authorizing resolution; relationship to other org policies

**2. Scope**
- **Entities:** parent, subsidiaries, affiliates, JVs
- **Personnel:** employees, contractors, vendors, partners
- **Assets:** electronic data, physical records, IP, BYOD, remote environments
- **Exclusions:** publicly available info, de-identified data (define standard)

**3. Definitions**
Define with legal precision; flag where definitions vary by jurisdiction:
- Confidential Information, Personal Data / PII (per GDPR Art. 4, CCPA § 1798.140, HIPAA 45 C.F.R. § 160.103)
- Data Breach, Security Incident, Data Owner, Data Custodian, Authorized User
- Classification Levels: Public / Internal / Confidential / Restricted

**4. Data Classification**

| Level | Description | Examples |
|-------|-------------|---------|
| Public | Approved for external release | Marketing materials |
| Internal | Business use; not for external distribution | Org charts, internal memos |
| Confidential | Limited distribution; legal obligations | Customer PII, financial data |
| Restricted | Highest sensitivity; regulatory protection | PHI, payment card data, credentials |

**5. Access Controls**
- Least privilege; separation of duties
- Lifecycle: request → data owner approval → provisioning → quarterly review → revocation on role change/termination
- Privileged access: separate admin accounts; logged and audited

**6. Authentication**

| Requirement | Standard |
|-------------|---------|
| Password length | 12+ characters; mixed case, numbers, symbols |
| MFA required for | Remote access, privileged accounts, Restricted data, cloud admin |
| Acceptable MFA | TOTP, hardware token, biometric; SMS discouraged for high-risk |
| Shared credentials | Prohibited |

**7. Encryption Standards**

| Context | Minimum Standard |
|---------|-----------------|
| Data at rest (Confidential/Restricted) | AES-256 |
| Data in transit | TLS 1.2+ (1.3 preferred) |
| Portable devices | Full-disk encryption |
| Email (Restricted) | End-to-end or secure portal |
| Backup media | Encrypted; separate key management |

Review annually; superseded by org Security Standards if more stringent.

**8. Acceptable Use**
- Prohibited: illegal activity, harassment, circumventing controls, credential sharing
- Monitoring: org reserves right; no expectation of privacy on org systems
- BYOD: MDM enrollment, encryption, remote wipe on loss/termination

**9. Physical Security**
- Lock unattended devices; clean desk for Confidential/Restricted materials
- Secure disposal: cross-cut shredding (paper); cryptographic erasure or destruction (media)
- Visitor access: escorted in secure areas; logs maintained

**10. Data Retention & Disposal**

| Category | Period | Basis |
|----------|--------|-------|
| PHI | 6 years | HIPAA 45 C.F.R. § 164.530(j) |
| Financial records | 7 years | IRS / GLBA |
| Student records | Per FERPA | 34 C.F.R. § 99 |
| Incident logs | 3 years min | [Regulatory basis] |

Certificate of destruction required for Restricted data.

**11. Roles & Responsibilities**

| Role | Obligations |
|------|-------------|
| Board / Exec | Policy approval; resource allocation |
| CISO | Program ownership; standards; audit; regulator liaison |
| IT / Security | Controls; patching; monitoring; vulnerability mgmt |
| Legal / Privacy | Breach notification decisions; regulatory liaison |
| Managers | Access approval; team compliance; off-boarding |
| All Employees | Credential protection; incident reporting; training |
| DPO | Required under GDPR Art. 37 if applicable |

**12. Incident Response**

Lifecycle:
1. **Detect & Report** — within [1–4 hours] to security hotline
2. **Assess** — severity triage; activate IRT if Sev 1/2
3. **Contain** — isolate systems; preserve evidence; chain of custody
4. **Eradicate** — remove threat; patch vulnerability
5. **Recover** — restore from clean backups; verify integrity
6. **Post-Incident Review** — within 14 days; root cause; corrective action plan

IRT: CISO (lead), IT Security, Legal, HR, PR/Comms, Executive Sponsor.

**13. Breach Notification**

| Framework | Deadline | Recipients |
|-----------|----------|-----------|
| HIPAA | 60 days (individuals); 60 days HHS + media if 500+ | Individuals, HHS, media |
| GDPR | 72 hours to SA; without undue delay to individuals if high risk | SA, affected individuals |
| CCPA/CPRA | Expedient / without unreasonable delay | Consumers; AG if 500+ CA |
| State laws | 30–90 days (varies) | Residents, AGs, credit bureaus |
| PCI DSS | Immediately | Card brands, acquiring bank |

Legal counsel notified immediately upon any incident involving personal data.

**14. Third-Party & Vendor Management**
- Security assessment before vendor access to Confidential/Restricted data
- Required contractual provisions: DPA / BAA as applicable
- Right-to-audit for Restricted data vendors
- Access revoked immediately on contract termination

**15. Regulatory Compliance Matrix**

| Framework | Applicability | Key Requirements |
|-----------|--------------|-----------------|
| HIPAA (45 C.F.R. §§ 164.302–318) | Healthcare / PHI | Admin, physical, technical safeguards; BAAs |
| GLBA (16 C.F.R. § 314) | Financial institutions | Risk assessment; safeguards; service provider oversight |
| FERPA (34 C.F.R. § 99) | Education | Student record protection; disclosure restrictions |
| GDPR | EU personal data | Lawful basis; data subject rights; DPIAs; SCCs |
| CCPA/CPRA | CA residents | Consumer rights; opt-out; privacy notice |
| PCI DSS v4.0 | Payment cards | Detailed controls in separate PCI procedures |
| NIST CSF 2.0 | Voluntary | Identify, Protect, Detect, Respond, Recover, Govern |
| ISO 27001 | Voluntary | ISMS; Annex A controls |

**16. Training & Awareness**
- All personnel: at hire + annually; phishing simulation semi-annually
- High-risk roles (sysadmins, developers, finance): role-specific training annually
- Completion tracked; non-completion escalated; records retained 3 years

**17. Compliance Monitoring & Audit**
- Annual risk assessment; quarterly vulnerability scans; annual penetration test
- Access reviews: semi-annual (Confidential), quarterly (Restricted)
- Remediation SLAs — Critical: 30 days, High: 60 days, Medium: 90 days

**18. Enforcement**
Progressive discipline: retraining → written warning → suspension/termination → civil liability → criminal referral. Factors: intent, severity, prior violations, self-reporting.

**19. Policy Administration**
- Review: annually or upon major incident, regulatory change, material org change
- Approval: [CEO/Board] on CISO + General Counsel recommendation
- Employees acknowledge receipt in writing; at-will status unaffected

### Signature Block

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CEO | | | |
| CISO | | | |
| General Counsel | | | |

### Employee Acknowledgment
*I acknowledge receipt of, have read, and agree to comply with the Information Security Policy (Version [#], effective [Date]).*

Name: ______ Title: ______ Date: ______ Signature: ______

## Guidelines

- **Multi-jurisdiction conflicts:** apply most stringent standard or add jurisdiction-specific schedules
- **Encryption floors:** AES-256 / TLS 1.2+ are minimums; revise per NIST guidance updates
- **GDPR DPO:** required if org is public authority, conducts large-scale monitoring, or processes special category data at scale — confirm applicability before drafting `[VERIFY]`
- **HIPAA BAAs:** policy cross-references but does not replace BAA; maintain separate vendor register
- **PCI DSS:** detailed technical controls in separate PCI documentation to allow updates without policy re-approval
- **At-will disclaimer:** verify enforceability under applicable state law `[VERIFY]`
- **Collective bargaining:** if unionized workforce, confirm no bargaining obligation before implementation
- **Do not fabricate citations** — use `[VERIFY]` for any citation not confirmed against primary source
