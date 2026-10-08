---
name: draft-boilerplate-clauses-sboghossian
title: Boilerplate Clauses Library
description: Use when drafting or reviewing the standard end-of-contract "miscellaneous" or "general provisions" section, or when a specific boilerplate clause needs to be pulled, adapted, or reviewed. Contains market-standard language for entire agreement, no waiver, severability, notices, governing law, dispute resolution (DIAC, ICC, court-of-choice), force majeure, counterparts/e-signature, assignment, and construction clauses — all with MENA-specific variants and enforceability notes.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-boilerplate-clauses
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Boilerplate Clauses Library

## When to use this

Use this skill to:
- Draft the standard "miscellaneous" or "general provisions" section of any commercial contract.
- Pull a specific boilerplate clause when the user requests one by name.
- Review a boilerplate section and flag problematic, missing, or poorly drafted clauses.
- Adapt clauses for MENA jurisdictions where US/UK defaults create enforceability problems.

## Clause 1 — Entire Agreement (Integration clause)

**Purpose**: prevents claims that oral representations, prior negotiations, or other documents form part of the contract.

**Standard text**:
> *This Agreement constitutes the entire agreement between the Parties with respect to its subject matter and supersedes all prior agreements, understandings, representations, and warranties, whether oral or written, relating to the same subject matter.*

**MENA notes**:
- Enforceable in DIFC, ADGM, UK (subject to misrepresentation claims).
- UAE onshore: civil-law courts may look at pre-contractual conduct and good-faith dealings even with this clause; it reduces but does not eliminate the risk.
- KSA: Sharia principles of good faith may allow a court to consider surrounding circumstances.
- LB: Article 366 Code of Obligations and Contracts allows interpretation based on common intent; this clause helps but is not absolute.

## Clause 2 — No Waiver

**Purpose**: ensures that not enforcing a right in one instance does not permanently extinguish it.

**Standard text**:
> *No failure or delay by a Party in exercising any right, power, or remedy under this Agreement shall operate as a waiver of that right, power, or remedy. A waiver in any particular instance does not operate as a continuing waiver or a waiver of any other right, power, or remedy. A waiver is only effective if given in writing signed by the waiving Party.*

**MENA notes**: Enforceable across MENA; the writing requirement for waiver is important and should be included.

## Clause 3 — Severability

**Purpose**: preserves the contract if one clause is void or unenforceable.

**Standard text**:
> *If any provision of this Agreement is found by a court or arbitral tribunal of competent jurisdiction to be invalid, illegal, or unenforceable in any respect, that provision shall be modified to the minimum extent necessary to make it valid, legal, and enforceable. If such modification is not possible, the provision shall be severed from this Agreement. The validity, legality, and enforceability of the remaining provisions shall not in any way be affected or impaired.*

**MENA notes**:
- KSA courts have inherent power to modify Sharia-incompatible clauses (e.g., interest provisions) rather than void the whole contract. The severability clause supports this outcome.
- UAE Civil Code Article 27: void clause does not automatically void the whole contract if the clause can be severed.

## Clause 4 — Notices

**Purpose**: establishes a defined mechanism and deemed-receipt rules for contractual notices.

**Standard text (multi-channel)**:
> *Any notice or communication under this Agreement shall be in writing and shall be delivered by: (a) email with read receipt or delivery confirmation to the address set out in Schedule [X]; (b) registered post or courier to the address set out in Schedule [X]. Notices shall be deemed received: (i) for email, on confirmation of delivery or at 9:00 am on the next Business Day in the recipient's jurisdiction if delivered outside business hours; (ii) for registered post, two (2) Business Days after dispatch; (iii) for courier, on signature of receipt. Either Party may change its notice address by written notice to the other.*

**MENA notes**:
- LB: e-signature and electronic notices recognized under Law 81/2018; specify the email address precisely.
- KSA: WhatsApp and SMS are widely used commercially but are NOT reliable notice mechanisms in a contract; stick to email.
- UAE: electronic notices to company email accepted; for formal legal process, consider adding the UAE postal address.
- For notices triggering limitation periods or dispute resolution clauses: require email plus confirmed-delivery method.

