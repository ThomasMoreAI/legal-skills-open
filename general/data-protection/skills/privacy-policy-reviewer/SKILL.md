---
name: privacy-policy-reviewer
title: 'Skill: privacy-policy-reviewer'
description: Review a privacy policy or terms of service against a structured scorecard, combining TOSDR's human-curated ratings with LLM analysis. Use when a user wants to review, analyze, or understand a privacy policy or terms of service before signing up for a service or after receiving a policy update notification.
author: amanahuja
author_url: https://github.com/amanahuja/privacy-skills/tree/main/skills/privacy-policy-reviewer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Skill: privacy-policy-reviewer

Review a privacy policy or terms of service against a structured scorecard,
combining TOSDR's human-curated data with LLM analysis. Designed for
privacy-conscious users who want a fast, honest, sourced read of what they
are actually agreeing to.

---

## When to Use This Skill

Invoke when the user:
- Provides a URL to a privacy policy or terms of service
- Asks you to review, analyze, or summarize a privacy policy
- Provides a service name and wants to know about its privacy practices
- Has received a "policy updated" email and wants to understand what it means

---

## Step-by-Step Workflow

### Step 1: Get the URL or Service Name

Ask the user:

> "Please provide the URL to the privacy policy or terms of service you want
> reviewed, or the name of the service."

If a **URL** is provided:
- Fetch the page content
- Extract the domain (e.g., `surf.social` from `https://about.surf.social/privacy-policy/`)
- Run a TOSDR search using that domain as the query (see TOSDR API below)

If a **service name** is provided:
- Run a TOSDR search using the service name as the query
- Do NOT fetch any URL yet

### Step 2: TOSDR Lookup — Always Confirm with User

Run: `GET https://api.tosdr.org/search/v5?query=<domain or service name>`

**Always present the result(s) to the user and ask for confirmation — even if
only one result is returned, even if no result is found.**

Format the confirmation as:

If one or more results found:
> "I found the following in the TOSDR database. Please confirm which one
> matches the service you want to review, or let me know if none of these
> are correct:
>
> 1. **[Name]** — Rating: [X] — [URL] — tosdr.org/en/service/[id]
> 2. **[Name]** — Rating: [X] — [URL] — tosdr.org/en/service/[id]
> 3. None of these / proceed without TOSDR data"

If no results found:
> "This service is not currently in the TOSDR database. I'll proceed with
> LLM analysis only. If you have a policy URL, please provide it now."

If the user confirms a TOSDR match:
- Fetch full service data: `GET https://api.tosdr.org/service/v3?id=<id>`
- Note: `rating`, `is_comprehensively_reviewed`, `points` array, `documents` array

**Policy source resolution — follow this order strictly, do not skip steps:**

1. The `documents` array in the TOSDR service response contains the exact
   URLs TOSDR used to analyze this service. Extract these URLs first.
   These are the authoritative policy sources for this service.

2. If the user provided a URL in Step 1, add it to the document list if
   it is not already present.

3. For scorecard rows covered by TOSDR approved points: use the TOSDR data
   directly. Do NOT fetch any URL for these rows.

4. For scorecard rows NOT covered by TOSDR points (i.e., gaps): fetch the
   documents[] URLs to find relevant policy language for LLM analysis.

5. If `documents` is empty AND the user provided no URL: ask the user to
   provide the policy URL directly. Do not attempt to guess URLs, do not
   search for alternate paths, do not try common patterns like /privacy
   or /en/privacy.

6. If `is_comprehensively_reviewed` is true: expect most or all rows to
   be covered by TOSDR points. Limit fetching to only what is needed for
   uncovered rows. Do not re-analyze rows that TOSDR has already covered.

### Step 3: Select Review Tier

Ask the user:

> "What level of review do you need?
>
> **Standard** — You're deciding whether to sign up for an everyday service
> (social app, newsletter, SaaS tool). Covers the most important red flags.
>
> **Enhanced** — The service handles real identity, financial information,
> location data, or workplace data. Deeper analysis of what's collected and
> who sees it.
>
> **High Sensitivity** — You're evaluating a service in the context of health,
> reproductive choices, mental health, immigration status, or legal exposure.
> Full analysis including law enforcement access, sensitive data categories,
> and consent withdrawal rights."

