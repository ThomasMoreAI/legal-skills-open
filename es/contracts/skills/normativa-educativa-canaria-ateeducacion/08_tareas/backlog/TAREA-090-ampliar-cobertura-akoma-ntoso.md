---
id: TAREA-090
titulo: "Ampliar la cobertura Akoma Ntoso: artículos 3+, normas nuevas, disposiciones y LOFP art. 2"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-22
fecha_actualizacion: 2026-08-22
fecha_cierre: 2026-08-22
relacionadas: [TAREA-088, TAREA-089, NOR-003, NOR-004, NOR-005, NOR-006, NOR-007, NOR-009, NOR-018, NOR-024, NOR-043, NOR-047, NOR-079, NOR-080]
siguiente_accion: null
---

# TAREA-090 — Ampliar la cobertura Akoma Ntoso

## Objetivo

Cinco líneas de ampliación sobre la fase piloto:

1. Artículo 3 (o siguiente relevante) de las normas ya cubiertas.
2. Artículos 1 y 2 de normas nuevas de alto impacto con copia local trazable:
   `NOR-009` (ROC), `NOR-018` (orden IES), `NOR-024` (atención a la diversidad).
3. Soporte del generador para disposiciones adicionales/finales (`tipo:`).
4. Artículo 2 de la LOFP (`NOR-007`) como párrafos numerados.
5. Todo lo anterior validado contra XSD (TAREA-089).

## Criterios de cierre

- Cada bloque nuevo contrastado con BOE o BOC; no se infiere estructura desde
  texto plano. La copia local de `NOR-018` tiene aviso del validador: se usa
  solo la fuente oficial BOC.
- Los XML se regeneran con `generar_interoperabilidad.py`; sin edición manual.
- README de pilotos, comprobaciones de `pages.yml` y catálogo actualizados.
- `--check`, validación XSD (TAREA-089) y `validar_corpus.py --sin-avisos` pasan.

## Notas

Consulta de fuentes oficiales el 2026-08-22. El alcance se limita a artículos
en prosa o listas numeradas simples; si un artículo trae tablas o anexos, se
excluye y se documenta.

## Coordinación con trabajo paralelo

Reservado el 2026-08-22 junto con TAREA-089 sobre `feat/akoma-ntoso-fase-3`.
