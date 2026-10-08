# Transferência Internacional de Dados (arts. 33-36, LGPD)

## Objetivo
Avaliar a legalidade da transferência de dados pessoais para fora do Brasil, comum em uso de cloud, SaaS e APIs de IA hospedadas no exterior.

## Quando se aplica
Sempre que dados pessoais saem do território nacional, incluindo:
- provedores de cloud com regiões fora do Brasil (AWS, Azure, GCP);
- SaaS e analytics estrangeiros;
- APIs de IA/LLM de terceiros (ex.: OpenAI, Anthropic, Google) — ver [[llm-audit]];
- subprocessadores e CDNs internacionais.

## Mecanismos legais válidos (art. 33)
A transferência só é permitida quando houver pelo menos um:
- país/organismo com **grau de proteção adequado** reconhecido pela ANPD;
- **cláusulas-padrão contratuais (CPC)** aprovadas pela ANPD, cláusulas contratuais específicas, normas corporativas globais ou selos/certificados;
- cooperação jurídica internacional, proteção da vida, execução de política pública;
- **consentimento específico e em destaque** do titular, com informação sobre o caráter internacional;
- obrigação legal, execução de contrato ou exercício regular de direitos.

## Regulamento da ANPD (Res. CD/ANPD nº 19/2024)
- A **Resolução CD/ANPD nº 19/2024** (23/08/2024) aprovou o Regulamento de Transferência Internacional de Dados e as **cláusulas-padrão contratuais (CPC)**.
- O prazo de 12 meses para incorporar as CPC aos instrumentos contratuais **encerrou em 23/08/2025**. Não existe mais período de adaptação.
- Consequência para a auditoria: contrato de transferência internacional que ainda não incorporou as CPC — ou outro mecanismo aprovado equivalente — é **não conformidade atual**, e não item "em adequação".
- As CPC não podem ser alteradas de forma a reduzir o nível de proteção; cláusulas contratuais específicas exigem submissão à ANPD.

## Países e organismos com grau adequado reconhecido
- **Resolução CD/ANPD nº 32/2026** (26/01/2026) — reconhece a **União Europeia** como organismo internacional com grau adequado de proteção.
- Efeito prático: transferência para destinatário na UE que se enquadre no reconhecimento **dispensa CPC** como fundamento do art. 33; a decisão de adequação passa a ser o mecanismo legal.
- A dispensa é **apenas do mecanismo do art. 33** — permanecem obrigatórios base legal do art. 7º/11, informação ao titular, contrato de operador (art. 39) e as garantias de segurança do art. 46.
- Estados Unidos, Reino Unido e demais destinos **não** possuem reconhecimento de adequação pela ANPD: continuam exigindo CPC ou outro mecanismo do art. 33.

## Checklist atômico
Sem dado pessoal saindo do País, os itens ficam `NAO_APLICAVEL`, com a evidência (região dos serviços e dos provedores).

Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `TI-01` | O fluxo de dados para o exterior está mapeado (destino, provedor, finalidade)? | 14 | `MEDIO` | — | `DOCUMENTAL` | arts. 33 e 37 |
| `TI-02` | Há mecanismo do art. 33 documentado para cada transferência: adequação reconhecida (União Europeia, Res. CD/ANPD nº 32/2026) ou, nos demais destinos, as CPC da Res. CD/ANPD nº 19/2024 incorporadas ao contrato, ou outro mecanismo aprovado? | 14 | `ALTO` | `CRITICO` com mecanismo comprovadamente ausente (contrato ou termos examinados) em destino sem adequação | `DOCUMENTAL` | art. 33; Res. CD/ANPD nº 19/2024 |
| `TI-03` | As CPC ou o mecanismo adotado cobrem os operadores e subprocessadores internacionais, inclusive os de segundo nível? | 14 | `MEDIO` | — | `DOCUMENTAL` | art. 33; Res. CD/ANPD nº 19/2024 |
| `TI-04` | O titular é informado sobre a transferência internacional na política de privacidade? | 14 | `ALTO` | — | `DOCUMENTAL` | arts. 9º e 33 |
| `TI-05` | Dados sensíveis transferidos têm hipótese do art. 11 e proteção reforçada (criptografia, restrição de acesso)? | 14 | `ALTO` | — | `TECNICO` | arts. 11, 33 e 46 |

Dependências (contagem única de `core/scoring-engine.md`): com o segundo item `NAO_CONFORME`, o primeiro fica `NAO_APLICAVEL`.
- `TI-03` depende de `TI-02`: não há mecanismo cuja cobertura avaliar enquanto ele não estiver evidenciado.

## Mapeamento para severidade e score
- Destino sem adequação e mecanismo do art. 33 **comprovadamente ausente** (contrato ou termos examinados, sem as CPC da Res. CD/ANPD nº 19/2024 nem outro mecanismo): `CRITICO`.
- Mecanismo **não evidenciado** (contrato ou termos do provedor não localizados ou não examinados; termos padrão podem conter as cláusulas): `ALTO`, com evidência `AUSENTE`, até a verificação.
- Transferência sem informação ao titular: `ALTO`.
- Contrato com CPC incorporadas, mas sem cobertura dos subprocessadores: `MEDIO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `governanca` (domínio 14) para todos os itens deste módulo. As três primeiras regras acima são a criticidade e o agravante de `TI-02`, `TI-04` e `TI-03`.

## Relação com outros módulos
- Postura cloud e exposição: ver [[cloud-audit]].
- Gestão de operadores/subprocessadores e DPA: ver [[dpo-framework]].
