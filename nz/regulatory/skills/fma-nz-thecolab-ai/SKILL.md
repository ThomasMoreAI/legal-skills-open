---
name: fma-nz-thecolab-ai
title: FMA NZ
description: Query FMA warnings/alerts and licensed provider pages for NZ crowdfunding, peer-to-peer lending, and financial-advice sources. Search alerts, list/register providers by type, and return source-backed JSON payloads for machine-readable workflows.
author: thecolab-ai
author_url: https://github.com/thecolab-ai/.skills/tree/main/skills/fma-nz
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: nz
practice: regulatory
language: en
sources:
- title: Api Notes
  path: references/api-notes.md
- title: Source Notes
  path: references/source-notes.md
---

# FMA NZ

## Goal

Provide practical, safe access to New Zealand Financial Markets Authority public information for:

- warnings-and-alerts listing and details
- licensed provider discovery for crowdfunding and peer-to-peer lending
- pointers to the Financial Advice Provider licensing ecosystem and the Financial Service Providers Register

## Use this when

- A user asks for recent FMA warnings and alerts about scams, impersonation, or unregistered providers
- A task needs licensed provider lookup by name/type across FMA public pages
- A workflow needs source URLs and machine-readable metadata for NZ fintech consumer protection checks

## Do not use this for

- Circumventing login walls, bot challenges, or any private/credentialed APIs
- Storing or persisting any scraped payloads
- Treating summary-only outputs as legal or compliance advice

## CLI

Run with:

```bash
python3 skills/fma-nz/scripts/cli.py <command>
```

## Commands

- `warnings list [--query TEXT] [--since YYYY|YYYY-MM-DD] [--until YYYY|YYYY-MM-DD] [--limit N] [--json]` - search/paginate FMA warnings/alerts by text and date window
- `warnings get <slug-or-url> [--json]` - fetch warning detail with source URL, dates, and summary
- `providers list [--type crowdfunding|p2p|advice|all] [--query TEXT] [--limit N] [--json]` - search FMA licensed-provider listings with type hints
- `providers get <slug-or-url-or-fsp-number> [--json]` - fetch one licensed-provider detail page
- `providers sources [--type crowdfunding|p2p|advice|all] [--json]` - return curated source pages and capability notes
- `provider-search <query> [--type crowdfunding|p2p|advice|all] [--limit N] [--json]` - convenience search wrapper over provider listing
- `crowdfunding-platforms [--query TEXT] [--limit N] [--json]` - curated alias for crowdfunding providers
- `advice-providers [--query TEXT] [--limit N] [--json]` - advice-provider source discovery entry point

## Notes

- Read-only, no keys or session credentials required for the FMA public pages the skill queries.
- Advice-provider register discovery is source-limited: FMA links to the Financial Service Providers Register for searchable coverage, and that register requires a JS-enabled flow in this environment.
- Upstream is handled defensively with `upstream_unavailable` exits when traffic is blocked.

## Resources

- `scripts/cli.py` - command implementations
- `scripts/smoke_test.py` - outage-tolerant smoke checks
- `references/api-notes.md` - source URLs, endpoint behaviour, caveats, and field notes
