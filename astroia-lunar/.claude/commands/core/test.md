---
description: Lancer les tests pytest avec contexte minimal
---

# Objectif

Exécuter les tests backend rapidement sans scanner tout le repository. Fournit un feedback rapide sur l'état des tests.

# Contexte à Charger

- `apps/api/conftest.py` — Fixtures pytest partagées
- `apps/api/pytest.ini` — Configuration pytest

# Rôle

Tu es un runner de tests efficace. Tu exécutes les tests et rapportes les résultats de manière concise.

# Contraintes

- TOUJOURS : Exécuter depuis `apps/api`
- TOUJOURS : Utiliser `pytest -q` par défaut (mode rapide)
- JAMAIS : Modifier les fichiers de test
- JAMAIS : Scanner tout le repository

# Workflow

1. `cd apps/api && pytest -q` (mode rapide par défaut)
2. Si argument fourni : `pytest tests/test_<arg>.py -v`
3. Si flag `-v` : mode verbose
4. Rapporter : nombre tests passés/échoués avec résumé

# Résultat Attendu

```
✓ 59 tests passés
✗ 2 tests échoués :
  - test_lunar_cache.py::test_cache_hit
  - test_auth.py::test_invalid_token
```

# Exemples d'Utilisation

```
/test                    → pytest -q (tous les tests, mode rapide)
/test lunar              → pytest tests/test_lunar*.py -v
/test -v                 → pytest -v (tous les tests, verbose)
/test auth               → pytest tests/test_auth*.py -v
```

# v1.0 - 2026-01-25
