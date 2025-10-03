| Explication                      | Test                               | Résultat attendu |
|----------------------------------|------------------------------------|------------------|
| Plusieurs couleurs dans la liste | ["rouge", "bleu", "vert", "rouge"] | 2                |
| Une couleur seulement            | ["rouge", "rouge", "rouge"]        | 3                |
| Liste vide                       | [ ]                                | 0                |
| Couleur avec des majuscules      | ["ROUGE", "rouge", "bleu"]         | 3                |
| Couleur avec une majuscule       | ["Rouge", "rouge", "bleu"]         | 3                |
| Chiffre dans la liste            | [12, "rouge", "bleu"]              | TypeError        |