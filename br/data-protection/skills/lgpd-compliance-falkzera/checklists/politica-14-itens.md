# Checklist: Política de Privacidade: 14 itens obrigatórios

> Validação final do `politica-privacidade.md` antes de publicar. Cada item ausente vira risco de não-conformidade com art. 9º + 18 + 33 + 41 + 48 da LGPD.

Base normativa de cada item:

| # | Item | Base | OK |
|---|---|---|---|
| 1 | **Identificação completa do controlador**, razão social/nome civil, CNPJ ou CPF, endereço, e-mail/canal de contato | Art. 5º VI + 9º III e IV | ☐ |
| 2 | **Identificação do Encarregado (DPO)**, nome ou e-mail de contato (visível, em destaque). Se ATPP sem DPO, canal genérico tipo `privacidade@` | Art. 5º VIII + 41 §§ 1º e 2º | ☐ |
| 3 | **Finalidades específicas**, uma a uma, **sem genéricos**. Nada de "para melhorar sua experiência" | Art. 6º I + 9º I | ☐ |
| 4 | **Base legal** para cada tratamento (art. 7º, comuns / art. 11, sensíveis) | Art. 7º + 11 | ☐ |
| 5 | **Categorias de dados coletados**, cadastrais, financeiros, navegação, geolocalização, dispositivo, biométricos, etc. | Art. 5º I e II | ☐ |
| 6 | **Forma e duração do tratamento**, como coleta, por quanto tempo | Art. 9º II + 15 | ☐ |
| 7 | **Compartilhamento com terceiros**, quem recebe, finalidade, responsabilidades | Art. 9º V e VI + 27 | ☐ |
| 8 | **Transferência internacional**, países, garantias (SCC, decisão de adequação, etc.) | Art. 33 + Res. 19/2024 | ☐ |
| 9 | **Tempo de retenção / prazo de eliminação** por categoria | Art. 15 + 16 | ☐ |
| 10 | **Medidas de segurança** técnicas e administrativas aplicadas | Art. 6º VII + 46 | ☐ |
| 11 | **Direitos do titular** (lista dos 9 do art. 18) + **como exercê-los** (URL ou e-mail) | Art. 9º VII + 17-22 | ☐ |
| 12 | **Procedimento em caso de incidente**, comunicação a ANPD e titulares em prazo razoável | Art. 48 + Res. 15/2024 | ☐ |
| 13 | **Política de cookies** (se aplicável), link pra `politica-cookies.md` | Art. 7º §4º + Guia ANPD Cookies 23/01/2025 | ☐ |
| 14 | **Data da última atualização** e **histórico de versões** | Boas práticas: Guia PPSI | ☐ |

## Itens recomendados adicionais (boas práticas mercado)

- [ ] **Sumário/índice clicável** no topo
- [ ] **Linguagem clara**, sem juridiquês excessivo (princípio da transparência, art. 6º VI)
- [ ] **Camadas de informação** (resumo executivo + detalhe), modelo "layered notice" da ANPD
- [ ] **Glossário** de termos técnicos (cookie, processador, tratamento)
- [ ] **Versão acessível** (contraste, tipografia legível, compatibilidade com leitor de tela)
- [ ] **Direito de reclamar à ANPD** explicitamente mencionado, com link [gov.br/anpd/pt-br/canais_atendimento/cidadao/peticao-de-titular](https://www.gov.br/anpd/pt-br/canais_atendimento/cidadao/peticao-de-titular)
- [ ] **Compromisso de comunicar mudanças materiais** com 30 dias de antecedência

## Itens condicionais

- [ ] **Se trata dados sensíveis**: seção dedicada explicando proteção reforçada (art. 11)
- [ ] **Se trata dados de criança/adolescente**: seção sobre verificação de idade e consentimento parental (art. 14)
- [ ] **Se faz decisão automatizada**: seção sobre revisão e critérios (art. 20)
- [ ] **Se faz transferência internacional**: lista detalhada de países + base legal (SCC) (art. 33)
- [ ] **Se faz marketing**: seção específica sobre opt-in/opt-out de comunicações comerciais

## Validação de paridade (anti-dark-pattern)

- [ ] **Botão "Excluir minha conta"** tem mesma visibilidade que "Criar conta"?
- [ ] **Revogar consentimento** é tão fácil quanto conceder?
- [ ] **Banner de cookies**: "Rejeitar opcionais" tem mesma proeminência que "Aceitar todos"?
- [ ] **Canal do DPO** está em destaque (rodapé visível em todas as páginas)?

## Validação de linguagem

Pra cada seção, perguntar:

- [ ] Um cidadão com escolaridade média entende?
- [ ] Há jargão técnico não explicado?
- [ ] As finalidades são **concretas** ou **genéricas**?
- [ ] Há ambiguidade ("podemos coletar", "às vezes compartilhamos")? **Específico ou nada.**

## Output final

Quando todos os checkboxes estiverem marcados, o documento está pronto pra publicação. Salvar em:

- **Repositório:** `<projeto>/legal/politica-privacidade.md`
- **Publicação web:** rota `/privacidade` (Next.js: `app/(legal)/privacidade/page.tsx`)
- **Link no footer:** em todas as páginas
- **Versionamento:** commit com mensagem `chore(legal): publica política de privacidade vYYYY-MM-DD`
