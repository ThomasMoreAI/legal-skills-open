---
name: id-consumer-debt-codearranger
title: Idaho Consumer-Debt Defense
description: 'Use when defending an Idaho consumer against a debt-collection lawsuit (typically by a debt buyer or collection agency, in the Magistrate Division or District Court). Triggers: "sued by a debt collector in Idaho", "debt buyer Bonneville County", "Idaho statute of limitations on credit card debt", "time-barred debt Idaho", "Idaho Collection Agency Act license", "answer a collection complaint Idaho", "Idaho Consumer Protection Act", "FDCPA Idaho", "chain of title Idaho debt", "wage garnishment exemption Idaho". Subject-matter bundle covering the federal FDCPA / Regulation F / FCRA layer, the Idaho Consumer Protection Act, Idaho Collection Agency Act licensing (Department of Finance), the Idaho Credit Code, the statute-of-limitations framework, chain-of-title / standing and debt-buyer evidence foundation, discovery targeting the chain of title, post-judgment exemptions and garnishment, and the two-way I.C. § 12-120 attorney-fee exposure.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
---

# Idaho Consumer-Debt Defense

> **NOT LEGAL ADVICE.** This subject-matter bundle describes a procedural and substantive framework
> for Idaho consumer-debt cases, not legal advice and not strategic advice for any specific case.
> Outcomes are fact-specific; the choice of defenses, claims, motions, and discovery belongs to the
> litigant (and any counsel the litigant retains). Statute numbers, dollar thresholds, and day counts
> change — verify every citation against the current Idaho Code (legislature.idaho.gov), the Idaho
> Rules of Civil Procedure, and the Idaho Rules of Evidence before filing, and consult a licensed
> Idaho attorney.

Use this bundle when an Idaho consumer has been sued by a **debt collector** — typically a **debt
buyer** (Midland Credit Management, Portfolio Recovery Associates, LVNV Funding, Cavalry SPV,
Jefferson Capital, etc.) or a **collection agency** acting for an original creditor. See "Forum"
below for whether the suit belongs in the **Magistrate Division** or **District Court**.

## The Idaho consumer-debt landscape

Idaho layers a federal regime over an Idaho-specific one.

**Federal layer.** **FDCPA**, 15 U.S.C. §§ 1692–1692p — the workhorse for debt-buyer defense and
counterclaims; reaches **third-party** collectors and debt buyers, generally **not** original
creditors. **Regulation F**, 12 C.F.R. pt. 1006 — the CFPB rule implementing the FDCPA (eff. Nov. 30,
2021; call-frequency, validation-notice content, time/place rules). **FCRA**, 15 U.S.C. § 1681 et
seq. — credit-reporting accuracy, dispute, and the § 1681c-2 (§ 605B) identity-theft block. The
verbatim federal text lives in the shared corpus; cross-reference
`../id-law-references/references/federal-debt-laws/` rather than duplicating it here.

