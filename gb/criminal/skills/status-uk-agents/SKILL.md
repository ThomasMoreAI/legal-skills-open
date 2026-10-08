---
name: status-uk-agents
title: /legal-clinic-uk:status
description: Case status summary by audience — client-facing (plain language), internal (for the supervising solicitor or barrister), or tribunal/court-ready (formal format per local court or tribunal rules). Same facts, different framing and depth. Use when a student needs to update the client, brief the supervisor, or prepare a court or tribunal status report.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/status
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: criminal
language: en
---

# /legal-clinic-uk:status

1. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → supervision style, plain-language standards, jurisdiction.
2. Use the workflow below. Read case notes.
3. Generate for the specified audience:
   - `client` — plain language, what happened/next/you do/reach us
   - `internal` — procedural posture, done since last check-in, upcoming, needs supervisor input, student's assessment
   - `court` — formal status report in caption format per current court/tribunal rules
4. Supervision routing per audience (client-facing and court/tribunal-ready usually flag).

```
/legal-clinic-uk:status client
```

```
/legal-clinic-uk:status internal
```

```
/legal-clinic-uk:status court
```

---

# Status: Audience-Aware Case Summaries

## Purpose

UK law school clinics generate enormous numbers of status updates — to clients, to supervisors, to co-advisers, to courts and tribunals. Same case, same facts, completely different documents. This skill takes the case notes and produces the right summary for the right reader.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → supervision style, plain-language standards (for client-facing), jurisdiction.
Case notes for facts.

## Audience modes

### Client-facing

**Reader:** The client. Probably stressed. Possibly unfamiliar with legal process. Reading level per `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` plain-language standards (default plain English / approx. 6th grade equivalent). Follow SRA client care obligations — the client has a right to understand what is happening in their case. `[SRA-CODE]`

**Include:**
- What's happened since they last heard from the clinic
- What's happening next and when
- What (if anything) they need to do
- How to reach the clinic

**Don't include:**
- Legal analysis (they don't need to know the IRAC)
- Weaknesses in their case (unless it's time to have that conversation — and that's a call for the supervisor, not a status update)
- Jargon. If a legal term is unavoidable, explain it.

*Review label for the student (not for the client — strip before sending):*
`[AI-ASSISTED DRAFT — requires student review and supervision step per plugin config]`

Check whether your jurisdiction's student practice rules require any specific form of student/non-solicitor disclosure in client letters. Under the SRA Code of Conduct 2019, clients must be informed clearly about who is acting for them and the supervisory structure. `[SRA-CODE]`

```markdown
Dear [Client],

I wanted to update you on your case.

**What's happened:** [Plain English. "We sent a letter to your landlord on [date]" not "Correspondence was issued to the Respondent."]

**What's next:** [What and when. "The tribunal has set a hearing date of [date] at [time]. You must attend." Or: "We are waiting for the other side to respond. This could take a few weeks."]

**What you need to do:** [Specific and clear. Or: "Nothing right now — we will let you know when we need something from you."]

**How to reach us:** [Clinic phone, hours, student name]

[Student name]
Law Student — not a qualified solicitor or barrister
All advice is given under the supervision of [Supervisor], [Solicitor / Barrister], [SRA / BSB authorisation number]
[Clinic name]
```

**Before sending:** sending a client status update is a consequential action. The gate is the supervision workflow in `## Supervision style` in `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`. Confirm the draft has been reviewed per the supervision protocol (queue / flag / lighter-touch) and all internal review labels have been removed from the client-facing copy. Confirm the sign-off line identifies the student correctly and the supervising solicitor/barrister as required.

### Internal (for the supervisor)

**Reader:** The supervising solicitor or barrister. Knows the law. Wants to know where the case stands and what the student needs from them.

**Include:**
- Procedural status (where in the life of the case — pre-claim, post-issue, hearing listed, etc.)
- What's been done since last check-in
- What's coming up (deadlines, hearings, tribunal dates)
- Issues needing supervisor input
- Student's assessment (how it's going, concerns, strategic questions)

```markdown
# Status: [Client] — [Matter] — [date]

**Student:** [name] | **Procedural posture:** [pre-claim / ET1 submitted / ET3 received / preliminary hearing listed / main hearing listed / post-hearing / etc.]

## Since last check-in

- [What's been done]

## Upcoming

| Date | What | Action needed by |
|---|---|---|
| [date] | [deadline/hearing] | [date] |

## Needs supervisor input

- [Question or decision point — specific]

## Student's assessment

[How it's going. Strengths, concerns, strategic questions. This is where the student's thinking shows.]

---
[AI-ASSISTED DRAFT — student should revise the assessment section especially;
that's your thinking, not a summary of notes]
```

### Court/tribunal-ready

**Reader:** A judge, tribunal panel, or clerk. Formal. Specific to what the court or tribunal needs. Format varies by forum.

**E&W Courts (CPR):** follow the applicable Practice Direction for case management statements and directions questionnaires (N180 for county court allocation; case management information sheets for specialist courts).

**Employment Tribunal:** no standard "status report" form — follow any specific case management order or presidential guidance. The format is a letter or brief document to the tribunal identifying case status and any outstanding matters.

**First-tier Tribunal (Immigration):** follow Tribunal Procedure (First-tier Tribunal) (Immigration and Asylum Chamber) Rules 2014; any scheduled case management review directions.

**Format:** Per local rules and practice directions. Caption, statement of truth if required, signature block (student with supervisor's authorisation clearly stated), service if filed.

```markdown
═══════════════════════════════════════════════════════════════════════
  AI-ASSISTED DRAFT — requires student analysis and supervising
  solicitor/barrister review
  Court and tribunal filings ALWAYS require supervisor review before filing
═══════════════════════════════════════════════════════════════════════

[Caption / header per jurisdiction — VERIFY against current court/tribunal rules]
[VERIFY: format per applicable Practice Direction / Presidential Guidance / local directions]

STATUS REPORT / CASE MANAGEMENT INFORMATION

[Party] submits this status report pursuant to [the court's/tribunal's order
of [date] / the applicable case management directions / in advance of the
[case management hearing / review] scheduled for [date]].

1. Procedural history: [brief]

2. Current status: [directions compliance / outstanding steps / any agreed timetable]

3. Outstanding matters: [what's pending]

4. Proposed next steps: [scheduling, if the court/tribunal wants input]

[Signature block — student name, law student not a solicitor/barrister,
acting under supervision of [Supervisor], [Solicitor/Barrister],
[SRA/BSB authorisation number], [Clinic name]]

[Certificate of service if filing — per applicable rules]

---

[VERIFY: caption format, applicable rules, service requirements — per current
court/tribunal procedural rules and any specific directions in this case]
`[CPR-RULE]`
```

## Supervision routing

Per `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`:
- Client-facing → usually a flag trigger (client communication)
- Internal → no flag (it's going to the supervisor anyway)
- Court/tribunal-ready → always flagged if formal queue enabled; always requires supervisor review

## What this skill does NOT do

- **Decide what to tell the client.** Especially on bad news or case weaknesses — that's a conversation for the student and supervisor, then the student and client. Status updates are status, not strategic advice.
- **File anything with a court or tribunal.** Drafts the document; supervisor reviews; filing per clinic procedure.
- **Replace the student's assessment in internal status.** The "student's assessment" section is the student's thinking — the draft can scaffold it but can't write it.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`.
