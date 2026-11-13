# Checkpoint A de Baptiste JULIE

Identifiant GitHub : batj1509-cloud

## Travail réalisé au TD04

Le 13 novembre 2026, la branche locale main a été avancée sur le travail du TD03 par une fusion fast-forward de Baptiste. Le dossier de travail était propre avant la création de feature/display-observation-dates.

Le commit 2072690 ajoute get_first_date et get_last_date dans src/main.py et affiche les dates dans le résumé commun à AAPL et SP500. Le diff a été inspecté avant et après sélection. La branche a été comparée à main, puis fusionnée dans main en fast-forward. Le programme a été exécuté avec succès avant et après la fusion.

Résultats : 21 observations pour chaque série, du 2026-09-01 au 2026-09-30. AAPL : 250.00 à 266.20 USD. SP500 : 6600.00 à 6742.00.

## Captures enregistrées

Les trois captures originales prises dans le terminal VS Code sont présentes dans ce dossier.

- 01_terminal_python.png : exécution de python src/main.py.
- 02_git_status_log.png : git status et git log --oneline -5.
- 03_branch_merge.png : git branch, git branch --merged et git log --oneline --graph --decorate --all.

La branche feature/display-observation-dates est conservée après capture de la preuve de fusion. Elle ne doit être supprimée qu’après validation de l’enseignant. Dans la deuxième capture, le fichier non suivi est la première image ajoutée au dossier ; les preuves sont ensuite enregistrées dans un commit documentaire.

Le fichier docs/04_CHECKPOINTS_AND_EVIDENCE.md référencé par le TD04 n’est pas présent dans cette copie du dépôt ; cette liste reprend les noms et le dossier demandés dans labs/TD04_BRANCHES_AND_MERGE.md.

## Concepts à expliquer

Une branche permet d’enregistrer une évolution séparément de main. Avant fusion, le commit de la fonctionnalité n’appartenait qu’à la branche feature. Abandonner cette branche sans la fusionner aurait laissé main inchangée.

La comparaison git diff main..feature/display-observation-dates montrait les deux fonctions et les deux lignes d’affichage ajoutées. Après fusion, main contient le même commit. Le fast-forward déplace le pointeur main sur ce commit sans créer de commit de fusion supplémentaire.

Un conflit survient lorsque Git ne peut pas combiner automatiquement des modifications concurrentes. Il faut lire les deux versions, choisir le contenu final, retirer les marqueurs de conflit, sélectionner les fichiers résolus et terminer la fusion. Aucun conflit n’est survenu ici ; provoquer un conflit est facultatif.

Le main distant de l’équipe n’a pas été modifié. La sélection et la publication d’une base commune sont prévues au début du TD05.
