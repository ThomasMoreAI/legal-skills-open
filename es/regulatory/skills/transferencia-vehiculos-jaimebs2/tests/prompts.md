# Tests manuales — transferencia-vehiculos

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 — Comprar coche usado a particular

**Prompt**: "Quiero comprar un coche de segunda mano a un particular. ¿Qué pasos tengo que seguir?"

**Criterios de aceptación**:
- Lista los pasos en orden: comprobaciones previas, contrato, ITP, transferencia DGT.
- Menciona el informe de vehículo DGT para verificar cargas y embargos.
- Indica que hay que pagar el ITP (Modelo 620, ~4 %) antes de la transferencia.
- Lista la documentación necesaria para la DGT.
- Menciona la tasa DGT de transferencia (55,70 €).

---

## Test 2 — ITP del vehículo

**Prompt**: "He comprado un coche por 5.000 € pero las tablas de Hacienda dicen que vale 7.000 €. ¿Cuánto ITP pago?"

**Criterios de aceptación**:
- Explica que se tributa sobre el mayor de los dos valores (7.000 € en este caso).
- Aplica el tipo general del 4 % = 280 €.
- Indica que el plazo es de 30 días hábiles con el Modelo 620.
- Puede mencionar que el tipo varía por comunidad autónoma.
- Remite a fiscalidad-itp-ajd para más detalle.

---

## Test 3 — Notificación de venta

**Prompt**: "He vendido mi coche hace una semana. ¿Tengo que hacer algo más?"

**Criterios de aceptación**:
- Recomienda hacer la notificación de venta en la DGT.
- Explica que protege de multas y responsabilidad por accidentes posteriores.
- Indica cómo hacerla (Sede Electrónica con Cl@ve/certificado o presencialmente).
- Proporciona la URL de la DGT.

---

## Test 4 — Importar coche de la UE

**Prompt**: "Quiero traerme un coche de Alemania. ¿Qué trámites necesito?"

**Criterios de aceptación**:
- Menciona: Impuesto de Matriculación (según CO₂), IVA (según vendedor), homologación (COC), ITV previa a matriculación, matriculación DGT.
- Distingue entre compra a profesional y a particular para el IVA.
- No confunde con importación extra-UE (no menciona aranceles aduaneros).
