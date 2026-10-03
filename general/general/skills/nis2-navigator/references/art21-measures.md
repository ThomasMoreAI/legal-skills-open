# Art. 21 Risk Management Measures — Assessment Reference

## Table of Contents
1. Maturity Scoring Scale
2. The 10 Measures — Detail & Assessment Questions
3. Scoring Guidance

---

## 1. Maturity Scoring Scale

| Score | Level | Description | Evidence indicators |
|-------|-------|-------------|-------------------|
| 0 | **Non-existent** | No awareness, no measures | No documentation, no assigned responsibilities, topic not on management agenda |
| 1 | **Ad hoc** | Informal, reactive, person-dependent | Some awareness exists, individual efforts, no documented process, no regular review |
| 2 | **Defined** | Documented policy/process, inconsistently applied | Written policy exists, partial implementation, gaps in coverage or enforcement, infrequent reviews |
| 3 | **Managed** | Consistently implemented, monitored, periodically reviewed | Full implementation, regular audits/reviews, metrics tracked, management reporting in place |
| 4 | **Optimized** | Continuously improved, measured, integrated into enterprise risk management | KPIs drive improvement, lessons learned fed back, external benchmarking, board-level integration |

---

## 2. The 10 Measures

**Additional reference sources per measure:**
- **BSI #nis2know Infopakete**: The BSI publishes detailed guidance for each measure at bsi.bund.de. Reference the relevant Infopaket when discussing German-specific implementation
- **ENISA Technical Implementation Guidance** (June 2025): Provides practical implementation advice, evidence examples, and mappings to ISO/IEC 27001 and other standards for each of the 13 thematic areas in CIR 2024/2690
- **BSI-Standards 200-1/200-2/200-3**: BSI's own ISMS and risk management methodology, recommended as orientation alongside ISO 27001
- **BSI RUN methodology**: 5-level maturity assessment (Geplant → Implementiert → Evaluiert → Optimiert → Kontinuierlich verbessert) — useful as an alternative or complementary maturity framework to the 0-4 scale used in this skill

**Note on CIR 2024/2690:** For entities in the digital infrastructure and digital provider sectors (DNS, TLD, cloud, data centre, CDN, MSP/MSSP, online marketplace, search engine, social network, trust services), Commission Implementing Regulation (EU) 2024/2690 imposes additional binding technical requirements across 13 thematic areas beyond the general Art. 21 measures. If the assessed entity falls into these sectors, flag that the CIR applies and that additional granular requirements must be assessed separately.

### Measure (a): Risk Analysis and Information System Security Policies
**Directive:** Art. 21(2)(a) | **BSIG-neu:** § 30(2) Nr. 1
**ISO 27001:2022:** A.5.1 (Policies for information security), A.5.2 (IS roles and responsibilities), A.8.1 (User endpoint devices)

**What NIS2 requires:** A systematic approach to identifying, analyzing, and managing risks to network and information systems, underpinned by documented information security policies.

**Assessment question:**
> "Does your organization have documented information security policies, and do you conduct regular risk assessments of your network and information systems? How often are these reviewed?"

**Scoring guidance:**
- 0: No IS policies, no risk assessment practice
- 1: Some informal risk awareness, policies may exist but are outdated or incomplete
- 2: IS policy documented, risk assessments conducted but not regularly or comprehensively
- 3: IS policy suite in place, risk assessments conducted at least annually, results fed into decision-making
- 4: Risk-based approach fully integrated into business processes, continuous risk monitoring, policies reviewed and updated on defined cycles

---

### Measure (b): Incident Handling
**Directive:** Art. 21(2)(b) | **BSIG-neu:** § 30(2) Nr. 2
**ISO 27001:2022:** A.5.24 (IS incident management planning), A.5.25 (Assessment and decision on IS events), A.5.26 (Response to IS incidents), A.5.27 (Learning from IS incidents), A.6.8 (IS event reporting)

**What NIS2 requires:** Procedures for detecting, managing, and responding to security incidents, including escalation, containment, and recovery processes.

**Assessment question:**
> "Do you have a documented incident response procedure? Does it include detection, escalation paths, containment, and post-incident review? Have you tested it in the last 12 months?"

**Scoring guidance:**
- 0: No incident handling procedure
- 1: Informal "call the IT team" approach, no documented procedure
- 2: Incident response plan exists on paper but untested, roles unclear
- 3: Documented procedure, defined roles, tested (tabletop or live) at least annually, post-incident reviews conducted
- 4: Mature incident response with SIEM/SOC integration, regular exercises, lessons-learned process, metrics on MTTD/MTTR

---

### Measure (c): Business Continuity and Crisis Management
**Directive:** Art. 21(2)(c) | **BSIG-neu:** § 30(2) Nr. 3
**ISO 27001:2022:** A.5.29 (IS during disruption), A.5.30 (ICT readiness for business continuity), A.8.13 (Information backup), A.8.14 (Redundancy of information processing facilities)

