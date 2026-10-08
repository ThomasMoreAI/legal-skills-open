"""Motor v6: números canónicos, gazetteer, identidad unificada, verificación final."""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from gazetteer import APELLIDOS, NOMBRES
from rutas_app import ruta_lista_blanca, rutas_modelo_spacy

ARCHIVO_LISTA_BLANCA = ruta_lista_blanca()

SUFIJO_SOCIETARIO = (
    r"(?:S\.?\s*A\.?\s*S\.?\s*(?:BIC)?|"
    r"S\.?\s*A\.?\s*(?:E\.?\s*S\.?\s*P\.?)?|"
    r"LTDA\.?|LIMITADA|"
    r"E\.?\s*U\.?|"
    r"E\.?\s*S\.?\s*P\.?|"
    r"S\.?\s*C\.?\s*A\.?|"
    r"S\.?\s*EN\s*C\.?|"
    r"&\s*C[IÍ]A\.?|"
    r"Y\s*C[IÍ]A\.?|"
    r"COOPERATIVA|"
    r"FONDO\s+DE\s+EMPLEADOS)"
)

NUM_ID = r"\d{1,3}(?:[.\s]\d{3}){1,3}(?:-\d)?|\d{6,12}"
NUM_LARGO = r"\d{5,}(?:[.\-]\d+)*"
CELULAR = r"[36]\d{9}"
FIJO = r"60[1-8]\d{7}"

PATRONES_CATALOGO: list[tuple[str, str, str, int | None]] = [
    # (regex, display, tipo, índice del grupo sensible o None = match completo)
    (rf"(?i)(?:c\.?\s*c\.?|c[eé]dula\s+de\s+ciudadan[ií]a|c[eé]dula)\s*(?:no\.?|n[°º]\.?|n[uú]mero|:)?\s*({NUM_ID})",
     "cédula [CÉDULA]", "CÉDULA", 1),
    (rf"(?i)(?:c\.?\s*e\.?|c[eé]dula\s+de\s+extranjer[ií]a)\s*(?:no\.?|n[°º]\.?|:)?\s*({NUM_ID})",
     "cédula extranjería [CÉDULA_EXTRANJERÍA]", "CÉDULA_EXTRANJERÍA", 1),
    (rf"(?i)(?:t\.?\s*i\.?|tarjeta\s+de\s+identidad)\s*(?:no\.?|n[°º]\.?|:)?\s*({NUM_ID})",
     "tarjeta identidad [TARJETA_IDENTIDAD]", "TARJETA_IDENTIDAD", 1),
    (rf"(?i)(?:t\.?\s*p\.?|tarjeta\s+profesional)\s*(?:no\.?|n[°º]\.?|n[uú]mero|:)?\s*({NUM_ID})",
     "tarjeta profesional [TARJETA_PROFESIONAL]", "TARJETA_PROFESIONAL", 1),
    (rf"(?i)(?:pasaporte|pas\.?)\s*(?:no\.?|n[°º]\.?|:)?\s*([A-Z]?\d{{6,12}})",
     "pasaporte [PASAPORTE]", "PASAPORTE", 1),
    (rf"(?i)(?:nuip|registro\s+civil)\s*(?:no\.?|n[°º]\.?|:)?\s*({NUM_ID})",
     "NUIP [NUIP]", "NUIP", 1),
    (rf"(?i)n\.?\s*i\.?\s*t\.?\s*(?:no\.?|n[°º]\.?|:)?\s*(\d{{3}}\.?\d{{3}}\.?\d{{3}}[-–]?\d)",
     "NIT [NIT]", "NIT", 1),
    (rf"(?i)\b(\d{{3}}\.?\d{{3}}\.?\d{{3}})\s*[-–]\s*(\d)\b",
     "[NIT]", "NIT", 0),
    (r"\b\d{5}[-\s]?\d{2}[-\s]?\d{2}[-\s]?\d{3}[-\s]?\d{4}[-\s]?\d{5}[-\s]?\d{2}\b",
     "[RADICADO]", "RADICADO", None),
    (r"\b\d{23}\b", "[RADICADO]", "RADICADO", None),
    (rf"(?i)(?:expediente|proceso|radicado|noticia\s+criminal|spoa)\s*(?:no\.?|n[°º]\.?|:)?\s*({NUM_LARGO})",
     "expediente [EXPEDIENTE]", "EXPEDIENTE", 1),
    (rf"(?i)cuenta\s+contrato\s*(?:no\.?|n[°º]\.?|n[uú]mero|:)?\s*({NUM_LARGO})",
     "cuenta contrato [CUENTA_CONTRATO]", "CUENTA_CONTRATO", 1),
    (rf"(?i)cuenta\s+(?:de\s+)?(?:ahorros?|corriente)\s*(?:no\.?|n[°º]\.?|:)?\s*({NUM_LARGO})",
     "cuenta bancaria [CUENTA_BANCARIA]", "CUENTA_BANCARIA", 1),
    (rf"(?i)(?:p[oó]liza|factura|contrato|cr[eé]dito|obligaci[oó]n|medidor|c[oó]digo\s+(?:de\s+)?usuario|"
     rf"historia\s+cl[ií]nica|carn[eé]|afiliaci[oó]n|licencia\s+de\s+conducci[oó]n|"
     rf"escritura\s+p[uú]blica|comparendo|noticia\s+criminal|nunc|spoa)\s*"
     rf"(?:no\.?|n[°º]\.?|n[uú]mero|:)?\s*({NUM_LARGO})",
     "identificador [IDENTIFICADOR]", "IDENTIFICADOR", 1),
    (rf"(?i)(?:tel[eé]fono|tel\.?|cel(?:ular)?|m[oó]vil|fax|whatsapp|wsp)\s*[:\.]?\s*({CELULAR}|{FIJO})",
     "teléfono [TELÉFONO]", "TELÉFONO", 1),
    (rf"(?<![\d@])({CELULAR})(?!\d)", "[TELÉFONO]", "TELÉFONO", 1),
    (rf"(?<![\d@])({FIJO})(?!\d)", "[TELÉFONO]", "TELÉFONO", 1),
    (r"\b3\d{2}[\s.\-]?\d{3}[\s.\-]?\d{4}\b", "[TELÉFONO]", "TELÉFONO", None),
    (r"\b60\d[\s.\-]?\d{3}[\s.\-]?\d{4}\b", "[TELÉFONO]", "TELÉFONO", None),
    (r"\b(?:\d{4}[\s-]?){3}\d{4}\b", "[TARJETA]", "TARJETA", None),
    (r"(?i)\b@[\w.]{3,30}\b", "[USUARIO_RED]", "USUARIO_RED", None),
    (r"(?i)\b(?:https?://|www\.)[\w./?=&%-]+\b", "[URL]", "URL", None),
    (r"\b[\w.+-]+@[\w-]+\.[\w.]+\b", "[CORREO]", "CORREO", None),
    (r"(?i)\b(?:calle|cra\.?|carrera|cl\.?|av(?:enida)?\.?|transversal|tv\.?|diagonal|dg\.?|km\.?)\s+\d+[A-Za-z]?\s*(?:bis)?\s*(?:#|n[°º]\.?|no\.?)\s*\d+[A-Za-z]?\s*[-–]?\s*\d*",
     "[DIRECCIÓN]", "DIRECCIÓN", None),
    (r"\b[A-Z]{3}\s?-?\s?\d{3}\b", "[PLACA]", "PLACA", None),
    (r"\b\d{2,3}[A-Z]?\s?[-–]\s?\d{5,8}\b", "[MATRÍCULA]", "MATRÍCULA", None),
    (rf"(?i)matr[ií]cula\s+mercantil\s*(?:no\.?|n[°º]\.?|:)?\s*({NUM_LARGO})",
     "matrícula mercantil [MATRÍCULA_MERCANTIL]", "MATRÍCULA_MERCANTIL", 1),
]

