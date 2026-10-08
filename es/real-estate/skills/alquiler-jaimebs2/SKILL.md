---
name: alquiler-jaimebs2
title: Vivienda --- Alquiler de vivienda
description: 'Use when the user asks about renting a home in Spain: rental contracts (LAU), Ley 12/2023 por el derecho a la vivienda, duration and extensions, mandatory deposit (fianza), additional guarantees, rent updates (reference index replacing CPI), tenant and landlord rights, stressed market zones (zonas tensionadas), large landlords (grandes tenedores), tax deductions for rent, room rental, or eviction proceedings. Triggers on: ''alquiler vivienda'', ''alquiler piso'', ''contrato alquiler'', ''contrato arrendamiento'', ''LAU'', ''Ley Arrendamientos Urbanos'', ''Ley 12/2023'', ''ley vivienda'', ''fianza alquiler'', ''fianza piso'', ''subida alquiler'', ''actualización renta'', ''IPC alquiler'', ''índice referencia arrendamientos'', ''zona tensionada'', ''gran tenedor'', ''duración contrato alquiler'', ''prórroga alquiler'', ''desahucio impago'', ''desistimiento inquilino'', ''derechos inquilino'', ''deducción alquiler IRPF'', ''alquiler habitación'', ''depositar fianza''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/vivienda/alquiler
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

# Vivienda --- Alquiler de vivienda

Guía completa sobre el alquiler de vivienda en España: Ley de
Arrendamientos Urbanos (LAU), Ley 12/2023 por el derecho a la
vivienda, contratos, fianza, actualización de renta, derechos de
inquilino y arrendador, y zonas tensionadas.

> Esta skill orienta sobre la normativa general de arrendamientos.
> **No sustituye asesoramiento jurídico profesional.**

---

## 1. Marco legal

El alquiler de vivienda habitual en España se regula por:

- **Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos
  (LAU)**: norma principal que regula los contratos de arrendamiento.
- **Ley 12/2023, de 24 de mayo, por el derecho a la vivienda**:
  introduce zonas tensionadas, limitación de rentas para grandes
  tenedores, y modifica aspectos de la LAU.
- **Código Civil**: aplicable a alquileres de habitación y
  supletoriamente.

---

## 2. El contrato de alquiler

### Duración

| Tipo de arrendador | Duración mínima obligatoria | Prórroga obligatoria |
|---|---|---|
| **Persona física** | 5 años | + 3 años (prórroga tácita) |
| **Persona jurídica** (empresa, sociedad) | 7 años | + 3 años (prórroga tácita) |

- Si se pacta un plazo inferior (ej. 1 año), se prorroga
  automáticamente año a año hasta llegar a 5 (o 7) años, salvo que
  el inquilino comunique que no quiere renovar con **30 días** de
  antelación.
- Si transcurrido el plazo de 5 (o 7) años ninguna de las partes
  comunica con **4 meses** (arrendador) o **2 meses** (inquilino)
  de antelación que no desea renovar, el contrato se prorroga
  automáticamente **3 años más** (prórroga tácita, art. 10 LAU).

### Forma del contrato

- Puede ser **verbal o escrito**, pero se recomienda siempre escrito.
- Cualquiera de las partes puede exigir que se formalice por escrito.
- Debe incluir: identidad de las partes, identificación de la vivienda,
  duración, renta, fianza depositada, cláusulas adicionales.
- El certificado de eficiencia energética debe adjuntarse o su
  referencia debe constar en el contrato.

---

## 3. Fianza y garantías adicionales

### Fianza legal obligatoria

- **1 mensualidad** de renta en vivienda habitual (art. 36.1 LAU).
- El arrendador debe **depositar** la fianza en el organismo
  autonómico correspondiente (servicio de depósito de fianzas):
  - Madrid: IVIMA / Comunidad de Madrid.
  - Cataluña: INCASOL.
  - Andalucía: Junta de Andalucía.
  - etc.
- Se devuelve al finalizar el contrato, en un plazo de **30 días**
  desde la entrega de llaves. Si no se devuelve, devenga interés
  legal.
- Puede dedicarse a cubrir desperfectos o rentas impagadas, pero
  **no es el último mes de alquiler** (error habitual).

### Garantías adicionales

Desde la reforma de la LAU por RDL 7/2019:

- El arrendador puede exigir como máximo **2 mensualidades
  adicionales** como garantía (fianza + 2 meses = 3 meses máximo).
- Formas: depósito adicional, aval bancario, seguro de impago.
- En contratos de más de 5 (o 7) años, se pueden pactar garantías
  superiores.

---

## 4. Actualización de la renta

