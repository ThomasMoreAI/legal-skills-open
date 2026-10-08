"""
lgpd_compliance/pii.py, decorator e helpers de anotação PII
==========================================================
Skill: lgpd-compliance (Parte 3)

Cole em: app/lgpd_compliance/pii.py (ou similar) e importe nos modelos.

Uso:
    from lgpd_compliance.pii import pii, contains_pii, PII

    @contains_pii
    class User(Base):
        @pii(finalidade=["autenticacao"], base_legal="art_7_V_contrato",
             retencao="conta+5y", sensibilidade="baixa")
        email: Mapped[str] = mapped_column(String(255))

    # Ou em Pydantic
    class UserSchema(BaseModel):
        email: Annotated[str, PII(finalidade=["autenticacao"], ...)]

O script gerar-inventario.py consome essas anotações via reflection.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Literal


# === Constantes ============================================================

BASES_LEGAIS_VALIDAS = {
    # Art. 7º, dados comuns
    "art_7_I_consentimento",
    "art_7_II_obrigacao_legal",
    "art_7_III_politicas_publicas",
    "art_7_IV_pesquisa",
    "art_7_V_contrato",
    "art_7_VI_processo",
    "art_7_VII_protecao_vida",
    "art_7_VIII_tutela_saude",
    "art_7_IX_legitimo_interesse",
    "art_7_X_credito",
    # Art. 11, dados sensíveis
    "art_11_I_consentimento_sensivel",
    "art_11_II_a_obrigacao_legal_sensivel",
    "art_11_II_b_politicas_publicas_sensivel",
    "art_11_II_c_pesquisa_sensivel",
    "art_11_II_d_processo_sensivel",
    "art_11_II_e_protecao_vida_sensivel",
    "art_11_II_f_tutela_saude_sensivel",
    "art_11_II_g_prevencao_fraude_sensivel",
}

SENSIBILIDADES_VALIDAS = {
    "baixa",
    "media",
    "alta",
    "critica",
    "variavel",
    "alta_inferencia",
}

Sensibilidade = Literal[
    "baixa", "media", "alta", "critica", "variavel", "alta_inferencia"
]


# === Estrutura canônica ====================================================

@dataclass
class PII:
    """Metadado LGPD anexado a um campo ou classe."""

    finalidade: list[str]
    base_legal: str
    retencao: str
    sensibilidade: Sensibilidade
    compartilha_com: list[str] = field(default_factory=list)
    visivel_para: list[str] = field(default_factory=list)
    criptografia_repouso: str | None = None
    obrigatorio: bool = True
    observacao: str | None = None

    def __post_init__(self) -> None:
        if self.base_legal not in BASES_LEGAIS_VALIDAS:
            raise ValueError(
                f"base_legal inválida: {self.base_legal!r}. "
                f"Válidas: {sorted(BASES_LEGAIS_VALIDAS)}"
            )
        if self.sensibilidade not in SENSIBILIDADES_VALIDAS:
            raise ValueError(
                f"sensibilidade inválida: {self.sensibilidade!r}. "
                f"Válidas: {sorted(SENSIBILIDADES_VALIDAS)}"
            )
        if not self.finalidade:
            raise ValueError("finalidade não pode ser lista vazia")


# === Decorators =============================================================

def pii(**kwargs: Any) -> Callable[[Any], Any]:
    """
    Decorator que anexa metadado PII a um campo (atributo de classe SQLAlchemy,
    coluna Drizzle/Prisma transpilada, etc.).

    O metadado vira atributo `_pii` no objeto decorado, consumido por
    gerar-inventario.py via reflection.

    Não tem efeito em runtime além de marcar, é puro metadado.
    """
    meta = PII(**kwargs)

    def _decorator(obj: Any) -> Any:
        setattr(obj, "_pii", meta)
        return obj

    return _decorator


def contains_pii(cls: type) -> type:
    """
    Marca uma classe/tabela como contendo PII. O CI verifica que todos os
    atributos públicos têm @pii ou @no_pii.
    """
    setattr(cls, "_contains_pii", True)
    return cls


def no_pii(obj: Any) -> Any:
    """Marca explicitamente um campo como NÃO sendo PII (FK opaca, timestamp etc.)."""
    setattr(obj, "_no_pii", True)
    return obj


# === Helpers pra extração (usados por gerar-inventario.py) ================

def extrair_pii_de_classe(cls: type) -> dict[str, PII]:
    """
    Inspeciona uma classe e retorna {nome_do_campo: PII} pra cada atributo
    anotado com @pii.
    """
    resultado: dict[str, PII] = {}
    for nome in dir(cls):
        if nome.startswith("_"):
            continue
        attr = getattr(cls, nome, None)
        meta = getattr(attr, "_pii", None)
        if isinstance(meta, PII):
            resultado[nome] = meta
    return resultado


def validar_classe_contains_pii(cls: type) -> list[str]:
    """
    Retorna lista de campos da classe que estão sem anotação @pii nem @no_pii.
    Falha do CI se a classe é @contains_pii e essa lista não está vazia.
    """
    if not getattr(cls, "_contains_pii", False):
        return []

    faltando: list[str] = []
    for nome in dir(cls):
        if nome.startswith("_"):
            continue
        attr = getattr(cls, nome, None)
        if attr is None or callable(attr):
            continue
        if getattr(attr, "_pii", None) is not None:
            continue
        if getattr(attr, "_no_pii", False):
            continue
        faltando.append(nome)
    return faltando
