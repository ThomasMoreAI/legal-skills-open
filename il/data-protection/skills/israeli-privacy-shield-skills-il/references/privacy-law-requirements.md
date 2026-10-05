# Israeli Privacy Protection Law (Post Amendment 13): Detailed Requirements

## Overview
The Protection of Privacy Law, 5741-1981 (Chok Haganat HaPratiut) is Israel's primary
data protection legislation. It is supplemented by the Privacy Protection (Data Security)
Regulations of 2017 and was comprehensively overhauled by Amendment 13, which the Knesset
approved by the Knesset in early August 2024 (sources disagree between the 5th and the 8th, and the exact day is NOT verified here; the date that governs is the in-force date) and which came into force on August 14, 2025. Amendment 13
narrowed database registration, added
a mandatory Privacy Protection Officer (DPO) obligation, expanded the definition of
personal data to cover online identifiers, and significantly increased enforcement powers
and administrative fines.

## Enforcement Authority
- **Privacy Protection Authority (PPA)** (Rashut LeHaganat HaPratiut)
- Under the Ministry of Justice
- Website: https://www.gov.il/en/departments/the_privacy_protection_authority
- Amendment 13 powers: unannounced supervisory inspections, binding compliance orders,
  and administrative fines reaching millions of shekels (with multipliers for large-scale
  or sensitive-data databases), on top of existing criminal liability

## Database Registration Requirements (Amendment 13 regime)

### When Registration is Required
Amendment 13 narrowed registration. A database must be registered with the PPA only if:
1. It is owned or managed by a public body, OR
2. It contains data on more than 10,000 individuals AND its main purpose is collecting
   personal data in order to disclose it to third parties as a business or for value,
   including direct-mailing services (a data broker)

The broad pre-Amendment triggers (any database with sensitive data, credit-information
services, health/genetics/financial data, direct marketing) and the old "Form 1"
five-trigger model no longer apply.

### Notification Tier for Large Sensitive Databases
Separately from registration, a controller of a database that is NOT subject to
registration but holds especially-sensitive data on more than 100,000 individuals must
submit a notification to the PPA within 30 days. The notification includes:
- The controller's identity, address, and contact details
- The Privacy Protection Officer's identity and contact details (if one is required)
- A copy of the database definition document prepared under the Data Security Regulations

### Registration / Notification Process
1. File through the PPA at https://www.gov.il/en/departments/the_privacy_protection_authority
2. Include: database name, purpose, types of data, data sources, recipients, and the
   database definition document
3. Changes to database purpose or scope require an updated filing

## Security Levels and Requirements

### Basic Level
Applies to: Databases with fewer than 10,000 records containing non-sensitive data

Requirements:
- Physical security of premises
- Access control (user authentication)
- Activity logging
- Backup procedures
- Written security procedures document
- Employee awareness

### Medium Level
Applies to: Databases with 10,000+ records OR containing sensitive data

Additional requirements beyond Basic:
- Encryption of data at rest and in transit
- Appointment of a security officer (memune al bitachon meida)
- Periodic access review
- Enhanced logging and monitoring
- Incident response procedures
- Third-party access controls
- Data processing agreements with service providers

### High Level
Applies to: Government databases, health data, financial data, databases with 100,000+
records, or intermediate-level databases that grant authorized access to more than 100 people

Additional requirements beyond Medium:
- A security risk assessment at least once every 18 months
- A penetration test of the database systems at least once every 18 months, with the
  results discussed and the faults found remediated and documented
- Comprehensive incident response plan
- Data Protection Officer (DPO) appointment
- Advanced encryption standards
- Detailed data flow mapping
- Regular employee training program
- Business continuity plan

## Privacy Protection Officer (DPO): Amendment 13

Amendment 13 added a mandatory DPO obligation. A DPO must be appointed by:
- Public bodies (government ministries, municipalities, universities, HMOs, etc.),
  except national-security entities, and processors acting for those public bodies
- Data brokers: a controller whose database holds personal data on more than 10,000
  individuals and whose main purpose is collecting personal data to disclose it to third
  parties as a business or for value
- Entities that systematically monitor individuals on a large scale, or whose core
  business includes processing especially-sensitive data on a large scale

The DPO is the contact point with the PPA and monitors compliance. The PPA announced it
would not enforce the appointment obligation until October 31, 2025.

## Consent Requirements

### Valid Consent Must Be
- **Informed:** Data subject knows what data is collected and for what purpose
- **Specific:** Consent for each distinct purpose of processing
- **Freely given:** No undue pressure or bundling with unrelated services
- **Documentable:** Organization must be able to demonstrate consent was obtained

### When Consent is Required
- Initial collection of personal data
- Any use beyond the originally stated purpose
- Transfer of data to third parties
- Cross-border transfer of data
- Processing of sensitive data categories

