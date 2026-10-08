---
name: wa-discovery-codearranger
title: Washington Discovery Practice
description: 'This skill should be used when drafting, responding to, or compelling discovery in a Washington civil case across any subject matter. Triggers include "requests for production", "interrogatories", "RFA", "requests for admission", "meet and confer", "CR 26(i) conference", "CRLJ 26(f) conference", "motion to compel", "discovery responses", "discovery objections", "RFP objections", "privilege log", "proportionality", "CR 33 limits", "CR 34", "CR 36", "CR 37", "CRLJ 37". Covers the matter-neutral procedural framework: discovery request drafting, response drafting and objections, meet-and-confer mechanics, and the full motion-to-compel workflow with mandatory fee-shifting under CR 37(a). Subject-matter-specific request banks (e.g., debt-buyer RFPs targeting chain of title) live with the relevant subject-matter skill (e.g., wa-consumer-debt). Compose with wa-statewide-format, wa-pro-se, wa-law-references, wa-draft-motion, and wa-fact-check.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-discovery
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

# Washington Discovery Practice

Discovery is where civil cases are won or lost. This skill covers
the **matter-neutral procedure**: request and response drafting,
objection frameworks, the meet-and-confer requirement, and the
motion-to-compel workflow. Subject-matter-specific request banks
(debt-buyer discovery targeting chain of title, landlord-tenant
discovery targeting notice, etc.) live with the relevant
subject-matter skill.

## What this skill covers

- **Drafting** discovery requests: RFPs, interrogatories, RFAs
- **Responding** to opposing discovery: objection frameworks,
  privilege, proportionality
- **Meet and confer** letters under CR 26(i) / CRLJ 26(f)
  (required before any discovery motion)
- **Motion to compel** under CR 37(a) / CRLJ 37(a) with mandatory
  fee-shifting request

Matter-neutral templates live in `references/`:

- `references/meet-and-confer.md` — CR 26(i) / CRLJ 26(f) letter
  template and certification language
- `references/objection-responses.md` — objection-response
  framework, common misuses, how to preserve objections

For subject-matter-specific request banks, see the relevant
subject-matter skill (e.g., `wa-consumer-debt` provides
`references/rfp-debt-buyer.md`,
`references/interrogatories-debt-buyer.md`,
`references/rfa-debt-buyer.md`, and
`references/meet-and-confer-debt-buyer.md`).

## The CR / CRLJ framework

Washington discovery is governed by Civil Rules **26–37**
(superior court) and **CRLJ 26–37** (district court — largely
parallel). Key rules:

- **CR / CRLJ 26** — general scope. Any non-privileged matter
  **relevant to a claim or defense and proportional to the needs
  of the case** (the 2017 amendment adopted federal-style
  proportionality).
- **CR 26(i) / CRLJ 26(f)** — **conference of counsel** required
  before filing any discovery motion.
- **CR 33 / CRLJ 33** — interrogatories to parties.
- **CR 34 / CRLJ 34** — requests for production of documents.
- **CR 36 / CRLJ 36** — requests for admission.
- **CR 37 / CRLJ 37** — motion to compel and sanctions.

### Timing

- **Response period** — 30 days from service (verify against
  current rule text via `wa-law-references/references/online-sources.md`).
- **Add 3 days** for service by mail (CR 6(e) / CRLJ 6(d)).
- **Email service** — only with consent (CR 5(b)).

### Limits

- **CR 33(b)** — 40 interrogatories per party in superior court,
  including subparts, unless court orders more.
- **CRLJ 33** — similar limits; verify current rule text.
- **No preset limit on RFPs or RFAs**, but proportionality
  constraints apply under CR 26(b)(1).

## Drafting principle: aim at the element the opposing party must prove or defend

Every discovery request should target an **element** the opposing
party must prove or defend. A request that does not map to an
element is likely objectionable as not proportional.

Mapping an element-by-element strategy is subject-matter specific:

- In a **debt-collection** case, elements include standing,
  agreement, performance, breach, and damages — see
  `wa-consumer-debt/SKILL.md` for the full element list and
  request bank.
- In a **landlord-tenant** case, elements typically include the
  tenancy, notice, breach, and damages.
- In a **tort** case, elements typically include duty, breach,
  causation, and damages.

