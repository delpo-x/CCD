# Gli enigmi (SOLO DIRETTORE)

Cinque rompicapo da tavolo, ispirati ai giochi investigativi con prove da maneggiare. Nessuno aggiunge informazione al caso: ognuno è una strada più divertente verso una prova che esiste già. Per questo la soluzione, il colpevole e la catena verificata non cambiano.

## Le quattro regole

1. **Nessun enigma è indispensabile.** Ognuno ha una via di uscita: se il tavolo non lo risolve entro l'orario indicato, lo apri tu e la prova entra in gioco lo stesso.
2. **Si gioca al tavolo del tenente.** Due o tre giocatori lavorano all'enigma, gli altri continuano a parlare e a cercare. Nessuno resta fermo più di cinque minuti.
3. **Aiuti a scalini.** Se chiedono aiuto, dai un solo scalino per volta, nell'ordine scritto sotto, con una pausa di almeno un minuto tra uno e l'altro.
4. **Punti.** Ogni enigma risolto vale **+2** a ciascuno dei giocatori che ci hanno lavorato, fino a tre. Segna i nomi su un post-it. Per giocatore si contano al massimo **+6**. Se lo apri tu per la via di uscita, nessun punto.

## Il terminale del tenente

`enigmi/terminale.html` è una pagina da tenere aperta su un telefono o un tablet al tuo tavolo, anche senza internet. I giocatori scelgono l'enigma, scrivono la risposta e la pagina dice «giusto» o «non ancora». Con il pulsante «Chiedi un aiuto» mostra lo scalino successivo. Serve se non vuoi controllare le risposte a mente. Se preferisci la carta, le soluzioni sono qui sotto.

Per rigenerarlo dopo una modifica: `python games/build_enigmi_terminale.py games/hawaii-2004`.

## Quando esce ciascun enigma

| N. | Enigma | Da dove nasce | Quando esce | Via di uscita |
|----|--------|---------------|-------------|---------------|
| 1 | La striscia cifrante | Riga in margine nel taccuino di Noe (indizio 12) | Quando Noe mostra il taccuino | Alla campanella (minuto 55) leggi tu la riga |
| 2 | La cassetta K-3 | Chiave d'ottone di Nalu (oggetto 02) | Quando Nalu porta la chiave al tavolo | Al minuto 65 la cassetta si apre da sola: «Nalu gira la chiave e il lucchetto cede: non era chiuso a fondo.» |
| 3 | Tre foto senza ora | Foto di Noe (indizi 06 e 26) e rapporto 05 | Quando ci sono insieme sul tavolo | Non serve uscita: è un bonus, le foto valgono comunque |
| 4 | La lavagna delle 23:15 | Tutte le prove di alibi | Appesa dall'inizio | Non serve uscita: si riempie nel gioco libero |
| 5 | Il nastro: cosa manca? | Registratore di Maleko (oggetto 06) | Quando il tenente lo sequestra o Maleko lo consegna | Se nessuno lo nota, alla fine dici tu: «Manca il boato» |

## Enigma 1: la striscia cifrante

**Cosa vedono.** In margine al taccuino di Noe (indizio 12): `FRSLD LQ N3 FKLDYH D QDOX`.

