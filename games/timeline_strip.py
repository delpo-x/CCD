# -*- coding: utf-8 -*-
"""Pagina «La tua serata, a colpo d'occhio» per il fascicolo di un giocatore.

Legge la sezione con gli orari dalla scheda del personaggio e produce markdown
con una striscia SVG (asse 20:00-24:00, fascia dell'omicidio) e l'elenco numerato.
"""
import re


def minuti(hhmm):
    h, m = hhmm.split(":")[:2]
    return int(h) * 60 + int(m)


def striscia(root, n, nome):
    testo = (root / f"personaggi/Character_{n}_scheda_personaggio.md").read_text(encoding="utf-8")
    sez = re.search(
        r"^## (?:La tua serata, com'è andata davvero|Cosa hai fatto davvero[^\n]*)\n(.*?)(?=^## )",
        testo, re.M | re.S).group(1)
    voci = []
    for riga in sez.split("\n"):
        m = re.match(r"- \*\*(\d{1,2}:\d{2}(?::\d{2})?)([^*]*)\*\*\s*(.*)", riga)
        if m:
            voci.append((minuti(m.group(1)), (m.group(1) + m.group(2)).strip(), m.group(3).strip()))
    voci.sort(key=lambda v: v[0])

    W, X0, T0, TB, T1 = 520, 14, 20 * 60, 23 * 60, 23 * 60 + 45
    LUN = W - 2 * X0
    # scala spezzata: 20-23 compresse (28%), dopo le 23 ingrandite (72%)
    x = lambda t: X0 + ((t - T0) / (TB - T0) * 0.28 if t <= TB else 0.28 + (t - TB) / (T1 - TB) * 0.72) * LUN
    lanes, ultimi = [], []
    for t, _, _ in voci:
        k = 0
        while k < len(ultimi) and x(t) - ultimi[k] < 21:
            k += 1
        if k == len(ultimi):
            ultimi.append(-99)
        ultimi[k] = x(t)
        lanes.append(k)
    H = 40 + 22 * len(ultimi) + 30
    ay = H - 26
    s = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Merriweather, Georgia, serif">']
    s.append(f'<rect x="{x(23*60+10):.1f}" y="4" width="{x(23*60+20)-x(23*60+10):.1f}" height="{ay-4}" fill="#B3125B" opacity="0.14"/>')
    s.append(f'<text x="{x(23*60+20)+3:.1f}" y="14" font-size="9" fill="#B3125B" font-weight="700">omicidio</text>')
    s.append(f'<line x1="{X0}" y1="{ay}" x2="{W-X0}" y2="{ay}" stroke="#0F6B6B" stroke-width="1.6"/>')
    ticks = [h * 60 for h in range(20, 24)] + [23 * 60 + m for m in (10, 20, 30, 40)]
    for tk in ticks:
        s.append(f'<line x1="{x(tk):.1f}" y1="{ay-4}" x2="{x(tk):.1f}" y2="{ay+4}" stroke="#0F6B6B" stroke-width="1.2"/>')
        s.append(f'<text x="{x(tk):.1f}" y="{ay+17}" font-size="9.5" fill="#4A4757" text-anchor="middle">{tk//60:02d}:{tk%60:02d}</text>')
    for (t, _, _), k in zip(voci, lanes):
        cy = ay - 16 - 22 * k
        s.append(f'<line x1="{x(t):.1f}" y1="{cy+9}" x2="{x(t):.1f}" y2="{ay}" stroke="#0F6B6B" stroke-width="0.8"/>')
    for i, ((t, _, _), k) in enumerate(zip(voci, lanes)):
        cy = ay - 16 - 22 * k
        s.append(f'<circle cx="{x(t):.1f}" cy="{cy}" r="9" fill="#B3125B"/>')
        s.append(f'<text x="{x(t):.1f}" y="{cy+3.5}" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">{i+1}</text>')
    s.append("</svg>")

    righe = ["# La tua serata, a colpo d'occhio", "",
             f"Il filo delle ore di {nome}, dalle 20 a mezzanotte. È la **verità del tuo personaggio**: non è quello che dirai al tenente, e non va mostrata. La fascia rosa è la finestra in cui, secondo il medico, è morto Keoki. Dopo le 23 la scala è ingrandita.",
             "", '<div class="striscia">' + "".join(s) + "</div>", ""]
    for i, (_, ora, t) in enumerate(voci):
        righe.append(f"{i+1}. **{ora}** {t}")
    return "\n".join(righe) + "\n"
