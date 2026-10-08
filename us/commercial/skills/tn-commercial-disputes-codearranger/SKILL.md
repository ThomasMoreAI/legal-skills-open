---
name: tn-commercial-disputes-codearranger
title: Tennessee Commercial Disputes
description: Subject-matter bundle for Tennessee commercial / business-to-business litigation. Covers Chancery Court (the principal commercial-equity forum), Davidson Business Court, the TCPA's narrow B2B reach under Pursell v. First American National Bank, Tennessee Uniform Trade Secrets Act (TUTSA, § 47-25-1701 et seq.), Uniform Voidable Transactions Act (§ 66-3-301 et seq.), Tennessee Revised LLC Act (§ 48-249-101 et seq.), Tennessee Business Corporation Act (§ 48-11-101 et seq.), Rule 9.02 fraud-with-particularity pleading, derivative actions, LLC/corporate dissolution and buy-out, business torts (tortious interference, civil conspiracy, conversion), Tennessee Uniform Arbitration Act (§ 29-5-301 et seq.) with FAA preemption, and Tennessee Securities Act (§ 48-1-101 et seq.).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-commercial-disputes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
---

# Tennessee Commercial Disputes

> **NOT LEGAL ADVICE.** Tennessee commercial practice is heavily
> Chancery-centric on equitable claims, with the unusual
> **Pursell** rule narrowing the TCPA's reach to most business-to-
> business disputes. Forum choice (Chancery vs. Circuit vs.
> Business Court vs. federal diversity) materially shapes
> available remedies and pace. Verify every statute number and
> case citation against the current Tenn. Code Ann. and Tennessee
> reporters before relying.

Use this subject-matter bundle for Tennessee commercial /
business-to-business civil litigation — contract, trade secret,
fraudulent transfer, intracorporate (corporate / LLC) disputes,
business torts, fiduciary-duty claims, and equitable enforcement.

## At a glance

- **Chancery is the commercial forum**: Tennessee Chancery Courts
  hold equity jurisdiction and concurrent jurisdiction over most
  legal claims. Most contract / fiduciary-duty / trade-secret /
  non-compete enforcement / dissolution matters route to Chancery.
- **Davidson County Business Court**: the 20th JD operates a
  designated Business Court division within the Chancery Court at
  Nashville. Cases are designated under a published threshold
  (typically business disputes exceeding a stated amount in
  controversy or involving particular subject-matter — confirm via
  the Davidson Chancery local rules). See
  `tn-davidson` for venue mechanics.
- **TCPA narrow in B2B**: under *Pursell v. First American
  National Bank*, 937 S.W.2d 838 (Tenn. 1996), the **Tennessee
  Consumer Protection Act** at Tenn. Code Ann. § 47-18-101 et
  seq. generally **does not reach** purely commercial / business-
  to-business transactions. See `tn-consumer-debt` for the
  consumer-side TCPA framework.
- **Fraud-with-particularity**: Tenn. R. Civ. P. 9.02 mirrors
  Fed. R. Civ. P. 9(b); every commercial-fraud claim must allege
  "the time, place, and contents of the false representation,
  the fact misrepresented, and what was obtained or given up as a
  consequence."
- **Pre-suit notice for some claims**: business claims that piggy-
  back on the TCPA's narrow B2B carve-out trigger the **45-day
  pre-suit demand** under § 47-18-109(a)(1). Most pure breach-of-
  contract / fiduciary-duty / trade-secret claims do **not** have
  a pre-suit-notice gate.

## SOL catalog (the most-used)

