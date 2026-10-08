---
name: az-commercial-disputes-codearranger
title: Arizona Commercial Disputes
description: 'Subject-matter bundle for Arizona commercial / business-to-business civil litigation — contract disputes, trade secret, fraudulent transfer, LLC / corporate disputes, business torts, civil racketeering, arbitration. Triggers: "Arizona commercial litigation", "Arizona business dispute", "Maricopa Commercial Court", "Arizona contract breach", "Arizona attorney fees", "UCC Arizona", "Arizona LLC dispute", "Arizona RULLCA", "Arizona judicial dissolution", "Arizona derivative action", "Arizona trade secret", "Arizona fraudulent transfer", "tortious interference", "Arizona civil RICO", "Arizona fraud particularity", "Arizona arbitration". Covers Maricopa Commercial Court, UCC, LLC Act, Business Corporation Act, Arizona Uniform Trade Secrets Act, Uniform Fraudulent Transfer Act, contract-action attorney-fee statute (A.R.S. § 12-341.01), civil racketeering with treble damages, Rule 9(b) fraud pleading.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-commercial-disputes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
---

# Arizona Commercial Disputes

> **NOT LEGAL ADVICE.** Generated content is a drafting aid. Arizona's
> contract-action attorney-fee statute (A.R.S. § 12-341.01) makes
> fee exposure a central strategic variable in almost every
> commercial matter, and several statutory remedies (trade-secret
> exemplary damages, civil-racketeering treble damages) carry precise
> multipliers and thresholds. Verify every statute number, dollar
> threshold, multiplier, and limitations count against the current
> Arizona Revised Statutes and Arizona reporters before relying.

Use this subject-matter bundle for Arizona commercial /
business-to-business civil litigation — contract, trade secret,
fraudulent transfer, intracorporate (corporate / LLC) disputes,
business torts, fiduciary-duty claims, civil racketeering, and
arbitration enforcement.

## At a glance

- **Attorney fees drive strategy.** A.R.S. § 12-341.01 gives the
  court **discretion** to award reasonable attorney fees to the
  **successful party** in any contested action **arising out of a
  contract**, express or implied. This is the single most important
  commercial-litigation lever in Arizona: it shapes settlement,
  Rule 68 offers, and pleading (frame claims to fall within or
  outside "arising out of contract"). Fees need not equal amounts
  actually paid but cannot exceed them.
- **The Maricopa County Commercial Court** runs a specialized
  complex-commercial-case docket within Superior Court. Eligible
  business disputes can be assigned to commercial-court judges for
  active case management. See `az-maricopa` and `az-superior-courts`
  for venue mechanics and assignment criteria; general business
  matters outside the commercial docket proceed in ordinary Superior
  Court civil departments.
- **Fraud-with-particularity**: Ariz. R. Civ. P. 9(b) requires that
  "the circumstances constituting fraud or mistake" be stated with
  particularity — Arizona's analog to Fed. R. Civ. P. 9(b).
- **Statutory civil racketeering**: A.R.S. § 13-2314.04 gives a
  private claimant injured by a **pattern of racketeering activity**
  a civil action in Superior Court for up to **treble damages** plus
  costs and attorney fees — Arizona's civil-RICO overlay. Confirm the
  predicate-act, pattern, and limitations requirements in the corpus
  before pleading.

## The Maricopa County Commercial Court

- Maricopa County Superior Court operates a **Commercial Court**
  docket for complex commercial / business disputes, with designated
  judges and case-management protocols geared to multi-party,
  document-intensive litigation.
- Assignment turns on eligibility criteria (subject matter, amount in
  controversy, complexity) set by local administrative order. Confirm
  current eligibility and the assignment / opt-in mechanics in the
  corpus and with `az-maricopa` before assuming commercial-court
  routing.
- Business disputes that do not qualify, or that arise outside
  Maricopa County, proceed in the ordinary Superior Court civil
  departments — see `az-superior-courts`.

