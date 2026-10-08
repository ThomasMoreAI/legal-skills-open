# Tests manuales -- fiscalidad-no-residentes

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 -- No residente con piso en Espana

**Prompt**: "Soy britanico, tengo un apartamento en la Costa del Sol que no alquilo. Tengo que pagar impuestos en Espana?"

**Criterios de aceptacion**:
- Indica que si, debe presentar Modelo 210 por imputacion de rentas inmobiliarias.
- Explica que la base es el 1,1-2 % del valor catastral.
- Indica que el tipo para no UE (post-Brexit) es el 24 %.
- Menciona que el plazo es el ano natural siguiente.
- Recomienda asesor especializado en fiscalidad internacional.

---

## Test 2 -- Ley Beckham

**Prompt**: "Me traslado a Espana por trabajo. Me han dicho que puedo acogerme a la Ley Beckham. Como funciona?"

**Criterios de aceptacion**:
- Explica el regimen especial del art. 93 LIRPF.
- Indica el tipo fijo del 24 % hasta 600.000 EUR.
- Menciona que dura 6 anos (ano de traslado + 5 siguientes).
- Indica el requisito de no haber sido residente en los 5 anos anteriores.
- Menciona el Modelo 149 y el plazo de 6 meses.

---

## Test 3 -- Venta de inmueble por no residente

**Prompt**: "Soy no residente y voy a vender mi piso en Espana. Que impuestos tengo que pagar?"

**Criterios de aceptacion**:
- Indica el IRNR al 19 % sobre la ganancia patrimonial.
- Explica la retencion del 3 % que el comprador debe practicar.
- Menciona que puede solicitar devolucion del exceso con Modelo 210.
- Indica que tambien se devenga plusvalia municipal.
- Recomienda asesor fiscal.

---

## Test 4 -- Redireccion a IRPF asalariados

**Prompt**: "Llevo viviendo en Espana 3 anos, trabajo aqui y quiero saber cuanto IRPF pago."

**Criterios de aceptacion**:
- Identifica que con mas de 183 dias al ano es residente fiscal.
- Redirige a fiscalidad-irpf-asalariados (o fiscalidad-autonomos si es autonomo).
- No aplica normativa de no residentes.
