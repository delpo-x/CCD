# -*- coding: utf-8 -*-
"""Genera enigmi/terminale.html: il terminale del tenente, una pagina offline.

Uso:  python games/build_enigmi_terminale.py games/hawaii-2004
I giocatori scrivono la risposta, la pagina dice «giusto» o «non ancora» e
dà un aiuto alla volta. Le risposte sono memorizzate come impronte (non in chiaro).
"""
import json, pathlib, re, sys

root = pathlib.Path(sys.argv[1])
SALE = "kapu2004"


def norm(s):
    return re.sub(r"[^A-Z0-9]", "", s.upper().replace("À", "A").replace("È", "E").replace("É", "E")
                  .replace("Ì", "I").replace("Ò", "O").replace("Ù", "U"))


def h32(s, seed):
    x = seed
    for ch in s.encode("utf-8"):
        x ^= ch
        x = (x * 16777619) & 0xFFFFFFFF
    return x


def impronta(s):
    s = SALE + norm(s)
    return f"{h32(s, 2166136261):08x}{h32(s, 2654435761):08x}"


# ogni enigma: gruppi di parole; la risposta è giusta se ogni gruppo ha almeno una parola presente.
# mode "cifre": si confrontano solo le cifre, nell'ordine.
ENIGMI = [
    {"id": 1, "titolo": "La riga cifrata del taccuino",
     "domanda": "Cosa dice la riga in margine? Scrivi il messaggio.",
     "gruppi": [["NALU"], ["K3"]], "mode": "parole",
     "ok": "Giusto. Il messaggio dice dove sta la copia del registro e chi ha la chiave. Dite al tenente cosa fate.",
     "aiuti": ["Le lettere sono state spostate, non inventate.",
               "Guardate la cifra: c'è un 3 in mezzo alle lettere, e una chiave ha una targhetta con un 3.",
               "Chiedi al tenente la striscia cifrante: serve a scorrere l'alfabeto."]},
    {"id": 2, "titolo": "La cassetta K-3",
     "domanda": "Scrivi le tre cifre del lucchetto.",
     "gruppi": [["396"]], "mode": "parole",
     "ok": "Click. Le rotelle girano e il coperchio si alza. Chiamate il tenente.",
     "aiuti": ["Cercate una somma, non una data.",
               "Ventidue pagamenti, tutti uguali.",
               "Diciottomila, ventidue volte. Le rotelle sono tre: migliaia."]},
    {"id": 3, "titolo": "Tre foto senza ora",
     "domanda": "In che ordine sono state scattate? Scrivi i tre numeri (per esempio 3-1-2).",
     "gruppi": [["231"]], "mode": "cifre",
     "ok": "L'ordine torna. Ora rispondete alle due domande della carta.",
     "aiuti": ["Il tabulato di Akoni dice quando comincia la chiamata.",
               "I coriandoli esplodono a un orario preciso, lo sanno tutti.",
               "Una sola foto ha Akoni che non telefona ancora."]},
    {"id": 4, "titolo": "La lavagna delle 23:15",
     "domanda": "Quale persona resta senza una prova per le 23:15? Scrivi il nome.",
     "gruppi": [["MALEKO"]], "mode": "parole",
     "ok": "Il nome è sulla lavagna. Il tenente prende nota.",
     "aiuti": ["Un alibi vale solo se lo prova qualcosa che non dipende da chi lo dice.",
               "Una persona non ha una riga piena: chi manca?",
               "Due righe vuote: una si riempie con i rapporti del laboratorio."]},
    {"id": 5, "titolo": "Il nastro: cosa manca?",
     "domanda": "Cosa non si sente sul nastro?",
     "gruppi": [["BOATO", "CORIANDOLI", "CANNONI", "SCOPPIO", "ESPLOSIONE"]], "mode": "parole",
     "ok": "Giusto: manca proprio quello. Il buco tra i due clic lo copre.",
     "aiuti": ["Il nastro è continuo, ma tra i due clic manca qualcosa di molto rumoroso.",
               "Quello che ricordate tutti, dalla veranda, alle 23:15."]},
]

dati = []
for e in ENIGMI:
    d = {k: e[k] for k in ("id", "titolo", "domanda", "ok", "aiuti", "mode")}
    d["gruppi"] = [[impronta(w) for w in g] for g in e["gruppi"]]
    dati.append(d)