## SOL catalog (the most-used)

| Claim | SOL | Citation |
|---|---|---|
| **Breach of written contract** | **6 years** | A.R.S. § 12-548 |
| **Breach of oral contract** | **3 years** | A.R.S. § 12-543 |
| **Sale of goods (UCC 2-725)** | **4 years** (parties may shorten to ≥ 1 year, not extend) | A.R.S. § 47-2725 |
| **Common-law fraud** | **3 years** (from discovery) | A.R.S. § 12-543 |
| **Tortious interference** | **2 years** | A.R.S. § 12-542 |
| **Conversion** | **2 years** | A.R.S. § 12-542 |
| **Trade-secret misappropriation (AUTSA)** | **3 years** from discovery | A.R.S. § 44-406 |
| **Fraudulent transfer (UFTA)** | actual fraud generally **4 years** (or 1 year from discovery); constructive **4 years** | A.R.S. § 44-1009 |
| **Civil racketeering** | **3 years** from discovery / **10 years** from violation | A.R.S. § 13-2314.04 |
| **Civil conspiracy** | follows the underlying tort | — |

Confirm exact counts and any discovery-rule nuance in the corpus; do
not rely on the table alone.

## The principal Arizona statutes / doctrines

### 1. Arizona UCC — A.R.S. Title 47

Arizona has enacted the Uniform Commercial Code at A.R.S. Title 47.

- **Article 2 (Sales)** — A.R.S. § 47-2101 et seq. Formation,
  warranties, performance, remedies. The **4-year statute of
  limitations** is at **A.R.S. § 47-2725**; parties may reduce it to
  not less than one year but may not extend it.
- **Article 3 (Negotiable Instruments)** — A.R.S. § 47-3101 et seq.
  Holder-in-due-course, enforcement of notes and drafts, and the
  instrument foundation for commercial collection.
- **Article 9 (Secured Transactions)** — A.R.S. § 47-9101 et seq.
  Attachment, perfection (financing-statement filing with the
  Arizona Secretary of State), priority, and the default /
  disposition / commercial-reasonableness regime. Article 9 questions
  drive most commercial-collection and collateral-priority disputes.

See `az-law-references/references/ucc-model/` for the model UCC and
the corpus for Arizona's enacting sections.

### 2. Arizona Limited Liability Company Act — A.R.S. § 29-3101 et seq.

- **This is the current Act.** The **2019 Arizona LLC Act (Arizona
  RULLCA)**, codified at **A.R.S. § 29-3101 et seq.** and **fully
  effective September 1, 2020**, replaced the prior LLC chapter at
  A.R.S. § 29-601 et seq. for all Arizona LLCs. Cite the § 29-3101
  chapter for any current dispute; reach for the old § 29-601 chapter
  only for conduct predating the transition or where a savings clause
  applies.
- **Member / manager duties** — fiduciary duties of loyalty and care
  under the Act; the operating agreement allocates management
  (member-managed vs. manager-managed) within the Act's
  non-waivable-duty floor.
- **Dissociation** — voluntary withdrawal and the statutory events of
  dissociation under the Act and the operating agreement.
- **Judicial dissolution** — on application of a member where it is
  not reasonably practicable to carry on the business in conformity
  with the certificate of organization / operating agreement, or on
  deadlock / oppression-type grounds. Dissolution is frequently a
  **buy-out lever** rather than an actual wind-up objective.
- **Derivative actions** — member standing, demand, and the
  litigation framework under the Act.

### 3. Arizona Business Corporation Act — A.R.S. § 10-101 et seq.

- **Shareholder remedies** — statutory remedies for shareholders,
  including relief in closely held corporations for oppressive /
  fraudulent / illegal conduct by those in control.
- **Derivative actions** — standing, **demand on the board**, and the
  special-litigation-committee / dismissal framework.
- **Inspection rights** — shareholder access to corporate books and
  records on proper purpose.
