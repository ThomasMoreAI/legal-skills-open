# Dados de Crianças e Adolescentes (art. 14, LGPD)

## Objetivo
Padronizar a avaliação do tratamento de dados pessoais de crianças (até 12 anos incompletos) e adolescentes, que recebem proteção reforçada.

## Regras legais (art. 14)
- O tratamento deve ser realizado sempre no **melhor interesse** da criança e do adolescente.
- Dados de **crianças** exigem **consentimento específico e em destaque de pelo menos um dos pais ou responsável legal** (art. 14, §1º).
- O controlador deve **manter pública** a informação sobre os tipos de dados coletados, a forma de utilização e os procedimentos para exercício de direitos (art. 14, §2º).
- Não condicionar a participação em jogo/aplicação/atividade ao fornecimento de dados além do necessário (art. 14, §4º).
- Esforços razoáveis para verificar que o consentimento foi dado pelo responsável, consideradas as tecnologias disponíveis (art. 14, §5º).

## Relação com o ECA Digital (Lei nº 15.211/2025)
Desde **17/03/2026** o art. 14 da LGPD convive com o **Estatuto Digital da Criança e do Adolescente**, que impõe obrigações próprias e regime sancionatório autônomo a provedores de produtos e serviços de TI acessíveis a menores.

- Sempre que este módulo identificar público infantojuvenil, **ativar também** [[eca-digital]].
- A LGPD trata da **licitude do tratamento** (base legal, finalidade, consentimento parental); o ECA Digital trata do **desenho e da operação do serviço** (aferição de idade, supervisão parental, moderação, publicidade, transparência).
- Um achado pode violar as duas normas ao mesmo tempo — nesse caso, citar ambos os fundamentos no `finding`.
- Autodeclaração de idade é **expressamente vedada** em serviços com conteúdo impróprio ou proibido a menores de 18 anos, que exigem verificação confiável **a cada acesso** (art. 9º, §1º da Lei nº 15.211/2025). Nos demais serviços, a autodeclaração isolada não satisfaz os arts. 10, 12 e 14 do ECA Digital nem os "esforços razoáveis" do art. 14, §5º da LGPD.
- Atenção ao limiar etário: a LGPD distingue criança (até 12 anos incompletos) de adolescente; o ECA Digital usa o corte de **até 16 anos** para a vinculação obrigatória de conta a responsável legal (art. 24) e de **menores de 18 anos** para conteúdo impróprio. Não unificar os três cortes.

## Checklist atômico
Pergunta de enquadramento (não pontua): há público infantojuvenil entre os titulares, ou o serviço é direcionado ou atrativo a menores? Se sim, ativar também [[eca-digital]]. Sem crianças nem adolescentes entre os titulares, os itens abaixo ficam `NAO_APLICAVEL`, com a evidência.

Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `CA-01` | O tratamento de dados de crianças tem consentimento específico e em destaque de pelo menos um dos pais ou do responsável legal? | BL | `CRITICO` | — | `TECNICO` | art. 14, §1º |
| `CA-02` | Há verificação de idade confiável, que não dependa só de autodeclaração, e esforço razoável para confirmar que o consentimento veio do responsável? | BL | `ALTO` | `CRITICO` quando o serviço estiver no escopo do ECA Digital | `TECNICO` | art. 14, §5º |
| `CA-03` | A coleta respeita a minimização, sem condicionar jogo, aplicação ou atividade ao fornecimento de dados além do necessário? | BL | `ALTO` | — | `TECNICO` | art. 14, §4º |
| `CA-04` | As informações sobre os dados coletados, o uso e o exercício de direitos estão públicas e acessíveis? | BL | `MEDIO` | — | `DOCUMENTAL` | art. 14, §2º |

## Mapeamento para severidade e score
- Tratamento de dado de criança sem consentimento parental: `CRITICO`.
- Ausência de verificação de idade em serviço com público infantil: `ALTO` pela LGPD e `CRITICO` quando o serviço estiver no escopo do ECA Digital.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `bases_legais` (domínio `BL`: dados de crianças, art. 14) para todos os itens deste módulo.

## Relação com outros módulos
- Obrigações do ECA Digital (aferição de idade, supervisão parental, transparência): ver [[eca-digital]].
- Consentimento granular: ver [[legal-bases-engine]].
- Direitos do titular exercidos por responsável: ver [[rights-of-data-subject]].
