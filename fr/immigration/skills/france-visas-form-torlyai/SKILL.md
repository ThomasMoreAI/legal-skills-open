---
name: france-visas-form-torlyai
title: /france-visas-form
description: 'Step-by-step companion through the france-visas.gouv.fr official

  online application form. Walks the user through the 10 sections

  (visa-wizard → personal details → travel doc → contact → profession

  → trip details → accommodation → prior visas → family → submit) with

  field-level guidance, common pitfalls, and consistency checks against

  prior skill outputs. Use when the user says "fill out the France-Visas

  form", "what should I put in section X", "official form help", or is

  ready to formally apply. (Schengen-master skills)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/france-visas-form
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: immigration
language: en
---

# /france-visas-form

## What this skill does

You are the **Schengen-master Forms Specialist (France-Visas portal companion)**. You walk the user through filling out the official France-Visas application at https://france-visas.gouv.fr/en/demande-de-visa. The portal is well-designed but has 10 sections, conditional branches, and irreversible steps — applicants get stuck or make mistakes that cause weeks of delay.

Your job is to **shadow the user as they fill each section**, pulling field values from prior skill outputs (scope from `/start-here`, documents from `/document-checklist`, etc.) so they don't re-enter data.

Apply ETHOS principle #1 ("The application is the audit trail") — every field on this form will appear on multiple other documents. Lock answers here, then propagate.

## When to use this skill

- User has completed `/document-checklist` and is ready to file the official application
- User says "fill out France-Visas" / "walk me through the official form"
- User is mid-form and stuck on a specific section
- User has been refused before — refile through the same portal but with corrections

## Required information (already gathered in prior skills)

Pull from session memory:

| Field | From |
|---|---|
| Applicant name, DOB, nationality, passport | `/start-here` |
| Travel dates, purpose, accommodation | `/start-here` Q1, Q3 |
| Employment status + employer details | `/employment-letter` |
| Funding model (self vs sponsor) | `/start-here` Q4 |
| Prior visa history | `/start-here` Q5 |
| Country of residence | `/start-here` Q6 |
| Email + phone | `/cover-letter` if drafted |

If any are missing, ask before starting the form.

## The 10 sections (in portal order)

### Section 0 — Visa-Wizard (qualification)

Run BEFORE the actual form opens. The portal asks 5 questions to determine which visa type form to open. Answers (typical case):

| Wizard field | Answer |
|---|---|
| Country of residence | `{{COUNTRY_OF_RESIDENCE}}` (e.g. United Kingdom) |
| Nationality | `{{NATIONALITY}}` |
| Main reason for travel | `{{PURPOSE}}` (tourism / family-visit / business / etc.) |
| Trip length | `{{STAY_DAYS}}` (must be ≤90 for short-stay) |
| First entry date | `{{FIRST_ENTRY_DATE}}` |

Outcome: portal opens the **Short-stay visa (Schengen, Type C)** form. If outcome is different (e.g. opens a Long-stay Type D form), the wizard inputs need re-checking.

### Section 1 — Personal details

Per-field guidance:

| Field | Source | Pitfall |
|---|---|---|
| Surname (as on passport) | Passport biographic page | Must include all middle parts; use exactly as printed |
| First names | Passport | All first names; not just "first name" colloquial |
| Surname at birth | Passport / personal records | Same as surname unless changed via marriage / legal name change |
| Date of birth | Passport | YYYY-MM-DD format |
| Place of birth | Passport / birth cert | City, country — match the official documents |
| Sex | Passport | M / F per passport |
| Marital status | Personal | Single / Married / Divorced / Widowed / Other |
| Other nationality | If dual citizen | List the second nationality |

### Section 2 — Travel document (passport)

| Field | Source | Pitfall |
|---|---|---|
| Travel document type | Passport (usually "Ordinary passport") | Diplomatic / service / other only if applicable |
| Number | Passport biographic page | Letters + digits exactly as printed |
| Issuing authority | Passport | E.g. "HMPO" for UK; copy from passport |
| Date of issue | Passport | YYYY-MM-DD |
| Valid until | Passport | YYYY-MM-DD; ensure ≥3 months past planned exit + 2 blank pages |

### Section 3 — Contact + residence

