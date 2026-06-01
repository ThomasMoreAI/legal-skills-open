# Cross-cutting context: the Ukrainian legal system

Orchestrator cold-start for any plugin under `ua/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Civil law; the 1996 Constitution is supreme. Unitary state; ongoing harmonisation with EU law under the Association Agreement.

## Sources of law (by priority)

1. The Constitution and Constitutional Court jurisprudence.
2. Ratified international treaties.
3. Codes and statutes (zakony) of the Verkhovna Rada.
4. Acts of the President and Cabinet of Ministers; regulatory acts.
5. Case law of the Supreme Court — conclusions on application of law have binding effect.

## Codes

Core codes: Civil Code (2003), Commercial Code, Civil Procedure Code, Criminal Code.

## Language

Statutes, decisions, and official documents are in Ukrainian. Court fees: судовий збір.

## Citation discipline (mandatory for every plugin under `ua/`)

- Statutes/codes: "Article 16 of the Civil Code of Ukraine".
- Supreme Court: by case number (e.g. "No. 910/1234/20").
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
