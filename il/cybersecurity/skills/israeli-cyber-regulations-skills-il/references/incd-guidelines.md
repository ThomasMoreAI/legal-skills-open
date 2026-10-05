# INCD (Ma'arach HaSyber) Framework Reference

## Overview

The Israel National Cyber Directorate (INCD / Ma'arach HaSyber HaLeumi) is the national authority responsible for defending Israel's cyberspace. Established under the Prime Minister's Office, INCD sets cybersecurity policy, coordinates incident response through CERT-IL, and issues guidelines for both public and private sectors.

**Official portal:** `https://www.gov.il/he/departments/israel_national_cyber_directorate`

## Organizational Structure

### CERT-IL (National Cyber Emergency Response Team)
- **Role:** Receives, analyzes, and responds to cyber incidents across all sectors
- **Hotline:** Available 24/7 for incident reporting
- **Services:** Threat intelligence sharing, incident investigation, forensic assistance
- **Free for:** All Israeli organizations (public and private)

### Government ICT Authority (Rashut HaTkshov HaMemshalti)
- **Role:** Sets IT and cybersecurity standards for government ministries and agencies
- **Mandate:** All government systems must comply with Rashut HaTkshov directives
- **Oversight:** Regular audits of government ICT systems

### Sector-Specific Coordination
INCD coordinates with sector regulators:
- **Banking:** Bank of Israel, Banking Supervision Division
- **Capital markets and securities:** Israel Securities Authority (ISA)
- **Insurance, pension and provident bodies:** Capital Market, Insurance and Savings Authority. A DIFFERENT regulator from the ISA, frequently conflated with it, and the one whose Institutional Bodies Circular 2016-9-14 governs insurer cyber risk
- **Health:** Ministry of Health, Digital Health Division
- **Energy:** Ministry of Energy, Infrastructure Protection
- **Telecom:** Ministry of Communications
- **Defense:** MALMAB (Directorate of Security of the Defense Establishment)

## Five-Pillar Cyber Defense Framework

### Pillar 1: Identify (Zihui)
**Objective:** Understand the organizational environment to manage cyber risk.

Key activities:
- **Asset inventory:** Catalog all hardware, software, data stores, and network components
- **Risk assessment:** Annual threat and vulnerability assessment
- **Supply chain mapping:** Identify all third-party dependencies and their risk profile
- **Data classification:** Categorize data by sensitivity (public, internal, confidential, restricted)
- **Business impact analysis:** Determine critical assets and acceptable downtime

### Pillar 2: Protect (Hagana)
**Objective:** Implement safeguards to ensure delivery of critical services.

Key controls:
- **Access control:** Role-based access, least privilege, MFA for privileged accounts
- **Encryption:** Data at rest and in transit encryption per classification level
- **Secure configuration:** Hardened baselines for servers, endpoints, and network devices
- **Patch management:** risk-based prioritisation, with critical patches treated as urgent. **No numeric SLA is stated here.** Earlier versions of this file gave 48 hours for critical patches and 30 days for the rest; those figures are not published by INCD and were removed on 2026-08-26 for the same reason the reporting-deadline ladder was. If an organisation needs a patch SLA, it comes from its own policy or its regulator, not from this file
- **Employee training:** Annual cybersecurity awareness training for all staff
- **Network segmentation:** Separate critical systems from general network

### Pillar 3: Detect (Gilui)
**Objective:** Identify cybersecurity events in a timely manner.

Key capabilities:
- **Continuous monitoring:** Log collection and analysis from all critical systems
- **Anomaly detection:** Behavioral analysis for unusual network and user activity
- **Threat intelligence:** Integration with CERT-IL feeds and commercial threat intel
- **Vulnerability scanning:** Regular automated scans of internal and external assets
- **Penetration testing:** Annual external penetration test (mandatory for critical infrastructure)

### Pillar 4: Respond (Tguva)
**Objective:** Take action regarding a detected cybersecurity incident.

Key procedures:
- **Incident response plan:** Documented, tested, and updated annually
- **Containment:** Procedures for isolating affected systems
- **Communication:** Internal escalation paths and external notification procedures
- **CERT-IL coordination:** Contact CERT-IL for assistance and intelligence sharing
- **Evidence preservation:** Chain of custody procedures for forensic evidence
- **Post-incident review:** lessons learned captured after incident closure. No INCD-published deadline exists for this; do not state one

### Pillar 5: Recover (Shichzur)
**Objective:** Restore capabilities and services impacted by a cybersecurity incident.

Key activities:
- **Business continuity plan:** Documented recovery procedures for all critical systems
- **Backup validation:** Regular testing of backup integrity and restoration procedures
- **DR testing:** Annual disaster recovery drill with documented results
- **Communication plan:** Stakeholder notification during and after recovery
- **Improvement cycle:** Incorporate lessons learned into preventive controls

## Critical Infrastructure Designations

INCD designates the following sectors as critical infrastructure with mandatory cybersecurity requirements:

| Sector | Examples | Lead Regulator |
|--------|----------|---------------|
| Energy | IEC, natural gas, refineries | Ministry of Energy |
| Water | Mekorot, municipal water authorities | Water Authority |
| Finance | Major banks, payment clearinghouses | Bank of Israel |
| Health | Major hospitals, HMO systems | Ministry of Health |
| Communications | Bezeq, Cellcom, Partner, HOT | Ministry of Communications |
| Transportation | Airports, ports, Israel Railways | Ministry of Transport |
| Government | Ministries, agencies, local authorities | Rashut HaTkshov |

### Obligations for Critical Infrastructure

**Read the caution before using this list.** The sector table above and the
practices below are a working picture of how critical-infrastructure supervision
operates in Israel; **they are not sourced to a published INCD instrument**, and
the designation machinery does not sit with INCD alone. Do not present any line
below as a citable legal duty, and do not tell an organisation it is designated
critical infrastructure. Whether a specific body is designated, and what it owes,
is determined through the statutory security-supervision machinery and the
organisation's own guiding body, and the organisation will know because it has
been told.

In particular, **"mandatory incident reporting to CERT-IL" was removed from this
list on 2026-08-26**, because it contradicted the corrected position in the next
section and in SKILL.md: INCD publishes no reporting deadline for any sector, and
the only binding civilian reporting statute is the Severe Cyber Attacks (Digital
Services and Hosting) Temporary Order Law, 5784-2023. A designated body's
reporting duty comes from its guiding body or sector regulator, not from this
list.

Commonly expected practices, as practice and not as cited duty:
- Risk assessment on a regular cycle, aligned to INCD methodology
- External penetration testing
- Continuous monitoring capability (SOC or equivalent)
- Participation in national cyber drills when called
- Supply chain security assessment for critical vendors

## Incident Reporting Procedures

### Reporting timeline: there isn't one, and this file used to invent it

**REMOVED 2026-08-26.** Earlier versions of this file carried a four-tier
severity ladder (Critical "within hours", High 24 hours, Medium 72 hours, Low
best effort). **No such ladder is published by INCD.** Its own reporting service
page publishes no deadline for any sector and describes the service as one that
"enables organisations and citizens to report", adding expressly that sharing
information with INCD does not substitute for a reporting duty owed to a guiding
body or regulator. The 24-hour and 72-hour figures resemble the clocks in the
**pending** National Cyber Defense bill, which is not law.

**What to say instead:**

| Question | Answer |
|---|---|
| Is there an INCD reporting deadline? | None is published. Do not state one |
| Is reporting mandatory? | For **digital-service and hosting providers**, yes: the Severe Cyber Attacks (Digital Services and Hosting) Temporary Order Law, 5784-2023, which INCD's reporting page cites. For everyone else it is voluntary |
| Where do the real clocks live? | With sector regulators: BOI Directive 366 for banks, ISA immediate reporting for listed companies, and the PPA immediate duty under regulation 11(d)(1) of the 2017 Data Security Regulations for medium and high security-level databases |
| Channel | INCD operational centre, 119, or 072-3990801, or 119@cyber.gov.il, 24/7 |

Reporting early is still good practice and CERT-IL assistance is free. Frame it
as practice, never as a deadline the organisation is breaching.

### What to Report
- Nature of the incident (type, vector, scope)
- Affected systems and data
- Current status (ongoing, contained, resolved)
- Impact assessment (data exposure, service disruption)
- Actions taken so far
- Assistance requested from CERT-IL

### CERT-IL Assistance
CERT-IL provides free assistance including:
- Incident investigation and forensic analysis
- Malware analysis
- Threat intelligence and indicators of compromise (IOCs)
- Coordination with international CERTs
- Recovery guidance

## INCD Baseline Recommendations

For organizations not designated as critical infrastructure, INCD recommends the following minimum controls:

1. **Endpoint protection:** Anti-malware on all endpoints, kept up to date
2. **Firewall:** Network firewall with deny-by-default policy
3. **Patch management:** Regular patching of OS and applications
4. **Access control:** Unique user accounts, strong passwords, MFA where possible
5. **Backup:** Regular backups stored offline or in separate network segment
6. **Email security:** Anti-phishing and anti-spam filters
7. **Awareness:** Basic cybersecurity training for all employees
8. **Incident plan:** Basic incident response procedure documented
9. **Encryption:** Encrypt sensitive data at rest and in transit
10. **Vendor management:** Assess cybersecurity posture of key vendors

## Compliance Mapping

**Annex A references below are ISO/IEC 27001:2022.** An earlier version of this file used 2013 Annex A numbering (A.9, A.16, A.17, A.12.4, A.7.2.2); the 2022 edition restructured Annex A into four themes (A.5 Organizational, A.6 People, A.7 Physical, A.8 Technological), so those control IDs no longer exist. Confirm each mapping against the standard edition you actually hold.

| INCD Requirement | ISO 27001 | SOC 2 | NIST CSF |
|-----------------|-----------|-------|----------|
| Asset inventory | A.8.1 | CC6.1 | ID.AM |
| Risk assessment | 6.1.2, A.8.2 | CC3.2 | ID.RA |
| Access control | A.5.15-A.5.18, A.8.2-A.8.5 | CC6.1-6.3 | PR.AC |
| Encryption | A.10.1 | CC6.1, CC6.7 | PR.DS |
| Monitoring | A.8.15-A.8.16 | CC7.1-7.3 | DE.CM |
| Incident response | A.5.24-A.5.28 | CC7.3-7.5 | RS.RP |
| Business continuity | A.5.29-A.5.30, A.8.14 | A1.2 | RC.RP |
| Awareness training | A.6.3 | CC1.4 | PR.AT |
