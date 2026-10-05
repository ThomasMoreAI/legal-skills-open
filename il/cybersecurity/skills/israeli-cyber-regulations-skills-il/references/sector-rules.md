# Sector-Specific Cybersecurity Regulations Reference

## Financial Services

### Bank of Israel Directive 364 (the operative framework since 18/05/2026)
**Applies to:** By its own applicability clause (section 10.1), Directive 364 binds corporations as defined in the Banking (Licensing) Law, 5741-1981, namely banking corporations, corporations under sections 11(a)(3a), 11(a)(3b) and 11(b), and **a payment-service provider of systemic importance** under section 36T.

**It does NOT apply to insurers.** The word "insurance" does not appear in Directive 364. Insurers, pension funds and provident funds (גופים מוסדיים) are supervised by the **Capital Market, Insurance and Savings Authority**, and their cyber instrument is **Institutional Bodies Circular 2016-9-14, "Cyber risk management in institutional bodies"** (31/08/2016), issued under the Supervision of Financial Services (Insurance) Law, 5741-1981 and the Provident Funds Law, 5765-2005. Earlier versions of this file applied the banking directives to insurers, which is a wrong-regulator error, not a citation slip.

**Non-bank payment and initiation licensees** are licensed and supervised by the **Israel Securities Authority** under the Payment Services and Payment Initiation Law, 5783-2023, which defines "the Authority" as the ISA and makes information security, cyber protection, risk management and business continuity licensing conditions set in the Authority's regulator instructions.

**Full title:** Proper Conduct of Banking Business Directive 364, "Management of IT, Information Security and Cyber Protection Risks". Published 18/11/2024, circular 2799.

**Status of the predecessors.** Directive 364 took effect on **18/05/2026**, or on
earlier adoption by the banking corporation, whichever came first. From that date
the BOI cancelled Directives **357** (Management of Information Technology),
**361** (Cyber Defense Management) and **363** (supply-chain cyber risk), together
with two supervision letters from 2009. **Do not cite 357, 361 or 363 as live
requirements.** The control content below carried forward substantially from 361
into 364 and remains a good working inventory, but every citation in a board
paper, audit response or gap analysis must be to 364.

**Directives that were NOT absorbed and remain in force:** 366 (incident
reporting, updated 17/06/2026, circular 2848, update 4, which added a duty to
report a "serious security event" under section 31 of the Financial Information
Service Law, 5782-2021, with a parallel change to reporting directive 880); 362
(cloud computing, updated 17/06/2026, circular 2849, version 5); 367 (banking via
communications, updated 17/06/2026, circular 2847); 368 (Open Banking in Israel,
01/09/2025, circular 2826).

**Cloud is not a BOI pre-approval regime.** Directive 362 requires senior
management to set a cloud policy defining which services count as "material cloud
computing" and therefore need board approval, which need senior-management
approval, and which need other approval, plus an annual written report to Banking
Supervision under reporting directive 881. The directive states the supervisory
approach is enabling ("Business enabler") and treats migration of systems to
cloud, including material systems, as part of technological development subject to
prudent risk management.

**Core requirements (carried forward from 361; map each to a 364 clause):**

#### Governance
- Board of directors must approve the cybersecurity strategy and policy
- Board must receive quarterly cybersecurity status reports
- Board must approve the annual cybersecurity work plan and budget
- A board member or committee must be designated as cyber-responsible

#### Personnel
- Dedicated CISO (Chief Information Security Officer) must be appointed
- CISO must report directly to senior management (CEO or deputy)
- CISO must have appropriate qualifications and experience
- Adequate staffing for cybersecurity function

#### Security Operations
- 24/7 Security Operations Center (SOC) for significant institutions
- Continuous monitoring of all critical systems and networks
- Real-time alert triage and escalation procedures
- Integration with CERT-IL for threat intelligence

#### Testing and Assessment
- Annual external penetration testing by a qualified Israeli firm
- Internal vulnerability assessments at least quarterly
- Red team exercises for major banks (recommended annually)
- Third-party security assessments of critical vendors

#### Third-Party Risk
- Due diligence on all technology vendors and service providers
- Cloud use is governed by Directive 362: the banking corporation's senior management sets a cloud policy defining which services are "material cloud computing" and need **board** approval and which need management approval, plus an annual written report to Banking Supervision under reporting directive 881. **There is no prior BOI approval of a cloud provider**
- Outsourcing of IT functions requires notification to BOI
- Ongoing monitoring of vendor security posture

