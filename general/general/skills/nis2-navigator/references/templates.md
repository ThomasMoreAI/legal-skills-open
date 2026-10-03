# NIS2 Navigator — Output Templates

## Table of Contents
1. Full Assessment Report Template
2. Executive Summary Template
3. Management Briefing Template

---

## 1. Full Assessment Report Template

Use this template to structure the final assessment output. Fill in all sections based on the assessment results. Adapt the German-specific sections based on jurisdiction selection.

```markdown
# NIS2 Compliance Assessment Report

**Date:** [Assessment date]
**Assessed entity:** [Organization name]
**Jurisdiction:** [EU / Germany / Both]
**Assessed by:** AI-assisted assessment (NIS2 Navigator) — to be validated by qualified legal counsel

---

## 1. Executive Summary

**Scope verdict:** [Essential entity / Important entity / Out of scope]
**Basis:** [Annex I/II sector] — [Size classification]
**Overall compliance score:** [X] / 40 — [🔴 Critical / 🟡 Needs Improvement / 🟢 On Track]
**Top 3 priority gaps:**
1. [Measure] — Maturity [score], Priority [P1/P2/P3]
2. [Measure] — Maturity [score], Priority [P1/P2/P3]
3. [Measure] — Maturity [score], Priority [P1/P2/P3]

---

## 2. Scope & Classification

| Field | Result |
|-------|--------|
| Sector | [Annex I/II sector and sub-sector] |
| Services in scope | [Specific services assessed] |
| Organization size | [Employees / Turnover / Balance sheet] |
| Size classification | [Medium / Large] |
| Entity category | [Essential / Important] |
| Legal basis | [Art. X Directive / § X BSIG-neu] |
| Special status | [Regardless-of-size / KRITIS / None] |
| Group structure | [Standalone / Part of group — assessment level noted] |

**Germany-specific (if applicable):**

| Field | Result |
|-------|--------|
| BSIG-neu category | [Besonders wichtige / Wichtige Einrichtung] |
| BSI registration | [Completed / Overdue — action required] |
| Nachweispflicht | [Applicable (deadline: Dec 2028) / Not applicable] |
| KRITIS status | [Yes — additional obligations / No] |

---

## 3. Gap Analysis — Art. 21 Risk Management Measures

| # | Measure | Art. 21 | § 30 BSIG | Maturity (0–4) | Status | ISO 27001 Ref |
|---|---------|---------|-----------|----------------|--------|--------------|
| a | Risk analysis & IS policies | (2)(a) | (2) Nr. 1 | [score] | [🔴/🟡/🟢] | A.5.1, A.5.2 |
| b | Incident handling | (2)(b) | (2) Nr. 2 | [score] | [🔴/🟡/🟢] | A.5.24–A.5.27 |
| c | Business continuity & crisis mgmt | (2)(c) | (2) Nr. 3 | [score] | [🔴/🟡/🟢] | A.5.29, A.5.30, A.8.13–14 |
| d | Supply chain security | (2)(d) | (2) Nr. 4 | [score] | [🔴/🟡/🟢] | A.5.19–A.5.23 |
| e | Network & IS acquisition/dev/maint | (2)(e) | (2) Nr. 5 | [score] | [🔴/🟡/🟢] | A.8.25–A.8.28, A.8.8 |
| f | Effectiveness assessment | (2)(f) | (2) Nr. 6 | [score] | [🔴/🟡/🟢] | A.5.35, A.5.36 |
| g | Cyber hygiene & training | (2)(g) | (2) Nr. 7 | [score] | [🔴/🟡/🟢] | A.6.3, A.5.10 |
| h | Cryptography & encryption | (2)(h) | (2) Nr. 8 | [score] | [🔴/🟡/🟢] | A.8.24 |
| i | HR security & access control | (2)(i) | (2) Nr. 9 | [score] | [🔴/🟡/🟢] | A.5.9, A.5.15–18, A.6.1–5 |
| j | MFA & secure communications | (2)(j) | (2) Nr. 10 | [score] | [🔴/🟡/🟢] | A.5.14, A.5.17, A.8.5 |

**Overall Score: [X] / 40**
**Overall Rating: [🔴 Critical / 🟡 Needs Improvement / 🟢 On Track]**

### Key Findings

[For each measure scored ≤ 2, provide a 2–3 sentence finding describing the gap and its significance.]

---

## 4. Compliance Roadmap

### Priority 1 — Immediate (0–3 months)

| Measure | Current | Target | Key Actions | Effort |
|---------|---------|--------|-------------|--------|
| [Measure name] | [Current state summary] | [Target state] | 1. [Action] 2. [Action] 3. [Action] | [S/M/L/XL] |

### Priority 2 — Short-term (3–6 months)

| Measure | Current | Target | Key Actions | Effort |
|---------|---------|--------|-------------|--------|
| [Measure name] | [Current state summary] | [Target state] | 1. [Action] 2. [Action] 3. [Action] | [S/M/L/XL] |

### Priority 3 — Medium-term (6–12 months)

| Measure | Current | Target | Key Actions | Effort |
|---------|---------|--------|-------------|--------|
| [Measure name] | [Current state summary] | [Target state] | 1. [Action] 2. [Action] 3. [Action] | [S/M/L/XL] |

### Maintenance (already compliant — maintain maturity)

[List measures at maturity 3–4 that require ongoing attention.]

---

## 5. Management Body Obligations

| Obligation | Basis | Status | Action Required |
|-----------|-------|--------|-----------------|
| Approve risk management measures | Art. 20(1) / § 38(1) BSIG | [Done / Pending] | [Describe] |
| Undergo cybersecurity training | Art. 20(2) / § 38(3) BSIG | [Done / Pending] | [Describe] |
| Oversee implementation | Art. 20(1) / § 38(1) BSIG | [Done / Pending] | [Describe] |
| Personal liability awareness | § 38(2) BSIG (Germany) | [Acknowledged / To brief] | [Describe] |

---

## 6. Germany-Specific Requirements (if applicable)

### BSI Registration
- Status: [Registered / Not registered]
- Action: [None / Register immediately via muk.bsi.bund.de]
- Risk: [Failure to register is independently sanctionable under § 60 BSIG]

### Nachweispflicht (besonders wichtige Einrichtungen only)
- Applicable: [Yes / No]
- Deadline: December 2028
- Recommended evidence path: [ISO 27001 / BSI IT-Grundschutz / B3S / Audit]
- Planning timeline: Begin preparation by mid-2027

### Incident Reporting Readiness (§ 32 BSIG)
- 24h Erstmeldung process: [In place / To establish]
- 72h Bestätigungsmeldung process: [In place / To establish]
- 1-month Abschlussbericht process: [In place / To establish]
- BSI portal access: [Configured / To configure]
- GDPR dual-reporting coordination: [Aligned / To align]

---

## 7. Recommended Next Steps

1. [Most critical immediate action]
2. [Second priority]
3. [Third priority]
4. Schedule management body briefing on NIS2 obligations and personal liability
5. [If Germany:] Complete BSI registration if not yet done
6. Establish incident reporting processes covering both NIS2 (BSI) and GDPR (DPA)
7. Plan Nachweispflicht evidence path (if besonders wichtige Einrichtung)
8. Review and update supplier contracts for NIS2 supply chain security requirements
9. Engage qualified legal counsel to validate this preliminary assessment

---

*This assessment was generated using NIS2 Navigator, an AI-assisted compliance tool. It provides structured guidance but does not constitute legal advice. All findings and recommendations should be validated by qualified legal counsel and cybersecurity professionals.*
```

