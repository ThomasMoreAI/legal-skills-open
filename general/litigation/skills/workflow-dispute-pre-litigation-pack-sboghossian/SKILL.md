---
name: workflow-dispute-pre-litigation-pack-sboghossian
title: Dispute Pre-Litigation Pack
description: Use when a user needs to prepare for litigation or arbitration — documenting a dispute, sending pre-action correspondence, evaluating claims and limitation periods, and deciding whether to file court proceedings or arbitration. Covers the full pre-litigation workflow from facts to filing decision, with MENA-specific limitation periods, arbitration clause analysis, and jurisdictional notes for UAE, KSA, LB, DIFC, and ADGM.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-dispute-pre-litigation-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Dispute Pre-Litigation Pack

## Purpose

This workflow guides the full pre-litigation process — from the moment a dispute arises to the decision to file (or not). The output is a documented dispute file, pre-action correspondence, and a clear filing recommendation. The critical constraint at every step: **the statute of limitations clock does not pause for negotiations**.

---

## Inputs

| Input | Required | Notes |
|-------|---------|-------|
| Dispute facts | Yes | Chronological narrative of what happened |
| Contract or legal basis | Yes | Underlying agreement or cause of action |
| Governing law | Yes | Determines claims, defenses, limitation periods |
| Counterparty identity | Yes | For conflict check and service of process |
| Desired outcome | Yes | Damages? Injunction? Specific performance? |
| Timeline of events | Yes | Key dates — helps calculate limitation period |
| Amount in dispute | Recommended | Drives cost/benefit analysis; determines which courts have jurisdiction |
| Insurance policies | Recommended | D&O, E&O, commercial liability — may require timely notification |

---

## Logic — Step-by-Step

### Step 1: Conflict Check and Engagement

Before any substantive work:
1. Run conflict check — [[efirm-conflict-check]] — ensure no prior representation of the counterparty
2. Engagement letter signed — [[draft-engagement-letter]] — before substantive analysis
3. Document privilege from the outset: communications should be lawyer-client from day one

### Step 2: Facts and Claims Assessment

**Factual narrative** — build a chronological timeline:
- List every material event with date, participants, and source document
- Identify the precipitating event (breach, tort, default, termination)
- Map the chain of causation from breach to damages

**Legal claims identification:**
- What cause(s) of action apply?
  - Breach of contract (most common): element checklist: valid contract, breach, causation, damages
  - Tort: depends on jurisdiction (civil law: delict under applicable code; common law: tort categories)
  - Unjust enrichment / quasi-contract: civil law jurisdictions often have explicit enrichment claims
  - Specific statutory claims: employment violations, IP infringement, competition law
- Map each claim to the applicable statute or common-law rule

**Damages calculation:**
- Direct / expectation damages: what would the non-breaching party have received if the contract had been performed?
- Consequential damages: recoverable only if foreseeable at time of contracting (Hadley v Baxendale rule in common law; similar civil law principles)
- Mitigation duty: the claimant must take reasonable steps to mitigate; failure to mitigate reduces recoverable damages
- Liquidated damages: if the contract provides a damages clause, analyze enforceability in the applicable jurisdiction (see jurisdictional notes below)

### Step 3: Statute of Limitations — Critical

**This is the highest-priority step.** Missing a limitation period extinguishes the claim regardless of its merits.

| Jurisdiction | Contract claims | Tort claims | Notes |
|-------------|----------------|-------------|-------|
| UAE (federal) | 15 years (Civil Code) | 3 years from knowledge of damage | Commercial claims: 10 years; some special claims have shorter periods |
| KSA | No codified general limitation period; case-by-case under judicial discretion; practical: file within 5 years | Varies | Sharia courts have flexibility; practical urgency: do not delay |
| Lebanon | Contract: 10 years (Code of Obligations); some specific contracts shorter | 3 years | Employment: 1 year after dismissal for many claims |
| DIFC | Contract: 6 years (DIFC Contract Law, mirroring English Limitation Act concepts) | 6 years (property), 3 years (personal injury) | DIFC Courts apply DIFC-specific limitation rules |
| ADGM | 6 years for contract and simple tort | ADGM follows English law approach | ADGM Courts have jurisdiction over ADGM entities |
| Egypt | Contract: 15 years (Civil Code Art. 374); commercial contracts: 7 years | 3 years | Insurance: 3 years |
| England & Wales | 6 years (Limitation Act 1980) | 6 years (contract); 3 years (personal injury) | |
| US (varies by state) | 3–6 years (contract); varies by tort | Varies | UCC contracts: 4 years in most states |

**If the limitation period is approaching (within 6 months):**
- File before negotiating — a filed complaint can be withdrawn; a missed deadline cannot be fixed
- Seek a tolling agreement: both parties agree to pause the limitation clock during negotiations (get this in writing)

### Step 4: Pre-Action Correspondence

In most jurisdictions, pre-action correspondence is required, expected, or strategically valuable:

