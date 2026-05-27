---
name: ada-accommodation-complaint
title: ADA Failure to Accommodate Complaint
description: Drafts an ADA failure-to-accommodate complaint for federal or state court filing. Covers Title I employment (42 U.S.C. § 12112) and Title III public accommodations (42 U.S.C. § 12182), including EEOC exhaustion, interactive process failures, and prayer for relief. Use when drafting an ADA complaint, disability discrimination pleading, failure-to-accommodate lawsuit, or right-to-sue complaint.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ada-accommodation-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# ADA Failure to Accommodate Complaint

Generates a litigation-ready complaint under ADA Title I (employment) or Title III (public accommodations) for federal or state court. Determines applicable title from intake facts, structures numbered allegations to satisfy Twombly/Iqbal plausibility, and produces a complete pleading with causes of action and prayer for relief.

## Intake Checklist

Gather before drafting:

- [ ] Plaintiff name, state of residence
- [ ] Disability: diagnosis, functional limitations, treating provider
- [ ] Accommodation request: date, form (oral/written), recipient, specific accommodation, medical documentation submitted
- [ ] Defendant response: denial letter, non-response timeline, or interactive process failure evidence
- [ ] **Title I only:** job description, hire date, performance reviews, adverse action date/reason
- [ ] **Title I only:** EEOC charge number, filing date, Right to Sue date, receipt date
- [ ] Damages: pay stubs, W-2s, benefits records, therapy/treatment records

## Complaint Structure

Draft the following sections in order:

### 1. Caption

Court name/division; plaintiff as "an individual with a disability"; defendant by full legal name; title: `COMPLAINT FOR FAILURE TO PROVIDE REASONABLE ACCOMMODATION UNDER THE AMERICANS WITH DISABILITIES ACT`; case number placeholder.

### 2. Nature of Action

2–4 sentences: title invoked → plaintiff's disability and limitation → accommodation requested → defendant's refusal or process failure → resulting harm.

### 3. Parties

**Plaintiff:** Name; residence state; disability status under 42 U.S.C. § 12102 (impairment / record of / regarded as); relationship with defendant.

**Defendant (Title I):** Legal name; business form; principal place of business; **15+ employees for 20+ weeks** in current or preceding calendar year.

**Defendant (Title III):** Legal name; owns/leases/operates place of public accommodation; category under § 12181(7).

### 4. Jurisdiction and Venue

| Basis | Citation |
|---|---|
| Federal question | 28 U.S.C. § 1331 |
| Title I | 42 U.S.C. § 12117(a) |
| Title III | 42 U.S.C. § 12188 |
| Supplemental state claims | 28 U.S.C. § 1367(a) |
| Venue | 28 U.S.C. § 1391(b) |

**EEOC exhaustion (Title I — mandatory):**
- Charge filed within **300 days** (deferral state) or **180 days** (non-deferral)
- Complaint filed within **90 days** of Right to Sue receipt per § 2000e-5(f)(1)
- Attach Right to Sue letter as Exhibit A

### 5. Factual Allegations

Numbered paragraphs, chronological:

1. **Disability** — impairment; how it substantially limits a major life activity per ADAAA; documentation provided to defendant
2. **Qualification** — position, essential functions, performance history establishing "otherwise qualified"
3. **Accommodation request** — date, form, recipient, content; medical documentation submitted
4. **Interactive process failure** — no meeting, no questions about limitations, no alternatives proposed, no good-faith engagement
5. **Denial and rebuttal** — defendant's reason(s) and rebuttal:
   - *Undue hardship:* low cost vs. resources; tax credits; minimal operational impact (§ 12111(10)(B))
   - *Not qualified:* performance record; prior success with informal accommodation
   - *Fundamental alteration:* modification does not alter core service/function
6. **Adverse action** — date, type (termination/demotion/denial of access/constructive discharge), stated reason
7. **Damages** — lost wages, benefits, out-of-pocket costs, emotional distress with treatment records
8. **Malice/reckless indifference** (if punitive damages sought) — pattern of discrimination, ignored counsel advice, animus statements

### 6. Causes of Action

**Count I — Failure to Accommodate (Title I), § 12112(a), (b)(5)(A):**
- [ ] Plaintiff has a disability (§ 12102)
- [ ] Plaintiff is otherwise qualified with or without accommodation
- [ ] Defendant had notice of disability and accommodation need
- [ ] Plaintiff requested a specific reasonable accommodation
- [ ] Defendant failed to accommodate or engage in good-faith interactive process
- [ ] Plaintiff suffered damages as proximate result

**Count I alt — Denial of Equal Enjoyment (Title III), § 12182(a), (b)(2)(A)(ii):**
- [ ] Plaintiff has a disability
- [ ] Defendant owns/operates a place of public accommodation
- [ ] Plaintiff requested reasonable policy/practice modification
- [ ] Modification would not fundamentally alter goods or services
- [ ] Defendant refused, denying full and equal access

**Count II — Retaliation (if applicable), § 12203(a):**
- [ ] Protected activity (accommodation request or opposition to discrimination)
- [ ] Adverse action by defendant
- [ ] Causal nexus

**Count III — State disability discrimination** (supplemental; cite applicable state statute)

### 7. Prayer for Relief

**Title I:** Reinstatement or front pay; back pay with prejudgment interest; compensatory damages (emotional distress); punitive damages if malice/reckless indifference shown; attorney's fees and costs (§ 12205); pre/post-judgment interest.

**Title III** (injunctive-focused): Permanent injunction requiring modification and ADA compliance; declaratory judgment; attorney's fees and costs (§ 12205).

> Omit specific dollar amounts per FRCP 8(a)(3).

### 8. Jury Demand

"Plaintiff demands a trial by jury on all issues so triable." (FRCP 38(b))

> Title III claims are equitable — no jury right. Limit or omit accordingly.

### 9. Signature Block

Per FRCP 11: date, attorney signature, name, bar number, state, firm, address, phone, email — "Attorney for Plaintiff." Add client verification if required by local rule.

## Pitfalls and Checks

- **ADAAA breadth:** Construe "substantially limits" broadly; never concede a narrow disability definition
- **Interactive process:** Defendant's failure to engage creates independent liability even if plaintiff's preferred accommodation is unreasonable — plead separately. [VERIFY: circuit split on whether failure alone is actionable]
- **Title I damages cap:** Compensatory + punitive capped at $50K–$300K by employer size (§ 1981a(b)(3)); back pay excluded from cap
- **State claims:** FEHA, NYSHRL, and analogs provide broader coverage and uncapped damages — always plead supplemental state claims
- **Twombly/Iqbal:** Every element needs specific factual allegations raising plausibility; no conclusory recitations
- **Medical privacy:** Include only detail necessary to establish substantial limitation; avoid gratuitous medical disclosure
- **Dual filing (Title I):** Verify EEOC charge was dual-filed with state agency in deferral states to preserve state law claims
