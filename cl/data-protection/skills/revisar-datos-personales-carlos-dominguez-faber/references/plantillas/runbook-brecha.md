# Runbook: se filtraron datos

Esto se escribe **antes** de que pase. El día que pasa nadie está en condiciones
de improvisar un procedimiento.

**Quién decide:** _(nombre y suplente)_
**Quién habla con la autoridad:**
**Quién habla con los afectados:**
**Contactos fuera de horario:**

---

## Hora 0 — Contener y anotar

Antes que nada, **empieza una bitácora con hora de cada paso**. Esa bitácora es
después tu prueba de que actuaste sin dilaciones indebidas.

1. Cortar el acceso: rotar credenciales, revocar tokens, cerrar el vector.
2. **No borres evidencia.** Preserva logs antes de limpiar. El impulso de "dejar
   todo limpio" destruye lo que necesitas para responder qué pasó.
3. Congelar despliegues.
4. Anotar hora exacta en que la organización tomó conocimiento. Ese es el reloj
   que corre.

## Hora 1 a 3 — Entender el alcance

Responder por escrito, aunque sea con incertidumbre:

- ¿Qué ocurrió: destrucción, filtración, pérdida, alteración o acceso no
  autorizado?
- ¿Qué categorías de datos? ¿Hay **sensibles**? ¿De **menores de 14**? ¿Datos
  **económicos, financieros, bancarios o comerciales**?
- ¿Cuántos titulares, aproximadamente?
- ¿Sigue abierto el vector?
- ¿Hay riesgo razonable para los derechos y libertades de esas personas?

Si la respuesta a la última es sí, o hay duda razonable, se reporta.

## El reporte a la Agencia

La ley pide reportar **por los medios más expeditos posibles y sin dilaciones
indebidas**. No fija un plazo en horas.

> El estándar europeo comparable habla de 72 horas, y es la referencia que
> probablemente se use para interpretar qué es "sin dilaciones indebidas". Ante
> la duda, actúa como si ese fuera el plazo.

No esperes a tener el cuadro completo: reporta lo que sabes y complementa
después.

**Contenido del reporte y del registro interno:**

- Naturaleza de la vulneración.
- Sus efectos.
- Categorías de datos afectados.
- Número aproximado de titulares.
- Medidas adoptadas para gestionarla y para prevenir que se repita.

## Avisar a las personas afectadas

**Obligatorio** cuando la vulneración afecte datos sensibles, datos de menores de
catorce años, o datos económicos, financieros, bancarios o comerciales.

En lenguaje claro y sencillo, señalando:

- Qué datos suyos se vieron afectados, concretamente.
- Qué consecuencias puede tener para esa persona.
- Qué medidas se tomaron.
- Qué puede hacer ella —cambiar contraseña, vigilar movimientos, etc.

Se notifica a cada titular. Si eso no es posible, se publica un aviso en un medio
de comunicación masivo de alcance nacional.

## Después

- [ ] Registrar la vulneración en el registro interno (es obligatorio, exista o no
      el reporte).
- [ ] Análisis de causa raíz, sin buscar culpables.
- [ ] Cerrar el hueco y verificar que quedó cerrado.
- [ ] Revisar si otros sistemas tienen el mismo hueco.
- [ ] Actualizar este runbook con lo que se aprendió.

---

## Lo que no hay que hacer

- **No minimizar por escrito.** "Fue un incidente menor" en un chat interno es un
  documento en tu contra si después resulta que no lo era.
- **No avisar tarde a propósito.** Omitir deliberadamente la comunicación de una
  vulneración es infracción **gravísima**: hasta 20.000 UTM.
- **No prometer lo que no sabes.** "Ningún dato fue comprometido" antes de
  haberlo verificado es la frase que más caro sale.

---

*Plantilla de apoyo, no un documento legal. Que un abogado la revise antes de
que la necesites.*
