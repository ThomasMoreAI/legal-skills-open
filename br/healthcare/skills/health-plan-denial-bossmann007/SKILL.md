---
name: health-plan-denial-bossmann007
title: /health-medical-legal:health-plan-denial
description: Triagem de negativa de operadora de plano de saúde. Análise de cobertura, rol ANS, cancelamento unilateral, reajuste abusivo. Aplicável a Lei 9.656/1998 (planos de saúde), CDC, Súmulas STJ. Use quando paciente/consumidor receber negativa de procedimento, cancelamento de plano, ou cobrança indevida.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/health-medical-legal/skills/health-plan-denial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: healthcare
language: pt
---

# /health-medical-legal:health-plan-denial

Triage de negativa de operadora de plano de saúde. Não é parecer de mérito — é leitura estruturada para decidir: qual é o argumento de cobertura? Qual é o argumento da operadora? Qual é a urgência? Qual é a próxima ação?

Cobre:
1. Tipo de negativa (exclusão de procedimento? Incompatibilidade com rol? Limite de sessões? Falta de autorização prévia?)
2. Rol ANS (Lei 14.454/2022 — rol é exemplarivo, não taxativo [modelo conhecimento — verificar]; negativa com base em "não consta do rol" é débil).
3. Lei 9.656/1998 — regime de planos de saúde; direitos do beneficiário.
4. CDC — consumidor é categoria legal; cláusulas abusivas (Art. 51) são nulas. [verified: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm]
5. Súmulas STJ sobre cobertura, rol, cancelamento, reajuste [modelo conhecimento — verificar].
6. Urgência médica (saúde em risco? Tutela de urgência pode ser necessária?).
7. Opções de resposta (resposta administrativa, tutela, reclamação à ANS, ação judicial).

**Output:** triage rating (cobertura forte, fraca, urgência alta), análise da alegação da operadora, recomendação de postura, próximas ações.

---

## Matter context

Check `## Matter workspaces` in CLAUDE.md. If enabled, load active matter context. If not, write to `~/.claude/plugins/config/claude-for-legal/health-medical-legal/inbound/`.

---

## Purpose

Health plan denials are among the most common consumer legal issues in Brasil. Operadora says "not covered." Patient says "I need it." Legal question: does the plan actually exclude it, or is the operadora wrong?

This skill reads the denial letter and the policy, does the legal mapping, and surfaces which arguments are strong and which are weak.

---

## Premissa de jurisdição (Brasil)

