# Amparo — método de trabajo

Skill de Claude para litigio de amparo mexicano, con una restricción de diseño de
la que cuelga todo lo demás:

> **Lo mecánico es de la IA. Lo interpretativo es del humano.**

La IA localiza, coteja y verifica. Nunca interpreta, nunca prioriza, nunca
argumenta. El andamio del concepto de violación se entrega con **los pasos
interpretativos vacíos**, marcados `INTERPRETACION_PENDIENTE_DEL_ABOGADO`.

Eso no es trabajo a medias: es el punto. Un abogado que no construyó el argumento
no puede defenderlo en audiencia.

---

## Qué hace

Un flujo de siete fases con checkpoints obligatorios:

| Fase | Qué pasa |
|---|---|
| 0 · Registro | Levanta la ficha del caso preguntando, nunca deduciendo. El abogado fija los ejes de descarte |
| 1 · Rutas | Enuncia rutas de ataque. **El abogado elige.** No hay ruta recomendada |
| 2 · Recolección | Busca material sobre la ruta elegida, incluida una **ronda adversa obligatoria** |
| 2.5 · Compuerta | Cinco ejes de verificación por fuente. No se salta |
| 3-bis · Control difuso | Acompaña los seis pasos. Los interpretativos salen vacíos |
| 3 · Andamio | Estructura el concepto de violación con el material verificado debajo de cada hueco |
| 4 · Contraste | Corre la posición de la contraparte contra lo construido |

**La compuerta de fuentes** verifica cinco ejes por cada fuente que vaya a
citarse: existencia y procedencia, vigencia, ámbito de obligatoriedad
(art. 217 LA), correspondencia textual literal, y pertinencia — que **nunca** se
evalúa, porque es el acto interpretativo central del litigio.

---

## Los dos modos de conexión

La skill corre igual con o sin el conector de bases jurídicas. Lo que cambia es
qué se puede verificar, y **se declara al arranque** en vez de fingirse.

| | Sin conector | Con conector |
|---|---|---|
| Fases, checkpoints, andamio | Completos | Completos |
| Origen de las fuentes | Las que aporta el abogado + portales oficiales | 750,000+ documentos consultables |
| Eje 1 · existencia y procedencia | Contra el material aportado | Contra las bases |
| Eje 2 · vigencia | `SIN_MOTOR_DE_VERIFICACION` | Grafo de superación |
| Eje 3 · obligatoriedad | `SIN_MOTOR_DE_VERIFICACION` | `v_autoridad_criterio`, art. 217 LA |
| Eje 4 · correspondencia textual | **Corre completo** | Corre completo |
| Ronda adversa | Web + delegada al abogado, expresamente | Barrido sobre las bases |

**El modo sin conector no relaja la compuerta.** La corre igual y devuelve el
veredicto honesto: `SIN_MOTOR`, con el conteo de cuántos criterios quedaron sin
verificar. Un dossier vacío nunca sale en `PASA`.

Y **sí puede fallar sin conector**: si una nota de superación aparece en la ficha
oficial del Semanario, o si el eje 4 encuentra que una frase atribuida a una
tesis no está en su texto. Eso último —atribuirle a una fuente algo que no
dice— es el error más caro en audiencia, y atraparlo no necesita las bases:
necesita el texto y la disciplina de compararlo.

Protocolo completo: [`references/modo_sin_conector.md`](references/modo_sin_conector.md).

---

## Instalación

**Claude Code** — clona el repo y copia la carpeta:

```bash
cp -r skills/amparo ~/.claude/skills/
```

**Claude.ai (web y escritorio)** — súbela como skill personalizada: comprime la
carpeta `skills/amparo/` en un `.zip` y súbela en Ajustes → Capacidades → Skills.

En ambos casos se invoca diciendo lo que necesitas —*"ayúdame a fundar este
amparo"*— no escribiendo un comando.

---

## Las reglas de hierro

Diecinueve reglas que no se negocian, en
[`references/reglas_de_hierro.md`](references/reglas_de_hierro.md). Las que más
gobiernan el día a día:

- **RH-3** — el sistema no escribe premisas, argumentos ni conclusiones.
- **RH-4** — no se ordena por relevancia. El orden es obligatoriedad → vigencia →
  circuito → fecha, y se declara.
- **RH-8** — sin ronda adversa no se avanza al andamio.
- **RH-16** — ningún checkpoint obligatorio se salta. No hay bandera de override.
- **RH-17** — **nada recordado.** Ninguna fuente se cita de memoria: cada ficha
  declara de dónde vino.
- **RH-18** — el modo se declara al arranque y en cada reporte.

Y un vocabulario cerrado de estados honestos
([`references/estados_honestos.md`](references/estados_honestos.md)) que existe
para que el sistema pueda decir *no sé* con precisión, en vez de rellenar el
hueco con prosa. `VIGENCIA_NO_VERIFICADA` significa *se consultó y no se halló
evidencia*; `SIN_MOTOR_DE_VERIFICACION` significa *nadie consultó*. No son lo
mismo y no se intercambian.

---

## El método es abierto; la verificación necesita las bases

Este repositorio contiene el método completo: las fases, los checkpoints, los
agentes, las plantillas y las reglas. Nada está recortado ni reservado.

Lo que no viaja aquí son las bases —jurisprudencia, sentencias, corpus
internacional, leyes federales y el grafo de vigencia y obligatoriedad—, que son
lo que permite resolver mecánicamente los ejes 2 y 3. Ese es el conector de
[CONSULTO](https://consulto.page).

No es una versión gratis limitada. Es un método que dice, en cada corrida,
exactamente qué pudo verificar y qué no.

---

## Estructura

```
SKILL.md      Orquestación: fases, checkpoints, arranque y declaración de modo
MODOS.md      Modos de trabajo (fundamentar, viabilidad, armar, romper) y su estado
agents/       Un archivo por agente: registro, rutas, buscadores, compuerta,
              control difuso, andamio, contraparte
references/   Reglas de hierro, estados honestos, compuerta, obligatoriedad,
              modo sin conector, anatomía del amparo, consultas técnicas
templates/    Ficha de caso, ficha de fuente, reporte de compuerta, andamio,
              control difuso, bitácora de descartes
```

---

## Licencia

Apache-2.0. El método se publica para que se adopte, se critique y se mejore.
