package api

import (
	"strings"
	"unicode"

	"golang.org/x/text/unicode/norm"
)

// KnownLaws maps common Spanish law names and abbreviations to BOE IDs
var KnownLaws = map[string]string{
	// Ley de Sociedades de Capital
	"lsc":                          "BOE-A-2010-10544",
	"ley de sociedades de capital":  "BOE-A-2010-10544",
	"sociedades de capital":         "BOE-A-2010-10544",
	"sociedades capital":            "BOE-A-2010-10544",

	// Código Civil
	"codigo civil":    "BOE-A-1889-4763",
	"cc":              "BOE-A-1889-4763",

	// Código de Comercio
	"codigo de comercio": "BOE-A-1885-6627",
	"codigo comercio":    "BOE-A-1885-6627",
	"ccom":               "BOE-A-1885-6627",
	"cdc":                "BOE-A-1885-6627",

	// Ley General Tributaria
	"ley general tributaria": "BOE-A-2003-23186",
	"general tributaria":     "BOE-A-2003-23186",
	"lgt":                    "BOE-A-2003-23186",

	// Estatuto de los Trabajadores
	"estatuto de los trabajadores": "BOE-A-2015-11430",
	"estatuto trabajadores":        "BOE-A-2015-11430",
	"et":                           "BOE-A-2015-11430",

	// Ley de Enjuiciamiento Civil
	"ley de enjuiciamiento civil": "BOE-A-2000-323",
	"enjuiciamiento civil":        "BOE-A-2000-323",
	"lec":                         "BOE-A-2000-323",

	// Ley Concursal
	"ley concursal":                    "BOE-A-2020-4859",
	"texto refundido ley concursal":    "BOE-A-2020-4859",
	"concursal":                        "BOE-A-2020-4859",

	// Constitución
	"constitucion":          "BOE-A-1978-31229",
	"constitucion espanola": "BOE-A-1978-31229",
	"ce":                    "BOE-A-1978-31229",

	// Ley Hipotecaria
	"ley hipotecaria": "BOE-A-1946-2453",
	"hipotecaria":     "BOE-A-1946-2453",
	"lh":              "BOE-A-1946-2453",

	// Ley de Propiedad Horizontal
	"ley de propiedad horizontal": "BOE-A-1960-10906",
	"propiedad horizontal":        "BOE-A-1960-10906",
	"lph":                         "BOE-A-1960-10906",

	// Ley de Arrendamientos Urbanos
	"ley de arrendamientos urbanos": "BOE-A-1994-26003",
	"arrendamientos urbanos":        "BOE-A-1994-26003",
	"lau":                           "BOE-A-1994-26003",

	// Ley de Propiedad Intelectual
	"ley de propiedad intelectual": "BOE-A-1996-8930",
	"propiedad intelectual":        "BOE-A-1996-8930",
	"lpi":                          "BOE-A-1996-8930",

	// Impuesto sobre Sociedades
	"ley del impuesto sobre sociedades": "BOE-A-2014-12328",
	"impuesto sobre sociedades":         "BOE-A-2014-12328",
	"impuesto sociedades":               "BOE-A-2014-12328",
	"lis":                               "BOE-A-2014-12328",

	// IRPF
	"ley del irpf": "BOE-A-2006-20764",
	"irpf":         "BOE-A-2006-20764",
	"lirpf":        "BOE-A-2006-20764",

	// IVA
	"ley del iva": "BOE-A-1992-28740",
	"iva":         "BOE-A-1992-28740",
	"liva":        "BOE-A-1992-28740",

	// Defensa de la Competencia
	"ley de defensa de la competencia": "BOE-A-2007-12946",
	"defensa de la competencia":        "BOE-A-2007-12946",
	"defensa competencia":              "BOE-A-2007-12946",
	"ldc":                              "BOE-A-2007-12946",

	// Código Penal
	"codigo penal": "BOE-A-1995-25444",
	"cp":           "BOE-A-1995-25444",

	// Ley de Enjuiciamiento Criminal
	"ley de enjuiciamiento criminal": "BOE-A-1882-6036",
	"enjuiciamiento criminal":        "BOE-A-1882-6036",
	"lecrim":                         "BOE-A-1882-6036",

	// Ley del Mercado de Valores
	"ley del mercado de valores": "BOE-A-2015-11435",
	"mercado de valores":         "BOE-A-2015-11435",
	"lmv":                        "BOE-A-2015-11435",

	// Ley de Modificaciones Estructurales
	"ley de modificaciones estructurales": "BOE-A-2023-19758",
	"modificaciones estructurales":        "BOE-A-2023-19758",
	"lme":                                 "BOE-A-2023-19758",

	// Ley de Patentes
	"ley de patentes": "BOE-A-2015-8328",
	"patentes":        "BOE-A-2015-8328",

	// Ley de Marcas
	"ley de marcas": "BOE-A-2001-23093",
	"marcas":        "BOE-A-2001-23093",

	// Protección de Datos
	"ley de proteccion de datos":                       "BOE-A-2018-16673",
	"proteccion de datos":                              "BOE-A-2018-16673",
	"lopdgdd":                                          "BOE-A-2018-16673",
	"lopd":                                             "BOE-A-2018-16673",
	"rgpd":                                             "BOE-A-2018-16673",

	// Consumidores
	"ley de consumidores":                                       "BOE-A-2007-20555",
	"ley general para la defensa de los consumidores":           "BOE-A-2007-20555",
	"consumidores":                                              "BOE-A-2007-20555",

	// Contratos del Sector Público
	"ley de contratos del sector publico": "BOE-A-2017-12902",
	"contratos sector publico":            "BOE-A-2017-12902",
	"lcsp":                                "BOE-A-2017-12902",

	// Sociedades Profesionales
	"ley de sociedades profesionales": "BOE-A-2007-5584",
	"sociedades profesionales":        "BOE-A-2007-5584",

	// Mediación
	"ley de mediacion": "BOE-A-2012-9112",

	// Arbitraje
	"ley de arbitraje": "BOE-A-2003-23646",
	"arbitraje":        "BOE-A-2003-23646",

	// Prevención de Riesgos Laborales
	"ley de prevencion de riesgos laborales": "BOE-A-1995-24292",
	"prevencion riesgos laborales":           "BOE-A-1995-24292",
	"lprl":                                   "BOE-A-1995-24292",

	// LOPJ
	"ley organica del poder judicial": "BOE-A-1985-12666",
	"poder judicial":                  "BOE-A-1985-12666",
	"lopj":                            "BOE-A-1985-12666",

	// Ley del Notariado
	"ley del notariado": "BOE-A-1862-4073",
	"notariado":         "BOE-A-1862-4073",

	// Ley de Fundaciones
	"ley de fundaciones": "BOE-A-2002-25180",
	"fundaciones":        "BOE-A-2002-25180",

	// Ley del Suelo
	"ley del suelo": "BOE-A-2015-11723",
	"suelo":         "BOE-A-2015-11723",
	"urbanismo":     "BOE-A-2015-11723",

	// Ley de Sociedades Laborales
	"ley de sociedades laborales": "BOE-A-2015-11071",
	"sociedades laborales":        "BOE-A-2015-11071",

	// Ley de Cooperativas
	"ley de cooperativas": "BOE-A-1999-15681",
	"cooperativas":        "BOE-A-1999-15681",

	// Sociedades (generic → LSC as most common)
	"sociedades": "BOE-A-2010-10544",

	// Concurso de acreedores
	"concurso de acreedores": "BOE-A-2020-4859",
	"concurso acreedores":    "BOE-A-2020-4859",

	// Hipoteca → Ley Hipotecaria
	"hipoteca":  "BOE-A-1946-2453",
	"hipotecas": "BOE-A-1946-2453",

	// Vivienda → Ley de Vivienda 2023
	"vivienda": "BOE-A-2023-12203",

	// Telecomunicaciones
	"telecos": "BOE-A-2022-10757",

	// Ley de Competencia Desleal
	"ley de competencia desleal": "BOE-A-1991-628",
	"competencia desleal":        "BOE-A-1991-628",
	"lcd":                        "BOE-A-1991-628",

	// Ley de Prevención de Blanqueo de Capitales
	"ley de prevencion del blanqueo de capitales": "BOE-A-2010-6737",
	"ley de blanqueo de capitales":                "BOE-A-2010-6737",
	"blanqueo de capitales":                       "BOE-A-2010-6737",
	"blanqueo capitales":                          "BOE-A-2010-6737",
	"prevencion blanqueo":                         "BOE-A-2010-6737",

	// Reglamento del Registro Mercantil
	"reglamento del registro mercantil": "BOE-A-1996-17533",
	"registro mercantil":                "BOE-A-1996-17533",
	"rrm":                               "BOE-A-1996-17533",

	// Ley del Impuesto sobre Sucesiones y Donaciones
	"ley del impuesto sobre sucesiones y donaciones": "BOE-A-1987-28141",
	"impuesto sucesiones":                            "BOE-A-1987-28141",
	"sucesiones y donaciones":                        "BOE-A-1987-28141",
	"isd":                                            "BOE-A-1987-28141",

	// Ley del Impuesto sobre Transmisiones Patrimoniales
	"ley del impuesto sobre transmisiones patrimoniales": "BOE-A-1993-25359",
	"transmisiones patrimoniales":                        "BOE-A-1993-25359",
	"itp":                                                "BOE-A-1993-25359",
	"itpajd":                                             "BOE-A-1993-25359",

	// Ley Reguladora de la Jurisdicción Contencioso-Administrativa
	"ley de la jurisdiccion contencioso administrativa": "BOE-A-1998-16718",
	"contencioso administrativo":                        "BOE-A-1998-16718",
	"ljca":                                              "BOE-A-1998-16718",

	// Ley de Propiedad Industrial (Patentes + Marcas ya están, pero añadimos el concepto)
	"propiedad industrial": "BOE-A-2015-8328",

	// Ley General de Telecomunicaciones
	"ley general de telecomunicaciones": "BOE-A-2022-10757",
	"telecomunicaciones":                "BOE-A-2022-10757",

	// Ley de Ordenación de la Edificación
	"ley de ordenacion de la edificacion": "BOE-A-1999-21567",
	"ordenacion edificacion":              "BOE-A-1999-21567",
	"loe":                                 "BOE-A-1999-21567",

	// Ley de Vivienda
	"ley de vivienda":     "BOE-A-2023-12203",
	"ley por el derecho a la vivienda": "BOE-A-2023-12203",

	// Ley de Regulación del Mercado Hipotecario
	"ley del mercado hipotecario": "BOE-A-1981-7986",
	"mercado hipotecario":         "BOE-A-1981-7986",

	// Ley de Crédito Inmobiliario
	"ley de credito inmobiliario":                      "BOE-A-2019-3814",
	"credito inmobiliario":                             "BOE-A-2019-3814",
	"ley reguladora de los contratos de credito inmobiliario": "BOE-A-2019-3814",

	// Ley de Auditoría de Cuentas
	"ley de auditoria de cuentas": "BOE-A-2015-8147",
	"auditoria de cuentas":        "BOE-A-2015-8147",
	"lac":                         "BOE-A-2015-8147",

	// Ley de Registro Civil
	"ley de registro civil": "BOE-A-2011-12628",
	"registro civil":        "BOE-A-2011-12628",

	// Ley de Extranjería
	"ley de extranjeria":                                "BOE-A-2000-544",
	"extranjeria":                                       "BOE-A-2000-544",

	// Ley General de la Seguridad Social
	"ley general de la seguridad social": "BOE-A-2015-11724",
	"seguridad social":                   "BOE-A-2015-11724",
	"lgss":                               "BOE-A-2015-11724",

	// Ley Reguladora de las Haciendas Locales
	"ley de haciendas locales":     "BOE-A-2004-4214",
	"haciendas locales":            "BOE-A-2004-4214",

	// Ley de Régimen Jurídico del Sector Público
	"ley de regimen juridico del sector publico": "BOE-A-2015-10566",
	"regimen juridico sector publico":            "BOE-A-2015-10566",
	"lrjsp":                                      "BOE-A-2015-10566",

	// Ley del Procedimiento Administrativo Común
	"ley del procedimiento administrativo comun": "BOE-A-2015-10565",
	"procedimiento administrativo":               "BOE-A-2015-10565",
	"lpac":                                       "BOE-A-2015-10565",
}

