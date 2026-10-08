# Tests manuales — extranjeria-familiar-ue

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Cónyuge de español

**Prompt**: "Soy colombiana y me acabo de casar con un español. ¿Qué trámites necesito para vivir y trabajar en España?"

**Criterios de aceptación**:
- Identifica que se rige por el régimen comunitario (no por reagrupación familiar del régimen general).
- Explica que debe solicitar la tarjeta de familiar de ciudadano de la Unión.
- Indica que tiene derecho a trabajar sin permiso de trabajo independiente.
- Describe el procedimiento y la documentación necesaria.
- Menciona que puede solicitar la tarjeta incluso estando en España.

---

## Test 2 — Diferencia régimen comunitario vs general

**Prompt**: "¿Cuál es la diferencia entre el régimen comunitario y el régimen general de extranjería?"

**Criterios de aceptación**:
- Explica claramente ambos regímenes.
- Indica a quién aplica cada uno.
- Menciona las diferencias principales: permiso de trabajo, documentos, renovación, procedimiento.
- Indica que el régimen comunitario es más favorable.

---

## Test 3 — Residencia permanente

**Prompt**: "Llevo 5 años en España con tarjeta de familiar comunitario. ¿Puedo pedir la residencia permanente?"

**Criterios de aceptación**:
- Confirma que tras 5 años de residencia legal continuada puede solicitar la residencia permanente.
- Explica que la tarjeta se renueva cada 10 años pero el derecho es permanente.
- Menciona que se mantiene incluso tras divorcio (con condiciones).
- Indica que pierde el derecho con ausencias superiores a 2 años consecutivos.

---

## Test 4 — Redireccionamiento a reagrupación

**Prompt**: "Tengo residencia en España y quiero traer a mis padres desde Marruecos. Mi mujer y yo somos marroquíes."

**Criterios de aceptación**:
- Identifica que se trata de reagrupación familiar del régimen general (no comunitario).
- Redirige a la skill extranjeria-reagrupacion.
- No aplica el régimen comunitario.
