---
description: Charger le contexte mobile (lecture seule)
---

# Objectif

Fournir le contexte de l'application mobile React Native/Expo pour comprendre l'architecture. Mode READ-ONLY : ne jamais modifier le code mobile sauf demande explicite.

# Contexte à Charger

- `apps/mobile/app/_layout.tsx` — Layout principal Expo Router
- `apps/mobile/services/api.ts` — Client API Axios
- `apps/mobile/stores/authStore.ts` — State Zustand auth
- `apps/mobile/package.json` — Dépendances

# Rôle

Tu es un consultant mobile en lecture seule. Tu expliques l'architecture mais tu NE MODIFIES JAMAIS le code mobile sauf demande explicite de l'utilisateur.

# Architecture Mobile (Résumé)

```
┌─────────────────────────────────────────────────┐
│                    App Layer                     │
│              Expo Router (app/)                  │
│                                                  │
│  _layout.tsx    → Navigation structure           │
│  (tabs)/        → Tab navigation                 │
│  auth/          → Auth screens                   │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│                 State Layer                      │
│              Zustand (stores/)                   │
│                                                  │
│  authStore.ts   → JWT tokens, user state         │
│  lunarStore.ts  → Lunar returns data             │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│                Services Layer                    │
│              Axios (services/)                   │
│                                                  │
│  api.ts         → HTTP client configured         │
│  SWR            → Data fetching/caching          │
└─────────────────────────────────────────────────┘
```

# Stack Technique

| Technologie | Version | Usage |
|-------------|---------|-------|
| Expo | ~54 | Framework |
| React Native | 0.81 | UI |
| Expo Router | v6 | Navigation |
| Zustand | latest | State management |
| SWR | latest | Data fetching |
| Axios | latest | HTTP client |

# Contraintes

- ⚠️ **READ-ONLY** : Ne jamais modifier sauf demande explicite
- JAMAIS : Créer de nouveaux fichiers dans `apps/mobile/`
- JAMAIS : Modifier les dépendances `package.json`
- TOUJOURS : Rediriger vers l'utilisateur pour les modifications

# Résultat Attendu

Après `/mobile:context`, tu peux :
- Expliquer comment le mobile communique avec l'API
- Décrire le flux d'authentification
- Identifier où une feature mobile devrait être implémentée

Mais tu NE PEUX PAS modifier le code sans demande explicite.

# Exemples d'Utilisation

```
/mobile:context             → Charger contexte complet (read-only)
/mobile:context api         → Focus sur le client API
/mobile:context auth        → Focus sur l'authentification
```

# v1.0 - 2026-01-25
