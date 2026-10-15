# -*- coding: utf-8 -*-
"""Genera il PDF completo di una partita a partire da <gioco>/pdf.json.

Uso:  python games/build_game_pdf.py games/hawaii-2004 [uscita.pdf]
Richiede: markdown, weasyprint (GTK3 su Windows).
"""
import json, pathlib, re, sys
import markdown
from weasyprint import HTML

root = pathlib.Path(sys.argv[1])
cfgpath = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else root / "pdf.json"
cfg = json.loads(cfgpath.read_text(encoding="utf-8"))
out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else root / cfg["output"]
th = cfg["theme"]

css = """
@import url('%(fonts)s');
:root { --ink:%(ink)s; --head:%(head)s; --accent:%(accent)s; --paper:%(paper)s; --line:%(line)s;
        --soft:%(soft)s; --muted:%(muted)s; --cover:%(cover)s; --cover-ink:%(cover_ink)s; --cover-accent:%(cover_accent)s; }
@page { size: A4; margin: 2.2cm 2.6cm; background: var(--paper);
  @top-center { content: "%(header)s"; font: italic 9pt '%(body_font)s', serif; color: var(--accent); }
  @bottom-center { content: "— " counter(page) " —"; font: 9pt '%(body_font)s', serif; color: var(--muted); } }
@page scheda { size: A4; margin: 1.6cm 2cm; background: var(--paper);
  @top-center { content: "%(header)s"; font: italic 9pt '%(body_font)s', serif; color: var(--accent); }
  @bottom-center { content: "— " counter(page) " —"; font: 9pt '%(body_font)s', serif; color: var(--muted); } }
@page cover { margin: 0; background: var(--cover); @top-center { content: none; } @bottom-center { content: none; } }
body { font-family: '%(body_font)s', Georgia, serif; font-size: 11pt; line-height: 1.6; color: var(--ink); }
h1, h2, h3 { font-family: '%(head_font)s', Georgia, serif; font-weight: %(head_weight)s; color: var(--head); line-height: 1.15; break-after: avoid; }
h1 { font-size: 25pt; margin: 0 0 14pt; padding-bottom: 8pt; border-bottom: 1.5pt solid var(--accent); }
h2 { font-size: 15pt; margin: 20pt 0 6pt; padding-left: 9pt; border-left: 3pt solid var(--accent); }
h3 { font-size: 12.5pt; margin: 14pt 0 4pt; color: var(--ink); }
p { margin: 0 0 8pt; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 8pt; padding-left: 16pt; } li { margin-bottom: 3pt; }
strong { color: var(--ink); }
table { border-collapse: collapse; width: 100%%; font-size: 9.5pt; margin: 10pt 0; break-inside: avoid; }
table.long { break-inside: auto; }
tr { break-inside: avoid; }
thead { display: table-header-group; }
th, td { border: .6pt solid var(--line); padding: 5pt 7pt; vertical-align: top; }
th { background: var(--soft); font-family: '%(head_font)s', serif; font-weight: 400; font-size: 10.5pt; color: var(--head); text-align: left; }
tr:nth-child(even) td { background: rgba(255,255,255,.55); }
blockquote { margin: 10pt 0; padding: 8pt 12pt; border-left: 3pt solid var(--accent); background: var(--soft); font-style: italic; color: var(--muted); break-inside: avoid; }
code, pre { font-family: Consolas, monospace; font-size: 9pt; background: var(--soft); border-radius: 2pt; }
pre { padding: 8pt; white-space: pre-wrap; }
hr { border: 0; border-top: .8pt solid var(--line); margin: 14pt 0; }
.doc { break-before: page; }
.doc.scheda { page: scheda; font-size: 9.5pt; line-height: 1.45; padding: 8pt 12pt; break-inside: avoid; }
.nb { white-space: nowrap; }
.doc.scheda p.task { margin: 0 0 8pt; padding-left: 15pt; text-indent: -15pt; }
.pt { color: var(--accent); font-weight: 700; white-space: nowrap; }
.doc.scheda.missione { font-size: 11pt; line-height: 1.55; padding: 18pt 20pt; }
.doc.scheda.missione h1 { font-size: 22pt; }
.doc.scheda.missione h2 { font-size: 13pt; margin: 12pt 0 4pt; }
.doc.scheda h1 { font-size: 19pt; margin-bottom: 6pt; padding-bottom: 4pt; }
.doc.scheda h2 { font-size: 12pt; margin: 7pt 0 2pt; }
.doc.scheda p, .doc.scheda li { margin-bottom: 2pt; }
.doc.scheda ul { margin-bottom: 3pt; list-style: square; }
.doc.scheda hr { margin: 4pt 0; }
.doc.scheda p:last-child { margin-bottom: 0; }
.doc.scheda h2 { margin-top: 5pt; }
.doc.scheda, .doc.invito, .doc.indizio { border: 1.2pt solid var(--accent); outline: .5pt solid var(--accent); outline-offset: 3pt; }
.doc.invito, .doc.indizio { padding: 18pt 20pt; }
.doc.invito { text-align: center; padding-top: 24pt; padding-bottom: 14pt; font-size: 11pt; line-height: 1.45; }
.doc.guida { font-size: 9.8pt; line-height: 1.45; }
.striscia { margin: 4pt 0 10pt; }
.striscia svg { width: 100%%; height: auto; }
.doc.guida h1 { font-size: 20pt; margin-bottom: 8pt; }
.doc.guida h2 { font-size: 12.5pt; margin: 9pt 0 3pt; }
.doc.guida table { font-size: 8.2pt; margin: 4pt 0; }
.doc.guida th, .doc.guida td { padding: 2pt 5pt; }
.doc.guida p, .doc.guida li { margin-bottom: 3pt; }
.doc.invito h1 { border: 0; font-size: 30pt; }
.doc.invito ul { list-style: none; padding: 0; }
.doc.indizio { background: rgba(255,255,255,.6); break-before: auto; break-inside: avoid; margin: 0 0 14pt; padding: 14pt 18pt; }
.part { break-before: page; break-after: page; text-align: center; padding-top: 8cm; }
.part h1 { font-size: 28pt; border: 0; } .part .orn { color: var(--accent); font-size: 18pt; letter-spacing: 8pt; }
.cover { page: cover; break-after: page; color: var(--cover-ink); text-align: center; height: 297mm; padding: 6.5cm 2.5cm 0; box-sizing: border-box; }
.cover .kicker { font: 600 11pt '%(body_font)s', serif; letter-spacing: 6pt; text-transform: uppercase; color: var(--cover-accent); }
.cover h1 { color: var(--cover-ink); border: 0; font-size: 40pt; margin: 18pt 0 10pt; }
.cover .sub { font: italic 13pt '%(body_font)s', serif; color: var(--cover-accent); }
.cover .rule { width: 60pt; height: 1.5pt; background: var(--cover-accent); margin: 20pt auto; }
.cover.fig { padding-top: 2.4cm; }
.cover img.ritratto { width: 6cm; height: 8cm; object-fit: cover; border: 1.5pt solid var(--cover-accent); border-radius: 4pt; margin-bottom: 8pt; }
.cover.fig .warn { margin-top: 1.4cm; }
table.galleria { border-collapse: separate; border-spacing: 5pt; margin: 8pt 0; }
table.galleria td { border: 0; background: none !important; text-align: center; width: 25%%; padding: 0; font-size: 8pt; line-height: 1.3; }
table.galleria img { width: 100%%; height: auto; border: .6pt solid var(--line); border-radius: 3pt; }
table.galleria b { display: block; font-size: 8.6pt; color: var(--ink); margin-top: 2pt; }
table.galleria td.tu img { border: 2pt solid var(--head); }
.cover .warn { margin: 5cm auto 0; max-width: 11cm; border: .8pt solid var(--cover-accent); padding: 10pt 14pt; font-size: 9pt; color: var(--cover-ink); text-align: left; }
""" % dict(th, header=cfg["header"])