Note the selected tier — it governs which cases are checked in the scorecard
and the tone of the narrative.

### Step 4: Jurisdiction

Ask the user:

> "What jurisdiction should I apply when assessing your privacy rights?
>
> - United States (no specific state) [default]
> - A specific US state (e.g., California, Virginia)
> - European Union / GDPR
> - Other country
>
> This affects which rights you have and how the policy's legal language
> applies to you."

Note the jurisdiction for use in the narrative and Key Flags sections.

---

## TOSDR API Reference

**Base URL:** `https://api.tosdr.org`

### Search
```
GET /search/v5?query=<string>
```
Returns: array of services with `id`, `name`, `rating`, `urls`,
`is_comprehensively_reviewed`, `slug`

### Full Service Data
```
GET /service/v3?id=<id>
```
Returns: `name`, `rating`, `is_comprehensively_reviewed`, `urls`, `documents`,
`points` array

Each point in `points` contains:
- `title` — short human-readable description
- `status` — only use points where `status == "approved"`
- `analysis` — longer explanation
- `case.title` — the case being addressed
- `case.classification` — `blocker`, `bad`, `neutral`, or `good`
- `case.weight` — importance weight (higher = more significant)
- `case.topic_id` — which topic this belongs to (see scorecard below)
- `case.description` — TOSDR's definition of this case

**Only use approved points** (`status == "approved"`). Discard pending,
declined, or disputed points.

---

## Scorecard: 12 Rows

The scorecard always has these 12 rows, in this order. Every row must appear
in the output. If a row cannot be assessed (no relevant policy language found,
no TOSDR points), mark it `[YELLOW]` or `[BAD/NEUTRAL]` and note
"Not addressed in this policy."

### TOSDR Topic ID Reference

| Topic ID | Topic Name                   |
|----------|------------------------------|
| 25       | Trackers                     |
| 26       | Anonymity                    |
| 27       | Ownership                    |
| 28       | Law and Government Requests  |
| 30       | Copyright License            |
| 34       | User Choice                  |
| 39       | Business Transfers           |
| 40       | Logs                         |
| 41       | Personal Data                |
| 42       | Dispute Resolution           |
| 44       | Jurisdiction & Governing Law |
| 45       | Right to Leave the Service   |
| 46       | Notice of Changing Terms     |
| 47       | Suspension and Censorship    |
| 48       | Third Parties                |
| 50       | Security                     |
| 56       | Types of Information Collected|
| 57       | Advertising                  |

### Row Definitions and Tier Scope

**Row 1: Cookies & Tracking** (Topics 25)

Standard: Are third-party advertising cookies used? Is cross-site tracking
present?

Enhanced: + fingerprinting, tracking pixels, social media pixels, DNT
response

High Sensitivity: + full scope of tracking technologies; whether tracking
could expose sensitive behavioral patterns

Key cases to surface:
- Third-party cookies for advertising (bad, w=70)
- Cross-site tracking (bad, w=60)
- Fingerprinting / device fingerprinting (bad, w=50)
- Social media pixels (bad)
- You are not being tracked (good, w=100)
- Cookie list provided (good)

---

**Row 2: Data Collection** (Topics 41, 56)

Standard: What broad categories of data are collected? Is collection
excessive?

Enhanced: + precise location, biometric data, device identifiers, inferred
preferences

High Sensitivity: + sensitive categories (health, reproductive, financial,
political), AI training use, automated profiling

Key cases to surface:
- Many different types of personal data collected (bad, w=50)
- Biometric data collected (bad, w=50)
- Precise GPS location collected (bad, w=50)
- Location data collected/shared (bad)
- App requires broad device permissions (bad)
- Personal data used for automated decision-making/profiling/AI training
  (blocker)