**Idaho layer.** **Idaho Consumer Protection Act (ICPA)** — I.C. § 48-601 et seq. (unfair/deceptive
acts in trade or commerce; private right of action, § 48-608). **Idaho Collection Agency Act** —
I.C. § 26-2222 et seq. (licensing, administered by the **Idaho Department of Finance**;
§ 26-2223 requires a license, and **subsection (6) reaches debt buyers**). **Idaho Credit Code**
(Idaho's UCCC) — I.C. Title 28, ch. 41–46 (§ 28-41-101). **Statutes of limitation** — I.C.
§§ 5-215 to 5-222. **Attorney fees in a contract / commercial-transaction collection case** — I.C.
§ 12-120 (two-way); frivolous-defense fees — I.C. § 12-121.

## The Idaho Consumer Protection Act (ICPA) — reaching abusive collection conduct

The **ICPA**, I.C. § 48-601 et seq., prohibits **unfair or deceptive acts or practices in the
conduct of any trade or commerce**. It carries a **private right of action** under **I.C. § 48-608**
for any person who suffers an ascertainable loss as a result of a prohibited method, act, or
practice.

- **Reaching collection conduct.** A collector that misrepresents the amount, character, or legal
  status of a debt; threatens action it cannot or will not take; or sues on a time-barred debt may
  commit an unfair or deceptive act actionable under the ICPA. Map each misrepresentation to a
  specific factual element (the false statement, materiality, ascertainable loss). The ICPA is the
  Idaho vehicle for the deceptive-practices theory the FDCPA also supplies federally.
- **Remedies / fees.** § 48-608 supplies the private-action remedies (actual damages and the
  statute's specified relief; the section also addresses fees and, in some circumstances, multiplied
  or minimum recovery). **Verify the current remedies and fee framework** against I.C. § 48-608
  before relying on it — the remedial structure is its own and is drift-prone. Do not assume
  FDCPA-style statutory damages.
- **Enforcement.** The **Idaho Attorney General's Consumer Protection Division** enforces the ICPA
  publicly; a consumer's private § 48-608 claim is separate from any AG action.

## Idaho Collection Agency Act — I.C. § 26-2222 et seq. (Department of Finance) — KEY DEFENSE ANGLE

Idaho **licenses collection agencies** under the **Idaho Collection Agency Act**, I.C. § 26-2222 et
seq., administered by the **Idaho Department of Finance** (finance.idaho.gov). **I.C. § 26-2223
requires a license** to engage in the collection-agency business in Idaho.

- **Debt buyers are covered.** § 26-2223 reaches, among others, one who collects an **indebtedness
  ... acquired from another person** that **"was either delinquent or in default at the time it was
  acquired"** — the **subsection (6)** debt-buyer hook. A debt buyer that purchased the consumer's
  charged-off account (delinquent/in-default when acquired) is therefore generally required to be
  **licensed** in Idaho to collect on it.
- **Check the license first.** Look up the plaintiff (and any servicer) with the **Idaho Department
  of Finance** before responding. An out-of-state debt buyer suing in Idaho without an Idaho license
  is a recurring pattern, and **capacity / standing-to-collect and licensure are litigable** — raise
  the plaintiff's license status in discovery (an RFA and an interrogatory) and as an affirmative
  defense.
- **Licensing as a pressure point — verify the consequence.** Operating **unlicensed** violates the
  Act. Whether the lack of a license **strips the plaintiff of capacity / standing to sue**, bars
  the recovery, or merely supplies a regulatory violation is **not automatic** — verify current Idaho
  authority via case-law research / CourtListener before arguing the suit or any resulting judgment
  is void. Treat lack of license as a **strong capacity/standing challenge and settlement lever**,
  pleaded with the verification caveat.

## Idaho Credit Code (Idaho's UCCC) — I.C. Title 28, ch. 41–46

The **Idaho Credit Code**, I.C. Title 28, chapters 41–46 (scope at **I.C. § 28-41-101**), is Idaho's
enactment of the Uniform Consumer Credit Code. It governs consumer-credit transactions, finance
charges, and related disclosures and remedies. Where the suit concerns a regulated consumer-credit
transaction, the Credit Code can bear on the **lawful amount** of the claim (permitted charges,
finance-charge limits) and on remedies — use it to test whether the balance sued upon includes
unauthorized charges. Pull the current article text from
`../id-law-references/references/id-statutes-debt/` and verify the applicable provisions.

## Statutes of limitation on the debt (DEFENSE)

The limitations bar is the single most powerful defense in stale-debt cases. The headline framework
— pull the authoritative, current text from `../id-law-references/references/id-statutes-debt/`:

| Claim | SOL | Citation |
|---|---|---|
| **Action on a written contract** | **5 years** | I.C. § 5-216 |
| **Oral contract / open account / unwritten contract** | **4 years** | I.C. § 5-217 |
| **Action upon a judgment** | **11 years** | I.C. § 5-215 |

- **Accrual on an open / mutual account.** I.C. § 5-222 fixes accrual on a mutual, open, and current
  account from the **time of the last item** proved in the account — pin the date of the last
  charge or payment that the plaintiff can actually prove.
- **Written contract vs. open account is litigable.** Whether a credit-card or revolving account is
  characterized as a **written contract** (5-year, § 5-216) or an **open account** (4-year, § 5-217)
  controls the cutoff and is contested in Idaho debt-buyer practice. **Do not assume a
  characterization — verify the current rule via case-law research** (CourtListener / Legal Data
  Hunter) before pleading the period, and pin the account documents (was there a signed agreement?).
- **Judgments.** An action **upon a judgment** runs **11 years** (I.C. § 5-215); a judgment lien's
  renewal mechanics are in **I.C. § 10-1111** — relevant when defending renewal or post-judgment
  enforcement of a stale judgment.
- **SOL is an affirmative defense** that must be **pleaded** in the answer or it is waived — raise it
  expressly. Once the account dates are fixed, a time-barred debt is also a strong **summary-judgment**
  ground.

## Chain of title / standing

A debt buyer must trace ownership from the original creditor through every intermediate buyer to
itself, with a **Bill of Sale** for each transfer, an **Assignment** specifically identifying **this**
account (account number), and **account-level data** matching this consumer's account. A bill of sale
referencing "an attached portfolio" without the attachment, or "all accounts sold on [date]" without
tying to **this** account, is **insufficient**. Standing turns on whether the plaintiff can prove it
owns this specific account.

- **Account-stated theory and the fee hook.** Plaintiffs often plead **account stated** to sidestep
  proof of the underlying agreement. Test whether there was any **agreed accounting** between **this**
  plaintiff and **this** defendant. Note the attorney-fee exposure: a successful party in a contract /
  commercial-transaction action may seek fees under **I.C. § 12-120** (see below) — account-stated
  pleading carries that fee hook, so defeating the underlying claim matters to fee exposure too.
- **Authentication.** Documents offered to prove the assignment and the account must be properly
  **authenticated** — the assignment, the bill of sale, and the account records each need a competent
  foundation (see the evidence section).

## Debt-buyer evidence foundation — I.R.E. 803(6) / 902(11)

To admit the account records and the assignment, the plaintiff must lay a foundation under **I.R.E.
803(6)** (records of a regularly conducted activity / business-records exception, via a custodian or
qualified witness) and may rely on **I.R.E. 902(11)** (self-authenticating **certified** business
records in lieu of a live custodian — which requires **pre-trial written notice** to the adverse
party and an opportunity to inspect).

- **The classic defense is challenging the affidavit / foundation.** The debt buyer's affiant
  typically has **no personal knowledge** of the **original creditor's** record-keeping and cannot
  lay an 803(6) foundation for **another entity's** records. Probe the affiant's basis of knowledge:
  did the affiant work for the original creditor? How are the assignor's records integrated into the
  buyer's system? Does the certification satisfy 902(11), and was the **pre-trial notice** given?
- An affidavit that recites conclusions ("the records are true and correct") without establishing the
  custodian's knowledge of how the **assignor's** records were made and kept is vulnerable on
  objection and on summary judgment.

## Discovery targeting chain of title

Idaho **allows interrogatories** (unlike some collection-defense regimes). Build the record before
trial or summary judgment:

- **Interrogatories — I.R.C.P. 33.** Cap of **40** interrogatories including discrete subparts. Use
  them on chain of title, the identity and basis of knowledge of the records custodian/affiant, the
  computation of the balance, and the plaintiff's Idaho Department of Finance license status.
- **Requests for Production — I.R.C.P. 34.** Demand the bills of sale and account-specific
  assignments tying **this** account to the plaintiff, the original cardholder/credit agreement,
  periodic statements, the charge-off statement, and the electronic account data.
- **Requests for Admission — I.R.C.P. 36.** Pin down elements — e.g., that the plaintiff lacks an
  account-specific assignment, that no signed agreement exists, that the plaintiff held no Idaho
  collection-agency license on the relevant dates. Unanswered RFAs are **deemed admitted**.
- **Timing and motion practice.** Responses are due in **30 days**; if responses are deficient,
  **meet-and-confer** and move to compel under **I.R.C.P. 37**.

See `id-discovery` for the full mechanics, response computation, and motion-to-compel practice.

## Post-judgment — exemptions and garnishment

If a judgment enters, exemptions and garnishment limits protect the consumer. Point dollar **amounts**
to `../id-law-references/references/id-statutes-debt/` and **verify current figures** — these are
drift-prone:

- **Wage-garnishment exemption — I.C. § 11-207.** Limits a wage garnishment to the lesser of **25%
  of disposable weekly earnings** or the amount by which disposable weekly earnings exceed **30× the
  federal minimum wage** — verify current figures.
- **Continuing garnishment — Title 11, ch. 7 (I.C. § 11-712).** Idaho's continuing wage-garnishment
  mechanism — confirm the duration and renewal mechanics.
- **Personal-property exemptions — I.C. § 11-605.** Exempts categorized personal property up to
  specified dollar amounts — verify current figures.
- **Homestead — I.C. § 55-1003.** Idaho homestead exemption; the dollar amount changes — **verify the
  current figure** before relying on it.

See `id-post-judgment` for claiming exemptions, contesting garnishment, and setting aside a default
judgment.

## Attorney fees — I.C. § 12-120 cuts both ways; § 12-121 for frivolousness

In a **commercial transaction** or **contract** collection action, **I.C. § 12-120** (notably
**§ 12-120(3)**, commercial transactions) provides that the **prevailing party** is entitled to
reasonable attorney fees. This is a **two-way** exposure and a critical risk consideration:

- A consumer who **defeats** the suit (e.g., wins on SOL, no chain of title, or lack of capacity to
  sue) may seek fees as the prevailing party under § 12-120.
- But a consumer who **loses** — including by failing to appear and suffering a **default judgment** —
  may be ordered to pay the **creditor's** reasonable fees on top of the debt and costs. **Never
  ignore a complaint** — default exposes the consumer to fees.
- **Frivolous-defense fees — I.C. § 12-121.** A court **may** award fees where a claim or **defense**
  was pursued frivolously, unreasonably, or without foundation — so plead defenses with a good-faith
  basis. **Verify the current statute and fee standard** before advising on exposure.

## Forum — Magistrate Division vs. District Court

Idaho's trial courts are unified, but collection suits are heard in different layers by amount:

- **Magistrate Division.** Collection suits **≤ $5,000** are heard in the Magistrate Division
  (general magistrate civil cap **$5,000**, **I.C. § 1-2208**; **Small Claims** jurisdiction up to
  **$5,000**, **I.C. § 1-2301**). Small-claims practice is simplified.
- **District Court.** Suits **> $5,000** are heard in District Court.
- **Districts by county.** **Ada County** sits in the **4th Judicial District**; **Bonneville
  County** sits in the **7th Judicial District**. See the venue / county skills for the specific
  court mechanics.

**Answer deadline.** A defendant must serve an answer within **21 days** after service of the
summons and complaint (**I.R.C.P. 12(a)(1)(A)**). Time is computed under **I.R.C.P. 2.2** (note Rule 6
is **RESERVED** in Idaho), with **+3 days** added when a paper is served by mail. Miss the deadline
and the plaintiff can take a **default** and then a **default judgment** (with § 12-120 fee exposure).
See `id-first-30-days` for the answer and `id-deadlines` for time computation.

## The five fact patterns

**Pattern 1 — Debt buyer with no chain of title.** Demand the bills of sale and account-specific
assignments tying **this** account to the plaintiff (RFP, I.R.C.P. 34); challenge the affiant's
I.R.E. 803(6)/902(11) basis of knowledge; verify the plaintiff's Idaho Department of Finance
collection-agency license (I.C. § 26-2223). Plead lack of standing / failure to prove assignment.

**Pattern 2 — Time-barred debt (SOL).** Pin the date of the **last item** on the account (I.C.
§ 5-222) or the last payment/charge the plaintiff can prove. Compare against the applicable period —
**written contract 5 years** (I.C. § 5-216) or **oral / open account 4 years** (I.C. § 5-217),
characterization litigable — and against the **11-year** judgment period (I.C. § 5-215) if the suit
is on a judgment. Plead SOL as an affirmative defense and consider summary judgment once dates are
fixed. **Verify the open-account vs. written-contract characterization via case-law research.**

**Pattern 3 — FDCPA / Regulation F validation or dispute violation.** Consumer disputed or never
received a compliant validation notice. FDCPA §§ 1692g (validation), 1692e (false/misleading), 1692f
(unfair); Reg F validation-notice content (12 C.F.R. pt. 1006). Pair with an **ICPA** unfair/deceptive
-practice theory (I.C. § 48-601 et seq.; private action § 48-608). Federal text:
`../id-law-references/references/federal-debt-laws/`.

**Pattern 4 — Wrong amount / wrong person.** Inflated balance (unauthorized fees/interest — test
against the **Idaho Credit Code**, I.C. § 28-41-101 et seq.) or mistaken identity / identity theft.
**FDCPA** §§ 1692e(2)/1692f(1) (misrepresenting / collecting amounts not owed); **ICPA** § 48-601 et
seq. (deceptive statement of the debt's amount or status); **FCRA** § 605B identity-theft block if
applicable (shared `federal-debt-laws/` corpus).

**Pattern 5 — Unlicensed collector / debt buyer.** Plaintiff or servicer holds no Idaho collection-
agency license. **Idaho Collection Agency Act**, I.C. § 26-2222 et seq.; **§ 26-2223** (license
required, with the **subsection (6)** debt-buyer hook for debt acquired delinquent/in default).
Raise as a **capacity / standing-to-collect** challenge and a settlement lever, verifying the
current consequence via case-law research before arguing the suit or judgment is void. Pair with
**ICPA / FDCPA** theories.

## Affirmative-defenses catalog

Plead all that apply in the answer (defenses not pleaded may be waived):

1. **Statute of limitations** — written contract 5 years (I.C. § 5-216) or oral / open account 4
   years (I.C. § 5-217), accrual on an open account from the last item (I.C. § 5-222); 11-year
   period for an action on a judgment (I.C. § 5-215). Summary-judgment ground.
2. **Lack of standing / failure to prove assignment** — plaintiff cannot prove it owns this account.
3. **Lack of capacity to sue** — unlicensed collection agency / debt buyer (Idaho Collection Agency
   Act, I.C. § 26-2222 et seq.; § 26-2223(6)); assert with the verification caveat.
4. **Failure to state a claim** — no chain of title or specific account terms.
5. **Lack of / failure of consideration.**
6. **Payment / accord and satisfaction / release / settlement.**
7. **Account stated** — no agreed accounting between this plaintiff and this defendant.
8. **Unauthorized charges** — balance includes charges not permitted under the Idaho Credit Code.
9. **Identity theft** (if applicable) — FCRA § 605B block.
10. **Discharge in bankruptcy** (if applicable).
11. **ICPA / FDCPA violation** (raised as a counterclaim; also a defense theme).

## Synthetic example outline (outline only — not a full filing)

A typical first response when sued by a debt buyer on a stale credit-card account:

1. **Answer with affirmative defenses** (`id-first-30-days`, `id-draft-motion`):
   - General denial of the unproven allegations (amount owed, ownership, account stated).
   - Affirmative defenses: SOL; lack of standing / failure to prove assignment; lack of capacity to
     sue (unlicensed under I.C. § 26-2223); account stated denied; failure to state a claim.
   - Caption and format per `id-statewide-format`; "Answer," "Memorandum," "Affidavit"/"Declaration"
     conventions.
2. **SOL defense developed** (`id-deadlines`, `id-fact-check`):
   - Pin the last item / last payment date (I.C. § 5-222); compute against I.C. § 5-216 / § 5-217;
     verify the open-account vs. written-contract characterization via case-law research.
   - If the suit is time-barred on the face of the dates, tee up a summary-judgment motion once
     discovery fixes the dates.
3. **Meet-and-confer / discovery letter** targeting chain of title (`id-discovery`):
   - RFP (I.R.C.P. 34) for bills of sale, account-specific assignment, original agreement,
     statements; interrogatories (I.R.C.P. 33) on the affiant's basis of knowledge and the license;
     RFA (I.R.C.P. 36) deeming key facts admitted; 30-day responses; motion to compel under
     I.R.C.P. 37 if deficient.

Draft each component with the sibling skills below; verify every citation with `id-fact-check`.

## Composition

- Statewide format baseline: `id-statewide-format`.
- Answer / first response: `id-first-30-days`, `id-draft-motion`. Declaration / affidavit:
  `id-draft-declaration`.
- Discovery / motion-to-compel: `id-discovery`. Exemptions / garnishment / set-aside:
  `id-post-judgment`.
- Deadlines / time computation: `id-deadlines`. Citation verification: `id-fact-check`.
- Reference corpora (Idaho statutes, court rules, and the symlinked federal text): `id-law-references`.
