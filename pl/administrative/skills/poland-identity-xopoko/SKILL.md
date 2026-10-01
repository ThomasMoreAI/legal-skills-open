---
name: poland-identity-xopoko
title: Poland Identity and Registration
description: Identity. Use when PESEL or meldunek matters.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-identity
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Identity and Registration

Use for PESEL, residence registration (`meldunek`), civil records, identity
documents, trusted digital identity prerequisites, and municipality-owned
registration workflows. Do not assume PESEL proves immigration status or that one
office issues every identifier.

Confirm the person's citizenship/status group, whether they are registering a
stay or applying on another legal basis, current gmina/city, housing evidence
available, and the exact downstream service that needs the identifier. Distinguish
PESEL, NIP, REGON, KRS, and document-number categories; never request or put a
real identifier, address, or record content in plugin input or output.

Search current Gov.pl and municipal sources, then verify the local office,
booking channel, form version, required evidence, and whether a representative is
allowed. Build a reviewable field and evidence-category checklist without
placing identifiers in bundled plugin tools.

Hands-on service assistance follows `../../references/automation-playbook.md`.
The user authenticates, proves identity, signs, and accepts declarations. After
explicit task scope, a caller-owned tool may inspect only the selected identity
document or record and fill necessary fields; booking, upload, download, or
submission requires fresh action-time confirmation. Original-document
surrender and biometric or in-person identity checks remain with the user.
For a public e-government landing page use `poland-digital-government`; for
foreign certificates, apostille, or sworn translation use
`poland-foreign-documents`; for local offices use
`poland-local-services`.

Read `../../references/digital-government-map.md`,
`../../references/browser-safety.md`, and
`../../references/locality-and-appointments.md` when the procedure crosses those
boundaries.
