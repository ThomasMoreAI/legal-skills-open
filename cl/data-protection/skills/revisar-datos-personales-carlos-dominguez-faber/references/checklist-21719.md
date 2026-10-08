# Los diez puntos

Cada punto trae qué buscar, qué delata el problema y el artículo que lo respalda.
Los artículos son de la Ley 19.628 en su texto modificado por la Ley 21.719,
vigente desde el 1 de diciembre de 2026.

---

## 1 · Inventario de datos personales

**Qué buscar:** todo campo que identifique o haga identificable a una persona
natural, en esquemas, formularios, tipos y payloads.

**Delata el problema:**
- Campos de texto libre (`notas`, `observaciones`, `comentarios`) sin restricción,
  donde termina cayendo información de salud o económica.
- Objetos JSON sin tipar que se guardan enteros (`metadata`, `extra`, `payload`).
- Tablas de importación o staging que nadie limpia.

**Salida esperada:** la tabla del paso 1 de la skill, completa.

> Art. 2 (definiciones) y art. 3 (principios).

---

## 2 · Minimización y proporcionalidad

**Qué buscar:** campos que el sistema pide pero no usa. Búscalos por su nombre en
todo el código: si un campo solo aparece en el `INSERT` y en el formulario, y
nunca se lee, no tiene finalidad.

**Delata el problema:**
- Fecha de nacimiento completa cuando bastaría un booleano de mayoría de edad.
- Dirección exacta o coordenadas para un servicio que no va a domicilio.
- RUT o documento de identidad cuando no hay obligación legal de identificar.
- Datos de terceros que nunca dieron su consentimiento (el "contacto de
  emergencia", los contactos del teléfono).
- Ingresos, ocupación o estado civil en servicios que no evalúan crédito.

**El arreglo:** por cada campo sin finalidad, dos opciones — se elimina, o se
documenta su finalidad. No hay tercera.

> Art. 3 c) proporcionalidad · art. 14 quáter protección por defecto.

---

## 3 · Consentimiento con evidencia

**Qué buscar:** cómo se captura, se guarda y se retira el consentimiento.

**Delata el problema:**
- Una sola columna booleana (`accepted_terms`, `acepto_todo`) para todas las
  finalidades juntas.
- Checkbox premarcado (`checked` por defecto).
- No se guarda **cuándo** se aceptó ni **qué versión** del texto.
- No existe forma de retirarlo, o retirarlo es mucho más difícil que darlo.
- Se asume el consentimiento por el solo uso del servicio.

**El arreglo:** una tabla de consentimientos con una fila por finalidad —
`titular_id`, `finalidad`, `version_texto`, `otorgado_en`, `revocado_en`, `canal`.
El consentimiento debe ser libre, informado, específico, previo e inequívoco.

> Art. 12 regla general · art. 14 ter k) derecho a retirarlo.

---

## 4 · Los derechos, como endpoints reales

**Qué buscar:** que existan los seis caminos, no solo un correo de contacto.

| Derecho | Qué debe existir |
|---|---|
| Acceso | Ver qué datos hay, su origen, finalidad y destinatarios |
| Rectificación | Corregir datos inexactos o desactualizados |
| Supresión | Borrado real, no una bandera |
| Oposición | Especialmente a marketing directo y perfilamiento |
| Portabilidad | Export en formato estructurado, genérico y de uso común |
| Bloqueo | Suspender el tratamiento mientras se resuelve un reclamo |

**Delata el problema:** que la única vía sea "escríbenos a contacto@". Que el
export sea un PDF (no es un formato operable por otro sistema). Que no exista
ningún concepto de bloqueo.

> Arts. 5 a 9 · art. 8 ter bloqueo · art. 9 portabilidad.

---

## 5 · El borrado que borra de verdad

**Qué buscar:** todos los lugares donde el dato se replica. Esta es la
verificación del paso 3 de la skill.

**Los siete escondites habituales:**
1. Soft delete: `deleted_at`, `activo = 0`, `is_deleted`. La fila sigue completa.
2. Tablas de auditoría o historial con copia íntegra del registro.
3. Logs de aplicación con datos personales en texto plano.
4. Colas de trabajos y webhooks con el payload guardado.
5. Caché y sesiones.
6. Exports y respaldos.
7. Sistemas de terceros que ya recibieron el dato.

**Ojo:** el soft delete puede ser legítimo si hay una obligación legal de
conservación —tributaria, por ejemplo—. Lo que no es legítimo es decirle a la
persona que sus datos fueron eliminados cuando no lo fueron. Si conservas, dilo,
y conserva solo lo que la obligación exige.

**El arreglo:** un mapa de borrado documentado — todos los destinos del dato y
qué pasa con cada uno.

> Art. 8 supresión · art. 3 c) proporcionalidad.

---

## 6 · Plazos y trazabilidad de las solicitudes

**Qué buscar:** que exista un registro de solicitudes con reloj, no una bandeja
de correo.

**Los plazos de la ley:**
- Acusar recibo y pronunciarse: **30 días corridos**, prorrogables **una sola vez
  por 30 más**.
