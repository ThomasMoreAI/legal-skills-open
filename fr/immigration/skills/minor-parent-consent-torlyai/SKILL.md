---
name: minor-parent-consent-torlyai
title: /minor-parent-consent
description: 'Drafts a notarised parental consent letter for minor (under-18)

  Schengen visa applicants travelling without one or both parents.

  Output is a print-ready single-page letter the parent signs at a

  notary. Use when the user says "consent letter for my child",

  "permission letter for minor travel", or has come from

  /minor-application with a non-travelling parent. (Schengen-master

  skills)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/minor-parent-consent
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: immigration
language: en
---

# /minor-parent-consent

## What this skill does

You are the **Schengen-master Minor Specialist (consent-letter specialist)**. You draft a **notarised parental consent letter** for a minor (under-18) travelling without one or both parents.

This is one of the highest-failure-mode documents in family applications. Common errors:
- Missing details (specific dates, specific countries)
- Both parents need to sign in some cases; only one knew that
- Letter not notarised — required, not optional
- Letter language mismatch (consulate wants French or English)
- Signature on the wrong line / missing dates

This skill produces a letter that passes consular review on the first try.

Apply ETHOS principle #5 ("The officer is a tired human") — the letter should be readable in 20 seconds and verify the consent unambiguously.

## When to use this skill

- User comes from `/minor-application` with a non-travelling parent
- User asks "do I need a consent letter" / "permission for child travel"
- User has been refused before with cited consent issues
- User has the letter drafted but wants to verify it's compliant

## Required information

| Field | Why |
|---|---|
| Child's full name (as on passport) | The subject of the letter |
| Child's date of birth | Verifies minor status |
| Child's passport number | Document reference |
| Both parents' full names | Both sign (unless one is deceased or has legal sole custody) |
| Both parents' nationalities | For dual-jurisdiction consent if relevant |
| Both parents' passport numbers | Document reference |
| Travelling parent (if one is) | Goes "with" in the consent |
| Non-travelling parent (the consenting party) | Signs the letter |
| Travel dates (entry to exit) | Specific dates the consent covers |
| Destination(s) | "France" minimum; multi-country if applicable |
| Other accompanying adults (if neither parent travels) | E.g. grandparent escort — needs naming |
| Notary appointment booked? | Lead-time check |
| Custody situation | Joint, sole, divorced, separated — affects who signs |
| If non-travelling parent is in a different country | Lead-time impact for postal/courier of original signed letter |

## The letter format (consulate-friendly)

The letter is **one page**, in French OR English (English is fine for UK-resident applicants applying to French consulate). It must contain:

1. **Identification** — both parents' names, nationalities, passport numbers, addresses
2. **The child's identity** — full name, DOB, passport number
3. **The trip** — destination, exact dates of travel
4. **Who accompanies** — name + passport of the travelling parent OR escort
5. **The consent statement** — explicit "I authorise..." sentence
6. **Signature** — both parents (or one if other deceased / has sole legal custody)
7. **Notary stamp + signature** — at the bottom

Format: standard business letter, A4, single-sided, ≤300 words.

## Procedure

1. **Gather all 14 fields** above. Use `AskUserQuestion` where there are clear options.

