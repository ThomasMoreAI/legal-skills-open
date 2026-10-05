---
name: entrevista-inicial-betobetico
title: Entrevista inicial — Legal-fondos
description: Entrevista inicial para configurar playbooks legales del GP — tipo de gestora, NDA playbook, side-letter playbook, MFN activas, template LPA, jurisdicciones. Triggers en "entrevista inicial", "configurar legal-fondos", "primer uso", "onboarding GC".
author: betobetico
author_url: https://github.com/betobetico/claude-para-servicios-financieros/tree/main/plugins/verticales/legal-fondos/skills/entrevista-inicial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: investment-funds
language: es
---

# Entrevista inicial — Legal-fondos

## Modo rápido (2 min)

1. **Tipo de gestora:** SGEIC / SGIIC / SGFT / EAFI con gestión
2. **Vehículos activos:** lista (FCR / FCRE / SICAV / SCR / SIF / Lux SCSp / Delaware LP / otros)
3. **¿Hay template LPA casa?** Sí/No (si sí, pídeselo en el modo completo)
4. **¿Hay playbook NDA?** Sí/No
5. **Idioma documentos:** ES / EN / bilingüe

## Modo completo (10-15 min)

### 1 — Entidad
- Razón social, CIF
- Forma jurídica
- Supervisor (CNMV)
- General Counsel (in-house) o externo
- Despacho asesor habitual

### 2 — Vehículos
Por cada vehículo activo:
- Forma jurídica + jurisdicción
- AUM
- LPA vigente (versión + fecha)
- LPs principales (con o sin nombres según preferencia del usuario)

### 3 — Playbook NDA
- ¿Plantilla casa para enviar NDAs?
- Cláusulas innegociables (líneas rojas):
  - Duración máx aceptable (típico 2-3 años)
  - Jurisdicción y ley aplicable (típico: ES / Inglaterra)
  - Standstill: ¿aceptable?
  - Non-circumvention: ¿aceptable?
  - Penalty clauses: ¿aceptable?
- Cláusulas negociables con bandas

### 4 — Playbook side letters
- ¿Has cedido alguna vez MFN (most favoured nation)?
- Lista de concesiones habituales que SÍ haces:
  - Fee discount (con criterios: importe, sector, primer cierre, etc.)
  - Co-investment rights
  - Advisory board seat
  - Reporting personalizado
  - Excuse / opt-out rights
  - Key person clause variations
- Lista de concesiones que NUNCA haces (líneas rojas)

### 5 — Template LPA
- ¿Tienes template del LPA?
- Cláusulas materiales clave configurables:
  - Management fee structure (% sobre committed vs invested, step-down)
  - Carry (típico 20% / catch-up 100% / hurdle 8%)
  - Investment period (típico 5 años)
  - Fund term (típico 10 años + 2 prórrogas)
  - Key person definitions
  - Default mechanism para LPs
  - Recycling allowed (sí/no, límites)
  - Co-invest priority
  - GP removal / no-fault termination
  - LPAC composition

### 6 — Subscription docs
- Plantilla casa
- Checks pre-firma (KYC/AML, idoneidad, FATCA/CRS, AEAT)
- Quiénes pueden suscribir (institucional only, profesional, minorista con mín. €100k)

### 7 — Vesting / pacto de socios
- ¿Carry distribuido entre el equipo?
- Vesting típico: cliff X meses, schedule Y años
- Good leaver / bad leaver definitions
- Transfer restrictions

### 8 — Procesos
- Sign-off matrix: qué decide el GC solo, qué escala al managing partner, qué al IC, qué a asesor externo
- Sistema de gestión documental (Drive, SharePoint, iManage, NetDocs)
- Sistema de e-firma (DocuSign, signaturit, Adobe Sign)

### 9 — Jurisdicciones
- País sede gestora
- Jurisdicciones donde se comercializa (con notificaciones AIFMD si aplica)
- Jurisdicciones de LPs (CRS / FATCA)
- Ley aplicable contratos (típico Lux / NY / Inglaterra)

## Guardar perfil

En `~/.claude/plugins/config/servicios-financieros/legal-fondos/CLAUDE.md` con la estructura habitual + secciones específicas:

- Playbook NDA (líneas rojas + bandas)
- Playbook side letters (concesiones permitidas + MFN actuales)
- Template LPA (cláusulas configurables)
- Sign-off matrix

## Cierre

Indica al usuario que ya puede ejecutar el resto de comandos. Sugiere empezar con `/legal-fondos:tracker-mfn` para validar que la matriz de side letters actuales está al día.
