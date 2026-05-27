---
name: breach-notification
title: Data Breach Notification Letter
description: Drafts legally compliant data breach notification letters to affected consumers under multi-state and federal statutes (HIPAA, GLBA, state AG requirements). Use when drafting breach notices, security incident consumer notifications, or data compromise letters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/breach-notification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: data-protection
language: en
---

# Data Breach Notification Letter

Drafts a consumer-facing breach notification letter satisfying multi-state statutory requirements with appropriate tone and actionable consumer guidance.

## Prerequisites

Gather before drafting:

1. **Incident details** — discovery date, breach type (unauthorized access, ransomware, inadvertent disclosure), affected timeframe
2. **Compromised data inventory** — exact data elements per affected population segment
3. **Jurisdiction list** — states where affected consumers reside (drives content and timing)
4. **Regulatory frameworks** — state breach statutes, plus sector-specific if applicable (HIPAA, GLBA, FERPA)
5. **Remediation services** — credit monitoring/identity protection vendor, enrollment details, duration, cost allocation
6. **Contact channels** — dedicated toll-free phone, email, URL for breach inquiries
7. **Signatory** — senior executive name and title (CEO, CPO, or GC)

## Letter Sections

Draft these sections in order:

### 1. Header & Salutation

- Organization legal name, address, letterhead
- Letter date (track against statutory deadlines)
- Personalized name if available; otherwise "Dear [Customer/Patient/Member]"
- Cite specific statute(s) under which notice is provided

### 2. Incident Description

- State purpose immediately: notifying recipient of a data security incident
- Plain language — no unnecessary technical jargon
- Include discovery date, nature of incident, general cause
- If investigation is ongoing, state so and commit to updates
- **Do not** disclose details that compromise security or ongoing investigations
- **Do not** speculate beyond confirmed facts

### 3. Compromised Data Categories

List only data elements actually affected:

| Category | Examples |
|---|---|
| Identifiers | Full name, address, phone, email |
| Government IDs | SSN, driver's license, passport number |
| Financial | Bank account, credit/debit card numbers |
| Health | Medical records, insurance IDs, diagnoses |
| Credentials | Usernames, passwords, security questions |

If different segments had different data exposed, produce individualized letters.

### 4. Organizational Response

- [ ] Containment measures taken
- [ ] Cybersecurity firm engaged for forensic investigation
- [ ] Law enforcement notified
- [ ] Regulatory authorities notified (state AGs, HHS if HIPAA)
- [ ] Additional security measures implemented
- [ ] Identity protection services offered — specify vendor, duration, enrollment deadline, cost (confirm no-cost), enrollment code/instructions

### 5. Consumer Protection Steps

Tailor to compromised data types:

| Action | Details |
|---|---|
| Fraud alert | Contact any one bureau; propagates to all three |
| Security freeze | Equifax: (800) 685-1111 / Experian: (888) 397-3742 / TransUnion: (888) 909-8872 |
| Credit monitoring | Free reports at AnnualCreditReport.com |
| Financial review | Monitor statements; report unauthorized activity immediately |
| Phishing vigilance | Warn recipients to distrust communications referencing this breach |
| FTC report | IdentityTheft.gov for identity theft reports and recovery plans |

Emphasize type-specific steps (e.g., card replacement for payment data, new credentials for login data).

### 6. Contact Information

- Dedicated toll-free number with hours and time zone
- Dedicated email and webpage URL with FAQs
- Multilingual support if applicable

### 7. Closing

- Express concern and commitment to data protection
- Apology where appropriate — avoid language implying negligence admission
- Signed by senior executive with name, title, and reference/tracking number

## Statutory Timing Reference

| Jurisdiction | Deadline | Notes |
|---|---|---|
| Most US states | 30–60 days from discovery | Some allow delay for law enforcement |
| California (Cal. Civ. Code § 1798.82) | "Most expedient time possible" | No fixed day count |
| New York (GBL § 899-aa) | "Most expedient time possible" | AG + DFS notification required |
| HIPAA (45 CFR § 164.404) | 60 days from discovery | HHS notification; media notice if 500+ affected |
| Florida (Fla. Stat. § 501.171) | 30 days | Among the strictest |

[VERIFY] Confirm current deadlines against applicable statutes; state laws change frequently.

## Multi-State Drafting

When consumers span multiple states, draft to the **most stringent** applicable standard across all elements (timing, content, delivery). Use state-specific supplements only where requirements are irreconcilable.

## Compliance Checklist

Verify before finalizing — apply the most stringent applicable state's requirements:

- [ ] Description of the incident
- [ ] Types of information involved
- [ ] Steps taken by organization
- [ ] Steps consumers can take
- [ ] Organization contact information
- [ ] Credit bureau contact information
- [ ] Government agency contacts (state AG, FTC)
- [ ] Delivery method compliant with state law (mail, email, substitute notice thresholds)
- [ ] Documentation of all notifications sent (dates, methods, proof of delivery)

## Tone

- Direct and transparent — do not minimize or catastrophize
- Professional empathy — acknowledge impact without over-apologizing
- Actionable — every paragraph should inform or instruct
- Legally defensible — assume the letter will be exhibit A in litigation

## Formatting

- Official letterhead, minimum 12-point readable font
- Target 1–2 pages
- Accessible format if electronic (screen-reader compatible)

---

**Key changes from the original:**

- **Frontmatter**: Removed `tags` (not in spec), tightened `description` to be concise with clear trigger guidance
- **Structure**: Replaced "Output Structure" + "Guidelines" split with a flat, scannable layout — letter sections flow directly into reference tables and checklists
- **Removed redundancy**: Eliminated the separate "Formatting Requirements" heading's prose, collapsed "Tone Principles" to "Tone", merged "Multi-State Drafting" inline rather than nesting under "Guidelines"
- **Token savings**: ~25% reduction — cut the repeated overview sentence, removed the "Draft the letter using the following sections in order" preamble (the heading already says it), tightened contact info section, compressed formatting rules
- **Preserved all domain content**: Every statutory reference, phone number, checklist item, and legal guardrail is intact
