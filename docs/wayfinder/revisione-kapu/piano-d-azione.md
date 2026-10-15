# Piano d'azione: revisione di Last Call al Kapu Lounge

Documento di consegna per le sessioni di implementazione. Contiene tutto ciò che serve senza dover rileggere la conversazione: le regole decise, i file da toccare, l'ordine, i controlli. Le decisioni complete, con le ragioni, stanno nei ticket in `tickets/`; qui sono ridotte all'azione.

**SPOILER**: il documento nomina l'assassino. Non distribuirlo ai giocatori.

## Obiettivo

Portare il caso a un livello superiore secondo i criteri decisi (ticket «Che cosa significa livello superiore»): legami ed emozione 40, rompicapo 40, tensione e ritmo 20, risate 0; tono noir serio e cupo; il direttore non innesca scene, reagisce; almeno due neofiti al tavolo; punti e missioni restano ma l'obiettivo principale è cooperativo.

Vincoli che non si toccano: **colpevole (Maleko), cronologia, catena di prove, nessun personaggio nuovo, 10 giocatori più il direttore**. Ogni modifica che sfiora uno di questi si ferma e si segnala.

## Regole di lavoro per ogni passo

1. Lingua: italiano. Ogni testo destinato ai giocatori passa dalla skill **humanizer**; ogni impaginazione dalla skill **ui-ux-pro-max**.
2. Modifiche con script Python che sostituiscono testo esatto, conservando il fine riga del file (molti file sono CRLF) e asserendo che il testo da sostituire compaia una volta sola.
3. A fine passo: lanciare il controllo del passo, poi commit con push. Un passo, un commit. I PDF si ricostruiscono solo alla fine di ciascuna ondata.
4. Comando di verifica del caso (deve chiudere con «Killer unico con tutte le prove: Maleko. OK»):
   `PYTHONUTF8=1 python games/hawaii-2004/verifica/verifica_caso.py`
5. Comando di build dei PDF (da PowerShell o Git Bash, con GTK3 sul PATH):
   `export PATH="$PATH:/c/Program Files/GTK3-Runtime Win64/bin"; cd C:/Users/nicola.IMPRONTE/Desktop/Nicola/CCD && PYTHONUTF8=1 uv run --project ../mystery-agents python games/build_game_pdf.py games/hawaii-2004`
   Racconto: `... python games/build_racconto_pdf.py games/hawaii-2004/racconto-keoki.md games/hawaii-2004/racconto-keoki.pdf`
6. Una sessione per passo. Ogni passo è dimensionato per stare in una sessione senza rileggere gli altri.

## Regole di gioco decise (riferimento unico)

- **Durata 2 h 30.** 0:00–0:10 introduzione; 0:10–0:35 intervista; 0:35–1:50 gioco libero (75 minuti); 1:50–2:00 discussione aperta con il tenente (10 minuti); 2:00–2:15 accuse scritte; 2:15–2:30 rivelazione, epiloghi, punti, bonus tavolo.
- **Cinque tempi del gioco libero.** 0–10 prime mosse; 10–40 scambi; 40 brindisi di Lani (invito sulla sua scheda, non regola); 40–55 buffet; 55 campanella; 55–75 pressione.
- **L'ultima chiamata del gioco, al minuto 55.** Suona la campanella del Kapu (oggetto di scena vero). Da lì ogni busta ancora chiusa va aperta, passata a qualcuno o consegnata al tenente; chi la tiene dichiara «la tengo» ad alta voce, perde il punto di quel compito e il tavolo perde quell'indizio. **Eccezione: la macchina fotografica di Noe non si può tenere**; Noe la mostra o la passa al tenente.
- **Il séparé.** Unico angolo privato nella sala: massimo due persone, clessidra da 3 minuti, porta socchiusa, tutti vedono chi entra e chi esce, nessuno origlia.
- **Buffet.** Minuti 40–55. Si resta in ruolo, il gioco non si ferma; carte e oggetti restano in tasca mentre si mangia (si parla e basta, bisbigli permessi); nessun indizio nuovo a tavola; gli scambi di oggetti si fanno prima o dopo.
- **Bonus tavolo.** Se almeno sette accuse corrette su Maleko (Maleko non accusa sé stesso: le accuse possibili sono nove), tutti prendono +5 e il direttore legge l'epilogo collettivo. Il vincitore resta chi ha più punti. Non altera la regola di parità né il punteggio di Maleko (+20 / +10 / 0, +5 se confessa prima delle accuse).
- **Difficoltà dei ruoli (solo nella guida del direttore).** Facile: Nalu, Kapono, Ike, Auntie Lei. Medio: Lani, Akoni, Pua, Noe. Difficile: Kalea, Maleko. I due neofiti ai ruoli facili.
- **Alibi con prezzo (nessun alibi cambia).** Akoni: la telefonata a Las Vegas, per usarla ammette che l'affare è morto. Ike e Kapono: il conducente, per usarlo ammettono gli scatoloni di Habana. Noe: le foto, per mostrarle apre la macchina fotografica con le immagini private di Kalea. Lani, Nalu, Pua, Auntie Lei: alibi senza prezzo.

