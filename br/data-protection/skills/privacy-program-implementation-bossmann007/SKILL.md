---
name: privacy-program-implementation-bossmann007
title: Privacy Program Implementation / LGPD Adequacy Plan
description: 'Implementação de Programa de Privacidade / Plano de Adequação à LGPD para empresa: mapeamento de dados, base legal por atividade, nomeação de Encarregado, RIPD, políticas, resposta a incidente, plano de adequação faseado.'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/privacy-legal/skills/privacy-program-implementation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Privacy Program Implementation / LGPD Adequacy Plan

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/privacy-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/privacy-legal/matters/<matter-slug>/`.

---

## Purpose

Implementar um programa de privacidade (ou "plano de adequação à LGPD") é estructurar como a empresa trata dados pessoais em conformidade com a Lei 13.709/2018. Este skill guia a empresa através de:

1. **Mapeamento de dados** — quais dados coleta, onde trata, com quem compartilha, por quanto tempo
2. **Base legal** — para cada finalidade de tratamento, qual é o artigo 7º (consentimento? legítimo interesse? contrato?) aplicável [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]
3. **Nomeação de Encarregado** — DPO/Encarregado de Proteção de Dados (Art. 41 LGPD [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
4. **Avaliação de Impacto (RIPD)** — em quais atividades (Art. 38 LGPD [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
5. **Políticas internas** — documento de conformidade documentando tudo acima
6. **Resposta a incidente** — plano de ação para possível vazamento (Art. 48 LGPD [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
7. **Plano faseado** — o que fazer agora vs. próximos 3/6/12 meses

## Jurisdiction assumption

**Premissa de jurisdição (Brasil):**

A LGPD (Lei 13.709/2018) dispõe sobre tratamento de dados pessoais por pessoa natural ou jurídica de direito público ou privado (Art. 1º); o escopo territorial e a oferta de bens/serviços para indivíduos localizados no Brasil aparecem no Art. 3º. Um programa de privacidade estrutura o cumprimento contínuo da lei e reduz exposição regulatória. Não é obrigatório por lei, mas é a base defensiva quando auditada pela ANPD (Autoridade Nacional de Proteção de Dados). [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]

Elementos obrigatórios sob LGPD:
- **Identificação do controlador** (Art. 5º, VI — quem decide fins e meios [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- **Indicação de Encarregado** (Art. 41 — DPO; dispensa possível para agente de pequeno porte per Res. CD/ANPD nº 2/2022 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm; https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022])
- **Registro de atividades de tratamento** (Art. 37 — inventário de dados / Matriz de Atividades [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- **Base legal para cada finalidade** (Art. 7º ou Art. 11 se sensível [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- **Avaliação de Impacto (RIPD)** quando a ANPD determinar ao controlador sua elaboração (Art. 38 [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- **Políticas de retenção** (Art. 16 — conservação após término do tratamento em hipóteses específicas; necessidade/minimização está no Art. 6º, III [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- **Direitos de titulares** (Art. 18 — acesso, correção, exclusão, portabilidade, etc. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- **Segurança** (Art. 46 — medidas técnicas e administrativas [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- **Plano de resposta a incidente** (Art. 48 — se houver incidente que possa acarretar risco ou dano relevante, comunicar ANPD + afetados [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])

> **No silent supplement.** If a research query to the configured legal research tool (JusBrasil, Escavador) returns few or no results for a LGPD provision or ANPD regulação, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [requirement]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?" A lawyer decides whether to accept lower-confidence sources.
>
> **Source attribution.** Where the plan cites a statute, regulation, or ANPD guidance, tag the citation: `[JusBrasil]`, `[Escavador]`, `[statute / gov.br]`, `[ANPD]`, or the MCP tool name; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

## Load prior context

Before producing a new implementation plan, check the outputs folder for prior work on this entity / controlador:

- **Prior `pia-generation` (RIPD) outputs** — if PIAs exist for specific processing activities, aggregate findings and refer to them rather than duplicating.
- **Prior `dpa-review` outputs** for vendors the company works with — inform the vendor-management section of the plan.

If prior work exists, cite it: "This plan builds on prior RIPD dated [date] and incorporates findings from [N] vendor DPA reviews."

## Load house style

Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → `## Privacy policy commitments` and `## PIA house style`. This plan should align with the company's published privacy policy and any existing compliance structures.

## The plan structure

### Step 1: Intake — Organizational assessment

Ask the company:

1. **What does the company do?** (e.g., SaaS platform, e-commerce, healthcare provider, financial services)
2. **What data does it collect?** (name, email, location, health, financial, behavioral, etc.)
3. **How many data subjects?** (customers, employees, vendors, partners)
4. **Where is data stored?** (Cloud, on-prem, multiple regions?)
5. **Do you have a DPO / Encarregado already?** If not, who will fill the role?
6. **Any prior incidents or regulatory contacts?** (ANPD inquiry, complaint, breach)
7. **What's the biggest compliance worry?** (international transfers, health data, children, etc.)

