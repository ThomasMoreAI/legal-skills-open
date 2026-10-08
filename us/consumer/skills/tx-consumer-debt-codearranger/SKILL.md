---
name: tx-consumer-debt-codearranger
title: Texas Consumer-Debt Defense
description: 'Use when defending a Texas consumer against a debt-collection lawsuit (debt buyer or collection agency, in a Justice Court debt-claim case, a County Court at Law, or a District Court). Triggers: "sued by a debt collector in Texas", "debt buyer sued me Texas", "Texas statute of limitations on credit card debt", "time-barred debt Texas", "Texas Debt Collection Act", "TDCA violation", "DTPA debt collector", "answer a debt-claim case Texas", "JP court debt claim", "sworn account Texas", "verified denial Rule 185", "surety bond debt collector Texas", "can they garnish my wages in Texas", "Monday rule answer Texas". Covers the federal FDCPA / Regulation F / FCRA layer, the Texas Debt Collection Act (Tex. Fin. Code Ch. 392; § 392.404 DTPA tie-in; § 392.101 surety bond), the DTPA (Ch. 17), limitations, sworn account (TRCP 185 / verified denial TRCP 93(10)), chain-of-title / standing and debt-buyer evidence foundation (TRE 803(6) / 902(10)), discovery, exemptions and the wage-garnishment
  bar, and CPRC Ch. 38.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
---

# Texas Consumer-Debt Defense

> **NOT LEGAL ADVICE.** This subject-matter bundle describes a procedural and substantive framework
> for Texas consumer-debt cases, not legal advice and not strategic advice for any specific case.
> Outcomes are fact-specific; the choice of defenses, claims, motions, and discovery belongs to the
> litigant (and any counsel the litigant retains). Statute numbers, dollar thresholds, jurisdictional
> ceilings, and day counts change — verify every citation against the current Texas statutes
> (Tex. Fin. Code, Tex. Bus. & Com. Code, Tex. Civ. Prac. & Rem. Code, Tex. Prop. Code), the Texas
> Rules of Civil Procedure, and the Texas Rules of Evidence before filing, and consult a licensed
> Texas attorney.

Use this bundle when a Texas consumer has been sued by a **debt collector** — typically a **debt
buyer** (Midland Credit Management, Portfolio Recovery Associates, LVNV Funding, Cavalry SPV,
Jefferson Capital, Velocity Investments, etc.) or a **collection agency** acting for an original
creditor. See "Forum" below for whether the suit belongs in a **Justice Court** (debt-claim case),
a **County Court at Law**, or a **District Court**.

## The Texas consumer-debt landscape

Texas layers a federal regime over a Texas-specific one.

**Federal layer.** **FDCPA**, 15 U.S.C. §§ 1692–1692p — the workhorse for debt-buyer defense and
counterclaims; reaches **third-party** collectors and debt buyers, generally **not** original
creditors. **Regulation F**, 12 C.F.R. pt. 1006 — the CFPB rule implementing the FDCPA
(call-frequency limits, validation-notice content, time/place rules). **FCRA**, 15 U.S.C. § 1681 et
seq. — credit-reporting accuracy, dispute, and the § 1681c-2 (§ 605B) identity-theft block. The
verbatim federal text lives in the shared corpus; cross-reference
`../tx-law-references/references/federal-debt-laws/` rather than duplicating it here.

**Texas layer.** **Texas Debt Collection Act (TDCA)** — Tex. Fin. Code Ch. 392 (prohibited
collection conduct; bonding requirement; the DTPA tie-in). **Deceptive Trade Practices–Consumer
Protection Act (DTPA)** — Tex. Bus. & Com. Code Ch. 17 (§§ 17.41–.63). **Statutes of limitation** —
Tex. Civ. Prac. & Rem. Code (CPRC) Ch. 16. **Sworn-account procedure** — Tex. R. Civ. P. 185 with
the mandatory verified denial under Tex. R. Civ. P. 93(10). **Attorney fees on a contract / sworn
account** — CPRC Ch. 38 (two-way). The **Office of Consumer Credit Commissioner (OCCC)** is the
state consumer-credit regulator; third-party debt collectors and credit bureaus file a surety bond
with the **Texas Secretary of State** under Fin. Code § 392.101.

