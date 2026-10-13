# I due progetti restano separati e comunicano solo via file JSON

`murder-generator` è AGPL-3.0, `mystery-agents` è MIT. Per non estendere l'obbligo AGPL a `mystery-agents`, i due non condividono codice né librerie: si scambiano solo file JSON (l'esportazione di `murder-generator` e lo **Stato di partita**), e un convertitore sta fuori da entrambi. Abbiamo scartato la fusione in un unico progetto, che sarebbe più comoda ma legherebbe tutto alla licenza AGPL. Non è una consulenza legale: da verificare prima di una pubblicazione.
