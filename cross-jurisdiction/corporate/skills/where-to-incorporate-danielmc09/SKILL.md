---
name: where-to-incorporate-danielmc09
title: Where to Incorporate
description: '[JURISDICTION] Compara territorios dentro de un pais para decidir donde conviene domiciliar la empresa, cruzando incentivos, ecosistema y costo real de operar alli. Usar antes de constituir, o al evaluar si mover el domicilio de una empresa existente.'
author: Danielmc09
author_url: https://github.com/Danielmc09/jurisdiction-latam/tree/main/jurisdiction-kit/skills/where-to-incorporate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: corporate
language: es
---

# Where to Incorporate

Dónde domiciliar la empresa, con los números de cada territorio.

## La carga de la prueba

**El punto de partida es donde vives y operas. Moverse es lo que hay que
justificar, no quedarse.**

El skill no compara opciones en igualdad de condiciones. Parte de tu
territorio actual y pregunta: *¿qué gana otro territorio que compense el
costo y la fricción de estar allá?*

Si la respuesta no se puede poner en números, la respuesta es quedarse.

## La regla que ordena todo

**El incentivo es el último criterio, no el primero.**

Orden real de peso:

1. **Dónde vives y operas de verdad** — el costo de operar lejos supera casi
   siempre al beneficio
2. **Dónde están tus clientes**
3. **Dónde está o estará tu equipo**
4. **Ecosistema**: programas, capital, red
5. **Incentivos tributarios**

Un beneficio que no puedes usar no es un beneficio. La mayoría exige
presencia física, contratación local o inversión mínima.

## Requiere

- El perfil del negocio de `jurisdiction-setup`
- Pack nacional y las capas territoriales candidatas
- **La realidad del fundador**: dónde vive, dónde opera, si puede o quiere
  moverse

---

## `[CRÍTICO]` Primera pregunta: ¿hay establecimiento físico?

**Todo el análisis se bifurca aquí.** No preguntarlo produce consejo
equivocado en la mitad de los casos.

### Rama A · Negocio con establecimiento abierto al público
Local, consultorio, taller, tienda, estudio.

El territorio lo define **dónde está el local**. Domiciliar en otra ciudad
no tiene sentido: el establecimiento arrastra registro, impuesto local,
autoridad sanitaria y licencias de apertura.

Aquí la comparación de territorios **casi siempre la gana donde vas a abrir**.

### Rama B · Negocio sin establecimiento físico
Software, servicios remotos, producto digital.

**Sí puedes domiciliar en una ciudad y trabajar desde otra.** No hay
obligación automática de abrir sucursal, y el trabajo remoto no crea un
establecimiento.

Pero hay una consecuencia que casi nadie modela:

> **La dirección mueve el domicilio registral. No mueve la actividad.**

`[VERIFICAR EN EL PACK]` Dónde se entiende realizada la actividad para
efectos del impuesto local. En varios países la regla para servicios es
**donde se ejecuta materialmente** —donde está la infraestructura humana y
técnica que presta el servicio— y no el domicilio del cliente, ni el lugar
de facturación, ni dónde se firmó el contrato.

**Consecuencia para los incentivos:** un beneficio local atado a *ejercer
la actividad* en ese territorio **no se captura con una dirección**. Un
beneficio atado a *estar registrado* ahí, sí.

## `[FILTRO PREVIO]` El punto de equilibrio

Antes de comparar nada, **descarta los incentivos que hoy no te sirven.**

Un incentivo tributario solo vale si hay base gravable sobre la cual
aplicarlo:

| Incentivo | No sirve si… |
|---|---|
| Tarifa reducida de renta | **No hay utilidad gravable.** 20% de cero es cero |
| Deducción por I+D | No hay renta contra la cual deducir, o no hay inversión que calificar |
| Exención del impuesto local de actividad | Los ingresos son tan bajos que el impuesto es marginal |
| Descuento por empleo formal | No vas a contratar este año |

**Regla:** por cada incentivo, calcula **cuánto ahorrarías el año que
viene con tus números reales**. Si el ahorro es menor que el costo de
fricción, sale de la comparación.

Muchos fundadores pre-ingresos persiguen beneficios que solo empiezan a
importar tres años después. **Decláralo cuando pase.**

## Restricciones que no son tuyas

A veces el territorio no lo eliges tú:

- **Un inversionista** puede exigir una jurisdicción o estructura concreta
- **Un cliente grande o una licitación** puede exigir registro local
- **Un programa de ecosistema** puede exigir domicilio en la región
- **Un socio** puede tener su propia restricción

**Pregunta si existe alguna antes de comparar.** Una restricción externa
cierra el análisis en un minuto.

## Dos tipos de beneficio, y solo uno viaja con la dirección

| Tipo | Ejemplo | ¿Basta domiciliar allá? |
|---|---|---|
| **Atado al registro o al domicilio** | Programas de la cámara de comercio, redes de innovación, convocatorias regionales | **Sí, normalmente** |
| **Atado al ejercicio de la actividad** | Exenciones del impuesto local de actividad, tarifas preferenciales | **No.** Requiere operar allá |

**Clasifica cada incentivo en uno de los dos antes de compararlo.** Es la
distinción que decide si mudar el domicilio sirve de algo.

---

## Qué se compara

Por cada territorio candidato:

### 1. Costo de constituir y mantener
Tarifas de registro · renovación anual · impuesto local de actividad y su
tarifa para esa actividad · otros locales

**Para la rama B:** el impuesto local se calcula donde se ejecuta la
actividad, que puede no ser donde está el domicilio. Calcúlalo allá.

### 2. Incentivos — y sus condiciones reales
Por cada uno:

```
- <incentivo> · <qué otorga> · <quién lo otorga>
  Requisitos:  <presencia | empleo local | inversión mínima | sector>
  Vigencia:    <desde-hasta>  · [CADUCA]
  Estado:      VIGENTE | PROYECTO NO APROBADO | DEROGADO
  Fuente:      <URL oficial>
```

**`[REGLA DURA]` Un incentivo anunciado no es un incentivo vigente.**
Muchos beneficios locales existen como proyecto de acuerdo u ordenanza sin
aprobar. Si el estado no es VIGENTE con fuente oficial, **no se cuenta en
la comparación**: se lista aparte como "posible, sin aprobar".

### 3. Ecosistema
Programas de aceleración · fondos públicos y su cadencia · red · talento
disponible en tu stack · costo de contratar

### 4. Costo de operar
Arriendo si aplica · salarios de mercado · conectividad

### 5. Fricción
Trámites presenciales · tiempos de la entidad local · si se puede hacer
todo en línea desde otra ciudad

---

## Formato de salida

```
## Punto de partida
<territorio donde vive y opera el fundador>
Para moverse habría que justificar: <cifra anual neta a favor>

## Restricciones externas
<inversionista | cliente | programa | ninguna>

## Descartados por el filtro de punto de equilibrio
- <incentivo> · ahorro estimado con tus números: <cifra> · no compensa

## Comparación

| Criterio | <A> | <B> | <C> |
|---|---|---|---|
| Costo constituir | | | |
| Impuesto local (tu actividad) | | | |
| Incentivos VIGENTES aplicables | | | |
| Programas de ecosistema | | | |
| Requiere presencia física | | | |
| Beneficios que viajan con la dirección | | | |
| Beneficios que exigen operar allá | | | |

## Incentivos que sí podrías usar
- <cuál> · <por qué encajas> · <qué tendrías que hacer>

## Incentivos que NO podrías usar
- <cuál> · <qué requisito no cumples>

## Anunciados pero sin aprobar
- <cuál> · <estado del trámite> · **no cuenta hoy**

## Costo anual de cada opción

| | Quedarse | <B> | <C> |
|---|---|---|---|
| Registro y renovación | | | |
| Impuesto local estimado | | | |
| Fricción (viajes, trámites) | | | |
| Incentivos aplicables hoy | −  | −  | −  |
| **Neto anual** | | | |

## Reversibilidad
Costo de cambiar el domicilio después: <cifra y tiempo>
→ Si es bajo: constituye donde estás y decide con datos

## Lo que no pude verificar
- <tema> · PREGUNTAR A: <cámara de comercio | contador>
```

**Si la columna "neto anual" no se puede llenar con cifras, el skill lo
dice y no simula una comparación.** Una tabla con celdas cualitativas
parece un análisis y no lo es.

**La sección de incentivos que NO puedes usar es la más útil.** Es donde se
cae la mitad de la ilusión, y es lo que un artículo de blog nunca te dice.

---

## Reversibilidad — el costo de equivocarse

**Esto no es una decisión permanente, y saberlo cambia cuánto hay que
pensarla.**

Cambiar el domicilio después implica:
- Reforma estatutaria y su inscripción
- Registro ante la cámara de comercio del nuevo domicilio
- Actualización ante la autoridad tributaria y los municipios
- Actualizar contratos, facturación y documentos

`[VERIFICAR EN EL PACK]` Costo y tiempo del cambio de domicilio.

**Consecuencia práctica:** si el costo de mover después es bajo, constituye
donde estás hoy y decide con datos cuando los tengas. Si es alto, la
decisión pesa más ahora.

**El error opuesto también existe:** postergar la constitución esperando la
decisión perfecta de domicilio. Operar sin constituir tiene su propio
costo — en varias jurisdicciones, responsabilidad personal.

## Preguntas que el skill debe hacer antes de comparar

1. **¿El negocio tiene establecimiento físico abierto al público?**
   Define toda la rama del análisis
2. ¿Puedes y quieres mudarte, o solo mover el domicilio legal?
3. ¿Vas a contratar? ¿Dónde vivirá esa gente?
4. ¿Tus clientes son locales o remotos?
5. ¿Tienes capital para invertir, si un incentivo lo exige como mínimo?
6. ¿Cuánto vale tu tiempo en trámites presenciales?
7. **¿Hay alguna restricción externa?** Inversionista, cliente grande,
   licitación o programa que exija una jurisdicción
8. **¿Tienes utilidad gravable hoy, o la vas a tener el año entrante?**
   Decide si los incentivos tributarios entran siquiera al análisis

**Sin estas respuestas la comparación es un folleto**, no una decisión.

---

## Qué NO hacer

- **No recomiendes un territorio.** Presenta la comparación y el costo de
  cada opción. La decisión es del humano
- **No cuentes incentivos sin aprobar** como si estuvieran vigentes
- **No asumas que domiciliar en otra ciudad obliga a abrir sucursal.** Sin
  establecimiento abierto al público, normalmente no
- **No asumas que la dirección traslada el impuesto local.** Para servicios
  suele seguir a donde se ejecuta la actividad
- No omitas clasificar cada incentivo: ¿viaja con la dirección o exige
  operar allá?
- No presentes cifras de incentivos sin año y sin fuente oficial
- No compares territorios de países distintos: eso es otra decisión, con
  implicaciones fiscales y migratorias que este skill no cubre
- No estimes ahorros tributarios como cifras firmes. **Eso lo calcula un
  contador** con los números reales. El skill produce órdenes de magnitud
  para descartar, no para declarar
- **No compares opciones en igualdad de condiciones.** El default es
  quedarse; moverse se justifica
- **No incluyas incentivos que el negocio no puede usar este año.** Van a
  la sección de descartados, con la razón
- No presentes la decisión como irreversible sin verificar el costo de
  cambiarla
