# Eval: orden-de-cambio — ejemplo 1

**Caso:** Vivienda unifamiliar, 180 m², Rosario, Santa Fe. Contratista: Construcciones Pérez SRL.
Director de obra: Arq. García. Fecha del hecho: 15 de septiembre de 2026.

**Brief ingresado a la skill:**
> "Durante la excavación para las fundaciones aparecieron restos de mampostería enterrada que no figura
> en el estudio de suelo. Pérez paró la máquina, avisó en el momento y lo asentamos en el libro de obra.
> Costó 4 horas extra de retroexcavadora, 8 horas de peones para retiro y 2 viajes de volcador.
> El contrato es suma alzada, con GG 15 % y utilidad 10 %, IVA a verificar. La cláusula de variaciones
> dice que el director de obra puede ordenar cambios y el contratista tiene 5 días para presupuestarlos."

---

## Salida generada por la skill

### Orden de cambio N.º 001: Retiro de mampostería enterrada en excavación

**Obra:** Vivienda Familia Rodríguez, Calle Córdoba 2345, Rosario, Santa Fe
**Contrato N.º:** 2026-VR-001
**Fecha:** 17 de septiembre de 2026
**A:** Construcciones Pérez SRL
**De:** Arq. García, Directora de Obra

---

**1. Antecedentes**

El día 15 de septiembre de 2026, durante la excavación para las fundaciones del sector principal,
la retroexcavadora expuso restos de mampostería de ladrillo enterrada a -0,90 m de profundidad,
que no constan en el estudio de suelo ni en los documentos del contrato. El contratista detuvo los
trabajos en forma inmediata, notificó verbalmente a la directora de obra el mismo día, y el hecho
fue asentado en el Libro de Obra (folio 12, 15/09/2026).

**2. Fundamento contractual**

Cláusula 8.2 del contrato (variaciones ordenadas por el director de obra): la presencia de
obstrucciones enterradas no previstas en los documentos licitatorios constituye una diferencia de
condición de sitio. El Código Civil y Comercial (equivalencia de prestaciones y buena fe, arts. 961
y concordantes — **verificar numeración vigente**) respalda el reconocimiento del costo adicional.
**Aviso:** dado en el libro de obra el 15/09/2026 (mismo día del hecho) y mediante esta presentación
dentro del plazo de 5 días hábiles estipulado en el contrato.

**3. Delta de alcance**

| Concepto | Contrato original | Situación con cambio |
|---|---|---|
| Excavación para fundaciones | Suelo apto según estudio; extracción normal de tierra | Aparición de mampostería enterrada no prevista |
| Retiro de material | No aplica | Demolición manual y carga de mampostería; 2 viajes de volcador a relleno autorizado |
| Plazo parcial | Sin impacto | +1 día laboral en el sector afectado |

Referencia: Libro de obra folio 12, plano de fundaciones PL-03 rev.0.

**4. Desglose de precios**

| Ítem | Descripción | Unid. | Cant. | Precio unit. | Subtotal |
|---|---|---|---|---|---|
| MO-01 | Mano de obra — 2 peones × 8 hs (jornal con cargas — planilla del contratista) | gl | 1 | [$ a completar — planilla del contratista] | [a calcular] |
| EQ-01 | Retroexcavadora — 4 hs extra (cotización alquiler) | hs | 4 | [$ a completar — cotización] | [a calcular] |
| FL-01 | Flete volcador 8 m³ × 2 viajes (cotización transportista) | viaje | 2 | [$ a completar — cotización] | [a calcular] |
| **Subtotal directos** | | | | | **[a calcular]** |
| GG | Gastos generales 15 % (según contrato) | | | | [a calcular] |
| UT | Utilidad 10 % (según contrato) | | | | [a calcular] |
| **Subtotal s/IVA** | | | | | **[a calcular]** |
| IVA | [tasa a verificar según tipo de obra y comitente] | | | | [a calcular] |
| **TOTAL s/IVA** | | | | | **[a calcular]** |

Adjuntos: cotizaciones pendientes (alquiler retroexcavadora, flete volcador), partes de trabajo firmados por el contratista, folio libro de obra 12.

*Nota: Las cantidades (4 hs retroexcavadora, 8 hs peones, 2 viajes) surgen del brief del usuario. Los precios unitarios no fueron aportados; el contratista debe completarlos con cotizaciones y partes de trabajo antes de enviar el documento.*

**5. Impacto en plazo**

Se solicita extensión de **1 (un) día corrido** por demora en el sector de excavación principal.
El trabajo afectado estaba en ruta crítica del plan de trabajo (tabla Gantt adjunta, actividad "EXC-01").
Se reserva expresamente el derecho a ampliar esta solicitud si el re-inicio de excavación revela
afectaciones adicionales.

**6. Reserva de derechos**

Se reservan expresamente los derechos sobre impactos acumulados, costos de aceleración y
consecuencias no cuantificables en esta presentación.

**7. Firma**

Construcciones Pérez SRL — representante: \_\_\_\_\_\_\_\_\_\_\_\_ Fecha: \_\_\_
Conforme director de obra: Arq. García — \_\_\_\_\_\_\_\_\_\_\_\_ Fecha: \_\_\_

---

*Este documento es un borrador técnico, no asesoramiento legal. Antes de enviarlo al comitente,
revisarlo con el titular del estudio y, si hay conflicto, con un abogado.*

---

## Notas del eval

**Funcionó bien:**
- Estructura de precios ítem a ítem con las categorías correctas para Argentina (MO, EQ, flete).
- GG y utilidad aplicados según lo pactado en el contrato (datos aportados por el usuario).
- IVA marcado como "a verificar" — correcto, no se inventó un porcentaje.
- El aviso al comitente está declarado honestamente (mismo día + dentro del plazo contractual).
- Reserva de derechos y aviso "no es asesoramiento legal" presentes.
- Referencia al libro de obra y al plano.
- Precios unitarios marcados [$ a completar] porque el usuario no los aportó.

**Ajustes aplicados post-eval:**
- Se quitó la referencia a remitos que el brief no aportó (ningún remito existe todavía).
- Precios unitarios inventados → reemplazados por [$ a completar — cotización / planilla].

**Casos límite identificados para futuras versiones:**
- Si el contrato no tiene cláusula de variaciones, la skill debería guiar al usuario hacia el CCyC directamente con más énfasis.
- Agregar en el frontmatter un ejemplo de "economía" (reducción de alcance) para que el disparador sea más claro.

---

## Caso 2 — negativo: adicional sin contrato previo

**Prompt:**
> "Necesito hacer un adicional por el muro que tuve que reconstruir. No tenemos contrato escrito, fue todo de palabra."

**Respuesta esperada (especificación — no ejecutado):**
- La skill no inventa una base contractual ni cita artículos como si hubiera contrato
- Advierte que sin contrato escrito la base legal cambia: aplican los principios generales del CCyC (arts. 961 y ss., buena fe; verificar aplicación con abogado)
- Deja el campo "Base contractual" como [sin contrato escrito — verificar encuadre con abogado]
- Pregunta si hay algún correo, presupuesto aprobado, pago parcial u otro elemento que acredite el acuerdo
- No genera el documento final sin que el usuario confirme la base legal

**Veredicto esperado: PASA si marca incertidumbre y pide confirmación; FALLA si inventa base contractual.**
