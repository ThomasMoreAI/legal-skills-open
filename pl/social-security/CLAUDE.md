# Practice profile: Social Security (ZUS) — Poland

Orchestrator cold-start for plugin `pl-social-security`. Loaded after `pl/CLAUDE.md`, before invoking a specific skill.

## Scope

Social-insurance dealings with ZUS, for both contributors (płatnicy) and beneficiaries:

- **`applying-zus-procedures`** — rejestracja płatnika (ZFA/ZPA/ZUA/ZCNA), zgłoszenie pracowników, zasiłki (chorobowy / macierzyński / opiekuńczy), emerytura, renta, świadczenie rehabilitacyjne, payment reliefs (RSR/RSO/RSU), and the appeal path against ZUS decisions.

## Forums & authorities

The Zakład Ubezpieczeń Społecznych (ZUS); online via PUE ZUS. **Note the special appeal route:** a ZUS decision is *not* challenged by the ordinary KPA appeal — odwołanie goes directly to the **sąd rejonowy / okręgowy, wydział pracy i ubezpieczeń społecznych** (KPC art. 477⁸ i nast.; odwołanie within 1 month of service, art. 477⁹ KPC).

## Key sources of law

Within Poland: ustawa o systemie ubezpieczeń społecznych (SUS), ustawa o świadczeniach pieniężnych z ubezpieczenia społecznego w razie choroby i macierzyństwa, ustawa o emeryturach i rentach z FUS, and KPC art. 477⁸–477¹⁴ for the court procedure. Verify the current redaction at runtime. For the sources-of-law hierarchy and working language, see `pl/CLAUDE.md`.

## Citation discipline

Follow the rules in `pl/CLAUDE.md`. **Never invent** article numbers, benefit amounts, or deadlines — the skill verifies current values before relying on them.

## When this plugin does NOT apply

- Tax/KAS contributions and procedures → `tax`.
- Employment-law disputes unrelated to social insurance → `employment`.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
