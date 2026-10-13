---
id: "02"
title: "Cosa richiede lo Stato di partita e come saltare gli agenti LLM"
labels: [wayfinder:research]
status: closed
assignee: claude-research
blocked_by: []
---

## Question

Quali campi dello Stato di partita di `mystery-agents` (`models/state.py`) servono davvero agli agenti di contenuto e di impaginazione (`a8`, `a9`)? Esiste o si può aggiungere una modalità che carica uno stato già scritto e salta gli agenti LLM? Quali agenti sono LLM e quali deterministici? Verificare se il formato salvabile su disco è già disponibile.

## Resolution

Lo Stato di partita è già serializzabile (modelli pydantic puri, round-trip JSON verificato) ma non esiste una modalità "carica stato e salta gli LLM": la CLI parte sempre da uno stato vuoto. Dei 14 nodi, 10 usano un LLM di chat, 2 l'API immagini (opzionali) e 2 sono deterministici (`a1` e `a9`). Per l'impaginazione bastano `a8_5` e `a9` con un sottoinsieme di campi (personaggi, relazioni, indizi, guida ospite, vittima, colpevole, cronologia, mondo, meta e config). Un grafo ridotto `a8_5 → a9` ha prodotto 18 PDF su 19 e lo ZIP da uno stato JSON, senza LLM. Il PDF mancante è andato in timeout con 12 processi paralleli e sembra un problema di carico, non di dati.

Dettagli: ramo locale `research/02-stato-di-partita`, file `docs/wayfinder/integrazione/research/02-stato-di-partita.md` (commit 2abc3c4), con prova di fattibilità in `poc/` e uno stato di esempio da `--dry-run`.
