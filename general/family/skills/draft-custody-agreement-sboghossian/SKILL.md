---
name: draft-custody-agreement-sboghossian
title: Child Custody Agreement (Post-Divorce / Separation)
description: Use when drafting a child custody and parenting arrangement agreement following divorce or separation. Jurisdiction-sensitive across MENA (hadanah/wilayah split in KSA, UAE, Egypt), Lebanon's 18 confessional courts, and civil-law jurisdictions. Covers physical custody, visitation, decision-making authority, child support, travel consent, and relocation. Always paired with court-ratification advice — most MENA jurisdictions require ratification to give the agreement enforcement weight.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-custody-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: family
language: en
---

# Child Custody Agreement (Post-Divorce / Separation)

## When to use this

Use this skill when parents need a written, structured agreement governing where the child lives, who makes decisions about the child's life, how time is allocated, and how financial support flows — after divorce or separation.

The skill is **jurisdiction-sensitive to a high degree**: religion, confession, and the parents' domicile together determine which court system has jurisdiction and what default rules govern. Before drafting any substantive clause, confirm the applicable legal system.

Do not use this skill as a substitute for local legal counsel in high-conflict custody disputes; recommend local representation and flag that any private agreement requires court or tribunal ratification in MENA jurisdictions to be enforceable against third parties (e.g., border control, schools).

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Both parents' full names, nationalities, and residences | Determines which courts have jurisdiction; multi-national families may have competing jurisdiction | — |
| Child/children (name, date of birth, nationality, habitual residence) | Habitual residence is the primary connecting factor for jurisdiction | — |
| Religion / confession of parents | In MENA, governs which personal-status court and what substantive rules apply | — |
| Marriage details (date, place, type — civil / religious) | Determines dissolution route and applicable law | — |
| Current living arrangements | Baseline for drafting a transition arrangement | — |
| Proposed custody structure | Physical custody holder; decision-making allocation | — |
| Financial capacity of each parent | Informs child support quantum | — |

## Optional inputs

- Existing court proceedings or temporary orders
- International travel restrictions already in place
- Special needs of any child
- Extended family involvement (grandparent access)
- School and healthcare preferences

## Jurisdictional framework

### KSA — Sharia courts

Under classical Islamic jurisprudence as applied by Saudi courts:

- **Hadanah** (physical custody / day-to-day care): mother has priority for young children. Traditional thresholds: boys until age 7, girls until age 9. Contemporary courts exercise discretion beyond these ages based on the child's best interests and the mother's circumstances.
- **Wilayah** (legal guardianship): father retains wilayah regardless of hadanah outcome. Wilayah covers major decisions: education, medical procedures, travel documents, and religious matters.
- **Child support (nafaqa)**: father bears financial responsibility for children regardless of custody arrangement.
- Agreements must be ratified by the Personal Status Court to be enforceable; submit through Najiz platform.

### UAE — Personal Status Law (Federal Law 28/2005)

- Same hadanah / wilayah split as KSA for Muslims.
- New Federal Law 41/2022 allows non-Muslims to opt into a civil personal-status regime that treats spouses more equally and permits joint custody arrangements closer to Western civil-law models.
- Abu Dhabi Civil Family Court established under the 2021 ADJD reforms handles non-Muslim civil cases.
- DIFC Wills and Probate Registry handles succession for non-Muslims; separate from custody.
- Child support: court-assessed; courts apply a financial assessment based on father's documented income.

### Lebanon — 18 confessional jurisdictions

Lebanon has no civil personal-status law for Lebanese nationals. Applicable law is determined by the religious community of each parent:

| Community | Court | Key rules |
|-----------|-------|-----------|
| Sunni | Dar al-Ifta / Sharia court | Hadanah / wilayah framework |
| Shia | Jaafari court | Similar framework with community-specific schools |
| Druze | Druze court | Irrevocable divorce only for men; custody rules derived from Druze doctrine |
| Maronite / Catholic denominations | Ecclesiastical court | Canon law; annulment not divorce |
| Greek Orthodox | Patriarchate court | Orthodox canon law; divorce permitted |
| Civil (via foreign marriage) | Lebanese civil courts on international comity basis | Foreign civil law applied; may be contested |

