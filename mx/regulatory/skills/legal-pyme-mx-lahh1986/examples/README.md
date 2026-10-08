# legal-pyme-mx — Ejemplos

## Ejemplo 1: Validar RFC de un proveedor antes de facturar

**Usuario:** "Voy a contratar a un proveedor con RFC `AAA151209DYA`. ¿Está limpio?"

```bash
./scripts/validate_rfc.py AAA151209DYA --check-69b
```

**Output:**
```json
{
  "rfc_input": "AAA151209DYA",
  "estructura": {
    "valido": true,
    "tipo": "persona_moral",
    "fecha_constitucion": "15-12-09",
    "homoclave": "DYA"
  },
  "listas_sat": {
    "69-B_Definitivos": {
      "status": "ENCONTRADO",
      "linea": "3,AAA151209DYA,\"AYC ADMINISTRACION Y ASESORIA COMERCIAL, S.A. DE C.V.\",Definitivo..."
    }
  },
  "riesgo_critico": true,
  "recomendacion": "NO facturar a/desde este RFC. Riesgo de no deducibilidad y auditoría."
}
```

**Lectura para el usuario:**
> 🚨 **NO contrates a este proveedor.** Está en la lista 69-B Definitivos del SAT como facturera (publicado oficio definitivo 25-nov-2020). Si le facturas o te factura, el SAT puede rechazar la deducción de ese gasto. Riesgo de auditoría + multas. Busca otro proveedor.

---

## Ejemplo 2: Generar Aviso de Privacidad para e-commerce

**Usuario:** "Tengo una tienda online de ropa, S.A. de C.V., RFC MRO230515AB1, oficinas en Roma Norte CDMX. Necesito mi aviso de privacidad."

```bash
./scripts/generate_aviso_privacidad.py \
  --tipo=integral \
  --razon-social="Modas Roma S.A. de C.V." \
  --rfc="MRO230515AB1" \
  --domicilio="Tonalá 50, Col. Roma Norte, Alcaldía Cuauhtémoc, CDMX, CP 06700" \
  --email-arco="privacidad@modasroma.mx" \
  --url-integral="https://modasroma.mx/privacidad" \
  --giro=ecommerce \
  --salida=/tmp/aviso_modasroma.md
```

**Output:** Aviso completo de 10 secciones listo para publicar en `modasroma.mx/privacidad`. Incluye:
- Datos personales recabados (nombre, RFC, domicilio, pago, historial compras)
- Finalidades primarias (cumplir pedido, factura, garantía, ley)
- Finalidades secundarias (marketing, ofertas) con opt-out claro
- Transferencias (SAT, pasarela pago, paquetería, contador)
- Derechos ARCO con procedimiento
- Uso de cookies
- Procedimiento de cambios

**Lectura accionable:**
> Publica este aviso en `modasroma.mx/privacidad` y enlaza desde el footer de todas tus páginas. Incluye una versión CORTA (de un párrafo) en cada formulario donde captures datos (registro, checkout). Mantén el email `privacidad@modasroma.mx` activo y responde solicitudes ARCO en 20 días hábiles.

---

## Ejemplo 3: Calcular costo total de un empleado con ISN

**Usuario:** "Voy a contratar un programador junior por $25,000 brutos al mes en Querétaro. ¿Cuánto realmente me cuesta?"

```python
import json
isn = json.load(open("data/isn_por_estado.json"))
tasa = isn["estados"]["Querétaro"]["tasa_pct"] / 100

salario_bruto = 25000
isn_mensual = salario_bruto * tasa

# Cuotas patronales IMSS aproximadas (clase 1, sin riesgo alto): ~10.5%
imss_patron = salario_bruto * 0.105

# INFONAVIT (aportación patronal): 5%
infonavit = salario_bruto * 0.05

# Sumar
costo_total = salario_bruto + isn_mensual + imss_patron + infonavit
```

**Output:**
```
Costo mensual REAL del empleado en Querétaro:

  Salario bruto:        $25,000
  ISN Querétaro 3%:        $750
  IMSS patronal ~10.5%: $2,625
  INFONAVIT 5%:         $1,250
  ─────────────────────────────
  TOTAL:               $29,625

Diferencia vs. salario contratado: 18.5% extra
Costo anual real:    $355,500 (vs. $300,000 nominal)

Comparativo si lo abres en otro estado:
  Querétaro     3.0% ISN → $29,625
  Chiapas       2.0% ISN → $29,375  (ahorras $250/mes = $3,000/año)
  Aguascalientes 2.5% ISN → $29,500
  BCN           1.8% ISN → $29,425

Para 5 empleados misma situación, cambiar de QRO a BCN ahorra ~$15,000/año.
```

---

## Ejemplo 4: ¿Necesito REPSE?

**Usuario:** "Tengo una agencia que pone instaladores en obras de mis clientes constructores. ¿Necesito REPSE?"

**Razonamiento del skill:**

