---
name: mi-commercial-disputes-codearranger
title: Michigan Commercial Disputes
description: Subject-matter bundle for Michigan commercial and business-to-business civil litigation. Triggers include "Michigan commercial litigation", "Michigan business court", "MCL 450.1489" shareholder oppression, "MCL 445.1901" trade secrets, "MCL 566.31" fraudulent transfer, "tortious interference Michigan", "statutory conversion MCL 600.2919a". Covers mandatory Business Court (MCL 600.8031), Michigan UCC (Articles 2/3/9), LLC and Corporation Acts (MCL 450.4101, 450.1101), shareholder oppression, MUTSA trade secrets, voidable transactions, business torts (tortious interference, conspiracy, statutory conversion with treble damages), fraud-with-particularity pleading (MCR 2.112(B)(1)), and Uniform Arbitration Act (MCL 691.1681) plus FAA preemption.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-commercial-disputes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
---

# Michigan Commercial Disputes

> **NOT LEGAL ADVICE.** Michigan routes most substantial
> business-to-business litigation through a **mandatory Business
> Court** docket in circuits with three or more judges, and forum /
> docket assignment materially shapes pace and case management.
> Statutory remedies (trade-secret exemplary damages, statutory
> conversion treble damages, shareholder-oppression buy-outs) carry
> precise thresholds and multipliers. Verify every statute number,
> dollar threshold, and limitations count against the current
> Michigan Compiled Laws and Michigan reporters before relying.

Use this subject-matter bundle for Michigan commercial /
business-to-business civil litigation — contract, trade secret,
fraudulent transfer, intracorporate (corporate / LLC) disputes,
business torts, fiduciary-duty claims, and arbitration enforcement.

## At a glance

- **The Business Court is mandatory** in any circuit with **not
  fewer than 3 circuit judges** (MCL 600.8033). Qualifying
  business / commercial disputes are assigned to a special Business
  Court docket. Most of Michigan's high-volume circuits — Wayne,
  Oakland, Macomb, Kent, Genesee — operate a Business Court. See
  `mi-wayne`, `mi-oakland`, and `mi-circuit-courts` for venue
  mechanics and assignment.
- **"Business or commercial dispute" is statutorily defined**
  (MCL 600.8031) and carries an enumerated **exclusion list**.
  Confirm both the inclusion criteria and the exclusions in the
  corpus before assuming Business Court assignment.
- **Fraud-with-particularity**: MCR 2.112(B)(1) requires that
  "the circumstances constituting fraud or mistake be stated with
  particularity" — Michigan's analog to Fed. R. Civ. P. 9(b).
- **Statutory treble-damages conversion**: MCL 600.2919a allows a
  victim of conversion (or knowing receipt / concealment of
  converted property) to recover **3 times actual damages, plus
  costs and reasonable attorney fees** — a powerful overlay on a
  common-law conversion count.

## The Michigan Business Court — MCL 600.8031–600.8047

- **Definition** (MCL 600.8031): a "business or commercial dispute"
  broadly includes actions in which all parties are business
  enterprises; actions between a business enterprise and its present
  or former owners, managers, shareholders, members, directors,
  officers, agents, employees, suppliers, guarantors of a commercial
  loan, or competitors arising out of those relationships; and
  nonprofit-governance disputes over organizational structure,
  governance, or finances. Statutory examples include sale / merger
  disputes, shareholder and membership rights, licensing / IP /
  trade-secret / antitrust / securities / noncompete agreements,
  commercial transactions, business insurance, and commercial real
  property.
- **Statutory exclusions** (MCL 600.8031): personal injury,
  wrongful death, malpractice; product-liability claims by
  individual claimants; family-division matters; probate and
  estates; criminal; condemnation; appeals; judgment enforcement;
  residential landlord-tenant; mortgage / foreclosure / condominium
  matters; motor-vehicle and individual-consumer insurance disputes;
  **employment discrimination**, civil-rights, and wrongful-discharge
  claims (except those by corporate officers / directors); and
  workers' compensation. See the corpus for the **complete** list —
  treat it as exhaustive when deciding whether a matter is a
  Business Court case.
