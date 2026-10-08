---
name: prompt-pack-request-for-arbitration-sboghossian
title: Request for Arbitration
description: Use when counsel needs to draft a Request for Arbitration (RfA) to be filed with an arbitral institution on behalf of a claimant. Covers factual summary, statement of claims, relief sought, proposed arbitrators, procedural requests, and required institutional attachments. Applicable to ICC, LCIA, DIAC, ADCCAC/ADIAC, CRCICA, SCCA, SIAC, ICSID, and UNCITRAL ad hoc proceedings, with MENA-specific guidance on seat selection and mandatory content under UAE, KSA, and DIFC/ADGM arbitration laws.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-request-for-arbitration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Request for Arbitration

## When to use this

Use this skill when a claimant (or its counsel) needs to prepare and file a formal Request for Arbitration with an arbitral institution or commence an ad hoc arbitration. This document is the procedural trigger that:
- Starts the arbitration clock (and in many institutions, sets the limitation-period cut-off).
- Establishes the institution's jurisdiction.
- Puts the respondent on notice of the claims.
- Sets out the relief sought so the tribunal's eventual mandate is defined.

**Timing note:** A Request for Arbitration is not a full Statement of Claim — it is the initiating document. Most institutional rules permit or require a fuller Statement of Claim/Memorial to be filed later. Ensure the RfA is comprehensive enough to establish jurisdiction but understand that claims can typically be developed in subsequent submissions.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Arbitral institution** | Each institution has specific mandatory form requirements and filing fees | Ask; do not assume |
| **Applicable institutional rules and version** | ICC 2021 Rules, LCIA Rules 2020, DIAC Rules 2022, SCCA Rules 2023 each differ | Ask; state "latest version" if uncertain and flag for verification |
| **Claimant name, address, and legal representative** | Required fields in all institutional RfA forms | Ask |
| **Respondent name and address** | Required fields | Ask |
| **Description of the contract and the dispute** | Establishes the factual foundation and the arbitration clause invoked | Ask: "Provide the contract, the relevant arbitration clause, and a brief description of the dispute" |
| **Claims and relief sought** | Defines the tribunal's mandate; must include a figure for the principal monetary claim | Ask: "What amounts are claimed? What other relief is sought (e.g., declaration, specific performance)?" |
| **Seat of arbitration and governing law** | Determines lex arbitri and choice of substantive law | Ask; these should be specified in the arbitration clause |

## Optional inputs

- **Proposed number and method of appointment of arbitrators** — if the arbitration agreement specifies (sole arbitrator vs. panel of three), reproduce; otherwise the default under the chosen rules applies.
- **Nomination of arbitrator (if sole arbitrator or tribunal appointment)** — some institutions (LCIA, UNCITRAL) allow claimant to nominate its co-arbitrator in the RfA.
- **Request for interim/emergency relief** — if urgent measures are needed before the tribunal is constituted, flag the emergency arbitrator procedure at this stage.
- **Confidentiality request** — some institutions require the parties to invoke confidentiality in the RfA to activate a default confidentiality regime.
- **Language of proceedings** — state here to avoid disputes later.

## Document structure

1. **Cover / transmission letter** — addressed to the institution's secretariat; brief statement that the attached RfA is being filed pursuant to [Institution] Rules Art. [X]; includes filing fee confirmation.

2. **Request for Arbitration body**

   ### (a) Parties
   - Claimant: full legal name, registered address, jurisdiction of incorporation, legal representative (counsel) with address and contact.
   - Respondent: same fields (to the extent known).

   ### (b) Arbitration agreement
   - Reproduce the arbitration clause verbatim from the contract (or attach the full contract and reference the clause).
   - If the arbitration agreement is in a separate standalone arbitration agreement, attach that document.
   - State: the clause provides for arbitration under [Institution] Rules with seat in [City/Jurisdiction].

   ### (c) Contract and dispute description
   - Summary of the underlying contract: type, date, parties, key commercial terms relevant to the dispute (not full recitation — leave detail for the Statement of Claim).
   - Summary of the dispute: what happened, when, what contractual obligation was breached, and any pre-dispute correspondence or attempts to resolve.
   - Note: keep factual narrative concise at RfA stage; the goal is to establish jurisdiction and put respondent on notice, not to make closing arguments.

   ### (d) Relief sought
   - Principal monetary claims (state amount and currency; if contested, state "not less than [X]").
   - Interest (specify rate and accrual date if contractually stipulated; otherwise "interest as the tribunal may determine").
   - Declaratory relief (if sought).
   - Costs of the arbitration.
   - Any other specific relief (e.g., delivery of goods, rectification of accounts).

   ### (e) Procedural requests
   - Number of arbitrators: [sole arbitrator / three arbitrators] per the arbitration agreement or institution default.
   - Nomination of claimant's co-arbitrator (if three-member tribunal): provide full name, CV, and confirmation of availability/independence (check institution rules on timing).
   - Language of the proceedings.
   - Seat of arbitration (if not fixed in the clause).
   - Emergency arbitrator request: if urgent relief is needed, state here and file separately under emergency rules.

   ### (f) Attachments
   - Exhibit A: underlying contract (or relevant extracts)
   - Exhibit B: pre-dispute correspondence (demand letters, etc.)
   - Exhibit C: proposed arbitrator's CV (if nominating)
   - Filing fee payment confirmation

