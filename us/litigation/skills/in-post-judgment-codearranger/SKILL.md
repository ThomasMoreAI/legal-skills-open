---
name: in-post-judgment-codearranger
title: Indiana Post-Judgment Procedure
description: 'Use for post-judgment matters in Indiana — **T.R. 59 motion to correct error** (Indiana-specific, 30-day, jurisdictional), **T.R. 60(B) relief from judgment**, **T.R. 69 proceedings supplemental** (judgment debtor exam, garnishment), exemptions under **IC 34-55-10**, federal **CCPA / IC 24-4.5-5-105** wage-garnishment cap (25%), judgment satisfaction, and appeal mechanics. Triggers: "T.R. 59 motion", "T.R. 60(B)", "Indiana wage garnishment", "garnishment exemption", "Indiana homestead exemption".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Indiana Post-Judgment Procedure

This skill covers everything that happens after a final judgment
is entered: post-trial motions, appeals, garnishment, debtor
examinations, supplemental proceedings, exemption claims, and
judgment satisfaction. Indiana has a unique post-trial procedural
device — the **Motion to Correct Error under T.R. 59** — that has
no direct federal analog and is a required preliminary step for
some appeals.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against current Indiana Trial Rules, Indiana Code, and
> case law before filing. Post-judgment deadlines are strict and
> jurisdictional.

## Trial Rule 59 — Motion to Correct Error (Indiana-specific)

T.R. 59 is the Indiana procedural device for raising errors
allegedly committed during trial or in the entry of judgment.
**Critical features**:

- **Filing deadline**: 30 days from the entry of final judgment
  (T.R. 59(C)). This is jurisdictional — late filings are
  dismissed for lack of jurisdiction.
- **No deadline extension**: T.R. 6(B) does not authorize
  extending the T.R. 59 deadline; *Cavinder Elevators, Inc. v.
  Hall*, 726 N.E.2d 285 (Ind. 2000).
- **Mandatory for some appeals**: Under Ind. App. R. 9(A)(1),
  certain issues must be raised in a T.R. 59 motion to be
  preserved for appeal — most importantly, issues about jury
  instructions, evidentiary rulings, and the sufficiency of the
  evidence.
- **Form**: state with specificity the alleged errors and the
  relief sought.
- **Ruling timeline**: T.R. 59(B) gives the trial court 45 days
  to rule; if no ruling, the motion is **deemed denied** and the
  appeal clock starts.

**Issues that require a T.R. 59 motion**:

- Newly discovered evidence (T.R. 59(A)(1))
- Excessive or inadequate damages (T.R. 59(A)(4))
- Sufficiency of the evidence (T.R. 59(A)(7))
- Verdict against the weight of the evidence
- Trial-court errors in evidentiary rulings or jury instructions

Issues that do NOT require T.R. 59 (preserved on the record):

- Pure legal questions ruled on before judgment
- Constitutional issues raised below

## Trial Rule 60(B) — Relief from Judgment

T.R. 60(B) is the equitable mechanism for setting aside a final
judgment. Tracks federal Rule 60(b) closely, with three Indiana-
specific differences:

| T.R. 60(B) Ground | Deadline | Standard |
|-------------------|----------|----------|
| (1) Mistake, surprise, excusable neglect | 1 year | Indiana applies a relaxed "any reasonable basis" standard for pro se defaults; *Smith v. Johnson*, 711 N.E.2d 1259 (Ind. 1999) |
| (2) Fraud, misrepresentation | 1 year | Clear and convincing evidence |
| (3) Newly discovered evidence | 1 year | Evidence material, not cumulative, could not have been discovered before trial |
| (4) Void judgment | "Reasonable time" | E.g., lack of personal jurisdiction; service defects |
| (5) Satisfied / released / discharged judgment | "Reasonable time" | Includes prior payment |
| (6) Any other reason justifying relief | "Reasonable time" | Equitable safety valve |
| (7) Mistake of fact in default judgment | 1 year | T.R. 60(B)(1) variant |
| (8) Meritorious defense to default | T.R. 60(B)(1)-(8) outer 1 year | Additional Indiana-specific provision |

**Most common post-judgment motion in consumer-debt cases**: T.R.
60(B)(1) — excusable neglect — to vacate a default judgment.
Required showing:

1. Explanation of why the answer was not filed within 20 days
   (e.g., never served, lost mail, illness)
2. Meritorious defense to the underlying claim (the defendant
   must allege facts that would defeat or reduce the judgment)
3. Motion filed within 1 year of judgment entry

The "meritorious defense" requirement is the Indiana-specific
catch — it is NOT just a procedural showing; the defendant must
allege facts that, if proved, would change the outcome.

## Trial Rule 69 — Proceedings Supplemental

T.R. 69 is the Indiana judgment-creditor's mechanism to discover
the judgment debtor's assets. Two main components:

### 1. Judgment debtor examination

The creditor files a "Verified Motion for Proceedings
Supplemental" or "Verified Motion in Aid of Execution." The court
issues an Order to Appear directing the debtor to appear at a
specified date and answer questions about assets.

- The motion must allege that the debtor has property subject to
  execution (a "good faith allegation" suffices)
