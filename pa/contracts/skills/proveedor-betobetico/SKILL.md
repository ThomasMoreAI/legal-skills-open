---
name: proveedor-betobetico
title: /proveedor
description: Revisor de IA de proveedor — revisa las condiciones contractuales de un proveedor de IA (SaaS con IA, API de modelos, herramientas de IA). Comprueba cláusulas sobre entrenamiento con datos, responsabilidad, cambios de modelo, SLAs y transparencia. Usar cuando el usuario diga "revisar contrato de IA", "condiciones del proveedor de IA", "¿podemos usar esta herramienta?" o adjunte un contrato de servicio de IA.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/gobernanza-ia/skills/proveedor
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
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

Contratar un proveedor de IA no es como contratar cualquier SaaS. Los riesgos son distintos: ¿entrenan con nuestros datos? ¿pueden cambiar el modelo sin aviso? ¿qué pasa si el output es incorrecto y causa daño? ¿respetan la normativa panameña de protección de datos? Panamá no tiene ley de IA vinculante, así que la revisión se apoya en buenas prácticas de gobernanza, en marcos internacionales de referencia (NIST AI RMF, ISO/IEC 42001) y, en lo conexo, en la Ley 81 de 2019 sobre protección de datos personales. Este skill revisa las condiciones contractuales del proveedor contra un checklist específico de IA.

---

## Cláusulas a revisar

### Cláusulas críticas de IA

| Cláusula | Riesgo si falta/inadecuada | Posición recomendada |
|---|---|---|
| **Entrenamiento con datos del cliente** | El proveedor puede usar nuestros datos para entrenar/mejorar sus modelos → pérdida de confidencialidad, posible infracción de la Ley 81 de 2019 | Prohibición expresa de usar datos del cliente para entrenamiento; si se permite, opt-in con alcance definido |
| **Propiedad del output** | Ambigüedad sobre quién es titular del contenido generado | Output generado con nuestros datos es nuestro; sin restricción de uso |
| **Responsabilidad por output** | El proveedor excluye toda responsabilidad por outputs incorrectos, sesgados o dañinos | Responsabilidad compartida; el proveedor responde de defectos del modelo |
| **Cambios de modelo** | El proveedor puede cambiar, degradar o retirar el modelo sin aviso | Notificación previa; evaluación de impacto ante cambios materiales; derecho de resolución |
| **SLA de disponibilidad y rendimiento** | Sin compromisos concretos de uptime o latencia | SLA medible con penalizaciones |
| **Transparencia del modelo** | No se sabe qué modelo se usa, cómo funciona, con qué datos fue entrenado | Documentación técnica suficiente para informar a usuarios y mantener supervisión humana |
| **Supervisión humana** | Sin mecanismo para que el implementador mantenga supervisión humana | Herramientas y APIs para implementar supervisión humana |
| **Buenas prácticas de gobernanza de IA** | Sin compromisos de gobernanza ni de protección de datos | Declaración de adhesión a estándares (NIST AI RMF / ISO 42001); cooperación en auditorías; notificación de cambios relevantes |

### Cláusulas estándar SaaS (con enfoque IA)

| Cláusula | Punto específico de IA |
|---|---|
| **Protección de datos / acuerdo de tratamiento** | ¿Cubre el tratamiento por el modelo de IA? ¿Los datos se procesan en la inferencia? ¿Se comparten con terceros (submodelos, APIs externas)? ¿Cumple la Ley 81 de 2019? |
| **Subencargados / subcontratistas** | ¿El proveedor usa modelos de terceros (OpenAI, Anthropic, etc.)? ¿Fluyen nuestros datos a esos terceros? |
| **Localización de datos** | ¿Dónde se procesan los datos para la inferencia? ¿Hay transferencias internacionales? ¿Se cumplen las condiciones de transferencia de la Ley 81 de 2019? |
| **Seguridad** | ¿Medidas específicas para IA? Adversarial testing, detección de envenenamiento de datos |
| **Confidencialidad** | ¿Los prompts/inputs están protegidos? ¿Se loguean? ¿Quién accede? |
| **Indemnización** | ¿Cubre reclamaciones de propiedad intelectual por outputs generados? (Ej., contenido que infringe derecho de autor — Ley 64 de 2012) |
| **Terminación** | ¿Qué pasa con nuestros datos al terminar? ¿El proveedor retiene datos de entrenamiento? |

---

## Verificación de gobernanza y cumplimiento conexo

| Aspecto | Pregunta | Referencia |
|---|---|---|
| ¿El sistema está clasificado como alto riesgo? | Si sí, ¿el proveedor aplica controles de gestión de riesgos? | Marco interno / NIST AI RMF |
| ¿Se proporciona documentación técnica? | Necesaria para gobernanza y supervisión humana | Marco interno |
| ¿Hay mecanismo de logging? | Registro de eventos para trazabilidad | Marco interno |
| ¿Se informa a los usuarios de que interactúan con IA? | Obligación de transparencia (buena práctica) | Marco interno |
| ¿El acuerdo de tratamiento cubre el procesamiento por IA? | Protección de datos personales | Ley 81 de 2019 |

---

## Formato de salida

```markdown
# Revisión de proveedor de IA: [Nombre del proveedor]

**Herramienta / Servicio:** [nombre]
**Tipo:** [SaaS con IA / API de modelo / Herramienta on-premise]
**Fecha:** [fecha]
**Nuestro rol:** [Implementador / Proveedor downstream]

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

## Gobernanza y cumplimiento conexo

| Aspecto | Estado | Observación |
|---|---|---|
| Gobernanza de IA (marco interno / NIST) | [Conforme / Gaps / No evaluable] | [detalle] |
| Protección de datos (Ley 81 de 2019) | [Conforme / Gaps] | [detalle] |

---

## Redlines recomendados

[Lista de cambios a solicitar al proveedor]

---

## Si no aceptan

[Alternativas y fallbacks para cada punto bloqueante]
```

---

## Marco de referencia

- NIST AI Risk Management Framework; ISO/IEC 42001 (sistema de gestión de IA)
- Ley 81 de 2019 sobre protección de datos personales (tratamiento, transferencias); autoridad: ANTAI
- Ley 64 de 2012 sobre derecho de autor (propiedad intelectual de outputs)
- Reglamento Europeo de IA (Reglamento UE 2024/1689): solo como referencia comparada internacional

---

## Lo que este skill NO hace

- No negocia con el proveedor — genera la posición y los redlines.
- No audita técnicamente el modelo de IA — revisa las condiciones contractuales.
- No clasifica el sistema de IA — para eso, usar `/gobernanza-ia:triaje` primero.
