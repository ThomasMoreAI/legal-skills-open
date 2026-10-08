---
name: mi-personal-injury-codearranger
title: Michigan Personal-Injury Practice
description: Subject-matter bundle for Michigan personal-injury and tort actions. Triggers include "Michigan personal injury", "Michigan auto accident", "no-fault Michigan", "MCL 500.3135" tort threshold, "McCormick v Carrier", "Michigan comparative fault 51%", "medical malpractice Michigan", "182-day notice Michigan", "product liability Michigan", "wrongful death Michigan", "GTLA Michigan" governmental immunity. Covers modified comparative fault with 51% non-economic bar (MCL 600.2959) and several liability (MCL 600.6304); no-fault auto regime (MCL 500.3101) with tort threshold (MCL 500.3135); products liability; medical-malpractice pre-suit gates (MCL 600.2912b, 2912d) with non-economic caps (MCL 600.1483); wrongful death (MCL 600.2922); GTLA governmental immunity (MCL 691.1401).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-personal-injury
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Michigan Personal-Injury Practice

> **NOT LEGAL ADVICE.** Michigan tort practice is deadline-sensitive
> and has unusual structural gates — the no-fault auto regime, the
> medical-malpractice Notice of Intent and Affidavit of Merit, and
> governmental immunity. Statute numbers, dollar caps, and day
> counts change (several Michigan caps are inflation-adjusted
> annually) — verify every SOL, cap, threshold, and predicate-notice
> clock against the current MCL before relying, and consult a
> licensed Michigan attorney about your specific case.

Use this subject-matter bundle for Michigan personal-injury and
tort actions — auto / no-fault accidents, premises (slip-and-fall),
product and general negligence, medical malpractice, wrongful
death, and claims against governmental entities.

## At a glance — the eight things that move every MI case

1. **3-year personal-injury SOL** at MCL 600.5805. Med-mal runs on
   a separate 2-year / 6-month-discovery clock (MCL 600.5838a).
   Calendar at intake.
2. **No-fault auto regime** at MCL 500.3101 et seq. A car-accident
   bodily-injury claim is **first** a PIP / first-party question;
   a third-party tort suit exists only if the **MCL 500.3135 tort
   threshold** is met.
3. **MCL 500.3135 tort threshold** — death, permanent serious
   disfigurement, or **"serious impairment of body function"** as
   construed in *McCormick v Carrier*, 487 Mich 180 (2010). The
   single most-litigated issue in Michigan auto cases.
4. **Modified comparative fault with a 51% bar on non-economic
   damages** under MCL 600.2959 — a plaintiff more than 50% at
   fault recovers **no non-economic damages** (economic damages
   are merely reduced by fault share).
5. **Several (not joint) liability** under the 1995 tort reform,
   MCL 600.6304(4). Identify all at-fault parties and **non-
   parties** for allocation; the defense may file notice of
   non-party fault under MCR 2.112(K).
6. **Med-mal pre-suit gates**: the **182-day Notice of Intent**
   (MCL 600.2912b) and the **Affidavit of Merit** (MCL 600.2912d),
   with expert qualification under MCL 600.2169. The two most
   common case-killers in Michigan health-care litigation.
7. **Med-mal non-economic caps** at MCL 600.1483 (lower and higher
   "catastrophic" tiers; both inflation-adjusted annually —
   confirm the current figures in corpus).
8. **Governmental immunity** under the GTLA, MCL 691.1401 et seq.
   Immunity is the default; work the claim into a statutory
   exception (highway, motor-vehicle, public-building, etc.) or
   it fails.

## Statute-of-limitations catalog

| Claim | SOL | Citation |
|---|---|---|
| **Personal injury (general negligence)** | **3 years** | MCL 600.5805 |
| **Property damage** | **3 years** | MCL 600.5805 |
| **Auto / no-fault first-party PIP benefits** | **1 year** from date of expense; 1-year-back rule | MCL 500.3145 |
| **Auto third-party bodily injury (tort)** | **3 years** | MCL 600.5805 |
| **Medical malpractice** | **2 years** from act/omission, or **6 months** from discovery, whichever is later; **6-year repose** | MCL 600.5838a + MCL 600.5805 |
| **Products liability** | **3 years** | MCL 600.5805 |
| **Wrongful death** | runs on the SOL of the **underlying claim** (saving statute) | MCL 600.2922 + MCL 600.5852 |
| **Premises liability** | **3 years** | MCL 600.5805 |
| **Claim against a governmental entity (GTLA)** | underlying SOL **+ notice prerequisites** (varies by exception) | MCL 691.1404 (highway) and related |

