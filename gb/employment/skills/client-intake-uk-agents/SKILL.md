---
name: client-intake-uk-agents
title: /legal-clinic-uk:client-intake
description: Structured intake — UK practice-area templates (housing, employment, immigration, family, consumer/debt, benefits, criminal defence), cross-area issue spotting, conflict flags, and triage classification. Produces a formatted case summary the student analyses and the supervisor reviews. Does NOT decide case acceptance. Use when starting a new client intake, running an intake interview, or writing up a new client's situation.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/client-intake
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: employment
language: en
sources:
- title: Readme
  path: references/intake-templates/README.md
---

# /legal-clinic-uk:client-intake

1. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → practice areas, intake templates, supervision style, flag triggers.
2. Use the workflow below.
3. Route to practice-area template. Listen for cross-area issues throughout.
4. Conflict check flags. Triage classification.
5. Output formatted case summary with AI-assisted label, verification prompts, supervision routing.

```
/legal-clinic-uk:client-intake
```

---

# Client Intake

## Purpose

Intake is one of the biggest bottlenecks in UK clinics. A student might spend 45 minutes interviewing, another hour writing it up, more time spotting the issues. Meanwhile the waitlist grows.

This skill structures the conversation, produces the write-up, spots issues across practice areas, and flags conflicts — so the student's time goes to analysis, not transcription.

**What it doesn't do:** decide whether to take the case. That's the student's analysis and the supervisor's judgment. Claude accelerates the information-gathering and structuring, not the lawyering.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → practice areas, intake templates (per practice area if multiple), supervision style, jurisdiction, flag triggers.

## Read the supervisor guide

Check for a practice-area guide at `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/guides/<practice-area>.md`. If one exists, use its intake questions, red flags, and good-fit criteria instead of the generic defaults below. If one doesn't exist, use the generic intake and note at the end of the intake summary: "This was a generic intake — your supervisor can tailor the questions for your clinic type with `/legal-clinic-uk:build-guide`."

## Workflow

### Step 1: Practice area routing

Which practice area does this intake start in? The client may not know — they know their problem, not the legal category.

> "Tell me what's going on — what brought you to the clinic today?"

From the answer, route to the appropriate intake template. If the clinic handles multiple areas and the problem spans them (housing client mentions immigration status, employment client mentions domestic violence), note all relevant areas — cross-area issue spotting is a feature, not a bug.

### Step 2: Practice-area-specific intake

Each practice area asks different questions. Use the template from `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` for this area. Defaults if none provided:

**Housing (England & Wales):**
- Type of housing: private rented, social / council, housing association
- What happened: Section 21 or Section 8 notice, actual eviction/lockout, disrepair, deposit dispute, anti-social behaviour allegation, unlawful eviction
- Tenancy details: start date, type (assured shorthold, assured, other), written tenancy agreement?
- Deposit: was it registered in an approved scheme (DPS, MyDeposits, TDS)? Prescribed information given?
- Rent: history, any arrears, Housing Benefit / Universal Credit housing costs involved?
- Disrepair / habitability: what conditions exist, when notified landlord, any response?
- Court date if possession claim already issued: Form N5 / accelerated possession claim?
- Timeline urgency: notice date, court date, bailiff warrant issued?

**Employment:**
- Employment status: employee, worker, or self-employed? Length of service?
- What happened: dismissal (fair / unfair / wrongful?), redundancy, discrimination, harassment, whistleblowing detriment, unpaid wages, holiday pay, constructive dismissal?
- Has ACAS early conciliation been started? Certificate number and issue date? (Critical for ET deadline calculation.)
- Relevant dates: last day of employment, act complained of, when client first knew
- Any internal grievance or appeal? Outcome?
- Timeline urgency: 3 months less one day from effective date of termination or act — **always flag this and confirm with supervisor before computing** `[LIMITATION-ACT-1980]`

**Immigration / Asylum:**
- Current immigration status and how entered
- Any prior applications, refusals, removals, encounters with the Home Office / Border Force
- Country conditions relevant to any asylum or humanitarian protection claim
- Family members and their statuses
- Criminal history (sensitive — explain why asking)
- Has any appeal been made? Upper Tribunal? Court of Appeal?
- Notice to complete questionnaire (NTQ), removal directions, reporting conditions?
- Timeline urgency: any pending hearings, deadlines, removal directions

**Family (England & Wales):**
- Relationship: marriage, civil partnership, cohabitation, separation, divorce
- What's at issue: child arrangements (residence / contact), financial remedy, domestic abuse protective injunction (non-molestation order, occupation order), forced marriage, FGM
- Children involved: ages, current arrangement, any safeguarding concerns
- Safety: any violence, threats, coercive control, fear — handle carefully; see cross-area flags; safety planning may be needed before legal advice
- Existing court orders (Child Arrangements Order, prohibited steps, etc.)
- Timeline urgency: any hearings scheduled; emergency injunction required?