### Hasta 2024

La renta se actualizaba según el **IPC** (Índice de Precios al
Consumo), salvo pacto de otro índice. Durante 2022-2024 se aplicaron
topes extraordinarios (2 % y 3 %) por la crisis inflacionaria.

### Desde 2025 --- Nuevo índice de referencia

La Ley 12/2023 establece que a partir de 2025 se aplica un **nuevo
índice de referencia para la actualización anual de los contratos de
arrendamiento de vivienda**, publicado por el INE, que sustituye al
IPC como índice por defecto.

- El índice lo publica el INE antes del 31 de diciembre de cada año.
- Se aplica a contratos que se actualicen a partir de su entrada en
  vigor.
- Si el contrato no pacta un índice, se aplica este nuevo índice.
- Si pacta el IPC u otro índice, se aplica el pactado.

### Procedimiento de actualización

1. La actualización solo puede hacerse en la **fecha de aniversario**
   del contrato (cada año).
2. El arrendador debe **comunicar por escrito** la actualización al
   inquilino con al menos **1 mes** de antelación.
3. Debe indicar el índice aplicado y el porcentaje de variación.
4. La nueva renta se aplica desde el mes siguiente a la comunicación.

---

## 5. Derechos del inquilino

### Prórroga obligatoria

- El contrato se extiende hasta 5 años (7 si persona jurídica) aunque
  se haya pactado menos (art. 9 LAU).
- Prórroga tácita de 3 años adicionales si nadie avisa (art. 10 LAU).

### Desistimiento

- El inquilino puede desistir del contrato tras **6 meses** desde la
  firma (art. 11 LAU).
- Debe comunicarlo con **30 días** de antelación.
- Indemnización: si se pactó en contrato, 1 mensualidad por cada año
  que falte por cumplir (proporcional por meses).

### Obras de conservación

- El arrendador está obligado a realizar las **obras de conservación**
  necesarias para mantener la vivienda habitable (art. 21 LAU).
- Urgentes: el inquilino puede realizarlas y exigir reembolso.
- No puede subir la renta por estas obras (salvo que sean de mejora).

### Derecho de adquisición preferente

Si el arrendador vende la vivienda:
- El inquilino tiene **derecho de tanteo** (30 días desde la
  notificación de la venta).
- Y **derecho de retracto** (30 días desde la inscripción en el
  Registro).
- Se puede renunciar en el contrato.

### Subrogación

Si el inquilino fallece, el contrato puede subrogarse en favor del
cónyuge, pareja de hecho, descendientes menores o dependientes que
convivieran habitualmente (art. 16 LAU).

---

## 6. Derechos del arrendador

### Recuperación por necesidad

El arrendador persona física puede recuperar la vivienda para sí
mismo, familiares de primer grado o cónyuge tras **1 año** de
contrato (art. 9.3 LAU), con las siguientes condiciones:

- Comunicación con **2 meses** de antelación.
- Debe destinarla a vivienda permanente.
- Si no la ocupa en **3 meses** o no la habita al menos 2 años, el
  inquilino puede volver en las mismas condiciones o exigir
  indemnización (1 mensualidad por año que faltase).

### Desahucio por impago (art. 27 LAU)

Si el inquilino no paga la renta:

1. **Requerimiento de pago**: burofax o comunicación fehaciente.
2. **Demanda de desahucio**: ante el juzgado de primera instancia.
3. **Enervación del desahucio**: el inquilino puede paralizar el
   proceso pagando toda la deuda **antes del juicio** (solo una vez;
   no opera si ya se le requirió fehacientemente con 30 días de
   antelación).
4. **Lanzamiento**: si no paga ni enerva, el juez fija fecha de
   desalojo.

La Ley 12/2023 introduce medidas de protección adicionales para
inquilinos en situación de **vulnerabilidad social o económica**
(suspensión de lanzamientos, derivación a servicios sociales).

---

## 7. Zonas tensionadas (Ley 12/2023)

### Qué son

Áreas donde el mercado de alquiler tiene una situación de
**desequilibrio** entre oferta y demanda. Las declara la comunidad
autónoma correspondiente, a petición del ayuntamiento, cuando:

- La carga media del coste de la hipoteca o alquiler + gastos
  + suministros supere el **30 %** de los ingresos medios de los
  hogares de la zona.
- Y el precio del alquiler o compra haya subido más de **3 puntos
  por encima del IPC** en los 5 años anteriores.

### Efectos en la renta

