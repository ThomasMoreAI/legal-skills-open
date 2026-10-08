/* =====================================================================
   MOTOR DE BUSCA — Jurisprudência da Justiça Eleitoral (TSE + 27 TREs)
   ---------------------------------------------------------------------
   Como usar (pela skill jurisprudencia-eleitoral):
   1. Ter uma aba com o portal carregado (window.hcaptcha precisa existir):
        https://jurisprudencia.tse.jus.br/#/jurisprudencia/pesquisa   (TSE)
        https://jurisprudencia-tres.tse.jus.br/#/jurisprudencia/pesquisa (TREs)
      O token hCaptcha é gerado a CADA chamada (uso único) e — comprovado —
      vale para os DOIS tenants, então uma aba só atende TSE e TREs.
   2. Injetar ESTE arquivo uma vez (define window.__jeSearch).
   3. Chamar:  await window.__jeSearch({ query:"...", tribunais:"ambos" })

   Robustez (aprendida em teste real):
   - hcaptcha.reset() + retry por chamada: o widget "esfria" quando a aba fica
     ociosa e a 1ª chamada retorna "Falha ao validar o HCaptcha"; o motor
     regenera o token e tenta de novo (até `tentativas`, padrão 3).
   - strip de HTML: textoEmenta/textoDecisao — e até numeroProcesso quando há
     realce — vêm com <span class="highlighted">…</span>; limpamos tudo.

   Nunca coloca credencial/segredo. Não versiona token. Standalone.
   ===================================================================== */