**Soluzione.** Cifrario di Cesare con scorrimento di 3 (la cifra 3 non cambia: è l'indizio per indovinarlo). Il testo è **COPIA IN K3 CHIAVE A NALU**.

**Cosa sblocca.** Dice dove sta la copia del registro (la cassetta K-3) e chi ha la chiave. Dà un motivo a Nalu per consegnare l'oggetto 02 e al tavolo per cercarlo.

**Aiuti.**
1. «Le lettere sono state spostate, non inventate.»
2. «Guardate la cifra: c'è un 3 in mezzo alle lettere, e una chiave ha una targhetta con un 3.»
3. Consegna la striscia cifrante (`enigmi/enigma_1_striscia.md`).

## Enigma 2: la cassetta K-3

**Cosa vedono.** Una cassetta con tre rotelle. Sul coperchio: «Quanto mi è costato il silenzio? Scrivilo in migliaia di dollari.»

**Soluzione.** **396**. Ventidue pagamenti da 18.000 dollari fanno 396.000 (indizio 08 e indizio 13).

**Cosa sblocca.** La carta 13 (copia del registro con la nota di Keoki sulle sei pagine date a un agente). È la prova che lega il registro a Maleko, insieme al rapporto 06.

**Perché è un buon enigma.** Il giocatore che ha la mezza pagina (Kalea, o chi la trova nel cestino) e quello che ha la chiave (Nalu) devono parlarsi.

**Aiuti.**
1. «Cercate una somma, non una data.»
2. «Ventidue pagamenti, tutti uguali.»
3. «Diciottomila, ventidue volte. Le rotelle sono tre: migliaia.»

**Via di uscita.** Al minuto 65, se la cassetta è ancora chiusa, la apri tu. Nessun punto.

## Enigma 3: tre foto senza ora

**Come prepararlo.** Stampa le tre foto senza didascalia e scrivi sul retro: **1 = IMG_0414, 2 = IMG_0412, 3 = IMG_0413**.

**Soluzione.** L'ordine è **2-3-1**.
- La foto 2 (IMG_0412): Akoni guarda il telefono e non sta ancora telefonando. La chiamata del tabulato inizia alle 23:13:10, quindi è la prima.
- La foto 3 (IMG_0413): i coriandoli sono appena esplosi, cioè alle 23:15, e Akoni è sulla scala, al telefono.
- La foto 1 (IMG_0414): Akoni è tornato in veranda, ancora al telefono, e la sedia è vuota. Il rapporto 05 conferma che dopo i botti Akoni ha ripreso a parlare e c'era una donna che diceva «un'altra, ferma».

Risposta alle domande della carta: Maleko lascia la veranda tra le 23:12 e le 23:16 (la sua sedia è vuota nella foto 1). In tutte e tre le foto ci sono Akoni, Pua e Auntie Lei.

**Aiuti.**
1. «Il tabulato di Akoni dice quando comincia la chiamata.»
2. «I coriandoli esplodono a un orario preciso, lo sanno tutti.»
3. «Una sola foto ha Akoni che non telefona ancora.»

## Enigma 4: la lavagna delle 23:15

**Come prepararla.** Stampa la carta in grande (A3 se puoi) e appendila accanto alla mappa dei luoghi. Lascia i pennarelli sul tavolo.

**Regola di compilazione.** Si scrive una riga solo se la prova esiste e un giocatore la porta al tavolo. Tu controlli che il codice sia davvero quello giusto. Un «l'ha detto lui» non basta.

**Soluzione, riga per riga.**

| Persona | Dov'era | Prova |
|---------|---------|-------|
| Lani | Sul palco col microfono | Testimonianza di sala, conto alla rovescia |
| Nalu | Al bancone, spara i coriandoli | Scontrini 23:14–23:17 (E05) |
| Ike | Allo scantinato | Bolla (E07) e conducente (E23) |
| Akoni | Sulla scala, al telefono | Foto IMG_0413 (E26), tabulato (E25) |
| Pua | Accanto alla porta | Foto IMG_0413 (E26), voce nella telefonata (E25) |
| Maleko | **Nessuna prova** | – |
| Kalea | Nel bagno del corridoio, al telefono | Tabulato (E02) e dichiarazione di Soo (E22) |
| Noe | In veranda, scatta la foto | IMG_0413 (la punta della scarpa, E26), voce nella telefonata (E25) |
| Kapono | Allo scantinato | Conducente (E23) |
| Auntie Lei | Seduta in veranda | Foto IMG_0413 (E26) |

**Si risolve** quando ogni riga ha una prova tranne una: **Maleko**. Se anche la riga di Kalea resta vuota perché mancano i rapporti 02 e 03, il tavolo li deve chiedere al tenente con una richiesta motivata. È la mossa che la lavagna insegna.

**Aiuti.**
1. «Un alibi vale solo se lo prova qualcosa che non dipende da chi lo dice.»
2. «Una persona non ha una riga piena: chi manca?»
3. «Due righe vuote, una si riempie con i rapporti del laboratorio.»

**Punti.** Vanno ai tre giocatori che scrivono le ultime tre righe.

## Enigma 5: il nastro, cosa manca?

**Quando.** Il registratore di Maleko (oggetto 06) si sequestra solo dopo un'accusa documentata. Quando succede, anziché leggere la trascrizione per intero, **fai ascoltare il nastro** leggendo ad alta voce, con voce piatta e senza commenti, il testo qui sotto.

> Musica, risate, saluti. Il brindisi di Keoki: «…e mahalo a tutti.» Un applauso. Ike che grida qualcosa su una barca.
> *Clic secco.*
> Voci, un bicchiere. Akoni: «Il voto è già comprato.» Più avanti Kalea: «Dillo a Keoki: finirà tutto domani.»
> Voci in veranda. Kalea al telefono: «Ufficio del sindaco…» Akoni e Pua parlano del «piano B». Qualcuno, in sala, comincia a chiamare il pubblico.
> *Clic secco.*
> Rumori di sala, voci, un tintinnio di bicchieri.

Non dire niente sul boato. Poi chiedi: «Cosa non si sente?»

**Soluzione.** Il **boato**: il conto alla rovescia e i cannoni dei coriandoli delle 23:15, che in veranda si sentono benissimo (lo dice anche Lopaka nel rapporto 05). Il buco del nastro li copre.

**Cosa prova.** Conferma, non accusa: l'ora la dà la foto IMG_0413. Chi nota il buco guadagna i punti.

**Aiuti.**
1. «Il nastro è continuo, ma tra i due clic manca qualcosa di molto rumoroso.»
2. «Quello che ricordate tutti, dalla veranda, alle 23:15.»

**Via di uscita.** Se nessuno lo nota, lo dici tu a fine ascolto: «Manca il boato.» Nessun punto.

## Cosa cambia nel resto del gioco

- `oggetto_02.md` e la missione di Nalu dicono che il lucchetto a tre cifre si risolve con l'enigma 2.
- L'indizio 12 ha la riga cifrata in margine.
- `regole_giocatore.md` spiega gli enigmi e il tetto di +6 punti.
- Il playtest va rifatto una volta con gli enigmi, per misurare i tempi e il tasso di accuse giuste: la lavagna del 23:15 può far scendere la difficoltà.
