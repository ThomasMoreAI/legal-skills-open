---
name: brief-bossmann007
title: /brief -- Briefing do Time Jurídico
description: Gera briefings contextuais para o trabalho jurídico — resumo diário, pesquisa por tema ou resposta a incidente. Use ao começar o dia e precisar de uma varredura de itens relevantes em e-mail, agenda e contratos, ao pesquisar uma questão jurídica específica em fontes internas, ou quando uma situação em desenvolvimento (vazamento de dados, ameaça de litígio, consulta regulatória) exigir contexto rápido.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/skills/brief
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: pt
---

# /brief -- Briefing do Time Jurídico

> Se você ver placeholders desconhecidos ou precisar checar quais ferramentas estão conectadas, veja [CONNECTORS.md](../../CONNECTORS.md).

Gera briefings contextuais para o trabalho jurídico. Suporta três modos: briefing diário, briefing temático e briefing de incidente.

**Importante**: Este comando auxilia em fluxos jurídicos, mas não fornece aconselhamento jurídico. Os briefings devem ser revisados por profissionais do direito habilitados antes de serem utilizados.

## Invocação

```
/brief daily              # Briefing matinal de itens relevantes
/brief topic [consulta]    # Briefing de pesquisa sobre uma questão jurídica específica
/brief incident [tema]     # Briefing rápido sobre uma situação em desenvolvimento
```

Se nenhum modo for especificado, pergunte ao usuário qual tipo de briefing ele precisa.

## Modos

---

### Briefing Diário

Um resumo matinal de tudo que um membro do time jurídico precisa saber para começar o dia.

#### Fontes a Verificar

Verifique cada fonte conectada em busca de itens relevantes:

**E-mail (se conectado):**
- Novas solicitações de contrato ou revisão
- Dúvidas ou relatos de compliance
- Respostas de contrapartes em negociações ativas
- Itens sinalizados ou urgentes da caixa de entrada jurídica
- Comunicações de advogados externos
- Newsletters regulatórias ou de atualização jurídica

**Agenda (se conectada):**
- Reuniões de hoje que exigem preparo jurídico (reuniões de conselho, revisões de operação, calls com fornecedores)
- Prazos da semana (vencimento de contratos, prazos de protocolo, prazos de resposta)
- Reuniões recorrentes do time jurídico

**Chat (se conectado):**
- Mensagens da madrugada em canais do time jurídico
- Mensagens diretas solicitando input jurídico
- Menções a temas jurídicos (contrato, compliance, privacidade, NDA, termos)
- Escalonamentos ou solicitações urgentes

**CLM (se conectado):**
- Contratos aguardando revisão ou assinatura
- Vencimentos se aproximando (próximos 30 dias)
- Acordos recém-celebrados

**CRM (se conectado):**
- Negócios avançando para etapas que exigem envolvimento jurídico
- Novas oportunidades sinalizadas para revisão jurídica

#### Formato de Saída

```
## Briefing Jurídico Diário -- [Data]

### Urgente / Ação Necessária
[Itens que exigem atenção imediata, ordenados por urgência]

### Pipeline de Contratos
- **Aguardando sua Revisão**: [quantidade e lista]
- **Aguardando Resposta da Contraparte**: [quantidade e lista]
- **Prazos se Aproximando**: [itens com vencimento esta semana]

### Novas Solicitações
[Solicitações de revisão contratual, NDA ou dúvidas de compliance recebidas desde o último briefing]

### Agenda de Hoje
[Reuniões com relevância jurídica e qual preparo é necessário]

### Atividade do Time
[Mensagens ou atualizações importantes dos canais do time jurídico]

### Prazos da Semana
[Prazos e datas de protocolo próximos]

### Fontes Indisponíveis
[Quaisquer fontes que não estavam conectadas ou retornaram erro]
```

---

### Briefing Temático

Pesquisa e briefing sobre uma questão ou tema jurídico específico em todas as fontes disponíveis.

#### Fluxo de Trabalho

1. Aceite a consulta temática do usuário
2. Pesquise nas fontes conectadas:
   - **Documentos**: Memorandos internos, análises anteriores, playbooks, precedentes
   - **E-mail**: Comunicações anteriores sobre o tema
   - **Chat**: Discussões do time sobre o tema
   - **CLM**: Contratos ou cláusulas relacionadas
