#!/usr/bin/env python3
"""
Rebuild enriched index from existing JSON index (skip BOE API download).
Much faster — only re-embeds with enriched texts.
"""

import json, os, struct, sys, time, urllib.request, urllib.error, re

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_API = "https://api.openai.com/v1/embeddings"
MODEL = "text-embedding-3-small"
DIMENSIONS = 1536
BATCH_SIZE = 100
INDEX_DIR = os.path.expanduser("~/.boe")
EXISTING_INDEX = os.path.join(INDEX_DIR, "index-v1.json")

# ============================================================
# ENRICHMENT DATA — Rich descriptions for major Spanish laws
# ============================================================

LAW_DESCRIPTIONS = {
    "BOE-A-2010-10544": "Ley de Sociedades de Capital (LSC). Regula sociedades anónimas (SA), sociedades limitadas (SL/SRL) y comanditarias por acciones. Constitución de sociedades, capital social, acciones, participaciones, junta general, administradores, responsabilidad del administrador, cuentas anuales, disolución, liquidación, transformación, compraventa de participaciones, compraventa de empresa, adquisición de sociedades, transmisión de acciones, venta de empresa, pacto de socios, derecho de suscripción preferente, aumento y reducción de capital, autocartera, dividendos, impugnación de acuerdos, derecho de separación, M&A societario.",
    "BOE-A-1889-4763": "Código Civil (CC). Derecho civil general: personas, familia, matrimonio, divorcio, separación, filiación, adopción, patria potestad, tutela, herencia, testamento, sucesiones, legítima, obligaciones, contratos, compraventa, arrendamiento, prescripción de deudas, plazos de prescripción (5 años acciones personales, 6 años acciones reales), caducidad de acciones, cuánto tiempo para reclamar una deuda, propiedad, posesión, usufructo, servidumbres, hipoteca, fianza, deudas, responsabilidad civil extracontractual, enriquecimiento injusto.",
    "BOE-A-1885-6627": "Código de Comercio. Derecho mercantil general: comerciantes, obligaciones mercantiles, registro mercantil, contabilidad, contratos mercantiles, comisión mercantil, depósito mercantil, préstamo mercantil, compraventa mercantil, letra de cambio, cheque, pagaré, seguros, quiebra (histórico).",
    "BOE-A-1995-25444": "Código Penal (CP). Derecho penal: delitos y penas. Homicidio, asesinato, lesiones, robo, hurto, estafa, apropiación indebida, daños, delitos contra el patrimonio, falsificación, delitos contra la Hacienda Pública, delito fiscal, blanqueo de capitales, cohecho, prevaricación, malversación, tráfico de drogas, violencia de género, agresión sexual, amenazas, coacciones, injurias, calumnias, delitos informáticos, delitos societarios, administración desleal, alzamiento de bienes. Me han robado y quiero denunciar, denuncia penal, víctima de un delito, cómo denunciar un robo.",
    "BOE-A-2015-11430": "Estatuto de los Trabajadores (ET). Derecho laboral: contrato de trabajo, tipos de contrato (temporal, indefinido, formación, prácticas), jornada laboral, salario, vacaciones, permisos, excedencias, despido, despido improcedente, despido objetivo, ERE, ERTE, indemnización por despido, negociación colectiva, convenio colectivo, representación de los trabajadores, modificación sustancial de condiciones, movilidad geográfica, subrogación laboral.",
    "BOE-A-2003-23186": "Ley General Tributaria (LGT). Derecho tributario: obligaciones tributarias, procedimiento de gestión tributaria, inspección, recaudación, infracciones y sanciones tributarias, prescripción tributaria (4 años), recursos, reclamaciones económico-administrativas, fraude fiscal, responsabilidad tributaria, obligados tributarios, domicilio fiscal, NIF.",
    "BOE-A-2000-323": "Ley de Enjuiciamiento Civil (LEC). Derecho procesal civil: juicio ordinario, juicio verbal, procedimiento monitorio, ejecución forzosa, medidas cautelares, prueba, recursos de apelación, casación, costas procesales, capacidad procesal, litisconsorcio, acumulación de acciones.",
    "BOE-A-2020-4859": "Texto Refundido de la Ley Concursal. Concurso de acreedores, insolvencia, quiebra, preconcurso, comunicación de negociaciones, plan de reestructuración, convenio de acreedores, liquidación concursal, créditos contra la masa, calificación del concurso, segunda oportunidad, exoneración de deudas.",
    "BOE-A-1978-31229": "Constitución Española (CE). Derechos fundamentales, libertades públicas, organización del Estado, división de poderes, Corona, Cortes Generales, Gobierno, Poder Judicial, Tribunal Constitucional, comunidades autónomas, reforma constitucional, derechos sociales.",
    "BOE-A-1994-26003": "Ley de Arrendamientos Urbanos (LAU). Alquiler de vivienda, arrendamiento, inquilino, arrendador, renta, duración del contrato, prórroga, desahucio, fianza, gastos de comunidad, subarriendo, derecho de adquisición preferente, actualización de renta, echar al inquilino.",
    "BOE-A-2010-6737": "Ley de Prevención del Blanqueo de Capitales y de la Financiación del Terrorismo. Blanqueo de dinero, lavado de capitales, KYC, diligencia debida, identificación del titular real, sujetos obligados, declaración de operaciones sospechosas, SEPBLAC, PBC/FT, compliance.",
    "BOE-A-2014-12328": "Ley del Impuesto sobre Sociedades (LIS). Fiscalidad de empresas, base imponible, deducciones, tipo impositivo, amortizaciones, gastos deducibles, consolidación fiscal, operaciones vinculadas, precios de transferencia, régimen PYME, reinversión de beneficios, eliminación de doble imposición.",
    "BOE-A-2006-20764": "Ley del Impuesto sobre la Renta de las Personas Físicas (IRPF). Impuesto sobre la renta, rendimientos del trabajo, rendimientos de capital, ganancias patrimoniales, retenciones, autónomos, estimación directa, estimación objetiva (módulos), deducciones, mínimo personal y familiar.",
    "BOE-A-1992-28740": "Ley del Impuesto sobre el Valor Añadido (IVA). Impuesto al consumo, hecho imponible, base imponible, tipos impositivos (general 21%, reducido 10%, superreducido 4%), exenciones, deducciones, régimen simplificado, recargo de equivalencia, operaciones intracomunitarias.",
    "BOE-A-2007-12946": "Ley de Defensa de la Competencia (LDC). Prácticas restrictivas, abuso de posición dominante, concentraciones empresariales, cártel, CNMC, control de fusiones, ayudas de Estado, libre competencia.",
    "BOE-A-1991-628": "Ley de Competencia Desleal (LCD). Actos de competencia desleal: engaño, confusión, denigración, imitación, explotación de reputación ajena, violación de secretos, inducción a la infracción contractual, actos de discriminación, venta a pérdida, publicidad ilícita.",
    "BOE-A-2018-16673": "Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales (LOPDGDD). Privacidad, RGPD, datos personales, consentimiento, delegado de protección de datos, derechos ARCO, derecho al olvido, portabilidad, transferencias internacionales, AEPD.",
    "BOE-A-2023-19758": "Ley de Modificaciones Estructurales de las Sociedades Mercantiles (LME). Fusiones, escisiones, cesión global de activo y pasivo, transformación de sociedades, traslado internacional de domicilio social, M&A, reestructuración societaria, fusiones y adquisiciones.",
    "BOE-A-2009-5614": "Ley sobre Modificaciones Estructurales de las Sociedades Mercantiles (anterior LME 2009). Fusiones, escisiones, cesión global, transformación societaria, fusiones y adquisiciones, M&A.",
    "BOE-A-2015-11435": "Ley del Mercado de Valores (LMV). Mercados financieros, valores negociables, acciones cotizadas, CNMV, OPA, información privilegiada, abuso de mercado, folleto informativo, inversión colectiva, ESI.",
    "BOE-A-1987-28141": "Ley del Impuesto sobre Sucesiones y Donaciones (ISD). Herencia, donaciones, impuesto sucesorio, base imponible, reducciones, bonificaciones por comunidad autónoma, seguros de vida, liquidación.",
    "BOE-A-1993-25359": "Ley del Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados (ITP-AJD). Compraventa de inmuebles, transmisiones onerosas, constitución de sociedades, documentos notariales, operaciones societarias.",
    "BOE-A-2007-20555": "Ley General para la Defensa de los Consumidores y Usuarios. Derechos del consumidor, garantías, desistimiento, cláusulas abusivas, información precontractual, comercio electrónico, reclamaciones.",
    "BOE-A-2015-11724": "Ley General de la Seguridad Social (LGSS). Cotizaciones, prestaciones, jubilación, pensión, incapacidad, desempleo, maternidad, paternidad, autónomos, RETA, régimen general, base de cotización, tarifa plana.",
    "BOE-A-1946-2453": "Ley Hipotecaria (LH). Registro de la propiedad, hipoteca, anotación preventiva, inscripción registral, prioridad registral, tercero hipotecario, fe pública registral, cancelación de cargas.",
    "BOE-A-1996-8930": "Ley de Propiedad Intelectual (LPI). Derechos de autor, copyright, obras literarias, artísticas, musicales, cinematográficas, software, derechos morales, derechos patrimoniales, licencias, plagio, canon digital.",
    "BOE-A-2015-8328": "Ley de Patentes. Propiedad industrial, invenciones, modelos de utilidad, solicitud de patente, OEPM, licencias obligatorias, nulidad de patente.",
    "BOE-A-2001-23093": "Ley de Marcas. Marca registrada, signos distintivos, denominación comercial, nombre comercial, registro de marca, OEPM, oposición, caducidad, nulidad de marca.",
    "BOE-A-1995-24292": "Ley de Prevención de Riesgos Laborales (LPRL). Seguridad y salud en el trabajo, accidente laboral, enfermedad profesional, evaluación de riesgos, plan de prevención, servicio de prevención, delegado de prevención.",
    "BOE-A-2007-5584": "Ley de Sociedades Profesionales. Sociedades de abogados, médicos, arquitectos, ingenieros y otros profesionales colegiados. Régimen especial de responsabilidad.",
    "BOE-A-1998-16718": "Ley de la Jurisdicción Contencioso-Administrativa (LJCA). Recurso contencioso-administrativo, procedimiento abreviado, medidas cautelares, ejecución de sentencias contra la Administración.",
    "BOE-A-2015-10565": "Ley del Procedimiento Administrativo Común (LPAC). Procedimiento administrativo, silencio administrativo, recursos (alzada, reposición, extraordinario de revisión), notificaciones electrónicas, plazos administrativos.",
    "BOE-A-2015-10566": "Ley de Régimen Jurídico del Sector Público (LRJSP). Organización administrativa, órganos colegiados, convenios, responsabilidad patrimonial de la Administración, relaciones interadministrativas.",
    "BOE-A-1882-6036": "Ley de Enjuiciamiento Criminal (LECrim). Proceso penal, denuncia, querella, instrucción, juicio oral, sentencia penal, recursos penales, prisión provisional, medidas cautelares penales, jurado.",
    "BOE-A-2017-12902": "Ley de Contratos del Sector Público (LCSP). Licitación pública, contratación pública, procedimiento abierto, restringido, negociado, mesa de contratación, garantías, modificación de contratos públicos.",
    "BOE-A-2023-12203": "Ley por el Derecho a la Vivienda. Vivienda protegida, zona tensionada, límite de alquiler, grandes tenedores, desahucio, vulnerabilidad, parque público de vivienda.",
    "BOE-A-2000-544": "Ley Orgánica de Extranjería. Inmigración, residencia, permiso de trabajo, visado, expulsión, reagrupación familiar, asilo, refugiados, NIE.",
    "BOE-A-1996-17533": "Reglamento del Registro Mercantil (RRM). Inscripción de sociedades, depósito de cuentas anuales, nombramiento de administradores, poderes, legalización de libros.",
    "BOE-A-1960-10906": "Ley de Propiedad Horizontal (LPH). Comunidad de propietarios, cuotas de participación, junta de propietarios, presidente, obras, derramas, morosidad, impugnación de acuerdos.",
    "BOE-A-2003-23646": "Ley de Arbitraje. Arbitraje comercial, convenio arbitral, árbitros, laudo arbitral, ejecución de laudos, arbitraje internacional.",
    "BOE-A-2012-9112": "Ley de Mediación en asuntos civiles y mercantiles. Mediación civil, mediación mercantil, acuerdo de mediación, mediador, procedimiento de mediación.",
    "BOE-A-2007-13409": "Ley del Trabajo Autónomo (LETA). Autónomos, trabajador por cuenta propia, TRADE, derechos y deberes del autónomo, prestaciones, Seguridad Social de autónomos, cuánto pago de autónomo.",
    "BOE-A-1985-12666": "Ley Orgánica del Poder Judicial (LOPJ). Organización judicial, jueces, magistrados, Consejo General del Poder Judicial, jurisdicción, competencia, independencia judicial.",
    "BOE-A-2004-21760": "Ley Orgánica de Medidas de Protección Integral contra la Violencia de Género. Violencia de género, violencia machista, orden de protección, juzgados de violencia, medidas penales, medidas civiles, asistencia integral a víctimas.",
}