**What NIS2 requires:** Business continuity measures including backup management, disaster recovery, and crisis management to ensure essential service availability during and after incidents.

**Assessment question:**
> "Do you have business continuity and disaster recovery plans covering your critical systems? Are backups regularly tested for recoverability? Do you have a crisis management process?"

**Scoring guidance:**
- 0: No BCP/DR plans, no backup strategy
- 1: Backups exist but untested, no formal BCP
- 2: BCP/DR documented, backups scheduled, but testing is irregular or incomplete
- 3: BCP/DR in place and tested annually, backup recovery tested regularly, crisis management roles defined
- 4: Comprehensive BCMS with RTO/RPO targets, automated failover tested, crisis exercises with management participation

---

### Measure (d): Supply Chain Security
**Directive:** Art. 21(2)(d) | **BSIG-neu:** § 30(2) Nr. 4
**ISO 27001:2022:** A.5.19 (IS in supplier relationships), A.5.20 (Addressing IS within supplier agreements), A.5.21 (Managing IS in the ICT supply chain), A.5.22 (Monitoring, review and change management of supplier services), A.5.23 (IS for use of cloud services)

**What NIS2 requires:** Security of the supply chain, including security-related aspects of relationships with direct suppliers and service providers. This is one of the most scrutinized NIS2 measures.

**Assessment question:**
> "How do you assess and manage cybersecurity risks from your suppliers and IT service providers? Do your contracts include security requirements? Do you monitor supplier security posture?"

**Scoring guidance:**
- 0: No consideration of supplier/third-party security risk
- 1: Awareness exists, some ad hoc checks on major suppliers
- 2: Security requirements in some contracts, basic vendor assessment questionnaire, no ongoing monitoring
- 3: Systematic vendor risk assessment, contractual security clauses standard, periodic reassessment, critical supplier monitoring
- 4: Mature third-party risk management program, tiered approach based on criticality, continuous monitoring, incident notification clauses, regular audits of critical suppliers

---

### Measure (e): Security in Network and Information Systems Acquisition, Development, and Maintenance
**Directive:** Art. 21(2)(e) | **BSIG-neu:** § 30(2) Nr. 5
**ISO 27001:2022:** A.8.25 (Secure development life cycle), A.8.26 (Application security requirements), A.8.27 (Secure system architecture and engineering), A.8.28 (Secure coding), A.8.8 (Management of technical vulnerabilities)

**What NIS2 requires:** Security integrated into the acquisition, development, and maintenance lifecycle of network and information systems, including vulnerability handling and disclosure.

**Assessment question:**
> "Is security integrated into how you acquire, develop, and maintain IT systems? Do you have a vulnerability management process, including handling of disclosed vulnerabilities?"

**Scoring guidance:**
- 0: No security in procurement/development lifecycle, no vulnerability management
- 1: Some awareness, ad hoc patching, no formal SDLC security
- 2: Vulnerability scanning exists, some procurement security criteria, development guidelines exist but inconsistently followed
- 3: Secure SDLC in place, regular vulnerability scanning and patching with defined SLAs, security in procurement criteria standard
- 4: DevSecOps integrated, automated vulnerability management, coordinated vulnerability disclosure process, security gates in all acquisition processes

---

### Measure (f): Policies and Procedures to Assess Effectiveness
**Directive:** Art. 21(2)(f) | **BSIG-neu:** § 30(2) Nr. 6
**ISO 27001:2022:** A.5.35 (Independent review of IS), A.5.36 (Compliance with policies, rules and standards)

**What NIS2 requires:** Policies and procedures to assess the effectiveness of cybersecurity risk management measures — essentially, testing and auditing whether your measures actually work.

**Assessment question:**
> "How do you verify that your cybersecurity measures are effective? Do you conduct audits, penetration tests, or other assessments? How often?"

**Scoring guidance:**
- 0: No assessment of effectiveness
- 1: Informal checks, reliance on "no incident = secure" assumption
- 2: Occasional penetration tests or audits, no regular cadence, limited scope
- 3: Annual penetration tests and internal audits, management reviews of IS effectiveness, findings tracked to remediation
- 4: Continuous assessment program (red team, bug bounty, automated security testing), KPIs tracked, board-level reporting on IS effectiveness

---

### Measure (g): Basic Cyber Hygiene Practices and Cybersecurity Training
**Directive:** Art. 21(2)(g) | **BSIG-neu:** § 30(2) Nr. 7
**ISO 27001:2022:** A.6.3 (IS awareness, education and training), A.5.10 (Acceptable use of information and other associated assets)

**What NIS2 requires:** Basic cyber hygiene practices (patching, password management, principle of least privilege) and regular cybersecurity training for all staff, including the management body (Art. 20(2) explicitly requires management training).

