# Tests manuales — incapacidad

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Baja médica: cuánto se cobra

**Prompt**: "Estoy de baja por una gripe. ¿Cuánto voy a cobrar?"

**Criterios de aceptación**:
- Identifica la contingencia como común (enfermedad común).
- Explica los porcentajes: días 1-3 = 0 %, días 4-20 = 60 %, día 21+ = 75 % de la base reguladora.
- Menciona que muchos convenios colectivos mejoran estos porcentajes.
- Indica que la empresa paga los días 4-15 y luego la mutua/INSS.

---

## Test 2 — Incapacidad permanente: grados

**Prompt**: "Me han dicho que me pueden dar una incapacidad permanente. ¿Qué grados hay y cuánto se cobra?"

**Criterios de aceptación**:
- Lista los 4 grados: parcial, total, absoluta y gran invalidez.
- Indica la prestación de cada uno (24 mensualidades, 55 %, 100 %, 100 % + complemento).
- Menciona el procedimiento (INSS, EVI, dictamen).
- Menciona la posibilidad de revisión de grado.

---

## Test 3 — Duración máxima de la baja

**Prompt**: "¿Cuánto tiempo puedo estar de baja como máximo?"

**Criterios de aceptación**:
- Indica 365 días + prórroga de 180 días = 545 días.
- Menciona la posibilidad de demora en calificación hasta 730 días.
- Explica quién puede dar el alta (médico, INSS a los 365 días, inspección).

---

## Test 4 — Redireccionamiento a nóminas

**Prompt**: "¿Cómo se refleja la baja en mi nómina?"

**Criterios de aceptación**:
- Indica que para detalle de nóminas se debe usar la skill laboral-nominas.
- No intenta explicar en profundidad la estructura de la nómina durante la baja.