**Consumer / Debt:**
- Type of debt or dispute: consumer contract, hire purchase, bank account, bailiff action, statutory demand, CCJ, bankruptcy petition
- Who's contacting them and how (FCA authorised? DCA? creditor direct?)
- Documentation: contracts, statements, Default Notices, default sums notices, final demand letters, statutory demand
- Has anything been filed against them: county court claim, statutory demand, winding-up petition?
- Timeline urgency: time to respond to CCJ claim (14 days from service), deadline to set aside statutory demand (18 days), answer to possession claim

**Benefits:**
- Which benefit: Universal Credit, PIP, ESA, Housing Benefit, Council Tax Support, Carer's Allowance, Child Benefit, other?
- What decision: refusal, reduction, sanction, overpayment recovery, appeal?
- Stage: mandatory reconsideration or First-tier Tribunal appeal?
- Dates: when decision made, when mandatory reconsideration requested, when FTT appeal lodged or due?
- Timeline urgency: mandatory reconsideration request (1 month from decision — extendable); FTT appeal (1 month from MR decision — extendable for good reason)

**Criminal defence (note: confirm clinic scope):**
- Nature of allegation, stage of proceedings
- Police interview (with or without solicitor?), charge, bail conditions, court date
- Whether client has a means-assessed right to legal aid (Legal Aid Agency)
- Timeline urgency: police bail return date, first hearing, any bail condition expiry

### Step 3: Cross-practice-area issue spotting

While running the practice-area template, listen for issues outside that area:

| Client says | Also flags |
|---|---|
| "I'm worried about my visa / leave to remain" | Immigration issue — even in a housing or employment intake |
| "My partner [threatening behaviour / controlling behaviour]" | DV / family law / non-molestation order — even in a debt intake |
| "I've been sanctioned on Universal Credit" | Benefits issue alongside housing or employment |
| "They're taking money from my wages" | Unlawful deduction — employment / consumer overlap |
| "The landlord threatened to call the Home Office" | Housing + immigration + possible unlawful eviction / retaliation claim |
| "I'm a carer and can't work" | Carer's Allowance / ESA / PIP alongside employment or housing |
| "I was dismissed when I told them I was pregnant" | Automatic unfair dismissal, sex discrimination — employment |

Note every cross-area issue in the summary. The clinic may handle it, refer it, or both — that's the supervisor's call.

### Step 4: Conflict check flags

Per whatever conflict-check process `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` describes. At minimum:

- Opposing party name(s) — does the clinic represent or have represented them?
- Related parties — anyone else the student or clinic might have a conflict with?
- Positional conflicts — is this case asking for something that would hurt another clinic client?

Flag for supervisor review. Don't resolve the conflict — surface it.

### Step 5: Triage classification

Not a case-acceptance decision — a triage input:

| Classification | Means |
|---|---|
| **Urgent** | Deadline in days, safety issue, removal directions, irreversible harm imminent |
| **Time-sensitive** | Deadline in weeks, harm ongoing but not immediately irreversible |
| **Standard** | No immediate deadline, can queue normally |
| **May be out of scope** | Issue is outside clinic's practice areas — flag for referral assessment (Citizens Advice, law centre, specialist provider) |

### Step 6: Supervision flag check

Per `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` supervision style and flag triggers. If formal queue or configurable flags are enabled, and a trigger is present (ET deadline, DV indicator, immigration status at issue, criminal exposure, benefits sanction), note the flag.

### Step 7: Deadline handoff — required deliverable

If the intake surfaces any timeline deadline (ET claim window, answer due to CCJ, housing possession hearing, asylum appeal, mandatory reconsideration deadline, FTT appeal, bail return date), **emit a copy-paste-ready `/legal-clinic-uk:deadlines --add ...` block as part of the intake output**. This is a required deliverable, not a suggestion.

Format each deadline as a fenced code block the student can copy, with every field pre-populated from the intake:

```
/legal-clinic-uk:deadlines --add
  case=[case slug or client-last-name-keyword]
  type=[et-claim|response|hearing|tribunal|limitation|appeal|mandatory-reconsideration|other]
  description="[one-line description of what is due]"
  due=[VERIFY — student + supervisor compute from triggering event]
  source="[triggering event + statute/rule cite, e.g., 'effective date of dismissal 2026-04-01, Employment Rights Act 1996 s.111(2) — ET1 due 3 months less one day']"
  owner=[student name]
  warnings=[14,7,3,1]
```

