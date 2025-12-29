/**
 * Tests pour useOnboardingStore
 * Focus: vérifier que le reset permet une re-hydratation
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { useOnboardingStore } from '../stores/useOnboardingStore';
import { STORAGE_KEYS } from '../types/storage';

describe('useOnboardingStore - Reset & Re-hydration', () => {
  beforeEach(async () => {
    // Clear store et AsyncStorage avant chaque test
    await AsyncStorage.clear();
    useOnboardingStore.setState({
      hasSeenWelcomeScreen: false,
      hasCompletedProfile: false,
      hasAcceptedConsent: false,
      hasSeenDisclaimer: false,
      hasCompletedOnboarding: false,
      profileData: null,
      hydrated: false,
    });
  });

  afterEach(async () => {
    await AsyncStorage.clear();
  });

  it('devrait hydrater depuis AsyncStorage au premier appel', async () => {
    // Setup: Simuler des données en AsyncStorage
    await AsyncStorage.multiSet([
      [STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN, 'true'],
      [STORAGE_KEYS.ONBOARDING_COMPLETED, 'true'],
      [STORAGE_KEYS.ONBOARDING_PROFILE, JSON.stringify({ name: 'Test User' })],
      [STORAGE_KEYS.ONBOARDING_CONSENT, 'true'],
      [STORAGE_KEYS.ONBOARDING_DISCLAIMER, 'true'],
    ]);

    // Hydrate
    await useOnboardingStore.getState().hydrate();

    // Vérifier état hydraté
    const state = useOnboardingStore.getState();
    expect(state.hydrated).toBe(true);
    expect(state.hasSeenWelcomeScreen).toBe(true);
    expect(state.hasCompletedOnboarding).toBe(true);
    expect(state.hasCompletedProfile).toBe(true);
    expect(state.hasAcceptedConsent).toBe(true);
    expect(state.hasSeenDisclaimer).toBe(true);
    expect(state.profileData).toEqual({ name: 'Test User' });
  });

  it('ne devrait pas re-hydrater si déjà hydraté (guard)', async () => {
    // Setup
    await AsyncStorage.setItem(STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN, 'true');

    // Première hydratation
    await useOnboardingStore.getState().hydrate();
    expect(useOnboardingStore.getState().hasSeenWelcomeScreen).toBe(true);

    // Changer AsyncStorage après hydratation
    await AsyncStorage.setItem(STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN, 'false');

    // Deuxième hydratation (devrait être bloquée par guard)
    await useOnboardingStore.getState().hydrate();

    // L'état ne doit PAS changer (guard actif)
    expect(useOnboardingStore.getState().hasSeenWelcomeScreen).toBe(true);
  });

  it('devrait permettre re-hydratation après reset (hydrated=false)', async () => {
    // ÉTAPE 1: Hydrate avec données complètes
    await AsyncStorage.multiSet([
      [STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN, 'true'],
      [STORAGE_KEYS.ONBOARDING_COMPLETED, 'true'],
      [STORAGE_KEYS.ONBOARDING_PROFILE, JSON.stringify({ name: 'Test User' })],
      [STORAGE_KEYS.ONBOARDING_CONSENT, 'true'],
      [STORAGE_KEYS.ONBOARDING_DISCLAIMER, 'true'],
    ]);

    await useOnboardingStore.getState().hydrate();

    let state = useOnboardingStore.getState();
    expect(state.hydrated).toBe(true);
    expect(state.hasCompletedOnboarding).toBe(true);
    expect(state.hasSeenWelcomeScreen).toBe(true);

    // ÉTAPE 2: Complete onboarding (déjà fait, mais on peut re-appeler)
    await useOnboardingStore.getState().completeOnboarding();

    state = useOnboardingStore.getState();
    expect(state.hasCompletedOnboarding).toBe(true);

    // ÉTAPE 3: Reset complet
    await useOnboardingStore.getState().reset();

    state = useOnboardingStore.getState();
    expect(state.hydrated).toBe(false); // ⚠️ CRITIQUE: doit être false
    expect(state.hasCompletedOnboarding).toBe(false);
    expect(state.hasSeenWelcomeScreen).toBe(false);
    expect(state.hasCompletedProfile).toBe(false);
    expect(state.hasAcceptedConsent).toBe(false);
    expect(state.hasSeenDisclaimer).toBe(false);
    expect(state.profileData).toBeNull();

    // Vérifier que AsyncStorage est vide
    const keys = await AsyncStorage.multiGet([
      STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN,
      STORAGE_KEYS.ONBOARDING_COMPLETED,
      STORAGE_KEYS.ONBOARDING_PROFILE,
      STORAGE_KEYS.ONBOARDING_CONSENT,
      STORAGE_KEYS.ONBOARDING_DISCLAIMER,
    ]);

    keys.forEach(([key, value]) => {
      expect(value).toBeNull(); // Toutes les clés doivent être null (supprimées)
    });

    // ÉTAPE 4: Re-hydrate (doit fonctionner car hydrated=false)
    // Simuler un nouvel onboarding en AsyncStorage
    await AsyncStorage.setItem(STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN, 'true');
    await AsyncStorage.setItem(STORAGE_KEYS.ONBOARDING_PROFILE, JSON.stringify({ name: 'New User' }));

    await useOnboardingStore.getState().hydrate();

    state = useOnboardingStore.getState();
    expect(state.hydrated).toBe(true); // Doit être re-hydraté
    expect(state.hasSeenWelcomeScreen).toBe(true);
    expect(state.profileData).toEqual({ name: 'New User' });
    expect(state.hasCompletedOnboarding).toBe(false); // Pas encore complet
  });

  it('devrait effacer toutes les clés AsyncStorage lors du reset', async () => {
    // Setup: Remplir AsyncStorage
    await AsyncStorage.multiSet([
      [STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN, 'true'],
      [STORAGE_KEYS.ONBOARDING_COMPLETED, 'true'],
      [STORAGE_KEYS.ONBOARDING_PROFILE, JSON.stringify({ name: 'Test' })],
      [STORAGE_KEYS.ONBOARDING_CONSENT, 'true'],
      [STORAGE_KEYS.ONBOARDING_DISCLAIMER, 'true'],
    ]);

    // Reset
    await useOnboardingStore.getState().reset();

    // Vérifier que toutes les clés sont supprimées
    const allKeys = [
      STORAGE_KEYS.HAS_SEEN_WELCOME_SCREEN,
      STORAGE_KEYS.ONBOARDING_COMPLETED,
      STORAGE_KEYS.ONBOARDING_PROFILE,
      STORAGE_KEYS.ONBOARDING_CONSENT,
      STORAGE_KEYS.ONBOARDING_DISCLAIMER,
    ];

    const values = await AsyncStorage.multiGet(allKeys);

    values.forEach(([key, value]) => {
      expect(value).toBeNull();
    });
  });

  it('devrait remettre tous les flags à false lors du reset', async () => {
    // Setup: Mettre tous les flags à true
    useOnboardingStore.setState({
      hasSeenWelcomeScreen: true,
      hasCompletedProfile: true,
      hasAcceptedConsent: true,
      hasSeenDisclaimer: true,
      hasCompletedOnboarding: true,
      profileData: { name: 'Test User', birthDate: new Date() },
      hydrated: true,
    });

    // Reset
    await useOnboardingStore.getState().reset();

    // Vérifier tous les flags
    const state = useOnboardingStore.getState();
    expect(state.hasSeenWelcomeScreen).toBe(false);
    expect(state.hasCompletedProfile).toBe(false);
    expect(state.hasAcceptedConsent).toBe(false);
    expect(state.hasSeenDisclaimer).toBe(false);
    expect(state.hasCompletedOnboarding).toBe(false);
    expect(state.profileData).toBeNull();
    expect(state.hydrated).toBe(false);
  });
});
