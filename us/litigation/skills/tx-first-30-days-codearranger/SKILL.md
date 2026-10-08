---
name: tx-first-30-days-codearranger
title: Texas — First 30 Days After Service
description: 'Use when a Texas defendant has just been served with a civil petition or citation. Triggers: "I got served in Texas", "answer a Texas lawsuit", "I was sued in Texas", "served with a citation in Texas", "when is my Texas answer due", "Texas Monday rule answer", "answer due 10 a.m. Monday Texas", "general denial Texas", "verified denial Texas Rule 93", "deny a sworn account Texas", "special exceptions Texas Rule 91", "Rule 91a dismissal Texas", "affirmative defenses Texas answer", "counterclaim Texas", "set aside Texas default judgment", "Craddock Texas default", "justice court answer 14 days Texas". Covers the TRCP 99 Monday-rule answer deadline (and the TRCP 502.5 justice-court 14-day answer), the TRCP 92 general denial, the TRCP 93 verified denials (including the TRCP 185 / 93(10) sworn-account denial), TRCP 91 special exceptions, TRCP 91a dismissal, affirmative defenses, compulsory vs. permissive counterclaims, and removal-to-federal caution. Delegates date math to tx-deadlines.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Texas — First 30 Days After Service

> **NOT LEGAL ADVICE.** Time is short. This skill helps a defendant
> sketch a response and surface the most important deadlines, but
> consult a licensed Texas attorney about substantive defenses when
> possible.

Use this skill when the defendant has **just been served** with a
**citation and petition** in a District Court, County Court at Law, or
Justice Court. It frames the response window: the time in which the
defendant must file an answer or risk a **default judgment**. Pull
verbatim rule text from `../tx-law-references/references/court-rules/`,
and compute the actual due date with `tx-deadlines`.

## ★ The clock — the Texas "Monday rule" — TRCP 99

> **★ The answer is NOT due a flat number of days after service.** In
> District Court and County Court at Law, the citation commands the
> defendant to file a written answer **"by 10:00 a.m. on the Monday
> next after the expiration of twenty days after the date of service"**
> (**TRCP 99**). Count 20 days from the date of service; then the answer
> is due at **10:00 a.m. on the next Monday** after that. This is the
> Texas **"Monday rule"** — flag it prominently and never treat the
> deadline as a flat 20-day count. Compute the exact date with
> `tx-deadlines` (`--rule answer-due`).

> **★ Justice Court is different — 14 days.** In Justice Court (small
> claims / debt claim / eviction, TRCP 500–510), the defendant's answer
> is due by the **end of the 14th day** after the date the defendant
> was served with citation (**TRCP 502.5**); eviction has its own
> compressed schedule under TRCP 510. Confirm the operative count
> against the corpus and `tx-deadlines`.

> ⚠ **Default risk.** If the defendant does not file an answer by the
> deadline, the plaintiff may take a **default judgment** (TRCP 239).
> Setting one aside later requires meeting the **Craddock** standard
> (below) — much harder than answering on time. **Filing any timely
> answer — even a bare general denial — cuts off a no-answer default.**

## Playbook

### Days 0–3 — read the petition, check the citation

- **Read every numbered paragraph.** Note who is suing, on what claims,
  for what relief, and what contracts / accounts / events are alleged.
  Check whether the petition pleads a **sworn account** (TRCP 185) — if
  so, a **verified denial is mandatory** (below).
- **Note the court, county, and cause number** — these go on every
  filing (`tx-statewide-format` caption).
- **Confirm the tier.** Justice Court (debt-claim / small claims /
  eviction) answers run on the 14-day TRCP 502.5 clock; District Court
  and County Court at Law answers run on the Monday rule (TRCP 99).
- **Check service** and the citation. Defective service, lack of
  personal jurisdiction, and improper venue are challengeable — preserve
  them (below). A defendant served by substituted service (TRCP 106) or
  citation by publication has special posture.

### Days 3–10 — choose the response strategy

The principal paths, which can be combined:

