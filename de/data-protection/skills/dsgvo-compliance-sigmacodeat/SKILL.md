---
name: dsgvo-compliance-sigmacodeat
title: DSGVO-Compliance Skill
description: 'Checks data processing activities for GDPR (DSGVO) compliance.

  Identifies required legal bases, data subject rights, documentation

  obligations, and breach notification requirements. Produces a compliance

  checklist and gap report. Covers Germany, Austria, and EU-wide rules.'
author: Sigmacodeat
author_url: https://github.com/Sigmacodeat/Sigmabrain/tree/main/server/skills/dsgvo-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: en
---

# DSGVO-Compliance Skill

## When To Use

- The user asks about GDPR compliance
- New data processing activity needs evaluation
- Data breach notification assessment
- Data subject rights request handling

## Protocol

### Step 1 — Map the Processing Activity

Identify:
- **Controller** (Verantwortlicher)
- **Processor** (Auftragsverarbeiter)
- **Purpose** (Zweck)
- **Data categories** (Kategorien)
- **Legal basis** (Art. 6 DSGVO)
- **Retention period** (Speicherdauer)
- **Recipients** (Empfänger)

### Step 2 — Check Legal Basis

Valid bases under Art. 6(1):
- (a) Consent
- (b) Contract necessity
- (c) Legal obligation
- (d) Vital interests
- (e) Public interest
- (f) Legitimate interests

### Step 3 — Data Subject Rights Checklist

- [ ] Right to information (Art. 13-14)
- [ ] Right of access (Art. 15)
- [ ] Right to rectification (Art. 16)
- [ ] Right to erasure (Art. 17)
- [ ] Right to restriction (Art. 18)
- [ ] Right to data portability (Art. 20)
- [ ] Right to object (Art. 21)
- [ ] Right not to be subject to automated decisions (Art. 22)

### Step 4 — Technical & Organizational Measures (TOMs)

- [ ] Pseudonymization
- [ ] Encryption
- [ ] Access control
- [ ] Audit logging
- [ ] Backup & recovery
- [ ] Staff training

### Step 5 — Documentation Requirements

- [ ] Processing records (Art. 30)
- [ ] DPIA if required (Art. 35)
- [ ] DPO appointment if required (Art. 37)
- [ ] Data Processing Agreements (Art. 28)
- [ ] Privacy notice

## Output Format

```
## DSGVO-Compliance-Check — [Activity]

### Verarbeitungstätigkeit
| Feld | Wert |
|---|---|
| Verantwortlicher | [Name] |
| Zweck | [Purpose] |
| Rechtsgrundlage | Art. 6(1) [Letter] |
| Datenkategorien | [List] |
| Speicherdauer | [Period] |

### Prüfung
| Anforderung | Status | Anmerkung |
|---|---|---|
| Rechtsgrundlage | ✅/⚠️/❌ | [Note] |
| Betroffenenrechte | ... | ... |
| TOMs | ... | ... |
| Dokumentation | ... | ... |

### Mängel
1. [Gap] — [Severity]

### Empfohlene Maßnahmen
1. [Action]

---
⚠️ Dies ist eine Orientierungsprüfung. Bei Unsicherheit konsultieren Sie
einen Datenschutzbeauftragten oder Fachanwalt.
```

## Anti-patterns

- Never assume consent is always valid
- Never ignore processor obligations
- Never omit cross-border transfer checks
- Never present findings as legally binding

## Contract

1. Every finding maps to a GDPR/DSGVO article (legal basis, data-subject right, duty).
2. Gaps are listed explicitly with the article they fail.
3. The output is a compliance checklist/gap report supporting, not replacing, the DPO.

## Anti-Patterns

- ❌ Declaring processing "compliant" as a legal assurance — flag gaps, recommend DPO review.
- ❌ Checking only the activities described while ignoring missing records (Art. 30) or DPIAs.
- ❌ Omitting the legal basis (Art. 6/9) for a processing activity.
