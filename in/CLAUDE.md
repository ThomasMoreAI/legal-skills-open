# Cross-cutting context: the Indian legal system

Orchestrator cold-start for any plugin under `in/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Common law tradition (post-British) with substantial codification. Federal republic (`Union of
India`) — Union (central) government, 28 states, and 8 union territories. Legislative
competence is allocated by the Seventh Schedule (Union List, State List, Concurrent List).

## Sources of law (by priority)

1. The Constitution of India (1950, as amended) — supreme; fundamental rights enforceable
   directly under Arts. 32 and 226.
2. International treaties — require parliamentary transformation for domestic effect.
3. Central (Union) laws — Acts of Parliament.
4. State laws — Acts of State Legislatures.
5. Subordinate legislation — Rules, Regulations, Notifications, and Orders issued under
   enabling Acts.
6. Case law — binding precedent: Supreme Court decisions bind all courts (Art. 141); High
   Court decisions bind subordinate courts within their territorial jurisdiction.

## Language

Statutes and court records are in English at the central level; regional languages apply
in some state work. The Supreme Court and most High Courts operate primarily in English.

## Citation discipline (mandatory for every plugin under `in/`)

- Statutes: "Section X of the [Name of Act], YEAR" — e.g., "Section 197 of the Code of
  Criminal Procedure, 1973".
- Constitution: "Article X of the Constitution of India".
- Cases: Supreme Court — "(YEAR) VOL SCC PAGE" or "AIR YEAR SC PAGE"; High Courts — give
  the court name and reporter.
- **Never invent** statute names, section numbers, or case citations. If unknown, say so
  explicitly and prompt the user to verify.

## Working with current law

Indian statutes are amended frequently (often by parallel `Amendment Acts`). Skills
depending on a specific rule must state the assumed version/date and warn the user that
recent amendments may change the answer.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
