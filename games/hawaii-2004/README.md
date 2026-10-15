# Last Call al Kapu Lounge

Gioco di ruolo investigativo noir, in italiano, per **10 giocatori + 1 direttore**. Durata: circa 2 ore e 30. Waikiki, Honolulu, sabato 14 agosto 2004.

Keoki Kealoha, fondatore del Kapu Lounge, viene trovato morto nel suo ufficio. Nel locale sono rimaste dieci persone con un debito, un segreto o un motivo per volerlo zitto. Il tenente Alapai della Omicidi ha chiuso le porte: nessuno esce finché non sa chi è stato.

## Come si gioca
- **Una sola stanza.** Tutta la serata si svolge in un'unica stanza, la sala del Kapu dopo la chiusura. Ufficio, corridoio, cucina, veranda e scantinato esistono solo nel racconto: i giocatori dicono a voce cosa cercano e dove, e il direttore consegna la carta o l'oggetto. Carte indizio, rapporti e oggetti sono materiali veri (stampati o di scena) e si usano lì dentro.
- Il **direttore** non gioca un personaggio: dirige. In scena è il tenente Alapai e interroga i giocatori; fuori scena è il narratore. Conosce la soluzione e non la dice.
- Ciascuno dei **10 giocatori** interpreta il suo personaggio con coerenza: ha dei segreti, delle bugie, delle paure, degli affetti.
- **L'intervista** (25 minuti): il tenente interroga ogni giocatore davanti a tutti. Ne esce un bacino di informazioni di valore diverso, vere e false.
- **Il gioco libero** (75 minuti): nessuna regia. I giocatori parlano, cercano, bluffano, si alleano. Il direttore consegna le carte indizio e, su richiesta motivata, i rapporti del laboratorio (solo il referto arriva da solo). Al minuto 55 suona la campanella dell'ultima chiamata: ogni busta ancora chiusa va aperta, passata o consegnata al tenente.
- **La discussione, le accuse e la rivelazione** (40 minuti): dieci minuti di discussione aperta davanti al tenente, poi ognuno scrive chi è stato e perché. Il direttore ricostruisce il delitto. Se il tavolo indica quasi tutto lo stesso colpevole, c'è un bonus per tutti.

Il caso è costruito perché **ogni personaggio abbia almeno cinque elementi di sospetto**, e perché la soluzione si possa raggiungere per due vie indipendenti (per esclusione e per catena positiva di prove).

## Contenuto della cartella
- `gioco/` – guida del direttore, soluzione, fascicolo del caso, matrice dei sospetti, registro delle iterazioni di verifica, banca di domande dell'intervista, riferimento indizi, mini-trame e punteggio (**SPOILER, solo direttore**)
- `personaggi/` – inviti, schede e **missioni segrete** dei 10 giocatori; dossier della vittima e scheda del tenente (solo direttore)
- `oggetti/` – dieci oggetti personali, da consegnare in buste chiuse
- `indizi/` – 17 carte indizio per i giocatori e, in `indizi/rapporti/`, 7 rapporti di laboratorio e polizia
- `verifica/verifica_caso.py` – controllo meccanico di spostamenti, tempi e alibi: verifica che resti un solo sospetto con tutte le prove
- `immagini/PROMPTS.md` – prompt per generare ritratti e oggetti di scena
- `scheletro/` – scheletro relazionale generato con murder-generator (vedi `scheletro/MAPPATURA.md`)
- `racconto-keoki.md` e `racconto-keoki.pdf` – racconto breve dal punto di vista di Keoki, da leggere dopo la partita
- `last-call-kapu-lounge-completo.pdf` – volume completo del direttore

## Ruoli

| N. | Personaggio | Ruolo | Genere |
|----|-------------|-------|--------|
| 1 | Lani Kealoha | Direttrice del locale, figlia di Keoki | F |
| 2 | Nalu Akana | Barman capo, cresciuto in casa Kealoha | M |
| 3 | Ikaika «Ike» Mahoe | Importatore | M |
| 4 | Akoni Mahoe | Emissario di Pacific Crest | M |
| 5 | Pualani «Pua» Mahoe | Agente immobiliare | F |
| 6 | Maleko Hanohano | Cliente fisso | M |
| 7 | Kalea Hanohano | Consigliera comunale | F |
| 8 | Noe Sato | Giornalista d'inchiesta | F |
| 9 | Kapono Medeiros | Tuttofare del locale | M |
| 10 | Leilani «Auntie Lei» Kealoha | Sorella di Keoki, socia | F |

I nomi sono hawaiani e si leggono come sono scritti, vocale per vocale: Keoki (ke-O-ki), Ikaika (i-KAI-ka), Pualani (pu-a-LA-ni), Akoni (a-KO-ni), Maleko (ma-LE-ko), Kalea (ka-LE-a), Kapono (ka-PO-no), Hanohano (ha-no-HA-no), Mahoe (ma-HO-e). Kuki è il soprannome di Lani, dall'inglese «cookie». La «K.» sul foglio del blocco (indizio 1) può indicare Kalea o Kuki: l'ambiguità è voluta.

Le immagini vanno salvate in `immagini/` con i nomi indicati in `PROMPTS.md`.

## Per cominciare
Il direttore legge `gioco/guida_direttore.md`, poi `gioco/soluzione.md`. Ai giocatori manda solo invito, scheda e missione.
