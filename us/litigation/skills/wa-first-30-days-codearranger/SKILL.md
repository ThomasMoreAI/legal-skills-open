---
name: wa-first-30-days-codearranger
title: The First 30 Days — From Service Through Answer
description: 'Use this skill when a Washington defendant has just been served with a civil summons and complaint in any subject-matter case and the answer window is running. Triggers include "I was just served", "summons and complaint", "what do I do first", "deadline to answer", "answer the complaint", "affirmative defenses checklist", "counterclaim planning", "CR 12", "CRLJ 12", "motion to dismiss or answer". Covers the matter-neutral from-service-through-answer window: CR 12 / CRLJ 12 response deadline, motion-to-dismiss vs. answer triage, affirmative-defenses checklist, counterclaim mechanics, compulsory-counterclaim analysis, evidence preservation, and initial discovery planning.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# The First 30 Days — From Service Through Answer

Most pro se defendants lose their case in the first 30 days — by
missing the answer deadline, by filing a defective answer, or by
failing to preserve the affirmative defenses and counterclaims
that would have saved them. This skill covers the
**matter-neutral** window from service of the summons and
complaint through filing a compliant answer or motion to dismiss,
and sets up the discovery posture for rounds 2 and 3.

For subject-matter-specific substantive guidance (fact patterns,
specific affirmative defenses, statutory counterclaims), compose
with the relevant subject-matter skill:

- Consumer-debt cases → `wa-consumer-debt`
- (Future: landlord-tenant, family, personal injury, etc.)

## Inputs to gather

Ask the user (use the `AskUserQuestion` tool for anything not
clear):

1. **Case name and cause number** — parties, court, cause number
   format (KCDC is `\d{2}CIV\d{6}KCX`; KCSC differs; verify).
2. **Subject matter** — contract, tort, consumer debt,
   landlord-tenant, family, etc. Determines which
   subject-matter skill to compose with.
3. **Date served** — exact date; needed for deadline math.
4. **Method of service** — personal, abode, substituted,
   publication (affects validity and excusable-neglect analysis).
5. **Is the user's address on the summons current?** — bears on
   whether the user is likely to miss future mailings.
6. **What's attached to the complaint** — contracts, records,
   declarations, exhibits, schedules. Scan the attachments for
   subject-matter pattern matching (delegate to the relevant
   subject-matter skill).
7. **Is a default already entered?** — if yes, this skill is
   **not** the right starting point; hand off to
   `wa-post-judgment` for a CR 60 / CRLJ 60 motion to vacate.
8. **Plaintiff identity** — individual, corporation, debt buyer,
   governmental, etc. Subject-matter skills may have specific
   checks (licensing, capacity, authority to sue).
9. **Prior communications** — any letters, calls, notices,
   demands, or negotiations.

## Step 1 — Compute the deadline (via wa-deadlines)

The answer window depends on the court (superior vs. district),
the method of service (personal vs. mail vs. out-of-state vs.
publication), and the current court-rule text. **Do not embed
specific day counts here** — `wa-deadlines` plus
`scripts/case-calendar.py` carry the current values; the rule
text lives in `wa-law-references/references/court-rules/CR.md`
and `CRLJ.md`.

**Hand off to `wa-deadlines`** with the date of service and the
court / method of service. The deadlines skill returns the
specific date and a court-day vs. calendar-day breakdown.
Surface the deadline in boldface to the user; create a calendar
entry.

**Critical**: **the answer deadline is not a "respond sometime"
window.** A late answer entitles the plaintiff to move for
default. If the user is already late:

- **Within the day** — file today; contemporaneous or next-day
  answers are commonly accepted without default.
- **A few days late but no default yet** — file the answer
  immediately; the plaintiff may or may not challenge timeliness.
- **Default entered** — hand off to `wa-post-judgment` for CR 60
  / CRLJ 60 motion to vacate.

## Step 2 — Subject-matter pattern recognition

Read the complaint and attachments. If the case is a recognized
subject matter with a dedicated skill, hand off that reading to
the subject-matter skill for fact-pattern triage:

- Consumer-debt → `wa-consumer-debt/SKILL.md` and its
  `references/fact-patterns.md`
- (Future bundles plug in here.)

The pattern is informational — it maps to the procedural options
the rules make available: (a) the choice between an MTD and an
answer, (b) the affirmative defenses that fit the pattern, (c)
the counterclaims the pattern raises, and (d) the discovery the
pattern points toward. Which of these the litigant pursues
remains the litigant's decision (and any counsel the litigant
retains).

If no subject-matter skill applies, proceed with the general
triage below.

## Step 3 — Motion to dismiss vs. answer (the triage)

Two paths from here.

### Motion to dismiss under CR 12(b)(6) / CRLJ 12(b)(6)

File if the complaint, taken as true:

- Does not state a claim (element missing on the face of the
  pleading)
- Is time-barred on the face of the pleading (SOL apparent from
  alleged dates)
- Lacks specificity required to put the defendant on notice
- Fails for subject-matter-specific reasons (consult the
  subject-matter skill — e.g., for a debt-buyer case, a missing
  assignment allegation)

