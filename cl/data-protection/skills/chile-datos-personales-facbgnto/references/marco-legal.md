# Marco legal chileno — anclas verificadas

> **Verificado el 21 de agosto de 2026.** Todo lo de abajo tiene fecha porque
> caduca. Antes de una auditoría jurídica definitiva, reverifica (protocolo al final).

## Qué ley rige

La **Ley 19.628 sobre protección de la vida privada** sigue siendo la ley base.
La **Ley 21.719** no la reemplaza: la reescribe casi por completo, crea la Agencia
de Protección de Datos Personales y sustituye el régimen sancionatorio.

Al hablar con el equipo, nombra la Ley 21.719 —así se conoce— pero recuerda que
formalmente el articulado vive en la Ley 19.628 modificada.

## Estado y fechas

| Hecho | Fecha | Fuente | Solidez |
|---|---|---|---|
| Publicación en el Diario Oficial | 13-12-2024 | LeyChile / Diario Oficial | confirmado |
| Entrada en vigencia (24 meses después) | **01-12-2026** | LeyChile / Diario Oficial | confirmado |
| Consejo directivo de la Agencia sin designar | agosto 2026 | prensa especializada | **indicio, no confirmado** |
| Proyecto de postergación en evaluación, no aprobado | al 11-08-2026 | prensa especializada | **indicio, no confirmado** |

Las dos últimas filas provienen de prensa: sirven para saber que **algo se está
moviendo**, no para afirmar el estado institucional. Confírmalas antes de ponerlas
en un documento que salga del equipo. Están fechadas al 11-08-2026, diez días antes
que el resto de este archivo: es el dato más volátil del documento.

Consecuencia práctica al día de hoy: **la ley aún no está vigente**, pero el plazo
corre y los sistemas que se estén construyendo ahora estarán bajo su alcance.
Diseñar hoy sin considerarla implica migrar esquemas después.

El Senado rechazó la terna de consejeros en mayo de 2026 y el plazo legal de
designación venció en junio de 2026; esa demora institucional es lo que originó la
discusión sobre postergar la vigencia. Mientras no se apruebe una ley que la
modifique, **rige el 1 de diciembre de 2026**.

## Definiciones que cambian el diseño

### Dato sensible

La definición chilena incluye categorías que un equipo acostumbrado al GDPR no
espera. Comprende, entre otros, los datos que revelan:

- origen étnico o racial;
- afiliación política, sindical o gremial;
- **situación socioeconómica**;
- convicciones ideológicas o filosóficas y creencias religiosas;
- datos relativos a la salud;
- datos biométricos y perfil biológico humano;
- vida sexual, orientación sexual e identidad de género.

> **La situación socioeconómica es la trampa.** En Chile, renta, tramo de ingreso,
> deuda, morosidad, scoring, previsión, plan de salud, beca o subsidio son datos
> sensibles. Un CRM, un módulo de cobranza o un motor de scoring que en Europa
> sería tratamiento ordinario aquí exige protección reforzada.

El tratamiento de datos sensibles requiere consentimiento **expreso**, salvo
excepciones acotadas (datos hechos públicos por el titular, salvaguarda de la vida,
defensa de derechos, disposición legal, ciertos tratamientos de organizaciones sin
fines de lucro respecto de sus miembros).

### Datos económicos, financieros, bancarios y comerciales

Tienen un tratamiento propio, con su propia lógica de finalidad y comunicación a
terceros. Si el sistema toca morosidad, historial crediticio o comportamiento de
pago, no lo trates como dato personal común: marca `REVISIÓN LEGAL REQUERIDA` y
verifica también la Ley 20.575.

### Datos de niños, niñas y adolescentes

Régimen propio en el **art. 16 quáter**, con reglas **diferenciadas por tramo de
edad**: el tratamiento de datos de niños y niñas requiere autorización del padre,
madre o representante legal, mientras que para adolescentes existen reglas
distintas, con tratamiento reforzado de los datos sensibles.

