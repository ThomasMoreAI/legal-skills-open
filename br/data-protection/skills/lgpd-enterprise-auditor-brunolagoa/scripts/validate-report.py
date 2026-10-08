#!/usr/bin/env python3
"""Valida os dados de um relatório do LGPD Enterprise Auditor contra as regras do framework.

Confere a estrutura (8 seções), os enums, os IDs do catálogo, a relação entre itens e achados,
as regras de evidência e o cálculo (score por área, score global, cobertura, classificação com
teto). Lê as regras dos próprios arquivos do framework, para não duplicá-las aqui.

Uso: scripts/validate-report.py RELATORIO [--framework DIR] [--md RELATORIO.md]
  RELATORIO    arquivo .html gerado pelo modelo (lê o bloco "lgpd-dados") ou .json com os dados
  --framework  pasta do framework (padrão: .agents/lgpd-enterprise-auditor deste repositório)
  --md         relatório em Markdown com os mesmos dados: confere IDs, score e classificação
Sai com 0 se não houver erro e com 1 se houver. Avisos não reprovam.
"""

import argparse
import json
import math
import os
import re
import sys

SECTIONS = ["resumo_executivo", "score_lgpd", "checklist_conformidade", "nao_conformidades",
            "itens_obrigatorios_ausentes", "riscos_identificados", "plano_adequacao", "recomendacoes_tecnicas"]
VALUE = {"CONFORME": 1.0, "PARCIAL": 0.5, "NAO_CONFORME": 0.0}
LEVELS = ["BAIXO", "MEDIO", "ALTO", "CRITICO"]
WEIGHT = {"CRITICO": 4, "ALTO": 3, "MEDIO": 2, "BAIXO": 1}
APPLICABILITY = {"APLICAVEL", "NAO_APLICAVEL", "NAO_VERIFICADO"}
CONTROL = {"TECNICO", "DOCUMENTAL"}
EVIDENCE_TYPE = {"ENCONTRADA", "PARCIAL", "AUSENTE"}
EVIDENCE_SOURCE = {"TECNICA", "DOCUMENTAL", "TECNICA + DOCUMENTAL"}
CONFIDENCE = {"ALTA", "MEDIA", "BAIXA"}
DEADLINE = {"IMEDIATO", "30_DIAS", "90_DIAS", "180_DIAS"}
DEADLINE_ORDER = ["IMEDIATO", "30_DIAS", "90_DIAS", "180_DIAS"]
MAX_DEADLINE = {"CRITICO": "IMEDIATO", "ALTO": "30_DIAS", "MEDIO": "90_DIAS", "BAIXO": "180_DIAS"}
EFFORT = {"P", "M", "G"}
CLASSES = ["CRITICO", "BAIXO_NIVEL", "PARCIALMENTE_CONFORME", "ALTA_CONFORMIDADE", "EXCELENTE"]
CAP = "PARCIALMENTE_CONFORME"
ALWAYS_APPLICABLE = {"bases_legais", "seguranca", "direitos_titular", "governanca"}
DATA_OPEN = '<script type="application/json" id="lgpd-dados">'

ROW = re.compile(r"^\| `([A-Z]{2,5}-\d{2,3})` \| (.*) \| (BL|\d+) \| `(\w+)` \| (.*) \| `(TECNICO|DOCUMENTAL)` \| (.*) \|$")
DOMAIN = re.compile(r"^\| `(BL|\d+)` \| (.*) \| `(\w+)` \|$")
AREA_WEIGHT = re.compile(r"^- `(\w+)`: (\d+)%$")
MANIFEST_FILES = re.compile(r"^- `files`: (.*)$")
DEPENDS = re.compile(r"^- `([A-Z]{2,5}-\d{2,3})` depende de `([A-Z]{2,5}-\d{2,3})`")


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def load_framework(root):
    """Lê do framework: pesos de área, mapa domínio → área, catálogo e arquivos de cada módulo."""
    weights, domains = {}, {}
    for line in read(os.path.join(root, "core", "scoring-engine.md")).splitlines():
        match = AREA_WEIGHT.match(line)
        if match:
            weights[match.group(1)] = int(match.group(2))
        match = DOMAIN.match(line)
        if match:
            domains[match.group(1)] = match.group(3)

    modules, catalog, depends = {}, {}, []
    manifests = os.path.join(root, "orchestrator", "manifests")
    for name in sorted(os.listdir(manifests)):
        if not name.endswith(".manifest.md"):
            continue
        module = name[: -len(".manifest.md")]
        modules[module] = set()
        for line in read(os.path.join(manifests, name)).splitlines():
            match = MANIFEST_FILES.match(line)
            if not match:
                continue
            for rel in re.findall(r"`([^`]+)`", match.group(1)):
                for row in read(os.path.join(root, rel)).splitlines():
                    pair = DEPENDS.match(row)
                    if pair:
                        depends.append((pair.group(1), pair.group(2)))
                    item = ROW.match(row)
                    if not item:
                        continue
                    allowed = {item.group(4)} | {lv for lv in re.findall(r"`(\w+)`", item.group(5)) if lv in WEIGHT}
                    catalog[item.group(1)] = {"module": module, "domain": item.group(3), "area": domains.get(item.group(3)),
                                              "criticality": item.group(4), "allowed": allowed, "control": item.group(6)}
                    modules[module].add(item.group(1))
    return weights, domains, modules, catalog, depends