### Consent Exceptions
Consent is not required when:
- Processing is required by law
- Processing is necessary to protect vital interests
- Processing is in the public interest
- Processing is necessary for performance of a contract
- Limited legitimate interest exception (interpreted narrowly by Israeli courts)

## Cross-Border Data Transfer

### General Rule
Personal data may not be transferred outside Israel unless the recipient country
provides adequate protection for personal data.

### Countries with Adequate Protection
- European Union member states. NOTE the direction: they are on the Israeli whitelist for outbound transfers; the EU adequacy decision separately authorises transfers FROM the EU TO Israel and is not the basis for an outbound Israeli transfer
- United Kingdom
- Other countries recognized by the Privacy Protection Authority

### Transfer Without Adequacy
Transfers to countries without adequate protection are permitted if:
- Data subject has given informed consent to the specific transfer
- Transfer is necessary for contract performance
- Transfer is necessary for legal proceedings
- Transfer is necessary to protect vital interests
- Contractual safeguards are in place (similar to EU Standard Contractual Clauses)

## Breach Notification (Amendment 13 regime)

### What Constitutes a Reportable Breach
Amendment 13 reframed the trigger. A reportable breach is an incident that poses a risk
to the rights and freedoms of affected individuals, including:
- Unauthorized access to personal data
- Unauthorized disclosure of personal data
- Loss, alteration, or destruction of personal data

