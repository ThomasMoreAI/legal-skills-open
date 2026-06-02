---
name: legal-brief
title: legal-brief — Briefing Jurídico
description: Gerar briefings contextuais para trabalho jurídico — resumo diário, pesquisa de tópico ou resposta a incidente. Use ao iniciar o dia e precisar de uma varredura de itens jurídicos relevantes por email, calendário e contratos, ao pesquisar uma questão jurídica específica em fontes internas, ou quando uma situação em desenvolvimento (vazamento de dados, ameaça de litígio, consulta regulatória) exige contexto rápido.
author: evolution-foundation
author_url: https://github.com/evolution-foundation/evo-nexus/tree/main/.claude/skills/legal-brief
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: pt
---

# legal-brief — Briefing Jurídico

> **Este documento não constitui aconselhamento jurídico — consulte o assessor jurídico habilitado antes de tomar decisões com base nesta análise.**
> Contatos legais: **Thaís Menezes** (contratos Brius/Etus) | **Vitor Lacerda** (jurídico Etus)

Gerar briefings contextuais para trabalho jurídico. Suporta três modos: brief diário, brief de tópico e brief de incidente.

## Acionamento

User executa `/legal-brief`, `/legal-brief daily`, `/legal-brief topic [consulta]` ou `/legal-brief incident [tópico]`.

Se nenhum modo for especificado, perguntar ao usuário qual tipo de brief é necessário.

## Modos

---

### Brief Diário

Um resumo matinal de tudo que um membro da equipe jurídica precisa saber para começar o dia.

#### Fontes a Verificar

Verificar cada fonte conectada para itens jurídicos relevantes:

**Gmail (via MCP):**
- Novas solicitações de contrato ou de revisão
- Questões ou relatórios de conformidade
- Respostas de contrapartes em negociações ativas
- Itens sinalizados ou urgentes da caixa de entrada jurídica
- Comunicações de advogados externos
- Newsletters de atualização jurídica ou regulatória

**Google Calendar (via MCP):**
- Reuniões de hoje que precisam de preparação jurídica (reuniões de conselho, revisões de negócios, chamadas com fornecedores)
- Prazos que se aproximam nesta semana (vencimentos de contratos, prazos de entrega, prazos de resposta)
- Sincronizações recorrentes da equipe jurídica

**Discord (canais jurídicos/contratos):**
- Mensagens do período anterior em canais relevantes
- Mensagens diretas solicitando parecer jurídico
- Menções de tópicos jurídicos relevantes (contrato, conformidade, privacidade, NDA, termos)
- Escalações ou solicitações urgentes

**int-evo-crm:**
- Negócios avançando para estágios que requerem envolvimento jurídico
- Novas oportunidades sinalizadas para revisão jurídica

**Arquivos locais / Notion:**
- Contratos aguardando revisão ou assinatura
- Datas de vencimento se aproximando (próximos 30 dias)
- Acordos recém-executados

#### Formato de Saída

```
## Brief Jurídico Diário — [Data]

### Urgente / Ação Necessária
[Itens que precisam de atenção imediata, ordenados por urgência]

### Pipeline de Contratos
- **Aguardando sua revisão**: [contagem e lista]
- **Aguardando resposta da contraparte**: [contagem e lista]
- **Prazos se aproximando**: [itens com vencimento nesta semana]

### Novas Solicitações
[Solicitações de revisão de contrato, pedidos de NDA, questões de conformidade recebidas desde o último brief]

### Calendário Hoje
[Reuniões com relevância jurídica e qual preparação é necessária]

### Atividade da Equipe
[Mensagens ou atualizações-chave dos canais Discord da equipe]

### Prazos desta Semana
[Prazos iminentes e datas de entrega]

### Fontes Não Disponíveis
[Quaisquer fontes que não estavam conectadas ou retornaram erros]
```

---

### Brief de Tópico

Pesquisa e briefing sobre uma questão ou tópico jurídico específico por todas as fontes disponíveis.

#### Fluxo de Trabalho

1. Aceitar a consulta de tópico do usuário
2. Pesquisar por todas as fontes conectadas:
   - **Documentos locais / Notion**: Memorandos internos, análises anteriores, playbooks, precedentes
   - **Gmail**: Comunicações anteriores sobre o tópico
   - **Discord**: Discussões da equipe sobre o tópico
   - **int-evo-crm**: Contratos ou cláusulas relacionados
3. Sintetizar constatações em um brief estruturado

#### Formato de Saída

