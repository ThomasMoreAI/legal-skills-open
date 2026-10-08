---
name: draft-compliance-manual-sboghossian
title: Draft — Compliance Manual
description: Use when asked to draft a compliance manual for a regulated business — a comprehensive internal policy document covering regulatory framework, roles and responsibilities (compliance officer, MLRO, board), key policies (AML, sanctions, data, conduct), training, reporting and escalation, audit, and sanction protocols. Applicable to financial services, fintech, professional services firms, and any business subject to MENA, EU, or US regulatory oversight.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-compliance-manual
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Draft — Compliance Manual

## When to use this

Use this skill when a regulated business needs a comprehensive internal compliance manual — the master governance document that:
- Summarizes all applicable regulatory frameworks in one place.
- Assigns ownership and accountability for each compliance obligation.
- Consolidates policies (AML, sanctions, data privacy, conduct of business) by reference or in full.
- Provides the documented framework that regulators and auditors expect to review.

A compliance manual is distinct from individual policies (AML policy, privacy policy): it is the overarching document that explains *how* all the policies fit together and *who* is responsible for what.

## Required inputs

| Input | Notes |
|---|---|
| Entity type and regulated activities | Bank, NBFI, broker-dealer, payment institution, law firm, real estate agent, etc. |
| Regulatory jurisdiction(s) | Determines which framework summaries and regulators to include |
| Compliance team structure | Compliance Officer, MLRO, Deputy; reporting lines |
| Board oversight structure | Compliance Committee or Risk Committee of the Board |
| Existing policies | List of stand-alone policies to cross-reference |
| Reporting cycle | Annual compliance report to board; quarterly to management |

## Document structure

### Chapter 1 — Purpose and scope

**Purpose**: This Compliance Manual establishes [Company Name]'s compliance framework and sets out the obligations of all staff and management in relation to regulatory compliance.

**Scope**: Applies to [all employees / all staff and contractors / all group entities named in Schedule 1]. Includes physical and virtual operations.

**Effective date**: [Date]. Review cycle: annual (or upon material regulatory change).

**Board approval**: This manual has been approved by the Board of Directors / Compliance Committee on [Date].

### Chapter 2 — Regulatory framework summary

For each applicable regulatory regime:
- Regulator identity and jurisdiction.
- Primary legal instruments (statute, regulation, rulebook).
- License / authorization held.
- Key obligations in summary.
- Reporting deadlines to the regulator.

**Template per jurisdiction**:

| Regime | Regulator | Primary law | License | Key obligations |
|---|---|---|---|---|
| UAE CBUAE | Central Bank UAE | Federal Decree-Law 20/2018 (AML) + CBUAE Regulations | Licensed payment institution | AML program; goAML registration; STR filing |
| DIFC DFSA | DFSA | DFSA Rulebook (GEN, AML modules) | Category 3C (Arranging) | Annual DFSA compliance return; AML module compliance |
| KSA SAMA | SAMA | SAMA AML/CFT Rules | Banking license | Annual compliance report; SAFIU STR filing |
| EU | National regulator | 6AMLD; PSD2; GDPR | PSD2 license | AML program; data protection; periodic reporting |

### Chapter 3 — Roles and responsibilities

**Board of Directors**:
- Ultimate accountability for compliance culture.
- Approve and review the compliance manual annually.
- Receive the annual compliance report.
- Address material compliance failures as a board matter.

**Compliance Committee** (if applicable):
- Board-level or management-level committee.
- Oversees compliance risk; escalates to Board.
- Reviews new regulatory developments.

**Compliance Officer (CO)**:
- Day-to-day oversight of the compliance program.
- Reporting line: directly to CEO and/or Board Compliance Committee (independent of business lines).
- Responsibilities: regulatory correspondence, compliance monitoring, policy maintenance, training, regulatory filings.
- Authority: CO may impose a temporary "hold" on a transaction pending compliance review; must have documented authority to escalate and refuse.

**Money Laundering Reporting Officer (MLRO)**:
- May be the same person as the CO in smaller firms; separate in larger regulated entities.
- Sole authority to file SARs/STRs with the relevant FIU.
- Receives internal suspicious activity reports from staff.
- See [[draft-aml-policy]] for the full MLRO mandate.

**Deputy CO / Deputy MLRO**:
- Acts in the absence of the CO or MLRO; identical authority during the period of substitution.

**Business line managers**:
- First-line compliance: responsible for embedding compliance in day-to-day operations.
- Escalate issues to CO; do not self-clear material compliance issues.

**All staff**:
- Comply with the manual, all policies, and all training requirements.
- Report actual or suspected violations to the CO or via the whistleblower channel.
- No retaliation against whistleblowers.

### Chapter 4 — Core policies (by reference and summary)

Each core policy is either incorporated here in full or by reference with a hyperlink to the current version. The manual lists all policies and their owners.

