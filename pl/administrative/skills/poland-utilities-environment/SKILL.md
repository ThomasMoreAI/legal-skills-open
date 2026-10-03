---
name: poland-utilities-environment
title: Poland Utilities and Environment
description: 'Utilities and environment: route electricity, gas, heating, water, waste, provider disputes, and local environmental services in Poland. Excludes technical repair and contract negotiation.'
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-utilities-environment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Utilities and Environment

Use for electricity, gas, district heating, water and sewerage, municipal waste,
metering, provider or billing escalation, energy-regulator routes, air-quality
or environmental reporting, and locality-owned services. Do not perform a
technical diagnosis, enter a property, or negotiate a contract as the user.

Capture the service type, provider or authority category, locality, tenancy or
owner context, outage/safety status, requested effect, and any deadline. Keep
account, meter, address, payment, and contract identifiers out of bundled
CLI/MCP inputs.

Separate emergency utility danger from an outage, billing complaint, contract
change, municipal service, environmental report, and consumer escalation.
Identify the responsible provider, gmina, regulator, or inspectorate; show the
official source, public status channel, online versus phone/in-person path, and
facts that vary by provider or locality. Read
`../../references/life-events-and-services.md`,
`../../references/daily-life-map.md`, and
`../../references/locality-and-appointments.md`.

For a provider portal or online authority form, apply
`../../references/automation-playbook.md`. The user authenticates and controls
payment credentials, contracts, signatures, and attestations. The agent may
inspect the minimum authorized account area and prepare fields; send, submit,
book, cancel, pay, upload, download, or change service needs fresh action-time
confirmation.

Route immediate electrical, gas, fire, or health danger to
`poland-emergency-rights`; housing ownership/tenancy disputes to
`poland-housing`; and consumer escalation to `poland-consumer-banking`.
