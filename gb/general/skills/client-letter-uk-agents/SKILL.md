---
name: client-letter-uk-agents
title: /legal-clinic-uk:client-letter
description: Routine UK client correspondence from templates — appointment confirmations, document requests, brief "we filed it" updates. Plain English, required elements including SRA client care obligations, supervision routing. NOT substantive advice. Use when a student needs to send routine correspondence, an appointment confirmation, a document request letter, or a brief status note to a client.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/client-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /legal-clinic-uk:client-letter

1. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → plain-language standards, supervision style, clinic contact info.
2. Use the templates and workflow below.
3. Match type to template. Plain-English check. SRA client care sign-off.
4. Output with AI-assisted label, supervision routing.

Scope: routine only. Substantive advice → `/legal-clinic-uk:status client` or a conversation with the supervisor.

```
/legal-clinic-uk:client-letter appointment
```

```
/legal-clinic-uk:client-letter doc-request
```

---

# Client Letter: Routine Correspondence

## Purpose

UK law school clinics send a lot of routine correspondence: "your appointment is Tuesday at 2pm," "please bring your tenancy agreement," "we filed your ET1." This skill handles those from templates so students aren't typing the same letter every week.

**Scope: routine only.** Substantive advice, bad news, case strategy — those are `/legal-clinic-uk:status client` or a conversation with the supervisor, not a template letter.

**Client care obligations.** Under the SRA Code of Conduct 2019, clients have a right to receive clear information about who is dealing with their matter, who is supervising, how to make a complaint, and the basis of the service provided. Even routine letters from a law school clinic should comply with the spirit of these obligations. The templates below include the required sign-off identifying the student and supervising solicitor/barrister. `[SRA-CODE]`

## Load context

`~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → plain-language standards, supervision style, clinic contact info.

## Pedagogy check

Read the supervisor guide for this practice area at `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/guides/<practice-area>.md`. Check the `pedagogy_posture` setting:

- **`guide` (default):** Produce the structure and the checklist. Ask the student to draft each section. Give feedback.
- **`assist`:** Produce the letter. Flag items for student review.
- **`teach`:** Don't produce the letter. Ask the student to draft it. Give feedback.

If no guide exists, use `guide`. Whatever the posture, the output always includes: "**Pedagogy mode: [assist/guide/teach]** — set by your supervisor's guide."

## Sign-off and student disclosure

Every letter from the clinic must make clear that the writer is a law student (not a qualified solicitor or barrister) and that the work is supervised by the named supervising solicitor or barrister. The templates below use a standard form — confirm this is consistent with the clinic's client care practices and any specific requirements of the clinic's authorisation model.

Where the clinic is authorised by the SRA, the SRA client care rules apply to correspondence as well as to substantive advice. Clients must be told who to contact if they are unhappy with the service and how to complain. For routine appointment letters this can be a brief line; for any letter that touches on the client's legal position, the supervisor should confirm the sign-off language is adequate. `[SRA-CODE]`

## Letter types

> **Review label goes OUTSIDE the letter.** The `[AI-ASSISTED DRAFT — requires review per plugin config supervision step]` tag is a note to the student, not part of the letter body. Place it above the rendered template, never inside the fenced letter content.

### Appointment confirmation

*Review label for the student (not for the client — strip before sending):*
`[AI-ASSISTED DRAFT — requires review per plugin config supervision step]`

```markdown
Dear [Client],

This confirms your appointment at [Clinic name]:

**Date:** [date]
**Time:** [time]
**Where:** [address / room / or "by phone at [number]"]
**With:** [student name]

**Please bring:** [documents needed — from case notes or leave as prompt for student to fill]

If you need to reschedule, please call us at [clinic phone] at least 24 hours beforehand.

If you have any concerns about the service you receive, please contact [supervisor name] at [contact details].

[Student name]
Law Student — not a qualified solicitor or barrister
All work is supervised by [Supervisor], [Solicitor / Barrister], [SRA / BSB authorisation number]
[Clinic name] | [phone] | [hours]
```

### Document request

*Review label for the student (not for the client — strip before sending):*
`[AI-ASSISTED DRAFT — requires review per plugin config supervision step]`

```markdown
Dear [Client],

To move your case forward, we need the following documents from you:

- [Document 1 — e.g., "Your tenancy agreement"]
- [Document 2 — e.g., "The notice you received from your landlord"]
- [Document 3]

**How to get them to us:** [drop off at clinic / email to [address] / bring to next appointment]

**Please send by:** [date — if there's a deadline, say why: "We need these by [date] so we can file your response before the court deadline."]

If you don't have some of these or aren't sure what we mean, call us at [clinic phone] and we can help.

If you have any concerns about the service you receive, please contact [supervisor name] at [contact details].

[Student name]
Law Student — not a qualified solicitor or barrister
All work is supervised by [Supervisor], [Solicitor / Barrister], [SRA / BSB authorisation number]
[Clinic name] | [phone] | [hours]
```

### Brief status update

For routine "we filed it" / "we're waiting" updates. (Fuller status updates → `/legal-clinic-uk:status client`.)

*Review label for the student (not for the client — strip before sending):*
`[AI-ASSISTED DRAFT — requires review per plugin config supervision step]`

```markdown
Dear [Client],

Quick update: [one-line what happened — "We submitted your ET1 claim to the Employment Tribunal on [date]" / "We sent the letter to your landlord on [date]"].

**What's next:** [one line — "We are waiting for their response" / "The tribunal will contact you about a hearing date"].

You do not need to do anything right now. We will let you know when we do.

If you have any concerns about the service you receive, please contact [supervisor name] at [contact details].

[Student name]
Law Student — not a qualified solicitor or barrister
All work is supervised by [Supervisor], [Solicitor / Barrister], [SRA / BSB authorisation number]
[Clinic name] | [phone] | [hours]
```

## Before sending

Sending a letter to a client is a consequential action. The gate is the supervision workflow in `## Supervision style` in `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`. That gate holds: every letter clears review before it leaves the clinic.

Before sending any of the letters above, confirm:

1. The draft has been reviewed per the supervision protocol (queue / flag / lighter-touch).
2. All internal review labels (`[AI-ASSISTED DRAFT]`, any `[VERIFY]` or `[FACT NEEDED]` tags) have been removed from the client-facing copy.
3. The sign-off correctly identifies the student and the supervising solicitor/barrister with authorisation details.
4. The letter complies with any client care obligations applicable to the clinic's authorisation model. `[SRA-CODE]`

**This is a student draft for supervising solicitor/barrister review, not a final letter.** Sending it has legal consequences for the client and may constitute a communication on the client's behalf. A licensed supervising solicitor or barrister reviews, edits, and signs off before the letter leaves the clinic.

## Plain-English check

Per `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` standards. Short sentences. No jargon. If a legal term is unavoidable, explain it the first time: "We filed your 'ET1' — that's the form that starts your Employment Tribunal claim."

## Supervision routing

Per `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`. Routine correspondence may or may not be a flag trigger depending on the supervision style. If lighter-touch: these go out after student review without a queue step. If formal queue: even routine letters queue.

## What this skill does NOT do

- **Substantive advice.** If the letter would say "here's what I think about your case" or "here's what you should do," that's not routine — that's `/legal-clinic-uk:status client` or a conversation with the supervisor first.
- **Bad news.** Case closing, adverse ruling, can't-help — those need thought, not a template. Flag for supervisor.
- **Anything to opposing solicitors or a court or tribunal.** Different audience, different skill (`/legal-clinic-uk:draft` or `/legal-clinic-uk:status court`).
