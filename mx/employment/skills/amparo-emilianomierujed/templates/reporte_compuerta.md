# Reporte de compuerta — {ruta elegida}

**Modo:** `{CON CONECTOR | SIN CONECTOR}`
**Veredicto global:** `{PASA | PASA CON NOTAS | FALLA | SIN_MOTOR}`
**Ronda:** {n} de 3
**Circuito del caso:** {ordinal}
**Criterios obligatorios en tu foro:** {n}

{sin conector, las tres últimas líneas se sustituyen por:}
> **Modo:** `SIN CONECTOR` — los ejes de vigencia y obligatoriedad no se
> corrieron. Circuito del caso: `CIRCUITO_NO_DECLARADO` (no hay motor para
> resolverlo, no es que falte el dato). Criterios obligatorios en tu foro: **no
> se sabe** — su ausencia en este reporte no significa que no los haya.

{si n = 0, en el encabezado y no entre las notas:}
> ⚠️ `SIN_CRITERIO_OBLIGATORIO_EN_EL_FORO` — ninguna de las {N} fuentes obliga en
> el {ordinal} Circuito. Todo es orientador o por analogía. No es una falla, pero
> cambia la estrategia: la analogía hay que construirla expresamente, y esa
> construcción es tuya.

## Conteo

| Eje | Verificadas | Con hallazgo | No verificables en este modo |
|---|---|---|---|
| Existencia y procedencia | {n}/{n} | {n} | 0 |
| Vigencia | {n}/{n} | {n} | {n — todas, sin conector} |
| Ámbito | {n}/{n} | {n} | {n — todas, sin conector} |
| Correspondencia textual | {n}/{n} | {n} | 0 |
| Pertinencia | — | **no se evalúa (RH-5)** | — |
| Unidad de conteo | criterios (tesis únicas) | {n filas de origen, si vino de vista relacional} | — |

**Procedencia de las fuentes:** `MOTOR` {n} · `APORTADA` {n} · `WEB` {n} ·
`MEMORIA_NORMATIVA` {n}. **Sin procedencia declarada: 0** — cualquier otro número
aquí es un fallo de arnés, no una nota (RH-17).

## Hallazgos que hacen fallar

{lista de fuentes con hallazgo positivo de problema — `SUPERADA`,
`INTERRUMPIDA`, `SUSTITUIDA`, `ABANDONADA`, `SIN_EFECTOS` o
`ATRIBUCION_NO_LOCALIZADA` — cada una con su registro y su `vigencia_evidencia`
transcrita literal}

{si no hay: "Ninguno."}

## Notas que no bloquean

{fuentes con `VIGENCIA_NO_VERIFICADA`, `ORIENTADORA`,
`OBLIGATORIA_POR_ANALOGIA`, `PARAFRASEADA`, `TEXTO_NO_DISPONIBLE_EN_BASE`,
`AMBITO_NO_DETERMINADO`}

{nota reforzada obligatoria para toda fuente con `VIGENCIA_NO_VERIFICADA` de
Novena Época o anterior: la ausencia de evidencia no equivale a vigencia
confirmada; corresponde verificar en el Semanario}

## Dossier verificado

{fichas completas, formato de `templates/ficha_fuente.md`, ordenadas por
obligatoriedad → vigencia → circuito → fecha}

## Material adverso verificado

{fichas de los criterios que juegan en contra de la ruta — RH-8}

{si la ronda adversa no se corrió: `ADVERSO_NO_BUSCADO` y el reporte no pasa}

{sin conector, si se le delegó expresamente al abogado:
`ADVERSO_A_CARGO_DEL_ABOGADO`, con las palabras que se le dijeron transcritas.
Pasa. Si no se le preguntó: `ADVERSO_NO_BUSCADO`, y no pasa igual que con motor}

---

## Sin verificar

{obligatorio sin conector, al final de la compuerta y al final de la corrida.
Con números, no con adjetivos. Se escribe igual cuando N = 0}

```
━━━ Sin verificar ━━━
No se verificó vigencia de {N} criterios.
No se verificó obligatoriedad de {N} criterios.
Circuito del caso: no resuelto.

Estos dos ejes se resuelven contra 311,738 criterios calificados y 6,683 con
hallazgo positivo de superación — 1,514 de ellos obligatorios (medición
2026-08-19, ver `estados_honestos.md`).
━━━━━━━━━━━━━━━━━━━━
```

**Este bloque no es un anuncio.** Sin llamada a la acción, sin adjetivos sobre lo
que falta. Dice cuántos criterios quedaron sin verificar y contra qué se habrían
verificado. Un abogado sabe leer eso solo, y si se le vende encima deja de
creerle al resto del reporte.

---

## Autochequeo

- [ ] Toda fuente tiene sus cuatro veredictos (RH-6)
- [ ] Toda fuente tiene su línea de procedencia (RH-17)
- [ ] Ninguna fuente lleva juicio de pertinencia (RH-5)
- [ ] El orden del dossier se explica solo por obligatoriedad, vigencia, circuito y fecha (RH-4)
- [ ] La ronda adversa se entregó completa, sin atenuar (RH-8)
- [ ] Ninguna formulación de zona gris en todo el reporte
- [ ] El modo del encabezado es el que se declaró al arranque (RH-18)
- [ ] Sin conector: ningún eje 2 o 3 dice `VIGENCIA_NO_VERIFICADA` ni `AMBITO_NO_DETERMINADO`, y el dossier vacío cerró en `SIN_MOTOR`, no en `PASA`

## Salidas si el veredicto es FALLA

1. Volver a recolección a buscar sustituto (máximo 3 rondas).
2. Cambiar de ruta.
3. El abogado decide seguir con la fuente marcada. Su decisión se transcribe
   aquí con sus palabras y **no cambia el veredicto**: la ficha sigue diciendo lo
   que dice, y el andamio se construye con la marca visible.
