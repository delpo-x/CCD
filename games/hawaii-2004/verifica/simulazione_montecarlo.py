"""Simulazione Monte Carlo di «Last Call al Kapu Lounge».

ATTENZIONE: è un modello. Le regole (punteggio, fasi, bonus tavolo, rottura di Maleko)
sono quelle del materiale. I comportamenti dei giocatori (attività, probabilità di trovare
un indizio, di essere convinti) sono IPOTESI dichiarate qui sotto, non misure. I numeri
dicono dove il gioco è fragile se le ipotesi reggono; non dicono come andrà una serata vera.

Uso: python simulazione_montecarlo.py [N] [seed] [--senza-rottura]
"""
import math
import random
import statistics as st
import sys

sys.stdout.reconfigure(encoding="utf-8")

N = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 200
SEED = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 20261015
ROTTURA = "--senza-rottura" not in sys.argv
MIN70 = "--senza-min70" not in sys.argv
TAVOLO = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--tavolo=")), "misto")
# Composizione dei tavoli: pesi dei profili (timido, medio, teatrale, baro). IPOTESI, non misure.
TAVOLI = {
    "misto":       (0.30, 0.40, 0.20, 0.10),
    "principianti": (0.60, 0.30, 0.08, 0.02),
    "esperti":     (0.05, 0.35, 0.55, 0.05),
    "silenzioso":  (0.55, 0.40, 0.05, 0.00),
    "con_bari":    (0.25, 0.35, 0.15, 0.25),
}

PG = ["Lani", "Nalu", "Ike", "Akoni", "Pua", "Maleko", "Kalea", "Noe", "Kapono", "Auntie Lei"]
EASY = ["Nalu", "Kapono", "Ike", "Auntie Lei"]
HARD = ["Kalea", "Maleko"]
INNOCENTI = [p for p in PG if p not in ("Maleko", "Kalea")]

# ---- Ipotesi sui giocatori (dichiarate) --------------------------------------
# attività: azioni medie nei 75 minuti (ricerca, richiesta, scambio, tentativo di compito)
# parla: probabilità di dire ad alta voce il proprio sospetto nella discussione
PROFILI = {
    "timido":    dict(peso=0.30, azioni=7,  parla=0.30, condivide=0.45, bara=0.0),
    "medio":     dict(peso=0.40, azioni=12, parla=0.55, condivide=0.60, bara=0.0),
    "teatrale":  dict(peso=0.20, azioni=15, parla=0.85, condivide=0.75, bara=0.0),
    "baro":      dict(peso=0.10, azioni=12, parla=0.60, condivide=0.30, bara=0.5),
}

# ---- Ipotesi sui pezzi di prova (probabilità di emergere al tavolo) ----------
# r = tasso per azione del tavolo: p = 1 - exp(-r * azioni_totali)
PEZZI_CATENA = {
    "nastro":     dict(r=0.0,    nota="due pause: si ottiene solo con sequestro, dopo altri pezzi"),
    "lampadina":  dict(r=0.0055, nota="indizio 15 + Kapono che racconta"),
    "vetri":      dict(r=0.011,  nota="nessuno dalla porta a vetri 23:12-23:19"),
    "cassetto":   dict(r=0.0075, nota="cassetto vuoto alle 22:55 (Auntie Lei, indizio 14)"),
    "movente":    dict(r=0.0035, nota="chiave -> indizio 13 + rapporto 06 sul nome Hanohano"),
}
ESCLUSIONI = {  # cosa toglie sospetti
    "IMG_0413":   dict(r=0.0,   scagiona=["Akoni", "Pua", "Noe", "Auntie Lei"]),   # forzata alla campanella
    "tabulato":   dict(r=0.0045, scagiona=["Akoni"]),
    "Lopaka":     dict(r=0.0035, scagiona=["Pua"]),
    "conducente": dict(r=0.0045, scagiona=["Ike", "Kapono"]),
    "scontrini":  dict(r=0.011,  scagiona=["Nalu"]),
    "Soo":        dict(r=0.0035, scagiona=["Kalea"]),
}
# indizi che spingono verso un innocente (false piste facili)
PISTE = {"Kalea": 3.2, "Akoni": 1.6, "Pua": 1.2, "Ike": 1.2, "Kapono": 1.4, "Lani": 1.0,
         "Nalu": 1.0, "Auntie Lei": 0.7, "Noe": 0.8}

