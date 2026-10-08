---
name: rat-betobetico
title: /rat
description: Crea o actualiza el Registro de Actividades de Tratamiento (RAT) conforme a la Ley 81 de 2019 y al Decreto Ejecutivo 285 de 2021, en el formato recomendado por la ANTAI. Genera una ficha por cada actividad de tratamiento con todos los campos obligatorios. Usar cuando el usuario dice "registro de actividades", "RAT", "crea una ficha de tratamiento", "actualiza el registro", o necesita documentar tratamientos de datos personales.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/proteccion-datos/skills/rat
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: data-protection
language: es
---

# /rat

1. Leer `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — perfil de práctica.
2. Identificar las actividades de tratamiento a documentar.
3. Completar cada ficha con los campos exigidos por la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021.
4. Producir las fichas en formato tabla ANTAI.

---

## Propósito

Documentar las actividades de tratamiento de datos personales de una organización en un RAT que cumpla la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021. En la práctica, el RAT es recomendable para cualquier organización que trate datos de forma no ocasional (que son casi todas).

## Campos obligatorios por ficha

| Campo | Descripción | Ejemplo |
|---|---|---|
| Nombre de la actividad | Denominación descriptiva | "Gestión de planillas" |
| Responsable del tratamiento | Identidad y datos de contacto | Empresa X, RUC, dirección, contacto |
| Corresponsable (si aplica) | Identidad y datos de contacto | — |
| Representante (si aplica) | Si el responsable no está domiciliado en Panamá | — |
| Responsable de protección de datos | Datos de contacto | datos@empresa.com |
| Finalidad del tratamiento | Para qué se tratan los datos | "Cumplimiento de obligaciones laborales" |
| Base de legitimación | Fundamento del tratamiento (arts. 6 y 8 de la Ley 81 de 2019) | "Necesidad contractual: ejecución del contrato de trabajo" |
| Categorías de titulares | Quiénes son los afectados | "Empleados" |
| Categorías de datos | Qué datos se tratan | "Identificativos, económicos, profesionales" |
| Datos sensibles | Si se tratan categorías especiales (definidas en el art. 4 de la Ley 81 de 2019; régimen reforzado, no transferibles salvo excepciones, art. 13) | "Datos de salud (incapacidades)" |
| Destinatarios | A quién se comunican los datos | "DGI, CSS, entidad bancaria" |
| Transferencias internacionales | Si hay, a qué países y garantías; el destino debe ofrecer un nivel de protección equivalente o superior, o concurrir condiciones (consentimiento, contrato, etc.) — Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 | "No" / "EE. UU. — garantías contractuales" |
| Plazos de conservación | Cuánto tiempo se conservan | "Duración de la relación laboral + plazo de prescripción aplicable" [verificar] |
| Medidas de seguridad | Descripción general | "Cifrado, control de accesos, copias de seguridad" |

## Bases de legitimación (arts. 6 y 8 de la Ley 81 de 2019)

> La regla general es el **CONSENTIMIENTO** previo, informado e inequívoco del titular (arts. 6 y 8). Se admiten además: necesidad contractual, obligación legal y autorización legal especial (excepciones tasadas del art. 8). El **"INTERÉS LEGÍTIMO" del responsable NO es una base de legitimación en la Ley 81** (a diferencia del RGPD).

| Base | Uso típico |
|---|---|
| Consentimiento del titular (regla general) | Marketing, cookies no esenciales, newsletters, y en general cualquier tratamiento sin otra base tasada |
| Necesidad contractual | Relación laboral, prestación de servicios contratados |
| Obligación legal | Obligaciones fiscales, prevención de blanqueo, CSS |
| Autorización legal especial | Supuestos previstos por ley |
| Protección de la vida/salud del titular | Emergencias sanitarias (excepcional) |
| Cumplimiento de función pública | Entidades del Estado |

> **Sin "interés legítimo":** tratamientos que bajo el RGPD se ampararían en el interés legítimo del responsable (videovigilancia, prevención del fraude, mercadeo directo) requieren en Panamá **consentimiento** o una de las **excepciones tasadas del art. 8**; el interés legítimo no es una base autónoma.

## Actividades de tratamiento habituales

Checklist para no olvidar tratamientos comunes:

- [ ] Gestión de RRHH / planillas
- [ ] Selección de personal
- [ ] Control horario / presencia
- [ ] Videovigilancia
- [ ] Gestión de clientes / CRM
- [ ] Facturación y contabilidad
- [ ] Mercadeo y comunicaciones comerciales
- [ ] Gestión de proveedores
- [ ] Gestión web / cookies
- [ ] Canal de denuncias
- [ ] Prevención de blanqueo de capitales (Ley 23 de 2015 / UAF) — obligación legal concurrente
- [ ] Gestión de reclamaciones / ejercicio de derechos del titular

## Formato de salida

```markdown
BORRADOR — REGISTRO DE ACTIVIDADES DE TRATAMIENTO — REVISIÓN OBLIGATORIA DEL RESPONSABLE DE PROTECCIÓN DE DATOS