**Notes**:

- The med-mal **6-month-from-discovery** extension and the **6-year
  statute of repose** (MCL 600.5838a) are independent of the 2-year
  clock. Confirm both — the repose can bar a claim the discovery
  rule would otherwise save.
- No-fault **PIP benefits** carry their own short 1-year clock and a
  **one-year-back rule** (MCL 500.3145) that limits recoverable
  expenses to the year preceding suit — distinct from the 3-year
  tort clock for the bodily-injury suit.
- The **wrongful-death saving statute** (MCL 600.5852) gives a
  personal representative additional time to bring a survived claim;
  it interacts with the underlying SOL — confirm the calculation.

## Comparative fault — the 51% bar and several liability

Michigan follows **modified comparative fault** with a 1995-tort-
reform structure that treats economic and non-economic damages
**differently**:

- **MCL 600.2959** — a plaintiff who is **more than 50%** at fault
  is **barred from recovering NON-economic damages** entirely.
  **Economic** damages are **not** barred at 51% — they are merely
  **reduced** by the plaintiff's percentage of fault.
- **MCL 600.6304(1)–(2)** — the trier of fact allocates fault among
  all persons who contributed to the injury, including the
  plaintiff and any non-parties.
- **MCL 600.6304(4)** — **several liability**: each defendant is
  liable only for its **allocated share** of damages. The 1995
  reforms abolished joint-and-several liability for most tort
  actions (a narrow exception survives for certain medical-
  malpractice and environmental contexts — confirm in corpus).

**Identification of all at-fault actors (parties and non-parties)**
is the central strategic concern. A defendant gives **notice of
non-party fault** under **MCR 2.112(K)** (generally within 91 days
of filing its first responsive pleading), which lets the jury
allocate fault to an absent actor. The plaintiff may then move to
add the named non-party as a defendant.

## No-fault automobile insurance — MCL 500.3101 et seq.

Michigan's no-fault system replaces most tort liability arising
from auto accidents with **first-party Personal Injury Protection
(PIP)** benefits, payable regardless of fault.

### First-party PIP benefits (MCL 500.3105–3107)

- **Allowable expenses** — reasonably necessary medical care,
  recovery, and rehabilitation.
- **Work loss** — up to a statutory monthly maximum (inflation-
  adjusted; confirm the current cap in corpus).
- **Replacement services** — up to a per-day cap.
- **Survivor's loss** for fatal accidents.

### The 2019 no-fault reforms

The 2019 amendments (effective in stages from 2019–2020) made
sweeping structural changes:

- **PIP medical coverage-level choice** (MCL 500.3107c) — insureds
  may elect coverage tiers (e.g., $50k / $250k / $500k / unlimited),
  ending mandatory unlimited PIP. Verify the current election menu
  and the conditions for opting below unlimited.
- **A medical fee schedule** (MCL 500.3157) capping provider
  reimbursement.
- Attendant-care limits and other cost-containment provisions.

These reforms changed the value and structure of first-party claims
substantially — date-of-accident matters because policy elections
and fee schedules differ over time.

### The tort threshold — MCL 500.3135

A **third-party** suit for **non-economic** damages (pain and
suffering) against an at-fault driver is permitted **only** where
the injured person suffered:

1. **Death**;
2. **Permanent serious disfigurement**; or
3. **Serious impairment of body function**.

**"Serious impairment of body function"** is the dominant battleground.
*McCormick v Carrier*, 487 Mich 180 (2010), overruled the more
restrictive *Kreiner v Fischer* framework and set the governing
test: (a) an **objectively manifested impairment** (observable or
perceivable from actual symptoms or conditions); (b) of an
**important body function** (one of value, significance, or
consequence to the injured person); that (c) **affects the
person's general ability to lead his or her normal life** (an
influence on some of the person's capacity to live in his or her
normal manner of living) — **no** temporal requirement and **no**
requirement that the impairment be permanent. The 2019 reforms
codified a *McCormick*-aligned definition into MCL 500.3135 —
confirm the current statutory text in corpus.

