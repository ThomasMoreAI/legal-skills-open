---
name: constitucion-betobetico
title: /constitucion
description: Checklist completo para la constitución de una Sociedad Limitada (SL) en España, desde la certificación negativa hasta el alta censal. Genera borradores de estatutos sociales y estructura de pacto de socios. Usar cuando el usuario dice "constituir una SL", "crear una empresa", "montar una sociedad", "estatutos sociales", o necesita el proceso de constitución paso a paso.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/startups/skills/constitucion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: es
---

# /constitucion

1. Leer `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` — perfil de práctica.
2. Recopilar datos de la sociedad a constituir.
3. Generar checklist con pasos y plazos.
4. Producir borradores de estatutos y estructura de pacto de socios.

---

## Propósito

Guiar paso a paso la constitución de una SL, con checklist de trámites, borradores de estatutos sociales básicos y estructura de pacto de socios. El skill cubre la constitución estándar — para constitución telemática exprés (CIRCE/PAE), señalar las diferencias.

## Datos necesarios

- **Denominación social** — hasta 5 opciones para la certificación negativa.
- **Socios fundadores** — nombres, DNI/NIE, porcentaje de participación.
- **Capital social** — mínimo 1 EUR (Ley 18/2022 de creación y crecimiento de empresas), aunque se recomienda al menos 3.000 EUR para operatividad.
- **Objeto social** — actividad o actividades.
- **Domicilio social** — dirección completa.
- **Órgano de administración** — administrador único, administradores mancomunados, solidarios o consejo de administración.
- **Ejercicio social** — habitualmente año natural.

## Checklist de constitución

| Paso | Trámite | Dónde | Plazo/Coste orientativo | Estado |
|---|---|---|---|---|
| 1 | Certificación negativa de denominación | RMNC (online o presencial) | 3-5 días hábiles / ~15 EUR | [ ] |
| 2 | Apertura de cuenta bancaria a nombre de la sociedad en constitución | Entidad bancaria | 1-3 días | [ ] |
| 3 | Desembolso del capital social | Cuenta de la sociedad | Antes de la escritura | [ ] |
| 4 | Redacción de estatutos sociales | Letrado / notario | Variable | [ ] |
| 5 | Otorgamiento de escritura pública de constitución | Notaría | 1-2 días / ~300-600 EUR | [ ] |
| 6 | Solicitud de NIF provisional | AEAT (modelo 036) | Antes de 30 días desde escritura | [ ] |
| 7 | Liquidación del ITPAJD (exento pero hay que presentar) | Comunidad Autónoma | 30 días hábiles | [ ] |
| 8 | Inscripción en el Registro Mercantil | RM provincial | 5-15 días hábiles / ~150-300 EUR | [ ] |
| 9 | Obtención del NIF definitivo | AEAT | Tras inscripción RM | [ ] |
| 10 | Alta censal y epígrafes IAE | AEAT (modelo 036/037) | Antes de iniciar actividad | [ ] |
| 11 | Alta en la Seguridad Social (empresa) | TGSS | Antes de contratar trabajadores | [ ] |
| 12 | Alta RETA del administrador/socios > 25% | TGSS | 30 días desde inicio actividad | [ ] |
| 13 | Legalización de libros | RM (telemático) | 4 meses desde cierre del ejercicio | [ ] |
| 14 | Licencia de actividad / declaración responsable | Ayuntamiento | Variable | [ ] |

## Estatutos sociales — Estructura base

