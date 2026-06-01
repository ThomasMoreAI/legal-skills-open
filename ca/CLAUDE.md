# Cross-cutting context: the Canadian legal system

Orchestrator cold-start for any plugin under `ca/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Bijural federation: common law in nine provinces and the territories, civil law in Québec (Civil Code of Québec). The Constitution (incl. the Charter) is supreme; binding precedent. The Supreme Court of Canada is the apex court.

## Sources of law (by priority)

1. The Constitution Acts 1867–1982 and the Canadian Charter of Rights and Freedoms.
2. Federal statutes and provincial/territorial statutes (per the division of powers).
3. Regulations.
4. Case law of the Supreme Court of Canada (binding precedent); in Québec, the Civil Code.

## Codes

Québec is governed by the Civil Code of Québec (CCQ); the rest of Canada follows common law.

## Language

Federal legislation and Supreme Court decisions are bilingual (English and French).

## Citation discipline (mandatory for every plugin under `ca/`)

- Statutes: "s 7 of the Charter"; "art. 1457 CCQ" (Québec).
- Cases: "R v Oakes, [1986] 1 SCR 103"; neutral "2020 SCC 1". Follow the McGill Guide.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