## The Texas Debt Collection Act (TDCA) — Tex. Fin. Code Ch. 392

The **TDCA**, Tex. Fin. Code Ch. 392, regulates **debt collection** in Texas. Unlike the FDCPA, the
TDCA reaches a broader set of collectors — its definition of "debt collector" can sweep in
**creditors collecting their own consumer debts** and not only third-party collectors — so it often
supplies a Texas remedy where the FDCPA does not reach the plaintiff. Confirm the current
"debt collector" / "third-party debt collector" definitions in
`../tx-law-references/references/tx-statutes-debt/` before relying on coverage.

- **Prohibited conduct — §§ 392.301–.306.** The Act enumerates the prohibited practices:
  **threats and coercion (§ 392.301)**, **harassment and abuse (§ 392.302)**, **unfair or
  unconscionable collection means (§ 392.303)**, **fraudulent, deceptive, or misleading
  representations (§ 392.304)**, the **deceptive use of names / forms simulating legal or judicial
  process (§ 392.305)**, and the **independent-debt-collector / attorney-name restrictions
  (§ 392.306)**. Map each abusive act the collector committed to a specific subsection and a
  specific factual element. Misrepresenting the **character, amount, or legal status** of the debt
  (a § 392.304 theory) and threatening action that cannot lawfully be taken (a § 392.301 theory) are
  the most common debt-buyer violations.
- **The § 392.404 tie-in — KEY.** A **violation of the TDCA is a deceptive trade practice
  actionable under the DTPA**, Tex. Bus. & Com. Code Ch. 17. Fin. Code **§ 392.404** makes a TDCA
  violation enforceable through the DTPA's private remedies (see the DTPA section below). This is
  the lever that turns a collection-conduct violation into **treble-damages exposure** for the
  collector — plead the TDCA violation **and** the § 392.404 tie-in expressly.
- **Remedies — § 392.403.** Independently of the tie-in, § 392.403 supplies a private action: a
  person may sue for **injunctive relief** to enjoin a continuing violation and for **actual
  damages**, and a successful claimant may recover **court costs and reasonable attorney fees**. A
  collector who fails to comply also faces the attorney-fee and bond consequences below. **Verify
  the current § 392.403 remedy and fee framework** against the corpus before relying on it.

## The § 392.101 surety-bond requirement — Texas has NO debt-collector license — KEY DEFENSE ANGLE

Texas does **not license** debt collectors. Instead, **Fin. Code § 392.101** requires a
**third-party debt collector** and a **credit bureau** to obtain and file a **surety bond** with the
**Texas Secretary of State** before engaging in debt collection in Texas. The bond is statutory and
runs in favor of persons damaged by the collector's violations of the chapter.

- **A bonding requirement, not a license.** Do not describe this as "licensing" — Texas has no
  debt-collector licensing regime. The § 392.101 obligation is a **bond on file with the Secretary
  of State**. The required penal sum of the bond is fixed by statute (currently **$10,000** — confirm
  the current figure against `../tx-law-references/references/tx-statutes-debt/`).
- **Check the bond filing first.** Look up the plaintiff (and any servicer) in the **Texas Secretary
  of State** records before responding. An **out-of-state debt buyer** suing in Texas that never
  filed the § 392.101 surety bond is a recurring pattern, and **operating without the required bond
  is litigable**. Failing to maintain the bond can itself be a § 392.101 violation that feeds the
  TDCA / § 392.404 DTPA tie-in.
- **Bond as a pressure point — verify the consequence.** Whether the absence of a § 392.101 bond
  **strips the plaintiff of capacity / standing to sue**, abates the action, or merely supplies a
  TDCA violation is **not automatic** — verify current Texas authority via case-law research /
  CourtListener before arguing the suit or any resulting judgment is barred. Treat the missing bond
  as a **strong TDCA violation, a verified-plea capacity challenge, and a settlement lever**, pleaded
  with the verification caveat. Raise the bond status in discovery (an RFA and an interrogatory).

## The Deceptive Trade Practices Act (DTPA) — Tex. Bus. & Com. Code Ch. 17

