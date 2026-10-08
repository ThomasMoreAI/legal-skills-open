---
name: kb-data-privacy-uae-pdpl-sboghossian
title: Knowledge Pack — UAE Data Protection Law (Federal Decree-Law 45/2021 + DIFC + ADGM)
description: Use when a matter involves personal data processing, privacy obligations, or data-breach response in UAE (onshore). Covers the UAE Federal Personal Data Protection Law (Federal Decree-Law 45/2021) and its executive regulations, TDRA oversight, lawful bases, sensitive data categories, cross-border transfer rules, data subject rights, and fines up to AED 20 million. Also covers the separate data-protection regimes of DIFC (DIFC Data Protection Law 5/2020) and ADGM (DP Regulations 2021) for free-zone entities. Triggers on UAE data privacy compliance, UAE PDPL, TDRA, DIFC DP, ADGM DP questions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-data-privacy-uae-pdpl
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: data-protection
language: en
---

# Knowledge Pack — UAE Data Protection Law (Federal Decree-Law 45/2021 + DIFC + ADGM)

## Overview: Three Parallel Regimes

The UAE has three distinct data-protection regimes depending on where the entity is established:

| Regime | Applicable To | Regulator |
|---|---|---|
| UAE Federal PDPL (DL 45/2021) | Onshore UAE entities + extra-territorial scope | TDRA (Telecommunications and Digital Government Regulatory Authority) |
| DIFC Data Protection Law 5/2020 | DIFC-registered entities | DIFC Commissioner of Data Protection |
| ADGM Data Protection Regulations 2021 | ADGM-registered entities | ADGM Registration Authority + ADGM Courts |

DIFC and ADGM have both received **EU adequacy decisions** making them recognized as providing adequate data protection for EU data transfers.

---

## Part 1: UAE Federal PDPL (Decree-Law 45/2021)

### Scope

Applies to:
- **Any entity** (public or private) that processes personal data of individuals in the UAE.
- **Extra-territorial**: foreign entities processing UAE residents' data to offer goods/services or monitor behavior.
- Excludes: purely personal/household use; public security, defense, judicial processing; anonymized/aggregated data.

### Key Definitions

- **Personal data**: any data relating to an identified or identifiable natural person.
- **Sensitive data**: health/medical data; genetic/biometric data; data on children; financial data; credit information; religious/political views; ethnic origin; criminal records.
- **Controller**: determines purposes and means.
- **Processor**: processes on controller's behalf.

### Lawful Bases

1. **Consent** — written or electronic; explicit for sensitive data; freely given; withdrawable.
2. **Contract** — necessary to perform a contract with the data subject.
3. **Legal obligation** — required by UAE law.
4. **Vital interests** — protection of life or health.
5. **Public interest** — task of public authority.
6. **Legitimate interests** — balancing test; not available for sensitive data.

### Data Subject Rights

| Right | Deadline |
|---|---|
| Access | 30 days |
| Rectification | 30 days |
| Erasure | 30 days |
| Restriction | Without undue delay |
| Portability | 30 days |
| Object to processing (especially direct marketing) | Immediately |
| Withdraw consent | At any time |

### Cross-Border Transfers

Transfer outside UAE permitted only if:
1. The destination country is on TDRA's **approved jurisdictions list** (includes EU/EEA, DIFC, ADGM, UK, and others with adequacy);
2. **Contractual safeguards** (TDRA-approved SCCs or binding corporate rules);
3. **Explicit consent** of the data subject;
4. Contract performance, legal claims, vital interests, or public interest.

### Breach Notification

- Notify **TDRA within 72 hours** of becoming aware.
- Notify **data subjects without undue delay** if the breach is likely to cause high risk.
- Maintain internal breach register.

### Penalties (Decree-Law 45/2021)

| Violation | Fine |
|---|---|
| Processing special data without consent | AED 5,000,000 – 20,000,000 |
| Transfer outside UAE without authorization | AED 5,000,000 – 20,000,000 |
| Failure to implement security measures | AED 1,000,000 – 10,000,000 |
| Violation of data subject rights | AED 250,000 – 1,000,000 |
| General non-compliance | AED 500,000 – 5,000,000 |

