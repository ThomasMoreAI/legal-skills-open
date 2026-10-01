---
name: poland-citizenship-long-term-xopoko
title: Poland Citizenship and Long-Term Status
description: Long-term status. Use for Polish permanent residence, EU long-term resident status, or citizenship routes; not temporary residence.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-citizenship-long-term
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: immigration
language: en
---

# Poland Citizenship and Long-Term Status

Use for permanent residence, EU long-term resident status, recognition or
restoration of Polish citizenship, and presidential citizenship-grant
navigation. Do not merge these routes or infer qualification from residence
duration alone.

Treat national permanent residence as its own procedure. Use
`mos-permanent-residence` for its current requirements and procedure,
`udsc-mos-electronic-residence` for the current electronic-filing mechanics,
and `mos-residence` for the service boundary. Do not substitute a citizenship
page or the EU long-term-resident checklist. Capture the claimed statutory-basis
category, present stay category, residence-history category when relevant,
family or Polish-origin context when relevant, current location, competent
voivode, and target date. These facts select a checklist; they do not prove
eligibility.

Capture citizenship group, current stated status, broad family or Polish-origin
context when relevant, residence history as non-identifying categories,
locality, target date, and whether a refusal or pending case exists. Name missing
facts instead of choosing the most favorable route.

Use current Office for Foreigners, Gov.pl, and competent voivodeship or central
authority sources. For each candidate route, identify its owner, current
instructions, evidence categories, language or document dependencies, human
review needs, and exact official landing-page handoff. Do not give an eligibility
verdict, guarantee a timeline, freeze a fee, or treat one route's conditions as
another's. At action time recheck the permanent-residence MOS form, current
filing channel, location rule, signature method, attachments, in-person identity
or biometric follow-up, official receipt, and competent-voivode instructions.

If hands-on service assistance is requested, apply
`../../references/automation-playbook.md`. The user authenticates and performs
signatures and citizenship declarations. Task-relevant record inspection and
form filling need explicit scope authorization; booking, upload, download,
payment initiation, and submission need fresh action-time confirmation. Preserve
qualified review for legally material declarations and exceptional routes. A
permanent-residence application remains the foreigner's procedure: the operator
may prepare reviewable fields, but the user personally authenticates, signs,
attests, completes any required in-person identity or biometric step, and
authorizes every consequential action. Treat an official acknowledgment or
other visible authority receipt as the completion proof.

Temporary stay belongs to `poland-stay-residence`; EU free-movement registration
to `poland-eu-mobility`; foreign certificates and translations to
`poland-foreign-documents`; refusals or delay to `poland-appeals-review`. Read
`../../references/immigration-status-map.md`.
