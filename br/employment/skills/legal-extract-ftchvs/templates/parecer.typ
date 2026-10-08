// PARECER JURÍDICO — Typst Template
// Usage: typst compile --root / --input data-path="/absolute/path/data/caso.json" parecer.typ parecer.pdf

#set document(
  title: "Parecer Jurídico",
  author: "Legal Extract",
)

#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2cm, left: 2.5cm, right: 2cm),
  header: align(right, text(8pt, fill: luma(150))[Parecer Jurídico — Processo Judicial],),
  footer: context [
    #align(center, text(8pt, fill: luma(150))[
      Página #counter(page).display("1") de #counter(page).final().first()
    ])
  ],
)

#set text(
  font: "New Computer Modern",
  size: 11pt,
  lang: "pt",
  region: "br",
)

#set par(justify: true, leading: 0.7em)
#set heading(numbering: none)

// Load case data from JSON
#let data-path = sys.inputs.at("data-path", default: "data/caso.json")
#let d = json(data-path)

// Helper: format Brazilian currency
#let brl(value) = {
  if value == none { return "N/A" }
  let s = str(calc.round(float(value), digits: 2))
  let parts = s.split(".")
  let inteiro = parts.at(0)
  let decimal = if parts.len() > 1 { parts.at(1) } else { "00" }
  if decimal.len() == 1 { decimal = decimal + "0" }
  // Add thousand separators
  let digits = inteiro.clusters()
  let formatted = ""
  for (i, ch) in digits.rev().enumerate() {
    if i > 0 and calc.rem(i, 3) == 0 { formatted = "." + formatted }
    formatted = ch + formatted
  }
  [R\$ #formatted,#decimal]
}

// Helper: get nested value safely
#let get(obj, ..keys) = {
  let result = obj
  for key in keys.pos() {
    if result == none { return none }
    if type(result) == dictionary and key in result { result = result.at(key) }
    else { return none }
  }
  result
}

// ============================================================
// TITLE
// ============================================================

#align(center, text(16pt, weight: "bold")[PARECER JURÍDICO])
#v(0.5cm)

#grid(
  columns: (1fr,),
  row-gutter: 0.3em,
  [*Data:* #d.meta.data_extracao.slice(0, 10)],
  [*Status:* APROVADO],
  [*Responsável:* #get(d, "processo", "advogados").at(0).nome -- #get(d, "processo", "advogados").at(0).oab],
)

#v(0.5cm)
#line(length: 100%, stroke: 0.5pt + luma(200))
#v(0.3cm)

// ============================================================
// 1. PARTES E REPRESENTAÇÃO
// ============================================================

#heading(level: 2)[1. Partes e Representação]

#let autor = get(d, "processo", "partes", "autor")
#let reu = get(d, "processo", "partes", "reu")
#let advs = get(d, "processo", "advogados")

*Autor:* #get(autor, "nome") (CPF: #get(autor, "cpf")) \
*Cedente:* #advs.at(0).nome (#advs.at(0).oab, CPF: #get(advs.at(0), "cpf")) \
*Réu:* #get(reu, "nome") #if get(reu, "cnpj") != none [(CNPJ: #get(reu, "cnpj"))]

#v(0.3em)

#if d.at("calculos_liquidacao", default: none) != none [
  *Honorários Advocatícios Sucumbenciais:* Fixados nos termos do art. 85, §§3º e 4º, II, CPC e Súmula 111 STJ. Valor apurado: #brl(get(d, "calculos_liquidacao", "resumo_valores", "sucumbencias", "total")) (fls. #d.calculos_liquidacao.fls.at(0)-#d.calculos_liquidacao.fls.last()).
]

// ============================================================
// 2. IDENTIFICAÇÃO DO PROCESSO
// ============================================================

#heading(level: 2)[2. Identificação do Processo]

#let proc = d.processo

*Processo Originário:* #proc.numero_principal \
*Processo de Execução/Cumprimento de Sentença:* #get(proc, "numero_cumprimento") \
*Juízo:* #proc.vara -- Comarca de #proc.comarca\-SP \
#{
  let tribunal-text = d.sentenca.tribunal
  if d.at("acordao", default: none) != none {
    tribunal-text = tribunal-text + " / " + d.acordao.tribunal + " — " + d.acordao.orgao_julgador
  }
  [*Tribunal:* #tribunal-text]
} \
*Objeto da Ação:* #proc.assunto \

#v(0.3em)

*Histórico Processual:*

#if d.at("sentenca", default: none) != none [
  Sentença proferida em #d.sentenca.data por #d.sentenca.juiz: #d.sentenca.dispositivo. #d.sentenca.resumo
]

#if d.at("acordao", default: none) != none [
  #v(0.2em)
  Acórdão (#d.acordao.tribunal, #d.acordao.orgao_julgador, Rel. #d.acordao.relator): #d.acordao.dispositivo. #d.acordao.resumo
]

#if d.at("embargos_declaracao", default: none) != none [
  #v(0.2em)
  Embargos de Declaração: #d.embargos_declaracao.resultado.
]

#v(0.3em)

