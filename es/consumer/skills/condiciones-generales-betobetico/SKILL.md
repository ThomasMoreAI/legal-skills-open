---
name: condiciones-generales-betobetico
title: /condiciones-generales
description: Revisor de condiciones generales de la contratación — analiza unas CGC para contratos con consumidores, aplica el control de inclusión (LCGC art. 5), el control de contenido (LGDCU arts. 82-91) y marca cláusulas con riesgo de nulidad por abusivas. Usar cuando el usuario diga "revisa estas condiciones", "son abusivas estas cláusulas", "T&C", "condiciones generales" o adjunte unas condiciones de contratación.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/consumo/skills/condiciones-generales
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: consumer
language: es
---

# /condiciones-generales

1. Cargar `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md` → sector, tipo de contrato, canal de venta.
2. Obtener las condiciones generales.
3. Aplicar control de inclusión (LCGC art. 5).
4. Aplicar control de contenido (LGDCU arts. 82-91).
5. Generar lista de cláusulas con riesgo de nulidad.

```
/consumo:condiciones-generales
[pegar las condiciones generales del e-commerce]
```

---

## Propósito

Las condiciones generales de la contratación (CGC) con consumidores están sujetas a un doble control en derecho español: el control de inclusión (que la cláusula se haya incorporado válidamente al contrato) y el control de contenido (que no sea abusiva). Una cláusula que no supera cualquiera de los dos controles es nula de pleno derecho. Este skill revisa ambos controles y marca las cláusulas problemáticas.

---

## Control de inclusión (LCGC art. 5)

Las CGC solo forman parte del contrato si:

| Requisito | Art. LCGC | Verificar |
|---|---|---|
| **Transparencia formal** | Art. 5.1 | Redacción clara, concreta y sencilla |
| **Accesibilidad** | Art. 5.1 | El adherente pudo conocerlas antes de contratar |
| **Aceptación expresa** | Art. 5.1 | Referencia expresa a las CGC; firmadas o aceptadas |
| **Legibilidad** | Art. 5 | Tamaño de letra, formato, estructura comprensible |
| **Contratación electrónica** | Art. 5.4 | Disponibles para almacenar y reproducir (LSSI art. 27) |

**Consecuencia del incumplimiento:** La cláusula no se incorpora al contrato (art. 7 LCGC). El contrato subsiste sin ella si es viable.

---

## Control de contenido — Cláusulas abusivas (LGDCU arts. 82-91)

### Cláusula general de abusividad (art. 82 LGDCU)

Son abusivas las cláusulas que, en contra de la buena fe, causen un **desequilibrio importante** entre los derechos y obligaciones de las partes en perjuicio del consumidor.

### Listas de cláusulas abusivas

| Tipo | Art. LGDCU | Ejemplos |
|---|---|---|
| **Vinculación del contrato a la voluntad del empresario** | Art. 85 | Reserva de modificación unilateral, plazos excesivos, interpretación unilateral |
| **Limitación de derechos del consumidor** | Art. 86 | Exclusión de responsabilidad, limitación de acciones legales, renuncia a derechos |
| **Falta de reciprocidad** | Art. 87 | Penalizaciones solo al consumidor, garantías desproporcionadas |
| **Garantías desproporcionadas** | Art. 88 | Fianzas excesivas, redondeos al alza |
| **Contrarias a normas de competencia y derecho aplicable** | Art. 90 | Sumisión a arbitraje no LGDCU, foro no del consumidor |

### Cláusulas negras (siempre abusivas)

Según la jurisprudencia del TJUE y del TS:
- Cláusula suelo sin transparencia material (STS 9 mayo 2013)
- Vencimiento anticipado desproporcionado
- Intereses moratorios desproporcionados
- Sumisión a fuero distinto del domicilio del consumidor (art. 90.2 LGDCU)
- Renuncia al derecho de desistimiento cuando es irrenunciable

---

## Control de transparencia material (jurisprudencia TJUE y TS)

Además del control de inclusión y contenido, la jurisprudencia exige **transparencia material** para las cláusulas que definen el objeto principal del contrato:

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
| 1 | [Ej., Modificación unilateral del precio] | Contenido | Nula | Art. 85.3 LGDCU | Eliminar o condicionar a derecho de resolución |
| 2 | [Ej., Fuero de Madrid] | Contenido | Nula | Art. 90.2 LGDCU | Sustituir por fuero del consumidor |
| 3 | [Ej., Letra ilegible en scroll] | Inclusión | Alto | Art. 5 LCGC | Reformatear con tamaño legible |
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

- LCGC (Ley 7/1998) — Ley sobre Condiciones Generales de la Contratación
- LGDCU (RDL 1/2007) — arts. 80-91 (cláusulas abusivas)
- LSSI-CE (Ley 34/2002) — art. 27 (contratación electrónica)
- Directiva 93/13/CEE — cláusulas abusivas en contratos con consumidores
- Jurisprudencia TJUE — Asuntos Banco Español de Crédito (C-618/10), Aziz (C-415/11), Kásler (C-26/13)
- STS 9 mayo 2013 (cláusula suelo — transparencia material)

---

## Lo que este skill NO hace

- No redacta condiciones generales desde cero — revisa las existentes.
- No sustituye el control judicial de abusividad — identifica riesgos para que el letrado decida.
- No analiza condiciones negociadas individualmente — solo CGC predispuestas.
