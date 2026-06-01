---
name: rat
title: /rat
description: Crea o actualiza el Registro de Actividades de Tratamiento (RAT) conforme al art. 30 del RGPD, en el formato recomendado por la AEPD. Genera una ficha por cada actividad de tratamiento con todos los campos obligatorios. Usar cuando el usuario dice "registro de actividades", "RAT", "crea una ficha de tratamiento", "actualiza el registro", o necesita documentar tratamientos de datos personales.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/proteccion-datos/skills/rat
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
---

# /rat

1. Leer `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — perfil de práctica.
2. Identificar las actividades de tratamiento a documentar.
3. Completar cada ficha con los campos del art. 30 RGPD.
4. Producir las fichas en formato tabla AEPD.

---

## Propósito

Documentar las actividades de tratamiento de datos personales de una organización en un RAT que cumpla el art. 30 RGPD. El RAT es obligatorio para organizaciones con más de 250 empleados y, en la práctica, para cualquier organización que trate datos de forma no ocasional (que son casi todas).

## Campos obligatorios por ficha (art. 30.1 RGPD)

| Campo | Descripción | Ejemplo |
|---|---|---|
| Nombre de la actividad | Denominación descriptiva | "Gestión de nóminas" |
| Responsable del tratamiento | Identidad y datos de contacto | Empresa X, CIF, dirección, contacto |
| Corresponsable (si aplica) | Identidad y datos de contacto | — |
| Representante (si aplica) | Si el responsable no está en la UE | — |
| DPD/DPO | Datos de contacto del DPD | dpd@empresa.com |
| Finalidad del tratamiento | Para qué se tratan los datos | "Cumplimiento de obligaciones laborales" |
| Base jurídica | Art. 6 RGPD (y art. 9 si datos especiales) | "Art. 6.1.b) RGPD — ejecución de contrato de trabajo" |
| Categorías de interesados | Quiénes son los afectados | "Empleados" |
| Categorías de datos | Qué datos se tratan | "Identificativos, económicos, profesionales" |
| Datos especiales (art. 9) | Si se tratan categorías especiales | "Datos de salud (bajas IT)" |
| Destinatarios | A quién se comunican los datos | "AEAT, TGSS, entidad bancaria" |
| Transferencias internacionales | Si hay, a qué países y garantías | "No" / "EE.UU. — decisión de adecuación" |
| Plazos de conservación | Cuánto tiempo se conservan | "Duración de la relación laboral + 4 años (prescripción)" |
| Medidas de seguridad | Descripción general | "Cifrado, control de accesos, copias de seguridad" |

## Bases jurídicas habituales (art. 6 RGPD)

| Base | Artículo | Uso típico |
|---|---|---|
| Consentimiento | Art. 6.1.a) | Marketing, cookies no esenciales, newsletters |
| Ejecución de contrato | Art. 6.1.b) | Relación laboral, prestación de servicios contratados |
| Obligación legal | Art. 6.1.c) | Obligaciones fiscales, PBC, SSocial |
| Intereses vitales | Art. 6.1.d) | Emergencias sanitarias (excepcional) |
| Interés público | Art. 6.1.e) | Administraciones públicas |
| Interés legítimo | Art. 6.1.f) | Videovigilancia, prevención del fraude, marketing directo (con límites) |

## Actividades de tratamiento habituales

Checklist para no olvidar tratamientos comunes:

- [ ] Gestión de RRHH / nóminas
- [ ] Selección de personal
- [ ] Control horario / presencia
- [ ] Videovigilancia
- [ ] Gestión de clientes / CRM
- [ ] Facturación y contabilidad
- [ ] Marketing y comunicaciones comerciales
- [ ] Gestión de proveedores
- [ ] Gestión web / cookies
- [ ] Canal de denuncias (Ley 2/2023)
- [ ] Prevención de blanqueo de capitales
- [ ] Gestión de reclamaciones / ARCO

## Formato de salida

```markdown
BORRADOR — REGISTRO DE ACTIVIDADES DE TRATAMIENTO — REVISIÓN DPD OBLIGATORIA

> **Nota para el revisor**
> - **Actividades documentadas:** [N]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** verificar bases jurídicas con DPD; confirmar plazos de conservación; revisar transferencias internacionales; validar medidas de seguridad con IT.

## RAT — [Nombre de la organización]

**Responsable del tratamiento:** [datos]
**DPD:** [datos]
**Fecha de actualización:** [fecha]

### Ficha 1: [Nombre de la actividad]

| Campo | Contenido |
|---|---|
| Finalidad | [finalidad] |
| Base jurídica | [base] |
| Categorías de interesados | [categorías] |
| Categorías de datos | [categorías] |
| Datos especiales | [sí/no — cuáles] |
| Destinatarios | [destinatarios] |
| Transferencias internacionales | [sí/no — detalle] |
| Plazo de conservación | [plazo — fundamentación] |
| Medidas de seguridad | [descripción] |

[Repetir para cada actividad]

### Resumen del RAT

| N.o | Actividad | Base jurídica | Datos especiales | TI | Estado |
|---|---|---|---|---|---|
| 1 | [nombre] | [base] | [sí/no] | [sí/no] | [completo/pendiente] |

---

**Qué hacer a continuación:**
1. **Añadir actividades** — documento más tratamientos que identifiques.
2. **EIPD** — `/proteccion-datos:eipd` si algún tratamiento requiere evaluación de impacto.
3. **Cláusulas informativas** — genero las cláusulas de información (arts. 13-14 RGPD) para cada tratamiento.
4. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **RGPD art. 30** — registro de actividades de tratamiento.
- **RGPD art. 6** — bases jurídicas del tratamiento.
- **RGPD art. 9** — tratamiento de categorías especiales de datos.
- **RGPD arts. 13-14** — información al interesado.
- **LOPDGDD arts. 31-32** — obligaciones del responsable.
- **Guía del RAT de la AEPD** — modelo y orientaciones.

## Guardarraíles

- **La base jurídica no se puede elegir a conveniencia.** Cada tratamiento tiene una base jurídica que se determina por su naturaleza, no por preferencia del responsable.
- **El consentimiento no es siempre la mejor opción.** Para relaciones laborales es ejecución de contrato (art. 6.1.b), no consentimiento — el trabajador no puede consentir libremente frente al empleador.
- **Los plazos de conservación deben estar justificados.** No basta con "indefinido" — hay que vincular cada plazo a una obligación legal o finalidad concreta.
- **Las transferencias internacionales incluyen servicios cloud.** Si usan AWS, Google Cloud, Microsoft Azure, etc., hay transferencia internacional — verificar garantías.
- **El RAT es un documento vivo.** Advertir que debe actualizarse cada vez que cambie un tratamiento.
