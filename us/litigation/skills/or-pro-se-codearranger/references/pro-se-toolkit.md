# Pro Se Toolkit — Common Motions (Oregon)

This toolkit lists the most-frequently-needed motion types for
Oregon pro se litigants and points to the relevant rule, the
deadline, and the supporting skill in this plugin.

## Defense-side motions (you are the defendant)

### 1. Motion to dismiss for failure to state a claim — ORCP 21 A(8)

Oregon's analog to FRCP 12(b)(6). The complaint, accepting all
allegations as true, fails to state ultimate facts entitling
plaintiff to relief.

- **Deadline**: 30 days after service of summons (ORCP 7 C(2))
- **Effect**: tolls answer deadline until court rules
- **Skill**: `or-first-30-days` for the strategic analysis;
  `or-draft-motion` for the form

### 2. Motion to dismiss for lack of subject-matter jurisdiction — ORCP 21 A(1)

The court has no power to hear this case (e.g., wrong court,
amount in controversy too low for venue, federal preemption).

- **Deadline**: 30 days
- **Skill**: `or-first-30-days`

### 3. Motion to dismiss for insufficient service — ORCP 21 A(5)

Plaintiff failed to comply with ORCP 7. Must include facts
showing what went wrong.

- **Deadline**: 30 days
- **Skill**: `or-first-30-days`

### 4. Answer with affirmative defenses and counterclaims

Oregon answers must be specific (admit or deny each allegation
of the complaint).

- **Deadline**: 30 days after service (ORCP 7 C(2))
- **Skill**: `or-first-30-days` for defense + counterclaim
  strategy; `or-draft-declaration` for sworn factual support

### 5. Motion to compel — ORCP 46 A

If the opposing party fails to produce documents under ORCP
43 or refuses to answer at deposition under ORCP 39.

- **Prerequisite**: Meet-and-confer certification (UTCR 5.045 /
  local SLR)
- **Fees**: Mandatory fee-shifting under ORCP 46 A(4)(a)
- **Skill**: `or-discovery`

### 6. Motion to vacate default — ORCP 71 B

The Oregon analog to FRCP 60(b). Grounds:

- (1) Mistake, inadvertence, surprise, or excusable neglect
- (2) Newly discovered evidence
- (3) Fraud, misrepresentation, or misconduct of an adverse
  party
- (4) Judgment is void
- (5) Judgment satisfied, released, or discharged
- (6) Any other reason justifying relief

- **Deadline**: 1 year for grounds (1)–(3); "reasonable time"
  for others
- **Skill**: `or-post-judgment`

### 7. Motion for summary judgment — ORCP 47

The case can be decided as a matter of law on the undisputed
material facts. Requires admissible evidence on every element.

- **Deadline**: Per case schedule (typically 60 days before
  trial)
- **Reply rules**: ORCP 47 C; response 28 days, reply 7 days
- **Skill**: `or-draft-motion` + `or-quality-check`

### 8. Garnishment exemption / Challenge to Writ of Garnishment

When a creditor garnishes wages or bank accounts, the debtor
can claim exemptions under ORS 18.345–18.385 (head of
household, unemployment benefits, social security, etc.).

- **Deadline**: 30 days from garnishment notice
- **Skill**: `or-post-judgment`

### 9. Motion to set aside dismissal / re-open case

Under ORCP 71 or ORCP 54 (depending on the basis for dismissal).

- **Skill**: `or-post-judgment`

## Plaintiff-side motions (you are the plaintiff)

### 1. Motion for default — ORCP 69

When the defendant fails to answer within 30 days of service.

- **Process**: Apply for **Order of Default** first; then for
  **Default Judgment** with damages computation
- **Skill**: `or-draft-motion`

### 2. Motion for entry of judgment after arbitration award — ORS 36.425

After mandatory arbitration concludes, if no party requests
trial de novo within 20 days, the prevailing party moves for
judgment on the award.

- **Skill**: `or-draft-motion`

### 3. Motion for issuance of writ of execution / garnishment — ORS 18.600

Post-judgment collection.

- **Skill**: `or-post-judgment`

## Either-side motions

### 1. Motion to compel discovery — ORCP 46 A (see above)

### 2. Motion for protective order — ORCP 36 C

When discovery is overbroad, harassing, or seeks privileged
material.

### 3. Motion for sanctions — ORCP 17

The Oregon analog to FRCP 11; signed pleadings must have
factual and legal basis. ORS 20.105 separately authorizes fees
on objectively unreasonable positions.

### 4. Motion to amend pleading — ORCP 23

"Leave shall be freely given" — Oregon follows the federal
liberal-amendment standard.

### 5. Motion for continuance — UTCR 6.030

Show good cause. Local SLR may add notice requirements.

### 6. Motion for fee waiver — ORS 21.682

For litigants who cannot afford filing fees. Form available on
the OJD forms page.

## Workflow per motion type

For any motion:

1. Pick the rule and read it (ORCP / UTCR / SLR)
2. Compute the deadline (`or-deadlines`)
3. Draft the motion + memorandum (`or-draft-motion`)
4. Draft the declaration with exhibits
   (`or-draft-declaration`)
5. Draft the proposed order (`or-draft-order`)
6. Reserve a hearing date (`or-schedule-hearing`)
7. Draft the Notice of Hearing (`or-draft-note`)
8. Assemble the packet (`or-file-packet`)
9. QC the packet (`or-quality-check`)
10. Fact-check before filing (`or-fact-check`)
11. File via File and Serve and serve under ORCP 9
12. Deliver working copies if SLR requires
13. Prepare for the hearing (`or-hearings`)
14. After the ruling, submit the signed order
    (`or-submit-order`)

## Statute-of-limitations chart (defense focus)

| Claim type | SOL | Authority |
|------------|-----|-----------|
| Written contract | 6 years | ORS 12.080(1) |
| Open account / credit card | 6 years | ORS 12.080(2)–(4) |
| Oral contract | 6 years | ORS 12.080(1) |
| Statutory liability | 6 years | ORS 12.080(2) |
| Personal injury (most torts) | 2 years | ORS 12.110 |
| Fraud / mistake | 2 years from discovery, max 10 | ORS 12.110(1) |
| Real property | 10 years | ORS 12.040 |
| Judgment renewal | 10 years | ORS 18.182 |
| UTPA action | 1 year from discovery; 6-year repose | ORS 646.638(6) |
| FDCPA action | 1 year from violation | 15 USC § 1692k(d) |

Always **verify against the current ORS** before relying on a
SOL. The legislature has updated some of these recently.

## Disclaimer

This toolkit is a procedural index, not legal advice. Every
motion has factual and strategic dimensions that affect whether
it should be filed. Where the stakes are significant, consult a
licensed Oregon attorney through the OSB Lawyer Referral Service
(503-684-3763) or a Modest Means Panel.
