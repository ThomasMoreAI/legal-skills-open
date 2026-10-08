# verify-attorney

A Claude skill that checks whether a lawyer, law firm, "immigration consultant", or "notario" is legitimate and safe to hire, before you pay or sign anything. It runs a licensure-first checklist against authoritative sources and returns a verdict plus one recommended action.

Works with Claude Code (and other agents that support the [Agent Skills](https://agentskills.io) format). It assesses legitimacy and hiring safety only. It does not give legal or immigration-strategy advice.

## Why

Legal-services fraud, especially in immigration, preys on people under pressure. "Notario" and "immigration consultant" scams, guaranteed-outcome promises, and Zelle-upfront-no-contract demands are common and often look professional. The reliable filter is not the website's polish. It is whether a named attorney is actually licensed and in good standing at the state bar, and whether the terms match how real firms operate.

## The checks

1. **Get a nameable identity** — an individual attorney's name, jurisdiction, and ideally a bar number. Refusal to name one is a red flag.
2. **State bar licensure (authoritative)** — confirm the license is active and matches the name; a bar number that names a *different* person is impersonation and the strongest scam signal.
3. **Attorney vs consultant/notario** — only a licensed attorney or a DOJ-accredited representative may give US immigration legal advice.
4. **Guaranteed outcome** — no ethical lawyer guarantees a government decision.
5. **Written engagement letter** — "no contract, my word" is a red flag.
6. **Payment structure** — cash/Zelle/crypto only and full upfront, on irreversible rails, is a red flag.
7. **Identity and footprint** — verifiable address, aged domain (RDAP), real reviews.

Verdicts: **Legit**, **Caution**, or **Scam / UPL**, each with a recommended action, plus a table of authoritative sources (state bar lookups, USCIS, DOJ EOIR, AILA, FTC).

## Install

### Claude Code

```bash
mkdir -p ~/.claude/skills/verify-attorney
cp SKILL.md ~/.claude/skills/verify-attorney/SKILL.md
```

On Windows: copy `SKILL.md` to `%USERPROFILE%\.claude\skills\verify-attorney\SKILL.md`.

Then ask something like "is this immigration lawyer legit?" and paste or name the provider.

### Other agents

The skill is a single self-contained `SKILL.md` in the Agent Skills format. Place it wherever your agent discovers skills. See [agentskills.io/specification](https://agentskills.io/specification).

## Scope and disclaimer

This is a legitimacy and safety screen, not legal advice and not a substitute for consulting a licensed attorney. Always confirm licensure yourself in the official state bar directory before hiring anyone.

## License

MIT. See [LICENSE](LICENSE).

## Contributing

Issues and pull requests welcome, especially additional state bar lookup notes and new fraud patterns.