- Solicitud de **bloqueo temporal: 2 días hábiles**, y mientras no se resuelva no
  se pueden seguir tratando esos datos.

**Delata el problema:** no hay tabla de solicitudes, no hay estado, no hay fecha
de recepción, no hay forma de demostrar cuándo se respondió.

> Art. 11 procedimiento ante el responsable · art. 34 bis c) responder tarde es
> infracción leve.

---

## 7 · La política pública de tratamiento

**Qué buscar:** una página pública y permanente con los doce contenidos que exige
el artículo 14 ter, con **fecha y versión**.

**Los doce:** política adoptada con fecha y versión · identificación del
responsable y su representante legal · medio de contacto para solicitudes ·
categorías de datos, universo de titulares, destinatarios, finalidades y base de
legitimidad · política y medidas de seguridad · los derechos del titular · el
derecho a recurrir ante la Agencia · transferencias internacionales y si el país
destino tiene nivel adecuado · período de conservación · origen de los datos ·
derecho a retirar el consentimiento · existencia de decisiones automatizadas con
información significativa sobre la lógica aplicada.

**Delata el problema:** política genérica copiada de una plantilla, que describe
un sistema que no es el que está corriendo. Ese es el peor caso: promete cosas
que el código no hace.

> Art. 14 ter.

---

## 8 · Inventario de terceros

**Qué buscar:** cada servicio externo que toca datos personales — proveedores de
IA, analítica, correo, mensajería, CRM, hosting, monitoreo de errores.

**Por cada uno:** qué datos recibe · para qué · dónde está alojado · qué dice su
política sobre uso y compartición · qué contrato existe · qué pasa al terminar.

**Delata el problema:**
- Trazas de error que suben el objeto de usuario completo al servicio de
  monitoreo.
- Analítica que recibe correo o identificador en la URL.
- Proveedores cuya política permite usar tus datos para entrenar o compartirlos
  con terceros.
- Sub-encargados que el proveedor contrató sin tu autorización escrita.

**Lo que dice la ley:** el encargado que trata los datos para un objeto distinto
del convenido, o los cede sin autorización, **pasa a ser responsable** y responde
personalmente y **solidariamente** contigo. No puede subdelegar sin autorización
específica y por escrito. Al terminar el servicio, debe suprimir o devolver los
datos.

> Art. 15 bis.

---

## 9 · Transferencia internacional

**Qué buscar:** si el dato sale de Chile, con qué mecanismo se justifica.

Los mecanismos que admite la ley: país con **nivel adecuado** de protección
(lista que publicará la Agencia) · **cláusulas contractuales** o normas
corporativas vinculantes con garantías adecuadas · **modelo de cumplimiento o
certificación** · o alguno de los supuestos excepcionales para transferencias
específicas y no habituales, entre ellos el consentimiento expreso del titular
para esa transferencia determinada.

**Delata el problema:** nadie se lo ha planteado. Es lo normal: casi todo
proyecto manda datos a Estados Unidos sin haberlo pensado — el modelo de
lenguaje, el hosting, la base de datos gestionada, el proveedor de correo.

**Y el detalle que cambia todo:** acreditar ante la Agencia que la transferencia
se hizo conforme a la ley **le corresponde al responsable**, no al proveedor.

> Arts. 27 a 29.

---

## 10 · Decisiones automatizadas trazables

**Qué buscar:** cualquier punto donde el sistema decide algo sobre una persona —
scoring, calificación de leads, aprobación o rechazo, priorización, moderación,
detección de fraude, evaluación de desempeño.

**Delata el problema:**
- Se guarda el resultado pero no los factores que lo produjeron.
- No se registra la versión del modelo ni del prompt que decidió.
- No hay forma de pedir intervención humana.
- La persona nunca supo que la decisión fue automática.

**Lo que exige la ley:** el titular puede oponerse a decisiones automatizadas que
le produzcan efectos jurídicos o le afecten significativamente. Hay tres
excepciones —contrato, consentimiento expreso, ley— pero **incluso en esas tres**
hay que garantizarle explicación, intervención humana, derecho a expresar su
punto de vista y a pedir revisión de la decisión.

**El arreglo:** una tabla de decisiones con `titular_id`, `entrada`,
`version_modelo`, `salida`, `factores`, `decidido_en`, `revisado_por`,
`revisado_en`. Y un camino real para pedir la revisión.

> Art. 8 bis · art. 14 ter l) · art. 15 ter (evaluación de impacto previa si hay
> perfilamiento con efectos significativos).

---

## Lo que esta auditoría no cubre

Fuera de alcance, siempre a un abogado:

- La redacción legal de la política de privacidad y los términos.
- Qué base de licitud aplica a cada tratamiento concreto.
- Los contratos con proveedores y encargados.
- La evaluación de impacto formal del artículo 15 ter.
- Si conviene adoptar el modelo de prevención certificado y designar delegado.
- Cualquier obligación sectorial —salud, banca, educación— que se sume a esta.
