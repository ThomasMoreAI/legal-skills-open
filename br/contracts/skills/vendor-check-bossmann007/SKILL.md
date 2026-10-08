---
name: vendor-check-bossmann007
title: /vendor-check -- Status de Acordos com Fornecedor
description: Verifica o status de acordos existentes com um fornecedor em todos os sistemas conectados — CLM, CRM, e-mail e armazenamento de documentos — com análise de lacunas e prazos próximos. Use ao integrar ou renovar um fornecedor, quando precisar de visão consolidada do que está assinado e do que falta (MSA, Acordo de Tratamento de Dados, SOW), ou ao checar vencimentos próximos e obrigações remanescentes.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/skills/vendor-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# /vendor-check -- Status de Acordos com Fornecedor

> Se você encontrar placeholders desconhecidos ou precisar checar quais ferramentas estão conectadas, veja [CONNECTORS.md](../../CONNECTORS.md).

Verifica o status de acordos existentes com um fornecedor em todos os sistemas conectados. Fornece visão consolidada do relacionamento jurídico.

**Importante**: Este comando auxilia em fluxos jurídicos mas não substitui aconselhamento jurídico. Relatórios de status de acordo devem ser verificados contra os documentos originais por profissional habilitado (OAB).

## Invocação

```
/vendor-check [nome do fornecedor]
```

Se nenhum nome de fornecedor for informado, peça ao usuário que especifique qual fornecedor checar.

## Workflow

### Etapa 1: Identificar o Fornecedor

Aceite o nome do fornecedor informado pelo usuário. Trate variações comuns:
- Razão social vs. nome fantasia
- Abreviações
- Relações de controladora/controlada

Peça esclarecimento ao usuário se o nome do fornecedor for ambíguo.

### Etapa 2: Buscar nos Sistemas Conectados

Busque o fornecedor em todos os sistemas conectados disponíveis, em ordem de prioridade:

#### CLM (Gestão de Ciclo de Vida Contratual) -- Se Conectado
Busque todos os contratos envolvendo o fornecedor:
- Acordos ativos
- Acordos vencidos (últimos 3 anos)
- Acordos em negociação ou pendentes de assinatura
- Aditivos e termos aditivos

#### CRM -- Se Conectado
Busque o registro do fornecedor/conta:
- Status da conta e tipo de relacionamento
- Oportunidades ou negócios associados
- Dados de contato do time jurídico/contratos do fornecedor

#### E-mail -- Se Conectado
Busque correspondência recente relevante:
- E-mails relacionados a contrato (últimos 6 meses)
- Anexos de NDA ou acordo
- Threads de negociação

#### Documentos (ex.: Box, Egnyte, SharePoint) -- Se Conectado
Busque:
- Acordos executados
- Redlines e minutas
- Materiais de due diligence

#### Chat (ex.: Slack, Teams) -- Se Conectado
Busque menções recentes:
- Pedidos de contrato envolvendo este fornecedor
- Dúvidas jurídicas sobre o fornecedor
- Discussões relevantes do time (últimos 3 meses)

### Etapa 3: Compilar Status do Acordo

Para cada acordo encontrado, reporte:

| Campo | Detalhes |
|-------|---------|
| **Tipo de Acordo** | NDA, MSA, SOW, Acordo de Tratamento de Dados, SLA, Contrato de Licença, etc. |
| **Status** | Ativo, Vencido, Em Negociação, Pendente de Assinatura |
| **Data de Vigência** | Quando o acordo começou |
| **Data de Vencimento** | Quando vence ou renova |
| **Renovação Automática** | Sim/Não, com prazo de renovação e período de aviso prévio |
| **Termos-Chave** | Teto de responsabilidade, lei aplicável, foro, disposições de rescisão |
| **Aditivos** | Quaisquer aditivos em arquivo |

### Etapa 4: Análise de Lacunas

Identifique quais acordos existem e o que pode estar faltando:

```
## Cobertura de Acordos

[OK] NDA -- [status]
[OK/FALTANDO] MSA -- [status ou "Não encontrado"]
[OK/FALTANDO] Acordo de Tratamento de Dados (LGPD) -- [status ou "Não encontrado"]
[OK/FALTANDO] SOW(s) -- [status ou "Não encontrado"]
[OK/FALTANDO] SLA -- [status ou "Não encontrado"]
[OK/FALTANDO] Apólice de Seguro -- [status ou "Não encontrado"]
```

Sinalize lacunas que possam ser necessárias conforme o tipo de relacionamento (ex.: se há MSA mas não há Acordo de Tratamento de Dados e o fornecedor trata dados pessoais — exigência do art. 39 LGPD).

### Etapa 5: Gerar Relatório

Produza relatório consolidado:

```
## Status de Acordo com Fornecedor: [Nome do Fornecedor]

**Data da Busca**: [data de hoje]
**Fontes Verificadas**: [lista de sistemas buscados]
**Fontes Indisponíveis**: [lista de sistemas não conectados, se houver]

## Visão Geral do Relacionamento

**Fornecedor**: [razão social completa]
**Tipo de Relacionamento**: [fornecedor/parceiro/cliente/etc.]
**Status no CRM**: [se disponível]

## Resumo de Acordos

### [Tipo de Acordo 1] -- [Status]
- **Vigência**: [data]
- **Vencimento**: [data] ([renova automaticamente / não renova automaticamente])
- **Termos-Chave**: [resumo dos termos materiais]
- **Localização**: [onde a cópia executada está armazenada]

### [Tipo de Acordo 2] -- [Status]
[etc.]

## Análise de Lacunas

[O que está em vigor vs. o que pode ser necessário]

## Ações Próximas

- [Vencimentos ou prazos de renovação se aproximando]
- [Acordos exigidos ainda não em vigor]
- [Aditivos ou atualizações que podem ser necessários]

## Observações

[Qualquer contexto relevante de buscas em e-mail/chat]
```

### Etapa 6: Lidar com Fontes Ausentes

Se sistemas-chave não estão conectados via MCP:

- **Sem CLM**: Anote que nenhum CLM está conectado. Sugira que o usuário verifique seu CLM manualmente. Reporte o que foi encontrado em outros sistemas.
- **Sem CRM**: Pule o contexto de CRM. Anote a lacuna.
- **Sem E-mail**: Anote que o e-mail não foi buscado. Sugira que o usuário busque em seu e-mail por "[nome do fornecedor] acordo" ou "[nome do fornecedor] NDA".
- **Sem Documentos**: Anote que o armazenamento de documentos não foi buscado.

Sempre declare claramente quais fontes foram verificadas e quais não foram, para que o usuário saiba a completude do relatório.

## Observações

- Se nenhum acordo for encontrado em nenhum sistema conectado, reporte isso claramente e pergunte ao usuário se há acordos armazenados em outro lugar
- Para grupos de fornecedores (ex.: fornecedor com múltiplas subsidiárias), pergunte se o usuário quer checar uma entidade específica ou o grupo inteiro
- Sinalize acordos vencidos que ainda possam ter obrigações remanescentes (confidencialidade, indenização, etc.)
- Se um acordo está próximo do vencimento (dentro de 90 dias), destaque isso com prioridade
