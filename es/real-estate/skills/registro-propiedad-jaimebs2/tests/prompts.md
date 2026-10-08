# Tests manuales --- vivienda-registro-propiedad

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 --- Nota simple

**Prompt**: "Quiero comprar un piso y me dicen que pida una nota simple. ¿Qué es, qué contiene y cómo la pido?"

**Criterios de aceptación**:
- Explica que es un extracto del Registro con la situación jurídica de la finca.
- Detalla el contenido: titularidad, descripción, cargas.
- Indica cómo pedirla online (sede.registradores.org, ~9 EUR + IVA) y presencial.
- Recomienda pedirla actualizada (menos de 15 días).
- Menciona que cualquier persona con interés legítimo puede solicitarla.

---

## Test 2 --- Principios registrales

**Prompt**: "¿Qué es la fe pública registral y cómo me protege si compro una vivienda?"

**Criterios de aceptación**:
- Explica el principio de fe pública registral (art. 34 LH).
- Indica que protege al comprador de buena fe que confía en el Registro.
- Menciona los requisitos: buena fe, título oneroso, inscripción.
- Puede mencionar otros principios relacionados (prioridad, tracto sucesivo).

---

## Test 3 --- Catastro vs. Registro

**Prompt**: "¿Cuál es la diferencia entre el Catastro y el Registro de la Propiedad?"

**Criterios de aceptación**:
- Indica que el Catastro es fiscal (Hacienda) y el Registro es jurídico (Justicia).
- Explica que la inscripción en el Catastro es obligatoria pero en el Registro es voluntaria.
- Menciona que el Catastro no prueba propiedad, el Registro sí (con fe pública).
- Señala las discrepancias habituales de superficie.
- Remite a la skill **catastro** para datos catastrales.

---

## Test 4 --- Routing a compraventa

**Prompt**: "Quiero comprar un piso, ¿cuáles son los pasos?"

**Criterios de aceptación**:
- Indica que el proceso completo de compraventa corresponde a la skill **vivienda-compraventa**.
- Puede mencionar brevemente la importancia de la nota simple y la inscripción.
