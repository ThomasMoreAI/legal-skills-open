---
name: az-personal-injury-codearranger
title: Arizona Personal-Injury Practice
description: 'Subject-matter bundle for Arizona personal-injury and tort actions. Triggers: "Arizona personal injury", "Arizona car accident", "Arizona auto accident", "Arizona pure comparative negligence", "Arizona comparative fault", "Arizona several liability", "joint liability abolished Arizona", "nonparty at fault Arizona", "Arizona no damages cap", "Arizona Constitution damages", "Arizona medical malpractice", "preliminary expert opinion affidavit Arizona", "Arizona notice of claim", "Arizona public entity", "dog bite Arizona", "Arizona slip and fall", "Arizona wrongful death", "Arizona UM UIM". Covers pure comparative negligence (A.R.S. § 12-2505), several liability with abolition of joint liability and nonparty-at-fault (§ 12-2506), constitutional prohibition on damage caps, medical-malpractice expert-affidavit gate (§ 12-2603), 180-day notice / 1-year SOL against public entities, 2-year SOL, dog-bite strict liability, UM/UIM coverage.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-personal-injury
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Arizona Personal-Injury Practice

> **NOT LEGAL ADVICE.** Arizona tort practice is deadline-sensitive
> and has structural features that diverge sharply from most states —
> pure comparative negligence, the constitutional ban on damage caps,
> the nonparty-at-fault apportionment regime, and the strict public-
> entity notice of claim. Statute numbers, day counts, and SOLs
> change — verify every SOL, threshold, and predicate-notice clock
> against the current A.R.S. before relying, and consult a licensed
> Arizona attorney about your specific case.

Use this subject-matter bundle for Arizona personal-injury and tort
actions — auto accidents, premises (slip-and-fall), product and
general negligence, medical malpractice, wrongful death, dog bites,
and claims against governmental entities.

## At a glance — the things that move every AZ case

1. **2-year personal-injury SOL** at A.R.S. § 12-542. Claims against
   a **public entity / public employee** run on a much shorter
   **1-year SOL** (A.R.S. § 12-821) and require a **180-day notice
   of claim** first (A.R.S. § 12-821.01). Calendar at intake.
2. **PURE comparative negligence** under A.R.S. § 12-2505 — a
   plaintiff's recovery is **reduced** in proportion to fault but is
   **NEVER barred**, even if the plaintiff is **more at fault than
   the defendant**. Arizona is NOT a modified / 50%-bar state.
3. **Several liability only** under A.R.S. § 12-2506 — Arizona
   **abolished joint liability**. Each defendant pays only its own
   allocated percentage of fault. Identify every at-fault actor.
4. **Nonparty at fault** (A.R.S. § 12-2506(B)) — the defense may
   shift fault to an absent person by serving a **notice of nonparty
   at fault** within the deadline in Ariz. R. Civ. P. 26(b). This
   is the central defensive lever in Arizona tort cases.
5. **NO DAMAGE CAPS — constitutional.** The Arizona Constitution
   **prohibits** the legislature from limiting injury/death damages
   (**art. 2 § 31** and **art. 18 § 6**). Arizona has **no med-mal
   cap and no non-economic-damages cap** of any kind.
6. **Med-mal preliminary expert affidavit** (A.R.S. § 12-2603) plus
   **expert qualification** (A.R.S. § 12-2604) — the early
   gates in health-care negligence cases (the § 12-2603 certification
   is filed **with the claim**, not pre-suit; the affidavit is served
   with the Rule 26.1 initial disclosures).
7. **Dog-bite strict liability** (A.R.S. § 11-1025) — owner liable
   regardless of the dog's prior viciousness or the owner's knowledge.
8. **UM/UIM coverage** is a frequent secondary recovery source in
   auto cases — confirm the policy and any statutory selection.

## Statute-of-limitations catalog

| Claim | SOL | Citation |
|---|---|---|
| **Personal injury (general negligence)** | **2 years** | A.R.S. § 12-542 |
| **Wrongful death** | **2 years** | A.R.S. § 12-542 |
| **Auto bodily injury / property damage** | **2 years** | A.R.S. § 12-542 |
| **Premises / slip-and-fall** | **2 years** | A.R.S. § 12-542 |
| **Medical malpractice** | **2 years** | A.R.S. § 12-542 |
| **Dog bite (statutory strict liability)** | **1 year** | A.R.S. § 12-541(5) — "liability created by statute" (the § 11-1025 strict-liability action) |
| **Dog bite (common-law negligence)** | **2 years** | A.R.S. § 12-542 |
| **Claim against a public entity / employee** | **1 year** + **180-day notice of claim** prerequisite | A.R.S. § 12-821 + § 12-821.01 |

