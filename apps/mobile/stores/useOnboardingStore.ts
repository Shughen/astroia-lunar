/**
 * Store Zustand pour l'onboarding
 * Gère le flow complet : welcome, profile, consent, disclaimer, cycle, slides
 */

import { create } from 'zustand';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { STORAGE_KEYS } from '../types/storage';
import { getNextOnboardingStep as getNextStep, type OnboardingState as FlowState } from '../services/onboardingFlow';

interface ProfileData {
  name?: string;
  birthDate?: Date;
  birthTime?: string; // Format HH:MM
  birthPlace?: string; // Ex: "Paris, France"
  birthLatitude?: number;
  birthLongitude?: number;
  // birthTimezone supprimé - sera auto-détecté par le backend depuis lat/lon
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

  // Helper de navigation
  getNextOnboardingStep: () => string;

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
    const state = get();

    // GUARD: Vérifier que TOUTES les étapes sont complètes
    const preconditions = {
      hasSeenWelcomeScreen: state.hasSeenWelcomeScreen,
      hasAcceptedConsent: state.hasAcceptedConsent,
      hasCompletedProfile: state.hasCompletedProfile,
      hasSeenDisclaimer: state.hasSeenDisclaimer,
    };

    const allComplete = Object.values(preconditions).every(v => v === true);

    if (!allComplete) {
      console.error('[OnboardingStore] ❌ completeOnboarding() - Préconditions manquantes:', preconditions);
      throw new Error('Cannot complete onboarding: preconditions not met');
    }

    console.log('[OnboardingStore] ✅ completeOnboarding() - Toutes les préconditions OK');

    // Marquer onboarding comme terminé
    await AsyncStorage.setItem(STORAGE_KEYS.ONBOARDING_COMPLETED, 'true');
    set({ hasCompletedOnboarding: true });

    console.log('[OnboardingStore] ✅ completeOnboarding() - Terminé');
  },

  /**
   * Calcule la prochaine étape d'onboarding selon l'état actuel
   * Ordre: welcome → consent → profile → disclaimer → slides → home
   * Utilise la fonction pure du service onboardingFlow
   */
  getNextOnboardingStep: () => {
    const state = get();
    // Map store state to flow state type
    const flowState: FlowState = {
      hasSeenWelcomeScreen: state.hasSeenWelcomeScreen,
      hasAcceptedConsent: state.hasAcceptedConsent,
      hasCompletedProfile: state.hasCompletedProfile,
      hasSeenDisclaimer: state.hasSeenDisclaimer,
      hasCompletedOnboarding: state.hasCompletedOnboarding,
    };
    return getNextStep(flowState);
  },

  reset: async () => {
    console.log('[OnboardingStore] 🗑️ Reset onboarding complet - START');

    // Liste explicite des clés à supprimer
    const keysToRemove = [
      STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN,
      STORAGE_KEYS.ONBOARDING_COMPLETED,
      STORAGE_KEYS.ONBOARDING_PROFILE,
      STORAGE_KEYS.ONBOARDING_CONSENT,
      STORAGE_KEYS.ONBOARDING_DISCLAIMER,
    ];

    console.log('[OnboardingStore] 📋 Clés AsyncStorage à supprimer:', keysToRemove);

    try {
      await AsyncStorage.multiRemove(keysToRemove);
      console.log('[OnboardingStore] ✅ AsyncStorage cleared');
    } catch (error) {
      console.error('[OnboardingStore] ❌ Erreur suppression AsyncStorage:', error);
      throw error;
    }

    // Reset du state Zustand
    set({
      hasSeenWelcomeScreen: false,
      hasCompletedProfile: false,
      hasAcceptedConsent: false,
      hasSeenDisclaimer: false,
      hasCompletedOnboarding: false,
      profileData: null,
      hydrated: false, // ⚠️ CRITIQUE: Force re-hydrate au prochain checkRouting
    });

    console.log('[OnboardingStore] ✅ Reset terminé - État final:', {
      hasSeenWelcomeScreen: false,
      hasCompletedProfile: false,
      hasAcceptedConsent: false,
      hasSeenDisclaimer: false,
      hasCompletedOnboarding: false,
      profileData: null,
      hydrated: false,
    });
  },

  hydrate: async () => {
    // ⚠️ GUARD: Ne jamais re-hydrater si déjà hydrated (sauf après reset où hydrated=false)
    if (get().hydrated) {
      console.log('[OnboardingStore] ⏭️ Déjà hydraté, skip hydratation');
      return;
    }

    try {
      console.log('[OnboardingStore] 💧 Hydratation depuis AsyncStorage...');
      const [
        hasSeenWelcome,
        onboardingCompleted,
        profileDataStr,
        consent,
        disclaimer,
        // Migration: vérifier ancienne clé hasSeenWelcome (sans "Screen")
        oldHasSeenWelcome,
      ] = await AsyncStorage.multiGet([
        STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN,
        STORAGE_KEYS.ONBOARDING_COMPLETED,
        STORAGE_KEYS.ONBOARDING_PROFILE,
        STORAGE_KEYS.ONBOARDING_CONSENT,
        STORAGE_KEYS.ONBOARDING_DISCLAIMER,
        'hasSeenWelcome', // Ancienne clé pour migration
      ]);

      // Migration: si ancienne clé hasSeenWelcome=true, migrer vers hasSeenWelcomeScreen
      let hasSeenWelcomeScreenValue = hasSeenWelcome[1] === 'true';
      if (!hasSeenWelcomeScreenValue && oldHasSeenWelcome[1] === 'true') {
        console.log('[OnboardingStore] 🔄 Migration: hasSeenWelcome=true → hasSeenWelcomeScreen=true');
        await AsyncStorage.setItem(STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN, 'true');
        await AsyncStorage.removeItem('hasSeenWelcome'); // Nettoyer ancienne clé
        hasSeenWelcomeScreenValue = true;
      }

      let profileData: ProfileData | null = null;
      if (profileDataStr[1]) {
        try {
          const parsed = JSON.parse(profileDataStr[1]);
          // Convertir birthDate string en Date si nécessaire
          if (parsed.birthDate && typeof parsed.birthDate === 'string') {
            parsed.birthDate = new Date(parsed.birthDate);
          }
          profileData = parsed;
        } catch (e) {
          console.error('[OnboardingStore] Error parsing profile data:', e);
        }
      }

      set({
        hasSeenWelcomeScreen: hasSeenWelcomeScreenValue,
        hasCompletedOnboarding: onboardingCompleted[1] === 'true',
        hasCompletedProfile: !!profileData,
        hasAcceptedConsent: consent[1] === 'true',
        hasSeenDisclaimer: disclaimer[1] === 'true',
        profileData,
        hydrated: true, // Marquer comme hydraté
      });
      console.log('[OnboardingStore] ✅ Hydraté:', {
        hasSeenWelcomeScreen: hasSeenWelcomeScreenValue,
        hasCompletedProfile: !!profileData,
        hasAcceptedConsent: consent[1] === 'true',
        hasCompletedOnboarding: onboardingCompleted[1] === 'true',
      });
    } catch (error) {
      console.error('[OnboardingStore] Error hydrating from AsyncStorage:', error);
      set({ hydrated: true }); // Même en cas d'erreur, marquer hydraté pour éviter boucle
    }
  },
}));
