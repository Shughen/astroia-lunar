# /app

Routes Expo Router.

## Structure actuelle

- `_layout.tsx` - Root layout (Stack)
- `index.tsx` - Home + routing guards
- `welcome.tsx` - Welcome screen
- `onboarding.tsx` - Onboarding slides (sera remplacé par `/onboarding/*` en Phase B)
- `login.tsx` - Login
- `natal-chart.tsx` - Thème natal
- `/lunar-returns/` - Révolutions lunaires
- `/transits/` - Transits
- `/calendar/` - Calendrier
- `/cycle/` - Cycles menstruels
- `/settings/` - Réglages
- `/debug/` - Debug/selftest

## Règles

- Pages uniquement (pas de logique métier)
- Routing guards dans `index.tsx`
- Utiliser les stores pour l'état
- Déléguer UI complexe aux composants
