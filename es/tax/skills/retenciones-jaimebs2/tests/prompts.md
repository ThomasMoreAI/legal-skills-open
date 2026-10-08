# Tests manuales -- fiscalidad-retenciones

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 -- Retencion a profesional

**Prompt**: "Tengo que pagar a un disenador autonomo por un trabajo. Que retencion le aplico en la factura?"

**Criterios de aceptacion**:
- Indica que la retencion a profesionales es del 15 %.
- Menciona que si es profesional nuevo (primeros 3 anos) puede ser del 7 %.
- Explica que debe declarar la retencion en el Modelo 111 trimestralmente.
- Indica que al final del ano debe presentar el Modelo 190.

---

## Test 2 -- Retencion sobre alquiler de local

**Prompt**: "Alquilo una oficina para mi negocio. Tengo que retener algo al propietario?"

**Criterios de aceptacion**:
- Indica que si, debe retener el 19 % del alquiler.
- Menciona el Modelo 115 trimestral.
- Indica el Modelo 180 como resumen anual.
- Aclara que no se retiene en alquileres de vivienda habitual.

---

## Test 3 -- Cuanto me retienen en la nomina

**Prompt**: "Gano 30.000 EUR brutos al ano, soy soltero y sin hijos. Cuanto me retienen de IRPF en la nomina?"

**Criterios de aceptacion**:
- Indica un porcentaje orientativo (14-17 % aproximadamente).
- Explica que depende de la situacion personal y familiar.
- Menciona el simulador de la AEAT para calculo preciso.
- Aclara que la retencion es un anticipo del IRPF, que se regulariza en la Renta.

---

## Test 4 -- Redireccion a autonomos

**Prompt**: "Soy autonomo y en mis facturas me retienen el 15 %. Como me lo deduzco luego?"

**Criterios de aceptacion**:
- Identifica que la pregunta es desde la perspectiva del perceptor (autonomo).
- Redirige a fiscalidad-irpf-autonomos (pagos fraccionados y Renta).
- Puede mencionar que las retenciones se deducen en el Modelo 130 y en la Renta (Modelo 100).