**Notes** (point to corpus — `az-law-references` `az-statutes-debt/` —
for the operative day counts and any tolling / discovery-rule text;
this skill does not hardcode them):

- The **public-entity 1-year SOL** (A.R.S. § 12-821) is far shorter
  than the general 2-year clock and runs alongside the **180-day
  notice of claim** (A.R.S. § 12-821.01). Treat any government
  defendant as a SOL emergency.
- Arizona recognizes a **discovery rule** for accrual in some claims
  (e.g., latent medical-malpractice injury) — confirm accrual and any
  minority / unsound-mind tolling in corpus before relying on a
  filing date.
- The statutory **dog-bite strict-liability** action and a **common-
  law** negligence dog-bite action carry **different** limitation
  periods — confirm which clock applies in corpus.

## Pure comparative negligence — A.R.S. § 12-2505

Arizona is a **pure comparative negligence** jurisdiction. This is a
distinctive, plaintiff-favorable feature — flag it clearly:

- **A.R.S. § 12-2505(A)** — "the claimant's action is **not barred**,
  but the full damages shall be **reduced in proportion to the
  relative degree of the claimant's fault**." A plaintiff who is
  **80% at fault still recovers 20%** of their damages. There is **no
  50% bar** and **no greater-than-defendant bar** — contrast the
  modified / 51%-bar systems used in most states.
- **The only carve-out** is for a claimant who **intentionally,
  wilfully, or wantonly** caused or contributed to the injury or
  wrongful death — that claimant has **no right** to comparative
  apportionment (A.R.S. § 12-2505(A)).
- Fault is assessed by the trier of fact and applied across **all**
  contributing actors, including nonparties (see § 12-2506 below).

## Several liability and nonparty at fault — A.R.S. § 12-2506

Arizona **abolished joint-and-several liability** for most tort
actions. The apportionment regime is the structural heart of Arizona
tort defense:

- **A.R.S. § 12-2506(A)** — "Each defendant is liable **only** for
  the amount of damages allocated to that defendant **in direct
  proportion to that defendant's percentage of fault**." The court
  enters **separate, several judgments** reflecting each defendant's
  proportionate share. There is no contribution among tortfeasors in
  the ordinary case because no one overpays its share.
- **A.R.S. § 12-2506(B) — nonparty at fault.** The fault of a
  **nonparty** may be considered in the allocation **if** the
  plaintiff settled with that nonparty **or** the defending party
  gives **notice before trial** identifying the nonparty and the
  basis for attributing fault. The mechanics — content and the
  **deadline** — are governed by **Ariz. R. Civ. P. 26(b)** (the
  notice of nonparty at fault). Missing the rule's deadline forfeits
  the ability to point the jury at the absent actor.
- **A.R.S. § 12-2506(D) — exceptions (joint liability survives).**
  Defendants remain **jointly** liable where they (1) **acted in
  concert**, (2) one acted as the **agent or servant** of the other,
  or (3) liability arises under the **federal Employers' Liability
  Act**. These are narrow — confirm the current list in corpus.

**Strategic upshot:** because each defendant pays only its allocated
share and the defense can shift fault onto empty chairs, **finding
and joining every solvent at-fault actor** — and **policing the
nonparty-at-fault notice** under Rule 26(b) — drives recovery in
Arizona multi-defendant cases.

## NO damage caps — the constitutional prohibition

**Arizona has no statutory cap on damages of any kind** — no
non-economic cap, no medical-malpractice cap, no punitive cap by
statute. This is a **constitutional** rule, not merely a legislative
choice, and it is the single most distinctive feature of Arizona tort
law:

- **Ariz. Const. art. 2, § 31** — "**No law shall be enacted in this
  state limiting the amount of damages to be recovered for causing
  the death or injury of any person.**"
- **Ariz. Const. art. 18, § 6** — "**The right of action to recover
  damages for injuries shall never be abrogated, and the amount
  recovered shall not be subject to any statutory limitation.**"

Together these provisions **forbid the Arizona legislature from
capping** injury or wrongful-death damages. Any attempt to impose a
damages cap by statute is unconstitutional. (Both provisions carry a
narrow carve-out for persons injured while attempting or engaged in
felony conduct.) Do **not** import another jurisdiction's cap
framework — in Arizona, plead **uncapped** economic and non-economic
damages.

## Medical malpractice — A.R.S. § 12-561 et seq.

Health-care liability is governed by A.R.S. Title 12, Chapter 5.1
("Actions Relating to Health Care," § 12-561 et seq.). Note that
**there is no damages cap** (above) — the gating issues are the
**expert affidavit** and **expert qualification** requirements:

