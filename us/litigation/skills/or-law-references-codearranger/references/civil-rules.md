# Oregon Rules of Civil Procedure — Rule-by-Rule Reference

The Oregon Rules of Civil Procedure (ORCP) are promulgated by
the **Council on Court Procedures** (CCP) under ORS 1.735 and
become effective on January 1 of odd-numbered years unless the
Legislative Assembly disapproves under ORS 1.735(2). The current
ORCP are available at:

**https://counciloncourtprocedures.org/**

and at:

**https://www.courts.oregon.gov/rules/Pages/orcp.aspx**

This reference summarizes the rules most frequently invoked in
civil practice. Pull verbatim text from the source above when
quoting in a brief.

> **NOT LEGAL ADVICE.** Verify every rule citation against the
> current ORCP — rules update on a two-year cycle.

## Rules at a glance

### ORCP 1 — Scope, citation, declarations under penalty of perjury

- **ORCP 1 A**: Scope; the ORCP govern procedure in all civil
  actions in circuit court.
- **ORCP 1 E**: A "declaration under penalty of perjury" in the
  form below may be used in lieu of a notarized affidavit:

  > "I hereby declare that the above statement is true to the
  > best of my knowledge and belief, and that I understand it
  > is made for use as evidence in court and is subject to
  > penalty for perjury."

  Or, equivalently, the shorter 28 USC § 1746-style form:

  > "I declare under penalty of perjury under the laws of the
  > State of Oregon that the foregoing is true and correct."

  Both are accepted statewide.

### ORCP 7 — Summons; service

- **ORCP 7 C(2)**: 30 days to answer after personal service in
  Oregon (counted from the date of service, excluding the day
  of service per ORCP 10 A).
- **ORCP 7 D(2)**: Methods — personal, substituted, office
  service, by mail (with consent or after another method
  failed), publication.
- **ORCP 7 D(3)**: Return of Service must be filed within 63
  days of service.
- **ORCP 7 E**: Who can serve — any non-party adult, sheriff,
  or process server.
- **ORCP 7 H**: Notice requirements for service in special
  proceedings.

### ORCP 9 — Service of pleadings and other papers

- **ORCP 9 A**: When service is required.
- **ORCP 9 B**: How served — personal delivery, mail, fax with
  consent, email or eService where authorized.
- **ORCP 9 C**: Mail rule — when service is by mail, **3
  additional days** are added to any prescribed response
  period.
- **ORCP 9 F**: Filing requirements.
- **ORCP 9 G**: Certificate of Service requirement.

### ORCP 10 — Time

- **ORCP 10 A**: Computing time — exclude the day of the
  triggering event; include the last day unless it falls on a
  weekend or legal holiday (ORS 187.010), in which case the
  period extends to the next business day.
- **ORCP 10 B**: When the period is less than 7 days,
  intermediate weekend / holiday days are excluded; for periods
  7 days or longer, intermediate weekend / holiday days are
  included.
- **ORCP 10 C**: 3-day mail rule (parallels ORCP 9 C).

Use `scripts/case-calendar.py` for deterministic date
arithmetic.

### ORCP 15 — Pleadings allowed

- Complaint, answer, reply, counterclaim, cross-claim, third-
  party complaint, fourth-party complaint.
- No reply to an answer is required unless the answer contains
  a counterclaim (ORCP 13).

### ORCP 17 — Signing of pleadings, sanctions

- Every pleading must be signed by an attorney or by the party
  (if pro se).
- The signature certifies the pleading is well-grounded in fact
  and warranted by law.
- Violation triggers sanctions (ORCP 17 C–E), which can include
  fees, costs, and other appropriate relief.

This is Oregon's analog to FRCP 11 and WA CR 11. ORS 20.105 is
the separate fees-for-objectively-unreasonable-positions statute.

### ORCP 21 — Defenses and objections; manner of presentation

The Oregon analog to FRCP 12 / WA CR 12. Defenses asserted as
motions:

- **ORCP 21 A(1)**: Lack of jurisdiction over the subject matter
- **ORCP 21 A(2)**: Lack of jurisdiction over the person
- **ORCP 21 A(3)**: Improper venue
- **ORCP 21 A(4)**: Insufficiency of service of summons
- **ORCP 21 A(5)**: Insufficiency of service of process
- **ORCP 21 A(6)**: That the party asserting the claim is not
  the real party in interest
- **ORCP 21 A(7)**: Failure to join a party under ORCP 29
- **ORCP 21 A(8)**: Failure to state ultimate facts sufficient
  to constitute a claim (the Oregon analog to FRCP 12(b)(6))
