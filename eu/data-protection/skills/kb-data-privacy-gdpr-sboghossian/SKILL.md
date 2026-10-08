---
name: kb-data-privacy-gdpr-sboghossian
title: Knowledge Pack — GDPR (EU 2016/679) and UK GDPR
description: Use when a matter involves EU or UK data protection law, including GDPR compliance, lawful bases for processing, data subject rights, DPO obligations, international transfers, breach notification, or supervisory authority engagement. Also use when comparing GDPR requirements against MENA-region privacy laws (Egypt, KSA PDPL, UAE PDPL) for cross-border operations. Priority P0 reference for any EU/UK-data-touching transaction.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-data-privacy-gdpr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# Knowledge Pack — GDPR (EU 2016/679) and UK GDPR

## Scope

The **General Data Protection Regulation (Regulation EU 2016/679)** applies to:

- Processing of **personal data** of **EU residents** (data subjects located in the EU at the time of processing), regardless of where the processing organization is established.
- Organizations **established** in the EU/EEA.
- Organizations **outside the EU** that:
  - Offer goods or services to EU residents (even for free), or
  - Monitor the behavior of EU residents.

The **UK GDPR** (retained after Brexit; amended by the UK Data Protection Act 2018) applies the same framework to UK residents. Post-Brexit, the EU and UK operate independent regimes; adequacy decisions exist between them but may be reviewed.

## Roles and Accountability

| Role | Definition | Key Obligation |
|---|---|---|
| Controller | Determines purposes and means of processing | Full GDPR compliance; appoints processor via DPA |
| Processor | Processes on controller's behalf | Only acts on controller instructions; Art 28 contract |
| Joint controllers | Jointly determine purposes and means | Agree on and publish roles and responsibilities (Art 26) |
| Data subject | Identified/identifiable natural person | Rights under Arts 15–22 |
| DPO | Data Protection Officer | Advise, monitor, cooperate with supervisory authority |

## Lawful Bases for Processing (Art 6)

1. **Consent** — specific, informed, freely given, unambiguous, withdrawable at any time. Not valid if conditioned on service delivery (bundled consent).
2. **Contract** — necessary to perform a contract with the data subject, or pre-contractual steps at their request.
3. **Legal obligation** — required by EU or Member State law.
4. **Vital interests** — protect the life of the data subject or a third party; used narrowly.
5. **Public task** — exercise of official authority or a task in the public interest vested by law.
6. **Legitimate interests (Art 6(1)(f))** — controller's or third party's interests, provided not overridden by data subject's fundamental rights. Requires documented balancing test. **Not available for public authorities** in their public-task capacity.

### Practical note for MENA-headquartered organizations
Organizations operating from KSA, UAE, or Lebanon that process EU personal data (e.g., EU client data, EU employee data) must comply with GDPR. They must designate an **EU representative** (Art 27) unless an EU establishment already exists.

## Special Category Data (Art 9)

Requires **explicit consent** or specific statutory exemptions:
- Health and medical data
- Genetic data
- Biometric data (for identification purposes)
- Racial or ethnic origin
- Religious or philosophical beliefs
- Political opinions
- Trade-union membership
- Sexual orientation and gender identity

Processing of **criminal conviction and offence data** (Art 10) subject to similar heightened restrictions.

## Data Subject Rights

| Right | Article | Deadline | Notes |
|---|---|---|---|
| Access (Subject Access Request) | Art 15 | 1 month | Extendable +2 months for complexity |
| Rectification | Art 16 | 1 month | |
| Erasure ("right to be forgotten") | Art 17 | 1 month | Subject to exceptions (legal obligation, public interest, legal claims) |
| Restriction | Art 18 | Without undue delay | Suspend processing while dispute resolved |
| Data portability | Art 20 | 1 month | Machine-readable format; only for consent/contract basis |
| Objection | Art 21 | Immediately | Stop processing unless compelling grounds; absolute right for direct marketing |
| No automated decisions | Art 22 | — | Applies to solely automated decisions with significant effect |

## Data Protection Officer (DPO)

**Mandatory when**:
- Public authority or body (with limited exceptions)
- Core activities = **large-scale regular and systematic monitoring** of data subjects
- Core activities = **large-scale processing of special category data**

DPO must:
- Have expert knowledge of data protection law
- Report directly to highest management level
- Be functionally independent (cannot be instructed)
- Register with supervisory authority
- Be accessible to data subjects

## Privacy by Design and by Default (Art 25)

- Privacy protections must be built into systems and processes from the outset.
- Default settings must be data-minimization compliant (only necessary data processed by default).
- Documented in Records of Processing Activities (RoPA).

## Records of Processing Activities (Art 30)

