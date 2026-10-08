---
name: tx-discovery-codearranger
title: Texas Discovery
description: Use when drafting, responding to, or compelling discovery in a Texas civil case. Triggers include "Texas discovery", "discovery control plan Texas", "Level 1 Level 2 Level 3 discovery Texas", "expedited action Texas Rule 169", "required disclosures Texas Rule 194", "interrogatories Texas Rule 197", "how many interrogatories can I serve in Texas", "25 interrogatory limit Texas", "request for production Texas Rule 196", "request for admission Texas Rule 198", "deemed admitted Texas RFA", "deposition Texas Rule 199", "motion to compel Texas Rule 215". Covers the TRCP 190 discovery-control-plan framework (Levels 1/2/3) and expedited actions (TRCP 169), required disclosures (TRCP 194), RFPs (196), interrogatories (197), requests for admission (198, deemed admitted), depositions (199), the TRCP 193.7 self-authentication of produced documents, the 30-day response window, and the motion-to-compel / sanctions workflow under TRCP 215. Texas ALLOWS written interrogatories.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Texas Discovery

> **NOT LEGAL ADVICE.** This skill helps draft and respond to
> discovery. Verify against the current Texas Rules of Civil Procedure,
> the court's local rules, and any docket-control or scheduling order
> before serving or filing.

Use this skill alongside `tx-statewide-format`, `tx-law-references`,
and (where applicable) `tx-first-30-days`. The Texas civil discovery
framework lives in **TRCP 190–215** and applies in the District Court
and the County Courts at Law. (Justice-court discovery is sharply
limited and runs under TRCP Part V — see `tx-county-courts`.) Pull the
verbatim rule text from `../tx-law-references/references/court-rules/`
before serving or responding.

## Texas allows written interrogatories

Texas permits the full toolkit of party discovery — written
interrogatories, requests for production, requests for admission, and
depositions — without leave of court, subject to the limits of the
governing **discovery control plan**. The response window for written
discovery is generally **30 days** (with nuances noted below — confirm
the exact count and triggers against the corpus).

## ★ The discovery control plan — TRCP 190

Every Texas case is assigned to one of **three discovery levels** under
**TRCP 190**, and the level governs the discovery period and the limits
on each device:

| Level | What it is |
|---|---|
| **Level 1 — TRCP 190.2** | Expedited actions and certain other limited cases (tied to **TRCP 169**, for claims at or below the statutory ceiling). Tight discovery period and per-side limits — e.g., capped deposition hours, capped interrogatories. Confirm the current dollar ceiling and the per-side limits against the corpus. |
| **Level 2 — TRCP 190.3** | The **default** plan when no Level 1 or Level 3 plan governs. The discovery period runs for a set time keyed to the first deposition or the trial setting, with the standard per-side limits. |
| **Level 3 — TRCP 190.4** | A **court-ordered, tailored plan** — the parties or the court craft a docket-control order setting the discovery period, limits, and deadlines for the specific case (common in complex matters). |

> **Identify the governing level before serving anything.** The level
> sets the discovery-period cutoff and the numeric limits; serving
> beyond them without leave is objectionable. Pull the day counts and
> per-side limits for the operative level from the corpus.

### Expedited actions — TRCP 169

A suit for monetary relief **at or below the statutory ceiling**
(exclusive of interest, costs, and attorney fees — confirm the current
ceiling against the corpus) is an **expedited action** under **TRCP
169**, automatically on **Level 1** discovery, with a limited discovery
period, limited per-side discovery, and a trial-setting requirement.
Pleading a higher relief range removes the case from the expedited
track.

## Required disclosures — TRCP 194

