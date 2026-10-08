---
name: legal-contract-reviewer-gonzalezpazmonica
title: legal-contract-reviewer — Revisor de Contratos
description: Revisión de contratos con matriz de riesgos RAG, red flags y resumen ejecutivo. Jurisdicción española.
author: gonzalezpazmonica
author_url: https://github.com/gonzalezpazmonica/savia/tree/main/.claude/skills/professional-domain/legal/legal-contract-reviewer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# legal-contract-reviewer — Revisor de Contratos

## Cuándo usar esta skill

- Al recibir un contrato para firma y necesitar evaluación rápida de riesgos.
- Antes de negociar términos: para identificar cláusulas inaceptables.
- En due diligence de adquisiciones: revisión de cartera contractual.
- Cuando se necesita un memorandum legal interno (no opinión jurídica externa).

## Inputs requeridos

| Campo | Descripción | Ejemplo |
|---|---|---|
| `contrato` | Texto completo o secciones relevantes | Cuerpo del NDA |
| `tipo` | Categoría del contrato | `NDA`, `servicios`, `laboral`, `compraventa` |
| `jurisdiccion` | País/comunidad autónoma aplicable | `ES` (por defecto), `CAT`, `PV` |
| `perfil_riesgo` | Postura negociadora del cliente | `conservador`, `moderado`, `agresivo` |

## Outputs producidos

1. **Matriz de riesgos** — tabla con columnas: cláusula / riesgo / probabilidad / impacto / score RAG / recomendación
2. **Lista de red flags** — cláusulas bloqueantes o que exigen negociación inmediata
3. **Resumen ejecutivo** — 3-5 párrafos para no juristas, con recomendación de firma/no firma/condicional
4. **Enmiendas sugeridas** — redlines concretas para cláusulas problemáticas

## Outputs excluidos

- Opinión jurídica vinculante (requiere abogado colegiado)
- Asesoramiento sobre estrategia procesal
- Interpretación auténtica de cláusulas en litigio

## Disclaimer

Todo output incluye disclaimer legal completo. Ver `docs/rules/domain/professional-domain-disclaimer.md`.

## Relación con otras skills

- **Upstream**: `legal-document-drafter` (cuando se necesita redactar antes de revisar)
- **Downstream**: `legal-compliance-checker` (tras identificar obligaciones legales en el contrato)