window.__jeSearch = async function (opts) {
  opts = opts || {};

  // Operadores em PT do site → sintaxe Elasticsearch (EN). Crus, E/OU/NÃO
  // viram termo literal na API; por isso normalizamos aqui.
  const norm = (s) => (' ' + String(s == null ? '' : s) + ' ')
    .replace(/\s+E\s+/g, ' AND ')
    .replace(/\s+OU\s+/g, ' OR ')
    .replace(/\s+N[ÃA]O\s+/g, ' NOT ')
    .replace(/\s{2,}/g, ' ')
    .trim();

  // Remove tags/realce e desescapa entidades (nomeadas comuns + numéricas).
  const clean = (s) => String(s == null ? '' : s)
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ')
    .replace(/&ndash;/g, '–').replace(/&mdash;/g, '—')
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"').replace(/&#3[49];/g, "'")
    .replace(/&#(\d+);/g, (m, n) => String.fromCharCode(+n))
    .replace(/&amp;/g, '&')
    .replace(/\s{2,}/g, ' ')
    .trim();

  let FIELDS = opts.campos || [
    'textoEmenta', 'textoDecisao', 'textoIndexacao',
    'indexacoes.textoSentencaIndexacao', 'assuntos.nomeAssunto',
    'partes.nomeParte', 'relatores.nome', 'numeroProcesso', 'numeroUnico'
  ];
  // "Incluir inteiro teor": adiciona o campo INTE (texto integral do acórdão).
  if (opts.incluirInteiroTeor && FIELDS.indexOf('INTE') < 0) FIELDS = FIELDS.concat('INTE');

  let q = norm(opts.query);
  if (opts.tribunal) q = '(' + q + ') AND siglaTribunalJE:"' + opts.tribunal + '"';
  if (opts.uf)       q = '(' + q + ') AND siglaUF:"' + opts.uf + '"';
  // Campos minerados do bundle do front (templates RELATORES/PARTES do form
  // avançado): filtro por relator e por parte via query_string escopado.
  if (opts.relator)  q = '(' + q + ') AND relatores.nome:"' + opts.relator + '"';
  if (opts.parte)    q = '(' + q + ') AND partes.nomeParte:"' + opts.parte + '"';
  // Filtro por data de julgamento — campo DATD (dd/mm/aaaa). O range exige
  // limites explícitos ("*" não funciona), então usamos sentinelas quando um
  // dos lados é omitido.
  if (opts.dataInicio || opts.dataFim) {
    const ini = opts.dataInicio || '01/01/1900';
    const fim = opts.dataFim || '31/12/2099';
    q = '(' + q + ') AND DATD:[' + ini + ' TO ' + fim + ']';
  }

  const qs = {
    query: q,
    default_operator: opts.operadorPadrao || 'AND',
    fields: FIELDS
  };
  // Dicionário de sinônimos do portal (checkbox "sinônimos" do front): o
  // bundle expande para analyzer "meu_sinonimos" no query_string.
  if (opts.sinonimos) qs.analyzer = 'meu_sinonimos';
  const termo = JSON.stringify({ bool: { must: [ { query_string: qs } ] } });

  async function mint() {
    if (!window.hcaptcha) throw new Error('window.hcaptcha ausente: carregue o portal SJUR antes.');
    try { window.hcaptcha.reset(); } catch (e) { /* widget pode não estar pronto p/ reset */ }
    const r = await window.hcaptcha.execute({ async: true });
    return (r && r.response) ? r.response : r;
  }

  function mapItem(d) {
    const rel = (d.relatores || []).map(r => clean(r.descricaoCompleta || r.nome)).filter(Boolean);
    const em = clean(d.textoEmenta);
    const dec = clean(d.textoDecisao);
    // Fonte do resumo: a ementa quando existir; senão o texto da decisão.
    // (Muitos acórdãos de TRE não trazem `textoEmenta`, só `textoDecisao`.)
    const fonteResumo = em || dec;
    const lim = opts.limiteResumo || 700;
    return {
      id: d.codigoDecisao,
      tribunal: d.siglaTribunalJE,
      uf: d.siglaUF,
      municipio: clean(d.nomeMunicipio),
      processo: clean(d.numeroProcesso),
      numeroUnico: clean(d.numeroUnico),
      classe: d.siglaClasse,
      classeDesc: clean(d.descricaoClasse),
      tipoDecisao: d.descricaoTipoDecisao,
      data: d.dataDecisao,
      anoEleicao: d.anoEleicao,
      relator: rel.join('; '),
      temPDF: !!d.temInteiroTeorPDF,
      temAudio: !!d.temInteiroTeorAudio,
      pdf: d.temInteiroTeorPDF
        ? ('https://sjur-servicos.tse.jus.br/sjur-servicos/rest/download/pdf/' + d.codigoDecisao)
        : null,
      temEmenta: em.length > 0,
      fonteResumo: em ? 'ementa' : (dec ? 'decisao' : 'nenhuma'),
      resumo: opts.ementaCompleta ? fonteResumo : fonteResumo.slice(0, lim),
      ementa: opts.ementaCompleta ? em : em.slice(0, lim),
      decisao: opts.incluirDecisao ? dec : undefined
    };
  }

  async function postOnce(tenant) {
    const body = {
      refinaTermos: [], refinaData: [],
      termoPesquisa: termo,
      pagina: opts.pagina || 0,
      tamanho: opts.tamanho || 25,
      tribunais: tenant === 'tse' ? ['tse'] : ['tre-*'],
      captchaToken: await mint(),
      ordenacao: opts.ordenacao || 'dj_desc',   // dj_desc | dj_asc | dtj_desc | dtj_asc | score
      refinamento: []
    };
    const url = 'https://sjur-pesquisa-api.tse.jus.br/' + tenant +
                '/sjur-pesquisa-backend/rest/public/pesquisa';
    return fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*' },
      body: JSON.stringify(body)
    }).then(r => r.json());
  }

  async function hit(tenant) {
    const tentativas = opts.tentativas || 3;
    let j;
    for (let i = 0; i < tentativas; i++) {
      j = await postOnce(tenant);
      if (!j.mensagem) break;                       // sucesso
      if (!/captcha/i.test(j.mensagem)) break;      // erro não é de captcha → não insiste
      await new Promise(res => setTimeout(res, 400)); // token novo na próxima volta
    }
    if (j.mensagem) return { tenant, erro: j.mensagem, total: 0, itens: [] };
    return { tenant, total: j.totalRegistros, itens: (j.content || []).map(mapItem) };
  }

  const alvo = opts.tribunais || 'tse';   // 'tse' | 'tres' | 'ambos'
  if (alvo === 'ambos') {
    const tse = await hit('tse');
    const tres = await hit('tres');
    return { consulta: q, tse, tres, total: (tse.total || 0) + (tres.total || 0) };
  }
  return { consulta: q, ...(await hit(alvo === 'tres' ? 'tres' : 'tse')) };
};
'engine pronto';