- **Mandatory establishment** (MCL 600.8033): "Every circuit with
  not fewer than 3 circuit judges shall have a business court" and
  must submit an operating plan to the State Court Administrative
  Office and the Supreme Court for approval.
- **Operation** (MCL 600.8035–600.8047): assignment to designated
  business-court judges, written opinions, and an opinion-publication
  / repository regime distinguish the docket from a general civil
  docket. Check the assigned circuit's Business Court local
  administrative order for designation procedure and any
  reassignment mechanics.

## SOL catalog (the most-used)

| Claim | SOL | Citation |
|---|---|---|
| **Breach of written / oral contract** | **6 years** | MCL 600.5807(9) |
| **Sale of goods (UCC 2-725)** | **4 years** (parties may shorten to ≥ 1 year, not extend) | MCL 440.2725 |
| **Common-law fraud / silent fraud** | **6 years** | MCL 600.5813 (residual) |
| **Tortious interference (contract / business expectancy)** | **3 years** | MCL 600.5805 |
| **Conversion (common-law and statutory MCL 600.2919a)** | **3 years** | MCL 600.5805 |
| **Trade-secret misappropriation (MUTSA)** | **3 years** from discovery | MCL 445.1907 |
| **Voidable transaction (UVTA)** | actual fraud **6 years** (or 1 year from discovery); constructive **6 years** | MCL 566.39 |
| **Statutory shareholder oppression** | **3 years** or **2 years** from discovery, whichever first | MCL 450.1489(1) |
| **Civil conspiracy** | follows the underlying tort | — |
| **Unjust enrichment / quasi-contract** | **6 years** | MCL 600.5813 |

Confirm exact counts and any borrowing / discovery-rule nuance in
the corpus; do not rely on the table alone.

## The principal Michigan statutes / doctrines

### 1. Michigan UCC — MCL 440.1101 et seq.

Michigan has enacted the Uniform Commercial Code at MCL 440.1101
et seq.

- **Article 2 (Sales)** — MCL 440.2101 et seq. Formation,
  warranties, performance, remedies. The **4-year statute of
  limitations** is at **MCL 440.2725**; parties may reduce it to
  not less than 1 year but may not extend it.
- **Article 3 (Negotiable Instruments)** — MCL 440.3101 et seq.
  Holder-in-due-course, enforcement of notes and drafts, and the
  business-records / instrument foundation for collection.
- **Article 9 (Secured Transactions)** — MCL 440.9101 et seq.
  Attachment, perfection (financing-statement filing with the
  Michigan Secretary of State under Part 5), priority, and the
  default / disposition / commercial-reasonableness regime in
  Part 6. Article 9 questions drive most commercial-collection and
  collateral-priority disputes.

See `mi-law-references/references/ucc-model/` for the model UCC and
the corpus for Michigan's enacting sections.

### 2. Michigan Limited Liability Company Act — MCL 450.4101 et seq.

- **Member / manager duties** — fiduciary duties of loyalty and
  care; the operating agreement governs management allocation
  (member-managed vs. manager-managed).
- **Dissociation** — voluntary withdrawal and the events of
  dissociation under the Act and the operating agreement.
- **Member oppression / member remedies** — **MCL 450.4515**
  provides a member remedy for acts of managers / members in control
  that are **"willfully unfair and oppressive"** to a member, with
  relief that parallels the corporate-oppression menu (dissolution,
  buy-out at fair value, injunction, damages, accounting).
- **Judicial dissolution** — MCL 450.4801–450.4807: on application
  of a member where it is not reasonably practicable to carry on the
  business in conformity with the articles / operating agreement, or
  on deadlock / oppression-type grounds. Dissolution is frequently a
  **buy-out lever** rather than an actual wind-up objective.

### 3. Michigan Business Corporation Act — MCL 450.1101 et seq.

- **Shareholder oppression** — **MCL 450.1489** authorizes a
  shareholder to seek relief for **"willfully unfair and oppressive
  conduct"** toward the shareholder (defined at MCL 450.1489(3) as a
  continuing course of conduct or significant action that
  substantially interferes with the shareholder's interests as a
  shareholder). Court-ordered relief includes **dissolution and
  liquidation**, amendment / cancellation of articles / bylaws /
  resolutions, **direction or prohibition of corporate or
  shareholder acts**, **purchase at fair value of the complaining
  shareholder's shares** (buy-out), and **damages**. The claim
  carries a **3-year / 2-year-from-discovery** limitations period
  (MCL 450.1489(1)). Publicly traded shares are excluded.
