---
name: gap-gobernanza-ia-4023-betobetico
title: /gap
description: Gap de gobernanza de IA — compara un cambio relevante en materia de IA (iniciativa o anteproyecto local, normativa panameña conexa, estándar o guía internacional de referencia) contra la postura de gobernanza de IA de la organización. Identifica gaps con prioridad y acción. Usar cuando el usuario diga "gap de IA", "nueva obligación de gobernanza de IA", "¿estamos preparados para...?" o ante cambios relevantes en IA.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/gobernanza-ia/skills/gap
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: contracts
language: es
---

# /gap

1. Cargar `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md` → postura de gobernanza, registro de sistemas, políticas de IA.
2. Identificar el cambio relevante.
3. Comparar contra la postura actual.
4. Generar tabla de gaps con prioridad y acción.

```
/gobernanza-ia:gap
NIST ha publicado una actualización de su AI Risk Management Framework.
¿Estamos alineados?
```

---

## Propósito

Panamá no cuenta con una ley de IA vinculante, pero el panorama evoluciona: iniciativas y anteproyectos locales [verificar], actualizaciones de la normativa conexa de protección de datos (ANTAI), nuevas versiones de estándares y guías internacionales de referencia (OCDE, UNESCO, NIST AI RMF, ISO/IEC 42001). Cada cambio puede crear un gap entre la práctica de gobernanza de la organización y el marco de referencia que ha adoptado. Este skill detecta esos gaps antes de que se conviertan en problemas de cumplimiento (en lo conexo) o en debilidades de gobernanza.

---

## Hitos de referencia en gobernanza de IA (orientativos)

| Ámbito | Qué seguir |
|---|---|
| **Iniciativas locales (Panamá)** | Anteproyectos de ley de IA, estrategias nacionales, lineamientos de la AIG [verificar] |
| **Protección de datos (Panamá)** | Resoluciones y guías de la ANTAI bajo la Ley 81 de 2019 |
| **Estándares internacionales** | Actualizaciones de NIST AI RMF e ISO/IEC 42001 |
| **Soft law internacional** | Principios de la OCDE, Recomendación de la UNESCO |

*Nota: salvo la normativa panameña conexa (datos personales), los demás hitos son referencia voluntaria, no obligaciones legales directas en Panamá.*

---

## Proceso de análisis

### Paso 1: Identificar el cambio

| Campo | Contenido |
|---|---|
| **Fuente** | [Iniciativa local / Normativa conexa (datos) / Estándar internacional / Guía / Soft law] |
| **Referencia** | [número, fecha, publicación] |
| **Tipo de cambio** | [Nueva obligación legal conexa / Estándar técnico / Guía interpretativa / Principio] |
| **Fecha de aplicabilidad** | [cuándo aplica o se recomienda cumplir] |
| **A quién afecta** | [Proveedor / Implementador / Distribuidor / Importador] |
| **¿Vinculante en Panamá?** | [Sí (normativa conexa) / No (referencia voluntaria)] |

### Paso 2: Mapear contra la postura actual

Revisar contra los elementos del sistema de gobernanza de IA:

| Elemento de gobernanza | Estado actual | Nueva exigencia | ¿Gap? |
|---|---|---|---|
| Inventario de sistemas de IA | [¿Existe? ¿Actualizado?] | [requisito] | |
| Clasificación de riesgo | [¿Se ha hecho para todos los sistemas?] | [requisito] | |
| Evaluaciones de impacto | [¿Realizadas?] | [requisito] | |
| Sistema de gestión de riesgos | [¿Implementado?] | [requisito] | |
| Documentación técnica | [¿Disponible?] | [requisito] | |
| Supervisión humana | [¿Definida?] | [requisito] | |
| Transparencia | [¿Cumplida?] | [requisito] | |
| Formación del personal | [¿Realizada?] | [requisito] | |
| Contratos con proveedores | [¿Revisados?] | [requisito] | |
| Protección de datos (Ley 81 de 2019) | [¿Cumplida?] | [requisito] | |

### Paso 3: Priorizar

| Prioridad | Criterio |
|---|---|
| **Alta** | Obligación legal conexa ya en vigor o entrada inminente; exposición significativa |
| **Media** | Estándar o exigencia próxima; requiere preparación |
| **Baja** | Recomendación o buena práctica; sin consecuencia legal directa |

---

## Formato de salida

```markdown
# Gap de gobernanza de IA

**Cambio relevante:** [referencia]
**Fecha:** [fecha]
**Aplicabilidad:** [desde cuándo]
**¿Vinculante en Panamá?:** [Sí / No — referencia voluntaria]

---

## Resumen

[2-3 frases: qué cambia y cuál es el impacto para la organización]

---

## Tabla de gaps

| # | Elemento de gobernanza | Posición actual | Nueva exigencia | Gap | Prioridad | Acción propuesta |
|---|---|---|---|---|---|---|
| 1 | [Ej., Documentación técnica] | [No existe para sistema X] | [Marco interno / NIST] | [Falta documentación] | Alta | [Generar documentación] |
| 2 | ... | ... | ... | ... | ... | ... |

---

## Plan de acción

| # | Acción | Responsable | Plazo | Vinculado a |
|---|---|---|---|---|
| 1 | [acción] | [persona/equipo] | [fecha] | [exigencia] |

---

## Sistemas afectados

| Sistema | Clasificación | Impacto del cambio |
|---|---|---|
| [nombre] | [alto riesgo / limitado / mínimo] | [qué cambia para este sistema] |
```

---

## Marco de referencia

- Iniciativas y anteproyectos locales de IA en Panamá [verificar]
- Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 sobre protección de datos personales; autoridad: ANTAI
- NIST AI Risk Management Framework; ISO/IEC 42001
- Principios de la OCDE sobre IA; Recomendación de la UNESCO sobre la ética de la IA
- Reglamento Europeo de IA (Reglamento UE 2024/1689): solo como referencia comparada internacional

---

## Lo que este skill NO hace

- No monitoriza automáticamente nuevos desarrollos — para eso, usar el agente `monitor-ia`.
- No implementa las medidas técnicas de cumplimiento — identifica qué falta.
- No certifica el cumplimiento de un marco — señala los gaps.