| Policy | Owner | Last reviewed | Applies to |
|---|---|---|---|
| AML / KYC Policy | MLRO | [Date] | All regulated activities |
| Sanctions Policy | CO | [Date] | All regulated activities |
| Data Protection Policy | DPO / CO | [Date] | All data processing |
| Conduct of Business Policy | CO + Business Line Head | [Date] | Client-facing activities |
| Conflicts of Interest Policy | CO | [Date] | All staff |
| Gifts and Entertainment Policy | CO | [Date] | All staff |
| Whistleblower / Speak Up Policy | Board / CO | [Date] | All staff |
| Information Security Policy | CISO / CO | [Date] | IT and data operations |
| Personal Account Dealing Policy | CO | [Date] | Investment-firm staff |
| Market Conduct Policy | CO | [Date] | Trading operations |

**AML / KYC summary**: [Reference: full policy at [location]]. Customer risk categorization; CDD/EDD; sanctions screening; SAR filing; record retention. See [[draft-aml-policy]].

**Sanctions summary**: screening against UN, OFAC, EU, UK, and local lists; daily updates; match handling procedure; strict liability framework.

**Data protection summary**: GDPR / UAE PDPL / Saudi PDPL alignment; DPO appointment; data subject rights; breach notification; cross-border transfer safeguards.

**Conduct of business**: fair treatment of customers; suitability; inducements; conflicts of interest; market conduct; client order handling.

### Chapter 5 — Training requirements

| Training module | Target audience | Frequency | Format | Record |
|---|---|---|---|---|
| AML/CFT Fundamentals | All staff | Annual | E-learning + quiz | Certificate stored in HR system |
| AML Advanced (SAR filing, EDD) | Compliance team, MLRO | Annual | Workshop | Attendance record |
| Sanctions Awareness | All staff | Annual | E-learning | Certificate |
| Data Protection Fundamentals | All staff | Annual | E-learning | Certificate |
| New Hire Orientation | New joiners | Within 30 days | In-person / online | HR onboarding record |
| Board Training | Directors | Annual | In-person briefing | Board minutes |

Non-completion of mandatory training: escalate to department head; HR performance record; after 30-day warning, escalate to CO for disciplinary action.

### Chapter 6 — Monitoring, testing, and audit

**Compliance monitoring** (ongoing, first-line):
- Transaction monitoring for AML (automated tool alerts + manual review).
- Customer file reviews (sample-based; frequency based on risk tier).
- Complaint monitoring.

**Compliance testing** (periodic, second-line):
- CO-led testing of specific compliance obligations (e.g., CDD file completeness; sanctions screening accuracy).
- Frequency: quarterly for high-risk areas; annually for others.
- Findings logged; management responses documented; tracked to remediation.

**Internal audit** (independent, third-line):
- Annual independent review of the compliance program.
- Scope: AML program effectiveness; data protection controls; training records; regulatory filing accuracy.
- Reports to Board Audit Committee.
- Findings: management action plan required within 30 days of report issue.

**Regulatory inspections**:
- CO manages all regulatory examinations.
- All staff must cooperate fully and refer all regulator queries to CO.
- CO notifies Board promptly of any inspection outcome.

### Chapter 7 — Reporting and escalation

**Internal escalation pathway**:
```
Staff → Line Manager → CO → CEO → Board Compliance Committee
```

**STR/SAR pathway**:
```
Staff → MLRO → External FIU filing
(never bypass the MLRO; never tip off the customer)
```

**Regulatory reporting**:
- Annual compliance report to Board: summary of compliance activities; issues identified; training completion; audit findings; regulatory developments.
- Periodic reports to management: monthly or quarterly compliance dashboard (incidents, open items, training status).
- Ad hoc reporting to regulator: material incidents, notifiable events, license condition breaches — report promptly; do not wait for the annual report cycle.

### Chapter 8 — Breach response and sanctions protocols

**Definition of a compliance breach**: any failure to comply with applicable law, regulation, regulatory rule, or this manual.

**Classification**:
- **Critical breach**: regulatory reporting required; immediate escalation to Board; potential criminal/regulatory liability.
- **Significant breach**: potential regulatory notification; escalation to CO and CEO; root-cause analysis.
- **Minor breach**: managed within the compliance function; documented; training response.

**Investigation procedure**:
1. CO receives notification (from staff, monitoring tool, or external source).
2. CO assesses materiality and classifies breach.
3. If Critical: notify Board and consider regulator notification within applicable timeframe.
4. Investigation: facts gathered, timeline established, root cause identified.
5. Remediation plan: control improvements, process changes, training.
6. Documentation: all steps logged; retained.

**Staff sanctions for willful non-compliance**:
- Minor: formal warning.
- Significant: written warning; training; supervisor notification.
- Serious / willful: disciplinary proceedings; potential termination; regulatory referral.

### Chapter 9 — Document control

| Attribute | Requirement |
|---|---|
| Version control | Every revision of this manual bears a version number and effective date |
| Approval | Board or Compliance Committee approval required for material amendments |
| Distribution | All staff must have access to the current version; superseded versions archived |
| Retention | Retained for at least 7 years after the effective date of the version |
| Language | Primary language: English; Arabic translation provided where required by regulation |

## Caveats and currency

Regulations change frequently. This manual must be reviewed:
- At least annually.
- Promptly upon any material change to applicable law or regulation.
- Upon any significant change to the business model.

A compliance manual that is out of date is worse than no manual — it creates false assurance. Assign ownership and a review calendar.

## Related skills

- [[draft-aml-policy]]
- [[draft-board-resolution]]
- [[draft-articles-of-association]]