**Demand letter** — [[draft-demand-letter]]:
- State the claim clearly and factually
- Specify the exact remedy demanded (amount, specific action)
- Set a clear deadline (14–21 days is typical; shorter for urgent IP matters)
- State the consequence of non-compliance (litigation / arbitration)
- Keep the tone professional; avoid threats that could constitute extortion under local law

**Without-prejudice communications:**
- Label all settlement communications "without prejudice" (common law) or "sans préjudice" (civil law, French influence)
- In UAE and KSA civil law, the concept applies but with less developed procedural protection than in English law — be cautious about what goes in without-prejudice correspondence
- A "without prejudice save as to costs" (Calderbank offer) is useful in DIFC proceedings to protect a cost position

**Cease and desist** — [[draft-cease-and-desist]] — if the dispute involves ongoing IP infringement, contractual breach, or solicitation of employees.

### Step 5: Mediation / ADR Consideration

Many contracts include a mandatory mediation or negotiation step before arbitration or litigation:
- Check the dispute resolution clause carefully: is there a condition precedent to filing?
- Most MENA courts actively encourage pre-filing mediation; some (UAE Mediation and Conciliation Law) require it for certain cases
- DIAC, DIFC-LCIA, and ICC all offer mediation services
- Benefits of mediation: confidential; flexible; preserves relationship; typically 30–60 days
- Document mediation participation — needed to show compliance if a condition precedent

### Step 6: Forum and Jurisdiction Analysis

**Where to file?** This decision determines procedure, cost, timeline, and enforceability:

| Forum | Features | MENA notes |
|-------|---------|-----------|
| UAE Federal Courts | Arabic proceedings; civil law; UAE mainland parties | Judgments enforceable in UAE; limited international enforcement |
| DIFC Courts | English law; English language; highly professional | New York Convention arbitration awards enforceable; DIFC Courts have enforcement protocols |
| ADGM Courts | English law; English language | Similar to DIFC; growing caseload |
| DIAC Arbitration | Dubai International Arbitration Centre; institutional rules | Very active for UAE/MENA commercial disputes |
| ICC Arbitration | Global institution; Paris secretariat | Preferred for large international disputes; expensive |
| DIFC-LCIA | DIFC-specific institution; London arbitration rules | Common for financial services and structured finance |
| MENA national courts | Country-specific | Lebanon courts: slow but improving; KSA: MHRC for commercial disputes; Egypt: Economic Courts for commercial |

**Arbitration clause check:**
- Does the contract contain an arbitration clause? If yes, court proceedings may be inadmissible — file arbitration request instead
- Is the arbitration clause enforceable? Check: seat, rules, arbitrator number, and language are all specified; check if the clause excludes any types of dispute
- Interim relief: courts can grant emergency injunctions even if arbitration clause exists; DIFC and ADGM courts are active on this

### Step 7: Third-Party Litigation Funding Assessment

For large claims (typically $1M+):
- Litigation funders (Burford Capital, Omni Bridgeway, Augusta Ventures) provide non-recourse financing in exchange for a share of recovery
- Common structures: funder advances legal fees; takes 20–40% of net recovery
- Suitable for: strong liability case; damages calculable; counterparty able to pay; case duration 18–36+ months
- DIFC and ADGM permit third-party funding; UAE mainland less clear — verify

### Step 8: Filing Decision

Make a final recommendation:

| Option | When appropriate |
|--------|----------------|
| File now | Limitation period imminent; counterparty unresponsive; ongoing harm; no realistic settlement prospect |
| Continue negotiation | Active negotiations; reasonable counterparty; deal possible; limitation period not imminent |
| File arbitration request | Contract contains arbitration clause; appropriate forum available |
| Seek interim relief only | Emergency (asset dissipation; ongoing infringement); file for interim injunction before full proceedings |
| Stand down | Claim too weak; damages too small; enforcement impossible (counterparty has no assets) |

---

## Critical Risk Controls

| Risk | Mitigation |
|------|-----------|
| Statute expiry | Track exact deadline from day one; set reminders at 6 months and 1 month before expiry |
| Pre-litigation conduct as evidence | Everything written or said pre-litigation can become evidence; document carefully |
| Without-prejudice contamination | Label all settlement communications correctly and promptly |
| Failure to notify insurer | D&O and E&O policies typically require prompt notification; late notification may void coverage |
| Asset dissipation | If counterparty is likely to hide assets, consider emergency freezing order (garnishment / Mareva injunction) simultaneously with filing |

---

## Output

1. **Dispute chronology** — dated timeline of key events with source documents
2. **Claims and damages analysis** — cause of action, damages calculation, confidence level
3. **Limitation period memo** — exact expiry dates and urgency assessment
4. **Demand letter** — [[draft-demand-letter]] delivered to counterparty
5. **Pre-action correspondence file** — all communications documented
6. **Forum and jurisdiction recommendation** — where to file and why
7. **Filing decision memo** — recommendation with rationale

---

## Related Skills

- [[draft-demand-letter]]
- [[draft-cease-and-desist]]
- [[draft-engagement-letter]]
- [[draft-litigation-complaint]]
- [[draft-arbitration-request]]
- [[efirm-conflict-check]]
- [[wiki-research]]
