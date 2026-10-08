---
name: lgpd-ropa-goul4rt
title: ROPA — Registro de Operações de Tratamento
description: Generate and maintain the Registro de Operações de Tratamento de Dados Pessoais (ROPA) required by LGPD Art. 37. Use when user asks for "ROPA", "registro de operações", "registro de tratamento", or as part of the lgpd-audit pipeline. Consolidates input from `lgpd-data-mapping` and `lgpd-legal-basis` into the official ANPD template structure. Especially relevant when preparing for ANPD inspection or onboarding a new vendor that requests the ROPA.
author: goul4rt
author_url: https://github.com/goul4rt/lgpd-skills/tree/main/skills/lgpd-ropa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# ROPA — Registro de Operações de Tratamento

Art. 37 LGPD: "O controlador e o operador devem manter registro das operações de tratamento de dados pessoais que realizarem, **especialmente quando baseado no legítimo interesse**."

## Pré-requisitos

- `.lgpd/data-map.md` preenchido (`lgpd-data-mapping`)
- `.lgpd/legal-basis.md` preenchido (`lgpd-legal-basis`)
- Encarregado designado (`lgpd-dpo-encarregado`)

Se faltar algum, execute a skill correspondente antes.

## Modelo base — ANPD para ATPP (8 campos)

A ANPD publicou em 14/jun/2023 modelo simplificado para Agentes de Tratamento de Pequeno Porte. Use-o como **mínimo**; controladores maiores devem expandir.

### Campos obrigatórios

1. Informações de contato (controlador, operador, encarregado)
2. Categorias de titulares
3. Categorias de dados pessoais
4. Compartilhamento de dados
5. Medidas de segurança
6. Período de armazenamento (retenção)
7. Operação realizada (atividade + finalidade + hipótese legal)
8. Observações

### Campos adicionais (recomendados para controladores fora de ATPP)

9. Avaliação de risco (link para RIPD se houver)
10. Transferência internacional (link para `.lgpd/transfers/`)
11. Fonte dos dados
12. Decisão automatizada presente?
13. Evidências de segurança (políticas, ISO, SOC2)

## Template — `.lgpd/ROPA.md`

Ver `assets/ropa-template.md` para o template completo.

## Workflow

1. Leia `data-map.md` e `legal-basis.md`.
2. Para cada atividade no data map, gere uma linha no ROPA.
3. Liste **separadamente** atividades como controlador vs. como operador.
4. Inclua atividades baseadas em legítimo interesse com destaque.
5. Salve em `.lgpd/ROPA.md`.
6. **⏸ CHECKPOINT**: peça revisão do Encarregado / jurídico antes de considerar v1 final.
7. Configure revisão semestral em calendário.

## Quem precisa ter ROPA?

- **Todo controlador e todo operador** (Art. 37 — sem exceção formal).
- ATPP pode usar formato simplificado da ANPD (Res. 2/2022).
- Pessoa natural com tratamento não-econômico está fora do escopo da LGPD (Art. 4º, I).

## Quem pode pedir o ROPA?

- ANPD (em fiscalização)
- Titulares (em DSAR — Art. 19 — eles têm direito a saber as finalidades e compartilhamentos)
- Operadores (durante due diligence — pode pedir versão pública)
- Auditores

Manter versão pública (sem segredos comerciais/IP) é boa prática.

## Versionamento

- ROPA é **vivo**. Versione com Git.
- Toda nova atividade, mudança de finalidade ou novo operador → nova versão do ROPA.
- Header do arquivo deve ter: versão, data, changelog resumido.

## Status update

```markdown
## F10 — ROPA ✓
- ROPA v1.0 publicado em `.lgpd/ROPA.md`
- {N} atividades como controlador
- {M} atividades como operador
- Revisão semestral agendada para {data}
- Próximo: lgpd-dpo-encarregado
```
