---
name: legal-compliance-gonzalezpazmonica
title: Legal Compliance — Auditoría contra Legislación Española
description: Usar cuando se audita compliance legal contra legislación española consolidada.
author: gonzalezpazmonica
author_url: https://github.com/gonzalezpazmonica/savia/tree/main/.claude/skills/legal-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: regulatory
language: es
sources:
- title: Domain Terms
  path: references/domain-terms.md
---

# Legal Compliance — Auditoría contra Legislación Española

## Fuente de datos: legalize-es

Repositorio git con 12.235 normas consolidadas del BOE en Markdown.
Cada norma tiene frontmatter YAML (título, identificador BOE, rango, estado, ELI).
Actualización diaria. Commits con fecha BOE real.

Ruta local: `$LEGALIZE_ES_PATH` (default `$HOME/.savia/legalize-es`).

## Algoritmo de búsqueda (3 fases)

### Fase 1 — Clasificación del input (~500 tokens)

Leer el documento a auditar (reglas de negocio, contrato, política, spec).
Extraer términos clave y mapear a dominios legales usando `domain-terms.md`.
Determinar CCAA si el proyecto tiene configuración regional.

Dominios detectables: protección de datos, comercio electrónico, laboral,
consumidores, accesibilidad, ciberseguridad, facturación, IA, financiero,
sanidad, educación, propiedad intelectual.

### Fase 2 — Búsqueda legislativa focalizada (~3.000 tokens)

Para cada dominio detectado:

1. **Fast path**: buscar directamente en las normas conocidas del dominio
   (BOE identifiers listados en domain-terms.md)
2. **Slow path**: si no hay match suficiente, grep amplio en `$LEGALIZE_ES_PATH/es/`
3. Filtrar por `status: "in_force"` en frontmatter
4. Ordenar por rango regulatorio (Constitución > LO > Ley > RD > Orden)
5. Cargar solo artículos relevantes, no la norma completa
6. Máximo 10 normas, ~50 artículos por auditoría

Búsqueda con script: `bash scripts/legalize-es.sh search "término" [es|es-{ccaa}]`

### Fase 3 — Análisis de compliance (~8.000 tokens)

Para cada regla/cláusula del input:

1. Identificar artículos de legislación aplicables
2. Evaluar cumplimiento: CUMPLE / NO CUMPLE / PARCIAL / NO APLICA
3. Clasificar hallazgos por severidad
4. Generar recomendación concreta
5. Construir matriz de trazabilidad regla→artículo

## Clasificación de severidad

| Severidad | Criterio | Riesgo |
|-----------|----------|--------|
| CRÍTICO | Sanción >100K€, nulidad, responsabilidad penal | Inmediato |
| ALTO | Sanción 10-100K€, obligación incumplida con plazo | Sprint actual |
| MEDIO | Recomendación regulatoria, riesgo reputacional | Próximo sprint |
| INFO | Buena práctica, mejora preventiva | Backlog |

## Priorización por rango normativo

```
1. Constitución Española (CE)
2. Leyes Orgánicas (LO)
3. Leyes ordinarias
4. Reales Decretos-ley (RDL)
5. Reales Decretos (RD)
6. Órdenes Ministeriales
7. Resoluciones
8. Normas autonómicas
```

## Template de output

```markdown
# Auditoría Legal — {Proyecto}
> Fecha: YYYY-MM-DD | Scope: {scope} | Dominio: {dominio}
> Fuente: legalize-es (commit {hash}, {fecha BOE})

## Resumen Ejecutivo
Hallazgos: N (X críticos, Y altos, Z medios, W info)
Cobertura: X% de reglas con base legal identificada

## Hallazgos
### [SEVERIDAD] {Título}
- **Regla/Cláusula**: {ref input}
- **Norma**: {nombre} — Art. {N}
- **ELI**: {enlace}
- **Incumplimiento**: {descripción}
- **Riesgo**: {sanción o consecuencia}
- **Recomendación**: {acción concreta}

## Matriz de Trazabilidad
| Regla | Norma | Artículo | Estado | Severidad |

## Disclaimer
⚖️ Este análisis es orientativo. No constituye asesoramiento jurídico.
```

## Historial de reformas

Usar `git log` sobre legalize-es para verificar vigencia:
```bash
git -C $LEGALIZE_ES_PATH log --oneline -5 -- es/{BOE-ID}.md
```

## Scopes de auditoría

| Scope | Input | Foco |
|-------|-------|------|
| rules | reglas-negocio.md | Cada RN contra artículos |
| contract | Documento contractual | Cláusulas, plazos, nulidades |
| architecture | ARCHITECTURE.md, specs | Privacy by design, seguridad |
| policy | Política privacidad, cookies | Conformidad textual |
| pbi | PBI description | Implicaciones legales del feature |
| full | Todo lo anterior | Auditoría transversal |