# ---- Compiti: probabilità base per giocatore e compito (3 a testa) -----------
# dipendenza da altri giocatori: la riuscita scala con l'attività del partner
COMPITI = {
    "Lani":       [0.55, 0.65, 0.80], "Nalu":       [0.55, 0.65, 0.60], "Ike":        [0.70, 0.60, 0.60],
    "Akoni":      [0.50, 0.55, 0.60], "Pua":        [0.45, 0.55, 0.55], "Maleko":     [0.60, 0.40, 0.90],
    "Kalea":      [0.65, 0.50, 0.55], "Noe":        [0.55, 0.60, 0.70], "Kapono":     [0.65, 0.50, 0.60],
    "Auntie Lei": [0.50, 0.60, 0.55],
}
PARTNER = {"Lani": "Auntie Lei", "Nalu": "Akoni", "Ike": "Auntie Lei", "Akoni": "Kalea", "Pua": "Auntie Lei",
           "Maleko": "Kalea", "Kalea": "Kapono", "Noe": "Akoni", "Kapono": "Kalea", "Auntie Lei": "Pua"}


def sceglie_profilo(rng):
    nomi = list(PROFILI)
    return rng.choices(nomi, weights=TAVOLI[TAVOLO])[0]


def assegna_profili(rng):
    """Il direttore dà i ruoli facili ai due principianti (timidi), con probabilità 0.8."""
    prof = {p: sceglie_profilo(rng) for p in PG}
    timidi = [p for p in PG if prof[p] == "timido"]
    for p in timidi:
        if p in HARD and rng.random() < 0.8:
            scambio = rng.choice([e for e in EASY if prof[e] != "timido"] or EASY)
            prof[p], prof[scambio] = prof[scambio], prof[p]
    return prof


