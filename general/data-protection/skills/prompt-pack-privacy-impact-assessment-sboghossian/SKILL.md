---
name: prompt-pack-privacy-impact-assessment-sboghossian
title: Privacy Impact Assessment
description: 'Use when conducting a privacy impact assessment (PIA) or data protection impact assessment (DPIA) for a new project, system, or product that processes personal data. Identifies privacy risks, assesses necessity and proportionality, evaluates safeguards, and recommends mitigating measures. MENA-aware: covers GDPR Article 35 requirements alongside UAE Personal Data Protection Law, KSA Personal Data Protection Law, and Lebanon''s data protection framework.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-privacy-impact-assessment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Privacy Impact Assessment

## When to use this

Use this skill when a company is launching a new project, system, product, or process that involves collecting, processing, sharing, or storing personal data — especially where the processing may be high-risk. The output is a structured PIA/DPIA document that can serve as internal governance documentation and, under GDPR Article 35, as a required pre-processing assessment.

**When is a DPIA mandatory under GDPR?**: Article 35 requires a DPIA before processing that is "likely to result in a high risk" to individuals, particularly:
- Systematic profiling
- Large-scale processing of special categories of data
- Systematic monitoring of publicly accessible areas
- Use of new technologies

Triggers:
- "Conduct a DPIA for our new [AI / app / platform / database] that processes [type of personal data]."
- "We're launching a new product — draft the privacy impact assessment."
- "Our DPO says we need a DPIA before we go live — build the template and complete it."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Project / system / product description | Scopes the assessment | Ask user |
| Personal data categories to be processed | Determines risk level; special categories trigger higher standard | Ask user |
| Data subjects | Who is affected: customers, employees, third parties | Ask user |
| Processing purposes | Legal basis analysis depends on purpose | Ask user |
| Data volume and geography | Volume affects proportionality; cross-border transfers require additional analysis | Ask user |
| Applicable law(s) | GDPR, UAE PDPL, KSA PDPL, or multiple | Ask user |

## Optional inputs

- Third-party processors or sub-processors involved
- Retention period
- Prior DPIAs or privacy reviews
- DPO consultation required / completed
- Risk tolerance of the organization

## PIA/DPIA document structure

---

**DATA PROTECTION IMPACT ASSESSMENT**

**Project/System name:** [Name]
**Version:** 1.0
**Date:** [Date]
**Prepared by:** [Name, Role]
**Reviewed by DPO:** [Name] / [Pending]
**Status:** [Draft / Final]

---

### Part 1: Description of the Processing

**1.1 Purpose(s) of the processing**

State the specific, explicit, and legitimate purposes for which personal data will be processed. Each purpose must have a separate legal basis.

| Processing purpose | Legal basis (GDPR) | Legal basis (UAE PDPL) | Legal basis (KSA PDPL) |
|---|---|---|---|
| [e.g., Customer identity verification] | Art. 6(1)(b) — contract performance | Contractual necessity | Contractual necessity |
| [e.g., Fraud detection and prevention] | Art. 6(1)(f) — legitimate interests | Legitimate interests | Legitimate interests |
| [e.g., Marketing communications] | Art. 6(1)(a) — consent | Explicit consent | Explicit consent |

**1.2 Nature of the processing**

Describe how personal data will be processed:
- Collection method (directly from data subjects; from third parties; from public sources)
- Storage: where and for how long
- Access controls: who within the organization has access; third-party access
- Automated decision-making: is personal data used for automated decisions with legal or similarly significant effects? (GDPR Art. 22)
- Profiling: is the system creating profiles about individuals?

**1.3 Personal data categories**

| Data category | Volume (approx.) | Sensitivity | Retention period |
|---|---|---|---|
| [Name, email, phone] | [X,000 records] | Standard | [X months after account closure] |
| [Financial data — account numbers, transaction history] | [X,000 records] | High | [X years — regulatory requirement] |
| [Health / medical data] | [If any] | Special category (GDPR Art. 9) | [Y] |
| [Biometric data] | [If any] | Special category (GDPR Art. 9) | [Y] |
| [Location data] | [If any] | High (if precise/continuous) | [Y] |

