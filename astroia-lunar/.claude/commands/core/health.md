---
description: Vérifier la santé complète du système (API, DB, tests)
---

# Objectif

Effectuer un check-up complet du système : API running, DB connectée, tests passants. Diagnostic rapide de l'état du projet.

# Contexte à Charger

- `apps/api/main.py:1-30` — Point d'entrée API
- `apps/api/config.py:1-50` — Configuration (sans secrets)

# Rôle

Tu es un moniteur système. Tu vérifies chaque composant et rapportes l'état de santé global.

# Contraintes

- TOUJOURS : Vérifier les 3 composants (API, DB, Tests)
- JAMAIS : Afficher les secrets (ANTHROPIC_API_KEY, etc.)
- JAMAIS : Afficher les mots de passe ou tokens

# Workflow

1. **API Check** : `curl -s http://localhost:8000/health`
2. **DB Check** : Vérifier connexion Supabase
3. **Tests Check** : `cd apps/api && pytest -q --tb=no`
4. Synthèse de l'état global

# Résultat Attendu

```
=== Health Check ===

API:    ✓ Running (localhost:8000)
DB:     ✓ Connected (Supabase)
Tests:  ✓ 59/59 passed

Status: 🟢 All systems operational
```

Ou en cas de problème :

```
=== Health Check ===

API:    ✗ Not running
DB:     ✓ Connected
Tests:  ⚠ 57/59 passed (2 failed)

Status: 🔴 Issues detected
  - Start API: uvicorn main:app --reload --port 8000
  - Fix failing tests: test_lunar_cache, test_auth
```

# Exemples d'Utilisation

```
/health                  → Check complet (API + DB + Tests)
/health api              → Check API uniquement
/health db               → Check DB uniquement
/health tests            → Check tests uniquement
```

# v1.0 - 2026-01-25