> **El corte etario exacto y su alcance por tipo de dato son una cuestión
> normativa: verifícalo en el art. 16 quáter del texto vigente antes de
> implementarlo.** No lo deduzcas de este archivo ni de analogías con el GDPR.

Consecuencia de ingeniería, independiente del corte exacto: hay que poder calcular
la edad del titular **al momento de cada tratamiento y de cada incidente**, lo que
obliga a almacenar fecha de nacimiento y a modelar la representación legal. Ver
`bases-y-consentimiento.md`.

El deber de notificar vulneraciones alcanza a los datos de **niños, niñas y
adolescentes** como categoría; no lo restrinjas a un tramo de edad.

## Bases de licitud

El tratamiento requiere una base de licitud identificable. El consentimiento es
**una** de ellas, no la regla general. Las restantes incluyen, entre otras:
ejecución o celebración de un contrato, cumplimiento de una obligación legal,
satisfacción de intereses legítimos del responsable, defensa de derechos ante
tribunales o autoridades, protección de la vida o salud, y el cumplimiento de una
misión o función de interés público por parte de organismos públicos.

Verifica el catálogo exacto y su redacción en el articulado vigente antes de
copiarlo a un enum de código. Dos casos merecen atención especial:

- **Sector público.** Si el sistema pertenece a un organismo del Estado, la base
  suele ser el ejercicio de su función legal, no el consentimiento. Forzar
  consentimiento ahí es un error de diseño: el titular no puede negarse sin perder
  el servicio público.
- **Datos económicos, financieros, bancarios y comerciales.** Tienen régimen propio
  (ver arriba). No los encajes a la fuerza en interés legítimo.

Rige el principio de **responsabilidad demostrada**: el responsable debe poder
acreditar la licitud. Traducción a ingeniería: la base de licitud tiene que estar
registrada en algún lado consultable, no vivir en la cabeza de quien escribió la
migración.

## Derechos del titular

Acceso, rectificación, supresión, oposición, **bloqueo** y **portabilidad**. Son
personales, intransferibles e irrenunciables, y se ejercen ante el responsable.

> **Plazo de respuesta: `REVISIÓN LEGAL REQUERIDA`.** Existe un plazo legal, pero no
> lo afirmes de memoria ni lo tomes de un blog: cítalo del articulado o pídelo a
> legal. Lo que sí puedes afirmar como ingeniería es que el plazo es **corto en
> relación con el trabajo manual que implica**, y que un proceso que exige a un
> ingeniero escribir consultas a mano no lo va a cumplir.

Bloqueo y portabilidad son los dos que suelen no tener soporte en el esquema.
Ver `derechos-y-ciclo-de-vida.md`.

## Vulneraciones de seguridad

Existe deber de reportar las vulneraciones a las medidas de seguridad **por los
medios más expeditos posibles y sin dilaciones indebidas** cuando exista riesgo
para los derechos y libertades de los titulares.

La notificación **a los titulares** es exigible especialmente cuando la brecha
afecta datos sensibles, datos de niños, niñas y adolescentes, o datos de
obligaciones económicas, financieras, bancarias o comerciales.

Requisito de ingeniería que se deriva de esto: para notificar hay que poder
responder *qué datos, de cuántas personas, en qué ventana de tiempo*. Un sistema
sin auditoría de acceso no puede contestarlo, y esa incapacidad es en sí misma un
hallazgo.

## Transferencias internacionales

Son lícitas, entre otras vías, cuando el país de destino ofrece un nivel adecuado
de protección, cuando median cláusulas contractuales con garantías suficientes, o
mediante modelos de certificación o normas vinculantes equivalentes.

Casi toda arquitectura cloud chilena transfiere datos fuera de Chile. Eso no está
prohibido, pero **debe estar identificado**: región del proveedor, qué datos salen,
bajo qué mecanismo. Ver `terceros-y-ia.md`.

## Sanciones

Régimen administrativo aplicado por la Agencia, con Registro Nacional de Sanciones.

