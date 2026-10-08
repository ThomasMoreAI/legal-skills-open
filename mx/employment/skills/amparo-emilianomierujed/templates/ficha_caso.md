# Ficha del caso

> Todo lo de este archivo lo dijo el abogado. Nada se dedujo ni se completó.
> Los campos que él no dio quedan como `NO DECLARADO` — no se rellenan.

**Modo de conexión:** `{CON CONECTOR | SIN CONECTOR}` — declarado al arranque y
fijo para toda la sesión (RH-18).

## Identificación

- **Quejoso:**
- **Acto reclamado:** {el acto concreto, con fecha, expediente y órgano}
- **Autoridad responsable:**
- **Autoridad ejecutora:** {si la hay}
- **Fecha de notificación / conocimiento:**
- **Plazo:** `PLAZO_NO_CALCULADO` — el cómputo corresponde al abogado (RH-13)

## Foro

- **Entidad:**
- **Municipio:** {obligatorio si la entidad devuelve `alcance = 'parcial'`. **Sin conector se pregunta siempre**: sin el grafo no se sabe cuáles están partidas}
- **Circuito:** {ordinal} — {de su perfil | del estado que indicó | resuelto con `municipio_circuito` | `CIRCUITO_NO_DECLARADO`}
- **Materia:**

> El ordinal es una traducción hecha por el sistema desde `grafo.entidad_circuito`
> y `municipio_circuito`. Se confirma en voz alta para que el abogado pueda
> corregirla antes de que se construyan mil palabras sobre el circuito equivocado.

{sin conector, la línea de circuito es siempre:}
```
CIRCUITO_NO_DECLARADO — no hay motor para resolverlo, no es que falte el dato.
Municipio registrado: {municipio}. Verifícalo tú antes de invocar obligatoriedad.
```

## Lo que el abogado ya trae

- **Pretensión:** {qué pide — lo tenía desde antes de abrir la herramienta}
- **Derecho humano que considera violado:**
- **Material propio:** {constancias, pruebas, normas que ya identificó}

## Ejes de descarte autorizados

> Estos ejes son del abogado, no del sistema. La IA solo los aplica, y todo lo
> que descarte con ellos queda en `bitacora-descartes.md` para rescate (RH-4).

- [ ] {eje 1}
- [ ] {eje 2}
- [ ] {…}

## Estados

- Circuito: `{OK | CIRCUITO_NO_DECLARADO}`
- Plazo: `PLAZO_NO_CALCULADO`
