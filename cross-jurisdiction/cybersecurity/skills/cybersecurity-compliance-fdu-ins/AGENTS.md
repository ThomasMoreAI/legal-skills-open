# Cybersecurity Compliance

> **Disclaimer**: This skill provides general educational information about legal topics relevant to software development. It is **not legal advice**. Laws vary by jurisdiction and change frequently. Always consult a qualified attorney licensed in the relevant jurisdiction before making legal decisions for your organization.

## Overview

Cybersecurity is no longer just a technical concern — it is a regulated activity. Mandatory incident reporting, board-level accountability, and third-party risk requirements are expanding globally. Organizations that experience a cyber incident face not only the technical challenge of response and recovery but also a complex web of legal obligations with strict timelines. Failure to comply with these obligations can result in penalties that compound the damage of the underlying incident. Understanding your reporting obligations, certification requirements, and insurance coverage before an incident occurs is essential.

## Cybersecurity Regulations

| Regulation | Jurisdiction | Scope | Key Requirements | Effective |
|---|---|---|---|---|
| **NIS2 Directive** | EU | Essential + important entities across 18 sectors | Risk management measures, 24hr incident reporting, supply chain security, board accountability | October 2024 |
| **DORA** | EU | Financial entities + ICT providers | ICT risk management, incident reporting, resilience testing, third-party risk management | January 2025 |
| **SEC Cyber Disclosure Rules** | US | Public companies | Material incident disclosure within 4 business days on Form 8-K, annual risk management disclosure | December 2023 |
| **CISA Incident Reporting (CIRCIA)** | US | Critical infrastructure | 72hr incident reporting, 24hr ransomware payment reporting | Rules being finalized |
| **State Breach Notification Laws** | US (all 50 states) | Organizations with residents' data | Notification to affected individuals + state AG within specified timeframes | Varies by state — some as short as 30 days |
| **PSTI Act** | UK | Consumer IoT devices | No default passwords, vulnerability disclosure policy, defined support period | April 2024 |
| **CER Directive** | EU | Critical entities | Risk assessment, resilience measures, incident notification | October 2024 |

## Breach Notification Timelines

One of the most critical aspects of cybersecurity compliance is understanding **how quickly you must report** an incident and **to whom**. These timelines begin running from the moment you become aware of the incident, making rapid detection and assessment capabilities essential.

| Jurisdiction / Law | Timeline | Notify Whom | Trigger |
|---|---|---|---|
| **GDPR** | 72 hours | Supervisory authority + data subjects if high risk | Personal data breach |
| **NIS2** | 24hr early warning + 72hr notification + 1 month final report | CSIRT / competent authority | Significant incident |
| **HIPAA** | 60 days | HHS + individuals + media if >500 affected | PHI breach |
| **SEC** | 4 business days | SEC on Form 8-K | Material cybersecurity incident |
| **California** | Expedient, without unreasonable delay | AG + individuals | Personal information breach |
| **Australia** | 30 days assessment + notification | OAIC + individuals | Eligible data breach |

**Key considerations:**
- Multiple notification obligations can be triggered by a single incident. A data breach affecting EU residents' personal data that also constitutes a significant NIS2 incident requires parallel notifications under both GDPR and NIS2 with different timelines and recipients.
- The definition of "awareness" or "discovery" that starts the clock varies by jurisdiction. Some laws start the clock when you reasonably should have known, not when you actually confirmed.
- Late notification can itself be a separate violation carrying its own penalties.

## Security Certifications and Frameworks

Many customers, partners, and regulators require evidence of your security posture through formal certifications or audit reports. Choosing the right framework depends on your market, customer base, and regulatory environment.

| Framework | Type | Scope | Who Needs It |
|---|---|---|---|
| **SOC 2** | Audit report (Type I or Type II) | Service organizations | SaaS vendors selling to enterprises |
| **ISO 27001** | Certifiable international standard | Any organization | Global enterprises, particularly in EU and APAC |
| **FedRAMP** | US federal government authorization | Cloud services for federal agencies | US government contractors and cloud providers |
| **StateRAMP** | State government authorization | Cloud services for state/local government | State and local government contractors |
| **CMMC** | DoD certification (Levels 1-3) | Defense contractors | US defense supply chain |
| **TISAX** | Automotive industry certification | Automotive supply chain | Automotive suppliers and partners |
| **HDS** | Healthcare hosting certification | Healthcare data hosting in France | Organizations hosting healthcare data in France |

**SOC 2 vs. ISO 27001:** SOC 2 is dominant in North America and focuses on controls relevant to service organizations (security, availability, processing integrity, confidentiality, privacy). ISO 27001 is more widely recognized internationally and provides a certifiable information security management system (ISMS). Many organizations pursue both.

**FedRAMP:** If you sell cloud services to US federal agencies, FedRAMP authorization is effectively mandatory. The process is rigorous and can take 12-18 months. FedRAMP Rev 5 aligns with NIST SP 800-53 Rev 5 controls. The FedRAMP authorization boundary must be clearly defined and all components within it must meet the required control baselines (Low, Moderate, or High).