Rules:
- One block per deadline surfaced. Do not combine.
- Leave `due=` as `[VERIFY — student + supervisor compute]` when the deadline is jurisdictional (ET 3-month rule, limitation period, mandatory reconsideration window). Students must confirm with the supervisor and check ACAS early conciliation position for ET claims.
- When a date is given in a document (hearing notice, court order, possession claim), put that date in `due=`.
- If no deadline is surfaced, omit this section — don't fabricate one.

## Output

```markdown
# Intake Summary: [Client name or ID]

---
[AI-ASSISTED DRAFT — requires student analysis and supervising solicitor/barrister review]

**Privilege and confidentiality.** This summary is derived from client communications that may attract legal professional privilege (LPP) under English law. Whether legal advice privilege or litigation privilege applies depends on the purpose of the communication and the stage of proceedings. Distributing this summary beyond the supervising solicitor/barrister and the student team can waive privilege. Keep it in the clinic's privileged file store, mark it appropriately, and make distribution decisions with your supervisor.

Students are not solicitors or barristers. This summary is supervised student work — it does not constitute legal advice and must not be sent to any client or third party without supervisor review.
---

**Date:** [date] | **Intake by:** [student] | **Practice area:** [primary + any cross-area]

## Bottom line

[Take the case / Decline because X / Need more info on Y — next step is Z]

## Client's situation (in their words)

[The narrative the client gave, before legal categorisation. This is the human story.]

## Legal issues identified

*Every statutory, case, or regulatory citation in this section carries a provenance tag. `[user provided]` if the supervisor uploaded the text, `[legislation.gov.uk]` / `[uk-legal]` if fetched from an official source this session, `[BAILII]` if from a BAILII tool result, `[model knowledge — verify]` otherwise. The default is `[model knowledge — verify]`. A supervising solicitor/barrister who cannot verify a cite against a connector needs to see the tag to know what to check first.*

### Primary ([practice area])
- [Issue 1]: [one line with any cite tagged, e.g., "Housing Act 1988 s.21 — validity of Section 21 notice `[model knowledge — verify]`"]
- [Issue 2]: [one line]

### Cross-practice-area flags
- [Other area]: [what the client said that raised it]
  [UNCERTAIN: whether clinic handles this or refers — supervisor call]

## Key facts

| Fact | Source | Documentation |
|---|---|---|
| [fact] | [client statement / document provided] | [have it / need it] |

## Conflict check

**Opposing party:** [name(s)]
**Related parties:** [any]
**Flag:** [clear / needs conflict check against clinic database]

## Triage

**Classification:** [Urgent / Time-sensitive / Standard / May be out of scope]
**Driving deadline:** [if any — date and what it is]

## Deadlines to log

[One `/legal-clinic-uk:deadlines --add ...` block per surfaced deadline — Step 7.
If none, omit this section.]

## Jurisdictional notes

*Every statute, rule, or case citation carries a provenance tag — same vocabulary as `## Legal issues identified`. Default `[model knowledge — verify]`. When no research connector is reachable for this session, record it in the **Sources:** line of the reviewer note.*

**Jurisdiction:** [England & Wales / Scotland / Northern Ireland]
[Court/tribunal-specific procedural notes, limitation periods, relevant rules, with each cite tagged]

## Supervision flags

[If supervision style includes flags: which fired and why. If formal queue: "QUEUED for [Supervisor]."]

---

## Verification prompts for the student

Before analysis, verify:
- [ ] [Specific fact the intake relies on — confirm with client or documents]
- [ ] [Deadline date — confirm from the actual notice/court document or ACAS certificate, not client's memory]
- [ ] [Any legal conclusion above is a starting hypothesis — research before relying on it]
- [ ] [For ET claims: confirm ACAS early conciliation certificate number and issue date before computing deadline]

## What this summary does NOT do

This summary does not decide whether the clinic takes this case. That's your analysis and [Supervisor]'s judgment. It structures what the client told you so you can spend your time on the analysis instead of the write-up.

Students are not solicitors or barristers — this summary must not be shared with the client or used as legal advice until reviewed and approved by [Supervisor].
```

## Practice-area intake template references

Store practice-area-specific question sets at `references/intake-templates/[area].md`. Cold-start populates these from the supervisor's intake form(s); if none provided, use the defaults above.

## What this skill does NOT do

- **Decide case acceptance.** Student analyses, supervisor decides.
- **Resolve conflicts.** Flags them for the supervisor.
- **Give advice during intake.** Intake is gathering; advice comes after analysis and supervisor review.
- **Produce a final document.** The summary is a starting point — the student reads it, corrects anything mischaracterised, and builds the analysis from it.

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced.
