# Murder Mystery Toolkit

Un insieme di strumenti per creare murder mystery party giocabili in italiano: uno genera lo scheletro delle relazioni tra giocatori, l'altro costruisce l'intreccio giallo e il materiale stampabile.

## Language

**Scenario**:
Insieme di personaggi con relazioni, segreti e obiettivi prodotto da `murder-generator`, ancora senza delitto né indizi.
_Avoid_: Trama, scenario giallo

**Scheletro relazionale**:
La parte dello **Scenario** che descrive chi è legato a chi, con quali segreti e obiettivi. È l'ingresso della pipeline integrata.
_Avoid_: Struttura, griglia

**Partita**:
Un murder mystery completo e giocabile: ambientazione, personaggi, delitto, cronologia, indizi e soluzione.
_Avoid_: Gioco, scenario, storia

**Stato di partita**:
Il file JSON che contiene tutta una **Partita** nel formato di `mystery-agents`; è il formato comune a tutti gli strumenti.
_Avoid_: Dump, configurazione

**Pacchetto**:
Lo ZIP finale con schede, inviti, indizi, guida e soluzione pronti da stampare.
_Avoid_: Output, export

**Ospite**:
La persona che organizza la serata: interpreta prima la vittima (Atto 1) e poi il detective (Atto 2).
_Avoid_: Game master, host, narratore

**Sospetto**:
Ciascuno dei personaggi giocati dagli invitati.
_Avoid_: Giocatore (quando si parla del personaggio), PG

**Indizio**:
Oggetto o documento nascosto che incrimina o scagiona un **Sospetto**; può essere una *falsa pista*.
_Avoid_: Prova, hint

**Provider LLM**:
La sorgente dei testi generati (Gemini via API oppure Claude in chat); è intercambiabile.
_Avoid_: Modello, backend
