---
id: TAREA-074
titulo: "Reparar el doble encodeo de las copias locales de texto oficial"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [NOR-043, NOR-047, PREG-008, TAREA-072]
---

# TAREA-074 — Reparación del doble encodeo en `07_corpus_ia/textos-completos/`

## Hallazgo

Al intentar contrastar las fichas curriculares de Primaria e Infantil contra su decreto, ninguna
competencia aparecía en el texto local. La causa no eran las fichas: **33 de las 97 copias
locales de texto oficial estaban dobles-codificadas** (UTF-8 leído como latin-1 y vuelto a
guardar como UTF-8).

El daño hacía ilegible buena parte del contenido:

- `ANEXO 1` aparecía como `ANEXOÂ 1`.
- `Competencia específica` no aparecía **ni una vez** en los textos de Primaria e Infantil,
  porque estaba escrito `Competencia especÃ­fica`.
- `Crecimiento en Armonía` era irrecuperable por búsqueda.

Los ficheros son mixtos: la cabecera que añade el proceso de exportación —con la URL oficial,
la fecha de consulta y la advertencia de R16— estaba bien codificada, y solo el cuerpo llegó
dañado. Por eso revertir el fichero entero fallaba.

## Trabajo realizado

Se añade `11_calidad/reparar_mojibake.py`, que repara únicamente los tramos que contienen la
firma del daño (`Ã` o `Â`) y solo si decodifican limpio como UTF-8. El texto sano no se toca.
Dos pasadas adicionales cubren los restos que quedan pegados a caracteres ASCII y que por eso
caen fuera de los tramos: la `Â` huérfana de un espacio duro y los indicadores ordinales
`Âº` y `Âª`.

Resultado: 33 ficheros reparados y **cero mojibake** en los 97.

Comprobación posterior: `Competencia específica` pasa de 0 a 52 apariciones en el decreto de
Primaria y de 0 a 12 en el de Infantil.

## Impacto

Estas copias son el material que alimenta la búsqueda y el RAG del corpus. Un tercio de ellas
era parcialmente inservible para búsqueda por texto sin que nada lo detectara.

## Prevención

`11_calidad/validar_corpus.py` comprueba ahora la codificación de las 97 copias locales y las
reporta como un tipo más, `TEXTOS`. La firma que busca es `Ã` o `Â` seguidos del segundo byte de
la secuencia original; exigir el par evita marcar una `Ã` legítima. Un fichero dañado devuelve
error y bloquea el cierre de tarea, con el comando de reparación en el propio mensaje.

`07_corpus_ia/textos-completos/**` se añade a las rutas que disparan el flujo de integración
continua, que antes no lo vigilaba.

## Daño residual no recuperable

Nueve de los 97 ficheros conservan caracteres `â` sueltos donde el original tenía comillas
tipográficas o puntos suspensivos. **No lo causó esta reparación**: el recuento es idéntico antes
y después —88 en el decreto de Infantil, por ejemplo—, así que el daño viene de la exportación
original.

Es irrecuperable por re-decodificación: solo queda el primer byte de la secuencia, y los dos
siguientes se perdieron. Reconstruirlos exigiría inferir qué signo había en cada caso, lo que
sería inventar. Afecta a signos de puntuación, no a palabras ni a códigos, así que no compromete
ni la búsqueda ni la cita. Se resolverá al re-exportar cada copia desde su PDF oficial.

## Pendiente

No se ha localizado la herramienta que generó estas copias: no hay ningún script de exportación
en el repositorio, y la cabecera —«Texto plano rápido generado desde el HTML oficial del BOC»—
sugiere un proceso manual o externo. Si vuelve a usarse, conviene comprobar que lee el HTML del
BOC declarando la codificación en lugar de dejar que la herramienta la adivine, que es de donde
sale este daño.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-074`. No se ha modificado ninguna ficha; solo copias locales de texto.
