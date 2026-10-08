# GitHub Pages y documentos públicos

Este directorio contiene la versión estática y mantenible del panel público del repositorio.

## Contenido principal

- `index.html`: panel principal del corpus.
- `assets/css/site.css`: estilos estáticos.
- `assets/js/site.js`: filtro cliente sin backend.
- `esquema-datos/`, `guias/`, `metodologia/`: documentación complementaria, incluida la estrategia de interoperabilidad jurídica y el perfil YAML portable.
- `datos/catalogo.jsonld`, `datos/legislacion.jsonld`, `datos/curriculos.jsonld`, `datos/fuentes.jsonld`: catálogo y grafos semánticos generados en JSON-LD.
- `datos/akoma-ntoso/`: pilotos estructurales delimitados y validados de Akoma Ntoso.

`llms.txt`, `llms-full.txt` y `skill.md` no se almacenan aquí. Tienen su única copia canónica en la raíz del repositorio o en `skills/`, y se publican como `https://ateeducacion.github.io/normativa_educativa_canaria/llms.txt`, `…/llms-full.txt` y `…/skill.md` mediante el flujo de trabajo `Publicar GitHub Pages`.

## Publicación con GitHub Actions

El sitio se construye y despliega con `.github/workflows/pages.yml`. El flujo:

1. Toma todo el contenido de `docs/`.
2. Copia al artefacto Pages los ficheros Markdown/YAML públicos del corpus (`README.md`, `index.md`, `status.yaml`, `AGENTS.md`, `00_gobierno-repositorio/`, `01_fuentes/`, `02_normativa/`, `03_curriculos/`, `05_relaciones/`, `06_indices/`, `07_corpus_ia/`, `09_decisiones-editoriales/` y `schemas/`).
3. Copia `llms.txt`, `llms-full.txt` y la skill canónica al artefacto Pages.
4. Sube el artefacto y lo despliega en GitHub Pages.

Para activar la publicación una vez:

1. Abra la configuración del repositorio en GitHub.
2. Entre en **Pages**.
3. En **Build and deployment**, seleccione **GitHub Actions** como origen.
4. Guarde los cambios.
5. El primer push a `main` que toque `docs/`, `llms.txt`, `llms-full.txt`, `skills/experto-normativa-educativa-canaria/SKILL.md` o el propio workflow lanzará el despliegue. También se puede lanzar a mano desde la pestaña **Actions** con **Run workflow**.

## URLs públicas esperadas

- `https://ateeducacion.github.io/normativa_educativa_canaria/`
- `https://ateeducacion.github.io/normativa_educativa_canaria/llms.txt`
- `https://ateeducacion.github.io/normativa_educativa_canaria/llms-full.txt`
- `https://ateeducacion.github.io/normativa_educativa_canaria/skill.md`
- `https://ateeducacion.github.io/normativa_educativa_canaria/06_indices/curriculos.yaml`
- `https://ateeducacion.github.io/normativa_educativa_canaria/06_indices/textos-oficiales.yaml`
- `https://ateeducacion.github.io/normativa_educativa_canaria/07_corpus_ia/textos-completos/texto-oficial-NOR-005-decreto-30-2023.txt`
- `https://ateeducacion.github.io/normativa_educativa_canaria/03_curriculos/eso/materias/CUR-001-biologia-y-geologia.md`
- `https://ateeducacion.github.io/normativa_educativa_canaria/03_curriculos/eso/materias/CUR-001-biologia-y-geologia.yaml`
- `https://ateeducacion.github.io/normativa_educativa_canaria/datos/catalogo.jsonld`
- `https://ateeducacion.github.io/normativa_educativa_canaria/datos/legislacion.jsonld`
- `https://ateeducacion.github.io/normativa_educativa_canaria/schemas/norma.schema.yaml`

## Notas de mantenimiento

- El bloque de inventario de `README.md`, la sección «Foto Indexada» de `llms.txt` y `docs/datos/inventario.json` se generan desde `06_indices/`. Después de modificar los índices, ejecute `python3 11_calidad/generar_inventario.py --write`; el flujo de validación comprueba que no queden desactualizados.
- El catálogo JSON-LD, el grafo de legislación, el bloque estructurado de `index.html` y el piloto Akoma Ntoso se generan desde las fichas normativas. Después de modificarlas, ejecute `python3 11_calidad/generar_interoperabilidad.py --write`; CI comprueba su correspondencia exacta.
- Edite `llms.txt` y `llms-full.txt` sólo en la raíz, y la skill pública sólo en `skills/experto-normativa-educativa-canaria/SKILL.md`. No existe una segunda copia en `docs/`; el despliegue los añade al sitio publicado, la skill como `SKILL.md` y `skill.md`.
- Si necesita previsualizar el sitio en local, copie temporalmente esos dos archivos a `docs/` o use el mismo procedimiento que el workflow.
- Para añadir páginas nuevas al sitio, añada el archivo dentro de `docs/` y actualice la navegación de `index.html` si procede.
