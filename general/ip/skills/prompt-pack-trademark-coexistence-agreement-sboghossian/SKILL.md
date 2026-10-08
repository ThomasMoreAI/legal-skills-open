---
name: prompt-pack-trademark-coexistence-agreement-sboghossian
title: Trademark Coexistence Agreement
description: Use when two trademark owners holding similar or identical marks need a binding agreement defining how they will coexist in the same or overlapping markets without confusion or infringement claims — typically arising from parallel registrations, expansion into each other's territory, or to resolve a trademark office opposition. Covers permitted uses, geographic and product-class limitations, dispute mechanisms for future conflicts, and mutual consent to registration provisions. Relevant across MENA and common-law jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-trademark-coexistence-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Trademark Coexistence Agreement

## When to use this

Use this skill when:

- Two companies own similar or identical trademarks in the same class and need to resolve coexistence to avoid mutual opposition proceedings or litigation
- A trademark office has raised a relative ground refusal (likelihood of confusion) and the applicant needs a consent / coexistence agreement from the earlier-rights holder to overcome it
- One party is expanding geographically into another party's market and a consent arrangement is preferable to litigation
- Parties reached a settlement in trademark infringement proceedings and need to memorialize co-existence terms

This is not a license — neither party is "licensing" its mark to the other. Each party retains ownership of its own mark; the agreement governs the boundary conditions under which both marks can coexist.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Party A full name + mark details (word mark, device, classes, registration numbers) | Defines the scope of each party's rights | Prompt user |
| Party B full name + mark details | Same | Prompt user |
| Description of similarity / conflict | Articulates why an agreement is needed | Prompt user |
| Territory of each party's permitted use | Geographic scope is the primary risk-management lever | Current registration territories; negotiate expansion notice rights |
| Goods / services for each party | Class-based or sub-class restrictions | Registered classes; if overlap, negotiate use restrictions by sub-category |
| Consent-to-registration scope | Defines what each party will consent to file / maintain | Specific countries and classes listed in Schedule A |

## Optional inputs

- **Visual differentiation requirements** — color, font, trade dress differences required to maintain distinctiveness
- **Non-opposition and non-cancellation covenants** — each party's commitment not to oppose or cancel the other's registrations
- **Expansion notification clause** — notice obligation before either party expands to new territory or class
- **Arbitration / expedited dispute mechanism** — if a future conflict arises between the marks
- **Confidentiality** — coexistence arrangements are sometimes sensitive commercial information

## Document structure

1. **Recitals** — history of the parties' marks; the conflict or opposition that necessitated the agreement; purpose of the arrangement
2. **Definitions** — "Mark A," "Mark B," "Territory A," "Territory B," "Permitted Goods/Services A," "Permitted Goods/Services B," "Confusion Threshold," "Registration Consent"
3. **Scope of permitted use — Party A** — the specific marks, territories, classes, and use contexts in which Party A may use its mark; any required visual differentiation obligations
4. **Scope of permitted use — Party B** — same for Party B; may be asymmetric
5. **Consent to registration** — each party's consent to the other's current and future registrations within agreed parameters; parties agree not to oppose each other's applications within scope; form of consent letter (often a separate Schedule for submission to trademark office)
6. **Non-disparagement** — neither party may take actions that undermine the value or validity of the other's mark (e.g., no claims that the other's mark is generic)
7. **Non-opposition and non-cancellation covenants** — each party agrees not to oppose, challenge, or petition to cancel the other's registrations within the agreed scope; carve-out for breach of the agreement
8. **Quality and use standards** — each party maintains quality standards so neither mark degrades in a way that harms the other's reputation
9. **Expansion notification** — prior written notice (e.g., 60 days) before either party seeks new registrations or begins use in new territories or classes that approach the boundary; consultation period before opposition is filed
10. **New conflicts clause** — procedure if a third party's mark creates confusion with one party's mark in a way that implicates the other; cooperation obligations
11. **Representation and warranties** — each party represents it owns its mark, it is not aware of pending cancellation proceedings, and it has authority to enter the agreement
12. **Duration and termination** — term tied to validity of the marks; termination for material breach; 30–90 day cure period before termination; effect on consent-to-registration upon termination
13. **Assignment** — whether the agreement runs with the mark (binds successors-in-title) or is personal; assignment of the mark should include assignment of the agreement
14. **Governing law and dispute resolution** — choice of court or arbitration (DIAC, SIAC, ICC, LCIA common in MENA); governing language clause
15. **Schedules** — A: Mark registrations and applications; B: Territory map; C: Permitted goods and services by class; D: Form of consent letter for trademark offices

