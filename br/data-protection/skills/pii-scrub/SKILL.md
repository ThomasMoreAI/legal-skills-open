---
name: pii-scrub
title: /pii-scrub
description: 'Before sharing client or processual content with the assistant, pseudonymize PII: names → PARTE_A/PARTE_B, CPF/CNPJ/RG → [REDIGIDO], endereços/e-mails/telefones → [REDIGIDO], processo numbers → [Nº PROCESSO]. Outputs pseudonymized text + a local de-para table for re-identification. Flags segredo de justiça and dados sensíveis (LGPD art. 11) risks. Use when pasting case files, contracts, client records, or any text with personal data into the assistant.'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/privacy-legal/skills/pii-scrub
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: en
---

# /pii-scrub

## Purpose

Before a lawyer pastes processual content, client data, or contracts into Claude, pseudonymize sensitive identifiers. This skill:
1. **Scrubs the text** — names → PARTE_A/PARTE_B, CPF/CNPJ/RG → [REDIGIDO], phone/email/address → [REDIGIDO], processo numbers → [Nº PROCESSO]
2. **Returns a local de-para table** — maps scrubbed IDs back to real values so you can re-identify results later
3. **Flags legal risks** — asks about segredo de justiça and LGPD art. 11 dados sensíveis before you paste

---

## Jurisdição & Base Legal (Brasil)

This skill assumes **Brasil (LGPD, Lei 13.709/2018)** as the default jurisdiction. The obligations around PII and dados sensíveis come from:

- **Lei 13.709/2018 (LGPD)** — art. 7 (base legal for treatment), art. 11 (dados sensíveis: health, race/ethnicity, political opinion, religious belief, union membership, genetic, biometric data), art. 48 (notification to ANPD upon incident), art. 41 (DPO obligations)
- **CPC (Código de Processo Civil)** — art. 189 (segredo de justiça — interesse público/social, família, dados íntimos e arbitragem confidencial podem tramitar em segredo; sucessões ou mediação não aparecem como categorias gerais autônomas) `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`
- **Lei 12.527/2011 (Lei de Acesso à Informação)** — art. 31 (personal data excluded from disclosure requirements unless subject consented)

---

## Load context

`~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → your privacy practice profile (DPA status, regulatory footprint, base legal for data handling by the assistant).

---

## Workflow

### Step 1: Ask about legal classification

Before scrubbing, ask:

> **Quick legal check — answer 1-2 questions:**
> 1. Does this document run under **segredo de justiça** (CPC art. 189 `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`) or involve a sealed/confidential proceeding? (Yes / No / Unsure)
> 2. Does it contain **dados sensíveis** (health, race/ethnicity, religion, political opinion, biometrics, union, genetic — LGPD art. 11 `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]`)? (Yes / No / Unsure)
>
> If yes to either: **caution flag** (see Step 4 below) before scrubbing.

### Step 2: Scrubbing rules

Apply these substitutions to the pasted text:

| PII type | Substitution | Example |
|---|---|---|
| **Person names** | PARTE_A, PARTE_B, PESSOA_[N] | "João da Silva" → PARTE_A; "Acme Corp" → PARTE_A; "Maria" (counterparty) → PARTE_B |
| **CPF / RG / CNPJ** | [REDIGIDO] | 123.456.789-00 → [REDIGIDO]; 17.123.456/0001-90 → [REDIGIDO] |
| **Email addresses** | [email — REDIGIDO] | joao@acme.com → [email — REDIGIDO] |
| **Phone numbers** | [telefone — REDIGIDO] | (11) 98765-4321 → [telefone — REDIGIDO] |
| **Addresses** | [endereço — REDIGIDO] | "Rua X, 123, São Paulo" → [endereço — REDIGIDO] |
| **Processo/Autos numbers** | [Nº PROCESSO] | "Autos nº 0001234-56.2023.8.26.0100" → [Nº PROCESSO] |
| **Bank account / card numbers** | [conta — REDIGIDO] | Qualquer sequência 8+ dígitos → [conta — REDIGIDO] |
| **Dates of birth** | [data de nascimento — REDIGIDO] | 15/03/1985 (if clearly DOB context) → [data de nascimento — REDIGIDO] |

**Preserve context:** Keep surrounding text and structure so the analysis makes sense. Preserve document formatting (headings, lists, paragraphs).

### Step 3: Build de-para table

Create a mapping table (local only, not sent to assistant with the document):

```markdown
## De-Para — [data/hora]

