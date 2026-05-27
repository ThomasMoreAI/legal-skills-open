---
name: ca-discovery-verification
title: California Discovery Verification
description: Drafts California Superior Court discovery verification pages under CCP §§ 2030.250 and 2031.250 with proper CCP § 2015.5 perjury declarations. Trigger when the user needs a verification page for interrogatory or inspection/RPD responses, mentions California discovery verification, party vs. attorney signing, information-and-belief clauses, or fixing unverified responses. CA Superior Court only — not federal.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ca-discovery-verification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting]
---

# California Discovery Verification

Produces correctly formatted CA verification pages with proper signer capacity, knowledge basis, and CCP § 2015.5 perjury declaration. Unverified responses are treated as no response — the responding party waives objections and faces motions to compel (*Appleton v. Superior Court* (1988) 206 Cal.App.3d 632 [VERIFY]).

## Quick Start

1. Gather intake details (see Pre-Draft Intake)
2. Select verification type by discovery device
3. Select knowledge basis clause
4. Draft verification from template
5. Run quality audit
6. Confirm alignment with user

## Pre-Draft Intake

Gather before drafting (apply labeled defaults if user says "use defaults" or "just draft"):

| Field | Details | Default |
|---|---|---|
| Discovery device | Interrogatories (Form/Special) or inspection demand/RPD | Interrogatory |
| Exact response title | Must match verbatim on verification | — |
| Caption info | Court name, case number, party names | — |
| Responding party type | Individual or entity (corp, LLC, partnership) | Individual |
| Signer identity | Legal name, title/role, authority basis (entities) | — |
| Knowledge basis | Personal knowledge only, or information and belief | Info & belief |
| Execution details | Date, city, state | — |

> Do not draft verification for responses that have not been finalized.

## Step 1: Select Verification Type

| Device | Statute |
|---|---|
| Interrogatories (Form/Special) | CCP § 2030.250 |
| Inspection demand / RPD | CCP § 2031.250 |
| Federal court | Stop — use FRCP 33/34 + 28 U.S.C. § 1746 [VERIFY] |

## Step 2: Select Knowledge Basis

- **Personal knowledge only**: "The matters stated in the foregoing responses are true of my own knowledge."
- **Information and belief** (signer relied on records, employees, or collected info): "The matters stated in the foregoing responses are true of my own knowledge, except as to those matters stated on information and belief, and as to those matters I believe them to be true."

## Step 3: Draft Verification

### Individual Template

```text
[CAPTION BLOCK]

VERIFICATION OF [PARTY NAME] TO [EXACT RESPONSE TITLE]

I am the [plaintiff/defendant] in this action. I have read the foregoing responses and know the contents thereof.
[KNOWLEDGE BASIS CLAUSE]

I declare under penalty of perjury under the laws of the State of California that the foregoing is true and correct.
Executed on [DATE], at [CITY], [STATE].

___________________________
[SIGNER NAME]
[Plaintiff/Defendant]
```

### Entity Template

```text
[CAPTION BLOCK]

VERIFICATION OF [ENTITY NAME] TO [EXACT RESPONSE TITLE]

I am the [TITLE] of [ENTITY NAME], a party to this action, and am authorized to make this verification for and on its behalf. I have read the foregoing responses and know the contents thereof.
[KNOWLEDGE BASIS CLAUSE]
[OPTIONAL: "I am informed by the employees and records of [ENTITY NAME] regarding the matters stated."]

I declare under penalty of perjury under the laws of the State of California that the foregoing is true and correct.
Executed on [DATE], at [CITY], [STATE].

[ENTITY NAME]
By: _______________________
    [SIGNER NAME]
    Its: [TITLE]
```

Templates apply to both interrogatory and inspection/RPD verifications — select the matching type from Step 1.

## Post-Draft Alignment

After delivering, confirm with the user:

1. Verification title matches response document title exactly
2. Signer has proper authority (especially for entities)
3. Knowledge basis clause is appropriate
4. Execution location is correct (out-of-state may need adjustment)

## Quality Audit

Before finalizing, verify all of the following:

- [ ] Verification title matches response title verbatim
- [ ] Signer capacity stated; entity authorization language included
- [ ] CCP § 2015.5 perjury language verbatim: "under the laws of the State of California"
- [ ] Execution date and city/state present
- [ ] Signature block includes name and capacity
- [ ] Objections not verified (attorney signs for objections)
- [ ] Knowledge basis clause matches actual basis of responses
- [ ] Federal court not using CCP form
- [ ] No attorney signature where party signature required

## Pitfalls

- Title mismatch between verification and response invites motions to compel
- Attorney-signed verifications invalid except narrow CCP § 446 circumstances [VERIFY]
- "Personal knowledge" clause wrong if signer relied on records — use information-and-belief
- Never verify legal objections — attorney signs the response document for those
- Omitting "under the laws of the State of California" from perjury declaration is a fatal defect
- No notarization unless court order or client policy requires it
- Perjury exposure for false verifications (Cal. Penal Code § 118) [VERIFY]
- All case citations must be verified or flagged `[VERIFY]` — do not invent case law
- **Attorney review required** — all output must be reviewed by supervising counsel before signature or service
