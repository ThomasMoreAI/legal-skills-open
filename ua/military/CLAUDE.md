# Practice profile: Military & Defence Law — Ukraine

> **DRAFT** — auto-generated on import; review and refine before merge.

Orchestrator cold-start for plugin `ua-military`. Loaded after `ua/CLAUDE.md`, before invoking a specific skill.

## Scope

Defence-law matters affecting service members: monetary payments and allowances, locating the correct military statutes and orders, the ВЛК (military-medical board) procedure and its appeal, and relief from criminal liability for СЗЧ / desertion on first voluntary return. Sensitive, fast-changing area — wartime regulation changes frequently.

## Forums & authorities

Military units and the ТЦК, the Ministry of Defence and its medical boards (ВЛК), and — on appeal — the higher ВЛК and the administrative courts (КАС). Criminal matters (СЗЧ, desertion) run through the investigator and the criminal courts.

## Key sources of law

Within Ukraine: the statutes on military duty and social protection of service members, the military disciplinary and service statutes, Ministry of Defence orders, and Cabinet of Ministers resolutions on payments. These change often and many carry martial-law modifications — cross-check `checking-martial-law-overrides` in `ua/general`. For the sources-of-law hierarchy and working language, see `ua/CLAUDE.md`.

## Citation discipline

Follow the rules in `ua/CLAUDE.md`. **Never invent** statute numbers, order numbers, payment amounts, or deadlines — each skill verifies the current redaction and values via official sources before relying on a reference.

## When this plugin does NOT apply

- Court challenge of a ВЛК conclusion or payment refusal → `litigation` (КАС route)
- General (non-military) legislation → `ua/general`

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