- **Derivative actions** — MCL 450.1491a et seq.: standing,
  demand on the board, and the special-litigation-committee review
  framework.
- **Inspection rights** — shareholder access to corporate books and
  records on proper purpose.
- **Judicial dissolution** — MCL 450.1801 et seq.: deadlock,
  illegality / oppression / fraud / waste by those in control.
- **Fiduciary duties** — director duty of care and loyalty;
  good-faith / business-judgment standard.

### 4. Michigan Uniform Trade Secrets Act (MUTSA) — MCL 445.1901 et seq.

- **"Trade secret" defined** (MCL 445.1902): information that
  derives independent economic value from not being generally known
  or readily ascertainable and is the subject of reasonable efforts
  to maintain secrecy.
- **Misappropriation** (MCL 445.1902): acquisition by improper
  means, or disclosure / use without consent by one who knew or had
  reason to know it was acquired improperly or under a duty of
  secrecy.
- **Injunctive relief** (MCL 445.1903): actual or threatened
  misappropriation may be enjoined.
- **Damages** (MCL 445.1904): actual loss **plus** unjust enrichment
  not captured by actual loss; or, in the alternative, a
  **reasonable royalty**. For **willful and malicious**
  misappropriation, the court may award **exemplary damages up to
  twice** the compensatory award.
- **Attorney fees** (MCL 445.1905): the court may award fees to the
  prevailing party for a bad-faith misappropriation claim, a
  bad-faith motion to terminate an injunction, or willful and
  malicious misappropriation.
- **Displacement** (MCL 445.1908): MUTSA displaces conflicting tort
  / restitutionary remedies for trade-secret misappropriation but
  leaves contract claims and non-misappropriation torts intact.
- **SOL** (MCL 445.1907): 3 years from discovery / reasonable
  discovery.

MUTSA claims commonly overlay **noncompete enforcement** (see
`mi-employment`) and **fiduciary-duty / faithless-employee**
theories.

### 5. Uniform Voidable Transactions Act (UVTA, formerly UFTA) — MCL 566.31 et seq.

Michigan adopted the Uniform Fraudulent Transfer Act, since
modernized as the **Uniform Voidable Transactions Act** at MCL
566.31 et seq.

- **Actual fraud** (MCL 566.34): transfer made with actual intent
  to hinder, delay, or defraud creditors; statutory "badges of
  fraud" inform intent.
- **Constructive fraud** (MCL 566.34 / 566.35): transfer for less
  than reasonably equivalent value while insolvent or rendered
  insolvent.
- **Remedies** (MCL 566.37): avoidance of the transfer; attachment;
  injunction; appointment of a receiver; judgment against the
  transferee.
- **SOL** (MCL 566.39): generally 6 years; actual-fraud claims may
  alternatively run 1 year from the date the transfer was or could
  reasonably have been discovered.

The UVTA is the primary tool for post-judgment commercial
collection where a debtor has moved assets to insiders. See
`mi-post-judgment` for execution practice.

### 6. Business torts

- **Tortious interference** — Michigan recognizes both
  **interference with contract** and **interference with a business
  relationship or expectancy**, the latter requiring a per-se
  wrongful act or a lawful act done with malice and unjustified in
  law. 3-year SOL (MCL 600.5805).
- **Civil conspiracy** — a combination of two or more persons to
  accomplish an unlawful purpose (or a lawful purpose by unlawful
  means); **not independently actionable** — it requires an
  underlying tort, and the limitations period follows that tort.
- **Conversion** — common-law conversion plus the **statutory
  conversion** remedy at **MCL 600.2919a**: a person damaged by
  another's stealing / embezzling / converting property, or by
  another's knowing receipt / concealment of converted property,
  may recover **3 times actual damages, plus costs and reasonable
  attorney fees** — a remedy expressly cumulative with other legal
  remedies.

