---
name: legal-signature-request
title: legal-signature-request — Encaminhamento para Assinatura
description: Preparar e encaminhar um documento para assinatura eletrônica — executar checklist pré-assinatura, configurar ordem de assinatura e enviar para execução. Use quando um contrato está finalizado e pronto para assinar, ao verificar nomes de entidades, anexos e blocos de assinatura antes de enviar, ou ao configurar um envelope com signatários sequenciais ou paralelos.
author: evolution-foundation
author_url: https://github.com/evolution-foundation/evo-nexus/tree/main/.claude/skills/legal-signature-request
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: pt
---

# legal-signature-request — Encaminhamento para Assinatura

> **Este documento não constitui aconselhamento jurídico — verifique se os documentos estão na forma final antes de enviar para assinatura.**
> Contatos legais: **Thaís Menezes** (contratos Brius/Etus) | **Vitor Lacerda** (jurídico Etus)

Preparar um documento para assinatura eletrônica — verificar completude, configurar ordem de assinatura e encaminhar para execução.

## Acionamento

User executa `/legal-signature-request` ou solicita encaminhar documento para assinatura.

## Fluxo de Trabalho

### Passo 1: Aceitar o Documento

Aceitar o documento em qualquer formato:
- **Upload de arquivo**: PDF, DOCX
- **Arquivo local / Notion**: Link para o documento em armazenamento local ou página Notion
- **Referência**: "O MSA com a Acme Corp que finalizamos ontem"

Se nenhum documento for fornecido, solicitar ao usuário que o forneça.

### Passo 2: Checklist Pré-Assinatura

Antes de encaminhar para assinatura, verificar:

```markdown
## Checklist Pré-Assinatura

- [ ] Documento está na forma final e acordada (sem redlines abertos)
- [ ] Todos os anexos e cronogramas estão incluídos
- [ ] Nomes de entidades jurídicas corretos nos blocos de assinatura
- [ ] Razão social completa conforme CNPJ (ex: "Evolution API LTDA" não apenas "Evolution")
- [ ] Datas corretas ou em branco para a data de execução
- [ ] Blocos de assinatura correspondem aos signatários autorizados
- [ ] Quaisquer aprovações internas obrigatórias foram obtidas
- [ ] Documento foi revisado por assessoria adequada (Thaís ou Vitor, conforme o caso)
- [ ] Versão do documento confirmada como definitiva (sem versões anteriores em aberto)
```

### Passo 3: Configurar a Assinatura

Coletar detalhes de assinatura:
- **Signatários**: Quem precisa assinar? (nomes, emails, cargos, poderes de representação)
- **Ordem de assinatura**: Sequencial ou paralela?
- **Aprovação interna**: Alguém precisa aprovar antes que a contraparte assine?
- **Destinatários em cópia**: Quem deve receber uma cópia do documento executado?
- **Validade jurídica**: Verificar se assinatura eletrônica é suficiente ou se é necessária assinatura qualificada (certificado ICP-Brasil)

#### Verificação de Poderes de Representação

Antes de enviar, verificar:
- O signatário interno tem poderes para assinar em nome da empresa (contrato social, procuração, ata)?
- Para contratos acima de determinado valor, Davidson Gomes precisa assinar?
- O signatário da contraparte tem poderes comprovados?
- Para contratos públicos ou com entidades governamentais: verificar requisitos específicos

### Passo 4: Encaminhar para Assinatura

**Se DocuSign MCP estiver conectado:**
- Criar o envelope/solicitação de assinatura no DocuSign
- Configurar campos de assinatura e ordem
- Adicionar quaisquer campos obrigatórios de rubrica ou data
- Enviar para assinatura

**Se DocuSign não estiver conectado:**
- Gerar documento de instrução de assinatura
- Fornecer o documento formatado para assinatura manual ou assinatura eletrônica simples
- Listar todos os signatários com informações de contato
- Orientar sobre o envio via Gmail (MCP) com instruções claras
- Registrar no sistema de controle de contratos (arquivo local / Notion)

#### Tipos de Assinatura Eletrônica no Brasil (Lei 14.063/2020)

| Tipo | Descrição | Adequado Para |
|------|-----------|---------------|
| **Simples** | Email + token, DocuSign padrão | Contratos comerciais de baixo/médio risco |
| **Avançada** | Verificação de identidade adicional | Contratos de médio/alto valor |
| **Qualificada (ICP-Brasil)** | Certificado digital A1/A3 | Contratos com órgãos públicos, certidões, documentos com fé pública |

Para contratos entre empresas privadas sem requisito legal específico, assinatura simples ou avançada via DocuSign é geralmente suficiente.

## Saída

```markdown
## Solicitação de Assinatura: [Título do Documento]

### Detalhes do Documento
- **Tipo**: [MSA / NDA / SOW / Aditivo / etc.]
- **Partes**: [Parte A] e [Parte B]
- **Páginas**: [X]
- **Tipo de Assinatura**: [Simples / Avançada / Qualificada ICP-Brasil]

### Verificação Pré-Assinatura: [APROVADO / PROBLEMAS ENCONTRADOS]
[Listar quaisquer problemas que precisam de atenção antes de enviar]

### Configuração de Assinatura
| Ordem | Signatário | Email | Cargo | Organização |
|-------|-----------|-------|-------|-------------|
| 1 | [Nome] | [email] | [Cargo/Função] | [Parte A] |
| 2 | [Nome] | [email] | [Cargo/Função] | [Parte B] |

### Destinatários em Cópia
- [Nome] — [email] — [motivo]

### Status
[Enviado para assinatura / Pronto para enviar / Problemas a resolver primeiro]

### Próximos Passos
- [O que esperar após o envio]
- [Prazo esperado para assinatura]
- [Acompanhamento se não assinado em X dias]
- [Onde arquivar o documento executado — local/Notion]
```

## Dicas

1. **Verificar nomes de entidades com cuidado** — O erro mais comum de assinatura é a razão social incorreta. Verificar sempre contra o CNPJ (Receita Federal) e o contrato social da empresa.
2. **Verificar poderes** — Garantir que cada signatário está autorizado a vincular sua organização. Em caso de dúvida, solicitar procuração ou ata que comprove os poderes.
3. **Guardar uma cópia** — Cópias executadas devem ser arquivadas em armazenamento local ou Notion imediatamente após a execução, com nomenclatura padronizada.
4. **Registro de contratos** — Após execução, atualizar o registro/controle de contratos com: data de execução, partes, valor, prazo de vigência, data de vencimento e alertas de renovação.
5. **Alertas de vencimento** — Configurar lembretes no Google Calendar (via MCP) para 90 dias, 60 dias e 30 dias antes do vencimento do contrato.

> **Este documento não constitui aconselhamento jurídico.** Contatos: Thaís Menezes | Vitor Lacerda
