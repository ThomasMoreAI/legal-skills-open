# Tests manuales -- fiscalidad-itp-ajd

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 -- Compra de vivienda de segunda mano

**Prompt**: "Voy a comprar un piso de segunda mano en Madrid por 250.000 EUR. Cuanto pago de impuestos?"

**Criterios de aceptacion**:
- Indica que tributa por TPO (Transmisiones Patrimoniales Onerosas).
- Menciona el tipo del 6 % en Madrid (orientativo).
- Calcula aproximadamente: 15.000 EUR de TPO.
- Menciona que la hipoteca tributa por AJD (paga el banco desde 2018).
- Indica el Modelo 600 y el plazo de 30 dias habiles.

---

## Test 2 -- Diferencia entre vivienda nueva y usada

**Prompt**: "Cual es la diferencia de impuestos entre comprar un piso nuevo y uno de segunda mano?"

**Criterios de aceptacion**:
- Explica la regla de incompatibilidad IVA/TPO.
- Vivienda nueva (de promotor): IVA 10 % + AJD.
- Vivienda segunda mano (de particular): TPO (6-10 % segun CCAA).
- Indica que los tipos de TPO varian por CCAA.

---

## Test 3 -- Transferencia de coche usado

**Prompt**: "Quiero comprar un coche de segunda mano a un particular. Que impuesto tengo que pagar?"

**Criterios de aceptacion**:
- Indica que tributa por TPO.
- Menciona el Modelo 620.
- Explica que la base imponible son las tablas de valoracion de Hacienda, no el precio pactado.
- Indica el tipo (4-8 % segun CCAA).
- Menciona que es necesario para la transferencia en la DGT.

---

## Test 4 -- Redireccion a IVA

**Prompt**: "Voy a comprar un local comercial a una empresa. Que impuestos pago?"

**Criterios de aceptacion**:
- Indica que al comprar a un empresario se aplica IVA (21 % para locales), no TPO.
- Menciona que ademas se aplica AJD.
- Puede redirigir a fiscalidad-iva para detalle sobre el IVA.
