# Diario — 2026-08-05: la deuda que el monitor escondía

## Lo que se pedía

Tres cosas sueltas que habían ido quedando: catalogar la Resolución de 30 de octubre de 2024,
catalogar el RD 157/2022, y mirar las 61 URL del monitor sin rastro en el corpus.

Las tres resultaron ser la misma cosa.

## El defecto de diseño

El monitor guarda un snapshot de URL vistas para no repetir avisos. Eso está bien. Lo que nadie
había mirado es la consecuencia: **una disposición detectada y nunca catalogada desaparece del
radar para siempre**. No vuelve a salir en ningún informe.

Había además un fallo de comparación. El monitor contrastaba URL contra URL, y la misma
disposición se publica de tres formas —PDF de la sede, HTML del boletín, texto consolidado—. Una
norma ya catalogada bajo una forma se contaba como pendiente bajo otra, y al revés.

Al cruzar snapshot y corpus por **identificador oficial** en vez de por URL aparecieron 58 URL sin
rastro desde mayo. Entre ellas el Real Decreto 659/2023, que es la norma que estructura todo el
sistema de FP y que cuatro fichas del corpus citaban sin poder enlazar.

## Un tropiezo por el camino

La primera versión del informe leía todo el Markdown del repositorio para buscar el
identificador. Al escribir la tarea con la lista de disposiciones pendientes, sus identificadores
pasaron a estar en el corpus, y el informe empezó a decir que ya estaban catalogadas. Trece
disposiciones desaparecieron del informe por haberlas mencionado.

Corregido: el informe sólo mira fuentes, normativa, currículos, relaciones e índices. Mencionar
algo en una tarea no es catalogarlo, y la herramienta que vigila la deuda no puede darse por
satisfecha con que alguien la haya escrito.

## Lo catalogado

Ocho normas, elegidas por un criterio: que otra ficha del corpus ya las citara sin poder
enlazarlas.

| Ficha | Norma | Quién la citaba |
| --- | --- | --- |
| `NOR-079` | RD 157/2022, enseñanzas mínimas de Primaria | `NOR-043`, que la desarrolla |
| `NOR-080` | RD 659/2023, ordenación del Sistema de FP | `NOR-073`, `NOR-074`, `NOR-078` y las resoluciones canarias |
| `NOR-081` | Resolución 30-10-2024, Grados D y E | `NOR-074`, `NOR-075`, `NOR-078` |
| `NOR-082` | Resolución 29-11-2024 | modifica a `NOR-081` |
| `NOR-083` | Resolución 26-03-2026 | amplía `NOR-081` |
| `NOR-084` | Resolución 17-04-2026 | corrige a `NOR-083` |
| `NOR-085` | Resolución 26-11-2025, dobles titulaciones | `NOR-075`, que declaraba modificarla |
| `NOR-086` | Resolución 02-05-2025, primer curso común | `NOR-085` |

Las tres del medio importan más de lo que parece: sin ellas, `NOR-081` figuraría en el corpus con
una redacción que ya no es la vigente. Y `NOR-084` corrige la omisión del Anexo III en la
publicación de marzo, sin el cual un itinerario de FP Adaptada no tiene distribución horaria.

Once relaciones, `REL-064` a `REL-074`, cierran la cadena. La que mejor resume el problema es
`REL-071`: `NOR-075` **decía en su propio texto** que modificaba el Anexo III de una resolución de
noviembre de 2025, pero esa resolución no existía en el corpus, así que la afirmación no se podía
seguir.

## Lo que queda, ya identificado

- **Siete resoluciones de 25 de febrero de 2026** sobre distribución horaria de los Grados C
  (Certificados Profesionales) y B (Certificados de Competencia), repartidas por familia
  profesional. El corpus no tiene representados esos dos grados: sólo D y E.
- **RD 658/2024**, que modifica el RD 659/2023 recién catalogado. Es lo más urgente de lo que
  queda: sin él, `NOR-080` no refleja su redacción vigente.
- Cinco disposiciones más del BOE sobre convalidaciones, equivalencias y certificados de
  profesionalidad.
- Nueve PDF de normativa interna de la Consejería, que antes exigen decidir si son normas u
  orientaciones: `R8` prohíbe mezclarlas.
- Cuatro resoluciones canarias que otras fichas citan y que siguen sin catalogar.

Todo eso queda en `TAREA-086`, con identificador y título de cada una, para que sea trabajo
ejecutable y no una lista de pendientes vaga.

## IDs consumidos

`FTE-086` a `FTE-093`, `NOR-079` a `NOR-086`, `REL-064` a `REL-074`, `TAREA-086`.
