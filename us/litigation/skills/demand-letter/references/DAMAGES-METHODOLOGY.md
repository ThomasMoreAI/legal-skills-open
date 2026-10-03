# Damages Methodology

Read this file when executing Step 4 of `../SKILL.md`. Every damages number in a demand letter must trace to one of the categories below, with the inputs, arithmetic, verification hook, and presentation choice recorded in the file history (or in a damages-worksheet exhibit). If a number cannot trace to one of these frameworks, cut it or flag it — do not publish.

## Cross-cutting rules

1. **No lump-sum client numbers as computed.** If the client supplies a total ("I want $200,000") without line-item backup, you have three options and no others:
   - **Request breakdown.** Pause drafting, tell the user what's missing, and resume when the inputs arrive.
   - **Label as unverified.** Keep the client number in the draft but mark it `[UNVERIFIED — client-provided]` and surface the flag in Checkpoint B (`../SKILL.md`).
   - **Abandon the number.** Draft without it and state that damages are "to be further documented" — common in early-stage statutory notices where the exact amount is not yet required.
2. **Never present a number as computed if it wasn't.** A table that shows "$ 47,318.52" to the penny implies precision that must be defensible line by line.
3. **Every line item needs a source.** An invoice, a billing statement, a medical-records summary, an expert report, a statute. No source = no number.
4. **Never assert fees without a verified basis.** See Fees and costs below.
5. **Never disclose the walkaway number.** The demand is the ask, not the floor. Leaving room for negotiation is expected; leaving room for suggestion of the floor is malpractice-adjacent.

## Category 1 — Direct (expectation) damages

The loss that naturally flows from the adverse party's conduct; the amount that puts the client in the position performance would have achieved.

| What to collect | Arithmetic | Verification hook | Presentation |
|---|---|---|---|
| Invoices, purchase orders, payment records, proof of tender, contract price terms, market-value evidence | Contract price minus value received; or cost-to-complete; or repair/replacement cost; or (for personal injury) medical specials billed-and-paid | None required if documented by invoice/billing statement; mark `[UNVERIFIED — client-provided]` if client provides only a summary | Inline narrative if one category; table if combined with consequentials |

**Personal injury specifics.** Medical specials have two numbers: **billed** and **paid**. Many jurisdictions limit recovery to the billed amount only if paid by the plaintiff or a non-collateral-source payer (collateral-source rule varies; `[VERIFY]`). In some jurisdictions, the paid amount is the admissible figure. Note both in the demand and state which number the demand is based on.

**Commercial specifics.** Expectation is the default measure for contract breach. Reliance damages (out-of-pocket costs incurred in reliance on the contract) are an alternative when expectation is speculative — use only one theory per claim.

## Category 2 — Consequential damages

Losses that flow from the breach but depend on the adverse party's knowledge or foreseeability at contract formation (UCC § 2-715(2)(a) / *Hadley v. Baxendale*) or, in tort, on proximate cause.

| What to collect | Arithmetic | Verification hook | Presentation |
|---|---|---|---|
| Communications establishing the adverse party's pre-breach awareness of the at-risk business / downstream customer / profit stream; lost-profits records; replacement-cost records; lost-employment records; causation chain documentation | Sum of identifiable downstream losses traceable to the breach through an unbroken causation chain | `legal-research` for jurisdiction's foreseeability standard (UCC § 2-715; common-law *Hadley* formulation; tort proximate-cause standard) | Always itemized; never a lump sum |

**Foreseeability rule.** State the foreseeability basis in the letter: "Defendant was advised by email dated [DATE] that Plaintiff's performance depended on [specific downstream relationship]." Without this, consequentials are easy targets for exclusion at summary judgment.

**Limitations of liability.** Many commercial contracts exclude or cap consequentials. Check the contract before claiming them. If the clause is facially valid, flag the claim is at risk and either (a) plead alternative theories that survive the cap (e.g., gross negligence, willful misconduct, fraud — if facts support) or (b) reduce the claim to the cap and say so.

## Category 3 — Statutory multipliers

Double, treble, or punitive damages available under a specific statute when specific conduct is proven. Never claim without citing the statute and naming the conduct.

| Common hooks | Multiplier | Triggering conduct | Verification |
|---|---|---|---|
| MA Ch. 93A § 9(3) | 2x or 3x actual | Willful or knowing violation; or insufficient response to a reasonable § 9(3) settlement offer | `legal-research` for current case law on "knowing or willful"; `JURISDICTION-PRESUIT.md` for the § 9(3) response mechanism |
| TX DTPA § 17.50(b)(1) | Up to 3x economic damages | "Knowing" violation for up to 3x economic; "intentional" for up to 3x mental anguish | `legal-research`; `citation-bluebook` for any case-law on the knowing/intentional distinction |
| MMWA (15 U.S.C. § 2301 et seq.) | No multiplier, but attorney's fees | Warranty breach; consumer-product scope | `legal-research` for scope; see `ARCHETYPE-INDEX.md` for exemplar |
| Lanham Act § 35 (15 U.S.C. § 1117) | Up to 3x profits/damages | Willful infringement | `legal-research`; `citation-bluebook` on the "exceptional case" standard |
| Defend Trade Secrets Act § 1836(b)(3)(C) | 2x damages | Willful and malicious misappropriation | `legal-research` |
| State punitive-damages statutes | Varies | Varies (clear-and-convincing "malice," "oppression," "fraud"; jurisdiction-specific caps) | `legal-research` for the state's standard AND cap |

