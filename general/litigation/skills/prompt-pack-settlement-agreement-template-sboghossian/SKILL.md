---
name: prompt-pack-settlement-agreement-template-sboghossian
title: Settlement Agreement Template
description: Use when a law firm or legal team needs a reusable settlement agreement template with bracketed placeholders for repeated use across multiple matters. Produces a fully structured template with representations, mutual releases, confidentiality, non-disparagement, and dismissal mechanics, ready to be populated for specific disputes. Distinguish from prompt-pack-settlement-agreement, which targets a specific dispute; this skill produces the reusable master template.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-settlement-agreement-template
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Settlement Agreement Template

## When to use this

Use this skill when:
- A law firm or in-house legal team needs a **reusable master template** for settlement agreements across multiple matters or clients.
- A legal operations function is building a document library and needs a jurisdiction-tested template.
- A GC wants to standardize how commercial disputes are settled, with pre-approved standard language and clearly marked negotiation variables.

**Relationship to settlement agreement skill:** [[prompt-pack-settlement-agreement]] drafts a settlement for a specific, identified dispute. This skill produces a template with `[BRACKETED VARIABLES]` to be filled in per matter. Use this skill first to build the template; use the other skill to generate a dispute-specific document.

## Template design principles

A good settlement agreement template must:
1. Be **jurisdiction-flexible** — include alternative clauses for different governing-law scenarios (civil-law vs. common-law; UAE vs. DIFC vs. KSA).
2. Be **modular** — clause blocks for optional provisions (installment payment, consent judgment, non-compete, ongoing relationship) that can be included or deleted.
3. Have **clear drafting notes** — editorial guidance within the template (in `{DRAFTING NOTE: ...}` format) so the lawyer populating it knows what to consider for each variable.
4. Be **lightly negotiated from the outset** — pro-settling-party defaults with known concession points identified.

## Document structure

The template follows the same structure as a matter-specific settlement agreement (see [[prompt-pack-settlement-agreement]]) but with:
- All party-specific information replaced by `[PARTY A]`, `[PARTY B]`.
- All monetary figures replaced by `[SETTLEMENT AMOUNT]`, `[INSTALLMENT AMOUNT]`, `[PAYMENT DATE]`.
- All dispute-specific references replaced by `[DESCRIPTION OF DISPUTE]`, `[CASE REFERENCE]`, `[COURT/TRIBUNAL]`.
- Alternative clause versions in brackets: `[OPTION 1: LUMP SUM PAYMENT] / [OPTION 2: INSTALLMENT PAYMENT]`.
- Jurisdiction-specific alternative clauses in separate boxes labeled by jurisdiction.

### Template clause sequence

1. **Cover information block**
   ```
   DATE: [DATE OF AGREEMENT]
   PARTY A: [FULL LEGAL NAME], a [entity type] incorporated in [jurisdiction], with registered address at [address] ("Party A")
   PARTY B: [FULL LEGAL NAME], a [entity type] incorporated in [jurisdiction], with registered address at [address] ("Party B")
   MATTER: [BRIEF DESCRIPTION OF DISPUTE]
   ```

2. **Recitals** — template with placeholders for dispute description and proceedings reference.

3. **Definitions block** — pre-defined: Settling Parties, Settlement Amount, Settlement Payment Date, Released Claims, Proceedings.

4. **Payment clause — three alternative modules:**

   *Module A — Lump sum:*
   ```
   [PARTY A] shall pay [PARTY B] the sum of [SETTLEMENT AMOUNT] in [CURRENCY] by bank transfer to [ACCOUNT DETAILS] by no later than [PAYMENT DATE].
   ```

   *Module B — Installments with consent judgment:*
   ```
   [PARTY A] shall pay [PARTY B] the Settlement Amount in [NUMBER] installments as follows:
   - Installment 1: [AMOUNT] by [DATE]
   - Installment 2: [AMOUNT] by [DATE]
   [...]
   If [PARTY A] fails to pay any installment within [5] Business Days of its due date, the full outstanding balance shall immediately become due and payable, and [PARTY B] shall be entitled to enter judgment against [PARTY A] for the outstanding balance without further proceedings.
   ```

   *Module C — Non-monetary settlement:*
   ```
   In full and final settlement, [PARTY A] shall [DESCRIBE NON-MONETARY OBLIGATION] by [DATE / within [X] days of this Agreement].
   ```

