# Prompt per le immagini – Last Call al Kapu Lounge

Questo file contiene i prompt per generare tutte le immagini del gioco. I prompt sono in **inglese**, perché i generatori (Midjourney, Flux, SDXL, DALL·E, Imagen, Firefly) seguono meglio l'inglese. Le note intorno sono in italiano.

Salva ogni immagine riuscita nella cartella `finali/` **con il nome indicato** accanto al titolo di ogni prompt. Le prove scartate vanno in `bozze/`. Questo file esiste anche in versione `PROMPTS.html`, con un pulsante «Copia» per ogni prompt: è quella da aprire sul cellulare. Quando sono pronte, mandamele e le inserisco in schede e PDF.

## Prima di cominciare

### Le tre regole che valgono per tutto
1. **Niente testo nell'immagine.** I generatori sbagliano le scritte. Dove un foglio, una lettera o un display deve «contenere» del testo, il prompt chiede una pagina con scrittura **illeggibile e sfocata**. Il testo vero (nei file `indizi/` e `oggetti/`) si aggiunge dopo, in impaginazione. Unica eccezione: la copertina.
2. **Nessun volto deve tradire il colpevole.** Tutti i ritratti hanno la stessa espressione: neutra, riservata, un po' sulla difensiva. Non generare sguardi colpevoli, sorrisi cattivi, ombre sinistre o mani nascoste, su Maleko come su chiunque altro, e niente di troppo rilassato o «innocente».
3. **Una sola epoca.** Honolulu, agosto 2004: niente smartphone, niente schermi piatti, niente auto moderne, niente auricolari. Telefoni a conchiglia, compatte digitali da 4 megapixel, registratori a microcassetta.

### Cosa è deciso e cosa no
Costumi e accessori vengono dalle schede, e i giocatori li usano per riconoscersi: non cambiarli. **Etnia, tratti del volto e colore dei capelli non sono scritti nelle schede.** Seguono la composizione reale delle Hawaii: nel 2004 la maggior parte degli abitanti è di origine mista (hawaiana, giapponese, filippina, cinese, portoghese, samoana, bianca) e il locale è pieno di «local». Ogni personaggio ha quindi un'origine mista precisa. Se vuoi altro, cambia quelle parole e lascia il resto.

### Blocchi comuni (da incollare dove indicato)