| Claim | SOL | Citation |
|---|---|---|
| **Breach of written contract** | **6 years** | Tenn. Code Ann. § 28-3-109(a)(3) |
| **Breach of oral contract** | **6 years** | § 28-3-109(a)(3) (Tennessee treats both equally for written/oral up to typical commercial contracts) |
| **Sale of goods (UCC § 47-2-725)** | **4 years** | Tenn. Code Ann. § 47-2-725 |
| **Breach of partnership / fiduciary duty** | **3 years** (property) / **6 years** if written contract / sometimes treated as breach of contract — case-specific | § 28-3-105 / § 28-3-109 |
| **Tortious interference (contract / business expectancy)** | **3 years** | § 28-3-105 |
| **Common-law fraud** | **3 years** | § 28-3-105 (discovery rule) |
| **TUTSA (trade secrets)** | **3 years** | Tenn. Code Ann. § 47-25-1709 (from discovery) |
| **TUFTA / Uniform Voidable Transactions** | **4 years** (actual fraud); **1 year** from discovery for constructive | Tenn. Code Ann. § 66-3-310 |
| **Conversion** | **3 years** | § 28-3-105 |
| **Civil conspiracy** | follows underlying tort | — |
| **TCPA (where applicable in B2B)** | **1 year** from discovery; max **5 years** | § 47-18-110 |
| **Securities Act (Tennessee blue-sky)** | **1 year / 4 years** repose | § 48-1-122 |
| **Promissory estoppel / unjust enrichment** | **6 years** (treated as quasi-contract) | § 28-3-109 |
| **Accountings / equitable claims (Chancery)** | typically **6 years** by analogy to written-contract SOL; equity may apply laches | — |

## The six principal Tennessee statutes / doctrines

### 1. The TCPA and the *Pursell* B2B exclusion

The Tennessee Consumer Protection Act at Tenn. Code Ann. § 47-18-
101 et seq. nominally prohibits "unfair or deceptive acts or
practices affecting the conduct of any trade or commerce" — broad
language that could read to cover B2B disputes. *Pursell v. First
American National Bank*, 937 S.W.2d 838 (Tenn. 1996), narrowed
the reach: the TCPA was intended to protect **consumers**, and a
commercial dispute between sophisticated business entities,
including disputes over the act of collecting a commercial debt
or enforcing a commercial contract, is generally **outside the
TCPA's scope**. Subsequent cases have refined the line — TCPA
*may* reach B2B conduct where one side functions as a consumer
or where the deceptive act is part of conduct affecting the
broader consumer marketplace — but the **strong default is
non-applicability** in pure B2B litigation.

**Drafting implications**:
- Do **not** plead a TCPA count in a pure B2B contract dispute
  unless there is a non-frivolous *Pursell*-distinguishing
  theory. Defense should move to dismiss under Rule 12.02(6)
  with *Pursell* citation.
- Plaintiff should rely on contract-based remedies (breach,
  fraud, conversion, tortious interference) rather than the
  TCPA's treble-damages + mandatory-fee draw.

### 2. Tennessee Uniform Trade Secrets Act (TUTSA) — § 47-25-1701 et seq.

Tennessee enacted the Uniform Trade Secrets Act in 2000.

- **"Trade secret" defined** (§ 47-25-1702(4)): information that
  derives independent economic value from not being generally
  known and is the subject of reasonable efforts to maintain
  secrecy.
- **Misappropriation** (§ 47-25-1702(2)): acquisition by
  improper means, or disclosure / use without consent by one
  who knew or had reason to know the trade secret was acquired
  by improper means / under duty of secrecy.
- **Injunctive relief** (§ 47-25-1703): actual or threatened
  misappropriation may be enjoined.
- **Damages** (§ 47-25-1704): actual loss + unjust enrichment;
  if neither is provable, a **reasonable royalty**. Willful and
  malicious misappropriation supports **exemplary damages of up
  to twice the compensatory award**.
- **Attorney's fees** (§ 47-25-1705): the court may award fees
  to the **prevailing party** if (a) bad-faith claim of
  misappropriation, (b) bad-faith motion to terminate an
  injunction, or (c) willful and malicious misappropriation.
- **Preemption** (§ 47-25-1708): TUTSA preempts conflicting
  state-law tort remedies for misappropriation, but leaves
  contract claims and tort claims **not based on**
  misappropriation intact.
- **SOL** (§ 47-25-1709): 3 years from discovery / reasonable-
  discovery date.

TUTSA cases often overlay **non-compete enforcement** (see
`tn-employment` for the *Udom* reasonableness framework) and
**fiduciary-duty / faithless-servant theories**.

### 3. Tennessee Uniform Voidable Transactions Act (formerly TUFTA) — § 66-3-301 et seq.

Tennessee adopted the Uniform Fraudulent Transfer Act in 2003;
the 2015 ULC amendments renamed it the **Uniform Voidable
Transactions Act**. Tennessee's current chapter is at
§ 66-3-301 et seq.

