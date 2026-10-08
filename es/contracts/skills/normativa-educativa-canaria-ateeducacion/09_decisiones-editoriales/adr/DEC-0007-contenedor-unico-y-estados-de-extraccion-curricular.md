---
id: DEC-0007
titulo: "Contenedor único de ficha curricular y estados de extracción"
estado: "Aceptada"
fecha: 2026-08-05
relacionadas: [PREG-007, DEC-0004, TAREA-065, TAREA-066, TAREA-067, TAREA-068, TAREA-069]
---

# DEC-0007 — Contenedor único de ficha curricular y estados de extracción

## Contexto

Al poner en marcha la validación automática (`TAREA-063`) se comprobó que las 58 fichas
curriculares en YAML seguían dos estructuras distintas:

- 26 fichas agrupaban el contenido bajo `elementos` y llevaban los metadatos completos.
- 32 fichas colocaban `competencias_especificas`, `bloques_saberes` y `criterios_evaluacion`
  directamente en la raíz y **carecían de diez campos**, entre ellos `fecha_consulta` (R4),
  `estado_vigencia` (R3) y `url_oficial`.

El problema no era cosmético. Esas 32 fichas incumplían reglas obligatorias del repositorio y,
además, ninguna declaraba `estado_extraccion`, de modo que nada advertía de que su extracción
era menos profunda: no contienen el enunciado oficial literal ni los descriptores operativos,
que es justamente lo que hace citable a una ficha curricular.

`DEC-0004` ya había fijado cuatro elementos obligatorios y previsto que las fichas incompletas
se mantuviesen en `estado_extraccion: pendiente`. Pero `pendiente` describe mal a una ficha que
tiene tres de los cuatro elementos volcados, y la propia `DEC-0004` no contempló que la
Formación Profesional no se ordena por competencias y saberes.

## Decisión

**1. Un único contenedor.** Toda ficha curricular agrupa su contenido bajo `elementos`. Se
retiran las listas de la raíz y `bloques_saberes` pasa a llamarse `saberes_basicos`.

**2. Dos modelos de contenido dentro del contenedor**, según el tipo de enseñanza:

- **Régimen general (LOMLOE)**: `competencias_especificas`, `criterios_evaluacion`,
  `saberes_basicos` y `descriptores_operativos` — los cuatro elementos de `DEC-0004`, más
  `situaciones_aprendizaje` con carácter opcional.
- **Formación Profesional (LOFP 3/2022)**: `modulos_profesionales`, con sus resultados de
  aprendizaje y criterios de evaluación por módulo, y `modulos_comunes_base` cuando el título
  vigente remita a un real decreto anterior.

Los cuatro elementos de `DEC-0004` **no se aplican a Formación Profesional**. Una ficha de FP
está completa cuando ha volcado los módulos del título correspondiente.

**3. `parcial` como estado intermedio explícito.** Se añade al vocabulario de
`estado_extraccion`, entre `pendiente` y `completado`. Una ficha es `parcial` cuando ha volcado
parte de los elementos obligatorios de su modelo, pero no todos. Esto refina la consecuencia de
`DEC-0004`, que solo contemplaba el binomio pendiente/completo.

**4. Metadatos derivados de la referencia, no inventados.** `url_oficial` y `fecha_consulta` se
toman de la ficha `FTE` que la ficha curricular ya declara en `fuente`; `estado_vigencia`, de la
`NOR` declarada en `norma_base`. Es la convención que ya seguían las fichas completas.

**5. La ficha manda sobre el índice.** Cuando `06_indices/curriculos.yaml` y la ficha discrepen
en `estado_extraccion`, `etapa`, `materia`, `norma_base` o `fuente`, la ficha es la fuente de
verdad. El validador lo comprueba en cada ejecución.

**6. Huecos documentales reconocidos.** Una entrada de índice cuya ficha nunca se escribió y no
se puede reconstruir se marca con `ficha: null` y un comentario. El hueco pasa a ser explícito e
intencionado en lugar de un descuido, y el validador deja de avisar de él. No se fabrica una
ficha para tapar el hueco: eso sería inventar lo que se hizo, contra R1.

## Consecuencias

- Las 58 fichas curriculares comparten estructura y pasan el esquema, que vuelve a exigir
  `url_oficial`, `fecha_consulta`, `estado_vigencia` y `observaciones` a todas.
- El reparto real queda: 18 fichas de ESO `completado` (4/4 elementos), 8 de FP `completado`
  según el modelo de módulos, y 32 `parcial` a la espera de sus descriptores operativos.
- Esas 32 llevan en `observaciones` una nota `[PENDIENTE]` que dice exactamente qué falta, y su
  re-extracción queda planificada en `TAREA-066` a `TAREA-069`, por etapa.
- El alias `etapa: fp` se unifica con `formacion-profesional`, el valor que ya usaban las fichas
  `NOR` en `etapas_afectadas`.
- Un consumidor del corpus —portal, RAG, export— puede fiarse de `estado_extraccion` para saber
  qué profundidad va a encontrar, en vez de deducirlo de la forma del documento.

## Alternativas descartadas

- **Dos esquemas separados** (`curriculum` y `curriculum-parcial`): institucionaliza la división
  y obliga a todo consumidor a tratar dos tipos de documento para siempre.
- **Re-extraer las 32 fichas antes de decidir**: correcto como destino, desproporcionado como
  bloqueo. Se convierte en backlog ordenado tras normalizar la estructura.

## Relación con IA

`estado_extraccion` pasa a ser el campo que un sistema RAG debe consultar antes de citar una
ficha curricular. Los chunks generados a partir de fichas `parcial` deben advertir de que la
vinculación con el perfil de salida no está volcada.
