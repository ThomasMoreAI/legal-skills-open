---
name: pensiones
title: /pensiones
description: Estima de forma orientativa la pensión de alimentos y la pensión compensatoria en procesos de familia. Usa las tablas orientadoras del CGPJ para alimentos y los criterios del art. 97 CC para la compensatoria. El resultado es SIEMPRE orientativo y requiere revisión profesional. Usar cuando el usuario dice "calcula la pensión", "pensión de alimentos", "pensión compensatoria", "cuánto corresponde de alimentos", o necesita una estimación para un convenio o demanda.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/familia/skills/pensiones
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: family
language: es
---

# /pensiones

1. Leer `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` — perfil de práctica y baremos.
2. Recopilar datos económicos de ambas partes.
3. Calcular estimación de pensión alimenticia.
4. Evaluar procedencia de pensión compensatoria.
5. Producir el informe orientativo.

---

## Propósito

Producir una estimación orientativa de las pensiones de alimentos y compensatoria para facilitar la negociación y redacción de convenios reguladores o demandas. SIEMPRE es orientativo — los juzgados aplican criterios propios y las circunstancias de cada caso son determinantes.

## ADVERTENCIA PERMANENTE

> **Este cálculo es ORIENTATIVO.** No vincula a ningún juzgado. Las tablas del CGPJ son orientadoras, no vinculantes. La pensión compensatoria depende de una valoración integral que solo el juez puede hacer con todos los elementos. Cualquier cifra producida por este skill requiere validación por un letrado que conozca los criterios del juzgado competente.

## Datos necesarios

### Para la pensión de alimentos

- **Ingresos netos mensuales** de cada progenitor (nómina, rendimientos, prestaciones).
- **Número de hijos menores** o mayores dependientes.
- **Tipo de custodia** — compartida o exclusiva.
- **Necesidades especiales** de los menores (discapacidad, enfermedad, actividades).
- **Gastos de vivienda** — hipoteca/alquiler, quién lo paga.
- **Ciudad/localidad** — el coste de vida varía.

### Para la pensión compensatoria

- **Ingresos netos mensuales** de cada cónyuge.
- **Patrimonio de cada cónyuge.**
- **Duración del matrimonio.**
- **Edad de cada cónyuge.**
- **Dedicación a la familia** — quién dejó de trabajar o redujo jornada, durante cuánto tiempo.
- **Cualificación profesional y perspectivas laborales.**
- **Estado de salud.**
- **Colaboración en la actividad profesional del otro cónyuge.**

## Pensión de alimentos (arts. 142-153 CC)

### Criterios legales

- **Art. 146 CC:** La cuantía será proporcional al caudal de quien los da y a las necesidades de quien los recibe.
- **Art. 93 CC:** El juez determinará la contribución de cada progenitor.
- **Art. 142 CC:** Comprende sustento, habitación, vestido, asistencia médica, educación.

### Tablas orientadoras del CGPJ

Las tablas del CGPJ (actualizadas periódicamente) cruzan los ingresos del obligado al pago con el número de hijos para obtener un rango orientativo. Son una referencia, no un baremo vinculante.

| Variable | Uso en el cálculo |
|---|---|
| Ingresos netos del obligado al pago | Eje principal de las tablas CGPJ |
| Número de hijos | Columna de las tablas |
| Custodia compartida | Ajuste a la baja (ambos contribuyen en especie durante su tiempo) |
| Ciudad grande vs. pequeña | Ajuste por coste de vida |
| Necesidades especiales | Incremento individualizado |

### Mínimo vital

El Tribunal Supremo ha establecido que existe un mínimo vital que debe garantizarse incluso cuando el obligado tiene ingresos muy bajos. La cifra orientativa varía entre 150-200 EUR/hijo/mes [verificar — varía por juzgado y fecha].

### Gastos extraordinarios

| Tipo | Clasificación habitual | Reparto |
|---|---|---|
| Sanitarios no cubiertos por SS | Extraordinario necesario | 50/50 o proporcional — sin necesidad de acuerdo previo |
| Actividades extraescolares | Extraordinario no necesario | Requiere acuerdo previo de ambos progenitores |
| Material escolar ordinario | Ordinario (incluido en pensión) | — |
| Excursiones del colegio | Ordinario | — |
| Ortodoncias, gafas | Extraordinario necesario | 50/50 o proporcional |

## Pensión compensatoria (art. 97 CC)

### Criterios del art. 97 CC

El juez fijará la pensión considerando:

1. **Los acuerdos previos de los cónyuges.**
2. **La edad y estado de salud.**
3. **La cualificación profesional y probabilidades de acceso al empleo.**
4. **La dedicación pasada y futura a la familia.**
5. **La colaboración en la actividad del otro cónyuge.**
6. **La duración del matrimonio y la convivencia.**
7. **La pérdida de derechos económicos.**
8. **El caudal y medios de cada cónyuge.**

### Estimación orientativa

No existe una fórmula legal. Criterios prácticos habituales en la jurisprudencia:

| Factor | Indicador | Peso orientativo |
|---|---|---|
| Desequilibrio económico | Diferencia de ingresos | Requisito previo — sin desequilibrio, no hay compensatoria |
| Duración del matrimonio | < 5 años / 5-15 / 15-25 / > 25 | A mayor duración, mayor cuantía y duración |
| Dedicación a la familia | Total / parcial / ninguna | Determinante |
| Edad y empleabilidad | Joven con formación / mayor sin formación | Determinante para duración |

### Duración

- **Temporal:** tendencia mayoritaria del TS. Duración orientativa: entre 1/3 y la totalidad de la duración del matrimonio, según circunstancias.
- **Indefinida:** casos excepcionales — matrimonios muy largos, cónyuge de edad avanzada sin posibilidad de inserción laboral.

## Formato de salida

```markdown
ORIENTATIVO — ESTIMACIÓN DE PENSIONES — NO VINCULANTE — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Datos utilizados:** [qué datos se proporcionaron y cuáles se estimaron]
> - **Tablas CGPJ:** [se aplicaron / no se aplicaron — motivo]
> - **Criterios del juzgado habitual:** [si constan en el perfil de práctica]
> - **Antes de actuar:** contrastar con criterios del juzgado competente; verificar ingresos reales con documentación fiscal; ajustar a las circunstancias concretas del caso.

## Estimación de pensiones: [Caso X]

### Pensión de alimentos

| Concepto | Valor |
|---|---|
| Ingresos netos progenitor A | [importe] |
| Ingresos netos progenitor B | [importe] |
| N.o de hijos | [N] |
| Tipo de custodia | [compartida / exclusiva] |
| **Estimación orientativa** | **[rango] EUR/mes** |
| Actualización | IPC anual |

**Fundamentación:** [explicación del cálculo]

### Gastos extraordinarios — Propuesta de reparto

| Tipo | Reparto propuesto | Acuerdo previo necesario |
|---|---|---|
| [tipo] | [reparto] | [sí/no] |

### Pensión compensatoria

| Criterio art. 97 CC | Valoración |
|---|---|
| Desequilibrio económico | [sí/no — cuantificación] |
| Duración del matrimonio | [años] |
| Dedicación a la familia | [total/parcial/ninguna] |
| Edad y empleabilidad | [valoración] |
| **Estimación orientativa** | **[importe] EUR/mes durante [duración]** |

**Fundamentación:** [explicación de los criterios aplicados]

---

**Qué hacer a continuación:**
1. **Incluir en convenio** — `/familia:convenio` con las cifras estimadas.
2. **Ajustar el cálculo** — aporta más datos para afinar la estimación.
3. **Comparar con criterios del juzgado** — si conoces los criterios de tu juzgado, dime y ajusto.
4. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **CC art. 93** — alimentos a los hijos en sentencia de nulidad, separación o divorcio.
- **CC art. 97** — pensión compensatoria.
- **CC arts. 142-153** — alimentos entre parientes.
- **CC art. 146** — proporcionalidad de los alimentos.
- **Tablas orientadoras del CGPJ** — publicadas periódicamente.

## Guardarraíles

- **SIEMPRE orientativo.** Repetir en cada salida que las cifras no vinculan al juzgado.
- **No inventar ingresos.** Si no hay datos de ingresos, no calcular — pedir los datos.
- **Las tablas del CGPJ no son vinculantes.** Muchos juzgados no las aplican o las aplican con variaciones significativas.
- **No confundir pensión alimenticia con compensatoria.** La alimenticia es para los hijos (irrenunciable); la compensatoria es entre cónyuges (disponible). Fundamentos, criterios y consecuencias de impago son completamente distintos.
- **Custodia compartida NO elimina la pensión alimenticia.** Si hay desproporción de ingresos, procede pensión aunque la custodia sea compartida (STS 55/2016 y posteriores).
- **No pasar por alto el mínimo vital.** Incluso con ingresos muy bajos del obligado, existe un mínimo.
- **La pensión compensatoria no es automática.** Requiere desequilibrio económico causado por el matrimonio. Si ambos cónyuges trabajan con ingresos similares, no procede.
