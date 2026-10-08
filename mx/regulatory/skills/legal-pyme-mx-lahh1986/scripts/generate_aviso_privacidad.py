#!/usr/bin/env python3
"""
legal-pyme-mx · generate_aviso_privacidad.py

Genera Aviso de Privacidad (corto, simplificado o integral) según
LFPDPPP (nueva ley DOF 20-03-2025) y guía oficial INAI.

Uso:
  generate_aviso_privacidad.py \
    --tipo=integral \
    --razon-social="Mi Empresa S.A. de C.V." \
    --rfc="MIE2401015A1" \
    --domicilio="Av. Reforma 100, Col. Centro, CDMX, CP 06000" \
    --email-arco="datos@miempresa.mx" \
    --giro=ecommerce \
    --salida=aviso.md

  generate_aviso_privacidad.py --json '{"tipo": "corto", "razon_social": "...", ...}'

Tipos:
  corto         para puntos de captura inmediatos (QR, formularios cortos, redes sociales)
  simplificado  para landing pages, sitio web, contratos breves
  integral      para sitio web sección dedicada, contratos, vínculos a políticas

Fuentes:
  - LFPDPPP 2025: research/diputados/leyes/LFPDPPP.pdf
  - Guía INAI:   research/inai/ManualAvisoPrivacidad.pdf
"""
import argparse
import json
import sys
from datetime import date
from pathlib import Path

FINALIDADES_POR_GIRO = {
    "ecommerce": {
        "primarias": [
            "Procesar tu compra, envío, devoluciones y garantía",
            "Generar tu factura electrónica (CFDI) según datos fiscales que proporciones",
            "Atender quejas, dudas y reclamaciones del producto/servicio",
            "Comunicarte cambios relevantes sobre tu pedido o cuenta",
            "Cumplir obligaciones fiscales, contables y legales aplicables",
        ],
        "secundarias": [
            "Enviarte ofertas, descuentos y novedades de nuestros productos",
            "Análisis estadístico de comportamiento de compra para mejorar el servicio",
            "Encuestas de satisfacción y retroalimentación",
        ],
        "datos_recabados": [
            "Nombre completo o razón social",
            "RFC y régimen fiscal (si solicita factura)",
            "Domicilio de envío y/o fiscal",
            "Teléfono y correo electrónico",
            "Datos de pago (procesados por pasarela; no almacenamos tarjeta completa)",
            "Historial de compras",
        ],
    },
    "servicios": {
        "primarias": [
            "Cumplir el contrato de prestación de servicios celebrado contigo",
            "Generar facturación electrónica con tus datos fiscales",
            "Mantener comunicación operativa del servicio",
            "Atender garantías, quejas, dudas y reclamaciones",
            "Cumplir obligaciones fiscales, contables y legales aplicables",
        ],
        "secundarias": [
            "Enviarte información de nuevos servicios o capacitaciones",
            "Encuestas de satisfacción y mejora continua",
        ],
        "datos_recabados": [
            "Nombre o razón social",
            "RFC y régimen fiscal",
            "Domicilio fiscal y/o de servicio",
            "Teléfono y correo electrónico",
            "Datos específicos del servicio contratado",
        ],
    },
    "salud": {
        "primarias": [
            "Brindar atención médica/odontológica/psicológica/nutricional según servicios contratados",
            "Mantener expediente clínico conforme NOM-004-SSA3",
            "Emitir recetas, indicaciones y referencias médicas",
            "Generar facturación electrónica",
            "Atender obligaciones legales sanitarias",
        ],
        "secundarias": [
            "Recordatorios de citas y seguimiento de tratamiento",
            "Información sobre nuevos tratamientos o servicios",
        ],
        "datos_recabados": [
            "Nombre completo, fecha de nacimiento, sexo",
            "RFC, CURP",
            "Datos de contacto",
            "Datos de salud (historial, alergias, tratamientos)",
            "Datos del seguro (si aplica)",
        ],
        "categoria_sensible": True,
    },
    "educacion": {
        "primarias": [
            "Inscripción y administración del programa educativo",
            "Mantener expediente académico",
            "Comunicación con padres/tutores (si menor de edad)",
            "Generar facturación de colegiatura y cuotas",
            "Cumplir obligaciones ante SEP y autoridades educativas",
        ],
        "secundarias": [
            "Comunicación de eventos, talleres y nuevos cursos",
            "Encuestas de calidad educativa",
        ],
        "datos_recabados": [
            "Nombre completo del alumno y padres/tutores",
            "Fecha de nacimiento, CURP",
            "Datos de contacto",
            "Historial académico previo",
            "Datos de salud relevantes (alergias, condiciones especiales)",
        ],
    },
    "generico": {
        "primarias": [
            "Cumplir con la relación comercial o de servicio contratada",
            "Generar facturación electrónica",
            "Atender solicitudes, quejas y reclamaciones",
            "Cumplir obligaciones fiscales, contables y legales aplicables",
        ],
        "secundarias": [
            "Comunicación de ofertas, descuentos y novedades",
            "Estudios estadísticos para mejorar nuestros servicios",
        ],
        "datos_recabados": [
            "Nombre o razón social",
            "RFC y régimen fiscal (cuando aplique)",
            "Domicilio",
            "Teléfono y correo electrónico",
        ],
    },
}


