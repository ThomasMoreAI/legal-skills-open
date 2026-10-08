---
name: wa-hearings-codearranger
title: Washington Hearings — Preparation and Conduct
description: Prepare for and conduct hearings in Washington State superior court and district court. Use when the user asks about oral argument, motion hearings, Zoom or in-person hearings, courtroom etiquette, what to wear to court, how to address the judge, how to present argument, hearing-day checklist, or how to prepare as a pro se litigant for a hearing.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Courtroom Etiquette
  path: references/courtroom-etiquette.md
- title: Hearing Day Checklist
  path: references/hearing-day-checklist.md
- title: Oral Argument
  path: references/oral-argument.md
- title: Zoom Hearings
  path: references/zoom-hearings.md
---

# Washington Hearings — Preparation and Conduct

A hearing is where a well-prepared pro se litigant wins or loses the
motion. The judge has usually read the briefs but has questions. The
hearing is your chance to answer them directly.

This skill covers both in-person and remote (Zoom / Teams) hearings in
Washington superior court and district court, with specific guidance
for King County District Court (KCDC).

> **NOT LEGAL ADVICE.** This skill is a procedural and drafting
> aid for hearing preparation, not legal advice. Verify current
> rules, judge-specific practices, and remote-appearance protocols
> before the hearing. Pair with substantive review by counsel
> where stakes warrant.

## Core principles

1. **The judge has read the briefs** — do not recite them. Focus on
   the two or three points the judge needs clarified, and on any
   questions the court will plausibly have.
2. **Answer questions directly** — when the judge asks a question,
   answer it first, then explain. Never dodge.
3. **Concede what must be conceded** — acknowledge weak points;
   argue the stronger points. A pro se litigant who concedes nothing
   loses credibility.
4. **Respect the clock** — motion calendars are tight. Offer to
   submit on the briefs if the judge seems inclined; take two
   minutes rather than ten if the case is strong on the papers.
5. **Stay calm** — opposing counsel may misstate facts or law.
   Correct them briefly and with precision. Do not argue about
   who is being dishonest.

## When to use this skill

Triggers include:

- "I have a hearing on [date] — how do I prepare"
- "What do I wear to court"
- "How do I address the judge"
- "How does a Zoom hearing work"
- "What do I say at the beginning of oral argument"
- "What should I bring to the hearing"
- "The judge asked a question I didn't expect — how do I handle it"
- "Is this a contested or uncontested motion calendar"
- "KCDC hearing" / "King County District Court hearing"

## Washington hearing format

### Superior court — civil motion calendar

- **Note for Motion Docket** sets the hearing (typically a Friday)
- Opposing response due **4 court days before** the hearing
- Reply due **2 court days before** the hearing (CR 6(d))
- Most judges hold oral argument on contested civil motions but
  will take "on the briefs" on request
- Typical argument time: **5 to 10 minutes per side**

### King County District Court (KCDC)

- Civil motion calendars at **Renton / Redmond / Shoreline /
  Burien / Kent** locations
- Most motion hearings are on **Zoom** by default as of 2024 — check
  the current General Order and the hearing notice for the link and
  case-by-case instructions
- Opposing response due **3 court days before** the hearing
  (CRLJ 6(d))
- Court calls the calendar; parties confirm presence; judge takes
  cases in order

### Trial call / readiness hearings

- Confirm readiness, exhibits, witnesses, length estimate
- Rarely a place for argument on the merits
- Be brief and direct

## Preparing for the hearing — the three documents

At any contested hearing, bring (or have on-screen for Zoom):

1. **A one-page outline** — headings for your three key points,
   with bullet phrases. Do not write it out verbatim — you will
   read it.
2. **A question-and-answer sheet** — anticipated judge questions,
   with your one-sentence answer. Review this the night before.
3. **The exhibit / authority list** — record citations, pincites,
   and the key pages of each exhibit, so you can flip immediately
   if the judge asks.

## Structure of oral argument

### Opening — 15 to 30 seconds

"Good morning, Your Honor. [Name], pro se defendant. This is
Defendant's motion to [dismiss / compel / for summary judgment].
The central issue is [one sentence]. I respectfully request
[relief]."

### Middle — the 2 or 3 core points

- State each point, give the record support, cite the authority
- Keep pincites short: "CP 42" or "Exhibit A, page 3" or
  "*Hangman Ridge*, 105 Wn.2d at 785"
- Answer anticipated objections before the judge raises them

### Closing — 15 seconds

"For the reasons in the briefs and argued here, Defendant
respectfully requests the Court grant the motion. Thank you,
Your Honor."

### Rebuttal (if you are the movant)

- Only rebut what opposing argued orally — do not re-argue your
  opening
- Correct factual misstatements first
- If rebuttal is not needed, say "Nothing further, Your Honor."

## Handling judge questions

**Rules:**

1. **Stop whatever you were saying** — the judge's question is the
   priority
2. **Answer the question first** — yes, no, or the specific fact
3. **Then explain** — if the answer needs context, provide it
   briefly
