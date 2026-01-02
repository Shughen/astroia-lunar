/**
 * Helpers pour éviter les require cycles avec useOnboardingStore
 */

import { useOnboardingStore } from '../stores/useOnboardingStore';
import { type OnboardingState } from '../services/onboardingFlow';

/**
 * Mapper l'état du store vers le type OnboardingState attendu par onboardingFlow
 * Utilisé comme getter pour goToNextOnboardingStep sans créer de cycle de dépendance
 */
export const getOnboardingFlowState = (): OnboardingState => {
  const s = useOnboardingStore.getState();
  return {
    hasSeenWelcomeScreen: s.hasSeenWelcomeScreen,
    hasAcceptedConsent: s.hasAcceptedConsent,
    hasCompletedProfile: s.hasCompletedProfile,
    hasSeenDisclaimer: s.hasSeenDisclaimer,
    hasCompletedOnboarding: s.hasCompletedOnboarding,
  };
};
