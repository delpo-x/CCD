---
id: "01"
title: "Diagnosi editoriale del caso attuale"
labels: [wayfinder:research]
status: closed
assignee: claude
blocked_by: []
---

## Question

Qual è lo stato del giallo «Last Call al Kapu Lounge» dopo le correzioni del 14 ottobre? Per ciascuna voce del brief (tensione, ritmo, colpi di scena, depistaggi, indizi, coerenza logica, originalità, finale) quali sono i punti di forza, le debolezze e le opportunità, distinguendo i problemi oggettivi dalle preferenze stilistiche? Sola lettura dei file di `games/hawaii-2004/`, nessuna modifica.

## Resolution

Il caso regge sul piano logico e cede su quello emotivo. Il rompicapo è solido: colpevole unico, catena di prove ricostruibile, mondo chiuso. Il peso che il brief dà ai legami (40) è coperto solo a metà: i segreti sono scritti bene, ma quasi tutti restano chiusi nella scheda del proprietario.

**[O]** = problema oggettivo, **[S]** = preferenza stilistica.

### Tensione
- **Forza.** L'ultima chiamata delle 23:15 dà alla serata un punto in cui tutto si ferma, e ha una causa nel mondo di gioco.
- **Debolezza [O].** La tensione sta nel passato. Il delitto è già avvenuto quando il gioco comincia: dopo c'è un'indagine, non una minaccia. Nessuno ha qualcosa da perdere *durante* la serata, salvo la reputazione.
- **Opportunità.** Dare a ogni giocatore una scadenza personale dentro la serata, qualcosa che si chiude se non agisce, invece del solo segreto da difendere.

### Ritmo
- **Forza.** La forma è chiara: intervista, gioco libero, accuse, rivelazione. I rapporti a richiesta motivata evitano che il caso si risolva da sé.
- **Debolezza [O].** Il direttore resta il collo di bottiglia (ricerche, rapporti, convocazioni, d6). Ora che non innesca scene, il carico non cala: cala solo la sua iniziativa. Servono scene che i giocatori accendono da soli.
- **Debolezza [O].** 60 risposte d'intervista in 25 minuti sono molte per un neofita. Ogni scheda ha bisogno di una prima mossa chiara nei primi 10 minuti.
- **Opportunità.** Tre colpi fissi (intervista, 23:15, accuse) e, in mezzo, scene tra giocatori che non passano dal direttore.

### Colpi di scena
- **Forza.** Kalea sembra colpevole e non lo è; l'assassino è un collega del tenente. Il ribaltamento a due livelli funziona.
- **Debolezza [O].** I colpi di scena sono quasi tutti *informativi* (un oggetto che si apre, un'ora che non torna). Pochi cambiano il rapporto tra due persone. Le «svolte» delle missioni sono in genere una riga da leggere ad alta voce.
- **Opportunità.** Almeno due svolte che mettano in crisi un legame (due che si credevano alleati e non lo sono), non solo un fatto nuovo.

### Depistaggi
- **Forza.** L'esca Kalea è il pezzo migliore: corrotta, mente, ha l'appuntamento delle 23:10, il petalo, la mezza pagina. Tutto la inchioda a qualcosa di vero che non è l'omicidio.
- **Debolezza [O].** Gli altri sono scagionati da dati oggettivi (palco, cannoni, conducente, tabulato, foto, voce) e la matrice dà a ciascuno una lettura innocente. Un giocatore attento li elimina presto e restano due nomi, Kalea e Maleko.
- **Debolezza [O].** I segreti di Ike (contrabbando) e Kapono (ricatto) non toccano il delitto: sono colore, non pista.
- **Opportunità.** Tenere vivi più a lungo due o tre sospetti *emotivamente* credibili: chi ha un movente che si capisce, non solo un alibi che si smonta.

### Indizi
- **Forza.** Catena in sette passi, nessun indizio basta da solo, ogni oggetto ha un proprietario, cinque prove citabili e numerate nell'accusa.
- **Debolezza [O].** Gli oggetti stanno in mano a chi ha il segreto: se non vuole mostrarli, non escono. Il gioco dipende dalla buona volontà di rivelare, fragile con i neofiti.
- **Debolezza [O].** Il caso si dimostra a freddo, ma nessuna prova costringe a scegliere tra due persone.
- **Opportunità.** Almeno un indizio che costi qualcosa a chi lo mostra.

### Coerenza logica
- **Forza.** `verifica_caso.py` conferma il colpevole unico. Orari, orologio avanti di un minuto, foto 0412/0413/0414, porta chiusa, conta dei presenti sono fissati.
- **Debolezza [S].** La coerenza vive di molta documentazione incrociata: ogni ritocco ai legami rischia di spostare un orario. Va ricontrollata a ogni passo, ed è il motivo del ticket di verifica.
- **Nota.** Il «90/100» resta una stima di progetto, mai provata con giocatori veri.

### Originalità
- **Forza.** Honolulu 2004, il locale con un rito dal 1971 e il colpevole poliziotto sotto copertura sono freschi per il genere.
- **Debolezza [S].** Il testimone tormentato che guida il tenente è un trope noto (già attenuato); il registro contabile come MacGuffin è classico.
- **Opportunità.** Il rito delle 23:15 è l'idea più originale: usarlo come cuore emotivo, non solo come orario.

### Finale
- **Forza.** Epiloghi personali brevi e secchi, in gran parte riusciti (Lani, Akoni, Noe, Kapono).
- **Debolezza [O].** Gli epiloghi sono quasi tutti indipendenti: ognuno chiude la propria storia, nessuno risponde a quello di un altro. Solo Kapono e Noe si parlano.
- **Debolezza [S].** La rivelazione ha la forma del verdetto, non della resa dei conti.
- **Opportunità.** Un finale in cui accusare ha un costo per chi accusa.

### Priorità per i ticket successivi
1. Legami: da «segreto accanto a segreto» a «segreto che dipende da un altro».
2. Scadenze personali durante la serata.
3. Sospetti emotivamente credibili oltre Kalea.
4. Un costo per chi mostra un indizio o accusa.
