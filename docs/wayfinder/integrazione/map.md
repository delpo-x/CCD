---
label: wayfinder:map
title: Integrazione murder-generator + mystery-agents
---

# Integrazione murder-generator + mystery-agents

Tracker: Markdown locale. Ogni ticket è un file in `tickets/`; il front matter dice tipo, stato, bloccanti e chi lo ha preso in carico. La frontiera sono i ticket aperti, non bloccati e senza assegnatario.

## Destination

Una specifica approvata, abbastanza precisa da affidare l'implementazione, di una pipeline che parte da uno **Scenario** di `murder-generator` e arriva a un **Pacchetto** stampabile in italiano; prima come comando unico, poi come pagina web di modifica sopra la stessa pipeline.

## Notes

- Italiano obbligatorio nell'output; i file di dati di `murder-generator` non si modificano.
- **Stato di partita** di `mystery-agents` è il formato comune.
- **Provider LLM** intercambiabile: oggi Claude in chat, Gemini solo se si attiva la fatturazione.
- I due progetti restano separati, collegati solo via JSON ([ADR 0001](../../adr/0001-progetti-separati-collegati-via-json.md)).
- Vocabolario: vedi `CONTEXT.md`.
- Ogni testo destinato ai giocatori (schede, inviti, indizi, guida, soluzione) passa da un controllo con la skill humanizer prima della consegna; la pipeline deve prevedere questo passaggio.
- Questa mappa è di pianificazione: ogni ticket produce una decisione, non codice.

## Decisions so far

- Il risultato finale è un comando unico, poi una pagina web sopra di esso.
- `murder-generator` fornisce lo scheletro relazionale; `mystery-agents` aggiunge delitto, indizi e cronologia.
- Il formato comune è lo Stato di partita JSON di `mystery-agents`, con un convertitore dall'esportazione di `murder-generator`.
- Output in italiano; la traduzione la fa il Provider LLM durante la conversione.
- Progetti separati, collegati solo via file JSON.
- [Struttura dell'esportazione JSON di murder-generator](tickets/01-struttura-esportazione-json.md): il JSON contiene solo identificatori (attributi, contatti, relazioni, eventi), non testi; il testo sta nei file `.murder`.
- [Cosa richiede lo Stato di partita e come saltare gli agenti LLM](tickets/02-requisiti-stato-di-partita.md): lo stato è già serializzabile e basta un grafo ridotto `a8_5 → a9` per produrre i PDF senza LLM (provato: 18/19 PDF).

## Not yet specified

- Impaginazione e modelli di PDF per partite scritte a mano o convertite.
- Altre lingue oltre all'italiano.
- Libreria di più partite e loro catalogo.
- Verifica automatica in CI.

## Out of scope

- Modificare il codice interno OCaml di `murder-generator`.
- Fondere i due codebase.
- Pubblicare un servizio ospitato per terzi.

## Tickets

| Ticket | Tipo | Bloccato da |
|--------|------|-------------|
| Struttura dell'esportazione JSON di murder-generator | research | – |
| Cosa richiede lo Stato di partita e come saltare gli agenti LLM | research | – |
| Come eseguire murder-generator da Windows | grilling | Struttura dell'esportazione JSON di murder-generator |
| Mappa dai concetti di murder-generator ai campi di Stato di partita | grilling | Struttura dell'esportazione JSON di murder-generator; Cosa richiede lo Stato di partita e come saltare gli agenti LLM |
| Provider LLM intercambiabile e modalità Claude in chat | grilling | Cosa richiede lo Stato di partita e come saltare gli agenti LLM |
| Flusso delle immagini | grilling | Cosa richiede lo Stato di partita e come saltare gli agenti LLM |
| Scelta del colpevole e costruzione dell'intreccio | grilling | Mappa dai concetti di murder-generator ai campi di Stato di partita |
| Controllo di risolvibilità e coerenza | grilling | Scelta del colpevole e costruzione dell'intreccio |
| Revisione umana e ciclo di modifica | grilling | Mappa dai concetti di murder-generator ai campi di Stato di partita; Scelta del colpevole e costruzione dell'intreccio |
| Pagina web di modifica | grilling | Revisione umana e ciclo di modifica |
