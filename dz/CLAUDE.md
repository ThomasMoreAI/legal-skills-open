# Cross-cutting context: the Algerian legal system

Orchestrator cold-start for any plugin under `dz/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law tradition, strongly influenced by French law; Islamic law is a source for family
and inheritance matters. The judiciary is split into a judicial order (tribunals, courts of
appeal, the Supreme Court) and an administrative order (administrative tribunals, the Council
of State), with a Tribunal of Conflicts between them. The Constitutional Court reviews the
constitutionality of laws (Constitution as revised in 2020).

## Sources of law (by priority)

1. The Constitution.
2. International treaties ratified by Algeria (rank above statutes once ratified).
3. Organic laws, laws, and ordinances.
4. Presidential and executive decrees; ministerial orders (arrêtés).
5. Case law of the Supreme Court and the Council of State — guiding, not formally binding.

## Codes and core instruments

Code civil (Ordonnance n° 75-58 du 26 septembre 1975), Code de commerce (Ordonnance n° 75-59
du 26 septembre 1975), Code de procédure civile et administrative (Loi n° 08-09 du 25 février
2008), Code pénal, and the tax codes. All texts are published in the Journal officiel
(JORADP).

## Language

Arabic is the official language and the Arabic text published in the JORADP prevails;
Tamazight is also a national and official language. French translations are published and
widely used in business and legal practice. When a skill works from a French version, say so
and flag that the Arabic text is authoritative.

## Citation discipline (mandatory for every plugin under `dz/`)

- Statutes: by type, number, and date — "Loi n° [NN-NN] du [date] relative à …"; codes:
  "art. [N] du Code civil".
- Cases: court (Cour suprême / Conseil d'État), chamber, date, and file number.
- **Never invent** article numbers, text numbers, dates, or case references. If unknown,
  say so and ask the user to verify in the JORADP.

## Working with current law

Rates, thresholds, and procedures change frequently — notably through the annual finance law
(loi de finances). A skill that depends on a specific rule must state the assumed version or
year and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