- **Judicial dissolution** — deadlock, illegality / oppression /
  fraud / waste / misapplication of assets by those in control, with
  buy-out alternatives.
- **Fiduciary duties** — director duty of care and loyalty;
  good-faith / business-judgment standard.

### 4. Arizona Uniform Trade Secrets Act (AUTSA) — A.R.S. § 44-401 et seq.

- **"Trade secret" and "misappropriation" defined** (A.R.S. § 44-401):
  information deriving independent economic value from not being
  generally known or readily ascertainable and subject to reasonable
  secrecy efforts; misappropriation by improper acquisition or by
  unauthorized disclosure / use.
- **Injunctive relief** (A.R.S. § 44-402): actual or threatened
  misappropriation may be enjoined.
- **Damages** (A.R.S. § 44-403): actual loss **plus** unjust
  enrichment not captured by actual loss; or a **reasonable royalty**
  in the alternative. For **willful and malicious** misappropriation,
  the court may award **exemplary damages up to twice** the
  compensatory award.
- **Attorney fees** (A.R.S. § 44-404): the court may award fees for a
  bad-faith misappropriation claim, a bad-faith motion to terminate
  an injunction, or willful and malicious misappropriation.
- **SOL** (A.R.S. § 44-406): 3 years from discovery / reasonable
  discovery.

AUTSA claims commonly overlay **noncompete enforcement** (see
`az-employment`) and **fiduciary-duty / faithless-employee** theories.

### 5. Uniform Fraudulent Transfer Act (UFTA) — A.R.S. § 44-1001 et seq.

Arizona enacted the **Uniform Fraudulent Transfer Act** at
A.R.S. § 44-1001 et seq.

- **Actual fraud** (A.R.S. § 44-1004): transfer made with actual
  intent to hinder, delay, or defraud creditors; statutory "badges of
  fraud" inform intent.
- **Constructive fraud** (A.R.S. §§ 44-1004 / 44-1005): transfer for
  less than reasonably equivalent value while insolvent or rendered
  insolvent.
- **Remedies** (A.R.S. § 44-1007): avoidance of the transfer;
  attachment; injunction; appointment of a receiver; judgment against
  the transferee.
- **SOL** (A.R.S. § 44-1009): see the corpus for the per-theory
  counts and the actual-fraud one-year-from-discovery extension.

UFTA is the primary tool for post-judgment commercial collection
where a debtor has moved assets to insiders. See `az-post-judgment`
for execution practice.

### 6. Business torts and statutory civil racketeering

- **Tortious interference** — Arizona recognizes both **interference
  with contract** and **interference with a business relationship or
  expectancy**, the latter requiring improper means or motive.
  2-year SOL (A.R.S. § 12-542).
- **Civil conspiracy** — an agreement of two or more persons to
  accomplish an unlawful purpose (or a lawful purpose by unlawful
  means); **not independently actionable** — it requires an
  underlying tort, and the limitations period follows that tort.
- **Conversion** — wrongful exercise of dominion over personal
  property inconsistent with the owner's rights. 2-year SOL
  (A.R.S. § 12-542).
- **Statutory civil racketeering** — **A.R.S. § 13-2314.04** gives a
  person injured in person, business, or property **by a pattern of
  racketeering activity** a civil action in Superior Court for
  recovery of **up to treble damages**, plus costs and attorney fees,
  and equitable relief (injunction, divestiture, constructive trust).
  Liability is proved by a **preponderance** standard. It requires a
  qualifying **pattern** of statutory predicate acts (fraud /
  schemes / theft offenses are common predicates in commercial
  matters); confirm the predicate list, the pattern / continuity
  requirement, and the **3-year-from-discovery / 10-year-from-violation**
  limitations frame in the corpus before pleading. Note the
  **jurisdictional** requirement under A.R.S. § 13-2314.04(H) to
  serve notice and a copy of the pleading on the Attorney General
  **within 30 days** after filing.

### 7. Pleading fraud with particularity — Ariz. R. Civ. P. 9(b)

