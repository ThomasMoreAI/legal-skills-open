---
name: poland-employment-services-xopoko
title: Poland Public Employment Services
description: 'Public employment services: route jobseeker registration, labour offices, unemployment status or benefits, training, and employer services. Excludes work permits and workplace-rights disputes.'
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-employment-services
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: social-security
language: en
---

# Poland Public Employment Services

Use for powiat labour-office ownership, jobseeker or unemployed-person
registration, unemployment benefit orientation, training and activation
programmes, public job listings, and employer-facing employment services. Use
`poland-work-authorization` for a foreign national's right-to-work route and
`poland-employment-rights` for contracts, wages, dismissal, or labour disputes.

Capture the requested service, broad citizenship/status and work-access
category, employment/end-of-work context, insurance history category, locality,
target date, and whether the actor is worker, jobseeker, or employer. Keep
identifiers, CVs, employer records, and benefit statements out of bundled
CLI/MCP inputs.

Identify the competent labour office and distinguish public listings,
registration, benefit assessment, training, employer notification, and work
authorization. Show current official source IDs, available channel, locally
varying appointment or document practice, and any fact that the office must
decide. Read `../../references/life-events-and-services.md`,
`../../references/work-tax-business.md`, and
`../../references/locality-and-appointments.md`.

For praca.gov.pl or another protected workflow, apply
`../../references/automation-playbook.md`. The user authenticates and controls
signatures and declarations. The agent may navigate and prepare reviewable
fields within the authorized actor/account scope; submit, send, book, upload,
download, or record change needs fresh action-time confirmation. Never switch
between employer and worker roles silently.

Route contributions to `poland-social-insurance`, benefits outside employment
services to `poland-benefits-support`, tax to `poland-tax`, and a refusal or
deadline dispute to `poland-appeals-review`.
