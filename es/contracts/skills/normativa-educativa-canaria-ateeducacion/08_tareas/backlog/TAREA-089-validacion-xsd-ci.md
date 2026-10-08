---
id: TAREA-089
titulo: "Validar los pilotos Akoma Ntoso contra el XSD oficial en CI"
estado: "Hecha"
prioridad: "Alta"
tipo: "calidad"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-08-22
fecha_actualizacion: 2026-08-22
fecha_cierre: 2026-08-22
relacionadas: [TAREA-087, TAREA-088, TAREA-090]
siguiente_accion: null
---

# TAREA-089 — Validación XSD de Akoma Ntoso en CI

## Objetivo

Hoy la validación contra el XSD de Akoma Ntoso 3.0 (OASIS LegalDocML 1.0) es
manual y local. El objetivo es que CI valide cada XML publicado en
`docs/datos/akoma-ntoso/` en cada push y pull request.

## Criterios de cierre

- XSD oficial incorporado al repositorio con su licencia citada.
- Paso de validación (`xmllint --schema`) en
  `.github/workflows/validar-corpus.yml` para todos los XML del directorio.
- La validación falla si un piloto deja de ser conforme.

## Notas

Se prefiere vendorizar el XSD antes que descargarlo en cada ejecución de CI,
para reproducibilidad. La ampliación de contenido se gestiona en TAREA-090.

## Coordinación con trabajo paralelo

Reservado el 2026-08-22 junto con TAREA-090 sobre `feat/akoma-ntoso-fase-3`.
