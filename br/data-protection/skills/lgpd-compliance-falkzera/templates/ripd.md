<!--
TEMPLATE: RELATÓRIO DE IMPACTO À PROTEÇÃO DE DADOS PESSOAIS (RIPD)
====================================================================
Base: art. 5º XVII + art. 38 + art. 10 §3º LGPD. Estrutura consolidada
com base nas orientações da ANPD (página oficial RIPD) e GDPR DPIA.

Gerar quando:
 - tratamento baseado em legítimo interesse
 - dados sensíveis em larga escala
 - decisões automatizadas que afetam direitos
 - dados de crianças/adolescentes/idosos
 - monitoramento sistemático
 - IA/ML que produz inferência

Documento INTERNO. Não publicar. Apresentar à ANPD quando solicitado.

Placeholders: {{...}} para preencher na geração.
-->

# Relatório de Impacto à Proteção de Dados Pessoais (RIPD)

**Projeto / Tratamento:** {{NOME_DO_TRATAMENTO}}
**Controlador:** {{CONTROLADOR_NOME}} ({{CONTROLADOR_DOC}})
**Encarregado (DPO):** {{DPO_NOME}}, {{DPO_CONTATO}}
**Data de elaboração:** {{DATA}}
**Versão:** {{VERSAO}}
**Responsável técnico:** {{RESPONSAVEL}}
**Status:** Rascunho / Aprovado

> Documento elaborado nos termos do art. 38 da LGPD, contendo descrição dos tipos de dados coletados, metodologia, análise de medidas de mitigação de risco.

---

## 1. Sumário Executivo

| | |
|---|---|
| **Finalidade do tratamento** | {{FINALIDADE_RESUMIDA}} |
| **Base legal** | {{BASE_LEGAL}} (art. {{ART}} LGPD) |
| **Categorias de dados** | {{CATEGORIAS}} |
| **Categoria de titulares** | {{TITULARES}} (estimativa: {{NUMERO_APROXIMADO}}) |
| **Nível de risco identificado** | {{NIVEL_RISCO}} (baixo / médio / alto) |
| **Decisão final** | {{DECISAO}} (prosseguir / prosseguir com mitigações / suspender / redesenhar) |

---

## 2. Descrição do Tratamento (art. 38 par. único)

### 2.1. Finalidade detalhada

{{DESCREVER FINALIDADE DE FORMA ESPECÍFICA, LIGANDO A UM PROCESSO DE NEGÓCIO CONCRETO. Evitar vagueza. Exemplo bom: "Avaliar perfil de crédito de candidato a crediário no checkout do e-commerce, com base em histórico interno + score Serasa, para aprovar ou recusar automaticamente a operação de até R$ 5.000."}}

### 2.2. Fluxo de dados

```
[ Origem / coleta ] → [ Processamento ] → [ Decisão / armazenamento ] → [ Compartilhamento ]
```

{{DIAGRAMA OU DESCRIÇÃO DETALHADA DO FLUXO}}

### 2.3. Categorias de dados e fonte

| Categoria | Fonte | Sensível? | Volume estimado |
|---|---|---|---|
| {{DADO}} | {{DE_ONDE_VEM}} | Sim/Não | {{N}} |

### 2.4. Categoria de titulares

{{Ex: clientes pessoa física do e-commerce, com perfil socioeconômico variado, incluindo possivelmente pessoas em situação de vulnerabilidade financeira.}}

### 2.5. Operadores envolvidos

| Operador | Função | País | DPA + SCC |
|---|---|---|---|
| {{NOME}} | {{O_QUE_FAZ}} | {{PAIS}} | Sim/Não |

### 2.6. Tempo de retenção

{{Especificar por tipo de dado e fundamento legal.}}

---

## 3. Necessidade e Proporcionalidade

### 3.1. A finalidade é legítima e específica?

{{Análise do princípio da finalidade (art. 6º I).}}

### 3.2. Os dados coletados são adequados, necessários e proporcionais?

{{Princípio da necessidade (art. 6º III). Justificar cada categoria coletada.}}

### 3.3. Há alternativa menos invasiva à finalidade pretendida?

{{Avaliar: poderia anonimizar? amostragem? agregar? Se sim e não foi feito, justificar.}}

---

## 4. Teste de Balanceamento (legítimo interesse: art. 10 §3º)

*Preencher apenas se a base legal for legítimo interesse (art. 7º IX).*

### 4.1. Interesse legítimo do controlador (ou terceiro)

{{Descrever interesse: segurança da plataforma, prevenção a fraude, melhoria de produto, etc.}}

### 4.2. Necessidade do tratamento

{{Por que NÃO basta consentimento? Por que NÃO basta outra base?}}

### 4.3. Direitos e liberdades fundamentais do titular

{{Impactos possíveis: discriminação, vigilância, dano patrimonial/moral.}}

