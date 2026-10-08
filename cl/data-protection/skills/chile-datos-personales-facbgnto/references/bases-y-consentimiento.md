# Bases de licitud, consentimiento y NNA

El consentimiento es **una** base de licitud, no la base por defecto. Forzar
consentimiento donde corresponde otra base es tan mal diseño como tratar datos
sin ninguna base: en el primer caso, el titular no puede negarse de verdad
(sector público, contrato); en el segundo, no hay nada que lo ampare.

Rige el principio de **responsabilidad demostrada**: la base tiene que quedar
registrada en algo consultable, no en la memoria de quien escribió la
migración. Ver `marco-legal.md` para el estado de vigencia y las fechas.

## Catálogo de bases de licitud

Verifica el catálogo exacto y su redacción en el articulado vigente antes de
copiarlo a un enum de código — esto es la traducción de ingeniería, no la cita
legal:

| Base | Cuándo aplica | Ejemplo típico |
|---|---|---|
| Consentimiento | El titular decide libremente, para una finalidad específica | Newsletter, geolocalización opcional, marketing |
| Ejecución o celebración de un contrato | El tratamiento es necesario para el contrato mismo | Datos de envío en un e-commerce, nómina para pagar sueldos |
| Cumplimiento de una obligación legal | Una norma distinta obliga al tratamiento | Retención tributaria, reporte a la UAF, libro de remuneraciones |
| Interés legítimo del responsable | Interés real, no forzado, que no se puede lograr de otra forma menos invasiva | Prevención de fraude, seguridad de la plataforma |
| Defensa de derechos ante tribunales o autoridades | Litigio o procedimiento administrativo en curso | Evidencia para una demanda |
| Protección de la vida o salud del titular | Urgencia | Ficha clínica de emergencia sin poder pedir consentimiento |
| Misión o función de interés público | Solo organismos del Estado, en ejercicio de su función legal | Un municipio procesando un beneficio social |

### Los dos casos que se fuerzan mal

- **Sector público.** Si el sistema pertenece a un organismo del Estado, la
  base suele ser el ejercicio de su función legal, no el consentimiento. Un
  formulario que pide "acepto tratar mis datos" para acceder a un trámite
  obligatorio es un antipatrón: el titular no puede negarse sin perder el
  servicio, y ese consentimiento no es libre. Documenta la función legal en su
  lugar.
- **Datos económicos, financieros, bancarios y comerciales.** Tienen régimen
  propio (ver `marco-legal.md` y `clasificacion-datos.md`). No los encajes a
  la fuerza en interés legítimo solo porque es la base más flexible del
  catálogo.

## Consentimiento — cuándo es válido

El consentimiento tiene que ser **libre, informado, específico e inequívoco**.
Cada palabra elimina un patrón de implementación habitual:

```
libre         Sin consecuencia negativa real por negarse. Si negarse bloquea
              un servicio que no depende de ese dato, no es libre.

informado     El titular supo, al momento de dar el consentimiento, qué dato,
              para qué, y por cuánto tiempo. Un enlace genérico a "Política de
              Privacidad" en el footer no informa sobre una finalidad
              específica.

específico    Por finalidad. Un booleano único ("acepto tratamiento de mis
              datos") que habilita marketing, analítica y cesión a terceros
              a la vez no es específico.

inequívoco    Requiere una acción afirmativa. Casillas premarcadas, opt-out
              en vez de opt-in, o "seguir navegando implica aceptar" no
              cumplen.
```

### Consentimiento expreso (datos sensibles)

El tratamiento de datos sensibles requiere consentimiento **expreso**, salvo
excepciones acotadas: datos hechos públicos por el propio titular, salvaguarda
de la vida, defensa de derechos, disposición legal, y ciertos tratamientos de
organizaciones sin fines de lucro respecto de sus propios miembros. Verifica el
listado exacto de excepciones en el articulado antes de invocar una: son
acotadas a propósito, no una salida general.

"Expreso" en ingeniería significa: una acción específica para ese dato
sensible, distinguible de la aceptación general de términos. No basta con que
el consentimiento general mencione, entre otras cosas, que se tratan datos de
salud.

### Modelo de datos mínimo

