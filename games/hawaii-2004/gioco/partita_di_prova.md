# La partita di prova (solo direttore)

Una prima serata vera serve a una cosa: capire dove il gioco regge e dove va ritarato. Il modello `verifica/simulazione_montecarlo.py` dà solo stime; questa serata dà i dati con cui correggerle. Non è una recita da rifinire: osserva, annota, e lascia che le cose vadano storte.

## Chi invitare

- Dieci giocatori, almeno due alla prima esperienza. Se ne hai solo otto o nove, vedi «Con meno di dieci».
- Dai i ruoli come dice la tabella della guida: i principianti sui ruoli facili (Nalu, Kapono, Ike, Auntie Lei). Kalea e Maleko vanno a chi ha già giocato o ama recitare.
- **Solo la tabella di difficoltà, nessun bilanciamento.** Non dare il ruolo favorito al giocatore più debole né il più sfavorito al più bravo per pareggiare le chance: la prova serve a misurare quanto Kalea è davvero favorita e quanto Maleko è svantaggiato. Prima della serata scrivi, per ciascun giocatore, ruolo ed esperienza (principiante, medio, esperto).
- Se puoi, scegli almeno una persona che parla volentieri e una che parla poco: la serata si vede dalla distanza tra le due.
- Avvisa tutti che è una prova: sul finire chiederai un parere di cinque minuti.

## Quando mandare i materiali

Una settimana prima, come da guida: invito, scheda e missione a ciascuno, con la riga sulle allergie. Chiedi di non condividere niente. Il giorno stesso della serata ti basta ricordare l'orario.

## Cosa stampare e preparare

Dalla guida, «Preparazione». In breve, per la prova:
- inviti, schede e missioni (30 fogli) e la piantina in dieci copie;
- le carte indizio e i rapporti, in buste divise per luogo;
- le dieci buste con gli oggetti, chiuse e con il nome del proprietario;
- le cinque carte piatto e le sei carte scena (nelle buste, con gli oggetti);
- campanella, clessidra da 3 minuti, cronometro, quaderno, post-it, un d6 a testa;
- il cartellone delle dichiarazioni;
- se fai la cena, il buffet come in `cena.md`, con i vassoi in frigo.

**Consiglio:** gioca la versione completa, con la cena. Il buffet è il punto più incerto del progetto: se lo togli alla prima prova non saprai se funziona.

## Il cronometro, minuto per minuto

| Ora serata | Gioco libero | Cosa succede | Cosa guardi |
|------------|--------------|--------------|-------------|
| 0:00–0:10 | | Introduzione, consegna delle buste | Qualcuno fa domande sulle regole? Quali? |
| 0:10–0:35 | | Intervista, 25 minuti | Chi si annoia mentre non tocca a lui? Quante risposte false al tenente? |
| 0:35–0:45 | 0–10 | Prime mosse | I principianti trovano la prima mossa? Chi non si è mosso al minuto 10? |
| 1:15 | 40 | Brindisi di Lani (se lo fa) | Come reagisce il tavolo? Calano le voci? |
| 1:15–1:30 | 40–55 | Buffet, se c'è | Il cibo interrompe o alimenta le conversazioni? Le carte piatto vengono lette? |
| circa 1:20 | circa 45 | Verità a metà di Kalea | Chi la innesca? Succede, oppure no? |
| 1:30 | 55 | Campanella dell'ultima chiamata | Le buste chiuse escono, passano, restano in tasca? Chi dice «la tengo»? |
| 1:30–1:50 | 55–75 | Pressione | Qualcuno resta senza nulla da fare? |
| 1:50–2:00 | | Discussione aperta, 10 minuti | Bastano? Pause lunghe? Qualcuno dice «è stata Kalea» ad alta voce? Quanti? |
| 2:00–2:15 | | Accuse scritte | Chi scrive cosa. |
| 2:15–2:30 | | Rivelazione, epiloghi, punti, bonus tavolo | Il bonus scatta? Chi vince? |

## Cosa osservare

Le otto cose del piano d'azione, più quattro dalle simulazioni.

**Dal piano:**
1. Dopo la campanella, gli indizi chiusi escono o restano in tasca?
2. I 10 minuti di discussione bastano, o servono 15?
3. I principianti trovano la prima mossa entro 10 minuti?
4. Il séparé è usato? Genera sospetto o viene ignorato?
5. Il brindisi di Lani arriva, e che effetto ha sul tavolo?
6. Il buffet interrompe o alimenta le conversazioni?
7. Kalea fa la rivelazione intorno al minuto 45? Chi la innesca?
8. Quante accuse su Maleko, e il bonus tavolo scatta?

