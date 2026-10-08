# Tests manuales --- vivienda-hipotecas

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 --- Fija vs. variable

**Prompt**: "Estoy buscando hipoteca para mi primera vivienda. ¿Me conviene más tipo fijo o variable?"

**Criterios de aceptación**:
- Explica las características de ambos tipos (y menciona la mixta).
- Indica que la fija da seguridad pero suele tener un tipo inicial más alto.
- Indica que la variable depende del Euribor y la cuota puede subir o bajar.
- Recomienda comparar la TAE (no solo el TIN).
- Menciona los documentos precontractuales (FEIN/FiAE).

---

## Test 2 --- Gastos de constitución

**Prompt**: "¿Qué gastos tiene firmar una hipoteca? ¿Los pago yo o el banco?"

**Criterios de aceptación**:
- Indica que desde la Ley 5/2019 el banco paga notaría, registro, gestoría y AJD de la hipoteca.
- El cliente paga la tasación y su copia de la escritura.
- Distingue entre gastos de la hipoteca y gastos de la compraventa.
- Menciona el coste orientativo de la tasación (250-500 EUR).

---

## Test 3 --- Amortización anticipada

**Prompt**: "Tengo ahorros y quiero adelantar parte de la hipoteca. ¿Cuánto me cobra el banco?"

**Criterios de aceptación**:
- Explica las dos opciones: reducir cuota o reducir plazo.
- Indica las comisiones máximas según la Ley 5/2019 (variable: 0,25 %/0,15 %; fija: 2 %/1,5 %).
- Aclara que a partir de cierto plazo no hay comisión en variable.
- Recomienda reducir plazo si se quiere ahorrar más intereses.

---

## Test 4 --- Routing al Euribor

**Prompt**: "¿Cuál es el Euribor de este mes?"

**Criterios de aceptación**:
- Indica que el dato actual del Euribor corresponde a la skill **bde**.
- Puede explicar brevemente qué es el Euribor y cómo afecta a la hipoteca.
- No inventa un valor del Euribor.
