# Checkpoint A — Alban Murat (`alban-murat`)

## 1. Local Workflow, Refactoring & Branch Merge (TD01–TD04)
- **Repository & Environment:** `esilv-marketpulse-g02-t01` (GitHub Codespaces, Python 3.14, Linux CLI)
- **Archive Branch:** `archive/td04-local` (restored into `main` at commit `7b6fb29`)
- **Feature Branch:** `feature/display-observation-dates` -> merged into local `main`
- **Key Commits:**
  - `399d09d` — `refactor: reuse market summary display`
  - `fc427e1` — `feat: display first and last observation dates`
  - `025164d` — `docs: add TEAM.md and Checkpoint A evidence`
- **Contribution:** Configured `TEAM.md`, refactored `src/main.py` to avoid duplicated summary formatting logic, implemented first and last observation date display on a dedicated feature branch, and merged cleanly into local `main`.

## 2. Attached Screenshots
- `01_terminal_python.png` — Execution of `python src/main.py` displaying the MarketPulse summary, instrument/benchmark details, and observation date range.
- `02_git_status_log.png` — Clean working tree (`git status`) and structured local commit history (`git log`) showing incremental commits.
- `03_branch_merge.png` — Creation of `feature/display-observation-dates`, feature commit, and fast-forward/clean merge back into `main`.