---
id: "01"
title: "Struttura dell'esportazione JSON di murder-generator"
labels: [wayfinder:research]
status: closed
assignee: claude-research
blocked_by: []
---

## Question

Qual è la struttura esatta del JSON prodotto da `murder-generator` (`Export.to_json`)? Quali informazioni contiene su personaggi, relazioni, segreti, obiettivi ed elementi, in quali lingue sono i testi, e come si ottiene da riga di comando (build nativa o JS) senza passare dal browser? Serve un esempio reale generato per 6 giocatori.

## Resolution

L'esportazione JSON di `murder-generator` (`Export.to_json`, `src/export.ml:686-740`) ha la forma `{version, characters[], events[]}`. Non contiene prosa, segreti o obiettivi come testo: solo identificatori inglesi (attributi, contatti con scopo `Protect`/`Harm`/`Help`, relazioni, id degli eventi), e non dipende dalla lingua. Il testo vero sta nei file `data/elements/*.murder` (fr, en, eo) e esce solo dall'esportazione org-mode o HTML. Il bersaglio di ogni contatto non è scritto: si deduce dall'ordine degli id, cosa che l'agente ha ricavato dal codice e controllato su un solo caso.

Da riga di comando la build nativa si pilota via stdin, ma serve una sequenza con pause (circa 40 s per la generazione) e va lanciata dalla radice del sorgente. L'esportazione HTML attiva ha prodotto un `Assert_failure` (`src/export.ml:536`) in una prova su due. Non c'è un seed, quindi ogni run è diverso. La build JS gira solo nel browser e non è stata esplorata.

Conseguenza per la mappa: il convertitore dovrà ricostruire il testo dagli identificatori usando i file `.murder`, oppure usare l'LLM per scrivere segreti e obiettivi a partire da quegli identificatori.

Dettagli: ramo locale `research/01-esportazione-json`, `docs/wayfinder/integrazione/research/01-esportazione-json.md` e `esempio-6-giocatori.json` (commit 5daa1f9).
