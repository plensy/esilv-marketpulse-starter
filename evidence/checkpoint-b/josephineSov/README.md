# Checkpoint B – josephineSov

- Nom : Joséphine Sauvé
- GitHub : @josephineSov
- Groupe / équipe : G02 – T01
- Dépôt : `esilv-marketpulse-g02-t01`
- Branche personnelle : `josephineSauve`

## Mes commits sur le `main` de l'équipe

| Commit | Message | TD |
|---|---|---|
| `f71e4b9` | `feat: display market metadata` | TD05 |
| `7ed7509` | `feat(analytics): implement index_by_date` | TD07 |
| `09ee508` | `feat(analytics): implement calculate_relative_performance` | TD07 |

## Ma Pull Request

- PR #5 `feat: display market metadata` : `main` ← `feature/display-market-metadata`. Relue et approuvée par PAULCO6, puis fusionnée.

## Pull Requests que j'ai relues

- PR #8 `feat: add core quantitative analytics module` (alban-murat), en tant que relectrice officielle du TD07 : **Approve**.
- PR #4 `feat: display data provider label in summary` (alban-murat), au TD06 : **Approve**.

## Preuves requises

| Fichier | TD | Contenu |
|---|---|---|
| `01_pull_request.png` | TD05 | ma PR #5 : titre, autrice josephineSov, `main` ← `feature/display-market-metadata`, description What changed / Why / Validation |
| `02_code_review.png` | TD07 | ma revue de la PR #8 : vérifications détaillées et **Approve**, PR fusionnée après la revue |
| `03_yahoo_market_data.png` | TD08 | `python src/main.py` sur `feature/yahoo-provider` : `Provider: Yahoo Finance`, données récupérées en direct le 2026-11-25 |
| `04_instrument_benchmark.png` | TD08 | AAPL et SP500 récupérés depuis Yahoo sur le même lookback (`1mo`) et le même intervalle (`1d`) : 23 séances chacun, du 2026-10-26 au 2026-11-25 |

## Preuves complémentaires

| Fichier | Contenu |
|---|---|
| `02_code_review_pr4.png` | ma revue de la PR #4 (TD06) |
| `pr5_review_merged.png` | ma PR #5 relue par PAULCO6, puis fusionnée après la revue (TD06) |
| `td07_comparison_run.png` | `python src/main.py` sur `main` après le TD07 : comparaison et base 100 sur les données CSV |

## TD05 – Remote branch + Pull Request

- Team Baseline Gate : `archive/td04-local` créée (locale), `main` aligné sur `origin/main`.
- Branche `feature/display-market-metadata` créée depuis le `main` commun.
- Commit `feat: display market metadata` : helper `display_market_metadata(asset)` qui affiche `market` et `currency`, réutilisé pour l'instrument (NASDAQ, USD) et le benchmark (US, USD).
- `git push -u origin feature/display-market-metadata`, puis PR #5 vers le `main` de l'équipe.

## TD06 – Code review

- Revue de la PR #4 : Files changed vérifié (1 ligne dans `src/main.py`), exécution de `python src/main.py` sur la branche, description cohérente avec le diff. Suggestion non bloquante : utiliser une constante `PROVIDER_LABEL` plutôt que `"CSV"` en dur. Résultat : **Approve**.
- Ma PR #5 a été approuvée par PAULCO6 sans correction demandée, donc aucun commit de correction. Fusionnée après la revue.
- `main` local synchronisé avec `git switch main` puis `git pull`, et `python src/main.py` fonctionne.

## TD07 – Data normalization + comparison

- Rôle : Student 2. J'ai codé `index_by_date` et `calculate_relative_performance` dans `src/analytics.py`, sur la branche commune `feature/analytics`.
- Relectrice officielle de la PR #8 : vérification des 5 fonctions, de la pureté du module (pas de `print`, pas de chargement de données), des formules, des cas limites (série vide, premier close à 0), de l'alignement et des valeurs attendues. **Approve**, puis merge par le Lead.
- `main` local synchronisé, branche locale `feature/analytics` supprimée avec `git branch -d`.
- Résultat sur les données CSV : 21 séances alignées, AAPL +6.48 %, SP500 +2.15 %, performance relative +4.33 points, base 100 : 106.48 contre 102.15.

## TD08 – Yahoo Finance

- Rôle : Student 2, validation des lignes canoniques et de la récupération en direct.
- `yfinance` installé avec `python -m pip install -r requirements.txt` (version 1.8.0).
- Validation de `fetch_yahoo_prices` : 23 séances pour AAPL et pour SP500, 7 champs dans l'ordre du contrat, `date` en texte `YYYY-MM-DD`, tickers canoniques `AAPL` / `SP500` (jamais `^GSPC`), prix en `float`, volume en `int`, lignes triées par date, aucun `print` dans le provider.
- `src/analytics.py` non modifié par la branche : les fonctions du TD07 tournent telles quelles sur les données Yahoo (23 séances alignées).
- Problème signalé à l'équipe : avec `PROVIDER = "csv"`, `main.py` plante (`ValueError: Unknown format code 'f' for object of type 'str'`), car `:.2f` est appliqué à `close`, qui est une chaîne en CSV. Correction proposée : convertir avec `float(...)` avant le formatage.