### Step 2: Data mapping (Matriz de Atividades)

Build a table of each major processing activity:

| Activity | Data categories | Purposes | Recipients | Retention | Legal basis | Risks |
|---|---|---|---|---|---|---|
| Customer account | Name, email, phone, address | Contract performance, marketing (consent) | Payment processor, CRM | 2 years post-termination + 5 years retention for tax | Art. 7º, I+II | Low if consent clear |
| Analytics | IP, behavior, clicks | Service improvement, business analytics | Analytics vendor (US-based) | 13 months | Art. 7º, IX (LI — **risky**, needs balancing test) | **Medium — international transfer Art. 33** |
| Marketing emails | Email, preferences | Promotional communications | Email platform | While consented | Art. 7º, I (must be opt-in) | Low if consent documented |
| Employee data | Name, tax ID, health insurance, performance | Payroll, HR, legal compliance | HR system, accountant, health insurance | 5 years post-termination (tax retention) | Art. 7º, II (contract + legal obligation) | Low for employees (expected) |

For each row, note: **Is the legal basis clear?** If "Legitimate Interest," is a balancing test documented? If international transfer, is there a Adequacy Decision or Standard Contractual Clause?

### Step 3: Legal basis assessment

For each data category, confirm the lawful basis per Art. 7º (or Art. 11 for sensitive data):

| Basis | When to use | Example | ⚠️ Risk if wrong |
|---|---|---|---|
| **I — Consent** | User actively agrees to data use (opt-in, not default) | "Check here to receive marketing emails" | **Highest risk** — must prove consent, must honor withdrawal |
| **II — Contract** | Data needed to perform a contract the user agreed to | Name + address to deliver an order | Low — data is necessary |
| **VII — Legal obligation** | Law requires the company to collect (tax, labor, court order) | Employee name + tax ID for payroll | Low — company has no choice |
| **IX — Legitimate Interest** | Company's interest to use data (non-essential) | Analytics to improve app performance | **Medium risk** — must pass balancing test (company benefit vs. user privacy) |

**Red flag:** If large portions of data collection rely on "legitimate interest" without documented balancing test, ANPD scrutiny is likely. Recommend shifting to consent or legal basis where possible.

**Example balancing test template:**
> We collect clickstream data (Art. 7º, IX — legitimate interest) because understanding user behavior is essential to improve our service, which benefits users. Balancing: our interest (improve service quality) outweighs user privacy cost (data is anonymized within 13 months, not shared with third parties). User can opt out via settings menu.

### Step 4: DPO / Encarregado nomination

**Does the company need a DPO?** Per Art. 41 LGPD [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]:
- Required if: monitoring of personal data is core activity (data broker, processor, regulator)
- Recommended if: large-scale or sensitive-data processing
- Dispensa possible if: small business OR small amount of data processing (Res. CD/ANPD nº 2/2022 [verified: https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022])

**If needed, who is it?**

- Internal hire (best: legally trained, can report directly to GC/CEO)
- Outsourced DPO (via consultancy)
- In-house operations manager with DPO training

