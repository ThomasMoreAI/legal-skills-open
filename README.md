# Legal Skills (Open)

> **Open-source library of legal AI skills** in the Anthropic Skills
> (`SKILL.md`) format, runnable by any MCP-compatible client — Claude Code,
> Claude Cowork, Cursor, ChatGPT, the ThomasMore desktop app. **3,500+ skills
> across 39 jurisdictions and 200+ practice plugins** — from filing-fee
> calculators and case-law analysis to GDPR DPA review and US securities
> disclosure. Apache-2.0, contribution-friendly, no lock-in.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-3%2C500%2B-brightgreen)
![Jurisdictions](https://img.shields.io/badge/jurisdictions-39-blue)
![Plugins](https://img.shields.io/badge/plugins-200%2B-blueviolet)
![Format: Anthropic Skills](https://img.shields.io/badge/format-Anthropic_Skills-orange)
![Runtime: MCP](https://img.shields.io/badge/runtime-MCP-9cf)

---

## Table of contents

- [What this repository is](#what-this-repository-is--an-open-source-legal-ai-skill-library)
- [Quick start — connect via MCP in 30 seconds](#quick-start--connect-via-mcp-in-30-seconds)
- [What a skill looks like (`SKILL.md` format)](#what-a-skill-looks-like-skillmd-format)
- [Coverage by jurisdiction](#coverage-by-jurisdiction)
- [Coverage by practice area](#coverage-by-practice-area)
- [Contributing a new legal AI skill](#contributing-a-new-legal-ai-skill)
- [License](#license)
- [FAQ](#faq)
- [Related projects](#related-projects)

---

## What this repository is — an open-source legal AI skill library

A **legal AI skill** is a single Markdown file (`SKILL.md`) that describes one
applied legal task — *«calculate the Russian commercial-court filing fee»,
«analyse this case under FRCP Rule 12(b)(6)», «check this DPA against
GDPR Article 28»* — in a structured format an AI agent can execute
deterministically.

Skills follow the [Anthropic Skills convention](https://www.anthropic.com/news/agent-skills):
YAML frontmatter (machine-readable contract) + Markdown body (the algorithm).
Every skill in this repository is grouped into a plugin by **jurisdiction**
and **practice area**:

```
{country}/{practice}/skills/{slug}/SKILL.md
```

Allowed `{country}` values: any ISO 3166-1 alpha-2 code, plus `general`
(jurisdiction-agnostic) and `cross-jurisdiction` (multi-country comparative).

**You don't install skills locally.** You connect any MCP-compatible client to
the MCP server `mcp.thomasmoreai.com`; the orchestrator finds and runs the
right skill via its `discover` and `invoke` tools.

---

## Quick start — connect via MCP in 30 seconds

### Claude Desktop / Claude Code

Add to `claude_desktop_config.json` (or your `mcp.json`):

```jsonc
{
  "mcpServers": {
    "thomasmore-legal": {
      "url": "https://mcp.thomasmoreai.com/mcp",
      "transport": "http"
    }
  }
}
```

### Cursor

Settings → MCP → Add server → URL: `https://mcp.thomasmoreai.com/mcp`.

### Any other Model Context Protocol client

Point it at `https://mcp.thomasmoreai.com/mcp` (Streamable HTTP transport).
Once connected, ask your agent something jurisdiction-specific, for example:

> *Apply the Russian commercial-court filing fee skill to a claim of 1,500,000 RUB.*
> *Review this DPA against GDPR Article 28 and EDPB Guidelines 07/2020.*
> *Check whether this US contract clause is enforceable in Delaware.*

The orchestrator picks the right skill automatically.

---

## What a skill looks like (`SKILL.md` format)

Real example from [`ru/arbitration/skills/poshlina-calc/`](ru/arbitration/skills/poshlina-calc/):

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

# Skill title

## When to apply
Triggers, example user prompts, what is out of scope.

## Algorithm
Step-by-step instructions for the orchestrator.

## Output contract
What the answer must contain — citations, disclaimer, structured fields.
```

The canonical schema is in
[`schemas/skill-frontmatter.schema.json`](schemas/skill-frontmatter.schema.json).
See [CONTRIBUTING.md](CONTRIBUTING.md) for the full walkthrough.

---

## Coverage by jurisdiction

39 jurisdictions, sorted by plugin count. Click any code to browse plugins
and skills for that jurisdiction.

| Jurisdiction | Plugins | Jurisdiction | Plugins |
|---|---:|---|---:|
| 🇺🇸 [`us/`](us/) — United States | 25 | 🇮🇱 [`il/`](il/) — Israel | 4 |
| 🇩🇪 [`de/`](de/) — Germany | 24 | 🇪🇺 [`eu/`](eu/) — European Union | 4 |
| 🌐 [`general/`](general/) — jurisdiction-agnostic | 22 | 🇨🇭 [`ch/`](ch/) — Switzerland | 4 |
| 🌍 [`cross-jurisdiction/`](cross-jurisdiction/) — comparative | 14 | 🇦🇹 [`at/`](at/) — Austria | 4 |
| 🇨🇳 [`cn/`](cn/) — China | 14 | 🇦🇺 [`au/`](au/) — Australia | 3 |
| 🇹🇷 [`tr/`](tr/) — Türkiye | 8 | 🇹🇼 [`tw/`](tw/) — Taiwan | 2 |
| 🇬🇧 [`gb/`](gb/) — United Kingdom | 8 | 🇷🇺 [`ru/`](ru/) — Russia | 2 |
| 🇪🇸 [`es/`](es/) — Spain | 8 | 🇯🇵 [`jp/`](jp/) — Japan | 2 |
| 🇰🇷 [`kr/`](kr/) — South Korea | 7 | 🇦🇷 [`ar/`](ar/) — Argentina | 2 |
| 🇵🇱 [`pl/`](pl/) — Poland | 6 | 🇦🇪 [`ae/`](ae/) — UAE | 2 |
| 🇧🇷 [`br/`](br/) — Brazil | 6 | 🇿🇦 [`za/`](za/) — South Africa | 1 |
| 🇫🇷 [`fr/`](fr/) — France | 5 | 🇻🇳 [`vn/`](vn/) — Vietnam | 1 |
| 🇨🇦 [`ca/`](ca/) — Canada | 5 | 🇹🇭 [`th/`](th/) — Thailand | 1 |
| 🇺🇦 [`ua/`](ua/) — Ukraine | 4 | 🇸🇦 [`sa/`](sa/) — Saudi Arabia | 1 |
| 🇸🇬 [`sg/`](sg/) — Singapore | 4 | 🇳🇬 [`ng/`](ng/) — Nigeria | 1 |
| 🇮🇳 [`in/`](in/) — India | 4 | 🇲🇽 [`mx/`](mx/) — Mexico | 1 |
| 🇱🇺 [`lu/`](lu/) — Luxembourg | 1 | 🇮🇹 [`it/`](it/) — Italy | 1 |
| 🇬🇷 [`gr/`](gr/) — Greece | 1 | 🇫🇮 [`fi/`](fi/) — Finland | 1 |
| 🇪🇬 [`eg/`](eg/) — Egypt | 1 | 🇨🇲 [`cm/`](cm/) — Cameroon | 1 |
| 🇦🇿 [`az/`](az/) — Azerbaijan | 1 | | |

---

## Coverage by practice area

25 practice areas covered across the 39 jurisdictions. Top areas by plugin count:

| Practice area | Plugins | Typical skills |
|---|---:|---|
| Data protection | 24 | GDPR DPA review, ROPA generation, breach notification, transfer-impact assessments |
| Litigation | 21 | Case-law analysis, pleadings drafting, procedural calculators, discovery review |
| Regulatory | 18 | Compliance checks, regulatory filings, AI governance reviews |
| General | 17 | Cross-practice skills (legal drafting, citation discipline, statute lookup) |
| Real estate | 11 | Lease review, title checks, zoning analysis |
| Contracts | 11 | Clause review, redlines, template generation |
| Corporate | 10 | Cap-table analysis, corporate filings, governance |
| Employment | 8 | Employee-handbook review, termination checks, wage-and-hour |
| Arbitration | 8 | Arbitration-clause design, award analysis, filing-fee calculators |
| Tax | 7 | Tax classification, transfer-pricing review, withholding analysis |
| Intellectual property | 7 | Trademark search, copyright analysis, patent landscaping |
| Trusts & estates | 6 | Will review, probate checks, trust drafting |
| Personal injury | 6 | Damages calculation, statute-of-limitations checks |
| Criminal | 6 | Sentencing analysis, charge-mapping, plea evaluation |
| Commercial | 6 | M&A diligence, commercial-contract review |

Other covered areas: **insurance**, **family**, **antitrust**, **healthcare**,
**finance**, **environmental**, **construction**, **bankruptcy**,
**securities**, **immigration**.

---

## Contributing a new legal AI skill

Skills are short Markdown files — you don't need to write any code.

1. Fork the repository.
2. Add a folder `{country}/{practice}/skills/{slug}/` with a `SKILL.md` inside.
3. If the plugin `{country}/{practice}/` doesn't exist yet, also add
   `plugin.json`, `CLAUDE.md`, and `README.md` (copy from
   [`ru/arbitration/`](ru/arbitration/) as a reference).
4. Open a pull request. CI validates frontmatter, license, and version bump.

CI rules (enforced automatically):

- **License whitelist.** `Apache-2.0`, `MIT`, `BSD-3-Clause`, `BSD-2-Clause`,
  `CC0-1.0`, `CC-BY-4.0`. AGPL / GPL / CC-NC / CC-ND are rejected.
- **`execution_mode: open`** — required in this repository.
- **Path consistency.** `name` must match the folder name; `jurisdiction` and
  `practice` must match the path segments.
- **Semver.** Bump `version` on every change to `SKILL.md`.

Full walkthrough: [CONTRIBUTING.md](CONTRIBUTING.md).
Canonical schema: [`schemas/skill-frontmatter.schema.json`](schemas/skill-frontmatter.schema.json).

You keep all rights to your skill and can publish it elsewhere — on
Lawvable, your own repository, a private deployment — without notifying us.

---

## License

[Apache License 2.0](LICENSE). The repository, every skill in it, and every
contribution to it are Apache-2.0 by default. You can use, modify, distribute,
and run these skills commercially — only attribution is required.

---

## FAQ

### Can I use these skills with Claude, Cursor, ChatGPT, or other clients?

Yes. The skills are delivered over the **Model Context Protocol (MCP)**, which
is supported by Claude Code, Claude Desktop, Cursor, ChatGPT (via MCP plugins),
the ThomasMore desktop app, and any other MCP-compatible client. Point your
client at `https://mcp.thomasmoreai.com/mcp` and the orchestrator handles
discovery and routing.

### Are these skills production-ready?

The repository is **community-curated**. Every skill carries an explicit
`version`, `author`, and `license`, and is reviewed against the schema
before merge. Output of every skill includes a built-in disclaimer that the
answer is informational and does not replace qualified legal advice. Treat
the library as a **second pair of eyes**, not as a substitute for a lawyer
admitted in the relevant jurisdiction.

### Why not just write a prompt myself?

Skills are versioned, testable, and citation-disciplined: each `SKILL.md`
specifies which statutes, regulations, or cases it relies on (and which
edition / date). Ad-hoc prompts drift, hallucinate citations, and aren't
reproducible across team members. Skills make legal AI workflows
**auditable** — important for compliance, conflicts checks, and post-mortems.

### What's the difference between this repo and Anthropic's `claude-for-legal`?

[`claude-for-legal`](https://github.com/anthropics/claude-for-legal) is
Anthropic's official suite of 12 legal plugins. This repository is a
**community-driven, jurisdictionally-tagged, much larger catalogue** under
the same Anthropic Skills format — the two are complementary, and a skill
from either can be invoked through MCP.

### How do I add a skill for my jurisdiction?

If your country code (ISO 3166-1 alpha-2) is missing, just create the folder
— e.g. `pt/contracts/skills/...` — and open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

### Why Apache-2.0 only? Why are AGPL / GPL / CC-NC rejected?

To stay friendly to **commercial deployments** (in-house legal tools, paid
SaaS, regulated industries). AGPL/GPL/CC-NC clauses create license friction
that effectively blocks adoption in those settings, defeating the purpose of
an open skill library.

### Is the orchestrator open-source too?

The orchestrator that serves these skills (`mcp.thomasmoreai.com`) is a
ThomasMore-operated service; the **skills themselves** in this repository are
fully open-source (Apache-2.0). You can run any skill against your own
orchestrator implementation — `SKILL.md` is just a Markdown file.

---

## Related projects

- [Anthropic Skills](https://www.anthropic.com/news/agent-skills) —
  the underlying `SKILL.md` format.
- [Model Context Protocol](https://modelcontextprotocol.io/) — the open
  protocol every MCP-compatible client speaks.
- [`anthropics/claude-for-legal`](https://github.com/anthropics/claude-for-legal) —
  Anthropic's official suite of legal plugins.
- [`travisvn/awesome-claude-skills`](https://github.com/travisvn/awesome-claude-skills) —
  curated list of Claude Skills resources.
- [`Vaquill-AI/awesome-legaltech`](https://github.com/Vaquill-AI/awesome-legaltech) —
  open-source legal-tech catalogue.
- [`wong2/awesome-mcp-servers`](https://github.com/wong2/awesome-mcp-servers) —
  curated list of MCP servers.

---

*Maintained by [ThomasMoreAI](https://github.com/ThomasMoreAI). Issues and
pull requests welcome.*
