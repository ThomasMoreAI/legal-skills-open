---
name: poland-foreign-documents-xopoko
title: Poland Foreign Documents
description: Foreign documents. Use for apostille, legalization, sworn translation, diploma recognition, or regulated-profession routing in Poland.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-foreign-documents
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Foreign Documents

Use when a foreign document may need an official copy, apostille or
legalization, sworn translation, academic recognition, or regulated-profession
recognition for a Polish procedure. Ordinary identity and civil-record issuance
belongs to `poland-identity`.

Start from the receiving authority and destination procedure. Ask only for the
issuing country and authority, document category, destination, language, form,
deadline, and the receiver's published requirement. Keep personal documents out
of bundled plugin tools and durable artifacts. A selected document may be
inspected or translated in a caller-owned tool only after explicit task-scoped
authorization and only to the minimum extent needed.

Use current Ministry of Foreign Affairs, sworn-translator register, NAWA, and
competent profession-authority sources. Build the chain from official copy to
authentication or exemption, authorized translation when required, receiver
format, and the exact official landing-page handoff. Preserve official Polish
terminology and identify where the receiver must confirm sufficiency. Do not
certify authenticity, translation accuracy, equivalence, or legal sufficiency.

For regulated-profession questions, use scenario
`professional-qualification-recognition` with
`gov-professional-qualifications-incoming` and `nawa-regulated-professions`.
First classify regulated versus non-regulated, qualification country, sector,
intended role, and profession-specific authority. Keep academic recognition,
professional recognition, and work authorization as separate decisions. Never
infer recognition, eligibility, document sufficiency, or permission to work.

Ordering, booking, payment initiation, upload, download, or submission follows
the action-time confirmation in `../../references/automation-playbook.md`. The
user authenticates, signs or attests, authorizes final payment, and chooses any
irreversible surrender or disposition of an original document.

Route the destination procedure to its owner. Read
`../../references/documents-and-language.md`.
