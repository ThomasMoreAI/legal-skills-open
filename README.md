# Legal Skills (Open)

Open collection of legal AI skills.

## What this is

A public, Apache-2.0-licensed repository of skills for legal AI agents.
Each skill is a single `SKILL.md` file (Anthropic Skills format: YAML frontmatter + Markdown body), grouped into plugins by jurisdiction and practice area: `{country}/{practice}/skills/{slug}/SKILL.md`.

## Using a skill

Skills are not installed locally. Connect the MCP server `mcp.thomasmoreai.com` from any MCP-compatible client (Claude Code, Claude Cowork, ThomasMore desktop, Cursor, …) and the orchestrator finds and runs the right skill through its `discover` and `invoke` tools.

## What a skill looks like

```yaml
---
name: poshlina-calc
title: Расчёт госпошлины в арбитражный суд РФ
description: Computes the Russian commercial-court filing fee under Tax Code arts. 333.21–333.22 / 333.37.
author: ThomasMore
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: ru
practice: arbitration
language: ru
tags: [госпошлина, арбитраж, расчёт]
---
```

## Repository layout

```
legal-skills-open/
├── LICENSE
├── README.md
├── schemas/
│   └── skill-frontmatter.schema.json   # canonical SKILL.md frontmatter spec
└── ru/
    └── arbitration/                    # plugin: ru-arbitration
        ├── plugin.json
        ├── CLAUDE.md
        └── skills/
            ├── poshlina-calc/SKILL.md
            └── case-law-analysis/SKILL.md
```

Allowed `{country}` values: any ISO 3166-1 alpha-2 code, plus `general` (jurisdiction-agnostic) and `cross-jurisdiction` (multi-country comparative).

## Contributing

Open a pull request that adds a `SKILL.md` under the right `{country}/{practice}/skills/{slug}/` path. CI validates the frontmatter, license, and version bump. See `CONTRIBUTING.md` for the full walkthrough.

## License

Apache License 2.0
