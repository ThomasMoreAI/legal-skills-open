---
name: mi-consumer-debt-codearranger
title: Michigan Consumer-Debt Defense
description: Use when defending a Michigan consumer against a debt-collection lawsuit. Triggers include "sued for a debt Michigan", "debt buyer Michigan", "FDCPA Michigan", "MCL 445.251" RCPA, "MCL 339.901" collection agency license, "time-barred debt Michigan", "chain of title Michigan debt". Covers federal FDCPA, Regulation F, FCRA; Michigan Regulation of Collection Practices Act (MCL 445.251); collection-agency licensing (MCL 339.901); Michigan Consumer Protection Act (MCL 445.901) with regulated-conduct exemption; chain-of-title under Michigan UCC Article 9; statutes of limitations (MCL 600.5807); and the District Court forum. Includes five fact-pattern triage, discovery banks, and affirmative-defenses catalog.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
---

# Michigan Consumer-Debt Defense

> **NOT LEGAL ADVICE.** This subject-matter bundle describes a procedural and substantive framework
> for Michigan consumer-debt cases, not legal advice and not strategic advice for any specific case.
> Outcomes are fact-specific; the choice of defenses, claims, motions, and discovery belongs to the
> litigant (and any counsel the litigant retains). Statute numbers, dollar thresholds, and day counts
> change — verify every citation against the current Michigan Compiled Laws (legislature.mi.gov) and
> the Michigan Court Rules before filing, and consult a licensed Michigan attorney.

Use this bundle when a Michigan consumer has been sued by a **debt collector** — typically a **debt
buyer** (Midland Credit Management, Portfolio Recovery Associates, LVNV Funding, Jefferson Capital,
Cavalry SPV, etc.) or a **collection agency** acting for an original creditor. The dominant forum is
the **District Court**; see "Forum" below.

## The Michigan consumer-debt landscape

Michigan layers a federal regime over a Michigan-specific one. A distinctive feature: Michigan has
**two** state collection statutes that reach collectors differently — the **Regulation of Collection
Practices Act (RCPA)**, MCL 445.251 et seq., whose prohibited-acts section (MCL 445.252) binds a
**"regulated person"** (defined at MCL 445.251(1)(g) to include first-party collectors such as an
employee collecting for one employer in the employer's name, and chartered banks / savings-and-loans /
credit unions collecting their own claims), making it **broader than the FDCPA** in that respect; and
the **Occupational Code, Article 9**, MCL 339.901 et seq., which **licenses third-party collection
agencies and debt buyers** through LARA and supplies the prohibited-practices / civil-liability rules
for licensees.

**Federal layer.** **FDCPA**, 15 U.S.C. §§ 1692-1692p — the workhorse for debt-buyer defense and
counterclaims; reaches **third-party** collectors and debt buyers, generally **not** original
creditors. **Regulation F**, 12 C.F.R. pt. 1006 — CFPB rule implementing the FDCPA (eff. Nov. 30,
2021; call-frequency, validation-notice, time/place rules). **FCRA**, 15 U.S.C. §§ 1681 et seq. —
furnisher / re-aging / dispute issues. Federal text lives in the shared corpus; cross-reference
`../mi-law-references/references/federal-debt-laws/` (symlinked into `claude-legal-federal-laws`).

**Michigan layer.** **RCPA** — MCL 445.251 to 445.258 (prohibited practices § 445.252; damages
§ 445.257). **Occupational Code Article 9** — MCL 339.901 et seq. (collection-agency definition,
LARA licensure). **MCPA** — MCL 445.901 et seq., with the regulated-conduct exemption at MCL 445.904.
**Michigan UCC Article 9** — MCL 440.9101 et seq. (assignments / chain of title).

## The RCPA — Michigan's broad first-party reach