## Ondata 1: serata giocabile a 2 h 30, senza cena

### Passo 0. Punto di ritorno
Tag `pre-revisione-2026-10` sull'ultimo commit buono (e push del tag). Si lavora poi su main.

### Passo 1. Regole e canone
**File:** `gioco/guida_direttore.md`, `gioco/mini_trame.md`, `README.md`, `gioco/soluzione.md`, `gioco/matrice_sospetti.md`, `gioco/interviste.md`.

Cosa cambia, con esempio:
- **Durata** da 2 ore e 20 a 2 ore e 30 ovunque; la tabella della guida diventa quella delle regole sopra. Esempio: la riga `| 1:50 – 2:05 | Il turno delle accuse |` diventa tre righe (discussione, accuse, rivelazione).
- **Guida:** aggiungere campanella al minuto 55, séparé, discussione di 10 minuti, bonus tavolo, camera non trattenibile, difficoltà dei ruoli. Esempio di formulazione per il direttore: «Al minuto 55 suona la campanella: "Ultima chiamata. Ogni busta ancora chiusa va aperta, passata o consegnata al tenente."»
- **Mini-trame:** bonus tavolo +5; regola delle buste all'ultima chiamata; epilogo collettivo; Pua e Akoni come fratelli (epilogo «Akoni scopre l'anticipo» diventa regolamento di conti tra fratelli).
- **Soluzione:** epilogo collettivo; punto di rottura di Maleko (due giocatori dicono ad alta voce «è stata Kalea» durante la discussione, allora confessa).
- **Matrice dei sospetti:** il costo di ciascun alibi (Akoni, Ike, Kapono, Noe) nella colonna «Lettura innocente» o in una colonna nuova «Costo».
- **Interviste:** riga 30, «Barman e figlio adottivo» diventa «Barman, cresciuto in casa Kealoha».
- **Non toccare:** veranda (luogo raccontato, corretto), 6,5 milioni (prima offerta), 7,2 milioni (rilancio, oggetto 04).

**Controllo:** `grep -rn -i "adottiv\|2 ore e 20\|2:20\|2 h 20" games/hawaii-2004 --include=*.md` non deve trovare altro che `scheletro/MAPPATURA.md`.

**Fine:** una sola durata (2 h 30) in tutti i file; la guida contiene tutte le regole sopra.

### Passo 2. Rete di sicurezza: estendere lo script
**File:** `verifica/verifica_caso.py`.

Oggi lo script non modella due prove che la soluzione cita: la telefonata di Akoni (rapporto 2) e Pua sentita da Lopaka (rapporto 5). Aggiungerle a `EVIDENCE`, creare i gruppi di ablazione `tabulato_Akoni` e `Lopaka_Pua`, e lanciare tutte le ablazioni: senza IMG_0413, senza Soo, senza conducente, senza tabulato di Akoni, senza Lopaka.

**Atteso:** con tutte le prove resta possibile solo Maleko. Senza IMG_0413, Akoni e Pua restano scagionabili dalle altre due prove nuove; Noe no (e per questo la camera non si può tenere). Se un'ablazione diverge, si segnala e non si corregge cambiando la cronologia.

