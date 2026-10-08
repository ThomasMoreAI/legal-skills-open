---
name: argentina-plazos-bitcoindefi
title: Cómputo de plazos · Derecho argentino
description: 'Computa plazos procesales, administrativos y de prescripción bajo derecho argentino: días hábiles judiciales, hábiles administrativos, corridos, en horas y en meses, con ferias, suspensiones y plazo de gracia, diferenciando jurisdicción (nacional/federal y provincias). Usar ante cualquier vencimiento, prescripción, caducidad, recurso o cómputo de plazo en causa judicial o administrativa argentina.'
author: Bitcoindefi
author_url: https://github.com/Bitcoindefi/agente-smith/tree/main/skills/argentina-plazos
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: litigation
language: es
---

# Cómputo de plazos · Derecho argentino

Skill original de Agente Smith (MIT). Método: **nunca computar sin identificar primero
jurisdicción, tipo de plazo y norma fuente — y verificar la norma en SAIJ antes de
afirmar el resultado.**

## Procedimiento obligatorio

1. **Jurisdicción y fuero.** ¿Nacional/federal, CABA o provincia (cuál)? ¿Judicial o
   administrativo? El código procesal aplicable cambia el cómputo completo. Si no está
   dicho, PREGUNTAR antes de computar.
2. **Tipo de plazo.** Identificar cuál de estos es, y su norma fuente:
   - **Días hábiles judiciales** (regla general procesal): no cuentan sábados, domingos,
     feriados ni días inhábiles declarados por el tribunal superior de la jurisdicción.
   - **Días hábiles administrativos** (procedimiento administrativo): régimen distinto
     del judicial (en el orden nacional, LNPA 19.549 y su reglamento).
   - **Días corridos** (derecho de fondo, CCCN art. 6; prescripción; muchos plazos de
     leyes especiales): cuentan todos los días; si vence en inhábil, verificar si la
     norma traslada el vencimiento.
   - **Horas / meses / años**: cómputo del CCCN art. 6 (los plazos de meses vencen el
     mismo número del mes correspondiente).
3. **Inicio del cómputo.** Regla procesal general: desde el día hábil siguiente a la
   **notificación válida**. Presupuesto crítico: si la notificación es nula o
   cuestionada, dejarlo asentado — el cómputo es condicional.
4. **Verificar la norma en SAIJ** (`saij_buscar_legislacion` + `saij_documento`) antes
   de afirmar cantidad de días o carácter del plazo. Citar artículo y texto.
5. **Computar con calendario real**: feriados nacionales + feriados/asuetos locales de
   la jurisdicción (verificar — los provinciales NO son los nacionales).
6. **Aplicar ferias y suspensiones** que correspondan:
   - Ferias judiciales (en el orden nacional, enero y feria de invierno según acordadas
     de la CSJN; cada provincia fija las suyas por acordada de su superior tribunal —
     verificar SIEMPRE la acordada local del año en curso).
   - Suspensiones por mediación prejudicial obligatoria u otras instancias previas
     según la jurisdicción y materia (verificar norma local).
7. **Plazo de gracia.** En el orden nacional, presentación en las dos primeras horas
   del día hábil siguiente al vencimiento (CPCCN art. 124). Las provincias tienen sus
   propias reglas (algunas dan más horas, otras difieren) — **verificar el código
   procesal local antes de contar con la gracia**.
8. **Salida.** Entregar tabla: acto · tipo de plazo · norma fuente (verificada, con
   uuid SAIJ) · inicio · vencimiento · gracia aplicable · riesgo.

## Reglas duras

- 🔴 **Plazo fatal**: marcarlo siempre y recomendar margen de seguridad (no presentar
  el último día si es evitable).
- **Prescripción ≠ caducidad**: la prescripción se suspende/interrumpe (CCCN arts.
  2539–2549); la caducidad en general no. Identificar cuál es antes de computar.
- Ejes de referencia de prescripción para orientar la búsqueda (SIEMPRE verificar el
  texto vigente en SAIJ): CCCN arts. 2560 (genérico 5 años), 2561 (especiales, daños),
  2562/2564 (2 años / 1 año, supuestos), LCT art. 256 (créditos laborales 2 años),
  materia tributaria y de faltas: regímenes propios por jurisdicción.
- **Nunca** afirmar un vencimiento sobre norma no verificada: marcar 🔲 verificación
  pendiente y decir qué falta confirmar (norma, feriado local, acordada de feria).
- Si dos cómputos son defendibles (p. ej. discusión sobre validez de la notificación),
  informar ambos escenarios: el propio y el peor escenario.
