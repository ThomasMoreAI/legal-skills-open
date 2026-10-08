# Automação Playwright — PJE-Calc Cidadão

Este arquivo documenta seletores, estratégias e armadilhas para automação do PJE-Calc Cidadão via Playwright (Python), com base na estrutura da aplicação JSF/RichFaces rodando em Tomcat.

> **IMPORTANTE (abril/2026):** Usar **Firefox** (`pw.firefox.launch()`), não Chromium. O PJE-Calc é
> desenvolvido para Firefox e RichFaces gera HTML com quirks específicos para Gecko. Chromium causa
> incompatibilidades em eventos AJAX, calendários RichFaces e popups JSF.

> **ARQUIVO .PJC:** O gerador nativo (`pjc_generator.py`) produz templates pré-liquidação que o PJE-Calc
> **rejeita** na importação. Sempre usar o fluxo: Preencher → Liquidar → Exportar (via PJE-Calc).

> **BOTÃO MANUAL:** Para criar verbas manuais na página de verbas, clicar `id="incluir"` (value="Manual"),
> NÃO o botão "Novo" (que cria um novo cálculo). Após criar, preencher `caracteristica`, `ocorrencia`
> e `base_calculo` obrigatoriamente — sem eles a liquidação falha com HTTP 500.

---

## Arquitetura da Aplicação

| Característica | Detalhe |
|---|---|
| Framework frontend | JSF 1.2 + RichFaces 3.x |
| Servidor | Apache Tomcat 6 (versão desktop) |
| Banco de dados | H2 (embedded) |
| URL padrão | `http://localhost:8080/pje-calc` |
| Autenticação | Sem certificado digital na versão desktop (login por usuário/senha) |
| Renderização | Server-side rendering; AJAX parcial via RichFaces a4j |

---

## Estratégias Gerais

### 1. Aguardar Respostas AJAX

O RichFaces usa AJAX para atualizar partes da página. Após clicar em botões como **Salvar**, **Gerar Ocorrências**, **Regerar**, **Adicionar** e **Liquidar**, aguardar:

```python
# Aguardar que o indicador de loading desapareça
page.wait_for_selector("#ajaxLoadingPanel", state="hidden", timeout=30000)

# Ou aguardar que um elemento específico apareça/desapareça
page.wait_for_load_state("networkidle", timeout=30000)
```

### 2. Navegação pelo Menu Lateral

O menu lateral usa links com IDs previsíveis baseados no nome da página:

```python
# Padrão de seletor para itens do menu lateral
menu_items = {
    "dados_calculo":       "a[id*='menuCalculo']",
    "faltas":              "a[id*='menuFaltas']",
    "ferias":              "a[id*='menuFerias']",
    "historico_salarial":  "a[id*='menuHistoricoSalarial']",
    "verbas":              "a[id*='menuVerbas']",
    "cartao_ponto":        "a[id*='menuCartaoPonto']",
    "salario_familia":     "a[id*='menuSalarioFamilia']",
    "seguro_desemprego":   "a[id*='menuSeguroDesemprego']",
    "fgts":                "a[id*='menuFGTS']",
    "contribuicao_social": "a[id*='menuContribuicaoSocial']",
    "prev_privada":        "a[id*='menuPrevidenciaPrivada']",
    "pensao_alimenticia":  "a[id*='menuPensaoAlimenticia']",
    "imposto_renda":       "a[id*='menuImpostoRenda']",
    "multas":              "a[id*='menuMultas']",
    "honorarios":          "a[id*='menuHonorarios']",
    "custas":              "a[id*='menuCustas']",
    "correcao_juros":      "a[id*='menuCorrecaoJuros']",
    "liquidar":            "a[id*='menuLiquidar']",
    "imprimir":            "a[id*='menuImprimir']",
}
```

### 3. Campos de Data

O PJE-Calc usa campos de texto simples para datas no formato `dd/mm/aaaa`:

```python
def fill_date(page, selector, date_str):
    """date_str no formato dd/mm/aaaa"""
    field = page.locator(selector)
    field.clear()
    field.fill(date_str)
    field.press("Tab")  # Dispara validação do campo
```