3. **Certificate of service** — some institutions require proof that the RfA has been sent to the respondent simultaneously.

## Jurisdictional notes

### DIAC (Dubai International Arbitration Centre) — Rules 2022
- RfA must include: parties, arbitration agreement, summary of dispute, relief, and filing fee.
- Three-arbitrator default for disputes above AED 5 million (approximately USD 1.36 million).
- Seat default: Dubai (if not specified in the clause).
- Filing fee: non-refundable registration fee payable on filing.

### ADIAC / ADCCAC (Abu Dhabi)
- Similar structure to DIAC; seat default: Abu Dhabi.
- Arabic translation of the RfA and key exhibits may be required if any party requests or if the seat requires it.

### SCCA (Saudi Center for Commercial Arbitration) — Rules 2023
- RfA must be in Arabic (or bilingual) when any party is Saudi or the seat is in KSA.
- Default number of arbitrators: one (unless parties agree three).
- Seat: Riyadh or another Saudi city unless parties have agreed otherwise.
- SCCA has an advance filing fee schedule based on claim value.

### CRCICA (Cairo Regional Centre for International Commercial Arbitration)
- UNCITRAL Model Rules-based; RfA follows the UNCITRAL Notice of Arbitration format.
- Arabic or English; French optional.
- Fee schedule on CRCICA website.

### ICC (International Chamber of Commerce) — Rules 2021
- Art. 4: RfA must include: parties, arbitration clause, contract description, relief, number/method of appointment of arbitrators, nominations (if applicable), seat/language/applicable law if not in the clause.
- Filing fee: USD 5,000 non-refundable registration.
- Terms of Reference (ICC Art. 23) will be established after constitution of the tribunal.

### LCIA — Rules 2020
- Art. 1: detailed RfA requirements including proposed method of appointment, nominee(s).
- Claimant nominates its arbitrator in the RfA for three-member tribunal; LCIA Court appoints the third.

### DIFC-LCIA (now DIAC under restructured arrangements post-2021)
- As of 2021, DIFC-LCIA cases are administered by DIAC; check the applicable rules version for legacy cases.

## Drafting standards

- **Limitation periods:** The date of filing the RfA (or the date of receipt by the institution) typically interrupts the limitation period. Confirm this with the applicable law of the arbitration agreement and the law of the seat. Filing urgency is therefore critical.
- **State claims precisely but not exhaustively.** The RfA defines the envelope of the tribunal's jurisdiction; claims asserted later that are outside the scope of the RfA may be inadmissible. However, excessive detail at this stage is unnecessary — save it for the Statement of Claim.
- **Attach the arbitration agreement.** Never rely on a summary; reproduce it verbatim and attach the full document. Jurisdictional challenges often turn on the exact wording.
- **Currency and interest.** Always specify the currency of each claim. For MENA practice, check whether the applicable law permits interest and at what rate — UAE onshore courts apply statutory interest; DIFC/ADGM courts apply commercial rates; KSA practice avoids conventional interest (mark-up structures are used instead in Sharia-compliant proceedings).

## Common mistakes

- **Failing to nominate a co-arbitrator in the RfA when required.** Under LCIA and some other rules, the claimant's right to nominate its co-arbitrator in the RfA is a one-time right; missing the window results in the institution appointing without input.
- **Not attaching the arbitration clause.** Institutions can refuse to register a case if the arbitration agreement is not supplied; a disputed or informal reference is insufficient.
- **Understating the claim amount.** The initial claim amount affects filing fees, default tribunal size, and potentially the institution's case management allocation. If the precise amount is uncertain, state "not less than [X]" and reserve the right to update.
- **Omitting interest.** Failing to include interest in the RfA risks the tribunal declining to award it later on jurisdictional grounds.
- **Seat not specified.** If the arbitration clause is silent on seat and the RfA does not specify one, the institution will decide — often at higher cost and with less predictability.

## Related skills

- [[prompt-pack-procedural-order-draft]]
- [[prompt-pack-statement-of-claim]]
- [[prompt-pack-statement-of-defense-arbitration]]
- [[prompt-pack-settlement-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