Ariz. R. Civ. P. 9(b): in allegations of fraud or mistake, the
circumstances constituting fraud or mistake must be stated with
particularity — Arizona's analog to Fed. R. Civ. P. 9(b). Plead the
**who, what, when, where, and how** — the speaker, the false
representation, its time and place, the fact misrepresented, and what
was obtained or given up as a consequence. UFTA actual-fraud and
civil-racketeering fraud predicates are commonly held to this
particularity standard.

### 8. Revised Uniform Arbitration Act — A.R.S. § 12-3001 et seq.

Arizona enacted the **Revised Uniform Arbitration Act (RUAA)** at
A.R.S. § 12-3001 et seq. (the definitions section is § 12-3001). It
largely tracks — and where interstate commerce is involved is
frequently preempted by — the **Federal Arbitration Act**
(9 U.S.C. § 1 et seq.).

- **Validity / enforcement**: written arbitration agreements are
  valid and enforceable except on generally applicable
  contract-formation grounds.
- **Motion to compel / stay**: a court compels arbitration and stays
  litigation of arbitrable claims; separability of the arbitration
  clause follows *Prima Paint*-style analysis where the FAA applies,
  and delegation clauses can route gateway arbitrability questions to
  the arbitrator.
- **Vacatur**: limited statutory grounds (corruption, fraud, evident
  partiality, exceeding powers, refusal to hear material evidence).
  "Manifest disregard" is **not** an FAA vacatur ground after
  *Hall Street Associates v. Mattel*, 552 U.S. 576 (2008).
- **Confirmation**: judgment entered on a confirmed award.

## Damages and remedies

| Claim | Compensatory | Exemplary / treble | Fees |
|---|---|---|---|
| Breach of contract | Expectation / reliance / restitution | Not available (contract-only) | **Discretionary to successful party** (A.R.S. § 12-341.01) |
| Breach + fraud | K + fraud damages | Punitive on clear-and-convincing evil mind | § 12-341.01 on the contract claim |
| AUTSA | Actual loss + unjust enrichment; reasonable royalty fallback | Up to **2x** on willful & malicious (A.R.S. § 44-403) | Bad-faith / willful (A.R.S. § 44-404) |
| Civil racketeering | Actual damages | Up to **3x** (A.R.S. § 13-2314.04) | **Costs + attorney fees** (A.R.S. § 13-2314.04) |
| Conversion | Value at conversion | Punitive on evil mind | American Rule |
| UFTA | Avoidance + judgment vs. transferee | — | Case-specific |
| Tortious interference | Lost profits + lost expectancy | Punitive on evil mind | American Rule |
| Shareholder / member oppression / dissolution | Buy-out at fair value; damages | — | Court discretion |

## Forum strategy

| Claim | Default forum | Notes |
|---|---|---|
| Complex commercial / business dispute (Maricopa) | **Maricopa Commercial Court** docket | Assignment per local administrative order — confirm eligibility |
| Trade-secret / noncompete enforcement | Superior Court | Equity forum for TRO + injunction; verified pleading + sealing |
| LLC / corporate dissolution + derivative | Superior Court | SLC review for corporate derivative |
| Commercial contract / UFTA / conversion | Superior Court | Justice Court if amount ≤ $10,000 |
| Civil racketeering | **Superior Court** (A.R.S. § 13-2314.04 names Superior Court) | Treble-damages + equitable-relief menu |
| Federal diversity (out-of-state defendant + $75k) | U.S. District Court (D. Ariz.) | Removal possible; **Erie** state substantive law |
| Arbitration motion to compel | Superior Court | FAA-preempted in interstate-commerce contracts |

## Drafting checklist

- [ ] Run the **A.R.S. § 12-341.01** fee analysis early — does the
      action "arise out of a contract"? Frame claims and Rule 68
      offers with the discretionary fee award in view.
