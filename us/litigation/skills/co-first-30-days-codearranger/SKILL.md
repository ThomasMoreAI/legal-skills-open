---
name: co-first-30-days-codearranger
title: Colorado — First 30 Days After Service
description: This skill should be used when a Colorado defendant has just been served with a civil complaint or petition. Triggers include "answer Colorado complaint", "I was sued in Colorado", "served with a summons in Colorado", "21 days to answer Colorado", "motion to dismiss Colorado", "C.R.C.P. 12(b)(5)", "affirmative defenses Colorado", "counterclaim Colorado", "default judgment Colorado", "first 30 days after being sued". Covers the C.R.C.P. 12 answer window (21 days for in-state defendants, 35 for out-of-state), the C.R.C.P. 12(b) motion-to-dismiss triage, affirmative defenses catalog including consumer-protection-act defenses, counterclaim and cross-claim mechanics, and the default-judgment risk timeline.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Colorado — First 30 Days After Service

> **NOT LEGAL ADVICE.** Time is short. This skill helps a defendant
> sketch a response and surface the most important deadlines, but
> consult a licensed Colorado attorney about substantive defenses
> when possible.

Use this skill when the defendant has **just been served** with a
civil complaint, petition, or notice. It frames the first 30 days
after service — the window in which the defendant must answer,
move to dismiss, or risk default.

## The clock

C.R.C.P. 12(a) sets the answer deadline:

| Defendant | Deadline | Authority |
|---|---|---|
| Colorado resident, in-state personal service | **21 days** after service | C.R.C.P. 12(a)(1) |
| Out-of-state defendant, personally served | **35 days** after service | C.R.C.P. 12(a)(2) |
| Service by publication / mail (when court order) | **35 days** | C.R.C.P. 4(g) / 12(a)(3) |
| Counterclaim or cross-claim (reply) | **21 days** | C.R.C.P. 12(a)(3) |
| Response to amended complaint | **14 days** (or remainder of original time, whichever is longer) | C.R.C.P. 15(a) |

Compute with `co-deadlines` — the C.R.C.P. 6(a)(1)(C) roll-forward
applies if the deadline lands on a Saturday, Sunday, or Colorado
legal holiday.

> ⚠ **Default risk**: if the defendant does not answer or move
> within the window, the plaintiff may move for **default
> judgment** under C.R.C.P. 55(b). Once entered, default is hard
> (but not impossible — see `co-post-judgment` on C.R.C.P. 60(b)) to
> set aside.

## Day-by-day playbook

### Days 0-3 — read the complaint carefully

- **Read every paragraph**. Note who is suing, on what claims, for
  what relief. List the alleged contracts, accounts, or events.
- **Note the case number, court, and division** — these go on every
  response.
- **Note the case type**:
  - `CV` district court civil
  - `C0` county court civil (≤ $25,000)
  - `S0` small claims (≤ $7,500)
  - `DR` domestic relations
  - `PR` probate
- **Check service**. Was the defendant **personally served**? Left
  with someone at the residence? Posted on the door? Service
  defects are gold-standard defenses — see C.R.C.P. 4 and
  *Goodman Assocs., LLC v. WP Mountain Props., LLC*, 222 P.3d 310
  (Colo. 2010).

### Days 3-10 — choose the response strategy

The defendant has three principal paths:

1. **Answer** — admit, deny, or claim lack of knowledge for each
   numbered paragraph; assert affirmative defenses; assert any
   counterclaims.
2. **Motion to Dismiss** under C.R.C.P. 12(b) — challenges the
   pleading without answering on the merits. If the motion is
   denied, the answer is then due **14 days** after the order
   (C.R.C.P. 12(a)(4)).
3. **Motion for More Definite Statement** under C.R.C.P. 12(e) — when
   the complaint is so vague the defendant cannot reasonably respond.
   Rarely useful; courts disfavor.

### C.R.C.P. 12(b) defenses — when to move to dismiss

C.R.C.P. 12(b) lists seven defenses that may be raised by motion
instead of (or in addition to) the answer:

- **12(b)(1)** lack of subject matter jurisdiction
- **12(b)(2)** lack of personal jurisdiction
- **12(b)(3)** improper venue
- **12(b)(4)** insufficient process
- **12(b)(5)** failure to state a claim upon which relief can be
  granted (the most common — Colorado's analog to FRCP 12(b)(6))
- **12(b)(6)** insufficient service of process
- **12(b)(7)** failure to join a party under C.R.C.P. 19

A C.R.C.P. 12(b)(5) motion is the most common pre-answer motion;
Colorado applies the **Twombly/Iqbal-equivalent plausibility
standard** under *Warne v. Hall*, 2016 CO 50, replacing the older
"no set of facts" test.

> ⚠ **Defense waiver**: 12(b)(2), (3), (4), (5) defenses are waived
> if not raised in the first responsive pleading (C.R.C.P. 12(h)).
> 12(b)(1) and (b)(7) are not waivable.

### Days 10-21 — draft the answer (or the motion)

#### Answer structure

```
                  ANSWER, AFFIRMATIVE DEFENSES,
                       AND COUNTERCLAIMS

Defendant John Doe (the "Defendant"), pro se, responds to
Plaintiff's Complaint as follows:

                          ANSWER

1. Defendant denies the allegations in paragraph 1.

2. Defendant lacks knowledge or information sufficient to form a
   belief about the truth of the allegations in paragraph 2 and
   therefore denies them.

3. Defendant admits the allegations in paragraph 3.

[...]

                  AFFIRMATIVE DEFENSES

4. First Affirmative Defense — Statute of Limitations.
   Plaintiff's claims are barred in whole or in part by the
   applicable statute of limitations under C.R.S. § 13-80-103.5.

5. Second Affirmative Defense — Failure to State a Claim.
   Plaintiff has failed to state a claim upon which relief may be
   granted under C.R.C.P. 12(b)(5).

[...]

                       COUNTERCLAIMS

[If asserting counterclaims, plead them as a separate complaint-
style block with numbered factual allegations and named claims.]

                          PRAYER FOR RELIEF

WHEREFORE, Defendant respectfully requests that the Court:

A. Enter judgment in favor of Defendant and against Plaintiff;
B. Dismiss Plaintiff's Complaint with prejudice;
C. Award Defendant attorneys' fees and costs as allowed by law;
D. Grant such other relief as the Court deems just and proper.
```

#### Standard affirmative-defense catalog (C.R.C.P. 8(c))

Plead all that may apply; failure to plead an affirmative defense in
the answer typically waives it.

- Accord and satisfaction
- Arbitration / award
- Assumption of risk
- Comparative negligence
- Discharge in bankruptcy
- Duress
- Estoppel
- Failure of consideration
- Fraud
- Illegality
- Injury by fellow servant
- Laches
- License
- Payment
- Release
- Res judicata / claim preclusion
- Statute of frauds
- **Statute of limitations** (very common; see SOL chart below)
- Waiver

**Subject-matter-specific defenses** (use `co-consumer-debt` for the
full debt-buyer affirmative-defense list, including standing/chain of
title, CFDCPA licensure, account stated, lack of meeting of the
minds, etc.).

### Statute of limitations — Colorado quick chart

| Claim | SOL | Authority |
|---|---|---|
| Liquidated debt / written instrument | **6 years** | C.R.S. § 13-80-103.5(1)(a) |
| Tort and most general civil actions | **2 years** | C.R.S. § 13-80-102 |
| Personal injury motor vehicle | **3 years** | C.R.S. § 13-80-101(1)(n) |
| Fraud, breach of fiduciary duty | **3 years** | C.R.S. § 13-80-101(1)(c) |
| CCPA (Consumer Protection Act) | **3 years** from accrual | C.R.S. § 6-1-115 |
| CFDCPA (state debt-collection law) | **1 year** from violation | C.R.S. § 5-16-113(4) |
| FDCPA (federal) | **1 year** from violation | 15 U.S.C. § 1692k(d) |
| Slander, libel | **1 year** | C.R.S. § 13-80-103(1)(a) |

### Counterclaims

C.R.C.P. 13 governs counterclaims:

- **Compulsory counterclaim** (13(a)): any claim arising out of the
  same transaction or occurrence — **must** be pleaded or it is
  waived
- **Permissive counterclaim** (13(b)): unrelated claim — may be
  pleaded
- A pro se filer should plead **all known counterclaims** at the
  time of answer; do not assume that something "isn't really part
  of this case" — Colorado courts apply compulsory-counterclaim
  preclusion strictly

### Cross-claims

C.R.C.P. 13(g) governs cross-claims against co-parties (same side
of the v.). Less common in two-party cases.

## Filing the answer / motion

- **E-file** through CCEFS (attorneys mandatory; pro se where
  available)
- **Pay the answer/response filing fee** (~$192 district court;
  lower in county court) or file JDF 205/206 for fee waiver
- **Serve the answer** on all parties per C.R.C.P. 5 (CCEFS
  e-service or by mail / hand delivery / email)
- **Include a Certificate of Service**

## After filing the answer

The case is now **at issue**, which triggers:

- C.R.C.P. 16(b) case-management clock starts
- C.R.C.P. 26(a)(1) initial disclosures due **28 days** after at-issue
- Initial CMC ~49 days after at-issue
- Discovery may now be served (see `co-discovery`)

## Composition

- For statewide format: `co-statewide-format`
- For drafting the answer / motion / declaration:
  `co-draft-motion`, `co-draft-declaration`
- For the specific court: `co-denver`, `co-arapahoe`,
  `co-county-courts`
- For deadlines arithmetic: `co-deadlines`
- For matter-specific defenses: `co-consumer-debt`, `co-family-law`

## References

- `references/answer-template.md` — full answer scaffold
- `references/motion-to-dismiss-template.md` — C.R.C.P. 12(b)(5)
  template
- `references/affirmative-defense-catalog.md` — annotated catalog
- `references/counterclaim-checklist.md`
- `references/service-defects.md` — C.R.C.P. 4 service-of-process
  analysis with case authority
- `references/default-prevention.md` — how the default clock works
  and how to interrupt it
