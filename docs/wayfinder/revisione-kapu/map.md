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
