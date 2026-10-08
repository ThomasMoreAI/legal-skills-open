---
name: in-first-30-days-codearranger
title: Indiana — First 30 Days After Service
description: 'This skill should be used when an Indiana defendant has just been served with a civil complaint and asks "I was just sued in Indiana", "I have 20 days to answer", "Trial Rule 6(C)", "Indiana answer template", "T.R. 12(B)(6) motion to dismiss", "Indiana affirmative defenses", "counterclaim Indiana", "default judgment Indiana T.R. 55", "what to do after being served Indiana", "Indiana civil summons response", or any related first-response question. Covers the 20-day answer deadline under T.R. 6(C), the T.R. 12(B) motion-to-dismiss framework (especially T.R. 12(B)(6) failure to state a claim), affirmative defenses catalog under T.R. 8(C), compulsory counterclaims under T.R. 13(A), default-judgment risk under T.R. 55, and the Appearance form under T.R. 3.1. Trigger phrases: "just been served Indiana", "20 days T.R. 6(C)", "T.R. 12(B)(6)", "Indiana motion to dismiss", "Indiana answer", "Indiana affirmative defenses", "T.R. 13 counterclaim", "T.R. 55 default".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Indiana — First 30 Days After Service

This skill is the procedural compass for an Indiana civil
defendant in the first 30 days after service. The 20-day answer
window under T.R. 6(C) is **the hardest deadline in Indiana
civil practice** — missing it triggers default judgment under
T.R. 55, which is then much harder to undo than to file the
answer in the first place.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify the date of service, the cause number, and the venue
> court's local rules before filing. Pro se defendants are
> strongly encouraged to use Indiana Legal Services or the local
> Self-Help Center within the first week.

## The 20-day clock — Trial Rule 6(C)

T.R. 6(C) sets the answer deadline:

> "A responsive pleading required under these rules shall be
> served within 20 days after service of the prior pleading."

Computation:

- **Day 0**: the day the Summons + Complaint is served
- **Day 1**: the first day counted under T.R. 6(A) — exclude the
  day of the event, include the last day
- **Day 20**: the answer (or first responsive motion) is due
- **If Day 20 is a weekend or IC 1-1-9-1 legal holiday**: the
  deadline extends to the next non-holiday day (T.R. 6(A))

Use `case-calendar.py --from YYYY-MM-DD --rule answer-due` to
compute the exact deadline.

**Service-by-mail (T.R. 4.1)**: When the Summons is served by
certified mail, the clock starts on the date the green card is
signed, NOT the date the certified packet was mailed. The 20-day
clock then runs from the green-card date.

## Step 1 — Verify service

Before doing anything else, confirm:

- The Summons names YOU (not a similar-name person)
- The cause number is real and matches the Complaint
- The service method is one of T.R. 4.1 (personal), 4.4
  (nonresident), 4.6 (organization), 4.12 (process-server), or
  T.R. 4.1(A) (certified mail with green card)
- The Summons states the court (Circuit, Superior, County
  Division) and the venue county
- The Complaint identifies the case type (PL, CC, CT, etc.) and
  the named defendants

If service is defective (e.g., served on someone other than the
named defendant, no green card returned), the appropriate motion
is **T.R. 12(B)(2) — lack of personal jurisdiction** or T.R.
12(B)(4)/(5) — insufficient process or service of process. These
must be raised in the first responsive pleading or they are
waived under T.R. 12(H)(1).

## Step 2 — Choose the response

Three primary options:

1. **Answer** (T.R. 8(B)): admit / deny each numbered paragraph,
   assert affirmative defenses, plead counterclaims if any
2. **Motion to Dismiss** (T.R. 12(B)): assert a procedural defect
   or T.R. 12(B)(6) failure to state a claim
3. **Both** — file a 12(B) motion AND an answer simultaneously
   (T.R. 12 permits this; many Marion defendants do it as a
   belt-and-suspenders approach)

Either filing satisfies T.R. 6(C); both forms toll default
judgment.

## The Answer — Trial Rule 8(B)

T.R. 8(B) requires the defendant to:

- Admit or deny each averment in the Complaint, paragraph by
  paragraph
- A general denial only suffices if the defendant denies "every
  averment of the pleading" — extremely rare in practice
- Use the formula: "Admitted." / "Denied." / "Lacking
  sufficient information to admit or deny, the defendant denies."
- The "lacking sufficient information" denial under T.R. 8(B)
  is functionally a denial that requires the plaintiff to prove
  the allegation

Indiana's pleading standard:

- *Warne v. Hall*, 373 P.3d 588 (Colo. 2016) is **NOT** Indiana
  law. Indiana retains the **liberal "notice pleading" standard**
  under T.R. 8(A); the plaintiff need only give "a short and
  plain statement of the claim showing that the pleader is
  entitled to relief"
- *Bushong v. Williamson*, 790 N.E.2d 467 (Ind. 2003), confirms
  that Indiana follows liberal notice pleading
- The Federal *Twombly* / *Iqbal* plausibility standard is NOT
  the Indiana standard

## Motion to Dismiss — Trial Rule 12(B)

T.R. 12(B) enumerates seven grounds for pre-answer dismissal:

| Ground | Rule | Standard |
|--------|------|----------|
| Lack of subject-matter jurisdiction | 12(B)(1) | Court has no power to hear this type of case |
| Lack of personal jurisdiction | 12(B)(2) | Insufficient contacts; service defect |
| Incorrect venue | 12(B)(3) | Wrong county under T.R. 75 |
| Insufficient process | 12(B)(4) | Summons defective |
| Insufficient service of process | 12(B)(5) | Service method defective |
| Failure to state a claim | 12(B)(6) | Even taking all allegations as true, the law affords no remedy |
| Failure to join indispensable party | 12(B)(7) | T.R. 19 party missing |