**Lei 9.656/1998 — Planos de Saúde:**
- **Art. 10:** Plano deve oferecer cobertura básica de procedimentos. [verified: https://www.planalto.gov.br/ccivil_03/leis/l9656.htm]
- **Rol (Art. 12):** ANS mantém rol exemplarivo de procedimentos [modelo conhecimento — verificar].
- **Exemplarivo não taxativo:** Negativa com base em "não consta do rol" é fraca. Rol é exemplo, não limite.
- **Art. 13, parágrafo único, II, "b":** em planos individuais/familiares, é vedada a denúncia (cancelamento) unilateral pela operadora, salvo fraude ou inadimplência superior a 60 dias. (O Art. 35-C trata da cobertura obrigatória de urgência/emergência, não do cancelamento.) [verified: https://www.planalto.gov.br/ccivil_03/leis/l9656.htm]
- **Reajuste:** Limitado a 2x ao ano [modelo conhecimento — verificar Lei 14.454/2022].

**CDC (Lei 8.078/1990) — Aplicável a planos de saúde:**
- Beneficiário é consumidor; operadora é fornecedora.
- **Art. 51:** Cláusulas abusivas são nulas. [verified: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm]

**Súmulas STJ [modelo conhecimento — verificar]:**
- "Cobertura de procedimento ainda que não listado em rol se prescrito por médico contratado e essencial para saúde."
- "Cancelamento de plano após sinistro é abusivo."
- "Reajuste superior aos limites legais é nulo."

---

## Step 1: Ler a negativa

Extrair:
- **Beneficiário:** nome, CPF, número de apólice.
- **Procedimento/tratamento solicitado:** qual é?
- **Fundamento da negativa:** por quê recusam? (não autorizado previamente, não consta do rol, limite atingido, exclusão contratual, carência, pré-existente, teste experimental, falta de comprovação de necessidade).
- **Referência contratual:** qual artigo/cláusula da apólice?
- **Procedimento de recurso:** ofereceram recurso administrativo? Prazo?

---

## Step 2: Verificar a política do plano

Se disponível, ler:
- **Rol de cobertura básica:** O procedimento consta? Se sim, negativa é débil.
- **Exclusões explícitas:** A apólice exclui procedimento?
- **Carência:** Há cláusula de carência? Foi cumprida?
- **Cláusula de necessidade:** Apólice exige "necessidade médica comprovada"? Há prescrição médica?

---

## Step 3: Analisar a alegação da operadora

**Argumentos que a operadora pode usar — força relativa:**

1. **"Não consta do rol."**
   - **Fraqueza:** Rol é exemplarivo [modelo conhecimento — verificar Lei 14.454/2022].
   - **Defensável se:** Procedimento é experimental.
   - **Contraponto:** Se procedure é padrão de cuidado, negativa é abusiva.

2. **"Exclusão contratual."**
   - **Força:** Se exclusão é específica e em letras claras, é mais defensável.
   - **Fraqueza sob CDC:** Cláusula abusiva (Art. 51) é nula mesmo se contrato diz. [verified: https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm]

3. **"Limite de sessões atingido."**
   - **Força:** Se contrato especifica.
   - **Fraqueza:** Limite arbitrário sem base clínica é abusivo.

4. **"Falta de autorização prévia."**
   - **Força:** Se contrato exige e não foi pedida.
   - **Fraqueza:** Requisito é suspeito sob CDC.

5. **"Teste experimental."**
   - **Força:** Se realmente experimental.
   - **Fraqueza:** Se off-label mas estabelecido, negativa é fraca [modelo conhecimento — verificar].

6. **"Carência não cumprida."**
   - **Força:** Se não foi cumprida.
   - **Fraqueza:** Carência tem limites. Carência de 2 anos é abusiva [modelo conhecimento — verificar].

7. **"Pré-existente."**
   - **Fraqueza:** Cobertura de pré-existente é quase obrigatória.

---

## Step 4: Merit assessment — cobertura

**Questions:**
- Is the procedure medically necessary?
- Is it standard of care?
- Is it explicitly excluded, or is operadora relying on "not in rol"?
- If excluded, is the exclusion reasonable or abusive?
- Was carency satisfied?

**Rating:**
- **🟢 Strong coverage case:** Procedure is standard, not excluded, carency satisfied, operadora's argument is "not in rol" (weak).
- **🟡 Debatable:** Procedure is newer, or limit is hit, or authorization wasn't sought.
- **🔴 Weak coverage:** Procedure is experimental, explicitly excluded, or carency not satisfied.

Be honest.

---

## Step 5: Urgência

**Is the patient's health in immediate danger?**

- **Sim (urgência altíssima):** Procedimento é life-saving. Patient may need **tutela de urgência** (liminar).
- **Médio:** Procedimento melhora qualidade de vida mas não é imediato.
- **Baixo:** Procedimento é eletivo.

If urgência is high, recommend tutela and fast escalation.

---

## Step 6: Opções de resposta

### A. Resposta administrativa

- **Quando:** Operadora ofereceu recurso; procedimento não é urgente.
- **Tradeoff:** Operadora pode negar recurso. Tempo longo.
- **Próximo passo:** Rascunhar resposta.

### B. Tutela de urgência (liminar)

- **Quando:** Procedimento é urgente e cobertura é forte.
- **Tradeoff:** Requer litigação rápida.
- **Próximo passo:** Contato com litigante; petição de tutela.

### C. Ação judicial

- **Quando:** Cobertura é forte; operadora recusa; há dano.
- **Tradeoff:** Litigação longa.
- **Próximo passo:** Litigação formal.

### D. Reclamação à ANS

- **Quando:** Padrão de negar; operadora é notoriamente abusiva.
- **Tradeoff:** ANS é regulador, não corte. Investigação lenta.
- **Próximo passo:** Consentimento do paciente; jogue em paralelo.

### E. Negociação direta

- **Quando:** Cobertura é débil, mas há path a compromise.
- **Tradeoff:** Operadora pode não querer.
- **Próximo passo:** Cartas sinalizando ação podem motivar.

---

## Output structure (LEAN)

```markdown
[WORK-PRODUCT HEADER]

# Triage: Health Plan Denial — [Beneficiary name redacted] v. [Operadora]

[⚠️ Reviewer note]

---

## The denial

[Operadora's stated reason.]

## Procedure & coverage analysis

[Is it standard of care? Is it explicitly excluded?]

## Merit rating — coverage

[🟢 Strong / 🟡 Debatable / 🔴 Weak]

## Urgência

[🔴 Immediate | 🟡 Serious harm if delayed | 🟢 Elective]

## Response options (rank-ordered)

### A. Admin appeal
### B. Emergency liminar
### C. Judicial action
### D. ANS complaint
### E. Direct negotiation

**Recommendation:** [A/B/C/D/E] — [rationale and timeline]

## Damages if successful

- **Material:** [cost]
- **Moral:** [yes/no]
- **Economic loss:** [if applicable]

---

## What next?

1. **Draft admin appeal**
2. **Draft tutela petition**
3. **Escalate to litigator**
4. **File ANS complaint**
5. **Something else**
```

---

## What this skill does not do

- Produce a court filing
- Settle the case
- Determine what "medical necessity" means
- Substitute for detailed litigation strategy