```
ESTATUTOS DE [DENOMINACIÓN SOCIAL], S.L.

TÍTULO I. DENOMINACIÓN, OBJETO, DOMICILIO Y DURACIÓN
Art. 1. Denominación: [nombre], Sociedad de Responsabilidad Limitada.
Art. 2. Objeto social: [actividades — redacción amplia pero concreta].
Art. 3. Domicilio social: [dirección completa].
Art. 4. Duración: indefinida. Inicio de operaciones: fecha de escritura.

TÍTULO II. CAPITAL SOCIAL Y PARTICIPACIONES
Art. 5. Capital social: [importe] EUR, dividido en [N] participaciones de [valor] EUR cada una.
Art. 6. Régimen de transmisión:
  - Inter vivos a socios: libre.
  - Inter vivos a terceros: derecho de adquisición preferente.
  - Mortis causa: derecho de adquisición preferente en [plazo] meses.

TÍTULO III. ÓRGANOS SOCIALES
Art. 7. Junta general: convocatoria, quórum, mayorías.
Art. 8. Órgano de administración: [tipo — administrador único / solidarios / mancomunados / consejo].
Art. 9. Duración del cargo: [indefinido o por plazo].
Art. 10. Retribución: [gratuito o sistema retributivo].

TÍTULO IV. EJERCICIO SOCIAL Y CUENTAS ANUALES
Art. 11. Ejercicio social: año natural.
Art. 12. Cuentas anuales conforme a la LSC.
```

## Pacto de socios — Estructura

El pacto de socios NO se inscribe en el RM — es un contrato privado entre socios. Cláusulas habituales:

| Cláusula | Contenido | Importancia |
|---|---|---|
| Dedicación | Dedicación exclusiva/parcial de cada socio | Alta |
| Vesting de fundadores | Consolidación progresiva de participaciones | Muy alta en startups |
| Decisiones reservadas | Materias que requieren unanimidad o mayoría reforzada | Alta |
| Non-compete | No competencia durante y después de la sociedad | Alta |
| Tag-along | Derecho de acompañamiento en ventas de participaciones | Alta |
| Drag-along | Obligación de venta conjunta si mayoría quiere vender | Alta |
| Bloqueo / deadlock | Mecanismo de resolución si hay empate | Media |
| Reparto de dividendos | Política de distribución | Media |
| Salida de socio | Good/bad leaver, valoración de participaciones | Muy alta |

## Formato de salida

```markdown
BORRADOR — CONSTITUCIÓN DE SL — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Datos aportados:** [qué datos se proporcionaron]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** verificar disponibilidad de denominación en RMNC; confirmar domicilio social; revisar estatutos con letrado y notario; pacto de socios con letrado mercantilista.

## Constitución de [Denominación], S.L.

### Checklist de trámites
[Tabla completa con estado]

### Estatutos sociales (borrador)
[Borrador adaptado a los datos]

### Estructura de pacto de socios
[Estructura con cláusulas recomendadas según el caso]

---

**Qué hacer a continuación:**
1. **Solicitar certificación negativa** — con las denominaciones propuestas.
2. **Desarrollar pacto de socios** — detallo las cláusulas que elijas.
3. **Stock options** — `/startups:stock-options` si vais a tener plan de incentivos.
4. **Incentivos fiscales** — `/startups:incentivos` para verificar si aplica la Ley de Startups.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **LSC (RDL 1/2010)** — Ley de Sociedades de Capital: arts. 1-38 (constitución SL).
- **RRM (RD 1784/1996)** — Reglamento del Registro Mercantil.
- **Ley 18/2022** — de creación y crecimiento de empresas (capital social mínimo 1 EUR).
- **Ley 14/2013 art. 15** — constitución telemática (CIRCE/PAE).

## Guardarraíles

- **Capital social de 1 EUR es legal pero no siempre práctico.** Advertir que hasta alcanzar 3.000 EUR hay restricciones (reserva del 20% de beneficios, responsabilidad solidaria de los socios en caso de liquidación — art. 4 bis LSC).
- **El pacto de socios no sustituye a los estatutos.** Lo que no esté en los estatutos no es oponible a terceros.
- **Alta en RETA obligatoria para administradores y socios con > 25% de capital** que ejerzan funciones de dirección o gerencia. No es opcional.
- **No olvidar la Ley de Prevención de Blanqueo** — los notarios verifican titularidad real.
- **No usar estatutos genéricos de internet.** Los estatutos deben adaptarse al caso concreto — un error en las cláusulas de transmisión o en el órgano de administración genera conflictos graves.
