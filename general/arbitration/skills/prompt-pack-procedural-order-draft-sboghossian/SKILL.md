---
name: prompt-pack-procedural-order-draft-sboghossian
title: Procedural Order Draft
description: Use when counsel or a tribunal secretary needs to draft Procedural Order No. 1 (or subsequent orders) for an arbitration. Covers timetable, document production, witness statements, expert reports, hearing logistics, and confidentiality. Applicable to institutional arbitrations under ICC, LCIA, DIAC, ADCCAC, CRCICA, SIAC, and UNCITRAL rules, with MENA seat considerations for UAE, DIFC, ADGM, Saudi Arabia, Lebanon, and Egypt.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-procedural-order-draft
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Procedural Order Draft

## When to use this

Use this skill when:
- An arbitral tribunal or the parties to an arbitration need a comprehensive Procedural Order No. 1 setting out the entire procedural framework for the case.
- A party representative (claimant's or respondent's counsel) wants to circulate a draft order to the tribunal for adoption or adaptation.
- A subsequent procedural order is needed (e.g., Procedural Order No. 2 on document production, Procedural Order No. 3 on expert evidence).
- Counsel needs to propose specific procedural rules at the first case-management conference (CMC).

This skill is procedural, not substantive — it concerns *how* the arbitration runs, not the merits. For the underlying substantive pleadings, use [[prompt-pack-statement-of-claim]] or [[prompt-pack-statement-of-defense-arbitration]].

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Arbitration case reference** | Identifies the case in the order's header | "[Case Ref TBD]" |
| **Arbitral institution and applicable rules** | Determines mandatory procedural requirements and deadlines | Ask; note that ICC, LCIA, DIAC, UNCITRAL each have different frameworks |
| **Seat of arbitration** | Determines the lex arbitri (curial law) governing procedural challenges | Ask; key seats: Dubai (UAE Arbitration Law, Federal Law No. 6 of 2018), DIFC, ADGM, Riyadh, Beirut, Paris, London |
| **Number of arbitrators and their identities** | Affects how the order is signed and how deliberations are referenced | Tribunal of [1/3] yet to be constituted vs. constituted |
| **Agreed procedural positions (if any)** | Reduces contested content; records what parties have agreed | None — draft as if no prior agreement unless instructed |

## Optional inputs

- **Agreed or proposed timetable dates** — counsel often exchange a draft Gantt chart; incorporate if provided.
- **Document production method preference** — Redfern schedule vs. IBA Rules on Evidence model; UNCITRAL Model vs. civil-law documentary approach.
- **Language of proceedings** — especially important in MENA where Arabic-language proceedings are sometimes required.
- **Seat-specific mandatory rules** — e.g., under UAE Federal Law No. 6 of 2018, certain rights cannot be waived by procedural order.
- **Confidentiality concerns** — whether to include a strict confidentiality provision or adopt the institution's default.

## Document structure

1. **Preamble** — case reference, names of parties, institution, applicable rules, date of constitution of the tribunal, date and form of CMC.
2. **Procedural timetable** — table or numbered list of milestones:
   - Statement of Claim / Memorial deadline
   - Statement of Defense / Counter-Memorial deadline
   - Reply Memorial (if permitted)
   - Rejoinder (if permitted)
   - Document production round(s)
   - Witness statement exchange
   - Expert report exchange
   - Pre-hearing conference
   - Final hearing dates
3. **Document production** — whether IBA Rules on Evidence apply; Redfern schedule process; relevance and materiality standards; form of production (native, PDF); privilege rules (which law governs privilege — lex arbitri vs. law of the document).
4. **Witness evidence**
   - Written witness statements in lieu of direct examination (standard in international arbitration)
   - Witness statement deadline, format, language
   - Right to call witnesses; notification procedure
   - Treatment of witness conferencing ("hot-tubbing") if adopted
5. **Expert evidence**
   - Party-appointed vs. tribunal-appointed experts
   - Expert report format and deadline
   - Joint memorandum of experts (identifying agreed/disagreed issues)
   - Tribunal-appointed expert: procedure, terms of reference
6. **Hearing logistics**
   - Dates, venue or virtual platform
   - Sequence of presentations
   - Time allocation (chess-clock or equal-time model)
   - Interpretation requirements (Arabic/English/French)
   - Transcription and real-time transcript services
7. **Confidentiality**
   - Scope: pleadings, awards, and evidence all confidential
   - Exceptions: enforcement proceedings, disclosure required by law, professional regulatory obligations
   - Specific restrictions on disclosure to related entities
