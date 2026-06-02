---
name: plain-language-letters-anthropics
title: '[DEPRECATED] Plain-Language Letters → see `/client-letter` and `/status client`'
description: 'Reference: DEPRECATED — use `/client-letter` for routine correspondence or `/status client` for substantive updates. Split into two more focused skills during the v2 rebuild. Kept as a redirect for migration.'
author: anthropics
author_url: https://github.com/anthropics/claude-for-legal/tree/main/legal-clinic/skills/plain-language-letters
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# [DEPRECATED] Plain-Language Letters → see `/client-letter` and `/status client`

This skill was split during the v2 rebuild:

- **Routine correspondence** (appointment confirms, document requests, brief
  "we filed it" updates) → `skills/client-letter/` — use `/client-letter [type]`

- **Substantive client status updates** → `skills/status/` in client-facing
  mode — use `/status client`

Both apply the plain-language standards (reading level, no jargon) from CLAUDE.md.

See the respective SKILL.md files for full workflows.
