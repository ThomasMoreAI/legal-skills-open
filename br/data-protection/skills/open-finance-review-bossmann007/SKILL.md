---
name: open-finance-review-bossmann007
title: Open Finance Brasil Compliance Review
description: Revisão de conformidade Open Finance Brasil — Resolução BCB 32/2020, consentimento explícito, compartilhamento de dados, interplay com LGPD (Lei 13.709/2018), direito de acesso e portabilidade.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/banking-fintech-legal/skills/open-finance-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: en
---

# Open Finance Brasil Compliance Review

## Matter context

Open Finance Brasil (Sistema Financeiro Aberto) requires participating institutions to share customer financial data via API with explicit consent. This skill reviews your proposed or existing Open Finance setup against Resolução BCB 32/2020 and the LGPD. It focuses on the legal/compliance requirements, not the technical API spec.

Read `## Organization profile` in `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md` first to see if you've recorded your Open Finance participation scope.

---

## Purpose

Resolução BCB 32/2020 (and subsequent amendments) establishes Open Finance rules for banks, payment institutions, and fintech platforms in Brazil. Participating institutions must:
- Identify what customer data they hold that falls under Open Finance scope
- Obtain explicit customer consent to share that data
- Provide APIs for authorized recipients to access that data
- Comply with LGPD when sharing personal data

The consent model is **critical**: Open Finance requires affirmative, revocable consent per data recipient and category. Implicit consent, bundled consent, or "consent once, share forever" violate the Resolução. This skill flags common consent gaps and LGPD compliance issues.

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

- **Resolução Conjunta CMN/BCB nº 1/2020** dispõe sobre a implementação do Open Finance por instituições financeiras, de pagamento e demais autorizadas pelo BCB; a **Resolução BCB nº 32/2020** trata da estrutura responsável pela governança do processo de implementação (não é um "Programa de Segurança Financeira") `[verified: https://normativos.bcb.gov.br/Lists/Normativos/Attachments/51028/Res_Conj_0001_v4_P.pdf]`
- **Lei 13.709/2018 (LGPD)** — Lei Geral de Proteção de Dados — governs personal data sharing; LGPD rights (acesso, portabilidade, retificação) interplay with Open Finance disclosure `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]`
- **Banco Central guidance documents** (BCB.gov.br/openbanking) elaborate on phased implementation timeline and technical standards `[unverified: not found in primary source]`

---

## Load the playbook

Read `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md` → `## Playbook` → `### Payment Systems and Open Finance`. Your playbook should record:
- **Open Finance participation status:** Yes (with scope) / No / Planned
- **Data categories you share:** accounts, transactions, credit products, other
- **Consent model you use:** explicit vs. implicit (should always be explicit)
- **LGPD intersection:** how you structure the DPA with recipients

If blank, I'll flag what you need to decide.

---

## Analysis

### 1. Scope — which data is Open Finance data?

Resolução BCB 32/2020 defines Open Finance scope (data customers can request to be shared) `[unverified: not found in primary source]`:

- **Accounts data:** account type, balance, limits, status
- **Transaction data:** historical transactions, payment records
- **Credit data:** credit products (loans, credit lines), terms, balance
- **Investment data** (if applicable): investment accounts, holdings, transactions
- **Other:** insurance products, exchange rates, etc. — depending on your product mix

