/**
 * Store Zustand pour l'onboarding
 * Gère le flow complet : welcome, profile, consent, disclaimer, cycle, slides
 */

import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { STORAGE_KEYS } from '../types/storage';

interface ProfileData {
  name?: string;
  birthDate?: Date;
}

interface OnboardingState {
  // État de progression
  hasSeenWelcomeScreen: boolean;
  hasCompletedProfile: boolean;
  hasAcceptedConsent: boolean;
  hasSeenDisclaimer: boolean;
  hasCompletedOnboarding: boolean;

  // Données temporaires
  profileData: ProfileData | null;

  // Flag d'hydratation (pour forcer re-check routing après reset)
  hydrated: boolean;

  // Actions
  setWelcomeSeen: () => Promise<void>;
  setProfileData: (data: ProfileData) => Promise<void>;
  setConsentAccepted: () => Promise<void>;
  setDisclaimerSeen: () => Promise<void>;
  completeOnboarding: () => Promise<void>;
  reset: () => Promise<void>;

  // Initialisation depuis AsyncStorage
  hydrate: () => Promise<void>;
}

export const useOnboardingStore = create<OnboardingState>((set, get) => ({
  // État initial
  hasSeenWelcomeScreen: false,
  hasCompletedProfile: false,
  hasAcceptedConsent: false,
  hasSeenDisclaimer: false,
  hasCompletedOnboarding: false,
  profileData: null,
  hydrated: false,

  setWelcomeSeen: async () => {
    await AsyncStorage.setItem(STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN, 'true');
    set({ hasSeenWelcomeScreen: true });
  },

  setProfileData: async (data: ProfileData) => {
    await AsyncStorage.setItem(STORAGE_KEYS.ONBOARDING_PROFILE, JSON.stringify(data));
    set({
      profileData: data,
      hasCompletedProfile: true,
    });
  },

  setConsentAccepted: async () => {
    await AsyncStorage.setItem(STORAGE_KEYS.ONBOARDING_CONSENT, 'true');
    set({ hasAcceptedConsent: true });
  },

  setDisclaimerSeen: async () => {
    await AsyncStorage.setItem(STORAGE_KEYS.ONBOARDING_DISCLAIMER, 'true');
    set({ hasSeenDisclaimer: true });
  },

  completeOnboarding: async () => {
    await AsyncStorage.setItem(STORAGE_KEYS.ONBOARDING_COMPLETED, 'true');
    set({ hasCompletedOnboarding: true });
  },

  reset: async () => {
    console.log('[OnboardingStore] 🗑️ Reset onboarding complet');
    await AsyncStorage.multiRemove([
      STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN,
      STORAGE_KEYS.ONBOARDING_COMPLETED,
      STORAGE_KEYS.ONBOARDING_PROFILE,
      STORAGE_KEYS.ONBOARDING_CONSENT,
      STORAGE_KEYS.ONBOARDING_DISCLAIMER,
    ]);
    set({
      hasSeenWelcomeScreen: false,
      hasCompletedProfile: false,
      hasAcceptedConsent: false,
      hasSeenDisclaimer: false,
      hasCompletedOnboarding: false,
      profileData: null,
      hydrated: false, // Force re-hydrate au prochain checkRouting
    });
    console.log('[OnboardingStore] ✅ Reset terminé, hydrated=false');
  },

  hydrate: async () => {
    try {
      console.log('[OnboardingStore] 💧 Hydratation depuis AsyncStorage...');
      const [
        hasSeenWelcome,
        onboardingCompleted,
        profileDataStr,
        consent,
        disclaimer,
      ] = await AsyncStorage.multiGet([
        STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN,
        STORAGE_KEYS.ONBOARDING_COMPLETED,
        STORAGE_KEYS.ONBOARDING_PROFILE,
        STORAGE_KEYS.ONBOARDING_CONSENT,
        STORAGE_KEYS.ONBOARDING_DISCLAIMER,
      ]);

      let profileData: ProfileData | null = null;
      if (profileDataStr[1]) {
        try {
          profileData = JSON.parse(profileDataStr[1]);
        } catch (e) {
          console.error('[OnboardingStore] Error parsing profile data:', e);
        }
      }

      set({
        hasSeenWelcomeScreen: hasSeenWelcome[1] === 'true',
        hasCompletedOnboarding: onboardingCompleted[1] === 'true',
        hasCompletedProfile: !!profileData,
        hasAcceptedConsent: consent[1] === 'true',
        hasSeenDisclaimer: disclaimer[1] === 'true',
        profileData,
        hydrated: true, // Marquer comme hydraté
      });
      console.log('[OnboardingStore] ✅ Hydraté:', {
        hasSeenWelcome: hasSeenWelcome[1] === 'true',
        hasCompletedProfile: !!profileData,
        hasAcceptedConsent: consent[1] === 'true',
      });
    } catch (error) {
      console.error('[OnboardingStore] Error hydrating from AsyncStorage:', error);
      set({ hydrated: true }); // Même en cas d'erreur, marquer hydraté pour éviter boucle
    }
  },
}));
