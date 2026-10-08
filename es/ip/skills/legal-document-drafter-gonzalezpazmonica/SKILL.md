---
name: legal-document-drafter-gonzalezpazmonica
title: legal-document-drafter — Redactor de Documentación Legal
description: Genera borradores de documentos legales ES (NDAs, cartas disciplinarias, acuerdos extinción). Marca datos pendientes.
author: gonzalezpazmonica
author_url: https://github.com/gonzalezpazmonica/savia/tree/main/.claude/skills/professional-domain/legal/legal-document-drafter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: ip
language: es
---

# legal-document-drafter — Redactor de Documentación Legal

## Cuándo usar esta skill

- Al necesitar un borrador de NDA para negociación inicial.
- Al redactar carta de despido disciplinario (art. 54-55 ET).
- Al preparar acuerdo de extinción de mutuo acuerdo.
- Para fichas de compliance, comunicaciones formales internas.
- Como punto de partida antes de revisión por abogado externo.

## Inputs requeridos

| Campo | Descripción | Ejemplo |
|---|---|---|
| `tipo_documento` | Tipo de documento a redactar | `NDA`, `carta-despido`, `acuerdo-extincion` |
| `partes` | Identidad y rol de cada parte | Empresa X (cedente), Empresa Y (cesionaria) |
| `terminos_clave` | Condiciones principales | Duración 2 años, ámbito mundial, confidencial |
| `jurisdiccion` | Ley aplicable | `ES` por defecto |

## Outputs producidos

1. **Borrador estructurado** — documento completo con todos los elementos obligatorios por tipo
2. **Marcadores [DATO PENDIENTE: descripción]** — en cada campo que requiere completar con dato real
3. **Notas de revisión** — puntos que requieren validación jurídica externa señalados con [VERIFICAR CON ABOGADO]
4. **Checklist de firma** — elementos a verificar antes de suscribir

## Restricciones críticas

- NUNCA inventa artículos, plazos legales o cifras que no sean de conocimiento general
- NUNCA omite el disclaimer legal final
- SIEMPRE marca con [DATO PENDIENTE: descripción] cada campo sin dato
- Los artículos del ET citados son los vigentes; verificar actualización normativa antes de uso

## Disclaimer

Todo output incluye disclaimer legal completo. Ver `docs/rules/domain/professional-domain-disclaimer.md`.

## Relación con otras skills

- **Upstream**: `legal-compliance-checker` (obligaciones a incluir en el documento)
- **Downstream**: `legal-contract-reviewer` (revisión del borrador generado)