**1.4 Data subjects**

- Customers / consumers: [approximate number; geography]
- Employees: [if applicable]
- Minors: Yes / No (if yes: triggers additional legal obligations in most jurisdictions; children's data requires parental consent under GDPR, UAE PDPL)

**1.5 Recipients and transfers**

| Recipient | Purpose | Legal basis for sharing | Location / Transfer mechanism |
|---|---|---|---|
| [Cloud provider name] | Infrastructure hosting | Processor agreement (GDPR Art. 28) | [Region]; [SCCs / adequacy / BCRs] |
| [Analytics provider] | Usage analytics | Processor agreement | [EU / US / other] |
| [Marketing platform] | CRM / email | Processor agreement | [Region] |
| [Law enforcement / regulators] | Legal obligation | Art. 6(1)(c) | Per applicable law |

**International transfers (GDPR)**: If personal data is transferred outside the EEA to a non-adequate country, identify the transfer mechanism: Standard Contractual Clauses (SCCs), Binding Corporate Rules, adequacy decision, or derogation. Post-Schrems II: document the Transfer Impact Assessment (TIA) for transfers to the US or other high-risk jurisdictions.

**MENA note**: UAE and KSA PDPL both restrict cross-border transfers; transfers require either (i) recipient country's data protection framework is deemed adequate, or (ii) contractual safeguards (data transfer agreements), or (iii) data subject consent.

---

### Part 2: Necessity and Proportionality Assessment

**2.1 Necessity**: Is the processing limited to what is necessary for the stated purpose?

| Processing activity | Necessary? | Evidence of necessity | Less intrusive alternative considered? |
|---|---|---|---|
| [Collect full DOB for age verification] | Yes / No | [Legal requirement / business purpose] | [Could collect only year — less intrusive] |
| [Real-time location tracking] | Yes / No | [Purpose] | [Batch location data sufficient?] |

**2.2 Proportionality**: Is the processing proportionate to the privacy intrusion?

For special categories (health, biometric, genetic, racial origin, etc.): justify necessity explicitly; demonstrate that less intrusive alternatives are not feasible.

**2.3 Data minimization**: Is only the minimum data necessary being collected? Document any data fields that are "nice to have" vs strictly necessary and confirm only necessary fields are collected.

**2.4 Purpose limitation**: Will data collected for one purpose be used for another? If yes, assess the compatibility of the secondary purpose with the original purpose under applicable law.

---

### Part 3: Risk Identification and Assessment

For each identified risk, assess likelihood and severity, and the resulting overall risk level (Low / Medium / High / Very High).

| Risk | Description | Likelihood (1–5) | Severity (1–5) | Inherent risk level | Existing controls | Residual risk level |
|---|---|---|---|---|---|---|
| Data breach — unauthorized access | Unauthorized parties access personal data | | | | [Encryption, access controls, MFA] | |
| Excessive data collection | More data collected than necessary | | | | [Privacy-by-design review in development] | |
| Unlawful cross-border transfer | Personal data transferred without adequate safeguards | | | | [DPA with processors; SCC review] | |
| Automated decision-making without transparency | Profiling decisions not explained to data subjects | | | | [Explainability requirements in product design] | |
| Data retention beyond purpose | Data kept longer than necessary | | | | [Automated deletion policy] | |
| Profiling of special categories | Health / financial data used for profiling | | | | [Separate consent; DPO review] | |
| Minors' data processed without parental consent | Children's data collected without appropriate consent | | | | [Age verification mechanism] | |

---

### Part 4: Mitigation Measures and Recommendations

For each Medium, High, or Very High risk, state the mitigation required:

| Risk | Mitigation measure | Owner | Implementation date | Status |
|---|---|---|---|---|
| Unauthorized access | Implement end-to-end encryption; role-based access control; MFA for all admin access | IT / Security | [Date] | [Planned/In progress/Complete] |
| Excessive data collection | Remove [field X] from registration form; privacy-by-design review before go-live | Product | [Date] | |
| Cross-border transfer | Execute SCCs with [Cloud Provider]; complete TIA for US transfer | Legal | [Date] | |
| Automated profiling | Implement explainability feature; right to human review process | Product / Legal | [Date] | |
| Retention | Configure automated deletion at [X months] post-inactivity; retention schedule approved | IT / Legal | [Date] | |

---

### Part 5: Consultation

**5.1 DPO consultation**: [Name] was consulted on [Date]. DPO's opinion: [summary of DPO's advice / concerns / approval].

