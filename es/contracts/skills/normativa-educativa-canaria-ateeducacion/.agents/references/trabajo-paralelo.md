# Trabajo en paralelo

Ábrelo cuando vayas a crear IDs o a hacer commit. Otra persona u otro agente puede estar en el repositorio a la vez. Los IDs no se reutilizan (R10).

## Antes de empezar

1. `git fetch origin main && git pull --rebase origin main`.
2. Lee en `status.yaml` qué `TAREA-NNN` están `En progreso`. No toques los archivos de una tarea ajena.
3. Calcula los siguientes IDs libres:

```bash
for p in FTE NOR REL CUR CHUNK PREG TAREA DEC; do
  last=$(grep -rhoE "${p}-[0-9]{3,5}" 06_indices 02_normativa 03_curriculos 05_relaciones 07_corpus_ia 08_tareas 09_decisiones-editoriales 01_fuentes 2>/dev/null \
         | sort -V | tail -1)
  echo "$p siguiente libre tras $last"
done
```

Anota los IDs antes de crear ficheros.

## Reserva

En cuanto sepas el ID, regístralo en su índice y haz commit pronto. Commits pequeños, uno por bloque, y push en cuanto validen.

## Antes de cada commit

1. `git fetch origin main`. Si hay commits nuevos, `git pull --rebase origin main`.
2. Vuelve a mirar los IDs libres.
3. `python3 11_calidad/validar_corpus.py` tiene que terminar con 0 errores. La primera vez hace falta `pip install pyyaml jsonschema`. El mismo validador corre en `.github/workflows/validar-corpus.yml`.

Que el YAML parsee no basta: la ficha puede cargar y aun así incumplir el esquema o faltar en el índice.

## Qué se añade al commit

Solo los archivos de esta tarea. En `status.yaml` y `06_indices/tareas.yaml`, solo el bloque de tu TAREA. No incluyas `.omc/` ni ficheros sin seguimiento de otra tarea.

## Si el ID ya existe

No lo reutilices. Renumera, actualiza frontmatter, cabeceras, referencias e índice, anótalo en el diario y vuelve a validar.
