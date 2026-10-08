# Tests manuales — extranjeria-reagrupacion

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Reagrupar cónyuge

**Prompt**: "Tengo residencia renovada en España y quiero traer a mi mujer desde Ecuador. ¿Qué necesito?"

**Criterios de aceptación**:
- Confirma que puede reagrupar al cónyuge con residencia renovada.
- Explica los requisitos: medios económicos (IPREM), informe de adecuación de vivienda.
- Describe el procedimiento: solicitud en Oficina de Extranjería, visado en consulado.
- Menciona los plazos orientativos.
- Indica que el cónyuge reagrupado tendrá autorización de trabajo.

---

## Test 2 — Reagrupar ascendientes

**Prompt**: "Quiero traer a mi madre de 70 años a España. Tengo residencia temporal renovada."

**Criterios de aceptación**:
- Indica que los ascendientes solo se pueden reagrupar con residencia de larga duración.
- Explica que debe ser mayor de 65 años (salvo excepciones humanitarias).
- Menciona que debe depender económicamente del reagrupante.
- Si tiene residencia temporal, indica que no puede reagrupar ascendientes todavía.

---

## Test 3 — Informe de vivienda

**Prompt**: "¿Qué es el informe de adecuación de vivienda para la reagrupación familiar?"

**Criterios de aceptación**:
- Explica que lo emite el Ayuntamiento.
- Describe qué valora (superficie, habitabilidad, número de habitaciones, servicios).
- Indica el plazo de emisión (30 días, silencio positivo).
- Menciona la documentación necesaria (contrato de alquiler o escritura, empadronamiento).

---

## Test 4 — Redireccionamiento a familiar UE

**Prompt**: "Mi marido es español y yo soy colombiana. ¿Necesito hacer reagrupación familiar?"

**Criterios de aceptación**:
- Indica que al ser cónyuge de ciudadano UE/español, se rige por el régimen comunitario, no por reagrupación familiar.
- Redirige a la skill extranjeria-familiar-ue.
- No intenta aplicar el procedimiento de reagrupación del régimen general.
