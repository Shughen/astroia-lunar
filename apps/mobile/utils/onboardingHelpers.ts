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

/**
 * Type ProfileData pour la fonction utilitaire (copié depuis useOnboardingStore)
 */
export interface ProfileData {
  name?: string;
  birthDate?: Date;
  birthTime?: string; // Format HH:MM
  birthPlace?: string; // Ex: "Paris, France"
  birthLatitude?: number;
  birthLongitude?: number;
}

/**
 * Type minimal pour isProfileComplete() - accepte unknown pour éviter erreurs de typage strict
 */
type MinimalProfileData = {
  birthDate?: unknown;
  birthTime?: unknown;
  birthPlace?: unknown;
  birthLatitude?: unknown;
  birthLongitude?: unknown;
};

/**
 * Vérifie si un profil est complet avec tous les champs critiques requis
 * Critères minimaux:
 * - birthDate présente (Date valide ou string non vide)
 * - birthTime présente (string non vide)
 * - birthPlace présente (string non vide)
 * - birthLatitude et birthLongitude valides (numbers finis, pas NaN)
 * 
 * @param profileData - Les données de profil à vérifier
 * @returns true si le profil est complet, false sinon
 */
export function isProfileComplete(profileData: MinimalProfileData | null | undefined): boolean {
  // Profil null ou undefined = incomplet
  if (!profileData) {
    return false;
  }

  // Vérifier birthDate (peut être Date ou string ISO)
  const birthDate = profileData.birthDate;
  if (!birthDate) {
    return false;
  }
  
  // Si c'est une Date, vérifier qu'elle est valide
  if (birthDate instanceof Date) {
    if (isNaN(birthDate.getTime())) {
      return false;
    }
  } else if (typeof birthDate === 'string') {
    if (birthDate.trim().length === 0) {
      return false;
    }
  } else {
    return false;
  }

  // Vérifier birthTime (string HH:MM requis)
  const birthTime = profileData.birthTime;
  if (typeof birthTime !== 'string' || birthTime.trim().length === 0) {
    return false;
  }

  // Vérifier birthPlace (string non vide)
  const birthPlace = profileData.birthPlace;
  if (typeof birthPlace !== 'string' || birthPlace.trim().length === 0) {
    return false;
  }

  // Vérifier latitude et longitude (numbers finis, pas NaN)
  const birthLatitude = profileData.birthLatitude;
  const birthLongitude = profileData.birthLongitude;
  if (
    typeof birthLatitude !== 'number' ||
    !Number.isFinite(birthLatitude) ||
    typeof birthLongitude !== 'number' ||
    !Number.isFinite(birthLongitude)
  ) {
    return false;
  }

  return true;
}
