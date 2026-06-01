---
name: legal-meeting-briefing-evolution-foundation
title: legal-meeting-briefing — Briefing para Reunião Jurídica
description: Preparar briefings estruturados para reuniões com relevância jurídica e rastrear itens de ação resultantes. Use ao preparar negociações de contratos, reuniões de conselho, revisões de conformidade, ou qualquer reunião onde contexto jurídico, pesquisa de antecedentes ou acompanhamento de ações seja necessário.
author: evolution-foundation
author_url: https://github.com/evolution-foundation/evo-nexus/tree/main/.claude/skills/legal-meeting-briefing
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: pt
---

# legal-meeting-briefing — Briefing para Reunião Jurídica

> **Este documento não constitui aconselhamento jurídico — consulte o assessor jurídico habilitado antes de tomar decisões com base nesta análise.**
> Contatos legais: **Thaís Menezes** (contratos Brius/Etus) | **Vitor Lacerda** (jurídico Etus)

Reunir contexto de fontes conectadas, preparar briefings estruturados para reuniões com relevância jurídica e ajudar a rastrear itens de ação que surgem das reuniões.

Os briefings devem ser revisados quanto a precisão e completude antes do uso.

## Acionamento

User executa `/legal-meeting-briefing` ou solicita preparar briefing para reunião jurídica.

## Metodologia de Preparação para Reunião

### Passo 1: Identificar a Reunião

Determinar o contexto da reunião a partir da solicitação do usuário ou do Google Calendar:
- **Título e tipo da reunião**: Que tipo de reunião é esta? (revisão de negócio, reunião de conselho, chamada com fornecedor, sincronização de equipe, reunião com cliente, discussão regulatória)
- **Participantes**: Quem estará presente? Quais são seus papéis e interesses?
- **Pauta**: Existe uma pauta formal? Quais tópicos serão abordados?
- **Seu papel**: Qual é o papel do membro da equipe jurídica nesta reunião? (assessor, apresentador, observador, negociador)
- **Tempo de preparação**: Quanto tempo está disponível para preparar?

### Passo 2: Avaliar as Necessidades de Preparação

Com base no tipo de reunião, determinar o que é necessário:

| Tipo de Reunião | Necessidades Principais de Preparação |
|---|---|
| **Revisão de Negócio** | Status do contrato, questões em aberto, histórico da contraparte, estratégia de negociação, requisitos de aprovação |
| **Conselho / Comitê** | Atualizações jurídicas, destaques do registro de riscos, questões pendentes, desenvolvimentos regulatórios, rascunhos de resolução |
| **Chamada com Fornecedor** | Status do acordo, questões em aberto, métricas de desempenho, histórico do relacionamento, objetivos de negociação |
| **Sincronização de Equipe** | Status da carga de trabalho, questões prioritárias, necessidades de recursos, prazos próximos |
| **Cliente / Customer** | Termos do acordo, histórico de suporte, questões em aberto, contexto do relacionamento |
| **Regulatório / Governo** | Antecedentes da questão, status de conformidade, comunicações anteriores, briefing de advogado |
| **Litígio / Disputa** | Status do caso, desenvolvimentos recentes, estratégia, parâmetros de acordo |
| **Interfuncional** | Implicações jurídicas de decisões de negócio, avaliação de risco, requisitos de conformidade (LGPD, CLT, etc.) |

### Passo 3: Reunir Contexto das Fontes Conectadas

Puxar informações relevantes de cada fonte conectada:

#### Google Calendar (via MCP)
- Detalhes da reunião (horário, duração, localização/link, participantes)
- Reuniões anteriores com os mesmos participantes (últimos 3 meses)
- Reuniões relacionadas ou acompanhamentos agendados
- Compromissos concorrentes ou restrições de tempo

#### Gmail (via MCP)
- Correspondência recente com ou sobre os participantes da reunião
- Tópicos de acompanhamento de reuniões anteriores
- Itens de ação abertos de interações anteriores
- Documentos relevantes compartilhados por email

