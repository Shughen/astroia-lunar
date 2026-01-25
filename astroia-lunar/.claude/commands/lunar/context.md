---
description: Charger le contexte complet de l'architecture lunar (4 couches)
---

# Objectif

Charger rapidement tout le contexte nécessaire pour travailler sur le domaine lunar returns. Évite les scans globaux du repository.

# Contexte à Charger

- `apps/api/routes/lunar_returns.py` — Routes API lunar
- `apps/api/services/lunar_returns_service.py` — Service principal
- `apps/api/services/lunar_interpretation_generator.py` — Générateur IA
- `apps/api/models/lunar.py` — Modèles SQLAlchemy lunar
- `apps/api/docs/LUNAR_ARCHITECTURE_V2.md` — Documentation architecture

# Rôle

Tu es un développeur expert du domaine lunar. Après avoir chargé ce contexte, tu peux répondre à toute question sur l'architecture lunar sans scanner le repo.

# Architecture Lunar (Résumé)

```
┌─────────────────────────────────────────────────┐
│                    API Layer                     │
│         routes/lunar_returns.py                  │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│                 Service Layer                    │
│         services/lunar_returns_service.py        │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              Generator Layer                     │
│    services/lunar_interpretation_generator.py    │
│                                                  │
│    Fallback: DB Cache → Claude → Templates → HC │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│                 Data Layer                       │
│    models/lunar.py + LunarInterpretationTemplate │
└─────────────────────────────────────────────────┘
```

# Contraintes

- TOUJOURS : Charger les 5 fichiers listés
- JAMAIS : Scanner d'autres fichiers sauf demande explicite

# Résultat Attendu

Après `/lunar:context`, tu dois pouvoir :
- Expliquer le flux complet d'une requête lunar
- Identifier où ajouter une feature lunar
- Debugger sans relire le code

# Exemples d'Utilisation

```
/lunar:context              → Charger tout le contexte lunar
/lunar:context routes       → Focus sur les routes uniquement
/lunar:context generator    → Focus sur le générateur IA
```

# v1.0 - 2026-01-25
