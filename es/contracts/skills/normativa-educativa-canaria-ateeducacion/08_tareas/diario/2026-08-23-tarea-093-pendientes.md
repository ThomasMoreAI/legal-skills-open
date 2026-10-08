# Diario — 2026-08-23: Pendientes del corpus resueltos o trazados (TAREA-093)

## Qué se ha hecho

### 1. Fichas históricas del backlog

Reconstruidas las 15 fichas que constaban en el índice sin ficha propia
(TAREA-028, 030-036, 046-052), generadas desde `06_indices/tareas.yaml` con
nota expresa de reconstrucción (sin contenido inventado, R1) y `ruta` añadida
al índice sustituyendo la marca `ficha: null` de DEC-0007.

### 2. Verificación de los marcadores [PENDIENTE] (32 en ~24 fichas)

Verificación contra fuentes oficiales del BOC y BOE con fecha 2026-08-23:

- **NOR-076**: verificadas dos modificaciones; catalogadas como `NOR-111`
  (Orden 16/07/2019, BOC 2019/145, anuncio 3854) y `NOR-112` (Orden
  28/09/2023, BOC 2023/201, anuncio 3291), con fuentes `FTE-118`/`FTE-119` y
  relaciones `REL-087`/`REL-088`. Sin modificación localizada del art. 24.2.
- **NOR-077**: verificada su modificación puntual por la disp. adic. undécima
  de la Orden de 13/12/2010 → `REL-089`; vigente sin norma que la sustituya.
- **NOR-074/075/078**: cuerpos desactualizados — las resoluciones que decían
  «no catalogada» ya lo están (`NOR-094`, `NOR-095`, `NOR-096`, `NOR-085`,
  `NOR-081`, `NOR-080`). Marcadores retirados.
- **NOR-087/088/090**: identificadas las resoluciones hermanas (`NOR-089`,
  091-093; BOC n.º 45 anuncios 733-736 y n.º 46 anuncio 750); las cláusulas de
  vigor indeterminables pasan a `[INTERPRETACIÓN]` y las no-derogaciones se
  documentan como hechos verificados.
- **NOR-082**: verificado que no hay cláusula de vigor ni modificación posterior.
- **NOR-101**: verificado que no existe desarrollo canario; corrección de fecha
  del real decreto (9 de julio, BOE 10/07/2024).
- **NOR-072**: marcadores desactualizados — RD 157/2022 ya es `NOR-079` y la
  copia local R16 existe desde 2026-08-05.
- **Portales FTE-057..067**: vinculados con sus objetivos existentes
  (`relacionadas` actualizadas); los objetivos aún sin catalogar quedan
  registrados en `TAREA-094`.

### 3. PREG-013 (resuelta)

El Gobierno de Canarias **no tiene dominio ELI propio** (404 en patrones
probados; sin proyecto ELI en el directorio oficial de `elidata.es` pese a
tener la jurisdicción `es-cn` registrada). El BOE asigna URIs
`boe.es/eli/es-cn/...` solo a parte de la normativa canaria (leyes sí;
el Decreto 30/2023 no tiene ELI). Regla práctica documentada: URL canónica del
BOC + ficha JurisCan; URIs es-cn caso por caso con verificación individual.

## IDs consumidos

- `TAREA-093` (esta tarea), `TAREA-094` (deuda catalogación), `FTE-118`,
  `FTE-119`, `NOR-111`, `NOR-112`, `REL-087`, `REL-088`, `REL-089`.

## Estado final

Validador: **0 errores · 0 avisos**. Deuda viva: TAREA-094 (catalogación,
prioridad Media).
