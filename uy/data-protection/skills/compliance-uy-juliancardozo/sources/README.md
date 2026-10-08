# Fuentes oficiales (`/sources`)

Esta carpeta es la **fuente de verdad normativa** de `compliance-uy`. Toda afirmación
legal del proyecto (en `references/controls.md`, en `packs/`, en los `templates/` y en los
documentos generados en `.compliance/`) debe poder rastrearse hasta un archivo de esta
carpeta, citando **norma + artículo + archivo local**.

## Reglas de citación del proyecto

1. Cada afirmación normativa se cita como: `(Norma, art. N — sources/archivo.md)`.
2. Todo lo que **no** pueda verificarse contra una fuente oficial uruguaya se marca con
   el literal `[verificar contra fuente oficial]`.
3. **No se copia texto legal de otras jurisdicciones** (p. ej. de `compliance-cl`). Las
   normas chilenas, españolas o europeas pueden citarse solo como antecedente doctrinario,
   nunca como base de una obligación uruguaya.
4. Los archivos `.md` de esta carpeta contienen **citación canónica + URL oficial + fecha de
   consulta + índice de artículos relevantes parafraseados**. El **texto íntegro oficial**
   de cada norma debe descargarse del enlace indicado y colocarse junto al `.md`
   correspondiente (p. ej. `sources/ley-18331.oficial.pdf`). Ver `scripts`/instrucciones en
   cada archivo.

## Por qué no se incluye el texto completo en el repo

Los textos legales se publican y actualizan en las bases oficiales (IMPO, Parlamento,
gub.uy). Para evitar versiones desactualizadas o transcripciones con errores, el repo
guarda **la referencia y el índice**, y deja la descarga del texto íntegro al usuario,
contra la fuente oficial vigente al momento de la auditoría.

## Inventario de fuentes

| Archivo | Norma / documento | Emisor | Fecha |
|---|---|---|---|
| `ley-18331.md` | Ley N° 18.331 — Protección de Datos Personales y Acción de Habeas Data | Poder Legislativo | 11/08/2008 |
| `ley-19670-arts-37-40.md` | Ley N° 19.670, arts. 37 a 40 (modifican el régimen de datos) | Poder Legislativo | 15/10/2018 |
| `decreto-414-009.md` | Decreto N° 414/009 — Reglamentario de la Ley 18.331 | Poder Ejecutivo | 31/08/2009 |
| `decreto-64-020.md` | Decreto N° 64/020 — Reglamenta arts. 37-40 de la Ley 19.670 | Poder Ejecutivo | 17/02/2020 |
| `urcdp-guias.md` | Guías y resoluciones de la URCDP (AGESIC) | URCDP | varias |

## Nota sobre numeración de artículos

Las distintas ediciones electrónicas de la Ley 18.331 muestran **discrepancias de
numeración** en el bloque de derechos del titular (información / acceso / rectificación /
comunicación). Donde existe esa duda, este proyecto cita el número y agrega
`[verificar numeración exacta contra fuente oficial]`. La numeración debe confirmarse contra
el texto consolidado vigente de IMPO antes de usar los documentos generados con valor legal.