### 4. Campos de Valor Monetário

Usar ponto ou vírgula como separador decimal conforme o locale da aplicação (padrão: vírgula):

```python
def fill_money(page, selector, value: float):
    """value como float; converte para string com vírgula"""
    formatted = f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    # Resultado: 1.234,56
    field = page.locator(selector)
    field.clear()
    field.fill(formatted)
```

### 5. Checkboxes

```python
def set_checkbox(page, selector, should_be_checked: bool):
    checkbox = page.locator(selector)
    if checkbox.is_checked() != should_be_checked:
        checkbox.click()
```

### 6. Selects (dropdowns)

```python
def select_option_by_text(page, selector, text):
    page.locator(selector).select_option(label=text)
    page.wait_for_load_state("networkidle")
```

---

## Mapeamento de Páginas e Seletores

### Página: Parâmetros do Cálculo

```python
PARAMETROS = {
    "estado":           "select[id*='estado']",
    "municipio":        "select[id*='municipio']",
    "admissao":         "input[id*='admissao']",
    "demissao":         "input[id*='demissao']",
    "ajuizamento":      "input[id*='ajuizamento']",
    "data_inicial":     "input[id*='dataInicial']",
    "data_final":       "input[id*='dataFinal']",
    "maior_remuneracao":"input[id*='maiorRemuneracao']",
    "ultima_remuneracao":"input[id*='ultimaRemuneracao']",
    "carga_horaria":    "input[id*='cargaHoraria']",
    "regime_trabalho":  "select[id*='regimeTrabalho']",
    "prazo_aviso":      "select[id*='prazoAvisoPrevio']",
    "btn_salvar":       "input[id*='btnSalvar'], button[id*='btnSalvar']",
}
```

### Página: Faltas

```python
FALTAS = {
    "data_inicial":     "input[id*='falta:dataInicial']",
    "data_final":       "input[id*='falta:dataFinal']",
    "justificada":      "input[type='checkbox'][id*='faltaJustificada']",
    "justificativa":    "input[id*='justificativa']",
    "btn_salvar":       "input[id*='btnSalvarFalta']",
}
```

### Página: Histórico Salarial

```python
HISTORICO = {
    "btn_novo":         "input[id*='btnNovoHistorico']",
    "nome":             "input[id*='historico:nome']",
    "incid_fgts":       "input[type='checkbox'][id*='incidenciaFGTS']",
    "incid_cs":         "input[type='checkbox'][id*='incidenciaCS']",
    "tipo_valor":       "select[id*='tipoValor']",
    "comp_inicial":     "input[id*='competenciaInicial']",
    "comp_final":       "input[id*='competenciaFinal']",
    "valor":            "input[id*='valorBase']",
    "btn_gerar":        "input[id*='btnGerarOcorrencias']",
    "btn_salvar":       "input[id*='btnSalvarHistorico']",
}
```

### Página: Verbas — Lançamento Expresso

```python
VERBAS_EXPRESSO = {
    "btn_expresso":     "input[id*='btnExpresso']",
    # Checkboxes das verbas: usar texto do label para localizar
    "checkbox_verba":   lambda nome: f"//label[contains(text(), '{nome}')]/preceding-sibling::input[@type='checkbox']",
    "btn_salvar":       "input[id*='btnSalvarExpresso']",
}
```

### Página: FGTS

```python
FGTS_PAGE = {
    "destino":          "select[id*='destinoFGTS']",
    "multa_checkbox":   "input[type='checkbox'][id*='apurarMulta']",
    "multa_tipo":       "select[id*='tipoMulta']",
    "multa_aliquota":   "input[id*='aliquotaMulta']",
    "multa_base":       "select[id*='baseMulta']",
    "saldo_data":       "input[id*='saldoData']",
    "saldo_valor":      "input[id*='saldoValor']",
    "btn_adicionar":    "input[id*='btnAdicionarSaldo']",
    "deduzir_fgts":     "input[type='checkbox'][id*='deduzirFGTS']",
    "btn_salvar":       "input[id*='btnSalvarFGTS']",
}
```

