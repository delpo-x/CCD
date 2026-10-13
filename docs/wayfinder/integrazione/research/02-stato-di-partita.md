# Ticket 02 - Cosa richiede lo Stato di partita e come saltare gli agenti LLM

Sorgenti primarie: codice in `mystery-agents/src/mystery_agents/` (branch `research/02-stato-di-partita`, base 3f7e527) ed esperimenti eseguiti in dry-run (nessuna chiamata API).

## Risposta breve

1. **Lo stato e' gia' serializzabile**: `GameState` e tutti i sotto-modelli sono `pydantic.BaseModel` puri (`models/state.py:635`). Round-trip verificato: `model_dump_json()` -> `GameState.model_validate_json()` funziona senza modifiche (`poc/poc_load_state.py`). Nel repo pero' nessun punto lo fa (grep `model_dump|model_validate|json.load` in `src/`: solo `debug_middleware.py:76` per i log e `i18n.py:300` per i locali).
2. **Non esiste una modalita' "carica stato e salta gli LLM"**. La CLI (`cli.py:149-163`) costruisce sempre un `GameState` vuoto e lancia il grafo da `START -> a1_config` (`workflow.py:316`). `--dry-run` non salta i nodi: li esegue tutti, ma ogni agente LLM restituisce dati finti (`BaseAgent._should_use_mock`, `agents/base.py:71-81`).
3. **Aggiungerla e' banale** perche' i nodi del grafo sono funzioni `GameState -> GameState`: basta un secondo grafo (o entry point) con solo `a8_5_host_images` + `a9_packaging`. PoC funzionante in `poc/poc_load_state.py` (~40 righe, nessuna modifica al codice di produzione): 18/19 PDF + ZIP generati da uno stato JSON caricato da disco, zero LLM.
4. **`--dry-run` offre un template utilizzabile**: `poc/example_state_dry_run.json` (13 KB) e' lo stato completo dopo a1..a8 in dry-run. Attenzione: i contenuti sono segnaposto (`MOCK_*`, `Character_1`, 2 soli indizi): utile come *forma* dello schema, non come contenuto.
5. Per il solo impaginatore (a8_5 + a9) servono **pochi campi** (sezione sotto): gran parte dello stato e' contesto per i prompt LLM a monte.

## Agenti: LLM o deterministici (`graph/workflow.py:300-355`)

