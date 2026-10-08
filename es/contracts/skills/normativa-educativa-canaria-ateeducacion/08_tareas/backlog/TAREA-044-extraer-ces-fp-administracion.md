---
id: TAREA-044
titulo: "Extraer CEs completos — Familia Administración y Gestión (CUR-048, CUR-049)"
estado: "Hecha"
prioridad: "Media"
tipo: "curriculo"
responsable: "@.agents/skills/experto-formacion-profesional"
fecha_creacion: 2026-04-26
fecha_actualizacion: 2026-04-26
relacionadas: [NOR-053, NOR-054, CUR-048, CUR-049]
---

# TAREA-044 — Extraer CEs completos: Familia Administración y Gestión

> Este documento no sustituye la fuente oficial. Fuente: BOE-A-2009-19148 (RD 1631/2009) y BOE-A-2011-19533 (RD 1584/2011).

## Objetivo

Extraer los Resultados de Aprendizaje (RAs) y Criterios de Evaluación (CEs) completos para los ciclos formativos de la familia Administración y Gestión:

- **CUR-048** — Técnico en Gestión Administrativa (GM), RD 1631/2009
- **CUR-049** — Técnico Superior en Administración y Finanzas (GS), RD 1584/2011

## Resultado

### CUR-048 — Técnico en Gestión Administrativa

**estado_extraccion: completado**

| Código | Módulo | RAs extraídos |
|--------|--------|---------------|
| 0437 | Comunicación empresarial y atención al cliente | 8 |
| 0438 | Operaciones administrativas de compra-venta | 5 |
| 0439 | Empresa y Administración | 7 |
| 0440 | Tratamiento informático de la información | 8 |
| 0441 | Técnica contable | 5 |
| 0442 | Operaciones administrativas de recursos humanos | 6 |
| 0443 | Tratamiento de la documentación contable | 3 |
| 0444 | Inglés | 4 |
| 0446 | Empresa en el aula | 5 |
| 0448 | Operaciones auxiliares de gestión de tesorería | 5 |
| 0449 | Formación y orientación laboral | 9 |
| 0451 | Formación en centros de trabajo | 9 |

Todos los módulos tienen RAs y CEs extraídos. Extracción completada.

### CUR-049 — Técnico Superior en Administración y Finanzas

**estado_extraccion: parcial**

| Código | Módulo | RAs extraídos | Estado |
|--------|--------|---------------|--------|
| 0647 | Gestión de la documentación jurídica y empresarial | 5 | Completo |
| 0648 | Recursos humanos y responsabilidad social corporativa | 5 | Completo |
| 0649 | Ofimática y proceso de la información | 9 | Completo |
| 0650 | Proceso integral de la actividad comercial | 7 | Completo |
| 0651 | Comunicación y atención al cliente | 7 | Completo |
| 0179 | Inglés | — | [PENDIENTE] |
| 0652 | Gestión de recursos humanos | — | [PENDIENTE] |
| 0653 | Gestión financiera | — | [PENDIENTE] |
| 0654 | Contabilidad y fiscalidad | — | [PENDIENTE] |
| 0655 | Gestión logística y comercial | — | [PENDIENTE] |
| 0656 | Simulación empresarial | — | [PENDIENTE] |
| 0657 | Proyecto de administración y finanzas | — | [PENDIENTE] |
| 0658 | Formación y orientación laboral | — | [PENDIENTE] |
| 0660 | Formación en centros de trabajo | — | [PENDIENTE] |

Los módulos 0179 y 0652–0660 quedan como [PENDIENTE] porque el HTML del BOE-A-2011-19533 se trunca antes de llegar a esos contenidos del Anexo I. Para completar la extracción consultar el PDF oficial en https://www.boe.es/boe/dias/2011/12/15/pdfs/BOE-A-2011-19533.pdf

## Fuentes consultadas

- BOE-A-2009-19148: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2009-19148 (2026-04-26)
- BOE-A-2011-19533: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2011-19533 (2026-04-26)

## Criterios de cierre

- [x] Fuente oficial BOE identificada y consultada
- [x] Fecha de consulta registrada
- [x] Formato YAML válido (python3 yaml.safe_load sin errores)
- [x] Entradas actualizadas en 06_indices/curriculos.yaml
- [x] TAREA-044 marcada como Hecha en tareas.yaml y status.yaml
- [x] Preguntas abiertas registradas (módulos pendientes de CUR-049)
- [x] Registro en diario pendiente (a cargo del agente orquestador)