Subject-matter skills supply the element list and the
ready-to-adapt request bank. This skill supplies the procedural
framework.

## Drafting checklist (matter-neutral)

- [ ] Define terms once (usually numbered paragraph at the start)
- [ ] Use plain English — do not reuse boilerplate that assumes
      a different case
- [ ] Specify time frames ("from origination to date of filing")
- [ ] Reference documents by specific name when known
- [ ] Identify the element the request targets (keeps
      proportionality challenges simple)
- [ ] Number sequentially and consistently
- [ ] Include a short certificate of service at the end

## Response strategy when you are the responder

### Preserve objections up front

Every response should begin with a **General Objections** section
preserving:

- Attorney-client privilege
- Work-product doctrine
- Proportionality / CR 26(b)(1)
- Relevance
- Overbreadth / unduly burdensome
- Other privileges (marital, clergy, medical — if applicable)

### Respond to each request

For each request:

1. Restate the request
2. State specific objections (in addition to general objections)
3. **Subject to and without waiving** the objections, respond
4. For **RFPs** — identify the responsive documents by Bates
   range or description; never say "all documents in my
   possession" without specifying what those are
5. For **IROGs** — answer fully or state that no responsive
   information exists
6. For **RFAs** — admit, deny, or state that after reasonable
   inquiry the matter cannot be admitted or denied (requires
   showing actual inquiry)

### Sign under oath

Interrogatory responses must be **verified under penalty of
perjury** (CR 33). RFP and RFA responses are signed by counsel
(or pro se party) as a representation under CR 26(g) — which
carries CR 11-like consequences for unfounded responses.

## Meet and confer — CR 26(i) / CRLJ 26(f)

**You cannot file a motion to compel without a prior
meet-and-confer effort.** The motion must include a certification.

Format of a CR 26(i) effort:

1. **Written request** listing deficient responses (not a rant —
   a letter)
2. **Reasonable time for response** (typically 7–10 business
   days)
3. **Phone or Zoom follow-up** if the written request is not
   substantively answered
4. **Certification language** in the motion describing the
   effort

Template at `references/meet-and-confer.md`.

Subject-matter skills may supply pattern paragraphs for common
deficiencies (e.g., `wa-consumer-debt/references/meet-and-confer-debt-buyer.md`).

Do **not** skip this step. Courts routinely deny motions to
compel that lack proper certification.

## Motion to compel workflow

1. **Identify the deficient responses** specifically — by request
   number and by reason (non-response, incomplete, privileged
   without log, etc.)
2. **Meet and confer** in writing and document the effort
3. **Draft the motion to compel** (via the `wa-draft-motion`
   skill):
   - Cite CR / CRLJ 37(a)
   - Include CR 26(i) / CRLJ 26(f) certification
   - Request **expenses under CR 37(a)(4) / (a)(5)** (mandatory
     if motion granted — see
     `wa-law-references/references/fees-and-costs.md`)
   - Request order compelling specific relief (production,
     verified answer, deemed admission)
4. **Note the motion** (via the `wa-draft-note` skill)
5. **Draft proposed order** (via the `wa-draft-order` skill)
6. **Serve and file** with Certificate of Service (via the
   `wa-file-packet` skill)

## Typical discovery sequence

Most civil cases benefit from staged discovery:

- **Round 1** — foundational / threshold issues (standing,
  notice, the core transaction)
- **Round 2** — merits detail (damages, performance, causation)
- **Round 3** — counterclaim predicate (if counterclaim pleaded)

Timing: after each round, assess gaps; move to compel on the
largest gaps before the next round; continue through roughly 60
days before trial unless the court sets a tighter cutoff.

Subject-matter skills (e.g., `wa-consumer-debt`) specify the
contents of each round for their subject.

## Notes

- **Read the responses carefully** — opposing objections
  frequently waive through incomplete preservation.
- **Keep a discovery log** — date served, response due, response
  received, deficiencies identified, meet-and-confer sent,
  motion filed.
- **Calendar the 30-day deadlines rigorously** — missed RFA
  deadlines deem the RFA admitted under CR 36(a).
- **Do not over-request** — a focused 15-request RFP set is more
  effective than a 100-request set.
- **Not legal advice.** This skill orchestrates draft
  generation; the user is responsible for every word filed.
