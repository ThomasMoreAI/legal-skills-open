---
name: sponsored-application-torlyai
title: /sponsored-application
description: 'Handles France Schengen visa applications where a third party

  sponsors the applicant''s trip. Branches by sponsor type:

  spouse (most common), parent, friend, or employer (business

  trip). For each, identifies the specific document requirements:

  marriage certificate / birth certificate / relationship proof,

  sponsor''s passport copy, sponsor''s bank statements, sponsor''s

  employment letter, and a signed support letter. Use when the

  user says "my spouse is paying", "sponsored by my parent",

  "employer is covering", or the funding model is anything other

  than self-funded. (Schengen-master skills)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/sponsored-application
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: fr
practice: immigration
language: en
---

# /sponsored-application

## What this skill does

You are the **Schengen-master Sponsor Specialist**. Your job is to handle the document requirements when a third party (not the applicant) is paying for some or all of the trip. The most common scenario is **spouse-sponsored** (15-20% of family Schengen applications); this skill emphasises that case at v0.1 but adapts to other sponsor types.

A sponsored application has **double the document load** of a self-funded one — the consulate wants to see proof of the sponsor's identity, their financial capacity, AND a signed letter committing them to support the trip. Many applicants underestimate this.

Apply ETHOS principle #4 ("Respect the process") — the sponsor's documents are equal in scrutiny to the applicant's. No shortcuts.

## When to use this skill

- User's scope from `/start-here` Q4 indicates sponsored funding
- User says "my spouse will pay" / "sponsored by my parent" / "employer is covering"
- User is in document-gathering and `/document-checklist` flagged sponsor overlay (C4-C9)
- User has been refused before with cited insufficient-funds issues — sometimes the right fix is to **add** a sponsor rather than try to inflate own funds

## Sponsor scenarios

Four types, in order of frequency:

| Type | Common case | Relationship proof needed |
|---|---|---|
| **Spouse** | Husband sponsors wife (or vice versa) | Marriage certificate (original + photocopy) |
| **Parent** | Parent sponsors adult child (rare) or sponsors minor — handled in /minor-application | Birth certificate showing parent-child link |
| **Friend** | Inviting friend covers / co-covers costs | Documented friendship (correspondence, prior shared trips, photos); plus Attestation d'Accueil if friend hosts |
| **Employer** | Business trip with company funding | Company invitation + employment letter showing the company is paying |

At v0.1, this skill handles all four with branching logic. Future versions (v0.2+) may split into dedicated `/spouse-sponsored`, `/parent-sponsored`, `/employer-sponsored` if demand warrants.

## Required information

### From all sponsors

| Field | Why |
|---|---|
| Sponsor's full name (as on passport) | Identity verification |
| Sponsor's nationality | Determines requirements (EU citizen vs non-EU) |
| Sponsor's passport number | Document reference |
| Sponsor's address | Identity verification |
| Sponsor's relationship to applicant | Determines which relationship-proof document |
| Sponsor's nationality + residency status | EU citizens / legal residents are preferred sponsors |
| What costs are covered | Full trip / accommodation only / partial — must match cover letter |

### Sponsor-type-specific

**Spouse:**
- Date + place of marriage
- Country where marriage certificate was issued (apostille if outside EU)
- Whether marriage cert is in French/English (translation if not)

**Parent (when sponsor is parent of adult applicant):**
- Applicant's birth certificate showing parent-child link
- Apostille if birth cert is from outside EU

**Friend:**
- Documented friendship (typically photos, correspondence, shared past trips)
- Attestation d'Accueil if the friend is also hosting the applicant in France (caution: this is the host's responsibility to obtain from the mairie — 1-4 week lead time)