1. **Original Answer** — typically a **general denial** under **TRCP 92**
   (one sentence putting the plaintiff to its proof on all but the
   matters that must be specifically or verifiably denied), plus any
   **verified denials (TRCP 93)**, **affirmative defenses**, and
   **counterclaims**.
2. **Special exceptions** under **TRCP 91** — the Texas vehicle to
   challenge a vague, defective, or insufficient pleading (Texas has
   **no general demurrer**). The remedy is an opportunity to replead,
   not dismissal.
3. **Rule 91a motion to dismiss** — to dismiss a cause of action with
   **no basis in law or fact** (below).
4. **Special appearance (TRCP 120a)** — to contest personal
   jurisdiction; it must be filed **before** any other plea (a general
   appearance waives the jurisdiction challenge), and follows the "due
   order of pleadings."

### ★ Verified denials — TRCP 93 (and the sworn-account denial)

> ⚠ **Some defenses must be denied under oath.** **TRCP 93** lists
> matters that must be denied by a **verified pleading** (a sworn
> denial / affidavit or an unsworn declaration under CPRC § 132.001) —
> a general denial alone is **not enough** to put them in issue. The
> list includes (verify the current text against the corpus): lack of
> legal capacity to sue or be sued, defect of parties, that a written
> instrument's execution is denied, want or failure of consideration,
> and — critically in collection suits — **denial of a sworn account
> under TRCP 93(10) / TRCP 185.**

> **★ Sworn account (TRCP 185).** If the plaintiff pleads its claim as
> a verified "suit on a sworn account," that verified account is
> **prima facie evidence** of the debt **unless** the defendant files a
> **written denial under oath** (TRCP 185, in the manner TRCP 93(10)
> requires). Failing to file the sworn denial can mean the plaintiff
> proves its case on the pleadings alone. **A defendant contesting a
> sworn-account suit must file the verified denial** — see
> `tx-consumer-debt`.

### Rule 91a — motion to dismiss a baseless cause of action

> **TRCP 91a** allows a party to move to dismiss a cause of action that
> has **no basis in law or in fact** — the Texas analog to a federal
> 12(b)(6) motion (added 2013). It must be filed **within 60 days after
> the first pleading containing the challenged cause of action** is
> served, and at least 21 days before the hearing. Fee-shifting under
> Rule 91a was **made discretionary by 2019 legislation** — confirm the
> current cost/fee rule against the corpus before relying on it.

### Days 10–30 — draft the answer (or the motion)

#### Answer structure (TRCP 92 / 93)

```
                    DEFENDANT'S ORIGINAL ANSWER

   Defendant [Name] files this Original Answer to Plaintiff's
   [Original Petition] and would respectfully show:

                       I. GENERAL DENIAL
   Pursuant to Tex. R. Civ. P. 92, Defendant generally denies each and
   every allegation in Plaintiff's petition and demands strict proof
   thereof by a preponderance of the evidence.

                  II. VERIFIED DENIAL (if applicable)
   Pursuant to Tex. R. Civ. P. 93 [and 185], Defendant specifically
   denies under oath that [there is a sworn account / the account is
   just and true / Defendant executed the instrument / there was
   consideration]. [Attach affidavit or CPRC § 132.001 declaration.]

                    III. AFFIRMATIVE DEFENSES
   [Plead each affirmative defense — TRCP 94 — that may apply.]

                       IV. COUNTERCLAIM (if any)
   [Plead complaint-style with numbered allegations and named counts.]
```

#### Affirmative-defense catalog — TRCP 94

Plead **all** that may apply (TRCP 94 requires affirmative defenses to
be **pleaded** or they may be waived). Common Texas defenses:

- Statute of limitations (very common — verify the period against
  `tx-deadlines` / the subject bundle: 4-year debt/contract under CPRC
  § 16.004; 2-year tort/PI under § 16.003)
