---
name: or-discovery-codearranger
title: Oregon Discovery — Procedural Reference
description: 'Use this skill for discovery in Oregon civil cases. Triggers include "RFP", "depositions", "RFA", "requests for admission", "meet and confer", "ORCP 46", "motion to compel", "discovery objections", "privilege log", "ORCP 39", "ORCP 43", "ORCP 45". Covers discovery request drafting, response strategy, meet-and- confer mechanics, and motion-to-compel with mandatory fee- shifting (ORCP 46 A(4)(a)). **Important**: written interrogatories are NOT available as of right — use depositions (ORCP 39), RFPs (ORCP 43), physical/mental exams (ORCP 44), or RFAs (ORCP 45). Subject-matter request banks (e.g., debt-buyer RFPs) live with relevant subject-matter skill (e.g., or- consumer-debt). Composes with or-statewide-format, or-pro-se, or-law-references, or-draft-motion, and or-fact-check.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Meet And Confer
  path: references/meet-and-confer.md
- title: Objection Responses
  path: references/objection-responses.md
---

# Oregon Discovery — Procedural Reference

This skill covers the **matter-neutral procedural framework** for
discovery in Oregon civil practice. The full ORCP text lives in
`or-law-references/references/civil-rules.md`. For subject-
matter-specific request banks (e.g., debt-buyer chain-of-title
RFPs), compose with the relevant subject-matter skill.

> **NOT LEGAL ADVICE.** Verify each rule and the local SLR before
> drafting.

## Oregon's distinctive discovery model — no interrogatories

The single most important fact about Oregon civil discovery:
**Oregon does NOT have written interrogatories under the ORCP as
a matter of right.**

Available discovery tools:

- **Depositions** — ORCP 39 (oral) and ORCP 40 (written
  questions; rare)
- **Requests for production** — ORCP 43
- **Physical / mental examination** — ORCP 44 (court order
  required)
- **Requests for admission** — ORCP 45
- **Subpoenas** for non-parties — ORCP 55

Why no interrogatories? Oregon's Council on Court Procedures
historically rejected the FRCP 33 model on the theory that
written interrogatories generate boilerplate disputes without
producing meaningful information; depositions and RFPs are
sufficient.

Practical implications:

- A party in Oregon **cannot serve written interrogatories** to
  the opposing party as a matter of right
- The court can order interrogatories by stipulation, in a
  mandatory arbitration proceeding (under the arbitrator's
  discretion), or by special order in unusual cases — but this
  is rare
- Pro se filers porting from Washington or federal practice
  often mis-serve "First Interrogatories" — these are unenforce-
  able in Oregon and will be objected to. The right tools are
  RFPs and short-form deposition.

## ORCP 36 — General scope of discovery

The scope test, identical to FRCP 26(b)(1):

- **Relevance**: relevant to a claim or defense
- **Proportionality**: proportional to the needs of the case,
  considering (1) importance of the issues, (2) amount in
  controversy, (3) party's relative access, (4) party's
  resources, (5) importance of the discovery in resolving issues,
  (6) burden / expense vs. likely benefit
- **Reasonably calculated to lead to admissible evidence**

Beyond the scope test, ORCP 36 sets:

- **ORCP 36 B(1)**: scope statement
- **ORCP 36 B(2)**: protected materials — privilege, work
  product, expert disclosures
- **ORCP 36 C**: protective orders — limiting discovery on
  motion

## ORCP 43 — Requests for production

The workhorse rule in Oregon discovery.

### Mechanics

- **ORCP 43 A**: Party may serve RFPs on any other party
- **ORCP 43 B**: Response within **30 days** (45 days if served
  with summons)
- **Form**: Each request states a specific category of
  documents; the response either produces, identifies
  responsive documents, or objects with specific grounds

### Drafting good RFPs

A well-drafted RFP is:

- **Specific**: targets a defined category of documents, not
  "all documents related to the case"
- **Tied to a claim or defense**: cites the relevance under
  ORCP 36 B(1) in a preamble if helpful
- **Bounded by time**: "documents dated between [date] and
  [date]"
