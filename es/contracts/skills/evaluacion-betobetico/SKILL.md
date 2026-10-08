---
name: evaluacion-betobetico
title: /evaluacion
description: Evaluación de impacto de IA — genera una evaluación de impacto completa para un sistema de IA, cubriendo clasificación de riesgo, derechos fundamentales y medidas de mitigación según el Reglamento de IA de la UE. Usar cuando el usuario diga "evaluación de impacto IA", "FRIA", "impacto en derechos fundamentales" o tras un triaje de alto riesgo.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/gobernanza-ia/skills/evaluacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
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

El Reglamento de IA exige que los deployers de sistemas de alto riesgo en determinados ámbitos realicen una evaluación de impacto en derechos fundamentales (art. 27 RIA) antes de poner el sistema en uso. Además, los proveedores de sistemas de alto riesgo deben implementar un sistema de gestión de riesgos (art. 9). Este skill genera la evaluación completa cubriendo ambos regímenes.

---

## Estructura de la evaluación

### 1. Descripción del sistema

| Campo | Contenido |
|---|---|
| **Nombre del sistema** | [nombre] |
| **Proveedor** | [nombre del proveedor] |
| **Versión** | [número de versión] |
| **Nuestro rol** | [Proveedor / Deployer / Ambos] |
| **Clasificación de riesgo** | [Resultado del triaje — art. y Anexo] |
| **Finalidad prevista** | [uso concreto que daremos al sistema] |
| **Ámbito de despliegue** | [dónde y para quién] |
| **Datos de entrada** | [qué datos consume el sistema] |
| **Datos de salida** | [qué produce: decisiones, recomendaciones, clasificaciones] |
| **Grado de autonomía** | [Totalmente autónomo / Decisión de apoyo / Humano en el bucle] |
| **Escala** | [Número estimado de personas afectadas] |

### 2. Evaluación de impacto en derechos fundamentales (art. 27 RIA)

Obligatoria para deployers de alto riesgo que sean organismos de derecho público o entidades privadas que presten servicios públicos, y en áreas de empleo, servicios esenciales (crédito, seguros, servicios sociales) y fuerzas de seguridad.

| Derecho fundamental | Impacto potencial | Probabilidad | Severidad | Medida de mitigación |
|---|---|---|---|---|
| **No discriminación** (art. 21 CDFUE) | [Ej., Sesgo algorítmico por género/raza/edad] | | | |
| **Igualdad de género** (art. 23 CDFUE) | | | | |
| **Dignidad humana** (art. 1 CDFUE) | | | | |
| **Protección de datos** (art. 8 CDFUE / RGPD) | [Ej., Tratamiento masivo de datos personales] | | | |
| **Vida privada** (art. 7 CDFUE) | | | | |
| **Libertad de expresión** (art. 11 CDFUE) | | | | |
| **Derecho a tutela judicial efectiva** (art. 47 CDFUE) | [Ej., Dificultad para impugnar decisiones automatizadas] | | | |
| **Derechos del niño** (art. 24 CDFUE) | [Si afecta a menores] | | | |
| **Derechos de personas con discapacidad** (art. 26 CDFUE) | | | | |
| **Acceso a servicios de interés económico general** (art. 36 CDFUE) | | | | |

### 3. Requisitos de alto riesgo (arts. 9-15 RIA)

Para cada requisito, evaluar el estado de cumplimiento:

| Requisito | Art. RIA | Estado | Gaps identificados | Medida propuesta |
|---|---|---|---|---|
| Sistema de gestión de riesgos | Art. 9 | | | |
| Gobernanza de datos | Art. 10 | | | |
| Documentación técnica | Art. 11 | | | |
| Registro de eventos (logging) | Art. 12 | | | |
| Transparencia e información | Art. 13 | | | |
| Supervisión humana | Art. 14 | | | |
| Exactitud, robustez, ciberseguridad | Art. 15 | | | |

### 4. Interacción con RGPD

Si el sistema trata datos personales (prácticamente siempre):

| Aspecto | Evaluación |
|---|---|
| **Base jurídica** | [art. 6 RGPD] |
| **¿Se requiere EIPD?** | [Probablemente sí — perfilado/decisiones automatizadas → art. 35 RGPD] |
| **Derecho a no ser objeto de decisiones automatizadas** | [art. 22 RGPD — ¿aplica? ¿excepciones?] |
| **Transparencia algorítmica** | [art. 13.2.f / 14.2.g RGPD — información sobre la lógica, importancia y consecuencias] |

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

## 2. Impacto en derechos fundamentales
[Tabla de derechos con impacto, probabilidad, severidad y mitigación]

## 3. Cumplimiento de requisitos de alto riesgo
[Tabla de requisitos arts. 9-15 con estado y gaps]

## 4. Interacción con RGPD
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

## Legislación de referencia

- Reglamento de IA (Reglamento UE 2024/1689) — arts. 9-15, 27
- Carta de los Derechos Fundamentales de la UE (CDFUE)
- RGPD arts. 22, 35 (decisiones automatizadas, EIPD)
- LOPDGDD art. 28 (obligaciones del responsable)

---

## Lo que este skill NO hace

- No audita técnicamente el sistema de IA (sesgo, robustez, exactitud) — identifica dónde hacerlo.
- No certifica el cumplimiento del Reglamento de IA — genera la evaluación para revisión.
- No revisa el contrato con el proveedor — para eso, usar `/gobernanza-ia:proveedor`.
