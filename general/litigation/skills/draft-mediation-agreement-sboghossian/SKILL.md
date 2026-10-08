---
name: draft-mediation-agreement-sboghossian
title: Mediation Agreement / Settlement Agreement
description: Use when drafting either a mediation agreement (submitting a dispute to mediation) or a settlement agreement (documenting terms reached after mediation or negotiation). Covers MENA and international institutional frameworks (DIAC, DIFC, ADGM, JAMS, CEDR, ICC ADR), confidentiality, without-prejudice protection, cost allocation, and the Singapore Convention on cross-border settlement enforcement. Triggers on "mediation agreement", "settlement agreement", "adr", "mediate", or "settle dispute" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-mediation-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Mediation Agreement / Settlement Agreement

## When to use this

This skill covers two related but distinct documents:

1. **Mediation Agreement** — signed before mediation begins; submits the dispute to a mediator; establishes the procedural framework (institution, rules, confidentiality, costs, timeline)

2. **Settlement Agreement** — signed after mediation (or direct negotiation) succeeds; documents the agreed settlement terms; is a binding contract replacing or supplementing the original dispute

Both documents are commonly used together: the mediation agreement governs the process; the settlement agreement records the outcome.

## Part I — Mediation Agreement

### When to draft this

Draft a mediation agreement when:
- Two parties wish to attempt mediated resolution before or instead of litigation/arbitration
- A contract requires mediation as a pre-condition to arbitration or litigation
- A court has ordered or recommended mediation

### Required inputs

| Input | Why it matters |
|-------|---------------|
| Parties | Full identification of all disputing parties |
| Dispute description | Brief neutral description of the dispute subject |
| Mediator identity or institution | Named mediator or institutional rules to govern selection |
| Confidentiality scope | What is covered; whether even the existence of the mediation is confidential |
| Timeline | Maximum duration of the mediation process |
| Cost allocation | How mediator fees and party costs are shared |
| Governing law | Applicable to the mediation agreement itself |

### Structure of the mediation agreement

1. **Recitals** — Identify the parties and the dispute (brief description without prejudicing positions); state the mutual desire to attempt mediation before other proceedings

2. **Mediator selection and appointment**
   - Named individual mediator: name, credentials, contact
   - Institutional process: which institution's rules govern appointment (DIAC, DIFC Centre for Amicable Dispute Resolution, ADGM IDRC, JAMS, CEDR, ICC ADR, Singapore Mediation Centre)
   - Backup: if named mediator is unavailable or unacceptable, fallback appointment mechanism

3. **Rules governing the mediation**
   - Institutional rules (by reference) or agreed bespoke rules
   - Language of mediation
   - Seat / location of mediation sessions (or virtual)
   - Each party's right to be represented by counsel

4. **Confidentiality**
   - **Absolute confidentiality**: everything said, disclosed, produced, or communicated in the mediation is confidential; no party may introduce mediation communications as evidence in any subsequent proceeding
   - Scope: covers the mediator, parties, counsel, any experts or observers
   - Exceptions: a) court order requiring disclosure; b) with all parties' written consent
   - Consider: whether even the existence of the mediation and its outcome (if settlement not reached) are confidential

5. **Without-prejudice nature**
   - All statements, proposals, and offers made during mediation are without prejudice to the parties' legal rights and positions
   - Not admissible in any court or arbitral proceeding

6. **Timeline**
   - Mediation to commence within X days of signing
   - Sessions: typically 1-3 days; right to extend by agreement
   - If no settlement within X weeks, mediation concluded (parties free to proceed to arbitration/litigation)

7. **Costs**
   - Mediator's fees: split equally (most common) or otherwise
   - Institutional administration fees: split equally
   - Each party bears its own legal costs
   - Deposit and payment mechanics

8. **No binding settlement unless in writing**
   - Mediation produces no binding obligation unless and until the parties sign a written settlement agreement
   - Mediator's proposals are non-binding suggestions, not arbitral awards

9. **Carve-out for protective measures**
   - Either party may seek interim or emergency relief from a court or arbitral tribunal without prejudicing the mediation
   - Such proceedings do not constitute a breach of the mediation agreement

10. **Governing law and jurisdiction**
    - Law applicable to the mediation agreement itself
    - Jurisdiction for any disputes about the mediation agreement (not the underlying dispute)

### Institutional frameworks in MENA

| Institution | Notes |
|---|---|
| **DIAC (Dubai International Arbitration Centre)** | Has mediation rules since 2022; can appoint mediators; also handles hybrid med-arb |
| **DIFC Centre for Amicable Dispute Resolution** | Operates within DIFC Courts structure; can convert settlement agreement into court order |
| **ADGM IDRC (International Dispute Resolution Centre)** | Mediation services; connected to ADGM Courts |
| **SCCA (Saudi Center for Commercial Arbitration)** | Provides mediation services; KSA parties often prefer local institution |
| **JAMS** | US-focused but operates internationally; widely used for cross-border disputes with US parties |
| **CEDR (Centre for Effective Dispute Resolution)** | UK-headquartered; widely respected internationally; sophisticated mediator panel |
| **ICC ADR** | International Chamber of Commerce ADR rules; global reach; preferred for complex international disputes |

