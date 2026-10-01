---
name: payment-institution-compliance-bossmann007
title: Payment Institution Compliance Review
description: Análise de conformidade — Lei 12.865/2013 (instituição de pagamento e arranjo de pagamento), Resoluções do BCB, Pix, verificação de exigências regulatórias por tipo de arranjo. Classifica sua operação e lista gaps conhecidos.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/banking-fintech-legal/skills/payment-institution-compliance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: en
---

# Payment Institution Compliance Review

## Matter context

Read `## Organization profile` in `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md` first. This skill applies the institution classification rules from your playbook to your current operation or a proposed product. It does not read external documents (no PJe, no automated regulator feed); you provide the details — product description, intended customer base, settlement infrastructure — and this skill triages compliance requirements.

---

## Purpose

Brazil's Lei 12.865/2013 (Lei das Instituições de Pagamento) distinguishes two types of payment entities: **Instituição de Pagamento** (regulated bank-like entity, requires BCB registration, capital, governance) and **Arranjo de Pagamento** (looser framework for specific payment systems, e.g., Pix participants, simple e-wallet operators). The line between them is **material** — it determines whether you need BCB license, how much capital you must hold, what infrastructure and governance apply, and which compliance burden lands on you. This skill classifies your operation against the statute and Banco Central regulations, flags any gaps, and stops short of saying "you must do this" — a lawyer decides.

It runs against your playbook positions from `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md` and flags any deviation or unclear rule.

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

Lei das Instituições de Pagamento (Lei 12.865/2013) governs payment institutions and payment arrangements in Brazil. Regulated by Banco Central do Brasil (BCB). Key statutes and resolutions `[verified: https://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2013/Lei/l12865.htm]`:

- **Lei 12.865/2013** — defines Instituição de Pagamento and Arranjo de Pagamento in Art. 6º; Art. 7º sets principles for payment arrangements and institutions. `[verified: https://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2013/Lei/l12865.htm]`
- **Resolução CMN 4.658/2018** (and updates) — política de segurança cibernética e requisitos para contratação de processamento/armazenamento de dados e computação em nuvem, observada pelas instituições autorizadas a funcionar pelo BCB (é resolução do CMN, não "Resolução BCB") `[verified: https://normativos.bcb.gov.br/Lists/Normativos/Attachments/50581/Res_4658_v1_O.pdf]`
- **Open Finance** — o marco de implementação é a **Resolução Conjunta CMN/BCB nº 1/2020**; a **Resolução BCB nº 32/2020** trata da estrutura responsável pela governança do processo de implementação `[verified: https://normativos.bcb.gov.br/Lists/Normativos/Attachments/51028/Res_Conj_0001_v4_P.pdf]`
- **Pix Resolution** — BCB rules for Pix participants, settlement on D+0 `[unverified: not found in primary source]`

---

## Load the playbook

Read `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md` → `## Playbook` → `### Payment Systems and Open Finance`. This section records your team's positions on:
- Whether you are or intend to be an Instituição de Pagamento or Arranjo de Pagamento
- Classification decision you've already made (if any)
- Pix participation scope (if applicable)

If the section is blank (`[PLACEHOLDER]`), proceed with the analysis and note that your playbook doesn't yet record this decision — you'll need to fill it in after you decide.

---

## Analysis

### 1. Institutional classification — Instituição vs. Arranjo

**Lei 12.865/2013 definitions** `[verified: https://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2013/Lei/l12865.htm]`:

- **Instituição de Pagamento (Art. 6º):** A legal entity (not a bank or payment bank) that, as its core business, receives funds from payers and makes them available to payees through payment arrangements. Typically requires BCB authorization, minimum capital, governance board, compliance officer, risk management, and annual financial reporting.

- **Arranjo de Pagamento (Art. 6º):** A set of rules and procedures that disciplines the provision of a payment service to the public accepted by more than one recipient, by direct access by final users, payers and recipients. Art. 7º sets principles for arrangements and institutions rather than defining the term.

**Your classification:**

Based on the description you provided, does your operation:

- (A) Receive funds from customers and make them available to recipients as your core business? → likely **Instituição de Pagamento**, requires BCB licensing.
- (B) Operate a payment system that participants access (customers send through your system, but may use other backends)? → likely **Arranjo de Pagamento**, licensing depends on what role you play in the system.
- (C) Provide ancillary services (e.g., account holding, KYC, but settlement is through another licensed entity)? → May fall outside Lei 12.865 scope or be part of an existing Arranjo.

**Action:** If your playbook records a classification decision, I'll compare your operation against it and flag any changes. If your playbook is blank, I'll note the classification needed and ask you to confirm it with a lawyer before proceeding with the compliance checklist.

### 2. Regulatory requirements by type