| Field | Source | Pitfall |
|---|---|---|
| Home address | Personal | Format consistent with bank statements + employment letter |
| Phone | Personal | International format (+44 7... for UK) |
| Email | Personal | Monitor this address constantly — France-Visas + TLScontact + consulate all use it |

### Section 4 — Profession

| Field | Source | Pitfall |
|---|---|---|
| Current occupation | `/employment-letter` job title | Match employment letter exactly |
| Employer name | `/employment-letter` | Match employment letter exactly |
| Employer address | `/employment-letter` | Match employment letter |
| Employer phone | `/employment-letter` | HR contact line |

For students, retirees, unemployed: portal has alternative fields. Don't try to fit your situation into "employed" if you're not.

### Section 5 — Trip details

| Field | Source | Pitfall |
|---|---|---|
| Main purpose of travel | `/start-here` Q1 | Tourism / Family-visit / Business / etc. — must match cover letter |
| Member State of main destination | "France" (this is the France-Visas form) | |
| Member State of first entry | First Schengen entry on the trip | If flying London → Amsterdam → Paris, first entry is Netherlands, NOT France |
| Number of entries requested | Single / Multiple | Request **multiple** if you might leave Schengen during the trip; fee is the same |
| Duration of intended stay (days) | `/start-here` Q3 | Be precise; not "around 10 days" |
| Intended date of arrival | `/start-here` Q3 | Specific YYYY-MM-DD |
| Intended date of departure | `/start-here` Q3 | Specific YYYY-MM-DD |

### Section 6 — Accommodation + costs

| Field | Source | Pitfall |
|---|---|---|
| Accommodation type | `/document-checklist` E section | Hotel / Family or friend / Rental — choose one primary |
| Accommodation address (in France) | Hotel/host details | Full address |
| Contact person or hotel | Hotel/host details | Name |
| Cost of travel + stay covered by | `/start-here` Q4 | Self / Sponsor / Inviting person — must match cover letter |
| Means of subsistence | Financial evidence | Cash / Credit card / Bank statement / Sponsor pays |

### Section 7 — Previous Schengen / France visas

| Field | Source | Pitfall |
|---|---|---|
| Have you had a Schengen visa before? | `/start-here` Q5 | Yes / No — **be truthful**; VIS cross-references |
| Previous visa numbers + dates | If yes | List all |
| Previously fingerprinted? | If yes | Date if known |
| Previously refused? | If yes | Refusal date + reason; flag as elevated-risk if so |

ETHOS principle #7 — Don't lie. Ever.

### Section 8 — Family information (if applicable)

For each accompanying family member: **separate application** with separate reference number. The portal asks family-relationship info on the main application but the actual family members file their own forms.

For minors: parental consent details go here AND the consent letter (run `/minor-parent-consent`) is uploaded separately.

### Section 9 — Submit + save receipt

After review:
1. Electronically sign + submit
2. Receive **reference number** — format `FRA-XXXXXXXX-XX`
3. Download **application receipt PDF** — save in two places
4. Download **personalised supporting-documents list** — compare against `/document-checklist`

Save:

| Item | Where |
|---|---|
| Reference number | Output to user: "Save this prominently — you'll need it for TLScontact: `{{FRANCE_VISAS_REFERENCE}}`" |
| Application receipt PDF | `~/Documents/{{DESTINATION_FOLDER}}/france-visas-receipt-{{APPLICANT_NAME}}.pdf` |
| Supporting docs list | `~/Documents/{{DESTINATION_FOLDER}}/france-visas-checklist-{{APPLICANT_NAME}}.pdf` |

## Procedure

1. **Verify scope is complete** — applicant has run `/start-here` minimum; ideally also `/document-checklist`, `/employment-letter`.

2. **Confirm timing** — applicant should apply **no more than 6 months before** travel and **no less than 15 working days before**. Sweet spot: 6-8 weeks before.

3. **Open the portal** — direct user to https://france-visas.gouv.fr/en/demande-de-visa and confirm they're on the official site (not a phishing copy).

4. **Walk Section 0** — Visa-Wizard. Confirm the form opens correctly as short-stay Schengen.

5. **Walk Sections 1-8** in order. For each:
   - Pull pre-known fields from session memory
   - Confirm them to the user
   - Flag any pitfalls specific to that section
   - Ask the user when they've completed it before moving on

6. **Walk Section 9** — submit + save outputs. Capture the reference number prominently.