The **RCPA** (MCL 445.251 et seq.) is the Michigan analog to the FDCPA, but its prohibited-acts
section (MCL 445.252) binds a **"regulated person"** — defined at MCL 445.251(1)(g) as a person whose
collection activities are confined and directly related to operating a business other than a
collection agency, including a regular employee who collects for one employer in the employer's name,
and state/federally chartered banks, savings-and-loans, and credit unions that collect their **own**
claims. Because "regulated person" thus reaches first-party / in-house collectors, the RCPA can apply
where the FDCPA generally does **not**. (Third-party collection agencies and debt buyers are instead
governed by the Occupational Code Article 9 prohibited-practices rules — see below.)

- **Prohibited practices** — MCL 445.252 enumerates communicating in a misleading or deceptive
  manner, simulating judicial process, misrepresenting the legal status/rights/consequences of a
  debt, harassing or abusive collection methods (with the 8 a.m.–9 p.m. call-time rule), and the like.
  Map the collector's conduct to the specific subsection.
- **Civil liability** — MCL 445.257: an injured person "may bring an action for damages or other
  equitable relief" and recover **actual damages or $50.00, whichever is greater**. For a **willful**
  violation the court may assess a civil fine of **not less than 3 times the actual damages, or
  $150.00, whichever is greater**, and **shall award reasonable attorney's fees and court costs** to a
  prevailing petitioner. (Verify the current figures and the willfulness standard.)

The treble-plus-mandatory-fees structure makes a well-founded RCPA counterclaim a real settlement
lever. The Occupational Code (below) is the parallel regime for *licensed third-party* collectors;
the two overlap and one course of conduct can implicate both — identify which actor is which.

## Occupational Code Article 9 — the licensing defense