### Página: Liquidar

```python
LIQUIDAR_PAGE = {
    "data_liquidacao":  "input[id*='dataLiquidacao']",
    "acumular_indices": "select[id*='acumularIndices']",
    "btn_liquidar":     "input[id*='btnLiquidar']",
    # Verificar pendências antes de liquidar
    "alertas":          ".alertaLiquidacao, [class*='alerta']",
    "erros":            ".erroLiquidacao, [class*='erro']",
}
```

---

## Armadilhas Comuns

### 1. Campos desabilitados após AJAX

Após selecionar um valor em um select (ex.: Estado → Município), o campo seguinte pode ser carregado via AJAX. Aguardar antes de interagir:

```python
page.locator("select[id*='estado']").select_option(label="Pará")
page.wait_for_selector("select[id*='municipio'] option:not([value=''])", timeout=10000)
```

### 2. Botão Salvar com múltiplos IDs

O PJE-Calc usa IDs dinâmicos gerados pelo JSF (ex.: `j_id123:btnSalvar`). Usar seletores com `*=` (contém) para maior robustez.

### 3. Diálogos de Confirmação (RichFaces Modal)

Alguns botões abrem modais de confirmação. Aguardar o modal e clicar em OK:

```python
# Aguardar modal aparecer
page.wait_for_selector(".rich-modalpanel", state="visible")
# Clicar em OK/Confirmar
page.locator(".rich-modalpanel button:has-text('OK'), .rich-modalpanel input[value='OK']").click()
page.wait_for_selector(".rich-modalpanel", state="hidden")
```

### 4. Regerar Ocorrências

Após alterar Parâmetros da Verba, o sistema marca automaticamente o checkbox de regeração. Verificar e clicar em Regerar:

```python
regerar_checkbox = page.locator("input[type='checkbox'][id*='regerarOcorrencias']")
if regerar_checkbox.is_visible() and regerar_checkbox.is_checked():
    page.locator("input[id*='btnRegerar']").click()
    page.wait_for_load_state("networkidle")
    # Escolher entre Manter ou Sobrescrever
    page.locator("input[id*='opcaoRegerar'][value='manter']").click()
    page.locator("input[id*='btnConfirmarRegerar']").click()
    page.wait_for_load_state("networkidle")
```

### 5. Timeout em Operações Longas

A operação Liquidar pode demorar vários segundos. Usar timeout estendido:

```python
page.locator("input[id*='btnLiquidar']").click()
page.wait_for_selector("[id*='resultadoLiquidacao']", timeout=120000)
```

### 6. Scroll em Páginas Longas

Após "Gerar Ocorrências" no Histórico Salarial, o botão Salvar fica no final da página:

```python
page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
page.locator("input[id*='btnSalvarHistorico']").click()
```

---

## Fluxo de Automação Recomendado

> **ATENÇÃO:** Este é um esqueleto simplificado. A implementação real deve seguir a sequência
> completa do Fluxo Macro (ver `pjecalc-operacional/SKILL.md`), incluindo TODAS as etapas
> intermediárias listadas abaixo. **SALVAR é OBRIGATÓRIO após cada página** — sair sem salvar
> perde todos os dados preenchidos.