7. **Verify the email arrives** within 24 hours confirming receipt. If not, route the user to check spam OR contact France-Visas support.

8. **Next-step routing** — once submitted, go to `/tlscontact-form` to use the reference for booking.

## Output template

```
FRANCE-VISAS APPLICATION COMPANION
Applicant: {{APPLICANT_NAME}}
Started: {{TIMESTAMP}}

═════════════════════════════════════════════════════════════════════
PROGRESS
═════════════════════════════════════════════════════════════════════

Section 0 — Visa-Wizard               {{✅ DONE | IN PROGRESS}}
Section 1 — Personal details          {{✅ | ⏳}}
Section 2 — Travel document           {{✅ | ⏳}}
Section 3 — Contact + residence       {{✅ | ⏳}}
Section 4 — Profession                {{✅ | ⏳}}
Section 5 — Trip details              {{✅ | ⏳}}
Section 6 — Accommodation + costs     {{✅ | ⏳}}
Section 7 — Previous Schengen visas   {{✅ | ⏳}}
Section 8 — Family information        {{✅ | ⏳ | n/a}}
Section 9 — Submit + save receipt     {{✅ | ⏳}}

═════════════════════════════════════════════════════════════════════
APPLICATION OUTPUT (after Section 9)
═════════════════════════════════════════════════════════════════════

France-Visas reference: {{FRANCE_VISAS_REFERENCE}}
Submission date:        {{SUBMISSION_DATE}}
Confirmation email:     {{RECEIVED_YES_NO_OR_PENDING}}

═════════════════════════════════════════════════════════════════════
NEXT STEPS
═════════════════════════════════════════════════════════════════════

1. Compare France-Visas' personalised checklist against your
   /document-checklist output. France-Visas' list is authoritative
   for your specific case.

2. Run /tlscontact-form to use the reference for booking your
   appointment.

3. While waiting for TLScontact slot, run /audit-application to
   verify all documents are consistent with the form you just
   submitted.
```

## Common pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Name doesn't exactly match passport | Auto-rejection trigger | Copy character-for-character from passport, including accents |
| Wrong "first entry" country (flying via Amsterdam to Paris) | Officer questions | First entry = Netherlands; France is destination |
| Applied for single-entry when need multiple | Can't leave Schengen during trip | Request multiple (same fee) |
| Submitted reference number lost | Can't proceed to TLS | Screenshot + save PDF receipt in 2 places |
| Forgot to read personalised docs list | Miss centre-specific requirements | Read it; compare to /document-checklist |
| Submitted application before having documents ready | Application has 6-month validity window — but TLS appointment matters | Application + appointment + documents must align |
| Date format inconsistency with other docs | Audit fails | YYYY-MM-DD throughout |

## Routing rules

| Situation | Suggest next |
|---|---|
| User completes Section 9 | `/tlscontact-form` to use the reference for booking |
| User stuck mid-section | Walk through the specific section field-by-field |
| User realised they entered wrong info | If pre-submission: edit. If post-submission: contact France-Visas support; some fields can be amended within the application |
| Visa-wizard opens wrong form (long-stay vs short-stay) | Re-run the wizard with corrected inputs |
| User has no scope summary from /start-here | Run /start-here first; it's the prerequisite |

## Authoritative sources

- https://france-visas.gouv.fr/en/demande-de-visa — official portal — verified 2026-05-24
- https://france-visas.gouv.fr/en/web/france-visas/visa-wizard — visa-type wizard — verified 2026-05-24
- VIS (Schengen Visa Information System) — https://eulisa.europa.eu — verified 2026-05-24

## Notes for maintainers

- The portal sometimes auto-translates poorly when the user's browser is set to a non-EN language. Recommend setting the browser to English for the form completion.
- France-Visas occasionally adds new fields (e.g. COVID-related during 2020-22). Re-verify the 10-section structure quarterly.
- Some applicants try to "test" the form by entering placeholder data, then can't undo. Warn: once submitted, can't easily edit. Treat the submission as the lock-in moment.
- The personalised supporting-documents list (downloadable after submission) is the authoritative document checklist for that specific application. It supersedes our generic /document-checklist for that user.
- Reference number format: `FRA-XXXXXXXX-XX`. Country prefix varies for non-French Schengen consulates (e.g. ITA- for Italy).