5. **Mutual release clause** — with three jurisdiction-specific variants:

   *Standard civil-law (UAE onshore / Lebanon / Egypt):*
   ```
   Each Party hereby releases and discharges the other Party from all claims, demands, actions, proceedings, liabilities, obligations, damages, costs, and expenses of any nature arising out of or in connection with [DESCRIPTION OF DISPUTE] (the "Released Claims"), including all claims that have been made or that could have been made in respect of the Released Claims.
   {DRAFTING NOTE: Under UAE Civil Transactions Law, a sulh release should identify the specific dispute with precision. A general release of "all claims ever" may be interpreted narrowly by UAE courts. Specify the dispute clearly.}
   ```

   *Standard common-law (DIFC / ADGM / UK / English law):*
   ```
   Each Party releases and forever discharges the other Party [...] from all claims [...] whether known or unknown as at the date of this Agreement, arising from or related to [DESCRIPTION OF DISPUTE].
   {DRAFTING NOTE: Include "known or unknown" language in common-law releases to capture latent claims. In civil-law systems, this language is less critical but harmless.}
   ```

6. **No admission clause** — standard; no jurisdiction variations needed.

7. **Confidentiality clause** — with permitted disclosure carve-outs:
   ```
   The existence and terms of this Agreement are confidential. Each Party agrees not to disclose the terms of this Agreement to any third party, except:
   (a) to legal, financial, or tax advisors who are bound by professional confidentiality;
   (b) as required by applicable law, regulation, or a competent governmental authority or court;
   (c) to enforce this Agreement.
   {DRAFTING NOTE: If either party is a listed company, securities law disclosure obligations may override this confidentiality provision. Verify with the client.}
   ```

8. **Non-disparagement clause** — optional module:
   ```
   {INCLUDE IF REQUESTED}
   Each Party agrees not to make, publish, or communicate any disparaging, defamatory, or negative statements or representations about the other Party, its directors, officers, employees, or products, whether orally, in writing, or online.
   Exception: truthful statements required by law or regulatory authority.
   ```

9. **Dismissal of proceedings** — conditional module:
   ```
   {INCLUDE IF PROCEEDINGS ARE PENDING}
   [PARTY A / CLAIMANT] undertakes to file a notice of discontinuance / consent order / withdrawal with the [COURT / TRIBUNAL / CASE REFERENCE] within [5] Business Days of [receipt of the Settlement Payment / execution of this Agreement].
   Both Parties will cooperate to give effect to the dismissal.
   ```

10. **Representations and warranties** — standard template; verify authority to enter.

11. **Governing law and dispute resolution** — alternative blocks:
    ```
    [OPTION 1 — UAE ONSHORE]
    This Agreement shall be governed by and construed in accordance with the laws of the United Arab Emirates. Any dispute arising from this Agreement shall be referred to the [Dubai Courts / Abu Dhabi Courts / relevant court].

    [OPTION 2 — DIFC]
    This Agreement shall be governed by DIFC law. Disputes shall be submitted to the exclusive jurisdiction of the DIFC Courts.

    [OPTION 3 — ARBITRATION]
    This Agreement shall be governed by [GOVERNING LAW]. Disputes shall be finally resolved by arbitration under the [ICC / DIAC / ADIAC / LCIA] Rules, with the seat in [CITY].
    ```

12. **Execution block** — signature lines for authorized signatories; witness lines (for jurisdictions where witnesses are required); date and place.

## Template maintenance notes

- **Review frequency:** This template should be reviewed annually and whenever a material change occurs in the governing law (UAE Civil Transactions Law, DIFC Contract Law, ADGM regulations).
- **Jurisdiction expansion:** Add jurisdiction-specific clause variants for Egypt (CRCICA seat) and Lebanon as needed.
- **Version control:** The template should carry a version number and last-reviewed date in the footer.

## Jurisdictional notes

See [[prompt-pack-settlement-agreement]] for full jurisdiction-specific notes on releases, confidentiality limitations, notarization, and language requirements. Those notes apply equally when populating this template.

Key jurisdiction-specific actions when populating the template:
- **UAE onshore:** select the sulh-specific release language; prepare Arabic bilingual execution copy; consider notarization for high-value amounts.
- **KSA:** execute in Arabic; consider notarization; be aware of confidentiality limitations.
- **DIFC/ADGM:** include "known and unknown claims" language; consider a consent order with the DIFC/ADGM Court.

## Drafting standards

- Template placeholders in `[CAPS AND BRACKETS]` are mandatory inputs.
- Template options in `{OPTION BLOCKS}` require a deliberate choice.
- Editorial notes in `{DRAFTING NOTE: ...}` are for the populating lawyer's eyes and must be deleted before the document is sent to the other party or executed.
- Do not include fictional example values in the published template — blank brackets only.

## Common mistakes

- **Template used without tailoring.** A settlement template is a starting point; the dispute-specific description in the release clause must always be tailored precisely. Generic templates with vague releases fail.
- **No instruction notes deleted.** Drafting notes left in the executed agreement embarrass counsel and create ambiguity.
- **Jurisdiction alternative clauses not resolved.** Templates with multiple `[OPTION 1 / OPTION 2]` blocks must have a single option selected before signature.

## Related skills

- [[prompt-pack-settlement-agreement]]
- [[prompt-pack-statement-of-claim]]
- [[prompt-pack-statement-of-defense]]
- [[heuristic-always-state-jurisdiction-first]]