**TRCP 194** requires **initial disclosures** without a discovery
request. Under the **amendment effective January 1, 2021**, disclosures
are now **automatic / initial-disclosure style** (modeled on the
federal approach): each party must, within the rule's window after the
first answer is filed, disclose the categories of information TRCP
194.2 lists — the parties' correct names, potential parties, legal
theories and factual bases, the amount and method of calculating
damages, witnesses, documents, insurance, and settlement agreements.
**Additional disclosures** for testifying experts (TRCP 194/195) and
pretrial disclosures follow on their own schedules. Confirm the current
window and the 194.2 list against the corpus.

## Requests for Production — TRCP 196

**TRCP 196** requests documents, electronically stored information
(ESI), and tangible things, and may seek **entry onto land** for
inspection. The responding party produces documents as kept in the
usual course of business or organized to correspond to the request's
categories, and responds within **30 days** after service (a party may
not serve RFPs before its own answer is due in some postures — confirm
the timing against the corpus). **ESI** is produced in a reasonably
usable form; address form-of-production and metadata by agreement,
consistent with TRCP 196.4 and the proportionality limits of TRCP 192.

## Interrogatories — TRCP 197

Written interrogatories to a party are governed by **TRCP 197**.

- **Numeric cap.** Under **TRCP 197.1** a party may serve **no more
  than 25 written interrogatories, excluding interrogatories asking a
  party only to identify or authenticate specific documents**, counting
  each discrete subpart as a separate interrogatory. (Levels 1 and 3
  may impose a different cap — confirm the operative limit and the
  subpart-counting rule against the corpus before serving a large
  set.)
- **Responses — 30 days.** Answers are served separately and fully, in
  writing under oath, within **30 days** after service (**TRCP
  197.2**), with each objection stated specifically. A responding
  party may answer by producing business records under **TRCP 197.2(c)**
  on the rule's conditions.

```
INTERROGATORIES

Pursuant to Tex. R. Civ. P. 197, [Defendant] requests that [Plaintiff]
answer the following Interrogatories separately and fully, in writing
under oath, within 30 days after service.

INTERROGATORY NO. 1: State the name, address, and telephone number of
each person with knowledge of relevant facts, and describe the subject
of that knowledge.

ANSWER: [Response]
```

## Requests for Admission — TRCP 198

- **Critical — deemed admitted.** Under **TRCP 198.2(c)** a matter is
  **deemed admitted, without the necessity of a court order,** unless
  the responding party serves a written answer or objection within
  **30 days** after service. Calendar RFA deadlines carefully — a
  missed deadline can concede dispositive facts.
- A party may move to **withdraw or amend** a deemed admission under
  **TRCP 198.3** on the rule's conditions (the merits are served and
  the requesting party is not unduly prejudiced) — but do not rely on
  withdrawal; answer on time.

## Depositions — TRCP 199

- **TRCP 199** governs oral depositions; serve **reasonable** written
  notice of the time, place, and deponent (TRCP 199.2). The per-side
  deposition limits (hours / number) are set by the **discovery level**
  — confirm against the corpus.
- For an **organization deposition** under **TRCP 199.2(b)(1)**,
  describe the matters for examination with reasonable particularity so
  the entity can designate a witness.
- Depositions on written questions (TRCP 200), depositions to perpetuate
  testimony (TRCP 202), and non-party / out-of-state depositions
  (TRCP 201, 205) have their own mechanics — confirm in the corpus.
- Remote / video depositions are permitted; state the method on the
  notice.

## Scope and proportionality — TRCP 192

Discovery extends to any matter **not privileged that is relevant to
the subject matter** of the action, with the **proportionality** limits
of **TRCP 192.4** (a court may limit discovery that is unreasonably
cumulative, obtainable more conveniently elsewhere, or whose burden
outweighs its likely benefit). Privileged matter and work product are
protected; assert a privilege expressly and serve a **withholding
statement / privilege log** under **TRCP 193.3**.

## Self-authentication of produced documents — TRCP 193.7

