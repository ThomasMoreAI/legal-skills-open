---
name: credit-contract-review-bossmann007
title: Credit Contract Review
description: Revisão de contrato bancário/crédito — juros, CET (Custo Efetivo Total), capitalização, tarifas, crédito consignado, CDC (Lei 8.078/1990), súmulas STJ sobre revisão de contratos bancários.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/banking-fintech-legal/skills/credit-contract-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: finance
language: pt
---

# Credit Contract Review

## Matter context

Read `## Playbook` → `### Banking / Credit Products` in `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md` first. This skill applies your team's positions on interest rates, CET disclosure, fee caps, and capitalization to a proposed or executed credit contract (loan, financing, credit line, etc.).

---

## Purpose

Brazilian banking contracts (empréstimo, financiamento, crédito pessoal) are subject to overlapping regimes: the Código Civil (Arts. 421-480 — general contract law), the CDC (Lei 8.078/1990 — consumer protection, when the borrower is a consumer), and specific Resolutions of the BCB for particular products. The most litigated issues are: **usury (vedada, but hard to define), CET disclosure, capitalization of interest, and abusive fees.**

This skill reviews a contract against your playbook positions and flags deviations, ambiguities, and known STJ precedent issues. It does not render a legal opinion; a lawyer makes the call on whether a deviation is acceptable.

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

- **Código Civil (Lei 10.406/2002)** — general contract law, Arts. 421-480 (contratos em geral); arts. 591-592 on loan (empréstimo/mútuo), with services/empreitada in the following provisions rather than "financing" as a single block. `[verified: https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm]`
- **CDC (Lei 8.078/1990)** — consumer protection law; applies when borrower is a consumer (destinatário final, Art. 2º); makes many contract terms abusive/void (Art. 51) `[verified: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm]`
- **Lei de Usura (Decreto 22.626/1933)** — antediluvian usury law; its rules do not apply to rates/charges in operations by institutions in the national financial system under STF Súmula 596. `[verified: https://www.planalto.gov.br/ccivil_03/decreto/d22626.htm; https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=30&sumula=2017]`
- **BCB Resolutions** — specific rules for crédito consignado (CCB), financiamento imobiliário, etc. `[unverified: not found in primary source]`
- **STJ precedent** — Súmulas and jurisprudence on capitalized interest, CET disclosure, abusive fees `[verified: https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias-antigas/2017/2017-02-09_18-51_Previsao-contratual-e-exigida-para-capitalizacao-de-juros-em-qualquer-periodicidade.aspx]`

---

## Load the playbook

Read `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md` → `## Playbook` → `### Banking / Credit Products`. Your playbook should record:
- **Interest cap policy:** e.g., "CET capped at 150% of BCB média de mercado for the product"
- **CET disclosure requirement:** Yes (mandatory) / No (certain products exempt)
- **Capitalization of interest:** Prohibited for consumers / Permitted for corporate with disclosure
- **Fee ceiling:** e.g., "Admin fee ≤ 1% of principal; processing fee ≤ R$ 200"
- **Termination and prepayment rights:** consumer right to prepay without penalty?

If blank, proceed with analysis and flag where the playbook needs clarification.

---

## Analysis

### 1. Borrower classification — consumer or not?

**CDC definition (Art. 2º):** A consumer is a person (physical or legal) who acquires or uses a product/service as a final user (destinatário final), not for resale or professional use.

- **Consumer:** Individual borrowing for personal use (car financing, credit card, personal loan)
- **Corporate:** Company borrowing for business use (working capital, expansion, equipment) — CDC may not apply if the company is clearly a professional buyer
- **Ambiguous:** A small business (microempreendedor) borrowing for personal/business overlap — increasingly treated as consumer-like under STJ recent precedent `[unverified: not found in primary source]`

**Action:** Confirm with the playbook: are you lending to consumers? If yes, CDC rules apply **cogently** (non-waivable). Many contract terms borrowers might accept are void per CDC Art. 51 (abusive clauses).

### 2. Interest rate and usury (a mess)

**The legal mess:** Brazil has no statutory usury cap (unlike many jurisdictions with fixed %). Lei de Usura caps are technically ~12% p.a. but haven't been enforced in decades. What remains are:

- **STJ precedent on "abusive interest":** Súmula 382/STJ — "A estipulação de juros remuneratórios superiores a 12% ao ano, por si só, não indica abusividade" `[settled — 2026-07-03]` (verificado contra STJ AtoM / arquivocidadao.stj.jus.br: no per se abuse over 12%; excessiveness analyzed case-by-case vs. taxa média de mercado). Instituições financeiras não se sujeitam à Lei de Usura (Súmula 596/STF) `[verified: https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=30&sumula=2017]`
- **CDC + consumer = risk:** For consumer credit, excessively high interest can be challenged as "abusive" (Art. 51 CDC) even if not per se usury

**Your policy:** Check the playbook. What's your interest rate ceiling? Common approaches:
- e.g., "Taxa média de mercado from BCB Estatísticas + [spread]" (observable, defensible)
- e.g., "150% of prime rate" (tied to a reference)
- e.g., "CET ≤ 60% p.a. for crédito consignado" (specific product cap)

**Red flags in the contract:**
- Interest rate way above market (defensible only if borrower is high-risk and corporate)
- No CET disclosed (if required)
- Interest rate adjustable without limit ("ao critério do credor" is classic abusive language)
- Capitalization of unpaid interest on top of interest (compounds the rate)

### 3. CET (Custo Efetivo Total) disclosure

**BCB requirement** `[unverified: not found in primary source]`: For many credit products, the lender must disclose CET (the true all-in annual percentage rate, including all fees and charges). This is **mandatory**, **in writing**, **before** the borrower signs. Failure to disclose is a BC violation and makes the contract challengeable.