#### Discord (canais relevantes)
- Discussões recentes sobre o tópico da reunião
- Mensagens de ou sobre os participantes da reunião
- Discussões da equipe sobre questões relacionadas
- Decisões relevantes ou contexto compartilhado em canais

#### Documentos locais / Notion
- Pautas de reunião e notas de reuniões anteriores
- Acordos, memorandos ou briefings relevantes
- Documentos compartilhados com os participantes da reunião
- Materiais de rascunho para a reunião

#### int-evo-crm (se relevante)
- Informações de conta ou oportunidade
- Histórico e contexto do relacionamento
- Estágio do negócio e marcos principais
- Mapa de stakeholders

#### Linear / GitHub (via MCP, para reuniões técnicas)
- Issues ou PRs relacionados a tópicos jurídicos/contratos
- Status de projetos que têm implicações contratuais

### Passo 4: Sintetizar em Briefing

Organizar as informações coletadas em um briefing estruturado (ver template abaixo).

### Passo 5: Identificar Lacunas de Preparação

Sinalizar qualquer coisa que não pôde ser encontrada ou verificada:
- Fontes que não estavam disponíveis
- Informações que parecem desatualizadas
- Questões que permanecem sem resposta
- Documentos que não puderam ser localizados

## Template de Briefing

```
## Briefing de Reunião

### Detalhes da Reunião
- **Reunião**: [título]
- **Data/Hora**: [data e hora com fuso horário — BRT (UTC-3)]
- **Duração**: [duração esperada]
- **Local**: [local físico ou link de vídeo]
- **Seu Papel**: [assessor / apresentador / negociador / observador]

### Participantes
| Nome | Organização | Função | Interesses Principais | Observações |
|---|---|---|---|---|
| [nome] | [org] | [função] | [o que eles se importam] | [contexto relevante] |

### Pauta / Tópicos Esperados
1. [Tópico 1] — [breve contexto]
2. [Tópico 2] — [breve contexto]
3. [Tópico 3] — [breve contexto]

### Contexto e Antecedentes
[Resumo de 2-3 parágrafos do histórico relevante, estado atual e por que esta reunião está acontecendo]

### Documentos Principais
- [Documento 1] — [breve descrição e onde encontrar — local/Notion]
- [Documento 2] — [breve descrição e onde encontrar]

### Questões em Aberto
| Questão | Status | Responsável | Prioridade | Observações |
|---|---|---|---|---|
| [questão 1] | [status] | [quem] | [A/M/B] | [contexto] |

### Considerações Jurídicas
[Questões, riscos ou considerações jurídicas específicas relevantes para os tópicos da reunião]

### Pontos de Discussão
1. [Ponto-chave a levantar, com contexto de suporte]
2. [Ponto-chave a levantar, com contexto de suporte]
3. [Ponto-chave a levantar, com contexto de suporte]

### Perguntas a Levantar
- [Pergunta 1] — [por que isso importa]
- [Pergunta 2] — [por que isso importa]

### Decisões Necessárias
- [Decisão 1] — [opções e recomendação]
- [Decisão 2] — [opções e recomendação]

### Linhas Vermelhas / Não Negociáveis
[Se esta é uma reunião de negociação: posições que não podem ser concedidas]

### Acompanhamento de Reunião Anterior
[Itens de ação pendentes de reuniões anteriores com estes participantes]

### Lacunas de Preparação
[Informações que não puderam ser encontradas ou verificadas; perguntas para o usuário]
```

## Orientação Específica por Tipo de Reunião

### Reuniões de Revisão de Negócio

Seções adicionais do briefing:
- **Resumo do negócio**: Partes, valor, estrutura, cronograma
- **Status do contrato**: Onde está no processo de revisão/negociação; questões pendentes
- **Requisitos de aprovação**: Quais aprovações são necessárias e de quem (incluindo Davidson Gomes se valor > limiar)
- **Dinâmica da contraparte**: Suas posições prováveis, comunicações recentes, temperatura do relacionamento
- **Negócios comparáveis**: Transações similares anteriores e seus termos (se disponíveis)

