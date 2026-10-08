---
name: constitucion-4102-betobetico
title: /constitucion
description: Checklist completo para la constitución de una sociedad en Panamá (S.A. o S. de R.L.), desde la verificación de denominación hasta el alta ante la DGI. Genera borradores de pacto social y estructura de pacto de accionistas. Usar cuando el usuario dice "constituir una sociedad", "crear una empresa", "montar una S.A.", "sociedad anónima", "S. de R.L.", "pacto social", o necesita el proceso de constitución paso a paso.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/startups/skills/constitucion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: corporate
language: es
---

# /constitucion

1. Leer `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` — perfil de práctica.
2. Recopilar datos de la sociedad a constituir.
3. Generar checklist con pasos y plazos.
4. Producir borradores de pacto social y estructura de pacto de accionistas.

---

## Propósito

Guiar paso a paso la constitución de una sociedad panameña (S.A. o S. de R.L.), con checklist de trámites, borradores de pacto social básico y estructura de pacto de accionistas. El skill cubre la constitución estándar — señalar cuándo conviene una S. de R.L. en lugar de una S.A. y viceversa.

## Elección de forma jurídica

- **Sociedad Anónima (S.A.) — Ley 32 de 1927.** La más utilizada en Panamá. Acciones, junta de accionistas, junta directiva (mínimo 3 directores: presidente, secretario y tesorero) [verificar]. Requiere agente residente (abogado o firma idónea).
- **Sociedad de Responsabilidad Limitada (S. de R.L.) — Ley 4 de 2009.** Cuotas de participación en lugar de acciones. Estructura más sencilla; suele preferirse para vehículos con pocos socios o por motivos de tratamiento fiscal en el extranjero.
- **Fundación de Interés Privado — Ley 25 de 1995.** No es una sociedad mercantil, pero es un vehículo habitual en Panamá para tenencia patrimonial y planificación; mencionarlo solo si encaja con el objetivo del usuario.

## Datos necesarios

- **Denominación social** — hasta 5 opciones para verificar disponibilidad. La S.A. debe incluir "Sociedad Anónima", "S.A." o "Inc."/"Corp." [verificar].
- **Socios fundadores / accionistas** — nombres, cédula o pasaporte, porcentaje de participación.
- **Capital social** — la Ley 32 de 1927 no exige un mínimo desembolsado; es habitual un capital autorizado de USD 10,000 dividido en 100 acciones de USD 100 [verificar].
- **Objeto social** — actividad o actividades (en Panamá puede redactarse de forma amplia, incluso "cualquier acto lícito de comercio").
- **Domicilio social** — dirección en Panamá.
- **Junta directiva / administración** — directores y dignatarios (S.A.) o administradores (S. de R.L.).
- **Agente residente** — abogado o firma de abogados idónea (obligatorio para la S.A.).

## Checklist de constitución

| Paso | Trámite | Dónde | Plazo/Coste orientativo | Estado |
|---|---|---|---|---|
| 1 | Verificación de disponibilidad de denominación | Registro Público de Panamá (en línea) | 1-2 días / sin coste relevante [verificar] | [ ] |
| 2 | Designación de agente residente | Abogado / firma idónea | Inmediato | [ ] |
| 3 | Redacción del pacto social | Abogado / notario | Variable | [ ] |
| 4 | Protocolización del pacto social en escritura pública | Notaría | 1-2 días / honorarios notariales [verificar] | [ ] |
| 5 | Inscripción en el Registro Público de Panamá | Registro Público | 2-5 días hábiles / tasa de registro según capital [verificar] | [ ] |
| 6 | Obtención del RUC y NIT | DGI (Dirección General de Ingresos) | Tras inscripción | [ ] |
| 7 | Aviso de Operación (si ejerce comercio en Panamá) | Panamá Emprende / MICI | Antes de iniciar actividad / tasa anual [verificar] | [ ] |
| 8 | Apertura de cuenta bancaria de la sociedad | Entidad bancaria | Variable (KYC del banco) | [ ] |
| 9 | Pago de la tasa única anual de la sociedad | DGI | Anual / USD 300 aprox. [verificar] | [ ] |
| 10 | Inscripción patronal en la CSS (si contrata personal) | Caja de Seguro Social | Antes de contratar trabajadores | [ ] |
| 11 | Registro de beneficiario final | Registro de beneficiarios finales (a través del agente residente) | Según plazo legal [verificar] | [ ] |
| 12 | Licencias/permisos sectoriales según actividad | Municipio / entidad sectorial | Variable | [ ] |

## Pacto social — Estructura base