### Preliminary expert opinion affidavit — A.R.S. § 12-2603

- **§ 12-2603(A)** — the claimant must **certify in a written
  statement filed and served with the claim** whether or not expert
  opinion testimony is necessary to prove the standard of care or
  liability.
- **§ 12-2603(B)** — if the claimant certifies that expert testimony
  **is** necessary, the claimant must **serve a preliminary expert
  opinion affidavit with the initial disclosures** required by
  **Ariz. R. Civ. P. 26.1**. The affidavit must address the expert's
  qualifications, the standard of care, the manner of breach, and how
  the breach caused the injury (confirm the statutory element list in
  corpus).
- A defective or missing affidavit exposes the claim to dismissal —
  treat it as an early case-dispositive gate.

### Expert qualifications — A.R.S. § 12-2604

The standard-of-care expert must satisfy Arizona's **matching-
specialty** rule — broadly, the expert must specialize in the **same
specialty** as the defendant (or, if the defendant is board-certified,
be **board-certified** in that specialty) and, during the year
immediately before the alleged malpractice, have devoted a majority
of professional time to **active clinical practice** or to
**instruction** of students in that specialty. Confirm the exact
qualification text in corpus before relying.

## Public entities — the notice of claim and 1-year SOL

Claims against the State, counties, cities, school districts, and
public employees are governed by A.R.S. Title 12, Article 2 — and the
prerequisites are **strict** and **commonly fatal**:

- **A.R.S. § 12-821.01 — 180-day notice of claim.** A person with a
  claim against a public entity, public school, or public employee
  must **file a notice of claim within 180 days** after the cause of
  action accrues. The notice must contain **facts sufficient to
  permit the entity to understand the basis of liability** and a
  **specific amount for which the claim can be settled** together
  with **facts supporting that amount**. **A claim not filed within
  180 days is barred** — Arizona courts enforce this strictly, and a
  defective sum-certain demand can sink the claim.
- **A.R.S. § 12-821 — 1-year SOL.** Even after a timely notice of
  claim, the lawsuit itself must be filed **within one year** after
  the cause of action accrues — half the general 2-year clock.
- **Calendar both clocks separately at intake.** A government
  defendant turns a routine PI matter into a deadline emergency: the
  180-day notice runs first, the 1-year suit clock runs alongside it.

## Dog-bite liability — A.R.S. §§ 11-1025 / 11-1020

- **A.R.S. § 11-1025(A) — strict liability.** The owner of a dog that
  **bites a person** in a public place or while the person is
  **lawfully** in or on a private place (including the owner's
  property) is **liable for damages "regardless of the former
  viciousness of the dog or the owner's knowledge of its
  viciousness."** No "one free bite" rule applies to the statutory
  action.
- **A.R.S. § 11-1020** — companion provision imposing liability on a
  person who allows a **dog to be at large** for any resulting injury
  to person or property (broader than a bite); confirm the interaction
  with § 11-1025 in corpus.
- **Provocation defense** — § 11-1025 cross-references the definition
  of "provocation" (see A.R.S. § 11-1027); provocation is the
  principal statutory defense.
- Distinguish the **statutory strict-liability** action from a
  **common-law negligence** dog-bite claim — they carry different
  limitation periods (see SOL catalog).

## Uninsured / underinsured motorist (UM/UIM)

In auto cases, **UM/UIM coverage** under the injured person's own (or
a resident relative's) policy is a frequent secondary recovery source
where the at-fault driver is uninsured or under-insured:

- Confirm the policy limits, any required **written rejection /
  selection** of UM/UIM coverage, and the **stacking** rules.
- UM/UIM claims are often **contractual** and may carry **policy /
  contractual** notice and suit deadlines distinct from the tort SOL —
  read the policy and confirm the operative limitation in corpus.

## High-yield Arizona PI checks

1. **What's the SOL?** General PI **2 years** (A.R.S. § 12-542).
   Public-entity defendant → **1 year** (§ 12-821) **+ 180-day notice
   of claim** (§ 12-821.01). Dog-bite statutory vs. common-law clock?
2. **Comparative fault?** Arizona is **PURE** — plaintiff recovers
   even if **more than 50%** at fault (A.R.S. § 12-2505), reduced by
   fault share. Only intentional/wilful/wanton conduct forfeits
   apportionment.
3. **Multiple actors?** Several liability only (A.R.S. § 12-2506(A));
   each defendant pays its own share. Watch for a defense **notice of
   nonparty at fault** under § 12-2506(B) / **Ariz. R. Civ. P. 26(b)**
   — and join every solvent at-fault actor.