```python
from playwright.sync_api import sync_playwright

def preencher_calculo(dados: dict):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)  # headless=True em produção; OBRIGATÓRIO Firefox
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # 1. Acessar o sistema
        page.goto("http://localhost:9257/pjecalc")
        page.wait_for_load_state("networkidle")

        # 2. Novo Cálculo (NUNCA usar "Cálculo Externo" para primeira liquidação)
        page.locator("a[id*='menuNovo']").click()
        page.wait_for_load_state("networkidle")

        # 3. Parâmetros do Cálculo
        # IMPORTANTE: valorCargaHorariaPadrao DEVE ser salvo aqui ANTES de criar Cartão de Ponto
        # Sem ele, clicar "Novo" no Cartão de Ponto causa NPE (HTTP 500)
        preencher_parametros(page, dados["parametros"])
        salvar_e_aguardar(page)  # OBRIGATÓRIO

        # 4. Faltas
        if dados.get("faltas"):
            page.locator("a[id*='menuFaltas']").click()
            for falta in dados["faltas"]:
                lancar_falta(page, falta)
            salvar_e_aguardar(page)  # OBRIGATÓRIO

        # 5. Férias
        if dados.get("ferias"):
            page.locator("a[id*='menuFerias']").click()
            lancar_ferias(page, dados["ferias"])
            salvar_e_aguardar(page)  # OBRIGATÓRIO

        # 6. Histórico Salarial
        page.locator("a[id*='menuHistoricoSalarial']").click()
        for historico in dados["historicos"]:
            lancar_historico(page, historico)
        salvar_e_aguardar(page)  # OBRIGATÓRIO

        # 7. Verbas (Expresso + Manual + Reflexos)
        page.locator("a[id*='menuVerbas']").click()
        lancar_verbas_expresso(page, dados["verbas"])
        salvar_e_aguardar(page)  # OBRIGATÓRIO

        # 8. Cartão de Ponto (se houver jornada)
        # DISTINÇÃO CRÍTICA: "Jornada de Trabalho Padrão" = CONTRATUAL (ex: 8h/dia)
        # Grade de Ocorrências = EFETIVAMENTE PRATICADA (ex: 10h/dia)
        # HE = praticada − padrão. Se preencher padrão com praticada → HE = 0 (ERRO!)
        if dados.get("cartao_ponto"):
            page.locator("a[id*='menuCartaoPonto']").click()
            configurar_cartao_ponto(page, dados["cartao_ponto"])
            salvar_e_aguardar(page)  # OBRIGATÓRIO

        # 9. FGTS
        # SEQUÊNCIA AJAX OBRIGATÓRIA para multa 40%:
        # checkbox multa → AGUARDAR AJAX → tipoDoValorDaMulta=CALCULADA → AGUARDAR AJAX → multaDoFgts=QUARENTA_POR_CENTO
        # Sem AJAX wait, os radios ficam disabled!
        page.locator("a[id*='menuFGTS']").click()
        configurar_fgts(page, dados["fgts"])
        salvar_e_aguardar(page)  # OBRIGATÓRIO

        # 10. Contribuição Social (INSS)
        page.locator("a[id*='menuContribuicaoSocial']").click()
        configurar_contribuicao_social(page, dados.get("contribuicao_social"))
        salvar_e_aguardar(page)  # OBRIGATÓRIO

        # 11. Imposto de Renda
        # 12. Multas e Indenizações
        # 13. Honorários + Custas
        # 14. Correção Monetária e Juros
        # (implementar conforme dados disponíveis, sempre salvando após cada página)

        # 15. Regerar Ocorrências (aba Verbas — se houve alterações nos parâmetros)
        regerar_ocorrencias(page)

        # 16. Liquidar
        page.locator("a[id*='menuLiquidar']").click()
        liquidar(page, dados["data_liquidacao"])

        # 17. Exportar .PJC
        exportar_pjc(page)

        browser.close()
```

---

## Notas sobre a Versão Cidadão vs. Corporativa

| Aspecto | Versão Cidadão (Desktop) | Versão Corporativa (Online) |
|---|---|---|
| Servidor | Tomcat 6 local | JBoss 5 |
| Banco | H2 embedded | Oracle 11g |
| Autenticação | Usuário/senha local | Certificado digital (PJe-JT) |
| Validar cálculo | Não disponível | Disponível |
| Importar do PJe | Não disponível | Disponível |
| Inicialização | Script `iniciarPjeCalc.sh` / `iniciarPjeCalc.bat` | Servidor institucional |
| Porta padrão | 8080 (configurável) | Definida pelo tribunal |

Para automação remota em container Docker, verificar:
1. Se o Tomcat inicializou completamente antes de acessar a URL.
2. Se o banco H2 está acessível (não bloqueado por outro processo).
3. Usar `wait_for_selector` com timeout generoso na primeira carga.