Un booleano `acepto_terminos = true` no es un registro de consentimiento. El
mínimo defendible:

```
titular_id
finalidad            una fila por finalidad, no una fila que cubre todas
version_texto        qué texto exacto aceptó — el texto cambia con el tiempo
canal                web, app, presencial, telefónico
fecha_otorgamiento
fecha_revocacion     null mientras esté vigente
ip, user_agent       si el canal es digital
```

Sin `finalidad` por fila, no puedes responder "¿para qué consintió esta
persona?" — y esa pregunta es exactamente la que hace un fiscalizador o un
titular ejerciendo el derecho de acceso.

### Revocación

Tiene que **detener el tratamiento**, no solo registrarse. Un `revoked_at` que
nadie consulta antes de encolar el correo de marketing simula cumplimiento sin
darlo: es peor que no tener el campo, porque el equipo cree que está cubierto.

Verifica el camino completo: revocar → el job que envía campañas filtra por
consentimiento vigente → deja de incluir a ese titular en la próxima corrida.
Si ese último salto no existe, el hallazgo es sobre el job, no sobre el
formulario de revocación.

### Reutilización de finalidad

Un dato recolectado para una finalidad y usado luego para otra sin nueva base
es un hallazgo, aunque la base original fuera válida. Pregunta de auditoría:
¿dónde más se usa este campo, además del propósito con el que se pidió? Un
email de confirmación de compra apareciendo en un export a una plataforma de
email marketing es el ejemplo más común.

## Niños, niñas y adolescentes (art. 16 quáter)

Régimen propio, con reglas **diferenciadas por tramo de edad**: niños y niñas
requieren autorización del padre, madre o representante legal; los
adolescentes tienen reglas distintas, con tratamiento reforzado si además hay
datos sensibles de por medio.

> **El corte etario exacto y su alcance por tipo de dato son cuestión
> normativa.** Verifícalo en el art. 16 quáter del texto vigente antes de
> implementarlo — no lo deduzcas de este archivo ni de analogías con el GDPR
> (cuyo corte de 13–16 años no es automáticamente aplicable aquí).

### Consecuencias de diseño, independientes del corte exacto

1. **Calcula la edad, no la infieras.** Almacena fecha de nacimiento; un flag
   `es_menor` fijado una vez queda obsoleto el día del cumpleaños. La edad hay
   que poder recalcularla al momento de cada tratamiento y de cada incidente.

2. **Modela la representación legal como relación, no como casilla.**

   ```
   titular_id
   representante_id
   tipo_representacion    padre | madre | tutor_legal
   acreditacion           cómo se verificó — no un checkbox declarativo
   vigente_desde, vigente_hasta
   ```

   Una casilla "confirmo que soy el padre/madre" sin ningún método de
   verificación es un hallazgo ALTO en cualquier auditoría: no acredita nada,
   solo registra una afirmación.

3. **Autorización por finalidad, no una autorización general.** Foto,
   ubicación, datos de salud y comunicaciones pueden requerir autorizaciones
   separadas del representante legal, no una sola casilla que cubre todo.

4. **Transición al cumplir la mayoría de edad.** Define qué pasa con el
   consentimiento otorgado por el representante cuando el titular deja de ser
   menor: ¿se solicita ratificación directa al titular, o se asume vigente?
   `REVISIÓN LEGAL REQUERIDA` si el proyecto no lo tiene resuelto.

5. **El deber de notificar vulneraciones alcanza a los datos de NNA como
   categoría completa**, no restringido a un tramo de edad específico.

## Registro consultable de bases de licitud

El principio de responsabilidad demostrada exige que la base esté en un lugar
consultable. Formato mínimo por tratamiento (alimenta
`docs/privacidad/inventario.md`, formato completo en `plantillas.md`):

```
tratamiento          p. ej. "envío de boletas electrónicas"
datos_involucrados    RUT, nombre, dirección
base_licitud          ejecución de contrato
evidencia             cláusula del contrato de servicio, sección 4
revisado              fecha
```

Sin esto, la pregunta "¿por qué pueden tratar mi RUT?" no tiene respuesta
verificable — y esa es, en la práctica, la primera pregunta que hace un
fiscalizador o un titular que ejerce el derecho de acceso.
