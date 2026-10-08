# Inventario de Atención a la Diversidad y Alumnado Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Sistematizar la normativa canaria vigente en materia de inclusión educativa, atención a la diversidad y procesos de admisión, incluyendo las resoluciones de instrucciones de los cursos 24/25, 25/26 y 26/27.

**Architecture:** Creación de fichas de fuente (FTE) y fichas normativas (NOR) siguiendo el estándar del repositorio, con un enfoque individual para cada resolución anual para permitir trazabilidad RAG precisa. Actualización de índices y establecimiento de relaciones jerárquicas.

**Tech Stack:** Markdown, YAML.

---

### Task 1: Fuentes de Atención a la Diversidad (FTE-027, FTE-029, FTE-030)

**Files:**
- Create: `01_fuentes/boc/FTE-027-decreto-25-2018-diversidad.md`
- Create: `01_fuentes/boc/FTE-029-orden-7-junio-2007-diversidad-basica.md`
- Create: `01_fuentes/boc/FTE-030-orden-13-diciembre-2010-neae.md`

- [ ] **Step 1: Crear FTE-027**
```markdown
---
id: FTE-027
titulo: "Decreto 25/2018, de 26 de febrero, por el que se regula la atención a la diversidad"
tipo_fuente: "boletin-oficial"
autoridad: "Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/boc/2018/046/001.html"
fecha_consulta: 2026-04-26
estado_fuente: "Activa"
---
# FTE-027 — Decreto 25/2018 (Diversidad)
```

- [ ] **Step 2: Crear FTE-029**
```markdown
---
id: FTE-029
titulo: "Orden de 7 de junio de 2007, medidas de atención a la diversidad en enseñanza básica"
tipo_fuente: "boletin-oficial"
autoridad: "Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/boc/2007/124/005.html"
fecha_consulta: 2026-04-26
estado_fuente: "Activa"
---
# FTE-029 — Orden 7 de junio de 2007 (Diversidad Básica)
```

- [ ] **Step 3: Crear FTE-030**
```markdown
---
id: FTE-030
titulo: "Orden de 13 de diciembre de 2010, atención al alumnado con NEAE"
tipo_fuente: "boletin-oficial"
autoridad: "Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/boc/2010/250/001.html"
fecha_consulta: 2026-04-26
estado_fuente: "Activa"
---
# FTE-030 — Orden 13 de diciembre de 2010 (NEAE)
```

- [ ] **Step 4: Commit**
```bash
git add 01_fuentes/boc/FTE-027-* 01_fuentes/boc/FTE-029-* 01_fuentes/boc/FTE-030-*
git commit -m "feat: añadir fuentes de atención a la diversidad"
```

### Task 2: Fuentes de Admisión (FTE-028, FTE-031, FTE-035)

**Files:**
- Create: `01_fuentes/boc/FTE-028-decreto-9-2022-admision.md`
- Create: `01_fuentes/boc/FTE-031-orden-3-marzo-2022-admision.md`
- Create: `01_fuentes/boc/FTE-035-resolucion-5-febrero-2026-admision-26-27.md`

- [ ] **Step 1: Crear FTE-028**
```markdown
---
id: FTE-028
titulo: "Decreto 9/2022, de 20 de enero, por el que se regula la admisión del alumnado"
tipo_fuente: "boletin-oficial"
autoridad: "Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/boc/2022/020/001.html"
fecha_consulta: 2026-04-26
estado_fuente: "Activa"
---
# FTE-028 — Decreto 9/2022 (Admisión)
```

- [ ] **Step 2: Crear FTE-031**
```markdown
---
id: FTE-031
titulo: "Orden de 3 de marzo de 2022, procedimiento de admisión del alumnado"
tipo_fuente: "boletin-oficial"
autoridad: "Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/boc/2022/049/001.html"
fecha_consulta: 2026-04-26
estado_fuente: "Activa"
---
# FTE-031 — Orden 3 de marzo de 2022 (Admisión Procedimiento)
```

- [ ] **Step 3: Crear FTE-035**
```markdown
---
id: FTE-035
titulo: "Resolución de 5 de febrero de 2026, convocatoria de admisión 2026-2027"
tipo_fuente: "boletin-oficial"
autoridad: "Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/boc/2026/031/001.html"
fecha_consulta: 2026-04-26
estado_fuente: "Activa"
---
# FTE-035 — Resolución Admisión 26/27
```

- [ ] **Step 4: Commit**
```bash
git add 01_fuentes/boc/FTE-028-* 01_fuentes/boc/FTE-031-* 01_fuentes/boc/FTE-035-*
git commit -m "feat: añadir fuentes de admisión de alumnado"
```

### Task 3: Fuentes de Resoluciones Anuales Diversidad (FTE-032, FTE-033, FTE-034)

**Files:**
- Create: `01_fuentes/portales-oficiales/FTE-032-resolucion-instrucciones-diversidad-24-25.md`
- Create: `01_fuentes/portales-oficiales/FTE-033-resolucion-instrucciones-diversidad-25-26.md`
- Create: `01_fuentes/portales-oficiales/FTE-034-resolucion-instrucciones-diversidad-26-27.md`

- [ ] **Step 1: Crear FTE-032**
```markdown
---
id: FTE-032
titulo: "Resolución n.º 261/2024, instrucciones atención diversidad 2024-2025"
tipo_fuente: "resolucion-administrativa"
autoridad: "DGOEII - Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/educacion/web/servicios/atencion_diversidad/instrucciones-24-25/"
fecha_consulta: 2026-04-26
estado_fuente: "Histórica"
---
# FTE-032 — Instrucciones Diversidad 24/25
```

