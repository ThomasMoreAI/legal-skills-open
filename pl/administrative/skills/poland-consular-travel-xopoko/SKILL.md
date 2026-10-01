---
name: poland-consular-travel-xopoko
title: Poland Consular and Travel Services
description: 'Consular and travel-document services: route Polish consular help, passports, emergency documents, foreign-consulate handoffs, and cross-border travel administration. Excludes travel booking.'
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-consular-travel
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Consular and Travel Services

Use for Polish consular services, passport or emergency-document orientation,
consular appointments, lost-document routes, help for Polish citizens abroad,
and identifying when a foreign national must contact their own embassy or
consulate. Do not book travel or assume that a residence document guarantees
border admission.

Establish whose authority is relevant, broad citizenship/status category,
current country and safe locality, document or service category, travel date,
and urgency. Do not place document numbers, scans, itineraries, or account
identifiers in bundled tools.

Separate Polish consular competence from a foreign state's consular competence,
ordinary travel documentation from immigration status, and routine appointments
from an emergency abroad. Show the exact official authority, country-specific
channel, appointment or personal-appearance requirement, fee/deadline facts to
verify, and emergency contact route. Read
`../../references/life-events-and-services.md`,
`../../references/documents-and-language.md`, and
`../../references/emergency-and-escalation.md`.

For an ordinary or temporary Polish passport, use
`polish-passport-and-consular-appointment` with `gov-passport-adult`,
`gov-temporary-passport`, `mfa-passports-abroad`, and `e-konsulat-portal`.
An ordinary adult passport is not an online submission: personal attendance and
biometrics remain required, while mission competence, appointment category and
availability are verified live. A foreign passport always routes to its issuing
state's current authority.

For an authorized e-Konsulat or other official portal task, apply
`../../references/automation-playbook.md`. The user authenticates and controls
signatures, declarations, identity checks, and payment authorization. The agent
may navigate and prepare reviewable fields; booking, submission, upload,
download, send, payment initiation, or cancellation needs fresh action-time
confirmation. Never bypass appointment controls or CAPTCHA.

Route Polish stay/residence to `poland-stay-residence`, EU free movement to
`poland-eu-mobility`, foreign-record use to `poland-foreign-documents`, and
immediate danger to `poland-emergency-rights`.