def extract_short_name(title):
    patterns = [
        r'por el que se aprueba el texto refundido de la (.+?)\.?$',
        r'por el que se aprueba (?:el |la )?(.+?)\.?$',
        r'por la que se (?:regula|aprueba|establece|modifica|desarrolla) (?:el |la |los |las )?(.+?)\.?$',
        r'por el que se (?:regula|aprueba|establece|modifica|desarrolla) (?:el |la |los |las )?(.+?)\.?$',
    ]
    for pat in patterns:
        m = re.search(pat, title, re.IGNORECASE)
        if m:
            result = m.group(1).strip().rstrip('.')
            if len(result) > 10:
                return result
    return ""

RANGO_KEYWORDS = {
    "ley orgánica": "ley orgánica",
    "ley foral": "norma foral navarra",
    "ley": "ley",
    "real decreto legislativo": "texto refundido",
    "real decreto-ley": "decreto-ley urgente",
    "real decreto": "reglamento",
    "decreto legislativo": "decreto legislativo autonómico",
}

def enrich_title(entry):
    eid = entry["id"]
    title = entry["title"]
    rango = entry.get("rango", "")
    
    if eid in LAW_DESCRIPTIONS:
        return f"{LAW_DESCRIPTIONS[eid]} Título oficial: {title}"
    
    short_name = extract_short_name(title)
    rango_lower = rango.lower() if rango else ""
    rango_kw = ""
    for k, v in RANGO_KEYWORDS.items():
        if k in rango_lower:
            rango_kw = v
            break
    
    parts = [title]
    if short_name and short_name != title and len(short_name) > 15:
        parts.append(f"Nombre corto: {short_name}.")
    if rango_kw:
        parts.append(f"Tipo: {rango_kw}.")
    
    return " ".join(parts)

