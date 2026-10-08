---
name: ga-discovery-codearranger
title: Georgia Discovery
description: 'This skill should be used when drafting, responding to, or compelling discovery in a Georgia civil case. Triggers include "Georgia interrogatories", "interrogatories under O.C.G.A. § 9-11-33", "requests for production Georgia", "requests for admission deemed admitted", "RFA Georgia", "Georgia deposition", "discovery period", "discovery deadline Georgia", "motion to compel Georgia", "protective order Georgia", "subpoena Georgia". Covers the Georgia Civil Practice Act discovery framework (O.C.G.A. §§ 9-11-26 to 9-11-37): the scope of discovery, the 50-interrogatory cap, requests for production, the requests-for-admission deemed-admitted trap, depositions, the 30-day (45-day if served with the summons) response window, the six-month USCR 5 discovery period, protective orders, supplementation, motions to compel with expenses, and subpoenas.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-discovery
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia Discovery

> **NOT LEGAL ADVICE.** This skill helps draft and respond to
> discovery. Verify against the current Georgia Civil Practice Act,
> the Uniform Court Rules, and the assigned judge's standing orders
> before serving or filing.

Use this skill alongside `ga-statewide-format`, `ga-law-references`,
and (where applicable) `ga-first-30-days`. Georgia civil discovery
derives from the **Georgia Civil Practice Act, O.C.G.A. §§ 9-11-26
through 9-11-37**, with the discovery *period* set by the Uniform
Court Rules.

## Snapshot — Georgia discovery clock

| Trigger | Deadline / event | Authority |
|---|---|---|
| Discovery period | **6 months** from the filing of the answer | USCR 5 |
| Written-discovery responses (served after the answer) | **30 days** after service | O.C.G.A. §§ 9-11-33, 9-11-34, 9-11-36 |
| Written-discovery responses (served **with the summons**) | **45 days** after service | O.C.G.A. §§ 9-11-33, 9-11-34, 9-11-36 |
| Extension / shortening of the discovery period | by stipulation or court order | USCR 5 |

> Frame day counts and the period start with cites; defer the exact
> calendar arithmetic (weekend / § 1-4-1 holiday roll-forward under
> O.C.G.A. § 1-3-1(d)(3)) to `ga-deadlines` / `case-calendar.py`.

## Scope of discovery — O.C.G.A. § 9-11-26(b)

Parties may obtain discovery of any matter, not privileged, that is
**relevant to the subject matter** of the action (O.C.G.A.
§ 9-11-26(b)). It need not be admissible if it appears reasonably
calculated to lead to admissible evidence. The scope governs every
device below.

## Interrogatories — O.C.G.A. § 9-11-33

Georgia **DOES allow written interrogatories**.

- **Cap: 50 interrogatories**, **including subparts** (O.C.G.A.
  § 9-11-33). Count each discrete subpart toward the limit; exceeding
  it requires leave of court.
- Service: any time after commencement (subject to the response-window
  rules above).
- Response due: **30 days** after service — **45 days** if served
  together with the summons (O.C.G.A. § 9-11-33).
- Form: each interrogatory answered separately and fully, under oath,
  with any objection stated in lieu of an answer.

```
INTERROGATORIES

Pursuant to O.C.G.A. § 9-11-33, [Defendant] requests that [Plaintiff]
answer the following Interrogatories separately and fully, in writing
and under oath, within the time allowed by law.

INTERROGATORY NO. 1: State the name, address, and telephone number of
each person with knowledge of the facts alleged in the Complaint.

ANSWER:
[Response]

INTERROGATORY NO. 2: [...]
```

## Requests for Production — O.C.G.A. § 9-11-34

- Reach documents, electronically stored information, and tangible
  things within a party's possession, custody, or control, and entry
  on land for inspection (O.C.G.A. § 9-11-34).
- Response due: **30 days** after service (**45 days** if served with
  the summons).
- Each request must be responded to specifically; production or a
  stated objection per item.

## Requests for Admission — O.C.G.A. § 9-11-36

> ⚠ **The deemed-admitted trap.** Under O.C.G.A. § 9-11-36, a matter
> is **admitted** unless the party served answers or objects **within
> the response period** (30 days, or 45 if served with the summons).
> Silence or a late response can conclusively establish the
> requested facts for the case. This is the single most dangerous
> discovery device for an unrepresented party — calendar RFA
> deadlines first.

