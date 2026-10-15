---
label: wayfinder:map
title: Revisione editoriale di Last Call al Kapu Lounge
---

# Revisione editoriale di Last Call al Kapu Lounge

Tracker: Markdown locale. Ogni ticket è un file in `tickets/`; il front matter dice tipo, stato, bloccanti e chi lo ha preso in carico. La frontiera sono i ticket aperti, non bloccati e senza assegnatario.

## Destination

Un piano di revisione editoriale approvato, abbastanza preciso da affidare l'implementazione a una sessione successiva: quali relazioni, segreti, scene, depistaggi e momenti di gioco migliorano il caso senza toccare colpevole, cronologia e catena di prove. Le modifiche ai file non fanno parte di questa mappa.

## Notes

- Gioco: `games/hawaii-2004/`. 10 giocatori più il direttore (tenente Alapai). Nessun personaggio nuovo.
- Italiano; ogni testo destinato ai giocatori passa dalla skill humanizer, e ogni impaginazione dalla skill ui-ux-pro-max.
- Il brief editoriale (ruolo di autore e editor, analisi di trama, personaggi, relazioni, dialoghi, cena con delitto, fasi A–F) è il criterio di lavoro. Principi: non approvare le idee dell'utente senza metterle alla prova, niente complessità fine a sé stessa, pochi segreti ben intrecciati, distinguere problemi oggettivi da preferenze stilistiche, dare un esempio concreto per ogni proposta.
- Il «12 partecipanti» del brief vale 10+1: deciso il 15 ottobre 2026.
- Vocabolario: vedi `CONTEXT.md`. Stato attuale del caso: `games/hawaii-2004/gioco/criticita_aperte.md`.
- Questa mappa è di pianificazione: ogni ticket produce una decisione, non modifiche ai file di gioco.

## Decisions so far

