# México: requisitos para los textos legales

Checklist para sitios cuyo responsable reside en México. Fuente principal: la **Ley Federal de
Protección de Datos Personales en Posesión de los Particulares** (LFPDPPP), publicada en el DOF
el 20 de marzo de 2025 y vigente desde el día siguiente. Texto vigente:
[Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf).

> Antes de usar esta referencia, abre el texto vigente y confirma que los artículos citados no
> han cambiado. Si encuentras una reforma, actualiza este archivo en el mismo cambio y repórtalo.

## Autoridad

- La **Secretaría Anticorrupción y Buen Gobierno** vigila la ley para el sector privado
  (artículo 2, fracción XV). Reemplazó al INAI, que se extinguió por la reforma de simplificación
  orgánica.
- No escribas "INAI" en textos nuevos; ante él se presentaba la solicitud de protección de
  derechos, que ahora va a la Secretaría (artículo 40).

## Aviso de privacidad integral (artículo 15)

Debe contener **al menos**:

1. Identidad y domicilio del responsable.
2. Datos personales que se tratarán, **identificando los sensibles**.
3. Finalidades, **distinguiendo las que requieren consentimiento** (por ejemplo, marketing) de
   las necesarias para la relación con la persona.
4. Opciones y medios para **limitar el uso o divulgación** de los datos.
5. Mecanismos, medios y procedimientos para ejercer los **derechos ARCO**.
6. Procedimiento y medio para comunicar **cambios al aviso**.

Buenas prácticas que la skill también incluye (no son fracciones del artículo 15, pero las piden
otros artículos):

- Cómo **revocar el consentimiento** (el artículo 7 exige que el aviso lo establezca).
- Persona o departamento de datos personales que atiende las solicitudes (artículo 29).
- Transferencias a terceros y su finalidad, si las hay (artículos 35 y 36).
- Fecha de última actualización.

## Aviso simplificado (artículo 16, fracción II)

Si los datos se recaban por medios electrónicos (formularios del sitio), se entrega en modalidad
simplificada con **al menos las fracciones I a IV del artículo 15** y el sitio donde consultar el
aviso integral. En el template va en `legal.formNotice` de `src/content/site/<idioma>.yaml` y se
muestra bajo cada formulario con el enlace al aviso integral.

Ejemplo de estructura (adaptar con datos reales):

> **[Responsable]**, con domicilio en **[domicilio]**, usará tu nombre, correo y mensaje para
> responder tu solicitud y, si lo autorizas, enviarte información comercial. Puedes negarte a
> esto último escribiendo a **[correo]**.

## Consentimiento (artículos 7, 8 y 9)

- Por regla general basta el **consentimiento tácito**: la persona conoce el aviso y no se opone.
- **Expreso** para datos financieros o patrimoniales.
- **Expreso y por escrito** (firma autógrafa, electrónica u otro mecanismo de autenticación)
  para **datos sensibles** (salud, origen étnico, creencias, preferencia sexual, etc.). Si un
  formulario pide datos sensibles, adviértelo como bloqueante: un formulario web simple no
  basta.
- El consentimiento se puede revocar en cualquier momento.
- Excepciones al consentimiento: artículo 9 (por ejemplo, cumplir una relación jurídica con la
  persona).

## Derechos ARCO (artículos 21 a 34)

- Acceso, rectificación, cancelación y oposición.
- La solicitud debe incluir lo del artículo 28: nombre y medio para notificaciones, documento de
  identidad, descripción de los datos y del derecho que se ejerce.
- Plazos (artículo 31): respuesta en máximo **20 días** desde que se recibe la solicitud; si
  procede, se hace efectiva en los **15 días** siguientes. Ambos plazos se pueden ampliar una
  sola vez por un periodo igual si se justifica.
- Es gratuito; solo se cobran costos de reproducción o envío (artículo 34).

## Conservación (artículo 10)

Los datos se suprimen cuando dejan de ser necesarios para las finalidades del aviso. Pide a la
persona su plazo real de conservación; no lo inventes.

## Cookies y tecnologías de rastreo

La ley de 2025 no las menciona de forma expresa. El Reglamento de la ley anterior (2011) y los
Lineamientos del Aviso de Privacidad (DOF, 2013) pedían informar en el aviso el uso de cookies,
web beacons y tecnologías similares, qué datos obtienen, para qué y cómo deshabilitarlas.

- **Verifica** si ya se publicó un Reglamento armonizado con la ley de 2025 (el transitorio
  Décimo Segundo da 90 días para adecuar reglamentos) y qué dice sobre rastreo.
- Mientras tanto, la práctica conservadora es: informar las cookies en el aviso y en una política
  de cookies, tratar la **publicidad** como finalidad que requiere consentimiento y ofrecer cómo
  rechazarla. En el template eso es `consent.mode: "opt-out"` como mínimo; usa `"opt-in"` si el
  sitio también se dirige a personas en la UE.

## Comercio electrónico y términos

Si el sitio vende productos o servicios en línea, revisa la **Ley Federal de Protección al
Consumidor**, en particular el capítulo de comercio electrónico (artículo 76 bis): identificación
del proveedor, información clara sobre precios, condiciones de compra, devoluciones y
cancelaciones, y medios de contacto. Texto vigente:
[Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPC.pdf).

## Lo que la skill no hace

- No define si el cliente debe registrarse ante alguna autoridad ni redacta contratos.
