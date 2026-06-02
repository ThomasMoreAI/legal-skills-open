# Cross-cutting context: the Finnish legal system

Orchestrator cold-start for any plugin under `fi/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law of the Nordic family; less consolidated codification than continental systems. The Constitution of Finland is supreme.

## Sources of law (by priority)

1. The Constitution of Finland.
2. International treaties and EU law (primacy under CJEU jurisprudence).
3. Acts of Parliament (laki/lag).
4. Decrees (asetus).
5. Case law of the Supreme Court (KKO) and Supreme Administrative Court (KHO) — guiding.

## Language

Statutes and decisions are published in Finnish and Swedish (both official).

## Citation discipline (mandatory for every plugin under `fi/`)

- Statutes: by name and statute number in the Statute Book (e.g. "(SDK 39/1889)").
- Supreme Court precedents: "KKO:2018:1"; Supreme Administrative Court: "KHO:2018:1".
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
