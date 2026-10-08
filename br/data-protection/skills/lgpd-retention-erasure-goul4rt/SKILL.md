---
name: lgpd-retention-erasure-goul4rt
title: Retention & Erasure
description: Define retention rules and erasure mechanisms (LGPD Arts. 15-16) reconciling subject's right to erasure (Art. 18, VI) with legal retention obligations (fiscal, labor, banking). Use when user asks 'retenção LGPD', 'quanto tempo guardar', 'eliminação de dados', 'soft delete vs hard delete', 'crypto-shredding', 'right to be forgotten'.
author: goul4rt
author_url: https://github.com/goul4rt/lgpd-skills/tree/main/skills/lgpd-retention-erasure
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Retention & Erasure

Arts. 15-16 LGPD definem o término do tratamento. Art. 18, VI dá direito à eliminação. A tensão prática é com **retenções legais obrigatórias**.

## Hierarquia de obrigações

```
Retenção legal obrigatória > Retenção contratual > Vontade do titular (Art. 18, VI)
```

Quando há obrigação legal de manter (fiscal, trabalhista, bancário, Marco Civil), o tratamento continua **bloqueado** (não usado para finalidade original) até o fim do prazo legal, depois é eliminado.

## Prazos comuns no Brasil

| Categoria | Prazo | Fonte |
|---|---|---|
| Fiscal (notas, impostos) | 5 anos | CTN Art. 173-174 |
| Trabalhista (contratos, folha) | 5 anos | CLT Art. 11 |
| Previdenciária | 10 anos | Lei 8.212/91 |
| Bancário | 10 anos | CMN |
| Marco Civil — logs de conexão | 1 ano | Lei 12.965/2014 Art. 13 |
| Marco Civil — logs de acesso a apps | 6 meses | Lei 12.965/2014 Art. 15 |
| CDC — relação de consumo | 5 anos | CDC Art. 27 (prescrição) |

## Estratégias de eliminação

### 1. Hard delete
Quando não há retenção legal. Cascata bem definida em todas as tabelas + replicas + backups quando possível.

### 2. Soft delete + bloqueio
Quando há retenção legal de **alguns campos**. Marcar `deletedAt`, mascarar campos não-essenciais, manter apenas o estritamente necessário.

### 3. Crypto-shredding
Quando há volume e dificuldade de varrer storage. Dados cifrados por chave do titular; eliminação = destrói a chave.

### 4. Anonimização
Substituto à eliminação. Após anonimizar (irreversivelmente), dado sai do escopo da LGPD (Art. 12).

## Schema Prisma

```prisma
model RetentionRule {
  id              String   @id @default(cuid())
  entity          String   // "User", "Order", "Message"
  purpose         String   // "marketing", "billing"
  retentionMonths Int
  legalBasis      String
  postAction      PostRetentionAction
  triggeredBy     String   // "consent_revoked", "contract_end", "ttl"
  active          Boolean  @default(true)
}

enum PostRetentionAction {
  HARD_DELETE
  ANONYMIZE
  CRYPTO_SHRED
  BLOCK_AND_RETAIN
}
```

## Job de eliminação automática

Cron job diário:
1. Identifica registros que ultrapassaram retenção
2. Aplica `postAction` conforme `RetentionRule`
3. Loga em `AuditLogEntry`
4. Notifica relatório semanal ao Encarregado

## Workflow para Art. 18, VI

Ver detalhes no skill `lgpd-dsar`. Resumo:
1. Recebe pedido
2. Verifica retenção legal
3. Se ZERO retenção → hard delete
4. Se PARCIAL → soft delete + crypto-shred dos campos elimináveis
5. Loga
6. Responde titular informando o que foi eliminado e o que foi bloqueado (com prazo)

## Status update

```markdown
## F8 — Retention ✓
- RetentionRules configuradas: {N}
- Job diário ativo
- Eliminação automatizada validada em ambiente staging
- {M} registros já em fila para eliminação
- Próximo: lgpd-incident-response
```
