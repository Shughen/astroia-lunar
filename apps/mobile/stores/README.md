# /stores

Zustand stores pour state management.

## Fichiers actuels

- `useAuthStore.ts` - Authentification
- `useNatalStore.ts` - Thème natal
- `useCycleStore.ts` - Cycle menstruel
- `useCalendarStore.ts` - Calendrier lunaire
- `useVocStore.ts` - Void of Course

## Fichiers à ajouter (Phase B)

- `useOnboardingStore.ts` - État onboarding (hasSeenWelcome, completed, etc.)

## Règles

- Un store par domaine fonctionnel
- Utiliser les types de `/types/stores.ts`
- Synchroniser avec AsyncStorage si nécessaire
- Actions asynchrones avec try/catch
