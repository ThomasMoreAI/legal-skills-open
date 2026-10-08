# Diario — 2026-05-22: TAREA-057 pipeline de vigilancia de normativa canaria

## Trabajo realizado

- Creado el scanner `11_calidad/monitor/scan_normativa.py` que vigila el portal
  oficial (FTE-001 + normativa clasificada FTE-013/014/015), diffea contra los
  índices y un snapshot, y reporta solo novedades. Modos `--dry-run` y `--seed`.
- Añadidos `11_calidad/monitor/requirements.txt`, `README.md` y el snapshot
  `portal-normativa-canaria.seen.json`, sembrado con el baseline actual (63 URLs).
- Creado el workflow `.github/workflows/monitor-normativa.yml` (cron semanal +
  manual): escanea, convierte PDFs con DocDigester2MD
  (`ghcr.io/ateeducacion/docdigester2md`, GitHub Models por defecto), sella los
  borradores con la cabecera R16 en `07_corpus_ia/_borradores-monitor/` y abre un
  PR etiquetado `monitor-normativa`.
- Documentada la carpeta `07_corpus_ia/_borradores-monitor/` como material no
  validado.

## Justificación

Hasta ahora las altas eran manuales y las novedades del portal podían pasar
semanas sin detectarse. El pipeline avisa de forma proactiva sin sustituir la
fuente oficial ni afirmar vigencia: el alta final sigue siendo supervisada
(AGENTS.md §7–§8), por lo que respeta R1–R5. Al trabajar por PR, nada llega a
`main` sin revisión.

## Verificación

- `python3 -m py_compile 11_calidad/monitor/scan_normativa.py` → OK.
- `--dry-run` contra el portal: 68 candidatas, 133 catalogadas, 0 nuevas tras el
  seed; al borrar una entrada del snapshot reaparece exactamente esa URL.
- Índices `status.yaml` y `06_indices/tareas.yaml` parsean con `yaml.safe_load`.

## IDs consumidos

- TAREA-057.
- No se han consumido IDs FTE/NOR/REL/CHUNK: el pipeline solo detecta y avisa.

## Coordinación con trabajo paralelo

- `git fetch origin main && git pull --rebase` antes de iniciar.
- Solo se han tocado ficheros nuevos del monitor más los bloques propios de
  TAREA-057 en `status.yaml` y `06_indices/tareas.yaml`.