- **ORCP 21 A(9)**: Pendency of another action between the same
  parties for the same cause
- **ORCP 21 B**: Other defenses (motion for a more definite
  statement; motion to strike)
- **ORCP 21 D**: Time — defenses (1)–(8) must be raised by
  motion before responsive pleading or in the responsive
  pleading; failure can waive the defense (ORCP 21 G)

### ORCP 23 — Amended and supplemental pleadings

- Leave to amend "shall be freely given when justice so
  requires" (ORCP 23 A) — Oregon follows the federal liberal-
  amendment standard.
- Amendments relate back to the original pleading when they
  arise from the same conduct, transaction, or occurrence
  (ORCP 23 C).

### ORCP 36 — General scope of discovery

- **ORCP 36 B(1)**: Scope — relevant to a claim or defense,
  reasonably calculated to lead to admissible evidence, and
  proportional to the needs of the case.
- **ORCP 36 B(2)**: Limits — privileged matter; trial preparation
  materials (work product); experts.
- **ORCP 36 C**: Protective orders.

### ORCP 39 — Depositions

- **ORCP 39 A**: When taken — after action commenced, any party
  may take depositions.
- **ORCP 39 B**: Notice required (5 days for parties; 7 for
  non-parties).
- **ORCP 39 C**: Stenographic, audio, or video recording.
- **ORCP 39 I**: Use of depositions at trial.
- **Limit**: 10 depositions per side without leave (per ORCP 36
  practice; check current rule).

### ORCP 43 — Production of documents

- **ORCP 43 A**: Party may serve requests for production of
  documents and things on any other party.
- **ORCP 43 B**: Response within 30 days (45 days if served
  with summons).
- **Subject to ORCP 36 scope and ORCP 36 C protective orders**.

### ORCP 44 — Physical and mental examination

- For when physical or mental condition of a party is in
  controversy; requires good cause and a court order in most
  cases.

### ORCP 45 — Requests for admission

- **ORCP 45 A**: Party may serve requests for admission of
  facts, application of law to facts, genuineness of documents.
- **ORCP 45 B**: Response within 30 days; failure to respond
  deems the matter admitted.
- **ORCP 45 C**: Withdrawal/amendment of admissions.

### ORCP 46 — Failure to make discovery; sanctions

The Oregon analog to FRCP 37 / WA CR 37.

- **ORCP 46 A(1)**: Application for order compelling
  discovery — requires that the party seeking the order have
  "in good faith conferred or attempted to confer" with the
  opposing party (meet-and-confer requirement).
- **ORCP 46 A(2)**: Failure to answer at deposition or to
  produce.
- **ORCP 46 A(3)**: Award of expenses against the disobedient
  party — discretionary; but
- **ORCP 46 A(4)(a)**: **Mandatory** award of reasonable
  expenses (including attorney fees) on a successful motion to
  compel, "unless the court finds that the opposition to the
  motion was substantially justified or that other
  circumstances make an award of expenses unjust."

### ORCP 47 — Summary judgment

The Oregon analog to FRCP 56 / WA CR 56.

- **ORCP 47 A**: When the moving party may file (after pleadings
  closed, or 20 days after action commenced if movant is
  defendant).
- **ORCP 47 C**: Procedure:
  - Motion filed at least **60 days** before trial
  - Response due **20 days** after service of motion
  - Reply due **5 days** after service of response
  - Hearing must be **at least 11 days** after filing of reply
- **Standard**: "No genuine issue as to any material fact" and
  the moving party is "entitled to judgment as a matter of
  law" (ORCP 47 C).
- **Burden**: The moving party makes a prima facie showing; the
  burden then shifts to the non-moving party to designate
  specific facts showing a genuine issue. *Two Two v. Fujitec
  America, Inc.*, 355 Or 319 (2014); *Jones v. General Motors
  Corp.*, 325 Or 404 (1997).
- **Affidavits / declarations** must be on personal knowledge
  and contain admissible facts (ORCP 47 D).
- **Evidence in opposition** must establish a genuine issue;
  inferences are drawn favorably to the non-movant.

### ORCP 54 — Dismissal of actions

- **ORCP 54 A**: Voluntary dismissal — by notice before answer
  or motion for SJ; by court order otherwise.
- **ORCP 54 B**: Involuntary dismissal — failure to prosecute,
  failure to comply with rules or court order.
- **ORCP 54 E**: Costs and fees on dismissal.

### ORCP 67 — Judgment

