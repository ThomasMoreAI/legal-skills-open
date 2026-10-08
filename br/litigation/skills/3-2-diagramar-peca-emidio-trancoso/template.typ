// =============================================================================
// template.typ — Legal Design simples e genérico para QUALQUER peça jurídica.
// Usado pela skill /diagramar-peca. Componentes leves e reutilizáveis —
// nada específico de "alegações finais". Edite as cores/fontes à vontade.
//
// Como usar no .typ gerado (compile com `typst compile --root . <arquivo>.typ`):
//   #import "/.agents/skills/3.2-diagramar-peca/template.typ": *
//   #show: peca.with(titulo: "...", juizo: "...", partes: "...")
// =============================================================================

// ─── Paleta ──────────────────────────────────────────────────────────────────
#let cor-principal = rgb("#1f4e79")   // azul institucional
#let cor-suave     = rgb("#eef2f7")   // fundo de blocos
#let cor-cinza     = rgb("#5a5a5a")
#let cor-aviso     = rgb("#fff4e6")   // fundo de destaque
#let cor-aviso-b   = rgb("#e8a33d")   // borda de destaque

// ─── Documento base ────────────────────────────────────────────────────────
// Envolve a peça inteira. Use com:  #show: peca.with(titulo: "...", ...)
#let peca(
  titulo: "",
  juizo: none,      // ex.: "Juízo da 2ª Vara Cível da Comarca de ..."
  partes: none,     // ex.: "FULANO move contra BELTRANO"
  rodape: none,     // ex.: "Advogado(a) — OAB/UF 000.000"
  corpo,
) = {
  set page(
    paper: "a4",
    margin: (x: 2.6cm, top: 2.6cm, bottom: 2.4cm),
    numbering: "1",
    footer: context if rodape != none {
      set text(size: 8pt, fill: cor-cinza)
      align(center, rodape)
    },
  )
  set text(font: ("Libertinus Serif", "Georgia", "Times New Roman"), size: 11pt, lang: "pt")
  set par(justify: true, leading: 0.78em, first-line-indent: 1.5em, spacing: 1.1em)

  // Títulos de seção com barra azul à esquerda
  show heading.where(level: 1): it => {
    set text(size: 13pt, weight: "bold", fill: cor-principal)
    block(above: 1.4em, below: 0.8em)[#it.body]
  }
  show heading.where(level: 2): it => {
    set text(size: 11.5pt, weight: "bold", fill: cor-cinza)
    block(above: 1.1em, below: 0.6em)[#it.body]
  }

  // Cabeçalho da peça
  if juizo != none {
    align(center, text(size: 10pt, fill: cor-cinza, upper(juizo)))
    v(1.2em)
  }
  align(center, text(size: 15pt, weight: "bold", fill: cor-principal, upper(titulo)))
  if partes != none {
    v(0.6em)
    align(center, text(size: 10pt, style: "italic", fill: cor-cinza, partes))
  }
  line(length: 100%, stroke: 0.5pt + cor-principal)
  v(1em)

  corpo
}

// ─── Destaque ────────────────────────────────────────────────────────────────
// Caixa para o ponto-chave que não pode passar batido.
#let destaque(corpo) = block(
  width: 100%,
  fill: cor-aviso,
  stroke: (left: 3pt + cor-aviso-b),
  inset: 12pt,
  radius: 2pt,
  above: 1em, below: 1em,
)[#set par(first-line-indent: 0pt); #corpo]

// ─── Citação em bloco ─────────────────────────────────────────────────────────
// Para transcrições, doutrina, dispositivos legais citados literalmente.
#let citacao(fonte: none, corpo) = block(
  width: 100%,
  fill: cor-suave,
  inset: (left: 14pt, rest: 11pt),
  radius: 2pt,
  above: 1em, below: 1em,
)[
  #set par(first-line-indent: 0pt)
  #set text(style: "italic")
  #corpo
  #if fonte != none [
    #v(0.4em)
    #text(size: 9pt, style: "normal", fill: cor-cinza)[— #fonte]
  ]
]

// ─── Fundamento (lei / jurisprudência) ─────────────────────────────────────────
// Caixa enxuta para citar uma fonte verificada. NÃO inventar: só preencher com
// dados reais (de /buscar-fontes ou /buscar-tjpr).
#let fundamento(tipo: "FUNDAMENTO", ref: "", corpo) = block(
  width: 100%,
  stroke: 0.75pt + cor-principal,
  inset: 11pt,
  radius: 2pt,
  above: 1em, below: 1em,
)[
  #set par(first-line-indent: 0pt)
  #text(size: 8.5pt, weight: "bold", fill: cor-principal)[#upper(tipo)#if ref != "" [ · #ref]]
  #v(0.3em)
  #corpo
]

// ─── Cronologia ────────────────────────────────────────────────────────────────
// Linha do tempo simples. Uso: #cronologia((("12/03/2024", "Contrato assinado"), ...))
#let cronologia(eventos) = block(above: 1em, below: 1em)[
  #set par(first-line-indent: 0pt)
  #for (data, evento) in eventos [
    #grid(
      columns: (3.2cm, 1fr),
      gutter: 8pt,
      text(weight: "bold", fill: cor-principal, size: 10pt)[#data],
      text(size: 10pt)[#evento],
    )
    #v(0.35em)
  ]
]

// ─── Marcador inline ───────────────────────────────────────────────────────────
// Etiqueta curta para guiar a leitura (ex.: #marcador("PEDIDO")).
#let marcador(txt) = box(
  fill: cor-principal,
  inset: (x: 5pt, y: 2pt),
  radius: 2pt,
  text(fill: white, size: 8pt, weight: "bold")[#upper(txt)],
)
