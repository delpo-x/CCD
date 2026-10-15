---
id: "09"
title: "Verifica di coerenza delle modifiche"
labels: [wayfinder:grilling]
status: closed
assignee: claude
blocked_by: ["04", "05", "06", "07", "08"]
---

## Question

Le modifiche decise non creano contraddizioni negli indizi, negli alibi, nei moventi, nella cronologia o nella soluzione? Quali controlli (script `verifica_caso.py`, rilettura incrociata) vanno rifatti e quali file toccano?

## Resolution

Le decisioni dei ticket precedenti reggono la cronologia, gli alibi e la catena di prove, con cinque correzioni. `verifica_caso.py` è stato rilanciato sullo stato attuale dei file: «Killer unico con tutte le prove: Maleko. OK». Il colpevole, gli orari e la catena non cambiano.

### Cosa regge
- **Alibi con prezzo.** Il conducente e la bolla di Habana provano che Ike e Kapono scaricavano; la telefonata di Akoni a Las Vegas e le foto restano ottenibili con le stesse ricerche di oggi. Il prezzo è conseguenza della richiesta del tavolo, non un rifiuto possibile: chi chiede il rapporto 4 espone il contrabbando.
- **Scaletta.** Brindisi al minuto 40, buffet 40–55, campanella 55, pressione 55–75, discussione, accuse.
- **Prime mosse.** Le dieci esistono già nelle missioni.
- **Veranda, 6,5 e 7,2.** Non sono vecchi: la veranda è il luogo raccontato, il séparé l'angolo nella sala; 6,5 milioni è la prima offerta e 7,2 il rilancio (oggetto 04).

### Le cinque correzioni
1. **Pua è sorella di Akoni e di Ike**, non ex moglie: lo dicono `Character_4` e `interviste.md`. La tensione diventa un regolamento di conti tra fratelli (Akoni 54, Pua 50, Ike 41). Zero modifiche a schede e interviste.
2. **Il 22:05 è il colloquio di Nalu con Keoki**, non un addio a Lani. Lani chiede proprio quello, e Nalu, se spinto, aggiunge «gli ho detto che me ne vado». Ciò che Nalu nasconde è dove sono finiti i 4.000 dollari presi dalla cassa (a Ike), non dove era. Resta al bancone: la sorveglianza della PB non cambia.
3. **La macchina fotografica di Noe non si può tenere** all'ultima chiamata. Lo script lo dimostra: senza IMG_0413 restano possibili Akoni, Pua, Noe e Maleko. Noe la mostra o la passa al tenente. Per gli altri oggetti la regola resta «la tengo, perdi il punto».
4. **Serata di 2 h 30.** 0:00–0:10 introduzione; 0:10–0:35 intervista; 0:35–1:50 gioco libero; 1:50–2:00 discussione aperta (10 minuti); 2:00–2:15 accuse; 2:15–2:30 rivelazione, epiloghi e bonus tavolo.
5. **Quattro piccole correzioni.**
   - Kalea: il «Cedo se Noe ti guarda negli occhi» e la riga «lo dirai solo se cedi» sulla luce sotto la porta del bagno diventano un solo innesco.
   - Maleko: *cede se due giocatori dicono ad alta voce «è stata Kalea» durante la discussione* (le accuse scritte sono segrete e non si possono contare).
   - Il lei sul piatto vuoto di Keoki è di plumeria bianca, non viola: il viola è del petalo di Kalea (indizio 04).
   - «Adottivo» sparisce: Nalu è «cresciuto in casa Kealoha».

### File da toccare nell'implementazione
- **Schede e inviti** (`personaggi/Character_1…10_scheda_personaggio.md`, `_invito.md`, `_missione.md`): «Voglio / Temo / Cedo se» su tutte; quattro fondi (Akoni, Pua, Kapono, Auntie Lei); Nalu non più adottato (`Character_1` due righe, `Character_2` invito e scheda); i 4.000 dollari e il «me ne vado» di Nalu; brindisi di Lani; innesco unico di Kalea; due battute di Maleko; costi degli alibi (Akoni, Ike, Kapono, Noe); durata 2 h 30 negli inviti.
- **Indizi.** `indizi/indizio_11.md`: il biglietto di Kapono chiede anche «e lascia stare Noe». Oggetto 05 invariato.
- **Guida e punteggio.** `gioco/guida_direttore.md`: scaletta a 2 h 30, discussione, campanella al 55, séparé, buffet, bonus tavolo, camera non trattenibile, difficoltà dei ruoli. `gioco/mini_trame.md`: bonus tavolo +5, regola delle buste, epilogo collettivo.
- **Documenti del caso.** `gioco/matrice_sospetti.md` (costi degli alibi), `gioco/soluzione.md` (epilogo collettivo), `gioco/interviste.md` (riga 30, adottivo), `README.md` (durata, adottivo), `gioco/criticita_aperte.md` (nota).
- **Materiali nuovi.** Sei carte scena, cinque carte piatto, scheda di cucina e servizio per il direttore.
- **Verifica.** `verifica/verifica_caso.py`: vedi sotto. `pdf.json`: nuovi file nel PDF; ricostruzione dei due PDF.

### Controlli da rifare dopo le modifiche
1. **Script esteso.** Oggi non modella la telefonata di Akoni (rapporto 2) né Pua sentita da Lopaka (rapporto 5). Aggiungere queste due prove al modello, poi rilanciare tutte le ablazioni (senza IMG_0413, senza Soo, senza conducente, senza tabulato di Akoni, senza Lopaka). Atteso: Maleko resta l'unico possibile con tutte le prove, e senza IMG_0413 restano Akoni e Pua scagionabili dalle altre due.
2. **Grep di coerenza.** `adottiv`, `ex moglie`, `2 ore e 20`, `2:20`, `2 h 20`, `75 minuti` (resta, è il gioco libero), `veranda` (non toccare).
3. **Rilettura incrociata** di ogni «Cedo se…» contro la catena di prove e gli alibi: Kalea e Maleko prima di tutti.
4. **Prima mossa.** Ogni scheda ha ancora un'azione di apertura chiara entro i primi 10 minuti dopo le tre righe in più.
5. **Humanizer** su ogni testo nuovo per i giocatori, **ui-ux-pro-max** sull'impaginazione, poi build dei PDF e controllo visivo.