The **DTPA**, Tex. Bus. & Com. Code §§ 17.41–.63, is Texas's consumer-protection statute and the
vehicle through which a TDCA violation is enforced (via the § 392.404 tie-in).

- **Consumer standing — § 17.45(4).** Only a **"consumer"** — one who seeks or acquires goods or
  services by purchase or lease — has DTPA standing. A consumer-debt defendant typically qualifies
  through the underlying credit transaction; confirm the consumer-status element for the specific
  facts, because a bare debt is not always a "good or service." The TDCA tie-in under § 392.404
  supplies DTPA standing for a TDCA violation **regardless** of the general consumer test — verify
  that interplay in the corpus.
- **The § 17.46(b) laundry list.** Section 17.46(b) enumerates the specific "false, misleading, or
  deceptive acts or practices" that are actionable per se. Map the collector's misrepresentations
  (about the character / amount / legal status of the debt, or about who owns it) to the specific
  § 17.46(b) subsection that fits.
- **Remedies — § 17.50.** A prevailing consumer recovers **economic damages**; for conduct committed
  **knowingly**, **mental-anguish damages** and up to **treble** the economic damages; and for
  conduct committed **intentionally**, treble damages on the broader measure — plus **court costs
  and reasonable and necessary attorney fees** under § 17.50(d). Confirm the current treble-damages
  multiplier and the knowing/intentional thresholds against the corpus.
- **§ 17.505 — 60-day pre-suit notice.** Before filing a DTPA claim (including a TDCA claim brought
  through § 392.404), the consumer must give the defendant **written notice at least 60 days before
  filing**, advising of the complaint and the amount of economic damages, mental-anguish damages,
  and expenses (including attorney fees). The notice is a **prerequisite** with limited exceptions
  (e.g., when notice is impracticable because limitations is about to run, or when the DTPA claim is
  asserted as a **counterclaim**). When a debt defendant wants to **counterclaim** for a TDCA/DTPA
  violation, the counterclaim exception may apply — verify the current § 17.505 text before relying
  on it.
- **§ 17.565 — 2-year limitations.** A DTPA action must be commenced within **two years** after the
  deceptive act or practice occurred (or after the consumer discovered or should have discovered it).
  This is **shorter** than the debt's 4-year contract limitations — pin the violation dates carefully
  when raising the DTPA / TDCA theory.

## Statutes of limitation on the debt (DEFENSE)

The limitations bar is the single most powerful defense in stale-debt cases. The headline framework
— pull the authoritative, current text from `../tx-law-references/references/tx-statutes-debt/`:

| Claim | SOL | Citation |
|---|---|---|
| **Debt / breach of contract (incl. credit-card and open accounts)** | **4 years** | CPRC § 16.004 |
| **Residual (no other period prescribed)** | **4 years** | CPRC § 16.051 |
| **DTPA / TDCA-via-DTPA claim** | **2 years** | Tex. Bus. & Com. Code § 17.565 |
| **Action on a foreign judgment / domesticated judgment** | (verify) | CPRC Ch. 16 / Ch. 35 |

- **Most consumer debt is on a 4-year clock.** Credit-card balances, open accounts, and other
  contract claims fall under **CPRC § 16.004** (and the residual **§ 16.051**). Accrual generally
  runs from the date the cause of action accrues — for a revolving account, commonly the date of
  **default / last activity** the plaintiff can prove. Pin the date of the last payment or charge
  that the plaintiff can actually establish.
- **Time-barred consumer debt is NOT revived by a partial payment — STRONG DEFENSE.** **Fin. Code
  § 392.307** governs the collection of **out-of-statute (time-barred) consumer debt**: a payment on,
  or other activity regarding, a time-barred consumer debt does **not** restart or revive the
  limitations period, and the collector must comply with the statute's notice requirements. Under
  **CPRC § 16.065**, an acknowledgment that revives a barred debt must be **in writing and signed**
  by the party to be charged — an oral promise or a partial payment alone does not revive it. Verify
  the current § 392.307 text (it was amended to add consumer protections) against the corpus.
