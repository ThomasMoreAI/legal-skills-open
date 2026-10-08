---
name: gap-privacidad-betobetico
title: /gap
description: Gap regulatorio de privacidad — compara un cambio normativo o una guía nueva de la ANTAI contra la política de privacidad y los procedimientos actuales. Identifica gaps, propone actualizaciones y prioriza. Usar cuando se publique una nueva guía, resolución o reforma normativa que afecte a protección de datos, o cuando el usuario diga "gap de privacidad", "actualizar política", "nueva guía ANTAI".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/privacidad/skills/gap
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: data-protection
language: es
---

# /gap

1. Cargar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md` → política actual, compromisos de privacidad, registro de actividades.
2. Identificar el cambio normativo (nueva guía, directriz, reforma, resolución).
3. Comparar contra la posición actual documentada.
4. Generar tabla de gaps con prioridad y propuesta de actualización.

```
/privacidad:gap
La ANTAI ha publicado nueva guía sobre el uso de cookies analíticas.
¿Afecta a nuestra política?
```

---

## Propósito

La normativa de protección de datos cambia: nuevas guías y resoluciones de la ANTAI, reformas legislativas, criterios de la Corte Suprema de Justicia. Cada cambio puede crear un gap entre lo que dice la norma y lo que refleja la política de privacidad, los procedimientos internos o los contratos vigentes. Este skill identifica esos gaps antes de que se conviertan en incumplimientos.

---

## Fuentes de cambio habituales

| Fuente | Tipo | Frecuencia |
|---|---|---|
| ANTAI | Guías, resoluciones sancionadoras, informes | Continua |
| Órgano Judicial / Corte Suprema de Justicia (CSJ) | Fallos sobre protección de datos y habeas data | Irregular |
| Asamblea Nacional / Órgano Ejecutivo | Reformas legislativas, decretos ejecutivos | Irregular |
| Gaceta Oficial de Panamá | Publicación de normas | Irregular |
| Referencia comparada internacional (no vinculante) | Directrices del CEPD, criterios de otras autoridades | Irregular |

---

## Proceso de análisis

### Paso 1: Identificar el cambio

- ¿Qué norma/guía/resolución ha cambiado?
- ¿Cuál es su alcance (qué tratamientos afecta)?
- ¿Desde cuándo es aplicable?
- ¿Es vinculante o recomendación?

### Paso 2: Comparar contra la posición actual

Revisar contra los siguientes documentos del perfil:

| Documento | Ubicación en el perfil | Aspecto a comprobar |
|---|---|---|
| Política de privacidad web | `## Política de privacidad` | Información al titular, bases de licitud, plazos |
| Política de cookies | `## Política de cookies` | Tipos de cookies, consentimiento, gestión |
| Registro de actividades (RAT) | `## Registro de actividades` | Bases de licitud, categorías, plazos |
| Encargos de tratamiento | `## Encargos de tratamiento — Playbook` | Cláusulas, subencargados, transferencias |
| Derechos del titular | `## Derechos del titular` | Canales, plazos, verificación |
| Protocolo de brechas | `## Brechas de seguridad` | Plazos, notificación, registro |
| Cláusula informativa empleados | `## Empleados` | Videovigilancia, geolocalización, control |

### Paso 3: Identificar gaps

Para cada aspecto afectado por el cambio:

- **¿Qué dice la norma ahora?**
- **¿Qué dice nuestra documentación actual?**
- **¿Hay divergencia?** Si sí → gap identificado

---

## Formato de salida

```markdown
# Gap regulatorio de privacidad

**Cambio normativo:** [referencia completa]
**Fecha de publicación:** [fecha]
**Fecha de aplicabilidad:** [fecha]
**Carácter:** [Vinculante / Recomendación / Criterio interpretativo]

---

## Resumen del cambio

[2-3 frases sobre qué cambia y a quién afecta]

---

## Tabla de gaps

| # | Aspecto afectado | Posición actual | Nueva exigencia | Gap | Prioridad | Acción propuesta |
|---|---|---|---|---|---|---|
| 1 | [Ej., Cookies analíticas] | [Lo que dice la política actual] | [Lo que exige la nueva guía] | [Descripción del gap] | [Alta/Media/Baja] | [Qué hacer] |
| 2 | ... | ... | ... | ... | ... | ... |

---

## Priorización

- **Alta:** incumplimiento actual o riesgo de sanción inminente
- **Media:** desajuste que debe corregirse en plazo razonable
- **Baja:** mejora recomendable, sin riesgo inmediato

---

## Plan de acción

| # | Acción | Responsable | Plazo propuesto | Estado |
|---|---|---|---|---|
| 1 | [Ej., Actualizar política de cookies] | [Encargado de protección de datos] | [15 días] | Pendiente |
| 2 | [Ej., Revisar encargos de tratamiento con proveedores de analítica] | [Jurídico] | [30 días] | Pendiente |
```

---

## Legislación de referencia

- Ley 81 de 2019 — marco general de protección de datos personales en Panamá
- Decreto Ejecutivo 285 de 2021 — reglamento de la Ley 81 de 2019
- Guías y resoluciones de la ANTAI
- Fallos del Órgano Judicial / Corte Suprema de Justicia en materia de protección de datos y habeas data
- Referencia comparada (no vinculante en Panamá): directrices del CEPD, como criterio internacional orientativo

---

## Lo que este skill NO hace

- No monitoriza cambios normativos automáticamente — para eso, configurar `/regulatorio:alertas`.
- No redacta la actualización de la política — marca qué debe cambiar. Para redactar, usar `/regulatorio:redaccion`.
- No determina si una resolución sancionadora de la ANTAI a un tercero nos afecta directamente — evalúa si el criterio subyacente aplica a nuestros tratamientos.
