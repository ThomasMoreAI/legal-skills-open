# Regras de Validação e HITL Triggers

Implementado em `modules/extraction.py` (`ValidadorSentenca`, `_validar_e_completar`)
e `webapp.py` (pré-verificações antes de iniciar automação).

---

## ValidadorSentenca — API

```python
from modules.extraction import ValidadorSentenca

resultado = ValidadorSentenca(dados).validar()
# resultado.valido   → bool
# resultado.erros    → list[str]  (bloqueantes)
# resultado.avisos   → list[str]  (não bloqueantes)
```

---

## Erros bloqueantes (impedem automação)

| Campo | Regra |
|---|---|
| `processo.estado` | Obrigatório e não vazio |
| `contrato.admissao` | Obrigatório, formato DD/MM/AAAA |
| `contrato.ultima_remuneracao` | Obrigatório, > 0 |
| `contrato.demissao` | Se informado: deve ser > admissao |
| `contrato.ajuizamento` | Se informado: deve ser >= demissao |
| IA indisponível | `_erro_ia=True` → status="erro_ia", processamento bloqueado |

---

## Avisos (não bloqueantes — mostram alerta mas não impedem)

| Trigger | Condição | Ação |
|---|---|---|
| HITL 1 | confidence médio < 0.7 | Sugere revisão geral |
| HITL 2 | Campo crítico com confidence < 0.7 (admissão, remuneração, estado) | Destaca campo |
| HITL 3 | `campos_ausentes` não vazio | Lista campos obrigatórios ausentes |
| HITL 4 | tipo_rescisao × verbas incompatíveis | Ex: justa causa + aviso prévio |
| HITL 5 | > 3 verbas não mapeáveis | Sugere classificação manual |
| HITL 6 | `honorarios` vazio mas relatório menciona honorários | Alerta extração falhou |
| HITL 7 | `historico_salarial` vazio | Alerta histórico ausente |
| HITL 8 | `ferias` vazio mas sentença menciona férias | Alerta períodos não capturados |
| CNJ | Dígito verificador módulo 97 inválido | Log + aviso no SSE (não bloqueia) |

---

## Matriz de compatibilidade — tipo_rescisao × verbas

| Tipo de Rescisão | Aviso Prévio | Multa FGTS 40% | Seguro Desemprego |
|---|---|---|---|
| sem_justa_causa | ✓ | ✓ | ✓ |
| justa_causa | ✗ | ✗ | ✗ |
| pedido_demissao | ✗ | ✗ | ✗ |
| rescisao_indireta | ✓ | ✓ | ✓ |
| distrato | ✗ (parcial) | ✗ (20%) | ✗ |
| morte | N/A | ✓ | N/A |
| culpa_reciproca | ✗ (50%) | ✗ (20%) | ✗ |

---

## Validação CNJ módulo 97

```python
def _validar_cnj(numero_seq: str, digito: str, ano: str, regiao: str, vara: str) -> bool:
    """
    Fórmula CNJ Res. 65/2008:
    Montar: NNNNNNN + "00" + AAAA + "5" + TT + OOOO
    Calcular: resto = int(numero) % 97
    Dígito correto: 97 - resto
    """
    try:
        num = numero_seq + "00" + ano + "5" + regiao + vara
        resto = int(num) % 97
        return int(digito) == (97 - resto)
    except Exception:
        return True  # não bloquear se dados inválidos
```

Segmento "5" = Justiça do Trabalho (fixo).
O aviso CNJ é não bloqueante — o número pode estar correto no PJE-Calc mesmo que a
validação falhe (OCR pode ter capturado dígito errado).

---

## Pré-verificações em webapp.py (antes de iniciar Playwright)

Executadas na ordem em `executar_automacao_sse()`:

```python
# 1. Sessão existe
calculo = repo.buscar_por_sessao(sessao_id)
if not calculo:
    yield "data: ERRO_EXPORTAVEL::Sessão não encontrada\n\n"
    return

# 2. Lock — impede execuções paralelas
if sessao_id in _sessoes_automacao:
    yield "data: ERRO_EXPORTAVEL::Automação já em andamento\n\n"
    return

# 3. Prévia confirmada
if not calculo.confirmado_em:
    yield "data: ERRO_EXPORTAVEL::Prévia não confirmada\n\n"
    return

# 4. Validação dos dados
resultado = ValidadorSentenca(dados).validar()
if not resultado.valido:
    erros = "; ".join(resultado.erros[:3])
    yield f"data: ERRO_EXPORTAVEL::Validação falhou: {erros}\n\n"
    return

# 5. CNJ (aviso não bloqueante)
if _cnj_invalido:
    yield f"data: {json.dumps({'msg': '⚠ CNJ: dígito inválido — verifique o número'})}\n\n"

# 6. PJe-Calc disponível (polling até 600s — Tomcat pode demorar para subir)
# → aguarda localhost:9257 responder antes de iniciar Playwright
```
