# Cross-jurisdiction (`cross-jurisdiction`)

Comparative skills that analyze several countries' law at once, grouped by practice area; each is a plugin in its own subdirectory.

## Plugins (practice areas)

| Plugin | Practice | Skills |
|---|---|---|
| [`data-protection/`](data-protection/) | Data Protection & Privacy | 6 |
| [`general/`](general/) | General / Cross-Practice | 1 |
| [`ip/`](ip/) | Intellectual Property | 1 |
| [`regulatory/`](regulatory/) | Regulatory & Administrative | 4 |

## Cross-cutting context

See [`CLAUDE.md`](CLAUDE.md) — orchestrator cold-start for `cross-jurisdiction/`: the jurisdiction guardrail and citation discipline. It loads before each plugin's own `CLAUDE.md`.

## Provenance & license

Skills imported from open sources ([CaseMark/skills](https://github.com/CaseMark/skills) and [lawve.ai](https://lawve.ai/en/skills) — both Apache-2.0 / per-skill); see each `SKILL.md` for provenance. License: Apache-2.0.
