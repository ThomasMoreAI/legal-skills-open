---
name: draft-guardianship-sboghossian
title: Guardianship Deed / Application
description: 'Use when drafting a guardianship deed or order application for minors (where parents are deceased or incapacitated) or incapacitated adults. Jurisdiction-sensitive across MENA: KSA Najiz court system (wilayah — paternal grandfather priority), UAE Personal Status Courts for Muslims and DIFC Wills & Probate Registry for non-Muslims, Lebanon''s confessional courts, and France (tutelle/curatelle for MENA-France dual nationals). Covers scope of guardian powers, property management rules, court reporting obligations, and handoff to a will or power of attorney.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-guardianship
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: family
language: en
---

# Guardianship Deed / Application

## When to use this

Guardianship is the legal appointment of an individual to manage the personal and/or financial affairs of a person who cannot manage them independently:

- **Minors** whose both parents are deceased or permanently incapacitated.
- **Incapacitated adults** (mental or physical incapacity preventing self-management of affairs).
- **Limited-purpose guardianship** (specific asset, decision, or matter — e.g., managing inherited real estate for a minor; consenting to a medical procedure).

Guardianship is distinct from:
- **Custody (hadanah)** — day-to-day physical care of a child (parent is alive).
- **Power of attorney** — voluntary delegation of authority by a competent adult.

The applicable legal system (which court has jurisdiction; what rules apply) is determined by the ward's religion, nationality, and domicile. In MENA, Islamic-law jurisdictions apply the wilayah (ولاية) framework; Western civil-law jurisdictions apply tutelle / curatelle or guardianship order regimes.

**Always recommend local court counsel** — guardianship requires court appointment in all jurisdictions; this skill supports drafting the application and related instruments, not the final order itself.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Ward (name, date of birth, nationality, religion, current residence) | Determines jurisdiction and applicable law | — |
| Proposed guardian (name, relationship to ward, capacity to act) | Courts assess fitness; relationship priority matters in Islamic-law systems | — |
| Reason for guardianship (death of parents; incapacity; specific matter) | Determines grounds and scope of application | — |
| Ward's assets (nature, value, jurisdiction where located) | Determines extent of property-management powers requested | — |
| Other persons with legitimate interest (relatives, prior guardian) | Must be served or notified in most systems | — |
| Preferred court / tribunal | Determined by jurisdiction, religion, nationality | — |

## Jurisdictional framework

### KSA — Wilayah under Sharia

In Saudi Arabia, wilayah (legal guardianship) follows Islamic law principles as administered by the Najiz court system (منصة ناجز — the unified court platform for personal-status filings).

**Priority order for wilayah:**
1. Father (if living and competent)
2. Paternal grandfather
3. Paternal brothers
4. Paternal uncles
5. Court-appointed guardian (for failure of all above, or in best-interest cases)

For incapacitated adults, the court (محكمة الأحوال الشخصية) appoints a guardian (ولي) following assessment.

**Key features:**
- Court approval required for all significant property transactions by the guardian.
- Annual financial reporting to the Personal Status Court.
- Compensation: guardians are entitled to reasonable compensation from the ward's estate, approved by the court.
- Successor guardian: the deed should nominate a successor (approved by court) to ensure continuity.

**Filing process:** through Najiz platform; legal counsel recommended for non-Saudi applicants.

### UAE — Personal Status Court and DIFC Wills Registry

**For Muslims:** UAE Personal Status Courts (Sharia-based) apply federal personal status law and Islamic jurisprudence for Muslim wards. Similar wilayah priority order as KSA.

**For non-Muslims (DIFC Wills and Probate Registry):**
- The DIFC Wills Service Centre allows non-Muslim expats to register wills and appoint guardians for children who are Dubai residents.
- A registered DIFC Will can designate a guardian for minor children.
- Note: the Will can nominate a guardian; UAE courts still have jurisdiction over the custody arrangement for children habitually resident in UAE.

**Abu Dhabi:** the Abu Dhabi Civil Family Court (established 2021 under ADJD reforms) handles guardianship for non-Muslims under civil-law principles.

### Lebanon — Confessional courts

Lebanon's guardianship system mirrors its personal-status framework: each religious community applies its own rules through its confessional court.

| Community | Court | Framework |
|---|---|---|
| Sunni / Shia | Sharia court | Wilayah framework (paternal line priority) |
| Druze | Druze Personal Status Court | Druze law |
| Christian denominations | Respective ecclesiastical courts | Canon law; appointments confirmed by civil authorities |

Guardianship appointments: confessional court appoints guardian; civil authorities register and enforce. Financial management of a ward's estate: supervised by court; transactions above a threshold (varies by community) require court approval.

