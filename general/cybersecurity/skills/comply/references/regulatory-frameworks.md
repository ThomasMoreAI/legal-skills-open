# Regulatory Frameworks Reference

## SOC2 Trust Service Criteria

### Overview
SOC2 reports are issued by CPA firms under AICPA standards. Type I evaluates control design at a point in time; Type II evaluates operating effectiveness over a period (typically 6-12 months).

### Trust Service Criteria (TSC)

| Category | ID Range | Key Controls |
|----------|----------|--------------|
| **Security** (Common Criteria) | CC1-CC9 | CC6.1 Logical/physical access, CC6.3 Access removal, CC7.2 Monitoring, CC8.1 Change management |
| **Availability** | A1.1-A1.3 | Capacity planning, disaster recovery, backup/restore |
| **Processing Integrity** | PI1.1-PI1.5 | Data completeness, accuracy, timeliness |
| **Confidentiality** | C1.1-C1.2 | Data classification, confidential data protection |
| **Privacy** | P1-P8 | Notice, choice, collection, use, access, disclosure, quality, monitoring |

### Key Controls for Engineering Teams

| Control | Description | Implementation Pattern |
|---------|-------------|----------------------|
| CC6.1 | Logical access security | RBAC/ABAC, MFA, SSO integration |
| CC6.2 | Access provisioning/deprovisioning | Automated onboarding/offboarding, access reviews |
| CC6.3 | Access removal on termination | Automated deprovisioning triggers |
| CC7.1 | Configuration management | Infrastructure as Code, drift detection |
| CC7.2 | System monitoring | SIEM, anomaly detection, alerting |
| CC8.1 | Change management | PR reviews, CI/CD gates, rollback procedures |
| CC9.1 | Risk mitigation | Risk register, control testing |

---

## PCI-DSS v4.0

### 12 Requirements

| Goal | Req | Description | Technical Focus |
|------|-----|-------------|-----------------|
| Build/Maintain Secure Network | 1 | Install and maintain network security controls | Firewalls, NSCs, microsegmentation |
| | 2 | Apply secure configurations | CIS benchmarks, hardening guides |
| Protect Account Data | 3 | Protect stored account data | Encryption at rest (AES-256), tokenization, truncation, hashing |
| | 4 | Protect data in transit | TLS 1.2+, certificate management |
| Maintain Vuln Mgmt | 5 | Protect from malicious software | Anti-malware, endpoint detection |
| | 6 | Develop and maintain secure systems | SDLC, code review, SAST/DAST, WAF |
| Access Control | 7 | Restrict access by business need | Least privilege, RBAC |
| | 8 | Identify users and authenticate | MFA, password policies, service account management |
| | 9 | Restrict physical access | Physical security (less relevant for cloud-native) |
| Monitor/Test | 10 | Log and monitor all access | Centralized logging, NTP sync, log integrity, 12-month retention |
| | 11 | Test security regularly | Vulnerability scans, penetration tests, IDS/IPS, change detection |
| InfoSec Policy | 12 | Support information security with policies | Security awareness, incident response, risk assessment |

### PCI-DSS v4.0 Key Changes from v3.2.1
- Customized approach allowed as alternative to defined approach
- Enhanced authentication requirements (Req 8.3.6: MFA for all CDE access)
- Targeted risk analysis for flexible implementation
- New e-commerce and phishing protections (Req 6.4.3: script integrity)
- Roles and responsibilities explicitly defined per requirement

### Cardholder Data Environment (CDE) Scoping
- **CDE systems**: Directly store, process, or transmit cardholder data
- **Connected-to systems**: Connect to CDE but don't handle CHD directly
- **Out of scope**: Segmented, no connectivity to CDE
- **Scope reduction**: Tokenization, P2PE, network segmentation

---

## HIPAA

### Safeguard Categories

| Category | Key Rules | Technical Controls |
|----------|-----------|-------------------|
| **Administrative** (§164.308) | Risk analysis, workforce training, contingency planning, BAA management | Risk assessment tools, training records, DR plans |
| **Physical** (§164.310) | Facility access, workstation security, device controls | Physical access logs, device encryption, media disposal |
| **Technical** (§164.312) | Access control, audit controls, integrity controls, transmission security | Unique user IDs, emergency access, auto-logoff, encryption |
| **Breach Notification** (§164.400-414) | Individual notice (60 days), HHS notice, media notice (500+) | Breach detection, notification workflows |

### Technical Safeguard Details (§164.312)

| Standard | Implementation | Required/Addressable |
|----------|----------------|---------------------|
| Access control (a)(1) | Unique user IDs, emergency access, auto-logoff, encryption | Required |
| Audit controls (b) | Record and examine system activity | Required |
| Integrity (c)(1) | Mechanisms to authenticate ePHI | Required |
| Authentication (d) | Verify person seeking access to ePHI | Required |
| Transmission security (e)(1) | Integrity controls, encryption for ePHI in transit | Required |

### Business Associate Agreement (BAA)
- Required when sharing ePHI with third parties
- Must specify permitted uses, safeguards, breach reporting
- Cloud providers (AWS, GCP, Azure) offer BAA-eligible services
- Not all cloud services are BAA-eligible (verify per service)

---

## ISO 27001:2022

### Annex A Control Themes (93 controls)

| Theme | Count | Key Controls |
|-------|-------|--------------|
| **Organizational** (A.5) | 37 | A.5.1 InfoSec policies, A.5.9 Asset inventory, A.5.15 Access control, A.5.23 Cloud security, A.5.36 Compliance |
| **People** (A.6) | 8 | A.6.1 Screening, A.6.3 Awareness/training, A.6.5 Responsibilities after termination |
| **Physical** (A.7) | 14 | A.7.1 Physical perimeters, A.7.9 Off-premises security, A.7.14 Secure disposal |
| **Technological** (A.8) | 34 | A.8.1 User endpoint devices, A.8.5 Secure auth, A.8.9 Config management, A.8.12 DLP, A.8.24 Cryptography, A.8.25 SDLC, A.8.28 Secure coding |

### ISO 27001:2022 Key Changes from 2013
- Reduced from 114 to 93 controls (merged/reorganized)
- New controls: Threat intelligence (A.5.7), Cloud security (A.5.23), ICT readiness for business continuity (A.5.30), Data masking (A.8.11), DLP (A.8.12), Monitoring (A.8.16), Web filtering (A.8.23), Secure coding (A.8.28)
- 4 themes replace 14 domains

### Statement of Applicability (SoA)
- Lists all 93 Annex A controls
- States applicability (applicable/not applicable) with justification
- Links each control to risk treatment plan
- Evidence of implementation for applicable controls
