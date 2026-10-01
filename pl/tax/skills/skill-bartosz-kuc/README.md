# verify-polish-company — a Claude Agent Skill

A single [Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
that teaches Claude (Claude Code, the Claude apps, or the Agent SDK) how to
verify Polish companies through **[skanfirmy.pl](https://skanfirmy.pl)** — the
same free, keyless API this repository documents.

It covers:

- **VAT status & bank-account** checks on the Ministry of Finance White List
  (Biała Lista) by NIP,
- **KRS** registry data (legal form, PKD, capital, address, representation),
- **REGON / GUS** lookup by NIP (for sole traders and other natural persons
  only name, legal form, entity type, town and activity status),
- **VIES** validation of EU VAT numbers,
- **bulk** checks of up to 30 NIPs in one call,
- and the equivalent **MCP** tools at `https://skanfirmy.pl/mcp`.

No API key, no account, no signup — the skill is just instructions; nothing is
installed or run beyond ordinary HTTP calls to the public endpoints. Per-IP rate
limits apply: 20 requests per 10 seconds for REST, 60 for MCP.

## Install

```bash
git clone https://github.com/bartosz-kuc/skanfirmy-mcp

# Claude Code — personal skills (all projects)
mkdir -p ~/.claude/skills
cp -R skanfirmy-mcp/skill ~/.claude/skills/verify-polish-company

# …or project-scoped skills (one repo only)
mkdir -p .claude/skills
cp -R skanfirmy-mcp/skill .claude/skills/verify-polish-company
```

Then start (or restart) Claude Code. The skill auto-loads when a task matches
its description — e.g. *"is NIP 5260250995 an active VAT payer?"* or
*"check this contractor's bank account on the White List"*.

For the Claude apps / Agent SDK, add the skill through that surface's skills
mechanism; `SKILL.md` is portable across all of them.

## Use it directly, without the skill

Everything the skill wraps is a plain public endpoint:

```bash
curl "https://skanfirmy.pl/regon/5260250995?format=json"
curl "https://skanfirmy.pl/nip/5260250995?format=json"
curl "https://skanfirmy.pl/vies/IE/6388047V?format=json"
```

The endpoint map for agents is at <https://skanfirmy.pl/llms.txt>, and the full
MCP server is documented in the [repository README](../README.md).

## License

MIT — free to use, copy and adapt. Data belongs to the respective public
registers (Ministry of Finance, Ministry of Justice, Statistics Poland /
GUS, European Commission).
