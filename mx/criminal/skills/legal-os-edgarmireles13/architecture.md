# Architecture — Visión técnica

Resumen de la capa técnica y organización del sistema.

System Overview

┌─────────────────────────────┐
│        Applications         │  ← apps/
├─────────────────────────────┤
│     Legal API / SDK Layer   │
├─────────────────────────────┤
│     Rule Engine (v2 core)   │
├─────────────────────────────┤
│   Knowledge Graph + Store   │  ← knowledge/
├─────────────────────────────┤
│   Templates + Generators    │  ← templates/
├─────────────────────────────┤
│   Ingestion / ETL Pipelines │  ← scripts/
└─────────────────────────────┘

Storage & Indexing

- Raw storage: versioned JSON
- Query layer: Graph DB (Neo4j / RDF triple store)
- Indexing: Elastic / OpenSearch
- Versioning: Git + semantic versioning

Integration points

- Poder Judicial / APIs gubernamentales
- Firmas electrónicas
- Correo, calendarios y sistemas contables

Operational concerns

- Seguridad y cumplimiento (auditoría, trazabilidad)
- Alta disponibilidad y backups
- Gestión de usuarios/roles y permisos

Next steps

- Implementar capa de grafo y esquema CANONICAL
- Diseñar API de evaluación y consulta (/v1)
- Crear prototipo mínimo del motor de reglas (v2)
