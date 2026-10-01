# Practice profile: Tax — France

Orchestrator cold-start for plugin `fr-tax`. Loaded after `fr/CLAUDE.md`, before
invoking a specific skill.

## Scope

French taxation for businesses and individuals: bookkeeping under the PCG, VAT returns, corporate and income tax, year-end closing and tax return package, wealth tax on real estate (IFI), and simulated tax audits.

## Forums & authorities

- DGFiP — assessment, collection, and tax audits.
- Administrative courts for most tax disputes (direct taxes, VAT); judicial courts for registration duties and wealth tax.

## Key sources of law

- Code général des impôts (CGI).
- Livre des procédures fiscales (LPF) — procedure, audits, taxpayer guarantees.
- BOFiP-Impôts — the administration's published doctrine.
- Plan comptable général (PCG) — accounting rules.
- The annual loi de finances — rates, brackets, thresholds.

## Citation discipline

Follow `fr/CLAUDE.md` (code article; Cass. chamber and `n° de pourvoi`; CE references). **Never invent** article numbers, case names, or docket numbers. State the tax year a rate or bracket comes from.

## When this plugin does NOT apply

- Invoicing mentions and payment terms → `fr/commercial`.
- Succession and gifts on real estate → `fr/real-estate`.
- Luxembourg or Algerian tax → `lu/tax`, `dz/tax`.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
