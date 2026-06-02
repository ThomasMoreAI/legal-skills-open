---
name: carta
title: /carta
description: 'Redacta correspondencia rutinaria de la clínica jurídica: citaciones, solicitudes de documentos, actualizaciones de estado del asunto. Toda carta requiere revisión y aprobación del supervisor antes del envío. Usar cuando el usuario dice "carta al cliente", "citación", "pide documentos", "actualización", o necesita comunicarse con el cliente por escrito.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/clinica-juridica/skills/carta
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: es
---

# /carta

1. Leer `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md` — perfil de la clínica.
2. Identificar el tipo de carta.
3. Generar el borrador.
4. Marcar como pendiente de revisión del supervisor.

---

## Propósito

Producir borradores de correspondencia rutinaria de la clínica jurídica para revisión del supervisor. NINGUNA carta se envía sin aprobación del supervisor.

## GATE: Revisión del supervisor

> **OBLIGATORIO.** Toda carta producida por este skill es un BORRADOR pendiente de revisión y aprobación del supervisor. No se envía al cliente ni a ninguna parte sin la aprobación expresa del supervisor. Incluir siempre la marca "BORRADOR — PENDIENTE DE APROBACIÓN DEL SUPERVISOR" en el encabezado.

## Tipos de carta

### 1. Citación

Convocatoria al cliente para una cita en la clínica.

| Campo | Contenido |
|---|---|
| Destinatario | Nombre del cliente |
| Motivo | Reunión inicial / seguimiento / firma de documentos / otro |
| Fecha y hora | Propuesta de fecha/hora |
| Lugar | Dirección de la clínica |
| Qué debe traer | Documentación necesaria |
| Contacto | Email/teléfono de la clínica para confirmar |

### 2. Solicitud de documentos

Petición al cliente de documentación necesaria para el caso.

| Campo | Contenido |
|---|---|
| Documentos solicitados | Lista detallada y específica |
| Para qué se necesitan | Explicación breve en lenguaje accesible |
| Plazo | Fecha límite para la entrega |
| Cómo entregarlos | En persona / email / correo postal |
| Consecuencias de no aportar | Sin amenazar — explicar que es necesario para avanzar |

### 3. Actualización de estado

Informe al cliente sobre el estado de su asunto.

| Campo | Contenido |
|---|---|
| Estado actual | Qué se ha hecho desde la última comunicación |
| Próximos pasos | Qué va a pasar ahora |
| Plazos pendientes | Si los hay — en lenguaje accesible |
| Acción del cliente | Si necesitamos algo del cliente |
| Contacto | Para dudas |

## Tono y estilo

- **Lenguaje claro y accesible.** Los clientes de la clínica pueden no tener formación jurídica.
- **Evitar jerga legal innecesaria.** Si hay que usar un término jurídico, explicarlo.
- **Respetuoso y profesional.** Sin ser frío ni distante.
- **Breve.** Las cartas rutinarias no necesitan más de una página.
- **Sin asesoramiento jurídico.** Las cartas rutinarias no contienen opiniones legales — para eso está el memo y la reunión presencial.

## Formato de salida

```markdown
BORRADOR — PENDIENTE DE APROBACIÓN DEL SUPERVISOR

---

**CLÍNICA JURÍDICA [nombre de la clínica]**
[Dirección]
[Teléfono] | [Email]

[Ciudad], [fecha]

**[Tipo de carta]**

Estimado/a D./D.a [nombre del cliente]:

[Cuerpo de la carta según el tipo]

Quedamos a su disposición para cualquier consulta.

Atentamente,

[Nombre del alumno/a]
Alumno/a de la Clínica Jurídica
Bajo la supervisión de [nombre del supervisor/a]

---

> **PARA EL SUPERVISOR:** Este borrador fue generado por [alumno/a] el [fecha]. Requiere su revisión y aprobación antes del envío. Marcar "APROBADO" y firmar para autorizar el envío.
>
> - [ ] Revisado
> - [ ] Aprobado para envío
> - Firma del supervisor: _______________
> - Fecha: _______________
```

## Guardarraíles

- **NUNCA enviar sin aprobación del supervisor.** Este es el guardarraíl más importante. Repetirlo en cada salida.
- **No incluir asesoramiento jurídico en cartas rutinarias.** Una carta de citación no es el lugar para opinar sobre las posibilidades del caso.
- **No prometer resultados.** Ni explícita ni implícitamente. "Estamos trabajando en su caso" — no "vamos a ganar".
- **Cuidado con los datos personales.** No incluir más datos de los necesarios. Si la carta se envía por email, verificar que el destinatario es correcto.
- **Adaptar al nivel del cliente.** Si el cliente no habla bien español, simplificar al máximo. Si necesita intérprete, coordinar antes de la cita.
- **No crear expectativas de plazo que no se puedan cumplir.** Si no se sabe cuándo habrá novedades, decir "le informaremos cuando tengamos novedades" — no poner una fecha inventada.
