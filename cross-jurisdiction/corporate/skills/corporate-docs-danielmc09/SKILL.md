---
name: corporate-docs-danielmc09
title: Corporate Docs
description: '[JURISDICTION] Arma la documentacion administrativa y societaria de una empresa: estatutos, objeto social, actas, libros, poderes y documentos estrategicos, separando lo que tiene fuerza legal de lo que no. Usar al constituir una sociedad, al reformar estatutos, o cuando falta la documentacion interna.'
author: Danielmc09
author_url: https://github.com/Danielmc09/jurisdiction-latam/tree/main/jurisdiction-kit/skills/corporate-docs
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: corporate
language: es
---

# Corporate Docs

La parte densa. Y la que más se arma mal, porque se mezclan tres cosas
distintas.

## Las tres familias — no se mezclan

| Familia | Fuerza legal | Se registra | Ejemplos |
|---|---|---|---|
| **Constitutivos** | **Sí** | Sí, ante el registro mercantil | Estatutos, objeto social, capital, administración |
| **Gobierno interno** | Parcial | No, pero pueden exigirse | Actas, libros, poderes, reglamentos |
| **Estratégicos** | **Ninguna** | No | Misión, visión, valores, código de cultura |

**El error más común:** meter la misión en los estatutos, o creer que la
visión es un requisito legal. No lo es. Nadie la registra y nadie la exige.

**Lo que sí importa legalmente es el objeto social**, y es otra cosa.

## Requiere

- El pack de la jurisdicción, sección de constitución de empresa
- La capa territorial: el registro mercantil es competencia local
- Tipo societario elegido, o la decisión pendiente

**Si el pack no tiene el contenido mínimo legal de los estatutos para ese
tipo societario, detente e investígalo.** Escribir estatutos sin conocer el
contenido obligatorio es garantizar que los rechacen.

---

# FAMILIA 1 · Constitutivos

## Objeto social — la decisión que la gente subestima

No es la misión. Define **qué puede hacer legalmente la sociedad.**

Dos caminos, y la ley de cada país decide cuáles existen:

| Enfoque | Ventaja | Riesgo |
|---|---|---|
| **Determinado** — lista de actividades | Claridad ante terceros y bancos | Cualquier giro nuevo exige reforma estatutaria |
| **Indeterminado** — "cualquier actividad lícita" | Flexibilidad total | Algunos terceros, bancos o licitaciones piden actividades explícitas |

`[VERIFICAR EN EL PACK]` Si la jurisdicción permite objeto indeterminado y
qué pasa si no se dice nada.

**No recomiendes uno.** Expón el intercambio y que decida el humano.

## Estatutos

Se arman en dos capas:

**Capa 1 — contenido mínimo legal.** Lo que la ley exige y sin lo cual el
registro **se abstiene de inscribir**. Sale del pack, no de una plantilla
genérica de internet.

**Capa 2 — lo opcional que conviene decidir ahora.** Reglas que si no se
pactan quedan sujetas a la regla supletoria de la ley, que puede no ser la
que quieres:

- Restricciones a la negociación de participaciones
- Derecho de preferencia
- Mayorías especiales para decisiones concretas
- Causales de exclusión de un socio
- Resolución de conflictos entre socios
- Reglas de sucesión o incapacidad del fundador

**Para un fundador único:** las capas 2 parecen innecesarias hoy y son
exactamente lo que se necesita el día que entra el segundo socio.
Escribirlas después cuesta una reforma estatutaria y una negociación.

`[REDACTAR CON ABOGADO]` — siempre. Este skill produce el borrador
estructurado y la lista de decisiones; no reemplaza la revisión.

## Salida

```
### <N>. <Cláusula>
<texto>

> Exigida por: <norma y artículo> · <URL>   ← si es de capa 1
> Opcional. Si no se pacta: <regla supletoria>  ← si es de capa 2
> [DECIDIR] <la pregunta concreta para el humano>
```

---

# FAMILIA 2 · Gobierno interno

Lo que no se registra pero puede exigirse en una auditoría, una diligencia
de inversión o una venta.

| Documento | Para qué |
|---|---|
| Acta de constitución | Deja registro de las decisiones fundacionales |
| Libro de actas | Toda decisión del máximo órgano |
| Libro de accionistas o socios | Quién tiene qué |
| Nombramiento de representante legal | Con aceptación del cargo |
| Poderes | Quién puede firmar qué y hasta cuánto |
| Reglamento interno de trabajo | Si aplica según número de empleados |
| Políticas obligatorias | Salen del pack: datos, seguridad, prevención |

`[VERIFICAR EN EL PACK]` Cuáles son obligatorios en esa jurisdicción, desde
qué tamaño, y si deben registrarse.

**Regla de las actas:** un acta se redacta el día de la decisión, no
después. Reconstruir actas hacia atrás es una señal de alerta en cualquier
diligencia.

---

# FAMILIA 3 · Estratégicos

**Cero fuerza legal.** Van aquí para que no se confundan con lo anterior.

## Advertencia obligatoria

> Misión, visión y valores no son documentos legales. No se registran, no
> se exigen y no producen efectos jurídicos. Escribirlos es útil para
> alinear un equipo y comunicar. **No confundirlos con el objeto social.**

## Cómo se escriben sin que suenen a plantilla

**Misión** — qué hace la empresa hoy, para quién, y por qué es distinto.
En presente. Sin adjetivos.

*Prueba:* si la misión sirve igual para un competidor, no es una misión.
Es una descripción de la categoría.

**Visión** — a dónde quiere llegar, con horizonte y verificable.

*Prueba:* si no se puede saber en cinco años si se cumplió o no, es un
deseo, no una visión.

**Valores** — cómo se decide cuando hay conflicto.

*Prueba dura:* un valor que nadie discutiría no es un valor. "Integridad"
no dice nada porque nadie declara lo contrario. Un valor real **implica
renunciar a algo**: "preferimos perder un cliente antes que prometer una
fecha que no podemos cumplir."

## Procedimiento

1. Pregunta por hechos, no por aspiraciones: ¿qué decisión difícil tomaron
   y por qué? ¿A qué cliente le dijeron que no?
2. Los valores salen de esas decisiones, no de una lista de adjetivos
3. Máximo 4 valores. Diez no se recuerdan y no guían nada
4. **Si el negocio no tiene aún decisiones difíciles tomadas, dilo.**
   Escribir valores antes de tener historia produce plantillas

---

## Qué NO hacer

- **No mezcles las tres familias en un documento**
- No pongas misión ni visión en los estatutos
- No escribas estatutos sin el contenido mínimo del pack
- **No generes cláusulas de responsabilidad, indemnidad ni resolución de
  conflictos.** Marca `[REDACTAR CON ABOGADO]`
- No recomiendes un tipo societario ni un enfoque de objeto social
- No copies estatutos de otra jurisdicción
- No produzcas valores genéricos. Si no hay material, dilo
- No entregues ningún documento sin su encabezado de borrador
