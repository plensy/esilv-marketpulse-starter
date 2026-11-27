# TD7 – Financial Analytics

## Objectif

Créer un module `analytics.py` contenant cinq fonctions permettant d'analyser des séries de données financières.

## Fonctions implémentées

### 1. index_by_date()

Permet d'indexer les observations financières par date afin de faciliter leur accès.

### 2. align_series()

Permet d'aligner deux séries financières en utilisant uniquement leurs dates communes.

### 3. calculate_period_return()

Calcule le rendement d'une série de prix sur une période.

Formule utilisée :

\[
R = \frac{P_{final}}{P_{initial}} - 1
\]

### 4. calculate_base_100()

Normalise une série de prix en base 100 afin de comparer leur évolution.

Le premier prix de la série est fixé à 100.

### 5. calculate_relative_performance()

Compare la performance d'un actif avec celle d'un benchmark.

La performance relative est calculée en soustrayant le rendement du benchmark au rendement de l'actif.

## Tests

Les tests unitaires ont été exécutés avec la commande :

```bash
python tests.py