The most-used: **T.R. 12(B)(6)** — failure to state a claim.
Standard: the court accepts all well-pleaded allegations as true
and asks whether, under any conceivable set of facts, the
plaintiff would be entitled to relief (*Trail v. Boys & Girls
Clubs of Northwest Ind.*, 845 N.E.2d 130 (Ind. 2006)).

**Waiver rules under T.R. 12(H)(1)**: The procedural defenses
(12(B)(2)-(5)) are waived if not raised in the first responsive
filing. The substantive defenses (12(B)(1), (6), (7)) may be
raised at any time before final judgment.

## Affirmative Defenses — Trial Rule 8(C)

Affirmative defenses MUST be pleaded in the Answer or they are
waived. T.R. 8(C) lists 19 named affirmative defenses; the
defendant should plead any that apply. Common defenses in
consumer-debt cases:

| Defense | When applicable |
|---------|-----------------|
| Statute of limitations | Claim is outside the IC 34-11 SOL (6/10 years) |
| Payment | Defendant paid the debt |
| Accord and satisfaction | Settlement was reached |
| Estoppel | Plaintiff's prior conduct prevents the claim |
| Failure of consideration | Defendant received no benefit |
| Release | Prior release of the claim |
| Res judicata | Prior judgment between the parties |
| Statute of frauds | Contract required to be in writing |
| Waiver | Plaintiff's prior conduct waived the right |
| Lack of standing | Plaintiff is not the real party in interest |
| Lack of capacity | Plaintiff is not licensed / authorized |
| Fraud | Plaintiff procured the contract by fraud |
| Duress | Defendant signed under coercion |
| Mistake | Mutual or unilateral mistake of fact |
| Illegality | Contract violates law or public policy |
| Set-off | Plaintiff owes defendant on another claim |
| FDCPA violations | If plaintiff is a debt collector |
| DCSA violations (IC 24-5-0.5) | Indiana UDAP defense |

The **chain-of-title defense** in debt-buyer cases is technically
a "lack of standing" or "real party in interest" defense under
T.R. 17(A) — see `in-consumer-debt` for the full template.

## Counterclaims — Trial Rule 13

T.R. 13(A) creates **compulsory counterclaims**: any claim the
defendant has against the plaintiff arising out of the
transaction or occurrence that is the subject matter of the
plaintiff's claim MUST be pleaded in the Answer, or it is barred.

T.R. 13(B) creates **permissive counterclaims**: claims arising
from a different transaction may be pleaded but are not required.

**In consumer-debt defense**: FDCPA, DCSA, and IUCCC counterclaims
arising from the collection conduct are compulsory under T.R.
13(A) because they arise from the same transaction or occurrence
(the collection effort). File them in the Answer or lose them.

## Cross-claims and third-party complaints

- **Cross-claim** (T.R. 13(G)): claim by one defendant against a
  co-defendant arising from the same transaction
- **Third-party complaint** (T.R. 14): defendant brings in a new
  party who may be liable for all or part of the plaintiff's
  claim (e.g., indemnitor)

## Default judgment risk — Trial Rule 55

If the defendant fails to answer within 20 days (and no extension
is granted), the plaintiff may move for default judgment under
T.R. 55:

- **T.R. 55(A) — entry of default**: clerk's entry; ministerial
  upon affidavit of non-appearance
- **T.R. 55(B) — default judgment**: court enters judgment;
  damages must be supported by affidavit or evidentiary hearing
- **T.R. 55(C) — setting aside default**: court may set aside
  default judgment under T.R. 60(B) (excusable neglect +
  meritorious defense; see `in-post-judgment`)

**The "meritorious defense" trap**: setting aside a default
requires showing both (1) why the answer was missed and (2) that
defendant has a meritorious defense. A pro se defendant who
simply asks "please let me defend" without alleging a defense
will be denied.

## The 30-day workflow

```
Day 0      Served with Summons + Complaint
Day 1      Read the Complaint twice; identify case type
Day 2      Use case-calendar.py to compute Day 20
Day 3      Calendar reminders for Day 10 (review) and Day 17
           (final draft)
Day 4-7    Gather facts; pull contracts, payments, correspondence
Day 8-10   Identify affirmative defenses (see table above)
Day 11-14  Draft the Answer; identify compulsory counterclaims
Day 15-17  Final draft; quality-check with in-quality-check
Day 18     E-file via Odyssey; serve all parties via Service
           Contacts; pay $177 filing fee for Civil Appearance
           (or claim indigent status)
Day 19-20  Confirm Odyssey acceptance; print file-stamped copy
Day 30     Affirmative defenses fully developed; first set of
           discovery prepared
Day 60     Joint CMS prepared (Marion / Hamilton); first status
           conference setting
```

## Composition

- `in-statewide-format` for T.R. 5(E) / T.R. 10 caption + format
- `in-pro-se` for self-represented Appearance + Answer
  conventions
- `in-deadlines` for the 20-day, 30-day, and 1-year T.R. 60(B)
  windows
- `in-discovery` for the first wave of discovery responses
- `in-draft-motion` for T.R. 12(B)(6) motion drafting
- `in-draft-declaration` for affirmative-defense factual support
- `in-consumer-debt` for debt-collection-specific affirmative
  defenses and counterclaims

## References

- `references/answer-template.md` — full T.R. 8(B) answer
  scaffold with affirmative defenses
- `references/motion-to-dismiss-template.md` — T.R. 12(B)(6)
  scaffold
- `references/affirmative-defenses-bank.md` — pre-drafted
  affirmative defense language
- `references/compulsory-counterclaim-checklist.md` — T.R. 13(A)
  analysis worksheet
- `references/appearance-form.md` — T.R. 3.1 Appearance with
  examples

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