All controllers with 250+ employees **or** processing that is not occasional, or involves special category / criminal data must maintain a written RoPA including:
- Controller's name and contact
- Processing purposes
- Categories of data subjects and data
- Recipients
- International transfer safeguards
- Retention periods
- Security measures

## Data Protection Impact Assessment (DPIA) (Art 35)

Required **before** commencing high-risk processing, including:
- Large-scale processing of special category data
- Systematic and extensive automated profiling
- Large-scale public monitoring (CCTV, tracking)
- Novel technologies with high privacy risk

DPIA must be consulted with supervisory authority if residual risk remains high (prior consultation, Art 36).

## International Transfers (Chapter V)

Personal data may only be transferred outside the EU/EEA to a third country if one of the following applies:

| Mechanism | Description |
|---|---|
| Adequacy decision (Art 45) | European Commission has determined the country provides adequate protection (UK, Switzerland, Japan, South Korea, UAE-DIFC and Abu Dhabi ADGM, Canada PIPEDA, etc.) |
| Standard Contractual Clauses (SCCs) (Art 46) | EU-approved model contracts (2021 version in 4 modules) |
| Binding Corporate Rules (BCRs) (Art 47) | Intra-group policies approved by lead supervisory authority |
| Codes of conduct / certification (Art 46) | Approved sector or certification scheme |
| Derogations (Art 49) | Explicit consent; contract performance; public interest; legal claims; vital interests — narrow use |

**Important for MENA**: DIFC (Dubai) and ADGM (Abu Dhabi) have EU adequacy decisions; UAE onshore, KSA, Egypt, and Lebanon do **not**. Transfers to KSA, Egypt, Lebanon must use SCCs or another mechanism.

## Breach Notification (Arts 33–34)

| Obligation | Deadline | Threshold |
|---|---|---|
| Notify supervisory authority | 72 hours from awareness | Any breach likely to result in risk to individuals |
| Notify data subjects | Without undue delay | Breach likely to result in **high** risk to individuals |

Breach register mandatory; all incidents documented (even those not reported externally).

## Penalties (Art 83)

| Tier | Maximum Penalty | Examples |
|---|---|---|
| Lower tier | €10M or 2% global annual turnover (higher) | RoPA breaches; processor DPA; DPIA |
| Upper tier | €20M or 4% global annual turnover (higher) | Unlawful processing; special category violations; international transfers; data subject rights |

**UK GDPR** (from 2024 ICO updated framework): £17.5M or 4% global annual turnover (higher).

Supervisory authorities may also issue warnings, reprimands, temporary/permanent bans on processing.

## Supervisory Authorities

- **EU**: each Member State designates one or more national Data Protection Authorities (DPAs).
- **One-stop-shop**: organizations with a main EU establishment deal primarily with that Member State's DPA (lead DPA). Cross-border processing triggers consistency mechanism.
- **UK**: Information Commissioner's Office (ICO) — independent from EU post-Brexit.
- Data subjects may complain to the DPA of their habitual residence, place of work, or place of the alleged infringement.

## UK GDPR Specifics

| Feature | UK GDPR |
|---|---|
| Maximum fine | £17.5M or 4% global turnover |
| Supervisory authority | ICO |
| EU/UK transfers | EU → UK: adequacy decision (under review); UK → EU: UK domestic adequacy decision for EU |
| SCCs | UK has its own IDTA (International Data Transfer Agreement) and UK addendum to EU SCCs |
| Future reform | UK Data Reform Act anticipated; ICO has published updated guidance |

## How to Use This Pack

When advising on GDPR compliance:
1. Establish whether GDPR applies (EU establishment or extra-territorial scope).
2. Identify the role (controller / processor / joint controller).
3. Map processing activities and identify the lawful basis for each.
4. Check for special-category or criminal data — higher bar.
5. Review or create RoPA (Art 30).
6. Assess DPO requirement.
7. Review international transfer mechanisms (critical for MENA organizations).
8. Check breach notification procedure is in place.
9. Verify data subject rights procedures are operational.

## Caveats & Currency

GDPR has been in force since May 2018. Supervisory authority guidance, EDPB (European Data Protection Board) opinions, and national DPA decisions continually develop the interpretation of key provisions. Verify:
- Current EU adequacy decisions (UK adequacy is time-limited and under review).
- EU SCCs version (2021 modules replaced the 2010 standard clauses).
- UK IDTA vs UK addendum — standard form issued by ICO.
- Member State national derogations (permitted under GDPR Arts 85–91 for specific sectors).

## Related Skills

- [[kb-data-privacy-egypt]]
- [[kb-data-privacy-ksa-pdpl]]
- [[kb-data-privacy-uae-pdpl]]
- [[kb-healthcare-regulation-mena]]
- [[draft-data-processing-agreement]]
- [[draft-privacy-policy]]
