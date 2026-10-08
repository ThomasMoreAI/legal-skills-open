---
name: prompt-pack-ip-assignment-agreement-sboghossian
title: IP Assignment Agreement
description: Use when a user needs to draft an IP assignment agreement transferring ownership of patents, trademarks, copyrights, or trade secrets from an assignor to an assignee. Covers consideration, ownership representations, further assurances, and recordation obligations. Applies across MENA and international jurisdictions with guidance on civil-law notarization and registration requirements.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-ip-assignment-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# IP Assignment Agreement

## When to use this

Use this prompt pack when a party (individual, company, or research institution) is transferring all right, title, and interest in intellectual property to another party — whether in the context of an employment exit, M&A transaction, spin-out, co-development settlement, or standalone IP monetization deal.

Triggers:
- "I need an IP assignment for [inventor/employee/contractor] assigning their patent rights to the company."
- "We're acquiring a startup and need an IP transfer deed for all their software and trade marks."
- "Draft an assignment covering the copyright in the designs we commissioned."

Do **not** use this skill for a *licence* (where rights are retained); route to [[prompt-pack-patent-license-agreement]] instead.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Assignor name & type | Determines capacity to assign; corporate vs individual | Ask user |
| Assignee name & type | Receiving party; affects recordation formalities | Ask user |
| IP description | Identifies what is being transferred (patent numbers, trade mark registrations, copyright works, trade secrets) | Ask user — be specific |
| Consideration | Required for legal enforceability; may be nominal (e.g. USD 1) or arm's-length | USD 1 + other good and valuable consideration |
| Governing law & jurisdiction | Affects form requirements, notarization, registration timing | Ask user |
| Effective date | When title passes | Date of execution |

## Optional inputs

- **Field-of-use restriction** — unusual in assignments but possible if partial assignment is intended
- **Retained licence back** — assignor retains a licence to use in specific fields post-assignment
- **Employee context** — state whether employment agreement already addresses IP ownership
- **Recorded patent numbers / trade mark registration numbers** — required for USPTO/EUIPO/local IP office recordation
- **Representations on encumbrances** — whether the IP is free of liens, pledges, or prior licences
- **Future improvements** — whether IP created after the effective date that is related to the assigned IP also transfers

## Document structure

1. **Recitals** — describe the relationship between the parties and the purpose of the assignment; cite any prior agreement (employment contract, development agreement) that already obligates assignment.

2. **Assignment clause** — absolute, present-tense grant: "Assignor hereby assigns, transfers, and conveys to Assignee all right, title, and interest in and to the Assigned IP." Specify whether the assignment includes goodwill (mandatory for trade marks in most jurisdictions to be effective against third parties).

3. **Consideration and acknowledgment** — recite the consideration; if nominal, include "the adequacy of which is hereby acknowledged" to fortify enforceability.

4. **Representations and warranties of Assignor**
   - Sole owner of the Assigned IP (or authorized to assign)
   - IP is unencumbered (no prior licences, pledges, security interests)
   - No pending or threatened claims challenging ownership or validity
   - IP does not infringe any third-party rights to Assignor's knowledge

5. **Further assurances** — Assignor agrees to execute any additional instruments (e.g., short-form assignments for recording, powers of attorney for prosecution purposes) and to cooperate in defending validity.

6. **Recordation obligations** — identify which party bears responsibility and cost for recording the assignment with relevant IP offices; set a deadline (e.g., 30 days after execution).

7. **Moral rights waiver** (where applicable) — in civil-law jurisdictions with non-waivable moral rights (FR, LB, EG), include a waiver/non-exercise covenant to the maximum extent permitted by law; note that outright waiver may not be enforceable.

8. **Confidentiality** — if trade secrets are included, retain duty of confidence obligations post-assignment.

9. **Governing law & dispute resolution** — select the law carefully; DIFC/ADGM provide common-law courts suitable for cross-border IP transactions.

10. **Entire agreement / severability / counterparts** — standard boilerplate but ensure counterparts clause covers e-signatures where legally valid.

## Jurisdictional notes

| Jurisdiction | Key requirements |
|---|---|
| **UAE (onshore)** | Assignment of patents/trade marks must be recorded with UAE Ministry of Economy; Arabic version may be required for notarization; no moral-rights waiver in copyright. |
| **UAE / DIFC / ADGM** | English-law friendly; DIFC Courts or ADGM Courts provide neutral forum; assignments recorded with DIFC / ADGM IP registries. |
| **KSA** | IP assignments must be notarized and recorded with SAIP (Saudi Authority for Intellectual Property); Arabic language instrument required for official purposes. |
| **Lebanon** | Assignment notarized before Lebanese notary public; recorded with IP Directorate (Ministry of Economy); moral rights in copyright non-waivable by law (Law No. 75/1999). |
| **Egypt** | Trade mark and patent assignments recorded with Egyptian Patent Office / Trade Marks Registry; Arabic language required; stamp duty applicable. |
| **France / EU** | Copyright moral rights non-waivable; assignment of software copyright must be in writing with specific mention of the assigned rights per Code de la propriété intellectuelle. |
| **UK / common law** | Legal assignment in writing signed by assignor required for copyright (CDPA 1988 s.90(3)); IP office recording for trade marks and patents advisable. |

## Drafting standards

- State the governing law in the first operative paragraph or in a clearly labeled governing law clause — do not bury it.
- Use "assigns, transfers, and conveys" (tripartite) rather than just "assigns" to cover all civil-law concepts of cession.
- Do not use US-style "work-made-for-hire" language for MENA or EU jurisdictions where that doctrine does not apply; instead use a direct assignment of copyright arising from commissioned works.
- If the assignment spans multiple countries, attach a schedule listing each registered IP right by country, number, and filing date.
- Flag the moral rights issue as a comment in the draft and propose the strongest available contractual workaround for the governing law.

## Common mistakes

- **Forgetting trade mark goodwill**: Many jurisdictions (UAE, UK, EU) require goodwill to pass with a trade mark assignment for it to be valid. Omitting this can render the assignment void.
- **Relying on "automatic" employee IP assignment**: In MENA jurisdictions, employment law provisions on IP ownership differ significantly from US/UK defaults. An explicit assignment deed is safer than reliance on the employment contract alone.
- **Not specifying the IP precisely**: Generic descriptions ("all IP relating to the software") are challenged at IP offices. Attach schedules with registration numbers and pending application numbers.
- **Omitting further-assurances on divisional / continuation applications**: Future patent filings derived from the assigned patent should be explicitly captured.
- **Neglecting recordation deadlines**: Some jurisdictions (e.g., KSA) impose time limits for recording; failure to record in time can affect priority over bona fide purchasers.

## Related skills

- [[prompt-pack-ip-due-diligence-checklist]]
- [[prompt-pack-patent-license-agreement]]
- [[prompt-pack-nda-strength-check]]
- [[prompt-pack-merger-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
