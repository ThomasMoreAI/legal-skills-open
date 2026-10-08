---
name: revision-fiscal-4101-betobetico
title: /revision
description: Revisor de declaraciones tributarias — revisión de coherencia de declaraciones fiscales. Cruza IVA deducido vs soportado, retenciones practicadas vs declaradas, base imponible del IS y otros parámetros. Marca discrepancias. Usar cuando el usuario diga "revisa esta declaración", "coherencia fiscal", "cuadre de modelos", "revisar 303" o adjunte datos.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/fiscal/skills/revision
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# /revision

1. Cargar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` → tipo de entidad, régimen, criterios.
2. Obtener los datos de la declaración.
3. Ejecutar las comprobaciones de coherencia.
4. Marcar discrepancias.
5. Generar informe de revisión.

```
/fiscal:revision
Modelo 303 del 2T 2026: IVA devengado 45.000 EUR, IVA soportado deducible
52.000 EUR, resultado a compensar 7.000 EUR.
```

---

## Propósito

Una declaración tributaria incoherente internamente o con otras declaraciones del mismo período es una señal roja para la AEAT. Este skill ejecuta las comprobaciones cruzadas habituales que un buen asesor fiscal realiza antes de presentar: ¿cuadran los números entre modelos? ¿hay discrepancias que la AEAT detectará automáticamente?

---

## Comprobaciones por modelo

### Modelo 303 (IVA)

| Comprobación | Cruce | Discrepancia típica |
|---|---|---|
| IVA devengado vs libro de facturas emitidas | Base imponible × tipo = cuota repercutida | Error en tipo aplicado o base |
| IVA soportado deducible vs libro de facturas recibidas | Solo deducible si cumple requisitos art. 92-100 LIVA | Facturas no deducibles incluidas |
| Prorrata | Si aplica: ¿se ha aplicado correctamente el % de prorrata? | Error en cálculo de prorrata |
| Operaciones no sujetas / exentas | ¿Se han declarado correctamente en las casillas correspondientes? | Operaciones mal clasificadas |
| Coherencia 303 ↔ 390 | Suma de los 303 del año = 390 | Diferencias por regularizaciones no cuadradas |
| Coherencia 303 ↔ 349 | Operaciones intracomunitarias del 303 = las del 349 | Operaciones no declaradas en uno u otro |

### Modelo 111 / 190 (Retenciones)

| Comprobación | Cruce | Discrepancia típica |
|---|---|---|
| Retenciones practicadas vs declaradas | Nóminas + facturas profesionales → mod. 111 | Retención mal calculada o no declarada |
| Coherencia 111 ↔ 190 | Suma de los 111 del año = 190 | Perceptor no incluido en el resumen anual |
| Retenciones ↔ certificados emitidos | Lo retenido = lo certificado al perceptor | Discrepancia genera incidencia al perceptor |

### Modelo 200 (Impuesto sobre Sociedades)

| Comprobación | Cruce | Discrepancia típica |
|---|---|---|
| Resultado contable → Base imponible | Ajustes extracontables correctamente aplicados | Ajuste omitido o duplicado |
| Tipo impositivo | ¿Se aplica el tipo correcto? (25% general, 23% para entidades <1M facturación, etc.) | Tipo incorrecto |
| Pagos fraccionados (mod. 202) | ¿Coherentes con el resultado final? | Diferencia significativa pagos vs liquidación |
| Bases imponibles negativas compensadas | ¿Dentro de los límites legales? (art. 26 LIS) | Compensación excesiva |
| Deducciones aplicadas | ¿Cumplen requisitos? ¿Dentro del límite conjunto? | Deducción no aplicable o excedida |

### Modelo 100 (IRPF)

| Comprobación | Cruce | Discrepancia típica |
|---|---|---|
| Rendimientos del trabajo | ¿Coinciden con certificados de retenciones? | Rendimiento no declarado |
| Rendimientos de actividades | ¿Coherentes con libros de ingresos y gastos? | Diferencia ingresos/gastos |
| Retenciones soportadas | ¿Coinciden con certificados? | Retención no aplicada |
| Deducciones autonómicas | ¿Se aplican las del domicilio fiscal correcto? | Deducción de otra comunidad |

---

## Comprobaciones cruzadas entre modelos

| Cruce | Qué verificar |
|---|---|
| 303 ↔ 200 | Ingresos declarados en IVA coherentes con cifra de negocio en IS |
| 111 ↔ 200 | Retenciones practicadas como gasto vs retenciones declaradas |
| 347 ↔ contrapartes | Operaciones >3.005,06 EUR declaradas por ambas partes |
| 190 ↔ perceptores | Retenciones certificadas = retenciones declaradas |

---

## Formato de salida

```markdown
# Revisión de declaración: Modelo [número] — [período]

**Entidad:** [nombre]
**Período:** [trimestre/año]
**Fecha de revisión:** [fecha]

---

## Resultado de la revisión

| Estado | Descripción |
|---|---|
| **Discrepancias encontradas** | [N] |
| **De las cuales críticas** | [N] |

---

## Detalle de comprobaciones

| # | Comprobación | Resultado | Discrepancia | Impacto | Acción |
|---|---|---|---|---|---|
| 1 | [Ej., IVA devengado vs libro] | [Cuadra / Discrepancia] | [Diferencia de 1.200 EUR] | [Potencial requerimiento] | [Revisar factura X] |
| 2 | ... | ... | ... | ... | ... |

---

## Discrepancias críticas (resolver antes de presentar)

[Lista detallada con origen de la discrepancia y solución propuesta]

---

## Observaciones

[Notas adicionales: cambios normativos que afectan al período, criterios interpretativos aplicados]
```

---

## Legislación de referencia

- LIVA (Ley 37/1992) — arts. 92-100 (deducciones), 164-166 (obligaciones formales)
- LIS (Ley 27/2014) — arts. 10-26 (base imponible), 29-39 (deducciones)
- LIRPF (Ley 35/2006) — régimen general
- LGT (Ley 58/2003) — arts. 119-120 (autoliquidaciones)
- RIRPF (RD 439/2007) — tipos de retención

---

## Lo que este skill NO hace

- No presenta declaraciones ante la AEAT — revisa la coherencia antes de presentar.
- No calcula la cuota a ingresar desde cero — verifica la coherencia de los datos facilitados.
- No sustituye al asesor fiscal — identifica discrepancias para que el profesional decida.
