---
id: PREG-012
titulo: "NOR-050 describe una Orden NEAE de 2023 que no aparece en el BOC, y de ella depende la derogación declarada de NOR-025"
estado: "Resuelta"
fecha_registro: 2026-08-05
fecha_resolucion: 2026-08-05
relacionadas: [NOR-050, NOR-024, NOR-025, NOR-026, FTE-053, REL-047, REL-048, NOR-077, TAREA-084, TAREA-085, PREG-010, PREG-011, DEC-0011]
---

# PREG-012 — La Orden de procedimientos NEAE de 2023 no se localiza

## Contexto

`NOR-050` declara una «Orden de 29 de mayo de 2023, por la que se establecen los procedimientos
reguladores de la respuesta educativa al alumnado con necesidades específicas de apoyo educativo
en la Comunidad Autónoma de Canarias», publicada en el BOC n.º 105 de 1 de junio de 2023, con
`nivel_evidencia: confirmado-fuente-primaria`.

El boletín declarado no la contiene. Se recorrieron después los sumarios de **los 255 boletines
del BOC de 2023** buscando cualquier disposición sobre necesidades específicas de apoyo
educativo: aparece **una sola**, y es un extracto de convocatoria de ayudas de marzo de 2023.

La única Orden de 29 de mayo de 2023 de la Consejería que existe en el BOC es
`BOC-A-2023-111-1880`, que resuelve la provisión del puesto de Secretario/a de Dirección. Nada
que ver.

Las dos páginas oficiales de normativa NEAE de la Consejería siguen listando como marco
procedimental vigente el Decreto 25/2018, la Orden de 13 de diciembre de 2010 y la Resolución de
9 de febrero de 2011, sin mención de ninguna orden de 2023 que las sustituya.

## Por qué esta es la más grave de las tres

`NOR-050` no está sola en el corpus: sostiene dos relaciones y un chunk.

- `REL-048` declara que **deroga los capítulos de procedimientos de `NOR-025`**, la Orden de 13
  de diciembre de 2010. Si `NOR-050` no existe, esa derogación tampoco, y `NOR-025` sigue
  íntegramente en vigor. El corpus estaría diciendo lo contrario de lo que ocurre, que es el
  peor error posible en un corpus normativo.
- `REL-047` declara que desarrolla el Decreto 25/2018 (`NOR-024`).
- `CHUNK-00014` resume sus procedimientos como si fueran los aplicables.

Ambas relaciones se registraron con `nivel_evidencia: confirmado-fuente-primaria` y citan
localización concreta —«disposición derogatoria única», «artículo 1 y preámbulo»— de un texto que
no se ha podido encontrar.

## La duda

¿Existe alguna orden canaria de 2023 que regule los procedimientos NEAE? Si no existe, hay que
retirar `NOR-050`, `FTE-053`, `REL-047`, `REL-048` y `CHUNK-00014`, y devolver a `NOR-025` y
`NOR-026` su vigencia declarada.

## Efecto mientras tanto

`NOR-050` queda en `Pendiente de verificación`. Las dos relaciones y el chunk quedan marcados y
degradados a `pendiente-verificacion`. `NOR-025` **no** se marca como derogada: hasta que se
demuestre lo contrario, la Orden de 13 de diciembre de 2010 sigue vigente.

## Respuesta (2026-08-05)

**No existe.** La búsqueda se amplió a **2022 y 2024 completos**, además del 2023 ya barrido:
1.028 boletines. En los tres años el BOC no publica ninguna disposición sobre procedimientos de
respuesta educativa al alumnado NEAE. Sólo convocatorias de ayudas.

`NOR-050` y `FTE-053` se retiran conforme a `DEC-0011`, y `REL-047`, `REL-048` y `CHUNK-00014`
quedan sin efecto.

### Lo que se revierte

Es la parte que importa. `NOR-025` figuraba como «Superada parcialmente» y `NOR-026` declaraba
que sus procedimientos habían sido desplazados, ambas cosas por efecto de una norma que no
existe. Las dos fichas llevan ahora una rectificación expresa de vigencia.

**El marco procedimental NEAE aplicable en Canarias es el del Decreto 25/2018 (`NOR-024`), la
Orden de 13 de diciembre de 2010 (`NOR-025`) y la Resolución de 9 de febrero de 2011
(`NOR-026`)**, más la Orden de 1 de septiembre de 2010 sobre los EOEP (`NOR-077`), catalogada hoy
al resolver `PREG-011`. Es lo que sostienen las propias páginas de normativa NEAE de la
Consejería.

Las tres copias locales de ese marco se completaron además desde el PDF firmado en `TAREA-084`:
`NOR-025` pasa de 750 a 1.729 líneas y `NOR-026` de 742 a 1.689, porque a la versión HTML le
faltaban los anexos.

De dónde salió `NOR-050` sigue sin saberse. La única Orden de 29 de mayo de 2023 de la Consejería
resuelve la provisión de un puesto de Secretario/a de Dirección.
