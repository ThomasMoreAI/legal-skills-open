# Practice profile: Data Protection (RODO) — Poland

Orchestrator cold-start for plugin `pl-data-protection`. Loaded after `pl/CLAUDE.md`, before invoking a specific skill.

## Scope

Drafting and reviewing personal-data documents under RODO (GDPR) as applied in Poland:

- **`applying-rodo`** — mapping GDPR articles to obligations: legal basis (art. 6/9), klauzule informacyjne (art. 13–14), umowa powierzenia (art. 28), naruszenia (art. 33–34), DPIA (art. 35), and data-subject requests (art. 15–22).

## Forums & authorities

The supervisory authority is the **Prezes Urzędu Ochrony Danych Osobowych (PUODO)**; its decisions are reviewed by the administrative courts (WSA → NSA). Civil claims (e.g. damages under art. 82 GDPR) go to the common courts.

## Key sources of law

RODO — Rozporządzenie (UE) 2016/679 (directly applicable, takes primacy), and the Polish ustawa o ochronie danych osobowych z 10.05.2018 (UODO) plus sector-specific provisions. Verify the current redaction and the latest PUODO/EDPB guidance at runtime. For the sources-of-law hierarchy and working language, see `pl/CLAUDE.md`.

## Citation discipline

Follow the rules in `pl/CLAUDE.md`. Cite GDPR by article (e.g. "art. 6 ust. 1 lit. b RODO") and UODO by article. **Never invent** article numbers, recital references, or decision signatures.

## When this plugin does NOT apply

- A data-subject access request as a routing/regime question → `administrative` (request-regime).
- Employment-specific data handling → `employment`.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