| Gravedad | Multa base | Tope alternativo para grandes empresas |
|---|---|---|
| Leves | hasta 5.000 UTM | — (además: amonestación escrita) |
| Graves | hasta 10.000 UTM | hasta **2% de los ingresos anuales por ventas** |
| Gravísimas | hasta 20.000 UTM | hasta **4% de los ingresos anuales por ventas** |

Agravantes que cambian el orden de magnitud:

- **Reincidencia** (nueva infracción dentro de un plazo acotado): la multa puede
  triplicarse.
- **Incumplimiento de las medidas ordenadas** dentro del plazo fijado: recargo
  sobre el monto.
- Sanciones accesorias: suspensión de operaciones de tratamiento e inscripción en
  un registro público de sanciones.

> **El tope porcentual es el que importa dimensionar.** Para una empresa grande,
> el 4% de las ventas anuales puede superar ampliamente las 20.000 UTM: quedarse
> con la columna de UTM subestima el riesgo justamente donde es mayor.

La graduación considera la gravedad, el daño, el beneficio económico obtenido, si
hubo datos sensibles o de NNA, y sanciones anteriores.

> Trata estas cifras como **orden de magnitud para dimensionar riesgo**, no como
> cita legal. Verifica contra el texto oficial antes de ponerlas en un documento
> que salga del equipo.

### Ventana de gracia para empresas de menor tamaño

> **Agregado por revisión externa el 22-08-2026, sin verificación directa
> contra el texto oficial en esta sesión — trátalo como `indicio, no
> confirmado` hasta pasar por el protocolo de reverificación de abajo.**
> Se documenta igual porque, de confirmarse, es de los datos más
> consultados al dimensionar riesgo para un cliente chileno — omitirlo
> por no haberlo verificado todavía sería peor que marcarlo como
> pendiente.

Según lo reportado: el artículo sexto transitorio de la Ley 21.719
establece que, durante los primeros 12 meses desde la entrada en vigencia
(es decir, aproximadamente hasta diciembre de 2027 si la vigencia se
mantiene en el 1 de diciembre de 2026 — ver "Estado y fechas" arriba), las
empresas de menor tamaño según la Ley 20.416 (microempresas, pequeñas y
medianas empresas) podrían recibir **amonestación escrita en lugar de
multa** ante una infracción, en vez del régimen sancionatorio de la tabla
de arriba.

Antes de usar esto para dimensionar riesgo con un cliente concreto:

1. Confirma el texto exacto del artículo sexto transitorio contra
   LeyChile/BCN — qué infracciones cubre (¿todas, o solo leves/graves?),
   si es automático o requiere que la empresa lo invoque, y si hay
   excepciones (p. ej. tratamiento de datos sensibles a escala, o
   reincidencia).
2. Confirma cómo se determina "empresa de menor tamaño" bajo la Ley
   20.416 (tramos por ventas anuales en UF) para el cliente concreto —
   no asumas que "es una empresa chica" basta sin calcularlo.
3. Actualiza esta sección con el resultado y quita la nota de "indicio,
   no confirmado" solo después de esa verificación — no antes.

## Modelo de prevención de infracciones y delegado de datos

La ley contempla un **modelo de prevención de infracciones** (art. 49), cuya
adopción y certificación se considera al momento de sancionar —trátalo como
**atenuante**; no afirmes que exime de responsabilidad sin cita del articulado.

Un **proyecto de reglamento** (Decreto N° 662/2025, Ministerio de Hacienda,
ingresado a toma de razón en agosto de 2025) detallaría su contenido mínimo:
identificación del responsable, designación de delegado de protección de datos,
registro de actividades de tratamiento, matriz de riesgos, protocolos internos,
canal de reportes, sanciones disciplinarias y capacitación. Bajo ese texto, la
designación del delegado sería obligatoria al adoptar y certificar un modelo de
prevención, podría ser interna o externa, y un grupo empresarial podría compartir
uno si mantiene políticas comunes.

