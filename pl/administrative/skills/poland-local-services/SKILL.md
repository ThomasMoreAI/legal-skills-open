---
name: poland-local-services
title: Poland Local Services
description: Local services. Use when Polish office ownership varies.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-local-services
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Local Services

Use when a procedure varies by voivodeship, powiat, gmina, city, or specific
office; when the user needs an appointment; or when national guidance must be
mapped to a local executor.

Confirm current or intended voivodeship, powiat or city with powiat rights,
gmina/city or Warsaw district, whether the address is
already established, procedure, citizenship/status group when relevant, deadline,
accessibility/language needs, and whether the person can attend in person. Do not
infer the competent office from a postal address without verifying the procedure's
territorial rule.

Use `regions` to normalize the voivodeship, then use `mswia-jst-directory` and
`gus-teryt-api` only to classify the territorial unit. They do not prove
procedural competence. First identify the authority level from the national
procedure, then use `bip-directory` and the local official site to verify the
office name, department,
territorial competence, service channel, current booking system, opening hours,
form version, accessibility, and contact method at action time. Municipal newcomer
centres can assist but do not replace the authority that owns the decision.

Use `local-authority-and-appointment` when the owner is not yet known. Handle
cities with powiat rights and Warsaw districts explicitly; never substitute the
nearest office for a current procedural-competence rule.

Appointments and cancellations can deny scarce slots or create deadlines. The
plugin may identify the public booking landing page and prepare a reviewable
checklist. With a caller-owned tool, use
`../../references/automation-playbook.md`: the user authenticates and completes
CAPTCHA/2FA; task-scoped form filling is allowed; booking, rescheduling, or
cancellation requires a fresh summary of service, office, time, place, and
consequence plus action-time confirmation. Never bypass CAPTCHA, hoard scarce
slots, or poll aggressively. Verify the visible appointment receipt before
claiming success.

Read `../../references/locality-and-appointments.md`; hand substantive questions
back to the relevant domain skill.