// Synonyms maps colloquial/common terms to their legal equivalents for better title matching
var Synonyms = map[string]string{
	"alquiler":             "arrendamientos urbanos",
	"alquileres":           "arrendamientos urbanos",
	"arrendamiento":        "arrendamientos urbanos",
	"inquilino":            "arrendamientos urbanos",
	"hipotecas":            "hipotecaria",
	"despido":              "estatuto trabajadores",
	"despidos":             "estatuto trabajadores",
	"contrato trabajo":     "estatuto trabajadores",
	"trabajador":           "estatuto trabajadores",
	"trabajadores":         "estatuto trabajadores",
	"herencia":             "codigo civil sucesiones",
	"herencias":            "codigo civil sucesiones",
	"testamento":           "codigo civil sucesiones",
	"divorcio":             "codigo civil matrimonio",
	"pension alimenticia":  "codigo civil alimentos",
	"delito":               "codigo penal",
	"delitos":              "codigo penal",
	"delito fiscal":        "codigo penal tributario",
	"impuestos":            "general tributaria",
	"hacienda":             "general tributaria",
	"autonomo":             "seguridad social autonomos",
	"autonomos":            "seguridad social autonomos",
	"quiebra":              "concursal",
	"registro mercantil":   "registro mercantil",
	"marcas patentes":      "propiedad industrial",
	"competencia desleal":  "competencia desleal",
	"blanqueo":             "blanqueo capitales",
	"lavado dinero":        "blanqueo capitales",
	"proteccion consumidor": "consumidores usuarios",
	"consumidor":           "consumidores usuarios",
	"privacidad":           "proteccion datos",
	"accidente laboral":    "prevencion riesgos laborales",
	"prevencion riesgos":   "prevencion riesgos laborales",
	"urbanismo":            "suelo urbanismo",
	"contrato publico":     "contratos sector publico",
	"contratacion publica": "contratos sector publico",
	"licitacion":           "contratos sector publico",
	"inmigracion":          "extranjeria",
	"visado":               "extranjeria",
	"residencia":           "extranjeria",
	"sociedad limitada":    "sociedades capital",
	"sociedad anonima":     "sociedades capital",
	"sl":                   "sociedades capital",
	"sa":                   "sociedades capital",
}

