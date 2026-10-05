#!/usr/bin/env python3
"""Produit un fichier Word (.docx) à partir d'un texte normatif, avec ou sans marques de révision.

Usage :
    # Correction : les écarts entre les deux textes deviennent des révisions Word (suivi des modifications)
    python3 redline_docx.py --original projet.txt --revise corrige.txt --sortie projet-corrige.docx

    # Rédaction : document propre, sans révision
    python3 redline_docx.py --revise projet.txt --sortie projet.docx

Options : --auteur (nom affiché dans Word, par défaut « Relecture légistique »).

Chaque ligne non vide du fichier texte devient un paragraphe. Les révisions sont calculées paragraphe par
paragraphe, puis mot par mot à l'intérieur d'un paragraphe modifié : dans Word, « Refuser toutes les
modifications » redonne le texte d'origine et « Accepter toutes les modifications » le texte corrigé. Le
suivi des modifications reste activé dans le document produit.

Préparer les deux fichiers en texte brut, sans Markdown (pas de « > », « ** », « # ») : les marques
« > » en début de ligne et « ** » sont retirées par précaution. Seule la bibliothèque standard de
Python 3.8+ est utilisée.
"""
import argparse
import datetime
import difflib
import re
import zipfile
from xml.sax.saxutils import escape

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


class Doc:
    def __init__(self, auteur):
        self.auteur = escape(auteur, {'"': "&quot;"})
        self.date = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        self.next_id = 1
        self.paragraphs = []

    def _id(self):
        self.next_id += 1
        return self.next_id

    def _attrs(self):
        return f'w:id="{self._id()}" w:author="{self.auteur}" w:date="{self.date}"'

    @staticmethod
    def _run(text, deleted=False):
        tag = "w:delText" if deleted else "w:t"
        return f'<w:r><{tag} xml:space="preserve">{escape(text)}</{tag}></w:r>'

    def ins(self, text):
        return f"<w:ins {self._attrs()}>{self._run(text)}</w:ins>" if text else ""

    def dele(self, text):
        return f"<w:del {self._attrs()}>{self._run(text, deleted=True)}</w:del>" if text else ""

    @staticmethod
    def _ppr(text, mark=""):
        t = text.strip()
        centre = bool(re.match(r"^(?:Article \d+(?:er)?(?: (?:bis|ter|quater))?|Article unique|"
                               r"(?:TITRE|CHAPITRE|Section|LIVRE)\b.*|D[ée]cr[èe]te\s?:|Arr[êe]te\s?:)$", t))
        jc = '<w:jc w:val="center"/>' if centre else '<w:jc w:val="both"/>'
        return f"<w:pPr><w:spacing w:after=\"120\"/>{jc}{mark}</w:pPr>"

    def add_equal(self, text):
        self.paragraphs.append(f"<w:p>{self._ppr(text)}{self._run(text)}</w:p>")

    def add_inserted(self, text):
        mark = f"<w:rPr><w:ins {self._attrs()}/></w:rPr>"
        self.paragraphs.append(f"<w:p>{self._ppr(text, mark)}{self.ins(text)}</w:p>")

    def add_deleted(self, text):
        mark = f"<w:rPr><w:del {self._attrs()}/></w:rPr>"
        self.paragraphs.append(f"<w:p>{self._ppr(text, mark)}{self.dele(text)}</w:p>")

    def add_changed(self, old, new):
        tok = lambda s: re.findall(r"\w+|\s+|[^\w\s]", s)
        a, b = tok(old), tok(new)
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        runs = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                runs.append(self._run("".join(a[i1:i2])))
            else:
                runs.append(self.dele("".join(a[i1:i2])))
                runs.append(self.ins("".join(b[j1:j2])))
        self.paragraphs.append(f"<w:p>{self._ppr(new)}{''.join(runs)}</w:p>")

    def document_xml(self):
        body = "".join(self.paragraphs)
        sect = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
                '<w:pgMar w:top="1417" w:right="1417" w:bottom="1417" w:left="1417" w:header="708" '
                'w:footer="708" w:gutter="0"/></w:sectPr>')
        return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                f'<w:document xmlns:w="{W_NS}"><w:body>{body}{sect}</w:body></w:document>')


def read_lines(path):
    lines = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = re.sub(r"^\s*>\s?", "", line.rstrip("\n")).replace("**", "").rstrip()
            if line.strip():
                lines.append(line.strip())
    return lines


def similarity(x, y):
    return difflib.SequenceMatcher(None, x, y, autojunk=False).ratio()


def build(doc, old_lines, new_lines):
    sm = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for line in new_lines[j1:j2]:
                doc.add_equal(line)
        elif op == "delete":
            for line in old_lines[i1:i2]:
                doc.add_deleted(line)
        elif op == "insert":
            for line in new_lines[j1:j2]:
                doc.add_inserted(line)
        else:
            # Apparier les paragraphes proches (réécriture) ; les autres sont supprimés ou insérés.
            olds, news = old_lines[i1:i2], new_lines[j1:j2]
            i = j = 0
            while i < len(olds) or j < len(news):
                if i < len(olds) and j < len(news) and similarity(olds[i], news[j]) >= 0.4:
                    doc.add_changed(olds[i], news[j]); i += 1; j += 1
                elif i < len(olds) and (j >= len(news) or
                                        any(similarity(olds[i], n) >= 0.4 for n in news[j + 1:])):
                    # le paragraphe d'origine correspond à un paragraphe plus loin : insérer d'abord
                    if j < len(news):
                        doc.add_inserted(news[j]); j += 1
                    else:
                        doc.add_deleted(olds[i]); i += 1
                elif i < len(olds):
                    doc.add_deleted(olds[i]); i += 1
                else:
                    doc.add_inserted(news[j]); j += 1


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
</Types>"""
ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""
DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>"""
STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W_NS}"><w:docDefaults><w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
<w:sz w:val="24"/><w:lang w:val="fr-FR"/></w:rPr></w:rPrDefault></w:docDefaults></w:styles>"""


def settings(track):
    flag = "<w:trackRevisions/>" if track else ""
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<w:settings xmlns:w="{W_NS}">{flag}<w:defaultTabStop w:val="708"/></w:settings>')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--original", help="texte d'origine (omettre pour un document propre)")
    ap.add_argument("--revise", required=True, help="texte corrigé ou rédigé")
    ap.add_argument("--sortie", required=True, help="chemin du .docx à produire")
    ap.add_argument("--auteur", default="Relecture légistique")
    args = ap.parse_args()

    doc = Doc(args.auteur)
    new_lines = read_lines(args.revise)
    if args.original:
        build(doc, read_lines(args.original), new_lines)
    else:
        for line in new_lines:
            doc.add_equal(line)

    with zipfile.ZipFile(args.sortie, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", ROOT_RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/document.xml", doc.document_xml())
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/settings.xml", settings(bool(args.original)))
    n_rev = doc.next_id - 1
    print(f"{args.sortie} : {len(new_lines)} paragraphes, {n_rev} marque(s) de révision.")


if __name__ == "__main__":
    main()
