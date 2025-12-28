# Onboarding Flow - Astroia Lunar

## Vue d'ensemble

Le flow d'onboarding guide l'utilisateur à travers 6 étapes avant d'accéder à l'application principale.

## Étapes du Flow

### 1. Welcome Screen (`/welcome`)
**Fichier**: `app/welcome.tsx`

- **Objectif**: Premier écran one-time, présentation rapide
- **Contenu**:
  - Emoji 🌙
  - "Bienvenue sur Astroia Lunar"
  - Bouton "Continuer"
- **Action**:
  ```typescript
  await setWelcomeSeen();
  router.replace('/');
  ```
- **Store**: `hasSeenWelcomeScreen = true`

### 2. Profile Setup (`/onboarding/profile-setup`)
**Fichier**: `app/onboarding/profile-setup.tsx`
**Étape**: 1/4

- **Objectif**: Collecter prénom + date de naissance
- **Champs**:
  - Prénom (TextInput)
  - Date de naissance (Date picker simplifié)
- **Validation**: Prénom requis
- **Action**:
  ```typescript
  await setProfileData({ name, birthDate });
  router.push('/onboarding/consent');
  ```
- **Store**:
  ```typescript
  hasCompletedProfile = true
  profileData = { name, birthDate }
  ```

### 3. Consent RGPD (`/onboarding/consent`)
**Fichier**: `app/onboarding/consent.tsx`
**Étape**: 2/4

- **Objectif**: Obtenir consentement RGPD
- **Contenu**:
  - Explication utilisation données
  - Politique de confidentialité
  - Checkbox "J'accepte"
- **Validation**: Checkbox doit être cochée
- **Action**:
  ```typescript
  await setConsentAccepted();
  router.push('/onboarding/disclaimer');
  ```
- **Store**: `hasAcceptedConsent = true`

### 4. Disclaimer Médical (`/onboarding/disclaimer`)
**Fichier**: `app/onboarding/disclaimer.tsx`
**Étape**: 3/4

- **Objectif**: Disclaimer médical/bien-être
- **Contenu**:
  - Clarification: astrologie ≠ conseil médical
  - Checkbox "J'ai lu et compris"
- **Validation**: Checkbox doit être cochée
- **Action**:
  ```typescript
  await setDisclaimerSeen();
  router.push('/onboarding/cycle-setup');
  ```
- **Store**: `hasSeenDisclaimer = true`

### 5. Cycle Setup (Optionnel) (`/onboarding/cycle-setup`)
**Fichier**: `app/onboarding/cycle-setup.tsx`
**Étape**: 4/4

- **Objectif**: Setup cycle menstruel (optionnel)
- **Contenu**:
  - Explication: Révolutions Lunaires = prioritaire
  - Cycles menstruels = secondaire
  - Bouton "Passer cette étape"
  - Bouton "Configurer mon cycle"
- **Actions**:
  ```typescript
  // Skip
  router.push('/onboarding'); // → slides

  // Configure (TODO: implement)
  // Pour l'instant, même chose que skip
  router.push('/onboarding');
  ```
- **Store**: Aucun changement (feature secondaire)

### 6. Value Proposition Slides (`/onboarding`)
**Fichier**: `app/onboarding/index.tsx`
**Dernière étape**

- **Objectif**: Présenter les 4 valeurs clés d'Astroia Lunar
- **Slides**:
  1. 🌙 Bienvenue - Révolutions Lunaires
  2. ⭐ Thème natal précis
  3. 🌙 Révolutions lunaires mensuelles
  4. 🔮 Transits et influences
- **Navigation**:
  - Bouton "Suivant" entre slides
  - Animation fade
  - Bouton "Passer" toujours visible
- **Action** (dernier slide):
  ```typescript
  await completeOnboarding();
  router.replace('/');
  ```
- **Store**: `hasCompletedOnboarding = true`

## Routing Guards (`app/index.tsx`)