- Repeat violations: doubled fines.
- Criminal liability for intentional violations causing damage.

---

## Part 2: DIFC Data Protection Law 5/2020 (DIFC DP)

### Scope

Applies to controllers and processors **established in the DIFC** or processing data of DIFC residents/employees.

### Alignment with GDPR

DIFC DP Law 5/2020 closely mirrors GDPR structure:
- Same six lawful bases (Art 6 equivalent)
- Same special-category data list (Art 9 equivalent)
- Same data subject rights (Arts 15–22 equivalent)
- DPO requirement mirrors GDPR
- 72-hour breach notification
- SCCs for international transfers
- DIFC Commissioner of Data Protection as supervisory authority

### DIFC EU Adequacy

DIFC has an **EU adequacy decision** — EU personal data may be transferred to DIFC-registered entities without additional safeguards.

### Penalties (DIFC DP)

- Up to **USD 100,000** per violation (Commissioner determination).
- Commissioner may issue enforcement notices, warnings, and audit requirements.

---

## Part 3: ADGM Data Protection Regulations 2021

### Scope

Applies to controllers and processors **registered in ADGM**.

### Alignment with GDPR

ADGM DP Regulations 2021 similarly align closely with GDPR:
- Same six lawful bases
- Special category data
- Data subject rights
- DPO requirement
- Breach notification
- International transfer safeguards

### ADGM EU Adequacy

ADGM (Abu Dhabi Global Market) also holds an **EU adequacy decision**.

### Penalties (ADGM DP)

- Up to **USD 28,000,000** (broadly capped; ADGM Registration Authority determines).

---

## Practical Mapping: Which Regime Applies?

```
Is the entity registered in DIFC? → Apply DIFC DP Law 5/2020
Is the entity registered in ADGM? → Apply ADGM DP Regulations 2021
Is the entity onshore UAE (Dubai, Abu Dhabi, SPC, other mainland)?
  → Apply UAE Federal PDPL (DL 45/2021)
Does the entity have presences in multiple zones?
  → Multiple regimes apply; compliance with each required
```

## Comparison Table

| Feature | UAE PDPL | DIFC DP | ADGM DP | GDPR |
|---|---|---|---|---|
| Regulator | TDRA | DIFC CDP | ADGM RA | National DPA |
| EU adequacy | No | Yes | Yes | N/A |
| Max fine | AED 20M | USD 100K | USD 28M | €20M / 4% |
| Breach notification | 72 hrs | 72 hrs | 72 hrs | 72 hrs |
| DPO required | Certain controllers | Mirrors GDPR | Mirrors GDPR | Certain controllers |
| Extra-territorial | Yes | Yes | Yes | Yes |

## Compliance Checklist

- [ ] Determine which regime(s) apply (onshore / DIFC / ADGM)
- [ ] Map personal data flows
- [ ] Document lawful basis for each processing activity
- [ ] Ensure consent mechanisms are compliant (explicit for sensitive data)
- [ ] Update privacy notices (Arabic and English for federal; English for DIFC/ADGM)
- [ ] Assess DPO requirement
- [ ] Implement cross-border transfer mechanisms
- [ ] Establish 72-hour breach notification procedure
- [ ] Put Data Processing Agreements in place with processors
- [ ] Implement security controls proportionate to risk
- [ ] Verify sector-specific layered obligations (CBUAE for banking, MOH/DHA/DOH for health)

## Caveats & Currency

The UAE Federal PDPL executive regulations have been issued in phases; TDRA guidance continues to develop. DIFC and ADGM publish their own updated guidance and enforcement decisions. EU adequacy for DIFC and ADGM should be verified for continued validity. Sector-specific requirements from CBUAE, DHA, DOH, and MOH add layers not covered here — verify current guidance.

## Related Skills

- [[kb-data-privacy-gdpr]]
- [[kb-data-privacy-ksa-pdpl]]
- [[kb-data-privacy-egypt]]
- [[kb-fintech-licensing-difc]]
- [[kb-healthcare-regulation-mena]]
- [[draft-data-processing-agreement]]
- [[draft-privacy-policy]]
