---
name: triaje-gobernanza-ia-3208-betobetico
title: /triaje
description: Triaje de caso de uso de IA — clasifica un sistema de IA por niveles de riesgo (inaceptable, alto riesgo, limitado, mínimo) según un marco de referencia por principios, dado que Panamá no cuenta con ley de IA vinculante. Comprueba contra el registro interno de sistemas de IA y emite las obligaciones aplicables. Usar cuando el usuario diga "vamos a usar IA para...", "¿qué riesgo tiene este sistema?", "nuevo caso de uso de IA", "triaje IA".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/gobernanza-ia/skills/triaje
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: general
language: es
---

# /triaje

1. Cargar `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md` → registro de sistemas IA, sectores, umbrales.
2. Recopilar información del caso de uso.
3. Clasificar según el marco interno de referencia por principios.
4. Identificar obligaciones aplicables.
5. Comprobar registro interno y emitir siguiente paso.

```
/gobernanza-ia:triaje
Queremos implementar un chatbot de atención al cliente con IA generativa
que responda consultas sobre productos financieros.
```

---

## Propósito

**Panamá no cuenta con una ley de IA vinculante.** Este triaje aplica un sistema de clasificación por niveles de riesgo basado en principios y marcos internacionales de referencia (OCDE, UNESCO, NIST AI RMF, ISO/IEC 42001), adoptado como política interna de gobernanza. Clasificar correctamente un caso de uso es el primer paso antes de desplegarlo: permite dimensionar controles, transparencia y supervisión humana, y verificar las obligaciones panameñas conexas (sobre todo protección de datos personales, Ley 81 de 2019). El Reglamento Europeo de IA se utiliza únicamente como referencia comparada de criterios, no como norma aplicable.

---

## Información necesaria

Antes de clasificar, recopilar:

1. **¿Qué hace el sistema?** (función concreta)
2. **¿Qué decisiones toma o asiste?** (autónomas / de apoyo)
3. **¿Sobre quién impacta?** (empleados, clientes, público general)
4. **¿En qué sector se despliega?** (financiero, sanitario, laboral, educativo, judicial...)
5. **¿Quién es el proveedor?** (propio / tercero)
6. **¿Cuál es nuestro rol?** (proveedor / implementador / distribuidor)
7. **¿Se usa para perfilado, scoring, biometría o decisiones automatizadas?**

---

## Clasificación por niveles de riesgo (marco interno de referencia)

### Nivel 1: Riesgo inaceptable — VEDADO por política interna

Prácticas que el marco interno de gobernanza considera inadmisibles (en línea con los principios de la OCDE y la UNESCO):

| Práctica inadmisible | Fundamento del marco de referencia |
|---|---|
| Técnicas subliminales, manipuladoras o engañosas que distorsionen el comportamiento | Principio de respeto a la autonomía |
| Explotación de vulnerabilidades (edad, discapacidad, situación social) | Principio de no daño y equidad |
| Scoring social por entidades con efectos perjudiciales desproporcionados | Principio de equidad y no discriminación |
| Evaluación de riesgo de delincuencia basada solo en perfilado o rasgos de personalidad | Principio de no discriminación |
| Creación o ampliación de BBDD de reconocimiento facial mediante scraping masivo | Protección de datos personales (Ley 81 de 2019) |
| Inferencia de emociones en el lugar de trabajo o centros educativos | Principio de dignidad y privacidad |
| Categorización biométrica para inferir datos sensibles (raza, opiniones políticas, orientación sexual...) | Datos sensibles (Ley 81 de 2019) |
| Identificación biométrica remota masiva en espacios públicos sin base legal | Privacidad y debido proceso |

**Si el caso de uso encaja aquí → BLOQUEO por política interna. No debe desplegarse.**

### Nivel 2: Alto riesgo

Sistemas con impacto significativo sobre derechos, seguridad o acceso a servicios esenciales:

| Área de alto riesgo | Ejemplos |
|---|---|
| **Biometría** (salvo excepciones) | Identificación biométrica remota, categorización biométrica |
| **Infraestructuras críticas** | Gestión de tráfico, suministro de agua, gas, electricidad |
| **Educación y formación profesional** | Acceso a centros educativos, evaluación de estudiantes |
| **Empleo y gestión de trabajadores** | Selección, promoción, despido, asignación de tareas, supervisión |
| **Acceso a servicios esenciales** | Scoring crediticio, seguros, servicios sociales |
| **Seguridad** | Evaluación de riesgo de reincidencia, polígrafos |
| **Migración, asilo y control de fronteras** | Evaluación de solicitudes, detección de documentos falsos |
| **Administración de justicia y procesos democráticos** | Asistencia en investigación legal, influencia en voto |

**Controles recomendados para sistemas de alto riesgo (marco interno basado en NIST AI RMF / ISO 42001):**
- Sistema de gestión de riesgos de IA
- Gobernanza y calidad de los datos
- Documentación técnica del sistema
- Registro de eventos (logging)
- Transparencia e información a usuarios
- Supervisión humana
- Exactitud, robustez y ciberseguridad
- Evaluación de impacto sobre los derechos de las personas (para el implementador)

### Nivel 3: Riesgo limitado — obligaciones de transparencia

| Sistema | Obligación |
|---|---|
| Chatbots y sistemas que interactúan con personas | Informar de que se está interactuando con IA |
| Sistemas de reconocimiento de emociones o categorización biométrica | Informar a las personas expuestas |
| Deep fakes / contenido generado por IA | Etiquetar como generado artificialmente |
| Contenido de texto generado por IA publicado para informar (noticias) | Etiquetar como generado por IA |

### Nivel 4: Riesgo mínimo

Todos los demás sistemas de IA. Sin controles específicos exigidos por el marco interno, pero se recomienda adherirse a códigos de conducta voluntarios.

---

## Formato de salida

```markdown
# Triaje de caso de uso de IA

**Sistema / Caso de uso:** [descripción]
**Fecha:** [fecha]
**Nuestro rol:** [proveedor / implementador / distribuidor]

---

## Clasificación

| Resultado | Nivel |
|---|---|
| **Nivel de riesgo** | [Inaceptable / Alto / Limitado / Mínimo] |
| **Base** | [criterio del marco de referencia aplicado / No clasificado] |

---

## Justificación

[Análisis de por qué se clasifica en este nivel, con referencia a los criterios aplicados]

---

## Obligaciones y controles aplicables

| Obligación / Control | Fuente | Responsable | Estado |
|---|---|---|---|
| [Ej., Sistema de gestión de riesgos] | [Marco interno / NIST AI RMF] | [Proveedor] | [Pendiente] |
| [Ej., Evaluación de impacto sobre derechos] | [Marco interno] | [Implementador] | [Pendiente] |
| [Ej., Base legal y derechos del titular] | [Ley 81 de 2019] | [Oficial de datos] | [Pendiente] |
| ... | ... | ... | ... |

---

## Registro interno

**¿Registrado en el inventario de sistemas IA?** [Sí / No — registrar]
**¿Requiere notificación a la ANTAI por tratamiento de datos personales?** [Si procede — Ley 81 de 2019]

---

## Siguiente paso

1. **Si alto riesgo** → Ejecutar `/gobernanza-ia:evaluacion` para la evaluación de impacto.
2. **Si riesgo limitado** → Implementar obligaciones de transparencia.
3. **Si riesgo mínimo** → Documentar la clasificación y proceder.
4. **Si inaceptable** → BLOQUEO por política interna. No desplegar.
```

---

## Marco de referencia

- Principios de la OCDE sobre IA y Recomendación de la UNESCO sobre la ética de la IA
- NIST AI Risk Management Framework; ISO/IEC 42001 (sistema de gestión de IA)
- Ley 81 de 2019 sobre protección de datos personales (decisiones automatizadas, datos sensibles); autoridad: ANTAI
- Reglamento Europeo de IA (Reglamento UE 2024/1689): solo como referencia comparada internacional, no aplicable en Panamá
- *Nota: Panamá no tiene ley de IA vinculante; los plazos y categorías son criterios de gobernanza interna, no obligaciones legales directas.*

---

## Lo que este skill NO hace

- No realiza la evaluación de impacto completa — para eso, usar `/gobernanza-ia:evaluacion`.
- No revisa contratos con proveedores de IA — para eso, usar `/gobernanza-ia:proveedor`.
- No certifica el cumplimiento del sistema — clasifica y lista obligaciones.