esc = lambda s: s.replace("'", "&#8217;")
_img = (f'<img class="ritratto" src="{cfg["cover_image"]}">' if cfg.get("cover_image") else "")
parts = [f'<div class="cover{" fig" if _img else ""}">{_img}<div class="kicker">{esc(cfg["kicker"])}</div><h1>{esc(cfg["title"])}</h1>'
         f'<div class="rule"></div><div class="sub">{esc(cfg["subtitle"])}</div>'
         f'<div class="warn">{esc(cfg["warn"])}</div></div>']

md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "nl2br"])
item = re.compile(r"\s*([-*▢]|\d+\.)\s")
for sec in cfg["sections"]:
    if sec["title"]:
        parts.append(f'<div class="part"><div class="orn">◆ ◆ ◆</div><h1>{esc(sec["title"])}</h1></div>')
    files = []
    for f in sec["files"]:
        files += [f"{f['prefix']}{i}{f['suffix']}" for i in f["range"]] if isinstance(f, dict) else [f]
    for f in files:
        text = (root / f).read_text(encoding="utf-8")
        lines, prev = [], ""
        for ln in text.split("\n"):
            if item.match(ln) and prev.strip() and not item.match(prev) and not prev.lstrip().startswith(("|", "#", ">")):
                lines.append("")
            if ln.startswith("▢"):
                lines.append("")
            lines.append(ln)
            prev = ln
        md.reset()
        kind = ("invito" if f.endswith("_invito.md")
                else "scheda missione" if f.endswith("_missione.md")
                else "guida" if f.endswith(("regole_giocatore.md", "piantina.md")) or "/striscia_" in f
                else "scheda" if "scheda_personaggio" in f
                else "indizio" if f.startswith(("indizi/", "oggetti/", "scene/", "enigmi/")) else "")
        body = md.convert(chr(10).join(lines))
        body = re.sub(r"<table>(.*?)</table>", lambda m: ("<table class=\"long\">" if m.group(1).count("<tr>") > 8 else "<table>") + m.group(1) + "</table>", body, flags=re.S)
        body = body.replace("<p>▢", "<p class=\"task\">▢")
        body = re.sub(r"\((\d+) punti\)", r'<span class="pt">(\1 punti)</span>', body)
        body = re.sub(r"(\d{1,2}:\d{2}(?::\d{2})?)(\s?–\s?)(\d{1,2}:\d{2}(?::\d{2})?)", r'<span class="nb">\1\2\3</span>', body)
        if f.endswith("scheda_personaggio.md"):
            body = body.replace("<h2>Cosa dirai al tenente</h2>", "<h2 style=\"break-before: page\">Cosa dirai al tenente</h2>")
        parts.append(f'<div class="doc {kind}">{body}</div>')

html = f"<html lang='it'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(parts)}</body></html>"
HTML(string=html, base_url=str(root)).write_pdf(str(out))
print("scritto", out, out.stat().st_size // 1024, "KB")
