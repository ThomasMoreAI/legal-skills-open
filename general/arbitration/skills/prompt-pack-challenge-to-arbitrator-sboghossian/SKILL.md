---
name: prompt-pack-challenge-to-arbitrator-sboghossian
title: Challenge to Arbitrator
description: Use when a party to arbitration needs to draft a formal challenge to an arbitrator based on conflicts of interest, lack of impartiality, or lack of independence. Covers ICC, LCIA, DIAC, ADGM, SIAC, and UNCITRAL rules; addresses the IBA Guidelines on Conflicts of Interest; and flags MENA-specific considerations including challenge procedures under UAE, DIFC, KSA, and Lebanon arbitration law.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-challenge-to-arbitrator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Challenge to Arbitrator

An arbitrator challenge is a high-stakes procedural step: the threshold for success is deliberately set high, and a failed challenge can damage credibility before the tribunal while strengthening the opponent's position. A well-crafted challenge must be factually precise, legally grounded in the applicable rules, and filed within strict time limits.

## When to use this

- A party has discovered facts that give rise to justifiable doubts about an arbitrator's impartiality or independence under the applicable rules.
- New information about an undisclosed relationship between an arbitrator and the opposing party or its counsel has surfaced during proceedings.
- An arbitrator has made procedural rulings that, taken together with other circumstances, suggest bias.
- The arbitration clause or the rules specify a challenge procedure and a deadline is imminent.

Do not use this skill to bring tactical or dilatory challenges — challenge grounds must be genuine. Filing a groundless challenge can expose the challenging party to adverse costs and sanctions.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Arbitration case reference or proceeding name | Identifies the proceeding formally | Ask the user |
| Arbitrator's name and role (sole, presiding, co-arbitrator) | The challenge is directed at a specific individual | Ask the user |
| Grounds for the challenge (conflict of interest / lack of impartiality / lack of independence) | The legal basis for the challenge | Ask the user to describe the specific facts giving rise to the challenge |
| Applicable arbitral rules | The procedural framework determines how and to whom the challenge is filed | Ask the user: ICC / LCIA / DIAC / ADGM / SIAC / UNCITRAL / ad hoc |
| Date when the challenging party became aware of the grounds | Most rules start a short time limit from date of knowledge | Ask the user — this is critical |
| Supporting evidence | The challenge must be supported by documentary proof | Ask the user to attach or describe available evidence |

## Optional inputs

- Prior communications from or with the arbitrator on the relevant relationship.
- The arbitrator's curriculum vitae or published disclosures (IBA Orange/Red List background check recommended).
- Whether the challenge is also being raised as a set-aside ground (post-award) as a fallback.
- Whether local counsel in the seat jurisdiction needs to be involved.

## Document structure

### 1. Heading / identification
- Case name and reference number.
- Names of the parties.
- Name of the institution (if any) or the co-arbitrators if an ad hoc challenge.
- Date of the challenge.
- Name of the challenging party and its counsel.

### 2. Procedural basis
- Cite the specific rule under which the challenge is filed (e.g., ICC Rules Art. 14–15; LCIA Rules Art. 10; DIAC Rules Art. 13; UNCITRAL Rules Art. 12–13; DIFC Arbitration Law Art. 13).
- State that the challenge is filed within the applicable time limit, citing the date of knowledge and the date of the challenge.
- If the time limit is close to expiry, note that the challenge is filed without prejudice to any rights that may arise from subsequently discovered facts.

### 3. Standard to be applied
- Most rules apply a "justifiable doubts" standard (UNCITRAL Model Law Art. 12(2)): circumstances that give rise to justifiable doubts about the arbitrator's impartiality or independence, judged objectively.
- The IBA Guidelines on Conflicts of Interest in International Arbitration (2014, updated 2024) provide the authoritative framework; the Red List identifies non-waivable conflicts, the Orange List waivable ones.
- Some institutional rules (LCIA, SIAC) apply a slightly higher standard of "real danger of bias"; flag if the applicable rules differ.