> **Nota para el revisor**
> - **Actividades documentadas:** [N]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** verificar bases de legitimación; confirmar plazos de conservación; revisar transferencias internacionales; validar medidas de seguridad con IT.

## RAT — [Nombre de la organización]

**Responsable del tratamiento:** [datos]
**Responsable de protección de datos:** [datos]
**Fecha de actualización:** [fecha]

### Ficha 1: [Nombre de la actividad]

| Campo | Contenido |
|---|---|
| Finalidad | [finalidad] |
| Base de legitimación | [base] |
| Categorías de titulares | [categorías] |
| Categorías de datos | [categorías] |
| Datos sensibles | [sí/no — cuáles] |
| Destinatarios | [destinatarios] |
| Transferencias internacionales | [sí/no — detalle] |
| Plazo de conservación | [plazo — fundamentación] |
| Medidas de seguridad | [descripción] |

[Repetir para cada actividad]

### Resumen del RAT

| N.o | Actividad | Base de legitimación | Datos sensibles | TI | Estado |
|---|---|---|---|---|---|
| 1 | [nombre] | [base] | [sí/no] | [sí/no] | [completo/pendiente] |

---

**Qué hacer a continuación:**
1. **Añadir actividades** — documento más tratamientos que identifiques.
2. **EIPD** — `/proteccion-datos:eipd` si algún tratamiento requiere evaluación de impacto.
3. **Cláusulas informativas** — genero las cláusulas de información al titular para cada tratamiento.
4. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 81 de 2019** — bases de legitimación (arts. 6 y 8; el consentimiento es la regla general; el interés legítimo no es base autónoma); datos sensibles (art. 4; régimen reforzado art. 13).
- **Decreto Ejecutivo 285 de 2021** — reglamento de la Ley 81 de 2019; registro de bases de datos / actividades de tratamiento (arts. 34-36; art. 35: registro de bases de datos); transferencias internacionales.
- **Guías ANTAI** — modelo y orientaciones.

## Guardarraíles

- **La base de legitimación no se puede elegir a conveniencia.** Cada tratamiento tiene una base que se determina por su naturaleza, no por preferencia del responsable.
- **El consentimiento no es siempre la mejor opción.** Para relaciones laborales suele ser la ejecución del contrato de trabajo, no el consentimiento — el trabajador no puede consentir libremente frente al empleador.
- **Los plazos de conservación deben estar justificados.** No basta con "indefinido" — hay que vincular cada plazo a una obligación legal o finalidad concreta.
- **Las transferencias internacionales incluyen servicios cloud.** Si usan AWS, Google Cloud, Microsoft Azure, etc., hay transferencia internacional — verificar garantías.
- **El RAT es un documento vivo.** Advertir que debe actualizarse cada vez que cambie un tratamiento.