**Assessment question:**
> "Do all employees receive cybersecurity awareness training? How often? Does this include your management body/board? Do you enforce basic hygiene practices like MFA, patching, and least-privilege access?"

**Scoring guidance:**
- 0: No training, no enforced hygiene practices
- 1: One-off training for some staff, basic password policy exists
- 2: Annual training for general staff, some hygiene practices enforced but gaps remain (e.g., no MFA everywhere, patching delays)
- 3: Regular training including management body, phishing simulations, hygiene practices comprehensively enforced, documented
- 4: Adaptive training program based on role and risk, management body completes dedicated cybersecurity training, continuous reinforcement, metrics on training effectiveness

---

### Measure (h): Policies and Procedures on the Use of Cryptography and Encryption
**Directive:** Art. 21(2)(h) | **BSIG-neu:** § 30(2) Nr. 8
**ISO 27001:2022:** A.8.24 (Use of cryptography)

**What NIS2 requires:** Policies governing the use of cryptography and, where appropriate, encryption to protect data confidentiality and integrity.

**Assessment question:**
> "Do you have a policy on the use of cryptography and encryption? Is data encrypted at rest and in transit for critical systems? How do you manage encryption keys?"

**Scoring guidance:**
- 0: No encryption policy, no systematic use of cryptography
- 1: TLS used on websites, no broader encryption strategy, no key management
- 2: Encryption policy exists, data-in-transit mostly encrypted, gaps in data-at-rest, basic key management
- 3: Comprehensive encryption policy, data encrypted at rest and in transit for all critical systems, key management process defined and operational
- 4: Crypto standards regularly reviewed, automated certificate management, HSM for key protection, crypto agility planning for post-quantum readiness

---

### Measure (i): Human Resources Security, Access Control Policies, and Asset Management
**Directive:** Art. 21(2)(i) | **BSIG-neu:** § 30(2) Nr. 9
**ISO 27001:2022:** A.5.9 (Inventory of information and other associated assets), A.5.15 (Access control), A.5.16 (Identity management), A.5.18 (Access rights), A.6.1 (Screening), A.6.2 (Terms and conditions of employment), A.6.5 (Responsibilities after termination or change of employment)

**What NIS2 requires:** HR security measures (screening, onboarding/offboarding), access control based on least privilege, and comprehensive asset management for network and information systems.

**Assessment question:**
> "Do you maintain an inventory of your critical IT assets? Is access to systems managed on a least-privilege basis with regular reviews? Do you have security-relevant HR processes for onboarding/offboarding?"

**Scoring guidance:**
- 0: No asset inventory, no formal access control, no HR security processes
- 1: Partial asset inventory, basic user account management, informal onboarding/offboarding
- 2: Asset inventory exists but may be incomplete, role-based access defined for some systems, HR processes exist but not consistently security-integrated
- 3: Comprehensive asset inventory regularly updated, RBAC across critical systems with periodic reviews, HR lifecycle fully integrated with access management
- 4: Automated asset discovery, zero-trust access model, JIT/JEA principles, continuous access certification, full HR-IT integration with automated provisioning/deprovisioning

---

### Measure (j): Multi-Factor Authentication, Secured Communications, and Emergency Communication Systems
**Directive:** Art. 21(2)(j) | **BSIG-neu:** § 30(2) Nr. 10
**ISO 27001:2022:** A.5.14 (Information transfer), A.5.17 (Authentication information), A.8.5 (Secure authentication)

**What NIS2 requires:** Use of MFA or continuous authentication solutions, secured voice/video/text communications, and secured emergency communication systems within the entity.

**Assessment question:**
> "Is multi-factor authentication deployed for all privileged access and remote access? Do you have secure communication channels for sensitive and emergency communications?"

**Scoring guidance:**
- 0: No MFA, no secure communications
- 1: MFA for some admin accounts only, standard email for all communications
- 2: MFA deployed for remote access and most privileged accounts, some encrypted communication channels available but not mandated
- 3: MFA enforced for all access, encrypted communication channels for sensitive exchanges, emergency communication procedure defined
- 4: Phishing-resistant MFA (FIDO2/passkeys), end-to-end encrypted communications standard, dedicated emergency communication system tested regularly, conditional access policies

---

## 3. Scoring Guidance

When the user's response is ambiguous, follow these principles:

- **Score what exists and works**, not what is planned or budgeted
- If a policy exists but is not enforced → score 2 maximum
- If practices are strong but undocumented → score 2 maximum (NIS2 requires documented measures)
- If only some systems/users are covered → reduce by 1 from what the coverage would suggest
- Where the user says "I think we do X" without certainty → probe once, then score conservatively
- Always explain your score: "I've scored this as 2 because while you have a policy, you mentioned it hasn't been tested in over a year."