4. **Damages?** **No caps** — plead uncapped non-economic and economic
   damages (Ariz. Const. art. 2 § 31 + art. 18 § 6). Do not import
   another jurisdiction's cap.
5. **Medical malpractice?** Certify under **§ 12-2603(A)**; serve the
   **preliminary expert opinion affidavit** with Rule 26.1 initial
   disclosures (**§ 12-2603(B)**); confirm the expert satisfies the
   matching-specialty rule (**§ 12-2604**).
6. **Public defendant?** **180-day notice of claim** with a sum-
   certain settlement demand and supporting facts (§ 12-821.01); **1-
   year suit clock** (§ 12-821). Both strict.
7. **Dog bite?** Statutory strict liability (§ 11-1025) — owner liable
   regardless of prior viciousness; assess the provocation defense
   (§ 11-1027).
8. **Auto case?** UM/UIM coverage available? Policy limits, selection
   / rejection, stacking, contractual notice deadlines?

## Drafting checklist

- [ ] Confirm the **2-year SOL** (or the **1-year** public-entity
      clock) is not running out within 30 days; calendar the **180-day
      notice of claim** separately for any government defendant.
- [ ] Plead **pure comparative negligence** awareness — recovery is
      reduced, **never barred**, by plaintiff's fault share (A.R.S.
      § 12-2505).
- [ ] Identify and **join every at-fault actor**; track the defense
      **notice of nonparty at fault** (A.R.S. § 12-2506(B) / Ariz. R.
      Civ. P. 26(b)) and move to add necessary defendants.
- [ ] In the damages prayer, plead **uncapped** economic **and** non-
      economic damages — Arizona's Constitution bars statutory caps
      (art. 2 § 31 + art. 18 § 6). Do not hardcode any cap.
- [ ] For **medical malpractice**, file the **§ 12-2603(A)
      certification** with the complaint and serve the **preliminary
      expert opinion affidavit** with the Rule 26.1 initial
      disclosures; confirm the expert meets **§ 12-2604**.
- [ ] For a **public defendant**, serve the **§ 12-821.01 notice of
      claim** within 180 days with a **specific settlement amount and
      supporting facts**, then file suit within the **1-year**
      § 12-821 window.
- [ ] For a **dog bite**, plead **§ 11-1025** strict liability and
      anticipate the **provocation** defense (§ 11-1027).
- [ ] In an **auto** case, identify any **UM/UIM** coverage and its
      separate contractual deadlines.

## Composition

- For statewide format and caption: `az-statewide-format`
- For first responsive pleading and affirmative defenses:
  `az-first-30-days`
- For drafting motions / declarations / orders: `az-draft-motion`,
  `az-draft-declaration`, `az-draft-order`
- For SOL / notice-of-claim clocks: `az-deadlines`
- For discovery (incl. Rule 26(b) nonparty-at-fault notice and Rule
  26.1 initial disclosures): `az-discovery`
- For QC: `az-quality-check`, `az-fact-check`

## References

- `az-law-references` — A.R.S., Ariz. R. Civ. P., Ariz. R. Evid.,
  Arizona Constitution, and federal symlinks (`az-statutes-debt/`
  holds the verbatim statutory text — point there for SOL day counts
  and operative section text)
- A.R.S. § 12-542 — 2-year personal-injury / wrongful-death SOL
- A.R.S. § 12-541(5) — 1-year statutory-liability limitation (the
  § 11-1025 dog-bite strict-liability action)
- A.R.S. § 12-2505 — pure comparative negligence (recovery reduced,
  never barred)
- A.R.S. § 12-2506 — several liability; nonparty at fault (B);
  acting-in-concert / agency exceptions (D)
- A.R.S. § 12-561 et seq. — actions relating to health care
- A.R.S. § 12-2603 — preliminary expert opinion affidavit (med-mal)
- A.R.S. § 12-2604 — expert qualifications (med-mal)
- A.R.S. § 12-821 — 1-year SOL against a public entity / employee
- A.R.S. § 12-821.01 — 180-day notice of claim against a public
  entity / public school / public employee
- A.R.S. § 11-1025 — dog-bite strict liability
- A.R.S. § 11-1020 — dog-at-large liability (injury to person or
  property)
- A.R.S. § 11-1027 — definition of "provocation" (dog-bite defense)
- Ariz. Const. art. 2, § 31 — no law limiting damages for death or
  injury
- Ariz. Const. art. 18, § 6 — right of action never abrogated; amount
  recovered not subject to any statutory limitation
- Ariz. R. Civ. P. 26(b) — notice of nonparty at fault
- Ariz. R. Civ. P. 26.1 — initial disclosures (trigger for the § 12-
  2603(B) preliminary expert affidavit)
