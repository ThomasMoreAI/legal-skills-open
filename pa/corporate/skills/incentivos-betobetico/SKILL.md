---
name: incentivos-betobetico
title: /incentivos
description: 'Mapea los incentivos y regímenes especiales disponibles para startups y empresas de base tecnológica en Panamá: régimen SEM (sedes de empresas multinacionales), Ciudad del Saber, Panamá Pacífico, EMMA, Zona Libre de Colón, así como la inmigración para fundadores e inversionistas (visa de inversionista, países amigos, jubilado pensionado). Genera una tabla de incentivos aplicables con requisitos y beneficio estimado. Usar cuando el usuario dice "incentivos", "régimen SEM", "Ciudad del Saber", "Panamá Pacífico", "visa de inversionista", "beneficios fiscales para startups", o quiere optimizar la estructura fiscal y migratoria de su empresa.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/startups/skills/incentivos
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: corporate
language: es
---

# /incentivos

1. Leer `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` — perfil de práctica.
2. Recopilar datos de la empresa y de los fundadores/inversionistas.
3. Evaluar cada incentivo y régimen migratorio aplicable.
4. Producir la tabla de incentivos con requisitos y beneficio.

---

## Propósito

Identificar los regímenes de incentivos y opciones migratorias aplicables a una startup o empresa innovadora en Panamá, verificar el cumplimiento de requisitos y estimar el beneficio. Es una herramienta de orientación — la aplicación concreta requiere asesor fiscal y abogado migratorio.

## Incentivos y regímenes disponibles

### 1. Régimen SEM (Sede de Empresa Multinacional) — Ley 41 de 2007

| Beneficio | Detalle | Requisito |
|---|---|---|
| ISR reducido sobre servicios a su grupo | Tarifa especial de ISR sobre la renta neta gravable [verificar] | Licencia SEM otorgada por la Comisión SEM |
| Exenciones de ITBMS en ciertos servicios | Servicios prestados a entidades del grupo en el exterior [verificar] | Operaciones con el grupo multinacional |
| Visas especiales para personal extranjero | Visa de personal permanente SEM | Empleados de la sede |
| Exención de impuesto sobre dividendos y remesas en ciertos casos | [verificar] | Según fuente de la renta |

**Idea clave:** el SEM es para grupos multinacionales que centralizan servicios (gestión, tesorería, I+D, soporte) desde Panamá. Encaja para startups que ya operan en varios países.

### 2. Ciudad del Saber — Decreto Ley 6 de 1998

| Beneficio | Detalle |
|---|---|
| Exenciones fiscales a empresas e instituciones afiliadas | Exención de ITBMS e impuestos de importación sobre equipos, ISR sobre ciertas actividades [verificar] |
| Ecosistema de innovación | Entorno orientado a tecnología, investigación e innovación |
| Visas para personal e investigadores | Facilidades migratorias para afiliados [verificar] |

**Requisito:** ser admitido como empresa o entidad afiliada a la Fundación Ciudad del Saber, con un proyecto alineado a su misión (tecnología, investigación, innovación, emprendimiento).

### 3. Panamá Pacífico — Ley 41 de 2004

| Beneficio | Detalle |
|---|---|
| Exenciones fiscales y aduaneras | Régimen especial de zona económica especial [verificar] |
| Actividades cubiertas | Servicios multinacionales, logística, manufactura ligera, back-office, call centers [verificar] |
| Ventanilla única | Trámites empresariales y migratorios centralizados |

### 4. EMMA — Empresa Multinacional de Servicios relacionados con la Manufactura — Ley 159 de 2020

| Beneficio | Detalle |
|---|---|
| ISR reducido | Tarifa especial sobre servicios de manufactura a su grupo [verificar] |
| Visas para personal | Facilidades migratorias [verificar] |

### 5. Zona Libre de Colón [verificar]

| Beneficio | Detalle |
|---|---|
| Exenciones aduaneras y fiscales | Para operaciones de comercio internacional, reexportación, logística [verificar] |
| Idóneo para | Distribución y comercio de mercancías hacia la región |

## Inmigración para fundadores e inversionistas