- **Bounded by party**: "documents created, sent, received,
  or maintained by [party or entity]"

Example (well-drafted):

> Request for Production No. 3: All documents constituting,
> referencing, or summarizing the original cardholder agreement
> between Defendant John Doe and Bank of America for account
> number ending in XXXX, including signature pages,
> incorporated terms and conditions, and any electronic
> acceptance records.

Example (poorly drafted):

> Request for Production No. 3: All documents related to the
> account.

### Common RFP objections (and how to overcome)

| Objection | Response |
|-----------|----------|
| Overbroad | Narrow the temporal or party scope; or stand on the request and let the court rule |
| Burdensome | Quantify the actual burden; ORCP 36 proportionality is a balancing test |
| Privileged | Request a privilege log per ORCP 36 B(2); the bare assertion is insufficient |
| Relevance | Cite the specific claim or defense the request relates to |
| Not in possession, custody, or control | Verify; "possession" includes documents the party can access by ordinary means |
| Trade secret | Propose a protective order under ORCP 36 C |
| Premature | Many objections labeled "premature" are actually relevance — push back |

## ORCP 39 — Depositions

### When and how

- After action is commenced, any party may take depositions on
  notice (5 days for parties, 7 for non-parties)
- Stenographic, audio, or video recording acceptable
- Subpoena required for non-party depositions (ORCP 55)
- ORCP 39 D limits to 7 hours per deposition (typical
  practice; verify current rule)

### Limits

- 10 depositions per side without leave (per ORCP 36 / practice)
- Leave required for repeat deposition of same witness, or to
  depose a person already deposed in a related action

### Use of depositions

- ORCP 39 I governs use of deposition testimony at trial:
  party admission, impeachment, unavailable witness, etc.
- ORCP 39 C governs recording — written transcript required
  for use as evidence; audio/video supplements

### Pro se deposition practice

Pro se litigants can take depositions, but the mechanics
(reservation of court reporter, subpoena issuance, recording
agreements) are complex. Many pro se litigants substitute the
**deposition by written questions under ORCP 40** for simple
factual depositions — slower but procedurally simpler.

## ORCP 45 — Requests for admission

### Mechanics

- Party serves written requests for admission of facts or
  application of law to facts
- Response within **30 days** (45 if served with summons)
- Failure to respond → **deemed admitted** (ORCP 45 B)
- Response options: admit, deny, or state inability to admit
  or deny with specifics

### Strategic use

RFAs are powerful in Oregon because:

- They narrow the issues for trial
- They establish foundational facts (e.g., "Plaintiff is a
  Delaware LLC", "the account was opened on [date]") without
  needing live testimony
- The 30-day default-admission risk creates pressure to
  respond

Each RFA should be a **single, simple fact** — compound RFAs
get partial denials that are hard to use. Example:

> Request for Admission No. 5: Admit that Plaintiff is a
> Delaware limited liability company.

NOT:

> Request for Admission No. 5: Admit that Plaintiff is a
> Delaware LLC organized in 2017 with its principal place of
> business in New Jersey and that it filed a Foreign LLC
> Registration in Oregon on April 1, 2024.

The compound form invites the response "Admitted in part,
denied in part" with no usable narrowing of issues.

### Withdrawal of admissions (ORCP 45 C)

- Court may permit withdrawal on motion if the presentation
  of the merits will be subserved and the requesting party is
  not prejudiced
- High bar; planned admissions and considered denials are
  preferred to last-minute withdrawal motions

## Meet and confer

**Mandatory** under ORCP 46 A — and under most local SLRs
(e.g., Multnomah SLR 5.045 / Washington Co SLR 5.046).

The meet-and-confer:

- Identifies the specific issue (e.g., "RFP No. 3 — Plaintiff's
  objection on grounds of burden")
- Records the parties' positions
- Documents the inability to resolve

### Sample meet-and-confer email

```
To:      [opposing counsel]
Subject: Meet and Confer — Discovery Dispute, Case No. 25CV12345

Counsel:

I am writing to meet and confer under ORCP 46 A (and Multnomah
SLR 5.045) regarding the discovery responses you served on
[date]. Specifically:

1.  RFP No. 3 (cardholder agreement) — your objection on
    grounds of burden. We disagree because [reasons]. We
    request that you supplement the response within 14 days,
    by [date]. If you cannot, please let us know whether the
    burden can be addressed by [proposed alternative —
    sampling, time-limited subset, etc.].

2.  RFP No. 5 (assignment schedule) — your objection on
    grounds of relevance. We disagree because [reasons]. We
    request supplementation within 14 days.

3.  RFP No. 6 (account history) — your objection on grounds
    of privilege. The bare assertion is insufficient under
    ORCP 36 B(2). Please provide a privilege log identifying
    each document withheld within 14 days.

If we cannot resolve these by [date], we will move to compel
under ORCP 46 A.

I am available by phone at [number] to discuss before [date].
Please let me know a good time.

Best,
[Name][, pro se]
```

The follow-up email confirming the call (and stating the
opposing party's position) is what the meet-and-confer
certification recites.

## Motion to compel (ORCP 46 A)

### Prerequisites

- A specific discovery request was served
- The opposing party responded with objections OR failed to
  respond
- The moving party met and conferred (or attempted to)
- The conference did not resolve the dispute

### Required content of the motion

1. Identification of the specific request at issue
2. The opposing party's response (or non-response)
3. Statement of why the response is deficient
4. Meet-and-confer certification (UTCR / local SLR)
5. Statement of relief — order compelling response, fees under
   ORCP 46 A(4)(a)

### Fee-shifting (ORCP 46 A(4)(a))

**Mandatory** if the motion is granted, unless the opposing
party's failure was "substantially justified" or other
circumstances make an award unjust.

The fee award is in addition to whatever sanctions (ORCP 46 B)
the court may impose. Track time spent on the motion — a fee
petition under ORCP 68 follows.

### Drafting the meet-and-confer certification

In Multnomah / Washington County (and many other counties):

```
                CERTIFICATION OF MEET AND CONFER
                  (Multnomah SLR 5.045 / ORCP 46 A)

Pursuant to Multnomah SLR 5.045 and ORCP 46 A, counsel for
Defendant certifies that:

1.  On [date 1], Defendant served First Requests for Production
    Nos. 1–6 on Plaintiff.

2.  On [date 2], Plaintiff served Responses, objecting on
    grounds of [grounds] without producing responsive documents.

3.  On [date 3], Defendant sent a meet-and-confer letter to
    Plaintiff (Exhibit 3) identifying the specific objections,
    explaining Defendant's position, and requesting
    supplementation within 14 days.

4.  On [date 4], Plaintiff responded (Exhibit 4), declining to
    supplement.

5.  The parties have been unable to resolve the discovery
    dispute and are at impasse.

Defendant therefore respectfully requests an order compelling
production under ORCP 46 A.
```

## Protective orders (ORCP 36 C)

A party from whom discovery is sought may move for a protective
order to:

- Forbid the discovery
- Limit the scope
- Require performance at a different time or place
- Restrict who may attend
- Seal the discovery materials

The standard: **good cause**. The court balances the burden
against the need.

## Discovery in mandatory arbitration

If the case is in ORS 36.400 mandatory arbitration, discovery
is limited to what the arbitrator's rules permit. Some
arbitrators allow interrogatories by stipulation; most rely on
ORCP 43 RFPs and short depositions.

If discovery disputes arise in arbitration, motion to the
**arbitrator**, not the circuit judge. The circuit judge hears
disputes about the arbitration *process* (e.g., arbitrator
disqualification), not substantive discovery.

## Subject-matter request banks

This skill is matter-neutral. For pre-built request banks:

- **Debt-buyer chain of title**: see `or-consumer-debt/
  references/rfp-debt-buyer.md` and `rfa-debt-buyer.md`
- **Landlord-tenant** (future): would live in `or-landlord-
  tenant/references/`
- **Personal injury** (future): would live in `or-personal-
  injury/references/`

## References

- `references/meet-and-confer.md` — full meet-and-confer
  protocol with sample emails and call-log templates
- `references/objection-responses.md` — drafting responses to
  RFPs, including objection libraries
