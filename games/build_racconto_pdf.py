"""Build the Hal novella PDF (A5, book layout) from racconto-hal.md."""
import html, re, sys
from pathlib import Path
from weasyprint import HTML

src = Path(sys.argv[1]); out = Path(sys.argv[2])
body = []
for block in re.split(r"\n\s*\n", src.read_text(encoding="utf-8").strip()):
    b = block.strip()
    if b.startswith("# "): body.append(f"<h1>{html.escape(b[2:])}</h1>")
    elif b.startswith("## "): body.append(f"<h2>{html.escape(b[3:])}</h2>")
    elif b == "***": body.append('<p class="sep">&#10086;</p>')
    else:
        t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html.escape(b, quote=False))
        cls = ' class="sub"' if b.startswith("*Un racconto") else ""
        body.append(f"<p{cls}>{t}</p>")
css = """
@page { size: A5; margin: 20mm 17mm 22mm 17mm;
  @bottom-center { content: counter(page); font: 9pt Georgia, serif; color: #666; } }
@page :first { @bottom-center { content: none; } }
body { font: 11pt/1.55 Georgia, 'Times New Roman', serif; color: #1a1a1a; hyphens: auto; }
h1 { font-size: 26pt; text-align: center; margin: 60mm 0 6mm; letter-spacing: .04em; }
p.sub { text-align: center; color: #555; text-indent: 0; margin-bottom: 0; }
h2 { font-size: 15pt; text-align: center; margin: 0 0 10mm; page-break-before: always; font-variant: small-caps; letter-spacing: .08em; }
h1 + p + h2 { page-break-before: always; }
p { margin: 0; text-align: justify; text-indent: 1.2em; orphans: 3; widows: 3; }
h2 + p, p.sep + p { text-indent: 0; }
p.sep { text-align: center; text-indent: 0; margin: 5mm 0; color: #777; }
"""
HTML(string=f"<html lang='it'><head><meta charset='utf-8'><style>{css}</style></head><body>{''.join(body)}</body></html>").write_pdf(out)
