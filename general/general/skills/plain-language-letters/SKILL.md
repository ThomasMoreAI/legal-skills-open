---
name: plain-language-letters
title: '[DEPRECATED] Plain-Language Letters → see `$legal-clinic:client-letter` and `$legal-clinic:status client`'
description: 'Reference: DEPRECATED — use `$legal-clinic:client-letter` for routine correspondence or `$legal-clinic:status client` for substantive updates. Split into two more focused skills during the v2 rebuild. Kept as a redirect for migration.'
author: alexchlou
author_url: https://github.com/alexchlou/codex-for-legal/tree/main/plugins/legal-clinic/skills/plain-language-letters
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

> Codex v1 local-input note: This migrated skill supports local files and pasted text by default. References to Drive, CLM IDs, Slack, Westlaw, iManage, Ironclad, eDiscovery, dockets, or other remote systems require a separately configured Codex connector/MCP server. When a connector is unavailable, ask for a local export, local file path, or pasted excerpts. If `config/local/codex-for-legal/<practice>/CLAUDE.md` is missing, ask the user to run the relevant `cold-start-interview` or `customize` skill and copy from `config/templates/codex-for-legal/<practice>/CLAUDE.md`.


# [DEPRECATED] Plain-Language Letters → see `$legal-clinic:client-letter` and `$legal-clinic:status client`

This skill was split during the v2 rebuild:

- **Routine correspondence** (appointment confirms, document requests, brief
  "we filed it" updates) → `skills/client-letter/` — use `$legal-clinic:client-letter [type]`

- **Substantive client status updates** → `skills/status/` in client-facing
  mode — use `$legal-clinic:status client`

Both apply the plain-language standards (reading level, no jargon) from CLAUDE.md.

See the respective SKILL.md files for full workflows.
