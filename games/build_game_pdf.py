# -*- coding: utf-8 -*-
"""Genera il PDF completo di una partita a partire da <gioco>/pdf.json.

Uso:  python games/build_game_pdf.py games/hawaii-2004 [uscita.pdf]
Richiede: markdown, weasyprint (GTK3 su Windows).
"""
import json, pathlib, re, sys
import markdown
from weasyprint import HTML

root = pathlib.Path(sys.argv[1])
cfg = json.loads((root / "pdf.json").read_text(encoding="utf-8"))
out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else root / cfg["output"]
th = cfg["theme"]

css = """
@import url('%(fonts)s');
:root { --ink:%(ink)s; --head:%(head)s; --accent:%(accent)s; --paper:%(paper)s; --line:%(line)s;
        --soft:%(soft)s; --muted:%(muted)s; --cover:%(cover)s; --cover-ink:%(cover_ink)s; --cover-accent:%(cover_accent)s; }
@page { size: A4; margin: 2.2cm 2cm; background: var(--paper);
  @top-center { content: "%(header)s"; font: italic 9pt '%(body_font)s', serif; color: var(--accent); }
  @bottom-center { content: "— " counter(page) " —"; font: 9pt '%(body_font)s', serif; color: var(--muted); } }
@page cover { margin: 0; background: var(--cover); @top-center { content: none; } @bottom-center { content: none; } }
body { font-family: '%(body_font)s', Georgia, serif; font-size: 10.5pt; line-height: 1.6; color: var(--ink); }
h1, h2, h3 { font-family: '%(head_font)s', Georgia, serif; font-weight: %(head_weight)s; color: var(--head); line-height: 1.15; break-after: avoid; }
h1 { font-size: 25pt; margin: 0 0 14pt; padding-bottom: 8pt; border-bottom: 1.5pt solid var(--accent); }
h2 { font-size: 15pt; margin: 20pt 0 6pt; padding-left: 9pt; border-left: 3pt solid var(--accent); }
h3 { font-size: 12.5pt; margin: 14pt 0 4pt; color: var(--ink); }
p { margin: 0 0 8pt; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 8pt; padding-left: 16pt; } li { margin-bottom: 3pt; }
strong { color: var(--ink); }
table { border-collapse: collapse; width: 100%%; font-size: 9.5pt; margin: 10pt 0; break-inside: avoid; }
th, td { border: .6pt solid var(--line); padding: 5pt 7pt; vertical-align: top; }
th { background: var(--soft); font-family: '%(head_font)s', serif; font-size: 10.5pt; color: var(--head); text-align: left; }
tr:nth-child(even) td { background: rgba(255,255,255,.55); }
blockquote { margin: 10pt 0; padding: 8pt 12pt; border-left: 3pt solid var(--accent); background: var(--soft); font-style: italic; color: var(--muted); break-inside: avoid; }
code, pre { font-family: Consolas, monospace; font-size: 9pt; background: var(--soft); border-radius: 2pt; }
pre { padding: 8pt; white-space: pre-wrap; }
hr { border: 0; border-top: .8pt solid var(--line); margin: 14pt 0; }
.doc { break-before: page; }
.doc.scheda { font-size: 9pt; line-height: 1.38; padding: 10pt 14pt; break-inside: avoid; }
.doc.scheda h1 { font-size: 19pt; margin-bottom: 6pt; padding-bottom: 4pt; }
.doc.scheda h2 { font-size: 12pt; margin: 7pt 0 2pt; }
.doc.scheda p, .doc.scheda li { margin-bottom: 2pt; }
.doc.scheda ul { margin-bottom: 3pt; list-style: square; }
.doc.scheda, .doc.invito, .doc.indizio { border: 1.2pt solid var(--accent); outline: .5pt solid var(--accent); outline-offset: 3pt; }
.doc.invito, .doc.indizio { padding: 18pt 20pt; }
.doc.invito { text-align: center; padding-top: 60pt; font-size: 12pt; }
.doc.invito h1 { border: 0; font-size: 30pt; }
.doc.invito ul { list-style: none; padding: 0; }
.doc.indizio { background: rgba(255,255,255,.6); }
.part { break-before: page; text-align: center; padding-top: 8cm; }
.part h1 { font-size: 28pt; border: 0; } .part .orn { color: var(--accent); font-size: 18pt; letter-spacing: 8pt; }
.cover { page: cover; break-after: page; color: var(--cover-ink); text-align: center; height: 297mm; padding: 6.5cm 2.5cm 0; box-sizing: border-box; }
.cover .kicker { font: 600 11pt '%(body_font)s', serif; letter-spacing: 6pt; text-transform: uppercase; color: var(--cover-accent); }
.cover h1 { color: var(--cover-ink); border: 0; font-size: 40pt; margin: 18pt 0 10pt; }
.cover .sub { font: italic 13pt '%(body_font)s', serif; color: var(--cover-accent); }
.cover .rule { width: 60pt; height: 1.5pt; background: var(--cover-accent); margin: 20pt auto; }
.cover .warn { margin: 5cm auto 0; max-width: 11cm; border: .8pt solid var(--cover-accent); padding: 10pt 14pt; font-size: 9pt; color: var(--cover-ink); text-align: left; }
""" % dict(th, header=cfg["header"])

esc = lambda s: s.replace("'", "&#8217;")
parts = [f'<div class="cover"><div class="kicker">{esc(cfg["kicker"])}</div><h1>{esc(cfg["title"])}</h1>'
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
            lines.append(ln + "  " if ln.startswith("▢") else ln)
            prev = ln
        md.reset()
        kind = ("invito" if f.endswith("_invito.md")
                else "scheda" if ("scheda_personaggio" in f or f.endswith("_missione.md"))
                else "indizio" if f.startswith(("indizi/", "oggetti/")) else "")
        parts.append(f'<div class="doc {kind}">{md.convert(chr(10).join(lines))}</div>')

html = f"<html lang='it'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(parts)}</body></html>"
HTML(string=html, base_url=str(root)).write_pdf(str(out))
print("scritto", out, out.stat().st_size // 1024, "KB")