**Fine:** lo script chiude con «Killer unico con tutte le prove: Maleko. OK» e le nuove ablazioni sono nell'output.

### Passo 3. Schede, missioni, inviti
Si divide in quattro sotto-sessioni, un commit ciascuna. Su ogni scheda si aggiungono le tre righe **Voglio / Temo / Cedo se** (bozze nella tabella sotto, da rifinire con l'humanizer) e si controlla che la prima mossa entro 10 minuti sia chiara.

| Giocatore | Voglio | Temo | Cedo se |
|---|---|---|---|
| Lani | tenere il Kapu come lo voleva papà | che la lettera di mamma dica che ho sbagliato tutto | Nalu smette di mentirmi |
| Nalu | uscire dal debito con Akoni e smettere di nascondermi | che Lani sappia di Ike prima che glielo dica io | Lani mi chiede in faccia «c'è qualcuno?» |
| Ike | tenere in piedi il giro un altro mese | il giorno in cui Auntie Lei vuole indietro i 50.000 | Nalu dice davanti a tutti che non si nasconde più |
| Akoni | chiudere l'affare da 7,2 milioni | che Las Vegas mi metta da parte | mi mettono davanti il registro |
| Pua | la commissione che è la mia pensione | di restare senza una lira | Akoni trova la ricevuta dell'anticipo |
| Maleko | salvare Kalea e il distintivo | che Kalea parli col tenente | due giocatori dicono ad alta voce «è stata Kalea» durante la discussione: confessa |
| Kalea | arrivare al voto in aula senza finire in carcere | che Noe scopra tutto | Noe mi guarda negli occhi e mi chiede la verità (innesco unico: dice «ho sentito dei passi e ho mentito per coprire chi li faceva» e ricorda la luce sotto la porta; non fa il nome) |
| Noe | la storia e Kalea | di dover scegliere | Kalea mi chiede di non pubblicare |
| Kapono | contare qualcosa | che Noe scopra che sono un ricattatore | Noe mi dice di aver visto il biglietto |
| Auntie Lei | che la terra resti in famiglia | che il mio silenzio sul testamento sia costato la vita a Keoki | Lani mi promette di non firmare |

**3a. Lani, Nalu, Ike** (`Character_1`, `Character_2`, `Character_3`: `_scheda_personaggio.md`, `_missione.md`, `_invito.md`).
- Nalu non è più adottato: «cresciuto in casa Kealoha» in `Character_1` (due righe: «fratello adottivo») e in `Character_2` (invito, ruolo, tre righe di scheda, riga 50).
- Nalu: i 4.000 dollari presi dalla cassa sono finiti a Ike; se Lani insiste sulle parole delle 22:05 (colloquio con Keoki sulla cassa), aggiunge «gli ho detto che me ne vado». Non lascia mai il bancone.
- Lani: invito a fare il brindisi al minuto 40 «quando senti il momento giusto».
- Le due metà: Lani ha il «me ne vado» di Nalu; Ike sa dove sono finiti i 4.000.

**3b. Akoni, Pua, Auntie Lei** (`Character_4`, `_5`, `_10`).
- Fondi: Akoni teme di essere messo da parte da Las Vegas; Pua è senza una lira dopo il divorzio e la commissione è la sua pensione; Auntie Lei ha taciuto mesi sul testamento.
- Pua e Akoni sono fratelli (nessuna modifica di parentela): l'anticipo è un tradimento verso il fratello; Ike sa che non è la prima volta.
- Auntie Lei: metà del sospetto su Maleko («Keoki mi parlò del mio amico che chiede troppo»). Lani ha l'altra metà (tre settimane prima Maleko è venuto a chiedere dell'ufficio di Keoki, lei gli aveva promesso la sede senza sapere che fosse della polizia).
- Akoni: il prezzo dell'alibi (la telefonata a Las Vegas, affare morto).

