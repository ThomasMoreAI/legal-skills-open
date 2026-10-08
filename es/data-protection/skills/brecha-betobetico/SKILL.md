---
name: brecha-betobetico
title: /brecha
description: Protocolo de respuesta ante brechas de seguridad de datos personales. Guía el proceso desde la detección hasta la notificación a la AEPD (72 horas, art. 33 RGPD) y la comunicación a los interesados si hay alto riesgo (art. 34 RGPD). Genera checklist de acciones y plantillas de notificación. Usar cuando el usuario dice "brecha de seguridad", "incidente de datos", "notificación AEPD", "nos han hackeado", "fuga de datos", o ante cualquier incidente que afecte a datos personales.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/proteccion-datos/skills/brecha
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
---

# /brecha

1. Leer `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — perfil de práctica.
2. Evaluar el incidente según la tipología y gravedad.
3. Determinar obligaciones de notificación.
4. Generar checklist de acciones y plantillas.

---

## Propósito

Guiar la respuesta inmediata ante una brecha de seguridad de datos personales, asegurando el cumplimiento de los plazos legales (72 horas para notificar a la AEPD) y la correcta evaluación del riesgo para los interesados.

## URGENCIA: El reloj corre

> **72 horas desde que se tiene conocimiento de la brecha** para notificar a la AEPD si existe riesgo para los derechos y libertades (art. 33.1 RGPD). Si se supera el plazo, hay que justificar el retraso. La AEPD considera que "tener conocimiento" es el momento en que el responsable tiene certeza razonable de que se ha producido un incidente de seguridad que afecta a datos personales.

## Paso 1: Detección y contención

| Acción | Responsable | Plazo | Estado |
|---|---|---|---|
| Confirmar que el incidente afecta a datos personales | IT + DPD | Inmediato | [ ] |
| Contener la brecha (aislar sistemas, revocar accesos) | IT | Inmediato | [ ] |
| Documentar: qué ha pasado, cuándo, cómo se detectó | IT + Legal | Primeras horas | [ ] |
| Preservar evidencias (logs, capturas, correos) | IT | Inmediato | [ ] |
| Activar equipo de respuesta a incidentes | Dirección | Inmediato | [ ] |

## Paso 2: Evaluación del riesgo

### Datos afectados

| Factor | Descripción | Impacto |
|---|---|---|
| Tipo de datos | Identificativos / económicos / salud / menores / penales | A más sensibilidad, mayor riesgo |
| Volumen | N.o de registros y de interesados afectados | A mayor volumen, mayor riesgo |
| Categorías de interesados | Empleados / clientes / menores / pacientes | Personas vulnerables = mayor riesgo |

### Naturaleza de la brecha

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Confidencialidad** | Acceso no autorizado o divulgación | Datos expuestos en internet, robo de BBDD |
| **Integridad** | Modificación no autorizada | Alteración de registros médicos |
| **Disponibilidad** | Pérdida de acceso (temporal o permanente) | Ransomware, destrucción de datos sin backup |

### Nivel de riesgo

| Nivel | Criterio | Obligación |
|---|---|---|
| **Sin riesgo** | Datos cifrados, brecha contenida sin acceso efectivo | Documentar internamente (art. 33.5) |
| **Riesgo** | Posible impacto en derechos y libertades | Notificar a AEPD en 72h (art. 33) |
| **Alto riesgo** | Probable impacto grave: usurpación de identidad, daño reputacional, perjuicio económico significativo | Notificar a AEPD + comunicar a interesados (art. 34) |

## Paso 3: Notificación a la AEPD (art. 33 RGPD)

### Plazo: 72 horas desde el conocimiento

### Contenido obligatorio de la notificación (art. 33.3 RGPD)

| Campo | Contenido |
|---|---|
| Naturaleza de la brecha | Tipo, categorías de datos y de interesados, n.o aproximado |
| Datos de contacto del DPD | Nombre, email, teléfono |
| Consecuencias probables | Descripción de los posibles efectos |
| Medidas adoptadas | Medidas de contención y mitigación |

### Canal: Sede electrónica de la AEPD

La notificación se realiza a través de la sede electrónica de la AEPD (formulario de notificación de brechas de seguridad). Se puede hacer una notificación inicial y complementarla después (art. 33.4 RGPD).

## Paso 4: Comunicación a los interesados (art. 34 RGPD)

### Solo si hay alto riesgo

| Campo | Contenido |
|---|---|
| Lenguaje | Claro y sencillo |
| Naturaleza de la brecha | Qué ha pasado, sin tecnicismos |
| Datos de contacto del DPD | Para más información |
| Consecuencias probables | Qué riesgos tiene para el interesado |
| Medidas adoptadas | Qué se ha hecho para solucionar y proteger |
| Recomendaciones | Qué puede hacer el interesado (cambiar contraseñas, vigilar cuentas, etc.) |

### Excepciones a la comunicación (art. 34.3 RGPD)

- Los datos estaban cifrados u otra medida que los haga ininteligibles.
- Se han tomado medidas posteriores que eliminan el alto riesgo.
- Supondría un esfuerzo desproporcionado — en ese caso, comunicación pública.

## Paso 5: Documentación (art. 33.5 RGPD)

Toda brecha debe documentarse, con independencia de si se notifica a la AEPD:

- Hechos: qué ocurrió, cuándo, cómo.
- Efectos: qué datos se vieron afectados.
- Medidas correctivas adoptadas.
- Decisión de notificar o no (y justificación si no se notifica).

## Formato de salida

```markdown
URGENTE — GESTIÓN DE BRECHA DE SEGURIDAD — ACCIÓN INMEDIATA REQUERIDA