def embed_batch(texts):
    payload = json.dumps({"model": MODEL, "input": texts, "dimensions": DIMENSIONS}).encode()
    req = urllib.request.Request(OPENAI_API, data=payload, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {OPENAI_API_KEY}",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
    return [e["embedding"] for e in sorted(data["data"], key=lambda x: x["index"])]

def save_binary_index(entries, path):
    valid = [e for e in entries if e.get("vector") is not None]
    with open(path, "wb") as f:
        f.write(b"BOEI")
        f.write(struct.pack("<I", 1))  # keep version 1 for Go compat
        f.write(struct.pack("<I", DIMENSIONS))
        f.write(struct.pack("<I", len(valid)))
        for e in valid:
            id_b = e["id"].encode()
            f.write(struct.pack("<I", len(id_b)))
            f.write(id_b)
            title_b = e["title"].encode()
            f.write(struct.pack("<I", len(title_b)))
            f.write(title_b)
            f.write(struct.pack(f"<{len(e['vector'])}f", *e["vector"]))
    size_mb = os.path.getsize(path) / (1024*1024)
    print(f"💾 Saved {path} ({size_mb:.1f} MB, {len(valid)} entries)")

def main():
    if not OPENAI_API_KEY:
        print("❌ Set OPENAI_API_KEY", file=sys.stderr); sys.exit(1)
    
    print("📂 Loading existing index...")
    with open(EXISTING_INDEX) as f:
        idx = json.load(f)
    
    entries = idx["entries"]
    print(f"   {len(entries)} entries loaded")
    print(f"   Manual descriptions: {len(LAW_DESCRIPTIONS)} laws\n")
    
    # Enrich
    enriched = []
    manual = 0
    for e in entries:
        txt = enrich_title(e)
        enriched.append(txt)
        if e["id"] in LAW_DESCRIPTIONS:
            manual += 1
    print(f"📝 {manual} manually described, {len(entries)-manual} auto/title-only")
    
    # Show examples
    for eid in ["BOE-A-1995-25444", "BOE-A-1889-4763"]:
        for i, e in enumerate(entries):
            if e["id"] == eid:
                print(f"\n  Example {eid}:")
                print(f"  Enriched: {enriched[i][:150]}...")
                break
    
    # Re-embed with enriched text
    print(f"\n🧠 Embedding {len(entries)} enriched texts...")
    for i in range(0, len(entries), BATCH_SIZE):
        batch = enriched[i:i+BATCH_SIZE]
        try:
            vecs = embed_batch(batch)
            for j, v in enumerate(vecs):
                entries[i+j]["vector"] = v
        except Exception as ex:
            print(f"  ⚠️ Batch {i}: {ex}", file=sys.stderr)
            time.sleep(5)
            try:
                vecs = embed_batch(batch)
                for j, v in enumerate(vecs):
                    entries[i+j]["vector"] = v
            except:
                for j in range(len(batch)):
                    entries[i+j]["vector"] = None
        
        done = min(i+BATCH_SIZE, len(entries))
        if done % 1000 == 0 or done == len(entries):
            print(f"  ... {done}/{len(entries)}")
        time.sleep(0.2)
    
    ok = sum(1 for e in entries if e.get("vector") is not None)
    print(f"✅ {ok}/{len(entries)} embedded")
    
    # Save
    save_binary_index(entries, os.path.join(INDEX_DIR, "index-v2.bin"))
    print("\n🎉 Done!")

if __name__ == "__main__":
    main()
