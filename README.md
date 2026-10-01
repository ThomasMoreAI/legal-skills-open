# Legal Skills (Open)

> **Open-source library of legal AI skills** in the Anthropic Skills
> (`SKILL.md`) format, runnable by any MCP-compatible client — Claude Code,
> Claude Cowork, Cursor, ChatGPT, the ThomasMore desktop app. **3,600+ skills
> across 40 jurisdictions and 280+ practice plugins** — from filing-fee
> calculators and case-law analysis to GDPR DPA review and US securities
> disclosure. Apache-2.0, contribution-friendly, no lock-in.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-3%2C600%2B-brightgreen)
![Jurisdictions](https://img.shields.io/badge/jurisdictions-40-blue)
![Plugins](https://img.shields.io/badge/plugins-280%2B-blueviolet)
![Format: Anthropic Skills](https://img.shields.io/badge/format-Anthropic_Skills-orange)
![Runtime: MCP](https://img.shields.io/badge/runtime-MCP-9cf)

---

## Table of contents

- [What this repository is](#what-this-repository-is--an-open-source-legal-ai-skill-library)
- [What a skill looks like (`SKILL.md` format)](#what-a-skill-looks-like-skillmd-format)
- [Coverage by jurisdiction](#coverage-by-jurisdiction)
- [Coverage by practice area](#coverage-by-practice-area)
- [License](#license)
- [FAQ](#faq)
- [Related projects](#related-projects)

---

## What this repository is — an open-source legal AI skill library

A **legal AI skill** is a single Markdown file (`SKILL.md`) that describes one
applied legal task — *«calculate the German court fee under the GKG for a
civil claim», «analyse this case under FRCP Rule 12(b)(6)», «check this DPA
against GDPR Article 28»* — in a structured format an AI agent can execute
deterministically.

Skills follow the [Anthropic Skills convention](https://www.anthropic.com/news/skills):
YAML frontmatter (machine-readable contract) + Markdown body (the algorithm).
Every skill in this repository is grouped into a plugin by **jurisdiction**
and **practice area**:

```
{country}/{practice}/skills/{slug}/SKILL.md
```

Allowed `{country}` values: any ISO 3166-1 alpha-2 code, plus `general`
(jurisdiction-agnostic) and `cross-jurisdiction` (multi-country comparative).

**There are two ways to use these skills:**

1. **Locally.** Since this repository is open source and every skill follows the
   Anthropic Skills/plugin format, you can clone it and use the skills locally
   (as Claude Code skills/plugins).
2. **Via the MCP server ThomasMore.** Connect any MCP-compatible
   client to the MCP server `mcp.thomasmoreai.com`; the orchestrator finds and
   runs the right skill via its `discover` and `invoke` tools. Follow
   [thomasmoreai.com](https://thomasmoreai.com/) for updates on the MCP server launch.

---

## What a skill looks like (`SKILL.md` format)

Real example from [`eu/data-protection/skills/gdpr-expert/`](eu/data-protection/skills/gdpr-expert/):

```yaml
---
name: gdpr-expert
title: GDPR Expert
description: GDPR expert for EU privacy compliance. Deep knowledge of General Data Protection Regulation including 99 articles, 7 principles, 6 lawful bases, data subject rights, DPO requirements, DPIA, breach notification, cross-border transfers, and enforcement.
author: GRCEngClub
author_url: https://github.com/GRCEngClub/claude-grc-engineering/tree/main/plugins/frameworks/gdpr/skills/gdpr-expert
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
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

40 jurisdictions, sorted by plugin count. Click any code to browse plugins
and skills for that jurisdiction.

| Jurisdiction | Plugins | Jurisdiction | Plugins |
|---|---:|---|---:|
| 🇺🇸 [`us/`](us/) — United States | 42 | 🇸🇬 [`sg/`](sg/) — Singapore | 4 |
| 🇩🇪 [`de/`](de/) — Germany | 36 | 🇦🇺 [`au/`](au/) — Australia | 3 |
| 🌐 [`general/`](general/) — jurisdiction-agnostic | 27 | 🇱🇺 [`lu/`](lu/) — Luxembourg | 3 |
| 🌍 [`cross-jurisdiction/`](cross-jurisdiction/) — comparative | 21 | 🇦🇪 [`ae/`](ae/) — UAE | 2 |
| 🇨🇳 [`cn/`](cn/) — China | 15 | 🇦🇷 [`ar/`](ar/) — Argentina | 2 |
| 🇵🇱 [`pl/`](pl/) — Poland | 13 | 🇯🇵 [`jp/`](jp/) — Japan | 2 |
| 🇫🇷 [`fr/`](fr/) — France | 11 | 🇷🇺 [`ru/`](ru/) — Russia | 2 |
| 🇪🇸 [`es/`](es/) — Spain | 9 | 🇹🇼 [`tw/`](tw/) — Taiwan | 2 |
| 🇪🇺 [`eu/`](eu/) — European Union | 9 | 🇦🇿 [`az/`](az/) — Azerbaijan | 1 |
| 🇬🇧 [`gb/`](gb/) — United Kingdom | 8 | 🇨🇲 [`cm/`](cm/) — Cameroon | 1 |
| 🇹🇷 [`tr/`](tr/) — Türkiye | 8 | 🇪🇬 [`eg/`](eg/) — Egypt | 1 |
| 🇧🇷 [`br/`](br/) — Brazil | 7 | 🇫🇮 [`fi/`](fi/) — Finland | 1 |
| 🇰🇷 [`kr/`](kr/) — South Korea | 7 | 🇬🇷 [`gr/`](gr/) — Greece | 1 |
| 🇺🇦 [`ua/`](ua/) — Ukraine | 7 | 🇮🇹 [`it/`](it/) — Italy | 1 |
| 🇦🇹 [`at/`](at/) — Austria | 6 | 🇲🇽 [`mx/`](mx/) — Mexico | 1 |
| 🇨🇦 [`ca/`](ca/) — Canada | 6 | 🇳🇬 [`ng/`](ng/) — Nigeria | 1 |
| 🇮🇱 [`il/`](il/) — Israel | 5 | 🇸🇦 [`sa/`](sa/) — Saudi Arabia | 1 |
| 🇨🇭 [`ch/`](ch/) — Switzerland | 4 | 🇹🇭 [`th/`](th/) — Thailand | 1 |
| 🇩🇿 [`dz/`](dz/) — Algeria | 4 | 🇻🇳 [`vn/`](vn/) — Vietnam | 1 |
| 🇮🇳 [`in/`](in/) — India | 4 | 🇿🇦 [`za/`](za/) — South Africa | 1 |

---

## Coverage by practice area

48 practice areas covered across the 40 jurisdictions. Top areas by plugin count:

| Practice area | Plugins | Typical skills |
|---|---:|---|
| Data protection | 25 | GDPR DPA review, ROPA generation, breach notification, transfer-impact assessments |
| Litigation | 22 | Case-law analysis, pleadings drafting, procedural calculators, discovery review |
| General | 19 | Cross-practice skills (legal drafting, citation discipline, statute lookup) |
| Regulatory | 19 | Compliance checks, regulatory filings, AI governance reviews |
| Contracts | 13 | Clause review, redlines, template generation |
| Real estate | 13 | Lease review, title checks, zoning analysis |
| Corporate | 10 | Cap-table analysis, corporate filings, governance |
| Tax | 10 | Tax classification, transfer-pricing review, withholding analysis |
| Commercial | 8 | M&A diligence, commercial-contract review |
| Intellectual property | 8 | Trademark search, copyright analysis, patent landscaping |
| Arbitration | 7 | Arbitration-clause design, award analysis, filing-fee calculators |
| Cybersecurity | 7 | DORA, NIS2 and CRA compliance, ICT contract review, incident reporting |
| Employment | 7 | Employee-handbook review, termination checks, wage-and-hour |
| Criminal | 6 | Sentencing analysis, charge-mapping, plea evaluation |
| Personal injury | 6 | Damages calculation, statute-of-limitations checks |

Other covered areas (each with 1–5 plugins): **antitrust**, **family**,
**government-contracts**, **insurance**, **trade**, **administrative**,
**bankruptcy**, **construction**, **finance**, **healthcare**,
**life-sciences**, **trusts-and-estates**, **white-collar**, **aviation**,
**constitutional**, **consumer**, **employee-benefits**, **environmental**,
**immigration**, **sanctions**, **social-security**, **sports**,
**capital-markets**, **energy**, **military**, **securities**, **tmt**,
**transportation**, **entertainment**, **gaming**, **investment-funds**,
**maritime**, **nonprofit**.

---

## License

[Apache License 2.0](LICENSE). The repository and every contribution to it are
Apache-2.0 by default. You can use, modify, distribute,
and run these skills commercially — only attribution is required.

---

## FAQ

### Can I use these skills with Claude, Cursor, ChatGPT, or other clients?

Yes. The skills are delivered over the **Model Context Protocol (MCP)**, which
is supported by Claude Code, Claude Desktop, Cursor, ChatGPT (via MCP plugins),
the ThomasMore desktop app, and any other MCP-compatible client. Point your
client at `https://mcp.thomasmoreai.com/` and the orchestrator handles
discovery and routing. Follow [thomasmoreai.com](https://thomasmoreai.com/) for 
updates on the MCP server launch.

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

### How do I add a skill for my jurisdiction?

If your country code (ISO 3166-1 alpha-2) is missing, just create the folder
— e.g. `pt/contracts/skills/...` — and open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Related projects

- [Anthropic Skills](https://www.anthropic.com/news/skills) —
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
