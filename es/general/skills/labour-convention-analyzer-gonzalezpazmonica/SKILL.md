---
name: labour-convention-analyzer-gonzalezpazmonica
title: labour-convention-analyzer — Analizador de Convenio Colectivo
description: Extrae y analiza cláusulas de convenios colectivos españoles. Interpreta en lenguaje claro, señala ambigüedades y advierte de posible desactualización.
author: gonzalezpazmonica
author_url: https://github.com/gonzalezpazmonica/savia/tree/main/.claude/skills/professional-domain/labour/labour-convention-analyzer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# labour-convention-analyzer — Analizador de Convenio Colectivo

## Cuándo usar esta skill

- Para interpretar cláusulas ambiguas de un convenio colectivo.
- Para determinar la categoría profesional correcta de un trabajador.
- Para consultar tablas salariales, jornada o permisos del convenio.
- Para identificar el régimen disciplinario aplicable antes de sancionar.
- Para verificar si un convenio está vigente o ha sido sustituido.

## Inputs requeridos

| Campo | Descripción | Ejemplo |
|---|---|---|
| `texto_convenio` | Fragmento o artículos relevantes del convenio | Texto copiado del BOE o del PDF del convenio |
| `consulta` | Pregunta concreta a resolver | "¿Cuántos días de permiso por matrimonio?" |
| `categoria` | Categoría profesional del empleado (si aplica) | "Técnico Especialista Nivel 3" |

## Inputs opcionales

| Campo | Descripción |
|---|---|
| `anio_publicacion` | Año del BOE en que se publicó el convenio |
| `ambito_geografico` | Estatal / autonómico / provincial / empresa |
| `sector` | Sector de actividad para localización en BOE |

## Outputs producidos

1. **Artículos relevantes extraídos** — fragmentos del convenio que responden a la consulta
2. **Interpretación en lenguaje claro** — explicación sin tecnicismos del alcance práctico
3. **Ambigüedades identificadas** — cláusulas con doble lectura posible que requieren criterio jurídico
4. **Alerta de vigencia** — indicación explícita si el convenio podría estar desactualizado
5. **Referencia BOE** — instrucciones para localizar la versión vigente si se detecta posible caducidad
6. **Disclaimer laboral** — obligatorio al final de cada output

## Outputs excluidos

- Interpretación jurídica vinculante de cláusulas contradictorias
- Resolución de conflictos de concurrencia entre convenios
- Asesoramiento en negociación colectiva

## Señales de convenio desactualizado

La skill advierte explícitamente cuando detecta:
- Fecha de vigencia expirada en el texto del convenio
- Referencias a normativa ya derogada (ej: RDL 1/1995 en lugar de ET vigente)
- Tablas salariales por debajo del SMI vigente
- Ausencia de mención al SMAC o procedimiento ASAC

## Relación con otras skills

- **Upstream**: `labour-conflict-resolver` (identificar convenio aplicable al conflicto)
- **Downstream**: `labour-document-drafter` (artículos del convenio para carta de despido)
- **Paralelo**: `legal-compliance-checker` (verificación de compliance del convenio con ET)

## Ver también

- `DOMAIN.md` — estructura de convenio, prioridad aplicativa, criterios de interpretación
- `prompt.md` — instrucciones de extracción y análisis para el modelo
