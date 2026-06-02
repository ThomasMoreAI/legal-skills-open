---
name: escritos-civiles-mx
title: Asistente de escritos civiles mexicanos
description: Genera primer borrador estructurado de escritos civiles mexicanos (demanda, contestación, recurso, promoción, alegatos) siguiendo el formato procesal del Código Federal de Procedimientos Civiles y los códigos locales. Cada borrador incluye sección de hechos numerados con referencia a anexos, preceptos invocados con cita literal del DOF, y argumentos jurídicos con anclaje en jurisprudencia SCJN cuando aplique. Usar cuando el abogado mexicano necesita producir el primer borrador de un escrito civil y quiere acelerar la redacción manteniendo la estructura procesal correcta. NO sustituye criterio profesional final.
author: migaceta
author_url: https://github.com/migaceta/skills-claude-derecho-mx/tree/main/escritos-civiles-mx
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: mx
practice: litigation
language: es
---

# Asistente de escritos civiles mexicanos

## Cuándo usar esta skill

- Tu cliente presenta un caso civil (mercantil, familiar, sucesorio, contractual, responsabilidad extracontractual) y necesitas el primer borrador del escrito.
- Tienes los hechos, las pruebas (anexos) y los preceptos relevantes — la skill estructura el escrito; tú validas.
- Quieres asegurar que el escrito sigue el formato procesal correcto antes de personalizar voz y argumentación.

## Reglas no negociables (heredadas del libro Cap 3)

1. **Validación obligatoria de citas.** La skill NO inventa números de registro de tesis. Si no identifica criterio aplicable, lo declara explícitamente: "No identifiqué criterio aplicable con los datos provistos". Bajo ninguna circunstancia genera referencias jurisprudenciales que no puedas verificar en `sjf2.scjn.gob.mx` o `bj.scjn.gob.mx`.

2. **Sanitización previa.** Antes de pegar el caso a esta skill, sanitiza datos identificables del cliente (nombres, RFC, CURP, montos exactos, fechas, direcciones) usando la skill `sanitizar-mx` o el [sanitizador en línea](https://migaceta.com/libros/ia-abogados/sanitizador).

3. **Referencia obligatoria al DOF.** Cada precepto citado debe llevar referencia a la fecha de publicación en el DOF y, si aplica, a la última reforma vigente.

## Estructura del output

La skill produce un escrito con cinco secciones:

### 1. Identificación procesal
- Tribunal competente (justifica competencia con artículo aplicable)
- Tipo de juicio (oral, ordinario, ejecutivo, especial, etc.)
- Partes (con marcadores `[PARTE-ACTORA]`, `[PARTE-DEMANDADA]` sanitizados)
- Vía procesal específica

### 2. Hechos
- Numerados con orden cronológico estricto
- Cada hecho referencía el anexo aplicable entre paréntesis: `(Anexo 1)`
- NO incluye conclusiones jurídicas (eso va en preceptos)
- Máximo 12 puntos para escritos iniciales, 18 para complejos

### 3. Preceptos legales aplicables
- Cita literal del precepto con número del artículo
- Referencia DOF de publicación + última reforma vigente
- Si hay reglamento aplicable: cita el artículo del reglamento

### 4. Argumentos jurídicos
- Estructura: precepto → interpretación judicial vigente → aplicación al caso → conclusión
- Tesis SCJN solo si la skill puede citar registro verificable; en caso contrario, indica "criterio pendiente de validación humana"
- Doctrina puede mencionarse pero el abogado debe validar atribución

### 5. Petitorio
- Concreto, numerado
- Cada punto del petitorio anclado en un argumento previo

## Ejemplo trabajado

**Input del usuario:**

> "Necesito demanda mercantil por incumplimiento de contrato de compraventa. Cliente [PARTE-ACTORA] vendió maquinaria a [PARTE-DEMANDADA] el [FECHA]. El comprador no pagó. Anexos: contrato, facturas, requerimientos extrajudiciales."

**Output esperado:**

```
═══════════════════════════════════════════════════════════
ESCRITO DE DEMANDA — JUICIO ORAL MERCANTIL

H. Juzgado [Letra y número] de lo Mercantil del [Distrito Judicial]
[Estado]

[PARTE-ACTORA], promoviendo en mi propio derecho, ante usted con
todo respeto comparezco para exponer:

I. HECHOS

1. Con fecha [FECHA-1] celebré contrato de compraventa con
   [PARTE-DEMANDADA], cuyo objeto fue la transmisión de propiedad
   sobre maquinaria industrial. (Anexo 1: Contrato de compraventa)

2. ...

II. PRECEPTOS LEGALES APLICABLES

A. Código de Comercio (publicado en DOF 13 de diciembre de 1889,
   con últimas reformas vigentes a [fecha]):

   - Artículo 1391: "...[cita literal]..."
   - Artículo 1392: "...[cita literal]..."

III. ARGUMENTOS JURÍDICOS

...

IV. PETITORIO

PRIMERO. Tenérseme por presentado en términos del presente escrito.
SEGUNDO. ...

═══════════════════════════════════════════════════════════
NOTAS DE VALIDACIÓN HUMANA PENDIENTE
- Verificar artículos del Código de Comercio contra DOF
- Si decides invocar tesis SCJN específica, búscala en sjf2.scjn.gob.mx
- Reescribir al menos un párrafo para preservar voz autoral
- Aplicar checklist de validación pre-firma del libro
```

## Test mínimo verificable

**Test 1.** Dado un caso con cliente sanitizado y anexos identificados, la skill produce escrito con las 5 secciones estructurales (Identificación, Hechos, Preceptos, Argumentos, Petitorio) sin omisión.

**Test 2.** La skill NO inventa números de registro de tesis SCJN. Si se le pide jurisprudencia que no puede verificar, responde explícitamente "criterio pendiente de validación humana".

**Test 3.** Cada precepto citado lleva referencia DOF de publicación.

## Limitaciones honestas

- Esta skill genera **primer borrador estructural**. No sustituye el conocimiento jurídico ni el criterio profesional del abogado responsable.
- Las tesis SCJN deben verificarse manualmente en fuente primaria antes de incorporar al escrito final.
- Para amparo (directo o indirecto) usar la skill complementaria `amparo-redactor`.
- Para temas IP, derecho autoral, INDAUTOR usar la skill `indaut-research-mx`.

## Cómo se relaciona con el libro

Esta skill aplica las Reglas 1 y 5 del Capítulo 3 ("Cinco reglas no negociables") y se complementa con la Plantilla 5 del back matter ("Checklist de validación de output IA"). Para el _stack_ completo de adopción ver Capítulo 14 ("Adoptando IA en tu práctica").

---

**Licencia:** CC BY 4.0. Modificación y redistribución con atribución
permitidas. Repositorio: `github.com/migaceta/skills-claude-derecho-mx`.