- [ ] **Step 2: Crear FTE-033**
```markdown
---
id: FTE-033
titulo: "Resolución n.º 327/2025, instrucciones atención diversidad 2025-2026"
tipo_fuente: "resolucion-administrativa"
autoridad: "DGOEII - Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/educacion/web/servicios/atencion_diversidad/instrucciones-25-26/"
fecha_consulta: 2026-04-26
estado_fuente: "Superada"
---
# FTE-033 — Instrucciones Diversidad 25/26
```

- [ ] **Step 3: Crear FTE-034**
```markdown
---
id: FTE-034
titulo: "Resolución n.º 584/2026, instrucciones atención diversidad 2026-2027"
tipo_fuente: "resolucion-administrativa"
autoridad: "DGOEII - Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/educacion/web/servicios/atencion_diversidad/instrucciones-26-27/"
fecha_consulta: 2026-04-26
estado_fuente: "Activa"
---
# FTE-034 — Instrucciones Diversidad 26/27
```

- [ ] **Step 4: Commit**
```bash
git add 01_fuentes/portales-oficiales/FTE-032-* 01_fuentes/portales-oficiales/FTE-033-* 01_fuentes/portales-oficiales/FTE-034-*
git commit -m "feat: añadir fuentes de resoluciones anuales de diversidad"
```

### Task 4: Fichas Normativas de Decretos y Órdenes (NOR-024 a NOR-028)

**Files:**
- Create: `02_normativa/canarias/decretos/NOR-024-decreto-25-2018-diversidad.md`
- Create: `02_normativa/canarias/decretos/NOR-025-decreto-9-2022-admision.md`
- Create: `02_normativa/canarias/ordenes/NOR-026-orden-7-junio-2007-diversidad.md`
- Create: `02_normativa/canarias/ordenes/NOR-027-orden-13-diciembre-2010-neae.md`
- Create: `02_normativa/canarias/ordenes/NOR-028-orden-3-marzo-2022-admision.md`

- [ ] **Step 1: Crear NOR-024 a NOR-028 con frontmatter completo**
- [ ] **Step 2: Commit**
```bash
git add 02_normativa/canarias/decretos/NOR-024-* 02_normativa/canarias/decretos/NOR-025-* 02_normativa/canarias/ordenes/NOR-026-* 02_normativa/canarias/ordenes/NOR-027-* 02_normativa/canarias/ordenes/NOR-028-*
git commit -m "feat: añadir fichas normativas de decretos y órdenes de diversidad y admisión"
```

### Task 5: Fichas Normativas de Resoluciones (NOR-029 a NOR-032)

**Files:**
- Create: `02_normativa/canarias/resoluciones/NOR-029-resolucion-instrucciones-diversidad-24-25.md`
- Create: `02_normativa/canarias/resoluciones/NOR-030-resolucion-instrucciones-diversidad-25-26.md`
- Create: `02_normativa/canarias/resoluciones/NOR-031-resolucion-instrucciones-diversidad-26-27.md`
- Create: `02_normativa/canarias/resoluciones/NOR-032-resolucion-admision-26-27.md`

- [ ] **Step 1: Crear NOR-029 a NOR-032 con frontmatter completo**
- [ ] **Step 2: Commit**
```bash
git add 02_normativa/canarias/resoluciones/NOR-029-* 02_normativa/canarias/resoluciones/NOR-030-* 02_normativa/canarias/resoluciones/NOR-031-* 02_normativa/canarias/resoluciones/NOR-032-*
git commit -m "feat: añadir fichas normativas de resoluciones anuales"
```

### Task 6: Actualización de Índices (fuentes.yaml, normativa.yaml)

**Files:**
- Modify: `06_indices/fuentes.yaml`
- Modify: `06_indices/normativa.yaml`

- [ ] **Step 1: Actualizar fuentes.yaml con las 9 nuevas fuentes**
- [ ] **Step 2: Actualizar normativa.yaml con las 9 nuevas normas**
- [ ] **Step 3: Commit**
```bash
git add 06_indices/*.yaml
git commit -m "docs: actualizar índices de fuentes y normativa con TAREA-016"
```

### Task 7: Relaciones Normativas (REL-020 a REL-025)

**Files:**
- Create: `05_relaciones/normativa/REL-020-decreto-diversidad-desarrolla-ley.yaml`
- Create: `05_relaciones/normativa/REL-021-resolucion-diversidad-instrucciones.yaml`
- Create: `05_relaciones/normativa/REL-022-decreto-admision-desarrolla-ley.yaml`

- [ ] **Step 1: Crear archivos YAML de relaciones**
- [ ] **Step 2: Actualizar 06_indices/relaciones.yaml**
- [ ] **Step 3: Commit**
```bash
git add 05_relaciones/normativa/*.yaml 06_indices/relaciones.yaml
git commit -m "feat: establecer relaciones normativas de diversidad y admisión"
```

### Task 8: Cierre de TAREA-016 y Actualización de Estatus

**Files:**
- Modify: `08_tareas/backlog/TAREA-016-inventariar-atencion-diversidad-y-alumnado.md`
- Modify: `status.yaml`
- Modify: `TODO.md`

- [ ] **Step 1: Marcar TAREA-016 como hecha**
- [ ] **Step 2: Actualizar status.yaml**
- [ ] **Step 3: Actualizar TODO.md**
- [ ] **Step 4: Commit final**
```bash
git add 08_tareas/backlog/TAREA-016-* status.yaml TODO.md
git commit -m "task: completar TAREA-016 inventario diversidad y alumnado"
```