### 7. Pleading fraud with particularity — MCR 2.112(B)(1)

MCR 2.112(B)(1): "In allegations of fraud or mistake, the
circumstances constituting fraud or mistake must be stated with
particularity." Plead the **who, what, when, where, and how** —
the speaker, the false representation, its time and place, the fact
misrepresented, and what was obtained or given up as a consequence.
Statutory-conversion and UVTA actual-fraud counts are commonly held
to the same particularity standard.

### 8. Michigan Uniform Arbitration Act — MCL 691.1681 et seq.

Michigan enacted the (revised) Uniform Arbitration Act at MCL
691.1681 et seq. It largely tracks — and where interstate commerce
is involved is frequently preempted by — the **Federal Arbitration
Act** (9 U.S.C. § 1 et seq.).

- **Validity / enforcement**: written arbitration agreements are
  valid and enforceable except on generally applicable
  contract-formation grounds.
- **Motion to compel / stay**: a court compels arbitration and stays
  litigation of arbitrable claims; severability / separability of
  the arbitration clause follows *Prima Paint*-style analysis where
  the FAA applies, and delegation clauses can route gateway
  arbitrability questions to the arbitrator.
- **Vacatur**: limited statutory grounds (corruption, fraud, evident
  partiality, exceeding powers, refusal to hear material evidence).
  "Manifest disregard" is **not** an FAA vacatur ground after
  *Hall Street Associates v. Mattel*, 552 U.S. 576 (2008).
- **Confirmation**: judgment entered on a confirmed award.

## Equitable-remedy practice

| Remedy | Standard | Authority |
|---|---|---|
| **TRO** | Immediate and irreparable injury; notice or reasons it cannot be given | MCR 3.310(B) |
| **Preliminary injunction** | (1) likelihood of success; (2) irreparable harm; (3) balance of harms; (4) public interest | MCR 3.310 |
| **Bond** | Required unless waived for good cause | MCR 3.310(D) |
| **Receivership** | Insolvency, dissipation risk, dispute over property | MCR 2.622; MCL 600.2926 |
| **Specific performance** | Real property; unique goods; inadequacy of damages | Common-law equity |
| **Accounting / constructive trust** | Unjust enrichment + traceable benefit + inadequate legal remedy | Common-law equity |

## Damages and remedies

| Claim | Compensatory | Exemplary / treble | Fees |
|---|---|---|---|
| Breach of contract | Expectation / reliance / restitution | Not available (contract-only) | American Rule unless K shifts |
| Breach + fraud | K + fraud damages | Exemplary on fraud where malice / oppression shown | American Rule |
| MUTSA | Actual loss + unjust enrichment; reasonable royalty fallback | Up to **2x** on willful & malicious (MCL 445.1904) | Prevailing party on bad-faith / willful (MCL 445.1905) |
| Statutory conversion | Actual damages | **3x actual damages** (MCL 600.2919a) | **Costs + reasonable attorney fees** (MCL 600.2919a) |
| Common-law conversion | Value at conversion | — | American Rule |
| UVTA | Avoidance + judgment vs. transferee | — | Case-specific |
| Tortious interference | Lost profits + lost expectancy | Exemplary on malice | American Rule |
| Shareholder / member oppression | Buy-out at fair value; damages | — | Court discretion (MCL 450.1489 / 450.4515) |

## Forum strategy

| Claim | Default forum | Notes |
|---|---|---|
| Substantial business / commercial dispute | **Business Court** (circuits with 3+ judges) | Mandatory assignment if within MCL 600.8031 and not excluded |
| Trade-secret / noncompete enforcement | Circuit Court (Business Court docket) | Equity forum for TRO + injunction; verified pleading + sealing |
| LLC / corporate dissolution + derivative | Circuit Court (Business Court docket) | SLC review for corporate derivative |
| Commercial contract / UVTA / conversion | Circuit Court (Business Court docket) | District Court if amount ≤ $25,000 |
| Excluded matters (PI, individual product-liability, employment-discrimination, etc.) | General civil docket | Per MCL 600.8031 exclusions |
| Federal diversity (out-of-state defendant + $75k) | U.S. District Court (E.D. / W.D. Mich.) | Removal possible; **Erie** state substantive law |
| Arbitration motion to compel | Circuit Court | FAA-preempted in interstate-commerce contracts |

