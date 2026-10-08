# Tests manuales --- vivienda-alquiler

Preguntas para validar que el agente usa la skill correctamente.

---

## Test 1 --- Contrato de alquiler

**Prompt**: "Voy a alquilar un piso como inquilino. ¿Cuánto dura el contrato mínimo y cuánto tengo que pagar de fianza?"

**Criterios de aceptación**:
- Indica duración mínima de 5 años (si persona física) o 7 (jurídica).
- Menciona la prórroga tácita de 3 años adicionales.
- Fianza: 1 mensualidad obligatoria.
- Garantías adicionales: máximo 2 meses más.
- Menciona que la fianza se deposita en el organismo autonómico.

---

## Test 2 --- Actualización de renta

**Prompt**: "Mi casero quiere subirme el alquiler. ¿Cuánto puede subir y con qué índice?"

**Criterios de aceptación**:
- Explica que desde 2025 se aplica el nuevo índice de referencia del INE.
- Indica que la actualización solo se aplica en la fecha de aniversario del contrato.
- Requiere comunicación escrita con 1 mes de antelación.
- Menciona que si el contrato pacta otro índice (IPC), se aplica el pactado.

---

## Test 3 --- Zonas tensionadas

**Prompt**: "He oído que en Barcelona hay zona tensionada. ¿Qué significa para mi alquiler?"

**Criterios de aceptación**:
- Explica qué es una zona tensionada (Ley 12/2023) y los criterios de declaración.
- Diferencia entre gran tenedor (índice de referencia) y no gran tenedor (renta anterior).
- Indica que la declaración corresponde a la comunidad autónoma.
- Menciona los umbrales: carga > 30 % de ingresos y subida > 3 pp sobre IPC en 5 años.

---

## Test 4 --- Routing a comunidad

**Prompt**: "Los vecinos de mi edificio hacen ruido por la noche. ¿Qué puedo hacer?"

**Criterios de aceptación**:
- Indica que las cuestiones de convivencia en comunidad corresponden a la skill **vivienda-comunidad-propietarios**.
- No intenta resolver el caso desde la perspectiva de la LAU.
