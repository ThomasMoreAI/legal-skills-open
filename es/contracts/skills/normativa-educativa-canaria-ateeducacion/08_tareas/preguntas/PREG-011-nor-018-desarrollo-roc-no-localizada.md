---
id: PREG-011
titulo: "NOR-018 parece confundir dos normas reales: la Orden de EOEP de 2010 y la Orden de desarrollo del ROC de 2013"
estado: "Resuelta"
fecha_registro: 2026-08-05
fecha_resolucion: 2026-08-05
relacionadas: [NOR-018, NOR-009, NOR-076, NOR-077, FTE-013, FTE-083, FTE-084, REL-061, REL-062, TAREA-084, TAREA-085, PREG-010, PREG-012, DEC-0011]
---

# PREG-011 — La Orden de desarrollo del ROC no es de 2010

## Contexto

`NOR-018` declara una «Orden de 1 de septiembre de 2010, por la que se desarrolla el Reglamento
Orgánico de los centros docentes públicos no universitarios de la Comunidad Autónoma de Canarias,
respecto de los Institutos de Educación Secundaria», publicada en el BOC n.º 178 de 10 de
septiembre de 2010, con `nivel_evidencia: confirmado-fuente-primaria`.

El boletín declarado **sólo contiene anuncios**: no hay en él ninguna disposición general. Se
recorrieron después los sumarios de **los 257 boletines del BOC de 2010** sin encontrar esa
orden.

Lo que sí existe son dos normas distintas, ambas verificadas en el sumario oficial:

| Norma | Publicación | Objeto |
| --- | --- | --- |
| Orden de **1 de septiembre de 2010** | BOC 2010/181, `BOC-A-2010-181-5207` | Desarrolla la organización y funcionamiento de los **equipos de orientación educativa y psicopedagógicos** de zona y específicos |
| Orden de **9 de octubre de 2013** | BOC 2013/200, `BOC-A-2013-200-5076` | Desarrolla el **Decreto 81/2010**, por el que se aprueba el Reglamento Orgánico de los centros docentes públicos no universitarios |

`NOR-018` toma la fecha de la primera y el objeto de la segunda.

El índice de normativa clasificada de la Inspección confirma que la norma de desarrollo del
Decreto 81/2010 es la de 9 de octubre de 2013.

## La duda

¿`NOR-018` debe corregirse para describir la Orden de 9 de octubre de 2013, o retirarse y
catalogarse esa orden con un identificador nuevo?

La regla R10 impide reutilizar identificadores, pero no impide corregir el contenido de una
ficha. La diferencia práctica es si algún consumidor externo ha citado ya `NOR-018` creyendo que
era la norma de 2010: en ese caso conviene retirarla y crear ficha nueva, para que la corrección
sea visible en lugar de silenciosa.

Conviene además valorar si la Orden de 1 de septiembre de 2010 sobre los EOEP merece ficha
propia: es normativa educativa canaria vigente y hoy no está en el corpus.

## Efecto mientras tanto

`NOR-018` queda en `Pendiente de verificación` y con `nivel_evidencia: pendiente-verificacion`.
Su copia local lleva advertencia de que no debe usarse.

## Respuesta (2026-08-05)

**Se retira la ficha y se catalogan las dos normas reales.** `DEC-0011` fija el criterio: una
ficha que confunde dos normas no se corrige en el sitio, porque quien la haya citado seguiría
creyendo que describe lo que decía, y porque la corrección silenciosa borra el rastro del error.

- `NOR-076` — Orden de **9 de octubre de 2013**, que desarrolla el Decreto 81/2010 (`NOR-009`).
  Aporta el objeto que `NOR-018` describía. Unifica en una sola norma lo que antes estaba en dos
  órdenes de 2006, una para Infantil y Primaria y otra para IES, y fija los parámetros que un
  equipo directivo aplica a diario: 25 horas semanales de horario del alumnado en Primaria y 30
  en Secundaria, jornada docente de 37,5 horas, plazos de reclamación de horarios y el umbral del
  15 % de inasistencia injustificada para el informe mensual de absentismo. Relaciones
  registradas: `REL-061` (desarrolla `NOR-009`) y `REL-062` (modifica el artículo 24.2 de
  `NOR-025`).
- `NOR-077` — Orden de **1 de septiembre de 2010**, sobre los equipos de orientación educativa y
  psicopedagógicos. Aporta la fecha que `NOR-018` usaba. Regula quién realiza la evaluación
  psicopedagógica del alumnado NEAE y cómo, con diez anexos de modelos documentales, y completa
  el marco NEAE junto a `NOR-024`, `NOR-025` y `NOR-026`.

Sobre si la Orden de EOEP merecía ficha propia: sí. Es normativa vigente que el corpus no tenía,
y su ausencia era justamente lo que hacía difícil detectar la confusión.