PATRONES_NUMERO_PUBLICO = [
    re.compile(r"(?i)\bley\s+\d{1,5}\s+de\s+(?:19|20)\d{2}"),
    re.compile(r"(?i)\bdecreto\s+\d{1,5}\s+de\s+(?:19|20)\d{2}"),
    re.compile(r"(?i)\bresoluci[oó]n\s+\d{1,6}"),
    re.compile(r"(?i)\bart[ií]culo\s+\d{1,4}"),
    re.compile(r"(?i)\bart\.\s*\d{1,4}"),
    re.compile(r"(?i)\bsentencia\s+(?:[STC]-?\d+|SU\d+)"),
    re.compile(r"(?i)\b(?:T|C|A|SU)-\d{2,4}(?:\s+de\s+(?:19|20)\d{2})?"),
    re.compile(r"(?i)\b(?:19|20)\d{2}\b"),
    re.compile(r"(?i)\bnumeral\s+\d{1,3}"),
    re.compile(r"(?i)\binciso\s+\d{1,3}"),
    re.compile(r"(?i)\bpar[aá]grafo\s+\d{1,3}"),
    re.compile(r"(?i)\bliteral\s+[a-z]\)"),
]

PATRON_EMPRESA = re.compile(
    rf"(?i)(?<![\w@])("
    rf"[A-ZÁÉÍÓÚÑ0-9][\wáéíóúñÁÉÍÓÚÑ'&\-.]{{0,35}}"
    rf"(?:\s+[A-ZÁÉÍÓÚÑ0-9][\wáéíóúñÁÉÍÓÚÑ'&\-.]{{0,35}}){{0,7}}\s+"
    rf"{SUFIJO_SOCIETARIO}"
    rf")(?![A-Za-z0-9])"
)

_PARTE_NOMBRE = r"(?:[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+|[A-ZÁÉÍÓÚÑ]{2,})"
_CONECTOR_NOMBRE = r"(?:\s+(?:de|del|y|van|von|san|santa)\s+)?"

PATRON_CONTEXTO_PERSONA = re.compile(
    r"(?i)(?:el\s+|la\s+)?(?:señor|señora|sr\.?|sra\.?|don|doña|"
    r"doctor|doctora|dr\.?|dra\.?|"
    r"suscrit[oa]|denunciante|demandante|actor|demandado|v[ií]ctima|"
    r"identificado(?:\s+con)?|empleado(?:\s+de)?|representante\s+legal|apoderado|"
    r"testigo|compareciente|ciudadano|ciudadana|"
    r"apoderado\s+judicial|parte\s+demandante|parte\s+demandada|"
    r"nombre\s+de|ciudadano\s+colombiano)\s+"
    rf"(({_PARTE_NOMBRE}{_CONECTOR_NOMBRE}){{2,5}})"
)

PATRON_NOMBRE_CAPITALIZADO = re.compile(
    rf"\b(({_PARTE_NOMBRE}{_CONECTOR_NOMBRE}){{2,5}})\b"
)

PATRON_NOMBRE_MAYUSCULAS = re.compile(
    r"\b([A-ZÁÉÍÓÚÑ]{2,}(?:\s+(?:DE|DEL|Y|VAN|VON|SAN|SANTA)\s+)?"
    r"(?:[A-ZÁÉÍÓÚÑ]{2,})(?:\s+[A-ZÁÉÍÓÚÑ]{2,}){1,4})\b"
)

_MAYUS_NO_PERSONA = frozenset({
    "identificacion", "denunciante", "denuncia", "penal", "consejo", "superior",
    "judicatura", "república", "republica", "colombia", "ministerio", "fiscalia",
    "fiscalía", "procuraduría", "procuraduria", "corte", "tribunal", "juzgado",
    "articulo", "artículo", "numeral", "inciso", "considerando", "fundamento",
    "hecho", "hechos", "pretension", "pretensión", "ordene", "reparacion", "reparación",
    "integral", "daño", "danio", "mayor", "edad", "domiciliado", "ciudad", "tarjeta",
    "profesional", "nombre", "propio", "actuando", "fundamento", "continuacion",
    "continuación", "expone", "exponen", "solicitud", "presente", "escrito",
})

ETIQUETAS_NER = {"PER": "PERSONA", "ORG": "EMPRESA", "LOC": "LUGAR"}

_GEO_AMBIGUO = frozenset({
    "santander", "cordoba", "bolivar", "cesar", "sucre", "cauca", "caldas", "armenia",
    "cali", "meta", "huila", "boyaca", "narino", "tolima", "magdalena", "risaralda",
    "quindio", "choco", "caqueta", "casanare", "putumayo", "amazonas", "guainia",
    "guaviare", "vaupes", "vichada", "atlantico", "antioquia", "cundinamarca",
})