> **Nota para el revisor**
> - **Plazo de notificación AEPD:** [fecha/hora límite — 72h desde conocimiento]
> - **Nivel de riesgo estimado:** [sin riesgo / riesgo / alto riesgo]
> - **Antes de actuar:** confirmar alcance real con IT; validar evaluación de riesgo con DPD; verificar si aplican obligaciones sectoriales adicionales.

## Brecha de seguridad: [Descripción breve]

### Cronología

| Fecha/hora | Evento |
|---|---|
| [fecha] | Detección del incidente |
| [fecha] | Conocimiento por el responsable |
| [fecha] | **Plazo límite notificación AEPD** |

### Evaluación de riesgo

[Tabla con la evaluación]

### Checklist de acciones

- [ ] Contención del incidente
- [ ] Preservación de evidencias
- [ ] Evaluación de riesgo completada
- [ ] Notificación a AEPD (si procede) — plazo: [fecha]
- [ ] Comunicación a interesados (si alto riesgo)
- [ ] Documentación interna del incidente
- [ ] Análisis de causa raíz
- [ ] Medidas correctivas implementadas

### Plantilla de notificación a AEPD

[Plantilla con los campos del art. 33.3 rellenados con los datos disponibles]

### Plantilla de comunicación a interesados (si procede)

[Plantilla en lenguaje claro]

---

**Qué hacer a continuación:**
1. **Notificar a AEPD** — ya está la plantilla, hay que presentarla en la sede electrónica.
2. **Comunicar a interesados** — si el riesgo es alto, enviar la comunicación.
3. **Análisis forense** — coordinar con IT el análisis de causa raíz.
4. **Actualizar protocolo** — ajustar medidas de seguridad para prevenir recurrencia.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **RGPD art. 33** — notificación de brechas a la autoridad de control.
- **RGPD art. 34** — comunicación de brechas a los interesados.
- **RGPD art. 33.5** — documentación de brechas.
- **LOPDGDD art. 73.s)** — infracción grave por no notificar.
- **Guía de la AEPD para la gestión y notificación de brechas de seguridad.**

## Guardarraíles

- **Las 72 horas son desde el CONOCIMIENTO, no desde el incidente.** Pero la AEPD interpreta "conocimiento" de forma amplia — no vale alegar desconocimiento si se debió detectar antes.
- **En caso de duda sobre si notificar, notificar.** Es mejor notificar una brecha que resulte menor que no notificar una que resulte grave.
- **No minimizar el riesgo para evitar notificar.** La AEPD sanciona tanto la falta de notificación como la evaluación de riesgo negligente.
- **Obligaciones sectoriales adicionales.** Según el sector (telecomunicaciones, banca, sanidad), puede haber obligaciones adicionales de notificación a otros reguladores.
- **No borrar evidencias.** La contención no puede destruir los logs y pruebas necesarios para el análisis forense.
- **Este skill gestiona la respuesta jurídica.** La respuesta técnica (contención, análisis forense) es competencia de IT/ciberseguridad.