def render_corto(d):
    """8-10 líneas para puntos de captura inmediatos (formularios, QR, mostrador)."""
    url = d.get('url_integral') or '[URL de tu sitio web]'
    return f"""# Aviso de Privacidad CORTO

**{d['razon_social']}** ({d['rfc']}), con domicilio en {d['domicilio']}, es responsable del tratamiento de tus datos personales.

Tus datos serán utilizados para las siguientes finalidades primarias:
{chr(10).join(f'- {f}' for f in d['finalidades_primarias'])}

{'**Si NO deseas** que tus datos se usen para finalidades secundarias (marketing, encuestas, estudios), márcalo en el cuadro correspondiente o escríbenos a ' + d['email_arco'] + '.' if d.get('finalidades_secundarias') else ''}

Para ejercer tus derechos de Acceso, Rectificación, Cancelación y Oposición (ARCO), o para conocer el aviso de privacidad integral, contáctanos en {d['email_arco']}.

Aviso integral disponible en: {url}

_Fecha de actualización: {d['fecha']}_
"""


def render_simplificado(d):
    """½ a 1 página para landing page o contrato breve."""
    txt = f"""# Aviso de Privacidad SIMPLIFICADO

**Responsable del tratamiento de tus datos personales**

{d['razon_social']} ({d['rfc']}), con domicilio fiscal en {d['domicilio']}, en cumplimiento a lo establecido por la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP, publicada en el DOF el 20 de marzo de 2025), hace de tu conocimiento el siguiente Aviso de Privacidad Simplificado.

## Datos personales que recabamos

{chr(10).join(f'- {x}' for x in d['datos_recabados'])}

## Finalidades del tratamiento

**Primarias (necesarias para la relación contractual o servicio):**
{chr(10).join(f'- {x}' for x in d['finalidades_primarias'])}

"""
    if d.get('finalidades_secundarias'):
        txt += f"""**Secundarias (NO necesarias; puedes oponerte):**
{chr(10).join(f'- {x}' for x in d['finalidades_secundarias'])}

Si NO deseas que tus datos se utilicen para las finalidades secundarias, por favor manifiesta tu negativa enviando un correo a **{d['email_arco']}** dentro de los 5 días hábiles siguientes a haber recibido este aviso, indicando "Negativa de finalidades secundarias" en el asunto.

"""

    txt += f"""## Derechos ARCO y revocación del consentimiento

Tienes derecho a Acceder, Rectificar, Cancelar u Oponerte al tratamiento de tus datos (derechos ARCO), así como a revocar el consentimiento otorgado. Para ejercer estos derechos, envía tu solicitud a **{d['email_arco']}**.

## Aviso de Privacidad Integral

El aviso de privacidad integral, con todas las modalidades de tratamiento, transferencias, uso de cookies y datos de contacto del responsable de datos personales, está disponible en: **{(d.get('url_integral') or '[URL pendiente — debes publicarlo en tu sitio]')}**.

_Última actualización: {d['fecha']}_
"""
    return txt


