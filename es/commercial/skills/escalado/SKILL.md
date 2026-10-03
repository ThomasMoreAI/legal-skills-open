---
name: escalado
title: Propósito
description: Enruta incidencias de revisión contractual al aprobador correcto según la matriz de escalado
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/mercantil/skills/escalado
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: commercial
language: en
---

## Propósito

Esta skill toma una incidencia detectada durante la revisión de un contrato mercantil, la clasifica según la matriz de escalado del despacho y redacta el mensaje de escalado dirigido al aprobador correspondiente. No envía el mensaje — lo presenta como borrador para aprobación del usuario.

## Instrucciones

### Paso 1 — Cargar matriz de escalado

1. Leer la matriz de escalado desde `~/.claude/plugins/config/claude-para-abogados/mercantil/CLAUDE.md`.
2. Si no existe matriz configurada, usar la matriz por defecto:
   - **Nivel 1 — Socio responsable**: Limitación de responsabilidad > umbral, indemnizaciones ilimitadas, cambio de ley aplicable.
   - **Nivel 2 — Abogado senior**: Desviaciones AMARILLO en cláusulas financieras, plazos de pago > 60 días, penalizaciones.
   - **Nivel 3 — Equipo de cumplimiento**: Cláusulas de protección de datos, transferencias internacionales, subcontratación.

### Paso 2 — Clasificar la incidencia

Determinar:

1. **Categoría**: financiera, responsabilidad, PI, datos, jurisdicción, otra.
2. **Severidad**: ROJO (bloqueante) o AMARILLO (requiere decisión).
3. **Impacto estimado**: cuantificable o cualitativo.
4. **Urgencia**: según plazos del contrato o negociación.

### Paso 3 — Identificar aprobador

Cruzar categoría y severidad con la matriz para determinar:

- Nombre/rol del aprobador.
- Canal de comunicación preferido (si está en config).
- Plazo de respuesta esperado.

### Paso 4 — Redactar mensaje de escalado

Generar un borrador conciso y estructurado.

## Formato de salida

```markdown
## Borrador de escalado

**Estado:** BORRADOR — Pendiente de aprobación del usuario

---

**Para:** [nombre/rol del aprobador]
**De:** [equipo de revisión contractual]
**Asunto:** Escalado [ROJO/AMARILLO] — [nombre del contrato] — [cláusula afectada]
**Urgencia:** [Alta/Media]
**Plazo de respuesta sugerido:** [fecha/plazo]

### Contexto

- **Contrato:** [nombre y contraparte]
- **Fase:** [negociación / renovación / ejecución]
- **Cláusula afectada:** [número y título]

### Incidencia

[Descripción concisa del problema en 2-3 frases]

### Posición del playbook

[Qué dice el playbook sobre esta cláusula]

### Posición del contrato

[Qué dice el contrato actualmente]

### Opciones

1. [Opción A con pros/contras]
2. [Opción B con pros/contras]

### Decisión requerida

[Qué necesita decidir el aprobador, formulado como pregunta concreta]
```

## Referencias normativas

- **CC art. 1258**: Los contratos obligan a todas las consecuencias conformes a la buena fe, uso y ley.
- **CC art. 1255**: Autonomía de la voluntad y sus límites (ley, moral, orden público).
- **Código de Comercio art. 2**: Actos de comercio.
- Normativa sectorial aplicable según la naturaleza del contrato.

## Guardrails

- **NO envía** el mensaje de escalado — siempre lo presenta como borrador.
- **NO toma** decisiones sobre la incidencia — solo presenta opciones.
- **NO contacta** directamente a ningún aprobador ni sistema externo.
- **NO modifica** el contrato ni propone redacciones alternativas en el escalado.
- **ESCALAR al usuario** si la incidencia no encaja en ninguna categoría de la matriz.
- **ESCALAR al usuario** si la severidad es ambigua entre ROJO y AMARILLO.
- **AVISAR** si la matriz de escalado no está configurada y se usa la matriz por defecto.
