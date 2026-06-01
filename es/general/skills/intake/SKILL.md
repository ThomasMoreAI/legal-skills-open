---
name: intake
title: /intake
description: Recogida estructurada de datos del cliente para la clínica jurídica. Identifica datos personales, asunto, jurisdicción, urgencia, conflictos de interés y cuestiones transversales. Deriva a turno de oficio si el asunto excede la competencia de la clínica. Usar cuando el usuario dice "nuevo cliente", "intake", "recogida de datos", "alta de cliente", o llega un asunto nuevo a la clínica.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/clinica-juridica/skills/intake
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# /intake

1. Leer `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md` — perfil de la clínica.
2. Ejecutar el formulario de intake.
3. Comprobar conflictos de interés.
4. Identificar cuestiones transversales (cross-area issue spotting).
5. Producir la ficha de cliente.

---

## Propósito

Recoger de forma estructurada toda la información necesaria para abrir un asunto en la clínica jurídica, detectar conflictos de interés, identificar las áreas del derecho involucradas y determinar si el asunto es competencia de la clínica o debe derivarse.

## Formulario de intake

### Bloque 1: Datos del cliente

| Campo | Obligatorio | Notas |
|---|---|---|
| Nombre y apellidos | Sí | |
| DNI/NIE/Pasaporte | Sí | Para conflictos |
| Dirección | Sí | Determina jurisdicción |
| Teléfono | Sí | |
| Email | Sí | |
| Idioma preferido | Sí | Si no habla español, necesidad de intérprete |
| Situación económica | Sí | Determinante para derivación a turno de oficio |

### Bloque 2: Datos del asunto

| Campo | Contenido |
|---|---|
| Descripción del asunto | Relato libre del cliente — no interrumpir, anotar |
| Área(s) del derecho | Civil, penal, administrativo, laboral, familia, extranjería, consumo, otro |
| Parte contraria | Nombre, relación con el cliente |
| Urgencia | Hay plazos en curso? Cuáles? |
| Documentación aportada | Lista de documentos que trae el cliente |
| Actuaciones previas | Ha consultado otro abogado? Hay procedimiento en curso? |

### Bloque 3: Conflictos de interés

Comprobar contra la base de datos de la clínica:

- El cliente ya fue atendido previamente? Por qué asunto?
- La parte contraria es o fue cliente de la clínica?
- Algún miembro del equipo tiene relación personal con las partes?

**Si hay conflicto:** no abrir el asunto. Derivar a otra clínica o al turno de oficio.

### Bloque 4: Cross-area issue spotting

Checklist de cuestiones transversales que el asunto puede implicar y que el estudiante/alumno puede no detectar:

| Área | Indicador | Check |
|---|---|---|
| Violencia de género | Relación de pareja + agresión/intimidación | [ ] |
| Menores en riesgo | Menores involucrados + desprotección | [ ] |
| Extranjería | Cliente extranjero + permiso en riesgo | [ ] |
| Protección de datos | Tratamiento indebido de datos personales | [ ] |
| Consumo | Relación empresa-consumidor | [ ] |
| Laboral | Relación de trabajo involucrada | [ ] |
| Fiscal | Implicaciones tributarias | [ ] |

### Bloque 5: Derivación

| Criterio | Gestiona la clínica | Deriva a turno de oficio | Deriva a especialista |
|---|---|---|---|
| Asunto dentro del ámbito de la clínica | Sí | — | — |
| Cliente cumple requisitos de justicia gratuita | — | Sí (Ley 1/1996) | — |
| Asunto excede complejidad/competencia | — | — | Sí |
| Conflicto de interés | — | Sí | — |
| Urgencia que la clínica no puede atender | — | Sí | — |

## Formato de salida

```markdown
CONFIDENCIAL — FICHA DE INTAKE — CLÍNICA JURÍDICA

## Ficha de cliente

| Campo | Valor |
|---|---|
| Nombre | [nombre] |
| DNI/NIE | [documento] |
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

**Decisión:** [la clínica asume / derivar a turno de oficio / derivar a especialista]
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

- **Ley 1/1996** — de Asistencia Jurídica Gratuita.
- **LOPD/RGPD** — protección de datos del cliente.
- **Código Deontológico de la Abogacía** — conflictos de interés, secreto profesional.

## Guardarraíles

- **Confidencialidad absoluta.** Los datos del cliente son confidenciales — no compartir fuera del equipo asignado y el supervisor.
- **No abrir asunto con conflicto de interés.** Si hay conflicto, derivar inmediatamente.
- **Los plazos no esperan.** Si el intake detecta plazos en curso (prescripción, caducidad, recurso), registrar inmediatamente en `/clinica-juridica:plazos` y avisar al supervisor.
- **Derivar cuando proceda.** La clínica tiene límites de competencia y capacidad. Derivar no es un fracaso — es responsabilidad profesional.
- **Especial cuidado con personas vulnerables.** Menores, víctimas de violencia de género, personas en situación irregular — activar protocolos específicos.
- **Todo lo que hace el alumno requiere supervisión.** Este skill produce una ficha para revisión del supervisor, no un producto final.