> **Useful in debt and contract cases.** Under **TRCP 193.7**, a
> document a party **produces in response to written discovery is
> authenticated** for use against that party in any pretrial proceeding
> or at trial — **unless**, within **10 days** (or a longer or shorter
> time the court allows) after the producing party has actual notice
> that the document will be used, the party objects to authenticity and
> states the specific basis. Confirm the current notice/objection
> window against the corpus. This rule lets a party use the opponent's
> own produced records without a sponsoring witness, and a debt
> defendant should watch the objection clock when a debt buyer produces
> account records.

## Motion to compel and sanctions — TRCP 215

If a party fails to respond, responds evasively, or lodges improper
objections, move to compel under **TRCP 215** (specifically TRCP 215.1
for the motion to compel and TRCP 215.2 for failure to comply with an
order). Texas conditions discovery relief on a good-faith effort to
resolve the dispute, and the motion should:

1. **Identify the specific deficiencies** (which interrogatory / RFP /
   RFA / disclosure, and why the response is inadequate).
2. **Attach** the requests and responses as exhibits.
3. **State a certificate of conference** describing the good-faith
   attempt to resolve the dispute without court action.
4. **Address each objection** on the merits.
5. **Request specific relief**: an order compelling responses by a date
   certain, plus an award of reasonable expenses.

```
Subject: Certificate of Conference re: Discovery Responses —
         [Case Short Title], Cause No. [Number]

[Name], this is my good-faith effort to confer under Tex. R. Civ. P.
215 before I file a Motion to Compel. Your responses to my First Set
of Interrogatories and Requests for Production, served on [DATE], are
deficient as follows:

  1. Interrogatory No. 3 — Boilerplate objection without specifying the
     vague term or quantifying the burden.
  2. Request for Production No. 7 — No documents produced though the
     petition references documents within this request.
  3. Request for Admission No. 2 — Evasive non-answer.

Please supplement by [date]. If I do not hear from you, I will proceed
with a Motion to Compel and seek expenses under Rule 215. [Name]
```

A motion to compel is set for hearing or submission — see `tx-hearings`
and `tx-schedule-hearing`.

### Sanctions ladder

- On a granted motion to compel, **TRCP 215.1** authorizes an award of
  the reasonable **expenses, including attorney fees**, caused by the
  failure, unless the resistance was substantially justified.
- For **disobedience of a discovery order**, **TRCP 215.2** escalates
  to stronger sanctions — up to striking pleadings, deeming matters
  established, prohibiting evidence, dismissal, or default judgment
  (the most severe "death-penalty" sanctions require the conduct and
  the sanction to be appropriately matched).
- **TRCP 215.4** addresses the consequences of failing to admit under
  Rule 198, and **TRCP 193.6** can exclude evidence not timely
  disclosed.

Verify the current subpart lettering against the verbatim TRCP 215 text
in `../tx-law-references/references/court-rules/`.

## Composition

- For drafting the motion to compel: `tx-draft-motion`
- For the supporting affidavit / unsworn declaration:
  `tx-draft-declaration`
- For the notice of hearing / setting on the motion: `tx-draft-note`,
  `tx-schedule-hearing`
- For statewide format: `tx-statewide-format`
- For deadline arithmetic (the 30-day response window, the discovery-
  level cutoff, and the TRCP 21a service add-on): `tx-deadlines`
- For venue: `tx-hcdc`, `tx-dcdc`, `tx-county-courts`
- For consumer-debt RFP / RFA banks, debt-buyer chain-of-title
  discovery, and attacking the TRE 902(10) business-records affidavit:
  `tx-consumer-debt`

## References

- `references/interrogatory-templates.md` — TRCP 197 templates (25-cap)
- `references/rfp-templates.md` — TRCP 196 templates
- `references/rfa-templates.md` — TRCP 198 templates
- `references/disclosure-checklist.md` — TRCP 194 initial-disclosure
  checklist
- `references/deposition-notice.md` — TRCP 199 notice scaffold
- `references/motion-to-compel.md` — TRCP 215 scaffold
- `references/conference-templates.md` — certificate-of-conference
  templates
