---
name: triaje-gobernanza-ia-betobetico
title: /triaje
description: Triaje de caso de uso de IA — clasifica un sistema de IA según los niveles de riesgo del Reglamento de IA de la UE (inaceptable, alto riesgo, limitado, mínimo). Comprueba contra el registro interno de sistemas de IA y emite las obligaciones aplicables. Usar cuando el usuario diga "vamos a usar IA para...", "¿qué riesgo tiene este sistema?", "nuevo caso de uso de IA", "triaje IA".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/gobernanza-ia/skills/triaje
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# /triaje

1. Cargar `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md` → registro de sistemas IA, sectores, umbrales.
2. Recopilar información del caso de uso.
3. Clasificar según el Reglamento de IA (Reglamento UE 2024/1689).
4. Identificar obligaciones aplicables.
5. Comprobar registro interno y emitir siguiente paso.

```
/gobernanza-ia:triaje
Queremos implementar un chatbot de atención al cliente con IA generativa
que responda consultas sobre productos financieros.
```

---

## Propósito

El Reglamento de IA de la UE establece un sistema de clasificación por niveles de riesgo que determina las obligaciones aplicables a cada sistema de IA. Clasificar correctamente un caso de uso es el primer paso obligatorio antes de desplegarlo. Una clasificación errónea puede suponer desde incumplimientos administrativos hasta sanciones de hasta el 7% del volumen de negocio global.

---

## Información necesaria

Antes de clasificar, recopilar:

1. **¿Qué hace el sistema?** (función concreta)
2. **¿Qué decisiones toma o asiste?** (autónomas / de apoyo)
3. **¿Sobre quién impacta?** (empleados, clientes, público general)
4. **¿En qué sector se despliega?** (financiero, sanitario, laboral, educativo, judicial...)
5. **¿Quién es el proveedor?** (propio / tercero)
6. **¿Cuál es nuestro rol?** (proveedor / deployer / distribuidor)
7. **¿Se usa para perfilado, scoring, biometría o decisiones automatizadas?**

---

## Clasificación por niveles de riesgo

### Nivel 1: Riesgo inaceptable (art. 5 RIA) — PROHIBIDO

Sistemas de IA cuyo uso está prohibido:

| Práctica prohibida | Art. 5 RIA |
|---|---|
| Técnicas subliminales, manipuladoras o engañosas que distorsionen el comportamiento | Art. 5.1.a |
| Explotación de vulnerabilidades (edad, discapacidad, situación social) | Art. 5.1.b |
| Scoring social por autoridades públicas con efectos perjudiciales desproporcionados | Art. 5.1.c |
| Evaluación de riesgo de delincuencia basada solo en perfilado o rasgos de personalidad | Art. 5.1.d |
| Creación o ampliación de BBDD de reconocimiento facial mediante scraping masivo | Art. 5.1.e |
| Inferencia de emociones en el lugar de trabajo o centros educativos (con excepciones) | Art. 5.1.f |
| Categorización biométrica para inferir datos sensibles (raza, opiniones políticas, orientación sexual...) | Art. 5.1.g |
| Identificación biométrica remota en tiempo real en espacios públicos por fuerzas de seguridad (con excepciones) | Art. 5.1.h |

**Si el caso de uso encaja aquí → BLOQUEO. No puede desplegarse.**

### Nivel 2: Alto riesgo (Anexo III RIA)

Sistemas incluidos en el Anexo III o que son componentes de seguridad de productos regulados (Anexo I):

| Área del Anexo III | Ejemplos |
|---|---|
| **Biometría** (salvo excepciones) | Identificación biométrica remota, categorización biométrica |
| **Infraestructuras críticas** | Gestión de tráfico, suministro de agua, gas, electricidad |
| **Educación y formación profesional** | Acceso a centros educativos, evaluación de estudiantes |
| **Empleo y gestión de trabajadores** | Selección, promoción, despido, asignación de tareas, supervisión |
| **Acceso a servicios esenciales** | Scoring crediticio, seguros, servicios sociales |
| **Fuerzas de seguridad** | Evaluación de riesgo de reincidencia, polígrafos |
| **Migración, asilo y control de fronteras** | Evaluación de solicitudes, detección de documentos falsos |
| **Administración de justicia y procesos democráticos** | Asistencia en investigación legal, influencia en voto |

**Obligaciones para sistemas de alto riesgo:**
- Sistema de gestión de riesgos (art. 9)
- Gobernanza de datos (art. 10)
- Documentación técnica (art. 11)
- Registro de eventos (art. 12)
- Transparencia e información a usuarios (art. 13)
- Supervisión humana (art. 14)
- Exactitud, robustez y ciberseguridad (art. 15)
- Evaluación de impacto en derechos fundamentales (art. 27 — para deployers)

### Nivel 3: Riesgo limitado — obligaciones de transparencia (art. 50)

| Sistema | Obligación |
|---|---|
| Chatbots y sistemas que interactúan con personas | Informar de que se está interactuando con IA |
| Sistemas de reconocimiento de emociones o categorización biométrica | Informar a las personas expuestas |
| Deep fakes / contenido generado por IA | Etiquetar como generado artificialmente |
| Contenido de texto generado por IA publicado para informar (noticias) | Etiquetar como generado por IA |

### Nivel 4: Riesgo mínimo

Todos los demás sistemas de IA. Sin obligaciones regulatorias específicas, pero se recomienda adherirse a códigos de conducta (art. 95 RIA).

---

## Formato de salida

```markdown
# Triaje de caso de uso de IA

**Sistema / Caso de uso:** [descripción]
**Fecha:** [fecha]
**Nuestro rol:** [proveedor / deployer / distribuidor]

---

## Clasificación

| Resultado | Nivel |
|---|---|
| **Nivel de riesgo** | [Inaceptable / Alto / Limitado / Mínimo] |
| **Base** | [Art. 5 / Anexo III punto X / Art. 50 / No clasificado] |

---

## Justificación

[Análisis de por qué se clasifica en este nivel, con referencia a los criterios aplicados]

---

## Obligaciones aplicables

| Obligación | Artículo RIA | Responsable | Estado |
|---|---|---|---|
| [Ej., Sistema de gestión de riesgos] | Art. 9 | [Proveedor] | [Pendiente] |
| [Ej., Evaluación de derechos fundamentales] | Art. 27 | [Deployer] | [Pendiente] |
| ... | ... | ... | ... |

---

## Registro interno

**¿Registrado en el inventario de sistemas IA?** [Sí / No — registrar]
**¿Registrado en la base de datos de la UE?** [Si procede — art. 49]

---

## Siguiente paso

1. **Si alto riesgo** → Ejecutar `/gobernanza-ia:evaluacion` para la evaluación de impacto.
2. **Si riesgo limitado** → Implementar obligaciones de transparencia.
3. **Si riesgo mínimo** → Documentar la clasificación y proceder.
4. **Si inaceptable** → BLOQUEO. No desplegar.
```

---

## Legislación de referencia

- Reglamento de IA (Reglamento UE 2024/1689) — arts. 5, 6, 9-15, 27, 50, 95, Anexos I y III
- Fechas de aplicación: prohibiciones desde febrero 2025; alto riesgo Anexo III desde agosto 2026; resto desde agosto 2025

---

## Lo que este skill NO hace

- No realiza la evaluación de impacto completa — para eso, usar `/gobernanza-ia:evaluacion`.
- No revisa contratos con proveedores de IA — para eso, usar `/gobernanza-ia:proveedor`.
- No certifica el cumplimiento del sistema — clasifica y lista obligaciones.