**Dalle simulazioni (quelle che il modello non sa dire):**
9. Chi resta fermo per più di 10 minuti? (Il modello stima che succeda in una partita su cinque.)
10. Quali prove emergono davvero: lampadina, cassetto, porta a vetri, movente, nastro? Il modello dà la lampadina al 42% e il movente al 30%.
11. Quanti dicono «è stata Kalea» prima della rottura di Maleko, e Maleko confessa?
12. Chi vince, e quanti punti ha Kalea rispetto agli altri? Il modello la dà favorita.

## Il foglio di osservazione

Tieni accanto al quaderno uno schema con queste righe. Scrivi l'ora (sul cronometro) accanto a ogni evento.

- Chi ha fatto la prima mossa entro il minuto 10 / chi no.
- Séparé: coppie, orari, durata.
- Brindisi di Lani: ora, reazioni.
- Buffet: ora d'inizio, chi serve, conversazioni nate.
- Verità di Kalea: ora, chi chiede, parole dette.
- Campanella: buste aperte, passate, consegnate, trattenute («la tengo»).
- Rapporti richiesti: quali, da chi, ora.
- Indizi consegnati: quali, a chi, ora.
- Discussione: chi parla, chi tace, nomi fatti ad alta voce, confessione sì/no.
- Accuse scritte: una riga per giocatore, e le prove citate.
- Punti finali e bonus tavolo.
- Momenti di confusione: cosa non era chiaro, e a chi.

## Cosa non fare durante la serata

- Non suggerire la soluzione, neanche se il tavolo sbaglia strada. Usa la scala dei suggerimenti della guida, dal gradino più basso.
- Non cambiare le regole in corsa. Se una regola non regge, annotalo e vai avanti: lo sistemi dopo.
- Non spiegare perché un indizio non è comparso. Annotalo.

## Dopo la serata

**Cinque minuti di parere a caldo**, con questo schema (vale per tutti, anche se il tavolo ha vinto o perso):
1. Hai capito cosa dovevi fare entro i primi 10 minuti? (sì / più o meno / no)
2. C'è stato un momento in cui non sapevi cosa fare? Quando?
3. Hai parlato con tutti quelli con cui volevi?
4. La cena ti ha aiutato a recitare, o ti ha distratto?
5. Quale scena ricorderai? Quale taglieresti?
6. Da 1 a 5, quanto ti sei sentito parte della storia?
7. Da 1 a 5, quanto era difficile il tuo ruolo? E quanto avresti voluto che lo fosse?
8. Cambieresti qualcosa nelle regole? Cosa?

Raccogli le risposte su fogli o a voce, come preferisci, ma scrivile la sera stessa.

**Entro il giorno dopo**, riporta qui sotto le cifre, che servono per correggere il modello:
- numero di giocatori, e quanti alla prima esperienza;
- ruolo ed esperienza di ognuno (la tabella scritta prima della serata);
- azioni stimate per giocatore (anche a occhio: poche, medie, molte);
- prove emerse (le cinque della catena e le esclusioni);
- numero di accuse su Maleko, e di accuse su altri;
- confessione di Maleko: sì/no, dopo quali parole;
- punti finali di tutti e vincitore;
- durata reale di ogni fase.

Con questi dati si rilancia `simulazione_montecarlo.py` correggendo le probabilità scritte in cima allo script, e si decide se ritarare punteggio, schede o tempi.

## Con meno di dieci

- **Nove giocatori:** togli Noe. IMG_0413 e le foto di Kalea restano al direttore, che le consegna a richiesta del tavolo. Il compito di Kapono su Noe cade, e Kapono ha una missione in meno.
- **Otto giocatori:** togli anche Pua. Il rapporto 05 mostra Akoni da solo.
- Sotto gli otto, rimanda: le dipendenze tra le missioni non reggono.

Queste riduzioni sono un'ipotesi da collaudare, non un fatto verificato. Con meno di dieci, la soglia del bonus tavolo (sette accuse su nove possibili) va rivista: scendi a cinque.

## Se qualcosa va storto

- **Il tavolo si ferma:** scala di suggerimenti, dal gradino più basso. Se serve, convoca al tuo tavolo chi è fermo da dieci minuti.
- **Un giocatore esce o si ammala:** gioca con nove (vedi sopra). Non prendere il suo ruolo.
- **La cena va in ritardo:** salta il buffet, mantieni brindisi e campanella.
- **Il colpevole è scoperto troppo presto:** non interrompere. Chiedi al tavolo che prove ha, e fai scrivere le accuse prima del tempo.