### France — Tutelle and Curatelle

For MENA-France dual nationals or for wards habitually resident in France:

**Tutelle** (full guardianship — for persons entirely incapable of managing their own affairs):
- Ordered by the Juge des tutelles (Family Court judge).
- Guardian (tuteur) manages all personal and financial affairs.
- Annual accounting to the court.
- Transactions above certain thresholds require court approval.

**Curatelle** (partial guardianship — for persons who need assistance but not full substitution):
- Ward retains capacity for day-to-day decisions; curator assists with significant decisions.
- Less restrictive than tutelle; preferred by courts when partial assistance is sufficient.

**Habilitation familiale** (simplified family authorization for adults with incapacity):
- Since 2015, allows family members to be granted authority to act for an incapacitated adult without full tutelle.
- Faster and less burdensome than tutelle.

## Document structure

### 1. Application to the Court (for appointment proceedings)

**Header:** Court name, application date, applicant (proposed guardian), ward details.

**Statement of facts:**
- Ward's identity, date of birth, religion, nationality, and current residence.
- Present legal status (minor / incapacitated adult).
- Circumstances necessitating guardianship (death certificate of parents; medical diagnosis of incapacity).
- Proposed guardian's identity, relationship to ward, and fitness.

**Scope of authority requested:**
- Personal care decisions (residence, education, healthcare for minors).
- Financial management powers:
  - Property management (manage but not dispose of real estate without court approval).
  - Investment authority (invest ward's assets conservatively; specify asset classes).
  - Contractual authority (enter contracts on ward's behalf up to [amount] without court approval; larger amounts require court authorization).
  - Business management (if ward holds a business interest).

**Compensation:** propose reasonable compensation from ward's estate, subject to court approval.

**Reporting:** undertaking to file annual accounts to the court; notify court of any change in ward's circumstances.

**Successor guardian:** name a successor guardian to prevent gaps in appointment.

### 2. Guardian's Deed (once appointed)

The guardian's deed confirms the terms of appointment and the guardian's undertakings:

1. **Identity of guardian and ward** — full details; date of court order.
2. **Scope of powers** — as ordered by the court; enumerate.
3. **Investment / property management rules** — conservative investment mandate; no speculative investments; real estate transactions require court approval.
4. **Accounting obligations** — annual accounts in the form required by the court; maintain proper records.
5. **Conflicts of interest** — guardian must notify the court of any transaction in which the guardian has a personal interest; conflicted transactions require independent counsel and court approval.
6. **Compensation** — as approved by the court; reimbursement of documented expenses.
7. **Successor guardian** — upon guardian's death or incapacity, the successor takes over; court notification required.
8. **Termination** — on ward reaching majority; on restoration of ward's capacity; on court order; on death.
9. **Jurisdiction and governing law** — as specified in the appointment order.

## Interaction with will and power of attorney

- **Will**: a parent may appoint a testamentary guardian in their will for minor children. The will is a nomination; the court confirms and appoints. See [[draft-will]] for will drafting, including testamentary guardian nomination.
- **Power of attorney**: for a living adult who wishes to grant authority before incapacity arises, a durable power of attorney is appropriate. Guardianship is court-supervised; a durable PoA is voluntary. See [[draft-power-of-attorney]].
- **DIFC Wills**: for non-Muslim expats in Dubai, a registered DIFC Will can nominate a guardian for children — the most practical mechanism available.

## Common mistakes

1. **Confusing custody (hadanah) with guardianship (wilayah)** — a parent with physical custody does not have legal guardianship (wilayah) under Islamic law if the father is alive; the two concepts must be addressed separately.
2. **Not serving interested parties** — courts require that other persons with legitimate interests (other relatives; previous guardians) be notified and given opportunity to object.
3. **Over-broad financial powers** — requesting unlimited investment authority for a guardian is rejected by courts; define a conservative investment mandate with thresholds above which court approval is required.
4. **No successor named** — a guardianship without a successor creates a gap if the guardian dies or becomes incapacitated.
5. **Ignoring the DIFC Wills Service** for non-Muslim UAE residents — this is the most practical and accessible route to ensure a guardianship nomination is recognized in Dubai.

## Related skills

- [[draft-will]] — will that nominates a testamentary guardian; executed alongside guardianship deed for comprehensive estate planning
- [[draft-power-of-attorney]] — voluntary delegation of authority short of full guardianship (for competent adults)
- [[draft-custody-agreement]] — physical custody arrangement for living separated/divorced parents (distinct from guardianship)
- [[draft-divorce-petition]] — divorce proceeding within which guardianship and custody may be determined
- [[review-personal-status]] — reviewing existing guardianship or custody orders for enforceability