def render_integral(d):
    """Aviso completo para sitio web, sección dedicada de privacidad."""
    txt = f"""# Aviso de Privacidad INTEGRAL

## 1. Identidad y domicilio del Responsable

**{d['razon_social']}** (en adelante, "el Responsable"), con domicilio fiscal en {d['domicilio']}, y Registro Federal de Contribuyentes **{d['rfc']}**, es responsable del tratamiento de tus datos personales.

## 2. Datos personales que serán sometidos a tratamiento

{chr(10).join(f'- {x}' for x in d['datos_recabados'])}

"""
    if d.get('categoria_sensible'):
        txt += """**Aviso sobre datos sensibles:** Algunos de los datos anteriores son considerados sensibles conforme al artículo 3, fracción VI de la LFPDPPP (datos de salud, biométricos, religiosos, etc.). Para su tratamiento solicitamos tu consentimiento expreso y por escrito mediante la firma o aceptación electrónica de este aviso.

"""

    txt += f"""## 3. Finalidades del tratamiento

**Finalidades primarias** (necesarias para la relación con el titular):
{chr(10).join(f'- {x}' for x in d['finalidades_primarias'])}

"""

    if d.get('finalidades_secundarias'):
        txt += f"""**Finalidades secundarias** (no necesarias; el titular puede oponerse):
{chr(10).join(f'- {x}' for x in d['finalidades_secundarias'])}

Si NO deseas que tus datos sean utilizados para las finalidades secundarias, envía un correo a **{d['email_arco']}** con el asunto "Negativa para finalidades secundarias" dentro de los 5 días hábiles siguientes. La negativa no será motivo para negarte los servicios primarios.

"""

    txt += f"""## 4. Transferencia de datos personales

El Responsable podrá transferir tus datos personales a las siguientes terceras personas:

- **Autoridades fiscales, administrativas o judiciales** competentes, cuando lo requieran por ley.
- **Proveedores de servicios contratados** (pasarela de pago, paquetería, hosting, contador, abogado), únicamente para las finalidades primarias y bajo contrato de confidencialidad.

Para estas transferencias **no se requiere tu consentimiento** conforme al artículo 37 de la LFPDPPP. Cualquier transferencia distinta requerirá tu consentimiento expreso.

## 5. Derechos ARCO

Como titular de tus datos, tienes derecho a:

- **Acceder** a los datos personales que poseemos.
- **Rectificar** los datos que sean inexactos o incompletos.
- **Cancelar** los datos cuando consideres que no se requieren.
- **Oponerte** al uso para fines específicos.

Para ejercer estos derechos, envía tu solicitud al correo **{d['email_arco']}** con:

1. Tu nombre completo y domicilio o medio para comunicarte la respuesta.
2. Identificación oficial (copia adjunta).
3. Descripción clara del derecho que ejerces y los datos involucrados.
4. Cualquier elemento o documento que facilite la localización de tus datos.

Te responderemos en un plazo máximo de 20 días hábiles conforme al artículo 32 de la LFPDPPP.

## 6. Revocación del consentimiento

En cualquier momento podrás revocar el consentimiento que has otorgado para el tratamiento de tus datos, dirigiendo tu solicitud al correo **{d['email_arco']}** siguiendo el mismo procedimiento que para los derechos ARCO. La revocación no podrá tener efectos retroactivos.

## 7. Limitación de uso y divulgación

Puedes limitar el uso o divulgación de tus datos mediante el mismo correo **{d['email_arco']}**. Adicionalmente, puedes inscribirte en el Registro Público para Evitar Publicidad de la PROFECO ({"https://repep.profeco.gob.mx/" if 'ecommerce' in d.get('giro_raw', '') else "https://repep.profeco.gob.mx/"}).

## 8. Uso de cookies y tecnologías similares

{"Nuestro sitio web utiliza cookies y tecnologías similares para mejorar tu experiencia. Las cookies utilizadas son: (a) técnicas o necesarias para el funcionamiento del sitio, (b) analíticas para entender el uso del sitio, y (c) de marketing para mostrarte contenido relevante. Puedes deshabilitarlas desde la configuración de tu navegador." if 'ecommerce' in d.get('giro_raw', '') or 'servicios' in d.get('giro_raw', '') else "Nuestro sitio puede utilizar cookies para mejorar tu experiencia. Para más información o deshabilitarlas, ajusta la configuración de tu navegador."}

## 9. Cambios al Aviso de Privacidad

Cualquier modificación al presente Aviso de Privacidad será comunicada a través de **{d.get('url_integral', 'nuestro sitio web')}** o por correo electrónico a los titulares registrados.

## 10. Autoridad

Si consideras que tu derecho de protección de datos personales ha sido vulnerado por alguna conducta u omisión del Responsable, podrás interponer una queja o denuncia ante la autoridad competente (al cierre de 2025, las funciones del extinto INAI fueron asumidas por la Secretaría Anticorrupción y Buen Gobierno — verifica autoridad vigente al momento de presentar).

---

_Última actualización: {d['fecha']}_
_Vigencia: este aviso permanece vigente hasta su próxima actualización._
"""
    return txt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tipo", choices=["corto", "simplificado", "integral"], default="integral")
    ap.add_argument("--razon-social")
    ap.add_argument("--rfc")
    ap.add_argument("--domicilio")
    ap.add_argument("--email-arco")
    ap.add_argument("--url-integral", default=None)
    ap.add_argument("--giro", choices=list(FINALIDADES_POR_GIRO.keys()), default="generico")
    ap.add_argument("--json", help="Pasa todos los inputs como JSON")
    ap.add_argument("--salida", help="Guardar a archivo")
    args = ap.parse_args()

    if args.json:
        d = json.loads(args.json)
    else:
        for required in ("razon_social", "rfc", "domicilio", "email_arco"):
            if not getattr(args, required.replace("_", "_"), None):
                ap.error(f"--{required.replace('_','-')} requerido (o usa --json)")
        d = {
            "tipo": args.tipo,
            "razon_social": args.razon_social,
            "rfc": args.rfc,
            "domicilio": args.domicilio,
            "email_arco": args.email_arco,
            "url_integral": args.url_integral,
            "giro": args.giro,
        }

    giro = d.get("giro", "generico")
    plantilla = FINALIDADES_POR_GIRO.get(giro, FINALIDADES_POR_GIRO["generico"])
    d.setdefault("finalidades_primarias", plantilla["primarias"])
    d.setdefault("finalidades_secundarias", plantilla.get("secundarias", []))
    d.setdefault("datos_recabados", plantilla["datos_recabados"])
    d.setdefault("categoria_sensible", plantilla.get("categoria_sensible", False))
    d.setdefault("fecha", date.today().isoformat())
    d["giro_raw"] = giro

    tipo = d.get("tipo", "integral")
    if tipo == "corto":
        out = render_corto(d)
    elif tipo == "simplificado":
        out = render_simplificado(d)
    else:
        out = render_integral(d)

    if args.salida:
        Path(args.salida).write_text(out, encoding="utf-8")
        print(f"✓ Aviso de privacidad ({tipo}) guardado en {args.salida}")
    else:
        print(out)


if __name__ == "__main__":
    main()
