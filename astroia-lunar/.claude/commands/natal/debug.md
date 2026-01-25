---
description: Debugger les natal charts et calculs astrologiques
---

# Objectif

Diagnostiquer les problèmes liés aux natal charts : calculs RapidAPI, stockage, affichage des positions planétaires.

# Contexte à Charger

- `apps/api/routes/natal.py` — Routes natal chart
- `apps/api/services/natal_chart_service.py` — Service calculs natal
- `apps/api/services/rapidapi_client.py` — Client RapidAPI (calculs astro)
- `apps/api/models/natal.py` — Modèles SQLAlchemy natal

# Rôle

Tu es un expert debugging natal charts. Tu comprends les calculs astrologiques (positions planétaires, maisons, aspects) et l'intégration RapidAPI.

# Architecture Natal

```
User Request → routes/natal.py
                    │
                    ▼
           natal_chart_service.py
                    │
                    ▼
           rapidapi_client.py ──→ RapidAPI (calculs)
                    │
                    ▼
              models/natal.py (stockage)
```

# Contraintes

- JAMAIS : Afficher RAPIDAPI_KEY
- TOUJOURS : Vérifier format date/heure (timezone)
- TOUJOURS : Valider coordonnées géo (lat/lon)

# Points de Debug

| Symptôme | Cause probable | Solution |
|----------|----------------|----------|
| 500 error | RapidAPI down | Vérifier status RapidAPI |
| Positions fausses | Timezone incorrecte | Valider UTC conversion |
| Pas de réponse | API key expirée | Vérifier RAPIDAPI_KEY |
| Données incomplètes | Parsing erreur | Checker response format |

# Workflow

1. **Vérifier input** : date, heure, lieu (lat/lon)
2. **Tester RapidAPI** : Appel direct avec logs
3. **Valider output** : Positions cohérentes
4. **Checker stockage** : Données en DB

# Exemples d'Utilisation

```
/natal:debug                → Diagnostic général natal
/natal:debug api            → Focus sur RapidAPI
/natal:debug positions      → Vérifier calculs planétaires
/natal:debug storage        → Investiguer stockage DB
```

# v1.0 - 2026-01-25
