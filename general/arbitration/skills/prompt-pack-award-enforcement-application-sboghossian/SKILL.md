---
name: prompt-pack-award-enforcement-application-sboghossian
title: Award Enforcement Application
description: Use when drafting an application to enforce a foreign or domestic arbitral award in a specific jurisdiction, including certified copies of the award and arbitration agreement, addressing enforcement requirements and anticipating grounds for refusal. Arbitration practice area; covers enforcement under the New York Convention and MENA-specific enforcement procedures (UAE, KSA, Egypt, Lebanon, DIFC, ADGM).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-award-enforcement-application
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Award Enforcement Application

## When to use this

Use this skill when drafting an **application to the competent court** to recognize and enforce an arbitral award, whether:
- A **foreign award** (made in a seat outside the enforcement jurisdiction) under the New York Convention 1958
- A **domestic award** (made in the same jurisdiction as enforcement) under the applicable national arbitration law

The enforcement application is typically a court filing — a petition or application supported by documents, factual summary, and legal argument for why the award should be recognized and enforcement granted. The opposing party (the award debtor) has limited but defined grounds to resist.

---

## Prompt template

> Draft an application to enforce [arbitral award] in [jurisdiction] under the New York Convention. Include certified copies of award and arbitration agreement, address enforcement requirements, and anticipate potential grounds for refusal.

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Award details (case reference, date, amount, parties) | Core of the application |
| Arbitral seat | Determines whether this is a foreign or domestic award; which Convention applies |
| Enforcement jurisdiction | Determines the applicable enforcement procedure, court, documents required |
| Award debtor's assets | Enforcement is only useful if there are assets to attach — confirm asset location |
| Current status of award (final? subject to set-aside proceedings at seat?) | Pending set-aside applications may affect enforcement timing |
| Grounds for resistance anticipated | Allows pre-emptive argumentation |

---

## Document structure

### 1. Introduction / heading

Court caption:
- Court name (full formal name)
- Case number (to be assigned)
- Applicant (award creditor)
- Respondent (award debtor)
- Nature of application: "Application for Recognition and Enforcement of Foreign Arbitral Award"

### 2. Statement of facts

Concise factual narrative:
- The parties and their relationship
- The arbitration agreement (which contract; arbitration clause reference)
- The dispute: brief summary of the claims
- The arbitral proceedings: institution used; seat; number of arbitrators; key procedural dates; hearing dates
- The award: date rendered; tribunal members; summary of outcome; amount awarded (principal + interest + costs)
- Current enforcement status: has the award been enforced or resisted in any other jurisdiction?
- Any set-aside proceedings at the seat (and their outcome or current status)

### 3. Documents in support

Standard documentary requirements for a New York Convention enforcement application:

| Document | Requirement |
|---------|------------|
| Original or certified copy of the award | New York Convention Art. IV(1)(a); most jurisdictions accept certified copies |
| Certified translation of the award | Required where the award is not in the enforcement court's official language |
| Original or certified copy of the arbitration agreement | Art. IV(1)(b) — the written arbitration agreement |
| Certified translation of the arbitration agreement | If not in the official language |
| Proof of service of the award on the respondent | Some jurisdictions require |
| Proof of finality of the award | Confirmation it is final and binding (not subject to appeal at the seat); statement from the institution or tribunal may suffice |

Jurisdiction-specific additional documents:
- **UAE (Dubai Courts)**: sworn Arabic translation of all documents; original filing fee payment receipt; power of attorney notarized and attested
- **UAE (DIFC Courts)**: English-language filing is standard; DIFC Court Form 1 for the claim; reduced documentary burden compared to onshore courts
- **Egypt**: Arabic translation; filing at the Cairo Court of Appeal (enforcement jurisdiction for foreign awards); proof that the seat country and Egypt are both NYC signatories
- **Lebanon**: filing at the Court of Appeal; Arabic translation; proof of finality

### 4. Grounds for recognition and enforcement

Summarize the legal basis:

**For foreign awards — New York Convention Art. III and V**:
> The Republic of [seat] and [enforcement jurisdiction] are both Contracting States to the Convention on the Recognition and Enforcement of Foreign Arbitral Awards (New York, 1958). Pursuant to Article III of the Convention, this Court shall recognize and enforce the Award in accordance with the rules of procedure of [enforcement jurisdiction] and subject only to the conditions set out in Article V.

State that none of the Art. V(1) grounds for refusal apply (see section 5 below).

**For domestic awards — national arbitration law**:
Reference the applicable national arbitration law enforcement provision (e.g., UAE Federal Arbitration Law Art. 52; Egyptian Arbitration Law Art. 56; Lebanese CPC Art. 801; DIFC Arbitration Law Art. 42).

### 5. Pre-empting grounds for refusal

Article V(1) NYC grounds (available to the award debtor to resist enforcement):
- **V(1)(a)**: Party incapacity or invalid arbitration agreement — address: both parties were legally capable; the arbitration agreement was valid under [governing law]
- **V(1)(b)**: Proper notice not given; unable to present case — address: Respondent was properly notified; had full opportunity to participate
- **V(1)(c)**: Award beyond scope of arbitration agreement — address: the award addresses only the submitted claims; within the scope of the arbitration agreement
- **V(1)(d)**: Improper composition of tribunal or procedure — address: tribunal constituted per agreement and institutional rules; procedure proper
- **V(1)(e)**: Award not yet binding or has been set aside at seat — address: the award is final and binding; no pending set-aside proceedings [or if there are proceedings: explain status and argue they should not delay enforcement]

