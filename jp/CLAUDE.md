# Cross-cutting context: the Japanese legal system

Orchestrator cold-start for any plugin under `jp/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law (German- and French-influenced) under the 1947 Constitution. Unitary state; the Supreme Court of Japan is the apex court and exercises constitutional review.

## Sources of law (by priority)

1. The Constitution of Japan and Supreme Court jurisprudence.
2. Treaties.
3. Statutes enacted by the Diet (hōritsu).
4. Cabinet orders and ministerial ordinances.
5. Case law of the Supreme Court — highly persuasive.

## Codes

Core codes: Civil Code (Minpō), Commercial Code (Shōhō), Companies Act, Penal Code, Code of Civil Procedure.

## Language

Statutes, decisions, and official documents are in Japanese.

## Citation discipline (mandatory for every plugin under `jp/`)

- Statutes/codes: "Article 709 of the Civil Code".
- Supreme Court: by date and official reporter (e.g. Minshū vol./no.).
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
