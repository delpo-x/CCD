# 01 - Struttura dell'esportazione JSON di murder-generator

Ticket: `tickets/01-struttura-esportazione-json.md`. Branch `research/01-esportazione-json`.
Tutti i riferimenti sono relativi a `murder-generator/`. Esempio reale (6 giocatori, build nativa WSL, commit upstream `40a0d27a...`): [`esempio-6-giocatori.json`](esempio-6-giocatori.json) (reindentato, 14 KB; l'originale e' una sola riga di 9 KB).

## Risposta in breve

1. `Export.to_json` (`src/export.ml:686-740`) produce un oggetto `{version, characters[], events[]}`. Non contiene testo narrativo: solo **identificatori interni in inglese** ("lingua generica").
2. Segreti, obiettivi e prosa **non** sono nel JSON come testo. Ci sono solo attributi (`Job`, `SecretSociety`...), contatti con `Goal`/`Know`, relazioni, e gli id degli eventi (`GodAlwaysExisted#0`). Il testo vero degli eventi sta in `data/elements/*.murder` (fr/en/eo) ed esce solo da org-mode/HTML.
3. Il JSON e' indipendente dalla lingua scelta (usa `generic`, `export.ml:689`); cambiano solo i **nomi** dei personaggi.
4. Da riga di comando: la build nativa e' un'interfaccia testuale interattiva, ma si pilota via stdin (ricetta sotto). Nessun driver necessario, anche se ne conviene uno per robustezza. La build JS (`js/`) e' solo browser.
5. Bug upstream: l'esportazione HTML puo' lanciare `Assert_failure src/export.ml:536` (visto in 1 run su 2, lingua fr) e bloccare tutto; disattivare HTML nella schermata dei formati.

## Struttura esatta

Serializzazione: `Yojson.Safe.to_string ~std:true` (`export.ml:690`), una sola riga, UTF-8. Esempio completo nel file JSON.

```jsonc
{
 "version": "40a0d27a4ca97c707402c28e87daaaa8c1b2775d\n",  // git rev-parse HEAD, con "\n" finale (FIXME upstream, src/dune:25)
 "characters": [ {                // un elemento per giocatore; l'indice (0..n-1) e' l'id usato altrove
   "name": "Tharria",
   "attributes": {                // mappa attributo -> valore (stringhe)
     "Famousness": "Famous", "Specy": "God", "Gender": "Female", "Age": "Young",
     "Born": "True", "Job": "Journalist", "SecretSociety": "?Triumvirate",
     "GrammarEO": "Normal", "GrammarEN": "Normal", "GrammarFR": "Normal", "Richness": "Neutral" },
   "contacts": [                  // uno per ogni ALTRO giocatore (n-1), SENZA indicare il bersaglio
     { "FamilyRelation": "None", "Goal": "Protect", "Know": "True" },
     { "FamilyRelation": "?GrandParent", "Goal": "Help", "Know": "True" } ],
   "relations": [ "neutral", "strong trust", "asymmetrical hate neutral" ],  // vedi sotto
   "complexity": 17, "difficulty": 10    // interi (State.character_complexity_final / _difficulty_final)
 } ],
 "events": [ {
   "begin": "20040101T190100", "end": "20040101T190100",   // RFC 2445 (Date.rfc2445), senza fuso
   "event": "GodAlwaysExisted#0",        // Events.print_event: id elemento + '#' + indice frase
   "attendees": [2],                     // indici in characters[]
   "all": [2]                            // all_attendees
 } ]
}
```

Codice: personaggi `export.ml:691-720`, eventi `721-737`.

Regole di lettura (verificate su esempio e sorgente):

- **Prefisso `?`** davanti a un valore (`"?Triumvirate"`, `"Know":"?True"`): valore **non fisso** (`fixed=false`), cioe' non vincolante/dedotto; senza `?` e' fisso (`export.ml:696,703`). `from_json` (`export.ml:742+`) lo rilegge allo stesso modo: il JSON e' re-importabile nel generatore.
- **Attributi**: presenti solo quelli assegnati al personaggio. Nei 12 personaggi osservati: `Age, Born, Curse, Disability, Famousness, Gender, GrammarEN/EO/FR, Job, Richness, SecretSociety, Specy, RoleInSecretSociety`. A differenza di org-mode, il JSON **non filtra** gli attributi interni (`is_internal_attribute`, `export.ml:35`, usato solo da org/HTML): `Grammar*` compaiono.
- **Contacts**: chiavi osservate `FamilyRelation, Goal (Protect|Harm|Help), Know, Relation (Conflicted...), FinancialDebt`. **Il bersaglio non e' scritto.** L'ordine e' quello di `PMap.foldi` con prepend, quindi per id del bersaglio **decrescente**, escluso se stessi (verificato su Arind/id 0: org-mode elenca Arannie(5), Éle(4), Tusselle(3)... nello stesso ordine). Per ricostruire il bersaglio: scorrere gli id n-1..0 saltando `c`. Inferenza dal codice + un controllo, non documentata.
- **Relations**: solo per `c' < c` (`if c <= c' then l`, `export.ml:710`): il personaggio 0 ha lista vuota, il 5 ne ha 5; ordine per `c'` decrescente. Valori da `Relation.to_string` (`src/relation.ml:40`): `[strong ]` + `neutral|hate|trust|chaotic|undetermined|avoidance`, oppure `asymmetrical A B`, `explosive X Y`. Una relazione per coppia.
- **Events**: in ordine cronologico (`State.get_history_final`). Un evento condiviso compare una volta per ogni gruppo di partecipanti (es. `WarBetweenGod#0` con `[2,3]` e `[4,0]`). 48 eventi, 22 id distinti nell'esempio. `Nome#k` indica la k-esima frase dell'elemento `Nome` in `data/elements/*.murder` (es. `element GodAlwaysExisted`, `religion.murder:59`); il JSON non porta ne' testo ne' placeholder dei nomi.

