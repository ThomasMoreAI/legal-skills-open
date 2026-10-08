---
name: lgpd-dpa-goul4rt
title: DPA — Data Processing Agreement (Art. 39 LGPD)
description: Draft and review Data Processing Agreements (DPA) with operadores under LGPD Art. 39. Use when user mentions 'DPA', 'contrato com operador', 'cláusulas LGPD', 'data processing agreement', or onboarding a new third-party service (analytics, cloud, payment, email, SMS, observability). Outputs DPA template + per-vendor sheets in `.lgpd/vendors/`.
author: goul4rt
author_url: https://github.com/goul4rt/lgpd-skills/tree/main/skills/lgpd-dpa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# DPA — Data Processing Agreement (Art. 39 LGPD)

Contrato entre controlador e operador. Sem cláusulas adequadas, controlador responde pelo operador (Art. 42).

## Cláusulas mínimas

1. **Identificação das partes** e papel de cada uma
2. **Objeto** — finalidade do tratamento pelo operador
3. **Instruções do controlador** — operador trata SOMENTE conforme instruções (Art. 39)
4. **Confidencialidade** — funcionários sob NDA
5. **Medidas de segurança** — listadas ou referenciadas
6. **Sub-operadores** — autorização prévia + responsabilidade solidária
7. **Auxílio a direitos do titular** — operador colabora em DSAR no SLA do controlador
8. **Incidentes de segurança** — operador notifica controlador imediatamente (recomendado: 24h máx)
9. **Devolução/eliminação** ao fim do contrato
10. **Auditoria** — direito do controlador auditar operador
11. **Responsabilidade** — Art. 42 LGPD aplica
12. **Transferência internacional** — se houver, cláusulas Res. 19/2024

## Template

Ver `assets/dpa-template.md`.

## Vendors comuns e seus DPAs públicos

| Vendor | DPA público | Cláusulas BR | Ação |
|---|---|---|---|
| AWS | sim — AWS GDPR DPA + adendo BR | parcial | adotar cláusulas Res. 19/2024 |
| GCP | sim | parcial | mesmo |
| Datadog | sim | não | exigir adendo BR |
| Stripe | sim | sim | revisar para LGPD |
| Discord | termos de serviço | não | considerar contato direto se uso for comercial |
| Sentry | sim | parcial | exigir adendo |

## Workflow

1. Liste operadores ativos (input de `lgpd-vendor-audit`)
2. Para cada um:
   - Existe DPA assinado?
   - Cobre os 12 itens?
   - Inclui transferência internacional se aplicável?
3. Para faltantes: enviar template de DPA
4. Salvar em `.lgpd/vendors/{vendor}.md`
5. Manter renovação anual em calendário

## Status update

```markdown
## F14 — DPA ✓
- {N} operadores ativos
- {M} com DPA assinado e aderente
- {X} pendentes: {lista}
- Próximo: lgpd-international-transfer
```
