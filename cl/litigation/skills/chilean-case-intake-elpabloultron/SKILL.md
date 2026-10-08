---
name: chilean-case-intake-elpabloultron
title: 'Habilidad: Mesa de Entrada de Casos (chilean-case-intake)'
description: Mesa de entrada de casos chilenos. Recibe una carpeta de expediente, un texto o una consulta en lenguaje natural, clasifica la materia con reglas (Rol/RIT y palabras clave), arma el plan de herramientas de la suite, ejecuta los pasos seguros y entrega el resultado con lo que falta declarado.
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-case-intake
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: litigation
language: es
---

# Habilidad: Mesa de Entrada de Casos (chilean-case-intake)

## 📌 Principios Rectores

1. **El plan primero, la ejecución después.** Nunca se ejecuta a ciegas: primero se arma el plan,
   se muestra y recién entonces se corre. El plan es lo que se discute con el abogado; los
   resultados son consecuencia de eso.
2. **Decidir no es adivinar.** La materia y el fuero salen de señales concretas (letra del Rol/RIT,
   palabras clave, instituciones nombradas). Cuando no alcanza, se dice «no alcanza» y se enumeran
   los datos que faltan. Elegir la materia más parecida es peor que no elegir ninguna.
3. **Ningún resultado se inventa.** Un paso que falla queda anotado con su error; un paso al que le
   faltan parámetros se saltea con su motivo. Un silencio disfrazado de respuesta es el peor
   resultado posible en un expediente.
4. **El caso lo cierra un abogado.** La mesa ordena el trabajo y trae las fuentes; la decisión
   jurídica y la firma son humanas.

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill.

- **Quién lee:** el abogado que recibe el caso y, cuando corresponde, el cliente que pregunta «¿en
  qué va mi causa?». El resumen del plan está escrito para que lo entienda quien no es abogado.
- **Lenguaje claro:** el primer término técnico de cada salida va seguido de su equivalencia simple
  **entre paréntesis** la primera vez — `fuero (protección legal que impide despedir a cierta persona
  sin autorización previa del tribunal)`, `RIT/Rol (el número con que el tribunal identifica la
  causa)`. Ninguna sigla sin expandir la primera vez.
- **Salida (estructura):** primero el resumen del plan en castellano (materia, fuero, qué se va a
  hacer), después la tabla de pasos con su por qué, después lo que falta, y al final la compuerta.
- **Citas:** cada afirmación normativa o jurisprudencial va con el formato de `AGENTS.md` §2
  (`[BCN - Ley N° 21.643, Art. 2]`, `[CS - Rol N° 45.123-2021, Fecha: 15-09-2022]`). Ninguna cita
  se escribe de memoria; lo que no está verificado va marcado, no rellenado.
- **Huecos marcados:** lo que no se pudo leer, consultar o verificar va marcado (`[VERIFICAR]`,
  `[FUENTE NO RESPONDIÓ]`, `[CITA FALTANTE]`), nunca rellenado.
- **Compuerta:** todo escrito que salga de acá lleva la Compuerta de Revisión Jurídica. No se anuncia como aprobado para firmar ni para presentar.

## 📎 Formato de Citación Obligatorio

El de `AGENTS.md` §2, sin variantes: `[BCN - Código del Trabajo, Art. 161]`,
`[Dictamen DT N° 1234/15 de 2024]`, `[CS - Rol N° 45.123-2021, Fecha: 15-09-2022]`,
`[NCG CMF N° 461]`. La mesa de entrada no cita de memoria: las citas son las que trajeron las
fuentes del plan, y lo que no se alcanzó a verificar queda marcado como tal.

## 🔄 El flujo (cuatro pasos)

1. **Analizar.** `caso_analizar(entrada, tipo=..., consulta=...)` con lo que haya: una carpeta, un
   texto o una consulta. Devuelve materia, fuero probable, instituciones, el plan y lo que falta.
2. **Mostrar el plan y repreguntar.** Se muestra `resumen` tal cual. Si hay `faltantes`, se le piden
   al abogado **antes** de ejecutar: el Rol/RIT, las fechas, el RUT de las partes, una frase sobre
   de qué se trata. No se completa por deducción.
3. **Ejecutar.** `caso_ejecutar(entrada, pasos=[...])` — se pueden elegir pasos. Cada resultado trae
   su estado; los errores se muestran como errores, con la fuente que no respondió.
4. **Entregar.** Resultados por paso, lo que quedó sin hacer, y la compuerta. Si el caso lo amerita,
   el expediente A4 lo arma `compile_legal_dossier`.

## 🧭 Cómo se decide la materia (y por qué así)

La decisión es determinista, no del modelo. Las señales, en orden de fuerza:

| Señal | Peso | Ejemplo |
|---|---|---|
| Letra del Rol/RIT | Fuerte, no absoluta: los tribunales no rotulan igual en todo el país | `T-1234-2026` → laboral |
| Palabras clave de la materia | Fuerte, y hace falta que coincidan al menos dos | «despido», «finiquito», «fuero» |
| Instituciones nombradas | Fuerte para el fuero y las búsquedas | «SII», «Contraloría», «TDLC» |
| Nombre de los documentos | Media: orienta, no decide | `01_demanda_civil.pdf` |

Con una sola señal, el plan **advierte** que la materia conviene confirmarla. Con señales de dos
materias, avisa que el caso puede ser mixto.

## 📋 Ejemplos

```text
# Consulta con datos
caso_analizar("Me despidieron sin aviso previo después de 6 años, el finiquito está mal calculado.
               Causa T-1234-2026 del Segundo Juzgado de Letras del Trabajo.",
              consulta="qué indemnizaciones me corresponden")

# Carpeta de expediente
caso_analizar("/home/estudio/casos/ailin", tipo="carpeta")

# Y la ejecución de los tres primeros pasos
caso_ejecutar("Me despidieron sin aviso previo…", pasos=[1, 2, 3])
```

## 🚫 Lo que esta habilidad no hace

- **No consulta el estado de una causa por su Rol/RIT.** La suite busca jurisprudencia en el Poder
  Judicial, no expedientes: eso se pide en la Oficina Judicial Virtual y no hay conector.
- **No lee documentos escaneados al analizar.** El OCR va en la ejecución, donde ya se sabe que hay
  que pagar ese tiempo.
- **No decide el derecho aplicable ni redacta estrategia.** Encuadra, ordena las fuentes y las trae.
- **No promete plazos.** Los cómputos de días hábiles son de otro módulo, con sus reglas.

---

⚖️ **Compuerta de Revisión Jurídica:** esta habilidad ordena el trabajo y trae fuentes. Todo escrito
que salga de acá debe ser validado por un abogado habilitado antes de su firma o presentación.