### 4. Statement of facts
Provide a precise, chronological factual narrative:
- The relationship, connection, or conduct that gives rise to the challenge.
- When and how the challenging party discovered these facts.
- What disclosure, if any, the arbitrator made and when.
- Any prior knowledge the challenging party had (which may affect the timeliness argument).

Keep this section strictly factual; argument comes in the next section.

### 5. Legal analysis
Map the facts to the applicable standard:
- Identify the specific category of conflict or bias ground (e.g., financial interest, prior representation, personal relationship, unconscious bias arising from conduct in proceedings).
- Cite the relevant IBA Guidelines category (Red, Orange, or Green list item).
- Apply the objective "justifiable doubts" test: would a fair-minded, informed observer have justifiable doubts?
- Address any disclosure failure separately: non-disclosure of a fact that should have been disclosed itself constitutes grounds under most rules, even if the underlying conflict would otherwise be waivable.

### 6. Relief requested
- Primary: disqualification of the named arbitrator from the proceedings.
- Consequential: suspension of the arbitral proceedings pending determination of the challenge.
- Costs: the challenging party's costs of the challenge, particularly if the arbitrator or institution caused delay by failing to disclose.

### 7. Evidence schedule
List all documents submitted in support, numbered sequentially as Exhibits C-1, C-2, etc.

## Jurisdictional and rules-specific notes

| Forum / Seat | Challenge procedure |
|---|---|
| ICC | Filed with the ICC Court of Arbitration; other party and arbitrator comment; Court decides without giving reasons; non-recourse to state courts during challenge |
| LCIA | Filed with the LCIA Court; full written submissions; LCIA Court decides; strictly confidential |
| DIAC (Dubai) | Filed with the DIAC; challenge decided by remaining tribunal or DIAC; governed by UAE Federal Arbitration Law No. 6 of 2018 |
| DIFC Arbitration Centre | DIFC Arbitration Law Art. 13 (UNCITRAL Model Law basis); challenge decided by institution or, failing agreement, DIFC Court |
| ADGM | ADGM Arbitration Regulations (2015); Model Law based; challenge decided by ADGM Court if institution fails to act within 30 days |
| UNCITRAL (ad hoc) | Challenging party notifies other party and tribunal within 15 days of knowledge; if not agreed, party may request national court to decide (seat's arbitration law governs) |
| KSA | Saudi Arbitration Law (Royal Decree No. M/34, 2012); challenge filed with arbitral institution or competent court; Arabic proceedings required for domestic disputes |
| Lebanon | Lebanese Arbitration Law (NCPC Arts. 762 et seq.); challenge before the president of the court of first instance if no institutional mechanism applies |

## Common mistakes

- **Missing the time limit.** Most rules require the challenge within 15–30 days of knowledge of the grounds. Missing this deadline forfeits the right to challenge (though the right to rely on the ground as a set-aside ground post-award may survive).
- **Confusing tactical delay with genuine grounds.** Institutions and courts are sophisticated; unfounded challenges are dismissed, often with costs.
- **Insufficient factual support.** "Apparent bias" from rulings alone is very rarely sufficient; concrete relationship facts are required.
- **Failing to distinguish the IBA list category.** Red List conflicts are non-waivable; Orange List conflicts can be waived by parties with knowledge; characterizing a Red List situation as Orange can be challenged by the institution.
- **Not considering the seat court as a fallback.** If the institution rejects the challenge, the seat's national arbitration law may allow an application to the national court within a further limited period.

## Related skills

- [[prompt-pack-arbitration-statement-of-claim]]
- [[prompt-pack-case-assessment-memo]]
- [[prompt-pack-demand-letter]]
- [[prompt-pack-arbitration-award-enforcement]]
- [[prompt-pack-arbitration-interim-measures]]