**What's CET:** It includes:
- Base interest rate
- Admin fees
- Processing fees
- Insurance (if bundled)
- Registration fees
- All other costs the borrower bears

**What's CET not:** Taxes (CPMF, if any), notary costs, appraisal fees for real estate (sometimes excluded depending on product).

**Contract language to check:**
- ✓ "CET: [percentage] p.a." clearly stated
- ✓ Breakout of what's included in CET
- ✓ Comparison: "Juros: [X]%; CET: [Y]%" to show the difference
- ✗ CET buried in footnotes or not disclosed
- ✗ CET omitted because "not required" (probably wrong; check BCB rules for your product)

### 4. Capitalization of interest

**For consumers (CDC):** Capitalization (compound interest) is prohibited except:
- Capitalização de juros com periodicidade inferior à anual é permitida em contratos com instituições do Sistema Financeiro Nacional celebrados a partir de 31/3/2000 (MP 1.963-17/2000, reeditada como MP 2.170-36/2001), **desde que expressamente pactuada** — Súmula 539/STJ `[settled — 2026-07-03]` (verificado contra STJ AtoM). A capitalização exige previsão contratual expressa em qualquer periodicidade (Tema 953/STJ) `[verified: https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias-antigas/2017/2017-02-09_18-51_Previsao-contratual-e-exigida-para-capitalizacao-de-juros-em-qualquer-periodicidade.aspx]`
- Interest on unpaid installments, calculated per period (not compound on compound) — the law is murky here and subject to STJ debate `[unverified: not found in primary source]`

**For corporates:** Capitalization is usually allowed, but must be transparent.

**Red flags:**
- Contract says "juros capitalizados mensalmente" without specifying scope (looks like compound compound)
- Penalty interest capitalized on top of regular interest
- Monthly rolling compound leading to exponential growth

### 5. Fees and charges

**CDC constraint (Art. 51):** "Abusive" fee clauses can be voided. What's abusive?
- Undisclosed fees
- Fees that are unreasonably high relative to the lender's cost or market
- Fees imposed outside the original terms (e.g., "we now charge a monthly admin fee, retroactively")

**Common fee traps:**
- Admin fee: Often 0.5–2% of principal. Defensible if disclosed and market-normal.
- Processing fee: Fixed or percentage. Per-se reasonable if ≤ cost to process.
- Mortgage registration fee / Title insurance: Often bundled; should be separate and itemized if consumer borrowing.
- Early payment penalty: Many contracts charge a "fine" if you repay early to recoup lost interest. STJ has oscillated on this — currently seems to allow it for corporate but not consumer. Flag this specifically. `[unverified: not found in primary source]`

**Your playbook check:** What's your fee ceiling? E.g., "Admin fee max 1.5% of principal", "No prepayment penalty for consumers"?

### 6. Crédito consignado (salary-deducted loans)

**Special rules apply** `[unverified: not found in primary source]`:
- CCB (Cédula de Crédito Bancário) is the instrument; specific BCB resolution governs terms
- Borrower consent + employer consent required
- Interest cap: Often lower than unsecured lending (because guaranteed by salary deduction)
- Pre-signing consent requirements: Written acknowledgment of terms before signing

**If the contract is consignado:**
- Verify consent documentation (employer + borrower)
- Check interest is within consignado parameters (usually lower than unsecured)
- Confirm T&Cs include mandatory disclosures specific to consignado products

### 7. No silent supplement

If a critical term in the contract conflicts with your playbook and the playbook is blank (`[PLACEHOLDER]`), I'll flag and ask: "Your playbook doesn't record a position on [interest caps / prepayment penalties / capitalization / other]. Options: (1) tell me your policy and I'll flag deviations; (2) defer and I'll flag this item as pending playbook guidance." Do not execute a contract without clarity on your limits.

---

## Consequential-action gate

**Before executing a credit contract that deviates from your playbook or uses terms you haven't vetted:**

Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Executing a credit contract that carries nonstandard terms (high interest, no CET disclosure, capitalized interest, prepayment penalties) has legal risk — the borrower can challenge it, and if the borrower is a consumer, CDC rules may void the term. This should be reviewed with an attorney. Have you discussed this contract's terms with legal counsel?
>
> If yes, proceed. If no, here's what to bring:
>
> - Who is the borrower: consumer (individual) or corporate?
> - Interest rate: what % and how does it compare to market/your policy?
> - CET: is it disclosed, and how?
> - Fees: list each fee and the amount/percentage.
> - Capitalization: is interest compounded? On what schedule?
> - Special provisions: prepayment penalties, adjustment clauses, security interest?
> - Deviation: how does this contract differ from your standard terms?
>
> (If you need a lawyer: OAB Brasil by estado; search "especialista em direito bancário" or "direito do consumidor".)

Do not execute without legal sign-off.

---

## What this skill does not do

- **Does not audit compliance for an ongoing loan portfolio.** Portfolio review/remediation is a separate engagement.
- **Does not calculate true CET.** CET calculation requires product-specific formulas and a calculator; this skill reviews disclosure, not math.
- **Does not advise on real estate financing-specific rules.** Financiamento imobiliário (CEF, Caixa, construtoras) has specialized BCB rules outside this skill.
- **Does not cover cross-border or foreign borrowers.** Additional complications (exchange risk, remittance tax, foreign credit bureau) exist but are not analyzed here.
- **Does not produce a compliance audit.** This skill reviews one contract against your playbook; an audit reviews all active contracts and systems.

---

*For STJ case law: search JusBrasil or Escavador for "Súmula STJ" + keyword (e.g., "juros" "capitalização"). For BCB rules: www.bcb.gov.br → Regulação → Crédito.*
