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
def P(domanda, gruppi, ok, aiuti, mode="parole"):
    return {"domanda": domanda, "gruppi": gruppi, "ok": ok, "aiuti": aiuti, "mode": mode}


ENIGMI = [
    {"id": 1, "titolo": "La riga cifrata del taccuino", "passi": [P(
        "Cosa dice la riga in margine? Scrivi il messaggio.", [["NALU"], ["K3"]],
        "Giusto. Il messaggio dice dove sta la copia del registro e chi ha la chiave. Dite al tenente cosa fate.",
        ["Le lettere sono state spostate, non inventate.",
         "Guardate la cifra: c'è un 3 in mezzo alle lettere, e una chiave ha una targhetta con un 3.",
         "Chiedi al tenente la striscia cifrante: serve a scorrere l'alfabeto."])]},
    {"id": 2, "titolo": "La cassetta K-3", "passi": [P(
        "Scrivi le tre cifre del lucchetto.", [["396"]],
        "Click. Le rotelle girano e il coperchio si alza. Chiamate il tenente.",
        ["Cercate una somma, non una data.", "Ventidue pagamenti, tutti uguali.",
         "Diciottomila, ventidue volte. Le rotelle sono tre: migliaia."])]},
    {"id": 3, "titolo": "Tre foto senza ora", "passi": [P(
        "In che ordine sono state scattate? Scrivi i tre numeri (per esempio 3-1-2).", [["231"]],
        "L'ordine torna. Ora rispondete alle due domande della carta.",
        ["Il tabulato di Akoni dice quando comincia la chiamata.",
         "I coriandoli esplodono a un orario preciso, lo sanno tutti.",
         "Una sola foto ha Akoni che non telefona ancora."], mode="cifre")]},
    {"id": 4, "titolo": "La lavagna delle 23:15", "passi": [P(
        "Quale persona resta senza una prova per le 23:15? Scrivi il nome.", [["MALEKO"]],
        "Il nome è sulla lavagna. Il tenente prende nota.",
        ["Un alibi vale solo se lo prova qualcosa che non dipende da chi lo dice.",
         "Una persona non ha una riga piena: chi manca?",
         "Due righe vuote: una si riempie con i rapporti del laboratorio."])]},
    {"id": 5, "titolo": "Il nastro: cosa manca?", "passi": [P(
        "Cosa non si sente sul nastro?", [["BOATO", "CORIANDOLI", "CANNONI", "SCOPPIO", "ESPLOSIONE"]],
        "Giusto: manca proprio quello. Il buco tra i due clic lo copre.",
        ["Il nastro è continuo, ma tra i due clic manca qualcosa di molto rumoroso.",
         "Quello che ricordate tutti, dalla veranda, alle 23:15."])]},
    {"id": 6, "titolo": "Chi eredita?", "passi": [
        P("Chi guadagna di più dalla sua morte? Scrivi un nome.", [["LANI"]],
          "Sulla carta, sì. Ma un movente non è una prova. Secondo passo: quanti dei tre eredi hanno una prova per le 23:15?",
          ["Il locale vale più di un assegno e di una quota."]),
        P("Quanti dei tre eredi hanno una prova per le 23:15?", [["3", "TRE", "TUTTI"]],
          "Tutti e tre. Seguire i soldi qui non porta a nessuno: cercate un'altra strada.",
          ["Guardate la lavagna delle 23:15.", "Uno è sul palco, uno spara i coriandoli, una è seduta in veranda."])]},
    {"id": 7, "titolo": "Il lei viola", "passi": [
        P("Chi ha il lei viola? Scrivi i due nomi.", [["KALEA"], ["LEI", "AUNTIE", "LEILANI"]],
          "Due persone, giusto. Secondo passo: di chi è la suola sul petalo del vaso?",
          ["Il resto degli ospiti ha lei bianchi, di plumeria."]),
        P("La suola liscia di gomma, numero grande: di chi può essere?", [["UOMO", "UOMINI", "MASCHILE", "MASCHIO"]],
          "Una scarpa da uomo. Le due donne col lei viola non c'entrano con quel passo: il petalo non basta a incastrarle.",
          ["Pensate al numero: grande.", "Né Kalea né Auntie Lei portano quella misura."])]},
    {"id": 8, "titolo": "Le casse di Aloha Cartage", "passi": [
        P("Che cosa c'è davvero nelle casse? Scrivi una parola.", [["SIGARI", "SIGARO", "HABANA"]],
          "Sigari di contrabbando: un movente per chi non vuole essere denunciato. Ma serve un testimone. Secondo passo: chi può dire dove erano i due firmatari?",
          ["«Habana» è una città, ma anche una cosa che si fuma."]),
        P("Chi può dire dove erano i due firmatari mentre scaricavano?", [["CONDUCENTE", "NAKAMURA", "AUTISTA"]],
          "Il conducente li ha visti scaricare. Chiedete al tenente la sua dichiarazione: spegne la pista.",
          ["Qualcuno firma la bolla senza essere né Ike né Kapono.", "È l'uomo con il camion."])]},
]

dati = []
for e in ENIGMI:
    passi = []
    for pa in e["passi"]:
        d = {k: pa[k] for k in ("domanda", "ok", "aiuti", "mode")}
        d["gruppi"] = [[impronta(w) for w in g] for g in pa["gruppi"]]
        passi.append(d)
    dati.append({"id": e["id"], "titolo": e["titolo"], "passi": passi})

PAGE = (pathlib.Path(__file__).parent / "terminale_template.html").read_text(encoding="utf-8")

out = root / "enigmi/terminale.html"
out.write_text(PAGE.replace("@@SALE@@", SALE).replace("@@DATI@@", json.dumps(dati, ensure_ascii=False)), encoding="utf-8")
print("scritto", out)