4. **If you don't know** — say "I don't know, Your Honor" and
   offer to supplement; never speculate
5. **Thank the judge for the question only rarely** — use this
   only when the question is genuinely clarifying, not
   reflexively

### Common question types and how to handle

| Question type | Response pattern |
|---------------|------------------|
| "Where in the record is [X]?" | Cite immediately: "Your Honor, that is at CP [page] — Plaintiff's response to RFP No. [X]." |
| "What is your strongest authority?" | One case, one sentence: "*Sprague v. Sumitomo*, 104 Wn.2d 751 — the case is directly on point because [X]." |
| "Isn't your position inconsistent with [Y]?" | Concede if true, distinguish if not: "Your Honor, on point [Y] Defendant's position is [direct answer]." |
| "What relief are you asking for?" | State the specific relief in the proposed order: "Defendant requests the Court enter the proposed order attached at [location], which dismisses with prejudice." |
| "Why didn't you do [Z]?" | Honest answer; do not over-explain |

## Courtroom etiquette

### Address

- **"Your Honor"** — always, every time
- **"The Court"** — when referring to the judge in the third
  person ("The Court has authority under CR 56...")
- **"Ms. [Last name] / Mr. [Last name]"** — when referring to
  opposing counsel; not by first name
- **"Plaintiff" / "Defendant"** — when referring to parties; do
  not say "they" or "he/she" by name unless clarification is
  needed

### Posture

- **Stand** when the judge enters and when addressing the court
  (in-person)
- **Stand** when making argument, unless the judge says sit
- **Do not interrupt** — opposing counsel, the judge, or
  witnesses
- **Turn off your phone** — not just silent, off

### Tone

- **Measured** — speak at a slower pace than feels natural
- **Clear** — short sentences; drop adverbs
- **Respectful** — even when opposing misstates. "Counsel is
  incorrect on that point; the record shows..."
- **Not sarcastic, not humorous** — neither of those land in
  court

### Dress

- **Business formal** — suit and tie, or equivalent
- **Dark colors** — navy, charcoal, black
- **Conservative** — no distractions

For remote hearings: dress the same from the waist up. Judges
notice.

## Remote (Zoom / Teams) hearings

See `references/zoom-hearings.md` for detailed technical setup.
Quick rules:

- Log in **15 minutes early**, with the link tested the day before
- Use a **hard-wired ethernet or strong wi-fi**, not cellular
- **Neutral background** — a blank wall or a professional virtual
  background; not a bedroom or kitchen
- **Camera at eye level** — stack books under the laptop if
  needed
- **Good lighting** — window or lamp in front of your face, not
  behind
- **Mute by default** — unmute only when the court calls your
  case or you have a question
- **Display name**: "[Last name], [First name] — Pro Se Defendant"
- **Wait to be recognized** before speaking

## Day-of preparation

See `references/hearing-day-checklist.md` for the detailed list.
Core items:

- Printed briefs, exhibits, and outline in a binder (in-person) or
  organized in files (Zoom)
- Proposed Order — printed for in-person, ready to email
- Water — brief sips only
- Arrival time: **30 minutes early** (in-person), **15 minutes
  early** (Zoom)
- Phone off

## If something goes wrong

- **Technical failure (Zoom)** — call the court clerk immediately
  using the number on the hearing notice. Do not leave the meeting
  unannounced
- **Late opposing filing** — note the timing on the record and
  request leave to respond in supplemental briefing if prejudiced
- **Judge appears hostile** — do not escalate. Stay measured.
  Acknowledge any factual error you made. Ask the judge to clarify
  the concern: "Your Honor, if I may ask a clarifying question —
  is the Court's concern with [X] or [Y]?"
- **You misstate something** — correct it at the next moment:
  "Your Honor, I need to correct something I said earlier — the
  actual record is [correct statement]."
- **Opposing counsel is abusive** — do not respond in kind. The
  record speaks for itself. Stay polite

## After the hearing

- **Thank the judge** — "Thank you, Your Honor" on the way out
- **Present the proposed order** — if the motion was granted and
  the judge wants the order on the bench, hand it up
- **Note orders from the bench** — if the judge rules orally, note
  the precise ruling on your outline immediately
- **Follow up in writing** — if the court requested supplemental
  briefing, calendar it

## References

- `references/courtroom-etiquette.md` — detailed etiquette, attire,
  address conventions
- `references/oral-argument.md` — full oral-argument structure and
  sample outlines
- `references/zoom-hearings.md` — remote-hearing technical and
  format rules, with KCDC specifics
- `references/hearing-day-checklist.md` — what to bring, what to
  do the morning of, how to arrive

## Notes

- **Every judge is different** — KCDC Judge Smith may run a tight
  calendar with strict time limits; Judge Jones may invite
  extended argument. Watch your judge's calendar once before your
  own hearing if possible
- **Record the hearing** — all hearings are recorded; transcripts
  are available by request. You do not need to take your own
  recording
- **Do not file anything new on the day of the hearing** — late
  filings annoy the court and may be struck