3. Sintetize os achados em um briefing estruturado

#### Formato de Saída

```
## Briefing Temático: [Tema]

### Resumo
[Resumo executivo de 2-3 frases dos achados]

### Histórico
[Contexto e histórico das fontes internas]

### Situação Atual
[Qual é a posição ou abordagem atual da organização, com base nos documentos disponíveis]

### Pontos-Chave
[Fatores importantes, riscos ou questões em aberto]

### Precedentes Internos
[Decisões, memorandos ou posições anteriores encontrados nas fontes internas]

### Lacunas
[Quais informações estão faltando ou quais fontes não estavam disponíveis]

### Próximos Passos Recomendados
[O que o usuário deve fazer com esta informação]
```

#### Observações Importantes
- Briefings temáticos sintetizam o que está disponível nas fontes conectadas; não substituem pesquisa jurídica formal
- Se o tema exigir jurisprudência atualizada ou doutrina, recomende que o usuário consulte uma base de pesquisa jurídica (ex.: JusBrasil, Migalhas, Revista dos Tribunais) ou um advogado externo
- Sempre indique as limitações das fontes pesquisadas

---

### Briefing de Incidente

Briefing rápido para situações em desenvolvimento que exigem atenção jurídica imediata (vazamento de dados, ameaças de litígio, consultas regulatórias, disputas de PI etc.).

#### Fluxo de Trabalho

1. Aceite o tema ou descrição do incidente
2. Varra rapidamente todas as fontes conectadas em busca de contexto relevante:
   - **E-mail**: Comunicações sobre o incidente
   - **Chat**: Discussões e escalonamentos em tempo real
   - **Documentos**: Políticas relevantes, planos de resposta, cobertura de seguro
   - **Agenda**: Reuniões de resposta agendadas
   - **CLM**: Contratos afetados, cláusulas de indenização, exigências de seguro
3. Compile em um briefing de incidente acionável

#### Formato de Saída

```
## Briefing de Incidente: [Tema]
**Preparado em**: [data/hora]
**Classificação**: [avaliação de severidade, se determinável]

### Resumo da Situação
[O que se sabe sobre o incidente]

### Linha do Tempo
[Resumo cronológico dos eventos com base nas fontes disponíveis]

### Considerações Jurídicas Imediatas
[Exigências de notificação à ANPD, obrigações de preservação de prova, questões de sigilo profissional]

### Acordos Relevantes
[Contratos, apólices de seguro ou outros acordos potencialmente envolvidos]

### Resposta Interna
[Quais ações de resposta já ocorreram, com base em e-mail/chat]

### Contatos-Chave
[Contatos internos e externos relevantes identificados nas fontes]

### Ações Imediatas Recomendadas
1. [Ação mais urgente]
2. [Segunda prioridade]
3. [etc.]

### Lacunas de Informação
[O que ainda não se sabe e precisa ser apurado]

### Fontes Verificadas
[O que foi pesquisado e o que não estava disponível]
```

#### Observações Importantes para Briefings de Incidente
- Velocidade importa. Produza o briefing rapidamente com a informação disponível, em vez de esperar informação completa
- Sinalize imediatamente qualquer obrigação de preservação de prova ou hold documental
- Anote questões de sigilo profissional (marque o briefing como confidencial / protegido por sigilo profissional, se aplicável)
- Se o incidente puder envolver vazamento de dados pessoais, sinalize os prazos de comunicação aplicáveis sob a LGPD (comunicação à ANPD e aos titulares em prazo razoável, conforme art. 48 da Lei 13.709/2018)
- Recomende o envolvimento de advogado externo se a questão for relevante

## Observações Gerais

- Se as fontes estiverem indisponíveis, destaque as lacunas claramente para que o usuário saiba o que não foi verificado
- Para briefings diários, aprenda as preferências do usuário ao longo do tempo (o que ele acha útil, o que prefere filtrar)
- Briefings devem ser acionáveis: cada item deve ter um próximo passo claro ou uma razão para estar incluído
- Mantenha os briefings concisos. Vincule aos materiais-fonte em vez de reproduzi-los integralmente
