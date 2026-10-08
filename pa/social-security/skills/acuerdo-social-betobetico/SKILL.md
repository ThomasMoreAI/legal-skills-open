---
name: acuerdo-social-betobetico
title: Propósito
description: Redacta acuerdos sociales (junta de accionistas y junta directiva) en formato del despacho
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/societario/skills/acuerdo-social
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: social-security
language: es
---

## Propósito

Esta skill redacta acuerdos sociales para juntas de accionistas y juntas directivas conforme a la Ley 32 de 1927 y al formato del despacho. Cubre los tipos más frecuentes: nombramientos, remociones, aprobación de estados financieros, aumentos de capital y reformas al pacto social.

## Instrucciones

### Paso 1 — Identificar tipo de acuerdo

Determinar el tipo solicitado:

1. **Nombramiento** de director/dignatario.
2. **Remoción** de director/dignatario.
3. **Aprobación de estados financieros** y aplicación de utilidades.
4. **Aumento de capital** (en efectivo, en especie, capitalización de créditos).
5. **Reducción de capital**.
6. **Reforma del pacto social** (objeto social, domicilio, denominación, etc.).
7. **Disolución y liquidación**.
8. **Otros**: transformación, fusión, escisión, autorización de operaciones con partes relacionadas.

### Paso 2 — Recopilar datos necesarios

Solicitar al usuario los datos según el tipo:

- **Nombramiento**: nombre, cédula / pasaporte, cargo, duración, remuneración, tipo de órgano.
- **Estados financieros**: período fiscal, cifras clave, propuesta de aplicación de utilidades.
- **Aumento de capital**: importe, prima, forma de pago, derecho de suscripción preferente.
- **Reforma del pacto social**: cláusula(s) a reformar, redacción propuesta.

### Paso 3 — Verificar requisitos legales

Comprobar según tipo de sociedad (S.A. / S. de R.L.):

- **Quórum**: conforme al pacto social y a la Ley 32 de 1927.
- **Mayorías**: conforme al pacto social y a la Ley 32 de 1927.
- **Formalidades**: convocatoria, derecho de información, informe de la junta directiva.
- **Inscripción registral**: si el acuerdo requiere protocolización en escritura pública e inscripción en el Registro Público.

### Paso 4 — Redactar el acuerdo

Seguir la estructura estándar del despacho (o la de config si existe).

## Formato de salida

```markdown
## Acuerdo social — [Tipo]

**Sociedad:** [denominación completa]
**RUC:** [número]
**Órgano:** Junta de Accionistas / Junta Directiva
**Fecha:** [fecha de la sesión]
**Convocatoria:** [forma y fecha] / Reunión con renuncia a convocatoria

---

### Asistentes / Quórum

[Lista de asistentes con porcentaje de capital / miembros de la junta directiva presentes]
Quórum: [porcentaje]% — Cumple pacto social / Ley 32 de 1927: [SÍ/NO]

### Orden del día

[Puntos numerados]

### Acuerdos adoptados

**[Número]. [Título del acuerdo]**

[Texto del acuerdo con referencia normativa]

Votación: [a favor] / [en contra] / [abstenciones]
Mayoría requerida: pacto social / Ley 32 de 1927 — Cumplida: [SÍ/NO]

### Trámites posteriores

| Trámite | Plazo | Responsable | Estado |
|---------|-------|-------------|--------|
| Protocolización en escritura pública | [plazo] | [nombre] | Pendiente |
| Inscripción en el Registro Público | [plazo] [verificar] | [nombre] | Pendiente |
| Pago de tasa única anual | Anual (B/. 300; 15 jul o 15 ene — Código Fiscal, art. 318-A) | [nombre] | Pendiente |
```

## Referencias normativas

- **Ley 32 de 1927**: sociedades anónimas — junta directiva y dignatarios.
- **Ley 32 de 1927**: reforma del pacto social.
- **Ley 32 de 1927**: junta de accionistas — convocatoria, constitución y adopción de acuerdos.
- **Pacto social**: quórum y mayorías aplicables a cada tipo de acuerdo.
- **Ley 32 de 1927, art. 13**: derecho de suscripción preferente en el aumento de capital (de carácter dispositivo: el pacto social puede excluirlo). El aumento de capital es reforma del pacto social (arts. 21, 56 y ss.), con protocolización en escritura pública e inscripción en el Registro Público.
- **Código de Comercio de Panamá**: protocolización e inscripción de actos societarios.
- **Registro Público de Panamá**: inscripción de acuerdos sociales.

## Guardrails

- **NO** certifica la validez del acuerdo — el borrador requiere revisión del abogado idóneo y del notario.
- **NO** verifica la identidad de los asistentes ni la validez de la convocatoria.
- **NO** sustituye la escritura pública ni el acta notarial cuando sea preceptiva.
- **NO** inscribe ni gestiona trámites ante el Registro Público.
- **ESCALAR** si el acuerdo requiere mayorías reforzadas y los datos de quórum son insuficientes.
- **ESCALAR** si se trata de operaciones con partes relacionadas (conflicto de interés).
- **AVISAR** si el tipo de sociedad no está especificado (S.A. y S. de R.L. tienen regímenes distintos).