**Risk of MTD**: the court takes allegations as true at this
stage. If the complaint is facially sufficient but weak, **MTD
will be denied** — and the user has used their first motion
without advancing. **Prefer MTD only where the facial defect is
real.**

If choosing MTD, **also file an answer within the CR 12 window as
a backstop** unless the MTD stays the response deadline (some
jurisdictions; verify against current rule text and local rules).

Hand off to `wa-draft-motion` with motion type = motion-to-dismiss.

### Answer + affirmative defenses + counterclaim

The more common path. File a compliant answer that:

1. Admits, denies, or states lack of knowledge for each numbered
   allegation (CR 8(b) / CRLJ 8(b)).
2. Preserves every available affirmative defense (CR 8(c) /
   CRLJ 8(c)).
3. Pleads counterclaims where the facts support them (compulsory
   vs. permissive — see below).

#### Affirmative defenses — general checklist

Plead every one that fits; **unpleaded defenses are waived**.
Matter-neutral defenses to consider in any civil case:

- [ ] **Statute of limitations** (applicable RCW 4.16 section
      depends on the claim)
- [ ] **Lack of standing** (CR 17(a), real-party-in-interest)
- [ ] **Lack of capacity to sue** (corporate registration,
      licensing where required by subject-matter statute)
- [ ] **Failure to state a claim** (CR 12(b)(6), preserved for
      later motion)
- [ ] **Lack of personal jurisdiction** (only if service was
      defective — verify before pleading)
- [ ] **Improper service** (similarly, only if documented)
- [ ] **Lack of subject-matter jurisdiction** (rare in civil;
      watch for amount-in-controversy in KCDC)
- [ ] **Waiver / estoppel / laches** (fact-specific)
- [ ] **Accord and satisfaction** (if any settlement was
      reached)
- [ ] **Payment** (if any part paid)
- [ ] **Set-off** (if plaintiff owes defendant on another
      claim)
- [ ] **Release** (if any release was signed)
- [ ] **Statute of frauds** (if applicable to the claim type)
- [ ] **Reservation**: "Defendant reserves the right to assert
      additional affirmative defenses as discovery reveals facts
      supporting them."

**Subject-matter-specific** defenses layer on top of this
checklist. For debt-buyer cases, add the defenses listed in
`wa-consumer-debt/SKILL.md` (RCW 19.16.110 licensing, failure of
consideration under Article 9, unclean hands / FDCPA, etc.).

#### Counterclaims — compulsory vs. permissive

**Compulsory counterclaims** (CR 13(a) / CRLJ 13(a)) — a claim
arising out of the same transaction or occurrence as the
plaintiff's claim. **Must be pleaded with the answer or is
waived.**

**Permissive counterclaims** (CR 13(b) / CRLJ 13(b)) — any other
claim the defendant has against the plaintiff. May be pleaded in
the answer or in a separate action.

Before filing, ask:

1. **Is there a claim back?** Does the defendant have any civil
   claim against the plaintiff?
2. **Is it compulsory?** Does it arise from the same
   transaction? If yes, plead it now or lose it.
3. **Is it time-barred?** Some counterclaims have short SOLs
   (e.g., FDCPA 1-year). Compulsory-counterclaim analysis may
   be the only thing that revives an otherwise stale claim.
4. **Does it add a party?** If yes, consult CR 13(h) / CR 19
   joinder rules.
5. **Does it survive jurisdictionally?** If pleaded in KCDC, the
   counterclaim amount cannot exceed the district court
   jurisdictional limit (RCW 3.66.020); consider transfer to
   superior court if it does.

Subject-matter skills (e.g., `wa-consumer-debt`) supply the menu
of counterclaims typically available in that subject matter.

**Prayer for relief** — plead every category of recovery the
claim supports: dismissal of the complaint, actual damages,
statutory damages, treble damages (where available by statute),
attorney fees (see
`wa-law-references/references/fees-and-costs.md` for every
applicable ground), costs, and such further relief as the court
deems just.

Hand off to `wa-draft-declaration` for a verification /
declaration and `wa-draft-motion` (or `wa-draft-note` +
file-packet flow) for the answer-and-counterclaim packet.

## Step 4 — Evidence preservation

Inform the user of their obligation to preserve:

- **Every document** relating to the transaction or occurrence
  (agreements, records, statements, letters, emails)
- **Electronic records** (texts, voicemails, call logs,
  metadata)
- **Third-party records** that the defendant can obtain (bank
  statements, employer records, medical records, credit-bureau
  reports, etc.)

Do not destroy anything, even documents the user thinks are
harmful — **spoliation is worse than any bad document.** Litigation
hold should attach the moment the defendant reasonably
anticipates litigation.

## Step 5 — Opening discovery plan (don't serve yet)

Line up — but do not serve — Round 1 of discovery. Timing:

- **Cannot serve before the answer is filed** (limits under CR
  26(d) and CRLJ 26).
- **Can serve with the answer or shortly after.**
- **Response window starts on service** (current day count per
  CR 33/34/36 — see `wa-deadlines`).

Prepare (via `wa-discovery`):