**MCL 339.901 et seq.** licenses **collection agencies** (defined at MCL 339.901 to include a person
"directly engaged in collecting or attempting to collect a claim owed or due or asserted to be owed
or due another," and persons furnishing collection forms/systems). A **debt buyer** collecting on
purchased accounts is generally acting as a collection agency for licensing purposes — confirm
against the current definition.

- **Licensure through LARA** — a third-party collection agency / debt buyer must hold a Michigan
  collection-agency license. Check the LARA licensee lookup for the plaintiff and its servicer.
- **Licensing as a defense / pressure point** — an **unlicensed** collector or debt buyer violates
  Article 9. Whether that **voids** the debt or only exposes the collector to penalties / an
  unfair-practice theory is **not automatic** — verify current case law before arguing the plaintiff
  lacks capacity to sue or the judgment is void. Treat lack of license as evidence of an unfair
  practice and a settlement lever, not a guaranteed merits defense.

## The MCPA and its narrowed scope — read before pleading

The **MCPA** (MCL 445.901 et seq.) offers broad remedies on paper, but the Michigan Supreme Court has
sharply **narrowed** its reach through the **regulated-conduct exemption** at **MCL 445.904(1)(a)**,
which exempts "[a] transaction or conduct specifically authorized under laws administered by a
regulatory board or officer acting under statutory authority of this state or the United States."

- In ***Smith v Globe Life Insurance Co***, 460 Mich 446 (1999), and ***Liss v Lewiston-Richards,
  Inc***, 478 Mich 203 (2007), the Court read the exemption to ask whether the **general transaction**
  is authorized/regulated — not whether the specific misconduct is — exempting large swaths of
  **licensed/regulated lending and financial-services conduct** from the MCPA.
- **Takeaway:** the MCPA often does **NOT** reach collection on a **licensed/regulated** loan or
  credit product. Do **not** reflexively plead an MCPA claim for ordinary collection on regulated
  credit — it is vulnerable to dismissal under the exemption. The **FDCPA**, the **RCPA** (MCL
  445.252), and the **Occupational Code** prohibited-practices rules are the right vehicles for
  collection-conduct claims. Verify there is no intervening authority before any categorical
  statement.

## Statutes of limitations on the debt

Point to the corpus (`references/mi-statutes-of-limitations.md` and the `mi-statutes-debt` corpus) for
the authoritative, current counts — these are drift-prone. The headline rules:

| Claim | SOL | Citation |
|---|---|---|
| **Breach of written/general contract** (most credit-card debt) | **6 years** | MCL 600.5807(9) |
| **Sale of goods (UCC Article 2)** | **4 years** | MCL 440.2725 |

- MCL 600.5807(9) supplies the **6-year** default for breach of contract not otherwise specified,
  capturing **most credit-card and open-account debt**; the clock generally runs from breach / **date
  of last payment or activity** (fact-dependent — pin down the account history).
- The **4-year** UCC period (MCL 440.2725) governs the **sale of goods** and can **displace** the
  contract period where the obligation is for goods.
- **SOL is an affirmative defense** that must be **pleaded** (MCR 2.111(F)) or it is waived — raise it
  expressly in the answer. It is also a **summary-disposition ground** under **MCR 2.116(C)(7)**; a
  time-barred debt is a strong (C)(7) motion candidate.

## Chain of title / standing — Michigan UCC Article 9

A debt buyer must trace ownership from the original creditor through every intermediate buyer to
itself under **Michigan UCC Article 9** (MCL 440.9101 et seq.), with a **Bill of Sale** for each
transfer, an **Assignment** specifically identifying **this** account (account number), and
**account-level data** matching this consumer's account. A bill of sale referencing "an attached
portfolio" without the attachment, or "all accounts sold on [date]" without tying to **this** account,
is **insufficient**. Standing turns on whether the plaintiff can prove it owns this specific account.

**Business-records foundation.** To admit the account records and the assignment, the plaintiff must
lay a foundation under **MRE 803(6)** (records of a regularly conducted activity, via a custodian or
qualified witness) and **MRE 902(11)** (self-authenticating certified business records, in lieu of a
live custodian). Recurring theme: the debt buyer's affiant has **no personal knowledge** of the
*original creditor's* record-keeping and cannot lay an 803(6) foundation for another entity's records.
Probe the affiant's basis of knowledge.

## Forum — most consumer-debt suits are in District Court

Most Michigan consumer-debt suits are filed in the **District Court**, a court of limited civil
jurisdiction (claims up to the statutory district-court cap — verify the current figure). The largest
is the **36th District Court** (Detroit). The **answer clock** runs under **MCR 2.108** (the period
depends on the manner of service — confirm the current days); miss it and the plaintiff can take a
default. **Default and default judgment** are governed by **MCR 2.603** — to set aside a default
(other than for lack of jurisdiction) the defendant generally must show **good cause** *and* file an
affidavit showing a **meritorious defense** (SOL, no chain of title, FDCPA/RCPA violation), within the
rule's time limit. See `mi-36th-district` / `mi-district-courts`, `mi-first-30-days`, and
`mi-post-judgment`.

## The five fact patterns

**Pattern 1 — Debt buyer with no chain of title.** Demand the Article 9 bills of sale and
account-specific assignments tying **this** account to the plaintiff (MCL 440.9101 et seq.); challenge
the affiant's MRE 803(6)/902(11) basis of knowledge; confirm the buyer holds a LARA collection-agency
license (MCL 339.901 et seq.).

**Pattern 2 — Time-barred debt.** Last payment 6-7+ years ago; credit-card debt is on or past the
**6-year** MCL 600.5807(9) line (or 4-year UCC line, MCL 440.2725). Pin the date of last activity;
plead SOL (MCR 2.111(F)) and move under **MCR 2.116(C)(7)**.

**Pattern 3 — FDCPA validation / dispute violation.** Consumer disputed or never got a compliant
validation notice. FDCPA §§ 1692g (validation), 1692e (false/misleading), 1692f (unfair); Reg F
validation content (12 C.F.R. pt. 1006). Parallel **RCPA** claim (MCL 445.252) reaches a "regulated
person" (incl. first-party / in-house collectors) the FDCPA may not.

**Pattern 4 — Wrong amount / wrong person.** Inflated amount (unauthorized fees/interest) or mistaken
identity / identity theft. **RCPA** (MCL 445.252(e)-(f)) bars inaccurate/misleading/deceptive
statements in a collection communication and misrepresenting a debt's legal status or the parties'
legal rights; **FDCPA** §§ 1692e(2)/1692f(1) (which expressly bar misrepresenting the amount and
collecting amounts not owed); **FCRA** § 605B identity-theft block if applicable.

**Pattern 5 — Unlicensed collector / debt buyer.** Plaintiff or servicer holds no Michigan
collection-agency license. **Occupational Code Article 9** (MCL 339.901 et seq.) — operating without a
license violates the Act; use as evidence of an unfair practice / settlement lever, verifying current
case law before arguing the suit or judgment is void. Pair with **RCPA / FDCPA** theories.

## Affirmative-defenses catalog

Plead all that apply in the answer (MCR 2.111(F) — defenses not pleaded are waived):

1. **Statute of limitations** — 6 years on contract (MCL 600.5807(9)) or 4 years on goods (MCL
   440.2725); summary-disposition ground under MCR 2.116(C)(7).
2. **Lack of standing / failure to prove assignment** — plaintiff cannot prove it owns this account
   (UCC Article 9).
3. **Failure to state a claim** — no chain of title or specific account terms (MCR 2.116(C)(8)).
4. **Lack of / failure of consideration.**
5. **Payment / accord and satisfaction / release / settlement** (MCR 2.116(C)(7)).
6. **Account stated** — no agreed accounting between this plaintiff and this defendant.
7. **Lack of capacity to sue** — unlicensed collection agency / debt buyer (MCL 339.901 et seq.);
   assert with the verification caveat.
8. **Identity theft** (if applicable) — FCRA § 605B block.
9. **Discharge in bankruptcy** (if applicable).
10. **FDCPA / RCPA violation** (raised as a counterclaim; also a defense theme).

See `references/affirmative-defenses.md` for the annotated catalog.

## Discovery strategy

In District Court the Michigan Court Rules' discovery provisions apply (subject to any
abbreviated-discovery rules for smaller cases — verify the venue): **Requests for Admission** (MCR
2.312) on the elements; **Interrogatories** (MCR 2.309) on chain of title, custodian identity, and
account-level data; **Requests for Production** (MCR 2.310) for bills of sale, assignments, the
original agreement, periodic statements, and electronic records; then **meet-and-confer** and a
**Motion to Compel** (MCR 2.313). The full RFP / RFA / interrogatory banks live in the references; see
`mi-discovery` for mechanics.