**Rule.** If you claim a multiplier, you must (a) identify the qualifying conduct with facts from §2 of the letter, (b) cite the statute verbatim or with pinpoint, and (c) verify the citation via `legal-research`. Do not claim a multiplier merely to inflate the demand — it reads as overreach and undermines the rest of the letter.

**Punitive damages in a demand letter.** Demanding punitive damages pre-suit signals posture but is rarely collected without litigation. Claim only when the factual record supports the heightened standard. Otherwise reserve.

## Category 4 — Prejudgment interest

Interest on unpaid amounts from an accrual date to the date of the demand (or to the date of judgment in litigation). Governed by statute, contract, or common law — jurisdiction-specific.

| What to collect | Arithmetic | Verification hook | Presentation |
|---|---|---|---|
| Accrual date (usually date of breach or demand for payment); governing interest rate; compounding rule (simple vs. compound) | Principal × rate × (days / 365) for simple; (1 + rate)^years × principal − principal for compound | `legal-research` for the state's prejudgment rate statute AND accrual rule; contract for a liquidated-rate clause | Inline line-item with rate and period shown |

**Required disclosure in the letter.** State the rate, the accrual date, and the source (e.g., "9% per annum, from {{DATE}} per {{STATE}} Stat. § {{X}}"). A bare number invites challenge.

**Contract interest.** If the contract specifies an interest rate for unpaid amounts, use that rate (subject to usury caps, jurisdiction-specific). If both contract and statute apply, contract typically controls — `[VERIFY]`.

## Category 5 — Liquidated damages

A contract-specified dollar amount triggered by a specified breach. Enforceable only if it is a reasonable estimate of difficult-to-calculate actual damages, not a penalty.

| What to collect | Verification hook | Presentation |
|---|---|---|
| The verbatim contract clause; evidence that actual damages would be difficult to calculate; case law on penalty doctrine in the governing jurisdiction | `citation-bluebook` + `legal-research` for enforceability case law | Quote the clause verbatim in §3 of the letter, then claim the amount in §4 |

**Rule.** If the clause is vulnerable to a penalty challenge (e.g., the amount is wildly disproportionate to any conceivable actual loss), claim it but also plead actual damages in the alternative so the demand does not collapse if the clause is struck.

## Category 6 — Mitigation offsets

Not a damages category — a subtraction. Must be addressed affirmatively whenever facts suggest a mitigation defense is in play.

**When to disclose.**
- Client received insurance or third-party payments for the same loss → collateral-source rule (jurisdiction-specific); disclose and explain why it does not reduce recovery.
- Client could have mitigated but did not → disclose what steps the client did take, why further mitigation was not feasible, or concede the offset.
- Client received partial payments → subtract from total demand, show the math.

**Presentation.** Inline in §4 after the damages table: "These figures account for [$X] in [collateral-source / partial-payment / salvage] received as of [DATE]. [Or: Plaintiff mitigated by doing {{X, Y, Z}}; further mitigation was infeasible because {{REASON}}.]"

## Category 7 — Fees and costs

Attorney's fees and costs of suit, collectable only when a specific contract or statute authorizes them.

| Basis | Examples | Verification |
|---|---|---|
| Contract fee-shifting clause | "Prevailing party entitled to fees" | Quote the clause verbatim; confirm it covers pre-suit demands (many don't) |
| Statutory fee-shifting | MA Ch. 93A § 9(4); CLRA § 1780(e); DTPA § 17.50(d); FDCPA § 1692k(a)(3); Lanham Act § 35; 42 U.S.C. § 1988; state UDAP statutes | `legal-research` + `citation-bluebook` |
| Bad-faith insurance | State-specific; varies | `legal-research` |
| Common-fund / collateral-litigation exceptions | Rare in demand-letter context | `legal-research` |

**Rule.** If the basis is a contract clause, quote it. If the basis is a statute, cite the specific subsection. If neither applies, do not claim fees. Unfounded fee demands are the most common ethics concern in demand-letter practice.

**Costs.** Court costs are not collectable pre-suit. Do not claim them until a complaint is filed. Investigative costs, expert fees, and out-of-pocket litigation expenses are separately governed by statute or contract — do not aggregate.

## Bifurcation rule

When to split the demand:
- **Liquidated today, consequentials later.** If direct damages are documented but consequentials require expert analysis not yet complete, demand the liquidated amount with full documentation, reserve consequentials for discovery or a supplemental demand. Say this explicitly in §4.
- **Monetary today, non-monetary via injunction.** When the relief includes both money and an injunction (e.g., trademark C&D with trebled profits), demand the money in §6 and demand the conduct change as a separate bullet, each with its own deadline.

## Presentation decision tree

- 1 category, <3 line items → inline narrative paragraph.
- 1 category, 3+ line items OR 2+ categories → table in §4.
- 4+ categories OR extensive billing-record backup → summary table in §4, full itemization in an appendix exhibit referenced inline.
- Medical specials in a personal-injury demand → always itemized by provider, with dates, billed/paid, and totals per provider; see `assets/examples/pi-ga-auto-allen-v-liberty-mutual-demand.pdf` for an exemplar.

## What NOT to include in the damages section

- Witness-strategy commentary.
- Expert-opinion summaries (attach the expert report as an exhibit; do not paraphrase in the letter).
- Emotional-distress multipliers that are not grounded in a specific damages theory.
- Any number that is not backed by a source.
- The walkaway number.
