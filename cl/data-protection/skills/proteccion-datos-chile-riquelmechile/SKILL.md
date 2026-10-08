---
name: proteccion-datos-chile-riquelmechile
title: Protección de Datos Chile
description: Analiza, diseña, implementa o audita cumplimiento de protección de datos personales en Chile bajo la Ley 19.628 y su reforma por Ley 21.719. Úsala para privacidad, datos personales, consentimiento, derechos de titulares, DPIA, incidentes, encargados, transferencias internacionales, biometría, niños y adolescentes, decisiones automatizadas, IA, modelos de prevención, políticas, contratos, código, APIs, bases de datos o arquitectura.
author: riquelmechile
author_url: https://github.com/riquelmechile/Skills-Chile/tree/main/skills/proteccion-datos-chile
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: data-protection
language: es
sources:
- title: Marco Y Vigencia
  path: references/marco-y-vigencia.md
- title: Obligaciones Y Derechos
  path: references/obligaciones-y-derechos.md
- title: Seguridad Incidentes Dpia Ia
  path: references/seguridad-incidentes-dpia-ia.md
- title: Terceros Transferencias Sanciones
  path: references/terceros-transferencias-sanciones.md
---

# Protección de Datos Chile

**Última verificación jurídica: 2026-08-14.**

Convierte la normativa chilena de protección de datos en decisiones, controles y evidencia verificable. No declares cumplimiento por la existencia de una política: exige evidencia de diseño y operación.

> Esta skill apoya análisis y cumplimiento. Para decisiones jurídicas de alto impacto, litigios, sanciones o interpretaciones dudosas, identifica la incertidumbre y solicita revisión profesional; no inventes una conclusión para cerrar el análisis.

## 0. Router temporal obligatorio

Antes de aplicar una obligación, fija la fecha relevante del tratamiento, incidente, contrato o auditoría.

- **Hasta 30-NOV-2026:** la Ley 19.628 vigente sigue siendo el régimen exigible. La Ley 21.719 se usa como **readiness / transición**, no como si todas sus obligaciones ya fueran exigibles.
- **Desde 01-DIC-2026:** aplica la Ley 19.628 modificada por la Ley 21.719 y sus modificaciones vigentes.
- Si el caso cruza ambas fechas, separa el análisis en periodos.
- Si la consulta depende de normativa posterior a la última verificación, revisa primero fuentes oficiales. Lee [`references/marco-y-vigencia.md`](references/marco-y-vigencia.md).

## Flujo de trabajo

1. **Define alcance y rol.** Identifica responsable, tercero mandatario/encargado, cesionario, órgano público, proveedor extranjero y titulares afectados. Determina si hay alcance territorial chileno.
2. **Modela el tratamiento.** Recorre: **qué datos**, **por qué**, **dónde**, **quién accede/recibe**, **cuánto tiempo**, **cómo se protegen**. Añade origen, base de licitud, transferencias, automatización y categorías especiales.
3. **Aplica norma artículo-primero.** Para cada hallazgo: artículo/regla → aplicabilidad → excepción → evidencia → brecha → acción. Nunca empieces por un control extranjero y luego fuerces la ley chilena a encajar.
4. **Exige evidencia.** Distingue `obligación legal`, `control recomendado` y `evidencia observada`. Una afirmación sin evidencia queda como `NO VERIFICADO`.
5. **Prioriza riesgo.** Usa `CRÍTICO / ALTO / MEDIO / BAJO`, justificando impacto en titulares, sensibilidad, escala, automatización, exposición y sanción potencial; no calcules una multa cierta sin procedimiento y hechos suficientes.
6. **Remedia con dueño y prueba.** Cada acción debe indicar responsable, plazo, evidencia de cierre y prueba de efectividad.
7. **Verifica vigencia.** En asuntos regulatorios actuales, confirma LeyChile/BCN, Diario Oficial y, cuando corresponda, instrucciones de la Agencia antes de cerrar.

## Salidas soportadas

### Respuesta jurídica-operativa

Entrega, en este orden:

1. régimen temporal aplicable;
2. regla y artículo;
3. por qué aplica o no aplica;
4. excepciones/condiciones;
5. evidencia que falta revisar;
6. acción práctica;
7. incertidumbres o normas complementarias pendientes.

### Gap analysis / auditoría

Usa esta matriz mínima:

| Requisito | Artículo | Aplica | Estado | Evidencia | Riesgo | Brecha | Acción | Owner | Plazo |
|---|---|---|---|---|---|---|---|---|---|

Estados: `CUMPLE`, `PARCIAL`, `NO CUMPLE`, `NO APLICA`, `NO VERIFICADO`.

Para obligaciones y derechos, lee [`references/obligaciones-y-derechos.md`](references/obligaciones-y-derechos.md).

### Revisión de software, arquitectura o IA

No revises sólo la política de privacidad. Inspecciona al menos:

- puntos de recolección y campos;
- base de licitud por finalidad;
- minimización y retención;
- permisos, secretos, logs, backups y ambientes;
- APIs, exportaciones, analítica, trackers y terceros;
- ubicación y transferencias internacionales;
- mecanismos para derechos del titular;
- perfilamiento y decisiones automatizadas;
- datos sensibles, biométricos y de niños, niñas o adolescentes;
- trazabilidad de incidentes y evidencia de controles.

Para seguridad, incidentes, DPIA e IA, lee [`references/seguridad-incidentes-dpia-ia.md`](references/seguridad-incidentes-dpia-ia.md).

### Terceros y gobernanza

Para contratos de encargados, cesiones, transferencias internacionales, sanciones y modelo de prevención, lee [`references/terceros-transferencias-sanciones.md`](references/terceros-transferencias-sanciones.md).

## Guardrails Chile-específicos

- **Brechas:** no asumas un plazo general de **72 horas** por analogía con GDPR; la Ley 21.719 usa el estándar de reporte a la Agencia **sin dilaciones indebidas** cuando concurre el umbral legal. Verifica además normativa sectorial aplicable.
- **RoPA:** un **RoPA / inventario de tratamientos es útil como control y evidencia, pero no lo presentes como obligación legal universal de la Ley 21.719** si no existe una norma específica aplicable al caso.
- **DPO:** el **DPO/delegado es parte del modelo voluntario de prevención de infracciones; no lo presentes como obligación universal para todo responsable** sin una fuente adicional que lo exija para ese caso.
- **GDPR/ISO:** GDPR, ISO/IEC 27001, ISO/IEC 27701, NIST u otros marcos pueden mejorar controles o servir de crosswalk, pero no sustituyen el texto chileno ni crean por sí solos una obligación legal local.
- **Fuentes públicas:** bajo el nuevo régimen, que un dato provenga de una fuente de acceso público no lo deja fuera de la ley.
- **Datos reales:** para ejemplos, pruebas y documentación, minimiza o anonimiza datos personales. No copies RUT, salud, biometría, credenciales u otros datos reales si no son imprescindibles.
- **Norma pendiente:** si la ley remite a reglamento, instrucción general, lista o criterio de la Agencia y no has verificado su versión vigente, marca `PENDIENTE DE VERIFICACIÓN REGULATORIA`.

## Disciplina de fuentes

Prioridad: (1) LeyChile/BCN y Diario Oficial; (2) Agencia de Protección de Datos Personales cuando sus actos sean vigentes; (3) regulador sectorial competente; (4) jurisprudencia/Contraloría según materia; (5) fuentes secundarias sólo como contexto.

No cites de memoria un número de artículo, plazo o sanción cuando la precisión pueda cambiar el resultado. Reabre la fuente oficial y verifica.