- **ORCP 67 A**: A judgment is final and appealable when entered
  in the register.
- **ORCP 67 B**: Multiple parties / multiple claims —
  enumeration in the judgment of which claims / parties it
  resolves.
- **ORCP 67 C**: Money judgment must specify amount, interest
  rate, and party against whom rendered.

### ORCP 68 — Allowance and recovery of attorney fees and costs

- **ORCP 68 A**: Definitions.
- **ORCP 68 B**: When fees are recoverable (by statute,
  contract, or rule).
- **ORCP 68 C(2)**: Procedure — statement of fees filed within
  **14 days** of judgment.
- **ORCP 68 C(3)**: Objections within 14 days of statement.
- **ORCP 68 C(4)**: Court may resolve on the papers or hold a
  hearing; must make findings on the requested amount.
- **ORCP 68 C(5)**: Reasonableness factors (see ORS 20.075 for
  the substantive criteria).

### ORCP 69 — Default

- **ORCP 69 A**: Entry of default by the clerk when the party
  has failed to plead or otherwise defend.
- **ORCP 69 B**: Application — by motion of the prevailing
  party.
- **ORCP 69 C**: Default judgment — may be entered by the clerk
  if the claim is for a sum certain; otherwise by judicial
  determination.
- **ORCP 69 D**: Setting aside default — see ORCP 71.

### ORCP 71 — Relief from judgment or order

The Oregon analog to FRCP 60(b) / WA CR 60(b).

- **ORCP 71 A**: Clerical mistakes — correctable at any time.
- **ORCP 71 B**: Other reasons — motion within a "reasonable
  time" not exceeding 1 year for grounds (1)–(3):
  - (1) Mistake, inadvertence, surprise, or excusable neglect
  - (2) Newly discovered evidence
  - (3) Fraud, misrepresentation, or other misconduct of an
    adverse party
  - (4) Judgment is void (no time limit)
  - (5) Judgment satisfied, released, or discharged; or it is
    no longer equitable (reasonable time)
  - (6) Any other reason justifying relief (reasonable time)

### ORCP 81 — Construction; effective dates

- **ORCP 81 A**: Construction — rules construed to secure just,
  speedy, and inexpensive determination.
- **ORCP 81 B**: Effective dates — January 1 of odd-numbered
  years.

## Procedural-motion quick reference

| Motion | Rule | Standard / form |
|--------|------|------------------|
| Motion to dismiss for failure to state | ORCP 21 A(8) | Treats allegations as true |
| Motion to dismiss for jurisdiction | ORCP 21 A(1)/(2) | Lack of subject-matter / personal |
| Motion to dismiss for service | ORCP 21 A(3)/(4)/(5) | Insufficient process or service |
| Motion to strike | ORCP 21 E | Insufficient defense / immaterial matter |
| Motion to compel | ORCP 46 A | After meet-and-confer; mandatory fee-shifting if granted |
| Motion for summary judgment | ORCP 47 | 60-day pre-trial filing window; 20/5/11-day response/reply/hearing intervals |
| Motion for default | ORCP 69 | After failure to answer in 30 days |
| Motion to vacate | ORCP 71 B | Six enumerated grounds; 1-year cap for (1)–(3) |
| Motion to amend | ORCP 23 A | "Leave shall be freely given" |
| Motion for continuance | UTCR 6.030 | Good cause |

## Comparison to Washington (helps porting templates)

| Concept | Oregon | Washington |
|---------|--------|------------|
| Rules system | Single ORCP | CR (superior) + CRLJ (district) |
| Failure to state | ORCP 21 A(8) | CR 12(b)(6) / CRLJ 12(b)(6) |
| Discovery scope | ORCP 36 B(1) | CR 26(b)(1) |
| Interrogatories | **Not available** without court order | CR 33 (available) |
| RFPs | ORCP 43 | CR 34 |
| RFAs | ORCP 45 | CR 36 |
| Motion to compel | ORCP 46 A | CR 37 |
| Summary judgment | ORCP 47 (60 days pre-trial; 20/5/11) | CR 56 (28 days; 11 days) |
| Default | ORCP 69 | CR 55 |
| Vacation | ORCP 71 | CR 60 |
| Time computation | ORCP 10 | CR 6 |

## How to re-pull

The ORCP are pulled by the quarterly remote-agent corpus refresh
(`scripts/pull_oregon_rules.py` — to be created). For ad hoc
verification, fetch from
https://counciloncourtprocedures.org/ or
https://www.courts.oregon.gov/rules/Pages/orcp.aspx
