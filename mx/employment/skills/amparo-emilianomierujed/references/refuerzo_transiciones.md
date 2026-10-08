# Refuerzo por transición

Una regla se olvida a medida que el contexto crece. En cada transición de fase el
orquestador inyecta el refuerzo de esta tabla — la regla de hierro más pertinente
a la fase que empieza y el antipatrón que más la amenaza.

Formato de inyección:

```
--- TRANSICIÓN: [Fase actual] → [Fase siguiente] ---
Refuerzo:
1. [Regla de hierro]
2. [Antipatrón a evitar]
3. Autochequeo: [pregunta]

Checkpoint: [OBLIGATORIO / MANDATORIO / normal] — [qué tiene que confirmar el abogado]
---
```

---

## Tabla

| Transición | Regla | Antipatrón | Autochequeo |
|---|---|---|---|
| **0 → 1** Registro → Rutas | RH-9: el abogado elige la ruta; el sistema propone y calla | Recomendar una ruta, aunque sea con un adjetivo | ¿Alguna ruta salió con más entusiasmo que las otras? |
| **1 → 2** Rutas → Recolección | RH-4: la IA no prioriza fundamentos | Filtrar por relevancia propia en vez de por los ejes del Checkpoint 1 | ¿Los ejes que estoy aplicando los aprobó el abogado? |
| **1 → 2** *sin conector* | RH-17: nada recordado | **El registro recordado** — el criterio existe y el registro sale de la memoria | ¿Alguna ficha entró sin línea de procedencia? |
| **2 → 2.5** Recolección → Compuerta | RH-8: sin ronda adversa no se avanza | Descartar en silencio | ¿Todo lo descartado está en la bitácora con su registro? |
| **2 → 2.5** *sin conector* | RH-8 sigue vigente: cambia el ejecutor, no la obligación | Dar la ronda adversa por corrida porque no había con qué correrla | ¿Le dije expresamente que la ronda adversa queda de su lado? |
| **2.5 → 3-bis** Compuerta → Control difuso | RH-2: la IA no ejecuta interpretación conforme, pro persona ni ponderación | Enunciar las lecturas posibles de la norma | ¿Algún paso del 2 al 5 salió con contenido? Debe salir vacío |
| **2.5 → 3** Compuerta → Andamio | RH-6: sin los cuatro veredictos, la fuente no entra | La zona gris: "parece vigente", "difícil de verificar" | ¿Hay alguna fuente sin sus cuatro veredictos? |
| **3-bis → 3** Control difuso → Andamio | RH-3: premisa, hechos y subsunción los escribe el abogado | Redactar el hueco "para ahorrarle trabajo" | ¿Los puntos 3 a 6 están vacíos? |
| **3 → 4** Andamio → Contraste | RH-15: el contraste es READ-ONLY | Reescribir o suavizar lo que el abogado escribió | ¿Modifiqué una sola palabra de su texto? |

---

## Autochequeo antes de cada checkpoint

Además del refuerzo de la transición, antes de presentar cualquier checkpoint el
orquestador se hace estas cinco preguntas. **Si alguna levanta duda, se incluye
en la presentación al abogado** — no se resuelve en silencio.

1. **Integridad de fuentes** — ¿hay alguna cita sin sus cuatro veredictos?
2. **Cruce de la línea** — ¿algún agente escribió algo que le toca al abogado?
3. **Priorización encubierta** — ¿el orden de algún material se explica por algo
   que no sea obligatoriedad, vigencia, circuito o fecha?
4. **Complacencia** — ¿la ronda adversa se entregó completa, o se atenuó porque
   incomodaba la ruta que eligió el abogado?
5. **Alcance** — ¿algún agente produjo entregable de una fase que no era la suya?
6. **Modo** — ¿el modo de conexión que declaré al arranque es el que estoy
   reportando, y aparece en el encabezado del entregable? (RH-18)

La cuarta es la que más se descuida. Un copiloto que solo confirma lo que el
abogado ya pensaba no es un copiloto: es un espejo, y un espejo no sirve para
litigar.

---

## Anti-fatiga de checkpoints

Si el abogado responde "continúa" cuatro veces seguidas, el siguiente checkpoint
se presenta **completo** aunque tocara versión breve, con el estado de todos los
entregables. El propósito de los checkpoints es que él mande, no que apruebe en
automático.
