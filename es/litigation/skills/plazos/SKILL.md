---
name: plazos
title: /plazos
description: Tracker de plazos procesales y extraprocesales para la clínica jurídica. Permite añadir, actualizar y cerrar plazos con alertas de proximidad. Incluye advertencias de responsabilidad profesional por preclusión. Usar cuando el usuario dice "añadir plazo", "plazos pendientes", "vence algo?", "tracker", "calendario de plazos", o necesita gestionar los plazos de los asuntos de la clínica.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/clinica-juridica/skills/plazos
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: litigation
language: es
---

# /plazos

1. Leer `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md` — perfil de la clínica.
2. Leer el tracker existente: `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/plazos.yaml`.
3. Ejecutar la acción solicitada.
4. Escribir el tracker actualizado.
5. Producir la vista de plazos con semáforo.

---

## Propósito

Mantener un registro centralizado de todos los plazos de los asuntos de la clínica, con alertas visuales por proximidad y advertencias de responsabilidad profesional. Un plazo incumplido en la clínica es responsabilidad del supervisor y puede causar un perjuicio irreparable al cliente.

## Acciones disponibles

### Añadir plazo

```
/clinica-juridica:plazos añadir
```

Datos requeridos:

| Campo | Obligatorio | Ejemplo |
|---|---|---|
| Caso (referencia) | Sí | "Caso 2025-031" |
| Descripción del plazo | Sí | "Plazo para contestar a la demanda" |
| Tipo | Sí | Procesal / extrajudicial / administrativo / prescripción |
| Fecha de vencimiento | Sí | 2025-06-15 |
| Base legal | Sí | "Art. 404 LEC — 20 días hábiles" |
| Alumno responsable | Sí | "María García" |
| Supervisor | Sí | "Prof. López" |
| Notas | No | "Notificación recibida el 15/05/2025" |

### Listar plazos

```
/clinica-juridica:plazos listar
```

Muestra todos los plazos activos con semáforo.

### Actualizar plazo

```
/clinica-juridica:plazos actualizar [ID]
```

### Cerrar plazo

```
/clinica-juridica:plazos cerrar [ID]
```

Registra cómo se cumplió el plazo y la fecha de cumplimiento.

## Semáforo de plazos

| Color | Criterio | Acción |
|---|---|---|
| Rojo | Vence en 3 días hábiles o menos | ACCIÓN INMEDIATA — avisar al supervisor |
| Naranja | Vence en 7 días hábiles o menos | Preparar la actuación |
| Amarillo | Vence en 15 días hábiles o menos | Planificar la actuación |
| Verde | Vence en más de 15 días hábiles | En plazo — seguimiento normal |
| Negro | VENCIDO | EMERGENCIA — avisar al supervisor INMEDIATAMENTE |

## Tracker (plazos.yaml)

```yaml
plazos:
  - id: PLZ-001
    caso: "Caso 2025-031"
    descripcion: "Plazo para contestar a la demanda"
    tipo: "procesal"
    fecha_vencimiento: 2025-06-15
    base_legal: "Art. 404 LEC — 20 días hábiles"
    alumno: "María García"
    supervisor: "Prof. López"
    estado: "activo"  # activo | cumplido | vencido
    notas: ""
    fecha_cumplimiento: null
    como_se_cumplio: ""
```

## Formato de salida

```markdown
PLAZOS — CLÍNICA JURÍDICA — [FECHA]

## Resumen

| Estado | Cantidad |
|---|---|
| Rojo (< 3 días) | [N] |
| Naranja (< 7 días) | [N] |
| Amarillo (< 15 días) | [N] |
| Verde (> 15 días) | [N] |
| VENCIDOS | [N] |

## Plazos activos

| ID | Caso | Descripción | Vence | Días | Estado | Alumno | Supervisor |
|---|---|---|---|---|---|---|---|
| PLZ-001 | [caso] | [descripción] | [fecha] | [N] | [semáforo] | [alumno] | [supervisor] |

## Alertas

[Lista de plazos en rojo o naranja con la acción requerida]

## Plazos cumplidos recientemente

[Últimos 5 plazos cerrados]
```

## Advertencias de responsabilidad profesional

> **PRECLUSIÓN.** Un plazo procesal vencido es irrecuperable. No hay segunda oportunidad para contestar a una demanda, interponer un recurso o proponer prueba fuera de plazo. El incumplimiento de un plazo procesal puede:
> - Causar indefensión al cliente.
> - Generar responsabilidad profesional del supervisor.
> - Constituir mala praxis en el ámbito de la clínica.

**Protocolo si un plazo se vence:**
1. Avisar al supervisor INMEDIATAMENTE.
2. Evaluar si hay alguna vía de subsanación (recurso de nulidad de actuaciones, recurso extraordinario).
3. Documentar qué pasó y por qué.
4. Informar al cliente.

## Guardarraíles

- **Los plazos procesales se cuentan en días hábiles (art. 130 LEC, art. 30.2 LPACAP para administrativo).** No confundir con días naturales. Agosto es inhábil en el ámbito jurisdiccional (salvo excepciones).
- **El cómputo empieza al día siguiente de la notificación.** No el mismo día.
- **Verificar siempre la base legal del plazo.** Un plazo mal calculado es tan peligroso como un plazo olvidado.
- **Nunca confiar solo en este tracker.** Es un complemento — el sistema oficial es LexNET / Justicia Digital para notificaciones judiciales.
- **Duplicar alertas.** Si un plazo es crítico, avisar al supervisor por este tracker Y por el medio habitual de comunicación (email, presencial).
- **El supervisor es responsable final.** Este tracker ayuda, pero la responsabilidad de cumplir los plazos es del supervisor de la clínica.
