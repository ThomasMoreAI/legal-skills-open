---
name: proveedor-3492-betobetico
title: /proveedor
description: Revisor de IA de proveedor — revisa las condiciones contractuales de un proveedor de IA (SaaS con IA, API de modelos, herramientas de IA). Comprueba cláusulas sobre entrenamiento con datos, responsabilidad, cambios de modelo, SLAs y transparencia. Usar cuando el usuario diga "revisar contrato de IA", "condiciones del proveedor de IA", "¿podemos usar esta herramienta?" o adjunte un contrato de servicio de IA.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/gobernanza-ia/skills/proveedor
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# /proveedor

1. Cargar `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md` → playbook de contratos IA, requisitos, posición.
2. Obtener el contrato o condiciones del proveedor.
3. Revisar cláusula por cláusula contra el playbook.
4. Generar tabla de cláusulas con riesgo.

```
/gobernanza-ia:proveedor
[pegar las condiciones de servicio de la herramienta de IA]
```

---

## Propósito

Contratar un proveedor de IA no es como contratar cualquier SaaS. Los riesgos son distintos: ¿entrenan con nuestros datos? ¿pueden cambiar el modelo sin aviso? ¿qué pasa si el output es incorrecto y causa daño? ¿cumplen con el Reglamento de IA? Este skill revisa las condiciones contractuales del proveedor contra un checklist específico de IA.

---

## Cláusulas a revisar

### Cláusulas críticas de IA

| Cláusula | Riesgo si falta/inadecuada | Posición recomendada |
|---|---|---|
| **Entrenamiento con datos del cliente** | El proveedor puede usar nuestros datos para entrenar/mejorar sus modelos → pérdida de confidencialidad, posible infracción RGPD | Prohibición expresa de usar datos del cliente para entrenamiento; si se permite, opt-in con alcance definido |
| **Propiedad del output** | Ambigüedad sobre quién es titular del contenido generado | Output generado con nuestros datos es nuestro; sin restricción de uso |
| **Responsabilidad por output** | El proveedor excluye toda responsabilidad por outputs incorrectos, sesgados o dañinos | Responsabilidad compartida; el proveedor responde de defectos del modelo |
| **Cambios de modelo** | El proveedor puede cambiar, degradar o retirar el modelo sin aviso | Notificación previa; evaluación de impacto ante cambios materiales; derecho de resolución |
| **SLA de disponibilidad y rendimiento** | Sin compromisos concretos de uptime o latencia | SLA medible con penalizaciones |
| **Transparencia del modelo** | No se sabe qué modelo se usa, cómo funciona, con qué datos fue entrenado | Documentación técnica suficiente para cumplir arts. 13-14 RIA |
| **Supervisión humana** | Sin mecanismo para que el deployer mantenga supervisión humana | Herramientas y APIs para implementar supervisión humana (art. 14 RIA) |
| **Cumplimiento del Reglamento de IA** | Sin compromisos de cumplimiento regulatorio | Declaración de cumplimiento; cooperación en auditorías; notificación de cambios regulatorios |

### Cláusulas estándar SaaS (con enfoque IA)

| Cláusula | Punto específico de IA |
|---|---|
| **Protección de datos / DPA** | ¿Cubre el tratamiento por el modelo de IA? ¿Los datos se procesan en la inferencia? ¿Se comparten con terceros (submodelos, APIs externas)? |
| **Subencargados / subcontratistas** | ¿El proveedor usa modelos de terceros (OpenAI, Anthropic, etc.)? ¿Fluyen nuestros datos a esos terceros? |
| **Localización de datos** | ¿Dónde se procesan los datos para la inferencia? ¿Hay transferencias internacionales? |
| **Seguridad** | ¿Medidas específicas para IA? Adversarial testing, detección de envenenamiento de datos |
| **Confidencialidad** | ¿Los prompts/inputs están protegidos? ¿Se loguean? ¿Quién accede? |
| **Indemnización** | ¿Cubre reclamaciones de PI por outputs generados? (Ej., contenido que infringe copyright) |
| **Terminación** | ¿Qué pasa con nuestros datos al terminar? ¿El proveedor retiene datos de entrenamiento? |

---

## Verificación de cumplimiento regulatorio

| Aspecto | Pregunta | Referencia |
|---|---|---|
| ¿El sistema está clasificado como alto riesgo? | Si sí, ¿el proveedor cumple arts. 9-15 RIA? | Reglamento de IA |
| ¿Se proporciona documentación técnica? | Art. 11 RIA exige documentación completa | Art. 11 RIA |
| ¿Hay mecanismo de logging? | Art. 12 RIA exige registro de eventos | Art. 12 RIA |
| ¿Se informa a los usuarios de que interactúan con IA? | Art. 50 RIA — obligación de transparencia | Art. 50 RIA |
| ¿El DPA cubre el tratamiento por IA? | RGPD arts. 28, 32 | RGPD |

---

## Formato de salida

```markdown
# Revisión de proveedor de IA: [Nombre del proveedor]

**Herramienta / Servicio:** [nombre]
**Tipo:** [SaaS con IA / API de modelo / Herramienta on-premise]
**Fecha:** [fecha]
**Nuestro rol RIA:** [Deployer / Proveedor downstream]

---

## Conclusión

[2-3 frases: ¿se puede contratar? ¿qué debe cambiar?]

**Hallazgos:** [N] Conforme [N] Riesgo medio [N] Riesgo alto [N] Bloqueante

---

## Tabla de cláusulas

| # | Cláusula | Lo que dice el contrato | Posición recomendada | Gap | Riesgo |
|---|---|---|---|---|---|
| 1 | Entrenamiento con datos | [texto] | [posición] | [gap] | [nivel] |
| 2 | Responsabilidad por output | [texto] | [posición] | [gap] | [nivel] |
| ... | ... | ... | ... | ... | ... |

---

## Cumplimiento regulatorio

| Aspecto | Estado | Observación |
|---|---|---|
| Reglamento de IA | [Conforme / Gaps / No evaluable] | [detalle] |
| RGPD | [Conforme / Gaps] | [detalle] |

---

## Redlines recomendados

[Lista de cambios a solicitar al proveedor]

---

## Si no aceptan

[Alternativas y fallbacks para cada punto bloqueante]
```

---

## Legislación de referencia

- Reglamento de IA (Reglamento UE 2024/1689) — arts. 9-15, 25-27, 50
- RGPD (Reglamento UE 2016/679) — arts. 28, 32, 44-49
- LOPDGDD (LO 3/2018)
- Directiva 85/374/CEE (responsabilidad por productos defectuosos — en revisión para IA)

---

## Lo que este skill NO hace

- No negocia con el proveedor — genera la posición y los redlines.
- No audita técnicamente el modelo de IA — revisa las condiciones contractuales.
- No clasifica el sistema de IA — para eso, usar `/gobernanza-ia:triaje` primero.