If **Instituição de Pagamento:**
- BCB authorization required (process can take 6-12 months) `[unverified: not found in primary source]`
- Minimum capital: [check current BCB requirement; last known was R$ 2M for some categories] `[unverified: not found in primary source]`
- Governance: Board, Audit Committee, Risk Committee (size depending on capital tier) `[unverified: not found in primary source]`
- Chief Compliance Officer and independent risk management `[unverified: not found in primary source]`
- Annual financial reporting to BCB, including prudential ratios `[unverified: not found in primary source]`
- Segregated customer funds (Conta de Depósitos Judiciais or equivalent) `[unverified: not found in primary source]`

If **Arranjo de Pagamento:**
- Classification and notification to BCB (less formal than Instituição authorization) `[unverified: not found in primary source]`
- If you own the Arranjo: governance and compliance rules, but often lighter than Instituição
- If you participate in an existing Arranjo (e.g., Pix): adherence to that Arranjo's operational rules

### 3. Open Finance (if applicable)

If you handle customer financial data (accounts, transactions, credit), you may be subject to Resolução BCB 32/2020 (Open Finance Brasil). This requires:
- Data sharing with customer consent `[unverified: not found in primary source]`
- API compliance with BCB standard (not your choice of format) `[unverified: not found in primary source]`
- Explicit customer consent model (not implicit) `[unverified: not found in primary source]`
- LGPD-compliant Data Processing Agreement with recipients `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]`

Check your playbook (`## Playbook` → `### Payment Systems and Open Finance` → `**Open Finance participation**`). If you're not Open Finance-eligible (e.g., you don't hold customer accounts), skip this.

### 4. AML/PLD (if handling customer funds)

Any entity accepting customer funds must comply with Lei 9.613/1998 (Lei de Prevenção à Lavagem de Dinheiro — AML/PLD law):
- Know Your Customer (KYC) — identity verification, beneficial ownership, source of funds `[verified: https://www.planalto.gov.br/ccivil_03/LEIS/L9613compilado.htm]`
- Customer Due Diligence (CDD) — ongoing transaction monitoring `[verified: https://www.planalto.gov.br/ccivil_03/LEIS/L9613compilado.htm]`
- Suspicious Activity Reporting (SAR) to COAF (Conselho de Controle de Atividades Financeiras) `[verified: https://www.planalto.gov.br/ccivil_03/LEIS/L9613compilado.htm]`

Your playbook should record your AML/PLD posture. If blank, this will be a standard requirement regardless.

---

## No silent supplement

If your playbook doesn't address a classification question (you haven't decided if you're pursuing Instituição or Arranjo status, or the decision is conditional on a regulatory change), I'll flag it and stop. Say: "The playbook doesn't yet record a classification decision for [your product]. Options: (1) tell me which path you're pursuing, and I'll structure the compliance checklist for that path; (2) defer and I'll flag this as a blocker to proceed." A lawyer makes the classification call, not this skill.

---

## Consequential-action gate

**Before making or announcing a VASP, Instituição, or Arranjo classification decision that affects company legal standing:**

Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Registering with or notifying the Banco Central that you are an Instituição de Pagamento or operating an Arranjo de Pagamento is a material regulatory decision. It commits the company to ongoing compliance, capital requirements, reporting, and governance rules. This decision should be reviewed with an attorney. Have you discussed this classification with your legal counsel? If yes, proceed. If no, here's what to bring to them:
>
> - Your business model: how do you handle customer funds?
> - The two paths (Instituição vs. Arranjo) and which one fits your model
> - What BCB licensing or notification process you'd enter
> - What compliance and governance burden applies to each path
> - Whether you're already in a licensed Instituição (e.g., you're a division of a bank) or standalone
>
> Classification decision: [classification you propose to pursue]
>
> (If you need a lawyer: OAB Brasil by estado; search "especialista em direito bancário" or contact the Ordem by region.)

Do not proceed to registration or regulatory notification without an explicit yes.

---

## What this skill does not do

- **Does not advise on CVM jurisdiction** (if your product touches securities, equity, or investment funds, CVM may also regulate you — separate framework)
- **Does not review your actual compliance infrastructure** (governance documents, policies, controls) — see `/banking-fintech-legal:compliance-audit` if that skill exists, or contract for a full compliance audit
- **Does not draft registration applications** — this skill triages classification and requirements; a lawyer and a regulatory consultant draft the BCB filing
- **Does not cover all BCB resolutions** — focuses on Lei 12.865/2013 and core Pix/Open Finance rules; many specialized resolutions apply to specific products (e.g., credit-specific rules, cross-border rules)
- **Does not interpret your specific business model** — you provide the description; I classify against the statute; you confirm with a lawyer

---

*For detailed BCB guidance, consult: Banco Central do Brasil (www.bcb.gov.br) → Pagamentos → Instituições de Pagamento; or obtain regulatory counsel in Brasil.*