Key traps:
- Mixed-confession marriages create genuine conflict-of-laws complexity; the court of the respondent's religion typically has jurisdiction.
- Lebanese nationals married abroad under civil law cannot obtain a civil divorce in Lebanon — they must use a foreign court or their confessional court.
- Cross-border enforcement: Lebanese custody orders are not always recognized abroad; include apostille and translation clauses.

### Egypt — Law 100/1985 (Personal Status for Muslims)

- Hadanah: mother has priority; boys until age 15, girls until marriage (court can extend).
- Wilayah (legal guardianship): father.
- Family courts (محاكم الأسرة) established under Law 10/2004 have exclusive jurisdiction.
- Parenting agreements must be ratified by the Family Court.

### France / EU

- Parental authority (autorité parentale) is joint by default post-divorce; unilateral exercise requires court order.
- Primary residence may alternate (garde alternée) or be fixed with one parent.
- Child support assessed by reference to the DGCS reference table (barème pension alimentaire).
- Brussels IIa Regulation (recast as Brussels IIb, effective 2022) governs cross-border jurisdiction within EU.
- Médiation familiale is strongly encouraged pre-litigation.

## Standard clauses

The following clauses apply where permitted by the applicable confessional or civil court regime:

### 1. Physical custody arrangement
Specify the primary residence parent. If shared/alternating, define the schedule with precision: week-on/week-off, academic term / holiday split, start and end times, handover location.

### 2. Visitation schedule
- Regular schedule: weekends (specify which), school holiday halves, public holiday allocation.
- Non-custodial parent's weekly contact minimum.
- Make-up time if a scheduled visit is missed.

### 3. Decision-making authority
Define the categories requiring joint decision-making (education, healthcare, religion, extracurricular activities) vs. day-to-day decisions within the custodial parent's household.

### 4. Child support
- Monthly amount, currency, payment method (direct deposit preferred).
- Indexation mechanism (CPI or agreed percentage per year).
- Treatment of extraordinary expenses (medical, educational, travel).
- Review trigger (significant change in income or needs).

### 5. Travel consent
**Critical for cross-border families.** Specify:
- Consent required for international travel; standard pre-approval period (e.g., 30 days written notice).
- Jurisdictions that require no additional consent (routine day-trips).
- Emergency travel procedure.
- Passport retention: where passports are kept (important in high-conflict situations).
- Countries to which travel requires enhanced consent (disputed jurisdictions, Hague Convention non-signatories).

### 6. Relocation procedure
If the primary custodian wishes to relocate more than X km / to another country:
- Advance notice period (typically 90 days).
- Negotiation period.
- Court approval if no agreement reached.

### 7. Communication
- Minimum weekly video calls between non-custodial parent and child.
- Response time for non-emergency communications.
- No disparagement obligations on both parents.

### 8. Variation clause
Agreement may be amended by written consent of both parents (subject to court ratification if required). Either parent may apply to court if circumstances materially change.

## Drafting standards

- **Name the child specifically** — generic drafting fails when a parent has children from multiple relationships.
- **Currency and payment mechanism** — in LB, specify USD vs LBP and actual transfer mechanism; LBP-denominated support has eroded dramatically in real terms.
- **No self-help provisions** — clauses permitting a parent to withhold visitation if support is unpaid are unenforceable in most jurisdictions and harmful to children. Do not draft them.
- **Court ratification advisory** — always include a clause stating the agreement is subject to ratification and the parties undertake to present it to the relevant court / tribunal for approval.
- **Bilingual** — in MENA jurisdictions, Arabic version is required for court filing; English is often the working language.

## Common mistakes

1. **Conflating hadanah with wilayah** — physical custody and legal guardianship are distinct concepts in Islamic-law systems; a mother holding hadanah does not have wilayah.
2. **Omitting travel consent detail** — the most litigated issue in cross-border families; vague language creates immediate disputes.
3. **Under-specifying handover logistics** — time, place, and transport responsibility must be explicit.
4. **No indexation on child support** — inflation (especially acute in Lebanon) erodes nominal support rapidly.
5. **Non-Muslims in MENA using Islamic-law defaults** — UAE Federal Law 41/2022 provides a civil alternative; present the option.

## Related skills

- [[draft-divorce-petition]] — the divorce proceeding within which the custody arrangement is typically settled
- [[draft-guardianship]] — appointing a guardian for minors in cases of parental incapacity or death
- [[draft-child-support-order]] — standalone support order where custody is already agreed
- [[review-personal-status]] — reviewing existing custody orders for enforceability and currency
