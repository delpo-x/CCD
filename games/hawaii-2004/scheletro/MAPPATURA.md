# Mappatura dello scheletro di murder-generator

`scheletro.json` e `scheletro.org` sono l'esito di una generazione di murder-generator con 10 giocatori, data 2004, e solo i temi Famiglia, Soldi, Romance, Segreti oscuri e «non adatto ai bambini».

Il generatore non produce un crimine: restituisce un **grafo di relazioni** (parentele, amori, debiti, favori, conflitti) tra personaggi con nomi e mestieri inventati. Ho tenuto solo il grafo. Le parentele e le date sono incoerenti (una persona nata nel 1809 risulta nonna di una ventenne), mestieri e società segrete sono stati sostituiti.

| Nome generato | Personaggio |
|---------------|-------------|
| Je | Lani Kealoha |
| Itonrson | Tommy Akana |
| Ergen | Ray Lund |
| Whergeehn | Brad Lund |
| Zyacester | Victoria «Vicki» Lund |
| Hihn | Marcus Delaney |
| Theams | Claudia Delaney |
| Derrough | Noe Sato |
| Fough | Jimmy «Jimbo» Pelletier |
| Sunes | Leilani «Auntie Lei» Kealoha |

## Legami del grafo tenuti nel gioco
- Itonrson e Je sono fratelli; Je ama Itonrson. → Tommy e Lani fratelli adottivi; lei lo ama.
- Itonrson ama Ergen. → Tommy e Ray hanno una relazione segreta.
- Itonrson ha un debito grosso con Whergeehn e con Zyacester. → Tommy deve soldi a Brad e a Vicki.
- Hihn e Theams sono fratelli in conflitto. → Marcus e Claudia.
- Hihn ha un favore e un debito grossi con Je. → Marcus deve un favore grosso a Lani.
- Fough ama Derrough. → Jimbo ama Noe.
- Theams ha un debito grosso con Fough. → Claudia viene ricattata da Jimbo.
- Derrough ama Theams. → Noe ama Claudia.
- Fough ed Ergen sono fratelli. → Jimbo e Ray sono fratellastri.
- Zyacester e Whergeehn sono fratelli. → Vicki e Brad.
- Whergeehn ed Ergen sono fratelli in conflitto esplosivo. → Brad e Ray.
- Je ha un debito con Whergeehn. → Lani ha una garanzia con Brad.
- Ergen ha un debito grosso con Sunes. → Ray deve soldi ad Auntie Lei.
- Sunes ha un favore grosso con Derrough. → Auntie Lei racconta storie e presta soldi a Noe.
- Zyacester ha un vecchio debito con Sunes. → Vicki e un vecchio favore di Auntie Lei.

Il crimine, la vittima, gli alibi, gli indizi e la soluzione sono stati scritti a mano.
