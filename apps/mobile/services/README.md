# /services

API clients et intégrations externes.

## Fichiers

- `api.ts` - Client API principal (axios, auth, lunar returns, transits, etc.)
- `geocoding.ts` - Service de géocodage

## Règles

- Tous les appels API doivent passer par ce dossier
- Utiliser les types de `/types/api.ts`
- Gestion d'erreurs centralisée
- Logging et monitoring
