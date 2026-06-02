---
name: eipd
title: /eipd
description: Generador de Evaluación de Impacto en Protección de Datos (EIPD) — genera una EIPD en el formato house configurado. Evalúa si es obligatoria según art. 35 RGPD + lista AEPD, estructura el análisis de riesgos y propone medidas de mitigación. Usar cuando se plantee un nuevo tratamiento de datos, un cambio sustancial en uno existente, o el usuario diga "necesito una EIPD", "evaluación de impacto" o "¿hay que hacer EIPD?".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/privacidad/skills/eipd
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
---

# /eipd

1. Cargar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md` → formato house de EIPD, proceso, criterios.
2. Determinar si la EIPD es obligatoria (si hay duda, usar `/privacidad:triaje` primero).
3. Recopilar información del tratamiento (preguntar lo que falte).
4. Generar la EIPD en el formato configurado.
5. Evaluar si procede consulta previa a la AEPD (art. 36 RGPD).

```
/privacidad:eipd
Queremos implementar un sistema de reconocimiento facial para control de acceso
en las oficinas.
```

---

## Propósito

La EIPD es obligatoria cuando un tratamiento entraña alto riesgo para los derechos y libertades de las personas físicas. Es el documento más completo del sistema de accountability del RGPD y debe realizarse **antes** de iniciar el tratamiento. Este skill genera la EIPD completa siguiendo la estructura del art. 35.7 RGPD y las guías de la AEPD.

---

## Cuándo es obligatoria la EIPD

### Supuestos del art. 35.3 RGPD

- Evaluación sistemática y exhaustiva de aspectos personales basada en tratamiento automatizado, incluida la **elaboración de perfiles**, con efectos jurídicos o significativos
- Tratamiento a **gran escala** de categorías especiales de datos (art. 9) o datos de condenas penales (art. 10)
- **Observación sistemática** a gran escala de una zona de acceso público

### Lista obligatoria de la AEPD (2019)

La AEPD publicó una lista de tratamientos que requieren EIPD. Incluye, entre otros:
- Perfilado (evaluación o predicción de aspectos personales)
- Toma de decisiones automatizadas con efectos jurídicos
- Observación, geolocalización o control del interesado de forma sistemática
- Tratamiento de datos especialmente protegidos o de naturaleza muy personal
- Tratamiento de datos a gran escala
- Asociación o combinación de conjuntos de datos
- Datos de sujetos vulnerables (menores, empleados, pacientes)
- Uso innovador de tecnologías
- Transferencias internacionales a países sin nivel adecuado
- Tratamientos que impidan ejercer derechos o acceder a un servicio/contrato

**Regla de los dos criterios:** Si el tratamiento cumple dos o más de los criterios del Grupo de Trabajo del Artículo 29 (WP248 rev.01), generalmente requiere EIPD.

---

## Estructura de la EIPD (art. 35.7 RGPD)

### 1. Descripción sistemática del tratamiento

| Campo | Contenido |
|---|---|
| **Actividad de tratamiento** | [nombre del tratamiento] |
| **Responsable** | [identificación] |
| **Encargados** | [lista de encargados involucrados] |
| **Finalidad** | [propósito específico y concreto] |
| **Base jurídica** | [art. 6 RGPD — cuál y por qué] |
| **Categorías de datos** | [qué datos se tratan] |
| **Categorías de interesados** | [a quién afecta] |
| **Fuentes de datos** | [cómo se recogen] |
| **Flujo de datos** | [dónde se almacenan, quién accede, transferencias] |
| **Plazo de conservación** | [criterios o plazos concretos] |
| **Tecnología utilizada** | [sistemas, algoritmos, proveedores] |

### 2. Necesidad y proporcionalidad

- ¿El tratamiento es **necesario** para la finalidad declarada? ¿Hay alternativas menos intrusivas?
- ¿Los datos recogidos son **proporcionales** a la finalidad? ¿Se aplica minimización (art. 5.1.c)?
- ¿La base jurídica es **adecuada** y está correctamente identificada?
- ¿Se informa a los interesados (arts. 13-14 RGPD)?
- ¿Se garantizan los derechos de los interesados (arts. 15-22)?
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
- **Organizativas:** formación, políticas internas, contratos de confidencialidad, auditorías periódicas, DPO designado

---

## Evaluación de riesgo residual y consulta previa

Si tras aplicar las medidas de mitigación el **riesgo residual sigue siendo alto**, es obligatorio realizar **consulta previa a la AEPD** antes de iniciar el tratamiento (art. 36 RGPD).

La consulta debe incluir: responsabilidades del responsable y encargado, fines y medios del tratamiento, medidas para proteger derechos, datos de contacto del DPO, y la propia EIPD.

La AEPD dispone de **8 semanas** (prorrogables 6 semanas más) para responder.

---

## Formato de salida

```markdown
# Evaluación de Impacto en Protección de Datos (EIPD)

**Tratamiento:** [nombre]
**Responsable:** [empresa]
**Fecha:** [fecha]
**Versión:** [número]
**Autor:** [nombre / equipo]
**DPO consultado:** [Sí/No — fecha]

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
[¿Procede consulta previa a la AEPD? Sí/No — justificación]

## 6. Plan de acción
| Medida | Responsable | Plazo | Estado |
|---|---|---|---|
```

---

## Legislación de referencia

- RGPD art. 35 (evaluación de impacto relativa a la protección de datos)
- RGPD art. 36 (consulta previa)
- LOPDGDD art. 28 (obligaciones generales del responsable)
- Lista de tratamientos que requieren EIPD (AEPD, 2019)
- Guía práctica para las evaluaciones de impacto de la AEPD
- Directrices del CEPD (WP248 rev.01) sobre EIPD

---

## Lo que este skill NO hace

- No sustituye el juicio del DPO — la EIPD requiere su informe (art. 35.2 RGPD).
- No realiza la consulta previa a la AEPD — señala cuándo es necesaria.
- No evalúa medidas de seguridad técnicas en detalle — eso es responsabilidad del equipo de seguridad.