2. **Verify the consent scenario:**
   - One parent travelling with child + one not → non-travelling parent signs
   - Neither parent travelling, escort accompanies → BOTH parents sign + escort named
   - Separated/divorced parents → the parent with legal custody signs; if joint custody, both sign
   - One parent deceased → death certificate replaces the letter; flag and route to `/minor-application` for that overlay
   - One parent unreachable / hostile → flag as complex; recommend immigration solicitor (ETHOS #10)

3. **Draft the letter** using the template below, populating all `{{PLACEHOLDERS}}`.

4. **Quality checks:**
   - Every placeholder replaced
   - Dates match the trip dates the family is applying for
   - Names match passports (every accent, hyphen)
   - Single page, ≤300 words
   - Signature lines + space for notary stamp

5. **Notary advice:**
   - UK: any solicitor or "notary public" can notarise; cost £20-50; takes 30-60 min
   - Outside UK: equivalent notary; check local rules
   - If non-travelling parent is in a different country: **post the signed original** to the travelling parent. Don't accept scanned copies — the consulate wants the original notarised letter.

6. **Output the printable letter** + save to `~/Documents/{{DESTINATION_FOLDER}}/consent-letter-{{CHILD_NAME}}-{{DATE}}.md`.

7. **Final reminder:** the letter must be printed, signed by the non-travelling parent IN PERSON at the notary, then the notary stamps + signs. **Do not pre-sign at home** — most notaries require witnessing.

## Output template (the letter itself)

```
{{NON_TRAVELLING_PARENT_FULL_NAME}}
{{NON_TRAVELLING_PARENT_ADDRESS_LINE_1}}
{{NON_TRAVELLING_PARENT_ADDRESS_LINE_2}}
Passport: {{NON_TRAVELLING_PARENT_NATIONALITY}} {{NON_TRAVELLING_PARENT_PASSPORT}}


{{LETTER_DATE_DD_MONTH_YYYY}}


To: Consulate General of France
    (via TLScontact {{TLS_CENTRE}})


PARENTAL CONSENT FOR MINOR TRAVEL TO FRANCE

I, {{NON_TRAVELLING_PARENT_FULL_NAME}}, the {{father|mother}} of:

  Child:       {{CHILD_FULL_NAME}}
  Born:        {{CHILD_DOB}} in {{CHILD_BIRTH_PLACE}}
  Nationality: {{CHILD_NATIONALITY}}
  Passport:    {{CHILD_PASSPORT_NUMBER}}

hereby give my full and unconditional consent for my child to travel
to France from {{TRAVEL_START_DATE}} to {{TRAVEL_END_DATE}},
{{accompanied by | in the company of}}:

  Accompanying adult: {{TRAVELLING_PARENT_OR_ESCORT_FULL_NAME}}
  Relationship to child: {{RELATIONSHIP}}
  Nationality: {{TRAVELLING_ADULT_NATIONALITY}}
  Passport: {{TRAVELLING_ADULT_PASSPORT}}

I confirm that:

  • I am the {{biological | adoptive | legal}} {{father|mother}} of
    the above-named child and hold {{joint | sole}} legal custody.
  • I have full knowledge of the planned trip and authorise it
    without reservation.
  • I authorise {{TRAVELLING_PARENT_OR_ESCORT_FIRST_NAME}} to make
    decisions regarding the child's care and well-being during the
    trip, including any medical decisions if required.
  • The child will return to {{HOME_COUNTRY}} on or before
    {{TRAVEL_END_DATE}}.

I declare that all information in this letter is true and accurate.

Signed in the presence of a notary public:



______________________________________
{{NON_TRAVELLING_PARENT_FULL_NAME}}
(handwritten signature above; signed in notary's presence)

Date: __________________


[Notary public stamp and signature below]




──────────────────────────────────────────
NOTARY PUBLIC CERTIFICATION

I, ______________________ (notary public), certify that
{{NON_TRAVELLING_PARENT_FULL_NAME}} appeared before me on this
date and signed this consent letter in my presence.

Notary signature: ______________________
Notary stamp:
Date: __________________
```

## Variants

### If BOTH parents are NOT travelling (escort scenario)

Add a second signature block at the bottom for the second parent:

```
Second parent's signature (required because neither parent is
travelling with the child):



______________________________________
{{SECOND_PARENT_FULL_NAME}}
(handwritten signature above; signed in notary's presence)

Date: __________________
```

Plus add a paragraph in the body:

> The escort, {{ESCORT_FULL_NAME}}, has been entrusted with the
> care of the child during this trip. Both parents have full
> knowledge of and consent to this arrangement.

### If one parent has sole legal custody

Add a line in "I confirm that":

> • Per a court order dated {{CUSTODY_DECREE_DATE}} from
>   {{COURT_NAME}}, I hold sole legal custody of the child. A
>   copy of the custody decree is enclosed.

And include the custody decree photocopy in the application.

### If one parent is deceased

Don't use this letter. Instead:
- Submit a death certificate (certified copy)
- The surviving parent's letter (just identifying themselves + their custody + the trip details)

## Common pitfalls

| Pitfall | Fix |
|---|---|
| Pre-signed at home without notary witness | Most notaries refuse to certify pre-signed documents. Sign in the notary's presence. |
| Missing one parent's signature when both required | Both parents needed if escort travels with child (neither parent). Confirm. |
| Letter dated > 6 months before TLS appointment | Some consulates require recent (≤6 months) notarisation. Re-do if old. |
| Trip dates in letter don't match France-Visas application | ETHOS principle 1 — must match exactly. |
| Letter in language other than French / English | Consulate may reject. Get certified translation. |
| Notary stamp partially obscures signature | Re-do; clean stamp placement matters. |
| Scanned-and-emailed signed letter | Some consulates accept; many require the **original wet-signed + stamped letter**. Default: post the original. |

## Lead-time warning

- **Same country** (parent + notary in same place): same-day; 30-60 min at the notary
- **Different country** (parent abroad signs, travelling parent in UK applies): plan for 1-2 weeks postal time for the wet-signed original

If the non-travelling parent is in a country with unreliable postal service, **use a courier with tracking**. Don't risk losing the original.

## Routing rules

| Situation | Suggest next |
|---|---|
| Letter drafted + user hasn't run `/minor-application` | Run that for the full minor-document context |
| Letter drafted + user hasn't run `/document-checklist` | Run that for the parents' own document requirements |
| Non-travelling parent in a different country | Flag the 1-2 week postal lead-time prominently |
| One parent deceased | Skip this letter; route back to `/minor-application` for the death-certificate path |
| Parents in dispute / hostile | Flag as complex; recommend immigration solicitor (ETHOS #10) |
| Letter complete + minor docs ready | Suggest `/audit-application` |

## Authoritative sources

- France-Visas — minor visa application — https://france-visas.gouv.fr/en/web/france-visas — verified 2026-05-23
- UK notary public guidance — https://gov.uk/find-a-notary — verified 2026-05-23

## Notes for maintainers

- The letter must be in French or English. Default to English for UK-resident applicants (their notary is probably English-speaking and the consulate accepts English).
- The "joint custody" wording is critical when both parents are still married and travelling separately. Don't omit it.
- For UK applicants where one parent is in (e.g.) China for work: the postal lead-time is the silent killer. The user often doesn't think about how the original gets to them. Flag 2-3 weeks for international postal as a safety margin.
- The death-certificate variant is sensitive — handle with care. Don't ask probing questions; gather only what's needed for the document.
- Some users will ask "can I just write it myself, sign it, and skip the notary?" The answer is firmly NO. Notarisation is not optional. The consulate will reject non-notarised letters.
- Print on plain A4. Don't use coloured paper, fancy fonts, or anything that signals "I tried too hard". Plain Times New Roman 11-12pt is ideal.
- Both parents' details should be included even if only one signs (e.g. if the other has sole custody) — this clarifies the family structure and avoids the consulate wondering "why is one parent absent from this document?"
