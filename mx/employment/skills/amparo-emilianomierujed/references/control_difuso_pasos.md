# Control difuso — guion de acompañamiento

Sustituye a la skill `control-difuso`, que ejecutaba el método de corrido:
enunciaba las interpretaciones posibles, elegía la más protectora y resolvía el
desenlace. Eso es precisamente lo que no se delega.

Marco: **Varios 912/2010**, tesis **P. LXIX/2011**, **CT 293/2011**, arts. **1º
CPEUM** y **29 CADH**.

---

## Regla que gobierna todo el guion

> **RH-2 — La IA nunca ejecuta una interpretación conforme, el principio pro
> persona ni una ponderación.**

Puede traer material sobre **cómo** se hacen. No los hace.

El principio pro persona (art. 1º, párr. 2 CPEUM: *"favoreciendo en todo tiempo a
las personas la protección más amplia"*; art. 29 CADH) es **criterio rector de
todo el análisis, no una etapa**. Opera en dos dimensiones —preferencia
interpretativa y preferencia normativa— y ambas son actos del abogado en cada
paso.

La secuencia siguiente es el **orden de exposición** que espera el foro (P.
LXIX/2011), no una jerarquía que subordine el pro persona a la interpretación
conforme.

---

## Los seis pasos

### Paso 0 — El par ya construido (recolectado en Fase 2, no aquí)

`grafo.v_par_convencional` dice si ya hay criterios que emparejaron esa norma
interna con una convencional.

**Se recupera en la Fase 2 y pasa por la compuerta**, como todo lo que va a
citarse. La fase 3-bis lo consume ya verificado. Consultarlo aquí saltaría la
compuerta, que es precisamente el agujero que la compuerta cierra.

Consulta y reglas de lectura en `references/consultas_mcp.md`.

Advertencia obligatoria: **vista vacía no significa que no haya control difuso
posible.** Solo el 0.74% de las tesis menciona algún instrumento internacional.
Significa que no hay una tesis que lo haya hecho explícito.

Y: **que un par exista no significa que el tratado prevalezca.** El grafo
registra que un tribunal dijo algo sobre dos normas; no existe arista norma→norma.

**Sin conector no hay paso 0.** No se dice "no hay par": se dice
`SIN_MOTOR_DE_VERIFICACION`, porque nadie consultó. La diferencia importa —
"vista vacía" ya es una afirmación débil sobre el mundo, y "no se consultó" no es
ninguna.

---

### Paso 1 — Parámetro de regularidad

| La IA aporta | El abogado hace |
|---|---|
| Normas y criterios **candidatos**, cada uno verificado por la compuerta, con su ámbito copiado literal y su link | **Decide cuáles integran el parámetro** |

Fuentes candidatas que la IA recupera:

- **CPEUM** — todos sus derechos, no solo el Capítulo I
- **Jurisprudencia nacional** — con `ambito` verificado en `v_autoridad_criterio`.
  Una tesis aislada nunca forma parámetro obligatorio, por más pertinente que sea
- **Tratados ratificados por México** — cualquier materia
- **Jurisprudencia de la Corte IDH** — contenciosos, opiniones consultivas,
  medidas provisionales, supervisión de cumplimiento
- **Órganos convencionales de supervisión** — comités ONU, CIDH, relatorías, UHRI

Cobertura de texto desigual: ver la tabla de `references/consultas_mcp.md`. Las
tablas sin cuerpo se entregan como ficha con link, sin comillas.

**Lo que la IA NO hace en este paso:** decir cuál norma del bloque es "la más
protectora". Identificar la norma más favorable es preferencia normativa, o sea
pro persona, o sea del abogado.

`INTERPRETACION_PENDIENTE_DEL_ABOGADO` hasta que él cierre el parámetro.

**Sin conector**, las candidatas se arman con el texto normativo de la CPEUM y de
los tratados ratificados, marcado `TEXTO_NO_COTEJADO`
(`references/modo_sin_conector.md` §7), más lo que el abogado aporte. La
jurisprudencia —nacional o interamericana— **nunca** entra de memoria, ni siquiera
el rubro. Sin `ambito` verificado, ninguna candidata puede presentarse como
parámetro obligatorio: eso queda expresamente del lado del abogado.

Es el único paso donde el modo sin conector pierde material de verdad. Los cinco
siguientes salen iguales, porque siempre fueron suyos.

---

### Paso 2 — Interpretación conforme en sentido amplio

| La IA aporta | El abogado hace |
|---|---|
| Interpretaciones **ya sostenidas por fuentes localizadas**, transcritas literalmente con su registro y link | **Formula la interpretación** |

La diferencia es fina y es toda la diferencia: la IA puede decir *"la tesis
2024847 sostuvo textualmente que [cita literal]"*. No puede decir *"la norma
admite las siguientes tres lecturas"*, porque enunciar el abanico de lecturas
posibles ya es interpretar.

Si no hay fuente que haya sostenido una interpretación, el paso sale vacío con
`SIN_CRITERIO_LOCALIZADO`. No se rellena con lecturas construidas.

---

### Paso 3 — Interpretación conforme en sentido estricto

| La IA aporta | El abogado hace |
|---|---|
| Lo mismo del paso 2, acotado a las lecturas compatibles con el parámetro que **el abogado** fijó en el paso 1 | **Formula la interpretación** |

Nota de método que el abogado decide, no el sistema: no se fuerza una lectura
artificiosa para "salvar" una norma restrictiva cuando el bloque ofrece una norma
más protectora — ahí corresponde preferencia normativa, no conforme forzada. El
sistema puede recordar la regla; no puede resolver cuál es el caso.

---

### Paso 4 — Principio pro persona

| La IA aporta | El abogado hace |
|---|---|
| Los criterios sobre **cómo opera** el principio (preferencia interpretativa y normativa), transcritos | **Aplica el principio** |

Este paso sale siempre vacío. No hay versión de él que la IA pueda llenar sin
violar RH-2.

---

### Paso 5 — Ponderación / test de proporcionalidad

| La IA aporta | El abogado hace |
|---|---|
| Los criterios sobre las gradas del test —fin legítimo, idoneidad, necesidad, proporcionalidad en sentido estricto— transcritos de fuentes verificadas | **Corre el test** |

Igual que el paso 4: sale vacío. Traer los criterios que explican cómo se corre
un test de proporcionalidad es recuperación. Correrlo es juzgar.

---

### Paso 6 — Desenlace

| La IA aporta | El abogado hace |
|---|---|
| El recordatorio del candado y de los efectos | **Decide el desenlace** |

Las tres salidas posibles, todas al caso concreto y con efecto *inter partes*:

- **(a) Interpretación conforme viable** — una lectura protectora salva la norma
- **(b) Preferencia normativa directa** — una norma del bloque más favorable
  desplaza a la nacional, sin rescatar la menos protectora
- **(c) Inaplicación al caso concreto** — ninguna conforme salva la norma y no
  hay norma de reemplazo

**Candado CT 293/2011 (recordatorio mecánico, siempre):** si la restricción
proviene de una **restricción expresa de la propia Constitución**, la SCJN hace
prevalecer esa restricción sobre la norma internacional más favorable. Si
`v_par_convencional` devolvió `restriccion_constitucional = 1`, se señala con el
registro que lo dice.

**RH-14:** nunca se declara invalidez general. Eso es control concentrado.

---

## Formato de salida

El agente entrega `caso/control-difuso.md` con los seis pasos, el material
verificado bajo cada uno y los huecos marcados
`INTERPRETACION_PENDIENTE_DEL_ABOGADO`.

No entrega conclusión. No sugiere desenlace. No dice cuál paso "parece más
prometedor".
