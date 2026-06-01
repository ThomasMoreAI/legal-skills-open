# Cross-cutting context: the Taiwanese legal system

Orchestrator cold-start for any plugin under `tw/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law (German- and Japanese-influenced) under the ROC Constitution. The Supreme Court is the apex court for ordinary matters; the Constitutional Court conducts constitutional review.

## Sources of law (by priority)

1. The ROC Constitution and Constitutional Court (Judicial Yuan) interpretations/judgments.
2. Statutes enacted by the Legislative Yuan.
3. Regulations and orders.
4. Case law of the Supreme Court and Supreme Administrative Court — persuasive.

## Codes

Core codes: Civil Code, Criminal Code, Code of Civil Procedure, Company Act.

## Language

Statutes, decisions, and official documents are in (Traditional) Chinese.

## Citation discipline (mandatory for every plugin under `tw/`)

- Statutes/codes: "Article 184 of the Civil Code".
- Cases: by year and case number of the issuing court.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