## Drafting checklist

- [ ] Determine whether the matter is a **"business or commercial
      dispute"** under MCL 600.8031 and **not** within the exclusion
      list — if so, expect mandatory **Business Court** assignment in
      a 3+-judge circuit.
- [ ] Confirm the **6-year contract SOL** (MCL 600.5807(9)) or the
      **4-year UCC 2-725 clock** (MCL 440.2725); for tort overlays
      use the 3-year MCL 600.5805 clock.
- [ ] Plead **fraud with MCR 2.112(B)(1) particularity** — speaker,
      representation, time, place, what was obtained / given up.
- [ ] For conversion, evaluate the **statutory MCL 600.2919a**
      treble-damages-plus-fees count alongside common-law conversion;
      plead the knowing-receipt / concealment theory where facts
      support it.
- [ ] For trade-secret claims: identify the trade secret with enough
      specificity to plead without destroying secrecy; seek a
      **protective order / sealing** for the description; pursue
      **2x exemplary damages + fees** on willful & malicious facts.
- [ ] For TRO / preliminary injunction: verified pleading + MCR 3.310
      motion + bond + declarations establishing **irreparable harm**
      (money damages inadequate).
- [ ] For UVTA: plead **badges of fraud** with particularity (actual
      fraud frequently held to the MCR 2.112(B)(1) standard).
- [ ] For oppression / dissolution: weigh **buy-out at fair value**
      (MCL 450.1489 corporate / MCL 450.4515 LLC) as a settlement
      lever vs. forced dissolution.
- [ ] For derivative claims: comply with the **demand** and
      **special-litigation-committee** framework (MCL 450.1491a).
- [ ] For arbitration: identify FAA vs. Michigan UAA governing law,
      separability of the clause, and any delegation provision before
      moving to compel.

## Composition

- For statewide format and caption: `mi-statewide-format`
- For Circuit Court / Business Court venue mechanics:
  `mi-wayne`, `mi-oakland`, `mi-circuit-courts`
- For limited-jurisdiction commercial claims ≤ $25,000:
  `mi-district-courts`, `mi-36th-district`
- For the first responsive pleading: `mi-first-30-days`
- For drafting motions / declarations / orders: `mi-draft-motion`,
  `mi-draft-declaration`, `mi-draft-order`
- For SOL / limitations arithmetic: `mi-deadlines`
- For discovery in a commercial matter: `mi-discovery`
- For noncompete / fiduciary-duty / MUTSA overlap with employment:
  `mi-employment`
- For post-judgment commercial collection (UVTA / execution):
  `mi-post-judgment`

## References

- `mi-law-references` — Michigan Compiled Laws, Michigan Court
  Rules, Michigan Rules of Evidence, federal-debt-laws + ucc-model
  symlinks
- MCL 600.8031–600.8047 — Business Court (definition, mandatory
  establishment, operation, exclusions)
- MCL 440.1101 et seq. — Michigan UCC (Article 2 sales incl. the
  4-year SOL at MCL 440.2725; Article 3 instruments; Article 9
  secured transactions)
- MCL 450.4101 et seq. — Michigan Limited Liability Company Act
  (member oppression MCL 450.4515; judicial dissolution
  MCL 450.4801)
- MCL 450.1101 et seq. — Michigan Business Corporation Act
  (shareholder oppression MCL 450.1489; derivative actions
  MCL 450.1491a; dissolution MCL 450.1801)
- MCL 445.1901 et seq. — Michigan Uniform Trade Secrets Act
  (damages MCL 445.1904; fees MCL 445.1905; SOL MCL 445.1907)
- MCL 566.31 et seq. — Uniform Voidable Transactions Act
- MCL 600.2919a — statutory conversion (treble damages + costs + fees)
- MCR 2.112(B)(1) — fraud-with-particularity pleading
- MCL 691.1681 et seq. — Michigan Uniform Arbitration Act
- *Hall Street Associates, L.L.C. v. Mattel, Inc.*, 552 U.S. 576
  (2008) — FAA vacatur grounds (informs UAA practice)
