---
name: sucesiones-donaciones-jaimebs2
title: Fiscalidad -- Impuesto de Sucesiones y Donaciones (ISD)
description: 'Use when the user asks about inheritance tax or gift tax in Spain (Impuesto de Sucesiones y Donaciones, ISD): when it applies (inheritance, legacy, gift, life insurance), regional competence (each Comunidad Autonoma sets its own rates and allowances), kinship groups (I-IV), tax structure (base, reductions, tariff, multiplier coefficients), filing deadlines (6 months for inheritance, 30 business days for gifts), Modelo 650 (sucesiones) and Modelo 651 (donaciones), major regional differences (Madrid 99% rebate, etc.), family business donation, donation accumulation rules. Triggers on: ''impuesto sucesiones'', ''impuesto donaciones'', ''herencia impuestos'', ''heredar piso'', ''donar dinero'', ''donar vivienda'', ''modelo 650'', ''modelo 651'', ''ISD'', ''sucesiones y donaciones'', ''cuanto se paga por herencia'', ''reduccion por parentesco'', ''bonificacion herencia'', ''donacion padre hijo'', ''plusvalia herencia'', ''aceptar herencia'', ''impuesto herencia comunidad autonoma''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/fiscalidad/sucesiones-donaciones
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# Fiscalidad -- Impuesto de Sucesiones y Donaciones (ISD)

Guia completa sobre el Impuesto de Sucesiones y Donaciones en Espana:
cuando se paga, como se calcula, que modelos se presentan, y las enormes
diferencias entre comunidades autonomas.

> **Competencia autonomica**: cada Comunidad Autonoma fija sus propias
> reducciones, bonificaciones y tarifas. Esta skill explica el marco
> estatal general. Para una consulta concreta, hay que verificar la
> normativa de la CCAA correspondiente.

> **No sustituye asesoramiento fiscal ni juridico profesional.**

---

## 1. Que es el ISD

El Impuesto de Sucesiones y Donaciones (ISD) es un tributo directo y
personal que grava las adquisiciones gratuitas de bienes y derechos:

| Hecho imponible | Cuando se devenga |
|---|---|
| **Sucesion** (herencia, legado) | Fallecimiento del causante |
| **Donacion** (inter vivos) | Acto de donacion |
| **Seguro de vida** | Fallecimiento del asegurado (si beneficiario != tomador/heredero) |

Se regula en la **Ley 29/1987** y el **Real Decreto 1629/1991**
(Reglamento).

### Quien paga

- **Sucesiones**: los **herederos** o legatarios (cada uno por su parte).
- **Donaciones**: el **donatario** (quien recibe).
- **Seguros de vida**: el **beneficiario**.

---

## 2. Competencia autonomica

El ISD es un impuesto **cedido a las comunidades autonomas**, que pueden
regular:

- Reducciones en la base imponible.
- Tarifa (escala de gravamen).
- Cuantias del patrimonio preexistente.
- Bonificaciones en la cuota.

**Consecuencia**: la carga fiscal puede variar enormemente de una CCAA
a otra. Una misma herencia puede costar desde practicamente 0 (Madrid)
hasta decenas de miles de euros (otras comunidades, segun parentesco y
cuantia).

### Ejemplos de bonificaciones autonomicas (orientativo)

| CCAA | Bonificacion tipica (Grupo I-II: descendientes/ascendientes/conyuge) |
|---|---|
| **Madrid** | 99 % en cuota (tanto sucesiones como donaciones) |
| **Andalucia** | Exencion para bases < 1 M EUR (Grupo I-II) |
| **Cataluna** | Reducciones por parentesco, sin bonificacion general en cuota |
| **Comunidad Valenciana** | 99 % (Grupo I-II, con limites) |
| **Pais Vasco / Navarra** | Normativa foral propia, muy favorable para familiares directos |
| **Galicia** | Reducciones significativas para grupos I-II |

**Estas cifras son orientativas y pueden cambiar.** Siempre verificar
la normativa vigente de la CCAA.

### Que CCAA es competente

- **Sucesiones**: la CCAA de **residencia habitual del fallecido** (en los
  5 anos anteriores al fallecimiento).
- **Donaciones de inmuebles**: la CCAA donde **radique el inmueble**.
- **Donaciones de otros bienes**: la CCAA de **residencia habitual del
  donatario**.

---

