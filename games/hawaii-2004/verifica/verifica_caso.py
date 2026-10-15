"""Verifica meccanica del caso «Last Call al Kapu Lounge».

Cosa controlla:
1. La cronologia vera è fisicamente possibile (nessun teletrasporto).
2. Ogni prova oggettiva è coerente con la cronologia vera.
3. Chi poteva trovarsi nell'ufficio alle 23:15:00, usando SOLO le prove oggettive
   (gli «alibi» che i giocatori possono davvero dimostrare), con e senza ciascuna prova.

Uso: python verifica_caso.py
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

def t(s):
    p = [int(x) for x in s.split(":")]
    while len(p) < 3:
        p.append(0)
    return p[0] * 3600 + p[1] * 60 + p[2]

def fmt(x):
    return "%02d:%02d:%02d" % (x // 3600, x % 3600 // 60, x % 60)

# Secondi di cammino tra i luoghi. VER = veranda, SALA, BAG = bagno signore,
# UFF = ufficio, CUC = cucina, SCANT = scantinato/vicolo (portello).
EDGES = {
    ("VER", "SALA"): 15, ("VER", "BAG"): 25, ("VER", "UFF"): 40, ("VER", "CUC"): 45,
    ("VER", "SCANT"): 75, ("SALA", "UFF"): 30, ("SALA", "BAG"): 40, ("SALA", "CUC"): 45,
    ("SALA", "SCANT"): 70, ("BAG", "UFF"): 10, ("BAG", "CUC"): 25, ("BAG", "SCANT"): 55,
    ("UFF", "CUC"): 15, ("UFF", "SCANT"): 45, ("CUC", "SCANT"): 30,
}
def dist(a, b, slow=1.0):
    if a == b:
        return 0
    return EDGES.get((a, b), EDGES.get((b, a))) * slow

SLOW = {"Auntie Lei": 3.0}  # bastone di koa

PEOPLE = ["Lani", "Nalu", "Ike", "Akoni", "Pua", "Maleko", "Kalea", "Noe", "Kapono", "Auntie Lei"]

# ---- 1. Cronologia VERA: (inizio, fine, luogo) -------------------------------
TRUTH = {
    "Lani":       [("22:30", "23:40", "SALA")],
    "Nalu":      [("22:30", "23:40", "SALA")],
    "Ike":        [("23:05", "23:35", "SCANT")],
    "Kapono":      [("23:05", "23:12:20", "SCANT"), ("23:13", "23:14", "CUC"), ("23:14:30", "23:35", "SCANT")],
    "Akoni":       [("23:00", "23:08", "UFF"), ("23:09", "23:13", "VER"), ("23:13:10", "23:20", "VER")],
    "Pua":      [("23:00", "23:20", "VER")],
    "Auntie Lei": [("23:00", "23:20", "VER")],
    "Noe":        [("23:00", "23:20", "VER")],
    "Kalea":    [("21:30", "21:45", "SALA"), ("21:46", "21:49", "BAG"), ("21:50", "22:00", "SALA"),
                   ("22:58", "23:09", "VER"), ("23:09:40", "23:13", "UFF"), ("23:13:10", "23:19", "BAG"), ("23:19:45", "23:20", "VER")],
    "Maleko":     [("21:30", "21:45", "SALA"), ("21:46", "21:51", "UFF"), ("21:52", "22:00", "SALA"),
                   ("23:00", "23:14", "VER"), ("23:14:40", "23:15:10", "UFF"), ("23:15:25", "23:17", "CUC"),
                   ("23:17:20", "23:18", "CUC"), ("23:19", "23:20", "VER")],
}
# Kapono risale per il fusibile: passa dal corridoio (CS) ma lo rappresentiamo con CUC (stessa fascia).

def check_truth():
    errors = []
    for p, segs in TRUTH.items():
        slow = SLOW.get(p, 1.0)
        for (a0, a1, pa), (b0, b1, pb) in zip(segs, segs[1:]):
            gap = t(b0) - t(a1)
            need = dist(pa, pb, slow)
            if gap < need:
                errors.append("%s: da %s (%s) a %s (%s) servono %ds, ne ha %d" % (p, pa, a1, pb, b0, need, gap))
    return errors

def place_at(p, when):
    for a, b, loc in TRUTH[p]:
        if t(a) <= when <= t(b):
            return loc
    return None

# ---- 2. Prove OGGETTIVE: (id, persona, luogo, inizio, fine) ------------------
EVIDENCE = [
    ("E-palco",   "Lani",       "SALA",  "23:14:50", "23:15:10"),   # conto alla rovescia davanti a sala e band
    ("E-cannoni", "Nalu",      "SALA",  "23:14:50", "23:15:10"),   # spara i coriandoli
    ("E05",       "Nalu",      "SALA",  "23:14:00", "23:17:00"),   # scontrini
    ("E07-a",     "Ike",        "SCANT", "23:05:00", "23:35:00"),   # bolla + conducente
    ("E07-b",     "Kapono",      "SCANT", "23:14:30", "23:35:00"),   # conducente, tranne il minuto del fusibile
    ("E02",       "Kalea",    "BAG",   "23:14:05", "23:17:20"),   # chiamata di Soo (acqua, eco, «passi fuori»)
    ("E06-0412a", "Akoni",       "VER",   "23:12:00", "23:12:00"),
    ("E06-0412b", "Pua",      "VER",   "23:12:00", "23:12:00"),
    ("E06-0412c", "Auntie Lei", "VER",   "23:12:00", "23:12:00"),
    ("E06-0412d", "Maleko",     "VER",   "23:12:00", "23:12:00"),
    ("E06-0414a", "Akoni",       "VER",   "23:16:00", "23:16:00"),
    ("E06-0414b", "Pua",      "VER",   "23:16:00", "23:16:00"),
    ("E06-0414c", "Auntie Lei", "VER",   "23:16:00", "23:16:00"),
    ("E06-noe12", "Noe",        "VER",   "23:12:00", "23:12:00"),   # la fotografa, in veranda quando scatta
    ("E06-noe16", "Noe",        "VER",   "23:16:00", "23:16:00"),
    ("E26-brad",  "Akoni",       "VER",   "23:15:10", "23:15:10"),   # IMG_0413
    ("E26-vicki", "Pua",      "VER",   "23:15:10", "23:15:10"),
    ("E26-lei",   "Auntie Lei", "VER",   "23:15:10", "23:15:10"),
    ("E26-noe",   "Noe",        "VER",   "23:15:10", "23:15:10"),
    ("R02-akoni", "Akoni",      "VER",   "23:13:10", "23:16:30"),   # rapporto 2: tabulato, chiamata a Las Vegas; Lopaka conferma che erano insieme
    ("R05-pua",   "Pua",        "VER",   "23:14:50", "23:15:10"),   # rapporto 5: Lopaka sente Pua gridare durante la chiamata
    ("Maleko-ret", "Maleko",    "VER",   "23:20:00", "23:20:00"),   # rientro visto dai presenti
]
EV_GROUPS = {  # per spegnere/accendere in blocco
    "IMG_0413": ["E26-brad", "E26-vicki", "E26-lei", "E26-noe"],
    "chiamata_Soo": ["E02"],
    "conducente": ["E07-a", "E07-b"],
    "tabulato_Akoni": ["R02-akoni"],
    "Lopaka_Pua": ["R05-pua"],
}

def check_evidence_vs_truth():
    errors = []
    for eid, p, loc, a, b in EVIDENCE:
        for when in {t(a), t(b)}:
            actual = place_at(p, when)
            if actual != loc and not (eid.startswith("E07-b") and actual in ("CUC",)):
                errors.append("%s: %s dovrebbe essere a %s alle %s, ma la verità dice %s" % (eid, p, loc, fmt(when), actual))
    return errors

# ---- 3. Chi può essere nell'ufficio alle 23:15:00 ----------------------------
SHOT = t("23:15:00")
def can_be_in_office(p, ev_ids):
    slow = SLOW.get(p, 1.0)
    pts = []
    for eid, q, loc, a, b in EVIDENCE:
        if q == p and eid in ev_ids:
            pts.append((t(a), t(b), loc))
    before = [x for x in pts if x[1] <= SHOT]
    after = [x for x in pts if x[0] >= SHOT]
    during = [x for x in pts if x[0] < SHOT < x[1]]
    for a, b, loc in during:
        if loc != "UFF":
            return False
    last = max(before, key=lambda x: x[1]) if before else None
    first = min(after, key=lambda x: x[0]) if after else None
    ok_before = True if last is None else (SHOT - last[1]) >= dist(last[2], "UFF", slow)
    ok_after = True if first is None else (first[0] - SHOT) >= dist("UFF", first[2], slow)
    return ok_before and ok_after

def table(ev_ids, title):
    res = {p: can_be_in_office(p, ev_ids) for p in PEOPLE}
    print("\n== %s ==" % title)
    for p in PEOPLE:
        print("  %-11s %s" % (p, "PUÒ essere nell'ufficio alle 23:15" if res[p] else "esclus%s" % ("a" if p in ("Lani", "Kalea", "Pua", "Noe", "Auntie Lei") else "o")))
    return [p for p in PEOPLE if res[p]]

if __name__ == "__main__":
    e = check_truth()
    print("Cronologia vera: %s" % ("OK" if not e else "ERRORI"))
    for x in e:
        print("  -", x)
    e = check_evidence_vs_truth()
    print("Prove vs verità: %s" % ("OK" if not e else "ERRORI"))
    for x in e:
        print("  -", x)
    all_ids = {x[0] for x in EVIDENCE}
    full = table(all_ids, "Tutte le prove oggettive")
    assert full == ["Maleko"], full
    # Atteso togliendo una prova alla volta. IMG_0413 è la prova che regge più alibi:
    # per questo la macchina fotografica di Noe non si può tenere all'ultima chiamata.
    attesi = {
        "IMG_0413": ["Noe", "Maleko"],
        "chiamata_Soo": ["Kalea", "Maleko"],
        "conducente": ["Ike", "Kapono", "Maleko"],
        "tabulato_Akoni": ["Maleko"],
        "Lopaka_Pua": ["Maleko"],
    }
    for gname, ids in EV_GROUPS.items():
        s = table(all_ids - set(ids), "Senza %s" % gname)
        assert sorted(s) == sorted(attesi[gname]), (gname, s)
    # Caso peggiore ammesso dalle regole: camera tenuta e rapporti 2 e 5 non chiesti.
    peggiore = table(all_ids - set(EV_GROUPS["IMG_0413"] + EV_GROUPS["tabulato_Akoni"] + EV_GROUPS["Lopaka_Pua"]),
                     "Senza IMG_0413, tabulato di Akoni e Lopaka")
    assert sorted(peggiore) == sorted(["Akoni", "Pua", "Noe", "Maleko"]), peggiore
    # Solo prove «facili» (palco, cannoni, scontrini, foto 0412/0414)
    easy = {i for i in all_ids if i.startswith(("E-", "E05", "E06", "Maleko"))}
    table(easy, "Solo prove facili (senza Soo, conducente, IMG_0413)")
    print("\nKiller unico con tutte le prove: Maleko. OK")
