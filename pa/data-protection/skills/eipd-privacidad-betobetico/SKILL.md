---
name: eipd-privacidad-betobetico
title: /eipd
description: Generador de Evaluación de Impacto en Protección de Datos (EIPD) — genera una EIPD en el formato house configurado. Evalúa si es obligatoria según la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021, estructura el análisis de riesgos y propone medidas de mitigación. Usar cuando se plantee un nuevo tratamiento de datos, un cambio sustancial en uno existente, o el usuario diga "necesito una EIPD", "evaluación de impacto" o "¿hay que hacer EIPD?".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/privacidad/skills/eipd
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: data-protection
language: es
---

# /eipd

1. Cargar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md` → formato house de EIPD, proceso, criterios.
2. Determinar si conviene una EIPD (buena práctica voluntaria, art. 8 de la Ley 81 de 2019; obligatoria solo si la ANTAI la ordena, art. 41 del Decreto Ejecutivo 285 de 2021). Si hay duda, usar `/privacidad:triaje` primero.
3. Recopilar información del tratamiento (preguntar lo que falte).
4. Generar la EIPD en el formato configurado.

```
/privacidad:eipd
Queremos implementar un sistema de reconocimiento facial para control de acceso
en las oficinas.
```

---

## Propósito

En Panamá la EIPD está definida (Decreto Ejecutivo 285 de 2021, art. 1.9) pero **NO es obligatoria con carácter general** para todo tratamiento de alto riesgo (no rige el modelo del art. 35 del RGPD). Es una **buena práctica voluntaria** del responsable (art. 8 de la Ley 81 de 2019) y **solo deviene exigible si la ANTAI la ORDENA**, en función de la gravedad del riesgo o la novedad tecnológica (art. 41 del Decreto Ejecutivo 285 de 2021). Este skill genera la EIPD completa siguiendo la Ley 81 de 2019 y su Decreto Ejecutivo 285 de 2021.

---

## Cuándo conviene la EIPD

No hay una lista cerrada de "supuestos de alto riesgo" que obliguen a EIPD. El Decreto Ejecutivo 285 de 2021 contiene **9 factores de evaluación del riesgo (art. 36)** y los criterios para que la ANTAI ordene una EIPD (**art. 41**: gravedad del riesgo y novedad tecnológica).

### Situaciones a valorar (factores de riesgo del art. 36 del Decreto Ejecutivo 285 de 2021)

- Evaluación sistemática y exhaustiva de aspectos personales basada en tratamiento automatizado, incluida la **elaboración de perfiles**, con efectos jurídicos o significativos
- Tratamiento a **gran escala** de datos sensibles
- **Observación sistemática** a gran escala de una zona de acceso público

### Tratamientos de mayor riesgo a considerar

Como criterio orientativo, suelen aconsejar una evaluación de impacto, entre otros:
- Perfilado (evaluación o predicción de aspectos personales)
- Toma de decisiones automatizadas con efectos jurídicos
- Observación, geolocalización o control del titular de forma sistemática
- Tratamiento de datos sensibles o de naturaleza muy personal
- Tratamiento de datos a gran escala
- Asociación o combinación de conjuntos de datos
- Datos de sujetos vulnerables (menores, empleados, pacientes)
- Uso innovador de tecnologías
- Transferencias internacionales a países sin nivel adecuado de protección
- Tratamientos que impidan ejercer derechos o acceder a un servicio/contrato

**Regla de los dos criterios:** Si el tratamiento cumple dos o más de estos criterios de alto riesgo, generalmente conviene realizar la evaluación de impacto. (Criterio internacional orientativo, no vinculante en Panamá.) [verificar]

---

## Estructura de la EIPD (Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021)

### 1. Descripción sistemática del tratamiento

| Campo | Contenido |
|---|---|
| **Actividad de tratamiento** | [nombre del tratamiento] |
| **Responsable** | [identificación] |
| **Encargados** | [lista de encargados involucrados] |
| **Finalidad** | [propósito específico y concreto] |
| **Base de licitud** | [Ley 81 de 2019 — cuál y por qué] |
| **Categorías de datos** | [qué datos se tratan] |
| **Categorías de titulares** | [a quién afecta] |
| **Fuentes de datos** | [cómo se recogen] |
| **Flujo de datos** | [dónde se almacenan, quién accede, transferencias] |
| **Plazo de conservación** | [criterios o plazos concretos] |
| **Tecnología utilizada** | [sistemas, algoritmos, proveedores] |

### 2. Necesidad y proporcionalidad

- ¿El tratamiento es **necesario** para la finalidad declarada? ¿Hay alternativas menos intrusivas?
- ¿Los datos recogidos son **proporcionales** a la finalidad? ¿Se aplica el principio de minimización (Ley 81 de 2019)?
- ¿La base de licitud es **adecuada** y está correctamente identificada?
- ¿Se informa a los titulares (deber de información de la Ley 81 de 2019)?
- ¿Se garantizan los derechos del titular (acceso, rectificación, cancelación/supresión, oposición, portabilidad)?
- ¿Existe mecanismo de limitación de conservación?

### 3. Identificación y evaluación de riesgos

Para cada riesgo identificado:

| Riesgo | Descripción | Probabilidad | Impacto | Nivel | Derechos afectados |
|---|---|---|---|---|---|
| [Ej., Acceso no autorizado] | [Detalle] | [Alta/Media/Baja] | [Alto/Medio/Bajo] | [Valor] | [Arts. afectados] |
| [Ej., Discriminación por perfilado] | [Detalle] | | | | |
| [Ej., Pérdida de datos] | [Detalle] | | | | |

Categorías de riesgo a evaluar:
- Acceso ilegítimo a datos
- Modificación no autorizada
- Pérdida de datos
- Discriminación
- Usurpación de identidad
- Pérdida de confidencialidad
- Limitación de derechos
- Perjuicio económico o social

### 4. Medidas de mitigación

Para cada riesgo identificado, proponer medidas concretas:

| Riesgo | Medida propuesta | Tipo | Riesgo residual |
|---|---|---|---|
| [Riesgo] | [Medida técnica u organizativa] | [Técnica/Organizativa] | [Alto/Medio/Bajo] |

Medidas habituales:
- **Técnicas:** cifrado, seudonimización, control de acceso, logs de auditoría, backups
- **Organizativas:** formación, políticas internas, contratos de confidencialidad, auditorías periódicas, encargado de protección de datos designado

---

## Evaluación de riesgo residual

Si tras aplicar las medidas de mitigación el **riesgo residual sigue siendo alto**, documéntalo y refuerza las medidas. En Panamá **NO existe** la figura de "consulta previa" a la ANTAI del art. 36 del RGPD: ni la Ley 81 de 2019 ni el Decreto Ejecutivo 285 de 2021 la prevén. Lo que sí puede ocurrir es que la **ANTAI ordene la realización de una EIPD** en función de la gravedad del riesgo o la novedad tecnológica (art. 41 del Decreto Ejecutivo 285 de 2021).

---

## Formato de salida

```markdown
# Evaluación de Impacto en Protección de Datos (EIPD)