// ExpandSynonyms checks if the query has a known synonym and returns the expanded version
func ExpandSynonyms(query string) (string, bool) {
	normalized := normalizeForAlias(query)
	if expanded, ok := Synonyms[normalized]; ok {
		return expanded, true
	}
	return query, false
}

// StopWords are common Spanish words to remove from search queries
var StopWords = map[string]bool{
	"ley": true, "real": true, "decreto": true, "legislativo": true,
	"organica": true, "de": true, "del": true, "la": true, "el": true,
	"los": true, "las": true, "por": true, "que": true, "se": true,
	"en": true, "y": true, "a": true, "para": true, "sobre": true,
	"con": true, "al": true, "un": true, "una": true, "lo": true,
	"texto": true, "refundido": true, "aprueba": true,
}

// normalizeForAlias strips accents, lowercases, and trims for alias matching
func normalizeForAlias(s string) string {
	s = strings.ToLower(strings.TrimSpace(s))
	// Strip accents
	var result []rune
	for _, r := range norm.NFD.String(s) {
		if !unicode.Is(unicode.Mn, r) { // Mn = nonspacing marks (accents)
			result = append(result, r)
		}
	}
	// Collapse multiple spaces
	return strings.Join(strings.Fields(string(result)), " ")
}

// LookupAlias checks if the query matches a known law alias
func LookupAlias(query string) (string, bool) {
	normalized := normalizeForAlias(query)
	if id, ok := KnownLaws[normalized]; ok {
		return id, true
	}
	return "", false
}

// RemoveStopWords strips common Spanish stop words from a query
func RemoveStopWords(input string) string {
	words := strings.Fields(strings.ToLower(input))
	var kept []string
	for _, w := range words {
		normalized := normalizeForAlias(w)
		if !StopWords[normalized] {
			kept = append(kept, w)
		}
	}
	if len(kept) == 0 {
		// Don't return empty — fall back to original minus very basic articles
		basicStop := map[string]bool{"de": true, "del": true, "la": true, "el": true, "los": true, "las": true}
		for _, w := range words {
			if !basicStop[w] {
				kept = append(kept, w)
			}
		}
	}
	return strings.Join(kept, " ")
}