**Excess economic loss** (e.g., work loss above the PIP cap) is
also recoverable in third-party tort under MCL 500.3135(3)(c)
without meeting the non-economic threshold.

## Products liability — MCL 600.2945–2949a

Michigan's 1995 product-liability reforms govern claims that a
product caused injury:

- **MCL 600.2945** — definitions ("product liability action,"
  "production," "manufacturer," "seller").
- **MCL 600.2946** — the plaintiff must prove a defect and
  causation; the **state-of-the-art / practical-alternative-design**
  framing for design-defect claims. Subsection (4) carries the
  **FDA / government-regulation compliance defense** — a rebuttable
  presumption that the manufacturer or seller is not liable where the
  aspect of the product that allegedly caused the harm complied with,
  or was approved under, a federal or state agency's standards.
- **MCL 600.2946a** — caps on non-economic damages in product cases
  (lower and higher tiers; inflation-adjusted — confirm in corpus),
  with an exception removing the cap where the defendant acted with
  the requisite culpability (e.g., gross negligence / intentional
  conduct under the statute).
- **MCL 600.2947(6)** — liability limits, including the
  **non-manufacturer-seller** protection (a seller other than a
  manufacturer is not liable unless it failed to exercise reasonable
  care, or made an express warranty that the product failed to conform
  to, that was a proximate cause of the harm).
- **MCL 600.2948** — adequate-warning / failure-to-warn provisions,
  including the obvious-risk limitation.
- **MCL 600.2949a** — the **knowledge-of-defect exception**: where the
  defendant had actual knowledge the product was defective and that
  the defect was substantially likely to cause the injury, and
  willfully disregarded that knowledge, the MCL 600.2946(4) /
  600.2946a / 600.2947 / 600.2948 protections do **not** apply.

## Medical malpractice — the pre-suit gates

Michigan imposes two pre-suit procedural prerequisites that are the
most common bases for dismissal.

### Notice of Intent — 182 days (MCL 600.2912b)

A claimant **may not commence** a medical-malpractice action
**until 182 days** after giving the prospective defendant a
**written Notice of Intent (NOI)**. (A 154-day window applies in
narrow circumstances — confirm.) The NOI must contain the statutory
elements at MCL 600.2912b(4):

- The factual basis for the claim;
- The applicable standard of practice or care alleged;
- The manner in which the standard was breached;
- The action that should have been taken to comply;
- The manner in which the breach was the proximate cause of injury;
- The names of all health professionals and facilities notified.

A defective NOI does not toll the SOL and can be fatal. *Bush v
Shabahang*, 484 Mich 156 (2009), permits good-faith amendment of a
defective NOI in some circumstances — but do not rely on cure.

### Affidavit of Merit — MCL 600.2912d

The plaintiff **must file an Affidavit of Merit (AOM)** signed by a
qualifying health professional **with the complaint** (a single
28-day extension is available for good cause). The AOM must state
the standard of care, the breach, the actions that should have been
taken, and the manner in which the breach caused injury.

- **Failure to file an AOM** with the complaint generally means the
  complaint **does not toll the SOL** and is subject to dismissal.
  *Scarsella v Pollak*, 461 Mich 547 (2000).

### Expert qualifications — MCL 600.2169

The standard-of-care expert (for the AOM and at trial) must satisfy
the **matching-specialty** rule — same board certification / same
specialty as the defendant, and (the year before the alleged
malpractice) devoted a majority of professional time to active
clinical practice or instruction in the relevant specialty.

### Non-economic damages caps — MCL 600.1483

Medical-malpractice **non-economic** damages are capped:

- A **lower (standard) cap** and a **higher (catastrophic) cap** —
  the higher cap applies to enumerated catastrophic injuries
  (e.g., hemiplegia/paraplegia/quadriplegia from brain or spinal-
  cord injury, permanent loss of cognitive capacity, permanent loss
  of a reproductive organ).