> Redactado en condicional a propósito: al 21-08-2026 el decreto constaba **en
> trámite, no publicado**, y un decreto ingresado en agosto de 2025 que sigue sin
> publicarse un año después es un dato que muy probablemente cambió. **Verifica su
> estado antes de citarlo**, y no lo presentes como vigente.

Relevancia para ingeniería: varios de esos elementos —registro de actividades,
matriz de riesgos, protocolos— se alimentan de artefactos que el equipo de
desarrollo produce. Por eso este skill exige mantener `docs/privacidad/inventario.md`.
La preparación técnica de estos elementos —delegado, matriz de riesgos, canal
de reportes, capacitación— tiene su propia referencia en
`shared/arquitectura/programa-cumplimiento.md` del skill `implementar-ley-21719`.

## Protocolo de reverificación

Ejecútalo antes de emitir una auditoría jurídica definitiva, o si la fecha de
verificación del encabezado tiene más de tres meses. **Si no puedes determinar la
fecha actual con certeza, asume que está desactualizado** y dilo en la respuesta.

1. Confirma la vigencia y el texto actualizado en **LeyChile / Biblioteca del
   Congreso Nacional** (`bcn.cl/leychile`). Si el visor no carga, usa el PDF de la
   norma; no reemplaces la fuente oficial por un blog.
2. Revisa si se aprobó alguna **ley modificatoria o de postergación**.
3. Revisa reglamentos publicados en el **Diario Oficial**, en especial el que
   regula modelos de prevención de infracciones.
4. Revisa instrucciones, guías y criterios de la **Agencia de Protección de Datos
   Personales**, una vez constituida.
4.5. Confirma el **artículo sexto transitorio** (ventana de gracia para
   empresas de menor tamaño, Ley 20.416) contra el texto oficial — ver
   "Ventana de gracia para empresas de menor tamaño" arriba, todavía sin
   verificar al momento de escribir este punto.
5. **Reporta las diferencias en la conversación**, indicando qué línea de este
   archivo quedó obsoleta y cuál es el dato correcto con su fuente. No reescribas
   este archivo: es una referencia del skill, y automodificarla propaga en
   silencio datos que nadie revisó. Si el usuario quiere que quede corregido, que
   actualice el skill explícitamente.

Jerarquía de fuentes: texto oficial de la norma → reglamento publicado →
instrucciones de la Agencia → guías de organismos públicos (p. ej. Secretaría de
Gobierno Digital) → doctrina especializada. Un blog corporativo o un artículo de
prensa sirve para detectar que **algo cambió**, nunca para afirmar **qué dice** la ley.

## Fuentes consultadas (21-08-2026)

- Secretaría de Gobierno Digital — Guía práctica de implementación de la nueva ley
  de datos personales en la Administración:
  https://wikiguias.digital.gob.cl/datos-personales/guia-practica-implementacion-nueva-ley-datos-personales
- DOE Actualidad Jurídica — Ley N° 21.719, conoce más sobre la nueva ley de datos
  personales: https://actualidadjuridica.doe.cl/ley-n-21-719-conoce-mas-sobre-la-nueva-ley-de-datos-personales/
- DOE Actualidad Jurídica — Gobierno evalúa postergar la entrada en vigencia
  (04-08-2026): https://actualidadjuridica.doe.cl/gobierno-evalua-postergar-entrada-en-vigencia-de-la-ley-de-proteccion-de-datos-personales/
- ESG Hoy — Piden acotar a 6 meses la postergación (11-08-2026):
  https://www.esghoy.cl/agpd-postergacion-ley-21719-proteccion-datos-personales/
- Diario Constitucional — Nuevo reglamento sobre modelos de prevención de
  infracciones: https://www.diarioconstitucional.cl/estudios-juridicos/nuevo-reglamento-que-regula-modelos-de-prevencion-de-infracciones-en-proteccion-de-datos-personales-por-diego-cordova-y/
- IAPP — El nuevo entorno regulatorio de la protección de datos personales en Chile:
  https://iapp.org/news/a/el-nuevo-entorno-regulatorio-de-la-proteccion-de-datos-personales-en-chile