```
PACTO SOCIAL DE [DENOMINACIÓN SOCIAL], S.A.

CLÁUSULA PRIMERA. Denominación: [nombre], Sociedad Anónima.
CLÁUSULA SEGUNDA. Objeto social: [actividades — redacción amplia; en Panamá se admite "cualquier acto lícito de comercio"].
CLÁUSULA TERCERA. Domicilio: [dirección en Panamá]; podrá establecer sucursales dentro o fuera de la República.
CLÁUSULA CUARTA. Duración: perpetua.
CLÁUSULA QUINTA. Capital social: [importe] USD, dividido en [N] acciones de [valor] USD cada una.
  - Clases de acciones: [comunes / preferidas; nominativas o al portador según corresponda — verificar restricciones vigentes].
CLÁUSULA SEXTA. Junta directiva: mínimo 3 directores; dignatarios presidente, secretario y tesorero [verificar].
CLÁUSULA SÉPTIMA. Junta general de accionistas: convocatoria, quórum, mayorías.
CLÁUSULA OCTAVA. Representación legal: [presidente u otro dignatario].
CLÁUSULA NOVENA. Agente residente: [abogado / firma idónea].
CLÁUSULA DÉCIMA. Disolución y liquidación conforme a la Ley 32 de 1927.
```

## Pacto de accionistas — Estructura

El pacto de accionistas NO se inscribe en el Registro Público — es un contrato privado entre accionistas. Cláusulas habituales:

| Cláusula | Contenido | Importancia |
|---|---|---|
| Dedicación | Dedicación exclusiva/parcial de cada socio | Alta |
| Vesting de fundadores | Consolidación progresiva de acciones | Muy alta en startups |
| Decisiones reservadas | Materias que requieren unanimidad o mayoría reforzada | Alta |
| Non-compete | No competencia durante y después de la sociedad | Alta |
| Tag-along | Derecho de acompañamiento en ventas de acciones | Alta |
| Drag-along | Obligación de venta conjunta si mayoría quiere vender | Alta |
| Bloqueo / deadlock | Mecanismo de resolución si hay empate | Media |
| Reparto de dividendos | Política de distribución | Media |
| Salida de socio | Good/bad leaver, valoración de acciones | Muy alta |

## Formato de salida

```markdown
BORRADOR — CONSTITUCIÓN DE SOCIEDAD — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Datos aportados:** [qué datos se proporcionaron]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** verificar disponibilidad de denominación en el Registro Público; confirmar domicilio y agente residente; revisar el pacto social con abogado y notario; pacto de accionistas con abogado mercantilista.

## Constitución de [Denominación], S.A.

### Checklist de trámites
[Tabla completa con estado]

### Pacto social (borrador)
[Borrador adaptado a los datos]

### Estructura de pacto de accionistas
[Estructura con cláusulas recomendadas según el caso]

---

**Qué hacer a continuación:**
1. **Verificar denominación** — con las denominaciones propuestas en el Registro Público.
2. **Desarrollar pacto de accionistas** — detallo las cláusulas que elijas.
3. **Stock options** — `/startups:stock-options` si vais a tener plan de incentivos.
4. **Incentivos** — `/startups:incentivos` para verificar si aplica algún régimen especial (SEM, Ciudad del Saber) o visa de inversionista.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 32 de 1927** — sobre sociedades anónimas.
- **Ley 4 de 2009** — sobre sociedades de responsabilidad limitada.
- **Código de Comercio de Panamá** — disposiciones mercantiles generales.
- **Ley 25 de 1995** — fundaciones de interés privado (vehículo alternativo).
- **Normativa de registro de beneficiario final [verificar]** — Ley 129 de 2020 [verificar].

## Guardarraíles

- **El agente residente es obligatorio para la S.A.** Debe ser un abogado o firma de abogados idónea en Panamá. No es opcional.
- **El pacto de accionistas no sustituye al pacto social.** Lo que no esté en el pacto social inscrito no es oponible a terceros.
- **Tasa única anual.** La sociedad debe pagar la tasa única anual (USD 300 aprox. [verificar]); el impago acumulado puede llevar a la suspensión de la sociedad en el Registro Público.
- **Cumplimiento de beneficiario final y prevención de blanqueo (Ley 23 de 2015).** El agente residente es sujeto obligado y debe mantener la debida diligencia y reportar a la UAF cuando proceda.
- **No usar pactos sociales genéricos.** El pacto social debe adaptarse al caso concreto — un error en las cláusulas de transmisión de acciones o en la junta directiva genera conflictos graves.
- **Acciones al portador.** Existen restricciones y régimen de custodia para las acciones al portador [verificar] — no emitirlas sin verificar el régimen vigente.