- **Actual fraud** (§ 66-3-305): transfer made with actual
  intent to hinder, delay, or defraud creditors. "Badges of
  fraud" catalog at § 66-3-305(b).
- **Constructive fraud** (§ 66-3-306): transfer made without
  receiving reasonably equivalent value while the debtor was
  insolvent or rendered insolvent.
- **Remedies** (§ 66-3-309): avoidance of the transfer;
  attachment; injunction; appointment of receiver; judgment
  against transferee for value of asset transferred.
- **SOL** (§ 66-3-310): 4 years from transfer for actual
  fraud; 4 years from transfer for constructive; **discovery
  rule** carries a 1-year extension after the transfer would
  have been reasonably discovered.

The UVTA is the principal tool for post-judgment commercial
collection where a debtor has dissipated assets to insiders.
See also `tn-post-judgment` for execution practice.

### 4. Tennessee Revised LLC Act — § 48-249-101 et seq.

Tennessee operates **two parallel LLC statutes**: the **original
1994 Act** at § 48-201-101 et seq. (governing LLCs formed before
2006) and the **Revised LLC Act** at § 48-249-101 et seq.
(governing LLCs formed on or after Jan. 1, 2006). Confirm the
governing statute by date of formation.

- **Member liability** (§ 48-249-114): members are not personally
  liable for LLC obligations; veil-piercing requires the
  *Dog House Investments* showing (Tennessee's reverse-veil and
  forward-veil framework).
- **Dissociation** (§ 48-249-503): voluntary withdrawal under
  the operating agreement; involuntary dissociation on
  enumerated grounds.
- **Judicial dissolution** (§ 48-249-616): on application of a
  member, if (a) not reasonably practicable to carry on; (b)
  members in deadlock and irreparable injury to LLC; (c)
  controlling members acting in manner illegal / oppressive /
  fraudulent. The dissolution remedy commonly drives **buy-out
  negotiations** in lieu of forced wind-up.
- **Derivative actions** (§ 48-249-801 et seq.): demand
  requirement; pleading particularity per Rule 23.06.
- **Fiduciary duties** (§ 48-249-403): duty of loyalty + duty of
  care + duty of good faith and fair dealing; the operating
  agreement may not eliminate the duty of good faith.

### 5. Tennessee Business Corporation Act — § 48-11-101 et seq.

The Tennessee BCA tracks the Model Business Corporation Act.

- **Shareholder derivative actions** (§ 48-17-401): demand on
  the board (no futility excuse since 1998 reform), 90-day
  wait, particularity per Rule 23.06; SLC review.
- **Inspection rights** (§ 48-26-102): shareholders may inspect
  books and records on 5-day written demand with proper
  purpose.
- **Judicial dissolution** (§ 48-24-301): grounds include
  director deadlock harmful to corporation; oppression /
  illegality / fraud by those in control; corporate assets
  being misapplied or wasted.
- **Appraisal rights** (§ 48-23-101 et seq.): shareholders
  dissenting from merger / share exchange / certain asset
  sales have buy-out right at fair value as of immediately
  before the corporate action.
- **Indemnification** (§ 48-18-501 et seq.): mandatory where
  director is wholly successful on the merits; permissive
  otherwise on good-faith finding.
- **Fiduciary duties**: duty of care + duty of loyalty +
  good-faith standard at § 48-18-301 (directors).

### 6. Tennessee Uniform Arbitration Act — § 29-5-301 et seq.

Tennessee's UAA largely mirrors the **Federal Arbitration Act**
(9 U.S.C. § 1 et seq.); FAA preemption applies to most
agreements involving interstate commerce.

- **Enforcement** (§ 29-5-303): written arbitration agreements
  are valid and enforceable except on contract-formation grounds.
- **Compelling arbitration** (§ 29-5-304): motion to compel;
  stay of court proceedings; severability of arbitration
  clause from main contract (Tennessee follows
  *Prima Paint*-style separability under the FAA where the
  underlying agreement involves interstate commerce).
- **Vacatur grounds** (§ 29-5-313): corruption, fraud, partiality,
  exceeding powers, refusal to hear material evidence. Manifest-
  disregard is **not** a Tennessee vacatur ground (and is no
  longer a FAA ground after *Hall Street Associates v. Mattel*,
  552 U.S. 576 (2008)).
