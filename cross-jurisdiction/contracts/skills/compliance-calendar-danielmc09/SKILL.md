---
name: compliance-calendar-danielmc09
title: Compliance Calendar
description: '[JURISDICTION] Deriva del pack de la jurisdiccion el calendario de obligaciones recurrentes y los disparadores por umbral, y reporta que vence y que se acaba de activar. Usar en revision periodica, al cruzar un umbral de ingresos o activos, o al contratar a la primera persona.'
author: Danielmc09
author_url: https://github.com/Danielmc09/jurisdiction-latam/tree/main/jurisdiction-kit/skills/compliance-calendar
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: contracts
language: es
---

# Compliance Calendar

El kit resuelve el día 1. Este skill resuelve el día 400.

## La diferencia con un calendario cualquiera

**Este skill no contiene ni una sola fecha.** Todas se derivan de las capas
cargadas: nacional, territorial, sectorial y de módulo.

Un calendario con fechas escritas dentro del skill queda obsoleto en
silencio el año siguiente. Aquí, si el pack está VENCIDO, **el skill se
detiene** en vez de reportar fechas viejas con seguridad.

## Requiere

`perfil-legal.md` · las capas cargadas · verificar el semáforo de vigencia

**Si alguna capa está VENCIDA, detente y exige `jurisdiction-research`.**
Reportar un vencimiento con datos de hace dos años es peor que no reportar.

---

## Los tres tipos de obligación

La mayoría de los calendarios solo modelan el primero. Los otros dos son
los que hunden a un fundador.

### 1. Recurrentes — por fecha
Se repiten en un ciclo fijo. Renovación del registro mercantil,
declaraciones periódicas, renovación de licencias, actas obligatorias.

```
- [recurrente] <obligación> · cada <ciclo> · vence <fecha o regla>
  · ante <entidad> · consecuencia: <qué pasa si no> · fuente: <URL>
```

### 2. Disparadas por umbral — **las peligrosas**
No tienen fecha. Se activan cuando el negocio cruza una línea, y **casi
siempre se cruza sin darse cuenta.**

```
- [umbral] <obligación> · se activa al superar <cifra + unidad + año>
  · plazo desde el disparo: <tiempo> · fuente: <URL>
```

Ejemplos del tipo: superar cierto nivel de ingresos y quedar obligado a
facturación electrónica; superar cierto nivel de activos y quedar obligado
a inscribirse en un registro; alcanzar cierto número de empleados y quedar
obligado a un reglamento interno.

**Regla del skill:** por cada obligación de umbral, pregunta al humano
**dónde está hoy** respecto de esa cifra. Un umbral sin posición conocida
no se puede vigilar.

### 3. Disparadas por evento
Se activan por un hecho, no por una fecha ni una cifra: contratar a la
primera persona, abrir sucursal, empezar a tratar datos de menores, recibir
inversión, exportar.

```
- [evento] <obligación> · se activa cuando <hecho>
  · plazo desde el hecho: <tiempo> · fuente: <URL>
```

---

## Procedimiento

### Modo 1 · Construir el calendario

1. Lee todas las capas cargadas
2. Extrae toda línea marcada `[recurrente]`, `[umbral]` o `[evento]`
3. **Para cada umbral, pregunta la posición actual del negocio.** Sin eso,
   no hay vigilancia posible
4. **Para cada evento, pregunta si ya ocurrió**
5. Escribe `calendario-compliance.md` con las tres listas separadas
6. Declara qué no pudo derivarse porque el pack no lo marcó

### Modo 2 · Reportar

```
## Vencido
- <obligación> · venció <fecha> · consecuencia: <cuál> · <entidad>

## Próximos 30 días
## Próximos 90 días

## Umbrales — posición actual
| Obligación | Umbral | Dónde estás | Margen |

## Umbrales cruzados desde la última revisión
- <obligación> · se activó · plazo: <tiempo> · **ACTUAR**

## Eventos ocurridos sin atender
- <obligación> · el hecho ocurrió el <fecha> · plazo: <tiempo>
```

**El bloque de umbrales va antes que el de fechas.** Un vencimiento de
fecha se ve venir; un umbral cruzado ya pasó.

### Modo 3 · Registrar cumplimiento

Marca lo cumplido con fecha y evidencia. **No borres el histórico**: la
prueba de haber cumplido es tan importante como cumplir.

---

## Cadencia sugerida

| Cuándo | Qué |
|---|---|
| Mensual | Reporte de próximos 90 días y posición de umbrales |
| Al cerrar el año fiscal | Revisar cifras que caducan y recalcular umbrales |
| Al ocurrir un evento | Revisar qué se activó |
| Cada 90 días | Verificar el semáforo de las capas |

---

## Qué NO hacer

- **No presenta el calendario como completo.** Deriva lo que el pack marcó;
  lo que el pack no marcó, no existe para él. Ese hueco se declara
- **No calcula fechas por analogía.** Si el pack no dice cuándo vence, dice
  "sin fecha verificada", no una estimación
- **No estima consecuencias ni sanciones** que no estén en el pack
- **No dice que estás al día.** Dice qué revisó y qué no pudo revisar
- No envía recordatorios. Se corre; no vigila solo

## Cierre obligatorio de todo reporte

> Este calendario deriva de las capas cargadas, verificadas el <fecha>. No
> es una lista exhaustiva de obligaciones legales. Las que el pack no
> registró no aparecen aquí. Confírmalo con un contador o abogado local.
