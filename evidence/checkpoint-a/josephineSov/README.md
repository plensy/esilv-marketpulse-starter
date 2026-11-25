# Checkpoint A – josephineSov

- Étudiante : Joséphine Sauvé (@josephineSov)
- Groupe / équipe : G02 – T01
- Dépôt : `esilv-marketpulse-g02-t01`
- Branche de travail : `josephineSauve`

## Preuves

| Fichier | Contenu |
|---|---|
| `01_terminal_python.png` | `python --version`, `git --version` et `python src/main.py` lancés depuis la racine du dépôt |
| `02_git_status_log.png` | `git status` (working tree propre) et `git log --oneline` montrant mes commits |
| `03_branch_merge.png` | `git branch`, `git branch --merged` et `git log --oneline --graph --decorate --all` après le merge, avant suppression de la branche feature |
| `historique.txt` | historique Git de la branche `josephineSauve` (graphe, correspondance avec les TD, détail de chaque commit) |

## Travail réalisé

- **TD01** : exploration du dépôt avec `pwd`, `ls`, `cd`, `cat`, `head`, `grep`. Inspection de `instruments.json` (AAPL / SP500) et de `prices.csv` (21 observations par série). `TEAM.md` complété.
- **TD02** : `get_first_close`, `get_last_close` (conversion `float`) et une fonction réutilisable `display_market_summary` appelée pour l'instrument et pour le benchmark.
- **TD03** : commit du travail du TD02 après `git status`, `git diff`, `git add src/main.py` et `git diff --staged` : `refactor: reuse market summary display`.
- **TD04** : branche `feature/display-observation-dates`, commit `feat: display first and last observation dates`, comparaison avec `git diff`, puis merge en **fast-forward** (historique linéaire, pas de commit de merge).

## Sortie finale de MarketPulse

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First date   : 2026-09-01
Last date    : 2026-09-30
First close  : 250.00 USD
Last close   : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First date   : 2026-09-01
Last date    : 2026-09-30
First close  : 6600.00
Last close   : 6742.00
```
