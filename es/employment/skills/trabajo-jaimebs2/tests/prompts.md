# Tests manuales — extranjeria-trabajo

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Permiso de trabajo por cuenta ajena

**Prompt**: "Soy marroquí y tengo una oferta de trabajo de una empresa en Almería. ¿Qué necesito para poder trabajar legalmente?"

**Criterios de aceptación**:
- Explica que necesita una autorización de residencia temporal y trabajo por cuenta ajena.
- Indica que es el empleador quien presenta la solicitud.
- Menciona la Situación Nacional de Empleo o el CODC.
- Describe el procedimiento: solicitud, visado en consulado, entrada, alta en Seguridad Social, TIE.
- No confunde con permiso de residencia sin trabajo.

---

## Test 2 — CODC y Situación Nacional de Empleo

**Prompt**: "¿Qué es el Catálogo de Ocupaciones de Difícil Cobertura y cómo afecta a la contratación de extranjeros?"

**Criterios de aceptación**:
- Explica que es una lista trimestral del SEPE con ocupaciones difíciles de cubrir.
- Indica que si la ocupación está en el CODC, no se exige la prueba de la Situación Nacional de Empleo.
- Menciona que varía por provincia y trimestre.
- Da ejemplos de ocupaciones habituales en el catálogo.

---

## Test 3 — Tarjeta Azul UE

**Prompt**: "Soy ingeniero informático de India con máster. ¿Puedo solicitar la Tarjeta Azul UE en España?"

**Criterios de aceptación**:
- Explica qué es la Tarjeta Azul UE (profesionales altamente cualificados).
- Menciona los requisitos: titulación superior, contrato de al menos 1 año, salario mínimo (1,5 veces el salario medio).
- Indica las ventajas (movilidad intraeuropea, reagrupación simplificada).
- Señala que no se exige la Situación Nacional de Empleo.

---

## Test 4 — De estudiante a trabajo

**Prompt**: "Llevo 2 años estudiando un máster en España y he encontrado trabajo. ¿Puedo cambiar mi permiso de estudiante a permiso de trabajo?"

**Criterios de aceptación**:
- Explica la modificación de situación de estancia por estudios a residencia y trabajo.
- Menciona que se puede hacer al finalizar estudios o tras 3 años.
- Indica la autorización de búsqueda de empleo tras estudios (12 meses).
- No redirige a otra skill innecesariamente.
