---
name: testamento-jaimebs2
title: Testamento — Guía Completa
description: 'Use when the user asks about wills (testamentos) in Spain: types of wills, legitimate heirs (legítimas), the three thirds system, cost of making a will, how to check if someone left a will (Registro General de Actos de Última Voluntad), or regional differences (derecho foral). Triggers on: ''testamento'', ''hacer testamento'', ''tipos de testamento'', ''testamento abierto'', ''testamento ológrafo'', ''legítima'', ''herederos forzosos'', ''tercio de legítima'', ''tercio de mejora'', ''tercio de libre disposición'', ''cuánto cuesta un testamento'', ''registro últimas voluntades'', ''desheredar'', ''derecho foral sucesiones'', ''legítima Cataluña'', ''legítima Aragón'', ''legítima Navarra'', ''testamento ante notario'', ''modificar testamento'', ''revocar testamento''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/justicia/testamento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: family
language: es
---

# Testamento — Guía Completa

Todo lo que necesitas saber sobre testamentos en España: tipos, cómo
otorgarlo, el sistema de legítimas, los tres tercios, coste, registro
de últimas voluntades y particularidades del derecho foral.

> Esta skill orienta sobre el marco general de los testamentos.
> **No sustituye asesoramiento jurídico o notarial profesional.**
> El derecho sucesorio varía significativamente entre comunidades
> autónomas con derecho foral propio.

---

## 1. Qué es un testamento

El testamento es el **acto jurídico** por el que una persona (testador)
dispone de sus bienes y derechos para después de su muerte. En España,
se rige por el **Código Civil** (arts. 657-743) y, en las comunidades
con derecho foral propio, por sus respectivas normativas.

Cualquier persona mayor de 14 años (o mayor de edad para el ológrafo)
puede otorgar testamento, siempre que tenga capacidad para ello.

URL: `https://www.notariado.org`

---

## 2. Tipos de testamento

### Testamento abierto ante notario (el más habitual)

- El testador expresa su voluntad ante un **notario**, que lo redacta
  y lo conserva en su protocolo.
- Es el más seguro y recomendable: evita problemas de interpretación
  y el notario verifica la capacidad del testador.
- **Coste**: entre **40 y 60 euros** aproximadamente (arancel
  notarial regulado). Es uno de los trámites notariales más económicos.
- Ventaja: no se puede perder ni destruir (queda en el protocolo
  notarial y registrado en el RGAUV).

### Testamento cerrado

- El testador entrega al notario un sobre cerrado con su última
  voluntad. El notario no conoce el contenido.
- Poco utilizado. Riesgo de defectos formales que lo invaliden.
- Se deposita ante el notario y se autoriza el acta de otorgamiento.

### Testamento ológrafo

- Escrito **enteramente a mano** por el testador, con fecha y firma.
- Solo pueden otorgarlo personas **mayores de edad**.
- Ventaja: gratuito y privado.
- Inconvenientes: riesgo de pérdida, destrucción, problemas de
  interpretación. Debe protocolizarse ante notario dentro de los
  **5 años** siguientes al fallecimiento.
- Requiere verificación judicial de autenticidad (cotejo de letra).

### Testamentos especiales

- **Militar**: en tiempo de guerra, ante oficial.
- **Marítimo**: a bordo de un buque, ante comandante.
- **En peligro de muerte**: ante 5 testigos, sin notario. Caduca a
  los 2 meses si el testador sobrevive.
- **En caso de epidemia**: ante 3 testigos mayores de 16 años.

---

## 3. El sistema de legítimas (derecho común)

En España (derecho común, Código Civil) no puedes disponer libremente
de todos tus bienes. La ley reserva una parte obligatoria
(**legítima**) a determinados herederos llamados **herederos forzosos**
o **legitimarios**.

### Los tres tercios

La herencia se divide conceptualmente en tres partes:

| Tercio | Para quién | Libertad del testador |
|---|---|---|
| **Legítima estricta** (1/3) | Herederos forzosos, a partes iguales | Sin libertad: se reparte obligatoriamente |
| **Mejora** (1/3) | Herederos forzosos, pero el testador puede elegir cómo repartirlo entre ellos | Libertad limitada: solo entre legitimarios |
| **Libre disposición** (1/3) | Quien quiera el testador | Libertad total |

### Herederos forzosos

1. **Hijos y descendientes**: les corresponden 2/3 de la herencia
   (legítima estricta + mejora).
2. **Padres y ascendientes** (si no hay descendientes): les corresponde
   1/2 de la herencia (o 1/3 si el cónyuge sobrevive).
3. **Cónyuge viudo**: no hereda en propiedad por legítima, sino en
   **usufructo**:
   - Con hijos: usufructo del tercio de mejora.
   - Con ascendientes: usufructo de 1/2 de la herencia.
   - Sin descendientes ni ascendientes: usufructo de 2/3.

### Desheredación

Solo es posible por las **causas tasadas** en el Código Civil
(arts. 852-855):

- Negar alimentos al testador.
- Maltrato de obra o injurias graves.
- Haber sido privado de la patria potestad (para hijos).
- Atentar contra la vida del testador.

La desheredación debe hacerse **expresamente en el testamento**,
indicando la causa. Si el desheredado la impugna y no se prueba la
causa, recupera su legítima.

---

## 4. Derecho foral: diferencias territoriales

Seis comunidades autónomas tienen **derecho civil propio** en materia
sucesoria, con reglas de legítimas diferentes al Código Civil:

### Cataluña

- Legítima: **25 %** del valor de la herencia (no en bienes concretos,
  sino como crédito).