def poisson(rng, lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def una_partita(rng):
    prof = assegna_profili(rng)
    azioni = {p: poisson(rng, PROFILI[prof[p]]["azioni"]) for p in PG}
    tot = sum(azioni.values())

    # ---- pezzi di catena e esclusioni
    trovati = {k: rng.random() < 1 - math.exp(-v["r"] * tot) for k, v in PEZZI_CATENA.items()}
    # Kapono timido o bugiardo: la lampadina si perde con prob. 0.3
    if trovati["lampadina"] and prof["Kapono"] == "timido" and rng.random() < 0.3:
        trovati["lampadina"] = False
    # il nastro: sequestro solo se il tavolo ha già lampadina o movente (prova documentata)
    if trovati["lampadina"] or trovati["movente"]:
        trovati["nastro"] = rng.random() < 0.55
    if MIN70 and sum(trovati[k] for k in ("vetri", "cassetto", "lampadina", "movente")) < 2:
        for k in ("vetri", "cassetto", "lampadina", "movente"):
            if not trovati[k]:
                trovati[k] = True  # suggerimento del minuto 70: ne emerge uno
                break
    escl = {k: rng.random() < 1 - math.exp(-v["r"] * tot) for k, v in ESCLUSIONI.items()}
    escl["IMG_0413"] = True  # campanella: la macchina fotografica non si tiene
    # mostrare IMG_0413 costa a Noe le foto di Kalea: una Noe timida la consegna comunque (regola)
    # ---- Kalea: dice la sua verità a metà solo se Noe è attiva
    kalea_verita = azioni["Noe"] >= 8 and rng.random() < 0.7

    # ---- sospetti individuali
    esclusi = set()
    for k, v in ESCLUSIONI.items():
        if escl[k]:
            esclusi.update(v["scagiona"])
    n_catena = sum(trovati[k] for k in ("lampadina", "vetri", "cassetto", "movente"))
    scelte_ad_alta_voce = []
    sospetto = {}
    for p in PG:
        if p == "Maleko":
            sospetto[p] = (None, 0)
            continue
        w = {}
        for q in PG:
            if q == p:
                continue
            if q == "Maleko":
                base = 0.55
            else:
                base = PISTE.get(q, 1.0)
            if q in esclusi:
                base *= 0.12
            w[q] = base
        # conoscenza individuale dei pezzi: ognuno ne riceve una parte
        cond = PROFILI[prof[p]]["condivide"]
        conosce = 0
        for k in ("lampadina", "vetri", "cassetto", "movente", "nastro"):
            if trovati[k] and rng.random() < 0.35 + 0.55 * cond + (0.3 if PROFILI[prof[p]]["bara"] else 0):
                conosce += 1
        w["Maleko"] += 2.6 * conosce
        sospetto[p] = (rng.choices(list(w), weights=list(w.values()))[0], conosce)
        if sospetto[p][0] == "Kalea" and rng.random() < PROFILI[prof[p]]["parla"]:
            scelte_ad_alta_voce.append(p)

    # ---- rottura di Maleko: due giocatori dicono «è stata Kalea» ad alta voce
    confessa = False
    if ROTTURA and len(scelte_ad_alta_voce) >= 2:
        p_confessa = 0.55 if prof["Maleko"] == "timido" else 0.85
        confessa = rng.random() < p_confessa
    # giocatori che bluffano per far scattare la regola: baro o teatrale, raro
    if ROTTURA and not confessa:
        provocatori = [p for p in PG if p != "Maleko" and prof[p] in ("baro", "teatrale") and rng.random() < 0.05]
        if len(provocatori) >= 2 and rng.random() < 0.85:
            confessa = True
            bluff = True
        else:
            bluff = False
    else:
        bluff = False

    # ---- accuse finali (scritte)
    accusa = {}
    for p in PG:
        if p == "Maleko":
            accusa[p] = None
            continue
        s, conosce = sospetto[p]
        if confessa:
            accusa[p] = "Maleko" if rng.random() < 0.93 else s
        else:
            # dopo la discussione chi ha ≥2 pezzi tende a convergere su Maleko
            if conosce >= 2 and rng.random() < 0.35:
                s = "Maleko"
            accusa[p] = s
    giuste = [p for p in PG if accusa[p] == "Maleko"]
    # ---- punti
    punti = {p: 0 for p in PG}
    for p in PG:
        for i, base in enumerate(COMPITI[p]):
            f = min(1.0, azioni[p] / 10.0) * (0.55 + 0.45 * min(1.0, azioni[PARTNER[p]] / 10.0))
            if rng.random() < base * f:
                punti[p] += 5
    # ultima chiamata: il baro tiene una busta con prob. 0.5 e perde un compito
    for p in PG:
        if PROFILI[prof[p]]["bara"] and punti[p] >= 5 and rng.random() < 0.5:
            punti[p] -= 5
    cit = {}
    for p in giuste:
        pezzi_noti = sum(trovati[k] for k in ("lampadina", "vetri", "cassetto", "movente", "nastro"))
        cit[p] = min(5, sum(1 for k in ("lampadina", "vetri", "cassetto", "movente", "nastro")
                            if trovati[k] and rng.random() < 0.7))
        punti[p] += 10 + 2 * cit[p]
    n_acc_m = len(giuste)
    if confessa:
        punti["Maleko"] += 5
    else:
        punti["Maleko"] += 20 if n_acc_m == 0 else (10 if n_acc_m <= 2 else 0)
    acc_kalea = [p for p in PG if accusa[p] == "Kalea"]
    if not acc_kalea:
        punti["Kalea"] += 5
    if kalea_verita:
        punti["Kalea"] += 5
    # +3 a chi mette in comune una prova che scagiona (tabulato, conducente), uno per prova
    for k in ("tabulato", "conducente"):
        if escl[k]:
            attivi = [p for p in PG if azioni[p] >= 8]
            if attivi:
                punti[rng.choice(attivi)] += 3
    bonus = n_acc_m >= 7
    if bonus:
        for p in PG:
            punti[p] += 5
    # vincitore con spareggi (accuse corrette, poi prove citate)
    chiavi = {p: (punti[p], 1 if accusa[p] == "Maleko" else 0, cit.get(p, 0)) for p in PG}
    top = max(chiavi.values())
    vincitori = [p for p in PG if chiavi[p] == top]
    # durate: modello con varianza assunta
    durata = (10 + rng.gauss(0, 1.5)) + (25 + rng.gauss(0, 3)) + 75 + 10 + (15 + rng.gauss(0, 2.5)) + (15 + rng.gauss(0, 4))
    # inattivi: meno di 3 azioni, o compiti bloccati (0 punti con ≥8 azioni)
    inattivi = [p for p in PG if azioni[p] < 4]
    bloccati = [p for p in PG if azioni[p] >= 8 and punti[p] == 0 and accusa[p] != "Maleko"]
    return dict(prof=prof, azioni=azioni, trovati=trovati, punti=punti, accusa=accusa, n_acc_m=n_acc_m,
                confessa=confessa, bluff=bluff, bonus=bonus, vincitori=vincitori, durata=durata,
                inattivi=inattivi, bloccati=bloccati, acc_kalea=len(acc_kalea),
                alta_voce=len(scelte_ad_alta_voce))


def main():
    rng = random.Random(SEED)
    R = [una_partita(rng) for _ in range(N)]
    print(f"tavolo={TAVOLO} N={N} seed={SEED} rottura_maleko={'sì' if ROTTURA else 'no'}  (valori CALCOLATI sul modello; le ipotesi sono STIMATE)")
    win = {p: 0.0 for p in PG}
    for r in R:
        for v in r["vincitori"]:
            win[v] += 1 / len(r["vincitori"])
    print("\nVittoria per personaggio (% partite, parità divisa):")
    for p in sorted(PG, key=lambda x: -win[x]):
        print(f"  {p:11s} {100*win[p]/N:5.1f}")
    fazioni = {"Innocenti (8)": INNOCENTI, "Kalea (esca)": ["Kalea"], "Maleko (assassino)": ["Maleko"]}
    print("\nPer fazione:")
    for f, ps in fazioni.items():
        print(f"  {f:20s} {100*sum(win[p] for p in ps)/N:5.1f}")
    ds = [r["durata"] for r in R]
    print(f"\nDurata modello (minuti): media {st.mean(ds):.1f}, dev.std {st.pstdev(ds):.1f}  (varianze assunte)")
    az = [r["azioni"][p] for r in R for p in PG]
    print(f"Azioni per giocatore in 75 min: media {st.mean(az):.1f}, dev.std {st.pstdev(az):.1f}")
    pt = {p: st.mean(r["punti"][p] for r in R) for p in PG}
    print("Punti medi:", ", ".join(f"{p} {pt[p]:.1f}" for p in PG))
    print(f"\nAccuse giuste su Maleko: media {st.mean(r['n_acc_m'] for r in R):.1f}")
    print(f"Bonus tavolo (≥7 giuste): {100*sum(r['bonus'] for r in R)/N:.1f}%")
    print(f"Maleko confessa: {100*sum(r['confessa'] for r in R)/N:.1f}%  (di cui per bluff provocato: {100*sum(r['bluff'] for r in R)/N:.1f}%)")
    print(f"Nessuna accusa su Maleko: {100*sum(r['n_acc_m']==0 for r in R)/N:.1f}%")
    print(f"Kalea accusata da ≥1: {100*sum(r['acc_kalea']>0 for r in R)/N:.1f}%; da ≥3: {100*sum(r['acc_kalea']>=3 for r in R)/N:.1f}%")
    print(f"≥1 giocatore con <4 azioni: {100*sum(bool(r['inattivi']) for r in R)/N:.1f}%")
    print(f"≥1 giocatore attivo con 0 punti e senza accusa giusta: {100*sum(bool(r['bloccati']) for r in R)/N:.1f}%")
    for k in PEZZI_CATENA:
        print(f"  pezzo «{k}» emerso: {100*sum(r['trovati'][k] for r in R)/N:.0f}%")
    nessuno = sum(not any(r["trovati"][k] for k in ("lampadina", "vetri", "cassetto", "movente", "nastro")) for r in R)
    print(f"  nessun pezzo di catena: {100*nessuno/N:.1f}%")
    ben = [r for r in R if r["n_acc_m"] >= 3]
    print(f"≥3 accuse giuste: {100*len(ben)/N:.1f}%")
    sino = [r for r in R if not r["confessa"]]
    print("Senza confessione, accuse giuste medie:", f"{st.mean(r['n_acc_m'] for r in sino):.1f}" if sino else "-")
    con = [r for r in R if r["confessa"]]
    print("Con confessione, accuse giuste medie:", f"{st.mean(r['n_acc_m'] for r in con):.1f}" if con else "-")


if __name__ == "__main__":
    main()