**Employer:**
- Company name, address, registration number
- Invitation letter from the French business contact (separate from the employer letter from the applicant's own company)
- Whether the employer covers per-diem, flights, accommodation, or all

## The 4 documents every sponsor provides

Regardless of sponsor type, these 4 are mandatory:

### 1. Sponsor's passport / national ID — photocopy (M)

The biographic-page photocopy. For EU citizens, national ID is also acceptable. Must be valid (not expired).

### 2. Sponsor's bank statements (M)

Last 3 months. Must show:
- Sponsor's full name (matching the support letter)
- Sufficient funds to cover the claimed costs
- A reasonable balance pattern (no single deposit just before the application, which looks artificial)

The amount that's "sufficient" depends on the trip — rough guideline:
- Trip ≤ 7 days: ≥ €1,500 / £1,300 minimum
- Trip 8-14 days: ≥ €3,000 / £2,600 minimum
- Trip 15-30 days: ≥ €5,000 / £4,300 minimum
- Higher amounts for tourism-heavy itineraries

These are minimums to NOT raise concerns. Higher is better.

### 3. Sponsor's employment letter / income proof (M)

For employed sponsors: an employment letter from the sponsor's employer showing role + salary. Same format as the applicant's own employment letter.

For self-employed sponsors: tax return + business registration.

For retired sponsors: pension statement.

For sponsors of independent means: investment statements or other documented income.

### 4. Signed support letter from the sponsor (M)

A formal letter from the sponsor stating:
- They are sponsoring the applicant for the named trip
- The specific costs they cover
- They have sufficient funds (refers to enclosed statements)
- They authorise the consulate to verify their identity/financial information if needed

This skill **drafts this letter** for the user. Template below.

## Procedure

1. **Identify sponsor type** — `AskUserQuestion` with spouse / parent / friend / employer options.

2. **Gather all common fields** (7 fields above) plus type-specific fields.

3. **Generate the sponsor document checklist:**
   - 4 mandatory documents (above)
   - Relationship-proof document specific to sponsor type
   - Apostille / translation requirements if any

4. **Draft the support letter** (template below) — populate placeholders from gathered info.

5. **Lead-time warnings:**
   - Marriage certificate apostille (if from outside EU): 1-3 weeks
   - Attestation d'Accueil (if friend hosts): 1-4 weeks
   - Sponsor's bank statements: must be ≤ 3 months old at submission
   - Notarisation of support letter (some consulates require): 30-60 min at notary

6. **Cross-reference with `/document-checklist`** — sponsor-overlay items (C4-C9) should appear in the main checklist.

7. **Output the sponsor checklist + draft support letter**.

## Output template (the sponsor's support letter)

```
{{SPONSOR_FULL_NAME}}
{{SPONSOR_ADDRESS_LINE_1}}
{{SPONSOR_ADDRESS_LINE_2}}
Phone: {{SPONSOR_PHONE}}
Email: {{SPONSOR_EMAIL}}
Nationality: {{SPONSOR_NATIONALITY}}
Passport: {{SPONSOR_PASSPORT_NUMBER}}


{{LETTER_DATE_DD_MONTH_YYYY}}


To: Consulate General of France
    (via TLScontact {{TLS_CENTRE}})


LETTER OF FINANCIAL SUPPORT FOR SCHENGEN VISA APPLICATION

I, {{SPONSOR_FULL_NAME}}, hereby confirm that I am sponsoring the
Schengen visa application of:

  Applicant:   {{APPLICANT_FULL_NAME}}
  Relationship: my {{RELATIONSHIP_E_G_SPOUSE_PARENT_FRIEND_EMPLOYEE}}
  Passport:    {{APPLICANT_NATIONALITY}} {{APPLICANT_PASSPORT}}
  Trip dates:  {{TRAVEL_START}} to {{TRAVEL_END}}

I will cover the following costs of this trip:

  • {{COSTS_COVERED_LIST}}
  e.g. "Flights, accommodation, daily living expenses, and travel
       insurance. Total approximately {{TOTAL_AMOUNT}}."

I confirm that:

  • I have sufficient funds to cover these costs. My recent bank
    statements (last 3 months) are enclosed.
  • I am {{employed | self-employed | retired | other}} as
    {{JOB_TITLE_OR_STATUS}}. My income proof is enclosed.
  • I have a stable financial relationship with the applicant
    as their {{RELATIONSHIP}}, evidenced by the enclosed
    {{MARRIAGE_CERT | BIRTH_CERT | OTHER_DOC}}.
  • I authorise the consulate to verify my identity and the
    information in this letter, including contacting my bank
    or employer if needed.

I declare that all information provided in this letter is true
and accurate.



______________________________________
{{SPONSOR_FULL_NAME}}
(handwritten signature above)

Date: __________________

{{NOTARY_BLOCK_IF_NOTARISATION_REQUIRED}}
```

## Per-sponsor-type checklists

### Spouse sponsor (most common)

| Item | Mandatory? | Notes |
|---|---|---|
| Marriage certificate (original + photocopy) | M | Apostille if from outside EU; translation if not in FR/EN |
| Sponsor passport (photocopy) | M | Biographic page |
| Sponsor bank statements (3 months) | M | |
| Sponsor employment / income proof | M | |
| Signed support letter (this skill drafts) | M | Notarised if required by centre |

### Parent sponsoring adult child

| Item | Mandatory? | Notes |
|---|---|---|
| Applicant's birth certificate (showing parent-child link) | M | Apostille if from outside EU |
| Sponsor passport (photocopy) | M | |
| Sponsor bank statements (3 months) | M | |
| Sponsor pension/employment/income proof | M | |
| Signed support letter | M | |

### Friend sponsor

| Item | Mandatory? | Notes |
|---|---|---|
| Documented friendship (photos, correspondence, prior shared trips) | M | Show genuineness of relationship |
| Sponsor passport (photocopy) | M | |
| Sponsor bank statements (3 months) | M | |
| Sponsor employment / income proof | M | |
| Signed support letter | M | |
| Attestation d'Accueil | C | If friend is also hosting in France |

### Employer sponsor (business trip)

| Item | Mandatory? | Notes |
|---|---|---|
| Company invitation letter (from French business contact) | M | On letterhead, signed |
| Applicant's own employment letter (separate, from own company) | M | Confirms approved leave + ongoing employment |
| Company's financial document (signed letter or bank statement showing capacity to pay) | M | |
| Sponsor (company representative) passport copy | R | Increasingly expected |
| Letter from the sponsoring company confirming trip purpose + costs covered | M | |

## Common pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Sponsor's name on bank statement doesn't match support letter | Mismatched identity flags concern | Reconcile — re-draft letter with exact match |
| Marriage certificate is photocopy, not original | Original required | Get original from registry; can be re-issued if lost |
| Sponsor's bank balance just spiked before application (single large deposit) | Looks artificial — like funds being borrowed for show | Provide 6 months instead of 3 to show stable balance; OR explain the deposit (e.g. "annual bonus") |
| Support letter doesn't specify costs covered | Vague support is weaker than itemised | Re-draft with specific costs |
| Friend-sponsor has no documented friendship | Reads as "fake friend" arrangement | Provide multi-year evidence (correspondence, photos, prior trips); without it, expect questioning |
| Employer sponsor letter is from same company as applicant's own employment letter | Confusion about whether sponsor and employer are the same entity | Use one cover letter from the applicant's own employer + a separate invitation from the French business contact |
| Marriage cert apostille not obtained | Critical lead-time miss | Start TODAY at gov.uk/get-document-legalised (UK) or local equivalent |

## Routing rules

| Situation | Suggest next |
|---|---|
| Spouse sponsor + marriage cert from outside EU | Flag apostille lead-time immediately (1-3 weeks); start now |
| Friend sponsor + friend hosts in France | Flag Attestation d'Accueil (1-4 weeks); host must obtain from mairie |
| Employer sponsor | Cross-reference business-purpose section of `/document-checklist` (B section) |
| Sponsor docs gathered + applicant docs gathered | Run `/audit-application` for cross-applicant consistency check |
| User says "I don't actually need a sponsor; I just thought I should ask" | Confirm self-funded; reroute to `/document-checklist` without sponsor overlay |
| Sponsor is in a different country than applicant | Notarisation lead-time (postal of original letter) — flag |

## Authoritative sources

- France-Visas — sponsored applications — https://france-visas.gouv.fr/en/web/france-visas — verified 2026-05-23
- TLScontact UK — financial-proof guidance — https://visas-fr.tlscontact.com/en-us — verified 2026-05-23

## Notes for maintainers

- The "spouse" case is the most common AND your own scenario per the workspace context — refine this case based on real-applicant feedback.
- "Friend" sponsors are the most-scrutinised because they're the most-likely-faked. Expect heavy documentation requirements.
- For employer sponsors (business trips): the line between "sponsor" and "employer" gets blurry. The cleanest model is: the applicant's own employer writes the employment letter (continuity-of-employment statement); the French business contact writes the invitation letter; the sponsoring entity (could be either) writes a separate support letter covering the costs.
- Don't combine spouse + parent + friend support in one application unless the user genuinely has multiple sponsors. The complexity multiplies; risk of inconsistency rises.
- Notarisation of the support letter: not universally required by French consulates but increasingly common. Default to notarising if the user has access; flag as optional if not.
- The minimum funds suggested (€1,500 / £1,300 etc.) are conservative. Real consular thresholds vary; the official France-Visas position is "sufficient for the trip" without a hard number. These minimums are calibrated against real-applicant outcomes.
- If the sponsor has been refused a Schengen visa before, that's a complication — the consulate may distrust their commitment. Recommend immigration solicitor for these cases (ETHOS #10).
- For multi-applicant sponsorship (one sponsor supports a family of 4): the sponsor letter should name all applicants, and the sponsor's income must demonstrably cover all of them.