- **Confirmation** (§ 29-5-312): judgment on the award entered
  in Chancery or Circuit. SOL on confirmation: 1 year from
  delivery of award.

## Pleading-particularity (Rule 9.02) and the *Twombly/Iqbal* / *Jarboe* overlay

- **Fraud (Rule 9.02)**: "the circumstances constituting fraud
  or mistake shall be stated with particularity." Tennessee
  reads this in line with the federal Rule 9(b). Plead the
  **time, place, contents, speaker, what was obtained or given
  up**.
- **Notice-pleading otherwise**: Tennessee remains a **notice-
  pleading** jurisdiction for most commercial claims, but the
  Tennessee Supreme Court's adoption of *Jarboe v. Landmark
  Community Newspapers*, 2014, raised the **summary-judgment
  bar** post-*Rye v. Women's Care Center of Memphis*, 477 S.W.3d
  235 (Tenn. 2015) (a Tennessee analog to *Celotex*). Discovery
  becomes the *de facto* test for whether a commercial claim
  survives.

## Equitable-remedy practice (Chancery)

| Remedy | Standard | Authority |
|---|---|---|
| **TRO** (no notice) | Immediate and irreparable injury; certified efforts to give notice or reason why not | Tenn. R. Civ. P. 65.03 |
| **Preliminary injunction** | (1) likelihood of success; (2) irreparable harm without injunction; (3) balance of equities; (4) public interest. See *Vance v. Schroering*, 1999 Tenn. App. LEXIS 84 | Tenn. R. Civ. P. 65.04 |
| **Bond** | Required unless waived for good cause; Chancery sets amount | Tenn. R. Civ. P. 65.05 |
| **Permanent injunction** | Same multi-factor with final-judgment standard | Tenn. R. Civ. P. 65.04 |
| **Attachment** | Statutory grounds (non-resident, fraudulent transfer, etc.); bond + verification | Tenn. Code Ann. § 29-6-101 et seq. |
| **Receivership** | Insolvent corp, dispute over property, dissipation risk | Tenn. R. Civ. P. 66; § 29-1-101 et seq. |
| **Specific performance** | Real estate (presumptively); unique chattels; inadequacy of damages | Common-law equity |
| **Constructive trust / accounting** | Unjust enrichment + traceable benefit + inadequate legal remedy | Common-law equity |

## Damages and remedies

| Claim | Compensatory | Punitive | Treble / liquidated | Fees |
|---|---|---|---|---|
| Breach of contract | Expectation / reliance / restitution | **Not available** (contract-only) | Liquidated if K-stipulated and reasonable | American Rule (unless K shifts) |
| Breach + fraud | Both K + fraud damages | Yes, on fraud count | — | American Rule |
| TUTSA | Actual loss + unjust enrichment; reasonable royalty as fallback | Up to **2x compensatory** on willful & malicious | — | Prevailing party on bad-faith / willful (§ 47-25-1705) |
| UVTA | Avoidance + judgment vs. transferee | — | — | Prevailing party in some constructive-fraud cases |
| TCPA (where applicable) | Actual damages | — | **Treble** on willful or knowing | Mandatory to prevailing plaintiff (§ 47-18-109) |
| Tortious interference | Lost profits + lost business expectancy | Yes, on intentional / malicious | — | American Rule |
| Securities fraud | Rescission + compensatory | Yes | — | Prevailing party (§ 48-1-122) |
| BCA derivative recovery | To corporation | — | — | Plaintiff fees on benefit-conferred theory |

## Forum strategy

| Claim | Default forum | Notes |
|---|---|---|
| Breach of commercial contract | **Chancery** (with concurrent Circuit jurisdiction); General Sessions if ≤ $25k | Chancery preferred where equitable relief is also sought |
| Trade-secret / non-compete enforcement | **Chancery** | Equity forum for TRO + injunction; verified complaint |
| LLC / corporate dissolution + derivative | **Chancery** | Equity forum; SLC review |
| TCPA (where it applies) | Chancery, Circuit, or General Sessions | Treble + mandatory fees draw makes plaintiff posture economical |
| TUFTA / UVTA | **Chancery** | Equity forum for avoidance + receivership |
| Federal diversity (out-of-state defendant + $75k) | **U.S. District Court** (E.D./M.D./W.D. Tenn.) | Removal possible; **Erie** state-substantive law applies |
| Arbitration motion to compel | Chancery or Circuit | FAA-preempted in interstate-commerce contracts |
| Davidson 20th JD business cases | Davidson Chancery Business Court | See `tn-davidson` |

