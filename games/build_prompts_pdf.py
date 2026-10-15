"""PDF semplice dei prompt per le immagini (pagine strette, leggibili sul cellulare).
Uso: python games/build_prompts_pdf.py games/hawaii-2004
"""
import sys
from pathlib import Path
from weasyprint import HTML, CSS

root = Path(sys.argv[1]) / "immagini"
css = CSS(string="""
@page{size:120mm 200mm;margin:8mm 7mm}
:root{--paper:#fff;--ink:#1C1B29;--card:#fff;--line:#bbb;--mut:#555;--head:#B3125B;--accent:#0F6B6B}
body{font:9.5pt/1.4 Georgia,serif;background:#fff;color:#1C1B29}
main{max-width:none;padding:0}
.bar,button,.ok{display:none!important}body{background:#fff!important}
h1{font-size:19pt}h2{font-size:13pt;margin-top:10pt;break-after:avoid}
.card{break-inside:avoid;border:1px solid #bbb;border-radius:6px;padding:5pt;margin:5pt 0}
.top small{font-size:8pt}
.pr{font:8.8pt/1.35 Arial,sans-serif;user-select:auto}
table{font-size:8.5pt}
""")
HTML(str(root / "PROMPTS.html")).write_pdf(str(root / "PROMPTS.pdf"), stylesheets=[css])
print("scritto", root / "PROMPTS.pdf")