---

## Part II — Settlement Agreement

### When to draft this

Draft a settlement agreement when the parties have reached agreement — whether through mediation, direct negotiation, or during litigation — and wish to document, formalize, and make enforceable their agreed resolution.

### Required inputs

| Input | Why it matters |
|-------|---------------|
| Parties | Full legal identification of all parties |
| Background and dispute | Neutral description; brief recitals of the dispute context |
| Settlement terms | Specific obligations — payment, conduct, asset transfer, etc. |
| Release scope | Who releases whom; what is released; what is excluded |
| Confidentiality requirements | Ongoing confidentiality obligations |
| Tax allocation | Who bears any tax consequences of the settlement |
| Governing law and enforcement mechanism | How is the settlement enforced if a party defaults |

### Structure of the settlement agreement

1. **Recitals**
   - Background: the parties, their commercial relationship, the genesis of the dispute
   - Dispute summary: what the dispute is about (without admitting fault)
   - Mutual desire to resolve: the parties wish to settle "to avoid the uncertainty and expense of further proceedings"

2. **Payment terms and non-monetary obligations**
   - Monetary settlement: amount, currency, payment schedule, account details
   - Non-monetary: transfer of assets, provision of services, referral of business, correction of records, public statement
   - Mechanics: exact payment dates; what triggers each obligation
   - Late payment: interest on late payments; right to re-open dispute if payment default persists beyond X days

3. **Release and discharge**
   - **Full and final mutual release**: each party releases the other from all claims, known and unknown, arising from the dispute description
   - Be precise about scope: is it limited to the specific dispute? Does it extend to all claims between the parties up to the date of the agreement?
   - Unknown claims release: in most jurisdictions, a general release covers unknown claims — state this expressly; California requires specific language for unknown claims (Civil Code § 1542 waiver)
   - **Carve-outs**: obligations under the settlement agreement itself are not released; obligations under surviving contracts not in dispute are not released
   - **Limitations on release in KSA**: Sharia-based settlements (sulh) are recognized; but releases purporting to waive Sharia rights may be challenged — verify with local counsel

4. **Confidentiality**
   - Both parties agree to keep the existence and terms of the settlement confidential
   - Exceptions: required disclosure to tax authorities, auditors, legal counsel, courts; disclosure required by law or regulation
   - Non-disparagement: neither party makes disparaging public statements about the other in connection with the settled dispute

5. **Dismissal of proceedings**
   - If litigation or arbitration is pending: parties agree to file for dismissal with prejudice (or equivalent) within X days of receiving the settlement payment
   - If DIFC Courts: consent order; if arbitration: consent award or withdrawal notice

6. **Tax allocation**
   - Specify how the settlement payment is to be treated for tax purposes (particularly relevant if the payment has an income, VAT, or withholding tax dimension)
   - Parties acknowledge they have obtained their own tax advice
   - Gross-up clause: if withholding tax is applicable, does the paying party gross up?

7. **Breach and remedies**
   - If either party fails to comply with settlement terms: the other party may re-open the underlying dispute and use the settlement agreement as evidence of the other's default
   - Alternatively: specific penalty for non-compliance (pre-agreed amount); applicable in civil-law jurisdictions

8. **Confidentiality of underlying proceedings** (if applicable)
   - If mediation was used, reference back to the mediation agreement's confidentiality provisions
   - Confirm that no mediation communications are admissible in any future proceedings

9. **Governing law and enforcement**
   - Law applicable to the settlement agreement
   - Forum for disputes about the settlement agreement

10. **Singapore Convention on International Settlement Agreements (2019)**
    The United Nations Convention on International Settlement Agreements Resulting from Mediation (Singapore Convention) allows cross-border enforcement of settlement agreements reached through mediation — analogous to how the New York Convention works for arbitral awards.
    - Applies where parties are from different contracting states
    - Signatory MENA states as of 2025: Saudi Arabia (signatory but check ratification status), UAE (signatory but check ratification status); LB not a signatory
    - To qualify: the agreement must have been reached through mediation; must state this expressly; mediator must have signed or institution must be identified
    - Include: express reference to mediation process; statement that it resulted from mediation; mediator's acknowledgment (or institutional certificate) if Singapore Convention enforcement is desired

## Common mistakes

- Not stating "without prejudice" expressly in the mediation agreement — mediation communications may be disclosed in subsequent proceedings
- Settling individual claims but not the underlying contract relationship (parties resume dealing and re-create the same dispute)
- Inadequate definition of release scope — one party discovers an unknown claim later and argues it was not released
- Omitting the carve-out for protective proceedings during mediation — a party seeking an urgent injunction from a court while mediation is pending should not breach the mediation agreement
- Settlement agreement not converting to a consent order / consent award — paper settlement; not directly enforceable without re-litigating the settlement breach

## Related skills

- [[draft-notice-of-arbitration]]
- [[draft-litigation-complaint]]
- [[review-dispute-resolution-clause]]
- [[draft-boilerplate-clauses]]
