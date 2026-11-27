# TD8 – Yahoo Finance

## Objectif

L'objectif du TD8 est de remplacer les données locales par des données de marché récupérées depuis Yahoo Finance, tout en conservant les fonctions d'analyse développées au TD7.

L'architecture utilisée est :

Yahoo Finance → Provider Yahoo → Données canoniques → Analytics TD7 → Comparaison terminal

## Technologies utilisées

- Python
- `yfinance`
- MarketPulse
- Données AAPL
- Benchmark S&P 500

## Fonctionnement

Le provider Yahoo Finance récupère les données de marché sur une période d'un mois avec un intervalle quotidien.

Les symboles utilisés sont :

| Ticker canonique | Symbole Yahoo Finance |
|---|---|
| AAPL | AAPL |
| SP500 | ^GSPC |

Le ticker canonique `SP500` reste inchangé dans MarketPulse. Le symbole `^GSPC` est utilisé uniquement pour la récupération des données Yahoo Finance.

## Données récupérées

Les données sont normalisées sous forme de lignes canoniques comprenant :

- date
- ticker
- open
- high
- low
- close
- volume

Les données de l'instrument et du benchmark sont ensuite alignées sur leurs dates communes.

## Réutilisation du TD7

Les fonctions d'analyse du TD7 sont réutilisées pour :

- aligner les séries de prix ;
- calculer les rendements sur la période ;
- normaliser les prix en base 100 ;
- calculer la performance relative de l'instrument par rapport au benchmark.

L'analyse financière reste indépendante du fournisseur de données.

## Conclusion

Le TD8 introduit une source de données externe dans MarketPulse grâce à Yahoo Finance et `yfinance`. Il permet de conserver une architecture modulaire où les données récupérées sont normalisées avant d'être transmises aux fonctions d'analyse du TD7.