```
## Brief de Tópico: [Tópico]

### Resumo
[Resumo executivo de 2-3 frases das constatações]

### Contexto
[Contexto e histórico das fontes internas]

### Estado Atual
[Qual é a posição ou abordagem atual da organização, com base nos documentos disponíveis]

### Considerações-chave
[Fatores importantes, riscos ou questões em aberto]

### Precedente Interno
[Decisões, memorandos ou posições anteriores encontradas nas fontes internas]

### Lacunas
[Que informações estão faltando ou quais fontes não estavam disponíveis]

### Próximos Passos Recomendados
[O que o usuário deve fazer com estas informações]
```

#### Notas Importantes
- Briefs de tópico sintetizam o que está disponível nas fontes conectadas; não substituem pesquisa jurídica formal
- Se o tópico requer autoridade jurídica atual ou jurisprudência brasileira, recomendar ao usuário consultar plataformas de pesquisa jurídica (Jusbrasil, LexML, AASP, IBJRIS, etc.) ou advogado externo
- Sempre registrar as limitações das fontes pesquisadas
- Para questões de direito brasileiro (LGPD, CLT, Código Civil, Marco Civil), verificar sempre a legislação atualizada e jurisprudência do STJ/STF quando relevante

---

### Brief de Incidente

Briefing rápido para situações em desenvolvimento que requerem atenção jurídica imediata (vazamentos de dados, ameaças de litígio, consultas regulatórias, disputas de PI, etc.).

#### Fluxo de Trabalho

1. Aceitar o tópico ou descrição do incidente
2. Varrer rapidamente todas as fontes conectadas para contexto relevante:
   - **Gmail**: Comunicações sobre o incidente
   - **Discord**: Discussões em tempo real e escalações
   - **Documentos locais / Notion**: Políticas relevantes, planos de resposta, cobertura de seguro
   - **Google Calendar**: Reuniões de resposta agendadas
   - **int-evo-crm / arquivos locais**: Contratos afetados, disposições de indenização, requisitos de seguro
3. Compilar em um brief de incidente acionável

#### Formato de Saída

```
## Brief de Incidente: [Tópico]
**Elaborado em**: [timestamp]
**Classificação**: [avaliação de severidade se determinável]

### Resumo da Situação
[O que se sabe sobre o incidente]

### Linha do Tempo
[Resumo cronológico dos eventos com base nas fontes disponíveis]

### Considerações Jurídicas Imediatas
[Requisitos de notificação regulatória, obrigações de preservação, questões de privilégio]

**Para incidentes de dados (LGPD art. 48):**
- Notificar a ANPD em prazo razoável (orientação: 72h para riscos graves)
- Notificar os titulares afetados se o incidente puder causar risco ou dano relevante
- Ativar protocolo de resposta a incidentes

### Acordos Relevantes
[Contratos, apólices de seguro ou outros acordos que podem estar implicados]

### Resposta Interna
[Qual atividade de resposta já ocorreu com base em email/Discord]

### Contatos-chave
[Contatos internos e externos relevantes identificados das fontes]
Internos: Thaís Menezes, Vitor Lacerda
Externos: [advogado externo se engajado]

### Ações Imediatas Recomendadas
1. [Ação mais urgente]
2. [Segunda prioridade]
3. [etc.]

### Lacunas de Informação
[O que ainda não se sabe e precisa ser determinado]

### Fontes Verificadas
[O que foi pesquisado e o que não estava disponível]
```

#### Notas Importantes para Briefs de Incidente
- A velocidade importa. Produzir o brief rapidamente com as informações disponíveis em vez de aguardar informações completas
- Sinalizar quaisquer obrigações de hold judicial ou preservação imediatamente
- Registrar considerações de privilégio (marcar o brief como privilegiado advogado-cliente / produto de trabalho se apropriado)
- Se o incidente pode envolver vazamento de dados, sinalizar os prazos aplicáveis de notificação (LGPD art. 48 — orientação ANPD: 72h para riscos graves)
- Recomendar engajamento de advogado externo se a questão for significativa — contatar Thaís Menezes ou Vitor Lacerda

## Notas Gerais

- Se as fontes não estiverem disponíveis, registrar as lacunas de forma proeminente para que o usuário saiba o que não foi verificado
- Para briefs diários, adaptar às preferências do usuário ao longo do tempo (o que é útil, o que quer filtrado)
- Briefs devem ser acionáveis: cada item deve ter um próximo passo claro ou motivo de inclusão
- Manter briefs concisos. Referenciar materiais-fonte em vez de reproduzi-los integralmente
- **Este documento não constitui aconselhamento jurídico.** Contatos: Thaís Menezes | Vitor Lacerda
