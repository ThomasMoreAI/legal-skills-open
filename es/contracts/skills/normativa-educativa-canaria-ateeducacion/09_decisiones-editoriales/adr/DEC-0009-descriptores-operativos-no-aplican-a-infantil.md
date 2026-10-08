---
id: DEC-0009
titulo: "Los descriptores operativos no aplican a Educación Infantil"
estado: "Aceptada"
fecha: 2026-08-05
relacionadas: [DEC-0004, DEC-0007, DEC-0008, NOR-047, CUR-034, CUR-035, CUR-036, TAREA-069, TAREA-076]
---

# DEC-0009 — Los descriptores operativos no aplican a Educación Infantil

## Contexto

`DEC-0004` fijó cuatro elementos obligatorios para toda ficha curricular, el cuarto de ellos la
vinculación con los descriptores operativos del perfil de salida. `DEC-0008` los modeló como
mapa por curso. Ninguna de las dos distinguió por etapa.

Al preparar la extracción de Infantil (`TAREA-069`) se comprobó contra el PDF oficial completo
del Decreto 196/2022 que **esos descriptores no existen en esa etapa**:

- cero apariciones de «descriptor»;
- cero de «perfil de salida»;
- cero códigos numerados del tipo `CCL1` o `STEM4` en todo el decreto.

No es una carencia del corpus ni un fallo de extracción. El **Perfil de salida es de la enseñanza
básica**, y la Educación Infantil no forma parte de ella. El Anexo 1 del decreto, «Competencias
clave en la Educación Infantil», describe las ocho competencias clave **solo en prosa**, sin
descriptores asociados ni numeración.

## Decisión

El cuarto elemento de `DEC-0004` —la vinculación con descriptores operativos— **no se exige a las
fichas curriculares de Educación Infantil**. Una ficha de Infantil puede estar en
`estado_extraccion: completado` sin `elementos.descriptores_operativos` y sin `descriptores` en
sus competencias.

Los tres elementos restantes siguen siendo obligatorios: competencias específicas con su
numeración oficial, criterios de evaluación y saberes básicos.

## Consecuencias

- `CUR-034`, `CUR-035` y `CUR-036` no pueden ni deben tener descriptores. `TAREA-069` se cerró
  por no proceder, no por quedar pendiente.
- El criterio de completitud pasa a depender de la etapa. Recapitulando lo que ya recogía
  `DEC-0007` y añadiendo esta excepción, los modelos vigentes son tres:

  | Ámbito | Elementos que definen la completitud |
  | --- | --- |
  | Régimen general (Primaria, ESO, Bachillerato) | Los cuatro de `DEC-0004` |
  | **Educación Infantil** | **Los tres primeros; los descriptores no existen** |
  | Formación Profesional (LOFP 3/2022) | Módulos profesionales con resultados de aprendizaje y criterios |

- Cualquier herramienta que mida la completitud curricular debe consultar la etapa antes de
  exigir descriptores.

## Motivo

Exigir un elemento que la fuente oficial no contiene obligaría a dejar tres fichas
permanentemente incompletas por una carencia inexistente, o —peor— a rellenarlas con descriptores
tomados de otra etapa, lo que sería inventar contenido normativo contra R1.

## Revisión futura

Si una norma posterior extendiera el perfil de salida a Educación Infantil, esta decisión decae y
las tres fichas pasarían a estar incompletas hasta volcarlos.