PAGE = r"""<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Terminale del tenente</title>
<style>
:root{--bg:#12112B;--card:#1d1c3b;--ink:#F7F3EA;--muted:#B9B4C9;--pink:#FF6FAE;--teal:#4FD1C5;--line:#3a3866;--ok:#7BE0A4;--no:#FF8FA3}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#F7F3EA;--card:#fff;--ink:#1C1B29;--muted:#4A4757;--pink:#B3125B;--teal:#0F6B6B;--line:#D8D0BE;--ok:#0B6B3A;--no:#A8132F}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 Georgia,'Merriweather',serif;padding:16px}
main{max-width:560px;margin:0 auto}
h1{font-size:1.5rem;margin:8px 0 4px;color:var(--pink)}
.sub{color:var(--muted);margin:0 0 16px}
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 16px}
.tabs button{min-height:44px;min-width:44px;padding:8px 14px;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--ink);font:inherit;cursor:pointer}
.tabs button[aria-pressed="true"]{border-color:var(--pink);box-shadow:0 0 0 2px var(--pink) inset}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px}
h2{font-size:1.15rem;margin:0 0 8px}
label{display:block;margin:12px 0 6px;color:var(--muted)}
input{width:100%;min-height:48px;padding:10px 12px;border-radius:10px;border:1px solid var(--line);background:transparent;color:var(--ink);font:inherit;font-size:1.1rem}
input:focus-visible,button:focus-visible{outline:3px solid var(--teal);outline-offset:2px}
.row{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.row button{flex:1;min-height:48px;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--ink);font:inherit;cursor:pointer}
.row .go{background:var(--pink);border-color:var(--pink);color:#fff;font-weight:700}
#msg{margin-top:14px;min-height:1.5em}
.ok{color:var(--ok)}.no{color:var(--no)}
ol{padding-left:20px;margin:8px 0 0}
.aiuti{margin-top:12px;color:var(--muted)}
</style></head><body><main>
<h1>Terminale del tenente</h1>
<p class="sub">Scegli l'enigma, scrivi la risposta. Un aiuto alla volta, se serve.</p>
<div class="tabs" id="tabs" role="group" aria-label="Enigmi"></div>
<section class="card" aria-live="polite">
<h2 id="titolo"></h2>
<p id="domanda"></p>
<label for="r">La tua risposta</label>
<input id="r" autocomplete="off" autocapitalize="characters" spellcheck="false">
<div class="row"><button class="go" id="verifica">Verifica</button><button id="aiuto">Chiedi un aiuto</button></div>
<p id="msg" role="status"></p>
<ol class="aiuti" id="aiuti"></ol>
</section>
<script>
const SALE="@@SALE@@",DATI=@@DATI@@;
function norm(s){return s.toUpperCase().normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/[^A-Z0-9]/g,"")}
function h32(s,seed){let x=seed>>>0;const b=new TextEncoder().encode(s);for(const c of b){x^=c;x=Math.imul(x,16777619)>>>0}return x}
function imp(s){s=SALE+norm(s);return h32(s,2166136261).toString(16).padStart(8,"0")+h32(s,2654435761).toString(16).padStart(8,"0")}
let cur=0;const usati=DATI.map(()=>0);
const $=id=>document.getElementById(id);
function giusto(e,txt){
  if(e.mode==="cifre"){return imp(txt.replace(/[^0-9]/g,""))===e.gruppi[0][0]}
  const parole=txt.toUpperCase().normalize("NFD").replace(/[̀-ͯ]/g,"").split(/[^A-Z0-9]+/).filter(Boolean);
  const hs=new Set(parole.map(imp));
  return e.gruppi.every(g=>g.some(h=>hs.has(h)));
}
function mostra(){
  const e=DATI[cur];
  $("titolo").textContent="Enigma "+e.id+": "+e.titolo;
  $("domanda").textContent=e.domanda;
  $("r").value="";$("msg").textContent="";$("msg").className="";
  $("aiuti").innerHTML="";
  for(let i=0;i<usati[cur];i++){const li=document.createElement("li");li.textContent=e.aiuti[i];$("aiuti").appendChild(li)}
  document.querySelectorAll("#tabs button").forEach((b,i)=>b.setAttribute("aria-pressed",String(i===cur)));
}
DATI.forEach((e,i)=>{const b=document.createElement("button");b.textContent=String(e.id);b.setAttribute("aria-label","Enigma "+e.id+": "+e.titolo);b.onclick=()=>{cur=i;mostra()};$("tabs").appendChild(b)});
$("verifica").onclick=()=>{const e=DATI[cur],t=$("r").value.trim();
  if(!t){$("msg").textContent="Scrivi una risposta.";$("msg").className="no";return}
  if(giusto(e,t)){$("msg").textContent=e.ok;$("msg").className="ok"}else{$("msg").textContent="Non ancora. Riprovate.";$("msg").className="no"}};
$("r").addEventListener("keydown",ev=>{if(ev.key==="Enter")$("verifica").click()});
$("aiuto").onclick=()=>{const e=DATI[cur];
  if(usati[cur]>=e.aiuti.length){$("msg").textContent="Gli aiuti sono finiti. Chiedete al tenente.";$("msg").className="no";return}
  usati[cur]++;mostra();$("msg").textContent="";};
mostra();
</script></main></body></html>
"""

out = root / "enigmi/terminale.html"
out.write_text(PAGE.replace("@@SALE@@", SALE).replace("@@DATI@@", json.dumps(dati, ensure_ascii=False)), encoding="utf-8")
print("scritto", out)