## 3. Grupos de parentesco

La normativa estatal clasifica a los beneficiarios en cuatro grupos, que
determinan las reducciones aplicables:

| Grupo | Parentesco | Reduccion estatal |
|---|---|---|
| **I** | Descendientes < 21 anos | 15.956,87 EUR + 3.990,72 EUR por ano < 21 (max. total 47.858,59 EUR) |
| **II** | Descendientes >= 21 anos, ascendientes, conyuge | 15.956,87 EUR |
| **III** | Colaterales 2.o y 3er grado (hermanos, tios, sobrinos), ascendientes/descendientes por afinidad | 7.993,46 EUR |
| **IV** | Colaterales 4.o grado y mas, extranos | Sin reduccion |

Las CCAA pueden mejorar (y mejoran) estas reducciones.

### Reducciones adicionales (normativa estatal)

- **Seguro de vida**: hasta 9.195,49 EUR (Grupos I y II).
- **Empresa familiar / participaciones**: 95 % del valor, si se cumplen
  requisitos de mantenimiento (10 anos en sucesiones, 5 en donaciones
  si hay normativa autonomica).
- **Vivienda habitual del fallecido**: 95 % del valor (max. 122.606,47 EUR
  por heredero), con obligacion de mantener 10 anos.
- **Discapacidad**: 47.858,59 EUR (>= 33 %) o 150.253,03 EUR (>= 65 %).

---

## 4. Estructura del calculo

```
1. Masa hereditaria bruta (valor bienes + derechos)
   - Deudas y cargas deducibles
   - Gastos deducibles (entierro, ultima enfermedad)
   = Masa hereditaria neta

2. Parte individual de cada heredero (segun testamento o ley)
   + Seguros de vida percibidos
   + Ajuar domestico (3 % del caudal relicto, presuncion)
   = BASE IMPONIBLE

3. Base imponible
   - Reducciones (parentesco, discapacidad, vivienda, empresa familiar)
   = BASE LIQUIDABLE

4. Base liquidable x TARIFA (escala progresiva) = CUOTA INTEGRA

5. Cuota integra x COEFICIENTE MULTIPLICADOR
   (segun parentesco y patrimonio preexistente)
   = CUOTA TRIBUTARIA

6. Cuota tributaria
   - Bonificaciones autonomicas
   = CUOTA A PAGAR
```

### Tarifa estatal (supletoria)

| Base liquidable (EUR) | Tipo marginal |
|---|---|
| 0 -- 7.993,46 | 7,65 % |
| 7.993,46 -- 15.980,91 | 8,50 % |
| 15.980,91 -- 23.968,36 | 9,35 % |
| 23.968,36 -- 31.955,81 | 10,20 % |
| 31.955,81 -- 39.943,26 | 11,05 % |
| 39.943,26 -- 47.930,72 | 11,90 % |
| 47.930,72 -- 55.918,17 | 12,75 % |
| 55.918,17 -- 63.905,62 | 13,60 % |
| 63.905,62 -- 71.893,07 | 14,45 % |
| 71.893,07 -- 79.880,52 | 15,30 % |
| 79.880,52 -- 119.757,67 | 16,15 % |
| 119.757,67 -- 159.634,83 | 18,70 % |
| 159.634,83 -- 239.389,13 | 21,25 % |
| 239.389,13 -- 398.777,54 | 25,50 % |
| 398.777,54 -- 797.555,08 | 29,75 % |
| Mas de 797.555,08 | 34,00 % |

### Coeficientes multiplicadores (normativa estatal)

Dependen del **patrimonio preexistente** del beneficiario y del grupo
de parentesco:

| Patrimonio preexistente (EUR) | Grupos I-II | Grupo III | Grupo IV |
|---|---|---|---|
| 0 -- 402.678,11 | 1,0000 | 1,5882 | 2,0000 |
| 402.678,11 -- 2.007.380,43 | 1,0500 | 1,6676 | 2,1000 |
| 2.007.380,43 -- 4.020.770,98 | 1,1000 | 1,7471 | 2,2000 |
| Mas de 4.020.770,98 | 1,2000 | 1,9059 | 2,4000 |

---

## 5. Plazos de presentacion

| Tipo | Plazo | Modelo |
|---|---|---|
| **Sucesiones** | **6 meses** desde el fallecimiento | **650** |
| **Donaciones** | **30 dias habiles** desde la donacion | **651** |