*Trânsito em Julgado Fase de Conhecimento:* #get(d, "certidao_transito_julgado", "data_transito") (fls. #d.certidao_transito_julgado.fls.at(0), p. #d.certidao_transito_julgado.paginas_pdf.at(0) do PDF) \

#if d.at("decisao_homologando_calculos", default: none) != none [
  *Trânsito em Julgado Execução:* #d.decisao_homologando_calculos.data (fls. #d.decisao_homologando_calculos.fls.at(0)-#d.decisao_homologando_calculos.fls.last()) \
  *Cálculos homologados:* #d.decisao_homologando_calculos.data (Decisão fls. #d.decisao_homologando_calculos.fls.at(0)-#d.decisao_homologando_calculos.fls.last())
]

#if d.at("oficios_requisitorios", default: none) != none and d.oficios_requisitorios.len() > 0 [
  #v(0.2em)
  *Data da expedição dos requisitórios:* Ofícios Requisitórios cadastrados no sistema PRECWEB (nº #d.oficios_requisitorios.at(0).numero).
]

// ============================================================
// 3. DADOS DO PRECATÓRIO E DA CESSÃO
// ============================================================

#heading(level: 2)[3. Dados do Precatório e da Cessão]

#if d.at("oficios_requisitorios", default: none) != none and d.oficios_requisitorios.len() > 0 {
  let prec = d.oficios_requisitorios.at(0)
  [
    *Ofício Requisitório:* nº #prec.numero (#prec.tipo_procedimento) \
    *Natureza do Crédito:* #prec.natureza_credito \
    *Valor do precatório:* #brl(prec.valores.valor_total) \
    #h(1em) Composição: Principal #brl(prec.valores.valor_principal) + Juros de Mora #brl(prec.valores.at("juros_mora_ate_dez_2021", default: prec.valores.at("juros_mora", default: 0))) + SELIC #brl(prec.valores.juros_selic) \
    *Status:* #prec.status \

    #if get(prec, "transito_fase_conhecimento") != none [
      *Trânsito Fase Conhecimento:* #prec.transito_fase_conhecimento \
      *Trânsito Embargos:* #prec.transito_embargos \
    ]
  ]
}

// ============================================================
// 4. DUE DILIGENCE E ANÁLISE DE RISCO
// ============================================================

#heading(level: 2)[4. Due Diligence e Análise de Risco]

#let transito = get(d, "certidao_transito_julgado", "data_transito")

#table(
  columns: (auto, auto, 1fr),
  inset: 8pt,
  stroke: 0.5pt + luma(200),
  fill: (_, row) => if row == 0 { luma(240) } else { none },
  table.header(
    [*Categoria*], [*Status*], [*Observações*],
  ),
  [Ação Rescisória], [Inexistente],
  [Sem ações rescisórias em curso. Trânsito em julgado em #transito. Prazo decadencial de 2 anos (art. 975, CPC).],

  [Ônus/Gravames], [Inexistente],
  [Sem penhoras, cessões anteriores ou gravames comunicados nos autos.],

  [Débitos Fiscais], [Verificar],
  [Consultar certidões federais, estaduais e trabalhistas do cedente.],

  [Débitos Trabalhistas], [Verificar],
  [Consultar TST e TRT por nome e CPF.],

  [Situação Serasa], [Verificar],
  [Consulta a ser realizada separadamente.],
)

// ============================================================
// 5. CONCLUSÃO
// ============================================================

#heading(level: 2)[5. Conclusão]

Considerando os elementos analisados, constata-se que:

#set enum(numbering: "a)")

+ O processo transitou em julgado em #transito, com decisão #if d.at("acordao", default: none) != none [favorável ao autor];

+ #if d.at("decisao_homologando_calculos", default: none) != none [
    Os cálculos de liquidação foram homologados judicialmente em #d.decisao_homologando_calculos.data, totalizando #brl(get(d, "calculos_liquidacao", "resumo_valores", "totalizacao", "total_geral"));
  ] else [
    Cálculos de liquidação pendentes de homologação;
  ]

+ #if d.at("pagamentos", default: none) != none and d.pagamentos.len() > 0 {
    let rpv_payments = d.pagamentos.filter(p => p.tipo == "RPV" or p.tipo == "Alvara" or (type(p.at("valor", default: none)) != none))
    if rpv_payments.len() > 0 [
      Pagamento(s) já efetuado(s) conforme extratos nos autos;
    ] else [
      Pagamentos pendentes;
    ]
  } else [
    Pagamentos pendentes;
  ]

+ Não foram identificadas ações rescisórias, gravames ou impedimentos ao crédito nos autos analisados.

#v(0.5em)
*Opina-se favoravelmente à aquisição do crédito*, ressalvadas as verificações externas de due diligence (certidões fiscais, trabalhistas e Serasa).

#v(1cm)
#line(length: 100%, stroke: 0.5pt + luma(200))
#v(0.5cm)

#align(center)[
  #proc.comarca -- SP, #d.meta.data_extracao.slice(0, 10)
  #v(1cm)
  #text(weight: "bold")[#advs.at(0).nome] \
  #advs.at(0).oab \
  ADVOGADO
]
