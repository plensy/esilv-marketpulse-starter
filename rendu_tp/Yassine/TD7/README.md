# TD7 – Financial Analytics

## Objectif

L'objectif du TD7 est de mettre en place des fonctions d'analyse financière permettant de comparer l'évolution de plusieurs séries de prix.

Les données sont organisées sous forme de lignes canoniques et les fonctions d'analyse sont regroupées dans `src/analytics.py`.

## Fonctions implémentées

### 1. `index_by_date()`

Permet d'organiser les données en utilisant les dates comme index afin de faciliter leur manipulation.

### 2. `align_series()`

Permet d'aligner deux séries de prix sur leurs dates communes afin de pouvoir effectuer une comparaison cohérente.

### 3. `calculate_period_return()`

Calcule le rendement d'une série sur une période à partir du premier et du dernier prix.

### 4. `calculate_base_100()`

Normalise une série de prix en base 100 afin de comparer son évolution.

Le premier prix de la série est fixé à 100.

### 5. `calculate_relative_performance()`

Compare la performance d'un actif avec celle d'un benchmark.

La performance relative est calculée en soustrayant le rendement du benchmark au rendement de l'actif.

## Tests

Les fonctions ont été vérifiées à l'aide des tests unitaires du projet.

## Conclusion

Ce TD permet de construire une première couche d'analyse financière réutilisable pour comparer des actifs et des benchmarks. Les fonctions développées seront réutilisées dans les TD suivants.