8. **Communications with the tribunal**
   - All communications through the institution's case management system or designated channel
   - Ex parte communications prohibition
   - Emergency/urgent applications procedure
9. **Miscellaneous**
   - Costs reserved
   - Modification of procedural order
   - Applicable law on substance (noted for reference, not decided here)
10. **Signatures** — tribunal member(s) and date; parties' acknowledgment if the order is agreed.

## Jurisdictional notes

### UAE — onshore (Federal Law No. 6 of 2018 on Arbitration)
- Modeled on the UNCITRAL Model Law; arbitration-friendly.
- Seat in Dubai or Abu Dhabi (onshore): parties may agree to exclude or modify many procedural provisions except those touching public policy.
- DIAC Rules (2022) provide detailed CMC procedures; Procedural Order No. 1 is expected within 30 days of constitution.
- Arabic-language requirement for enforcement proceedings in UAE courts means it is prudent to produce Arabic translations of the final award; not necessarily for interim procedural orders.

### DIFC Arbitration Centre (DIAC International)
- DIFC Arbitration Law (DIFC Law No. 1 of 2008, as amended) applies when the seat is DIFC.
- Procedural orders cannot be enforced against third parties in DIFC courts without a separate court order.
- Tribunal has broad discretion on procedure; parties commonly adopt IBA Rules on Evidence.

### ADGM Arbitration Centre
- ADGM Arbitration Regulations 2015 (UNCITRAL Model Law-based).
- Common-law procedural culture: witness cross-examination expected; witness statements standard.

### KSA — Saudi Center for Commercial Arbitration (SCCA)
- Saudi Arbitration Law (Royal Decree M/34 of 2012) and SCCA Rules 2023.
- Arabic is the default language of proceedings unless parties agree otherwise.
- Procedural orders must comply with Islamic law (Sharia) principles — e.g., interest (riba) provisions cannot be included in substantive orders but procedural orders are generally unaffected.
- Tribunal powers to order document production are somewhat narrower than in common-law seats.

### Egypt — Cairo Regional Centre for International Commercial Arbitration (CRCICA)
- Egyptian Arbitration Law No. 27 of 1994 (UNCITRAL Model Law-based).
- CRCICA Rules 2011 (as amended).
- Courts have occasionally intervened in procedural matters; ensure order language is precise to avoid grounds for challenge.

### Lebanon — Lebanese Arbitration Centre / Ad hoc
- Lebanon's Code of Civil Procedure (Arts. 762–814) governs domestic arbitration; New York Convention applies to international.
- Political instability has affected institutional capacity; ad hoc arbitration with Paris seat is common for Lebanese parties.

### France (Paris) — ICC / ICDR
- OHADA reference for West African parties often uses Paris seat.
- French lex arbitri (Code of Civil Procedure Arts. 1442–1527) is highly arbitration-friendly; courts intervene minimally.

## Drafting standards

- Use numbered paragraphs throughout for ease of reference and amendment.
- Express all deadlines as specific calendar dates (not "within X days of Y") to avoid disputes about counting.
- Distinguish between "shall" (mandatory) and "may" (discretionary) consistently.
- Attach a procedural timetable as an annex in table form — easier to revise at subsequent CMCs.
- Avoid prejudging substantive legal issues (applicable law, validity of clause, jurisdiction) in the procedural order; include a carve-out: "Nothing in this Order prejudges any issue of jurisdiction, merits, or liability."
- Include a version/amendment history at the bottom so superseded orders are traceable.

## Common mistakes

- **Importing US-style discovery rules** into a civil-law or MENA seat proceeding. Document production in MENA arbitration is narrower than US discovery; do not replicate "all documents relating to" formulations.
- **Omitting language of proceedings.** In MENA, the language issue (Arabic vs. English vs. French) is often contested; fixing it in Procedural Order No. 1 avoids later disputes.
- **Vague confidentiality clauses.** "The proceedings are confidential" without specifying scope creates disputes; enumerate what is covered.
- **Failing to address third-party funding disclosure.** ICC, LCIA, and DIAC rules increasingly require disclosure of TPF; the procedural order should set a deadline.
- **No mechanism for urgent applications.** Without an emergency procedure, parties may rush to national courts; include a 48-hour notice provision for urgent relief requests to the tribunal.

## Related skills

- [[prompt-pack-request-for-arbitration]]
- [[prompt-pack-statement-of-claim]]
- [[prompt-pack-statement-of-defense-arbitration]]
- [[prompt-pack-settlement-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
