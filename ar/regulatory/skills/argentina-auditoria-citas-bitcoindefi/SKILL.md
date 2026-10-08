---
name: argentina-auditoria-citas-bitcoindefi
title: Auditoría de citas · Verificación sistemática
description: 'Auditoría sistemática de citas normativas y jurisprudenciales en escritos: extrae todas las citas, las cruza contra la tabla de fuentes verificadas del caso (jurisprudencia/fuentes-*.md), y reporta citas verificadas ✅, bloqueantes sin respaldo 🔴, y pendientes 🔲. Paso obligatorio de cierre en argentina-bucles (Paso 6) y argentina-diagnostico (Sección G).'
author: Bitcoindefi
author_url: https://github.com/Bitcoindefi/agente-smith/tree/main/skills/argentina-auditoria-citas
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: regulatory
language: es
---

# Auditoría de citas · Verificación sistemática

Skill original de Agente Smith (MIT). Ejecutable como checklist independiente o
integrado en el cierre de redacción (`argentina-bucles`) y en la auditoría de escritos
ya hechos (`argentina-diagnostico`).

## Propósito

El principio duro del sistema: **"ninguna cita sin fuente verificada o marca 🔲"**.
Este skill automatiza esa verificación. Extrae citas del escrito, las busca en la
tabla de fuentes verificadas, y reporta el estado de cada una. Impide que un escrito
cierre sin resolver el estatus de toda cita.

## Prerrequisitos

1. **Escrito terminado** en cualquier formato (borrador de redacción, escrito final, etc.)
2. **Tabla de fuentes del caso:** archivo `jurisprudencia/fuentes-XXXX.md` donde XXXX
   puede ser identificador del expediente, fecha, o tipo de escrito. Formato estándar:

```markdown
# Fuentes verificadas · [Identificador del escrito/caso]

| Norma/Fallo | Cita textual | UUID SAIJ | URL | Secciones usadas |
|-------------|--------------|-----------|-----|------------------|
| Ley N° 27.043 | Art. 15 | abc-123-uuid | https://saij.gob.ar/... | §I.A.2, §III.1 |
| CSJN, Fallos 340:1313 | Considerando 5 | def-456-uuid | https://saij.gob.ar/... | §II.B |
| Resolución AFIP N° 4567/2023 | Art. 3 | ghi-789-uuid | https://saij.gob.ar/... | §IV.C.1 |
```

3. **Convención de citas en el escrito:**
   - Normas: "Ley N° X", "Decreto N° X", "Resolución N° X", "Art. X", "Artículo X"
   - Jurisprudencia: "Fallos T.XXX:XXX", "CSJN", "Cámara Nacional de X", "Juzgado de X"
   - Cualquier cita sin verificar en la tabla debe ir marcada con 🔲 en el escrito

## Proceso de auditoría (7 pasos)

### Paso 1 · Lectura del escrito

Leer el escrito completo de principio a fin. Anotar su estructura, tipo de pieza,
y secciones donde van las citas.

### Paso 2 · Extracción de citas

Extraer TODAS las referencias normativas y jurisprudenciales. Usar patrones regex
para identificar:

**Normativas:**
- "Ley N° [número]"
- "Decreto N° [número]"
- "Decreto-Ley N° [número]"
- "Resolución N° [número]"
- "Ordenanza N° [número]"
- "Disposición N° [número]"
- "Art. [número]" o "Artículo [número]"
- "Inciso", "Párrafo", "Inciso a)" [ligadas a norma anterior]

**Jurisprudenciales:**
- "Fallos T.[número]:[número]" o "Fallos [número]"
- "[Tribunal] [Sentencia/Res.] [número]/[año]"
- "CSJN", "Corte Suprema"
- "Cámara Nacional de [fuero]"
- "Juzgado de [fuero]"
- "C.A.[siglas], [número]/[año]"

**Doctrina (si aplica):**
- Autor + fecha
- Referencias a monografías, comentarios a leyes

Crear tabla PROVISIONAL:

```markdown
## Citas extraídas del escrito [nombre]

| N° | Cita textual (tal como aparece) | Tipo | Sección | Status |
|----|----------------------------------|------|---------|--------|
| 1 | "Art. 15 de la Ley N° 27.043" | Normativa | §I.A.2 | ⏳ |
| 2 | "Fallos CSJN T.340:1313" | Jurisprudencia | §III.1 | ⏳ |
| 3 | "la jurisprudencia pacífica 🔲" | Jurisprudencia | §II.B | 🔲 |
```

### Paso 3 · Búsqueda de fuentes

Leer la tabla de fuentes verificadas (`jurisprudencia/fuentes-*.md`). Por cada cita
extraída en Paso 2:

1. ¿Existe en la tabla de fuentes?
   - **SÍ:** anotarla con ✅, UUID y URL de fuente.
   - **NO:** ¿está marcada con 🔲 en el escrito original?
     - **SÍ:** anotarla con 🔲 (decisión del abogado de dejarla pendiente).
     - **NO:** marcar como 🔴 BLOQUEANTE.

### Paso 4 · Cruce y reconciliación

Actualizar tabla provisional con resultados:

