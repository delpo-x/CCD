"""Costruisce PROMPTS.html (pagina unica per cellulare) da immagini/PROMPTS.md.

Uso: python games/build_prompts_html.py games/hawaii-2004
Ogni prompt ha un pulsante «Copia» che copia il testo completo, con i blocchi
[STYLE], [PORTRAIT] e [OBJECT] già espansi, e una casella «fatto» salvata nel browser.
"""
import html
import re
import sys
from pathlib import Path

root = Path(sys.argv[1]) / "immagini"
md = (root / "PROMPTS.md").read_text(encoding="utf-8").replace("\r\n", "\n")

# blocchi comuni: **[NOME]** (...)\n> testo
blocks = dict(re.findall(r"\*\*\[(\w+)\]\*\*[^\n]*\n> ([^\n]+)", md))


def expand(p):
    for k, v in blocks.items():
        p = p.replace("[%s]" % k, v if k == "STYLE" else v + ".")
    return p


def full(prompt, section, fname):
    """Rende il prompt autosufficiente: formato, epoca, niente testo, negativo."""
    neg = blocks.get("NEG", "")
    sec = section.lower()
    if fname.startswith("copertina"):
        fmt = "vertical 2:3 poster, at least 1600x2400 px"
        neg = ", ".join(x for x in neg.split(", ") if x not in ("text", "letters", "captions", "logo"))
        txt = "The only readable text allowed is the one named above."
    else:
        if "ritratti" in sec:
            fmt = "vertical 3:4, at least 1024x1365 px"
        elif "luoghi" in sec:
            fmt = "horizontal 16:9, at least 1920x1080 px"
        else:
            fmt = "horizontal 4:3, at least 1600x1200 px"
        txt = "No readable text, letters or numbers anywhere in the image: any paper, label or screen shows only blurred, illegible marks."
    extra = ""
    if "ritratti" in sec:
        extra = (" Same neutral, guarded, slightly defensive expression as every other character: "
                 "no guilty look, no sinister smile, no hidden hands, no dramatic shadows across the face. "
                 "If a reference image is attached, keep exactly the same person, with the same face and hair.")
    return ("%s Image format: %s. Setting: Honolulu, August 2004: no smartphones, no flat screens, no modern cars, no earbuds. %s%s Avoid: %s."
            % (prompt.rstrip().rstrip(".") + ".", fmt, txt, extra, neg))


def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def render_text(lines):
    out, i = [], 0
    while i < len(lines):
        l = lines[i]
        if not l.strip() or l.strip() == "---":
            i += 1
        elif l.startswith("```"):
            j = i + 1
            while not lines[j].startswith("```"):
                j += 1
            out.append("<pre>%s</pre>" % html.escape("\n".join(lines[i + 1:j])))
            i = j + 1
        elif l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| ]+\|$", lines[i]):
                    rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            t = "<div class='tw'><table>"
            for n, r in enumerate(rows):
                tag = "th" if n == 0 else "td"
                t += "<tr>%s</tr>" % "".join("<%s>%s</%s>" % (tag, inline(c), tag) for c in r)
            out.append(t + "</table></div>")
        elif re.match(r"^(\d+\.|-) ", l):
            ordered = l[0].isdigit()
            items = []
            while i < len(lines) and re.match(r"^(\d+\.|-) ", lines[i]):
                items.append(re.sub(r"^(\d+\.|-) ", "", lines[i]))
                i += 1
            tag = "ol" if ordered else "ul"
            out.append("<%s>%s</%s>" % (tag, "".join("<li>%s</li>" % inline(x) for x in items), tag))
        elif l.startswith("> "):
            out.append("<blockquote>%s</blockquote>" % inline(l[2:]))
            i += 1
        else:
            out.append("<p>%s</p>" % inline(l))
            i += 1
        continue
    return "\n".join(out)


# spezza in sezioni "## " e, dentro, in carte "### N · `file` – titolo"
parts = re.split(r"\n(?=## )", md)
head = parts[0]
body = []
n_cards = 0
for sec in parts[1:]:
    lines = sec.split("\n")
    title = lines[0][3:]
    cards = re.split(r"\n(?=### )", "\n".join(lines[1:]))
    intro = cards[0].split("\n")
    out = ["<section><h2>%s</h2>" % inline(title), render_text(intro)]
    for c in cards[1:]:
        cl = c.split("\n")
        m = re.match(r"### (\d+) · `([^`]+)`\s*(?:–\s*(.*))?", cl[0])
        if not m:  # sottotitolo semplice
            out.append("<h3>%s</h3>%s" % (inline(cl[0][4:]), render_text(cl[1:])))
            continue
        num, fname, label = m.groups()
        q = [x for x in cl[1:] if x.startswith("> ")]
        prompt = full(expand(q[0][2:]), title, fname) if q else ""
        n_cards += 1
        out.append(
            "<article class='card' data-id='%s'>"
            "<div class='top'><span class='n'>%s</span><div><b>%s</b><small>%s</small></div>"
            "<label class='ok'><input type='checkbox'> fatto</label></div>"
            "<p class='pr'>%s</p>"
            "<button class='cp' type='button'>Copia prompt</button></article>"
            % (html.escape(fname), num, inline(label or fname), html.escape(fname), html.escape(prompt))
        )
    out.append("</section>")
    body.append("\n".join(out))

