---
name: signature-request-bossmann007
title: /signature-request -- Encaminhamento para Assinatura Eletrônica
description: Prepara e encaminha um documento para assinatura eletrônica — executa checklist pré-assinatura, configura ordem de assinatura, e envia para execução. Use quando um contrato está finalizado e pronto para assinar, ao verificar nomes de entidade, anexos e blocos de assinatura antes do envio, ou ao configurar envelope com signatários sequenciais ou paralelos.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/skills/signature-request
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# /signature-request -- Encaminhamento para Assinatura Eletrônica

> Se você encontrar placeholders desconhecidos ou precisar checar quais ferramentas estão conectadas, veja [CONNECTORS.md](../../CONNECTORS.md).

Prepara um documento para assinatura eletrônica — verifica completude, define ordem de assinatura e encaminha para execução.

**Importante**: Este comando auxilia em fluxos jurídicos mas não substitui aconselhamento jurídico. Verifique que os documentos estão na forma final antes de enviar para assinatura.

## Uso

```
/signature-request $ARGUMENTS
```

Preparar para assinatura: @$1

## Workflow

### Etapa 1: Aceitar o Documento

Aceite o documento em qualquer formato:
- **Upload de arquivo**: PDF, DOCX
- **URL**: Link para documento em ~~armazenamento em nuvem ou ~~CLM
- **Referência**: "O MSA da Acme Corp que finalizamos ontem"

### Etapa 2: Checklist Pré-Assinatura

Antes de encaminhar para assinatura, verifique:

```markdown
## Checklist Pré-Assinatura

- [ ] Documento está na forma final acordada (sem redlines abertos)
- [ ] Todos os anexos e exibits estão anexados
- [ ] Nomes de entidade corretos nos blocos de assinatura
- [ ] Datas corretas ou deixadas em branco para data de execução
- [ ] Blocos de assinatura correspondem aos signatários autorizados
- [ ] Aprovações internas necessárias foram obtidas
- [ ] Documento foi revisado pelo jurídico responsável
```

### Etapa 3: Configurar Assinatura

Levante os detalhes de assinatura:
- **Signatários**: Quem precisa assinar? (nomes, e-mails, cargos)
- **Ordem de assinatura**: Sequencial ou paralela?
- **Aprovação interna**: Alguém precisa aprovar antes de a contraparte assinar?
- **Cópia (CC)**: Quem deve receber cópia do documento executado?

### Etapa 4: Encaminhar para Assinatura

**Se ~~assinatura eletrônica está conectada (ICP-Brasil / Gov.br ou similar):**
- Crie o envelope/solicitação de assinatura
- Configure campos e ordem de assinatura
- Adicione campos de rubrica ou data necessários
- Envie para assinatura

**Se não conectado:**
- Gere documento de instrução de assinatura
- Forneça o documento formatado para assinatura física ou e-assinatura manual
- Liste todos os signatários com dados de contato

## Saída

```markdown
## Solicitação de Assinatura: [Título do Documento]

### Detalhes do Documento
- **Tipo**: [MSA / NDA / SOW / Aditivo / etc.]
- **Partes**: [Parte A] e [Parte B]
- **Páginas**: [X]

### Checagem Pré-Assinatura: [APROVADO / PROBLEMAS ENCONTRADOS]
[Liste quaisquer problemas que precisam de atenção antes do envio]

### Configuração de Assinatura
| Ordem | Signatário | E-mail | Papel |
|-------|--------|-------|------|
| 1 | [Nome] | [e-mail] | [Signatário Autorizado Parte A] |
| 2 | [Nome] | [e-mail] | [Signatário Autorizado Parte B] |

### Destinatários em Cópia
- [Nome] — [e-mail]

### Status
[Enviado para assinatura / Pronto para enviar / Problemas a resolver antes]

### Próximos Passos
- [O que esperar após o envio]
- [Prazo esperado de retorno]
- [Acompanhamento se não assinado em X dias]
```

## Dicas

1. **Verifique nomes de entidade com cuidado** — O erro de assinatura mais comum é nome de entidade incorreto.
2. **Verifique a autoridade** — Confirme que cada signatário está autorizado a vincular sua organização.
3. **Guarde uma cópia** — Cópias executadas devem ser arquivadas em ~~armazenamento em nuvem ou ~~CLM imediatamente após a execução. Para validade jurídica plena no Brasil, prefira assinatura com certificado ICP-Brasil (MP 2.200-2/2001) ou, quando admitida, assinatura eletrônica simples/avançada nos termos da Lei 14.063/2020 — confirme com o jurídico qual nível de assinatura é exigido para o tipo de documento. [verified: https://www.planalto.gov.br/ccivil_03/mpv/antigas_2001/2200-2.htm; https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14063.htm]
