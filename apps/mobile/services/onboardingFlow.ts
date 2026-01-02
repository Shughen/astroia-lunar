/**
 * Onboarding Flow Service
 *
 * Centralizes all onboarding routing logic to ensure sequential progression
 * and prevent rebounding or skipped steps.
 *
 * Flow:
 * /welcome → /onboarding/consent → /onboarding/profile-setup → /onboarding/disclaimer → /onboarding (slides) → / (Home)
 *
 * NOTE: This file does NOT import useOnboardingStore to avoid require cycles.
 * State is passed via a getter function parameter.
 */

import { Router } from 'expo-router';

/**
 * OnboardingState type
 * Represents the minimal state needed to determine next onboarding step
 */
export type OnboardingState = {
  hasSeenWelcomeScreen: boolean;
  hasAcceptedConsent: boolean;
  hasCompletedProfile: boolean;
  hasSeenDisclaimer: boolean;
  hasCompletedOnboarding: boolean;
};

/**
 * Pure function that calculates the next onboarding step based on state
 *
 * @param state - Current onboarding state
 * @returns Next route to navigate to
 */
export function getNextOnboardingStep(state: OnboardingState): string {
  // Sequential guards - first incomplete step determines next route
  if (!state.hasSeenWelcomeScreen) {
    return '/welcome';
  }
  if (!state.hasAcceptedConsent) {
    return '/onboarding/consent';
  }
  if (!state.hasCompletedProfile) {
    return '/onboarding/profile-setup';
  }
  if (!state.hasSeenDisclaimer) {
    return '/onboarding/disclaimer';
  }
  if (!state.hasCompletedOnboarding) {
    return '/onboarding'; // Slides
  }

  // All steps completed → Home
  return '/';
}

/**
 * Helper function that navigates to the next onboarding step with logging
 *
 * IMPORTANT: Receives a state getter to avoid circular dependencies with useOnboardingStore.
 * The getter ensures fresh state is read at navigation time.
 *
 * @param router - Expo router instance
 * @param sourceTag - Source identifier for logging (e.g., 'WELCOME', 'CONSENT')
 * @param getState - Function that returns fresh onboarding state (e.g., useOnboardingStore.getState)
 */
export async function goToNextOnboardingStep(
  router: Router,
  sourceTag: string,
  getState: () => OnboardingState
): Promise<void> {
  // Read FRESH state via the getter function
  // This ensures we get the most up-to-date state after async operations like setProfileData()
  const state = getState();

  const nextStep = getNextOnboardingStep(state);

  // Single comprehensive log line
  console.log(
    `[ONBOARDING_FLOW] from=${sourceTag} nextStep=${nextStep} state={` +
    `welcome=${state.hasSeenWelcomeScreen}, ` +
    `consent=${state.hasAcceptedConsent}, ` +
    `profile=${state.hasCompletedProfile}, ` +
    `disclaimer=${state.hasSeenDisclaimer}, ` +
    `completed=${state.hasCompletedOnboarding}}`
  );

  // Navigate to next step using replace (not push) to avoid back-stack issues
  router.replace(nextStep as any);
}