**DPO responsibilities:**
- Aceitar reclamações e comunicações dos titulares, prestar esclarecimentos e adotar providências (Art. 41, §2º, I [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- Receber comunicações da ANPD e adotar providências (Art. 41, §2º, II [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- Orientar funcionários e contratados sobre práticas de proteção de dados (Art. 41, §2º, III [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- Act as escalation point for privacy concerns

**Output:** DPO name, title, email, start date, training completed.

### Step 5: RIPD (Privacy Impact Assessments) — which activities need one?

**RIPD triggers (Art. 38 LGPD [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]):**
- [ ] Treatment founded on **legitimate interest** (Art. 7º, IX) — RIPD highly recommended (ANPD may require)
- [ ] Large-scale or sensitive data (health, financial, biometric, etc.)
- [ ] Automated decision-making that affects the person (Art. 20 LGPD [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
- [ ] Monitoring of personal data at scale
- [ ] Novel processing that hasn't been done before

For each high-risk activity identified in data mapping, ensure prior RIPD (or schedule one via `privacy-legal:pia-generation`).

**Output:** List of activities requiring RIPD + dates PIAs will be completed.

### Step 6: Policies and procedures

The company should document:

1. **Privacy Policy** (public-facing, Art. 9º LGPD [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
   - What data? Why? Who has access? How long? How to exercise rights?
   - Should be updated / reviewed annually by legal

2. **Data Processing Addendum (DPA)** — if company is a **processor** (Art. 5º, VII [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
   - For vendors who collect data on the company's behalf, the company must have a DPA
   - DPA should include: instructions, security, audit rights, sub-processor approval, deletion/return on termination

3. **Vendor management policy** — for third-party processors
   - Which vendors have access to personal data?
   - Are they subject to DPA?
   - Are they compliant (security, insurance, etc.)?

4. **Employee data handling policy**
   - Who can access employee data?
   - For what purposes?
   - Confidentiality clause in employment contract?

5. **Retention and deletion policy**
   - How long is data kept for each purpose?
   - How is data deleted / anonymized?
   - Who approves deletion requests?

6. **Incident response plan** (Art. 48 LGPD [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm])
   - If personal data is breached or compromised, what happens?
   - Notification timeline to ANPD (3 business days under current ANPD incident guidance [verified: https://www.gov.br/anpd/pt-br/assuntos/comunicacao-de-incidentes-de-seguranca-cis])
   - Notification to affected data subjects (if the incident can cause relevant risk or damage [verified: https://www.gov.br/anpd/pt-br/assuntos/comunicacao-de-incidentes-de-seguranca-cis])
   - Forensics / investigation process

### Step 7: Implementation roadmap (phased plan)

**Phase 1 (Month 1-2) — Foundation**
- [ ] Appoint DPO (internal or external)
- [ ] Map all data processing activities (Matriz de Atividades)
- [ ] Document legal basis for each activity
- [ ] Review and update Privacy Policy for compliance
- [ ] Conduct breach response training for team

**Phase 2 (Month 2-4) — Risk assessment & Gap closure**
- [ ] Schedule RIPD for high-risk activities (Art. 7º, IX; automated decisions; sensitive data)
- [ ] Audit vendor contracts for LGPD gaps / need DPA
- [ ] Implement consent mechanism for opt-in data use
- [ ] Test data subject rights fulfillment (access, deletion, portability requests)
- [ ] Build incident response runbook

**Phase 3 (Month 4-6) — Governance & Training**
- [ ] Complete all PIAs (RIPD)
- [ ] Sign/update DPAs with all vendors
- [ ] Train employees on data handling (e.g., "Don't share customer data in Slack")
- [ ] Document all policies in company wiki / drive
- [ ] Schedule annual compliance review

**Phase 4 (Ongoing) — Monitoring**
- [ ] DPO monitors for new data processing activities
- [ ] Audit vendor compliance (e.g., vendor's security certification)
- [ ] Review and update Privacy Policy annually
- [ ] Respond to ANPD / data subject inquiries

## Output

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Privacy Program Implementation Plan: [Company Name]

**Prepared by:** [name] | **Date:** [date] | **DPO:** [name / TBD]

---

## Executive summary

[Company name] collects [types of data] to [purposes]. Current compliance status: [compliant / has gaps]. This plan outlines [N]-phase roadmap to reach full LGPD compliance within [timeline].

---

## Section 1: Data mapping

[Matriz de Atividades table with all processing activities]

---

## Section 2: Legal basis assessment

[For each activity, confirm legal basis + risks]

---

## Section 3: DPO appointment

**Status:** [Appointed / TBD]
**Name:** [name]
**Training:** [Certification / to be scheduled]
**Reporting line:** [to GC / to CEO]

---

## Section 4: RIPD (Privacy Impact Assessment) status

| Activity | Status | Completion date |
|---|---|---|

---

## Section 5: Policies & procedures

| Document | Status | Last updated | Owner |
|---|---|---|---|
| Privacy Policy | [Draft / Approved] | [date] | [Legal] |
| DPA template | [Draft / Approved] | [date] | [Legal] |
| Vendor management policy | [TBD] | — | — |
| Retention & deletion policy | [TBD] | — | — |
| Incident response plan | [Draft / Approved] | [date] | [Security + Legal] |

---

## Section 6: Implementation roadmap

**Phase 1 (Month 1-2):** [Tasks]
**Phase 2 (Month 2-4):** [Tasks]
**Phase 3 (Month 4-6):** [Tasks]
**Phase 4 (Ongoing):** [Tasks]

---

## Key risks & mitigations

| Risk | Likelihood | Impact | Mitigation | Owner | Deadline |
|---|---|---|---|---|---|
| [Large-scale legitimate interest processing without balancing test] | M | H | Schedule RIPD for analytics activity | [DPO] | [date] |
| [International data transfer without Standard Contract Clause] | M | H | Execute SCC with cloud vendor | [Legal] | [date] |
| [No incident response plan] | L | H | Draft and train team | [Security + Legal] | [date] |

---

## What this skill does not do

- It doesn't perform the RIPD itself (that's `privacy-legal:pia-generation`).
- It doesn't draft the Privacy Policy (that's `digital-ecommerce-legal:terms-of-use-privacy-review` or similar).
- It doesn't negotiate DPAs with vendors (that's `commercial-legal:vendor-agreement-review` or privacy-legal DPA review).
