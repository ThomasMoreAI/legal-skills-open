# Registro de modos — skill `amparo`

Fuente única. Si un modo cambia de estado, cambia aquí primero.

> **Dos cosas se llaman "modo" en esta skill y no son lo mismo.**
>
> - **Modos de trabajo** — los cuatro de la tabla de abajo: `fundamentar`,
>   `viabilidad`, `armar`, `romper`. Responden a *en qué momento está el abogado*.
> - **Modos de conexión** — con conector / sin conector. Responden a *qué se puede
>   verificar*. Viven en `references/modo_sin_conector.md`.
>
> Son ejes independientes: cualquier modo de trabajo corre en cualquiera de los
> dos modos de conexión. Un modo de trabajo `PLANEADO` sigue sin existir, tengas
> conector o no.

| Modo | Estado | Momento del usuario | Fases | Agentes |
|---|---|---|---|---|
| `fundamentar` | **ACTIVO** | "Sé qué pedir, no con qué fundarlo" | 0, 1, 2, 2.5, 3-bis, 3, 4 | registro_caso, rutas, buscador_nacional, buscador_convencional, verificacion_fuentes, control_difuso, andamio, contraparte |
| `viabilidad` | **ACTIVO** | "No sé si tengo caso" | 0, 1, 1.5, 2 | registro_viabilidad, localizador_viabilidad, verificacion_fuentes_viabilidad, ficha_viabilidad |
| `armar` | `PLANEADO` | "Tengo el fundamento, no sé cómo armarlo" | — | redactor_formal (escrito, inactivo) |
| `romper` | `PLANEADO` | "Ya lo escribí y quiero que me lo rompan" | — | contraparte (reutilizable) |

---

## Regla de honestidad de modos

**Un modo `PLANEADO` no se simula.** Si el usuario lo invoca:

1. Se le dice que ese modo todavía no existe.
2. Se le ofrece `fundamentar` si su problema encaja.
3. Se le ofrece el MCP crudo si quiere armar su propio flujo — **si hay
   conector**. Sin él, esa tercera salida no existe y no se ofrece.

Improvisar el modo sobre la marcha produciría un método inventado en el momento,
que es exactamente lo que esta skill vino a corregir en las 8 skills anteriores.

---

## Decisiones de diseño cerradas

### `viabilidad` — el plazo (cerrado 2026-08-28)

Triage antes de que exista demanda: acto reclamado, autoridad, interés jurídico o
legítimo, principio de definitividad, procedencia, plazo.

**Problema tal como estaba planteado:** RH-13 prohíbe calcular plazos, y un
modo de viabilidad que no toca plazos es de utilidad limitada — es
probablemente la pregunta más frecuente de quien no sabe si tiene caso.

**Decisión:** el sistema localiza y transcribe la regla aplicable — el
artículo de la Ley de Amparo, su plazo en abstracto, sus excepciones — y
nunca hace la cuenta con fechas concretas. Estado nuevo,
`REGLA_DE_PLAZO_LOCALIZADA`, que siempre acompaña a `PLAZO_NO_CALCULADO` (ya
existente) y nunca lo sustituye: uno dice qué se encontró, el otro dice qué
no se hizo. Frontera exacta: *"Art. 17 de la Ley de Amparo: quince días
hábiles, salvo las excepciones del mismo artículo"* es mecánico (localizar y
transcribir); *"tu plazo vence el 12 de diciembre"* es interpretativo-
prohibido (requiere calendario, días inhábiles, criterios de cómputo que a
veces se litigan) y no se escribe en ningún entregable de este modo.

El mismo tratamiento se extendió a los otros tres ejes que un modo de
viabilidad no puede resolver por el abogado: interés jurídico o legítimo,
definitividad y procedencia. Ahí no hizo falta un estado nuevo — se reutiliza
`INTERPRETACION_PENDIENTE_DEL_ABOGADO` (mismo patrón que los huecos 3-6 del
andamio de `fundamentar`) — pero sí una regla de hierro nueva, **RH-20**,
porque ninguna regla existente nombraba estos tres ejes explícitamente.

Ver `references/estados_honestos.md` (`REGLA_DE_PLAZO_LOCALIZADA`) y
`references/reglas_de_hierro.md` (RH-20).

## Notas por modo planeado

### `armar`

Aquí se activa `redactor_formal_agent`, ya escrito. Su alcance está cerrado por
lista y todo lo que redacta es forma, no argumento: proemio, antecedentes,
autoridades responsables, preceptos violados, capítulo formal de suspensión,
puntos petitorios.

El concepto de violación llega ya escrito por el abogado. El modo lo ensambla, no
lo produce.

### `romper`

Auditoría adversarial de un escrito existente. `contraparte_agent` ya sirve casi
completo; falta la entrada (un escrito que el sistema no armó) y la verificación
de las citas que el escrito trae, que puede reusar la compuerta de fuentes.

Es el modo más barato de implementar de los tres.
