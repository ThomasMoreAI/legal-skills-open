# Practice profile: Tax — Algeria

Orchestrator cold-start for plugin `dz-tax`. Loaded after `dz/CLAUDE.md`, before
invoking a specific skill.

## Scope

Tax compliance and advice under Algerian law: corporate income tax (IBS), personal income tax (IRG), VAT, registration and stamp duties, customs duties, filings, and tax audits.

## Forums & authorities

- Direction générale des impôts (DGI) — assessment, collection, audits.
- Direction générale des douanes — customs duties.
- Administrative recourse first; then the administrative courts for tax disputes.

## Key sources of law

- Code des impôts directs et taxes assimilées.
- Code des taxes sur le chiffre d'affaires (VAT).
- Code des procédures fiscales.
- Code de l'enregistrement and Code du timbre.
- Code des douanes.
- The annual loi de finances and supplementary finance laws — they change rates and abolish or create levies every year.

## Citation discipline

Follow `dz/CLAUDE.md` (text type, number, and date; Arabic text prevails). **Never invent** article or text numbers — verify the current version in the JORADP. State the finance-law year a rate or threshold comes from; check whether a levy named in a skill still exists under the latest loi de finances.

## When this plugin does NOT apply

- Structuring the company or the deal → `dz/contracts` (or a corporate plugin when added).
- Tax fraud investigation and criminal exposure → `dz/white-collar`.
- French or Luxembourg tax → `fr/tax`, `lu/tax`.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