- [ ] Confirm the **6-year written-contract SOL** (A.R.S. § 12-548),
      the **3-year oral-contract SOL** (A.R.S. § 12-543), or the
      **4-year UCC 2-725 clock** (A.R.S. § 47-2725); for tort overlays
      use the 2-year A.R.S. § 12-542 clock.
- [ ] Plead **fraud with Ariz. R. Civ. P. 9(b) particularity** —
      speaker, representation, time, place, what was obtained / given
      up.
- [ ] For LLC disputes, cite the **current 2019 Act / Arizona RULLCA
      at A.R.S. § 29-3101 et seq.**, not the repealed § 29-601 chapter
      (use the old chapter only for pre-transition conduct).
- [ ] For trade-secret claims: identify the trade secret with enough
      specificity to plead without destroying secrecy; seek a
      **protective order / sealing**; pursue **2x exemplary damages +
      fees** on willful & malicious facts (A.R.S. §§ 44-403 / 44-404).
- [ ] For UFTA: plead **badges of fraud** with particularity
      (actual-fraud counts frequently held to the Rule 9(b) standard).
- [ ] For civil racketeering: confirm the **statutory predicate
      acts**, the **pattern / continuity** requirement, and the
      limitations frame before pleading A.R.S. § 13-2314.04 treble
      damages.
- [ ] For oppression / dissolution: weigh **buy-out at fair value** as
      a settlement lever vs. forced dissolution.
- [ ] For derivative claims: comply with the **demand** and
      **special-litigation-committee** framework under the BCA.
- [ ] For arbitration: identify FAA vs. Arizona RUAA governing law,
      separability of the clause, and any delegation provision before
      moving to compel under A.R.S. § 12-3001 et seq.

## Composition

- For statewide format and caption: `az-statewide-format`
- For Superior Court / Maricopa Commercial Court venue mechanics:
  `az-maricopa`, `az-superior-courts`
- For limited-jurisdiction commercial claims: `az-justice-courts`
- For the first responsive pleading: `az-first-30-days`
- For drafting motions / declarations / orders: `az-draft-motion`,
  `az-draft-declaration`, `az-draft-order`
- For SOL / limitations arithmetic: `az-deadlines`
- For discovery in a commercial matter: `az-discovery`
- For noncompete / fiduciary-duty / AUTSA overlap with employment:
  `az-employment`
- For post-judgment commercial collection (UFTA / execution):
  `az-post-judgment`

## References

- `az-law-references` — Arizona Revised Statutes, Arizona Rules of
  Civil Procedure, Arizona Rules of Evidence, federal-debt-laws +
  ucc-model symlinks
- A.R.S. § 12-341.01 — discretionary attorney fees to the successful
  party in a contract action
- A.R.S. Title 47 — Arizona UCC (Article 2 sales incl. the 4-year SOL
  at A.R.S. § 47-2725; Article 3 instruments; Article 9 secured
  transactions)
- A.R.S. § 29-3101 et seq. — Arizona Limited Liability Company Act
  (2019 Act / Arizona RULLCA, fully effective 2020; replaces the
  former § 29-601 chapter)
- A.R.S. § 10-101 et seq. — Arizona Business Corporation Act
  (shareholder remedies, derivative actions, dissolution)
- A.R.S. § 44-401 et seq. — Arizona Uniform Trade Secrets Act
  (damages A.R.S. § 44-403; fees A.R.S. § 44-404; SOL A.R.S. § 44-406)
- A.R.S. § 44-1001 et seq. — Uniform Fraudulent Transfer Act
- A.R.S. § 13-2314.04 — statutory civil racketeering (up to treble
  damages + costs + attorney fees)
- Ariz. R. Civ. P. 9(b) — fraud-with-particularity pleading
- A.R.S. § 12-3001 et seq. — Revised Uniform Arbitration Act
- *Hall Street Associates, L.L.C. v. Mattel, Inc.*, 552 U.S. 576
  (2008) — FAA vacatur grounds (informs RUAA practice)
