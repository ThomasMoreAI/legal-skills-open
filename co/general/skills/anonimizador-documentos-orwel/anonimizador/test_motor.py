"""Pruebas del motor v6 — solo datos ficticios, sin información real de clientes."""

from motor_anonimizacion import MotorAnonimizacion

# Empresa ficticia para pruebas de sufijos societarios compuestos
EMPRESA_FICTICIA = "SERVIGAS DEL NORTE S.A. E.S.P."
EMPRESA_VARIANTES = (
    f"{EMPRESA_FICTICIA} comenzó a cobrar. "
    "Ante reclamaciones, Servigas del Norte S.A. ESP recibió la solicitud. "
    "La empresa servigas del norte s.a. e.s.p. respondió negativamente."
)


def anonimizar(texto: str) -> str:
    motor = MotorAnonimizacion()
    hallazgos = motor.analizar(texto)
    return motor.aplicar(texto, hallazgos)


def test_empresa_societaria_en_todas_variantes():
    resultado = anonimizar(EMPRESA_VARIANTES)
    assert "SERVIGAS" not in resultado.upper()
    assert "S.A." not in resultado or "[EMPRESA" in resultado
    assert "E.S.P." not in resultado or "[EMPRESA" in resultado
    assert resultado.count("[EMPRESA_1]") == 3


def test_otra_empresa_distinta():
    """Cualquier empresa con sufijo societario, no una hardcodeada."""
    for nombre in [
        "CONSTRUCTORA EL PUENTE S.A.S.",
        "INVERSIONES ACME LTDA.",
        "COMERCIALIZADORA BETA S.A.",
        "ENERGÍA DEL VALLE S.A. E.S.P.",
    ]:
        resultado = anonimizar(f"La demanda contra {nombre} fue admitida.")
        raiz = nombre.split()[0]
        assert raiz not in resultado
        assert "[EMPRESA_" in resultado


def test_no_destruye_saldo():
    texto = "la eliminación total del saldo restante exigido y la financiación"
    resultado = anonimizar(texto)
    assert "saldo" in resultado.lower()
    assert "[EMPRESA" not in resultado


def test_cuenta_contrato():
    texto = "cobradas a la cuenta contrato No. 12345678, por ausencia de consentimiento"
    resultado = anonimizar(texto)
    assert "12345678" not in resultado
    assert "cuenta contrato" in resultado.lower()


def test_tarjeta_profesional_numero_no_palabras():
    texto = "identificado con Tarjeta Profesional No. 98765432 del Consejo Superior"
    resultado = anonimizar(texto)
    assert "98765432" not in resultado
    assert "Tarjeta Profesional" in resultado or "tarjeta profesional" in resultado.lower()


def test_no_anonimiza_corte_ni_codigo_civil():
    texto = "La Corte Constitucional aplicó el Código Civil según Ley 1564 de 2012"
    resultado = anonimizar(texto)
    assert "Corte Constitucional" in resultado
    assert "Código Civil" in resultado
    assert "1564" in resultado


def test_esp_no_queda_suelto():
    texto = f"La presente reclamación ante {EMPRESA_FICTICIA} se pronuncie"
    resultado = anonimizar(texto)
    assert "SERVIGAS" not in resultado.upper()
    assert "E.S.P." not in resultado
    assert "[EMPRESA_1]" in resultado


def test_cedula_variantes():
    for variante in [
        "CC 1.023.456.789",
        "c.c. 1023456789",
        "Cédula de Ciudadanía No. 1.023.456.789",
    ]:
        resultado = anonimizar(f"identificado con {variante}")
        assert "1.023.456.789" not in resultado
        assert "1023456789" not in resultado


def test_telefono_pegado_sin_separadores():
    """Caso real: celular de 10 dígitos pegado tras la palabra teléfono."""
    texto = "Comuníquese al teléfono 3001234567 o al correo ficticio@ejemplo.com"
    resultado = anonimizar(texto)
    assert "3001234567" not in resultado
    assert "[TELÉFONO" in resultado


def test_telefono_whatsapp():
    texto = "escribir por WhatsApp 6012345678 para más información"
    resultado = anonimizar(texto)
    assert "6012345678" not in resultado


def test_propagacion_apellido():
    texto = (
        "La señora Ana María López presentó la demanda. "
        "Posteriormente, López solicitó la reposición del acto."
    )
    resultado = anonimizar(texto)
    assert "López" not in resultado
    assert "[PERSONA_" in resultado


def test_nit_invalido_no_se_etiqueta_como_nit():
    """Formato NIT con DV incorrecto no debe clasificarse como NIT."""
    texto = "referencia interna 123.456.789-0 sin validez tributaria"
    motor = MotorAnonimizacion()
    hallazgos = motor.analizar(texto)
    assert not any(h.tipo == "NIT" for h in hallazgos)


