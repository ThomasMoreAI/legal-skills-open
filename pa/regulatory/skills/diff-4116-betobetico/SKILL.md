---
name: diff-4116-betobetico
title: /diff
description: Diff de política — compara un cambio regulatorio (nueva norma, reforma, guía, circular) contra la biblioteca de políticas internas. Muestra qué cambió, qué políticas afecta y propone actualizaciones concretas. Usar cuando se publique una norma nueva o el usuario diga "diff de política", "nueva norma", "¿nos afecta esta reforma?".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/regulatorio/skills/diff
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: regulatory
language: es
---

# /diff

1. Cargar `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md` → biblioteca de políticas, sectores, umbrales de materialidad.
2. Identificar el cambio regulatorio (norma, reforma, guía, resolución).
3. Comparar contra las políticas internas vigentes.
4. Generar informe de diferencias con propuestas de actualización.

```
/regulatorio:diff
La Superintendencia de Bancos ha publicado un nuevo acuerdo que modifica los
requisitos de debida diligencia del cliente (KYC) para clientes de alto riesgo.
```

---

## Propósito

Las políticas internas de una organización reflejan las obligaciones regulatorias vigentes en un momento dado. Cuando cambia la norma, las políticas quedan desalineadas. Este skill identifica exactamente qué ha cambiado, qué políticas internas se ven afectadas y propone la actualización concreta — antes de que el gap se convierta en incumplimiento.

---

## Proceso de análisis

### Paso 1: Identificar el cambio

| Campo | Contenido |
|---|---|
| **Norma / Guía** | [referencia completa: tipo de norma, número, fecha, Gaceta Oficial / acuerdo del supervisor] |
| **Tipo de cambio** | [Nueva norma / Reforma / Derogación / Guía interpretativa / Acuerdo / Resolución] |
| **Fecha de publicación** | [fecha] |
| **Entrada en vigor** | [fecha — inmediata o con vacatio legis] |
| **Período transitorio** | [si existe — duración y condiciones] |
| **Ámbito** | [sectorial / transversal; emisor: Asamblea Nacional / Órgano Ejecutivo / SBP / SMV / UAF] |

### Paso 2: Mapear el impacto

Para cada obligación nueva o modificada:

| Obligación regulatoria | Norma anterior | Nueva norma | Delta |
|---|---|---|---|
| [Ej., Plazo de notificación] | [Lo que decía antes] | [Lo que dice ahora] | [Qué cambia] |

### Paso 3: Cruzar con políticas internas

Revisar la biblioteca de políticas internas del perfil:

| Política interna | Sección afectada | Posición actual | Nueva exigencia | ¿Desalineada? |
|---|---|---|---|---|
| [Ej., Política de protección de datos] | [Sección 4.2] | [Lo que dice hoy] | [Lo que debería decir] | [Sí/No] |

### Paso 4: Proponer actualizaciones

Para cada política desalineada, proponer el cambio marcado:

```markdown
## Política: [Nombre de la política]

### Sección: [número y título]

**Texto actual:**
> [texto vigente]

**Texto propuesto:**
> [texto actualizado con cambios marcados]

**Justificación:** [por qué cambia — referencia a la nueva norma]
```

---

## Formato de salida

```markdown
# Diff de política regulatoria

**Cambio regulatorio:** [referencia completa]
**Fecha de publicación:** [fecha]
**Entrada en vigor:** [fecha]
**Período transitorio:** [si existe]

---

## Resumen del cambio

[3-5 frases: qué cambia, a quién afecta, cuál es la urgencia]

---

## Impacto en políticas internas

| # | Política afectada | Sección | Tipo de impacto | Urgencia |
|---|---|---|---|---|
| 1 | [nombre] | [sección] | [Modificación / Nueva obligación / Derogación] | [Alta/Media/Baja] |
| 2 | ... | ... | ... | ... |

---

## Propuestas de actualización

[Para cada política afectada: texto actual vs. texto propuesto]

---

## Políticas no afectadas

[Confirmar qué políticas revisadas NO necesitan cambios — para que conste que se revisaron]

---

## Calendario de implementación

| # | Acción | Responsable | Plazo | Vinculado a |
|---|---|---|---|---|
| 1 | [Ej., Actualizar política X] | [Compliance] | [Antes de entrada en vigor] | [Art. X nueva norma] |
```

---

## Legislación de referencia

- Normativa sectorial según el perfil de práctica configurado (Ley 23 de 2015, acuerdos de la SBP y de la SMV, guías de la UAF)
- Constitución Política de la República de Panamá (principio de publicidad de las normas) [verificar]
- Código Civil de Panamá (entrada en vigor de las leyes) [verificar]

---

## Lo que este skill NO hace

- No monitoriza cambios normativos — para eso, usar `/regulatorio:alertas`.
- No redacta la política actualizada completa — propone los cambios marcados. Para redacción completa, usar `/regulatorio:redaccion`.
- No evalúa si el cambio normativo es constitucionalmente válido — asume que la norma está vigente.
