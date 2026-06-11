# Practice profile: Tax — Poland

Orchestrator cold-start for plugin `pl-tax`. Loaded after `pl/CLAUDE.md`, before invoking a specific skill.

## Scope

Dealings with the tax administration (urząd skarbowy / KAS):

- **`applying-skarbowy-procedures`** — NIP (NIP-2/7/8, CEIDG), VAT-R, czynny żal (art. 16 KKS), korekta deklaracji (art. 81 OP), ulgi (art. 67a OP — odroczenie, raty, umorzenie), nadpłata (art. 72 OP), interpretacja indywidualna (Dyrektor KIS, art. 14b OP), tax control and proceedings (OP dz. IV), and appeals to DIAS and the administrative courts.

## Forums & authorities

The Krajowa Administracja Skarbowa (KAS): naczelnik urzędu skarbowego (first line), izby administracji skarbowej (IAS) and the Dyrektor IAS (DIAS) on appeal, urzędy celno-skarbowe (UCS), and the **Dyrektor Krajowej Informacji Skarbowej (KIS)** for individual interpretations. Judicial review by the administrative courts (**WSA → NSA**). Online: e-Urząd Skarbowy, KSeF, `eureka.mf.gov.pl` for interpretations.

## Key sources of law

Within Poland: Ordynacja podatkowa (OP), Kodeks karny skarbowy (KKS), and the substantive tax statutes (VAT, PIT, CIT, PCC). Verify the current redaction and rates at runtime. For the sources-of-law hierarchy and working language, see `pl/CLAUDE.md`.

## Citation discipline

Follow the rules in `pl/CLAUDE.md`. **Never invent** article numbers, rates, or deadlines — the skill verifies current values before relying on them.

## When this plugin does NOT apply

- Social-insurance contributions and ZUS procedures → `social-security`.
- Choosing which request/complaint regime applies in the abstract → `administrative`.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
