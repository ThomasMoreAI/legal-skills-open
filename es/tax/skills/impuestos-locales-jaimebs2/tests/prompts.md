# Tests manuales -- fiscalidad-impuestos-locales

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 -- IBI basico

**Prompt**: "Cuanto se paga de IBI por un piso? Como se calcula?"

**Criterios de aceptacion**:
- Explica que el IBI se calcula multiplicando el valor catastral por el tipo impositivo del ayuntamiento.
- Indica la horquilla de tipos (0,4-1,10 % para urbano).
- Menciona que el valor catastral lo fija el Catastro.
- Indica que lo paga el propietario a 1 de enero.

---

## Test 2 -- Plusvalia municipal al vender

**Prompt**: "Voy a vender mi piso. Tengo que pagar plusvalia municipal? Como se calcula?"

**Criterios de aceptacion**:
- Explica los dos metodos de calculo (objetivo por coeficientes y real por plusvalia efectiva).
- Indica que se puede elegir el mas favorable.
- Menciona que si no hay incremento real no se paga (sentencia TC 2021).
- Indica que el tipo maximo es del 30 %.
- Identifica al vendedor como sujeto pasivo en transmisiones onerosas.

---

## Test 3 -- Impuesto de circulacion con coche electrico

**Prompt**: "Tengo un coche electrico. Cuanto pago de impuesto de circulacion? Hay alguna bonificacion?"

**Criterios de aceptacion**:
- Indica que el IVTM es un impuesto municipal anual.
- Menciona la bonificacion de hasta el 75 % para vehiculos electricos.
- Aclara que la bonificacion depende del ayuntamiento concreto.
- Indica que lo paga el titular a 1 de enero.

---

## Test 4 -- Redireccion a ITP

**Prompt**: "Cuanto impuesto pago por comprar un piso de segunda mano?"

**Criterios de aceptacion**:
- Aclara que la compraventa de segunda mano tributa principalmente por ITP (no es un impuesto local).
- Redirige a fiscalidad-itp-ajd.
- Puede mencionar que ademas habra que pagar plusvalia municipal (la paga el vendedor).