- The debtor MUST appear; failure to appear = bench warrant +
  contempt
- The hearing is conducted under oath; the debtor must produce
  bank statements, employment records, asset lists
- Pro se debtors should bring exemption-claim forms

### 2. Garnishee defendant proceedings

To garnish wages or a bank account, the creditor names the
employer (or bank) as a "Garnishee Defendant" and serves a
Garnishee Summons under T.R. 4. The garnishee has 20 days to
answer.

## Wage garnishment cap

Indiana follows the federal Consumer Credit Protection Act
(CCPA) cap, which Indiana adopted at IC 24-4.5-5-105:

> **Cap**: 25% of disposable earnings per pay period, OR
> the amount by which disposable earnings exceed 30 times the
> federal minimum wage per week (currently 30 × $7.25 = $217.50),
> whichever is **lower**.

Calculation:
- Disposable earnings = gross pay - mandatory deductions (federal
  + state tax, FICA, FICA-M, mandatory retirement)
- Health insurance and voluntary deductions do NOT reduce
  disposable earnings

Garnishment is processed through the employer's payroll; the
employer remits the garnishment amount to the court (or the
creditor's attorney) each pay period.

**Exemption claims**: The debtor may file an exemption claim
under IC 34-55-10 with the court at any time during the
garnishment. Common exemptions:

| Property | Exemption | Statute |
|----------|-----------|---------|
| Homestead (residence) | $22,750 individual / $45,500 joint | IC 34-55-10-2(c)(1) |
| Tangible personal property | $11,375 | IC 34-55-10-2(c)(2) |
| Intangibles (money, bank accounts) | $475 | IC 34-55-10-2(c)(3) |
| Health aids | Full value | IC 34-55-10-2(c)(4) |
| Educational savings (529) | Full value | IC 34-55-10-2(c)(7) |
| Retirement accounts (qualified) | Full value | IC 34-55-10-2(c)(7) |
| Tools of the trade (professional) | $4,500 | IC 34-55-10-2(c)(8) |
| Unemployment / workers' comp benefits | Full value | IC 22-4-33-3 |
| Social Security benefits | Full value | Federal 42 U.S.C. § 407 |

The exemption amounts are indexed every six years (currently
effective March 1, 2022; next adjustment March 1, 2028).

## Judgment lien and renewal

A money judgment automatically becomes a lien on the debtor's
real property in the county where the judgment is entered (IC
34-55-9-2). The lien attaches at the time the judgment is
recorded with the County Recorder.

**Duration and renewal**:

- A judgment is enforceable for **20 years** from entry (IC
  34-55-1-2)
- May be renewed for additional 20-year periods by filing a
  motion before expiration
- The judgment lien on real property expires after 10 years (IC
  34-55-9-2) unless extended

## Satisfaction of Judgment

When the judgment is fully paid, the judgment creditor MUST file
a Satisfaction of Judgment (IC 34-55-9-3). The form is short:

```
STATE OF INDIANA              )  IN THE [COURT]
                              )  COUNTY OF [COUNTY]
[CREDITOR],                   )
              Plaintiff,      )  Cause No. [#####]
       v.                     )
[DEBTOR],                     )
              Defendant.      )

                  SATISFACTION OF JUDGMENT

Plaintiff [CREDITOR], by counsel, hereby acknowledges receipt
of full payment of the judgment entered in this cause on [DATE],
in the amount of $______, plus accrued interest. The judgment is
SATISFIED IN FULL.

Date: _______________

                              _______________________________
                              [PLAINTIFF'S COUNSEL], Atty. No.
```

The Satisfaction is filed with the clerk and recorded with the
County Recorder to clear the judgment lien from title. **Failure
of the creditor to file Satisfaction** within 14 days of full
payment exposes the creditor to a $100 penalty plus actual
damages under IC 34-55-9-3.

## Notice of Appeal — appellate procedure

If the case is appealable (final judgment), the Notice of Appeal
under Ind. App. R. 9 must be filed within **30 days** of the
final judgment OR within **30 days of the trial court's ruling
on a T.R. 59 motion**. The notice is filed in the trial court
(not the Court of Appeals) and identifies:

- The judgment being appealed
- The court to which the appeal is taken (Court of Appeals,
  district)
- The parties
- A request for the Clerk's Record

A bond may be required to stay execution pending appeal under
T.R. 62.

## Composition

- `in-statewide-format` for T.R. 5(E) / T.R. 10 baseline
- `in-marion` / `in-lake` / `in-county-courts` for venue
- `in-pro-se` for self-represented post-judgment relief
- `in-deadlines` for the 20-year judgment life and 30-day T.R.
  59 / appeal windows
- `in-draft-motion` for T.R. 60(B) motion scaffolders
- `in-consumer-debt` for collection-specific post-judgment issues

## References

- `references/tr59-vs-tr60.md` — comparison of the two relief
  mechanisms
- `references/exemption-claim-form.md` — IC 34-55-10 exemption
  claim form walkthrough
- `references/wage-garnishment-calc.md` — disposable-earnings
  worksheet
- `references/proceedings-supplemental.md` — judgment debtor
  exam procedure
- `references/satisfaction-of-judgment.md` — template + recording
  procedure

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
