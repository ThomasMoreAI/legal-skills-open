---
name: legal-admin-tracker
title: Legal Admin Tracker
description: Track legal and administrative obligations including IDs, permits, contracts, renewals, and due dates with reminder-ready outputs. Use when the user asks to organize paperwork, deadlines, compliance checklists, or contract follow-ups.
author: YaRepo
author_url: https://github.com/YaRepo/yaswarm-agency/tree/main/skills/legal-admin-tracker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Admin Tracker

## Overview
Use this skill to centralize deadlines, documents, and follow-ups for legal/admin operations.

## Workflow
1. Capture obligations and documents.
2. Normalize dates and responsible party.
3. Build deadline queue with urgency levels.
4. Generate follow-up actions and checklist status.

## Safety Rules
- Mark unknown due dates as unknown; never guess legal deadlines.
- Do not provide legal advice; provide process tracking only.
- Keep originals immutable in preview workflows.

## Resources
- Checklist template: `references/checklist-template.md`
- Tracker script: `scripts/deadline_queue.py`

## Output Contract
1. Deadline queue
2. Missing documents list
3. Follow-up actions
4. Risks and unresolved items
