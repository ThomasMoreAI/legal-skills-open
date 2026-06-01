---
name: legal-vendor-check
title: legal-vendor-check — Status de Acordos com Fornecedor
description: Verificar o status dos acordos existentes com um fornecedor em todos os sistemas conectados — int-evo-crm, Gmail, Notion e arquivos locais — com análise de lacunas e prazos próximos. Use ao integrar ou renovar um fornecedor, ao precisar de uma visão consolidada do que está assinado e o que está faltando (MSA, DPA, SOW), ou ao verificar vencimentos próximos e obrigações sobreviventes.
author: evolution-foundation
author_url: https://github.com/evolution-foundation/evo-nexus/tree/main/.claude/skills/legal-vendor-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: pt
---

# legal-vendor-check — Status de Acordos com Fornecedor

> **Este documento não constitui aconselhamento jurídico — relatórios de status de acordos devem ser verificados contra documentos originais por profissionais jurídicos qualificados.**
> Contatos legais: **Thaís Menezes** (contratos Brius/Etus) | **Vitor Lacerda** (jurídico Etus)

Verificar o status dos acordos existentes com um fornecedor em todos os sistemas conectados. Fornece uma visão consolidada do relacionamento jurídico.

## Acionamento

User executa `/legal-vendor-check [nome do fornecedor]` ou solicita verificar status de contratos com fornecedor.

Se nenhum nome de fornecedor for fornecido, solicitar ao usuário que especifique qual fornecedor verificar.

## Fluxo de Trabalho

### Passo 1: Identificar o Fornecedor

Aceitar o nome do fornecedor do usuário. Tratar variações comuns:
- Nome jurídico completo vs. nome comercial (ex: "Twilio Inc." vs. "Twilio")
- Abreviações (ex: "AWS" vs. "Amazon Web Services")
- Relacionamentos matriz/subsidiária (ex: "Meta" vs. "WhatsApp Business")
- Nomes em português vs. inglês (ex: "Google Brasil Internet Ltda." vs. "Google")

Perguntar ao usuário para esclarecer se o nome do fornecedor for ambíguo.

### Passo 2: Pesquisar nos Sistemas Conectados

Pesquisar o fornecedor em todos os sistemas disponíveis conectados, em ordem de prioridade:

#### int-evo-crm — Se Conectado
Pesquisar o registro do fornecedor/conta:
- Status da conta e tipo de relacionamento
- Informações de contato da equipe jurídica/contratos do fornecedor
- Oportunidades ou negócios associados

#### Gmail (via MCP) — Se Conectado
Pesquisar correspondência relevante recente:
- Emails relacionados a contratos (últimos 6 meses)
- Anexos de NDA ou acordo
- Tópicos de negociação
- Comunicações sobre renovação ou aditivos

#### Documentos locais / Notion — Se Disponível
Pesquisar:
- Acordos executados (MSA, NDA, SOW, DPA, SLA)
- Redlines e rascunhos
- Materiais de due diligence
- Certificados de seguro

#### Discord (canais jurídicos/operações) — Se Relevante
Pesquisar menções recentes (últimos 3 meses):
- Solicitações de contrato envolvendo este fornecedor
- Questões jurídicas sobre o fornecedor
- Discussões relevantes da equipe

#### Linear / GitHub (via MCP) — Se Relevante
Verificar:
- Issues relacionadas a este fornecedor (integrações, SLAs, incidentes)
- PRs ou funcionalidades que dependem de acordos com o fornecedor

### Passo 3: Compilar Status dos Acordos

Para cada acordo encontrado, relatar:

| Campo | Detalhes |
|-------|---------|
| **Tipo de Acordo** | NDA, MSA/Contrato-Mestre, SOW, DPA/Contrato de Processamento de Dados, SLA, Contrato de Licença, etc. |
| **Status** | Ativo, Vencido, Em Negociação, Aguardando Assinatura |
| **Data de Vigência** | Quando o acordo começou |
| **Data de Vencimento** | Quando vence ou renova |
| **Renovação Automática** | Sim/Não, com prazo de renovação e período de aviso prévio |
| **Termos Principais** | Teto de responsabilidade, lei aplicável, disposições de rescisão |
| **Aditivos** | Quaisquer aditivos ou adendos arquivados |
| **Localização** | Onde a cópia executada está armazenada |

### Passo 4: Análise de Lacunas

Identificar quais acordos existem e o que pode estar faltando:

```
## Cobertura de Acordos

[CHECK] NDA — [status]
[CHECK/FALTANDO] MSA / Contrato-Mestre — [status ou "Não encontrado"]
[CHECK/FALTANDO] DPA / Contrato de Processamento de Dados (LGPD) — [status ou "Não encontrado"]
[CHECK/FALTANDO] SOW(s) / Escopo de Trabalho — [status ou "Não encontrado"]
[CHECK/FALTANDO] SLA / Acordo de Nível de Serviço — [status ou "Não encontrado"]
[CHECK/FALTANDO] Certificado de Seguro — [status ou "Não encontrado"]
```