### 4.4. Expectativa razoável do titular

{{O titular esperaria esse tratamento dado o contexto e a relação com o controlador?}}

### 4.5. Mitigantes adotados

{{Lista de medidas que reduzem impacto: anonimização, agregação, opt-out facilitado, transparência reforçada, RIPD publicado, etc.}}

### 4.6. Conclusão do teste

☐ Interesse legítimo **prevalece** (com as mitigações acima) → prosseguir.
☐ Interesse legítimo **não prevalece** → redesenhar com outra base legal ou suspender.

---

## 5. Riscos Identificados e Mitigações

Pra cada risco, classificar probabilidade × impacto e mapear mitigação.

| # | Risco | Probabilidade | Impacto | Risco residual após mitigação | Mitigação |
|---|---|---|---|---|---|
| 1 | Vazamento de banco principal | Baixa | Alto | Médio | Criptografia em repouso, 2FA admin, backup off-site, runbook de incidente |
| 2 | Acesso indevido por colaborador | Baixa | Médio | Baixo | Menor privilégio, logs de acesso, termo de confidencialidade, treinamento |
| 3 | Decisão automatizada discriminatória | Média | Alto | Médio | Auditoria periódica do modelo, canal de contestação, revisão humana em casos limítrofes |
| 4 | Re-identificação de dados "anonimizados" | Baixa | Médio | Baixo | k-anonimato, supressão de identificadores indiretos, controle de combinações |
| 5 | Coleta excessiva (mission creep) | Média | Médio | Baixo | Revisão trimestral do ROPA, code review com checklist de PII |
| 6 | ... | | | | |

### 5.1. Riscos específicos do tratamento

{{Adicionar riscos contextuais: ex. se for app de saúde, risco de discriminação por seguradora; se for app de criança, risco de aliciamento.}}

---

## 6. Medidas Técnicas e Administrativas (art. 46 LGPD)

### Técnicas
- {{Listar: criptografia, controle de acesso, autenticação forte, hardening, monitoramento, etc.}}

### Administrativas
- {{Listar: políticas, treinamentos, termos de confidencialidade, gestão de fornecedores, plano de incidente.}}

### Específicas pra este tratamento
- {{Mitigações desenhadas especificamente, não cobertas pela política geral.}}

---

## 7. Direitos do Titular: atendimento operacional

Como cada um dos 9 direitos do art. 18 será atendido neste tratamento:

| Direito | Mecanismo |
|---|---|
| Confirmação | Self-service em /privacidade |
| Acesso | Self-service + canal DPO |
| Correção | Edição de perfil + canal DPO |
| Anonimização/Bloqueio/Eliminação | Endpoint admin |
| Portabilidade | GET /api/legal/export |
| Eliminação | Botão "Excluir conta" |
| Informação sobre compartilhamento | Política + log por usuário |
| Informação sobre consequências da negativa | UX no momento do consentimento |
| Revogação | Painel de preferências |

### Decisão automatizada (se aplicável: art. 20)

- **Como o titular saberá** que a decisão foi automatizada: {{...}}
- **Informações fornecidas** sobre critérios e procedimentos: {{...}}
- **Canal de contestação**: {{URL ou e-mail}}
- **SLA da revisão**: {{prazo}}

---

## 8. Decisão e Plano de Ação

### Decisão da Encarregada(o) sobre o tratamento

☐ **Prosseguir**, riscos aceitáveis, mitigações suficientes.
☐ **Prosseguir condicionalmente**, execução das mitigações marcadas abaixo como pré-requisito.
☐ **Suspender**, risco residual incompatível; redesenhar antes de retomar.

### Mitigações condicionantes (se aplicável)

| # | Mitigação | Responsável | Prazo |
|---|---|---|---|
| | | | |

### Cronograma de revisão

Este RIPD deve ser revisitado:
- **A cada 12 meses**, ou
- **Quando houver mudança material** no tratamento (nova categoria de dado, novo operador, nova finalidade, nova tecnologia, mudança regulatória)
- **Em caso de incidente** envolvendo este tratamento

---

## 9. Aprovações

| Função | Nome | Data | Assinatura |
|---|---|---|---|
| Encarregado (DPO) | {{DPO_NOME}} | | |
| Responsável de Segurança | | | |
| Responsável Técnico do Projeto | | | |
| Direção / Sócio | | | |

---

## Anexos

- A. Diagrama de fluxo de dados detalhado
- B. ROPA correspondente
- C. DPA com operadores relevantes
- D. Logs de auditoria de implementação das mitigações
- E. (se decisão automatizada) Documentação do modelo, dataset de treinamento, métricas de viés

---

## Histórico de versões

| Versão | Data | Mudanças | Autor |
|---|---|---|---|
| 1.0 | {{DATA}} | Versão inicial | {{DPO_NOME}} |
