# Tests manuales — alta-autonomo

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Nuevo autónomo desde cero

**Prompt**: "Quiero hacerme autónomo como programador freelance. ¿Por dónde empiezo?"

**Criterios de aceptación**:
- Explica el proceso paso a paso en orden cronológico.
- Menciona obtener identificación digital primero (Cl@ve o certificado).
- Indica alta en Hacienda (Modelo 036/037) y elección de epígrafe IAE.
- Indica alta en Seguridad Social (RETA vía Import@ss).
- Menciona la tarifa plana como opción para nuevos autónomos.
- No entra en detalle profundo sobre obligaciones fiscales continuas (remite a fiscalidad-autonomos).

---

## Test 2 — Tarifa plana y coste

**Prompt**: "¿Cuánto me va a costar ser autónomo el primer año? ¿Existe algún descuento en la cuota?"

**Criterios de aceptación**:
- Explica la tarifa plana (80 €/mes los primeros 12 meses).
- Indica los requisitos (no haber sido autónomo en los 2 años anteriores, alta en plazo).
- Da una estimación orientativa del coste del primer año.
- Menciona el coste de gestoría como opcional.

---

## Test 3 — Capitalización del desempleo

**Prompt**: "Estoy en paro y quiero hacerme autónomo. ¿Puedo usar mi prestación para eso?"

**Criterios de aceptación**:
- Explica la capitalización del desempleo (pago único).
- Indica las modalidades (pago único, abono de cuotas, combinación).
- Menciona que debe solicitarse ANTES de darse de alta como autónomo.
- Remite al SEPE como organismo competente.

---

## Test 4 — Distinción con fiscalidad-autonomos

**Prompt**: "Ya soy autónomo. ¿Qué impuestos tengo que pagar cada trimestre?"

**Criterios de aceptación**:
- Reconoce que la pregunta es sobre obligaciones fiscales continuas, no sobre el alta.
- Redirige a la skill fiscalidad-autonomos.
- No intenta responder con detalle sobre modelos trimestrales.