## Lingue

- `to_json` usa `generic s.given` (`export.ml:689`) e `Translation.generic = "<generic>"` (`src/translation.ml:10`): attributi/valori sono gli identificatori inglesi dei `.murder`. Cambiare `lang=` **non** cambia il JSON (confermato: run `lang=fr` produce `"Specy":"Dwarf"`, `"Job":"Priest"`).
- Con la lingua cambiano i **nomi propri** e, per org-mode/HTML, tutto il testo.
- `translations.json` (interfaccia): `eo`, `fr`, `en`, `es`. Testi degli elementi nei `.murder`: `translation fr|en|eo` (`religion.murder:70-72`); copertura di `es` nei contenuti non verificata.
- Un testo italiano non esiste: va prodotto a valle (LLM) da id e attributi, o partendo dalle frasi en/fr di org-mode.

## Come ottenerlo da riga di comando

Binario: `/root/murder-generator/_build/install/default/bin/murder_generator` (esy, `native/dune`). **Va lanciato con cwd = radice del sorgente** (legge `translations.json` e `data/` con percorsi relativi, altrimenti `Sys_error "translations.json: No such file"`).

Parametri in stile URL come argomenti `chiave=valore` (`native/inOut_native.ml:40-52`, tag in `src/main.ml:134-140`): `lang=en num=6 level=0.5 comp=0.5 date=2024-01-01 power=0.5 cats=all`. Con tutti presenti si salta alla schermata "player constraints" (`main.ml:1196+`); `cats` = `all`, vuoto o lista separata da virgole.

Il resto e' un menu numerato letto da stdin (`inOut_native.ml:511`; link `[n]` rinumerati a ogni schermata):

| passo | stdin | effetto |
|---|---|---|
| 1 | `7` | "Generate a scenario" |
| 2 | (dopo ~40 s) `1` | toglie HTML dai formati (JSON gia' attivo di default, `main.ml:1181`) |
| 3 | `9` | "Next step" -> esporta |
| 4 | `1` | link "Download as JSON" -> chiede nome file |
| 5 | percorso | scrive il file (`inOut_native.ml:434-445`; riga vuota = `murder.json` in cwd) |

**L'input va dato con ritardi** (generazione asincrona Lwt): inviando tutto insieme i numeri sono letti prima che i link esistano e si ottiene `Invalid number`. Script verificato (WSL, ~1 minuto):

```bash
cd /root/murder-generator
( sleep 2; echo 7; sleep 40; echo 1; sleep 1; echo 9; sleep 15; echo 1; sleep 1; echo /root/out.json; sleep 2 ) \
 | ./_build/install/default/bin/murder_generator lang=en num=6 level=0.5 comp=0.5 date=2024-01-01 power=0.5 cats=all
```

Da PowerShell: `wsl -d Ubuntu -u root -e bash -lc '...'`; da Git Bash impostare `MSYS_NO_PATHCONV=1`. Inserendo `echo 3` prima di `9` si attiva anche org-mode (link `[2]` nella schermata finale): testi leggibili nella lingua scelta. Verificato con `lang=fr` (`fr.json` 12 KB, `fr.org` 52 KB).

Limiti:
- Nessun seed: ogni run differisce (l'esempio non e' riproducibile). ~30-40 s per 6 giocatori.
- Le attese sono euristiche. Per robustezza: `pexpect` che aspetta "Download as JSON" prima di inviare `1`, oppure un driver OCaml che chiami `Export.process` + `Export.to_json` (`src/export.mli:33`, stato costruito in `main.ml:1102-1110`).
- Con HTML attivo, `Assert_failure src/export.ml:536:29` interrompe il programma dopo aver stampato i link ma prima che siano utilizzabili: spegnere sempre HTML.
- Build JS (`js/main_js.ml`, js_of_ocaml): solo browser; non esplorata.
- `/root/murder-generator` non e' stato modificato; file di prova in `/root/mg-exp`, script in `/root/run*.sh`.

## Estratto org-mode (fr) per confronto

Run `lang=fr` (scenario diverso da quello dell'esempio JSON). Il testo traducibile sta qui, non nel JSON:

```
*** Éle et Amantre ont toujours été en guerre.
    Cela fait maintenant partie de leurs identités.
    [1898-01-01 _ 21:40]
    - [X] Éle
    - [X] Amantre
```

nel JSON corrisponde a `{"event":"WarBetweenGod#0","attendees":[...]}`.

## Implicazioni

- Per segreti/obiettivi in prosa serve combinare JSON (struttura, `Goal`, `SecretSociety`, relazioni) + org-mode/HTML (testo) + `.murder` (sorgente delle frasi).
- Non esiste nozione di "colpevole"/"vittima": va aggiunta sopra (ticket 08).
