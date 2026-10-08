---
name: prompt-pack-work-for-hire-agreement-sboghossian
title: Work for Hire Agreement
description: Use when a company needs to engage a freelancer, consultant, or contractor to create copyrightable works (software, designs, content, marketing materials, technical documentation) and the company wants to own all resulting intellectual property. Covers work-for-hire declaration, IP assignment (belt and suspenders), moral rights waiver, delivery specifications, and payment terms. Critical in MENA where the US statutory work-for-hire doctrine does not apply — an express assignment is always required.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-work-for-hire-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Work for Hire Agreement

## When to use this

Use this skill when a company engages an independent contractor (not an employee) to create works that the company needs to own outright — not merely license. Typical scenarios:

- A software company engaging a freelance developer to build a custom module or application
- A marketing team commissioning a graphic designer or photographer for branded assets
- A startup engaging a content writer for web copy, white papers, or thought leadership
- An architecture or engineering firm commissioning technical drawings from a subconsultant
- A film production company commissioning music composition or visual effects

**Why "belt and suspenders"?** In the US, works created by independent contractors can be "works made for hire" under the Copyright Act if they fall within one of nine enumerated categories and there is a written agreement. Outside the US — and this is critical — the statutory work-for-hire concept does not exist in the same form. In UAE, KSA, Lebanon, Egypt, and the EU, copyright vests automatically in the natural person who created the work. The only reliable way for a company to own contractor-created work outside the US is an express IP assignment. The agreement should therefore include both a work-for-hire declaration (effective if the work qualifies under applicable law) AND an express present-tense assignment ("the Contractor hereby assigns all right, title, and interest") as a fall-back.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Company (purchaser) full name + registered address | The entity that will own the IP | Prompt user |
| Contractor / creator full name + address | The individual or entity creating the work | Prompt user — if a company, confirm whether the actual creator is an employee of that company |
| Description of the work / deliverables | Defines the scope of the IP assignment | Prompt user — be specific: software means source code AND object code AND documentation AND test suites |
| Delivery specifications | Acceptance criteria; format; handover method | Prompt user |
| Fees and payment schedule | Consideration for the assignment | Prompt user; milestone-based payments are common |
| Governing law | Determines IP assignment formalities | Jurisdiction of the company's primary operations |

## Optional inputs

- **Confidentiality / NDA obligation** — if contractor will be exposed to company trade secrets during the engagement
- **Non-solicitation** — restriction on contractor soliciting company's employees or customers during and for a period after the engagement
- **Background IP** — if contractor brings pre-existing IP ("background IP") that will be incorporated into the deliverables, the agreement must grant the company a license to that background IP
- **Third-party components** — contractor's disclosure and warranty that deliverables do not incorporate open-source code or third-party IP without disclosed licenses
- **Right of first refusal** — company right to engage contractor for future related works
- **Kill fee** — if company terminates for convenience before delivery, a defined kill fee is often negotiated

## Document structure

1. **Definitions** — "Work," "Deliverables," "Background IP," "Foreground IP," "Moral Rights," "Open Source Software," "Confidential Information," "Acceptance Criteria"

2. **Services and deliverables** — specific description of what the contractor will create; delivery timeline (milestone schedule if applicable); specification of format and handover method (e.g., GitHub repository with transfer of ownership; layered design files in Figma/Sketch; source files and raw assets)

3. **Work-for-hire declaration** — to the fullest extent permitted by applicable law, all Foreground IP created under this agreement constitutes works made for hire for the company; the company is the author and owner from creation; this clause is effective in US law for qualifying works; note that in non-US jurisdictions this is supplemented by §4

4. **IP assignment (belt and suspenders)** — to the extent any Foreground IP does not constitute a work made for hire: the Contractor hereby irrevocably assigns to the company all right, title, and interest in and to such Foreground IP, including all patents, copyrights, moral rights (to the extent waivable), trade secrets, database rights, and other intellectual property rights, in all media and formats, throughout the world, for the full term of any such rights; the assignment is for consideration received (recited)

5. **Moral rights waiver** — to the maximum extent permitted by applicable law, the Contractor irrevocably waives all moral rights (including the right of paternity and the right of integrity) in the Foreground IP in favor of the company and its successors and assigns; note that in France, Lebanon, and some other civil-law jurisdictions, moral rights are inalienable and cannot be waived — in those jurisdictions, the contractor must agree not to exercise moral rights in a manner adverse to the company (the practical equivalent of a waiver)

6. **Background IP** — contractor identifies and discloses all Background IP to be incorporated; grants company a perpetual, irrevocable, royalty-free license to use Background IP as incorporated in the Deliverables; contractor represents that it has the right to grant this license; company does not acquire ownership of Background IP

7. **Open-source and third-party components** — contractor warrants it will not incorporate open-source software under a "copyleft" license (GPL, AGPL) without prior written approval; if approved, contractor discloses the specific components and licenses; contractor warrants no third-party IP is incorporated without appropriate license

8. **Representations and warranties** — contractor: (a) is the original creator of the Foreground IP; (b) has full right and authority to make this assignment; (c) the Foreground IP does not infringe any third-party IP rights; (d) no liens or encumbrances on the IP; (e) Deliverables conform to the specifications; company: authorized to enter the agreement; payment obligations are valid

9. **Delivery and acceptance** — delivery timeline; acceptance procedure; acceptance criteria; consequence of failure to deliver (termination, rework obligation); deemed acceptance after [10-business-day] review period with no objection

