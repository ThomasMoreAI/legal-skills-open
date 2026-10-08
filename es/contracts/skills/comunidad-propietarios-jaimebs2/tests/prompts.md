# Tests manuales --- vivienda-comunidad-propietarios

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 --- Vecino moroso

**Prompt**: "Un vecino de mi comunidad no paga las cuotas desde hace un año. ¿Qué podemos hacer?"

**Criterios de aceptación**:
- Menciona el requerimiento extrajudicial como primer paso.
- Explica el procedimiento monitorio del art. 21 LPH.
- Indica que el moroso no puede votar ni impugnar acuerdos.
- Menciona la afección real (el piso responde de la anualidad en curso y las 3 anteriores).
- Indica que se puede embargar el inmueble si no paga.

---

## Test 2 --- Instalación de ascensor

**Prompt**: "En mi edificio no hay ascensor y hay un vecino con discapacidad. ¿La comunidad está obligada a ponerlo?"

**Criterios de aceptación**:
- Indica que si el coste no supera 12 mensualidades de gastos comunes, es obligatorio.
- Si supera 12 mensualidades, se necesita 3/5 de propietarios y cuotas.
- Menciona que un solo propietario con discapacidad o mayor de 70 puede exigirlo dentro del límite.
- Explica la obligación de accesibilidad de la LPH.

---

## Test 3 --- Alquiler turístico

**Prompt**: "Un vecino ha puesto su piso en Airbnb y hay ruido constante. ¿Puede la comunidad prohibirlo?"

**Criterios de aceptación**:
- Indica que se puede limitar o condicionar con 3/5 de propietarios y cuotas.
- Menciona que se puede incrementar la cuota del piso turístico hasta un 20 %.
- Indica que el acuerdo debe inscribirse en el Registro de la Propiedad.
- Cita el RDL 7/2019 como base legal.

---

## Test 4 --- Routing a alquiler

**Prompt**: "Quiero alquilar mi piso. ¿Qué dice la LAU sobre el contrato?"

**Criterios de aceptación**:
- Indica que esa consulta corresponde a la skill **vivienda-alquiler**.
- No intenta explicar la LAU en detalle.