## Composition

- Statewide format: `mi-statewide-format`. Dominant forum: `mi-36th-district`, `mi-district-courts`.
- Answer / first response: `mi-first-30-days`, `mi-draft-motion`. Declaration: `mi-draft-declaration`.
- Proposed order: `mi-draft-order`. Notice / motion: `mi-draft-note`, `mi-draft-motion`.
- Discovery / motion-to-compel: `mi-discovery`. Set-aside / garnishment: `mi-post-judgment`.
- Deadlines: `mi-deadlines`. Pro se conventions: `mi-pro-se`. QC: `mi-quality-check`, `mi-fact-check`.

## References

- `references/fdcpa.md`, `references/reg-f.md`, `references/fcra.md` — federal layer (see
  `../mi-law-references/references/federal-debt-laws/`)
- `references/mi-rcpa.md` — RCPA (MCL 445.251-.258; practices § 445.252; damages § 445.257)
- `references/mi-occupational-code-art9.md` — Occupational Code Article 9 licensing (MCL 339.901 et seq.)
- `references/mi-mcpa.md` — MCPA (MCL 445.901 et seq.) + the MCL 445.904 exemption (*Smith v Globe
  Life* / *Liss v Lewiston-Richards*)
- `references/mi-statutes-of-limitations.md` — MCL 600.5807(9) / MCL 440.2725
- `references/chain-of-title.md` — Michigan UCC Article 9 doctrine
- `references/evidence-debt-buyer.md` — MRE 803(6) / 902(11) foundation
- `references/rfp-debt-buyer.md`, `references/rfa-debt-buyer.md`,
  `references/interrogatories-debt-buyer.md` — discovery banks
- `references/affirmative-defenses.md` — annotated catalog
- `references/online-sources-consumer-debt.md` — canonical URLs
