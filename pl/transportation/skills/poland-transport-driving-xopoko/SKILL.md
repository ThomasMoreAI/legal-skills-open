---
name: poland-transport-driving-xopoko
title: Poland Transport and Driving
description: Transport. Use when Polish licences or passenger rights matter.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-transport-driving
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: transportation
language: en
---

# Poland Transport and Driving

Use for driving-licence exchange or recognition, vehicle/driver administrative
routes, public-transport authority navigation, and the local office or document
chain. Do not decide whether a foreign licence is valid from nationality alone.

Confirm issuing country, licence category and validity, residence/status context,
date of establishing residence, locality, professional-driving context, and the
specific action sought. Avoid licence, registration, VIN, address, and insurance
numbers in bundled tools; do not open personal transport documents.

Use `drivers-act-consolidated` for the legal recognition and ordinary-residence
distinction, then `gov-driving-licence-exchange` and the competent local authority
for the service route. Verify treaty/EU context, required translations or
verification, any medical or examination step, appointment channel, fee, and
form at action time. For hands-on portal help, apply
`../../references/automation-playbook.md`: the user authenticates, signs,
attests, and handles original-document surrender; task-scoped record inspection
and form filling are allowed, while booking, payment initiation, submission,
upload, download, or record change requires fresh action-time confirmation.

Do not merge the foreign-licence clocks. The six-month recognition period in
the current Act on Vehicle Drivers applies to the foreign-licence categories it
names and runs from the start of permanent or temporary stay. The separate
Gov.pl exchange route uses at least 185 days of living in Poland. Neither clock
starts automatically on the issue date of a residence card or EU Blue Card, and
EU/EEA/Swiss and certain UK licences have separate branches. Keep the answer
undetermined until issuing country, licence type and validity, residence facts,
and current official rules are verified.

Foreign document chains route to `poland-foreign-documents`; municipal routing
to `poland-local-services`; EU mobility context to `poland-eu-mobility`. For an
accident, danger, or police matter use `poland-emergency-rights`. Read
`../../references/daily-life-map.md`.
