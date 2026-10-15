# -*- coding: utf-8 -*-
"""Genera un PDF riservato per ogni giocatore (senza soluzione né colpevole).

Uso:  python games/build_player_packs.py games/hawaii-2004
Per ogni personaggio unisce: invito, regole, piantina, scheda, missione,
una pagina «cosa ricevi in busta» e le carte piatto e scena che gli spettano.
Usa games/build_game_pdf.py per l'impaginazione.
"""
import json, pathlib, re, shutil, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from timeline_strip import striscia

root = pathlib.Path(sys.argv[1])
base = json.loads((root / "pdf.json").read_text(encoding="utf-8"))
tmp = root / "_build"
tmp.mkdir(exist_ok=True)
outdir = root / "giocatori"
outdir.mkdir(exist_ok=True)

# numero personaggio -> (nome file, oggetti, carte piatto, carte scena)
SLUG = {1: "lani", 2: "nalu", 3: "ike", 4: "akoni", 5: "pua", 6: "maleko",
        7: "kalea", 8: "noe", 9: "kapono", 10: "auntie_lei"}
OGGETTI = {1: ["01"], 2: ["02"], 3: ["03"], 4: ["04"], 5: ["05"], 6: ["06"],
           7: ["07"], 8: ["08", "09"], 9: [], 10: ["10"]}
PIATTI = {1: "lani", 2: "nalu", 8: "noe", 9: "kapono", 10: "lei"}
SCENE = {1: "scene/scena_04_lani_nalu_ike.md", 10: "scene/scena_05_lani_lei.md",
         9: "scene/scena_01_kalea_kapono.md", 8: "scene/scena_02_kalea_noe.md",
         5: "scene/scena_03_pua_akoni.md", 6: "scene/scena_06_maleko_kalea.md"}

PUNTI = {
    6: """# Il conto del tuo ruolo

Oltre ai compiti, la tua serata ha un punteggio a parte. Conta quante persone ti accusano nei fogli.

- Nessuno ti accusa: **+20 punti**.
- Ti accusano una o due persone: **+10 punti**.
- Ti accusano in tre o più: **0 punti**.
- Confessi di tua volontà prima che il tenente legga le accuse: **+5 punti**, e il tuo epilogo cambia.
""",
    7: """# Il conto del tuo ruolo

Oltre ai compiti, la tua serata ha un punteggio a parte.

- Nessuno ti accusa dell'omicidio: **+5 punti**.
- Prima del turno delle accuse racconti la tua verità a metà sul colloquio delle 23:10, a Noe o davanti al tavolo: **altri +5 punti**.

Il massimo è 10, e il secondo bonus dipende da una tua azione: nessuno può dartelo al posto tuo.
""",
}


def titolo(path):
    return re.search(r"^# (.+)$", (root / path).read_text(encoding="utf-8"), re.M).group(1)


for n, slug in SLUG.items():
    scheda = (root / f"personaggi/Character_{n}_scheda_personaggio.md").read_text(encoding="utf-8")
    nome = re.search(r"^# Scheda Personaggio: (.+)$", scheda, re.M).group(1).strip()

    righe = ["# Cosa ricevi in busta", "",
             "Il direttore ti consegna le buste a inizio serata, chiuse e con il tuo nome. Sei libero di aprirle, mostrarle, tacerle o passarle. Entro la campanella del minuto 55 ogni busta ancora chiusa va aperta, passata o consegnata al tenente.", ""]
    oggetti = [titolo(f"oggetti/oggetto_{o}.md") for o in OGGETTI[n]]
    if n == 9:
        oggetti = ["Il biglietto di ricatto che hai già in tasca (indizio 11)"]
    righe += ["## Il tuo oggetto"] + [f"- {o}" for o in oggetti] + [""]
    seguono = []
    if n in PIATTI:
        seguono.append("la **carta piatto** della cena (facoltativa)")
    if n in SCENE:
        seguono.append("la **carta scena**")
    if seguono:
        righe += ["## Le carte che seguono", "",
                  "Dopo questa pagina trovi " + " e ".join(seguono) + ". Non portano indizi.", ""]
    if n in PUNTI:
        righe += ["", PUNTI[n].replace("# Il conto del tuo ruolo", "## Il conto del tuo ruolo").strip(), ""]
    (tmp / f"busta_{n}.md").write_text("\n".join(righe), encoding="utf-8")

    (tmp / f"striscia_{n}.md").write_text(striscia(root, n, nome), encoding="utf-8")
    files = [f"personaggi/Character_{n}_invito.md", "gioco/regole_giocatore.md",
             "gioco/piantina.md", f"personaggi/Character_{n}_scheda_personaggio.md",
             f"_build/striscia_{n}.md", f"personaggi/Character_{n}_missione.md"]
    files.append(f"_build/busta_{n}.md")
    if n in PIATTI:
        files.append(f"oggetti/piatto_{PIATTI[n]}.md")
    if n in SCENE:
        files.append(SCENE[n])

    cfg = {k: base[k] for k in ("header", "kicker", "theme")}
    cfg.update({
        "output": f"giocatori/{n:02d}_{slug}.pdf",
        "title": "Last Call al Kapu Lounge",
        "subtitle": f"Il fascicolo di {nome}",
        "warn": f"Documento riservato: non mostrarlo a nessuno e non leggere le pagine segnate «non leggerla prima» finché non è il momento. Non serve impararlo a memoria.",
        "sections": [{"title": "", "files": files}],
    })
    cfgpath = tmp / f"cfg_{n}.json"
    cfgpath.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
    subprocess.run([sys.executable, str(pathlib.Path(__file__).parent / "build_game_pdf.py"),
                    str(root), str(outdir / f"{n:02d}_{slug}.pdf"), str(cfgpath)], check=True)

shutil.rmtree(tmp)
print("fatto:", len(SLUG), "fascicoli in", outdir)