**Your institution's scope:** What data do you hold that falls under Open Finance? List the categories. If you don't hold accounts (e.g., you're a pure lending platform), Open Finance scope may be narrower or zero.

**Action:** Confirm with your playbook which categories you participate in. If your playbook says "we don't participate," skip to "What this skill does not do."

### 2. Consent model — explicit and revocable

**Resolução BCB 32/2020 requirement** `[unverified: not found in primary source]`: Consent must be **explicit** and **per recipient and data category**. 

This means:
- ✓ Customer logs in, sees list of authorized recipients (banks, fintech, mortgage companies), checks boxes for which ones can access their data, and confirms
- ✗ One "I agree to share my data" button that grants all access forever
- ✗ Consent bundled with T&Cs (buried, not affirmative)
- ✓ Customer can revoke access to any recipient at any time via simple dashboard
- ✗ Revocation requires phone call or email to support

**Your consent flow:** Describe (or share a screenshot of) your consent collection. I'll flag if it:
- Lumps multiple recipients or data categories into one button
- Lacks a clear revocation mechanism
- Uses implicit consent (e.g., "we'll share unless you opt out")
- Combines Open Finance consent with other consents (possible if clearly separated, but risky)

### 3. LGPD intersection — personal data, controller/processor, DPA

Open Finance data is personal data under LGPD (Lei 13.709/2018). When you share customer data with a recipient (fintech, another bank), you must:

- **Establish controller/processor roles (Art. 5º LGPD):** Are you the controller (you decide what data to collect and how to share it)? Is the recipient also a controller (they decide to use the data)? Both are typically controllers for their own purposes.
- **Have a DPA (Art. 33 LGPD) if the recipient is a processor:** Not typically the case in Open Finance (recipients are usually controllers too), but flag if unclear.
- **Include LGPD scope in your consent:** Customers must know they're sharing "personal data per LGPD" — not just "financial data." `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]`
- **Provide LGPD rights:** Customers have the right to access (Art. 18 LGPD), correct (Art. 19), delete (Art. 17, with exceptions for contractual obligations), port their data (Art. 20) — these rights exist independently of Open Finance consent.

**Your LGPD compliance:** Do your Open Finance terms explain LGPD rights? Do you have mechanisms to honor data access and portability requests? This is separate from Open Finance, but failures here are failures in both regimes.

### 4. No silent supplement

If your playbook doesn't yet address Open Finance participation (you haven't decided whether to offer data sharing), I'll flag and ask: "Your playbook doesn't record an Open Finance participation decision. Options: (1) you plan to participate — tell me scope and I'll structure the compliance checklist; (2) you don't plan to participate — I'll verify no gaps; (3) decision pending — I'll flag as TBD." Do not proceed with compliance design without a decision on participation.

---

## Consequential-action gate

**Before launching an Open Finance data-sharing flow or collecting first customer consent:**

Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/banking-fintech-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Open Finance consent collection and data sharing is a LGPD-regulated activity. Consent flows, data-sharing agreements, and recipient onboarding affect your compliance posture and customer privacy rights. This should be reviewed with an attorney before go-live. Have you discussed your Open Finance implementation plan with legal counsel?
>
> If yes, proceed. If no, here's what to bring to them:
>
> - Scope: which data categories you plan to share
> - Consent flow: how you collect and manage consent (wireframe or description)
> - Recipients: list of institutions/fintech you plan to onboard
> - LGPD terms: how you communicate LGPD rights to customers
> - Revocation: how customers opt out or revoke individual recipient access
>
> (If you need a lawyer: OAB Brasil by estado; search "especialista em direito de dados" or "especialista em fintech".)

Do not launch without legal sign-off.

---

## What this skill does not do

- **Does not validate API specs.** Open Finance requires specific API standards (Swagger/OpenAPI, rate limiting, security headers, etc.). A developer/architect reviews that; this skill reviews compliance only.
- **Does not draft data-sharing agreements.** Formal agreements between you and recipients (DPA if processor role, or terms of data access) are outside scope; a lawyer drafts those.
- **Does not audit your LGPD program.** Full LGPD compliance (DIA, privacy-by-design, Data Protection Officer, etc.) is a separate engagement; this skill focuses on Open Finance + LGPD intersection.
- **Does not cover CVM-regulated data** (securities, investment funds). If you share investment product data, CVM rules may also apply — separate review.
- **Does not cover phased implementation timeline.** BCB has staged Open Finance rollout (phases 1-4) with different institution categories eligible in each phase. Check BCB.gov.br/openbanking for which phase you're in; this skill assumes you're participating.

---

*For BCB guidance: www.bcb.gov.br/en/OpenBanking. For LGPD detail: www.gov.br/cidadania/pt-br/acesso-a-informacao/lgpd.*
