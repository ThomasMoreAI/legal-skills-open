---
name: gaps-betobetico
title: /gaps
description: 'Tracker de gaps regulatorios — lista los gaps abiertos entre la normativa vigente y las políticas/procedimientos internos. Estado de cada gap: identificado / en análisis / propuesta enviada / implementado / cerrado. Prioridad: alta / media / baja. Usar cuando el usuario diga "gaps abiertos", "¿qué tenemos pendiente?", "estado del compliance", "tracker de gaps".'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/regulatorio/skills/gaps
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: regulatory
language: es
---

# /gaps

1. Cargar `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md` → registro de gaps, políticas, sectores.
2. Leer el registro de gaps del directorio de outputs.
3. Filtrar según parámetros (sector, prioridad, estado).
4. Generar tabla de estado actualizada.

```
/regulatorio:gaps --prioridad alta
```

---

## Propósito

Un gap regulatorio identificado pero no cerrado es un riesgo latente. Este skill mantiene la visibilidad sobre todos los gaps abiertos: cuáles se han identificado, cuáles están en análisis, cuáles tienen propuesta de solución y cuáles se han cerrado. Es el tablero de control del compliance regulatorio.

---

## Ciclo de vida de un gap

```
IDENTIFICADO → EN ANÁLISIS → PROPUESTA ENVIADA → IMPLEMENTADO → CERRADO
```

| Estado | Significado | Responsable |
|---|---|---|
| **Identificado** | Gap detectado (por `/regulatorio:diff`, `/regulatorio:alertas` o manualmente) | Compliance |
| **En análisis** | Se está evaluando el impacto y la solución | Compliance + Área afectada |
| **Propuesta enviada** | Se ha redactado la actualización y enviado para aprobación | Policy owner |
| **Implementado** | La política/procedimiento se ha actualizado | Compliance |
| **Cerrado** | Verificado que la implementación es correcta y completa | Compliance |

---

## Priorización

| Prioridad | Criterio | Plazo objetivo |
|---|---|---|
| **Alta** | Incumplimiento activo o riesgo de sanción; norma ya en vigor sin período transitorio | Inmediato (días) |
| **Media** | Desalineación significativa con período transitorio o riesgo moderado | Semanas |
| **Baja** | Mejora recomendable; gap menor sin riesgo directo de sanción | Meses |

---

## Formato del registro de gaps

Cada gap se registra con:

| Campo | Contenido |
|---|---|
| **ID** | Identificador único (ej., GAP-2026-001) |
| **Fecha de identificación** | [fecha] |
| **Origen** | [diff / alerta / auditoría / manual] |
| **Cambio regulatorio** | [referencia a la norma/guía] |
| **Política afectada** | [nombre de la política interna] |
| **Descripción del gap** | [qué falta o qué está desalineado] |
| **Prioridad** | [Alta / Media / Baja] |
| **Estado** | [Identificado / En análisis / Propuesta enviada / Implementado / Cerrado] |
| **Responsable** | [persona o equipo] |
| **Fecha objetivo** | [cuándo debe estar cerrado] |
| **Notas** | [contexto adicional] |

---

## Formato de salida

```markdown
# Tracker de gaps regulatorios

**Fecha de consulta:** [fecha]
**Filtro aplicado:** [sector / prioridad / estado / todos]

---

## Resumen

| Estado | Cantidad |
|---|---|
| Identificado | [N] |
| En análisis | [N] |
| Propuesta enviada | [N] |
| Implementado | [N] |
| Cerrado (último mes) | [N] |
| **Total abiertos** | **[N]** |

---

## Gaps abiertos

| ID | Prioridad | Estado | Política | Gap | Responsable | Fecha objetivo |
|---|---|---|---|---|---|---|
| GAP-2026-001 | Alta | En análisis | [política] | [descripción] | [nombre] | [fecha] |
| GAP-2026-002 | Media | Identificado | [política] | [descripción] | [nombre] | [fecha] |
| ... | ... | ... | ... | ... | ... | ... |

---

## Gaps vencidos (fecha objetivo superada)

[Lista de gaps cuyo plazo ha vencido — requieren atención inmediata]

---

## Siguiente paso

1. **Actualizar un gap** — indicar ID y nuevo estado.
2. **Cerrar un gap** — indicar ID y confirmar implementación.
3. **Nuevo gap** — describir y se registrará.
4. **Generar propuesta** — `/regulatorio:redaccion` para redactar la actualización.
```

---

## Legislación de referencia

- Normativa sectorial según el perfil configurado
- Principio de diligencia debida regulatoria (compliance)

---

## Lo que este skill NO hace

- No detecta gaps automáticamente — para eso, usar `/regulatorio:diff` o `/regulatorio:alertas`.
- No redacta la solución al gap — para eso, usar `/regulatorio:redaccion`.
- No aprueba el cierre del gap — requiere confirmación del policy owner.
