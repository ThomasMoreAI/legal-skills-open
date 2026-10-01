---
name: clinic-privacy-implementation-bossmann007
title: /health-medical-legal:clinic-privacy-implementation
description: Estruturação de Plano de Privacidade e Proteção de Dados Pessoais em saúde para clínica/hospital. Sob LGPD Art. 11 (dados sensíveis), Código de Ética Médica (sigilo médico), regulação CFM sobre prontuário eletrônico, e Lei 9.656 (se operadora de plano de saúde). Use quando iniciar um programa de privacidade ou avaliar conformidade.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/health-medical-legal/skills/clinic-privacy-implementation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: healthcare
language: pt
---

# /health-medical-legal:clinic-privacy-implementation

Estrutura um Plano de Privacidade e Proteção de Dados (equivalente ao RIPD sob Art. 38 LGPD) adaptado para contexto de saúde. Cobre:

1. Identificação de dados sensíveis (prontuário eletrônico, genética, história psiquiátrica, etc.)
2. Bases legais sob LGPD Art. 11 (consentimento vs. tratamento para saúde do titular, etc.)
3. Sigilo médico sob Código de Ética Médica e Estatuto da OAB.
4. Fluxos de dados (coleta, armazenamento, acesso, compartilhamento com terceiros).
5. Direitos do titular (acesso, correção, portabilidade, eliminação).
6. Riscos específicos a saúde (vazamento de dados genéticos, re-identificação, discriminação) e mitigações.
7. Guarda de prontuário e prazos de retenção — mínimo de 20 anos a partir do último registro (Res. CFM 1.821/2007, art. 8º; Lei 13.787/2018) `[verified: https://sistemas.cfm.org.br/normas/visualizar/resolucoes/BR/2007/1821]`.
8. Conformidade com Lei 9.656 (se operadora de plano de saúde) [verified: https://www.planalto.gov.br/ccivil_03/leis/l9656.htm].

**Output:** rascunho de Plano de Privacidade com estrutura, riscos identificados, matriz de mitigações, nomeação de responsáveis, prazos.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (default for in-house users), skip the rest of this paragraph. If enabled and there is no active matter, ask: "Which matter is this for?" Load the active matter's `matter.md` for overrides. Write outputs to `~/.claude/plugins/config/claude-for-legal/health-medical-legal/matters/<matter-slug>/`.

---

## Purpose

Um Plano de Privacidade é conversa com liderança (clínica, hospital, operadora), capturada. Pergunta: que dados coletamos, por quê, por quanto tempo, quem acessa, o que pode dar errado, como mitigamos?

Este skill estrutura essa conversa e escreve a output no formato desta equipe — o que foi aprendido de planos prévios e práticas locais.

---

## Jurisdição e regime

**Premissa:** LGPD (Lei 13.709/2018). Dado referente à saúde é dado pessoal **sensível** (Art. 5º, II); seu tratamento é regido pelo Art. 11. Exige **consentimento específico e destacado** (Art. 11, I) OU uma das hipóteses do Art. 11, II — entre elas, proteção da vida ou da incolumidade física do titular/terceiro e tutela da saúde por profissionais, serviços ou autoridade sanitária. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm]

Sigilo médico é independente da LGPD: Código de Ética Médica (Res. CFM 2.217/2018, arts. 73-79 `[verified: https://sistemas.cfm.org.br/normas/visualizar/resolucoes/BR/2018/2217]`) + violação de segredo profissional (Código Penal art. 154 `[verified: https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm]`) tornam a divulgação de informação médica ilegal sem consentimento ou justa causa, mesmo que a LGPD permitisse o tratamento.

Se a clínica/hospital também opera plano de saúde, Lei 9.656/1998 + ANS (Agência Nacional de Saúde) adiciona requisitos. Verificar regulação ANS atual sobre guarda e acesso a dados [unverified: not found in primary source].

---

## Load prior context

Antes de escrever um novo Plano de Privacidade, verificar se há prior work na pasta de outputs:
- Prior use-case-triage (PIA anterior?) — ler rating de risco e condições.
- Prior DPA reviews com fornecedores que processam dados de paciente — informam análise de compartilhamento / terceiros.

Se prior output for encontrado, citar: "Plano anterior ([data]) rating [risco]. Este Plano atualiza esse baseline — [o que mudou, o que se mantém]."

Se nenhum prior for encontrado, declarar explicitamente: "Sem prior triage ou Plano anterior — este é cold start."

---

## Load house style

Ler `~/.claude/plugins/config/claude-for-legal/health-medical-legal/CLAUDE.md` → `## Privacy and data protection (health)`. Ali estão:
- Categorias de dados que a clínica/hospital realmente trata.
- Bases legais (Art. 7 + 11 LGPD) para cada finalidade, já mapeadas.
- Retenção de prontuário (quanto tempo guardar).
- Sigilo médico — política local.

**Use a estrutura do Plano prévio se existir.** O objetivo é que este Plano pareça com os outros que essa equipe produz, não um genérico.

---

## Step 0: É necessário um Plano?