- 10–15 RFPs targeting the **threshold / foundational** elements
  of the plaintiff's claim.
- 5–8 interrogatories identifying witnesses, document custodians,
  and key computations.
- 5–8 RFAs narrowing issues (deemed admitted if not answered
  within the response window — a powerful lever).

Subject-matter skills supply the specific request banks (e.g.,
`wa-consumer-debt/references/rfp-debt-buyer.md`).

Hold for service on a day tied to a calendar plan — **do not
serve all discovery at once** on day 1; stagger by round (see
`wa-discovery/SKILL.md` for the general cadence).

## Step 6 — Counterclaim preparation

Before pleading a counterclaim, verify its elements and
preservation window. Some subject-matter statutes (FDCPA,
FCRA, CPA) have specific notice requirements or short SOLs.
Compose with the subject-matter skill to confirm:

- Are the elements adequately pleaded on the facts available?
- Is a **pre-suit notice** required (e.g., under a specific
  statute)?
- Are there **compulsory-counterclaim** issues if the claim is
  not pleaded now?
- Does the counterclaim require any **verification** or
  declaration?

Pro se note: any correspondence with the plaintiff goes into the
evidentiary record. Write as if a judge will read it.

## Step 7 — Assemble and file the answer packet

Hand off to `wa-file-packet` with components:

- Answer and affirmative defenses
- Counterclaim (if pleading one)
- Certificate of service
- Note (only if the defendant needs a hearing at this stage —
  usually not)
- **Not** the discovery yet — hold for after filing

For KCDC, the clerk-issued-date rule applies to hearings, not to
the answer itself. Answers are filed through the KCDC e-filing
portal; no hearing reservation needed for an answer.

Before filing, run `wa-fact-check` on the packet. Stray
citations in an answer can undercut a user's credibility for the
rest of the case.

## Step 8 — Calendar the next 60 days

Set reminders for:

- [ ] **Day of filing**: answer filed, CoS filed, service on
      opposing counsel completed
- [ ] **Day +1**: confirm plaintiff received the answer (email
      delivery receipt or certificate)
- [ ] **Day +7 to +14**: serve Round 1 discovery
- [ ] **Day +37 to +44** (30 + 3 mailing + small buffer): track
      plaintiff's discovery response
- [ ] **Day +30**: review plaintiff's answer to counterclaims
      (if timely filed); note any deemed admissions on RFAs
- [ ] **Day +60**: assess whether meet-and-confer + motion to
      compel is warranted; hand off to `wa-discovery`

## Common pitfalls

- **Filing a general denial** — CR 8(b) / CRLJ 8(b) require
  paragraph-by-paragraph response; a general denial admits
  allegations the defendant failed to specifically deny.
- **Failing to plead affirmative defenses** — each unpleaded
  defense is waived under CR 8(c) / CRLJ 8(c).
- **Filing an answer that includes substantive admissions** —
  pro se answers sometimes recite facts the defendant thinks
  "strengthen" their case; avoid, unless the fact is undisputed
  and necessary.
- **Ignoring the compulsory-counterclaim analysis** — a
  transaction-or-occurrence counterclaim not pleaded with the
  answer may be barred by res judicata in a later action.
- **Filing too much too early** — discovery served with the
  answer often produces a generic objection-fest; better to
  serve after a day or two of reflection and after reading
  plaintiff's exact attachments.
- **Forgetting to plead fees** — "Defendant prays for
  reasonable attorney fees under [every applicable ground —
  see `wa-law-references/references/fees-and-costs.md`]."
- **Skipping the subject-matter skill** — on a debt-buyer
  complaint, failing to compose with `wa-consumer-debt` will
  miss the FDCPA counterclaim, the RCW 19.16.110 licensing
  defense, the chain-of-title discovery, and the fact-pattern
  triage.

## Deliverables

End of this skill's run, the user should have:

- [ ] A calendared answer deadline (via `wa-deadlines`)
- [ ] A subject-matter classification and (if applicable) a
      pattern match via the subject-matter skill
- [ ] A decision: motion to dismiss vs. answer, with reasoning
- [ ] A drafted answer with affirmative defenses and (if
      applicable) counterclaim (via `wa-draft-motion` /
      `wa-draft-declaration`)
- [ ] A drafted Certificate of Service
- [ ] An assembled filing packet (via `wa-file-packet`)
- [ ] A fact-check pass (via `wa-fact-check`)
- [ ] A discovery plan for Rounds 1–3 (via `wa-discovery`),
      unfiled, queued for service
- [ ] A 60-day forward calendar

## Notes

- **Respond by the deadline.** Every other decision can be
  corrected; missing the deadline often cannot.
- **Do not have substantive conversations with opposing
  counsel** without a plan. Any admissions made orally become
  evidence; any settlement discussion should be in writing.
- **Keep a case journal** from day one — date, event, document
  — with every phone call, letter, and email logged. The
  journal is itself admissible as a present-sense impression /
  business record for the declaration later.
- **Not legal advice.** This skill orchestrates draft
  generation; the user is responsible for every word filed
  and is encouraged to consult a licensed attorney for the
  decisive calls.
