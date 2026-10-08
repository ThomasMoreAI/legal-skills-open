---
name: orden-de-cambio-raimondifernando-web
title: 'Skill: Orden de cambio / Adicional de obra'
description: 'Redactá un adicional u orden de cambio de obra con base contractual, delta de alcance, desglose de precios ítem por ítem e impacto en plazo. Usala cuando te pidan escribir un adicional, una orden de cambio, papelizar un trabajo extra, responder a una indicación verbal del comitente, o documentar una economía. Produce un documento completo con fundamento legal (Código Civil y Comercial), descripción del cambio, tabla de precios ítem a ítem y reserva de derechos sobre impactos diferidos. Disparadores: "adicional", "orden de cambio", "trabajo extra", "economía", "directiva del comitente", "fuera de contrato", "variación de alcance".'
author: raimondifernando-web
author_url: https://github.com/raimondifernando-web/claude-catalogo/tree/main/plugins/rubro-estudio-arquitectura/skills/orden-de-cambio
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: contracts
language: es
---

# Skill: Orden de cambio / Adicional de obra

Un adicional que dice "trabajo extra — $48.500" se negocia a la baja o se rechaza. Uno defensible responde
tres preguntas antes de que las hagan: *por qué tengo derecho* (qué artículo, qué hecho lo origina),
*qué cambió exactamente* (delta respecto del contrato original), y *cuánto cuesta de verdad*
(precios unitarios con análisis, más plazo). Esta skill genera ese documento.

## Qué produce

- Un **documento de orden de cambio/adicional** listo para membrete
- **Fundamento contractual**: artículo del Código Civil y Comercial o cláusula del contrato privado que habilita el adicional
- **Delta de alcance**: comparación entre lo contratado y la nueva situación, con referencia a planos y pliego
- **Desglose de precios**: mano de obra, materiales, equipos, subcontratistas, gastos generales y utilidad
- **Impacto en plazo** y **reserva de derechos** para impactos no cuantificados todavía

## Inputs que necesitás

Pedí lo que falte; con un brief mínimo, avanzá de todas formas y marcá los huecos con `[confirmar]`:

- **El hecho que origina el cambio**: instrucción escrita o verbal del director de obra, plano revisado, diferencia de condición de sitio, exigencia nueva del ente regulador, error u omisión del proyecto. Fecha.
- **Base contractual**: número de cláusula del contrato o artículo del CCyC aplicable; porcentajes de gastos generales, utilidad y IVA pactados (si no están en el contrato ni los aporta el usuario, dejá [GG: __ %, a confirmar con contrato] y [Utilidad: __ %, a confirmar]).
- **Alcance original**: qué decían los documentos del contrato antes del cambio (plano, pliego, cómputo).
- **Precios o datos de costos**: cuadrillas, horas, cantidades de material, cotizaciones de subcontratistas. Estimativos están bien; la skill los estructura.
- **Situación de plazo**: ¿la tarea afectada está en la ruta crítica? Fecha de entrega contractual vigente.

## Marco legal y comercial argentino

**Fundamento según tipo de hecho:**

| Hecho que origina el cambio | Base legal / contractual |
|---|---|
| Instrucción del comitente o director de obra que amplía el alcance | CCyC art. 1264 (variación acordada); cláusula de variaciones del contrato privado |
| Variación inevitable por causa justificada (ej. necesidad técnica sobreviniente) | CCyC art. 1265 (variación unilateral del contratista con autorización del comitente) — **verificar aplicación al caso** |
| Diferencia de condición de sitio respecto de lo documentado | Principio de equivalencia de prestaciones; buena fe contractual (CCyC art. 961). **Verificar cláusula específica en el contrato** |
| Error u omisión del proyecto | Responsabilidad del proyectista; derecho al precio justo por el trabajo ejecutado (CCyC art. 1270) — **verificar con abogado** |
| Redeterminación de precios (obra pública) | Decreto 691/2016 [verificar vigencia] y normativa provincial; índice CAC (Cámara Argentina de la Construcción) |
| Ajuste pactado (obra privada) | Cláusula de ajuste del contrato; en su defecto, negociación con base en variación CAC o INDEC |

