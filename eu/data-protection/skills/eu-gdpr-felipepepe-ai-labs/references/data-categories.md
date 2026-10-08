# Categorías de Datos — GDPR

## Datos Personales (Art. 4)

Cualquier información relacionada con una persona identificada o identificable.

| Tipo | Ejemplos | Nivel de protección |
|--|---------|------|
| Identificadores directos | Nombre, DNI, pasaporte, matrícula | **Standard** |
| Contacto | Email, teléfono, dirección postal | **Standard** |
| Datos de cuenta | Username, password hash, salt | **Standard + cifrado** |
| Datos técnicos | IP address, user-agent, device fingerprint | **Standard** |
| Ubicación | GPS, dirección IP geolocalizada | **Standard** |
| Datos financieros | IBAN, tarjeta de crédito, historial crediticio | **Elevado** |
| Contenido de comunicaciones | Mensajes, emails, archivos adjuntos | **Standard** |

## Datos de Categoría Especial — Art. 9

Prohibidos por defecto. Solo permitidos con excepciones específicas (Art. 9(2)).

| Tipo | Ejemplos | ¿Almacenar en BD? |
|--|---------|------|
| Salud | Historial médico, diagnósticos, medicación | NO sin base legal específica |
| Biometría | Huella digital, reconocimiento facial | NO sin consentimiento explícito |
| Genéticos | Datos ADN, tests genéticos | NO sin consentimiento explícito |
| Opiniones políticas | Afiliación partidista, firma de peticiones | NO sin consentimiento explícito |
| Sindicalización | Afiliación sindical | NO sin consentimiento explícito |
| Religión | Creencias religiosas, prácticas | NO sin consentimiento explícito |
| Orientación sexual | Preferencia sexual | NO sin consentimiento explícito |
| Raza/etnia | Origen racial o étnico | NO sin consentimiento explícito |
| Vida sexual | Información sobre vida sexual | NO sin consentimiento explícito |
| Antecedentes penales | Art. 10 — registros penales | NO sin autorización legal |

## Datos de Menores (Art. 8)

- **Menores de 16 años**: Consentimiento parental obligatorio en la UE
- Los Member States pueden bajar a **13 años** (España: 14 años)
- El código debe detectar edad y aplicar flujo de consentimiento parental si aplica

## Datos Inferidos / Derivados

Datos que no se recogieron originalmente como personales pero que permiten identificar a una persona:

- Perfil de comportamiento (clicks, navegación, tiempo en página)
- Score de crédito o riesgo
- Preferencias de compra inferidas
- Análisis de patrones de uso

**Si se puede inferir una identidad → es dato personal → aplica GDPR**