- Each request must be admitted, denied, or met with a statement of
  why the party cannot truthfully admit or deny.
- A party may move to **withdraw or amend** an admission under the
  standard in O.C.G.A. § 9-11-36(b), but relief is not automatic.

## Depositions — O.C.G.A. §§ 9-11-30, 9-11-31

- **Oral depositions** under O.C.G.A. § 9-11-30; **depositions on
  written questions** under O.C.G.A. § 9-11-31.
- Notice must state the time and place; a non-party deponent is
  compelled by subpoena (see below).
- An organization may be deposed through a designated representative
  on described matters (O.C.G.A. § 9-11-30(b)(6)).

## Protective orders — O.C.G.A. § 9-11-26(c)

On motion and for good cause, the court may enter a protective order
to shield a party or person from annoyance, embarrassment,
oppression, or undue burden or expense — including orders that
discovery not be had, be had on specified terms, or be limited in
scope (O.C.G.A. § 9-11-26(c)). A motion for a protective order should
document a good-faith effort to resolve the dispute first.

## Supplementation — O.C.G.A. § 9-11-26(e)

A party is under a duty to **supplement** prior responses in the
circumstances set out in O.C.G.A. § 9-11-26(e) — including newly
identified witnesses and corrections of responses later learned to be
incorrect.

## Motion to compel and expenses — O.C.G.A. § 9-11-37

If a party fails to answer, answers evasively or incompletely, or
asserts unfounded objections, the requesting party may move to
**compel** under O.C.G.A. § 9-11-37(a). The motion should:

1. **Identify each deficient response** (which interrogatory / request
   for production / request for admission and why it is inadequate).
2. **Attach the requests and the responses** as exhibits.
3. **Document the effort to confer** in good faith to obtain the
   discovery without court action.
4. **Request specific relief** — an order compelling responses by a
   date certain and an award of the **reasonable expenses, including
   attorney's fees**, that O.C.G.A. § 9-11-37(a)(4) authorizes against
   the losing party absent substantial justification.

Stronger sanctions for disobeying a discovery order — including
striking pleadings, dismissal, or default — are available under
O.C.G.A. § 9-11-37(b).

## Subpoenas — O.C.G.A. § 24-13-23 and § 9-11-45

- Subpoenas to **non-parties** for testimony or documents issue under
  the Evidence Code, O.C.G.A. § 24-13-23, with the civil-discovery
  subpoena mechanics of O.C.G.A. § 9-11-45.
- A subpoena may command attendance at a deposition or trial and may
  require production of documents and tangible things.
- Serve a copy of any documents-only subpoena consistent with the
  notice requirements so opposing parties can object.

## Discovery in Magistrate Court

Magistrate Court ($15,000 civil cap) runs a **relaxed** procedure
under O.C.G.A. §§ 15-10-40 to 15-10-53 in which the formal CPA
discovery devices generally do not apply; discovery there is limited
and court-directed. The full §§ 9-11-26 to 9-11-37 framework above is
the State / Superior Court regime. See `ga-magistrate`. Note that
post-judgment discovery in aid of execution remains available under
O.C.G.A. § 9-11-69 (see `ga-post-judgment`).

## Composition

- For format baseline: `ga-statewide-format`
- For deadline arithmetic (period start, response windows):
  `ga-deadlines`
- For drafting the motion to compel: `ga-draft-motion`
- For the supporting affidavit / declaration: `ga-draft-declaration`
- For the usual debt forum and the relaxed Magistrate procedure:
  `ga-state-court`, `ga-magistrate`
- For consumer-debt RFP / RFA / interrogatory banks and the
  business-records (O.C.G.A. § 24-8-803(6)) foundation fight:
  `ga-consumer-debt`
- For verifying citations before serving or filing: `ga-fact-check`

## References

- `references/interrogatory-templates.md` — Georgia interrogatory
  sets (50-cap aware) and answer/objection forms
- `references/rfp-rfa-templates.md` — requests for production and
  requests for admission, with deemed-admitted warnings
- `references/motion-to-compel.md` — § 9-11-37 motion-to-compel
  scaffold with the expenses request
