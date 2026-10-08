---
name: politica-3142-betobetico
title: Propósito
description: Redacta políticas laborales internas adaptadas al convenio colectivo y normativa aplicable
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/laboral/skills/politica
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: employment
language: es
---

## Propósito

Esta skill redacta políticas laborales internas para empresas españolas, adaptándolas al convenio colectivo aplicable y a la normativa vigente. Cada política sigue una estructura estándar e incluye las referencias legales obligatorias.

## Instrucciones

### Paso 1 — Identificar tipo de política

1. **Teletrabajo / trabajo a distancia** — Ley 10/2021.
2. **Desconexión digital** — LOPDGDD art. 88.
3. **Prevención del acoso** — LO 3/2007 art. 48, RD 901/2020.
4. **Plan de igualdad** — LO 3/2007, RD 901/2020 (obligatorio > 50 trabajadores).
5. **Registro de jornada** — ET art. 34.9, RDL 8/2019.
6. **Código de conducta / canal de denuncias** — Ley 2/2023 (protección del informante).
7. **Uso de dispositivos digitales** — LOPDGDD arts. 87-91.
8. **Formación y desarrollo** — ET art. 23.

### Paso 2 — Cargar contexto

1. Leer convenio colectivo aplicable desde configuración o documento proporcionado.
2. Identificar requisitos específicos del convenio que afecten a la política.
3. Determinar tamaño de empresa (afecta a obligaciones: plan de igualdad, canal de denuncias).

### Paso 3 — Redactar política

Estructura estándar:

1. **Objeto y ámbito de aplicación**: qué regula y a quién aplica.
2. **Marco normativo**: leyes y convenio aplicables.
3. **Definiciones**: términos clave.
4. **Contenido sustantivo**: reglas, derechos y obligaciones.
5. **Procedimiento**: cómo se implementa y gestiona.
6. **Régimen sancionador**: consecuencias del incumplimiento (remisión al convenio/ET).
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
**Convenio colectivo:** [nombre]
**Versión:** [número] — Fecha: [fecha]
**Aprobado por:** [pendiente de aprobación]

---

### 1. Objeto y ámbito de aplicación

[Texto de la política]

### 2. Marco normativo

- [Norma 1 con artículos]
- [Norma 2 con artículos]
- [Convenio colectivo — artículos relevantes]

### 3. Definiciones

[Términos y definiciones]

### 4. [Contenido sustantivo según tipo]

[Cuerpo de la política]

### 5. Procedimiento

[Pasos de implementación]

### 6. Régimen sancionador

[Remisión a convenio y ET arts. 54, 58]

### 7. Vigencia y revisión

[Fecha de entrada en vigor y periodicidad de revisión]

---

**NOTA:** Este documento es un BORRADOR que requiere revisión jurídica,
negociación con la representación legal de los trabajadores (si procede)
y aprobación de la dirección antes de su entrada en vigor.
```

## Referencias normativas principales

- **Ley 10/2021**: Trabajo a distancia — acuerdo individual obligatorio.
- **LOPDGDD** (LO 3/2018) art. 88: Derecho a la desconexión digital.
- **LOPDGDD arts. 87-91**: Derechos digitales en el ámbito laboral.
- **LO 3/2007**: Igualdad efectiva — obligaciones empresariales.
- **RD 901/2020**: Planes de igualdad y su registro.
- **RD 902/2020**: Igualdad retributiva.
- **Ley 2/2023**: Protección del informante (canal de denuncias).
- **ET art. 34.9**: Registro de jornada.
- **ET art. 64**: Derechos de información y consulta de los representantes.

## Guardrails

- **NO** sustituye la negociación colectiva cuando sea legalmente obligatoria.
- **NO** aprueba ni publica la política — genera un BORRADOR.
- **NO** implementa la política en sistemas de RRHH.
- **NO** redacta planes de igualdad completos (requieren diagnóstico negociado).
- **ESCALAR** si la política requiere negociación obligatoria con representantes y estos no han participado.
- **ESCALAR** si la empresa supera umbrales que activen obligaciones adicionales (50, 100, 250 trabajadores).
- **AVISAR** si no se proporciona convenio colectivo y las mejoras convencionales pueden ser relevantes.