---

## 2. Executive Summary Template

For situations where only a quick summary is needed (e.g., management email, board briefing prep):

```markdown
## NIS2 Compliance — Executive Summary

**Entity:** [Name] | **Sector:** [Sector] | **Category:** [Essential / Important]

**Overall Readiness: [X/40] — [🔴/🟡/🟢]**

**Critical gaps requiring immediate action:**
- [Gap 1]: [One-line description]
- [Gap 2]: [One-line description]

**Key deadlines:**
- BSI registration: [Status]
- Nachweispflicht: [Date if applicable]

**Management body action items:**
- [ ] Approve NIS2 risk management measures
- [ ] Complete cybersecurity training
- [ ] Acknowledge personal liability under § 38(2) BSIG
```

---

## 3. Management Briefing Template

For preparing the Art. 20 / § 38 BSIG management body briefing:

```markdown
## Management Briefing: NIS2 Compliance Obligations

### Why This Matters — Personal Liability
Under § 38(2) BSIG-neu, management body members are **personally liable** for damages arising from failure to ensure adequate cybersecurity measures under § 30 BSIG. This is not an abstract corporate risk — it attaches to individual board members and Geschäftsführer.

### Your Legal Obligations
1. **Approve** the organization's cybersecurity risk management measures (§ 38(1) BSIG)
2. **Oversee** their implementation — delegation to CISO is permitted for execution, but oversight responsibility cannot be delegated
3. **Undergo** regular cybersecurity training personally (§ 38(3) BSIG)

### Current Status
- Overall compliance score: [X/40]
- Critical gaps: [List top 3]
- Recommended investment: [Summary of effort/budget needed]

### Decisions Required
1. Approve the attached risk management measures [reference]
2. Authorize budget of [amount] for remediation priorities P1 and P2
3. Schedule management body cybersecurity training for [proposed date]
4. Acknowledge and document personal liability awareness

### Enforcement Context
- Fines: Up to €10M or 2% worldwide turnover (essential entities)
- BSI can conduct proactive inspections of besonders wichtige Einrichtungen
- BSI can issue binding remediation orders with deadlines
- In extreme cases: temporary ban on management functions
```
