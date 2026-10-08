---
name: gap-gobernanza-ia-betobetico
title: /gap
description: Gap regulatorio de IA — compara un cambio normativo en materia de IA (Reglamento de IA, estándares armonizados, guías de la Comisión o de autoridades nacionales) contra la postura de gobernanza de IA de la organización. Identifica gaps con prioridad y acción. Usar cuando el usuario diga "gap de IA", "nueva obligación del Reglamento de IA", "¿estamos preparados para...?" o ante cambios regulatorios en IA.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/gobernanza-ia/skills/gap
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# /gap

1. Cargar `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md` → postura de gobernanza, registro de sistemas, políticas de IA.
2. Identificar el cambio regulatorio.
3. Comparar contra la postura actual.
4. Generar tabla de gaps con prioridad y acción.

```
/gobernanza-ia:gap
La Comisión ha publicado la primera tanda de estándares armonizados para
sistemas de IA de alto riesgo. ¿Estamos alineados?
```

---

## Propósito

El Reglamento de IA se despliega progresivamente (2025-2027) y genera un flujo continuo de obligaciones nuevas: estándares armonizados, guías de aplicación, actos delegados, códigos de prácticas. Cada uno puede crear un gap entre lo que exige la norma y lo que hace la organización. Este skill detecta esos gaps antes de que se conviertan en incumplimientos.

---

## Calendario de aplicación del Reglamento de IA

| Fecha | Obligaciones que entran en vigor |
|---|---|
| **Febrero 2025** | Prohibiciones (art. 5); alfabetización en IA (art. 4) |
| **Agosto 2025** | Modelos de propósito general (GPAI) — arts. 51-56; gobernanza — arts. 64-70 |
| **Agosto 2026** | Sistemas de alto riesgo (Anexo III); obligaciones de deployers (art. 27) |
| **Agosto 2027** | Sistemas de alto riesgo como componentes de seguridad (Anexo I) |

---

## Proceso de análisis

### Paso 1: Identificar el cambio

| Campo | Contenido |
|---|---|
| **Fuente** | [Reglamento de IA / Estándar armonizado / Guía Comisión / Autoridad nacional / Código de prácticas] |
| **Referencia** | [número, fecha, publicación] |
| **Tipo de cambio** | [Nueva obligación / Estándar técnico / Guía interpretativa / Acto delegado] |
| **Fecha de aplicabilidad** | [cuándo hay que cumplir] |
| **A quién afecta** | [Proveedor / Deployer / Distribuidor / Importador] |

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
| Registro en base de datos UE | [¿Completado?] | [requisito] | |

### Paso 3: Priorizar

| Prioridad | Criterio |
|---|---|
| **Alta** | Obligación ya en vigor o entrada inminente; sanción potencial significativa |
| **Media** | Obligación próxima; requiere preparación |
| **Baja** | Recomendación o buena práctica; sin sanción directa |

---

## Formato de salida

```markdown
# Gap regulatorio de IA

**Cambio regulatorio:** [referencia]
**Fecha:** [fecha]
**Aplicabilidad:** [desde cuándo]

---

## Resumen

[2-3 frases: qué cambia y cuál es el impacto para la organización]

---

## Tabla de gaps

| # | Elemento de gobernanza | Posición actual | Nueva exigencia | Gap | Prioridad | Acción propuesta |
|---|---|---|---|---|---|---|
| 1 | [Ej., Documentación técnica] | [No existe para sistema X] | [Art. 11 RIA] | [Falta documentación] | Alta | [Generar documentación] |
| 2 | ... | ... | ... | ... | ... | ... |

---

## Plan de acción

| # | Acción | Responsable | Plazo | Vinculado a |
|---|---|---|---|---|
| 1 | [acción] | [persona/equipo] | [fecha] | [obligación] |

---

## Sistemas afectados

| Sistema | Clasificación | Impacto del cambio |
|---|---|---|
| [nombre] | [alto riesgo / limitado / mínimo] | [qué cambia para este sistema] |
```

---

## Legislación de referencia

- Reglamento de IA (Reglamento UE 2024/1689) — completo
- Estándares armonizados publicados por CEN/CENELEC
- Guías de aplicación de la Comisión Europea
- Códigos de prácticas para GPAI (art. 56 RIA)

---

## Lo que este skill NO hace

- No monitoriza automáticamente nuevos desarrollos regulatorios — para eso, configurar `/regulatorio:alertas` con filtro de IA.
- No implementa las medidas técnicas de cumplimiento — identifica qué falta.
- No certifica el cumplimiento del Reglamento de IA — señala los gaps.
