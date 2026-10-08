# Legal Compliance — Dominio

## Por qué existe esta skill

Los proyectos de software tienen obligaciones legales que a menudo se
descubren tarde (en producción, ante una reclamación, o en una auditoría
externa). Esta skill permite detectar incumplimientos normativos en fase
de diseño, antes de que generen riesgo real, cruzando las reglas del
proyecto contra la legislación española consolidada.

## Conceptos de dominio

- **Norma consolidada**: texto legal con todas las reformas integradas
  en un solo documento Markdown (fuente: legalize-es, BOE).
- **ELI**: European Legislation Identifier — URL canónica única de cada norma.
- **Rango regulatorio**: jerarquía normativa que determina prevalencia
  (Constitución > LO > Ley > RD > Orden > Resolución).
- **CCAA**: Comunidad Autónoma — legislación regional que complementa
  la estatal. 17 jurisdicciones en legalize-es.
- **Base legal**: fundamento jurídico que habilita una actividad
  (ej: Art. 6.1 RGPD para tratamiento de datos).

## Reglas de negocio que implementa

- Trazabilidad regla→artículo: cada regla de negocio debe poder
  vincularse a al menos un artículo de legislación vigente.
- Priorización por rango normativo: una LO prevalece sobre un RD.
- Solo legislación vigente: filtrar `status: "in_force"` del frontmatter.
- Disclaimer obligatorio en todo output: no es asesoramiento jurídico.
- Máximo 10 normas por auditoría para respetar budget de contexto.

## Relación con otras skills

- **Upstream**: `regulatory-compliance` (detección sectorial alimenta
  la selección de dominios legales a auditar).
- **Downstream**: `spec-driven-development` (specs incluyen constraints
  legales descubiertos por esta skill).
- **Downstream**: `governance-enterprise` (hallazgos alimentan la
  matriz de controles y el registro de decisiones).
- **Paralelo**: `adversarial-security` (ciberseguridad tiene base
  legal en ENS y NIS2, complementarios).

## Decisiones clave

- **Grep sobre embeddings**: el corpus legislativo es estable,
  estructurado y tiene frontmatter YAML. La búsqueda por grep es
  determinista, reproducible y no requiere dependencias externas.
  Alineado con Principio #2 (independencia del proveedor).
- **No incluir jurisprudencia v1**: las sentencias requieren un parser
  diferente y cambian la naturaleza del output (de cumplimiento a
  riesgo procesal). Planificado para fases futuras.
- **Legislación local (no cloud)**: legalize-es se clona localmente.
  Funciona offline. Los datos legislativos son públicos (dominio
  público), pero el input del proyecto puede ser N4.