## Clause 5 — Governing Law

**Standard text**:
> *This Agreement is governed by and construed in accordance with the laws of [jurisdiction], without regard to its conflict of laws rules.*

**Jurisdiction options and notes**:

| Governing law | When to choose |
|---|---|
| **UAE Federal Law** | Onshore UAE contracts; UAE-resident parties; real estate; employment |
| **DIFC Law** | DIFC-registered entities; cross-border commercial contracts where English common-law principles preferred; finance |
| **ADGM Law** | ADGM-registered entities; similar to DIFC but Abu Dhabi seat |
| **English Law** | Cross-border finance, international M&A, shipping; widely accepted as neutral |
| **KSA Law** | KSA-party contracts; government contracts; real estate in KSA |
| **Lebanese Law** | LB-party contracts; real estate in LB; construction in LB |
| **French Law** | Cross-border contracts with French parties; historically popular in LB |

**Critical**: See [[heuristic-governing-law-must-match-forum]]. The governing law and the dispute resolution forum must be consistent. Choosing English law + DIFC courts works well. Choosing English law + KSA courts creates a mismatch that KSA courts will resolve by applying KSA law anyway.

## Clause 6 — Dispute Resolution: Arbitration

### DIAC (Dubai International Arbitration Centre) — recommended for UAE/MENA disputes
> *Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity, or termination, shall be finally settled by arbitration administered by the Dubai International Arbitration Centre (DIAC) in accordance with the DIAC Arbitration Rules in force at the time of filing. The seat of arbitration shall be Dubai (DIFC). The arbitral tribunal shall consist of [one / three] arbitrator(s). The language of the arbitration shall be [English / Arabic / English and Arabic].*

### ICC
> *Any dispute arising out of or in connection with this Agreement shall be finally settled under the Rules of Arbitration of the International Chamber of Commerce by [one / three] arbitrator(s) appointed in accordance with the said Rules. The seat of arbitration shall be [Dubai / Abu Dhabi / London / Paris]. The language shall be [English / French].*

### LCIA
> *Any dispute arising out of or in connection with this Agreement shall be finally resolved by arbitration under the LCIA Arbitration Rules 2020. The seat of arbitration shall be [London / Dubai (DIFC)]. The number of arbitrators shall be [one / three]. The language of the arbitration shall be English.*

### DIFC Courts (not arbitration — litigation)
> *The DIFC Courts shall have exclusive jurisdiction over any dispute arising out of or in connection with this Agreement.*

### Lebanese courts
> *The courts of Beirut (Commercial Court) shall have exclusive jurisdiction over any dispute arising out of or in connection with this Agreement. Lebanese law shall govern.*

### KSA — note on arbitration
KSA arbitration is possible and enforceable under the Saudi Arbitration Law (Royal Decree M/34 2012). For KSA-seated arbitrations, the Saudi Center for Commercial Arbitration (SCCA) is the leading institution. Note that KSA courts retain supervisory jurisdiction and may set aside an award on Sharia-incompatibility grounds.

## Clause 7 — Force Majeure

**Standard text**:
> *Neither Party shall be in breach of this Agreement or liable for any delay in performing, or failure to perform, any of its obligations under this Agreement to the extent that such delay or failure results from an event of Force Majeure. For this purpose, "Force Majeure" means any event beyond a Party's reasonable control including, without limitation: acts of God, war, armed conflict, terrorism, riot, civil commotion, governmental action or restriction, pandemics, epidemics or quarantine, natural disaster, fire, flood, or labour disruption. A Party claiming Force Majeure must: (a) promptly notify the other Party in writing upon becoming aware of the Force Majeure event; (b) use commercially reasonable efforts to mitigate the effect of the Force Majeure event; and (c) resume performance as soon as reasonably practicable. If a Force Majeure event continues for more than [90] days, either Party may terminate this Agreement on [30] days' written notice.*

