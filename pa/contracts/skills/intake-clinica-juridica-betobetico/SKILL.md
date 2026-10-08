---
name: intake-clinica-juridica-betobetico
title: /intake
description: Recogida estructurada de datos del cliente para el consultorio jurídico. Identifica datos personales, asunto, jurisdicción, urgencia, conflictos de interés y cuestiones transversales. Deriva a la defensoría de oficio si el asunto excede la competencia del consultorio. Usar cuando el usuario dice "nuevo cliente", "intake", "recogida de datos", "alta de cliente", o llega un asunto nuevo al consultorio.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/clinica-juridica/skills/intake
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: contracts
language: es
---

# /intake

1. Leer `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md` — perfil del consultorio.
2. Ejecutar el formulario de intake.
3. Comprobar conflictos de interés.
4. Identificar cuestiones transversales (cross-area issue spotting).
5. Producir la ficha de cliente.

---

## Propósito

Recoger de forma estructurada toda la información necesaria para abrir un asunto en el consultorio jurídico, detectar conflictos de interés, identificar las áreas del derecho involucradas y determinar si el asunto es competencia del consultorio o debe derivarse.

## Formulario de intake

### Bloque 1: Datos del cliente

| Campo | Obligatorio | Notas |
|---|---|---|
| Nombre y apellidos | Sí | |
| Cédula / pasaporte / carné de residente | Sí | Para conflictos |
| Dirección | Sí | Determina jurisdicción (provincia, distrito, corregimiento) |
| Teléfono | Sí | |
| Email | Sí | |
| Idioma preferido | Sí | Si no habla español, necesidad de intérprete |
| Situación económica | Sí | Determinante para derivación a la defensoría de oficio |

### Bloque 2: Datos del asunto

| Campo | Contenido |
|---|---|
| Descripción del asunto | Relato libre del cliente — no interrumpir, anotar |
| Área(s) del derecho | Civil, penal, administrativo, laboral, familia, migración, consumo, otro |
| Parte contraria | Nombre, relación con el cliente |
| Urgencia | Hay plazos en curso? Cuáles? |
| Documentación aportada | Lista de documentos que trae el cliente |
| Actuaciones previas | Ha consultado otro abogado? Hay procedimiento en curso? |

### Bloque 3: Conflictos de interés

Comprobar contra la base de datos del consultorio:

- El cliente ya fue atendido previamente? Por qué asunto?
- La parte contraria es o fue cliente del consultorio?
- Algún miembro del equipo tiene relación personal con las partes?

**Si hay conflicto:** no abrir el asunto. Derivar a otro consultorio o a la defensoría de oficio.

### Bloque 4: Cross-area issue spotting

Checklist de cuestiones transversales que el asunto puede implicar y que el estudiante/alumno puede no detectar:

| Área | Indicador | Check |
|---|---|---|
| Violencia doméstica | Relación de pareja + agresión/intimidación | [ ] |
| Menores en riesgo | Menores involucrados + desprotección | [ ] |
| Migración | Cliente extranjero + estatus migratorio en riesgo | [ ] |
| Protección de datos | Tratamiento indebido de datos personales (Ley 81 de 2019) | [ ] |
| Consumo | Relación proveedor-consumidor (Ley 45 de 2007) | [ ] |
| Laboral | Relación de trabajo involucrada (Código de Trabajo) | [ ] |
| Tributario | Implicaciones tributarias (ISR / ITBMS) | [ ] |

### Bloque 5: Derivación

| Criterio | Gestiona el consultorio | Deriva a defensoría de oficio | Deriva a especialista |
|---|---|---|---|
| Asunto dentro del ámbito del consultorio | Sí | — | — |
| Cliente cumple requisitos de asistencia legal gratuita | — | Sí [verificar] | — |
| Asunto excede complejidad/competencia | — | — | Sí |
| Conflicto de interés | — | Sí | — |
| Urgencia que el consultorio no puede atender | — | Sí | — |

## Formato de salida

```markdown
CONFIDENCIAL — FICHA DE INTAKE — CONSULTORIO JURÍDICO

## Ficha de cliente

| Campo | Valor |
|---|---|
| Nombre | [nombre] |
| Cédula / pasaporte | [documento] |
| Contacto | [teléfono / email] |
| Fecha de intake | [fecha] |
| Alumno/a responsable | [nombre] |
| Supervisor/a | [nombre] |

## Asunto

**Descripción:** [resumen del asunto]
**Área(s) del derecho:** [áreas identificadas]
**Urgencia:** [alta/media/baja — plazos en curso: sí/no]
**Parte contraria:** [identificación]

## Conflictos de interés

**Resultado:** [sin conflicto / conflicto detectado — detalle]

## Issue spotting

| Cuestión transversal | Detectada | Acción |
|---|---|---|
| [área] | [sí/no] | [acción recomendada] |

## Derivación

**Decisión:** [el consultorio asume / derivar a defensoría de oficio / derivar a especialista]
**Motivo:** [fundamentación]

## Próximos pasos

1. [Paso 1]
2. [Paso 2]

---

**Qué hacer a continuación:**
1. **Memo de caso** — `/clinica-juridica:memo` para el análisis IRAC.
2. **Investigación** — `/clinica-juridica:investigacion` para la hoja de ruta.
3. **Registrar plazos** — `/clinica-juridica:plazos` si hay plazos en curso.
4. **Carta al cliente** — `/clinica-juridica:carta` para confirmación de recepción.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Constitución Política, art. 22** — garantía de defensa y acceso a la justicia [verificar].
- **Ley 81 de 2019** — protección de datos personales del cliente.
- **Código de Ética y Responsabilidad Profesional del Abogado** — conflictos de interés, secreto profesional [verificar].

## Guardarraíles

- **Confidencialidad absoluta.** Los datos del cliente son confidenciales — no compartir fuera del equipo asignado y el supervisor.
- **No abrir asunto con conflicto de interés.** Si hay conflicto, derivar inmediatamente.
- **Los plazos no esperan.** Si el intake detecta plazos en curso (prescripción, caducidad, recurso), registrar inmediatamente en `/clinica-juridica:plazos` y avisar al supervisor.
- **Derivar cuando proceda.** El consultorio tiene límites de competencia y capacidad. Derivar no es un fracaso — es responsabilidad profesional.
- **Especial cuidado con personas vulnerables.** Menores, víctimas de violencia doméstica, personas en situación migratoria irregular — activar protocolos específicos.
- **Todo lo que hace el alumno requiere supervisión.** Este skill produce una ficha para revisión del supervisor, no un producto final.