- Payment / accord and satisfaction / release
- Discharge in bankruptcy
- Statute of frauds
- Estoppel / waiver / laches
- Failure of consideration / fraud / illegality
- Res judicata / collateral estoppel (prior judgment)
- Lack of standing / chain of title (debt-buyer cases — see
  `tx-consumer-debt`)
- Limitation of liability / proportionate responsibility (CPRC Ch. 33)

### Counterclaims — compulsory vs. permissive — TRCP 97

- **Compulsory counterclaim (TRCP 97(a)).** A pleader **must** state any
  claim against the opposing party that arises out of the **transaction
  or occurrence** that is the subject of the opposing party's claim and
  does not require third parties over whom the court lacks jurisdiction.
  A compulsory counterclaim not pleaded can be **barred** later. Plead
  all known related counterclaims with the answer.
- **Permissive counterclaim (TRCP 97(b))** — any other claim against an
  opposing party. **Cross-claims** against co-parties run under TRCP
  97(e). Note **CPRC § 16.069** allows a counterclaim arising from the
  same transaction to be filed even if limitations would otherwise have
  run, within a short window after the original claim — confirm against
  the corpus.

### Removal to federal court — caution

> If the suit could have been brought in federal court (a federal claim
> or complete diversity above the amount-in-controversy threshold), a
> defendant generally has **30 days from service** to remove under 28
> U.S.C. § 1446. Removal is a **federal procedural step** with its own
> strict clock that can run separately from the state answer deadline —
> evaluate it early, and do not let the state answer lapse while
> considering removal.

### Setting aside a default — the Craddock standard

If a default judgment is already entered, a defendant may move for new
trial to set it aside. Texas applies the **Craddock v. Sunshine Bus
Lines** standard (*Craddock v. Sunshine Bus Lines, Inc.*, 133 S.W.2d
124 (Tex. 1939)): the movant must show that (1) the failure to answer
was **not intentional or the result of conscious indifference** but due
to accident or mistake; (2) the motion sets up a **meritorious
defense**; and (3) granting it will **not cause delay or injury** to
the plaintiff. The motion for new trial is itself deadline-bound
(within 30 days of the judgment) — see `tx-post-judgment` and
`tx-deadlines`.

## Filing the answer / motion

- **File** with the clerk in the caption — district clerk (District
  Court), county clerk (County Court at Law), or the JP's clerk
  (Justice Court). E-file through **eFileTexas.gov** (mandatory for
  attorneys; available to self-represented filers).
- **Serve** all parties under **TRCP 21 / 21a** with a certificate of
  service (the answer does not require formal citation service).
- **Sign** under **TRCP 57** (party signature) and TRCP 13 (the
  signature is a certification; sanctions attach).

## Composition

- Format / caption / verification: `tx-statewide-format`
- Drafting + the summary-judgment standard (traditional 166a(c) /
  no-evidence 166a(i)): `tx-draft-motion`, `tx-draft-declaration`
- Filing court: `tx-hcdc`, `tx-dcdc`, `tx-county-courts`
- Deadline arithmetic (the Monday rule, the 14-day JP answer):
  `tx-deadlines`; default vacatur / Craddock: `tx-post-judgment`
- Matter-specific defenses: `tx-consumer-debt`, `tx-family-law`
- Noticing any motion for hearing or submission: `tx-schedule-hearing`,
  `tx-hearings`
- Pro se signature conventions: `tx-pro-se`

## References

- `references/answer-template.md` — full TRCP 92 general-denial answer
  with the TRCP 93 verified-denial and TRCP 94 affirmative-defense
  sections
- `references/verified-denial-sworn-account.md` — TRCP 185 / 93(10)
  sworn-account denial scaffold with the CPRC § 132.001 declaration
- `references/special-exceptions-91a.md` — TRCP 91 special exceptions
  and TRCP 91a motion-to-dismiss grounds (the 60-day window)
- `references/affirmative-defense-catalog.md` — annotated, keyed to the
  TRCP 94 pleading requirement
- `references/default-and-craddock.md` — taking / setting aside a
  default and the Craddock three-part test