"LLM" = chiama `BaseAgent.invoke` -> `create_agent(...).invoke` (`agents/base.py:164`). Il costruttore istanzia comunque un `ChatGoogleGenerativeAI` via `LLMCache` (chiave fittizia `dry-run-dummy-key` se manca `GOOGLE_API_KEY`, `config.py:56-61`: nessuna rete finche' non si invoca).

| Nodo | Classe / tier | Tipo | Legge (state.*) | Scrive | Riferimenti |
|---|---|---|---|---|---|
| a1_config | `ConfigLoaderAgent` (no BaseAgent) | deterministico (YAML) | `config.config_file` + flag CLI | `config` | a1_config.py:25-90 |
| a2_world | `WorldAgent` tier1 | **LLM** | `config` | `world` | a2_world.py:31,111-114 |
| v1_world_validator | tier2 | **LLM** (validatore, loop max 2 retry) | `world`, `config` | `world_validation`, `world_retry_count` | v1_world_validator.py:40,149; workflow.py:241 |
| a2_5_visual_style | tier2 | **LLM** | `world.*`, `config` | `visual_style` | a2_5_visual_style.py:32,93 |
| a3_characters | tier2 | **LLM** | `config`, `world.summary` | `characters` | a3_characters.py:36,107 |
| a3_5_character_images | `CharacterImageAgent` | **API immagini Gemini** (non chat LLM); saltato se `generate_images=False` | `characters`, `visual_style`, `config.country`, `meta.id` | `characters[].image_path` | a3_5_character_images.py:57,92,240; workflow.py:93 |
| a4_relationships | tier2 | **LLM** | `characters` | `relationships` | a4_relationships.py:35,111 |
| a5_crime | tier1 | **LLM** | `characters`, `world.summary`, `config` | `crime` | a5_crime.py:36,112 |
| a6_timeline | tier2 | **LLM** | `characters`, `maps` (mai popolato), `crime.time_of_death` | `timeline_global` | a6_timeline.py:24,58,103 |
| a7_killer | tier1 | **LLM** | `characters`, `timeline_global`, `crime` | `killer_selection` | a7_killer_selection.py:20,124 |
| v2_game_logic_validator | tier1 | **LLM** (loop: retry -> a6, max 3) | `killer_selection`, `timeline_global`, `characters`, `config` | `validation`, `retry_count` | v2_game_logic_validator.py:30,145; workflow.py:265,343 |
| **a8_content** | `ContentGenerationAgent` tier2 | **LLM** | `config`, `world`, `crime.*`, `characters`, `killer_selection` | `host_guide`, `clues`, `killer_brief_narrative` | a8_content.py:54,170-176 |
| **a8_5_host_images** | `HostImageAgent` | **API immagini Gemini**; no-op se `generate_images=False` (a8_5:76); errori inghiottiti (workflow.py:221) | `crime.victim`, `host_guide.host_act2_detective_role`, `visual_style`, `config.country`, `meta.id` | `crime.victim.image_path`, `...detective_role.image_path` | a8_5_host_images.py:44-52,83-101 |
| **a9_packaging** | `PackagingAgent` | **deterministico**: eredita BaseAgent e crea un LLM tier3 inutilizzato (a9:94) ma `run` non chiama mai `invoke`; scrive MD, WeasyPrint -> PDF, ZIP | vedi sotto | `packaging` (+ file su disco) | a9_packaging.py:203-406 |

Riepilogo: **LLM chat** = a2, v1, a2.5, a3, a4, a5, a6, a7, v2, a8 (10 nodi). **Immagini** = a3.5, a8.5 (opzionali). **Deterministici** = a1, a9. Nessun nodo scrive `personal_timelines`, `maps`, `generated_assets` (campi dichiarati ma morti; `maps` e' letto da a6 ma nessuno lo popola).

## Campi realmente richiesti dall'impaginazione (a8_5 + a9)

Letti da `a9_packaging.py` (verificato per grep delle chiamate `state.*` e degli oggetti passati ai `_write_*`):

- `meta.id` (nome cartella/ZIP), `meta.created_at` (a9:206,416)
- `config`: `language` (etichette, nomi file, traduzioni), `country`, `region`, `custom_epoch_description`, `duration_minutes`, `theme`, `keep_work_dir`, `killer_knows_identity`, `generate_images` (solo a8_5). `dry_run` deve essere `False`, altrimenti a8_5 usa i mock.
- `world`: `epoch`, `location_name`, `gathering_reason` (a9:108,419,601,798; opzionale, con fallback)
- `characters[]`: `id`, `name`, `role`, `public_description`, `personality_traits`, `personal_secrets`, `personal_goals`, `act1_objectives`, `motive_for_crime`, `relation_to_victim`, `costume_suggestion`, `image_path` (a9:624-780). Non usati: gender, age_range, live_action_killer_instructions.
- `relationships[]`: `from_character_id`, `to_character_id`, `type`, `description`, `tension_level` (a9:669-700)
- `crime.victim`: `name`, `role_in_setting`, `public_persona`, `personality_traits`, `secrets`, `costume_suggestion`, `image_path` (a9:788-850). `crime.murder_method`/`crime_scene` **non** sono letti da a9 (solo da a7/a8 a monte).
- `killer_selection`: `killer_id`, `rationale`, `truth_narrative` (a9:499-512,712); `killer_brief_narrative` solo se `killer_knows_identity`.
- `timeline_global`: `time_blocks[].start/end/events[].description` e `live_action_murder_event` (`time_approx`, `room_id`, `description`, `character_ids_involved`) (a9:523-555)
- `host_guide`: `spoiler_free_intro`, `host_act1_role_description`, `setup_instructions`, `runtime_tips`, `live_action_murder_event_guide`, `act_2_intro_script`, `host_act2_detective_role` (`character_name`, `public_description`, `personality_traits`, `clues_to_reveal`, `guiding_questions`, `final_solution_script`, `costume_suggestion`, `image_path`)
- `clues[]`: `id`, `type`, `title`, `description`, `incriminates`, `exonerates`, `is_red_herring` (a9:929-998). Non usati: `assigned_to_character_id`, `relates_to_events`, `reveal_phase`.
- Solo per a8_5 (se si generano immagini): `visual_style` (opzionale, c'e' un fallback).

**Non servono ad a8_5/a9**: `validation`, `world_validation`, `retry_count*`, `max_*`, `personal_timelines`, `maps`, `generated_assets`, `crime.murder_method|crime_scene|possible_*`, `world.summary|visual_keywords|constraints|location_type`, `meta.version`.

Obbligatori per `GameState` sono solo `meta` e `config` (state.py:641-642); a9 degrada con fallback se `world/host_guide/crime` mancano, ma quei campi producono i documenti. Un importatore da murder-generator deve quindi produrre: `characters`, `clues`, `host_guide`, `crime.victim`, `killer_selection`, `timeline_global`, `world`, `relationships`, piu' `config.language` coerente con la lingua dei testi.

## Esperimento

```
# dump (dry-run a1..a8; install funzionante con PYTHONPATH sul worktree)
python poc/poc_load_state.py dump game.example.yml poc/example_state_dry_run.json
# carica il JSON, salta gli LLM, esegue solo a8_5 + a9
python poc/poc_load_state.py pack poc/example_state_dry_run.json <out_dir>
```

Esito: `model_validate_json` ok. Grafo `[a8_5 -> a9]` completato con `dry_run=False` e senza chiave API reale: 18/19 PDF + ZIP alla prima esecuzione (1 timeout di 30 s su `guia_del_anfitrion` con 12 worker WeasyPrint paralleli, `a9:132-200`: flake di carico, non di stato). Struttura prodotta: `juego/` (guida anfitrione, soluzione, riferimento indizi), `personajes/` (invito + scheda per personaggio, vittima, detective), `pistas/`.

## Punti di attenzione per l'integrazione

- **Percorsi immagini**: `image_path` e' un percorso assoluto locale; a9 incorpora l'immagine solo se `Path(image_path).exists()` (a9:634,802,870). Uno stato importato deve puntare a file esistenti o lasciarli `null` (appare il testo "no image").
- **ID coerenti**: i riferimenti incrociati usano gli `id` (`incriminates`, `from/to_character_id`, `killer_id`, `character_ids_involved`). a9 ha un match parziale per nome (a9:557-593) ma conviene ID corretti.
- **Lingua**: a9 non traduce i contenuti, solo etichette e nomi file (a9:207-208); `config.language` deve essere uno di `es|en|it|de|he` (state.py:18).
- **Dove inserire la modalita'**: minimo, un flag in `cli.py` tipo `--from-state state.json` che fa `GameState.model_validate_json(...)` e invoca un `create_packaging_workflow()` (a8_5 -> a9) in `graph/workflow.py`. Salvare lo stato a ogni nodo con `model_dump_json` darebbe anche il resume.
- `workflow.stream` nella CLI restituisce gli stati come dict (`cli.py:204`): per salvare lo stato finale usare `GameState.model_validate(final_state)`.

## File

- `poc/poc_load_state.py` - PoC (non e' codice di produzione)
- `poc/example_state_dry_run.json` - template di stato completo da dry-run
