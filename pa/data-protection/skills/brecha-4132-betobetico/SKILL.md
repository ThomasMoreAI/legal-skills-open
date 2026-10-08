---
name: brecha-4132-betobetico
title: /brecha
description: Protocolo de respuesta ante brechas de seguridad de datos personales. Guía el proceso desde la detección hasta la notificación conjunta a la ANTAI y a los titulares afectados cuando haya riesgo, en 72 horas, conforme a la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021. Genera checklist de acciones y plantillas de notificación. Usar cuando el usuario dice "brecha de seguridad", "incidente de datos", "notificación ANTAI", "nos han hackeado", "fuga de datos", o ante cualquier incidente que afecte a datos personales.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/proteccion-datos/skills/brecha
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
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

Guiar la respuesta inmediata ante una brecha de seguridad de datos personales, asegurando el cumplimiento del plazo de 72 horas para notificar conjuntamente a la ANTAI y a los titulares afectados, y la correcta evaluación del riesgo.

## URGENCIA: El reloj corre

> **Desde que se tiene conocimiento del incidente** hay un plazo de **72 horas** para notificar (art. 37 del Decreto Ejecutivo 285 de 2021). Cuando la violación represente un **riesgo** (umbral único, no "alto riesgo"), la notificación se dirige **conjuntamente a la ANTAI y a los titulares afectados** en ese mismo plazo de 72 horas. Si se supera el plazo, hay que justificar el retraso. Se entiende por "tener conocimiento" el momento en que el responsable tiene certeza razonable de que se ha producido un incidente de seguridad que afecta a datos personales.

## Paso 1: Detección y contención

| Acción | Responsable | Plazo | Estado |
|---|---|---|---|
| Confirmar que el incidente afecta a datos personales | IT + responsable de protección de datos | Inmediato | [ ] |
| Contener la brecha (aislar sistemas, revocar accesos) | IT | Inmediato | [ ] |
| Documentar: qué ha pasado, cuándo, cómo se detectó | IT + Legal | Primeras horas | [ ] |
| Preservar evidencias (logs, capturas, correos) | IT | Inmediato | [ ] |
| Activar equipo de respuesta a incidentes | Dirección | Inmediato | [ ] |

## Paso 2: Evaluación del riesgo

### Datos afectados

| Factor | Descripción | Impacto |
|---|---|---|
| Tipo de datos | Identificativos / económicos / salud / menores / judiciales | A más sensibilidad, mayor riesgo |
| Volumen | N.o de registros y de titulares afectados | A mayor volumen, mayor riesgo |
| Categorías de titulares | Empleados / clientes / menores / pacientes | Personas vulnerables = mayor riesgo |

### Naturaleza de la brecha

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Confidencialidad** | Acceso no autorizado o divulgación | Datos expuestos en internet, robo de BBDD |
| **Integridad** | Modificación no autorizada | Alteración de registros médicos |
| **Disponibilidad** | Pérdida de acceso (temporal o permanente) | Ransomware, destrucción de datos sin backup |

### Nivel de riesgo

> En Panamá hay un **único umbral**: el "riesgo". A diferencia del RGPD, la norma no distingue "notificar a la ANTAI si hay riesgo" frente a "comunicar a los titulares solo si hay alto riesgo". El art. 37 del Decreto Ejecutivo 285 de 2021 exige notificar **a la ANTAI y a los titulares afectados conjuntamente, en 72 horas**, cuando la violación represente un riesgo.

| Nivel | Criterio | Obligación |
|---|---|---|
| **Sin riesgo** | Datos cifrados, brecha contenida sin acceso efectivo | Documentar internamente (art. 38 del Decreto Ejecutivo 285 de 2021) |
| **Riesgo** | Posible impacto en los derechos del titular | Notificar **conjuntamente a la ANTAI y a los titulares afectados** en 72 horas (art. 37 del Decreto Ejecutivo 285 de 2021) + documentar (art. 38) |

## Paso 3: Notificación conjunta a la ANTAI y a los titulares

### Plazo: 72 horas desde el conocimiento (art. 37 del Decreto Ejecutivo 285 de 2021)

Cuando haya riesgo, la notificación se dirige **a la ANTAI y a los titulares afectados conjuntamente**, en el mismo plazo de 72 horas. No existe el escalonado del RGPD.

### Contenido mínimo de la notificación (art. 37 del Decreto Ejecutivo 285 de 2021)

| Campo | Contenido |
|---|---|
| Naturaleza del incidente | Tipo, categorías de datos comprometidos y de titulares, n.o aproximado |
| Acciones correctivas inmediatas | Medidas de contención y mitigación adoptadas |
| Recomendaciones al titular | Qué puede hacer el titular para protegerse |
| Medios para más información | Datos de contacto (nombre, email, teléfono) |

### Canal: ANTAI

La notificación se realiza a través del canal habilitado por la ANTAI.

## Paso 4: Comunicación a los titulares afectados

