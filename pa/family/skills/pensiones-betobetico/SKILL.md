---
name: pensiones-betobetico
title: /pensiones
description: Estima de forma orientativa la pensión alimenticia a los hijos y la pensión alimenticia entre cónyuges en procesos de familia bajo el Código de la Familia de Panamá. Aplica el criterio de proporcionalidad (necesidades del alimentista y caudal del alimentante) y los criterios del Código de la Familia para la pensión entre cónyuges. El resultado es SIEMPRE orientativo y requiere revisión profesional. Usar cuando el usuario dice "calcula la pensión", "pensión alimenticia", "pensión de cónyuge", "cuánto corresponde de alimentos", o necesita una estimación para un convenio o demanda.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/familia/skills/pensiones
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: family
language: es
---

# /pensiones

1. Leer `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` — perfil de práctica y baremos.
2. Recopilar datos económicos de ambas partes.
3. Calcular estimación de pensión alimenticia a los hijos.
4. Evaluar procedencia de pensión alimenticia entre cónyuges.
5. Producir el informe orientativo.

---

## Propósito

Producir una estimación orientativa de las pensiones alimenticias (a los hijos y, en su caso, entre cónyuges) para facilitar la negociación y redacción de convenios de divorcio o demandas. SIEMPRE es orientativo — los juzgados seccionales de familia aplican criterios propios y las circunstancias de cada caso son determinantes.

## ADVERTENCIA PERMANENTE

> **Este cálculo es ORIENTATIVO.** No vincula a ningún juzgado. En Panamá no existen tablas oficiales de cálculo de pensiones: la cuantía se fija por el principio de proporcionalidad del Código de la Familia. La pensión entre cónyuges depende de una valoración integral que solo el juez puede hacer con todos los elementos. Cualquier cifra producida por este skill requiere validación por un abogado idóneo que conozca los criterios del juzgado competente.

## Datos necesarios

### Para la pensión alimenticia a los hijos

- **Ingresos netos mensuales** de cada progenitor (planilla, rendimientos, prestaciones), en balboas (B/.) / USD.
- **Número de hijos menores** o mayores dependientes.
- **Tipo de guarda** — compartida o exclusiva.
- **Necesidades especiales** de los menores (discapacidad, enfermedad, actividades).
- **Gastos de vivienda** — hipoteca/alquiler, quién lo paga.
- **Ciudad/localidad** — el costo de vida varía (área metropolitana vs. interior).

### Para la pensión alimenticia entre cónyuges

- **Ingresos netos mensuales** de cada cónyuge.
- **Patrimonio de cada cónyuge.**
- **Duración del matrimonio.**
- **Edad de cada cónyuge.**
- **Dedicación a la familia** — quién dejó de trabajar o redujo jornada, durante cuánto tiempo.
- **Cualificación profesional y perspectivas laborales.**
- **Estado de salud.**
- **Colaboración en la actividad profesional del otro cónyuge.**

## Pensión alimenticia a los hijos (Código de la Familia de Panamá)

### Criterios legales

- **Principio de proporcionalidad:** la cuantía será proporcional al caudal de quien los da y a las necesidades de quien los recibe. [verificar art. del Código de la Familia]
- **Determinación judicial:** el juez determinará la contribución de cada progenitor. [verificar art.]
- **Contenido de los alimentos:** comprende sustento, habitación, vestido, asistencia médica y educación. [verificar art.]

### Criterios de cálculo

En Panamá no hay tablas oficiales; el cálculo descansa en la proporcionalidad. Variables habituales:

| Variable | Uso en el cálculo |
|---|---|
| Ingresos netos del obligado al pago | Eje principal — capacidad económica del alimentante |
| Número de hijos | A más hijos, mayor carga total a repartir |
| Guarda compartida | Ajuste a la baja (ambos contribuyen en especie durante su tiempo) |
| Área metropolitana vs. interior | Ajuste por costo de vida |
| Necesidades especiales | Incremento individualizado |

### Mínimo de subsistencia

Debe garantizarse un mínimo de subsistencia al menor incluso cuando el obligado tiene ingresos muy bajos. La cifra orientativa varía según el caso y el juzgado [verificar — no hay cuantía legal fija].

### Gastos extraordinarios

| Tipo | Clasificación habitual | Reparto |
|---|---|---|
| Sanitarios no cubiertos por la CSS o el seguro | Extraordinario necesario | 50/50 o proporcional — sin necesidad de acuerdo previo |
| Actividades extraescolares | Extraordinario no necesario | Requiere acuerdo previo de ambos progenitores |
| Material escolar ordinario | Ordinario (incluido en pensión) | — |
| Excursiones del colegio | Ordinario | — |
| Ortodoncia, lentes | Extraordinario necesario | 50/50 o proporcional |

## Pensión alimenticia entre cónyuges (Código de la Familia de Panamá)

### Criterios

El juez fijará la pensión considerando, entre otros [verificar arts. del Código de la Familia]:

1. **Los acuerdos previos de los cónyuges.**
2. **La edad y estado de salud.**
3. **La cualificación profesional y probabilidades de acceso al empleo.**
4. **La dedicación pasada y futura a la familia.**
5. **La colaboración en la actividad del otro cónyuge.**
6. **La duración del matrimonio y la convivencia.**
7. **La pérdida de derechos económicos.**
8. **El caudal y medios de cada cónyuge.**

### Estimación orientativa

No existe una fórmula legal. Criterios prácticos habituales:

| Factor | Indicador | Peso orientativo |
|---|---|---|
| Necesidad / desequilibrio económico | Diferencia de ingresos | Requisito previo — sin necesidad, no hay pensión entre cónyuges |
| Duración del matrimonio | < 5 años / 5-15 / 15-25 / > 25 | A mayor duración, mayor cuantía y duración |
| Dedicación a la familia | Total / parcial / ninguna | Determinante |
| Edad y empleabilidad | Joven con formación / mayor sin formación | Determinante para duración |

### Duración

- **Temporal:** opción habitual. Duración orientativa: entre 1/3 y la totalidad de la duración del matrimonio, según circunstancias.
- **Indefinida:** casos excepcionales — matrimonios muy largos, cónyuge de edad avanzada sin posibilidad de inserción laboral.

## Formato de salida

```markdown
ORIENTATIVO — ESTIMACIÓN DE PENSIONES — NO VINCULANTE — REVISIÓN DE ABOGADO OBLIGATORIA

> **Nota para el revisor**
> - **Datos utilizados:** [qué datos se proporcionaron y cuáles se estimaron]
> - **Criterio de proporcionalidad:** [cómo se aplicó]
> - **Criterios del juzgado habitual:** [si constan en el perfil de práctica]
> - **Antes de actuar:** contrastar con criterios del juzgado competente; verificar ingresos reales con documentación (planilla, declaración del ISR ante la DGI); ajustar a las circunstancias concretas del caso.

## Estimación de pensiones: [Caso X]

### Pensión alimenticia a los hijos

| Concepto | Valor |
|---|---|
| Ingresos netos progenitor A | [importe en B/.] |
| Ingresos netos progenitor B | [importe en B/.] |
| N.o de hijos | [N] |
| Tipo de guarda | [compartida / exclusiva] |
| **Estimación orientativa** | **[rango] B/. /mes** |
| Actualización | Índice de precios al consumidor (anual) |

**Fundamentación:** [explicación del cálculo]

### Gastos extraordinarios — Propuesta de reparto

| Tipo | Reparto propuesto | Acuerdo previo necesario |
|---|---|---|
| [tipo] | [reparto] | [sí/no] |

### Pensión alimenticia entre cónyuges

| Criterio | Valoración |
|---|---|
| Necesidad / desequilibrio económico | [sí/no — cuantificación] |
| Duración del matrimonio | [años] |
| Dedicación a la familia | [total/parcial/ninguna] |
| Edad y empleabilidad | [valoración] |
| **Estimación orientativa** | **[importe] B/. /mes durante [duración]** |

**Fundamentación:** [explicación de los criterios aplicados]

---

**Qué hacer a continuación:**
1. **Incluir en convenio** — `/familia:convenio` con las cifras estimadas.
2. **Ajustar el cálculo** — aporta más datos para afinar la estimación.
3. **Comparar con criterios del juzgado** — si conoces los criterios de tu juzgado, dime y ajusto.
4. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Código de la Familia de Panamá** — alimentos a los hijos en sentencia de nulidad, separación o divorcio. [verificar art.]
- **Código de la Familia** — pensión alimenticia entre cónyuges. [verificar art.]
- **Código de la Familia** — alimentos entre parientes y contenido de los alimentos. [verificar arts.]
- **Código de la Familia** — proporcionalidad de los alimentos. [verificar art.]

## Guardarraíles

- **SIEMPRE orientativo.** Repetir en cada salida que las cifras no vinculan al juzgado.
- **No inventar ingresos.** Si no hay datos de ingresos, no calcular — pedir los datos.
- **En Panamá no hay tablas oficiales.** El cálculo descansa en la proporcionalidad; no presentar ninguna cifra como baremo vinculante.
- **No confundir pensión a los hijos con pensión entre cónyuges.** La de los hijos es irrenunciable; la pensión entre cónyuges es disponible. Fundamentos, criterios y consecuencias de impago son distintos.
- **Guarda compartida NO elimina la pensión alimenticia.** Si hay desproporción de ingresos, procede pensión aunque la guarda sea compartida.
- **No pasar por alto el mínimo de subsistencia.** Incluso con ingresos muy bajos del obligado, debe garantizarse un mínimo al menor.
- **La pensión entre cónyuges no es automática.** Requiere necesidad y desequilibrio económico. Si ambos cónyuges trabajan con ingresos similares, no procede.
- **El impago de pensión alimenticia puede tener consecuencias penales.** En Panamá el incumplimiento de la obligación de alimentos puede dar lugar a sanciones (apremio corporal / responsabilidad penal) [verificar base legal].