- **SOL is an affirmative defense that must be pleaded.** Limitations is an **affirmative defense**
  (TRCP 94) and must be **affirmatively pleaded** in the Original Answer or it is waived — raise it
  expressly. Once the account dates are fixed, a time-barred debt is also a strong **summary-judgment
  ground**, including the **no-evidence** motion (TRCP 166a(i)) where the plaintiff cannot produce
  evidence of a timely accrual date.
- **Counterclaim relation-back — § 16.069.** A counterclaim or cross-claim that arises out of the
  same transaction is not barred even if limitations has run, if filed within 30 days of the answer
  date — relevant when pairing a TDCA/DTPA counterclaim with the answer.

## Sworn account — TRCP 185 and the mandatory verified denial (TRCP 93(10)) — TRAP

Collection suits are frequently pleaded as a **suit on a sworn account** under **Tex. R. Civ. P.
185**. A petition supported by a **proper affidavit** that the account is just and true, due, and
that all just and lawful offsets, payments, and credits have been allowed is **prima facie
evidence** of the debt — the plaintiff need not otherwise prove it up at trial.

- **The verified-denial trap.** A sworn account is taken as **prima facie proof UNLESS** the
  defendant files a **written denial under oath** — a **verified denial** — denying the account.
  **Tex. R. Civ. P. 93(10)** lists "a denial of an account" among the pleas that must be **verified
  by affidavit**, and TRCP 185 requires the denial to be under oath to put the account in issue. A
  **general denial alone does NOT defeat a sworn account** — this is the single most common
  pro-se trap in Texas collection practice.
- **What the verified denial must do.** It must state under oath that the account is **not just or
  true**, in whole or in part, and (best practice) specifically deny the items contested. File it
  with the Original Answer. The denial may be verified by **affidavit** or by an **unsworn
  declaration** under CPRC § 132.001 (an unsworn declaration may substitute for an affidavit).
- **Defective sworn-account affidavits.** Test the plaintiff's TRCP 185 affidavit: is it made on
  **personal knowledge**, does it attach a **systematic record** of the account, and does it cover a
  **transaction between the parties** (a sworn account proper lies on the sale of goods/services
  between the parties, not always on a purchased credit-card balance)? A debt buyer's sworn-account
  affidavit on a third party's records is vulnerable — and a proper verified denial forces the
  plaintiff back to ordinary proof.

## Chain of title / standing

A debt buyer must trace ownership from the **original creditor** through every intermediate buyer to
itself, with a **Bill of Sale** for each transfer, an **Assignment** specifically identifying
**this** account (account number), and **account-level data** matching this consumer's account. A
bill of sale referencing "an attached pool of accounts" without the attachment, or "all accounts
sold on [date]" without tying to **this** account, is **insufficient**. Standing turns on whether
the plaintiff can prove it owns this specific account.

- **Account-stated theory and the fee hook.** Plaintiffs often plead **account stated** or
  **quantum meruit** alongside breach of contract to sidestep proof of the underlying agreement.
  Test whether there was any **agreed accounting** between **this** plaintiff and **this** defendant.
  Note the fee exposure: a successful party on a **contract / sworn account** may seek fees under
  **CPRC Ch. 38** (see below), so defeating the underlying claim matters to fee exposure too.
- **Authentication.** The documents offered to prove the assignment and the account must be properly
  **authenticated** — the bill of sale, the account-specific assignment, and the account records
  each need a competent foundation (see the evidence section).

## Debt-buyer evidence foundation — TRE 803(6) / 902(10)

To admit the account records and the assignment, the plaintiff must satisfy the **business-records**
hearsay exception, **Tex. R. Evid. 803(6)**, through a custodian or qualified witness — or rely on
the Texas self-authentication device, **Tex. R. Evid. 902(10)**.

- **TRE 902(10) is the Texas business-records affidavit.** Rule 902(10) supplies the **affidavit
  form** and the **pre-trial filing / notice mechanics** that let business records be
  self-authenticated **without a live custodian**: the records and the affidavit must be **filed
  with the clerk** and notice given to the other parties at least **14 days** before trial (confirm
  the current notice period against the corpus), and a party may then object. This is the device
  debt buyers use in lieu of a live records custodian.