Sinalizar quaisquer lacunas que possam ser necessárias com base no tipo de relacionamento:
- Se há MSA mas sem DPA e o fornecedor trata dados pessoais → **CRÍTICO sob a LGPD**
- Se há SOW mas sem MSA → risco de falta de termos-mestre regulando a relação
- Se fornecedor acessa sistemas internos mas sem acordo de segurança → risco operacional/jurídico

#### Verificações LGPD para Fornecedores

Para qualquer fornecedor que trata dados pessoais de titulares brasileiros, verificar especificamente:
- [ ] Contrato de Processamento de Dados (art. 37 LGPD) está em vigor?
- [ ] Base legal de tratamento está identificada e documentada?
- [ ] Suboperadores do fornecedor estão listados e aprovados?
- [ ] Mecanismo de transferência internacional está válido (se dados saem do Brasil)?
- [ ] Prazo de notificação de incidente está dentro do exigido (orientação ANPD: 72h para riscos graves)?
- [ ] Obrigações de devolução/destruição de dados na rescisão estão definidas?

### Passo 5: Gerar Relatório

```
## Status de Acordos com Fornecedor: [Nome do Fornecedor]

**Data da Verificação**: [data de hoje]
**Fontes Verificadas**: [lista de sistemas pesquisados]
**Fontes Não Disponíveis**: [lista de sistemas não conectados, se houver]

## Visão Geral do Relacionamento

**Fornecedor**: [razão social completa + CNPJ se conhecido]
**Tipo de Relacionamento**: [fornecedor/parceiro/cliente/etc.]
**Status no CRM**: [se disponível]
**Trata Dados Pessoais**: [Sim/Não — se Sim, verificar DPA]

## Resumo dos Acordos

### [Tipo de Acordo 1] — [Status]
- **Vigência**: [data]
- **Vence**: [data] ([renova automaticamente / não renova automaticamente])
- **Aviso de não-renovação**: [prazo]
- **Termos Principais**: [resumo dos termos materiais]
- **Localização**: [onde a cópia executada está armazenada]

### [Tipo de Acordo 2] — [Status]
[etc.]

## Análise de Lacunas

[O que está em vigor vs. o que pode ser necessário]

## Alertas de Conformidade LGPD

[Verificações específicas de proteção de dados — se aplicável]

## Ações Próximas

- [Quaisquer vencimentos ou prazos de renovação se aproximando]
- [Acordos obrigatórios ainda não existentes]
- [Aditivos ou atualizações que podem ser necessários]
- [Alertas: vencimentos em 90 dias ou menos devem ser configurados no Google Calendar]

## Observações

[Qualquer contexto relevante das buscas em email/Discord]
```

### Passo 6: Tratar Fontes Ausentes

Se sistemas-chave não estiverem conectados via MCP:

- **Sem CRM (int-evo-crm)**: Registrar que o CRM não foi verificado. Sugerir ao usuário verificar manualmente. Relatar o que foi encontrado em outros sistemas.
- **Sem Gmail**: Registrar que o email não foi pesquisado. Sugerir ao usuário pesquisar seu email por "[nome do fornecedor] contrato" ou "[nome do fornecedor] NDA".
- **Sem Documentos/Notion**: Registrar que o armazenamento de documentos não foi pesquisado. Sugerir verificação manual das pastas de contratos.

Sempre declarar claramente quais fontes foram verificadas e quais não foram, para que o usuário saiba a completude do relatório.

## Gestão Proativa de Renovações

Ao identificar contratos próximos do vencimento, recomendar:

| Prazo até Vencimento | Ação Recomendada |
|---------------------|-----------------|
| > 90 dias | Registrar no calendário; monitorar |
| 60-90 dias | Iniciar revisão interna; decidir renovar/renegociar/encerrar |
| 30-60 dias | Contatar fornecedor para renovação; escalar para Thaís se negociação |
| < 30 dias | Ação urgente — escalar imediatamente para Thaís Menezes ou Vitor Lacerda |

**Ação**: Para cada contrato com vencimento em 90 dias ou menos, oferecer configurar lembrete no Google Calendar (via MCP).

## Notas

- Se nenhum acordo for encontrado em nenhum sistema conectado, relatar isso claramente e perguntar ao usuário se tem acordos armazenados em outro lugar
- Para grupos de fornecedores (ex: fornecedor com múltiplas subsidiárias), perguntar se o usuário quer verificar uma entidade específica ou o grupo inteiro
- Sinalizar quaisquer acordos vencidos que ainda podem ter obrigações sobreviventes (confidencialidade, indenização, proteção de dados — que podem sobreviver à rescisão sob a LGPD)
- Se um acordo está se aproximando do vencimento (dentro de 90 dias), destacar isso de forma proeminente
- **Este documento não constitui aconselhamento jurídico.** Contatos: Thaís Menezes | Vitor Lacerda
