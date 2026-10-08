# TEST-CASES — /frontend-privacy/transparencia

> Verificar estos casos antes de publicar cambios a la skill.  
> El score debe estar dentro de ±3 pts del esperado.

---

## T1 — Sin política, con analytics y Meta Pixel

**Input:**
```
/frontend-privacy/transparencia "App web con Google Analytics y Facebook 
Pixel activos. Sin política de privacidad publicada. Sin banner de cookies. 
Opera en Colombia y Brasil."
```

**Cálculo esperado:**
- Sin política → +10
- Sin banner de cookies (con analytics y ads) → +10
- Scripts cargan antes del consentimiento → +5 (asumido, marcar supuesto)
- F_rigor = 1.25 (Brasil)
- Raw = 25 × 1.25 = 31.25 → **Score: 31 🔴**

**Hallazgos esperados:**
1. 🔴 Sin política de privacidad (+10)
2. 🟡 Sin banner de cookies con scripts de terceros (+10)
3. 🟡 Scripts de terceros cargando sin consentimiento (+5)

---

## T2 — Política existente con varios gaps de contenido

**Input:**
```
/frontend-privacy/transparencia "Política de privacidad en el footer. 
No menciona terceros ni períodos de retención. Sin datos de contacto 
del responsable del tratamiento. No hay DPO mencionado. Opera en México."
```

**Cálculo esperado:**
- Política existe → 0
- Sin terceros (+5) + sin retención (+5) + sin contacto (+5) = +15 total → cap en +15
- F_rigor = 1.00 (MX)
- Raw = 15 × 1.00 = 15 → **Score: 15 🟡**

**Hallazgos esperados:**
1. 🟡 Política incompleta — sin lista de terceros, sin retención, sin contacto (+15 cap)

---

## T3 — Transparencia conforme (GDPR)

**Input:**
```
/frontend-privacy/transparencia "Política en footer con índice, fecha de 
actualización, base legal por finalidad, lista de terceros con países 
(AWS EU, Stripe US+SCCs), DPO con email publicado. Banner de cookies con 
categorías granulares (necesarias/funcionales/analytics/marketing), 
botón Rechazar igual de prominente que Aceptar. Scripts de GA cargando 
solo tras consentimiento confirmado. Usuarios en España."
```

**Cálculo esperado:**
- Política completa → 0 en todas las dimensiones
- Banner conforme → 0
- DPO publicado → 0
- F_rigor = 1.25 (España = GDPR)
- Raw = 0 × 1.25 = 0 → **Score: 0 🟢**

**Output esperado:** Sin hallazgos. La skill no debe generar falsos positivos en transparencia conforme.

---

## T4 — Cookies no conformes, política OK (UE)

**Input:**
```
/frontend-privacy/transparencia "Política completa con todos los elementos 
requeridos por GDPR. Banner de cookies solo tiene botón 'Aceptar todo' — 
el botón 'Rechazar' es un texto gris sin estilo al lado. Los scripts de 
analytics se cargan inmediatamente al abrir el sitio. Usuarios en Alemania."
```

**Cálculo esperado:**
- Política OK → 0
- Banner sin opción real de rechazar → +10
- Scripts cargan antes del consentimiento → +5
- F_rigor = 1.25 (Alemania = GDPR)
- Raw = 15 × 1.25 = 18.75 → **Score: 19 🟡**

**Nota de validación:** La skill debe detectar el dark pattern del banner aun cuando la política esté completa.

---

## Criterio de éxito

| Criterio | Umbral |
|---|---|
| Score dentro de ±3 pts del esperado | 4/4 |
| T3 (conforme) no genera falsos positivos | Sí |
| T4 detecta dark pattern del banner sin importar política | Sí |
| T1 marca supuesto de scripts pre-carga | Sí |
