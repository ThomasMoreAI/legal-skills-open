---
name: demanda_laboral
description: Plantilla básica para demanda laboral (demanda por despido injustificado)
inputs:
  - trabajador
  - empleador
  - hechos
  - indemnizacion

---

# DEMANDA LABORAL (Plantilla)

A: H. Tribunal competente

Asunto: Demanda por despido injustificado

Actores:
- Trabajador: {{trabajador.name}} ({{trabajador.rfc or "N/A"}})
- Empleador: {{empleador.name}}

Hechos:
{{#each hechos}}
- {{this}}
{{/each}}

Concepto jurídico:
Se alega despido injustificado, conforme a {{indemnizacion.reference_norm}}

Pretensiones:
1. Pago de indemnización por despido injustificado: {{indemnizacion.amount}}
2. Demás prestaciones conforme a ley.

Atentamente,

_____________________
Nombre del representante
