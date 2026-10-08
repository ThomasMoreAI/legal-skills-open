---
id: DEC-0011
titulo: "Cómo se retira una ficha que describe una norma que no existe"
estado: "Aceptada"
fecha: 2026-08-05
relacionadas: [DEC-0010, NOR-017, NOR-018, NOR-050, FTE-051, FTE-053, REL-047, REL-048, PREG-010, PREG-011, PREG-012, TAREA-085]
---

# DEC-0011 — Retirada de fichas que no describen una norma real

## Contexto

El corpus tenía previsto qué hacer con una norma **derogada** (R9: no se borra, se marca) y con
un identificador que deja de usarse (R10: no se reutiliza). No tenía previsto el caso que
apareció en `TAREA-085`: una ficha que describe una norma **que nunca existió**.

Tres fichas —`NOR-017`, `NOR-018` y `NOR-050`— declaraban título, fecha de disposición, fecha de
publicación, boletín, fuente y estado de vigencia, con `nivel_evidencia:
confirmado-fuente-primaria`. Al recorrer uno a uno los sumarios de **todos los boletines del BOC
de cinco años por norma** no aparece ninguna disposición que corresponda.

`FTE-051` ya había planteado el mismo problema en `DEC-0010`, y se resolvió caso a caso. Con tres
casos más conviene fijar el procedimiento.

## Por qué no basta con marcarlas «Pendiente de verificación»

Ese estado significa «no hemos podido confirmarlo», y es el correcto mientras la búsqueda esté en
curso. Pero deja indefinidamente en el corpus una entidad que otras fichas pueden citar y que un
sistema de recuperación puede devolver. `NOR-050` lo mostró: sostenía una relación que afirmaba
la derogación de una norma que sigue vigente.

## Decisión

Una ficha se retira como **catalogación errónea** cuando se cumplen las tres condiciones:

1. La búsqueda en fuente oficial ha sido **exhaustiva y documentada**: no basta con no
   encontrarla, hay que poder decir dónde se buscó y con qué alcance.
2. Ninguna fuente oficial la respalda: ni el boletín, ni los índices de normativa de la propia
   administración, ni los repertorios consolidados.
3. Se ha registrado una `PREG-NNN` con el razonamiento y, cuando existe, la hipótesis de con qué
   se confundió.

La retirada consiste en:

- `estado_vigencia: "No normativa"` y `nivel_evidencia: "pendiente-verificacion"`.
- Un bloque `[CATALOGACIÓN ERRÓNEA]` al principio del cuerpo, con la fecha, la `PREG` y el alcance
  de la búsqueda.
- **La ficha no se borra y su identificador no se reutiliza** (R9 y R10).
- Todo lo que dependía de ella —fuentes creadas para darle respaldo, relaciones, chunks— se marca
  igual y se degrada a `pendiente-verificacion`.
- **Lo que la ficha retirada afirmaba sobre terceros se revierte.** Si declaraba derogar una
  norma, esa norma vuelve a considerarse vigente. Es la parte que más importa: retirar la ficha
  sin deshacer sus efectos deja el error donde estaba.

## Lo que la retirada no es

No es una afirmación de que la norma no exista en ningún sitio. Es una afirmación de que **el
corpus no puede sostenerla**, que es lo único que el corpus puede decir. Si aparece la fuente, la
ficha se rehabilita con la evidencia y se anota en su historia; no se crea una nueva.

Por eso el estado es `No normativa` y no un estado nuevo de tipo «inexistente»: describe lo que
la ficha es hoy dentro del corpus, no una tesis sobre el mundo.

## Cuando la ficha confunde dos normas reales

`NOR-018` no era una invención: tomaba la fecha de una orden real y el objeto de otra. En ese
caso **se catalogan las dos normas reales con identificadores nuevos** y la ficha confusa se
retira. No se «corrige en el sitio», por dos razones:

1. Una ficha cuyo contenido cambia de norma manteniendo el identificador rompe la estabilidad que
   promete R10 a quien la haya citado.
2. La corrección en el sitio es invisible. La retirada deja rastro de que hubo un error, que es
   información útil para quien haya usado el corpus antes.

## Consecuencias

- `NOR-017`, `NOR-018` y `NOR-050` quedan retiradas. `FTE-053` también, por existir sólo para dar
  fuente a la tercera.
- `REL-047` y `REL-048` quedan sin efecto. `NOR-025` y `NOR-026` recuperan su vigencia declarada:
  el marco procedimental NEAE de Canarias sigue siendo el del Decreto 25/2018 con la Orden de 13
  de diciembre de 2010 y la Resolución de 9 de febrero de 2011.
- Las dos normas que `NOR-018` confundía se catalogan como `NOR-076` —Orden de 9 de octubre de
  2013, desarrollo del Reglamento Orgánico— y `NOR-077` —Orden de 1 de septiembre de 2010, EOEP—.
- El validador no puede detectar este defecto: necesita contrastar contra el boletín, que es red.
  La comprobación vive en `11_calidad/reexportar_texto_oficial.py --auditar` y debe ejecutarse al
  catalogar y de forma periódica.

## Alternativa descartada

**Borrar las fichas.** Es lo que haría un catálogo normal, pero el corpus se lee y se cita.
Borrar deja preguntas sin respuesta a quien ya usó `NOR-050` y no encuentre explicación de por
qué desapareció. Marcar cuesta lo mismo y responde.
