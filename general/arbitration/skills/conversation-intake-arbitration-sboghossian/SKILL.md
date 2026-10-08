---
name: conversation-intake-arbitration-sboghossian
title: Intake — Arbitration
description: 'Use before drafting any arbitration-related document — a request for arbitration, statement of claim, terms of reference, or procedural application — to gather the six essential inputs: the arbitration clause, parties, dispute facts, relief sought, procedural status, and time-sensitive issues. Covers all major arbitral institutions active in MENA (DIAC, DIFC-LCIA, ICC, LCIA, SIAC). P0 drafting gate for all arbitration matters.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-arbitration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Intake — Arbitration

## When to use this

Use this intake skill before drafting any arbitration document, including:
- Request for arbitration (filing document to initiate proceedings).
- Statement of claim or statement of defence.
- Application for interim relief (emergency arbitrator, injunction).
- Terms of reference.
- Procedural correspondence with a tribunal or institution.

Do not draft any arbitration document until the six required inputs are confirmed. The choice of institution, rules, and seat determines the entire procedure and document format — an ICC Request looks materially different from a DIAC Request.

## The six required inputs

### 1. Arbitration clause

This is the most critical input. Gather:
- **Is there an arbitration clause?** If yes: what does it say? Get the exact text if possible.
- **Institutional or ad hoc?** Institutional rules (ICC, DIAC, DIFC-LCIA) provide a complete procedural framework; ad hoc arbitration (e.g., UNCITRAL Rules) requires more procedural agreement between parties.
- **Which rules?** ICC Rules? DIAC Rules? DIFC-LCIA Rules (note: LCIA took over from DIFC-LCIA in 2021)? SIAC Rules? LCIA Rules? HKIAC Rules? ICDR Rules?
- **Seat of arbitration?** This is the legal home of the arbitration and determines which national courts can assist or review the award. It is not the same as the hearing venue.
- **Language?** The arbitration language determines the language of all submissions and the award.
- **Governing law?** Often different from the seat — the substantive law governing the dispute.

**Common clause validity traps:**
- Clause signed by a party without authority (check corporate authorization).
- Clause in a standard-form agreement that was not specifically brought to the party's attention (may be unenforceable in some civil-law jurisdictions).
- Clause that is pathological (e.g., refers to a non-existent institution or contradictory procedural rules).
- Stepped dispute resolution clause requiring prior negotiation or mediation — confirm those steps were completed before filing.

### 2. Parties

For each party:
- Full legal name and entity type (individual, company, government entity).
- Jurisdiction of incorporation or nationality.
- Registered address and physical address.
- Role (Claimant / Respondent).
- Authorized representative if known.

For international arbitration, confirm whether any party is a state or state-owned entity — this triggers sovereign immunity analysis and may affect enforcement.

### 3. Underlying dispute — facts

Gather a clear, chronological statement of the facts giving rise to the claims:
- What was the agreement between the parties (brief description)?
- What happened that gave rise to the dispute?
- What did the Respondent do (or fail to do) that the Claimant says is a breach?
- What is the approximate date of the breach or last event?

The facts will form the foundation of the Statement of Claim. They must be presented chronologically and kept to the materially relevant events — not every background detail.

### 4. Relief sought

Identify all categories of relief:
- **Monetary damages:** quantum (approximate, in the governing currency); nature (direct loss, consequential loss, lost profit, wasted expenditure).
- **Declaratory relief:** (e.g., "declare that the contract has been validly terminated").
- **Injunctive relief:** if urgent (e.g., "restrain Respondent from disposing of assets pending the award").
- **Specific performance:** (e.g., "order Respondent to complete the construction works").
- **Costs:** claimant will typically request costs; quantify estimated legal fees if known.
- **Interest:** pre-award and post-award interest; the applicable rate depends on the substantive law.

Note the difference between **relief in the Request for Arbitration** (broad framing) and **relief in the Statement of Claim** (fully particularized). The intake is for the Request stage.

### 5. Procedural status