### Reuniões de Conselho e Comitê

Seções adicionais do briefing:
- **Atualização do departamento jurídico**: Resumo de questões, ganhos, novas questões, questões encerradas
- **Destaques de risco**: Principais riscos do registro de riscos com mudanças desde o último relatório
- **Atualização regulatória**: Desenvolvimentos regulatórios materiais que afetam o negócio (LGPD, ANPD, CLT, regulamentações setoriais)
- **Aprovações pendentes**: Resoluções ou aprovações necessárias do conselho/comitê
- **Resumo de litígios**: Questões ativas, provisões, acordos, novos processos

### Reuniões Regulatórias / Governamentais

Seções adicionais do briefing:
- **Contexto do órgão regulatório**: Qual regulador (ANPD, PROCON, CADE, Receita Federal, MP, TCU), qual divisão, suas prioridades atuais e padrões de enforcement
- **Histórico da questão**: Interações anteriores, submissões, linha do tempo de correspondência
- **Postura de conformidade**: Status de conformidade atual nos tópicos relevantes (LGPD, Marco Civil, CLT, etc.)
- **Coordenação com advogado**: Envolvimento de Thaís Menezes ou Vitor Lacerda, assessoria anterior recebida
- **Considerações de privilégio**: O que pode e não pode ser discutido; quaisquer riscos de privilégio

## Rastreamento de Itens de Ação

### Durante/Após a Reunião

Ajudar o usuário a capturar e organizar itens de ação da reunião:

```
## Itens de Ação de [Nome da Reunião] — [Data]

| # | Item de Ação | Responsável | Prazo | Prioridade | Status |
|---|---|---|---|---|---|
| 1 | [tarefa específica e acionável] | [nome] | [data] | [A/M/B] | Aberto |
| 2 | [tarefa específica e acionável] | [nome] | [data] | [A/M/B] | Aberto |
```

### Melhores Práticas para Itens de Ação

- **Seja específico**: "Enviar redline da Seção 4.2 ao advogado da contraparte" não "Acompanhar contrato"
- **Designar responsável**: Cada item de ação deve ter exatamente um responsável (não uma equipe ou grupo)
- **Definir prazo**: Cada item de ação precisa de uma data específica, não "em breve" ou "o quanto antes"
- **Registrar dependências**: Se um item de ação depende de outro ou de input externo, registrar
- **Distinguir tipos**:
  - Ações da equipe jurídica (coisas que a equipe precisa fazer)
  - Ações da equipe de negócios (coisas a comunicar aos stakeholders)
  - Ações externas (coisas que a contraparte ou Thaís/Vitor precisam fazer)
  - Reuniões de acompanhamento (reuniões que precisam ser agendadas no Google Calendar)

### Acompanhamento

Após a reunião:
1. **Distribuir itens de ação** a todos os participantes (via Gmail ou Discord conforme adequado)
2. **Configurar lembretes no Google Calendar** para prazos
3. **Atualizar sistemas relevantes** (int-evo-crm, Linear, Notion/arquivos locais) com resultados da reunião
4. **Arquivar notas da reunião** no local de documento adequado (Notion ou pasta local)
5. **Sinalizar itens urgentes** que precisam de atenção imediata — Thaís ou Vitor se jurídico

### Cadência de Acompanhamento

- **Itens de alta prioridade**: Verificar diariamente até concluídos
- **Itens de média prioridade**: Verificar na próxima sincronização da equipe ou revisão semanal
- **Itens de baixa prioridade**: Verificar na próxima reunião agendada ou revisão mensal
- **Itens atrasados**: Escalar para o responsável; sinalizar na próxima reunião relevante

> **Este documento não constitui aconselhamento jurídico.** Contatos: Thaís Menezes | Vitor Lacerda