Article V(2) NYC grounds (court may raise on its own motion):
- **V(2)(a)**: Subject matter not arbitrable under enforcement law — address: commercial dispute; fully arbitrable under [enforcement jurisdiction] law
- **V(2)(b)**: Enforcement would be contrary to public policy — this is the most common ground raised in MENA enforcement; pre-empt it specifically (see jurisdictional notes below)

### 6. Relief sought

> The Applicant respectfully requests that this Honourable Court:
> 1. Recognize the Award as a binding arbitral award;
> 2. Grant leave to enforce the Award as a judgment of this Court;
> 3. Enter judgment in favor of the Applicant against the Respondent for the principal amount of [currency + amount], together with interest at the rate of [X%] per annum from [date] and costs of [amount] as awarded;
> 4. Order the Respondent to pay the Applicant's costs of this application; and
> 5. Grant such further relief as the Court considers appropriate.

---

## Jurisdictional enforcement procedures

### UAE — DIFC Courts (fastest route for foreign awards)
The DIFC Courts are the most efficient enforcement venue in the UAE for international awards:
- File a claim under the DIFC Courts Practice Direction on Arbitration
- Proceedings are in English; no sworn Arabic translation required
- Awards can be enforced in the DIFC judicial zone; through the DIFC-Dubai Courts Enforcement Protocol, DIFC orders can be enforced against assets in onshore Dubai
- Timeline: as fast as 6–8 weeks for uncontested enforcement

### UAE — Dubai Courts (onshore)
- All documents must be in Arabic (sworn translation by licensed translator)
- File the application at the Dubai Courts of First Instance (execution court)
- Timeline: 3–12 months depending on whether respondent contests
- Public policy objections: Dubai Courts have generally upheld international awards; specific issues arise with awards requiring payment of interest on Islamic finance instruments

### UAE — Abu Dhabi Courts (onshore) / ADGM Courts
Similar to Dubai Courts for onshore. ADGM Courts mirror DIFC procedure for ADGM-seated arbitrations and foreign awards.

### KSA — Saudi Courts
- Saudi courts enforce under the NYC and the Arab League Convention on the Enforcement of Judgments and Awards (1952)
- Arabic translation required; certified by Ministry of Foreign Affairs
- Sharia-law public policy ground: awards requiring payment of conventional interest (riba) may be challenged; courts have declined to enforce interest components in some cases
- Timeline: 6–18 months; enforcement through the General Court or the Commercial Court

### Egypt — Court of Appeal (Cairo)
- File at the Cairo Court of Appeal (Art. 56 Egyptian Arbitration Law)
- Arabic translation required
- Egypt is generally enforcement-friendly; courts have declined enforcement on public policy grounds in relatively few cases
- Timeline: 6–12 months

### Lebanon — Court of Appeal
- File at the Court of Appeal of the enforcement district
- Arabic or French translation (courts accept both)
- Lebanon is generally enforcement-friendly
- Timeline: variable; court capacity constraints

---

## Public policy — MENA-specific considerations

The public policy ground (Art. V(2)(b) NYC) is most often invoked in MENA to resist enforcement. Common scenarios:

| Issue | How courts have handled it |
|-------|--------------------------|
| Interest / riba (KSA, UAE Islamic finance context) | Saudi courts: may sever interest; UAE onshore courts: enforce conventional interest in commercial (non-Islamic finance) awards |
| Sharia-law non-compliance of the underlying transaction | Generally raised unsuccessfully unless the contract is fundamentally contrary to Islamic law |
| Award based on contract that violates mandatory law (e.g., unlicensed agency in UAE) | Courts have set aside or declined enforcement in some cases; flag if contract had licensing issues |
| Due process (natural justice) | Courts apply this ground strictly — procedural irregularities must be material |

Pre-empt public policy arguments in the application by demonstrating: the underlying transaction was lawful; interest is commercial (not usurious); the tribunal's findings are supported by the evidence.

---

## Common mistakes

- Missing certified translation — enforcement is routinely rejected without proper Arabic (or local language) translation
- Applying to the wrong court — some jurisdictions require filing at courts of appeal, not courts of first instance
- Not addressing pending set-aside proceedings at the seat — courts will inquire; address proactively
- Weak public policy pre-emption — leaving the respondent to raise public policy unchallenged
- Not securing assets before filing — by the time enforcement is sought, the debtor may have transferred assets; consider applying for a court-ordered asset freeze simultaneously

---

## Related skills

- [[prompt-pack-arbitration-agreement-clause]] — the clause that creates the right to arbitrate and thus the award
- [[prompt-pack-arbitration-clause-comparison]] — institutional/seat selection affects enforcement complexity
- [[prompt-pack-arbitration-cost-submission]] — the costs that form part of the award being enforced
- [[kb-arbitration-mena]] — MENA arbitration law and enforcement reference
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction determines procedure