- **The classic defense is attacking the affiant's basis of knowledge.** The debt buyer's affiant
  typically has **no personal knowledge** of the **original creditor's** record-keeping and cannot
  lay an 803(6) foundation for **another entity's** records. Probe the affiant's basis of knowledge:
  did the affiant work for the original creditor? How are the assignor's records integrated into the
  buyer's system, and were they kept in the regular course of the **assignor's** business? Does the
  902(10) affidavit satisfy the rule's form, and was the **pre-trial notice / filing** done on time?
  An affidavit that recites conclusions without establishing the custodian's knowledge of how the
  **assignor's** records were made and kept is vulnerable on objection and on summary judgment.
- **TRCP 193.7 self-authentication.** A document a party produces in discovery is **authenticated**
  for use against that party unless the party objects within the rule's deadline — useful for using
  the plaintiff's own produced documents (or for forcing the plaintiff to authenticate what it
  produced).
- **Justice-court caveat.** Under **TRCP 500.3(e)** the Rules of Evidence do **not** apply in a
  Justice Court except where Part V (Rules 500–510) incorporates them — so the 803(6) / 902(10)
  foundation fight is sharpest in **County Court at Law** and **District Court**, and on a **de novo
  appeal** from the Justice Court. See `tx-county-courts` and the venue skills.

## Discovery targeting chain of title

Texas **allows interrogatories** and a full discovery toolkit. Build the record before trial or
summary judgment — but mind the **discovery control plan** (TRCP 190: Level 1 / Level 2 / Level 3)
and the **expedited-actions** track (TRCP 169) that may constrain a smaller case:

- **Interrogatories — TRCP 197.** Capped at **25** interrogatories (excluding those identifying
  persons with knowledge of relevant facts — confirm the current cap and exclusions against the
  corpus). Use them on chain of title, the identity and basis of knowledge of the records custodian /
  affiant, the computation of the balance, and the plaintiff's § 392.101 Secretary-of-State bond
  status.
- **Requests for Production — TRCP 196.** Demand the **bills of sale** and **account-specific
  assignments** tying **this** account to the plaintiff, the original cardholder / credit agreement,
  periodic statements, the charge-off statement, and the electronic account data.
- **Requests for Admission — TRCP 198.** Pin down elements — e.g., that the plaintiff lacks an
  account-specific assignment, that no signed agreement exists, that the plaintiff held no § 392.101
  surety bond on the relevant dates. Unanswered RFAs are **deemed admitted** (TRCP 198.2(c)).
- **Required disclosures — TRCP 194.** The amended rule makes initial disclosures automatic — use
  the plaintiff's disclosures as an early window into the documents and witnesses.
- **Timing and motion practice.** Responses are generally due in **30 days** (with TRCP 21a add-on
  days for the method of service — point to the corpus); if responses are deficient,
  **confer** and move to compel under **TRCP 215**.

See `tx-discovery` for the full mechanics, the Level 1/2/3 control-plan framework, response
computation, and motion-to-compel practice.

## Forum — Justice Court vs. County Court at Law vs. District Court

Texas collection suits are heard in different courts by amount and type:

