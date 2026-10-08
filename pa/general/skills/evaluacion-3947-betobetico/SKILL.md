---
name: evaluacion-3947-betobetico
title: /evaluacion
description: Evaluación de impacto de IA — genera una evaluación de impacto completa para un sistema de IA, cubriendo clasificación de riesgo, derechos de las personas y medidas de mitigación según un marco de gobernanza por principios (Panamá no tiene ley de IA vinculante). Usar cuando el usuario diga "evaluación de impacto IA", "impacto en derechos fundamentales" o tras un triaje de alto riesgo.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/gobernanza-ia/skills/evaluacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: general
language: es
---

# /evaluacion

1. Cargar `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md` → registro de sistemas, formato house, proceso.
2. Verificar si existe triaje previo (`/gobernanza-ia:triaje`). Si no, ejecutar triaje primero.
3. Recopilar información detallada del sistema.
4. Generar la evaluación de impacto.
5. Evaluar medidas de mitigación.

```
/gobernanza-ia:evaluacion
Sistema de scoring crediticio automatizado para aprobación de préstamos
al consumo — clasificado como alto riesgo en triaje previo.
```

---

## Propósito

Panamá no cuenta con una ley de IA vinculante. Por buenas prácticas de gobernanza, los implementadores de sistemas de IA de alto riesgo deben realizar una evaluación de impacto sobre los derechos de las personas antes de poner el sistema en uso, y mantener un sistema de gestión de riesgos sobre el modelo (en línea con el NIST AI RMF y la ISO/IEC 42001). Cuando el sistema trate datos personales, aplican además las obligaciones de la Ley 81 de 2019 supervisada por la ANTAI. Este skill genera la evaluación completa cubriendo ambos planos: gobernanza de IA y protección de datos.

---

## Estructura de la evaluación

### 1. Descripción del sistema

| Campo | Contenido |
|---|---|
| **Nombre del sistema** | [nombre] |
| **Proveedor** | [nombre del proveedor] |
| **Versión** | [número de versión] |
| **Nuestro rol** | [Proveedor / Implementador / Ambos] |
| **Clasificación de riesgo** | [Resultado del triaje] |
| **Finalidad prevista** | [uso concreto que daremos al sistema] |
| **Ámbito de despliegue** | [dónde y para quién] |
| **Datos de entrada** | [qué datos consume el sistema] |
| **Datos de salida** | [qué produce: decisiones, recomendaciones, clasificaciones] |
| **Grado de autonomía** | [Totalmente autónomo / Decisión de apoyo / Humano en el bucle] |
| **Escala** | [Número estimado de personas afectadas] |

### 2. Evaluación de impacto sobre los derechos de las personas

Recomendada para implementadores de sistemas de alto riesgo, especialmente entidades que presten servicios públicos o esenciales, y en áreas de empleo, servicios esenciales (crédito, seguros, servicios sociales) y seguridad. La referencia normativa panameña directa es la protección de los derechos constitucionales y la Ley 81 de 2019 cuando hay tratamiento de datos personales.

| Derecho / valor protegido | Impacto potencial | Probabilidad | Severidad | Medida de mitigación |
|---|---|---|---|---|
| **No discriminación / igualdad** | [Ej., Sesgo algorítmico por género/raza/edad] | | | |
| **Igualdad de género** | | | | |
| **Dignidad humana** | | | | |
| **Protección de datos personales** (Ley 81 de 2019) | [Ej., Tratamiento masivo de datos personales] | | | |
| **Vida privada / intimidad** | | | | |
| **Libertad de expresión** | | | | |
| **Tutela judicial y debido proceso** | [Ej., Dificultad para impugnar decisiones automatizadas] | | | |
| **Derechos del niño** | [Si afecta a menores] | | | |
| **Derechos de personas con discapacidad** | | | | |
| **Acceso a servicios esenciales** | | | | |

### 3. Requisitos de control para alto riesgo (marco interno / NIST AI RMF / ISO 42001)