| Scrubbed | Real value | Context |
|---|---|---|
| PARTE_A | João da Silva | Plaintiff/demandante |
| PARTE_B | Acme Corp | Defendant/demandada |
| [REDIGIDO] | 123.456.789-00 | CPF of PARTE_A |
| [Nº PROCESSO] | 0001234-56.2023.8.26.0100 | São Paulo Federal Court, case ID |
| [email — REDIGIDO] | joao@acme.com | PARTE_A contact |
```

Save this locally in a safe place (password-protected file, encrypted note, not shared). It's your key to re-identify results.

### Step 4: Caution flags

If the answer to Step 1 question 1 or 2 is **yes**:

> **⚠️ Caution:** This document is classified as [segredo de justiça / contains dados sensíveis under LGPD art. 11]. Even pseudonymized, consider:
>
> - **Segredo de justiça:** Sealed proceedings should not be discussed outside the legal team. Pasting here may waive the seal's confidentiality. Confirm that your organization has authorized disclosure to the AI assistant for legal analysis.
> - **Dados sensíveis (LGPD art. 11):** Health records, biometric data, religious/political affiliation, racial/ethnic origin, union membership, genetic data cannot be processed by the assistant unless you have a **valid base legal (LGPD art. 7)** — ex., explicit consent, contractual necessity, legal obligation, or vital interest. Pseudonymization helps but does not create a base legal. Ask: does your privacy policy or user agreement permit processing of [type] data by third-party AI? If not, do not paste.
> - **Recommendation:** If unsure, ask your DPO or privacy counsel before pasting.

Do not block the user from proceeding — just flag the risk. They decide.

---

## Output format

Return TWO items:

1. **Scrubbed text** (ready to paste into the assistant):
```
[Full text with PII substituted, formatted as received]
```

2. **De-para table** (save locally):
```markdown
## De-Para — [date/time]
[Table as above]

**Preserve this table.** It is your key to re-identify results later. Do not share with the assistant or anyone without need-to-know.
```

---

## Nota sobre sigilo profissional e LGPD

Este skill não gera sigilo profissional — pseudonymização não transforma um documento num memorando jurídico protegido. Se a análise que você faz depois, apoiada neste scrub, é rascunho para consultoria a um advogado, aquele rascunho precisa do cabeçalho apropriado (sigilo profissional advogado-cliente, Estatuto OAB, Lei 8.906/1994). O scrub é pré-processamento; o sigilo vem da relação jurídica com o profissional que orienta.

**Base legal: não resolvida.** Pseudonymização reduz risco mas não resolve o problema de base legal — sua empresa precisa de base legal (LGPD art. 7) para passar dados pessoais pro assistente, mesmo pseudonymizados. Se não tem (ex.: dados de cliente, sem consentimento informado, sem base contratual), isso é uma lacuna LGPD que este skill sinaliza mas não cura.

---

## What this skill does not do

- **Make a legal judgment on confidentiality.** It flags segredo de justiça and dados sensíveis. Your lawyer decides whether to proceed.
- **Guarantee anonymization.** Pseudonymization + context (document structure, dates, amounts) *may* still allow re-identification. For high-stakes data, consider a redaction lawyer, not an AI.
- **Create a LGPD-compliant basis.** It flags the base-legal gap. Solving that is between you and your DPO/counsel.
- **Encrypt or store the de-para table.** You manage the local table — back it up, protect it, delete it when done.

---

## Examples

### Example 1: Employment matter

**Input:**
```
João da Silva, CPF 123.456.789-00, contratado em 01/02/2020,
foi rescindido em 30/11/2023 pela Acme Corp (CNPJ 17.123.456/0001-90).
Contato: joao@acme.com, (11) 98765-4321.
Endereço: Rua das Flores, 456, São Paulo, SP.
Motivo da rescisão: desempenho insuficiente (notificado em 15/11/2023).
```

**Output (scrubbed):**
```
PARTE_A, [REDIGIDO], contratado em [data — 01/02/2020], 
foi rescindido em 30/11/2023 pela PARTE_A (Empresa) ([REDIGIDO]).
Contato: [email — REDIGIDO], [telefone — REDIGIDO].
Endereço: [endereço — REDIGIDO], São Paulo, SP.
Motivo da rescisão: desempenho insuficiente (notificado em [data — 15/11/2023]).
```

**De-para:**
| PARTE_A (person) | João da Silva | Employee |
| [REDIGIDO] (CPF) | 123.456.789-00 | PARTE_A's CPF |
| PARTE_A (company) | Acme Corp | Employer |
| [REDIGIDO] (CNPJ) | 17.123.456/0001-90 | Employer CNPJ |
| [email — REDIGIDO] | joao@acme.com | PARTE_A contact |
| [telefone — REDIGIDO] | (11) 98765-4321 | PARTE_A contact |
| [endereço — REDIGIDO] | Rua das Flores, 456, São Paulo, SP | PARTE_A address |

### Example 2: Civil litigation / caution flag

**Input (after caution check):**
```
Autos nº 0001234-56.2023.8.26.0100 (Tribunal de Justiça de São Paulo).
Demandante: Silva e Cia. Ltda. (CNPJ 11.222.333/0001-44)
Demandado: Fornecedor Brasil Imp. Exp. (CNPJ 22.333.444/0001-55)
Questão: inadimplência de R$ 500.000,00.
Data da sentença: 10/12/2024, Juiz Fernando de Souza.
```

**Caution flag first:**
> ⚠️ This is a civil case from TJSP. Check: does it run under segredo de justiça? If sealed/confidential, confirm your org has authorization to discuss with AI counsel.

**Output (scrubbed if user confirms):**
```
[Nº PROCESSO] (Tribunal de Justiça de São Paulo).
Demandante: PARTE_A ([REDIGIDO])
Demandado: PARTE_B ([REDIGIDO])
Questão: inadimplência de R$ 500.000,00.
Data da sentença: 10/12/2024, Juiz [REDIGIDO].
```

---

**Antes de usar:** Leia a seção `## Antes de colar dados de cliente` no `litigation-legal/CLAUDE.md` e `privacy-legal/CLAUDE.md`.
