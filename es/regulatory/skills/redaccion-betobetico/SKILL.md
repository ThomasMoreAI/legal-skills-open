---
name: redaccion-betobetico
title: /redaccion
description: 'Redactor de política — redacta la actualización de una política interna para cerrar un gap regulatorio. Muestra los cambios marcados respecto a la versión vigente. Gate: PROPUESTA — requiere aprobación del policy owner antes de implementar. Usar cuando el usuario diga "redacta la actualización", "nueva versión de la política", "cierra este gap" o tras un `/regulatorio:diff`.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/regulatorio/skills/redaccion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: regulatory
language: es
---

# /redaccion

1. Cargar `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md` → políticas vigentes, estilo house, proceso de aprobación.
2. Identificar la política a actualizar y el gap a cerrar.
3. Obtener la versión vigente de la política.
4. Redactar la actualización con cambios marcados.
5. Emitir como PROPUESTA — no implementar sin aprobación.

```
/regulatorio:redaccion GAP-2026-001
```

---

## Propósito

Un gap identificado necesita una solución concreta: la nueva redacción de la política que cierra la brecha. Este skill genera esa redacción mostrando exactamente qué cambia respecto a la versión vigente, para que el policy owner pueda revisar y aprobar con conocimiento de causa.

---

## Proceso

### Paso 1: Identificar el gap y la política

| Campo | Contenido |
|---|---|
| **Gap** | [ID o descripción] |
| **Cambio regulatorio** | [norma que origina el gap] |
| **Política afectada** | [nombre y versión vigente] |
| **Sección(es) afectada(s)** | [identificar las secciones concretas] |

Si la política no está disponible (no se proporcionó como documento semilla), pedir al usuario que la facilite.

### Paso 2: Analizar el gap

- ¿Qué exige la nueva norma que la política actual no refleja?
- ¿Hay que añadir contenido nuevo, modificar contenido existente o eliminar contenido obsoleto?
- ¿El cambio afecta solo la redacción o también los procedimientos operativos?

### Paso 3: Redactar la actualización

Principios de redacción:

- **Mínima intervención.** Cambiar solo lo necesario para cerrar el gap. No reescribir secciones que funcionan.
- **Coherencia interna.** Verificar que el cambio no contradice otras secciones de la misma política.
- **Coherencia con otras políticas.** Verificar que no contradice otras políticas del sistema.
- **Trazabilidad.** Cada cambio se justifica con referencia a la norma que lo origina.
- **Estilo house.** Mantener la terminología, estructura y formato de la política vigente.

### Paso 4: Marcar los cambios

Usar formato de control de cambios:

- **Texto añadido:** marcado con `[+texto nuevo+]`
- **Texto eliminado:** marcado con `[-texto eliminado-]`
- **Texto modificado:** combinación de eliminación + adición

---

## Gate de aprobación

**PROPUESTA** — Este borrador requiere la aprobación del policy owner antes de implementarse. No actualizar la política vigente hasta recibir aprobación explícita.

Incluir siempre:

```markdown
---

**PROPUESTA — PENDIENTE DE APROBACIÓN**

**Policy owner:** [nombre / puesto del aprobador]
**Fecha de propuesta:** [fecha]
**Fecha límite recomendada:** [fecha — vinculada a entrada en vigor de la norma]
**Motivo:** Cierre de gap [ID] originado por [cambio regulatorio]

Para aprobar: confirmar por [canal habitual].
Para modificar: indicar los cambios y se generará nueva versión.
Para rechazar: indicar el motivo.

---
```

---

## Formato de salida

```markdown
# Propuesta de actualización de política

**Política:** [nombre]
**Versión vigente:** [número / fecha]
**Versión propuesta:** [número / fecha]
**Gap que cierra:** [ID o descripción]
**Cambio regulatorio:** [referencia]

---

## Resumen de cambios

[2-3 frases: qué cambia y por qué]

---

## Cambios marcados

### Sección [X]: [Título]

**Texto vigente:**
> [texto actual completo de la sección]

**Texto propuesto:**
> [texto con marcas de cambio: [+añadido+] / [-eliminado-]]

**Justificación:** [referencia a la norma que lo exige]

---

[Repetir para cada sección afectada]

---

## Verificación de coherencia

- [ ] Coherencia interna de la política: [Sí / Flag]
- [ ] Coherencia con otras políticas del sistema: [Sí / Flag]
- [ ] Terminología consistente: [Sí / Flag]

---

## PROPUESTA — PENDIENTE DE APROBACIÓN

[Bloque de aprobación]
```

---

## Legislación de referencia

- Normativa sectorial según el gap que se cierra
- Buenas prácticas de gestión de políticas corporativas (ISO 37301 — Compliance)

---

## Lo que este skill NO hace

- No aprueba ni implementa la actualización — es una propuesta para revisión.
- No identifica gaps — para eso, usar `/regulatorio:diff` o `/regulatorio:gaps`.
- No redacta políticas nuevas desde cero — actualiza políticas existentes. Para una política nueva, indicar que se necesita un proceso de creación diferente.