def load_data(path):
    text = read(path)
    if path.lower().endswith((".html", ".htm")):
        start = text.find(DATA_OPEN)
        end = text.find("</script>", start)
        if start < 0 or end < 0:
            sys.exit("Bloco de dados \"lgpd-dados\" não encontrado em %s." % path)
        block = text[start + len(DATA_OPEN):end]
        if "<" in block:
            sys.exit("O bloco de dados contém o caractere '<'; ele deve ser escrito como \\u003c.")
        text = block
    try:
        data = json.loads(text)
    except ValueError as error:
        sys.exit("Os dados do relatório não são um JSON válido: %s" % error)
    if not isinstance(data, dict) or data.get("_modelo"):
        sys.exit("O arquivo ainda está com o bloco de dados do modelo, sem dados de auditoria.")
    return data


def band(score):
    return ("CRITICO" if score < 50 else "BAIXO_NIVEL" if score < 70 else "PARCIALMENTE_CONFORME" if score < 85
            else "ALTA_CONFORMIDADE" if score < 95 else "EXCELENTE")


def half_up(value):
    return int(math.floor(value + 0.5))


def text_of(value):
    return "; ".join(str(v) for v in value) if isinstance(value, list) else ("" if value is None else str(value))


def validate(data, weights, modules, catalog, md_text=None, depends=()):
    errors, warnings = [], []
    err, warn = errors.append, warnings.append

    for section in SECTIONS:
        if not data.get(section):
            err("seção ausente ou vazia: %s" % section)
    meta = data.get("meta") or {}
    score_block = data.get("score_lgpd") or {}
    items = data.get("checklist_conformidade") or []
    findings = data.get("nao_conformidades") or []

    # ── checklist ────────────────────────────────────────────────────────
    by_id = {}
    modulated = {f.get("item_id") for f in findings if f.get("severity_modulation")}
    for item in items:
        ident = item.get("id") or "(sem id)"
        if ident in by_id:
            err("%s: ID repetido no checklist" % ident)
        by_id[ident] = item
        appl = item.get("applicability", "APLICAVEL")
        if appl not in APPLICABILITY:
            err("%s: applicability inválida (%s)" % (ident, appl))
        if item.get("score_area") not in weights:
            err("%s: score_area inválida (%s)" % (ident, item.get("score_area")))

        entry = catalog.get(ident)
        if entry is None:
            if re.match(r"^EX-\d{2,3}$", ident):
                if not item.get("justification"):
                    err("%s: item extra sem justification (por que não cabe em nenhum item do catálogo)" % ident)
            else:
                err("%s: ID fora do catálogo (item extra usa EX-nn)" % ident)
        else:
            if item.get("score_area") != entry["area"]:
                err("%s: score_area %s difere da área do catálogo (%s)" % (ident, item.get("score_area"), entry["area"]))
            if item.get("control_type") and item["control_type"] != entry["control"]:
                err("%s: control_type %s difere do catálogo (%s)" % (ident, item["control_type"], entry["control"]))
            crit = item.get("criticality")
            if crit:
                allowed = set(entry["allowed"])
                if ident in modulated:
                    allowed |= {LEVELS[LEVELS.index(lv) - 1] for lv in entry["allowed"] if LEVELS.index(lv) > 0}
                if crit not in allowed:
                    err("%s: criticality %s não é a do catálogo (%s) nem um agravante previsto na linha do item"
                        % (ident, crit, entry["criticality"]))

        if appl == "APLICAVEL":
            status = item.get("status")
            if status not in VALUE:
                err("%s: status inválido (%s)" % (ident, status))
            if item.get("criticality") not in WEIGHT:
                err("%s: criticality inválida (%s)" % (ident, item.get("criticality")))
            if item.get("control_type") not in CONTROL:
                err("%s: control_type inválido (%s)" % (ident, item.get("control_type")))
            etype, source = item.get("evidence_type"), item.get("evidence_source")
            if not text_of(item.get("evidence")):
                err("%s: item avaliado sem evidence" % ident)
            if etype not in EVIDENCE_TYPE:
                err("%s: evidence_type inválido (%s)" % (ident, etype))
            if source not in EVIDENCE_SOURCE:
                err("%s: evidence_source inválido (%s)" % (ident, source))
            if item.get("evidence_confidence") not in CONFIDENCE:
                err("%s: evidence_confidence inválida (%s)" % (ident, item.get("evidence_confidence")))
            if status == "CONFORME" and etype != "ENCONTRADA":
                err("%s: CONFORME exige evidence_type ENCONTRADA" % ident)
            if status == "PARCIAL" and etype != "PARCIAL":
                err("%s: status PARCIAL exige evidence_type PARCIAL" % ident)
            if status == "NAO_CONFORME" and etype not in ("PARCIAL", "AUSENTE"):
                err("%s: NAO_CONFORME exige evidence_type PARCIAL ou AUSENTE" % ident)
        else:
            if item.get("status"):
                err("%s: item %s não tem status" % (ident, appl))
            if not item.get("justification"):
                err("%s: item %s sem justification" % (ident, appl))
            if appl == "NAO_VERIFICADO" and (item.get("control_type") or (entry or {}).get("control")) == "DOCUMENTAL":
                err("%s: controle DOCUMENTAL nunca é NAO_VERIFICADO" % ident)

    active = meta.get("modules")
    if isinstance(active, list) and active:
        for module in active:
            if module not in modules:
                err("meta.modules: módulo desconhecido (%s)" % module)
                continue
            missing = sorted(modules[module] - set(by_id))
            if missing:
                err("módulo %s: itens do catálogo ausentes do checklist: %s" % (module, ", ".join(missing)))
        for ident in by_id:
            entry = catalog.get(ident)
            if entry and entry["module"] not in active:
                err("%s: item do módulo %s, que não está em meta.modules" % (ident, entry["module"]))
    else:
        warn("meta.modules ausente: a presença de todos os itens do catálogo não foi conferida")

    # Dependências do catálogo: com o item de que depende reprovado, o dependente sai do cálculo.
    for dependent, target in depends:
        if dependent in by_id and target in by_id and by_id[target].get("status") == "NAO_CONFORME" \
                and by_id[dependent].get("applicability", "APLICAVEL") == "APLICAVEL":
            err("%s: depende de %s, que está NAO_CONFORME; deve ficar NAO_APLICAVEL" % (dependent, target))

    # ── achados ──────────────────────────────────────────────────────────
    seen = {}
    for finding in findings:
        ident = finding.get("id") or "(sem id)"
        ref = finding.get("item_id")
        item = by_id.get(ref)
        if item is None:
            err("%s: item_id %s não existe no checklist" % (ident, ref))
            continue
        if ref in seen:
            err("%s: o item %s já tem o achado %s" % (ident, ref, seen[ref]))
        seen[ref] = ident
        severity = finding.get("severity")
        if severity not in WEIGHT:
            err("%s: severity inválida (%s)" % (ident, severity))
            continue
        status, crit = item.get("status"), item.get("criticality")
        if status not in ("NAO_CONFORME", "PARCIAL"):
            err("%s: aponta para %s, que não está NAO_CONFORME nem PARCIAL" % (ident, ref))
        elif crit in WEIGHT:
            if status == "NAO_CONFORME" and severity != crit:
                err("%s: severity %s difere da criticality do item %s (%s)" % (ident, severity, ref, crit))
            below = LEVELS[max(LEVELS.index(crit) - 1, 0)]
            if status == "PARCIAL" and severity != below:
                err("%s: item %s está PARCIAL, então a severity deve ser %s (um nível abaixo da criticality %s), não %s"
                    % (ident, ref, below, crit, severity))
        for field in ("title", "problem", "lgpd_article", "evidence", "technical_impact", "legal_impact", "recommendation", "owner"):
            if not text_of(finding.get(field)):
                err("%s: campo obrigatório ausente (%s)" % (ident, field))
        if finding.get("evidence_type") not in EVIDENCE_TYPE:
            err("%s: evidence_type inválido (%s)" % (ident, finding.get("evidence_type")))
        if finding.get("evidence_source") not in EVIDENCE_SOURCE:
            err("%s: evidence_source inválido (%s)" % (ident, finding.get("evidence_source")))
        if finding.get("evidence_confidence") not in CONFIDENCE:
            err("%s: evidence_confidence inválida (%s)" % (ident, finding.get("evidence_confidence")))
        deadline = finding.get("deadline_suggestion")
        if deadline not in DEADLINE:
            err("%s: deadline_suggestion inválido (%s)" % (ident, deadline))
        elif DEADLINE_ORDER.index(deadline) > DEADLINE_ORDER.index(MAX_DEADLINE[severity]):
            err("%s: prazo %s é mais longo que o máximo para severidade %s (%s)" % (ident, deadline, severity, MAX_DEADLINE[severity]))
        if finding.get("effort") not in EFFORT:
            err("%s: effort inválido (%s)" % (ident, finding.get("effort")))
    for ident, item in by_id.items():
        if item.get("applicability", "APLICAVEL") == "APLICAVEL" and item.get("status") in ("NAO_CONFORME", "PARCIAL") and ident not in seen:
            err("%s: item %s sem achado em nao_conformidades" % (ident, item.get("status")))

    # ── cálculo ──────────────────────────────────────────────────────────
    area = {}
    kind = {"TECNICO": [0.0, 0], "DOCUMENTAL": [0.0, 0]}
    for item in items:
        slot = area.setdefault(item.get("score_area"), {"sum": 0.0, "weight": 0, "n": 0, "nv": 0})
        appl = item.get("applicability", "APLICAVEL")
        if appl == "NAO_VERIFICADO":
            slot["nv"] += 1
        if appl != "APLICAVEL" or item.get("status") not in VALUE or item.get("criticality") not in WEIGHT:
            continue
        weight = WEIGHT[item["criticality"]]
        slot["sum"] += VALUE[item["status"]] * weight
        slot["weight"] += weight
        slot["n"] += 1
        if item.get("control_type") in kind:
            kind[item["control_type"]][0] += VALUE[item["status"]] * weight
            kind[item["control_type"]][1] += weight
    scored = {name: 100.0 * slot["sum"] / slot["weight"] for name, slot in area.items() if slot["weight"] and name in weights}
    total_weight = sum(weights[name] for name in scored)
    overall = sum(scored[name] * weights[name] for name in scored) / total_weight if total_weight else None
    n_status = sum(slot["n"] for slot in area.values())
    n_nv = sum(slot["nv"] for slot in area.values())
    coverage = 100.0 * n_status / (n_status + n_nv) if n_status + n_nv else None

    declared_areas = {a.get("id"): a for a in score_block.get("areas") or []}
    for name in weights:
        declared = declared_areas.get(name)
        if declared is None:
            err("score_lgpd.areas: área %s não declarada" % name)
            continue
        if declared.get("weight") is not None and abs(float(declared["weight"]) - weights[name]) > 0.001:
            err("área %s: peso declarado %s difere de core/scoring-engine.md (%s)" % (name, declared["weight"], weights[name]))
        if declared.get("applicability") == "NAO_APLICAVEL":
            if name in ALWAYS_APPLICABLE:
                err("área %s é sempre aplicável e está como NAO_APLICAVEL" % name)
            if name in scored:
                err("área %s está como NAO_APLICAVEL, mas tem itens avaliados" % name)
            if not declared.get("justification"):
                err("área %s NAO_APLICAVEL sem justification" % name)
            continue
        if name not in scored:
            if declared.get("score") is not None:
                err("área %s: score declarado sem nenhum item avaliado" % name)
            elif not declared.get("justification"):
                err("área %s sem item avaliado e sem justification (cobertura insuficiente)" % name)
            continue
        if declared.get("score") is None or abs(float(declared["score"]) - scored[name]) > 0.06:
            err("área %s: score declarado %s, recalculado %.1f" % (name, declared.get("score"), scored[name]))
        adjusted = 100.0 * weights[name] / total_weight
        if declared.get("adjusted_weight") is not None and abs(float(declared["adjusted_weight"]) - adjusted) > 0.011:
            err("área %s: peso ajustado declarado %s, recalculado %.2f" % (name, declared["adjusted_weight"], adjusted))
        slot = area[name]
        area_coverage = 100.0 * slot["n"] / (slot["n"] + slot["nv"])
        if declared.get("coverage") is not None and abs(float(declared["coverage"]) - area_coverage) > 0.06:
            err("área %s: cobertura declarada %s, recalculada %.1f" % (name, declared["coverage"], area_coverage))

    final_score = None
    if overall is None:
        err("nenhum item avaliado: não há score a conferir")
    else:
        final_score = half_up(overall)
        if score_block.get("score") != final_score:
            err("score global: declarado %s, recalculado %d (%.3f)" % (score_block.get("score"), final_score, overall))
        expected = band(final_score)
        critical = [f.get("id") for f in findings if f.get("severity") == "CRITICO"]
        if critical and CLASSES.index(expected) > CLASSES.index(CAP):
            expected = CAP
        if score_block.get("classification") != expected:
            err("classificação: declarada %s, esperada %s%s" % (score_block.get("classification"), expected,
                                                               " (teto por achado crítico)" if critical else ""))
    if coverage is not None and (score_block.get("coverage") is None or abs(float(score_block["coverage"]) - coverage) > 0.06):
        err("cobertura: declarada %s, recalculada %.1f" % (score_block.get("coverage"), coverage))
    for key, (total, weight) in (("score_tecnico", kind["TECNICO"]), ("score_documental", kind["DOCUMENTAL"])):
        if weight and score_block.get(key) is not None and abs(float(score_block[key]) - 100.0 * total / weight) > 0.06:
            err("%s: declarado %s, recalculado %.1f" % (key, score_block[key], 100.0 * total / weight))

    scenario = meta.get("scenario")
    if scenario and scenario != "full_audit" and not score_block.get("out_of_scope"):
        warn("cenário %s: score_lgpd.out_of_scope não lista os domínios fora do escopo" % scenario)

    # ── relatório em Markdown com os mesmos dados ────────────────────────
    if md_text is not None:
        absent = sorted(ident for ident in by_id if not re.search(r"\b%s\b" % re.escape(ident), md_text))
        if absent:
            err("relatório .md: itens do checklist ausentes: %s" % ", ".join(absent))
        absent = sorted(f.get("id") for f in findings if f.get("id") and not re.search(r"\b%s\b" % re.escape(f["id"]), md_text))
        if absent:
            err("relatório .md: achados ausentes: %s" % ", ".join(absent))
        if final_score is not None and "%d/100" % final_score not in md_text:
            err("relatório .md: não traz o score %d/100" % final_score)
        if score_block.get("classification") and "`%s`" % score_block["classification"] not in md_text:
            err("relatório .md: não traz a classificação %s" % score_block["classification"])

    summary = "%d itens (%d avaliados), %d achados, score %s" % (len(items), n_status, len(findings),
                                                               "—" if final_score is None else final_score)
    return errors, warnings, summary


def main():
    parser = argparse.ArgumentParser(description="Valida os dados de um relatório do LGPD Enterprise Auditor.")
    parser.add_argument("report")
    parser.add_argument("--framework", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                                            ".agents", "lgpd-enterprise-auditor"))
    parser.add_argument("--md")
    args = parser.parse_args()

    weights, _domains, modules, catalog, depends = load_framework(args.framework)
    if sum(weights.values()) != 100 or not catalog:
        sys.exit("Framework inválido em %s: pesos de área não somam 100 ou catálogo vazio." % args.framework)
    data = load_data(args.report)
    errors, warnings, summary = validate(data, weights, modules, catalog, read(args.md) if args.md else None, depends)

    print("Relatório: %s" % summary)
    for message in warnings:
        print("  aviso %s" % message)
    for message in errors:
        print("  ERRO  %s" % message)
    if errors:
        print("%d erro(s)." % len(errors))
        sys.exit(1)
    print("Relatório consistente com o framework.")


if __name__ == "__main__":
    main()
