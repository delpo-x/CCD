# Registro delle iterazioni (SOLO DIRETTORE)

Il caso è stato interrogato come lo farebbe un investigatore con trent'anni di mestiere: ogni iterazione cerca un buco, lo trova, e poi si ripara o si distrugge e si ricostruisce. Il controllo meccanico è in `verifica/verifica_caso.py` (cronologia fisicamente possibile, prove coerenti con la verità, chi può trovarsi nell'ufficio alle 23:15 con e senza ciascuna prova).

## Iterazione 0 · Audit del caso precedente: scartato

Domanda dell'investigatore: «Chi poteva essere nell'ufficio alle 23:15, usando solo prove oggettive?»

| Sospetto | Esito |
|----------|-------|
| Lani, Nalu, Ike, Kapono, Akoni, Pua, Noe, Auntie Lei | Tutti con un alibi documentato (palco, scontrini, bolla, due foto) |
| Maleko | Aveva solo la finestra 23:14–23:20, ma era «il testimone» |
| Kalea | Unica senza alibi |

**Verdetto**: soluzione per esclusione in un quarto d'ora. Il registro con le iniziali «K.H.» e il taccuino di Noe puntano a lei dal primo minuto. Difficoltà reale: **35/100**. Troppo semplice. Distruggo l'assassino e riscrivo la storia attorno a lui.

Altro difetto strutturale: il padrone di casa (Keoki) era interpretato dal direttore. Va eliminato.

## Iterazione 1 · Nuova soluzione: Maleko. Prove e buchi trovati

Ricostruzione: Kalea resta colpevole di corruzione, non di omicidio. L'assassino è suo fratello Maleko.

Buchi trovati nel primo impianto:

1. **Il registro bruciato nel vicolo.** Ike e Kapono scaricavano lì dal portello fino alle 23:35 e avrebbero visto Maleko. → Il registro brucia nel braciere della cucina; Maleko non usa mai la porta di servizio.
2. **Chi aveva la pagina strappata?** Keoki l'aveva in tasca; se Maleko la prende dal corpo, la mezza pagina nel cestino non si spiega. → Kalea gliela strappa di mano alle 23:10: una metà nel cestino, l'altra nella sua borsetta. Maleko prende dal corpo solo il registro.
3. **Il 23:15 non era un dato.** Nessuno poteva dire che lo sparo fosse alle 23:15. → La chiamata di Hanale Soo (capo campagna di Kalea) sente «un botto più secco in mezzo ai botti» alle 23:15.
4. **Alibi di Kalea: da dove viene?** Se è colpevole solo di bugie, serve un alibi vero che le costi qualcosa. → Chiamata in arrivo di Soo 23:14:05–23:17:20 dal bagno signore. Prova che non ha sparato, e prova che ha mentito sulla veranda.
5. **Solo Maleko senza alibi.** La conferma per esclusione (iterazione 0) si ripresenta: eliminati gli altri, resta lui. → Il cluster in veranda (Akoni, Pua, Auntie Lei, Noe) viene scagionato solo da IMG_0414, che Noe non vuole mostrare (la sua macchina contiene foto private di Kalea). Senza IMG_0414 restano plausibili **quattro** persone oltre a Maleko (verificato dallo script).
6. **Come si arriva a Maleko senza eliminare?** Serve una prova positiva indipendente. → Catena: registratore con due pause (21:45–21:52 e 23:14–23:19) + lampadina del corridoio allentata dopo le 23:14 + revolver nella cassa degli ampli + registro bruciato in cucina + cassetto vuoto alle 22:55 + schiena vista da Auntie Lei al brindisi.
7. **I tempi di Kapono.** Lo script ha scoperto che Kapono non poteva arrivare dal fondo dello scantinato in 20 secondi. → Esce alle 23:12:20, passa dal corridoio alle 23:13, torna giù alle 23:14.
8. **Il racconto di Keoki (appendice).** Nel racconto, l'ultimo visitatore è identificato da una stretta a due dita e da un bicchiere di bianco: sono i segni di Kalea. → Da riscrivere (vedi iterazione 3).

## Iterazione 2 · Interrogatorio a freddo: «Se fossi il tenente»

L'investigatore legge solo ciò che i giocatori sapranno, senza la soluzione.

**Sospetto 1: Kalea.** Movente (396.000), bugia (veranda fino alle 23:30), presenza nell'ufficio (E01), mezza pagina nel cestino, petali sul bavero. → Un giocatore attento la tiene in cima alla lista per almeno mezz'ora.

**Sospetto 2: Akoni.** Ha pagato lui. Ha avuto l'ultimo incontro (23:00–23:08), ha mentito sul colloquio («solo il prezzo»), ha registrato «il voto è già comprato». Alibi: foto 23:12 e 23:16, ma tre minuti di buco. → Resta in lista fino a IMG_0414.

**Sospetto 3: Noe.** È la fotografa: non è mai nelle sue foto. Ama Kalea, ha il taccuino. → Resta in lista finché non mostra IMG_0414.

**Sospetto 4: Kapono.** Dice di non aver lasciato lo scantinato. Il conducente smentisce. Il biglietto di ricatto è in tasca. → Cade con la testimonianza del conducente, ma la bugia lo compromette per mezz'ora.

**Sospetto 5: Nalu.** Ruba alla cassa, ha la chiave, ha i debiti, sa dei coriandoli. Alibi limpido (cannoni, scontrini), ma i suoi strofinacci hanno la stessa sigla di quello nel revolver. → Falsa pista di mestiere.

**Ripensamento dell'investigatore**: «Troppo ordinato». Il registro è bruciato, ma i petali, la mezza pagina e il biglietto «K. – 23:10» portano tutti a una sola donna. Cerco chi non ha nulla da guadagnare dal fatto che sia lei la sospettata, e invece lo fa. Maleko è il testimone che la accusa, mentre tace il proprio buco.