```
Pregunta clave: ¿pones personal a disposición de un tercero para que ejecute
trabajos en sus instalaciones, con tus instrucciones supervisadas por ellos?

→ Sí: REPSE OBLIGATORIO (Art. 15-A LFT, reforma 2021)
→ No: No aplica (es venta de servicio terminado, no subcontratación)

Tu caso: instaladores trabajando físicamente en obras de constructores
→ Calificas como "Servicios Especializados u Obras Especializadas (SOE)"
→ REPSE OBLIGATORIO

Si NO lo tienes:
- Tu cliente constructor NO puede deducir tu factura ni acreditar el IVA.
- Multa potencial $4,000,000 MXN para ti Y para tu cliente.
- Tu cliente probablemente te dejará de contratar al saberlo.

Trámite:
1. Registro en https://repse.stps.gob.mx/ (requiere e.firma vigente).
2. Demostrar: a) cumplimiento SAT (opinión positiva), b) IMSS al corriente,
   c) actividad económica del servicio especializado en RFC, d) constancias.
3. Tiempo: 20 días hábiles si todo está limpio. Vigencia: 3 años.

Fuente: Guía REPSE STPS — https://repse.stps.gob.mx/
        LFT Art. 12-15 — research/diputados/leyes/LFT.pdf
```

---

## Ejemplo 5: Validar CURP de empleado

**Usuario:** "Voy a dar de alta a Juan Pérez en IMSS. Su CURP es PERJ800614HDFTRR05. ¿Está bien?"

```bash
./scripts/validate_curp.py PERJ800614HDFTRR05
```

**Output:**
```json
{
  "validacion": {
    "valido": false,
    "iniciales": "PERJ",
    "fecha_nacimiento": "1980-06-14",
    "sexo": "Hombre",
    "entidad_codigo": "DF",
    "entidad_nombre": "Ciudad de México",
    "homonimia": "0",
    "digito_verificador_calculado": 9,
    "digito_verificador_ok": false,
    "razon_invalida": "dígito verificador esperado 9, llegó 5"
  }
}
```

**Lectura:**
> La estructura es válida pero el dígito verificador (último carácter) no
> coincide. Probablemente hay un error de captura — confirma con Juan mostrando
> su CURP impresa o validándola en https://www.gob.mx/curp/. NO la captures en
> IDSE así porque IMSS la rechazará.

---

## Ejemplo 6: Checklist completo para abrir e-commerce

**Usuario:** "Voy a vender ropa online desde CDMX como persona moral. ¿Qué necesito legalmente?"

**Output estructurado:**

```
Checklist para abrir e-commerce — CDMX

OBLIGATORIO FEDERAL:
[ ] Alta en SAT como persona moral (Régimen General de Ley)
    → CFF + RMF 2026 Anexo 2 ficha aplicable
    → Trámite: portal SAT con e.firma de notario constituyente
[ ] Inscripción al RFC + obligaciones (ISR mensual, IVA mensual, declaración anual, retenciones nómina)
[ ] Adquirir e.firma + Certificado de Sello Digital (CSD) para facturar
[ ] Contratar PAC para timbrado CFDI 4.0
[ ] Publicar Aviso de Privacidad LFPDPPP (corto en formularios + integral en sitio)
    → ./scripts/generate_aviso_privacidad.py --tipo=integral --giro=ecommerce ...
[ ] Cumplir LFPC art. 76 Bis: domicilio físico visible, RFC, contacto, precios con IVA, garantías, devoluciones
[ ] Si manejas suscripciones recurrentes → cumplir reforma 12-12-2025 (botón claro de cancelación)
[ ] Si HAY empleados:
    [ ] Alta patronal IMSS (IDSE)
    [ ] Alta patronal INFONAVIT (Portal Empresarial)
    [ ] Cumplir Ley Federal del Trabajo (contrato escrito, recibos timbrados, vacaciones, aguinaldo, PTU)
    [ ] Si 16+ empleados: NOM-035 Guía II
    [ ] ISN CDMX 3% sobre nómina mensual

OPCIONAL PERO MUY RECOMENDADO:
[ ] Registrar marca en IMPI (LFPPI) → buscar primero en MARCia
[ ] Registrar contrato de adhesión en RCAL PROFECO
[ ] Obtener Distintivo Digital PROFECO (badge de confianza)

LOCAL CDMX (verificar con CONAMER):
[ ] Licencia de funcionamiento (Alcaldía)
[ ] Uso de suelo compatible con actividad
[ ] Si tienes bodega física: Protección Civil + anuncios

Costo total estimado de cumplimiento año 1 (CDMX, S.A. de C.V., 1 empleado salario $15K):
- Notario constitución:           ~$15,000 - 35,000
- e.firma + CSD:                  ~$1,500
- PAC (timbrado anual ~5K CFDIs): ~$3,000 - 12,000
- Contador externo (mensual):     ~$3,500 × 12 = $42,000
- ISN CDMX 3% × $15K × 12:        $5,400
- Total año 1:                   ~$70,000 - 100,000

Riesgos por NO cumplir, ranqueados por probabilidad × impacto:
1. CFDI mal timbrado (perder deducibilidad clientes) → ALTA freq, $50K-500K
2. Aviso privacidad ausente o malo (queja INAI/SABG) → BAJA freq, $20K-300K
3. Empleado en honorarios sin alta IMSS → MEDIA freq, $100K-1M (capital constitutivo)
4. Sin REPSE prestando servicios → BAJA freq, hasta $4M MXN
```
