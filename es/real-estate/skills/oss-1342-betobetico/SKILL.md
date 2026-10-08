---
name: oss-1342-betobetico
title: Propósito
description: Clasifica licencias de software de código abierto y detecta incompatibilidades con el modelo de distribución
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/propiedad-intelectual/skills/oss
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

## Propósito

Esta skill analiza las licencias de software de código abierto (OSS) utilizadas en un proyecto y las clasifica según su nivel de copyleft. Detecta incompatibilidades con el modelo de distribución o explotación de la empresa y señala riesgos de cumplimiento.

## Instrucciones

### Paso 1 — Obtener inventario de dependencias

1. Leer el listado de dependencias proporcionado (package.json, pom.xml, requirements.txt, SBOM, o listado manual).
2. Identificar la licencia de cada componente.
3. Si la licencia no está clara, marcarlo como "licencia desconocida" — riesgo por defecto ALTO.

### Paso 2 — Clasificar licencias

| Categoría | Licencias | Riesgo de copyleft |
|-----------|-----------|-------------------|
| **Permisiva** | MIT, BSD-2, BSD-3, Apache 2.0, ISC, Unlicense | Bajo — permite uso comercial y propietario |
| **Copyleft débil** | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-2.0 | Medio — copyleft limitado al componente |
| **Copyleft fuerte** | GPL-2.0, GPL-3.0, AGPL-3.0 | Alto — extiende copyleft a obra derivada |
| **No libre / Propietaria** | Licencias comerciales, SSPL, BUSL | Requiere análisis individual |

### Paso 3 — Evaluar contra modelo de distribución

Modelos de distribución de la empresa:

- **SaaS / cloud**: AGPL es el riesgo principal (extiende copyleft a uso en red).
- **Distribución binaria**: GPL obliga a ofrecer código fuente.
- **Biblioteca/SDK**: LGPL permite linkado dinámico; GPL no.
- **Uso interno**: la mayoría de licencias OSS no imponen obligaciones sin distribución.

### Paso 4 — Detectar incompatibilidades

- GPL-2.0 y Apache-2.0 son incompatibles (cláusula de patentes).
- GPL-2.0-only y GPL-3.0-only son incompatibles entre sí.
- Licencias con cláusula de atribución: verificar que se cumple.
- Licencias con restricción de uso (BUSL, Commons Clause): no son OSS.

## Formato de salida

```markdown
## Revisión de licencias OSS

**Proyecto:** [nombre]
**Modelo de distribución:** [SaaS/binaria/biblioteca/interno]
**Fecha del análisis:** [fecha]
**Dependencias analizadas:** [número]

### Resumen

| Categoría | Número | Porcentaje |
|-----------|--------|------------|
| Permisiva | [n] | [%] |
| Copyleft débil | [n] | [%] |
| Copyleft fuerte | [n] | [%] |
| Desconocida | [n] | [%] |

### Incompatibilidades detectadas

| Componente | Licencia | Problema | Severidad | Acción recomendada |
|------------|----------|----------|-----------|-------------------|
| [nombre] | [licencia] | [descripción] | [ALTA/MEDIA/BAJA] | [acción] |

### Inventario completo

| Componente | Versión | Licencia | Categoría | Compatible | Notas |
|------------|---------|----------|-----------|------------|-------|
| [nombre] | [ver] | [licencia] | [cat] | [SÍ/NO/?] | [nota] |

### Obligaciones de cumplimiento

[Lista de acciones necesarias: atribución, oferta de código fuente, etc.]
```

## Referencias normativas

- **LPI** (RDL 1/1996): arts. 95-104 (protección de programas de ordenador).
- **LPI art. 99**: Cesión de derechos de explotación de software.
- **LPI art. 100**: Límites a los derechos — copia de seguridad, interoperabilidad.
- **Directiva 2009/24/CE**: Protección jurídica de programas de ordenador.
- **Directiva (UE) 2019/790**: Derechos de autor en el mercado único digital.

## Guardrails

- **NO** proporciona asesoramiento jurídico vinculante sobre cumplimiento de licencias.
- **NO** modifica el código fuente ni elimina dependencias.
- **NO** contacta con titulares de derechos para solicitar licencias.
- **NO** determina con certeza si un uso concreto constituye "obra derivada" — eso requiere análisis jurídico especializado.
- **ESCALAR** si se detectan componentes AGPL en proyecto SaaS sin política de cumplimiento.
- **ESCALAR** si hay dependencias con licencia desconocida en componentes críticos.
- **AVISAR** si el modelo de distribución no está claro y afecta al análisis.