**Risultato**: i due percorsi funzionano.

- **Per esclusione**: servono IMG_0414, la chiamata di Soo e il conducente. Nessuno viene gratis.
- **Per prova positiva**: servono almeno tre dei sei elementi della catena su Maleko.

## Iterazione 3 · Buchi residui e riparazioni

| # | Buco | Riparazione |
|---|------|-------------|
| 1 | Il direttore non sa se rivelare che Maleko è un poliziotto | Scheda del capo: sa che esiste un agente sotto copertura solo se qualcuno lo dice o se un giocatore chiede di controllare il nome |
| 2 | Il registratore di Maleko si ascolta solo se lui lo consegna | Il capo può sequestrare ogni registratore dopo un'accusa documentata contro Maleko; Noe ha la sua cassetta |
| 3 | Il «passo di Maleko» nel racconto di Kalea è soggettivo | Resta un indizio soggettivo: la prova oggettiva è la lampadina e la pausa del registratore |
| 4 | Troppe telefonate come alibi | Soo (Kalea), Lopaka (Akoni e Pua, voce sullo sfondo) sono due; gli altri alibi sono scatti, scontrini, bolla, palco, coriandoli |
| 5 | Auntie Lei esclusa per il bastone: assunzione | È confermata anche da IMG_0414 e dalla voce che Lopaka sente |
| 6 | Il racconto di Keoki conduce a Kalea | Riscrivo il capitolo 3 (23:10–23:15): arriva prima Kalea, poi Maleko. L'ultimo visitatore alza due dita, il gesto dell'agente che ferma qualcuno |

## Iterazione 4 · Audit incrociato dei documenti finali

Dopo aver scritto tutte le schede, le missioni e il racconto, ho riletto ogni documento contro il fascicolo, le interviste e le prove, cercando contraddizioni.

| # | Buco | Riparazione |
|---|------|-------------|
| 1 | Il fascicolo diceva che il conducente se ne va alle 23:07; le schede, la bolla e il rapporto 4 dicono 23:35 | Corretto il fascicolo: il conducente resta fino alle 23:35 |
| 2 | Maleko dice «ho solo guardato dalla porta a vetri» e insieme «ero in fondo alla sala» | Nuova risposta: «Corridoio no. Sono entrato in sala dalla porta a vetri e basta» (interviste e scheda) |
| 3 | Noe dichiarava di non aver visto Keoki dal brindisi: falso, c'era | Risposta ufficiale riscritta: lo ha visto al brindisi, gli ha parlato l'ultima volta una settimana fa |
| 4 | Interviste: Ike «cugino di Akoni» | Corretto in «fratello minore» |
| 5 | Auntie Lei vede una schiena nello specchio dell'anticamera, ma l'anticamera non era nella planimetria | Aggiunta al fascicolo la riga «Anticamera» (specchio macchiato, guardaroba, sedia di Lei) |
| 6 | La matrice, le interviste e la soluzione citano codici E01–E26 che non avevano una tabella | Aggiunta la tabella «Codici E» in `riferimento_indizi.md` |
| 7 | La guida rimandava a `rapporto_05` per il controllo del nome di Maleko (è il 06) e a «E21» | Corretti i riferimenti |
| 8 | La matrice dava alibi ad Auntie Lei con la voce che Akoni avrebbe sentito al telefono: Lopaka sente Noe, non Lei | Alibi di Lei ancorato a IMG_0414; alibi di Noe a IMG_0414 e alla voce sentita da Lopaka |
| 9 | IMG_0414: Akoni «in primo piano, di spalle» sulla scala, ma Noe fotografa verso la sala | Akoni sul bordo sinistro, di profilo, sulla scala laterale |
| 10 | Maleko esce dalla veranda «dicendo che va a cercare Kalea», ma Pua, Lei e Noe non se lo ricordavano | Aggiunta la frase «Vado a cercare mia sorella» sulle tre schede: dà a Maleko una copertura e ai giocatori un appiglio |
| 11 | Racconto di Keoki: l'ultimo visitatore era Kalea, e Maleko non compariva | Racconto riscritto: Kalea alle 23:10, la striscia di luce che si spegne, il passo con la suola di gomma, le due dita alzate. Keoki non dice il nome perché l'ha promesso a Maleko alle 20:45 |
| 12 | Missioni e inviti parlavano di un Atto 1 con Keoki giocato dall'ospite | Riscritti tutti: nessun compito in sala prima del delitto, nessun ospite-personaggio |

Rieseguito `verifica_caso.py`: nessuna violazione.

## Valutazione finale della difficoltà

| Criterio | Punti su 10 |
|----------|-------------|
| Il sospetto ovvio (Kalea) è innocente dell'omicidio ma colpevole di altro | 10 |
| Almeno due «false soluzioni» complete (Kalea, Akoni/Pua, Noe) | 9 |
| Nessun indizio da solo risolve il caso | 9 |
| Esiste una prova positiva indipendente dall'esclusione | 9 |
| L'alibi di Maleko è debole ma non assurdo | 8 |
| Informazioni nascoste dietro ostacoli di gioco (Noe, registratore, rapporto di giugno) | 9 |
| Equità: ogni elemento necessario è raggiungibile | 9 |
| Carico gestibile per un tavolo di dieci | 8 |
| Coerenza meccanica (script) | 10 |
| Il colpevole non è il «trope» atteso | 9 |
| **Totale** | **90/100** |

Nota onesta: il punteggio è una stima di progetto, non un test sul campo. Il vero collaudo è una serata con dieci persone; dopo la prima partita ritaratura con la scala di suggerimenti (vedi guida del direttore).