### Prorroga en sucesiones

Se puede solicitar una prorroga de **6 meses mas** (total 12 meses)
dentro de los **5 primeros meses** del plazo original. La prorroga
genera intereses de demora.

### Donde se presenta

- Oficinas de la CCAA competente (no en la AEAT, salvo Pais Vasco
  y Navarra que tienen haciendas forales).
- Muchas CCAA permiten presentacion telematica.

---

## 6. Donaciones: aspectos clave

### Requisitos para aplicar beneficios fiscales

Muchas CCAA exigen que la donacion se formalice en **escritura publica**
ante notario para aplicar las reducciones y bonificaciones.

### Acumulacion de donaciones

Las donaciones entre las mismas personas en un plazo de **3 anos** se
acumulan a efectos de calcular el impuesto (se suman las bases para
aplicar la escala progresiva).

### Donacion de vivienda

Si se dona una vivienda, ademas del ISD se puede generar:
- **Plusvalia municipal** (IIVTNU) -> ver **fiscalidad-impuestos-locales**.
- **Ganancia patrimonial en IRPF** para el donante (aunque no reciba
  dinero, tributa por la diferencia entre valor de adquisicion y valor
  de transmision).

### Donacion de dinero

Forma habitual de ayudar a hijos para comprar vivienda. Muchas CCAA
tienen reduccion especifica si el dinero se destina a la compra de
primera vivienda habitual.

---

## 7. Sucesiones: aspectos practicos

### Pasos tras el fallecimiento

1. Obtener certificado de defuncion.
2. Solicitar certificado de ultimas voluntades y seguro de vida
   (Registro General de Actos de Ultima Voluntad, plazo: 15 dias
   habiles tras el fallecimiento).
3. Obtener copia del testamento (si existe) del notario que lo
   otorgo.
4. Inventariar bienes y deudas.
5. Formalizar la aceptacion/particion de herencia ante notario
   (escritura publica).
6. Liquidar el ISD (Modelo 650) y la plusvalia municipal si hay
   inmuebles.
7. Inscribir en el Registro de la Propiedad los inmuebles heredados.

### Renuncia a la herencia

Se puede renunciar a la herencia si las deudas superan los bienes.
La renuncia debe ser **expresa y ante notario**. Si se renuncia, el
ISD no se devenga para el renunciante.

---

## 8. Resumen rapido

```
IMPUESTO DE SUCESIONES Y DONACIONES (ISD):
  Competencia autonomica → cada CCAA fija reducciones y bonificaciones

SUCESIONES:
  Plazo: 6 meses desde fallecimiento (prorrogable 6 mas)
  Modelo: 650
  Grupos parentesco: I (desc. <21) / II (desc. >=21, asc., conyuge)
                     III (hermanos, tios, sobrinos) / IV (extranos)

DONACIONES:
  Plazo: 30 dias habiles
  Modelo: 651
  Frecuente: escritura publica necesaria para bonificaciones
  Acumulacion: donaciones en 3 anos se suman

CALCULO:
  Base imponible - reducciones = base liquidable
  Base liquidable x tarifa = cuota integra
  Cuota integra x coeficiente multiplicador = cuota tributaria
  Cuota tributaria - bonificacion autonomica = a pagar

DIFERENCIAS ENORMES POR CCAA:
  Madrid: bonificacion 99 %
  Andalucia: exencion < 1 M EUR (Grupo I-II)
  Otras: mucho mas gravoso
```

---

## Cuando NO usar esta skill

- Si pregunta por **compraventa de vivienda usada** (ITP, AJD) ->
  **fiscalidad-itp-ajd**.
- Si pregunta por la **plusvalia municipal** al heredar/donar un
  inmueble -> **fiscalidad-impuestos-locales**.
- Si pregunta por tramites de **aceptacion de herencia** (aspecto
  juridico, no fiscal) -> **justicia-herencias**.
- Si pregunta por **IRPF** (declaracion de la renta) ->
  **fiscalidad-irpf-asalariados** o **fiscalidad-irpf-autonomos**.
- Si pregunta por **IVA** -> **fiscalidad-iva**.
- Si pregunta por el **Impuesto de Sociedades** ->
  **fiscalidad-sociedades**.
- Si pregunta por **estadisticas de recaudacion** -> **aeat**.
