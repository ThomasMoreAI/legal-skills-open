# Política de seguridad

## Cómo maneja tus datos la skill (lee esto antes de correrla)

`compliance-uy` corre **localmente dentro de Claude Code**, en tu sesión/máquina. No es un servicio que
suba tu código a ningún lado.

- **No exfiltra tu código ni tus datos.** La skill lee el repo para **mapear** dónde hay datos personales y
  qué proveedores se usan; ese análisis se queda en tu entorno y se escribe en `<repo>/.compliance/`.
- **Nunca copia secretos ni credenciales a los documentos generados.** Cuando detecta secretos en el código
  (control `sec-secrets`) los trata como **ubicación de evidencia** (`archivo:línea`), no copia el valor. Si
  encontrás un secreto hardcodeado, la remediación es **rotarlo y moverlo a variables de entorno / un gestor
  de secretos**, no documentarlo.
- **`.compliance/` puede contener información sensible del negocio** (inventario de datos, proveedores,
  brechas). Decidí con criterio si lo commiteás a un repo privado o público. Recomendación: repo privado, o
  agregá `.compliance/` a `.gitignore` si preferís no versionarlo.
- **Human-in-the-loop obligatorio.** La skill genera **borradores** y un diagnóstico; la interpretación legal
  tiene zonas grises (un abogado puede leer un artículo distinto a otro, y el criterio de la URCDP evoluciona).
  La decisión y la responsabilidad final son del usuario. No constituye asesoría legal (ver `NOTICE.md`).

## Alcance del análisis (qué ve y qué no)

La skill audita el **código del repo**. La privacidad **no vive solo en el repo**: también fluye por correo,
WhatsApp, CRM, planillas, herramientas SaaS, formularios en papel y procesos manuales. Esos canales la skill
**no los ve** — quedan a cargo del responsable. La skill te lo recuerda y los incorpora al RAT por cuestionario.

## Reportar una vulnerabilidad

Si encontrás un problema de seguridad en esta skill (no en tu app):

1. **No abras un issue público** con los detalles del exploit.
2. Usá los **GitHub Security Advisories** del repo (pestaña *Security* → *Report a vulnerability*) o escribí
   al mantenedor.
3. Incluí pasos para reproducir, impacto y, si podés, una propuesta de arreglo.

Respondemos lo antes posible y coordinamos la divulgación responsable.

## Versiones soportadas

Proyecto en estado **alpha**: se da soporte a la rama `main`. Las correcciones de seguridad se aplican sobre `main`.