10. **Fees and payment** — fee amounts; payment schedule (e.g., 30% on execution; 40% on delivery; 30% on acceptance); invoicing requirements; late payment interest; taxes (contractor responsible for its own income taxes; company responsible for applicable VAT/GST on fees)

11. **Confidentiality** — contractor obligations re: company Confidential Information; during and [3 years] post-engagement; return of confidential materials on termination; carve-out for publicly available information

12. **Term and termination** — fixed project term; termination for cause (material breach, 14-day cure); termination for convenience by company (kill fee if applicable); effect on IP: assignment is irrevocable even if company terminates for convenience; partial assignment of IP for completed deliverables

13. **Governing law and dispute resolution** — choice of law; dispute resolution (arbitration or court); escalation procedure

14. **Further assurances** — contractor must execute any documents (formal copyright assignment deeds, patent applications, trademark assignments) reasonably required to perfect the company's IP ownership after the agreement ends

15. **Schedule A** — deliverables list with specifications; Schedule B — milestone and payment schedule

## Jurisdictional notes

| Jurisdiction | Copyright ownership of contractor works | Moral rights | Formality for assignment |
|---|---|---|---|
| UAE | Federal Decree-Law No. 38/2021 on IP — copyright vests in the creator; assignment must be in writing | Moral rights recognized; cannot be waived but can be agreed not to exercise | Written assignment required; notarization recommended for major works; Arabic version for UAE courts |
| DIFC | Common law copyright (DIFC IP Law 2019) — no statutory work-for-hire for contractors; assignment required | Moral rights waivable in writing | Written assignment; DIFC Law of Obligations applies |
| ADGM | English-law-influenced IP regime; no contractor work-for-hire; assignment required | Moral rights partially waivable | Written assignment |
| KSA | Copyright Law (Royal Decree M/41/2002 as amended 2020) — copyright vests in creator; employer-employee exception for employment only | Moral rights recognized (right of attribution, integrity); cannot be assigned but practical waiver possible | Written assignment required; Arabic required; SAIP registration recommended for high-value works |
| Lebanon | Intellectual Property Law No. 75/1999 — copyright vests in creator | Moral rights inalienable under Lebanese law | Written assignment required; best practice: notarized |
| Egypt | Intellectual Property Law No. 82/2002 — copyright vests in creator | Moral rights perpetual and inalienable | Written assignment required; may be registered at EGYPO |
| EU | Software Directive (2009/24/EC) — employer-employee works: employer owns; contractor works: creator owns | Moral rights vary by member state (FR: inalienable; DE: limited waiver; NL: limited waiver) | Written assignment; some member states require specific formalities |
| UK | Copyright Designs and Patents Act 1988 — contractor works vest in contractor; employee works vest in employer | Moral rights waivable in writing | Written assignment |
| US | Copyright Act § 101 (work made for hire for employees; for contractors: only if commissioned for specified categories AND written agreement) | No moral rights for most works; Visual Artists Rights Act limited exception | Written agreement required for work-for-hire designation; otherwise assignment |

**MENA moral rights trap:** In Lebanon and Egypt, moral rights are inalienable. The drafter cannot simply insert a waiver clause and expect it to be effective. Instead, include a clause under which the contractor agrees not to exercise moral rights in any manner adverse to the company's use, exploitation, or modification of the deliverables — this achieves the commercial effect of a waiver without purporting to extinguish inalienable rights.

**Employees vs. contractors:** If the purported "contractor" is actually an employee under local labor law (relevant in UAE, KSA, and Lebanon where the distinction is fact-specific), the work-for-hire and assignment provisions may operate differently. Flag if the engagement appears to be a disguised employment relationship.

## Drafting standards

- **Always include both work-for-hire AND assignment clauses** — the assignment is the operative provision in MENA and EU; the work-for-hire clause adds protection for US-nexus works
- **"Hereby assigns" in present tense** — a future-tense assignment ("contractor agrees to assign") creates only a contractual obligation, not an immediate proprietary transfer; use "irrevocably assigns" or "hereby assigns"
- **Source code delivery obligation** — specify that source code (not just compiled output), test suites, and documentation must be delivered; failure to specify often results in disputes at delivery
- **Further assurances clause is essential** — IP registration formalities often arise months or years after the engagement ends; the contractor must be contractually obligated to cooperate

## Common mistakes

- **Relying on work-for-hire alone outside the US** — invalid in MENA and EU for independent contractors
- **Future-tense assignment** — "agrees to assign" is not the same as "hereby assigns"; creates a promise, not a property right
- **No background IP license** — if contractor's pre-existing code is incorporated and there is no license, the company may not be able to use the deliverable without infringing the contractor's IP
- **Moral rights ignored** — particularly in LB, EG, and FR; an aggressive interpretation can force the company to credit the contractor or prevent modification of the work
- **Open-source GPL components** — incorporating GPL-licensed code into a proprietary product can "infect" the product and require open-sourcing under the GPL; requires disclosure and approval
- **No further assurances clause** — contractor may become uncontactable after engagement ends; without this clause, the company has no contractual basis to compel cooperation with IP registration

## Related skills

- [[prompt-pack-nda-unilateral]]
- [[prompt-pack-trade-secret-protection-policy]]
- [[prompt-pack-trademark-license-agreement]]
- [[draft-ip-assignment]]
- [[kb-ip-mena]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