**5.2 Regulator consultation**: Under GDPR Article 36, prior consultation with the supervisory authority is required if the DPIA indicates Very High residual risk that cannot be mitigated. This assessment concludes that residual risk is [Low / Medium / High]. Prior consultation [is / is not] required.

**5.3 Data subject consultation**: For large-scale deployments affecting a defined group of data subjects, consultation with representatives of the affected group is recommended (not mandatory under GDPR but considered best practice).

---

### Part 6: Conclusion and Sign-off

**Overall risk rating**: [Low / Medium / High] after mitigations

**Assessment**: The proposed processing [can proceed / should be modified as follows / should not proceed as currently designed] because:
- [Key finding 1]
- [Key finding 2]

**Conditions for approval** (if any): The processing may proceed subject to completion of mitigation measures [list] by [Date].

| Role | Name | Signature | Date |
|---|---|---|---|
| Project Owner | | | |
| DPO | | | |
| Legal Counsel | | | |
| [CISO / IT Security] | | | |

---

## Jurisdictional notes

| Law | DPIA requirement | When mandatory | Regulator |
|---|---|---|---|
| **GDPR (EU/UK)** | Mandatory for high-risk processing (Art. 35) | See Article 35(3) triggers and supervisory authority lists | Local DPA (CNIL in FR; ICO in UK; etc.) |
| **UAE PDPL (Federal Decree-Law No. 45/2021)** | PIA recommended; UAE Data Office may issue guidance on when mandatory | High-risk processing involving sensitive data | UAE Data Office (TDRA) |
| **KSA PDPL** | PIA required for certain high-risk processing | Special categories; large scale; cross-border transfers | SDAIA / National Data Management Office |
| **Lebanon** | No dedicated PDPL in force as of 2026; draft law pending; applicable rules under sectoral laws (banking secrecy, telecoms) | n/a | n/a |
| **Egypt** | Data Protection Law No. 151 of 2020; DPIA not explicitly required but recommended | n/a | Ministry of Communications / NCSC |

**GDPR adequacy note**: UAE and KSA have not been granted EU adequacy decisions as of 2026. Transfers from the EEA to UAE/KSA require SCCs or other transfer mechanisms. Document the Transfer Impact Assessment (TIA) in the cross-border transfers section.

## Common mistakes

- **Conducting the DPIA after go-live**: a DPIA must be completed before processing begins for high-risk processing; a retrospective DPIA after a system is live is a compliance breach.
- **Treating all risks as Low to avoid DPO escalation**: genuine High and Very High risks require mitigation or prior consultation with the supervisory authority; under-assessing risks creates liability.
- **No DPO sign-off where required**: GDPR requires DPO consultation; failing to involve the DPO is a procedural violation.
- **Ignoring cross-border transfer requirements**: many MENA organizations transfer data to US cloud providers without SCCs in place; this is a material GDPR breach risk for companies with EU customers or employees.
- **No review cycle**: DPIAs should be reviewed when the system or the law materially changes; a one-time DPIA that is never updated becomes stale and ineffective.

## Related skills

- [[prompt-pack-open-banking-api-terms]]
- [[prompt-pack-lending-platform-terms]]
- [[prompt-pack-payment-services-agreement]]
- [[prompt-pack-legal-hold-management-procedure]]
- [[heuristic-always-state-jurisdiction-first]]