> ⚠️ Los números de artículo del CCyC son orientativos. Antes de enviar el documento, verificá la cita exacta con el plexo normativo vigente y, ante conflicto, consultá a un abogado.

**Estructura de precios:**
**Nunca generes precios unitarios ni porcentajes de memoria. Si el usuario no los aporta, dejá la celda como [$ a completar — cotización / parte de trabajo / planilla del contratista] y el subtotal como [a calcular].**
Construí desde registros, no números redondos: mano de obra (cuadrilla × horas × jornal básico con cargas sociales), materiales (cantidades × precio de lista o cotización adjunta), equipos (alquiler o costo horario propio), subcontratistas (presupuesto firmado), luego aplicá el porcentaje de gastos generales y utilidad del contrato. **IVA: verificar tasa aplicable según tipo de obra y destino** (puede ser 10,5 % o 21 %; consignarlo explícitamente). Lo que sea estimado, marcarlo como `[estimado]`.

**Plazo:** declarar la extensión en días corridos pedida y si afecta la ruta crítica. Si no podés cuantificarlo todavía, reservá expresamente el derecho a reclamar la extensión.

**Libro de obra:** cualquier instrucción verbal que origine este adicional debería volcarse en el libro de obra ese mismo día. Si no está asentada, mencionarlo en la sección de antecedentes.

## Formato de salida

### Orden de cambio N.º [#]: [Título breve]

**Obra / N.º de contrato / Fecha / A / De**

**1. Antecedentes** — qué hecho originó el cambio, cuándo ocurrió y cómo fue comunicado (asiento en libro de obra, correo, plano revisado, etc.).

**2. Fundamento contractual** — cláusula del contrato y/o artículo del CCyC aplicable. Estado del aviso: dado en fecha [x], dado en esta presentación, o fuera de plazo (indicar si es el caso — no ocultarlo).

**3. Delta de alcance** — tabla "contrato original / situación con cambio" con referencia a planos y pliego.

**4. Desglose de precios**
| Ítem | Descripción | Unid. | Cant. | Precio unit. | Subtotal |
| MO | Mano de obra — [cuadrilla] × [hs] × [jornal] | gl | 1 | | |
| MT | Materiales — [ítem] | | | | |
| EQ | Equipos | | | | |
| SC | Subcontratistas | gl | 1 | | |
| **Subtotal directos** | | | | | |
| GG | Gastos generales (\_\_%) | | | | |
| UT | Utilidad (\_\_%) | | | | |
| IVA | IVA [tasa a verificar] % | | | | |
| **TOTAL** | | | | | |

Adjuntos: cotizaciones, partes de trabajo, análisis de precios unitarios.

**5. Impacto en plazo** — [X] días corridos pedidos / en ruta crítica: sí/no / o explícitamente reservado para análisis posterior.

**6. Reserva de derechos** — se reservan expresamente los derechos sobre impacto acumulado, aceleración y consecuencias no cuantificables en esta presentación.

**7. Bloque de firmas** y línea: *"Este documento es un borrador técnico, no asesoramiento legal. Antes de enviarlo al contratista o al comitente, revisarlo con el titular del estudio y, si hay conflicto, con un abogado."*

> **Regla de la casa:** mostrá este borrador y pedí confirmación antes de enviarlo o compartirlo con la otra parte.

## Qué NO hace esta skill

- No analiza si el adicional es procedente desde un punto de vista legal — eso requiere un abogado.
- No hace seguimiento de pagos ni de certificaciones de obra.
- No genera análisis de precios unitarios detallados (APU) — puede esquematizarlos; el detalle lo cargás vos.
- No valida si el plazo contractual ya venció.

## Checklist de calidad

- [ ] Hay una cláusula contractual o artículo del CCyC citado (con nota de verificar si no estás seguro del número)
- [ ] El aviso al comitente está declarado honestamente: dado a tiempo, dado en esta presentación, o tardío
- [ ] Cada línea de costo tiene respaldo o está marcada `[estimado]`
- [ ] GG, utilidad e IVA siguen lo pactado en el contrato, o se aclara que son de mercado
- [ ] El impacto en plazo está declarado afirmativamente o reservado — nunca en silencio
- [ ] La reserva de derechos y el aviso "no es asesoramiento legal" están presentes
