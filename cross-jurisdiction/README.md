# Cross-jurisdiction (`cross-jurisdiction`)

Comparative skills that analyze several countries' law at once, grouped by practice area; each is a plugin in its own subdirectory.

## Plugins (practice areas)

| Plugin | Practice | Skills |
|---|---|---|
| [`antitrust/`](antitrust/) | Antitrust & Competition | 1 |
| [`arbitration/`](arbitration/) | Arbitration & ADR | 1 |
| [`aviation/`](aviation/) | Aviation & Aerospace | 1 |
| [`commercial/`](commercial/) | Commercial | 3 |
| [`constitutional/`](constitutional/) | Constitutional & Public Law | 2 |
| [`contracts/`](contracts/) | Contracts | 17 |
| [`corporate/`](corporate/) | Corporate | 7 |
| [`criminal/`](criminal/) | Criminal Law | 1 |
| [`cybersecurity/`](cybersecurity/) | Cybersecurity & Information Security | 1 |
| [`data-protection/`](data-protection/) | Data Protection | 52 |
| [`employee-benefits/`](employee-benefits/) | Employee Benefits & Executive Compensation | 3 |
| [`employment/`](employment/) | Employment & Labor | 2 |
| [`environmental/`](environmental/) | Environmental Law | 1 |
| [`family/`](family/) | Family Law | 2 |
| [`general/`](general/) | General | 26 |
| [`healthcare/`](healthcare/) | Healthcare | 1 |
| [`ip/`](ip/) | Intellectual Property | 16 |
| [`life-sciences/`](life-sciences/) | Life Sciences & Pharma | 4 |
| [`litigation/`](litigation/) | Litigation | 6 |
| [`personal-injury/`](personal-injury/) | Personal Injury & Torts | 2 |
| [`real-estate/`](real-estate/) | Real Estate | 1 |
| [`regulatory/`](regulatory/) | Regulatory & Compliance | 22 |
| [`sanctions/`](sanctions/) | Sanctions & Export Controls | 3 |
| [`social-security/`](social-security/) | Social Security & Welfare | 1 |
| [`tax/`](tax/) | Tax | 1 |
| [`tmt/`](tmt/) | Technology, Media & Telecommunications | 1 |
| [`trade/`](trade/) | International Trade & Customs | 1 |
| [`trusts-and-estates/`](trusts-and-estates/) | Trusts & Estates | 1 |
| [`white-collar/`](white-collar/) | White-Collar & Investigations | 4 |

## Cross-cutting context

See [`CLAUDE.md`](CLAUDE.md) — orchestrator cold-start for `cross-jurisdiction/`: the jurisdiction guardrail and citation discipline. It loads before each plugin's own `CLAUDE.md`.

## Provenance & license

Skills imported from open sources ([CaseMark/skills](https://github.com/CaseMark/skills) and [lawve.ai](https://lawve.ai/en/skills) — both Apache-2.0 / per-skill); see each `SKILL.md` for provenance. License: Apache-2.0.
