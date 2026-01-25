---
description: Charger le contexte complet de l'architecture natal charts
---

# Objectif

Charger rapidement tout le contexte nécessaire pour travailler sur le domaine natal charts. Permet de comprendre l'architecture sans scanner le repo.

# Contexte à Charger

- `apps/api/routes/natal.py` — Routes API natal
- `apps/api/services/natal_chart_service.py` — Service principal
- `apps/api/services/rapidapi_client.py` — Client calculs astro
- `apps/api/models/natal.py` — Modèles de données

# Rôle

Tu es un développeur expert du domaine natal. Après ce contexte, tu peux répondre à toute question sur l'architecture natal.

# Architecture Natal (Résumé)

```
┌─────────────────────────────────────────────────┐
│                    API Layer                     │
│              routes/natal.py                     │
│                                                  │
│  POST /natal/chart    → Créer natal chart        │
│  GET  /natal/chart    → Récupérer chart user     │
│  GET  /natal/aspects  → Calculer aspects         │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│                 Service Layer                    │
│          natal_chart_service.py                  │
│                                                  │
│  - Validation input (date, coords)               │
│  - Orchestration calculs                         │
│  - Transformation données                        │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              External API Layer                  │
│            rapidapi_client.py                    │
│                                                  │
│  - Calculs positions planétaires                 │
│  - Calculs maisons                               │
│  - Calculs aspects                               │
└─────────────────────────────────────────────────┘
```

# Données Natal Chart

- **Positions** : Soleil, Lune, planètes (longitude, signe, degré)
- **Maisons** : 12 maisons (cuspides, signes)
- **Aspects** : Conjonctions, oppositions, trigones, etc.

# Contraintes

- TOUJOURS : Charger les 4 fichiers listés
- JAMAIS : Scanner d'autres fichiers sauf demande

# Exemples d'Utilisation

```
/natal:context              → Charger tout le contexte natal
/natal:context routes       → Focus routes API
/natal:context service      → Focus service calculs
```

# v1.0 - 2026-01-25
