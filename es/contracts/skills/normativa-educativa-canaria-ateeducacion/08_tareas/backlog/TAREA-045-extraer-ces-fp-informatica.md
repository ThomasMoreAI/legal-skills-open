---
id: TAREA-045
titulo: "Extraer CEs completos — Familia Informática y Comunicaciones (CUR-050, CUR-051)"
estado: "Hecha"
prioridad: "Media"
tipo: "curriculo"
responsable: "@.agents/skills/experto-formacion-profesional"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [NOR-055, NOR-056, CUR-050, CUR-051, TAREA-040]
---

# TAREA-045 — Extraer CEs completos: FP Informática y Comunicaciones (CUR-050, CUR-051)

> Este documento no sustituye a la fuente oficial.

## Objetivo

Añadir los Criterios de Evaluación (CEs) completos a los módulos profesionales de los
ciclos formativos de Grado Superior de la familia Informática y Comunicaciones:

- **CUR-050** — T.S. Desarrollo de Aplicaciones Multiplataforma (DAM), RD 450/2010 (BOE-A-2010-8067)
- **CUR-051** — T.S. Desarrollo de Aplicaciones Web (DAW), RD 686/2010 (BOE-A-2010-9269)

Los archivos ya contaban con módulos y enunciados de Resultados de Aprendizaje (RAs)
extraídos en TAREA-040, pero los `criterios_evaluacion` estaban vacíos (`[]`).

## Fuente oficial consultada

- URL DAM: `https://www.boe.es/diario_boe/txt.php?id=BOE-A-2010-8067`
- URL DAW: `https://www.boe.es/diario_boe/txt.php?id=BOE-A-2010-9269`
- Fecha de consulta: 2026-04-26

## Módulos procesados — CUR-050 (DAM)

| Código | Módulo | CEs extraídos |
|--------|--------|--------------|
| 0483 | Sistemas Informáticos | Completos (7 RAs, 6+7+7+8+8+6+6 CEs) |
| 0484 | Bases de Datos | Completos (7 RAs, 8+8+6+8+9+8+6 CEs) |
| 0485 | Programación | Completos (9 RAs, 9+9+7+10+8+9+8+8+7 CEs) |
| 0373 | Lenguajes de Marcas y Sistemas de Gestión | Completos (7 RAs, 9+8+7+8+8+9+10 CEs) |
| 0487 | Entornos de Desarrollo | Completos (6 RAs, 6+7+8+7+7+8 CEs) |
| 0486 | Acceso a Datos | Completos (6 RAs, 7+10+7+8+7+9 CEs) |
| 0488 | Desarrollo de Interfaces | Completos (7 RAs, 7+7+8+8+8+7+6 CEs) |
| 0489 | Programación Multimedia y Dispositivos Móviles | [PENDIENTE] — HTML truncado |
| 0490 | Programación de Servicios y Procesos | [PENDIENTE] — HTML truncado |
| 0491 | Sistemas de Gestión Empresarial | [PENDIENTE] — HTML truncado |
| 0492 | Proyecto DAM | [PENDIENTE] — HTML truncado |
| 0493 | Formación y Orientación Laboral | [PENDIENTE] — HTML truncado |
| 0494 | Empresa e Iniciativa Emprendedora | [PENDIENTE] — HTML truncado |
| 0495 | Formación en Centros de Trabajo | [PENDIENTE] — HTML truncado |

**Estado resultante CUR-050:** `parcial` (7/14 módulos con CEs completos)

## Módulos procesados — CUR-051 (DAW)

| Código | Módulo | CEs extraídos |
|--------|--------|--------------|
| 0483 | Sistemas Informáticos | Completos (7 RAs) |
| 0484 | Bases de Datos | Completos (7 RAs) |
| 0485 | Programación | Completos (9 RAs) |
| 0373 | Lenguajes de Marcas y Sistemas de Gestión | Completos (7 RAs) |
| 0487 | Entornos de Desarrollo | Completos (6 RAs) |
| 0612 | Desarrollo Web en Entorno Cliente | Completos (7 RAs) |
| 0613 | Desarrollo Web en Entorno Servidor | Parcial: RAs 1-7 completos; RA 8 [PENDIENTE] |
| 0614 | Despliegue de Aplicaciones Web | [PENDIENTE] — HTML truncado |
| 0615 | Diseño de Interfaces Web | [PENDIENTE] — HTML truncado |
| 0616 | Proyecto DAW | [PENDIENTE] — HTML truncado |
| 0617 | Formación y Orientación Laboral | [PENDIENTE] — HTML truncado |
| 0618 | Empresa e Iniciativa Emprendedora | [PENDIENTE] — HTML truncado |
| 0619 | Formación en Centros de Trabajo | [PENDIENTE] — HTML truncado |

**Estado resultante CUR-051:** `parcial` (6/13 módulos con CEs completos; 1 parcial)

## Limitación técnica

El documento HTML del BOE está truncado: el visor web de BOE-A-2010-8067 termina en el
módulo 0488, y el de BOE-A-2010-9269 termina a mitad del módulo 0613 (RA 8). Los módulos
restantes requieren acceso al PDF oficial del RD 450/2010 y RD 686/2010 respectivamente.

Los criterios no disponibles se han marcado con `[PENDIENTE: documento HTML del BOE
truncado — consultar PDF oficial]`, conforme a la regla R15.

## Tarea de seguimiento recomendada

Crear una nueva TAREA para extraer los CEs pendientes de los módulos 0489-0495 (DAM) y
0613-RA8, 0614-0619 (DAW) a partir del PDF oficial de los RD correspondientes.
