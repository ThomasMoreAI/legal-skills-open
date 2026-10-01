# Practice profile: Real Estate — Luxembourg

Orchestrator cold-start for plugin `lu-real-estate`. Loaded after `lu/CLAUDE.md`, before
invoking a specific skill.

## Scope

Real property in Luxembourg: notarial conveyancing costs (registration and transcription duties, the Bëllegen Akt tax credit), capital gains on real estate, succession involving real estate, and management of co-owned buildings.

## Forums & authorities

- Notaries — conveyancing deeds.
- Administration de l'enregistrement, des domaines et de la TVA (AED) — registration and transcription duties.
- Justice de paix and tribunaux d'arrondissement for disputes.

## Key sources of law

- Code civil — property, sale, succession.
- Loi modifiée du 16 mai 1975 portant statut de la copropriété des immeubles bâtis.
- Registration and transcription duty rules; income-tax rules on capital gains.

## Citation discipline

Follow `lu/CLAUDE.md` ("art. [N] du Code civil"; "loi du [date]"; court, date, docket). **Never invent** article numbers, case names, or docket numbers. Duty rates and the Bëllegen Akt amount change — state the assumed date.

## When this plugin does NOT apply

- Income tax beyond real-estate gains → `lu/tax`.
- French real estate → `fr/real-estate`.
- Audit of a property company's accounts → `lu/regulatory`.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
