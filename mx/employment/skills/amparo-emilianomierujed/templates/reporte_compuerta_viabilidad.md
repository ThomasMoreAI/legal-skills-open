# Reporte de compuerta — viabilidad

> Agrupado por **eje** (plazo, procedencia, definitividad, interés), no por
> ruta: `viabilidad` no arma rutas de ataque, arma un dossier acotado por
> cada uno de los cuatro ejes del art. 61 LA y sus vecinos. Mismo protocolo
> de fondo que `templates/reporte_compuerta.md`, mismo rigor.

**Modo:** `{CON CONECTOR | SIN CONECTOR}`
**Veredicto global:** `{PASA | PASA CON NOTAS | FALLA | SIN_MOTOR}`
**Ronda:** {n} de 3
**Circuito del caso:** {ordinal}

{sin conector, la última línea se sustituye por:}
> **Modo:** `SIN CONECTOR` — los ejes de vigencia y ámbito no se corrieron
> para las tesis; la vigencia de la norma citada tampoco (no hay acceso a
> `leyes_federales`, solo a la versión mostrada en el portal oficial).
> Circuito del caso: `CIRCUITO_NO_DECLARADO`.

## Conteo por eje

| Eje | Fuentes | Con hallazgo | No verificables en este modo |
|---|---|---|---|
| Plazo (LA arts. 17-18) | {n} | {n} | {n} |
| Procedencia (LA art. 61 + tesis) | {n} | {n} | {n} |
| Definitividad (LA art. 61 + tesis) | {n} | {n} | {n} |
| Interés jurídico/legítimo (LA art. 5 + tesis) | {n} | {n} | {n} |
| Pertinencia | — | **no se evalúa (RH-5)** | — |

**Procedencia de las fuentes:** `MOTOR` {n} · `APORTADA` {n} · `WEB` {n} ·
`MEMORIA_NORMATIVA` {n}. **Sin procedencia declarada: 0** — cualquier otro
número aquí es un fallo de arnés, no una nota (RH-17).

## Hallazgos que hacen fallar

{lista de fuentes con hallazgo positivo de problema — `SUPERADA`,
`INTERRUMPIDA`, `SUSTITUIDA`, `ABANDONADA`, `SIN_EFECTOS`,
`ATRIBUCION_NO_LOCALIZADA`, o un artículo de ley citado con
`leyes.estatus` en `revisar_abrogacion`/`abrogada` — cada una con su registro
o número de artículo y su evidencia transcrita literal}

{si no hay: "Ninguno."}

## Notas que no bloquean

{fuentes con `VIGENCIA_NO_VERIFICADA`, `ORIENTADORA`,
`OBLIGATORIA_POR_ANALOGIA`, `PARAFRASEADA`, `AMBITO_NO_DETERMINADO`, o un
artículo de ley con `N/A — norma federal, aplicación general` en el eje de
ámbito}

## Dossier verificado por eje

{fichas completas, formato de `templates/ficha_fuente.md` (incluido el bloque
"Artículo de ley federal"), agrupadas bajo cada uno de los cuatro ejes,
ordenadas dentro de cada eje por obligatoriedad → vigencia → circuito → fecha}

## Material adverso verificado

{fichas de causales, excepciones o tesis que juegan en contra de la
viabilidad — RH-8 adaptado a este modo: aquí vive dentro de los ejes de
procedencia y definitividad, no en un archivo aparte}

{si la ronda adversa no se corrió: `ADVERSO_NO_BUSCADO` y el reporte no pasa}

{sin conector, si se le delegó expresamente al abogado:
`ADVERSO_A_CARGO_DEL_ABOGADO`, con las palabras que se le dijeron
transcritas. Pasa. Si no se le preguntó: `ADVERSO_NO_BUSCADO`, y no pasa
igual que con motor}

---

## Sin verificar

{obligatorio sin conector, al final de la compuerta. Con números, no con
adjetivos. Se escribe igual cuando N = 0}

```
━━━ Sin verificar ━━━
No se verificó vigencia de {N} criterios.
No se verificó ámbito de obligatoriedad de {N} criterios.
No se verificó vigencia de la norma de {N} artículos de ley citados.
Circuito del caso: no resuelto.
━━━━━━━━━━━━━━━━━━━━
```

---

## Autochequeo

- [ ] Toda fuente tiene sus veredictos completos (RH-6)
- [ ] Toda fuente tiene su línea de procedencia (RH-17)
- [ ] Ninguna fuente lleva juicio de pertinencia (RH-5)
- [ ] El dossier de cada eje se explica solo por obligatoriedad, vigencia,
      circuito y fecha (RH-4)
- [ ] El material adverso de procedencia y definitividad está completo, sin
      atenuar porque incomode al caso (RH-8)
- [ ] Ningún artículo de ley federal lleva un veredicto de vigencia o ámbito
      del vocabulario de tesis (`SUPERADA`, `OBLIGATORIA`, etc.) — usa el
      mapeo de `references/compuerta_fuentes.md`
- [ ] Ninguna formulación de zona gris en todo el reporte
- [ ] El modo del encabezado es el que se declaró al arranque (RH-18)
- [ ] Sin conector: ningún eje de vigencia dice `VIGENCIA_NO_VERIFICADA` ni
      `AMBITO_NO_DETERMINADO`, y un dossier vacío cerró en `SIN_MOTOR`, no en
      `PASA`

## Salidas si el veredicto es FALLA

1. Volver a localización a buscar sustituto (máximo 3 rondas).
2. El abogado decide seguir con la fuente marcada. Su decisión se transcribe
   aquí con sus palabras y **no cambia el veredicto**.

No existe una tercera salida de "cambiar de ruta": este modo no arma rutas.
