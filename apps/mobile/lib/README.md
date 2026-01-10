# /lib

Domain logic, business rules, et configuration centralisée.

## Structure

- `/config.ts` - Configuration centralisée (API endpoints, feature flags)
- `/dev.ts` - Helpers pour mode développement (DEV_AUTH_BYPASS)
- `/lunar/` - Logique métier liée aux révolutions lunaires (à venir)
- `/astrology/` - Helpers astrologiques (calculs, conversions) (à venir)

## Règles

- Pas de dépendance aux composants React Native
- Fonctions pures autant que possible
- Exportations claires et documentées