Para cada requisito, evaluar el estado de cumplimiento:

| Requisito | Referencia | Estado | Gaps identificados | Medida propuesta |
|---|---|---|---|---|
| Sistema de gestión de riesgos | NIST AI RMF / ISO 42001 | | | |
| Gobernanza de datos | Marco interno / Ley 81 de 2019 | | | |
| Documentación técnica | Marco interno | | | |
| Registro de eventos (logging) | Marco interno | | | |
| Transparencia e información | Marco interno | | | |
| Supervisión humana | Marco interno | | | |
| Exactitud, robustez, ciberseguridad | Marco interno | | | |

### 4. Interacción con la Ley de Protección de Datos Personales

Si el sistema trata datos personales (prácticamente siempre):

| Aspecto | Evaluación |
|---|---|
| **Base legal del tratamiento** | [consentimiento u otra base — Ley 81 de 2019] |
| **¿Se requiere evaluación de impacto de datos?** | [Probablemente sí — perfilado/decisiones automatizadas; valorar conforme a la Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021] |
| **Derechos del titular ante decisiones automatizadas** | [acceso, rectificación, oposición — Ley 81 de 2019] |
| **Transparencia algorítmica** | [información sobre la lógica, importancia y consecuencias del tratamiento] |

### 5. Medidas de mitigación

| Riesgo | Medida | Tipo | Responsable | Plazo |
|---|---|---|---|---|
| [Sesgo algorítmico] | [Auditoría de sesgo pre-despliegue + periódica] | Técnica + Organizativa | [Equipo IA + Legal] | [Pre-despliegue] |
| [Opacidad de decisiones] | [Explicabilidad: motivos de la decisión al afectado] | Técnica | [Proveedor] | [Pre-despliegue] |
| [Falta de supervisión humana] | [Humano en el bucle para decisiones de alto impacto] | Organizativa | [Operaciones] | [Pre-despliegue] |

---

## Formato de salida

```markdown
# Evaluación de impacto de sistema de IA

**Sistema:** [nombre]
**Proveedor:** [nombre]
**Clasificación de riesgo:** [nivel — referencia al triaje]
**Fecha:** [fecha]
**Autor:** [nombre / equipo]

---

## 1. Descripción del sistema
[Tabla descriptiva]

## 2. Impacto sobre los derechos de las personas
[Tabla de derechos con impacto, probabilidad, severidad y mitigación]

## 3. Cumplimiento de requisitos de control para alto riesgo
[Tabla de requisitos con estado y gaps]

## 4. Interacción con la Ley de Protección de Datos Personales
[Análisis de protección de datos]

## 5. Medidas de mitigación
[Tabla consolidada de medidas]

## 6. Conclusión
**Riesgo residual:** [Alto / Medio / Bajo]
**¿Puede desplegarse?** [Sí / Sí con condiciones / No]
**Condiciones:** [lista si aplica]

## 7. Plan de seguimiento
| Actividad | Frecuencia | Responsable |
|---|---|---|
| Auditoría de sesgo | [Semestral] | [Equipo IA] |
| Revisión de incidentes | [Continua] | [Operaciones] |
| Actualización de evaluación | [Anual o ante cambios] | [Legal + IA] |
```

---

## Marco de referencia

- Principios de la OCDE sobre IA y Recomendación de la UNESCO sobre la ética de la IA (referencia comparada)
- NIST AI Risk Management Framework; ISO/IEC 42001 (sistema de gestión de IA)
- Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 sobre protección de datos personales (decisiones automatizadas, evaluación de impacto); autoridad: ANTAI
- Reglamento Europeo de IA (Reglamento UE 2024/1689): solo como referencia comparada internacional, no aplicable en Panamá

---

## Lo que este skill NO hace

- No audita técnicamente el sistema de IA (sesgo, robustez, exactitud) — identifica dónde hacerlo.
- No certifica el cumplimiento de un marco — genera la evaluación para revisión.
- No revisa el contrato con el proveedor — para eso, usar `/gobernanza-ia:proveedor`.
