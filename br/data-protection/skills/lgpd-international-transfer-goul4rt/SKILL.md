---
name: lgpd-international-transfer-goul4rt
title: Transferência Internacional de Dados
description: Set up international data transfers per LGPD Arts. 33-36 and Resolução CD/ANPD nº 19/2024 (Cláusulas-Padrão Contratuais brasileiras). Use when user asks 'transferência internacional', 'AWS US LGPD', 'cláusulas-padrão', 'SCCs Brasil', 'data residency', or onboarding any operator outside Brazil. Outputs per-vendor transfer assessment in `.lgpd/transfers/`.
author: goul4rt
author_url: https://github.com/goul4rt/lgpd-skills/tree/main/skills/lgpd-international-transfer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Transferência Internacional de Dados

Arts. 33-36 LGPD + **Resolução CD/ANPD nº 19/2024** (Cláusulas-Padrão Contratuais brasileiras).

## Hipóteses do Art. 33 (9 bases)

I. País com nível de proteção adequado (ANPD ainda não publicou lista oficial)
II. Garantias contratuais:
   (a) cláusulas contratuais específicas
   (b) **cláusulas-padrão** ← caminho mais usado, regulado pela Res. 19/2024
   (c) normas corporativas globais (BCRs)
   (d) selos/certificados/códigos de conduta
III. Cooperação jurídica internacional
IV. Proteção da vida
V. Autorização específica da ANPD
VI. Acordo de cooperação internacional
VII. Execução de política pública
VIII. Consentimento específico e destacado do titular
IX. Cumprimento de obrigação legal, contrato, etc.

## Cláusulas-Padrão (Res. 19/2024 Anexo II)

- Devem ser adotadas **integralmente, sem alteração**, exceto preenchimento de identificação
- Prazo de adoção em contratos: 12 meses (encerrou ago/2025) — atualmente obrigatório
- Estrutura: identificação, finalidades, transferências posteriores, responsabilidades, princípios, direitos do titular, medidas técnicas, lei aplicável, encerramento

## Workflow

1. Listar todos os operadores fora do Brasil (cloud US, observability, comms, etc.)
2. Para cada um, escolher hipótese do Art. 33
3. Implementar:
   - Se IIb (mais comum): assinar adendo com Cláusulas-Padrão do Anexo II
   - Se VIII: capturar consentimento específico (raro na prática)
4. Documentar em `.lgpd/transfers/{vendor}.md`
5. Citar na política de privacidade

## Template — `.lgpd/transfers/{vendor}.md`

```markdown
# Transferência Internacional — {Vendor}

- **Operador**: {nome}
- **País**: {país}
- **Finalidade**: {específica}
- **Dados transferidos**: {lista}
- **Hipótese do Art. 33**: II, (b) cláusulas-padrão
- **Cláusulas-Padrão (Res. 19/2024)**: assinadas em {data}
- **Documento**: link para PDF assinado
- **Sub-operadores autorizados**: {lista}
- **Salvaguardas adicionais**: criptografia em trânsito e em repouso, pseudonimização
- **Avaliação de adequação**: {data} — risco residual {nível}
- **Próxima revisão**: {data}
```

## Status update

```markdown
## F14b — Transferências internacionais ✓
- {N} operadores fora do BR
- {M} com cláusulas-padrão assinadas
- {X} pendentes: {lista}
- Próximo: lgpd-vendor-audit (review anual)
```