```typescript
// A) Vérifier auth (sauf si DEV_AUTH_BYPASS)
if (!isBypassActive && !isAuthenticated) {
  router.replace('/login');
  return;
}

// B) Vérifier welcome screen
if (!onboardingStore.hasSeenWelcomeScreen) {
  router.replace('/welcome');
  return;
}

// Mode DEV_AUTH_BYPASS: arrêter ici
if (isBypassActive) {
  // Accès direct home après welcome
  return;
}

// C) Vérifier profil
if (!onboardingStore.hasCompletedProfile) {
  router.replace('/onboarding/profile-setup');
  return;
}

// D) Vérifier consentement
if (!onboardingStore.hasAcceptedConsent) {
  router.replace('/onboarding/consent');
  return;
}

// E) Vérifier disclaimer
if (!onboardingStore.hasSeenDisclaimer) {
  router.replace('/onboarding/disclaimer');
  return;
}

// F) Vérifier onboarding slides
if (!onboardingStore.hasCompletedOnboarding) {
  router.replace('/onboarding');
  return;
}

// Afficher Home
```

## État Persisté (AsyncStorage)

| Clé | Type | Valeur |
|-----|------|--------|
| `hasSeenWelcomeScreen` | `string` | `"true"` |
| `onboarding_profile` | `JSON` | `{ name, birthDate }` |
| `onboarding_consent` | `string` | `"true"` |
| `onboarding_disclaimer` | `string` | `"true"` |
| `onboarding_completed` | `string` | `"true"` |

## Reset Onboarding

Pour tester le flow complet:

```typescript
import { useOnboardingStore } from './stores/useOnboardingStore';

const { reset } = useOnboardingStore();
await reset();
```

Ou via AsyncStorage:
```typescript
import AsyncStorage from '@react-native-async-storage/async-storage';

await AsyncStorage.multiRemove([
  'hasSeenWelcomeScreen',
  'onboarding_profile',
  'onboarding_consent',
  'onboarding_disclaimer',
  'onboarding_completed',
]);
```

## Adaptation pour Astroia Lunar

Le flow a été adapté depuis `astroia-app` avec les changements suivants:

### Modifications de contenu
- **Priorité**: Révolutions Lunaires (pas parentalité)
- **Secondaire**: Cycles menstruels (optionnel)
- **Slides**: Adapté pour focus lunar returns
- **Cycle Setup**: Skippable, mention claire que c'est secondaire

### Modifications techniques
- Utilisation de `useOnboardingStore` (Zustand)
- Routing guards refactorés
- Nested Stack pour `/onboarding/*`
- Suppression ancien `/app/onboarding.tsx`

## Diagramme de flux

```
┌─────────────┐
│ App Start   │
└─────┬───────┘
      │
      v
┌─────────────────┐
│ Auth Check      │──No──> /login
└─────┬───────────┘
      │ Yes
      v
┌─────────────────────────┐
│ hasSeenWelcomeScreen?   │──No──> /welcome
└─────┬───────────────────┘
      │ Yes
      v
┌─────────────────────────┐
│ DEV_AUTH_BYPASS?        │──Yes──> Home (skip onboarding)
└─────┬───────────────────┘
      │ No
      v
┌─────────────────────────┐
│ hasCompletedProfile?    │──No──> /onboarding/profile-setup
└─────┬───────────────────┘
      │ Yes
      v
┌─────────────────────────┐
│ hasAcceptedConsent?     │──No──> /onboarding/consent
└─────┬───────────────────┘
      │ Yes
      v
┌─────────────────────────┐
│ hasSeenDisclaimer?      │──No──> /onboarding/disclaimer
└─────┬───────────────────┘
      │ Yes
      v
┌─────────────────────────┐
│                         │
│ /onboarding/cycle-setup │ (Optionnel, peut skip)
│                         │
└─────┬───────────────────┘
      │
      v
┌─────────────────────────┐
│ hasCompletedOnboarding? │──No──> /onboarding (slides)
└─────┬───────────────────┘
      │ Yes
      v
┌─────────────┐
│    Home     │
└─────────────┘
```

## Tests

### Test manuel du flow
1. Reset onboarding state
2. Relancer l'app
3. Vérifier redirection vers `/welcome`
4. Compléter chaque étape
5. Vérifier redirection correcte à chaque étape
6. Vérifier state persisté dans AsyncStorage

### Points de contrôle
- [ ] Welcome screen affiché une seule fois
- [ ] Profile setup validation fonctionne
- [ ] Consent checkbox requis
- [ ] Disclaimer checkbox requis
- [ ] Cycle setup skippable
- [ ] Slides navigation fluide
- [ ] Redirection vers home après dernier slide
- [ ] DEV_AUTH_BYPASS skip onboarding après welcome
