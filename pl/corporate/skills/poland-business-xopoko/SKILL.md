---
name: poland-business-xopoko
title: Poland Business
description: Business. Use when Polish registries matter.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-business
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: corporate
language: en
---

# Poland Business

Use for business-form navigation, CEIDG/KRS/REGON lookups, registration phases,
licensed activity discovery, founder immigration dependencies, and official
registry evidence. Do not select a legal or tax form for the user from a generic
question.

Confirm citizenship/status group, intended activity, sole trader versus entity
question, founders, locality, employees, regulated activity, cross-border scope,
and the decision the user is actually making. Route residence dependencies to
`poland-stay-residence`, tax analysis to `poland-tax`, and ZUS questions to
`poland-social-insurance`.

Prefer public registry lookups and official Biznes.gov.pl, CEIDG, KRS, and GUS
sources. Only an unauthenticated, officially documented public registry API may
support read-only verification. Credentialed APIs and undocumented endpoints
are outside this plugin's boundary.

Build a dependency graph: legal/status gate, form decision requiring advice,
registry and identifiers, regulated-activity checks, tax/ZUS, banking/accounting,
and post-registration duties. Prepare reviewable drafts and checklists without
placing personal values in bundled plugin tools.

Hands-on registry work follows `../../references/automation-playbook.md`. The
authorized business actor handles authentication, secrets, signatures, legal or
tax attestations, final payment authorization, and irreversible closure. After
explicit task scope, the agent may inspect relevant records and fill necessary
fields; registration, server-side draft creation, record changes, upload,
download, and payment initiation require action-time confirmation. Read
`../../references/work-tax-business.md`.