#### Incident Management
- Report technological-failure, information-security and cyber-attack events to Banking Supervision under **Directive 366** (update 4, 17/06/2026). **This file states no clock**: an earlier version said "within 24 hours", which is not sourced to any published BOI instrument. Read 366 for the triggers and mechanics
- Maintain detailed incident response plan, tested annually
- Post-incident analysis and lessons learned within 30 days
- Customer notification for incidents affecting personal data

#### Business Continuity
- Disaster recovery site with tested failover capability
- Annual DR drill with documented results reported to BOI
- Recovery Time Objective (RTO) aligned with business criticality
- Backup integrity verification procedures

### Payment Services Security (BOI payment-service supervision + IT/cyber directives)
**Applies to:** Payment service providers, payment initiation services, fintech companies with BOI licenses.

**Note on numbering:** Directive 357 was "Management of Information Technology" (general IT governance), never a payment-security directive, and it is repealed as of 18/05/2026. Payment-service security comes from BOI supervision of payment service providers together with Directive 364. The control areas below are the substantive payment-security expectations.

**Key control areas:**

#### Transaction Security
- Real-time fraud detection and prevention for all payment channels
- Multi-factor authentication (MFA) for high-value or high-risk transactions
- Transaction limits and velocity checks
- Behavioral analytics for anomaly detection

#### Data Protection
- End-to-end encryption for payment data in transit
- Encryption at rest for stored payment credentials
- PCI DSS compliance required for card data handling
- Tokenization for payment credential storage

#### API and Open Banking Security
- Secure API design following Open Banking standards
- OAuth 2.0 / OpenID Connect for API authentication
- API rate limiting and abuse prevention
- Certificate-based mutual TLS for inter-institution APIs

#### Consumer Protection
- Real-time alerts for suspicious transactions
- Easy mechanism for customers to dispute and freeze accounts
- Transparent disclosure of security practices
- Clear incident communication procedures

#### Pre-Launch Requirements

**Caution, added 2026-08-26.** An earlier version of this file stated that new
licensees "must submit a cybersecurity assessment to BOI before launch" and that
BOI "may require remediation before granting operational approval". **Neither is
sourced**, and it is the same error class this skill corrected for cloud in
v1.3.0, where a supposed BOI pre-approval gate turned out not to exist. Do not
tell a licensee there is a pre-launch cyber sign-off. Licensing conditions are
set in the licence itself and in the supervisor's correspondence with the
applicant; direct the user there, and to the payment-services licensing team, to
establish what is actually required of them.

The items below are expectations a prudent applicant should be ready to meet, not
citable requirements:
- Assessment must cover: architecture review, penetration test results, SOC readiness
- BOI may require remediation before granting operational approval
- Ongoing reporting obligations post-launch

## Healthtech / Digital Health

### Ministry of Health Cyber Requirements
**Applies to:** Hospitals, HMOs (kupot cholim), digital health companies, medical device manufacturers.

**The citable instruments, which this file previously failed to name:**

