# AGENTS.md

## 1. Propósito

Corpus Markdown/YAML de normativa educativa y currículos aplicables en Canarias, para consulta humana y para IA. No sustituye la fuente oficial.

## 2. Antes de editar

Si vas a crear entidades o a hacer commit, abre [`.agents/references/trabajo-paralelo.md`](.agents/references/trabajo-paralelo.md). No hace falta leer `README.md`, `status.yaml` ni las plantillas para una corrección puntual. No toques los archivos de una `TAREA-NNN` que esté `En progreso` y no sea la tuya.

## 3. Reglas de evidencia

Todo dato normativo se rastrea hasta una fuente oficial: nombre, localización, fecha de consulta y ficha interna.

- R1. No se crea contenido normativo sin fuente oficial.
- R2. Todo resumen indica que no sustituye la fuente oficial.
- R3. Toda norma tiene estado de vigencia.
- R4. Toda ficha tiene fecha de consulta.
- R5. Todo análisis tiene fecha de análisis.
- R6. Toda relación normativa se registra en YAML.
- R7. El material para IA es breve, trazable y fiel.
- R8. No se mezclan normas con orientaciones que no son norma.
- R9. No se borran normas derogadas; se marcan.
- R10. Los IDs son estables, correlativos y no se reutilizan.
- R11. Los índices YAML se actualizan con cada fuente, norma, currículo o chunk.
- R12. Las dudas se registran como `PREG-NNN`.
- R13. Las interpretaciones se marcan con `[INTERPRETACIÓN]`.
- R14. Las hipótesis se marcan con `[HIPÓTESIS]`.
- R15. Lo pendiente se marca con `[PENDIENTE]`.
- R16. Toda copia local de texto completo indica URL oficial, fecha de consulta, fecha de exportación y que no sustituye la fuente oficial.

## 4. Carpetas

- `01_fuentes/`: portales, BOE, BOC y otras fuentes oficiales.
- `02_normativa/`: una ficha por norma.
- `03_curriculos/`: fichas curriculares.
- `04_analisis/`: notas y síntesis.
- `05_relaciones/`: relaciones entre normas y currículos.
- `06_indices/`: índices YAML por ID.
- `07_corpus_ia/`: resúmenes, chunks y textos rápidos.
- `08_tareas/`: tareas, diario y preguntas.
- `09_decisiones-editoriales/`: decisiones del corpus.
- `10_plantillas/`: plantillas.
- `11_calidad/`: validación, enlaces y vigencia.

## 5. Formato

Las claves de primer nivel del frontmatter empiezan en la columna 0. Lo anidado usa dos espacios. Los `---` y el cuerpo Markdown también empiezan en la columna 0. Las fichas nuevas salen de `10_plantillas/`. Los índices son mapas por ID. El detalle de cada alta está en [`.agents/references/altas.md`](.agents/references/altas.md).

## 6. Skills

`.agents/skills/` es el árbol canónico. `.claude/skills/` es una copia completa, archivo por archivo. Al cambiar un skill local, deja las dos copias iguales:

```bash
rsync -a --delete --exclude .DS_Store --exclude .venv .agents/skills/ .claude/skills/
```

Los que se cargan solos:

- `catalogacion-fuentes`, `analisis-normativo`, `analisis-curricular`.
- `control-vigencia`, `relaciones-normativas`, `preparacion-corpus-ia`, `control-calidad-documental`, `publicacion-portal`.
- `lenguaje-claro`: prosa en castellano. En una cita de norma, solo señala.
- `legalize-es`: texto consolidado de [legalize-dev/legalize-es](https://github.com/legalize-dev/legalize-es). El clon va a `.legalize-es/` y no se versiona. Dentro solo `grep`, `git log`, `git show` y `git diff`. La cita se contrasta con el BOE.

Las lentes de etapa y de ámbito están en `references/` de `analisis-normativo` y de `analisis-curricular`. Los directorios `experto-*` y `perfil-docente` que quedan al lado solo tienen un `LEEME.md`, para las rutas que ya citan las tareas. No son skills.

La skill pública para asistentes de fuera está en [`skills/experto-normativa-educativa-canaria/SKILL.md`](skills/experto-normativa-educativa-canaria/SKILL.md), la ruta que reconoce `gh skill install`. El portal la sirve como `SKILL.md`. No es lo mismo que `experto-normativa-canaria`.

Los skills de terceros se instalan con `gh skill install OWNER/REPO PATH --dir .agents/skills`. El origen está en [`.agents/upstream-skills.txt`](.agents/upstream-skills.txt). Se mantienen verbatim. [`.github/workflows/update-agent-skills.yml`](.github/workflows/update-agent-skills.yml) los actualiza cada lunes y abre un PR. No fusiona solo.

| Skill | Origen | Licencia |
| --- | --- | --- |
| `github-actions-hardening` | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) `skills/github-actions-hardening` | MIT |

El aviso del corpus legal está en [`.agents/licenses/legalize-es-NOTICE.txt`](.agents/licenses/legalize-es-NOTICE.txt).

## 7. Cierre

Una tarea pasa a `Hecha` con fuente oficial, fecha de consulta, formato válido, entrada en el índice, ID correcto y, si es norma, estado de vigencia. Las dudas quedan en `PREG-NNN` y el cambio queda en el diario. El validador es `python3 11_calidad/validar_corpus.py`, con 0 errores.
