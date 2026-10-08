---
name: politica-betobetico
title: Propósito
description: Redacta políticas laborales internas adaptadas a la convención colectiva y normativa aplicable
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/laboral/skills/politica
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: employment
language: es
---

## Propósito

Esta skill redacta políticas laborales internas para empresas panameñas, adaptándolas a la convención colectiva aplicable (cuando exista) y a la normativa vigente. Cada política sigue una estructura estándar e incluye las referencias legales obligatorias.

## Instrucciones

### Paso 1 — Identificar tipo de política

1. **Teletrabajo / trabajo a distancia** — Ley 126 de 2020.
2. **Uso de dispositivos digitales y datos personales** — Ley 81 de 2019 (protección de datos personales) [verificar].
3. **Prevención del hostigamiento y la discriminación** — Ley 7 de 2018.
4. **Igualdad y no discriminación** — Constitución y Código de Trabajo.
5. **Seguridad y salud en el trabajo / riesgos profesionales** — normativa de la CSS y del Código de Trabajo.
6. **Código de conducta / canal de denuncias** — buenas prácticas de cumplimiento; en sujetos obligados, alinear con la Ley 23 de 2015 (prevención de blanqueo) y la UAF [verificar].
7. **Reglamento interno de trabajo** — Código de Trabajo, aprobación por MITRADEL cuando aplique [verificar].
8. **Capacitación y desarrollo** — Código de Trabajo.

### Paso 2 — Cargar contexto

1. Leer la convención colectiva aplicable (si existe) desde configuración o documento proporcionado.
2. Identificar requisitos específicos de la convención que afecten a la política.
3. Determinar el tamaño de la empresa y su sector (puede activar obligaciones adicionales, p. ej. reglamento interno de trabajo o comités de seguridad e higiene) [verificar].

### Paso 3 — Redactar política

Estructura estándar:

1. **Objeto y ámbito de aplicación**: qué regula y a quién aplica.
2. **Marco normativo**: leyes y convención aplicables.
3. **Definiciones**: términos clave.
4. **Contenido sustantivo**: reglas, derechos y obligaciones.
5. **Procedimiento**: cómo se implementa y gestiona.
6. **Régimen sancionador**: consecuencias del incumplimiento (remisión a la convención, al reglamento interno de trabajo y al Código de Trabajo).
7. **Vigencia y revisión**: entrada en vigor y periodicidad de revisión.
8. **Anexos**: formularios, modelos de solicitud si aplica.

### Paso 4 — Verificar cumplimiento normativo

Comprobar que la política:
- Cumple los mínimos legales y de convenio.
- No contiene cláusulas abusivas o discriminatorias.
- Incluye las menciones obligatorias por ley.
- Respeta la negociación colectiva cuando sea preceptiva.

## Formato de salida

```markdown
## Política de [tipo]

**Empresa:** [denominación]
**Convención colectiva:** [nombre, si existe]
**Versión:** [número] — Fecha: [fecha]
**Aprobado por:** [pendiente de aprobación]

---

### 1. Objeto y ámbito de aplicación

[Texto de la política]

### 2. Marco normativo

- [Norma 1 con artículos]
- [Norma 2 con artículos]
- [Convención colectiva — cláusulas relevantes, si existe]

### 3. Definiciones

[Términos y definiciones]

### 4. [Contenido sustantivo según tipo]

[Cuerpo de la política]

### 5. Procedimiento

[Pasos de implementación]

### 6. Régimen sancionador

[Remisión a la convención colectiva, al reglamento interno de trabajo y a las causas disciplinarias del Código de Trabajo]

### 7. Vigencia y revisión

[Fecha de entrada en vigor y periodicidad de revisión]

---

**NOTA:** Este documento es un BORRADOR que requiere revisión jurídica,
consulta con la representación de los trabajadores (si procede), aprobación
de MITRADEL cuando la ley lo exija (p. ej. reglamento interno de trabajo) [verificar]
y aprobación de la dirección antes de su entrada en vigor.
```

## Referencias normativas principales

- **Ley 126 de 2020**: Teletrabajo.
- **Ley 81 de 2019**: Protección de datos personales (tratamiento de datos del trabajador); autoridad de control: ANTAI.
- **Ley 7 de 2018**: Prevención del hostigamiento, acoso y discriminación.
- **Código de Trabajo de Panamá**: reglamento interno de trabajo, jornada, causas disciplinarias [verificar].
- **Normativa de riesgos profesionales** administrada por la CSS (Ley 51 de 2005).
- **Ley 23 de 2015** y **UAF**: prevención de blanqueo (relevante para canales de denuncia en sujetos obligados).
- **MITRADEL**: aprobación y registro de reglamentos internos de trabajo cuando aplique [verificar].

## Guardrails

- **NO** sustituye la negociación colectiva cuando sea legalmente obligatoria.
- **NO** aprueba ni publica la política — genera un BORRADOR.
- **NO** implementa la política en sistemas de RRHH.
- **NO** redacta reglamentos internos de trabajo completos (requieren aprobación de MITRADEL cuando la ley lo exija) [verificar].
- **ESCALAR** si la política requiere consulta o negociación obligatoria con los trabajadores y estos no han participado.
- **ESCALAR** si la empresa supera umbrales que activen obligaciones adicionales (p. ej. reglamento interno de trabajo, comités de seguridad e higiene) [verificar].
- **AVISAR** si no se proporciona convención colectiva y las mejoras convencionales pueden ser relevantes.