_SUSTANTIVOS_COMUNES = {
    "acción", "accion", "acto", "administrativo", "alegato", "apelación", "apelacion",
    "archivo", "auto", "circular", "comunicación", "comunicacion", "concepto",
    "conclusión", "conclusion", "constancia", "contestación", "contestacion",
    "contrato", "correo", "cuenta", "decisión", "decision", "decreto", "demanda",
    "derecho", "despacho", "devolución", "devolucion", "documento", "ejecutivo",
    "eliminar", "eliminación", "eliminacion", "escrito", "estado", "exigido",
    "expediente", "factura", "fallo", "financiación", "financiacion", "fondo",
    "informe", "instalación", "instalacion", "intereses", "interna", "liquidación",
    "liquidacion", "memorial", "notificación", "notificacion", "oficio", "pago",
    "petición", "peticion", "presente", "proceso", "providencia", "reclamación",
    "reclamacion", "reintegro", "reparaciones", "reposición", "reposicion",
    "resolución", "resolucion", "respuesta", "saldo", "sentencia", "solicitud",
    "subsidio", "sumario", "tarjeta", "profesional", "total", "tutela", "usuario",
    "valor", "verbal", "vía", "via", "citación", "citacion", "cobro", "cobros",
    "consumo", "irregular", "pactado", "restante", "definitiva", "definitivo",
    "ordinario", "ejecutoria", "pronuncie", "mediante", "excedente",
    "acordado", "apareciendo", "recibos", "ausencia", "consentimiento", "válido",
    "valido", "participación", "participacion", "firma", "elaborados", "soportan",
    "inexistencia", "inexigibilidad", "obligaciones", "cobradas",
    "artículo", "articulo", "numeral", "inciso", "parágrafo", "paragrafo",
    "código", "codigo", "ley", "tribunal", "corte", "juzgado",
    "ministerio", "república", "republica", "departamento", "municipio",
    "demandante", "demandado", "actor", "contra", "según", "segun",
    "abogado", "parte", "civil", "penal", "laboral", "circuito",
    "sección", "seccion", "promiscuo", "municipal", "capítulo", "capitulo",
    "título", "titulo", "libro", "anexo", "anexos", "párrafo", "parrafo",
    "considerando", "fundamento", "fundamentos", "pretensión", "pretension",
    "hecho", "hechos", "prueba", "pruebas", "testigo", "perito", "dictamen",
    "acuerdo", "entrega", "acta", "designada", "empleado", "informó", "manera",
    "superior", "consejo", "judicatura", "regional", "seccional",
}

_PALABRAS_NO_NOMBRE_EMPRESA = {
    "la", "el", "los", "las", "un", "una", "de", "del", "al", "en", "a", "ante",
    "empresa", "sociedad", "compañía", "compania", "firma", "grupo", "solicitud",
    "reclamación", "reclamacion", "presente", "comunicación", "comunicacion",
    "recibió", "recibio", "recibi", "mediante", "según", "segun", "contra", "entre", "desde",
    "respondió", "respondio", "negativamente", "cobrar", "reclamaciones",
    "hacia", "sobre", "bajo", "sin", "con", "por", "para", "que", "cual", "cuyo",
}

_PARTES_NOMBRE_STOP = {
    "de", "del", "la", "las", "los", "y", "da", "do", "van", "von", "san", "santa",
}

_INDICADORES_EMPRESA = {
    "constructora", "compañía", "compania", "grupo", "inversiones",
    "comercializadora", "distribuidora", "agropecuaria", "inmobiliaria",
    "corporación", "corporacion", "fundación", "fundacion", "cooperativa",
    "sociedad", "empresa", "firma", "estudio", "asociados", "holding",
}

_TIPOS_CANONICOS = frozenset({"TELÉFONO", "CÉDULA", "CÉDULA_EXTRANJERÍA", "NIT", "CORREO"})


