---
name: condiciones-generales-4008-betobetico
title: /condiciones-generales
description: Revisor de condiciones generales de la contratación — analiza unas CGC para contratos de adhesión con consumidores, aplica el control de inclusión y el control de contenido de la Ley 45 de 2007 y marca cláusulas con riesgo de nulidad por abusivas. Usar cuando el usuario diga "revisa estas condiciones", "son abusivas estas cláusulas", "T&C", "condiciones generales" o adjunte unas condiciones de contratación.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/consumo/skills/condiciones-generales
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: consumer
language: es
---

# /condiciones-generales

1. Cargar `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md` → sector, tipo de contrato, canal de venta.
2. Obtener las condiciones generales.
3. Aplicar control de inclusión del contrato de adhesión (Ley 45 de 2007).
4. Aplicar control de contenido — cláusulas abusivas (Ley 45 de 2007).
5. Generar lista de cláusulas con riesgo de nulidad.

```
/consumo:condiciones-generales
[pegar las condiciones generales del e-commerce]
```

---

## Propósito

Las condiciones generales de la contratación (CGC) en contratos de adhesión con consumidores están sujetas a un doble control en derecho panameño: el control de inclusión (que la cláusula se haya incorporado válidamente al contrato) y el control de contenido (que no sea abusiva), conforme a la Ley 45 de 2007. Una cláusula abusiva es nula. Este skill revisa ambos controles y marca las cláusulas problemáticas.

---

## Control de inclusión del contrato de adhesión (Ley 45 de 2007)

Las CGC solo forman parte del contrato si: [verificar]

| Requisito | Base legal | Verificar |
|---|---|---|
| **Transparencia formal** | Ley 45 de 2007 | Redacción clara, concreta y sencilla |
| **Accesibilidad** | Ley 45 de 2007 | El adherente pudo conocerlas antes de contratar |
| **Aceptación expresa** | Ley 45 de 2007 | Referencia expresa a las CGC; firmadas o aceptadas |
| **Legibilidad** | Ley 45 de 2007 | Tamaño de letra, formato, estructura comprensible |
| **Contratación electrónica** | Ley 45 de 2007 | Disponibles para almacenar y reproducir |

**Consecuencia del incumplimiento:** La cláusula no se incorpora al contrato. El contrato subsiste sin ella si es viable. [verificar]

---

## Control de contenido — Cláusulas abusivas (Ley 45 de 2007)

### Cláusula general de abusividad [verificar]

Son abusivas las cláusulas que, en contra de la buena fe, causen un **desequilibrio importante** entre los derechos y obligaciones de las partes en perjuicio del consumidor.

### Tipos de cláusulas abusivas [verificar]

| Tipo | Base legal | Ejemplos |
|---|---|---|
| **Vinculación del contrato a la voluntad del proveedor** | Ley 45 de 2007 | Reserva de modificación unilateral, plazos excesivos, interpretación unilateral |
| **Limitación de derechos del consumidor** | Ley 45 de 2007 | Exclusión de responsabilidad, limitación de acciones legales, renuncia a derechos |
| **Falta de reciprocidad** | Ley 45 de 2007 | Penalizaciones solo al consumidor, garantías desproporcionadas |
| **Garantías desproporcionadas** | Ley 45 de 2007 | Fianzas excesivas, redondeos al alza |
| **Contrarias al régimen de protección al consumidor** | Ley 45 de 2007 | Renuncia de derechos irrenunciables, foro no del consumidor |

### Cláusulas habitualmente abusivas [verificar]

- Modificación unilateral del precio o de las condiciones sin causa justificada y sin derecho de resolución
- Penalizaciones o intereses moratorios desproporcionados
- Exclusión o limitación de la responsabilidad del proveedor por daños al consumidor
- Renuncia al derecho de retracto cuando es irrenunciable [verificar]
- Sumisión a un foro distinto del domicilio del consumidor [verificar]

---

## Control de transparencia material

Además del control de inclusión y contenido, conviene exigir **transparencia material** para las cláusulas que definen el objeto principal del contrato:

- El consumidor debe comprender las **consecuencias económicas** de la cláusula
- No basta con que sea legible — debe ser comprensible en su alcance real
- Aplica especialmente a: cláusulas de precio, intereses, comisiones, vencimiento anticipado

---

## Proceso de revisión

Para cada cláusula de las CGC:

1. **Identificar** — ¿Es una condición general (predispuesta, impuesta, generalidad)?
2. **Control de inclusión** — ¿Es transparente, accesible, aceptada expresamente?
3. **Control de contenido** — ¿Crea desequilibrio en perjuicio del consumidor?
4. **Transparencia material** — Si define el objeto principal, ¿es comprensible?
5. **Clasificar** — Conforme / Riesgo medio / Riesgo alto / Nula

---

## Formato de salida

```markdown
# Revisión de condiciones generales: [Empresa / Producto]

**Fecha:** [fecha]
**Tipo de contrato:** [compraventa / suscripción / servicio / etc.]
**Canal:** [online / presencial / mixto]

---

## Resumen

**Cláusulas revisadas:** [N]
**Conformes:** [N] | **Riesgo medio:** [N] | **Riesgo alto:** [N] | **Nulas:** [N]

---

## Hallazgos

| # | Cláusula (resumen) | Control fallido | Riesgo | Base legal | Recomendación |
|---|---|---|---|---|---|
| 1 | [Ej., Modificación unilateral del precio] | Contenido | Nula | Ley 45 de 2007 | Eliminar o condicionar a derecho de resolución |
| 2 | [Ej., Fuero distinto al del consumidor] | Contenido | Nula | Ley 45 de 2007 | Sustituir por el foro del domicilio del consumidor |
| 3 | [Ej., Letra ilegible en scroll] | Inclusión | Alto | Ley 45 de 2007 | Reformatear con tamaño legible |
| ... | ... | ... | ... | ... | ... |

---

## Cláusulas con riesgo de nulidad

[Lista detallada con texto exacto, fundamento y propuesta de corrección]

---

## Recomendaciones generales

[Observaciones transversales: estructura, legibilidad, coherencia interna]
```

---

## Legislación de referencia

- Ley 45 de 2007 — protección al consumidor y defensa de la competencia (contratos de adhesión y cláusulas abusivas) [verificar]
- ACODECO — Autoridad de Protección al Consumidor y Defensa de la Competencia
- Código de Comercio de Panamá — régimen de los contratos mercantiles
- Resoluciones de la ACODECO y jurisprudencia de la Corte Suprema de Justicia sobre cláusulas abusivas [verificar]

---

## Lo que este skill NO hace

- No redacta condiciones generales desde cero — revisa las existentes.
- No sustituye el control judicial de abusividad — identifica riesgos para que el abogado decida.
- No analiza condiciones negociadas individualmente — solo CGC predispuestas.