- Data collected even without direct interaction (blocker)
- IP address collected (neutral)

---

**Row 3: Data Sharing** (Topics 48)

Standard: Is data shared with non-essential third parties? With advertisers?

Enhanced: + is data acquired from third parties (data brokers feeding data
in)? How many third parties are involved?

High Sensitivity: + can third parties re-share your data? Are subprocessors
listed?

Key cases to surface:
- Data shared with non-essential third parties (bad, w=50)
- Data given to third parties essential to operation (bad, w=50)
- Data gathered from third parties about you (bad, w=50)
- Many third parties involved (bad)
- Data not shared with third parties (good)
- Third-party list provided (good)

---

**Row 4: Advertising** (Topic 57)

Standard: Is personal data used for ads? Can you opt out?

Enhanced: + is data shared with third-party ad networks? Is your identity
used in ads shown to others?

High Sensitivity: + could ad targeting reveal sensitive category data to
advertisers?

Key cases to surface:
- Personal data used for advertising (bad, w=50)
- Targeted third-party advertising (bad, w=40)
- Identity used in ads shown to others (blocker, w=50)
- Personal data used for marketing (bad)
- Opt out of targeted advertising available (good, w=25)

---

**Row 5: Your Rights** (Topics 34, 45)

Standard: Can you delete your account? Can you opt out of communications?

Enhanced: + can you access, correct, export your data? Is there a Privacy
Manager or equivalent?

High Sensitivity: + can you withdraw consent? What happens to data after
account deletion? Are GDPR/CCPA rights honored? Is there a DPA contact?

Key cases to surface:
- Right to access, correction, deletion (good, w=50)
- Data archive/export available (good, w=40)
- Opt out of promotional communications (good, w=10)
- Right to leave the service (good)
- You can delete your content (good, w=50)

---

**Row 6: Content Ownership** (Topics 27, 30)

Standard: Do you retain ownership of what you post? Does the service claim
a broad license over your content?

Enhanced: + does the license survive account deletion? Can content be
sublicensed to third parties?

High Sensitivity: + could licensed content expose sensitive information about
you after you leave?

Key cases to surface:
- You maintain ownership of your content (good)
- License kept even after account closed (bad, w=50)
- Content can be licensed to third parties (bad, w=50)
- Copyright license limited to service purposes (good)
- You waive moral rights (blocker, w=50)

---

**Row 7: Data Retention** (Topics 40, 41)