**3c. Maleko, Kalea, Noe, Kapono** (`Character_6`, `_7`, `_8`, `_9`).
- Maleko: punto di rottura; due battute pronte su fatti veri («Ho sentito Akoni alle 22:40: "Il voto è già comprato"»; il debito di Pua e la sua commissione da 260.000 dollari). Il nastro è a doppio taglio: se il tavolo chiede di ascoltarlo, Maleko deve rifiutare (la missione lo vieta) e il rifiuto è già sospetto. Maleko e Noe: nessuna scena in più.
- Kalea: innesco unico (vedi tabella), non pronuncia mai il nome del fratello.
- Noe: il prezzo dell'alibi (camera con le immagini private); la camera si mostra o si passa all'ultima chiamata.
- Kapono: fondo (Keoki lo ha tirato fuori dalla miseria dopo l'incidente da surfista; il ricatto è la sua vendetta su un mondo in cui non conta); biglietto di ricatto che chiede «e lascia stare Noe»; prezzo dell'alibi (gli scatoloni di Habana).
- `indizi/indizio_11.md`: il biglietto di Kapono contiene «20.000 dollari, e lascia stare Noe». Se Kapono lo consegna a Kalea, la seconda copia resta nella sua giacca come indizio (regola già presente nelle mini-trame).

**3d. Inviti e README** (`personaggi/Character_1…10_invito.md`, `README.md`): durata 2 h 30; adottivo tolto; una riga nell'invito per chi dovesse segnalare allergie (nessuna restrizione al momento).

**Controllo di ciascuna sotto-sessione:** lo script chiude OK; nessuna «Cedo se…» contraddice un alibi o la catena di prove (rilettura incrociata); la prima mossa entro 10 minuti c'è e coincide con quella decisa:
Lani chiede a Nalu delle 22:05; Nalu dice a Ike «Non dire niente di noi»; Ike porta la scatola ad Auntie Lei in pegno; Akoni cerca Kalea («l'accordo regge»); Pua da Auntie Lei («mi serve il tuo sì»); Maleko da Kalea («non parlare col tenente senza di me»); Kalea cerca Kapono; Noe da Akoni, per la parola «Kahuna»; Kapono da Kalea col biglietto; Auntie Lei chiede un dollaro a Ike.

### Passo 4. Stampa dell'ondata 1
- Aggiungere a `pdf.json` eventuali file nuovi; ricostruire i due PDF (gioco completo, racconto non cambia) con la skill ui-ux-pro-max; controllare le pagine delle schede (le tre righe in più non devono spezzare la scheda).
- Aggiornare `gioco/criticita_aperte.md` con una sezione «Revisione del 15 ottobre: applicata».
- Aggiornare la memoria del progetto.

**Fine ondata 1:** la serata è giocabile a 2 h 30 senza cena. Si può giocare.

## Ondata 2: cena, scene, racconto (facoltativa)

### Passo 5. La cena
**File nuovi:** una scheda di cucina per il direttore (`gioco/cena.md`) e cinque carte piatto (`oggetti/` o `indizi/`, a scelta, senza numero di indizio). **File toccati:** `gioco/guida_direttore.md`, `personaggi/Character_9_scheda_personaggio.md` (invito a portare i vassoi), le cinque schede interessate.

- **Carte piatto** (ognuna dà una riga di ricordo e una persona a cui portare il piatto): Lani, maiale kalua, la ricetta di Keoki, lo porta ad Auntie Lei; Auntie Lei, haupia, la ricetta di Malia, lo porta a Lani; Kapono, poke pescato da lui, lo porta a Noe; Nalu, il drink della casa (ghiaccio e limoni), lo porta a Ike; Noe, il piatto di Keoki vuoto con un lei di **plumeria bianca** (il viola è del petalo di Kalea, indizio 04), lo posa sul bancone in silenzio.
- **Menù da supermercato**, tutto pronto prima: spalla di maiale in forno basso 6–8 ore con paprika affumicata, sfilacciata, in panini al latte piccoli già farciti (il giorno prima); poke di salmone da sushi in tazzine, in frigo fino al minuto 38–40 (se non c'è salmone da sushi, tonno in scatola con soia, sesamo, cipolla, avocado); lomi-lomi di salmone affumicato, pomodoro e cipolla rossa (la mattina); musubi di riso con prosciutto cotto scottato e nori (tre ore prima, nella pellicola); insalata di maccheroni (il giorno prima); haupia di latte di cocco e amido di mais, a quadrotti (il giorno prima); ananas fresca a spicchi; piña colada analcolica in brocche. Spesa stimata 60–75 €, non verificata sui prezzi.
- **Servizio:** Kapono porta i vassoi dal frigo al minuto 40 (invito sulla sua scheda); il direttore non si alza dal tavolo del tenente.
- **Il filo narrativo:** il buffet è l'addio che Keoki aveva preparato per la sua ultima serata; il tenente lo lascia mangiare perché nessuno esce comunque.

**Controllo:** le scene di Lani e Auntie Lei restano due scene distinte (brindisi e metà sul sospetto su Maleko); nessun oggetto di gioco ha bisogno di scambi durante i minuti 40–55.

### Passo 6. Le sei carte scena
**File nuovi:** sei carte con la sola frase d'apertura (il resto lo giocano i giocatori). Il ticket relazioni dà quattro coppie con scena (la quinta, Maleko-Noe, resta senza scena per scelta); a queste si aggiungono Kalea-Noe e Maleko-Kalea nel séparé.
1. Kalea e Kapono: il ricatto personale («e lascia stare Noe»). Apertura di Kapono: «Il prezzo è cambiato.»
2. Kalea e Noe: la verità a metà (l'innesco di Kalea). Apertura di Noe: «Guardami e dimmelo.»
3. Pua e Akoni (fratelli): la ricevuta dell'anticipo. Apertura di Pua: «Devo farti firmare una cosa.»
4. Lani, Nalu, Ike: i 4.000 dollari e il «me ne vado».
5. Lani e Auntie Lei: le due metà su Maleko.
6. Maleko e Kalea nel séparé: «Non parlare col tenente senza di me.»

Le frasi esatte vanno scritte con l'humanizer.

### Passo 7. Racconto e stampa finale
- `racconto-keoki.md`: una riga sull'addio che Keoki aveva preparato (il buffet); controllare che il racconto non contenga «adottivo» né nulla che contraddica Pua sorella.
- Aggiungere `gioco/cena.md` e le carte a `pdf.json`; ricostruire entrambi i PDF; controllo visivo.

## Controlli finali (dopo ogni ondata)

1. `verifica_caso.py`: «Killer unico con tutte le prove: Maleko. OK» con le ablazioni nuove.
2. `grep` di coerenza: `adottiv`, `ex moglie`, `2 ore e 20`, `2:20`, `2 h 20` non devono comparire nei file di gioco (tranne `scheletro/`).
3. Rilettura incrociata di ogni «Cedo se…» contro la catena di prove e gli alibi, Kalea e Maleko per primi.
4. Prima mossa entro 10 minuti presente su tutte le schede.
5. Tutti i testi nuovi per i giocatori passati dall'humanizer; tutte le pagine nuove dall'impaginazione ui-ux-pro-max.
6. PDF ricostruiti e aperti a occhio.

## Lista di collaudo per la serata vera

Otto cose che il direttore osserva e riporta dopo, per decidere se ritarare:
1. Dopo la campanella al minuto 55, gli indizi chiusi escono o restano in tasca?
2. I 10 minuti di discussione bastano, o servono 15?
3. I neofiti trovano la prima mossa entro 10 minuti?
4. Il séparé è usato? Genera sospetto o è ignorato?
5. Il brindisi di Lani arriva e che effetto ha sul tavolo?
6. Il buffet interrompe o alimenta le conversazioni?
7. Kalea fa la rivelazione intorno al minuto 45? Chi la innesca?
8. Quante accuse su Maleko, e il bonus tavolo scatta?

## Fuori da questo piano

Cambiare colpevole, cronologia o catena di prove; aggiungere personaggi; toccare i progetti `murder-generator` e `mystery-agents`; il collaudo con un gruppo vero e la ritaratura della difficoltà (la stima 90/100 resta di progetto).