**CMMC:** The Cybersecurity Maturity Model Certification is required for Department of Defense contractors. CMMC 2.0 simplified the model to three levels: Level 1 (foundational, self-assessment), Level 2 (advanced, third-party assessment for critical programs), and Level 3 (expert, government-led assessment). Level 2 aligns with NIST SP 800-171.

## Cyber Insurance

Cyber insurance has become an important component of organizational risk management, and insurers are increasingly prescriptive about the security controls they require.

**What cyber insurance typically covers:**

- **First-party coverage** — Direct costs to your organization: incident response and forensics, business interruption losses, data recovery costs, ransomware payments (where legal), notification costs, credit monitoring for affected individuals, public relations and crisis management.
- **Third-party coverage** — Claims from others: regulatory fines and penalties (where insurable), legal defense costs, settlements and judgments from lawsuits, media liability.

**Common insurer requirements:**

Insurers increasingly require specific security controls as a condition of coverage. Failure to maintain these controls can void your policy or result in claim denial:

- **Multi-factor authentication (MFA)** on all remote access, email, and privileged accounts
- **Endpoint detection and response (EDR)** deployed across all endpoints
- **Regular, tested backups** with offline or immutable copies
- **Documented incident response plan** that is tested at least annually
- **Employee security awareness training** conducted regularly
- **Patch management program** with defined timelines for critical vulnerabilities
- **Privileged access management** with least-privilege principles
- **Email security** including anti-phishing controls

**Premium factors:** Premiums are influenced by industry, revenue, data volume, security maturity, claims history, and the specific controls you have in place. Organizations with strong security postures and certifications (SOC 2, ISO 27001) often receive more favorable terms.

## Incident Response Plan

Multiple regulations now **legally require** organizations to maintain and test an incident response plan. Beyond regulatory compliance, a well-prepared incident response capability dramatically reduces the cost and impact of security incidents.

**Regulations requiring incident response plans:**

- NIS2 (Article 21 — incident handling)
- DORA (Article 17 — ICT-related incident management process)
- HIPAA Security Rule (§164.308(a)(6) — security incident procedures)
- PCI DSS v4.0 (Requirement 12.10 — incident response plan)
- NIST Cybersecurity Framework (Respond function)
- Many state breach notification laws implicitly require response readiness

**Key components of a compliant incident response plan:**

1. **Detection and analysis** — How incidents are identified, classified by severity, and triaged. Define what constitutes a reportable incident under each applicable regulation.
2. **Containment** — Immediate actions to limit the scope and impact of the incident. Short-term containment (isolate affected systems) and long-term containment (apply fixes while maintaining business operations).
3. **Legal notification and regulatory coordination** — Mapped timelines and procedures for every applicable notification obligation. Legal counsel should be involved immediately to manage privilege and direct the response.
4. **Forensic investigation** — Evidence preservation, chain of custody, root cause analysis. Use qualified forensic investigators, and be aware that forensic reports may be discoverable in litigation unless properly protected by attorney-client privilege.
5. **Eradication and recovery** — Remove the threat, restore affected systems, verify integrity, and return to normal operations with enhanced monitoring.
6. **Post-incident review and lessons learned** — Document what happened, what worked, what did not, and what changes are needed. Many regulations (NIS2, DORA) require formal post-incident reports.

**Critical legal consideration:** Involve legal counsel at the start of any incident response, not at the end. Communications during incident response may be discoverable in subsequent litigation or regulatory proceedings. Structuring the response under attorney-client privilege can protect sensitive assessments and recommendations.

## Best Practices

- **Recognize that cyber incidents trigger mandatory legal obligations, and legal counsel should be part of the incident response team from the first moment.** Delaying legal involvement can result in missed notification deadlines, waived privilege, and increased liability.
- **Map all of your notification obligations before an incident occurs.** Create a matrix of every regulation, customer contract, and insurance policy that imposes notification requirements, including timelines, recipients, content requirements, and methods. Do not try to figure this out during the chaos of an active incident.
- **Pursue security certifications strategically based on your market.** SOC 2 for North American enterprise sales, ISO 27001 for international markets, FedRAMP for US government, CMMC for defense. These certifications also demonstrate due diligence in regulatory and litigation contexts.
- **Test your incident response plan at least annually through tabletop exercises.** Include technical staff, legal counsel, executive leadership, and communications teams. Simulate scenarios that trigger multiple notification obligations simultaneously.
- **Maintain cyber insurance and understand your policy's conditions and exclusions.** Review your policy annually, ensure you are meeting all required security controls, and understand what is and is not covered — particularly regarding ransomware, nation-state attacks, and war exclusions.
- **Monitor the regulatory landscape actively.** NIS2 transposition into national laws, CIRCIA final rules, and evolving SEC enforcement priorities are all creating new obligations. Assign responsibility for tracking regulatory changes to a specific role.
- **Implement board-level cybersecurity governance.** NIS2 and SEC rules explicitly require board or management body accountability for cybersecurity. Ensure regular reporting to the board, documented risk acceptance decisions, and management training on cyber risk.
- **Treat third-party risk management as a regulatory requirement, not just a best practice.** NIS2, DORA, and many industry frameworks require formal assessment and ongoing monitoring of your supply chain's cybersecurity posture. Maintain an inventory of critical suppliers and their security certifications.