Forma parte de la notificación conjunta del art. 37 del Decreto Ejecutivo 285 de 2021: cuando haya **riesgo** (umbral único, no "alto riesgo"), se comunica a los titulares afectados en el mismo plazo de 72 horas, junto con la notificación a la ANTAI.

| Campo | Contenido |
|---|---|
| Lenguaje | Claro y sencillo |
| Naturaleza del incidente | Qué ha pasado, sin tecnicismos |
| Datos de contacto | Para más información |
| Consecuencias probables | Qué riesgos tiene para el titular |
| Acciones correctivas | Qué se ha hecho para solucionar y proteger |
| Recomendaciones | Qué puede hacer el titular (cambiar contraseñas, vigilar cuentas, etc.) |

## Paso 5: Documentación

Toda brecha debe documentarse, con independencia de si se notifica (art. 38 del Decreto Ejecutivo 285 de 2021):

- Fecha del incidente.
- Motivo del incidente.
- Hechos y efectos: qué ocurrió, cómo, y qué datos se vieron afectados.
- Medidas correctivas adoptadas.
- Decisión de notificar o no (y justificación si no se notifica).

## Formato de salida

```markdown
URGENTE — GESTIÓN DE BRECHA DE SEGURIDAD — ACCIÓN INMEDIATA REQUERIDA

> **Nota para el revisor**
> - **Plazo de notificación conjunta (ANTAI + titulares):** [fecha/hora límite — 72 horas desde el conocimiento, art. 37 del Decreto Ejecutivo 285 de 2021]
> - **Nivel de riesgo estimado:** [sin riesgo / riesgo]
> - **Antes de actuar:** confirmar alcance real con IT; validar evaluación de riesgo con el responsable de protección de datos; verificar si aplican obligaciones sectoriales adicionales.

## Brecha de seguridad: [Descripción breve]

### Cronología

| Fecha/hora | Evento |
|---|---|
| [fecha] | Detección del incidente |
| [fecha] | Conocimiento por el responsable |
| [fecha] | **Plazo límite notificación conjunta (ANTAI + titulares): 72 horas (art. 37 del Decreto Ejecutivo 285 de 2021)** |

### Evaluación de riesgo

[Tabla con la evaluación]

### Checklist de acciones

- [ ] Contención del incidente
- [ ] Preservación de evidencias
- [ ] Evaluación de riesgo completada
- [ ] Notificación conjunta a la ANTAI y a los titulares afectados (si hay riesgo) — plazo: 72 horas (art. 37 del Decreto Ejecutivo 285 de 2021)
- [ ] Documentación interna del incidente (art. 38 del Decreto Ejecutivo 285 de 2021)
- [ ] Análisis de causa raíz
- [ ] Medidas correctivas implementadas

### Plantilla de notificación a la ANTAI

[Plantilla con el contenido mínimo del art. 37 del Decreto Ejecutivo 285 de 2021, rellenada con los datos disponibles]

### Plantilla de comunicación a los titulares afectados (notificación conjunta)

[Plantilla en lenguaje claro]

---

**Qué hacer a continuación:**
1. **Notificar a la ANTAI** — ya está la plantilla, hay que presentarla por el canal habilitado (72 horas, art. 37 del Decreto Ejecutivo 285 de 2021).
2. **Comunicar a los titulares afectados** — si hay riesgo, enviar la comunicación conjuntamente, en el mismo plazo de 72 horas.
3. **Análisis forense** — coordinar con IT el análisis de causa raíz.
4. **Actualizar protocolo** — ajustar medidas de seguridad para prevenir recurrencia.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 81 de 2019** — deber de seguridad y confidencialidad.
- **Decreto Ejecutivo 285 de 2021** — art. 37 (notificación en 72 horas, conjunta a la ANTAI y a los titulares afectados ante riesgo, y contenido mínimo) y art. 38 (documentación de toda brecha).
- **Guías de la ANTAI** para la gestión y notificación de incidentes de seguridad.

## Guardarraíles

- **El plazo cuenta desde el CONOCIMIENTO, no desde el incidente.** No vale alegar desconocimiento si la brecha se debió detectar antes [verificar].
- **En caso de duda sobre si notificar, notificar.** Es mejor notificar una brecha que resulte menor que no notificar una que resulte grave.
- **No minimizar el riesgo para evitar notificar.** La ANTAI puede sancionar tanto la falta de notificación como la evaluación de riesgo negligente [verificar].
- **Obligaciones sectoriales adicionales.** Según el sector (telecomunicaciones, banca, salud), puede haber obligaciones adicionales de notificación a otros reguladores (SBP, ASEP, MINSA, etc.) [verificar].
- **No borrar evidencias.** La contención no puede destruir los logs y pruebas necesarios para el análisis forense.
- **Este skill gestiona la respuesta jurídica.** La respuesta técnica (contención, análisis forense) es competencia de IT/ciberseguridad.
