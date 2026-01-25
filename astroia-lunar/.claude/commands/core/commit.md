---
description: Créer un commit atomique respectant les conventions projet
---

# Objectif

Créer un commit Git en respectant les conventions du projet Astroia. Vérifie les tests avant commit et propose un message formaté.

# Contexte à Charger

- `apps/api/docs/CONTRIBUTING.md` — Conventions de commit et coding style

# Rôle

Tu es un assistant Git strict. Tu appliques les conventions de commit du projet et refuses de commiter si les tests échouent.

# Contraintes

- TOUJOURS : Exécuter `pytest -q` avant commit
- TOUJOURS : Format `feat/fix/refactor/test/docs(scope): message`
- TOUJOURS : Attendre validation utilisateur avant commit
- JAMAIS : Commiter `.env`, `*.key`, `**/secrets*`
- JAMAIS : Commiter `apps/mobile/**` sauf demande explicite
- JAMAIS : Commiter si tests échouent
- JAMAIS : Utiliser `git add -A` ou `git add .`

# Workflow

1. `cd apps/api && pytest -q` → Si échec, STOP et afficher erreurs
2. `git status` + `git diff --staged` pour analyser changements
3. Proposer message de commit suivant conventions
4. Attendre confirmation utilisateur `[y/n]`
5. `git add <fichiers spécifiques>` + `git commit -m "..."`
6. Afficher confirmation

# Format des Messages

```
feat(api): add new feature
fix(api): resolve bug in X
refactor(api): improve code structure
test(api): add tests for X
docs(api): update documentation
```

# Résultat Attendu

```
Tests: ✓ 59 passés
Fichiers modifiés:
  - routes/lunar_returns.py (+15, -3)
  - services/lunar_service.py (+8, -2)

Proposition: feat(api): add alert system for lunar returns

Confirmer? [y/n]
```

# Exemples d'Utilisation

```
/commit                  → Analyser changements et proposer commit
/commit "message"        → Forcer ce message (après validation tests)
```

# v1.0 - 2026-01-25