| Categoría migratoria | Idóneo para | Requisito orientativo [verificar] |
|---|---|---|
| Visa de inversionista (negocio propio) | Fundador que invierte y opera una empresa en Panamá | Inversión mínima en la empresa y generación de empleo local [verificar montos] |
| Visa de países amigos | Nacionales de países con relaciones amistosas que invierten o trabajan | Vínculo económico o profesional con Panamá [verificar lista de países y requisitos] |
| Visa de inversionista calificado | Inversión significativa (inmueble, depósito, valores) | Monto de inversión elevado [verificar] |
| Jubilado pensionado | Fundadores/socios con renta pasiva | Pensión vitalicia mínima [verificar monto] |
| Permiso de trabajo bajo régimen especial (SEM, Ciudad del Saber, Panamá Pacífico) | Personal extranjero de empresas en régimen especial | Vinculado a la licencia del régimen |

## Formato de salida

```markdown
BORRADOR — MAPA DE INCENTIVOS Y MIGRACIÓN — REVISIÓN FISCAL Y MIGRATORIA OBLIGATORIA

> **Nota para el revisor**
> - **Datos de la empresa:** [resumen]
> - **Incentivos y regímenes evaluados:** [N]
> - **Elementos marcados [verificar]:** [N — especialmente montos, tarifas y requisitos que pueden haber cambiado]
> - **Antes de actuar:** verificar requisitos con asesor fiscal y abogado migratorio; comprobar vigencia de cada régimen; confirmar montos de inversión exigidos; iniciar trámite de licencia/visa con el organismo competente.

## Incentivos y migración: [Nombre de la empresa]

### Resumen

| Régimen / Visa | Aplicable | Beneficio estimado | Requisito pendiente |
|---|---|---|---|
| Régimen SEM | [sí/no/potencial] | [ahorro / visas] | [requisito] |
| Ciudad del Saber | [sí/no/potencial] | [exenciones] | [requisito] |
| Panamá Pacífico | [sí/no/potencial] | [exenciones] | [requisito] |
| EMMA | [sí/no/potencial] | [ISR reducido] | [requisito] |
| Visa de inversionista (fundadores) | [sí/no/potencial] | [residencia] | [monto de inversión] |

### Análisis detallado por régimen

[Para cada régimen aplicable: requisitos, estado de cumplimiento, pasos para acceder, beneficio estimado]

### Plan de acción

| Acción | Responsable | Plazo | Prioridad |
|---|---|---|---|
| [acción] | [quién] | [cuándo] | [alta/media/baja] |

---

**Qué hacer a continuación:**
1. **Solicitar licencia de régimen** — SEM / Ciudad del Saber / Panamá Pacífico, según encaje.
2. **Iniciar trámite migratorio** — visa de inversionista o régimen especial para los fundadores extranjeros.
3. **Plan de stock options** — `/startups:stock-options` para el equipo.
4. **Constitución** — `/startups:constitucion` si la sociedad aún no está constituida bajo la forma adecuada.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 41 de 2007** — régimen de Sedes de Empresas Multinacionales (SEM).
- **Decreto Ley 6 de 1998** — Ciudad del Saber.
- **Ley 41 de 2004** — Área Económica Especial Panamá Pacífico.
- **Ley 159 de 2020** — Empresa Multinacional de Servicios relacionados con la Manufactura (EMMA).
- **Código Fiscal de Panamá** — Impuesto sobre la Renta (ISR), principio de territorialidad.
- **Decreto Ley 3 de 2008 y normativa migratoria [verificar]** — categorías de visa de inversionista, países amigos, jubilado pensionado.

## Guardarraíles

- **Los montos, tarifas y requisitos cambian.** Marcar `[verificar]` en toda cifra o requisito concreto — la normativa de incentivos y migración panameña se reforma con frecuencia.
- **Cada régimen exige una licencia o admisión previa.** Sin la licencia SEM, la afiliación a Ciudad del Saber o el registro en Panamá Pacífico, no aplica ningún beneficio.
- **El principio de territorialidad es la base del sistema fiscal panameño.** Solo tributan en Panamá las rentas de fuente panameña; muchos beneficios derivan de operar con el exterior — verificar la fuente de cada renta.
- **No prometer exenciones automáticas.** El beneficio depende del cumplimiento estricto de requisitos (empleo local, sustancia económica, tipo de actividad). Verificar siempre.
- **La migración del fundador y la estructura societaria deben planificarse juntas.** El monto de inversión exigido para la visa y la forma societaria interactúan — coordinar con abogado migratorio.
- **Siempre derivar a asesor fiscal y abogado migratorio.** La aplicación de regímenes especiales y la obtención de residencias requieren planificación profesional. Un error puede suponer la pérdida del incentivo o el rechazo de la visa.