## Drafting checklist

- [ ] Identify the **operative contract** and its **forum-selection**
      and **arbitration** clauses before drafting; arbitration
      first.
- [ ] Confirm the **6-year written-contract SOL** at § 28-3-109 or
      the **4-year UCC § 47-2-725** clock; for tort overlays use
      the 3-year § 28-3-105 clock.
- [ ] Plead **fraud with Rule 9.02 particularity** — time, place,
      contents, speaker, what was obtained.
- [ ] Do **not plead TCPA** in a pure B2B commercial dispute
      without a non-frivolous *Pursell* workaround.
- [ ] For trade-secret claims: identify the trade secret with
      sufficient specificity to plead but not so broadly as to
      destroy secrecy; consider a **sealed protective order**
      for the trade-secret description.
- [ ] For TRO / preliminary injunction: verified complaint +
      Rule 65.03 / 65.04 motion + bond + supporting declarations
      establishing **irreparable harm** (money damages
      inadequate).
- [ ] For UVTA: plead **badges of fraud** with particularity (Rule
      9.02 standard frequently applied to fraudulent-transfer
      claims).
- [ ] For LLC / corporate derivative: comply with the **demand
      requirement** under § 48-17-401 / § 48-249-801; plead
      demand-made or demand-excused with particularity per
      Rule 23.06.
- [ ] For dissolution: consider whether **buy-out negotiation**
      is preferable to forced wind-up; the dissolution petition
      is often a settlement lever.
- [ ] For arbitration motion to compel: identify FAA vs. UAA
      governing law; severability of the arbitration clause;
      delegation clauses.

## Composition

- For statewide format and caption: `tn-statewide-format`
- For Chancery venue mechanics (Davidson Business Court): `tn-davidson`,
  `tn-shelby`, `tn-knox`, `tn-hamilton`, or `tn-county-courts`
- For limited-jurisdiction commercial claims ≤ $25k: `tn-general-sessions`
- For first responsive pleading: `tn-first-30-days`
- For drafting motions / declarations / orders: `tn-draft-motion`,
  `tn-draft-declaration`, `tn-draft-order`
- For SOL/limitations arithmetic: `tn-deadlines`
- For TCPA / collection-agency-licensing parallel: `tn-consumer-debt`
- For non-compete / fiduciary duty / TUTSA overlap with employment:
  `tn-employment`
- For post-judgment commercial collection: `tn-post-judgment`

## References

- `tn-law-references` — Tenn. Code Ann., Tenn. R. Civ. P., Tenn.
  R. Evid., federal-debt-laws + ucc-model symlinks
- Tenn. Code Ann. Title 47 (UCC + Consumer Protection + Trade Secrets)
- Tenn. Code Ann. Title 48 (Corporations + LLCs + Securities)
- Tenn. Code Ann. Title 66 ch. 3 (UVTA / TUFTA)
- Tenn. Code Ann. Title 29 ch. 5 (Uniform Arbitration Act)
- Tenn. Code Ann. Title 29 ch. 1 / Title 29 ch. 6 (Equitable
  proceedings; attachment)
- *Pursell v. First American National Bank*, 937 S.W.2d 838
  (Tenn. 1996) — TCPA B2B exclusion
- *Rye v. Women's Care Center of Memphis, MPLLC*, 477 S.W.3d 235
  (Tenn. 2015) — summary-judgment standard
- *Murfreesboro Medical Clinic, P.A. v. Udom*, 166 S.W.3d 674
  (Tenn. 2005) — non-compete reasonableness
- *Hall Street Associates v. Mattel*, 552 U.S. 576 (2008) —
  FAA vacatur grounds (impacts UAA practice)
- Davidson Chancery Business Court rules — see `tn-davidson`
  + the local-rules pointer at `tn-law-references/references/
  court-rules/Tenn-Local-Rules-Practice.md`