- Has pre-arbitration negotiation been attempted (as required by many stepped clauses)?
- Has mediation been attempted (if the clause requires it)?
- Has a cooling-off period expired (if the clause imposes one)?
- Has any court been approached? Are there parallel proceedings?
- Has any default or demand notice been sent to the Respondent?

Many institutional rules (including ICC Rules Art. 6) require a description of any failed attempts to resolve the dispute before filing.

### 6. Time-sensitive issues

- **Interim relief:** does the Claimant need an emergency arbitrator or urgent injunction? Most major institutions now offer emergency arbitrator procedures (ICC: Emergency Arbitrator Rules; SIAC: Schedule 1; LCIA: Article 9B; DIAC: Article 14.5 of 2022 Rules). Emergency applications must typically be filed simultaneously with or immediately after the Request for Arbitration.
- **Statute of limitations:** calculate whether the claim is time-barred under the applicable substantive law. If limitation is a concern, the Request for Arbitration must be filed before the deadline.
- **Asset preservation:** is there risk that the Respondent will dissipate assets before an award? Consider whether a precautionary attachment (kaza haytia / seizing order in civil-law jurisdictions) should be sought from a national court in parallel with the arbitration filing.

## Institutional guidance — key MENA-relevant institutions

| Institution | Acronym | Seat options | Notes |
|---|---|---|---|
| Dubai International Arbitration Centre | DIAC | Dubai (usually) | Governed by UAE Federal Arbitration Law (Law No. 6 of 2018); DIAC 2022 Rules; strong for UAE-nexus disputes |
| DIFC-LCIA (now LCIA with DIFC seat) | DIFC-LCIA | DIFC, Dubai | After the 2021 restructure, new cases are filed under LCIA Rules with DIFC as the seat; DIFC Courts are the supervisory court |
| International Chamber of Commerce | ICC | Paris (default) or any seat chosen by parties | The international neutral choice; ICC 2021 Rules; higher administrative costs; good for large cross-border disputes |
| London Court of International Arbitration | LCIA | London (default) or any seat | Often chosen for English-law governed contracts; LCIA 2020 Rules |
| Singapore International Arbitration Centre | SIAC | Singapore (default) or any seat | Strong for Asian nexus; excellent emergency arbitrator procedure |
| Saudi Center for Commercial Arbitration | SCCA | Riyadh | Preferred for KSA-nexus disputes; required for some Saudi government contracts |
| Abu Dhabi International Arbitration Centre | ADIAC / arbitrateAD | Abu Dhabi | Abu Dhabi nexus; ADGM Courts as supervisory court for ADGM-seat arbitrations |

## Filing fee calculation

Most institutions calculate filing fees based on the amount in dispute. As a rough guide:
- ICC: €3,000 filing fee + administrative + arbitrator fees; can total 3–5% of the amount in dispute.
- DIAC: AED 10,000 minimum; fee schedule on DIAC website.
- LCIA: £1,750 registration fee + hourly rate for arbitrators.

Filing fees are substantial for small claims — flag this to the client if the dispute amount is under $50,000, as institutional arbitration may be economically disproportionate.

## Critical verification checklist

Before any filing:

- [ ] Arbitration clause is signed by all parties with proper authority.
- [ ] The dispute falls within the scope of the clause ("arises out of or in connection with this agreement").
- [ ] Pre-arbitration steps completed (negotiation, mediation, notice periods).
- [ ] Limitation period is not expired.
- [ ] Emergency relief needs assessed — if yes, simultaneous EM application prepared.
- [ ] Correct institution identified — do not file with ICC if the clause says DIAC.
- [ ] Governing law and seat confirmed.
- [ ] Filing fee calculated and client notified.
- [ ] Counsel admitted or recognized in the seat jurisdiction (some institutions have representation rules).

## Output of this intake

After gathering the six inputs, produce:
1. A structured intake summary for lawyer review.
2. A draft Request for Arbitration tailored to the relevant institutional rules.
3. A procedural timeline estimating key milestones (Terms of Reference, document production, hearing, award).

See [[draft-arbitration-request]] for the document-drafting skill.

## Related skills

- [[conversation-clarifying-questions]]
- [[conversation-disclaimer]]
- [[draft-arbitration-request]]
