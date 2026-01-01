# Architecture - Lunation Mobile App

## Vue d'ensemble

Application React Native (Expo) pour le suivi des révolutions lunaires et cycles menstruels.

## Structure du projet

```
apps/mobile/
├── app/                      # Expo Router - pages et routing
│   ├── _layout.tsx          # Root layout
│   ├── index.tsx            # Home (après auth/onboarding)
│   ├── welcome.tsx          # Premier écran one-time
│   ├── login.tsx            # Authentification
│   ├── onboarding/          # Flow onboarding complet
│   │   ├── _layout.tsx      # Nested stack pour onboarding
│   │   ├── index.tsx        # Slides de value proposition
│   │   ├── profile-setup.tsx # Prénom + date de naissance
│   │   ├── consent.tsx      # Consentement RGPD
│   │   ├── disclaimer.tsx   # Disclaimer médical
│   │   └── cycle-setup.tsx  # Setup cycle (optionnel)
│   ├── natal-chart.tsx      # Calcul thème natal
│   ├── lunar-returns/       # Révolutions lunaires
│   ├── cycle/               # Cycles menstruels
│   ├── transits/            # Transits planétaires
│   ├── calendar/            # Calendrier lunaire
│   └── settings/            # Paramètres
├── stores/                   # Zustand state management
│   ├── useAuthStore.ts      # Authentification
│   ├── useOnboardingStore.ts # État onboarding
│   ├── useNatalStore.ts     # Thème natal
│   └── useCycleStore.ts     # Cycles menstruels
├── services/                 # API clients
│   └── api.ts               # Axios client + endpoints
├── types/                    # TypeScript interfaces
│   ├── api.ts               # Types API responses
│   ├── stores.ts            # Types stores Zustand
│   └── storage.ts           # Constantes AsyncStorage
├── utils/                    # Fonctions utilitaires pures
│   ├── date.ts              # Formatage dates
│   └── astrology-format.ts  # Formatage données astro
├── lib/                      # Configuration et helpers
│   ├── config.ts            # Configuration app
│   ├── dev.ts               # Helpers dev (DEV_AUTH_BYPASS)
│   └── device.ts            # Info device
└── constants/                # Constantes
    └── theme.ts             # Colors, fonts, spacing
```

## Principes architecturaux

### 1. **Séparation des responsabilités**
- **app/**: Routing et UI components (Expo Router)
- **stores/**: State management (Zustand + AsyncStorage)
- **services/**: Communication API (Axios)
- **utils/**: Fonctions pures sans side-effects
- **lib/**: Configuration et helpers métier
- **types/**: Interfaces TypeScript centralisées

### 2. **State Management**
- **Zustand** pour la gestion d'état global
- **AsyncStorage** pour la persistance locale
- Pattern: `hydrate()` au mount pour charger depuis AsyncStorage

### 3. **Routing**
- **Expo Router** (file-based routing)
- Guards dans `app/index.tsx` vérifient:
  1. Authentification
  2. Welcome screen vu
  3. Profil complété
  4. Consentement accepté
  5. Disclaimer vu
  6. Onboarding complété

### 4. **API Communication**
- Axios client centralisé dans `services/api.ts`
- Interceptors pour authentification (token)
- Types TypeScript pour toutes les responses
- Gestion d'erreurs standardisée

### 5. **TypeScript Strict**
- Toutes les fonctions typées
- Interfaces centralisées dans `/types`
- Pas de `any` sauf dans la gestion d'erreurs API

## Flow Onboarding

```mermaid
graph TD
    A[App Start] --> B{Auth?}
    B -->|Non auth| C[/login]
    B -->|Auth OK| D{Welcome vu?}
    D -->|Non| E[/welcome]
    D -->|Oui| F{DEV_AUTH_BYPASS?}
    F -->|Oui| Z[Home]
    F -->|Non| G{Profil complété?}
    G -->|Non| H[/onboarding/profile-setup]
    G -->|Oui| I{Consent?}
    H --> I
    I -->|Non| J[/onboarding/consent]
    I -->|Oui| K{Disclaimer?}
    J --> K
    K -->|Non| L[/onboarding/disclaimer]
    K -->|Oui| M{Onboarding slides?}
    L --> N[/onboarding/cycle-setup]
    N --> M
    M -->|Non| O[/onboarding]
    M -->|Oui| Z[Home]
    E --> D
```

## Stores Zustand

### useOnboardingStore
```typescript
interface OnboardingState {
  hasSeenWelcomeScreen: boolean;
  hasCompletedProfile: boolean;
  hasAcceptedConsent: boolean;
  hasSeenDisclaimer: boolean;
  hasCompletedOnboarding: boolean;
  profileData: ProfileData | null;

  setWelcomeSeen: () => Promise<void>;
  setProfileData: (data) => Promise<void>;
  setConsentAccepted: () => Promise<void>;
  setDisclaimerSeen: () => Promise<void>;
  completeOnboarding: () => Promise<void>;
  reset: () => Promise<void>;
  hydrate: () => Promise<void>;
}
```

## Conventions de code

### 1. **Imports**
```typescript
// 1. React/React Native
import React from 'react';
import { View, Text } from 'react-native';

// 2. Expo
import { useRouter } from 'expo-router';

// 3. Stores
import { useOnboardingStore } from '../stores/useOnboardingStore';

// 4. Services
import { lunarReturns } from '../services/api';

// 5. Utils
import { formatDate } from '../utils/date';

// 6. Constants
import { colors, fonts } from '../constants/theme';
```

### 2. **Naming**
- **Components**: PascalCase (e.g., `ProfileSetupScreen`)
- **Files**: kebab-case (e.g., `profile-setup.tsx`)
- **Functions**: camelCase (e.g., `formatDate`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `STORAGE_KEYS`)
- **Stores**: `use[Name]Store` (e.g., `useOnboardingStore`)

### 3. **Console Logs**
Format: `[COMPONENT] Message`
```typescript
console.log('[PROFILE-SETUP] Profil sauvegardé →', data);
```

## Testing

### Test Structure
```
__tests__/
├── setup.test.ts            # Sanity check
├── api.test.ts              # API authentication
├── date.test.ts             # Date utilities (11 tests)
└── astrology-format.test.ts # Astrology formatting (12 tests)
```

### Run Tests
```bash
npm run test        # Jest tests
npm run typecheck   # TypeScript compilation
npm run check       # Both
```

## Dev Tools

### DEV_AUTH_BYPASS
Variable d'environnement pour skip authentication en dev:
```bash
EXPO_PUBLIC_DEV_AUTH_BYPASS=true
EXPO_PUBLIC_DEV_USER_ID=1
```

Guards s'arrêtent après welcome screen quand activé.

## Priorités Produit

1. **Révolutions Lunaires** (feature principale)
   - Timeline des 12 prochains retours
   - Interprétations détaillées
   - Aspects et positions

2. **Cycles Menstruels** (feature secondaire)
   - Optionnel dans onboarding
   - Corrélation avec phases lunaires
   - Peut être skippé

## Prochaines étapes

- [ ] Tests E2E du flow complet
- [ ] Documentation API endpoints
- [ ] Optimisation performance
- [ ] Internationalisation (i18n)
