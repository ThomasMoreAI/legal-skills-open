---
name: madurez-ia-betobetico
title: Madurez IA y EU AI Act
description: Diagnóstico de madurez IA de la participada y clasificación bajo EU AI Act. Identifica casos de uso (producto y operaciones), evalúa datos, gobierno, sesgo, transparencia. Define plan de cumplimiento si aplica alto riesgo. Triggers en "madurez IA", "EU AI Act", "AI assessment", "clasificación IA", "DD de IA".
author: betobetico
author_url: https://github.com/betobetico/claude-para-servicios-financieros/tree/main/plugins/verticales/capital-privado/skills/madurez-ia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: administrative
language: es
---

# Madurez IA y EU AI Act

## Paso 0
Carga perfil. Contexto: el plugin de Capital Privado evalúa participadas reales del fondo o targets en proceso.

## Paso 1 — Identificación de casos de uso

Inventario:

| # | Caso de uso | Producto / Interno | Modelo (propio/3rd party) | Datos | Decisión que afecta a personas? |
|---|---|---|---|---|---|
| 1 | Scoring crediticio | Producto | LightGBM propio + LLM | Histórico crédito | Sí (clientes finales) |
| 2 | Soporte al cliente | Producto | OpenAI GPT-4 | Conversaciones | No (sugerencias a agente) |
| 3 | Reclutamiento | Interno | HiBob + ATS | CVs | Sí (candidatos) |
| ... | | | | | |

## Paso 2 — Clasificación EU AI Act

Para cada caso de uso, clasifica:

- **Riesgo inaceptable (prohibido)** — social scoring, manipulación subliminal, biometría en tiempo real en espacios públicos (con excepciones policiales)
- **Alto riesgo** — Anexo III: empleo, educación, crédito, seguros vida/salud, gestión infra crítica, biometría, RRHH, fuerzas de seguridad, migración, administración de justicia
- **Riesgo limitado (transparencia)** — chatbots, deepfakes, sistemas de reconocimiento de emociones
- **Riesgo mínimo** — el resto (filtros spam, recomendadores no críticos)

Para **alto riesgo**, obligaciones:
- Sistema de gestión de riesgos
- Calidad de datos (training, validation, testing)
- Documentación técnica
- Trazabilidad (logging)
- Transparencia e información al usuario
- Supervisión humana
- Robustez, ciberseguridad, precisión
- Evaluación de conformidad
- Marcado CE
- Registro UE

## Paso 3 — Gobierno y datos

- ¿Existe AI policy interna?
- ¿Existe AI risk officer / DPO involucrado?
- ¿Datos de entrenamiento: origen, consentimiento, calidad?
- ¿Datos personales en training? RGPD art. 22 — decisiones automatizadas
- ¿Sesgo: hay auditorías, tests, métricas de fairness?
- ¿Transparencia: hay model cards, explicabilidad?
- ¿Plan de re-entrenamiento y monitorización de drift?

## Paso 4 — Riesgos transversales

- **Reputacional:** prensa, regulador, redes
- **Legal:** sanciones EU AI Act (hasta €35M o 7% facturación global)
- **Operacional:** dependencia de proveedor de modelo (OpenAI, Anthropic, Google) — riesgo de cambio de TOS
- **Técnico:** alucinaciones, jailbreaks, prompt injection
- **Ético:** sesgo, discriminación, exclusión

## Paso 5 — Plan de cumplimiento (si alto riesgo)

| Workstream | Acciones | Owner | Fecha límite |
|---|---|---|---|
| Documentación técnica | Crear AI System Card | CTO + DPO | Q+1 |
| Sistema de gestión de riesgos | Implementar | CTO | Q+2 |
| Auditoría de sesgo | Externa | Compliance | Q+2 |
| Trazabilidad / logging | Implementar pipeline | DataOps | Q+1 |
| Marcado CE y registro UE | Iniciar evaluación de conformidad | Legal | Q+3 |

## Paso 6 — Score de madurez (1–5)

- **1** Ad hoc — sin gobierno, sin documentación
- **2** Reactivo — políticas básicas pero no operacionalizadas
- **3** Definido — gobierno claro, documentación, AI policy
- **4** Gestionado — auditorías regulares, métricas de fairness, supervisión humana
- **5** Optimizado — proceso continuo de mejora, certificaciones, leader del sector

## Cierre

> *Diagnóstico orientativo. La clasificación final EU AI Act y la evaluación de conformidad requieren asesor legal y auditoría técnica especializada. Fechas según calendario de aplicación del Reglamento — confirmar versión vigente.*