@dataclass
class Hallazgo:
    texto: str
    reemplazo: str
    tipo: str
    fuente: str
    activo: bool = True
    patron: re.Pattern | None = None
    clave: str = ""
    confianza: str = "alta"
    variantes: list[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.clave:
            self.clave = _normalizar(self.texto)


def _validar_dv_nit(nit_completo: str) -> bool:
    digitos = re.sub(r"\D", "", nit_completo)
    if len(digitos) < 10:
        return False
    base = [int(d) for d in digitos[:9].zfill(9)]
    dv_declarado = int(digitos[9])
    pesos = [41, 37, 29, 23, 19, 17, 13, 7, 3]
    total = sum(a * b for a, b in zip(base, pesos))
    residuo = total % 11
    dv_calc = residuo if residuo < 2 else 11 - residuo
    return dv_calc == dv_declarado


def _normalizar(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _normalizar_texto_documento(texto: str) -> str:
    t = unicodedata.normalize("NFC", texto)
    t = t.replace("\u00a0", " ").replace("\u200b", "")
    t = t.replace("\u2013", "-").replace("\u2014", "-")
    t = t.replace("\u2018", "'").replace("\u2019", "'")
    t = t.replace("\u201c", '"').replace("\u201d", '"')
    return t


def _solo_digitos(valor: str) -> str:
    return re.sub(r"\D", "", valor)


def _flexibilizar_texto(texto: str) -> str:
    partes = re.split(r"(\s+)", texto)
    resultado = []
    for p in partes:
        if p.isspace():
            resultado.append(r"\s+")
        else:
            resultado.append(re.escape(p))
    return "(?i)" + "".join(resultado)


def _regex_digitos_flexible(digitos: str) -> re.Pattern:
    """Patrón que matchea dígitos con separadores opcionales (funciona por párrafo)."""
    cuerpo = r"[\s.\-]?".join(re.escape(c) for c in digitos)
    return re.compile(rf"(?<![\d@]){cuerpo}(?!\d)")


def _regex_valor_flexible(valor: str) -> re.Pattern:
    d = _solo_digitos(valor)
    if len(d) >= 5 and d == _solo_digitos(valor.replace(" ", "")):
        if len(d) in (10, 11) and d[0] in "36":
            return _regex_digitos_flexible(d)
        return re.compile(rf"(?<!\d){re.escape(valor)}(?!\d)|{_regex_digitos_flexible(d).pattern}", re.IGNORECASE)
    return re.compile(_flexibilizar_texto(valor).replace("(?i)", ""), re.IGNORECASE)


def _tokens_nombre(valor: str) -> list[str]:
    out = []
    for p in valor.split():
        p = p.strip(".,;:!?¿¡\"'()")
        n = _normalizar(p)
        if len(n) >= 3 and n not in _PARTES_NOMBRE_STOP:
            out.append(n)
    return out


def _puntaje_gazetteer(valor: str) -> int:
    tokens = _tokens_nombre(valor)
    if len(tokens) < 2:
        return 0
    score = 0
    for t in tokens:
        if t in NOMBRES:
            score += 2
        if t in APELLIDOS:
            score += 2
    return score


def _es_mayusculas_nombre(valor: str) -> bool:
    """True si parece nombre en MAYÚSCULAS (escritos jurídicos)."""
    palabras = [p.strip(".,;:!?¿¡\"'()") for p in valor.split() if p.strip()]
    if len(palabras) < 2:
        return False
    if not all(p.isupper() or p.upper() == p for p in palabras if len(p) > 1):
        return False
    return True


def _nombre_mayusculas_valido(valor: str) -> bool:
    tokens = [_normalizar(p) for p in valor.split()]
    tokens = [t for t in tokens if t and t not in _PARTES_NOMBRE_STOP]
    if len(tokens) < 2:
        return False
    if any(t in _MAYUS_NO_PERSONA for t in tokens):
        return False
    if any(t in _SUSTANTIVOS_COMUNES for t in tokens):
        return False
    en_gazetteer = sum(1 for t in tokens if t in NOMBRES or t in APELLIDOS)
    return en_gazetteer >= 1


def _limpiar_nombre_empresa(valor: str) -> str | None:
    valor = valor.strip().rstrip(".")
    sm = re.search(rf"(?i)\s+({SUFIJO_SOCIETARIO})\s*\.?$", valor)
    if not sm:
        return None
    palabras = [p.rstrip(".,;:!?¿¡") for p in valor[:sm.start()].strip().split()]
    while palabras and palabras[0].lower() in _PALABRAS_NO_NOMBRE_EMPRESA:
        palabras.pop(0)
    if not palabras:
        return None
    palabras = palabras[-5:]
    return f"{' '.join(palabras)} {sm.group(1).strip()}".strip()


def _clave_empresa(nombre: str) -> str:
    limpio = _limpiar_nombre_empresa(nombre) or nombre
    sm = re.search(rf"(?i)\s+({SUFIJO_SOCIETARIO})", limpio)
    if sm:
        raiz = limpio[:sm.start()].strip().split()[-1].lower()
        suf = re.sub(r"[^a-zA-Z]", "", sm.group(1).upper())
        return f"{raiz}_{suf}"
    return _normalizar(limpio)


def _sufijo_a_regex(sufijo_texto: str) -> str:
    s = sufijo_texto.upper()
    if re.search(r"S\.?\s*A\.?\s*E\.?\s*S\.?\s*P", s):
        return r"S\.?\s*A\.?\s*(?:E\.?\s*S\.?\s*P\.?)?"
    if re.search(r"S\.?\s*A\.?\s*S", s):
        return r"S\.?\s*A\.?\s*S\.?"
    if re.search(r"S\.?\s*A\.?(?!.*S)", s):
        return r"S\.?\s*A\.?"
    if "LTDA" in s or "LIMITADA" in s:
        return r"LTDA\.?|LIMITADA"
    if re.search(r"E\.?\s*S\.?\s*P", s):
        return r"E\.?\s*S\.?\s*P\.?"
    if re.search(r"E\.?\s*U", s):
        return r"E\.?\s*U\.?"
    if re.search(r"S\.?\s*C\.?\s*A", s):
        return r"S\.?\s*C\.?\s*A\.?"
    return re.escape(sufijo_texto).replace(r"\ ", r"\s+")


def _regex_empresa_flexible(nombre: str) -> re.Pattern:
    nombre = nombre.strip().rstrip(".")
    m = PATRON_EMPRESA.search(nombre + " ")
    if not m:
        return re.compile(rf"(?<![\w@]){re.escape(nombre)}(?![A-Za-z0-9])", re.IGNORECASE)

    full = m.group(1).strip().rstrip(".")
    sm = re.search(rf"(?i)\s+({SUFIJO_SOCIETARIO})\s*\.?$", full)
    if not sm:
        return re.compile(rf"(?<![\w@]){re.escape(full)}(?![A-Za-z0-9])", re.IGNORECASE)

    raiz = full[:sm.start()].strip()
    sufijo_pat = _sufijo_a_regex(sm.group(1))
    raiz_esc = re.escape(raiz).replace(r"\ ", r"\s+")
    regex = rf"(?i)(?<![\w@]){raiz_esc}\s+{sufijo_pat}(?![A-Za-z0-9])"
    return re.compile(regex)


def _es_numero_publico(texto: str, inicio: int, fin: int) -> bool:
    contexto = texto[max(0, inicio - 60):min(len(texto), fin + 30)]
    for patron in PATRONES_NUMERO_PUBLICO:
        if patron.search(contexto):
            return True
    return False


def _span_digitos_en_match(texto: str, m: re.Match) -> tuple[int, int]:
    fragmento = m.group(0)
    offset = m.start()
    dm = re.search(r"\d[\d\s.\-]{4,}\d", fragmento)
    if dm:
        return offset + dm.start(), offset + dm.end()
    return m.start(), m.end()


@dataclass
class MotorAnonimizacion:
    reemplazos_manual: dict = field(default_factory=dict)
    _nlp: object | None = field(default=None, repr=False)
    _terminos_blanca: list[str] = field(default_factory=list, repr=False)
    _patrones_blanca: list[re.Pattern] = field(default_factory=list, repr=False)
    _alias: dict[str, str] = field(default_factory=dict, repr=False)
    _contadores: dict[str, int] = field(default_factory=dict, repr=False)

    def __post_init__(self):
        self._cargar_lista_blanca()

    def _cargar_lista_blanca(self):
        if ARCHIVO_LISTA_BLANCA.exists():
            try:
                datos = json.loads(ARCHIVO_LISTA_BLANCA.read_text(encoding="utf-8"))
                self._terminos_blanca = datos.get("terminos", [])
                self._patrones_blanca = [
                    re.compile(p) for p in datos.get("patrones_publicos", [])
                ]
            except Exception:
                pass

    def es_publico(self, texto: str) -> bool:
        if not texto or len(texto.strip()) < 2:
            return True
        norm = _normalizar(texto)
        if norm in _GEO_AMBIGUO:
            return False
        for termino in self._terminos_blanca:
            t = _normalizar(termino)
            if len(t) < 3:
                continue
            if norm == t:
                return True
            if " " in t and len(t) >= 8 and t in norm:
                return True
        for patron in self._patrones_blanca:
            if patron.search(texto):
                return True
        return False

    def _cargar_nlp(self):
        if self._nlp is not None:
            return self._nlp
        try:
            import spacy
        except ImportError:
            return None
        for ruta in rutas_modelo_spacy():
            try:
                self._nlp = spacy.load(ruta)
                return self._nlp
            except OSError:
                continue
        try:
            self._nlp = spacy.load("es_core_news_sm")
        except OSError:
            self._nlp = None
        return self._nlp

    def _asignar_alias(self, clave: str, tipo: str) -> str:
        k = _normalizar(clave) if not clave.startswith("tel_") else clave
        if k in self._alias:
            return self._alias[k]
        self._contadores[tipo] = self._contadores.get(tipo, 0) + 1
        etiqueta = f"[{tipo}_{self._contadores[tipo]}]"
        self._alias[k] = etiqueta
        return etiqueta

    def _alias_telefono(self, digitos: str) -> str:
        clave = f"tel_{digitos}"
        if clave in self._alias:
            return self._alias[clave]
        return self._asignar_alias(clave, "TELÉFONO")

    def _registrar(self, hallazgos: dict[str, Hallazgo], h: Hallazgo):
        clave = h.clave
        if clave in hallazgos:
            existente = hallazgos[clave]
            if h.tipo == "EMPRESA":
                if len(h.texto) < len(existente.texto):
                    hallazgos[clave] = h
            elif len(h.texto) > len(existente.texto):
                hallazgos[clave] = h
            return
        hallazgos[clave] = h

    def _marcar_zona(self, zonas: list[tuple[int, int]], inicio: int, fin: int):
        zonas.append((inicio, fin))

    def _zona_ocupada(self, zonas: list[tuple[int, int]], inicio: int, fin: int) -> bool:
        return any(a <= inicio and fin <= b for a, b in zonas)

    def _crear_hallazgo(self, valor: str, display: str, tipo: str, fuente: str,
                        clave: str, confianza: str = "alta") -> Hallazgo:
        if tipo == "TELÉFONO":
            digitos = _solo_digitos(valor)
            patron = _regex_digitos_flexible(digitos)
            reemplazo = self._alias_telefono(digitos)
            return Hallazgo(
                texto=digitos, reemplazo=reemplazo, tipo=tipo, fuente=fuente,
                patron=patron, clave=f"tel_{digitos}", confianza=confianza,
                variantes=[valor] if valor != digitos else [],
            )
        if tipo in _TIPOS_CANONICOS or tipo.startswith("CUENTA") or tipo in ("IDENTIFICADOR", "NÚMERO"):
            digitos = _solo_digitos(valor)
            if digitos and len(digitos) >= 5 and digitos == _solo_digitos(valor):
                patron = _regex_digitos_flexible(digitos)
                texto_canon = digitos
            else:
                patron = _regex_valor_flexible(valor)
                texto_canon = valor
            reemplazo = display if "[" in display else display
            return Hallazgo(
                texto=texto_canon, reemplazo=reemplazo, tipo=tipo, fuente=fuente,
                patron=patron, clave=clave, confianza=confianza,
            )
        patron = re.compile(_flexibilizar_texto(valor).replace("(?i)", ""), re.IGNORECASE)
        reemplazo = display if "[" in display else display
        return Hallazgo(
            texto=valor, reemplazo=reemplazo, tipo=tipo, fuente=fuente,
            patron=patron, clave=clave, confianza=confianza,
        )

    def _detectar_catalogo(self, texto: str, hallazgos: dict[str, Hallazgo],
                           zonas_ocupadas: list[tuple[int, int]]):
        for regex, display, tipo, grupo_idx in PATRONES_CATALOGO:
            for m in re.finditer(regex, texto):
                if grupo_idx is not None:
                    if grupo_idx == 0:
                        valor = m.group(0).strip()
                    else:
                        valor = m.group(grupo_idx).strip()
                else:
                    valor = m.group(0).strip()
                if not valor:
                    continue
                if tipo == "NIT" and not _validar_dv_nit(valor if grupo_idx != 0 else m.group(0)):
                    continue
                zi, zf = _span_digitos_en_match(texto, m) if tipo == "TELÉFONO" else (m.start(), m.end())
                if self._zona_ocupada(zonas_ocupadas, zi, zf):
                    continue
                if tipo == "TELÉFONO":
                    digitos = _solo_digitos(valor)
                    if len(digitos) not in (10, 11) or digitos[0] not in "36":
                        continue
                    clave = f"tel_{digitos}"
                    h = self._crear_hallazgo(digitos, display, tipo, "catálogo", clave)
                elif grupo_idx is not None and _solo_digitos(valor) and len(_solo_digitos(valor)) >= 5:
                    clave = f"{tipo.lower()}_{_solo_digitos(valor)}"
                    h = self._crear_hallazgo(valor, display, tipo, "catálogo", clave)
                else:
                    clave = _normalizar(valor)
                    h = self._crear_hallazgo(valor, display, tipo, "catálogo", clave)
                self._registrar(hallazgos, h)
                self._marcar_zona(zonas_ocupadas, zi, zf)

    def _detectar_empresas(self, texto: str, hallazgos: dict[str, Hallazgo],
                           zonas_ocupadas: list[tuple[int, int]]):
        empresas_vistas: dict[str, str] = {}

        for m in PATRON_EMPRESA.finditer(texto):
            valor = _limpiar_nombre_empresa(m.group(1).strip())
            if not valor or len(valor) < 4:
                continue
            if self._zona_ocupada(zonas_ocupadas, m.start(), m.end()):
                continue
            if self.es_publico(valor):
                continue
            clave = _clave_empresa(valor)
            if clave not in empresas_vistas:
                empresas_vistas[clave] = self._asignar_alias(valor, "EMPRESA")

            patron_flex = _regex_empresa_flexible(valor)
            matches = list(patron_flex.finditer(texto)) or [m]
            for m2 in matches:
                match_text = m2.group(0).strip().rstrip(".")
                if self.es_publico(match_text):
                    continue
                h = Hallazgo(
                    texto=match_text, reemplazo=empresas_vistas[clave], tipo="EMPRESA",
                    fuente="societario", patron=patron_flex, clave=clave)
                self._registrar(hallazgos, h)
                self._marcar_zona(zonas_ocupadas, m2.start(), m2.end())

    def _registrar_persona(self, hallazgos: dict[str, Hallazgo], valor: str, fuente: str,
                           confianza: str, zonas_ocupadas: list[tuple[int, int]],
                           inicio: int, fin: int):
        valor = valor.strip().strip(".,;:!?¿¡")
        if len(valor) < 5 or not self._es_persona_valida(valor):
            return
        clave = f"persona_{_normalizar(valor)}"
        if clave in hallazgos and hallazgos[clave].tipo == "EMPRESA":
            return
        reemplazo = self._asignar_alias(valor, "PERSONA")
        pat = re.compile(_flexibilizar_texto(valor).replace("(?i)", ""), re.IGNORECASE)
        h = Hallazgo(texto=valor, reemplazo=reemplazo, tipo="PERSONA", fuente=fuente,
                     patron=pat, clave=clave, confianza=confianza)
        self._registrar(hallazgos, h)
        self._marcar_zona(zonas_ocupadas, inicio, fin)

    def _detectar_contexto_persona(self, texto: str, hallazgos: dict[str, Hallazgo],
                                  zonas_ocupadas: list[tuple[int, int]]):
        for m in PATRON_CONTEXTO_PERSONA.finditer(texto):
            valor = m.group(1).strip()
            self._registrar_persona(
                hallazgos, valor, "contexto", "alta", zonas_ocupadas, m.start(1), m.end(1))

    def _detectar_gazetteer(self, texto: str, hallazgos: dict[str, Hallazgo],
                            zonas_ocupadas: list[tuple[int, int]]):
        for m in PATRON_NOMBRE_CAPITALIZADO.finditer(texto):
            valor = m.group(1).strip()
            if self._zona_ocupada(zonas_ocupadas, m.start(), m.end()):
                continue
            if _es_mayusculas_nombre(valor):
                if not _nombre_mayusculas_valido(valor):
                    continue
            elif _puntaje_gazetteer(valor) < 3:
                continue
            self._registrar_persona(
                hallazgos, valor, "gazetteer", "alta", zonas_ocupadas, m.start(), m.end())

    def _detectar_nombres_mayusculas(self, texto: str, hallazgos: dict[str, Hallazgo],
                                     zonas_ocupadas: list[tuple[int, int]]):
        """Nombres en MAYÚSCULAS típicos de denuncias y escritos (sin depender de spaCy)."""
        for m in PATRON_NOMBRE_MAYUSCULAS.finditer(texto):
            valor = m.group(1).strip().strip(".,;:!?¿¡")
            if self._zona_ocupada(zonas_ocupadas, m.start(), m.end()):
                continue
            if not _nombre_mayusculas_valido(valor):
                continue
            if not self._es_persona_valida(valor):
                continue
            self._registrar_persona(
                hallazgos, valor, "mayúsculas", "alta", zonas_ocupadas, m.start(), m.end())

    def _propagar_apellidos(self, texto: str, hallazgos: dict[str, Hallazgo],
                            zonas_ocupadas: list[tuple[int, int]]):
        personas = sorted(
            [h for h in hallazgos.values() if h.tipo == "PERSONA"],
            key=lambda h: -len(h.texto),
        )
        alias_por_token: dict[str, str] = {}
        for persona in personas:
            for parte in persona.texto.split():
                p = parte.strip(".,;:!?¿¡\"'()")
                n = _normalizar(p)
                if len(n) >= 4 and n not in _PARTES_NOMBRE_STOP and n not in _SUSTANTIVOS_COMUNES:
                    if n in NOMBRES or n in APELLIDOS:
                        alias_por_token.setdefault(n, persona.reemplazo)

        for token, alias in alias_por_token.items():
            patron = re.compile(
                rf"(?<![A-Za-zÁÉÍÓÚÑáéíóúñ@]){re.escape(token)}(?![A-Za-zÁÉÍÓÚÑáéíóúñ])",
                re.IGNORECASE)
            clave = f"parte_{token}"
            if clave in hallazgos:
                continue
            for m in patron.finditer(texto):
                if self._zona_ocupada(zonas_ocupadas, m.start(), m.end()):
                    continue
                if self.es_publico(m.group(0)):
                    continue
                h = Hallazgo(
                    texto=m.group(0), reemplazo=alias, tipo="PERSONA",
                    fuente="propagación", patron=patron, clave=clave, confianza="media")
                self._registrar(hallazgos, h)
                self._marcar_zona(zonas_ocupadas, m.start(), m.end())

    def _detectar_manual(self, texto: str, hallazgos: dict[str, Hallazgo]):
        for real, rol in sorted(self.reemplazos_manual.items(), key=lambda x: -len(x[0])):
            if not real:
                continue
            patron = re.compile(_flexibilizar_texto(real).replace("(?i)", ""), re.IGNORECASE)
            for m in patron.finditer(texto):
                h = Hallazgo(texto=m.group(0), reemplazo=rol, tipo="MANUAL",
                             fuente="manual", patron=patron, clave=_normalizar(real))
                self._registrar(hallazgos, h)

    def _detectar_ner(self, texto: str, hallazgos: dict[str, Hallazgo],
                      zonas_ocupadas: list[tuple[int, int]]):
        nlp = self._cargar_nlp()
        if nlp is None:
            return
        for ent in nlp(texto).ents:
            if ent.label_ not in ETIQUETAS_NER:
                continue
            valor = ent.text.strip()
            if len(valor) < 3 or "\n" in valor or any(c.isdigit() for c in valor):
                continue
            if self._zona_ocupada(zonas_ocupadas, ent.start_char, ent.end_char):
                continue
            if self.es_publico(valor):
                continue
            tipo = ETIQUETAS_NER[ent.label_]
            if tipo == "EMPRESA" and not PATRON_EMPRESA.search(valor):
                continue
            if tipo == "PERSONA":
                if not self._es_persona_valida(valor):
                    continue
                if _puntaje_gazetteer(valor) < 2 and ent.label_ == "PER":
                    continue
                self._registrar_persona(
                    hallazgos, valor, "NER", "media", zonas_ocupadas,
                    ent.start_char, ent.end_char)
                continue
            reemplazo = self._asignar_alias(valor, tipo)
            patron = re.compile(_flexibilizar_texto(valor).replace("(?i)", ""), re.IGNORECASE)
            h = Hallazgo(texto=valor, reemplazo=reemplazo, tipo=tipo, fuente="NER",
                         patron=patron, clave=_normalizar(valor))
            self._registrar(hallazgos, h)
            self._marcar_zona(zonas_ocupadas, ent.start_char, ent.end_char)

    def _es_persona_valida(self, valor: str) -> bool:
        if self.es_publico(valor):
            return False
        palabras = [_normalizar(p) for p in valor.split()]
        if any(p in _SUSTANTIVOS_COMUNES for p in palabras):
            return False
        if any(p in _INDICADORES_EMPRESA for p in palabras):
            return False
        if PATRON_EMPRESA.search(valor):
            return False
        return True

    def _detectar_red_numeros(self, texto: str, hallazgos: dict[str, Hallazgo],
                              zonas_ocupadas: list[tuple[int, int]]):
        patrones = [
            re.compile(r"(?<![\d@])(\d{10})(?!\d)"),
            re.compile(r"\b(\d{5,}(?:[.\-]\d+)*)\b"),
        ]
        vistos: set[str] = set()
        for patron_num in patrones:
            for m in patron_num.finditer(texto):
                valor = m.group(1)
                digitos = _solo_digitos(valor)
                if digitos in vistos:
                    continue
                vistos.add(digitos)
                if self._zona_ocupada(zonas_ocupadas, m.start(), m.end()):
                    continue
                if _es_numero_publico(texto, m.start(), m.end()):
                    continue
                if len(digitos) < 5:
                    continue
                if len(digitos) == 10 and digitos[0] in "36":
                    h = self._crear_hallazgo(
                        digitos, "[TELÉFONO]", "TELÉFONO", "red dinámica", f"tel_{digitos}")
                else:
                    contexto_antes = texto[max(0, m.start() - 40):m.start()]
                    ctx_match = re.search(
                        r"(?i)(cuenta\s+contrato|factura|contrato|p[oó]liza|medidor|c[oó]digo|"
                        r"cr[eé]dito|obligaci[oó]n|expediente|radicado|proceso|referencia|"
                        r"cuenta|usuario|cliente|servicio|instalaci[oó]n|tel[eé]fono|cel|m[oó]vil)"
                        r"\s*(?:no\.?|n[°º]\.?|n[uú]mero|:)?\s*$",
                        contexto_antes)
                    if ctx_match:
                        ctx = ctx_match.group(1).strip().lower()
                        self._contadores["NÚMERO"] = self._contadores.get("NÚMERO", 0) + 1
                        reemplazo = f"{ctx} [NÚMERO_{self._contadores['NÚMERO']}]"
                        h = self._crear_hallazgo(
                            valor, reemplazo, "NÚMERO", "red dinámica", f"num_{digitos}")
                    else:
                        reemplazo = self._asignar_alias(digitos, "NÚMERO")
                        h = self._crear_hallazgo(
                            valor, reemplazo, "NÚMERO", "red dinámica", f"num_{digitos}")
                self._registrar(hallazgos, h)
                self._marcar_zona(zonas_ocupadas, m.start(), m.end())

    def _unificar_personas(self, hallazgos: dict[str, Hallazgo]):
        personas = [h for h in hallazgos.values() if h.tipo == "PERSONA"]
        if not personas:
            return
        parent = {h.clave: h.clave for h in personas}

        def find(x: str) -> str:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: str, b: str):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        for i, h1 in enumerate(personas):
            t1 = set(_tokens_nombre(h1.texto))
            for h2 in personas[i + 1:]:
                t2 = set(_tokens_nombre(h2.texto))
                if t1 & t2:
                    union(h1.clave, h2.clave)

        grupos: dict[str, list[Hallazgo]] = {}
        for h in personas:
            grupos.setdefault(find(h.clave), []).append(h)

        for miembros in grupos.values():
            canon = max(miembros, key=lambda h: len(h.texto))
            alias_previo = miembros[0].reemplazo
            alias = alias_previo if alias_previo.startswith("[PERSONA") else \
                self._asignar_alias(_normalizar(canon.texto), "PERSONA")
            clave_grupo = f"grupo_{_normalizar(canon.texto)}"
            variantes_set: set[str] = {m.texto for m in miembros}
            for m in miembros:
                for parte in m.texto.split():
                    p = parte.strip(".,;:!?¿¡\"'()")
                    if len(p) >= 4 and _normalizar(p) not in _PARTES_NOMBRE_STOP:
                        variantes_set.add(p)
            variantes = sorted(variantes_set, key=len, reverse=True)
            for h in miembros:
                h.reemplazo = alias
                h.clave = clave_grupo
                h.variantes = variantes
            for v in variantes:
                if any(m.texto == v for m in miembros):
                    continue
                pat = re.compile(_flexibilizar_texto(v).replace("(?i)", ""), re.IGNORECASE)
                extra = Hallazgo(
                    texto=v, reemplazo=alias, tipo="PERSONA", fuente="variante",
                    patron=pat, clave=clave_grupo, confianza=canon.confianza, variantes=variantes)
                self._registrar(hallazgos, extra)

    def _consolidar_para_revision(self, hallazgos: list[Hallazgo]) -> list[Hallazgo]:
        """Una fila por persona unificada y una por cada otro dato."""
        resultado: list[Hallazgo] = []
        vistos: set[str] = set()
        otros: dict[str, Hallazgo] = {}

        for h in hallazgos:
            if h.tipo == "PERSONA":
                if h.clave in vistos:
                    continue
                vistos.add(h.clave)
                grupo = [x for x in hallazgos if x.tipo == "PERSONA" and x.clave == h.clave]
                canon = max(grupo, key=lambda x: len(x.texto))
                variantes = sorted({x.texto for x in grupo} | set(canon.variantes), key=len, reverse=True)
                display = Hallazgo(
                    texto=variantes[0] if variantes else canon.texto,
                    reemplazo=canon.reemplazo,
                    tipo="PERSONA",
                    fuente=canon.fuente,
                    patron=canon.patron,
                    clave=canon.clave,
                    confianza=canon.confianza,
                    variantes=variantes,
                    activo=canon.activo,
                )
                if len(variantes) > 1:
                    display.fuente = f"{canon.fuente} (+{len(variantes)-1} variantes)"
                resultado.append(display)
            elif h.clave not in otros or len(h.texto) > len(otros[h.clave].texto):
                otros[h.clave] = h

        resultado.extend(otros.values())
        return sorted(resultado, key=lambda h: (h.tipo != "PERSONA", h.texto.lower()))

    def detectar_pendientes(self, texto: str,
                            hallazgos: list[Hallazgo],
                            parrafos: list[str] | None = None) -> list[Hallazgo]:
        """Revisión invertida sobre texto aplicado por párrafo (como en Word)."""
        motor_tmp = MotorAnonimizacion()
        motor_tmp._terminos_blanca = self._terminos_blanca
        motor_tmp._patrones_blanca = self._patrones_blanca
        bloques = parrafos if parrafos else texto.split("\n")
        preview_partes = [motor_tmp.aplicar(p, hallazgos) for p in bloques if p.strip()]
        preview = "\n".join(preview_partes)

        pendientes: dict[str, Hallazgo] = {}
        zonas: list[tuple[int, int]] = []

        for bloque in preview_partes:
            for m in re.finditer(r"(?<![\d@])(\d{5,})(?!\d)", bloque):
                valor = m.group(1)
                if _es_numero_publico(bloque, m.start(), m.end()):
                    continue
                clave = f"pend_num_{valor}"
                if clave in pendientes:
                    continue
                h = Hallazgo(
                    texto=valor, reemplazo=f"[PENDIENTE_{len(pendientes)+1}]",
                    tipo="REVISAR", fuente="número restante", activo=False,
                    confianza="baja", clave=clave,
                    patron=_regex_digitos_flexible(valor) if valor.isdigit() else None)
                pendientes[clave] = h

        for bloque in preview_partes:
            for m in PATRON_NOMBRE_CAPITALIZADO.finditer(bloque):
                valor = m.group(1).strip()
                if len(valor) < 5 or self.es_publico(valor):
                    continue
                if _puntaje_gazetteer(valor) < 2:
                    continue
                if not self._es_persona_valida(valor):
                    continue
                clave = f"pend_nom_{_normalizar(valor)}"
                if clave in pendientes:
                    continue
                h = Hallazgo(
                    texto=valor, reemplazo=f"[PENDIENTE_{len(pendientes)+1}]",
                    tipo="REVISAR", fuente="nombre restante", activo=False,
                    confianza="baja", clave=clave)
                pendientes[clave] = h

        return sorted(pendientes.values(), key=lambda h: h.texto.lower())

    def verificar_resultado(self, parrafos: list[str],
                            hallazgos: list[Hallazgo]) -> list[Hallazgo]:
        """Escaneo final: datos sensibles que sobrevivieron al reemplazo."""
        return self.detectar_pendientes("", hallazgos, parrafos=parrafos)

    def analizar(self, texto: str) -> list[Hallazgo]:
        texto = _normalizar_texto_documento(texto)
        self._alias.clear()
        self._contadores.clear()
        hallazgos: dict[str, Hallazgo] = {}
        zonas_ocupadas: list[tuple[int, int]] = []

        self._detectar_catalogo(texto, hallazgos, zonas_ocupadas)
        self._detectar_empresas(texto, hallazgos, zonas_ocupadas)
        self._detectar_manual(texto, hallazgos)
        self._detectar_contexto_persona(texto, hallazgos, zonas_ocupadas)
        self._detectar_nombres_mayusculas(texto, hallazgos, zonas_ocupadas)
        self._detectar_gazetteer(texto, hallazgos, zonas_ocupadas)
        self._detectar_ner(texto, hallazgos, zonas_ocupadas)
        self._propagar_apellidos(texto, hallazgos, zonas_ocupadas)
        self._detectar_red_numeros(texto, hallazgos, zonas_ocupadas)
        self._unificar_personas(hallazgos)

        return self._consolidar_para_revision(list(hallazgos.values()))

    def _recolectar_spans(self, texto: str, hallazgos: list[Hallazgo]) -> list[tuple[int, int, str, str]]:
        spans: list[tuple[int, int, str, str]] = []
        activos = [h for h in hallazgos if h.activo]

        for h in activos:
            if h.tipo == "PERSONA":
                variantes = list(dict.fromkeys(h.variantes or [h.texto]))
                for v in variantes:
                    patron = re.compile(_flexibilizar_texto(v).replace("(?i)", ""), re.IGNORECASE)
                    for m in patron.finditer(texto):
                        if not self._es_persona_valida(m.group(0)):
                            continue
                        spans.append((m.start(), m.end(), h.reemplazo, m.group(0)))
                continue

            patron = h.patron or re.compile(r"(?<!\w)" + re.escape(h.texto) + r"(?!\w)", re.IGNORECASE)
            for m in patron.finditer(texto):
                match = m.group(0)
                if h.tipo == "EMPRESA":
                    limpio = _limpiar_nombre_empresa(match)
                    if not limpio or not PATRON_EMPRESA.search(limpio + " "):
                        continue
                spans.append((m.start(), m.end(), h.reemplazo, match))

        spans.sort(key=lambda s: (-(s[1] - s[0]), -s[0]))
        aprobados: list[tuple[int, int, str, str]] = []
        for span in spans:
            if any(not (span[1] <= a or span[0] >= b) for a, b, _, _ in aprobados):
                continue
            aprobados.append(span)
        return sorted(aprobados, key=lambda s: -s[0])

    def aplicar(self, texto: str, hallazgos: list[Hallazgo],
                registro_salida: dict | None = None) -> str:
        texto = _normalizar_texto_documento(texto)
        if registro_salida is None:
            registro_salida = {}
        spans = self._recolectar_spans(texto, hallazgos)
        for inicio, fin, reemplazo, original in spans:
            texto = texto[:inicio] + reemplazo + texto[fin:]
            registro_salida[original] = reemplazo
        return texto

    def mapa_activos(self, hallazgos: list[Hallazgo]) -> dict[str, str]:
        return {h.texto: h.reemplazo for h in hallazgos if h.activo}