Sob LGPD, um RIPD (análise de impacto) é mandatório quando:
- Processamento fundado em **legítimo interesse** (Art. 10, §3º, que autoriza a ANPD exigir RIPD).
- Processamento de **dados sensíveis em larga escala** (Art. 11).
- **Decisões automatizadas** que afetem interesses do titular (Art. 20).
- Qualquer atividade de **alto risco às liberdades civis e direitos fundamentais** (Art. 38, que autoriza a ANPD exigir RIPD).

Para saúde, o padrão é **sempre** fazer um Plano porque:
1. Dado de saúde é dado pessoal sensível (Art. 5º, II); o tratamento é regido pelo Art. 11. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm]
2. Vazamento causa dano grave (discriminação, exposição, re-identificação).
3. Não-conformidade é risco regulatório (ANPD, CFM, ANS).

Responda: "É necessário um Plano de Privacidade para sua operação." Proceda.

---

## The intake

Converse com o cliente (clínica, hospital, compliance, legal lead) para obter:

### O que e por quê

- **Qual é a atividade de tratamento?** Ex.: "Clínica de cirurgia plástica coletando histórico genético e foto antes do procedimento."
- **Dados específicos.** Não "dados de paciente" — quais campos? Prontuário eletrônico, genética, história psiquiátrica, imagens, resultado de COVID?
- **Coleta nova ou existente?** Já coletam esses dados? Estão mudando a forma?
- **Finalidades.** Por quê coletam? Tratamento (Art. 7, II / 11, II)? Pesquisa (Art. 7, IX + Arts. 11, II / 11, III)? Publicidade (Art. 7, X + análise cuidadosa)?

### Base legal (LGPD Art. 7 + 11)

Para cada finalidade:
- **Art. 7 (pessoa natural):** Art. 7, II (execução de contrato / tratamento) vs. Art. 7, X (legítimo interesse) — qual é a base?
- **Art. 11 (dados sensíveis):** Consentimento específico e destacado (Art. 11, I) ou exceção Art. 11, II-III (profissional de saúde no exercício)?

**Pesquisar os gatilhos obrigatórios atuais para RIPD sob LGPD.** Verificar se há resolução ANPD dedicada a RIPD em saúde (estado: não vigente [modelo conhecimento — verificar]). Sinalizar incerteza.

### Who and where

- **Quem acessa os dados?** Médicos? Enfermagem? Administrativo? Cobrança? Pesquisa?
- **Terceiros.** Fornecedores de prontuário eletrônico, labs, hospital parceiro, empresa de backup, insurer?
- **Armazenamento.** On-premises, cloud (qual provedor?), qual região?
- **Retenção.** Quanto tempo guardam prontuário? CFM exige mínimo [estado incerto — verificar].

### O que pode dar errado

- **Se vazar:** qualidade do dano? Genética vazada pode ser usada pra discriminação. Histórico psiquiátrico, idem. Imagens de procedimento delicado, idem.
- **Re-identificação:** dados "anonimizados" podem ser re-identificados se combinados com outros datasets?
- **Surprise test:** paciente esperaria que você guarde isso por 20 anos? Compartilharia com terceiro?
- **Opt-out:** pode o paciente dizer não a processamento não-essencial? Como?

---

## Writing the Plano

Usar estrutura do `## Privacy and data protection` no config CLAUDE.md se capturada. Se não, usar este default com headers LEAN e conteúdo focado:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs]

# Plano de Privacidade e Proteção de Dados Pessoais em Saúde — [Clínica/Hospital]

**Preparado por:** [name] | **Data:** [date] | **Status:** DRAFT / APROVADO
**Proprietário:** [clínica] | **Revisor de privacidade:** [name]

---

## Sumário executivo

[Duas frases: o que coletam, por quê, se está OK.]

**Risco geral:** [🟢 Baixo / 🟡 Médio / 🟠 Alto / 🔴 Muito Alto]

---

## 1. Descrição do tratamento

**Categorias de dados:** [campos específicos]
**Titulares:** [pacientes / pesquisados]
**Finalidade:** [tratamento, pesquisa, administrativo]

## 2. Base legal

| Finalidade | Base (Art. 7 ou 11 LGPD) | Notas |
|---|---|---|
| [finalidade 1] | Art. 7, II | [notas] |

## 3. Fluxo de dados

**Coleta:** [como/onde] | **Armazenamento:** [sistema, região] | **Acesso:** [quem] | **Compartilhamento:** [terceiros] | **Retenção:** [duração]

## 4. Sigilo médico (Código de Ética Médica)

**Conformidade?** [sim/não — se não, explain compliance gap]

## 5. Direitos do titular (Art. 18 LGPD)

| Direito | Pode ser exercido? |
|---|---|
| Acesso | |
| Correção | |
| Eliminação | |

## 6. Riscos e mitigações

| Risco | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|
| [risco específico] | L/M/H | L/M/H | [controle] | Done/Planned/Gap |

**Risco residual:** [assessment]

## 7. Recomendação

[APROVADO / COM CONDIÇÕES / MUDANÇAS REQUERIDAS]

**Condições:** [list]

---
```

---

## What this skill does not do

- Não aprova o processamento. Um humano assina o Plano.
- Não gera parecer médico-legal. Isso é trabalho de perito.
- Não monitora conformidade pós-lançamento.
- Não substitui consulta com especialista em saúde / privacidade.