neg = blocks.get("NEG", "")
page = """<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Prompt immagini · Last Call al Kapu Lounge</title>
<style>
:root{--ink:#1C1B29;--head:#B3125B;--accent:#0F6B6B;--paper:#F7F3EA;--card:#fff;--line:#d9d2c2;--mut:#5b5870}
@media (prefers-color-scheme:dark){:root{--ink:#F1ECE0;--head:#FF6FAE;--accent:#4FC7C7;--paper:#12112B;--card:#1d1c3a;--line:#34325c;--mut:#a9a6c4}}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.55 Merriweather,Georgia,serif}
main{max-width:760px;margin:0 auto;padding:16px 16px 80px}
h1{font:400 30px/1.15 'Abril Fatface',Georgia,serif;color:var(--head);margin:8px 0 4px}
h2{font:400 24px/1.2 'Abril Fatface',Georgia,serif;color:var(--head);margin:36px 0 10px;border-bottom:2px solid var(--line);padding-bottom:6px}
h3{font-size:17px;margin:20px 0 6px}
p,li{margin:.5em 0}
code,pre{font:14px/1.45 ui-monospace,Consolas,monospace;background:rgba(127,127,127,.15);border-radius:4px}
code{padding:1px 5px}pre{padding:10px;overflow:auto}
blockquote{margin:8px 0;padding:10px 12px;border-left:4px solid var(--accent);background:rgba(127,127,127,.1);font-size:15px}
.tw{overflow:auto}table{border-collapse:collapse;font-size:15px}td,th{border:1px solid var(--line);padding:6px 8px;text-align:left}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;margin:14px 0}
.card.done{opacity:.55}
.top{display:flex;gap:10px;align-items:flex-start}
.top>div{flex:1;min-width:0}.top b{display:block}.top small{color:var(--mut);font:13px ui-monospace,Consolas,monospace;word-break:break-all}
.n{background:var(--head);color:#fff;border-radius:8px;min-width:34px;padding:2px 6px;text-align:center;font:700 14px sans-serif}
.ok{font:14px sans-serif;white-space:nowrap;min-height:44px;display:flex;align-items:center;gap:6px}
.ok input{width:22px;height:22px}
.pr{font:15px/1.5 -apple-system,Segoe UI,sans-serif;background:rgba(127,127,127,.1);border-radius:8px;padding:10px;user-select:all}
button.cp{width:100%;min-height:48px;border:0;border-radius:10px;background:var(--accent);color:#fff;font:700 16px sans-serif;cursor:pointer}
button.cp:focus-visible,.ok input:focus-visible{outline:3px solid var(--head);outline-offset:2px}
button.cp.ok2{background:var(--head)}
.bar{position:sticky;top:0;background:var(--paper);padding:8px 0;font:14px sans-serif;color:var(--mut);border-bottom:1px solid var(--line);z-index:2}
</style></head><body><main>
<h1>Prompt per le immagini</h1>
<div class="bar"><span id="cnt">0</span> di @@n@@ fatti · le spunte restano su questo telefono</div>
@@head@@
<h3>Negativo (da incollare nel campo «negative prompt»)</h3>
<p class="pr">@@neg@@</p>
<button class="cp" type="button" data-t="@@negattr@@">Copia negativo</button>
@@body@@
</main>
<script>
const K='kapu-prompts-v1';let st={};try{st=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){}
function save(){try{localStorage.setItem(K,JSON.stringify(st))}catch(e){}}
function upd(){document.getElementById('cnt').textContent=document.querySelectorAll('.card.done').length}
document.querySelectorAll('.card').forEach(c=>{
 const id=c.dataset.id,cb=c.querySelector('input');
 if(st[id]){cb.checked=true;c.classList.add('done')}
 cb.onchange=()=>{c.classList.toggle('done',cb.checked);st[id]=cb.checked;save();upd()};
 c.querySelector('button').onclick=e=>cp(e.target,c.querySelector('.pr').textContent)});
document.querySelectorAll('button[data-t]').forEach(b=>b.onclick=()=>cp(b,b.dataset.t));
function cp(b,t){const done=()=>{const o=b.textContent;b.textContent='Copiato';b.classList.add('ok2');setTimeout(()=>{b.textContent=o;b.classList.remove('ok2')},1400)};
 if(navigator.clipboard)navigator.clipboard.writeText(t).then(done,()=>fb(t,done));else fb(t,done)}
function fb(t,d){const a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}a.remove();d()}
upd();
</script></body></html>
"""
head_html = render_text(head.split("\n")[1:])
vals = dict(n=str(n_cards), head=head_html, neg=html.escape(neg),
            negattr=html.escape(neg, quote=True), body="\n".join(body))
out = page
for k, v in vals.items():
    out = out.replace("@@%s@@" % k, v)
(root / "PROMPTS.html").write_text(out, encoding="utf-8")
print("scritto", root / "PROMPTS.html", n_cards, "carte")
