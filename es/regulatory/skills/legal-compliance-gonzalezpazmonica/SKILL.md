---
name: legal-compliance-gonzalezpazmonica
title: Legal Compliance — Auditoría contra Legislación Española
description: Usar cuando se audita compliance legal contra legislación española consolidada.
author: gonzalezpazmonica
author_url: https://github.com/gonzalezpazmonica/savia/tree/main/.claude/skills/legal-compliance
license: MIT
version: 0.1.1
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

Repositorio git de normas consolidadas del BOE en Markdown (upstream declara
más de 12.000; `legalize-es.sh status` da la cifra real del corpus local).
Cada norma es `es/{BOE-ID}.md` (estatal) o `es-{ccaa}/{ID}.md` (autonómica),
con frontmatter YAML: `title`, `identifier`, `rank` (p. ej. `ley_organica`),
`status` (`in_force` / `repealed`), `last_updated`, `source` (ELI).
Los artículos son encabezados Markdown: `###### Artículo 13. Derecho de acceso.`
Commits con fecha BOE real.

Ruta local: `$LEGALIZE_ES_PATH` (default `$HOME/.savia/legalize-es`).

## Contrato del script (`scripts/legalize-es.sh`)

| Comando | Qué hace |
|---|---|
| `status` | Ruta, nº de normas estatales y CCAA, último commit |
| `search "término" [es\|es-{ccaa}]` | Búsqueda **literal** (no regex, sin distinguir mayúsculas) en normas con `status: in_force` en el frontmatter; ordena por rango; máximo 20 resultados y avisa si trunca |
| `search-article <BOE-ID> "Artículo 13"` | Extrae solo ese artículo, desde su encabezado hasta el siguiente. Acepta `13`, `Art. 13`, `13 bis`, o un encabezado literal (`Disposición adicional primera`) |
| `check-status <BOE-ID>` | VIGENTE / DEROGADA / DESCONOCIDO (si falta `status`) |
| `history <BOE-ID>` | `git log` de la norma (avisa si el clone es superficial) |
| `install` / `update` | Clona (`--depth=1`) o actualiza el corpus (requieren red) |

Exit codes: `0` encontrado · `1` sin resultados, norma o artículo inexistente
· `2` uso inválido (término vacío, ámbito o identificador no válidos; los
identificadores solo admiten letras, dígitos y guiones) · `3` corpus no
disponible.

**Regla anti-alucinación**: solo se cita un artículo que `search-article`
haya devuelto con exit 0. Exit 1 o 3 significa *sin fuente*: el hallazgo
queda como «NO VERIFICADO», nunca como CUMPLE. Sin corpus (exit 3) no se
emite auditoría, solo las instrucciones de instalación.

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
3. Filtrar por `status: "in_force"` en frontmatter (lo hace `search`)
4. Ordenar por rango regulatorio (Constitución > LO > Ley > RDL > RD > Orden
   > Resolución; lo hace `search`; rangos no reconocidos van al final)
5. Cargar solo artículos relevantes con `search-article`, no la norma completa
6. Máximo 10 normas, ~50 artículos por auditoría

Búsqueda con script: `bash scripts/legalize-es.sh search "término" [es|es-{ccaa}]`

### Fase 3 — Análisis de compliance (~8.000 tokens)

Para cada regla/cláusula del input:

1. Identificar artículos de legislación aplicables (extraídos con exit 0)
2. Evaluar cumplimiento: CUMPLE / NO CUMPLE / PARCIAL / NO APLICA /
   NO VERIFICADO (sin artículo extraído del corpus)
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

CE > LO > Ley > RDL > RD > Orden > Resolución > normas autonómicas.

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
Este análisis es orientativo. No constituye asesoramiento jurídico.
```

## Historial de reformas

Usar `git log` sobre legalize-es para verificar vigencia:
```bash
bash scripts/legalize-es.sh history {BOE-ID}
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