**[STYLE]** (in coda a ogni prompt)
> cinematic still, tropical neo-noir, Honolulu Waikiki 2004, shot on 35mm film (Kodak Vision3 500T look), 50mm lens, shallow depth of field, available light only, deep contrast, hot pink neon (#FF6FAE) and teal neon (#0F6B6B) glow reflecting on dark koa wood, humid haze, fine film grain, muted but saturated colors, no text, no letters, no logos, no watermark, no frame, no border

**[NEG]** (campo «negative prompt»; se non c'è, accoda «avoid: …»)
> cartoon, illustration, anime, 3D render, plastic skin, oversmoothed skin, airbrushed, text, letters, captions, watermark, logo, signature, modern smartphone, flat-screen TV, modern car, deformed hands, extra fingers, asymmetrical eyes, duplicate faces, stock photo smile, postcard beach, daylight, cheerful tourist mood

**[PORTRAIT]** (per tutti i ritratti)
> waist-up portrait, vertical 3:4, subject looking straight into the camera, neutral guarded expression with the mouth closed, head and shoulders in sharp focus, neon pink light from camera left and teal from camera right, background out of focus

**[OBJECT]** (per tutti gli oggetti di scena)
> top-down shot slightly tilted by 15 degrees, horizontal 4:3, single subject centered, dark koa wood table or aged paper surface, one soft light from the upper left plus faint neon glow on the edge, deep shadows, no hands in the frame unless specified

### Formati
- **Ritratti:** verticale 3:4, almeno 1024×1365 px.
- **Oggetti e indizi:** orizzontale 4:3, almeno 1600×1200 px.
- **Luoghi:** orizzontale 16:9, almeno 1920×1080 px.
- **Copertina:** verticale 2:3, almeno 1600×2400 px.

### Come tenere i volti coerenti
Genera **prima** i ritratti dei giocatori, poi usa ognuno come immagine di riferimento (`--cref` in Midjourney, «character reference» altrove, «image prompt» al 60–70% negli altri strumenti) per le immagini in cui compare lo stesso personaggio. Tre famiglie devono somigliarsi (i tratti sono per l'origine scelta sopra):
- **Mahoe** (Akoni, Pua, Ike): fratelli. Stessa mascella larga, occhi infossati, naso largo.
- **Hanohano** (Maleko, Kalea): fratello e sorella. Stessi zigomi alti, occhi scuri e allungati, sopracciglia dritte.
- **Kealoha** (Keoki, Auntie Lei, Lani): Lani ha gli occhi del padre.

Nalu, Noe e Kapono non sono imparentati con nessuno.

---

## Ritratti dei personaggi

### 01 · `ritratto_01_lani.png` – Lani Kealoha, 31 anni
> [PORTRAIT] Hawaiian-Japanese mixed-heritage woman, 31, black hair in a low loose bun with a single red hibiscus tucked behind her ear, dark navy aloha shirt with a faint black print, a walkie-talkie clipped to her belt, no makeup, dark circles under the eyes from lack of sleep, stubborn jaw, tired but resolute. Background: the polished koa bar of a nightclub, a pink neon sign blurred behind her. [STYLE]

### 02 · `ritratto_02_nalu.png` – Nalu, 29 anni
> [PORTRAIT] Hawaiian-Samoan mixed-heritage man, 29, lean athletic build, short black hair, a short-sleeve red aloha shirt, a black bartender apron, a steel cocktail shaker in his right hand, a bartender's half-smile held back, nervous hands. Background: rows of colored liquor bottles lit from below behind the bar. [STYLE]

### 03 · `ritratto_03_ike.png` – Ike Mahoe, 41 anni
> [PORTRAIT] Hawaiian-Chinese mixed-heritage man, 41, wide jaw and deep-set eyes (brother of Akoni and Pua Mahoe), dark brown hair combed back, a faded flower-print aloha shirt, sand-colored trousers, sunglasses hooked in the shirt pocket, a silver ring on his left pinky, evasive half-smile. Background: a veranda at night with palm silhouettes and a teal neon glow. [STYLE]

### 04 · `ritratto_04_akoni.png` – Akoni Mahoe, 54 anni
> [PORTRAIT] Hawaiian-Chinese mixed-heritage man, 54, wide jaw and deep-set eyes (brother of Ike and Pua Mahoe), neat grey hair, a light linen suit with a pale blue open-collar shirt and no tie, a large chunky wristwatch, a courteous croupier smile that does not reach the eyes. Background: a dinner table with wine glasses blurred behind him. [STYLE]

### 05 · `ritratto_05_pua.png` – Pua Mahoe, 50 anni
> [PORTRAIT] Hawaiian-Chinese mixed-heritage woman, 50, wide jaw and deep-set eyes (sister of Akoni and Ike Mahoe), straight black hair dyed dark auburn to the shoulders, a tailored turquoise skirt suit, a white plumeria lei, a cell phone in each hand, a designer handbag on the arm, a fast professional smile. Background: tall glass windows onto a night beach, neon reflecting in the glass. [STYLE]

### 06 · `ritratto_06_maleko.png` – Maleko Hanohano, 49 anni
> [PORTRAIT] Hawaiian-Filipino mixed-heritage man, 49, dark hair with grey at the temples, high cheekbones and long dark eyes (brother of Kalea Hanohano), a faded flower-print aloha shirt, khaki trousers, a white cotton handkerchief in the breast pocket, a small notebook visible in the back pocket, the mild tired look of an insurance agent, calm and patient. Background: the dark far end of a bar counter with an untouched bottle of beer. Keep the expression neutral and mild: nothing that suggests guilt. [STYLE]

### 07 · `ritratto_07_kalea.png` – Kalea Hanohano, 45 anni
> [PORTRAIT] Hawaiian-Filipino mixed-heritage woman, 45, high cheekbones and long dark eyes (sister of Maleko Hanohano), straight black hair with a side parting, an ivory tailored suit, a purple orchid lei with a few petals loose on the lapel, a leather handbag on the shoulder, a new flip phone in her hand, composed institutional smile with tense eyes. Background: a veranda with pink neon and wicker chairs. [STYLE]

### 08 · `ritratto_08_noe.png` – Noe, 33 anni
> [PORTRAIT] Japanese-Hawaiian woman, 33, short black hair, a light cotton jacket over a dark top, a silver compact digital camera on a strap around her neck and a press badge clipped to the jacket, dry ironic eyes, a mouth ready for a joke. Background: a crowded nightclub room, strongly out of focus, with warm neon dots. [STYLE]

### 09 · `ritratto_09_kapono.png` – Kapono, 36 anni
> [PORTRAIT] Portuguese-Hawaiian mixed-heritage man, 36, broken nose, light brown sun-bleached hair, sun-lined tanned skin, a flower-print shirt worn open over a black staff t-shirt, work gloves poking from a pocket, the shoulders of a former surfer, a silent suspicious gaze. Background: the back of the club, stacked wooden crates and a bare lightbulb. [STYLE]

### 10 · `ritratto_10_auntie_lei.png` – Auntie Lei, 71 anni
> [PORTRAIT] Native Hawaiian woman, 71, broad face, white hair gathered in a bun, a floral muumuu, a purple orchid lei, thick-rimmed glasses, both hands resting on a koa wood cane, a piercing gaze that sees everything, a slow dignified stillness. Background: a wicker chair on a veranda, a stained antique mirror at her shoulder, pink neon on the wall. [STYLE]

### 11 · `ritratto_11_keoki.png` – Keoki Kealoha, 64 anni (la vittima)
> [PORTRAIT] Native Hawaiian man, 64, broad face, short white hair, a grey moustache, a dark navy aloha shirt with a wilted lei around the neck, forearms of a retired Navy cook, a gruff but kind face, tired eyes. Background: his small office with framed black-and-white photographs, a green banker's lamp, a dark wood desk. Slightly warm and sepia-tinted, as in an old photograph on a shelf. [STYLE]

### 12 · `ritratto_12_alapai.png` – Tenente Kimo Alapai, 52 anni (il direttore)
> [PORTRAIT] Hawaiian-Chinese mixed-heritage man, 52, a faded aloha shirt, a thin tie, a straw hat, a small notebook and a pencil in his hand, a calm ironic expression with a hint of a smile, patient eyes. Background: the nightclub with the lights turned off, only a thin pink neon line from the door. [STYLE]

---

## Le tre foto della macchina di Noe (indizi 06 e 26)

Sono immagini **di gioco**: i giocatori le guardano e ci ragionano. Conta la composizione, non l'estetica. Stile diverso dal resto: **sembrano scatti di una compatta digitale del 2004**, con flash diretto, 4 megapixel, colori un po' slavati, rumore digitale, nessuna profondità di campo. Non usare [STYLE] qui. Se serve la data stampata in arancione in basso a destra, aggiungila dopo in impaginazione (`'04 8 14  23:12`, ecc.).

Usa gli stessi volti dei ritratti 04, 05, 06 e 10.

### 13 · `foto_IMG_0412.png` – indizio 06, ore 23:12
> Amateur flash photo taken with a 2004 compact digital camera (4 megapixels, direct on-camera flash, slightly washed colors, mild digital noise, flat lighting). A veranda at night with wicker chairs and a glass door behind. Four people sit and stand around a low table: a man in a light linen suit (Akoni, looking down at a flip phone), a woman in a turquoise suit (Pua, standing), an old woman with white hair, a purple orchid lei and a cane (Auntie Lei, seated), and a man in a faded floral shirt and khakis (Maleko, seated at the end). In the foreground one wicker chair is empty, with a half-full glass of white wine on the small table beside it. No text, no date stamp.

### 14 · `foto_IMG_0413.png` – indizio 26, ore 23:15 (la foto nascosta)
> Amateur photo taken with a 2004 compact digital camera, flash off, available neon light, slightly blurry, as if taken in a hurry, shot from a dark veranda looking inward through a large glass door into a nightclub hall at the exact moment a burst of confetti and colored streamers explodes in the air inside, stage lights, a few blurred guests. On the left edge of the frame, in profile on a side staircase leading down to the beach, a man in a light linen suit with a flip phone pressed against his ear. In the center, close to the glass door, a woman in a turquoise suit, and next to her an old white-haired woman seated in a wicker chair with a cane. At the very bottom edge of the frame, the tip of a pair of dark shoes (the photographer's). No text, no date stamp.

### 15 · `foto_IMG_0414.png` – indizio 06, ore 23:16
> Amateur flash photo taken with a 2004 compact digital camera (4 megapixels, direct on-camera flash, washed colors, noise), the same veranda at night. Three people only: a man in a light linen suit at the left with a flip phone to his ear (Akoni), a woman in a turquoise suit (Pua), and an old white-haired woman with a purple orchid lei and a cane seated at the right (Auntie Lei). No fourth person. In the foreground, the same wicker chair still empty, the half-full glass of white wine still on the small table. No text, no date stamp.

---

## Indizi (le carte, `indizi/`)

Tutti i fogli e i documenti: scrittura **illeggibile e sfocata** (regola 1).

### 16 · `indizio_01_foglio_impronta.png`
> [OBJECT] A yellow notepad on a dark wooden desk: the top sheet has been torn off, and the sheet underneath carries the faint embossed impression of handwriting pressed through from above, visible only as grooves, not letters. A black ballpoint pen lies beside it. Green banker's lamp glow from the upper left. [STYLE]

### 17 · `indizio_03_revolver.png`
> [OBJECT] A Smith & Wesson Model 36 revolver, blue steel, short barrel, wrapped loosely in a white kitchen towel with blue embroidered letters (illegible) and grey ash smudges, lying on top of a black guitar amplifier road case in a dim corridor. Stark single-source light. [STYLE]

### 18 · `indizio_04_petali.png`
> [OBJECT] Four purple orchid petals on a dark carpet; one petal bears a clear flat rubber-sole footprint, large and smooth. Teal neon glow on the carpet. [STYLE]

### 19 · `indizio_05_scontrini.png`
> [OBJECT] Four narrow thermal cash-register receipts lined up on a dark bar counter next to a half-empty tiki glass with a paper umbrella; the printed times are small and blurred. Pink neon reflection in the wet counter. [STYLE]

### 20 · `indizio_07_bolla.png`
> [OBJECT] A carbon-copy delivery slip with two signatures at the bottom (scribbled, unreadable), lying on an open wooden crate; the stencil on the bottom of the crate reads «HABANA» (this one word is allowed). Bare lightbulb light, cellar atmosphere. [STYLE]

### 21 · `indizio_08_pagina_registro.png`
> [OBJECT] Half of a page torn violently from a green clothbound ledger: a ragged diagonal edge, three columns of dates and numbers in blue ballpoint, all illegible, a darker stain in one corner. On a dark wooden desk. [STYLE]

### 22 · `indizio_09_offerta.png`
> [OBJECT] A formal business letter on cream stationery with a blurred corporate letterhead, a fountain pen across it, a dark leather desk blotter; one signature at the bottom, illegible. [STYLE]

### 23 · `indizio_10_testamento.png`
> [OBJECT] Three pages of a draft will with handwritten corrections in blue ink and margin notes, a ballpoint pen and a pair of reading glasses on top, an old manila folder underneath. [STYLE]

### 24 · `indizio_11_biglietto.png`
> [OBJECT] A small crumpled sheet of paper, flattened, with blocky capital handwriting (illegible), a coffee ring and creases, on a worn wooden table. [STYLE]

### 25 · `indizio_12_taccuino_noe.png`
> [OBJECT] A reporter's spiral notebook open to a page with scribbled notes and one line underlined twice, a small cassette recorder beside it. [STYLE]

### 26 · `indizio_13_copia_registro.png`
> [OBJECT] A grainy black-and-white photocopy of a ledger page with 22 rows of dates and amounts (illegible), a pencil line underlining the last row, lying over an open steel safe-deposit box. [STYLE]

### 27 · `indizio_14_cassetto_vuoto.png`
> [OBJECT] An open desk drawer, dark lacquered wood, empty, with a clean darker revolver-shaped silhouette on the bottom where oil has stained the finish, an almost-full box of .38 cartridges at the back. Undisturbed dust around the shape. [STYLE]

### 28 · `indizio_15_lampadina.png`
> [OBJECT] A bare light bulb in a ceiling socket in a dark service corridor, slightly unscrewed, a tiny white cotton thread caught on the glass. Doors in the background in deep shadow. [STYLE]

### 29 · `indizio_16_braciere.png`
> [OBJECT] A small iron charcoal brazier in a restaurant kitchen, compact grey ashes with the corner of a scrap of burned green cloth visible, a trace of ink on it, illegible. Metal pots hanging in the dark. [STYLE]

### 30 · `indizio_17_strofinacci.png`
> [OBJECT] A neat pile of nine white kitchen towels with blue embroidered lettering (illegible), a wet sink with soap traces behind it, a visible gap on the shelf where a tenth would sit. [STYLE]

---

## Oggetti personali (`oggetti/`)

### 31 · `oggetto_01_busta_malia.png`
> [OBJECT] A cream envelope aged by time, handwriting in blue ink on the front (illegible), sealed, on dark wood, a faint ring where a glass once stood. [STYLE]

### 32 · `oggetto_02_chiave_k3.png`
> [OBJECT] A small brass key with a small brass tag (blank), lying on a dark bar counter. [STYLE]

### 33 · `oggetto_03_scatola_sigari.png`
> [OBJECT] A plain light-wood cigar box, no markings, lid slightly open, a single cigar and a folded handwritten note inside (illegible), dark counter surface. [STYLE]

### 34 · `oggetto_04_offerta_rilanciata.png`
> [OBJECT] A formal offer letter on corporate stationery with a blurred letterhead, a short clause in small print at the bottom, a fountain pen across it, dark desk. [STYLE]

### 35 · `oggetto_05_ricevuta.png`
> [OBJECT] A short receipt form with three handwritten lines (illegible) and an empty signature line, on a glossy table. [STYLE]

### 36 · `oggetto_06_registratore_maleko.png`
> [OBJECT] A small microcassette recorder with a red indicator light on, lying on a dark bar counter beside an untouched bottle of beer, soft neon glow. [STYLE]

### 37 · `oggetto_07_busta_kalea.png`
> [OBJECT] A thick brown envelope with hundred-dollar bills sticking out, resting inside an open ivory leather handbag, a flip phone beside it. [STYLE]

### 38 · `oggetto_08_registratore_noe.png`
> [OBJECT] A journalist's handheld cassette recorder with a cassette inside, a hand pressing the play button, teal neon in the background. [STYLE]

### 39 · `oggetto_09_macchina_noe.png`
> [OBJECT] A silver compact digital camera with a press badge dangling from the strap, on a small table on a veranda at night, a dim wicker chair behind it. [STYLE]

### 40 · `oggetto_10_atto_1958.png`
> [OBJECT] An aged yellowed property deed with a faded stamp and two blurred signatures, folded corners, old ink, on dark wood. [STYLE]

---

## Carte piatto della cena (`oggetti/piatto_*.md`)

Solo se fai la cena. Luce più calda e meno noir, sempre con il bagliore del neon sui bordi.

### 41 · `piatto_lani_kalua.png`
> [OBJECT] A tray of small soft milk-bread buns filled with shredded smoked pulled pork, on dark wood, a paper napkin, warm tungsten light with pink neon rim. [STYLE]

### 42 · `piatto_lei_haupia.png`
> [OBJECT] A white tray with squares of firm coconut pudding (haupia), a spatula beside it, on dark wood. [STYLE]

### 43 · `piatto_kapono_poke.png`
> [OBJECT] Several small ceramic cups of salmon poke with sesame seeds and sliced onion, on a bed of crushed ice, a pair of chopsticks across the tray. [STYLE]

### 44 · `piatto_nalu_drink.png`
> [OBJECT] A tall glass of clear ice with two thick lemon slices, condensation running down it, on a dark bar counter, neon reflection in the water. [STYLE]

### 45 · `piatto_noe_piatto_vuoto.png`
> [OBJECT] An empty white plate on a dark bar counter, a white plumeria lei laid on top, a dim neon sign blurred behind. Quiet, mournful. [STYLE]

---

## I luoghi (per atmosfera e per il direttore)

Formato 16:9. Nessuna persona.

### 46 · `luogo_sala.png`
> A nightclub main hall after closing, Waikiki 2004, a small stage with a drum set and a microphone, a long koa wood bar with a cash register, bar stools, colored confetti and streamers on the floor, a blackboard above the bar (blurred, illegible), pink and teal neon, wet polished floor. [STYLE]

### 47 · `luogo_ufficio.png`
> A small cluttered office from the 2000s, a dark wooden desk, a chair pulled back, a green banker's lamp, a notepad, framed photographs on the wall, an archive cabinet, teal neon from the window. [STYLE]

### 48 · `luogo_corridoio.png`
> A narrow service corridor with a single bare lightbulb, a half-open office door at the far end, a black amplifier case against the wall, doors on both sides. [STYLE]

### 49 · `luogo_veranda.png`
> A veranda facing a night beach, wicker chairs around a low table, a large glass door lit from inside by neon, a side staircase going down to the sand, palm silhouettes, surf in the dark. [STYLE]

### 50 · `luogo_cucina.png`
> A restaurant kitchen after hours, steel counters, a sink, an iron charcoal brazier, hanging pans, a stack of white towels on a shelf. [STYLE]

### 51 · `luogo_scantinato.png`
> A basement storeroom with a loading hatch open onto an alley at night, stacked wooden crates, a bare bulb. [STYLE]

---

## Copertina

### 52 · `copertina.png` (qui il testo è permesso)
> Vertical 2:3 poster in a retro noir style for a Waikiki nightclub, 2004. A pink neon sign reading «KAPU LOUNGE» above a doorway (this text only, nothing else), palm trees, a night sky in deep indigo (#12112B), teal reflections on wet pavement, the silhouette of an older man in an aloha shirt leaving through the door, backlit, a faint hot-pink glow around him. Cinematic, shot on 35mm film, high contrast, no other text, no logo.

---

## Elenco di controllo

| Gruppo | File | Priorità |
|--------|------|----------|
| Foto di Noe (di gioco) | 13, 14, 15 | **Alta**: i giocatori le guardano |
| Ritratti | 01–12 | **Alta** |
| Indizi | 16–30 | Media: servono se stampi le carte con immagine |
| Oggetti personali | 31–40 | Media |
| Piatti | 41–45 | Solo con la cena |
| Luoghi | 46–51 | Bassa: per atmosfera |
| Copertina | 52 | Media |

Se hai poco tempo: genera solo le **tre foto**, i **dieci ritratti dei giocatori** e la **copertina**. Il resto aggiunge atmosfera ma non cambia la partita.

---

## Come lavorare con i piani gratuiti di ChatGPT e Gemini

### Le cartelle
```
immagini/
  PROMPTS.md       questo file
  PROMPTS.html     la stessa cosa, per il cellulare
  finali/          le immagini scelte, con il nome esatto del prompt
  bozze/           tutto il resto, senza fretta di rinominare
```
Quando una bozza è quella buona, la copi in `finali/` col nome giusto. Il nome è l'unica cosa che mi serve per inserirla in schede e PDF.

### Il metodo
1. **Un giorno, un gruppo.** I piani gratuiti concedono poche immagini al giorno, e i limiti cambiano senza preavviso: controllali nell'app. Procedi per priorità, non per numero. Giorno 1: ritratti 01–06. Giorno 2: ritratti 07–12. Giorno 3: le tre foto di Noe e la copertina. Poi indizi e oggetti, quando vuoi.
2. **Un personaggio, una conversazione.** Genera il ritratto, tienilo aperto e per ogni immagine successiva dello stesso personaggio scrivi «stessa persona di questa immagine» e incolla il prompt nuovo. È il modo più economico per tenere il volto coerente senza strumenti a pagamento.
3. **Le famiglie in sequenza.** Fai prima Akoni, poi Pua e Ike nella stessa conversazione di Akoni, chiedendo «fratello/sorella di questa persona». Lo stesso per Maleko e Kalea.
4. **Le tre foto di Noe sono le più difficili**, perché i generatori sbagliano il numero di persone. Tira 3–4 tentativi per ognuna e scegli quella con le persone giuste, anche se è meno bella. Conta la composizione.
5. **Se compare del testo**, rigenera una volta con «no text, no letters». Se resta, lo copro io in impaginazione.
6. **Per gli oggetti puoi usare la fotocamera**: una busta, una chiave, una scatola di sigari veri, fotografati di sera con una lampada, costano meno di un'immagine generata e non sbagliano le dita. Per le carte indizio col testo è anche la soluzione più pulita.
7. **Chi fa cosa.** Non ho prove che uno dei due strumenti sia migliore sui volti. Fai un test con il ritratto 06 (Maleko) su entrambi e tieni quello che ti convince di più: poi usa sempre quello per tutti i personaggi.