```markdown
| N° | Cita textual | Tipo | Sección | En tabla fuentes | UUID SAIJ | Estatus |
|----|--------------|------|---------|------------------|-----------|---------|
| 1 | "Art. 15, Ley N° 27.043" | Normativa | §I.A.2 | SÍ | abc-123 | ✅ |
| 2 | "Fallos CSJN T.340:1313" | Jurisprudencia | §III.1 | SÍ | def-456 | ✅ |
| 3 | "jurisprudencia pacífica 🔲" | Jurisprudencia | §II.B | NO | — | 🔲 |
| 4 | "Decreto N° 1234/2023" | Normativa | §IV.1 | NO | — | 🔴 BLOQUEANTE |
```

### Paso 5 · Reporte de bloqueos

Listar TODO lo que es 🔴 (bloqueante). Cada ítem bloquea el cierre del escrito:

> **🔴 BLOQUEANTES (DEBEN RESOLVERSE):**
> - Ítem 4: "Decreto N° 1234/2023" en §IV.1 · Solución: verificar en SAIJ e incorporar a tabla, o reformular el párrafo sin esa cita

### Paso 6 · Pendientes (decisiones del abogado)

Listar TODO lo que es 🔲. Son decisiones que el abogado debe confirmar antes de
presentar:

> **🔲 PENDIENTES (DECISIÓN DEL ABOGADO):**
> - Ítem 3: "jurisprudencia pacífica" en §II.B · Acción: ampliar la cita (nombre, año, tribunal) para verificación, o confirmar deliberadamente dejarla genérica

### Paso 7 · Cierre y registro

Guardar el reporte completo como `jurisprudencia/AUDITORIA-[fecha-hora].md`.
Incluir:
- Escrito auditado (nombre y sección)
- Tabla completa de citas (4 Paso)
- Bloqueantes (Paso 5)
- Pendientes (Paso 6)
- Timestamp de auditoría

Ejemplo:

```markdown
# Auditoría de citas · [Nombre del escrito]

**Fecha:** 2026-08-16 14:30  
**Escrito:** escritos/demanda-principal.md  
**Tabla de fuentes:** jurisprudencia/fuentes-exp-123456.md

## Resumen

- ✅ Verificadas: 8
- 🔴 Bloqueantes: 2
- 🔲 Pendientes: 1

## Tabla completa de citas

[la tabla del Paso 4 aquí]

## 🔴 BLOQUEANTES

- Ítem 4: "Decreto N° 1234/2023" → NO ESTÁ EN TABLA, SIN MARCA 🔲 EN ESCRITO
- Ítem 7: "Cámara de Apelaciones…" → REFERENCIA INCOMPLETA, NO VERIFICABLE

## 🔲 PENDIENTES

- Ítem 3: "jurisprudencia pacífica" → ESCRITO MARCA 🔲, REQUIERE DECISIÓN DEL ABOGADO
```

## Integración en argentina-bucles (Paso 6)

**Paso 6 MODIFICADO · Verificación final de citas con auditoría**

1. Correr esta skill: **argentina-auditoria-citas** sobre el escrito borrador.
2. Resolver TODO lo que sea 🔴 (bloqueante):
   - Opción A: incorporar la fuente a la tabla (buscar en SAIJ si falta)
   - Opción B: eliminar la cita y reformular el párrafo
   - Opción C: marcar como 🔲 si es deliberadamente genérica
3. Confirmar TODO lo que sea 🔲 (pendiente): es decisión irreversible.
4. Entregar: escrito limpio + tabla de fuentes + reporte de auditoría.

## Integración en argentina-diagnostico (Sección G)

**Sección G MODIFICADO · Derecho (con auditoría de citas)**

1. Leer la sección de Derecho del escrito.
2. Correr esta skill: **argentina-auditoria-citas**.
3. En la tabla de diagnóstico (G):
   - 🟢 si todas las citas son ✅ (verificadas) o 🔲 (pendientes deliberadas)
   - 🟡 si hay citas verificadas pero la tabla de fuentes está incompleta
   - 🔴 si hay citas 🔴 bloqueantes sin resolver

## Reglas duras

1. **Sin cita = sin afirmación.** Toda afirmación fáctica o normativa va con cita.
2. **Sin verificación = 🔲.** No hay "probablemente", "creo que", "la doctrina dice":
   o está en la tabla o va marcada 🔲.
3. **Auditoría SIEMPRE.** Tanto en redacción nueva (argentina-bucles) como en
   diagnóstico de existentes (argentina-diagnostico), el paso de auditoría es
   OBLIGATORIO. No hay cierre sin él.
4. **La tabla es viva.** Conforme se desarrolla el caso, la tabla de fuentes
   `jurisprudencia/fuentes-*.md` crece. Pero el escrito solo puede citar lo que
   está en su tabla correspondiente.

## Herramientas MCP requeridas

- `saij_buscar_legislacion` y `saij_buscar_jurisprudencia`: para buscar citas
  cuando el escrito las incluye pero no están en la tabla local (decisión: crearlas
  o marca 🔲).
- `saij_documento(uuid)`: para verificar el contenido exacto de cada cita cuando
  se agrega a la tabla.

## Checksum de auditoría

Para asegurar que una auditoría fue completa, verificar que la suma de:
(Verificadas ✅) + (Bloqueantes 🔴) + (Pendientes 🔲) = Total de citas extraídas

Si no coinciden, rehacer la auditoría.
