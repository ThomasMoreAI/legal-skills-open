# Cross-cutting context: the Vietnamese legal system

Orchestrator cold-start for any plugin under `vn/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Socialist legal system of the civil-law family; the 2013 Constitution is supreme and law is enacted by the National Assembly. Selected court precedents (án lệ) are officially published for reference.

## Sources of law (by priority)

1. The 2013 Constitution.
2. Codes and laws of the National Assembly.
3. Ordinances and resolutions of the Standing Committee; government decrees; circulars.
4. Published precedents (án lệ) of the Supreme People's Court.

## Codes

Core codes: Civil Code (2015), Penal Code, Civil Procedure Code, Labour Code.

## Language

Statutes, decisions, and official documents are in Vietnamese.

## Citation discipline (mandatory for every plugin under `vn/`)

- Statutes/codes: "Article 117 of the Civil Code 2015".
- Precedents: by án lệ number (e.g. "Án lệ số 01/2016/AL").
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
