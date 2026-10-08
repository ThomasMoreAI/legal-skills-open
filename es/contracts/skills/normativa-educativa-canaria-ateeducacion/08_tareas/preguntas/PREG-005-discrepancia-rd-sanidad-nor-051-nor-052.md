---
id: PREG-005
titulo: "Discrepancia en números de RD de ciclos de Sanidad (NOR-051 y NOR-052)"
estado: "Resuelta"
fecha_registro: 2026-04-26
fecha_resolucion: 2026-04-26
relacionadas: [NOR-051, NOR-052, CUR-046, CUR-047]
---

# PREG-005: Discrepancia en números de RD de ciclos de Sanidad (NOR-051 y NOR-052)

## Estado
Resuelta (2026-04-26)

## Pregunta
¿Son correctos los números de Real Decreto catalogados en NOR-051 (RD 1538/1995) y NOR-052 (RD 772/2014) para los títulos de Cuidados Auxiliares de Enfermería e Imagen para el Diagnóstico y Medicina Nuclear respectivamente?

## Contexto
Durante la TAREA-038 (extracción de módulos profesionales de la familia Sanidad), el agente verificó los documentos BOE correspondientes y encontró discrepancias:

### NOR-051 — Cuidados Auxiliares de Enfermería
- El número de RD catalogado en TAREA-037 fue **1538/1995** (posiblemente tomado de todofp.es).
- Al buscar en BOE.es, el agente encontró que **BOE-A-1995-13533** corresponde al **RD 546/1995** (publicado el 5 de junio de 1995, BOE núm. 133), que establece el título de Técnico en Cuidados Auxiliares de Enfermería.
- El agente también identificó **BOE-A-1995-13592** como el RD 558/1995 (currículo detallado).
- Hipótesis: el número 1538/1995 puede corresponder a un Real Decreto de currículo autonómico o a un error en el catálogo todofp.es.

### NOR-052 — Imagen para el Diagnóstico y Medicina Nuclear
- El número de RD catalogado en TAREA-037 fue **772/2014**.
- Al buscar en BOE.es, el agente encontró que **BOE-A-2014-10067** corresponde al **RD 770/2014** (publicado el 4 de octubre de 2014, BOE núm. 241), que establece el título de Técnico Superior en Imagen para el Diagnóstico y Medicina Nuclear.
- El **RD 772/2014** (BOE-A-2014-10069) corresponde al título de **Radioterapia y Dosimetría** (diferente ciclo).
- Hipótesis: el número 772/2014 puede ser un error en el catálogo todofp.es o en la catalogación de TAREA-037.

## Acción recomendada
1. Verificar directamente en BOE.es y en todofp.es los RDs correctos para ambos títulos.
2. Si se confirma la discrepancia, renombrar NOR-051 y NOR-052 con el número de RD correcto y actualizar todos los campos relacionados.
3. Actualizar CUR-046 y CUR-047 con las referencias BOE correctas.

## Respuesta (verificada en BOE.es, 2026-04-26 — TAREA-042)

### NOR-051 — Cuidados Auxiliares de Enfermería
- **RD correcto: 546/1995**, de 7 de abril.
- **BOE-A-1995-13533** — BOE núm. 133, publicado el 5 de junio de 1995.
- URL: https://www.boe.es/buscar/doc.php?id=BOE-A-1995-13533
- El RD 558/1995 (BOE-A-1995-13592, BOE núm. 134, 6 de junio de 1995) establece el currículo detallado.
- El número 1538/1995 no corresponde a este título en el BOE; era un error de catalogación.

### NOR-052 — Imagen para el Diagnóstico y Medicina Nuclear
- **RD correcto: 770/2014**, de 12 de septiembre.
- **BOE-A-2014-10067** — BOE núm. 241, publicado el 4 de octubre de 2014.
- URL: https://www.boe.es/buscar/doc.php?id=BOE-A-2014-10067
- El RD 772/2014 (BOE-A-2014-10069) corresponde al título de Radioterapia y Dosimetría (ciclo diferente).
- El número 772/2014 era un error de catalogación.

### Acciones realizadas
- Frontmatter de NOR-051 corregido: título, nombre_corto, fecha_publicacion, boe_referencia, url_oficial.
- Frontmatter de NOR-052 corregido: ídem.
- CUR-046: url_oficial actualizada a BOE-A-1995-13533.
- CUR-047: url_oficial actualizada a BOE-A-2014-10067.
- Nombres de archivo NO renombrados (estabilidad R10); pendiente en tarea futura.

## Entradas relacionadas
- `NOR-051`: Ficha del título de Cuidados Auxiliares de Enfermería — corregida a RD 546/1995.
- `NOR-052`: Ficha del título de Imagen para el Diagnóstico — corregida a RD 770/2014.
- `CUR-046`: Currículo placeholder del ciclo GM Sanidad — url_oficial actualizada.
- `CUR-047`: Currículo placeholder del ciclo GS Sanidad — url_oficial actualizada.
- `TAREA-038`: Tarea de extracción que detectó la discrepancia.
- `TAREA-042`: Tarea de resolución de esta pregunta.
