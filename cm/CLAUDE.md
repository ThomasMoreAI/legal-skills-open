# Cross-cutting context: the Cameroonian legal system

Orchestrator cold-start for any plugin under `cm/`. Loaded before the plugin-specific `CLAUDE.md`.

## Legal family

Bijural system: civil law (French-influenced) in the Francophone regions and English common law in the Anglophone North-West and South-West regions. OHADA uniform law governs business/commercial matters across the country. The Supreme Court is the apex court.

## Sources of law (by priority)

1. The Constitution.
2. OHADA Uniform Acts (directly applicable for commercial, company, security, and insolvency law) and other ratified treaties.
3. Statutes (lois) and ordinances.
4. Regulations (décrets, arrêtés).
5. Case law of the Supreme Court and, for OHADA matters, the CCJA (Common Court of Justice and Arbitration).

## Codes

Business law is governed by the OHADA Uniform Acts; civil and criminal matters by the applicable codes/received common law depending on region.

## Language

Both French and English are official; legislation is published in both.

## Citation discipline (mandatory for every plugin under `cm/`)

- OHADA: cite the relevant Uniform Act and article (e.g. "art. [N], Uniform Act on General Commercial Law").
- Statutes: "Law No. [N] of [year]", article number.
- **Never invent** article numbers, case names, or court references. If unknown, say so
  and prompt the user to verify.

## Working with current law

Statutes and codes are amended frequently. A skill that depends on a specific rule must
state the assumed version/date and warn the user to confirm it is current.

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute/regulation and the rules of the specific court or agency before relying on it.