- Colpevole (Maleko), cronologia e catena di prove restano fissi; si rivedono relazioni, segreti, scene e depistaggi.
- Nessun personaggio nuovo: 10+1.
- Mappa e ticket come file markdown in `docs/wayfinder/` (il repo è pubblico e contiene spoiler).
- La destinazione è il piano, non le modifiche applicate.
- La cena a tema entra come ticket successivo (08).
- [Che cosa significa «livello superiore» per questa serata](tickets/03-criteri-livello-superiore.md): pesi legami/emozione 40, rompicapo 40, tensione 20, risate 0; noir serio e cupo; il direttore non innesca scene; almeno due neofiti, quindi ogni scheda ha una prima mossa; punti e missioni restano ma l'obiettivo principale è cooperativo.
- [Diagnosi editoriale del caso attuale](tickets/01-diagnosi-editoriale.md): il rompicapo regge, i legami sono coperti a metà; priorità: legami che dipendono l'uno dall'altro, scadenze personali, sospetti credibili oltre Kalea, un costo per chi accusa o mostra un indizio.
- [Mappa delle relazioni esistenti](tickets/02-mappa-relazioni.md): solo tre legami reggono il caso (Maleko-Kalea, Kalea-Kapono, Kalea-Noe) e passano tutti per Kalea; il resto è a raggiera da Keoki o decoro.
- [Quali relazioni potenziare e con quali segreti](tickets/04-relazioni-da-potenziare.md): cinque legami a due metà, ciascuna in mano a un giocatore: Kalea-Kapono-Noe (ricatto personale), Pua ex moglie di Akoni, triangolo Lani-Nalu-Ike, Lani e Auntie Lei su Maleko; Maleko-Noe invariato.
- [Profondità psicologica dei personaggi](tickets/05-profondita-personaggi.md): quattro correzioni di fondo (Akoni, Pua, Kapono, Auntie Lei), tre righe «Voglio / Temo / Cedo se» su ogni scheda, Maleko cede se Kalea è accusata da due persone, Nalu non è più adottato, difficoltà dei ruoli solo nella guida.
- [Scene e interazioni da giocare nella serata](tickets/06-scene-e-interazioni.md): cinque tempi nei 75 minuti, campanella dell'ultima chiamata al minuto 55 (busta chiusa = punto perso), séparé a due con clessidra, sei carte scena, prime mosse dalle missioni, bonus tavolo +5 con almeno sette accuse corrette su Maleko, brindisi di Lani come invito.
- [Depistaggi e colpi di scena senza toccare la catena di prove](tickets/07-depistaggi-e-colpi-di-scena.md): nessuna pista nuova; gli alibi di Akoni, Ike, Kapono e Noe costano un'ammissione; Kalea dice una verità a metà verso il minuto 45 senza fare il nome; Maleko ha due battute pronte (la frase di Akoni sul nastro, il debito di Pua) e il nastro è a doppio taglio; scartati complici e false confessioni.
- [La cena a tema come intermezzo](tickets/08-cena-a-tema.md): buffet di pupu dai minuti 40 al 55, dentro il respiro tra il brindisi di Lani e la campanella; si resta in ruolo, carte e oggetti in tasca mentre si mangia; cinque carte piatto (Lani, Auntie Lei, Kapono, Nalu, Noe); menù da supermercato preparato in anticipo dal direttore, vassoi portati da Kapono.
- [Verifica di coerenza delle modifiche](tickets/09-verifica-coerenza.md): tutto regge; cinque correzioni (Pua è sorella, il 22:05 è Nalu-Keoki e i 4.000 dollari finiscono a Ike, la macchina fotografica non si può tenere, serata di 2 h 30, piccole correzioni su Kalea, Maleko, lei bianco e adottivo); elenco dei file da toccare e dei controlli da rifare.
- [Piano d'azione ordinato](tickets/10-piano-d-azione.md): consegnato come [piano-d-azione.md](piano-d-azione.md), due ondate (la prima rende la serata giocabile a 2 h 30, la seconda aggiunge cena, carte scena e racconto), un passo per sessione, tag di ritorno, lista di collaudo di otto osservazioni.

## Not yet specified

- Collaudo dal vivo con un gruppo vero e ritaratura della difficoltà (la stima 90/100 è di progetto).
- Impatto sull'impaginazione dei PDF e sul materiale stampabile dopo le modifiche.
- Eventuali materiali di scena (musica, costumi, menù stampato).

## Out of scope

- Cambiare colpevole, cronologia o catena di prove.
- Aggiungere personaggi.
- Applicare le modifiche ai file di gioco (sessione di implementazione a parte).
- Modificare i progetti `murder-generator` e `mystery-agents`.

## Tickets

| Ticket | Tipo | Bloccato da |
|--------|------|-------------|
| Diagnosi editoriale del caso attuale | research | – |
| Mappa delle relazioni esistenti | research | – |
| Che cosa significa «livello superiore» per questa serata | grilling | – |
| Quali relazioni potenziare e con quali segreti | grilling | Diagnosi editoriale del caso attuale; Mappa delle relazioni esistenti; Che cosa significa «livello superiore» per questa serata |
| Profondità psicologica dei personaggi | grilling | Diagnosi editoriale del caso attuale; Che cosa significa «livello superiore» per questa serata |
| Scene e interazioni da giocare nella serata | grilling | Quali relazioni potenziare e con quali segreti; Profondità psicologica dei personaggi |
| Depistaggi e colpi di scena senza toccare la catena di prove | grilling | Diagnosi editoriale del caso attuale |
| La cena a tema come intermezzo | grilling | Che cosa significa «livello superiore» per questa serata; Scene e interazioni da giocare nella serata |
| Verifica di coerenza delle modifiche | grilling | Quali relazioni potenziare e con quali segreti; Profondità psicologica dei personaggi; Scene e interazioni da giocare nella serata; Depistaggi e colpi di scena senza toccare la catena di prove; La cena a tema come intermezzo |
| Piano d'azione ordinato | grilling | Verifica di coerenza delle modifiche |
