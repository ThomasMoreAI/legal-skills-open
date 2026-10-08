# Tests manuales --- vivienda-compraventa

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 --- Proceso de compra de un piso

**Prompt**: "Quiero comprar un piso de segunda mano en Madrid. ¿Cuáles son los pasos y cuánto me va a costar en impuestos y gastos?"

**Criterios de aceptación**:
- Describe el proceso: nota simple, arras, escritura, inscripción en Registro.
- Menciona ITP como impuesto principal en segunda mano (no IVA).
- Indica que el ITP varía por comunidad autónoma.
- Lista los gastos: notaría, registro, gestoría, tasación (si hipoteca).
- Menciona la necesidad de certificado energético y referencia catastral.
- Remite a **fiscalidad-itp-ajd** para detalle del ITP.

---

## Test 2 --- Tipos de arras

**Prompt**: "He encontrado un piso que me gusta y el vendedor me pide firmar arras. ¿Qué tipos hay y qué pasa si me echo atrás?"

**Criterios de aceptación**:
- Explica los tres tipos: penitenciales, confirmatorias y penales.
- Indica que las penitenciales son las más habituales.
- Explica la consecuencia: comprador pierde señal, vendedor devuelve el doble.
- Menciona el importe habitual (5-10 % del precio).
- Cita el art. 1454 del Código Civil para las penitenciales.

---

## Test 3 --- Gastos del vendedor

**Prompt**: "Voy a vender mi casa. ¿Qué impuestos tengo que pagar?"

**Criterios de aceptación**:
- Menciona la plusvalía municipal (IIVTNU) y remite a **fiscalidad-impuestos-locales**.
- Menciona la ganancia patrimonial en IRPF (19-27 %).
- Indica la exención por reinversión en vivienda habitual.
- Menciona la exención para mayores de 65 años.
- Si tiene hipoteca, menciona gastos de cancelación.

---

## Test 4 --- Routing a hipotecas

**Prompt**: "¿Qué tipo de hipoteca me conviene más, fija o variable?"

**Criterios de aceptación**:
- Indica que esa consulta corresponde a la skill **vivienda-hipotecas**.
- No intenta dar detalle sobre tipos de hipoteca.