## Jurisdictional notes

| Jurisdiction | Key instrument | Notable point |
|---|---|---|
| UAE (onshore) | Federal Decree-Law No. 36/2021 on Trademarks | Ministry of Economy (MOE) registers trademarks; consent of earlier rights holder can overcome relative ground opposition; Arabic text of agreement may be required for MOE submission |
| DIFC / ADGM | No separate trademark law — DIFC / ADGM residents use UAE federal registration + WIPO Madrid Protocol | Agreement binding as commercial contract under DIFC Contract Law or common law |
| KSA | Saudi Trademarks Law (Royal Decree M/21/2020) + implementing regulations | SAIP (Saudi Authority for Intellectual Property) oversees registration; coexistence agreements submitted as supporting documents for consent; Arabic version required |
| Lebanon | Industrial and Commercial Property Law No. 240/2000 | Ministry of Economy and Trade registration; consent letter practice less developed; agreement can be used as evidence in opposition/cancellation proceedings |
| Egypt | Trademark Law No. 82/2002 (Part I) | EGYPO (Egyptian Patent Office) oversees; consent letters accepted; agreement should be notarized and translated into Arabic |
| GCC (as bloc) | GCC Trademark Office | GCC-wide registration available; coexistence agreement scope should specify whether it covers the GCC bloc registration in addition to national filings |
| EU | EU Trade Mark Regulation (EUTMR); EUIPO | EUIPO accepts letter of consent to overcome relative grounds; coexistence agreement must cover all EU member states for an EUTM consent |
| UK | Trade Marks Act 1994; UKIPO | Post-Brexit EUTM no longer covers UK; separate UK TMA consent required |

**Critical trap — "runs with the mark":** If the agreement does not expressly bind assignees and successors, a party that sells its business can inadvertently void the coexistence arrangement. Always include an assignment clause requiring the burden and benefit to pass to mark successors.

**MENA opposition window:** UAE trademark opposition window is 30 days from publication; KSA is 60 days. Time from amicable agreement to executed consent letter must fit within these windows if the agreement is being used to overcome an opposition.

**Moral rights and trade dress (civil law):** In Lebanon and Egypt, judicial interpretation of trademark law may give weight to visual similarity beyond the registered mark. Consider including a trade dress differentiation schedule.

## Drafting standards

- **Be specific about permitted classes and territories** — vague descriptions of scope are the primary source of future disputes; use NICE classification numbers
- **Include a form consent letter as a Schedule** — trademark offices in UAE, KSA, and Egypt need a standalone letter (not just the coexistence agreement) to process consent to registration
- **No injunction-by-default language** — in civil-law jurisdictions, injunctions are not automatic; include an interim relief cooperation clause
- **Language of the agreement** — in KSA and UAE, an Arabic version (or bilingual with Arabic controlling in local proceedings) is essential

## Common mistakes

- **Not specifying that the agreement runs with the mark** — renders it valueless on assignment
- **Using the agreement as a license** — if Party A authorizes Party B to use Party A's mark (rather than permitting B to use B's own mark), you have a license, not a coexistence agreement; different legal regime applies
- **Omitting the expansion notification clause** — leaves the boundary undefined for future geographic expansion
- **Failing to attach current registration details as a Schedule** — creates ambiguity about which registrations the consent covers
- **Single-language agreement submitted to an Arabic-language trademark office** — will be returned or require separate notarized translation

## Related skills

- [[prompt-pack-trademark-license-agreement]]
- [[prompt-pack-nda-mutual]]
- [[kb-ip-mena]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