Standard: Are specific retention timeframes given, or is it vague ("as long
as necessary")?

Enhanced: + is deleted content actually deleted? Are logs purged on a
schedule?

High Sensitivity: + is there a minimum retention standard? Can anonymized
data be re-identified? What happens to data if you withdraw consent?

Key cases to surface:
- Logs deleted after finite period (good)
- Data retention minimum necessary (good)
- Content not really deleted after deletion (blocker, w=50)
- Vague retention language — flag explicitly if no timeframes given

---

**Row 8: Terms Changes** (Topic 46)

Standard: Will you be notified of material changes? Can changes take effect
without notice?

Enhanced: + is consent assumed from continued use? Is a 30-day notice
committed?

High Sensitivity: + can terms change in ways that affect sensitive data
processing without meaningful opportunity to object?

Key cases to surface:
- Terms may change at discretion without notice (bad)
- Notified of material changes with 30-day advance notice (good)
- Consent assumed from usage (bad)
- Should revisit terms periodically (neutral)

---

**Row 9: Account Suspension** (Topic 47)

Standard: Can your account be suspended or content deleted without notice or
reason?

Enhanced: same, with attention to appeal rights

High Sensitivity: + could suspension expose or strand sensitive data?

Key cases to surface:
- Account deleted/suspended without notice or reason (bad, w=60)
- Content deleted without reason or notice (blocker, w=50)
- Banned users cannot re-register (neutral)

---

**Row 10: Arbitration & Disputes** (Topic 42)

Standard: Are you forced into binding arbitration? Is class action waived?

Enhanced: + which jurisdiction governs? Is the venue favorable to the
service?

High Sensitivity: + in a sensitive context (e.g. health data breach), forced
arbitration removes your ability to join a class action — flag this
prominently

Key cases to surface:
- Forced into binding arbitration (bad)
- Class action waiver (bad, w=50)
- Not forced into binding arbitration (good)
- Governing court jurisdiction (neutral, w=0 — but note the location)

---

**Row 11: Acquisition & Shutdown** (Topic 39)

Standard: Can your data be transferred in a merger, acquisition, or
bankruptcy?

Enhanced: + do you have any opt-out rights if a transfer occurs?

High Sensitivity: + in a sensitive context, a data transfer to an unknown
acquirer could be dangerous — flag if no user rights are stated on transfer

Key cases to surface:
- Data transferred in bankruptcy/acquisition (bad, w=50)
- No user opt-out on data transfer — flag as gap if absent

---

**Row 12: Government Requests** (Topic 28)

Standard: Will they notify you if law enforcement requests your data?

Enhanced: + what legal standard triggers disclosure (warrant vs. legal
process vs. "appropriate")?

High Sensitivity: + in sensitive contexts (reproductive health, immigration),
government data requests carry direct legal risk to the user. Flag the
absence of a warrant requirement or user notification as a significant
concern. Note jurisdiction of the service (US services are subject to US law
enforcement).

Key cases to surface:
- Data disclosed to government without user notice (bad, w=50)
- Third parties require legal basis to access data (good)
- No warrant canary or transparency report — flag as gap at High Sensitivity

---

## Source Labeling Rules

Every scorecard row must be labeled with its source. Use these labels
consistently:

**When data comes from TOSDR approved points:**
```
  ⓣ TOSDR-verified   [BLOCKER] / [BAD] / [NEUTRAL] / [GOOD]
```
Use TOSDR's exact classification terminology: BLOCKER, BAD, NEUTRAL, GOOD.
Include the case title and point ID where useful.

**When data comes from LLM analysis of the policy text:**
```
  ⚙ LLM-generated    [RED] / [YELLOW] / [GREEN]
```
Use Red/Yellow/Green. Always include a direct quote from the policy text.

**When a row is hybrid (some TOSDR points, some LLM gaps):**
```
  ⓣ/⚙ Hybrid        [BAD] / [YELLOW]
```
Label each sub-finding individually within the row.

**In the output header, always state the overall method:**
```
ANALYSIS METHOD: TOSDR-verified (partial, 8/12 rows) + LLM-generated (4/12 rows)
              or TOSDR-verified (comprehensive)
              or LLM-generated only (not in TOSDR)
```

---

## Output Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SERVICE:         [Name]
POLICY URL:      [URL]
LAST UPDATED:    [Date from policy, or "Not stated"]
TOSDR:           [Not found | Found — Grade X, N points, [not] comprehensive]
TIER:            [Standard | Enhanced | High Sensitivity]
JURISDICTION:    [As specified by user]
ANALYSIS METHOD: [See labeling rules above]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

── TOSDR RECORD ──────────────────────────────────
[If found:]
Grade: [X]  |  Points: [N] approved  |  Comprehensive: [Yes/No]
Link: https://tosdr.org/en/service/[id]

[If not found:]
Not in TOSDR database.
Consider submitting: https://edit.tosdr.org/new_service

── SCORECARD ─────────────────────────────────────

[For each row:]
[Row Name]        [⚙/ⓣ/ⓣ/⚙] [CLASSIFICATION]
                  One precise sentence. Direct quote or "Not addressed
                  in this policy." For TOSDR rows, cite the case title.

[All 12 rows always present, in order]

── NARRATIVE ─────────────────────────────────────
[3-5 sentences. Calibrated to the selected tier and jurisdiction.
Structure:
  - Overall pattern: is this service better/worse/average for its type?
  - Structural risks: what you cannot mitigate regardless of settings
  - Easy wins: specific actionable steps available right now
  - Ongoing vigilance: what to watch for going forward
  - Jurisdiction angle: what the specified jurisdiction adds or changes

Tone: direct, precise, non-alarmist. Assume a privacy-conscious reader
who does not need basic concepts explained. Treat omissions as signals.
Do not soften findings. Do not pad with reassurances.

At High Sensitivity tier: lead with the specific risk context (e.g.,
reproductive health, immigration) and make explicit how the policy's
gaps or weaknesses interact with that threat model.]

── KEY FLAGS ─────────────────────────────────────
⛔ RED / BLOCKER items — each with a direct quote from the policy:

  [Row name] — [one sentence explaining the risk]
    "[direct quote from policy text]"

✓ NOTABLE POSITIVES — only if genuinely above average:
  · [specific positive finding]

── LINKS ─────────────────────────────────────────
TOSDR:              [Link or "Not found — submit: edit.tosdr.org/new_service"]
Open Terms Archive: [Link if found, or "Not tracked"]
Policy source:      [URL]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Narrative Tone by Tier

**Standard**
Calibrate to: "Is this service worth signing up for?"
Acceptable risk framing — some Yellows are normal. Focus on what's
genuinely unusual. Don't over-alarm about boilerplate.

**Enhanced**
Calibrate to: "What does this service actually know about me and who
sees it?"
Be specific about data flows. Name the third parties if listed. Note
whether the policy gives you real control or just the appearance of it.

**High Sensitivity**
Calibrate to: "Could this data be used against me?"
Do not soften. A vague retention policy at this tier is not "something
to watch" — it is a concrete risk. Government request language must be
read in light of the user's stated context. If the service is US-based
and the user's context involves reproductive health or immigration,
explicitly note that US law enforcement can compel disclosure without
a warrant in many circumstances, and that the policy's language does
or does not provide any protection against this.

---

## Jurisdiction Guidance

**United States (no state)**
- Note which state's law governs (from the policy's jurisdiction clause)
- Flag binding arbitration and class action waivers — these limit federal
  court access