- **Justice Court — debt-claim case (TRCP 500–510, esp. 508).** Most small consumer-debt suits are
  filed as a **debt-claim case** under **TRCP 508** in a **Justice Court** (Justice of the Peace,
  divided into precincts). The Justice Court hears debt claims up to a statutory ceiling (confirm the
  current ceiling against the corpus / Gov't Code § 27.031). Justice-court procedure is simplified —
  **TRCP 500.3(e)** says the other Rules of Civil Procedure and the Rules of Evidence do **not**
  apply except where Part V incorporates them. **Answer deadline:** the defendant must file a written
  answer by the **end of the 14th day** after the citation is served (**TRCP 502.5**). Appeal from a
  Justice Court is **de novo to the County Court** (TRCP 506) on an appeal bond, cash deposit, or
  **Statement of Inability to Afford Payment**.
- **County Court at Law / Constitutional County Court.** Mid-tier civil jurisdiction; also hears
  **de novo appeals** from Justice Courts. The full Rules of Civil Procedure and Rules of Evidence
  apply.
- **District Court.** General-jurisdiction trial court for larger civil disputes.
- **The Monday rule (TRCP 99).** In **District Court** and **County Court at Law** (not Justice
  Court), the Original Answer is due by **10:00 a.m. on the Monday next after the expiration of
  twenty days** after the date of service — **not** a flat 20-day count. Flag this prominently;
  miscounting it produces defaults.
- **Never ignore a citation.** Failure to answer by the deadline lets the plaintiff take a
  **default judgment**, with **CPRC Ch. 38 attorney fees** added on top of the debt and costs. See
  `tx-first-30-days` for the answer and `tx-deadlines` for time computation.

## Post-judgment — exemptions, the wage-garnishment bar, and turnover

If a judgment enters, Texas's famously **debtor-protective** exemptions and the constitutional
wage-garnishment bar protect the consumer. Point dollar amounts and acreage to
`../tx-law-references/references/tx-statutes-debt/` and **verify current figures** — these are
drift-prone:

- **Wages are generally protected from garnishment — Tex. Const. art. XVI § 28.** The Texas
  Constitution prohibits garnishment of **current wages for personal service** except for
  court-ordered child support and spousal maintenance. **Ordinary consumer-debt judgments cannot
  be collected by wage garnishment in Texas** — a major debtor protection. (A creditor may still
  reach wages **after** they are paid and deposited, by other means.)
- **Bank-account garnishment and turnover.** A judgment creditor **can** garnish a **bank account**
  (post-judgment garnishment) and may obtain a **turnover order** under **CPRC § 31.002** reaching
  non-exempt property the debtor owns or controls. Identify which funds in the account are
  **exempt** (e.g., traceable exempt wages, Social Security, certain benefits).
- **Homestead — Tex. Prop. Code Ch. 41.** Texas's homestead is **unlimited in value** and limited
  only by **acreage** (urban vs. rural, single adult vs. family). Point the current acreage caps to
  the corpus.
- **Personal-property exemptions — Tex. Prop. Code Ch. 42.** Texas exempts a categorized list of
  personal property up to an **aggregate dollar cap** (different ceilings for a **family** vs. a
  **single adult**). Point the current aggregate caps to the corpus.
- **Judgment dormancy — CPRC § 34.001.** A judgment becomes **dormant** if no writ of execution
  issues within the statutory period (confirm the current period and the revival mechanics).

See `tx-post-judgment` for claiming exemptions, contesting garnishment / turnover, and setting aside
a default judgment.

## Attorney fees — CPRC Ch. 38 cuts both ways

In a suit on an **oral or written contract** (including a **sworn account**), **CPRC Ch. 38** lets
the **prevailing party** recover **reasonable attorney fees**. This is a **two-way exposure** and a
critical risk consideration:

- A consumer who **defeats** the suit (e.g., wins on limitations, no chain of title, or a fatal
  evidentiary gap) may be positioned to seek fees as a prevailing party — verify the current Ch. 38
  scope, including the 2021 amendment broadening recovery against organizations / LLCs, against the
  corpus.
- But a consumer who **loses** — including by failing to answer and suffering a **default judgment**
  — may be ordered to pay the **creditor's** reasonable fees on top of the debt and costs. **Never
  ignore a citation.**
- A **TDCA / DTPA** prevailing claimant has a **separate** fee entitlement (Fin. Code § 392.403;
  Tex. Bus. & Com. Code § 17.50(d)). Plead defenses and counterclaims with a good-faith basis.

## The five fact patterns

**Pattern 1 — Debt buyer with no chain of title.** Demand the bills of sale and account-specific
assignments tying **this** account to the plaintiff (RFP, TRCP 196); challenge the affiant's
TRE 803(6) / 902(10) basis of knowledge of the **original creditor's** records; verify the
plaintiff's § 392.101 Secretary-of-State surety bond. Plead lack of standing / failure to prove
assignment, and file a **verified denial (TRCP 93(10))** if the suit is on a sworn account.

**Pattern 2 — Time-barred debt (SOL).** Pin the date of **default / last activity** the plaintiff
can prove. Compare against the **4-year** contract / debt period (CPRC § 16.004; residual § 16.051).
Confirm no written, signed acknowledgment revived the debt (CPRC § 16.065) and that a partial
payment did **not** revive it (Fin. Code § 392.307). Plead limitations as an affirmative defense
(TRCP 94) and consider a **no-evidence summary judgment** (TRCP 166a(i)) once the dates are fixed.

**Pattern 3 — FDCPA / Regulation F / TDCA validation or dispute violation.** Consumer disputed or
never received a compliant validation notice, or the collector misrepresented the debt. FDCPA
§§ 1692g (validation), 1692e (false/misleading), 1692f (unfair); Reg F validation-notice content
(12 C.F.R. pt. 1006). Pair with a **TDCA** theory (Fin. Code §§ 392.301–.304) brought through the
**§ 392.404 DTPA tie-in** for treble-damages exposure — mind the **§ 17.505 60-day notice** and the
**2-year** DTPA limitations (§ 17.565). Federal text:
`../tx-law-references/references/federal-debt-laws/`.

**Pattern 4 — Wrong amount / wrong person.** Inflated balance (unauthorized fees / interest) or
mistaken identity / identity theft. **FDCPA** §§ 1692e(2) / 1692f(1) (misrepresenting / collecting
amounts not owed); **TDCA** § 392.304 (misrepresenting the **character / amount** of the debt) via
the § 392.404 DTPA tie-in; **FCRA** § 605B identity-theft block if applicable (shared
`federal-debt-laws/` corpus). Test the balance against the contract and any permitted charges.

**Pattern 5 — Unbonded collector / debt buyer.** Plaintiff or servicer never filed the § 392.101
**surety bond** with the Texas Secretary of State (Texas has **no debt-collector license** — it is a
**bonding** requirement). Raise it as a **TDCA violation**, a **verified-plea capacity** challenge,
and a settlement lever, verifying the current consequence via case-law research before arguing the
suit or judgment is barred. Pair with **TDCA / DTPA / FDCPA** theories.

## Affirmative-defenses catalog

Plead all that apply in the Original Answer; verified pleas (TRCP 93) must be **under oath**.
Defenses not pleaded may be waived (TRCP 94):

1. **Statute of limitations** — 4-year debt / contract period (CPRC § 16.004; residual § 16.051);
   no written-signed acknowledgment to revive (CPRC § 16.065); partial payment does not revive a
   time-barred consumer debt (Fin. Code § 392.307). Summary-judgment ground.
2. **Verified denial of the sworn account** — under oath, TRCP 93(10) / 185 (mandatory to contest a
   sworn account; a general denial does not suffice).
3. **Lack of standing / failure to prove assignment** — plaintiff cannot prove it owns this account.
4. **Want of capacity / unbonded collector** — no § 392.101 surety bond on file (verified plea,
   TRCP 93; assert with the verification caveat).
5. **Failure to state a claim / special exceptions (TRCP 91)** — no chain of title or specific
   account terms; or a **TRCP 91a** motion to dismiss a claim with no basis in law or fact.
6. **Lack of / failure of consideration** (verified, TRCP 93(9)).
7. **Payment / accord and satisfaction / release / settlement.**
8. **Account stated denied** — no agreed accounting between this plaintiff and this defendant.
9. **Usury / unauthorized charges** — balance includes charges not permitted by contract or law.
10. **Identity theft** (if applicable) — FCRA § 605B block.
11. **Discharge in bankruptcy** (if applicable).
12. **TDCA / DTPA / FDCPA violation** — raised as a **counterclaim** (mind the § 17.505 notice /
    counterclaim exception and § 16.069 relation-back); also a defense theme.

## Synthetic example outline (outline only — not a full filing)

A typical first response when sued by a debt buyer on a stale credit-card account in a Justice Court
debt-claim case (or County Court at Law on appeal):

1. **Original Answer with verified denial + affirmative defenses** (`tx-first-30-days`,
   `tx-draft-motion`):
   - **General denial** (TRCP 92) of the unproven allegations (amount owed, ownership, account
     stated) **plus** a **verified denial of the sworn account** under oath (TRCP 93(10) / 185) if
     the suit is pleaded as a sworn account.
   - Affirmative defenses: limitations (TRCP 94); lack of standing / failure to prove assignment;
     want of capacity (unbonded under § 392.101); account stated denied; failure of consideration
     (verified).
   - Caption and format per `tx-statewide-format`; "Original Answer," "Affidavit" / "Unsworn
     Declaration" (CPRC § 132.001) conventions; calendar the answer deadline — **end of the 14th
     day** in Justice Court (TRCP 502.5) or the **Monday rule** in District / County Court (TRCP 99).
2. **SOL defense developed** (`tx-deadlines`, `tx-fact-check`):
   - Pin the default / last-activity date; compute the **4-year** period (CPRC § 16.004 / § 16.051);
     confirm no signed written acknowledgment (CPRC § 16.065) and no revival by partial payment
     (Fin. Code § 392.307).
   - If time-barred on the face of the dates, tee up a **no-evidence summary judgment**
     (TRCP 166a(i)) once discovery fixes the dates (in County / District Court).
3. **Discovery targeting chain of title** (`tx-discovery`):
   - RFP (TRCP 196) for bills of sale, account-specific assignment, original agreement, statements;
     interrogatories (TRCP 197) on the affiant's basis of knowledge and the § 392.101 bond; RFA
     (TRCP 198) deeming key facts admitted; 30-day responses; motion to compel under TRCP 215 if
     deficient — minding the Level 1/2/3 control plan and any expedited-action limits.
4. **Optional counterclaim** for a **TDCA violation via the § 392.404 DTPA tie-in** — observe the
   **§ 17.505** notice / counterclaim exception and the **2-year** DTPA limitations (§ 17.565).

Draft each component with the sibling skills below; verify every citation with `tx-fact-check`.

## Composition

- Statewide format baseline: `tx-statewide-format`.
- Answer / first response (incl. verified denial): `tx-first-30-days`, `tx-draft-motion`. Affidavit /
  unsworn declaration: `tx-draft-declaration`.
- Discovery / control plan / motion-to-compel: `tx-discovery`. Exemptions / garnishment / turnover /
  set-aside: `tx-post-judgment`.
- Deadlines / time computation (Monday rule, 14-day JP answer, 30-day discovery): `tx-deadlines`.
  Citation verification: `tx-fact-check`.
- Venue mechanics: `tx-hcdc`, `tx-dcdc`, `tx-county-courts` (and Justice Court / debt-claim
  practice).
- Pre-filing quality control and packet assembly: `tx-quality-check`, `tx-file-packet`.
- Reference corpora (Texas statutes, court rules, and the symlinked federal text): `tx-law-references`.

## References

- `../tx-law-references/references/tx-statutes-debt/` — Texas statute corpus: **Tex. Fin. Code
  Ch. 392** (TDCA — §§ 392.101 bond, 392.301–.306 prohibited conduct, 392.307 time-barred debt,
  392.403 remedies, 392.404 DTPA tie-in); **Tex. Bus. & Com. Code Ch. 17** (DTPA — § 17.46(b) list,
  § 17.50 remedies, § 17.505 notice, § 17.565 limitations); **CPRC Ch. 16** (limitations — § 16.004,
  § 16.051, § 16.065, § 16.069), **Ch. 38** (attorney fees), **§ 31.002** (turnover), **§ 34.001**
  (dormancy), **§ 132.001** (unsworn declaration); **Tex. Prop. Code Ch. 41 / 42** (homestead /
  personal-property exemptions)
- `../tx-law-references/references/court-rules/` — TRCP 92 / 93 / 94 (denials, verified pleas,
  affirmative defenses), 99 (Monday rule), 166a (summary judgment incl. no-evidence), 169 / 190
  (expedited actions / discovery control plans), 185 (sworn account), 193.7 (self-authentication),
  194–198 / 215 (discovery), 500–510 (Justice Court / debt claim); Tex. R. Evid. 803(6) / 902(10)
- `../tx-law-references/references/federal-debt-laws/` — FDCPA, Regulation F, FCRA verbatim (shared
  corpus; do not duplicate)