- Legitimarios: solo hijos/descendientes. El cónyuge no es legitimario,
  pero tiene derecho a la cuarta viudal si carece de medios.

### Aragón

- **Legítima colectiva**: 1/2 de la herencia, pero el testador puede
  repartirla libremente entre todos los descendientes (puede dejar
  todo a uno solo).
- Gran libertad de distribución.

### Navarra

- **No existe legítima material**. La legítima es simbólica
  ("5 sueldos febles y una robada de tierra").
- Libertad de testar prácticamente total.

### País Vasco

- Legítima: 1/3 de la herencia para descendientes.
- El testador puede elegir cómo distribuirla entre ellos.
- Sistema flexible.

### Baleares

- Mallorca y Menorca: legítima similar al Código Civil pero con
  particularidades.
- Ibiza y Formentera: sistema propio (heredero universal obligatorio
  y "escreix").

### Galicia

- Legítima: 1/4 de la herencia para descendientes.
- El testador puede asignarla a uno o varios hijos.

**Importante**: la ley aplicable depende de la **vecindad civil** del
fallecido, no de dónde se encuentren los bienes ni de dónde se otorgó
el testamento.

---

## 5. Cómo otorgar testamento

### Pasos

1. **Decidir** cómo quieres repartir tus bienes (respetando las
   legítimas de tu vecindad civil).
2. **Pedir cita** con un notario. No hace falta documentación especial,
   solo el DNI/NIE.
3. **Expresar tu voluntad** al notario. Él te asesora y redacta el
   testamento conforme a la ley.
4. **Firmar** el testamento en presencia del notario.
5. El notario lo **inscribe** en el Registro General de Actos de Última
   Voluntad (RGAUV).

### Coste

- Arancel regulado: entre **40 y 60 euros** para un testamento estándar.
- Si incluye cláusulas complejas (fideicomisos, sustituciones), puede
  ser algo más.
- Es uno de los documentos notariales más baratos.

### Modificación y revocación

- El testamento se puede **modificar o revocar** en cualquier momento
  otorgando uno nuevo.
- El último testamento válido es el que prevalece.
- No es necesario destruir el anterior; el nuevo lo revoca
  automáticamente en lo que sea incompatible.

---

## 6. Registro General de Actos de Última Voluntad (RGAUV)

El RGAUV es un registro del Ministerio de Justicia que inscribe
**la existencia** de testamentos otorgados ante notario (no su
contenido).

### Para qué sirve

- Para saber **si una persona fallecida dejó testamento** y ante qué
  notario.
- Es obligatorio consultarlo tras un fallecimiento antes de tramitar
  la herencia.

### Cómo obtener el certificado

- **Online**: sede electrónica del Ministerio de Justicia
  (`https://sede.mjusticia.gob.es`), con certificado digital o Cl@ve.
- **Presencial**: en la Gerencia Territorial del Ministerio de Justicia.
- **Plazo**: solo se puede solicitar a partir de **15 días hábiles**
  desde el fallecimiento.
- **Coste**: tasas de aproximadamente 4 euros.

### Qué indica el certificado

- Si consta o no testamento inscrito.
- Fecha del último testamento y notario autorizante.
- No revela el contenido del testamento.

---

## 7. Testamento y pareja de hecho

Las parejas de hecho **no son herederas legales** en la mayoría de las
comunidades autónomas salvo que el testamento lo establezca
expresamente. Algunas comunidades (Cataluña, País Vasco, Navarra) les
reconocen ciertos derechos sucesorios, pero siempre inferiores a los
del cónyuge.

**Consejo práctico**: si convives en pareja de hecho y quieres que tu
pareja herede, es imprescindible hacer testamento.

---

## 8. Resumen rápido

```
TIPOS DE TESTAMENTO:
  ├── Abierto ante notario (el más habitual, 40-60 €)
  ├── Cerrado (poco usado)
  ├── Ológrafo (manuscrito, gratuito, más arriesgado)
  └── Especiales (militar, marítimo, peligro de muerte)

LEGÍTIMAS (derecho común):
  ├── 1/3 legítima estricta → hijos a partes iguales
  ├── 1/3 de mejora → hijos, el testador elige reparto
  └── 1/3 libre disposición → quien quiera el testador

DERECHO FORAL (distinto):
  ├── Cataluña: legítima 25 % (como crédito)
  ├── Aragón: 1/2 colectiva (muy flexible)
  ├── Navarra: sin legítima material
  ├── País Vasco: 1/3 para descendientes
  ├── Baleares: varía por isla
  └── Galicia: 1/4 para descendientes

REGISTRO DE ÚLTIMAS VOLUNTADES:
  ├── Ministerio de Justicia (sede electrónica)
  ├── Se pide desde 15 días hábiles tras el fallecimiento
  └── Indica si hay testamento y ante qué notario
```

---

## Cuándo NO usar esta skill

- Si pregunta por los **pasos prácticos tras un fallecimiento**
  (tramitación de herencia, aceptación, renuncia) → **herencias**.
- Si pregunta por el **Impuesto de Sucesiones y Donaciones**
  → **fiscalidad-sucesiones-donaciones**.
- Si pregunta por **poderes notariales** → **poder-notarial**.
- Si pregunta por el **texto de una ley** (Código Civil, etc.)
  → **boe**.
- Si pregunta por **certificados del Registro Civil** (defunción,
  nacimiento) → **registro-civil**.
- Si pregunta por **compraventa de vivienda** y escrituras
  → **vivienda-compraventa**.
