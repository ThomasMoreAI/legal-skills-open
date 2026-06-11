# Practice profile: Administrative Procedure — Poland

Orchestrator cold-start for plugin `pl-administrative`. Loaded after `pl/CLAUDE.md`, before invoking a specific skill.

## Scope

Choosing the correct legal regime for a written document addressed to an authority, register, or other holder of information — preventing the mixing of incompatible procedures in one text:

- **`determining-pl-request-regime`** — routing a request/letter to a single regime (one document = one regime) across UDIP (public information), KPA (administrative procedure), PPSA (complaints to administrative courts), RODO access, registry extracts, special procedures, and advocate/radca prawny letters.

## Forums & authorities

Administrative organs of first instance and appeal (organ wyższego stopnia), and on judicial review the **administrative courts — Wojewódzki Sąd Administracyjny (WSA) and Naczelny Sąd Administracyjny (NSA)** under PPSA. Sector-specific bodies (US/KAS, ZUS, USC, UdSC) have their own plugins.

## Key sources of law

Within Poland: ustawa o dostępie do informacji publicznej (UDIP), Kodeks postępowania administracyjnego (KPA), Prawo o postępowaniu przed sądami administracyjnymi (PPSA), RODO (2016/679) + UODO, and the relevant registry/special statute. Verify the current redaction at runtime. For the sources-of-law hierarchy and working language, see `pl/CLAUDE.md`.

## Citation discipline

Follow the rules in `pl/CLAUDE.md`. **Never invent** article numbers, deadlines, or case signatures — verify the current version before relying on a reference.

## When this plugin does NOT apply

- Tax procedures (US/KAS) → `tax`; social insurance (ZUS) → `social-security`; foreigners (cudzoziemcy) → `immigration`; civil-status acts (USC) → `family`.
- Drafting the substantive document itself → the relevant practice plugin.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