- **Both caps are adjusted for inflation annually.** Do **not**
  hardcode a dollar figure — **point to corpus / the State Court
  Administrative Office's current-year table** for the operative
  amount on the date of judgment.

Economic damages (medical expenses, wage loss, lost earning
capacity) are **not** capped.

## Wrongful death — MCL 600.2922

Michigan consolidates wrongful-death and survival claims into a
single **wrongful-death action** (the "wrongful-death saving
statute"):

- The action is brought by the **personal representative** of the
  decedent's estate.
- It runs on the **SOL of the underlying claim** (e.g., 3-year
  negligence, or the med-mal clock for a malpractice death), with
  the **MCL 600.5852 saving statute** giving the personal
  representative additional time to bring a survived claim —
  confirm the interaction with the underlying SOL.
- **Damages** include conscious pain and suffering of the decedent
  before death, loss of financial support, and the **loss of
  society and companionship** of surviving family members under
  MCL 600.2922(6).
- A wrongful-death settlement requires **probate-court approval**
  and distribution among statutory beneficiaries.

## Governmental immunity — the GTLA, MCL 691.1401 et seq.

Claims against the State, counties, municipalities, school
districts, and other governmental agencies are governed by the
**Governmental Tort Liability Act**.

**Critical mechanics**:

- **Broad immunity is the default.** MCL 691.1407(1) immunizes a
  governmental agency engaged in the exercise or discharge of a
  **governmental function**. The claim **must fit a statutory
  exception** or it fails. The exceptions:
  - **Highway exception** — MCL 691.1402 (failure to keep highways
    in reasonable repair), with a strict pre-suit **notice
    requirement** under **MCL 691.1404** (typically 120 days).
  - **Motor-vehicle exception** — MCL 691.1405 (negligent operation
    of a government-owned vehicle).
  - **Public-building exception** — MCL 691.1406 (dangerous /
    defective public building).
  - Proprietary-function, governmental-hospital, and sewage-disposal
    exceptions also exist — confirm scope in corpus.
- **Individual employees** — MCL 691.1407(2) immunizes employees
  unless their conduct amounted to **gross negligence** that was
  "the proximate cause" of the injury. *Robinson v City of Detroit*,
  462 Mich 439 (2000), construes "the proximate cause" as **the one
  most immediate** cause — a demanding standard.
- **Notice and timing traps** — several exceptions carry their own
  short pre-suit notice clocks (the highway exception's 120-day
  notice under MCL 691.1404 is the classic). **Calendar these
  separately from the underlying SOL.**

## High-yield Michigan PI checks

1. **What's the SOL?** General PI 3 years (MCL 600.5805); med-mal
   2-year / 6-month-discovery / 6-year repose (MCL 600.5838a);
   PIP 1 year + one-year-back (MCL 500.3145).
2. **Auto case?** Is it first-party PIP, third-party tort, or both?
   Does the injury meet the **MCL 500.3135 threshold** (death,
   permanent serious disfigurement, or **serious impairment of body
   function** under *McCormick*)? Date-of-accident PIP election
   tier and fee schedule (2019 reforms)?
3. **Comparative fault?** Plaintiff more than 50% at fault → **no
   non-economic recovery** (MCL 600.2959). Non-parties at fault
   identified? Several-liability allocation (MCL 600.6304(4))?
   Defense MCR 2.112(K) non-party notice?
4. **Medical malpractice?** **182-day NOI** (MCL 600.2912b) +
   **AOM filed with complaint** (MCL 600.2912d) + matching-specialty
   expert (MCL 600.2169) + non-economic cap (MCL 600.1483, current-
   year inflation figure)?
5. **Governmental defendant?** Does the claim fit a GTLA exception
   (highway / motor-vehicle / public-building)? **Pre-suit notice**
   clock (e.g., 120 days under MCL 691.1404)? Gross-negligence /
   "the proximate cause" standard for individual employees?
6. **Products case?** Defect + causation (MCL 600.2946); FDA /
   government-regulation compliance presumption (MCL 600.2946(4));
   non-manufacturer-seller protection (MCL 600.2947(6));
   knowledge-of-defect exception that defeats those defenses
   (MCL 600.2949a); cap under MCL 600.2946a (current figure)?
7. **Wrongful death?** Personal representative appointed? Underlying
   SOL + MCL 600.5852 saving statute? Loss-of-society damages
   (MCL 600.2922(6))? Probate approval of any settlement?

## Drafting checklist

- [ ] Confirm the **3-year SOL** (or the med-mal / PIP clock) is not
      running out within 30 days.
- [ ] In an **auto** case, plead the **MCL 500.3135 threshold** with
      specificity — objectively manifested, important body function,
      effect on general ability to lead a normal life (*McCormick*).
- [ ] Plead **comparative fault** awareness — non-economic recovery
      is barred above 50% fault (MCL 600.2959); address any defense
      MCR 2.112(K) non-party notice and move to add necessary
      defendants.
- [ ] For **medical malpractice**, send the **182-day NOI** with all
      MCL 600.2912b(4) elements before filing; file the **AOM with
      the complaint** under MCL 600.2912d; confirm the expert
      satisfies MCL 600.2169.
- [ ] In the damages prayer, **point to the current-year MCL 600.1483
      / 600.2946a cap figure** rather than hardcoding an amount;
      separate economic (uncapped) from non-economic (capped).
- [ ] For a **governmental defendant**, draft to a **GTLA exception**
      and serve any required **pre-suit notice** (e.g., MCL 691.1404)
      on its own clock.
- [ ] For a **products** case, name the manufacturer and assess the
      non-manufacturer-seller protection (MCL 600.2947(6)) and the
      FDA / government-regulation compliance presumption
      (MCL 600.2946(4)).
- [ ] For **wrongful death**, confirm a personal representative is
      appointed and plead under MCL 600.2922 with loss-of-society
      damages.

## Composition

- For statewide format and caption: `mi-statewide-format`
- For Circuit Court venue: `mi-wayne`, `mi-oakland`,
  `mi-circuit-courts`
- For District Court (≤ $25k) venue: `mi-district-courts`,
  `mi-36th-district`
- For first responsive pleading: `mi-first-30-days`
- For drafting motions / declarations / orders: `mi-draft-motion`,
  `mi-draft-declaration`, `mi-draft-order`
- For SOL / NOI / notice-of-claim clocks: `mi-deadlines`
- For discovery: `mi-discovery`
- For QC: `mi-quality-check`, `mi-fact-check`

## References

- `mi-law-references` — MCL, MCR, MRE, and federal symlinks
- MCL 600.5805 — general 3-year personal-injury / property SOL
- MCL 600.5838a — medical-malpractice SOL + 6-year repose
- MCL 600.2959 — modified comparative fault (51% non-economic bar)
- MCL 600.6304 — allocation of fault + several liability
- MCL 500.3101 et seq. — no-fault automobile insurance regime
- MCL 500.3105–3107 / 3107c / 3157 — PIP benefits + 2019 reforms
- MCL 500.3135 — third-party tort threshold
- MCL 500.3145 — PIP 1-year SOL + one-year-back rule
- MCL 600.2945–2949a — products liability
- MCL 600.2912b — 182-day Notice of Intent (med-mal)
- MCL 600.2912d — Affidavit of Merit (med-mal)
- MCL 600.2169 — expert qualifications (med-mal)
- MCL 600.1483 — medical-malpractice non-economic caps (inflation-
  adjusted; see current-year figure in corpus)
- MCL 600.2922 / 600.5852 — wrongful death + saving statute
- MCL 691.1401 et seq. — Governmental Tort Liability Act
- MCL 691.1402 / 691.1404 / 691.1405 / 691.1406 / 691.1407 — GTLA
  exceptions + highway notice + employee immunity
- MCR 2.112(K) — notice of non-party fault
- *McCormick v Carrier*, 487 Mich 180 (2010) — serious impairment
  of body function
- *Robinson v City of Detroit*, 462 Mich 439 (2000) — GTLA "the
  proximate cause" standard
- *Scarsella v Pollak*, 461 Mich 547 (2000) — AOM filing requirement
- *Bush v Shabahang*, 484 Mich 156 (2009) — NOI amendment
