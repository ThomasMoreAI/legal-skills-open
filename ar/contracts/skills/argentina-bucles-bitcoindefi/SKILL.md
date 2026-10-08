---
name: argentina-bucles-bitcoindefi
title: Bucle de fundamentación · Redacción de escritos desde cero
description: 'Bucle de fundamentación para construir DESDE CERO un escrito de fondo bajo derecho argentino (demanda, contestación, recurso, alegato, descargo administrativo): encuadre, investigación de fuentes en SAIJ, esqueleto argumental en cascada, borrador, crítica adversarial y verificación de citas. Usar cuando hay que redactar y fundamentar un escrito nuevo; para auditar uno ya escrito usar argentina-diagnostico.'
author: Bitcoindefi
author_url: https://github.com/Bitcoindefi/agente-smith/tree/main/skills/argentina-bucles
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: contracts
language: es
---

# Bucle de fundamentación · Redacción de escritos desde cero

Skill original de Agente Smith (MIT). Método iterativo en 7 pasos: no se redacta nada
hasta tener el esqueleto argumental montado sobre fuentes verificadas.

## Paso 1 · Encuadre

- **Tipo de pieza y molde PRIMERO:** identificar qué presentación es (demanda,
  descargo de faltas, recurso, nota…) y ante qué órgano, con la skill
  `argentina-formatos`. El esqueleto del Paso 3 y el borrador del Paso 4 se montan
  sobre ESE molde — jamás sobre el esqueleto de demanda por defecto. Ante la duda,
  preguntar.
- Hechos en una cronología limpia (fecha → hecho → prueba que lo respalda).
- Pretensión exacta: ¿qué se pide y contra quién?
- Jurisdicción y fuero (condiciona procedimiento, plazos y estilo). Si falta, preguntar.
- Restricciones estratégicas del caso (qué NO decir, qué no convalidar, qué reservar).
  Leerlas de la ficha del caso y respetarlas como reglas duras.

## Paso 2 · Investigación de fuentes (SAIJ)

Para cada eje del argumento:
1. `saij_buscar_legislacion` → identificar la norma → `saij_documento(uuid)` → **leer
   el texto real** y su vigencia. La norma se cita por lo que dice, no por lo que se
   recuerda.
2. `saij_buscar_jurisprudencia` → fallos que sostengan (y fallos que contradigan — se
   buscan a propósito). Leer con `saij_documento` antes de citar.
3. Registrar cada fuente: norma/fallo · cita textual breve · uuid · URL.
4. Lo no verificable queda 🔲 y NO entra al escrito como afirmación.

## Paso 3 · Esqueleto argumental

- Cada argumento como silogismo: **norma (verificada) → hecho (probado) → consecuencia
  (pedida)**. Si falta la prueba del hecho, el argumento baja a subsidiario o se
  descarta.
- Cascada de subsidiariedad: argumento principal → subsidiarios en orden ("aun si no
  se admitiera X, entonces Y"). Las nulidades e inadmisibilidades van como cuestión
  previa, sin convalidar nada.
- Un párrafo = una idea. Numerar secciones.

## Paso 4 · Borrador

Redactar sección por sección sobre el esqueleto: encabezado y personería → objeto →
hechos → prueba → derecho → petitorio → reservas. Estilo: claro, sobrio, sin adjetivos
que no prueben nada; cada afirmación fáctica con su respaldo citado.

## Paso 5 · Crítica adversarial (el bucle)

Releer el borrador dos veces con sombreros distintos:
- **Como contraparte:** ¿qué contestaría? ¿qué hecho negaría? ¿qué debilidad explota?
  → reforzar o podar.
- **Como juez/autoridad:** ¿qué falta probar? ¿qué pedido es incongruente o excesivo?
  ¿dónde hay ruido que tapa el punto fuerte? → simplificar.
Repetir el bucle hasta que una pasada no produzca cambios sustanciales (máx. 3).

## Paso 6 · Verificación final de citas (auditoría sistemática)

**Usar skill `argentina-auditoria-citas` (auditoría obligatoria).**

1. Crear tabla de fuentes verificadas: archivo `jurisprudencia/fuentes-[identificador].md`
   con todas las normas/fallos investigados en Paso 2 (formato en skill argentina-auditoria-citas).
2. **Correr auditoría:** skill `argentina-auditoria-citas` sobre el escrito borrador.
3. Resolver TODO lo que sea 🔴 (bloqueante):
   - Opción A: incorporar la norma/fallo a la tabla (buscar en SAIJ si falta).
   - Opción B: eliminar la cita y reformular el párrafo sin ella.
   - Opción C: marcar deliberadamente con 🔲 si es genérica (decisión del abogado).
4. Confirmar TODO lo que sea 🔲 (pendiente): es decisión irreversible que va en el cierre.
5. Entregar:
   - Escrito final (100% citas verificadas ✅ o deliberadamente 🔲).
   - Tabla de fuentes (jurisprudencia/fuentes-*.md).
   - Reporte de auditoría (generado por argentina-auditoria-citas).

## Paso 7 · Cierre

Correr `argentina-diagnostico` sobre el resultado (auditoría de las 9 secciones) y
entregar: escrito + tabla de fuentes + reporte de auditoría de citas + lista de 
decisiones estratégicas que quedan en cabeza del abogado firmante.

## Reglas duras

- Jamás inventar jurisprudencia, carátulas o números: si no está verificado, no se cita.
- Las reglas estratégicas del caso (ficha) prevalecen sobre cualquier preferencia de
  redacción.
- El escrito final lo firma y decide el abogado: señalar toda decisión irreversible.
