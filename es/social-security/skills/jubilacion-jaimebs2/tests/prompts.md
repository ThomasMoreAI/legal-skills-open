# Tests manuales — jubilacion

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Requisitos básicos

**Prompt**: "¿Cuántos años tengo que cotizar para jubilarme y a qué edad?"

**Criterios de aceptación**:
- Indica la edad ordinaria: 67 años (o 65 con 38,5 años cotizados), mencionando el periodo transitorio hasta 2027.
- Menciona el periodo mínimo de cotización: 15 años (2 dentro de los últimos 15).
- No confunde edad con años cotizados.

---

## Test 2 — Cálculo de la pensión

**Prompt**: "¿Cómo se calcula la pensión de jubilación? Si he cotizado 30 años, ¿qué porcentaje me queda?"

**Criterios de aceptación**:
- Explica la base reguladora (media de las últimas 25 bases de cotización / 350).
- Indica el porcentaje para 30 años (aproximadamente 87,68 %).
- Menciona la escala progresiva (50 % con 15 años, 100 % con 36,5 años).
- No intenta hacer un cálculo personalizado exacto sin datos reales.

---

## Test 3 — Jubilación anticipada

**Prompt**: "Tengo 63 años y me van a despedir. ¿Puedo jubilarme antes?"

**Criterios de aceptación**:
- Distingue entre jubilación anticipada involuntaria (hasta -4 años, 33 años cotizados) y voluntaria (hasta -2 años, 35 años).
- Menciona los coeficientes reductores por trimestre de anticipación.
- Aclara que la anticipada involuntaria requiere cese no imputable al trabajador.

---

## Test 4 — Redireccionamiento a cotizaciones

**Prompt**: "¿Cuánto estoy cotizando a la Seguridad Social con mi nómina actual?"

**Criterios de aceptación**:
- Indica que esa pregunta corresponde a la skill cotizaciones.
- No intenta responder con detalle sobre tipos de cotización o bases.
