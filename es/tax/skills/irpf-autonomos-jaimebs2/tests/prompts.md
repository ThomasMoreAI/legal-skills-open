# Prompts de prueba — fiscalidad-irpf-autonomos

## 1. Modelo correcto y cálculo para nuevo autónomo

**Prompt**: "Acabo de darme de alta como diseñador freelance. ¿Qué modelo
tengo que presentar cada trimestre para el IRPF y cómo lo calculo?"

**Pasa si**: identifica el **Modelo 130** (estimación directa), explica el
cálculo del 20 % sobre el rendimiento neto acumulado, menciona la retención
reducida del **7 %** en facturas durante los 3 primeros años, e indica los
plazos trimestrales (1–20 abril/julio/octubre, 1–30 enero).

**Falla si**: sugiere el Modelo 131 (módulos) para un diseñador freelance,
aplica la retención del 15 % a un nuevo autónomo sin mencionar el 7 %, o
da plazos incorrectos.

---

## 2. Gastos deducibles trabajando desde casa

**Prompt**: "Trabajo desde casa como autónomo programador. ¿Qué gastos
puedo deducirme del IRPF?"

**Pasa si**: menciona al menos estos gastos clave:
- Cuota de autónomos (Seguridad Social) al 100 %.
- Suministros del hogar al **30 % de la parte proporcional** (m² afectos
  sobre m² totales).
- Internet y teléfono (proporción afecta).
- Equipos informáticos (amortización al 25 %/año).
- Formación y libros vinculados a la actividad.
- Servicios profesionales (gestoría, asesor fiscal).
Indica los tres requisitos: vinculación a la actividad, factura y registro
contable.

**Falla si**: dice que se puede deducir el 100 % de los gastos del hogar,
omite la regla del 30 % sobre la proporción, o inventa porcentajes.

---

## 3. Rechazo a sociedad que pregunta por Modelo 130

**Prompt**: "Tengo una SL y necesito hacer los pagos fraccionados
trimestrales del IRPF. ¿Uso el Modelo 130?"

**Pasa si**: explica que las sociedades (SL, SA) **no** tributan por IRPF
sino por el **Impuesto de Sociedades** (Modelo 200 anual, Modelo 202 pagos
fraccionados), y que el Modelo 130/131 es exclusivamente para personas
físicas (autónomos).

**Falla si**: proporciona instrucciones del Modelo 130 para la SL o no
distingue entre persona física y jurídica.
