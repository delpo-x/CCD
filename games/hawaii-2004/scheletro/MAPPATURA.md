# Mappatura dello scheletro di murder-generator

`scheletro.json` e `scheletro.org` sono l'esito di una generazione di murder-generator con 10 giocatori, data 2004, e solo i temi Famiglia, Soldi, Romance, Segreti oscuri e «non adatto ai bambini».

Il generatore non produce un crimine: restituisce un **grafo di relazioni** (parentele, amori, debiti, favori, conflitti) tra personaggi con nomi e mestieri inventati. Ho tenuto solo il grafo. Le parentele e le date sono incoerenti (una persona nata nel 1809 risulta nonna di una ventenne), mestieri e società segrete sono stati sostituiti.

| Nome generato | Personaggio |
|---------------|-------------|
| Je | Lani Kealoha |
| Itonrson | Nalu Akana |
| Ergen | Ikaika «Ike» Mahoe |
| Whergeehn | Akoni Mahoe |
| Zyacester | Pualani «Pua» Mahoe |
| Hihn | Maleko Hanohano |
| Theams | Kalea Hanohano |
| Derrough | Noe Sato |
| Fough | Kapono Medeiros |
| Sunes | Leilani «Auntie Lei» Kealoha |

## Legami del grafo tenuti nel gioco
- Itonrson e Je sono fratelli; Je ama Itonrson. → Nalu e Lani fratelli adottivi; lei lo ama.
- Itonrson ama Ergen. → Nalu e Ike hanno una relazione segreta.
- Itonrson ha un debito grosso con Whergeehn e con Zyacester. → Nalu deve soldi a Akoni e a Pua.
- Hihn e Theams sono fratelli in conflitto. → Maleko e Kalea.
- Hihn ha un favore e un debito grossi con Je. → Maleko deve un favore grosso a Lani.
- Fough ama Derrough. → Kapono ama Noe.
- Theams ha un debito grosso con Fough. → Kalea viene ricattata da Kapono.
- Derrough ama Theams. → Noe ama Kalea.
- Fough ed Ergen sono fratelli. → Kapono e Ike sono fratellastri.
- Zyacester e Whergeehn sono fratelli. → Pua e Akoni.
- Whergeehn ed Ergen sono fratelli in conflitto esplosivo. → Akoni e Ike.
- Je ha un debito con Whergeehn. → Lani ha una garanzia con Akoni.
- Ergen ha un debito grosso con Sunes. → Ike deve soldi ad Auntie Lei.
- Sunes ha un favore grosso con Derrough. → Auntie Lei racconta storie e presta soldi a Noe.
- Zyacester ha un vecchio debito con Sunes. → Pua e un vecchio favore di Auntie Lei.

Il crimine, la vittima, gli alibi, gli indizi e la soluzione sono stati scritti a mano.