| Tipo de arrendador | Efecto en zona tensionada |
|---|---|
| **Gran tenedor** (10+ viviendas en esa zona) | La renta del nuevo contrato no puede superar el **índice de referencia** publicado por el Ministerio |
| **No gran tenedor** | La renta del nuevo contrato no puede superar la renta del **contrato anterior** (con actualización por índice) |
| **Vivienda no alquilada en los últimos 5 años** | Se aplica el índice de referencia (como gran tenedor) |

### Gran tenedor

La Ley 12/2023 define como **gran tenedor** al propietario de:
- **10 o más inmuebles de uso residencial** en todo el territorio, o
- **5 o más inmuebles** si la comunidad autónoma así lo decide para
  zonas tensionadas.

---

## 8. Deducciones fiscales por alquiler

### Para el inquilino

- **Estatal**: deducción suprimida para contratos desde 2015. Mantienen
  el derecho los contratos anteriores al 01/01/2015 (régimen
  transitorio).
- **Autonómicas**: muchas comunidades autónomas mantienen deducciones
  propias (por menores de cierta edad, renta baja, familias numerosas,
  etc.). Varían enormemente entre CCAA.

### Para el arrendador

Reducción en el rendimiento neto del alquiler en IRPF:

| Supuesto | Reducción |
|---|---|
| **General** (desde Ley 12/2023) | 50 % |
| Zona tensionada + bajada de renta > 5 % | 90 % |
| Zona tensionada + nuevo contrato a joven (18-35 años) | 70 % |
| Vivienda rehabilitada en los 2 años anteriores | 60 % |

Estas reducciones aplican a contratos firmados a partir de la entrada
en vigor de la Ley 12/2023. Contratos anteriores mantienen el régimen
previo (60 % general).

---

## 9. Alquiler de habitación

El alquiler de una **habitación** dentro de una vivienda tiene un
régimen legal diferente:

- **No se rige por la LAU** (que regula vivienda completa como
  habitual), sino por el **Código Civil** y el acuerdo de las partes.
- No hay duración mínima obligatoria.
- No hay prórroga forzosa.
- La fianza es la que pacten las partes (no existe el mínimo de 1 mes
  ni el máximo de 2 meses adicionales de la LAU).
- El arrendador no está obligado a depositar la fianza en el organismo
  autonómico (aunque algunas CCAA lo exigen igualmente).

---

## 10. Resumen rápido

```
CONTRATO:
  ├── Duración mínima: 5 años (persona física) / 7 años (jurídica)
  ├── Prórroga tácita: +3 años si nadie avisa
  ├── Forma: escrito recomendado (puede ser verbal)
  └── Certificado energético obligatorio

FIANZA:
  ├── 1 mes obligatorio (depositar en organismo autonómico)
  ├── Garantías adicionales: máximo 2 meses más
  └── Devolución: 30 días desde entrega de llaves

ACTUALIZACIÓN DE RENTA:
  ├── Desde 2025: nuevo índice INE (sustituye al IPC por defecto)
  ├── Comunicación escrita con 1 mes de antelación
  └── Solo en la fecha de aniversario del contrato

DERECHOS DEL INQUILINO:
  ├── Prórroga obligatoria (5/7 años + 3 tácita)
  ├── Desistimiento tras 6 meses (preaviso 30 días)
  ├── Obras de conservación a cargo del arrendador
  └── Tanteo y retracto si se vende la vivienda

ZONAS TENSIONADAS (Ley 12/2023):
  ├── Gran tenedor: renta limitada por índice de referencia
  ├── No gran tenedor: renta máxima = renta anterior
  └── Declaradas por la comunidad autónoma

FISCALIDAD:
  ├── Inquilino: deducciones autonómicas (varían por CCAA)
  └── Arrendador: reducción 50-90 % en IRPF
```

---

## Cuándo NO usar esta skill

- Si necesita el **proceso de compraventa** de una vivienda -->
  **vivienda-compraventa**.
- Si pregunta por **hipotecas** --> **vivienda-hipotecas**.
- Si pregunta por el **Registro de la Propiedad** -->
  **vivienda-registro-propiedad**.
- Si pregunta por **comunidad de propietarios** (juntas, cuotas,
  obras, morosos) --> **vivienda-comunidad-propietarios**.
- Si pregunta por **IBI o plusvalía municipal** -->
  **fiscalidad-impuestos-locales**.
- Si pregunta por **IRPF de asalariados** (deducciones en detalle) -->
  **fiscalidad-irpf-asalariados** (cuando exista).
- Si pregunta por **datos catastrales** --> **catastro**.
- Si pregunta por **herencias de vivienda** -->
  **fiscalidad-sucesiones-donaciones**.
- Si pregunta por el **texto de la LAU o la Ley 12/2023** -->
  **boe**.
