---
name: acuerdo-social
title: Propósito
description: Redacta acuerdos sociales (junta general y consejo de administración) en formato del despacho
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/societario/skills/acuerdo-social
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: en
---

## Propósito

Esta skill redacta acuerdos sociales para juntas generales y consejos de administración conforme a la LSC y al formato del despacho. Cubre los tipos más frecuentes: nombramientos, ceses, aprobación de cuentas, ampliaciones de capital y modificaciones estatutarias.

## Instrucciones

### Paso 1 — Identificar tipo de acuerdo

Determinar el tipo solicitado:

1. **Nombramiento** de administrador/consejero.
2. **Cese** de administrador/consejero.
3. **Aprobación de cuentas anuales** y aplicación de resultado.
4. **Ampliación de capital** (dineraria, no dineraria, compensación de créditos).
5. **Reducción de capital**.
6. **Modificación estatutaria** (objeto social, domicilio, denominación, etc.).
7. **Disolución y liquidación**.
8. **Otros**: transformación, fusión, escisión, autorización de operaciones vinculadas.

### Paso 2 — Recopilar datos necesarios

Solicitar al usuario los datos según el tipo:

- **Nombramiento**: nombre, DNI/NIF, cargo, duración, retribución, tipo de órgano.
- **Cuentas anuales**: ejercicio, cifras clave, propuesta de aplicación de resultado.
- **Ampliación**: importe, prima, forma de desembolso, derecho de suscripción preferente.
- **Modificación estatutaria**: artículo(s) a modificar, redacción propuesta.

### Paso 3 — Verificar requisitos legales

Comprobar según tipo de sociedad (SL/SA):

- **Quórum**: arts. 193-194 LSC (ordinario/reforzado).
- **Mayorías**: arts. 198-201 LSC (SL) / arts. 201-204 LSC (SA).
- **Formalidades**: convocatoria, derecho de información, informe de administradores.
- **Inscripción registral**: si el acuerdo requiere escritura pública e inscripción.

### Paso 4 — Redactar el acuerdo

Seguir la estructura estándar del despacho (o la de config si existe).

## Formato de salida

```markdown
## Acuerdo social — [Tipo]

**Sociedad:** [denominación completa]
**CIF:** [número]
**Órgano:** Junta General / Consejo de Administración
**Fecha:** [fecha de la sesión]
**Convocatoria:** [forma y fecha] / Junta Universal

---

### Asistentes / Quórum

[Lista de asistentes con porcentaje de capital / miembros del consejo presentes]
Quórum: [porcentaje]% — Cumple art. [X] LSC: [SÍ/NO]

### Orden del día

[Puntos numerados]

### Acuerdos adoptados

**[Número]. [Título del acuerdo]**

[Texto del acuerdo con referencia normativa]

Votación: [a favor] / [en contra] / [abstenciones]
Mayoría requerida: art. [X] LSC — Cumplida: [SÍ/NO]

### Trámites posteriores

| Trámite | Plazo | Responsable | Estado |
|---------|-------|-------------|--------|
| Escritura pública | [plazo] | [nombre] | Pendiente |
| Inscripción RM | 2 meses (art. 94 RRM) | [nombre] | Pendiente |
| Depósito de cuentas | 30 junio (art. 279 LSC) | [nombre] | Pendiente |
```

## Referencias normativas

- **LSC arts. 159-252**: Órgano de administración.
- **LSC arts. 285-345**: Modificaciones estatutarias.
- **LSC arts. 159-180**: Junta general — convocatoria, constitución, adopción de acuerdos.
- **LSC arts. 193-201**: Quórum y mayorías.
- **LSC arts. 308-315**: Ampliación de capital y derecho de suscripción preferente.
- **LSC arts. 160-161**: Competencias de la junta general.
- **RRM arts. 94-113**: Inscripción de acuerdos sociales.

## Guardrails

- **NO** certifica la validez del acuerdo — el borrador requiere revisión del letrado y del notario.
- **NO** verifica la identidad de los asistentes ni la validez de la convocatoria.
- **NO** sustituye el acta notarial cuando sea preceptiva.
- **NO** inscribe ni gestiona trámites registrales.
- **ESCALAR** si el acuerdo requiere mayorías reforzadas y los datos de quórum son insuficientes.
- **ESCALAR** si se trata de operaciones vinculadas (art. 190 LSC — conflicto de interés).
- **AVISAR** si el tipo de sociedad no está especificado (SL/SA tienen regímenes distintos).