**Tratamiento:** [nombre]
**Responsable:** [empresa]
**Fecha:** [fecha]
**Versión:** [número]
**Autor:** [nombre / equipo]
**Encargado de protección de datos consultado:** [Sí/No — fecha]

---

## 1. Descripción del tratamiento
[Tabla descriptiva completa]

## 2. Necesidad y proporcionalidad
[Análisis punto por punto]

## 3. Riesgos identificados
[Tabla de riesgos con probabilidad, impacto y nivel]

## 4. Medidas de mitigación
[Tabla de medidas con riesgo residual]

## 5. Conclusión
[Riesgo residual global: alto/medio/bajo]
[Medidas adicionales si el riesgo residual sigue siendo alto — recordar que la ANTAI puede ordenar la EIPD (art. 41 del Decreto Ejecutivo 285 de 2021); en Panamá no existe la "consulta previa" del RGPD]

## 6. Plan de acción
| Medida | Responsable | Plazo | Estado |
|---|---|---|---|
```

---

## Legislación de referencia

- Ley 81 de 2019, art. 8 — la EIPD es una buena práctica voluntaria del responsable
- Decreto Ejecutivo 285 de 2021 — reglamento de la Ley 81 de 2019 (art. 1.9: definición de EIPD; art. 36: factores de evaluación del riesgo; art. 41: la ANTAI puede ordenar la EIPD)
- Guías y resoluciones de la ANTAI sobre evaluaciones de impacto
- Referencia comparada (no vinculante en Panamá): directrices del CEPD (WP248 rev.01) sobre EIPD, como criterio internacional orientativo

---

## Lo que este skill NO hace

- No sustituye el juicio del encargado de protección de datos — la EIPD requiere su valoración.
- No tramita consultas previas a la ANTAI (esa figura del RGPD no existe en Panamá); señala cuándo la ANTAI podría ordenar una EIPD (art. 41 del Decreto Ejecutivo 285 de 2021).
- No evalúa medidas de seguridad técnicas en detalle — eso es responsabilidad del equipo de seguridad.
