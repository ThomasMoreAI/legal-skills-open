# Practice profile: Military & Defence Law — Ukraine

Orchestrator cold-start for plugin `ua-military`. Loaded after `ua/CLAUDE.md`, before invoking a specific skill.

## Scope

Defence-law matters affecting service members. This is a sensitive, fast-changing area — wartime regulation is amended frequently, so currency-checking is mandatory.

- **`calculating-military-payments`** — бойові, фронтова надбавка, ОГД (поранення/загибель), payments to families of POWs/missing persons, матдопомога, УБД, military pensions: formulas, pro-rata for partial months, documents, typical refusal grounds.
- **`military-statute-refs`** — verified reference table for the military statutes, MO orders, and CMU resolutions (with `zakon.rada` IDs and URLs).
- **`vlk-procedure`** — the ВЛК (military-medical board) procedure: fitness categories А/Б/В/Г/Д, steps, deadlines, and grounds for setting a conclusion aside, plus its appeal.
- **`szch-decriminalization`** — relief from criminal liability for СЗЧ (ст. 407 КК) or desertion (ст. 408 КК) on a first voluntary return under ч. 5 ст. 401 КК.

## Forums & authorities

Military units and the **ТЦК**; the **Ministry of Defence and its medical boards (ВЛК)**. ВЛК conclusions are appealed hierarchically (гарнізонна → окружна → Центральна ВЛК) and/or to the **administrative courts (КАС)** — note the КАС limitation periods (6 months generally, 3 months after a hierarchical complaint, ст. 122 КАС). Criminal matters (СЗЧ, desertion) run through the investigator, prosecutor, and criminal courts.

## Key sources of law

Used by the skills (verify the current redaction at runtime — IDs are `zakon.rada` identifiers):

- **Statutes & service:** Дисциплінарний статут ЗС (`551-14`), Статут внутрішньої служби (`548-14`), гарнізонної та вартової служби (`550-14`), стройовий (`549-14`); ЗУ «Про військовий обов'язок і військову службу» (`2232-12`), «Про мобілізаційну підготовку та мобілізацію» (`3543-12`), «Про соціальний і правовий захист військовослужбовців та членів їх сімей» (`2011-12`), «Про статус ветеранів війни» (`3551-12`).
- **ВЛК:** Положення про військово-лікарську експертизу — наказ МО № 402 (`z1109-08`).
- **Payments:** постанова КМУ № 168 (`168-2022-п`), фронтова надбавка — № 419 (`419-2024-п`), and related CMU resolutions.
- **СЗЧ relief:** ч. 5 ст. 401 КК, introduced by Закон № 3902-IX (`3902-20`), in force from 07.09.2024.

Many of these carry martial-law modifications — cross-check `checking-martial-law-overrides` in `ua/general`.

## Citation discipline

Follow the rules in `ua/CLAUDE.md`. **Never invent** statute/order numbers, payment amounts, or deadlines — each skill verifies the current redaction and values against official sources before relying on them. Criminal defence (СЗЧ) requires the participation of a lawyer.

## When this plugin does NOT apply

- Court challenge of a ВЛК conclusion or payment refusal → `litigation` (КАС route).
- General, non-military legislation → `ua/general`.
- Administrative services unrelated to service (passports, driver licences) → `administrative`.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