### Notification to the Authority
- A "Severe Security Incident" must be reported to the Privacy Protection Authority
  **immediately** (miyad) upon discovery, per the Data Security Regulations (2017). There is
  NO fixed 72-hour deadline in Israeli law (do not import GDPR's 72 hours); the PPA may then
  direct the controller to notify affected data subjects.
- Must include: the nature of the breach, the categories and approximate number of
  affected individuals, the likely consequences, and the measures taken or proposed

### Notification to Data Subjects
- Required **when the PPA directs the controller to notify** after the incident is
  reported (Israeli Data Security Regulations), NOT on the controller's own GDPR-style
  "high risk" self-assessment
- Must be in clear, concise, plain language (Hebrew) and explain: the nature of the
  breach, the types of data affected, the potential consequences, contact details for
  more information, and the protective steps individuals can take

### Documentation
- All security incidents must be documented regardless of whether they cross the
  reporting threshold
- Documentation must include: timeline, scope, response actions, decisions, lessons learned
- Retain documentation per the controller's broader retention policy and consistent with
  enforcement-defensibility (PPA inspections under Amendment 13 may request historical records)

## Penalties

### Criminal Penalties
- Violations of the Privacy Protection Law can result in criminal prosecution
- Maximum penalties: Up to 5 years imprisonment for severe violations
- Fines as determined by criminal court

### Civil Liability
- Data subjects may sue for damages resulting from privacy violations
- Compensation for non-material damage (emotional distress) is available
- Class actions are possible for widespread violations

### Administrative Enforcement
- Privacy Protection Authority can issue orders and impose conditions
- Authority can require corrective measures
- Authority can publicize violations (naming and shaming)

## GDPR Comparison Notes (Post Amendment 13)

### Areas Where Israeli Law is Stricter or Distinct
- Database registration requirement still exists (no GDPR equivalent since ROPA replaced
  it), though Amendment 13 narrowed it to public bodies and data brokers, plus a separate
  100,000-record especially-sensitive notification tier
- Criminal penalties for privacy violations (up to 5 years imprisonment)

### Areas Where the Two Frameworks Now Converge
- Breach notification: Israel requires "immediate" notification of a Severe Security
  Incident to the PPA (Data Security Regulations 2017), which DIFFERS from GDPR's fixed
  72-hour rule. The PPA may direct notification to affected data subjects; this is a point
  of divergence from GDPR, not convergence
- Personal data scope: Amendment 13 expressly includes online identifiers (IP addresses,
  geolocation, device identifiers), aligning with GDPR Recital 30
- DPO obligation: Amendment 13 added a mandatory DPO requirement, though the Israeli
  triggers (public bodies, data brokers, large-scale monitoring/sensitive processing) are
  framed more narrowly than GDPR Article 37

### Areas Where GDPR is Still Stricter
- Higher financial penalties (up to 4% of global annual revenue)
- Broader extra-territorial application
- More comprehensive right to erasure (right to be forgotten)
- More detailed lawful basis framework (6 legal bases vs. consent-primary)
- Data Protection Impact Assessment requirement
- Privacy by Design and by Default as explicit legal requirements

### Key Practical Differences for Multinational Companies
- Companies operating in both Israel and EU must comply with both frameworks
- Israeli adequacy decision means data flows from EU to Israel are generally permitted
- Israeli companies processing EU residents' data must comply with GDPR
- Recommended approach: comply with the stricter requirement in each area

## Amendment 13 detail moved from SKILL.md (AI governance, enforcement powers, fines)

**AI governance for automated decision-making.** Amendment 13 requires transparency and oversight for AI systems that make decisions affecting individuals (credit scoring, hiring, insurance, fraud detection). Requirements include:
- Documentation of the decision logic and data inputs
- Ability to explain outcomes to affected individuals
- Human oversight for high-impact decisions
- Bias and accuracy monitoring

**Enforcement powers and fines.** Amendment 13 significantly expands the Authority's administrative powers:
- Direct supervisory inspections without prior notice
- Administrative fines are set per violation by the statute, not as a single ceiling. Section 23כו(a) sets NIS 150,000 for the listed violations (processing in an unregistered database that required registration, failing to notify a notifiable database, running a direct-mail database unregistered, and similar), and the head of the Authority may impose DOUBLE that amount where the database holds personal information on 1,000,000 people or more. Other schedule items carry their own amounts, including NIS 320,000 for specified breaches of the Data Security Regulations and NIS 30,000 for lighter ones.
- Two different per-person schedules apply, and they are easy to conflate. For unlawful APPROACHES and direct-mail violations (Section 23כו(c)(1)) the fine is NIS 50 multiplied by the number of people approached, rising to NIS 100 per person where the approach concerned specially-sensitive information, with a floor of NIS 30,000 if that multiplication comes to less. For the Section 23כו(d)(1) violations the fine is NIS 2 for each person whose personal information is in the database, or NIS 4 per person where the information is specially sensitive.
- The 5% ceiling is a REDUCTION mechanism, not a headline fine: on the violator's request, where the penalty exceeds 5% of their turnover the head of the Authority reduces it to 5% of turnover. A violator with no turnover does not get that reduction.
- A private civil right of action under **Section 15א** ("פיצויים לדוגמה"): a court may award damages not dependent on proof of harm, up to **NIS 10,000** per violation, for the violations listed there. Some of them require the data subject to have first approached the controller and waited a set period (90 days for the registration case).
- Ability to issue binding compliance orders


**Recent enforcement, and it has moved from individuals to organisations.**

- **July 2026, Meuhedet (health fund), NIS 256,000** for failing the immediate-reporting duty, the FIRST such penalty since Amendment 13 took effect. A technological fault let some members view relatives' medical records; the fund knew in November 2025 and reported only at the end of January 2026, about two months after the member who first reported it. The fine is stated as the figure after the reductions the law provides for.
- **August 2026, A.D. Karting Hutzot (2014) Ltd, NIS 12,000** for breaching the notification duty at the point of collection under section 11 of the Law. Small fines for basic transparency failures are now being issued.
- The PPA also fined an individual (a former National Insurance Institute employee) NIS 75,000 for unauthorized retrieval of sensitive data from Bituach Leumi databases.

Enforcement is live, it reaches large regulated bodies, and the health fund case shows the reporting duty being enforced on its own, without any finding about the underlying security failure.

**What changed for database registration.** Amendment 13 narrowed registration to public bodies and to data brokers (databases of 10,000+ individuals whose primary purpose is selling/disclosing personal data to third parties). The broad pre-Amendment "any sensitive database" rule no longer applies. The separate 100,000-record especially-sensitive notification tier (file with the Authority within 30 days) is described above.



## DPIA detail moved from SKILL.md

### Step 9: Data Protection Impact Assessment (DPIA)

A DPIA is a structured pre-processing assessment that documents privacy risks, alternatives considered, and mitigations. The PPL does not contain a GDPR-Article-35-style explicit DPIA mandate, but the PPA's published guidance on AI systems treats DPIA as the recommended best practice for demonstrating compliance. Where a Privacy Protection Officer is appointed under Amendment 13, the PPO is the natural owner of the DPIA process as part of monitoring overall compliance.

**When to conduct a DPIA (PPA AI Guidelines + Amendment 13 framing):**
- Before deploying AI systems that process data on a wide scale
- Before deploying AI systems that include sensitive data
- Before deploying processing that poses high risk to data subjects' rights
- Before large-scale systematic monitoring of individuals (CCTV at scale, location tracking, behavioral profiling)
- Before automated decisions affecting individuals (credit, hiring, insurance, fraud detection)

**DPIA contents:**
1. Description of the processing: purpose, data categories, data sources, retention, recipients
2. Necessity and proportionality: is each category necessary for the stated purpose?
3. Risks to data subjects: probability + severity, including bias and discrimination for AI systems
4. Mitigations: technical (encryption, access controls, minimization) and organizational (training, audit)
5. Residual risk: what remains after mitigations and whether it is acceptable
6. Consultation: with the PPO and, for high residual risk, optional prior consultation with the PPA
7. Sign-off and review cycle (annual or on material change)

Keep DPIAs in the documentation evidence pack. The PPA's unannounced inspection powers under Amendment 13 mean an undocumented DPIA is functionally a missing DPIA.