- Note if the service honors Global Privacy Control
- At High Sensitivity: flag that the US has no federal comprehensive
  privacy law; user's rights depend heavily on the service's own policy
  commitments

**US State specified**
- California (CCPA/CPRA): user has opt-out of sale/sharing rights, right
  to know, right to delete, right to correct, non-discrimination right.
  Check whether the policy's California section matches these.
- Virginia (CDPA), Colorado (CPA), Connecticut (CTDPA), Texas (TDPSA),
  and others: check if policy acknowledges applicable state law.
- Most other US states: note that comprehensive state privacy law may not
  yet apply; user's rights are limited to what the policy voluntarily offers.
- Wisconsin: no comprehensive state privacy law as of 2026. User's rights
  are limited to what the policy voluntarily offers and any applicable
  sector-specific law (HIPAA for health, GLBA for finance).

**European Union / GDPR**
- Check for: lawful basis for processing, right to erasure, right to
  portability, data protection officer contact, EU representative named,
  adequacy decision or SCCs for data transfers out of EEA
- Flag if policy claims GDPR compliance but does not name a DPA contact
  or EU representative — this is a red flag
- Note if the policy's consent mechanism is genuine opt-in or opt-out-by-
  default

**Other countries**
- Apply best judgment based on the jurisdiction's known privacy framework
- Flag whether the service acknowledges the user's jurisdiction at all

---

## Important Constraints

- **Never fabricate TOSDR data.** If the API returns no results, say so.
  Do not guess at ratings or cite cases that were not returned by the API.
- **Always quote directly from the policy** for any LLM-generated finding.
  Do not paraphrase in a way that changes the meaning.
- **Treat omission as a signal**, not as neutral. If data export is not
  mentioned, note this as a gap, not as "unclear."
- **Do not explain basic privacy concepts** to the user. They are
  privacy-conscious. Be precise and direct.
- **All 12 scorecard rows must appear** in every output, even if some are
  marked "Not addressed in this policy."
- **Confirm TOSDR matches with the user** before using any TOSDR data.
  A wrong match would produce misleading output.