| Instrument | Date | Issuer |
|---|---|---|
| **Director-General Circular 06/2022, "Basic regulation for cyber protection in the Israeli health system"** (רגולציית יסוד להגנת סייבר במערכת הבריאות בישראל) | effective 13.03.2022 | MoH Director-General's office |
| "Organisational defence doctrine, information security and cyber, health sector" (תורת הגנה ארגונית אבטחת מידע וסייבר מגזר הבריאות) | 08.12.2021 | MoH Digital Technologies and Data Division |
| Cyber crisis preparedness and management PAKAL (פק"ל אבטחת מידע וסייבר, היערכות וניהול משבר סייבר) | 15.03.2022, updated 13.02.2023 | MoH Digital Technologies and Data Division |

Cite circular **06/2022** by number. An unnumbered reference to "the MoH circular on health information security" is not usable in a compliance document.

#### Patient Data Protection
- Encryption required for all patient data (at rest and in transit)
- Access controls: role-based with minimum necessary access
- Audit trails for all access to patient records
- De-identification requirements for research and analytics use

#### Health Information Systems
- Core clinical systems (EMR/EHR) are subject to Ministry of Health oversight. **This file previously said MOH approval is "required"; that approval gate is not sourced** and was softened on 2026-08-26. Establish the actual requirement from circular 06/2022 and from the ministry's digital-health division rather than asserting a sign-off
- Change management procedures for clinical system updates
- Integration security for HL7/FHIR-based health data exchange

#### Medical Device Cybersecurity
- Pre-market: cybersecurity risk assessment required for MOH registration
- Software Bill of Materials (SBOM) for connected medical devices
- Vulnerability disclosure and patch management procedures
- Post-market surveillance for cybersecurity vulnerabilities
- Alignment with FDA and EU MDR cybersecurity guidance

#### Telemedicine Security
- Secure video communication (end-to-end encryption)
- Patient identity verification before clinical session
- Recording and storage policies per MOH guidelines
- Cross-border telemedicine additional requirements

#### Reporting
- Cyber incidents affecting patient safety: immediate reporting to MOH
- Data breaches involving patient data: report to Privacy Protection Authority
- Medical device vulnerabilities: report to MOH Medical Devices Division

## Defense / Aerospace

### MALMAB (Directorate of Security of the Defense Establishment)
**Applies to:** Defense contractors, aerospace companies, companies handling classified information.

#### This skill carries no MALMAB requirements, deliberately

**REMOVED 2026-08-26.** Earlier versions of this file listed a four-level
classification ladder (including a "Sodi Beyoter Beyoter / Top Secret" tier) and a
control list for defence contractors. **MALMAB directives are not published**, so
none of it could be verified against any source, and the fourth classification
tier does not correspond to any published Israeli classification scheme. It has
been removed rather than corrected, because substituting a different unverified
ladder would repeat the error.

**What to do instead.** For defence and aerospace work, tell the user plainly that
the governing requirements are not public, and route them to their organisation's
MALMAB security officer (קצין ביטחון) and to the contracting authority's security
annex, which is where the applicable classification, clearance and network
requirements are actually specified for their contract. Do not describe MALMAB
controls, clearance tiers, or audit expectations from memory: a confident wrong
answer here has security-clearance consequences for the user.

## Telecom / ISPs

### Ministry of Communications Requirements
**Applies to:** Telecommunications providers, ISPs, mobile operators.

**The cyber duty is a licence condition, not a regulation, which is why it is easy to miss.** The instruments are the Ministry's administrative directive **"Cyber Protection Management"** (הוראת מינהל, ניהול הגנת הסייבר) and a matching **"Cyber Protection Management" annex to licences** granted under the Communications (Telecommunications and Broadcasts) Law, 5742-1982, applied to operators by licence amendment. Searching for "telecom cyber regulations" will not surface either; search the ministry's policy collector and the licence terms.

**Dates and the amendment number are deliberately not stated here.** They were carried in a draft of this file with day-level precision that could not be verified against the ministry's own publication in this cycle, and a compliance document would have copied them verbatim. Confirm the directive's current date and the operative licence-amendment number from the Ministry of Communications policy collector before citing either.

The network-security, lawful-intercept and data-retention items below are separate duties and are not the cyber instrument.

#### Network Security
- Infrastructure protection against DDoS and network-level attacks
- Redundancy and resilience for critical communication infrastructure
- Monitoring and detection capabilities for network anomalies
- Incident response procedures for service-affecting events

#### Lawful Intercept
- Compliance with Wiretap Law (Chok Ha'a'azanot Seter, 1979)
- Technical capability for lawful intercept as required by court order
- Strict access controls for intercept systems
- Audit trails for all intercept-related activities

#### Customer Data
- Data retention periods per regulatory requirements
- Customer data protection (billing, call records, location data)
- Notification requirements for data breaches affecting customers
- Secure handling of subscriber identity information

## Energy / Utilities

### Critical Infrastructure Cybersecurity
**Applies to:** Electricity generation and distribution (IEC), natural gas, water (Mekorot), oil refineries.

#### OT/SCADA Security
- Network segmentation between IT and OT environments
- Dedicated monitoring for industrial control systems
- Restricted remote access to OT systems (MFA + VPN minimum)
- Regular vulnerability assessments of SCADA/ICS components
- Patch management adapted for OT availability requirements

#### Physical-Cyber Convergence
- Integrated security operations covering both physical and cyber domains
- Access control systems with cybersecurity protections
- Video surveillance system security
- Environmental monitoring integration

#### Reporting
- Reporting duties follow from designation under the Regulation of Security in Public Bodies Law, 5758-1998, and run through the guiding body. **INCD publishes no mandatory reporting duty or deadline**; an earlier version of this file asserted one
- Ministry of Energy reporting for energy sector-specific incidents
- Water Authority reporting for water system incidents
- National Infrastructure Forum participation

## Regulator Contact Information

| Regulator | Department | Responsibility |
|-----------|-----------|---------------|
| INCD / CERT-IL | National Cyber Directorate | National cyber incident response |
| Bank of Israel | Banking Supervision | Financial sector cyber regulation |
| ISA | Israel Securities Authority | Listed company cyber disclosure |
| MOH | Digital Health Division | Health sector cyber requirements |
| Ministry of Communications | Telecom Regulation | Telecom sector security |
| Ministry of Energy | Infrastructure Protection | Energy sector security |
| MALMAB | Defense Security | Defense sector security |
| Privacy Protection Authority | Ministry of Justice | Data breach reporting (privacy) |