def test_nombre_contexto_senor():
    """Caso real: nombre tras 'el señor' (ficticio)."""
    texto = (
        "El 4 de marzo de 2024, el señor Julián Romero, empleado de la firma "
        "designada por SERVIGAS DEL NORTE S.A. E.S.P., informó de manera verbal."
    )
    resultado = anonimizar(texto)
    assert "Julián" not in resultado
    assert "Romero" not in resultado
    assert "[PERSONA_" in resultado


def test_telefono_en_parrafo_separado():
    """Teléfono en línea distinta al prefijo (como en Word)."""
    motor = MotorAnonimizacion()
    texto_completo = "Comuníquese al teléfono\n3001234567 para más información."
    hallazgos = motor.analizar(texto_completo)
    parrafo_numero = "3001234567"
    resultado = motor.aplicar(parrafo_numero, hallazgos)
    assert "3001234567" not in resultado
    assert "[TELÉFONO" in resultado


def test_personas_unificadas_mismo_alias():
    texto = (
        "El señor Carlos Mendoza presentó la demanda. "
        "Posteriormente Mendoza solicitó la reposición. "
        "Carlos Mendoza compareció ante el juzgado."
    )
    motor = MotorAnonimizacion()
    hallazgos = motor.analizar(texto)
    personas = [h for h in hallazgos if h.tipo == "PERSONA"]
    assert len(personas) == 1
    resultado = motor.aplicar(texto, hallazgos)
    assert "Mendoza" not in resultado
    assert "Carlos" not in resultado or "[PERSONA_" in resultado


def test_apellido_geografico_no_es_publico():
    """Córdoba como apellido debe anonimizarse (no confundir con departamento)."""
    texto = "El señor Pedro Córdoba presentó escrito de tutela."
    resultado = anonimizar(texto)
    assert "Córdoba" not in resultado


def test_denuncia_nombre_mayusculas_suscrito():
    """Caso real: nombre en MAYÚSCULAS tras 'El suscrito' en denuncia penal."""
    texto = (
        "I. IDENTIFICACIÓN DEL DENUNCIANTE\n"
        "El suscrito JUAN DAVID VANEGAS ROLDÁN, mayor de edad, identificado con "
        "cédula de ciudadanía No. 1.234.567.890, domiciliado en la ciudad de Bogotá, "
        "abogado en ejercicio con Tarjeta Profesional No. 123456 del Consejo Superior "
        "de la Judicatura, actuando en nombre propio, presenta DENUNCIA PENAL."
    )
    resultado = anonimizar(texto)
    assert "JUAN" not in resultado
    assert "VANEGAS" not in resultado
    assert "ROLDÁN" not in resultado and "ROLDAN" not in resultado
    assert "[PERSONA_" in resultado
    assert "Consejo Superior" in resultado or "CONSEJO" in resultado.upper()


def test_parrafo_reclamacion_ficticio():
    texto = (
        f"La presente reclamación ante {EMPRESA_FICTICIA} se pronuncie mediante acto "
        "administrativo de fondo sobre: la inexistencia e inexigibilidad de las "
        "obligaciones cobradas a la cuenta contrato No. 12345678, por ausencia de "
        "consentimiento válido; la eliminación total del saldo restante exigido y la "
        "financiación que continúa apareciendo en los recibos."
    )
    resultado = anonimizar(texto)
    assert "SERVIGAS" not in resultado.upper()
    assert "12345678" not in resultado
    assert "saldo" in resultado.lower()
    assert "E.S.P." not in resultado


if __name__ == "__main__":
    tests = [
        test_empresa_societaria_en_todas_variantes,
        test_otra_empresa_distinta,
        test_no_destruye_saldo,
        test_cuenta_contrato,
        test_tarjeta_profesional_numero_no_palabras,
        test_no_anonimiza_corte_ni_codigo_civil,
        test_esp_no_queda_suelto,
        test_cedula_variantes,
        test_telefono_pegado_sin_separadores,
        test_telefono_whatsapp,
        test_propagacion_apellido,
        test_nit_invalido_no_se_etiqueta_como_nit,
        test_nombre_contexto_senor,
        test_telefono_en_parrafo_separado,
        test_personas_unificadas_mismo_alias,
        test_apellido_geografico_no_es_publico,
        test_denuncia_nombre_mayusculas_suscrito,
        test_parrafo_reclamacion_ficticio,
    ]
    fallos = 0
    for t in tests:
        try:
            t()
            print(f"OK  {t.__name__}")
        except AssertionError as e:
            fallos += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"\n{len(tests) - fallos}/{len(tests)} pruebas pasaron")
    raise SystemExit(1 if fallos else 0)