**MENA notes**:
- UAE Civil Code Articles 273-274: force majeure (القوة القاهرة) and supervening impossibility: recognized and codified.
- KSA: Sharia recognizes "qahira" (force majeure) defense; courts are generally willing to apply it during certified emergency periods.
- LB: Code of Obligations and Contracts Articles 340–343: force majeure recognized; "imprévision" (changed circumstances) doctrine also available in LB.

## Clause 8 — Counterparts and Electronic Signatures

**Standard text**:
> *This Agreement may be executed in one or more counterparts, each of which shall constitute an original, and all of which, taken together, shall constitute one and the same agreement. Delivery of an executed counterpart by email (PDF) or electronic signature platform shall be as effective as delivery of a manually signed original. Electronic signatures (including those generated by DocuSign, Adobe Sign, or equivalent platforms) shall be deemed equivalent to original wet-ink signatures to the extent permitted by applicable law.*

**MENA e-signature notes**:
- **UAE**: Electronic Transactions Law (Federal Decree-Law 46/2021) recognizes electronic signatures; DocuSign and qualified electronic signatures accepted for most commercial contracts; some transactions (real estate transfers, court filings) still require notarized wet ink.
- **LB**: Law 81/2018 on Electronic Transactions recognizes e-signatures; Tawqi3i is the Lebanese e-notarization platform for contracts requiring notarization. See [[inst-tawqi3i-esignature-bridge]].
- **KSA**: Electronic Transactions Law (Royal Decree M/18 2007) recognizes e-signatures; Nafath national digital identity is the authentication platform; for notarized contracts use Mawthq.
- **DIFC / ADGM**: Electronic Transactions Law (DIFC Law 2 of 2017); DocuSign and qualified electronic signatures fully accepted.

## Clause 9 — Assignment

**Standard text (mutual restriction)**:
> *Neither Party may assign, transfer, or delegate any of its rights or obligations under this Agreement without the prior written consent of the other Party, which consent shall not be unreasonably withheld, conditioned, or delayed. Notwithstanding the foregoing, either Party may assign this Agreement without consent to: (a) an Affiliate; or (b) the acquirer of all or substantially all of its business or assets, provided that the assignee assumes all obligations under this Agreement. Any purported assignment in violation of this clause shall be void.*

**Variants**:
- Buyer-favorable (one-way permission): "The Company may assign this Agreement to an Affiliate or acquirer without consent. [Counterparty] may not assign without the Company's prior written consent."
- Anti-assignment hard lock: "Neither Party may assign this Agreement in any circumstances without the prior written consent of the other."

## Clause 10 — Headings and Construction

**Standard text**:
> *Headings in this Agreement are for convenience only and do not affect its interpretation. In this Agreement, unless the context otherwise requires: (a) references to the singular include the plural and vice versa; (b) "include" and "including" are not exhaustive; (c) references to "writing" include email; (d) references to a "person" include individuals, corporations, partnerships, and unincorporated associations; (e) references to a statute or regulation include any amendment or re-enactment.*

## Sharia-compatibility note (KSA and applicable onshore UAE/MENA)

For contracts subject to KSA law or reviewed by Sharia-applying courts:
- Avoid the word "interest" (faida/riba) in penalty and default payment provisions; use "compensation for delay" or "pre-agreed liquidated compensation tied to actual loss."
- Penalty clauses (شرط الجزاء) are enforceable if framed as a pre-estimate of genuine loss; courts may reduce if punitive. See [[heuristic-shariah-compliance-check-when-relevant]].
- Certainty (gharar): avoid excessive uncertainty in price or delivery terms.

## Related skills

- [[draft-contract-skeleton-builder]]
- [[draft-bilingual-ar-en-side-by-side]]
- [[heuristic-governing-law-must-match-forum]]
- [[heuristic-shariah-compliance-check-when-relevant]]
- [[inst-tawqi3i-esignature-bridge]]
