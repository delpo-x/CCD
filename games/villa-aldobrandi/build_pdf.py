import pathlib, sys, re, markdown
from weasyprint import HTML

root = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])

sections = [
    ("Panoramica", ["README.md"]),
    ("Parte 1 - Per l'Ospite (spoiler)", [
        "gioco/guida_ospite.md", "gioco/soluzione.md", "gioco/riferimento_indizi.md"]),
    ("Parte 2 - Vittima e detective", [
        "personaggi/scheda_vittima.md", "personaggi/scheda_detective.md"]),
    ("Parte 3 - Inviti e schede dei sospetti", [
        f"personaggi/Character_{i}_{k}.md" for i in range(1, 7) for k in ("invito", "scheda_personaggio")]),
    ("Parte 4 - Indizi", [f"indizi/indizio_{n:02d}.md" for n in range(1, 11)]),
    ("Parte 5 - Prompt per le immagini", ["immagini/PROMPTS.md"]),
]

css = """
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Libre+Baskerville:wght@400;700&display=swap');
:root { --ink:#450A0A; --burg:#7C2D12; --gold:#A16207; --paper:#FBF6EE; --line:#E3D3B8; --muted:#5B4A44; }
@page { size: A4; margin: 2.2cm 2cm 2.2cm; background: #FBF6EE;
  @top-center { content: "Il Brindisi di Villa Aldobrandi"; font: italic 9pt 'Cormorant Garamond', serif; color: #A16207; }
  @bottom-center { content: "— " counter(page) " —"; font: 9pt 'Cormorant Garamond', serif; color: #5B4A44; } }
@page cover { margin: 0; background: #450A0A; @top-center { content: none; } @bottom-center { content: none; } }
body { font-family: 'Libre Baskerville', Georgia, serif; font-size: 10.5pt; line-height: 1.6; color: var(--ink); }
h1, h2, h3 { font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 700; color: var(--burg); line-height: 1.15; break-after: avoid; }
h1 { font-size: 26pt; margin: 0 0 14pt; padding-bottom: 8pt; border-bottom: 1.5pt solid var(--gold); letter-spacing: .3pt; }
h2 { font-size: 16pt; margin: 20pt 0 6pt; padding-left: 9pt; border-left: 3pt solid var(--gold); }
h3 { font-size: 13pt; margin: 14pt 0 4pt; color: var(--ink); }
p { margin: 0 0 8pt; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 8pt; padding-left: 16pt; } li { margin-bottom: 3pt; }
strong { color: var(--ink); }
table { border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 10pt 0; break-inside: avoid; }
th, td { border: .6pt solid var(--line); padding: 5pt 7pt; vertical-align: top; }
th { background: #F1E4CC; font-family: 'Cormorant Garamond', serif; font-size: 11pt; color: var(--burg); text-align: left; }
tr:nth-child(even) td { background: #FFFBF3; }
blockquote { margin: 10pt 0; padding: 8pt 12pt; border-left: 3pt solid var(--gold); background: #F6EBD6; font-style: italic; color: var(--muted); break-inside: avoid; }
code, pre { font-family: Consolas, monospace; font-size: 9pt; background: #F1E4CC; border-radius: 2pt; }
pre { padding: 8pt; white-space: pre-wrap; }
hr { border: 0; border-top: .8pt solid var(--line); margin: 14pt 0; }
.doc { break-before: page; }
.doc.scheda { font-size: 9pt; line-height: 1.38; padding: 10pt 14pt; break-inside: avoid; }
.doc.scheda h1 { font-size: 20pt; margin-bottom: 6pt; padding-bottom: 4pt; }
.doc.scheda h2 { font-size: 12.5pt; margin: 7pt 0 2pt; }
.doc.scheda p, .doc.scheda li { margin-bottom: 2pt; }
.doc.scheda ul { margin-bottom: 3pt; }
.doc.invito ul { list-style: none; padding: 0; }
.doc.scheda, .doc.invito, .doc.indizio { border: 1.2pt solid var(--gold); padding: 18pt 20pt; outline: .5pt solid var(--gold); outline-offset: 3pt; }
.doc.invito { text-align: center; padding-top: 60pt; font-size: 12pt; }
.doc.invito h1 { border: 0; font-size: 30pt; }
.doc.indizio { background: #FFFDF8; }
.doc.scheda ul { list-style: square; }
.part { break-before: page; text-align: center; padding-top: 8cm; }
.part h1 { font-size: 30pt; border: 0; } .part .orn { color: var(--gold); font-size: 20pt; letter-spacing: 8pt; }
.cover { page: cover; break-after: page; color: #FBF6EE; text-align: center; height: 297mm; padding: 6.5cm 2.5cm 0; box-sizing: border-box; }
.cover .kicker { font: 600 12pt 'Cormorant Garamond', serif; letter-spacing: 6pt; text-transform: uppercase; color: #E3C58A; }
.cover h1 { color: #FBF6EE; border: 0; font-size: 42pt; margin: 18pt 0 10pt; }
.cover .sub { font: italic 14pt 'Cormorant Garamond', serif; color: #E3C58A; }
.cover .rule { width: 60pt; height: 1.5pt; background: #A16207; margin: 20pt auto; }
.cover .warn { margin: 5cm auto 0; max-width: 11cm; border: .8pt solid #A16207; padding: 10pt 14pt; font-size: 9pt; color: #F1E4CC; text-align: left; }
"""

parts = ['<div class="cover"><div class="kicker">Murder mystery party</div><h1>Il Brindisi di Villa Aldobrandi</h1>'
         '<div class="rule"></div><div class="sub">6 giocatori + 1 ospite · 90 minuti · Lago d&#8217;Orta</div>'
         '<div class="warn"><b>Attenzione, spoiler.</b> Questo è il volume completo dell&#8217;ospite: contiene soluzione, colpevole e indizi. '
         'Ai giocatori stampa solo inviti, schede personaggio e indizi.</div></div>']

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists"])
for title, files in sections:
    if title != "Panoramica":
        parts.append(f'<div class="part"><div class="orn">◆ ◆ ◆</div><h1>{title}</h1></div>')
    for f in files:
        text = (root / f).read_text(encoding="utf-8")
        item = re.compile(r"\s*([-*▢]|\d+\.)\s")
        lines, prev = [], ""
        for ln in text.split("\n"):
            if item.match(ln) and prev.strip() and not item.match(prev) and not prev.lstrip().startswith(("|", "#", ">")):
                lines.append("")
            lines.append(ln + "  " if ln.startswith("▢") else ln)
            prev = ln
        text = "\n".join(lines)
        md.reset()
        kind = "invito" if f.endswith("_invito.md") else "scheda" if "scheda_personaggio" in f else "indizio" if f.startswith("indizi/") else ""
        parts.append(f'<div class="doc {kind}">{md.convert(text)}</div>')

html = f"<html lang='it'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(parts)}</body></html>"
HTML(string=html, base_url=str(root)).write_pdf(str(out))
print("scritto", out, out.stat().st_size // 1024, "KB")
