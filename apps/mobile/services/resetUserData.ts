/**
 * Service de reset complet des données utilisateur locales
 * Reset atomique : toutes les données sont supprimées avant navigation
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { STORAGE_KEYS } from '../types/storage';
import { useOnboardingStore } from '../stores/useOnboardingStore';
import { useAuthStore } from '../stores/useAuthStore';
import { useCycleStore } from '../stores/useCycleStore';
import { useNatalStore } from '../stores/useNatalStore';
import { useResetStore } from '../stores/useResetStore';
import { clearAllLunarCache } from './lunarCache';
import { cancelAllNotifications } from './notificationScheduler';

/**
 * Reset complet et atomique de toutes les données locales utilisateur
 * 
 * Supprime :
 * - Onboarding flags (welcome, consent, profile, disclaimer, onboarding_completed)
 * - Données de profil (birth_date, birth_time, birth_place, etc.)
 * - Journal (toutes les entrées journal_entry_*)
 * - Cache lunaire (lunar_day_*)
 * - Stores (onboarding, auth, cycle, natal)
 * - Notifications planifiées
 * - Token d'authentification
 * 
 * @returns Promise<void>
 */
export async function resetAllUserData(): Promise<void> {
  const resetStore = useResetStore.getState();
  
  // Marquer le reset en cours
  resetStore.setIsResetting(true);
  console.log('[ResetService] 🗑️ START: Reset complet des données locales');

  try {
    // Récupérer toutes les clés une seule fois au début
    const allKeys = await AsyncStorage.getAllKeys();
    console.log(`[ResetService] 📋 Total clés AsyncStorage: ${allKeys.length}`);

    // 1. Annuler toutes les notifications planifiées
    console.log('[ResetService] Step 1: Annulation des notifications...');
    await cancelAllNotifications();
    console.log('[ResetService] ✅ Notifications annulées');

    // 2. Supprimer toutes les entrées de journal (journal_entry_*)
    console.log('[ResetService] Step 2: Suppression des entrées de journal...');
    const journalKeys = allKeys.filter((key) => key.startsWith('journal_entry_'));
    if (journalKeys.length > 0) {
      await AsyncStorage.multiRemove(journalKeys);
      console.log(`[ResetService] ✅ Journal supprimé (${journalKeys.length} entrées)`);
    } else {
      console.log('[ResetService] ✅ Aucune entrée de journal à supprimer');
    }

    // 3. Supprimer le cache lunaire (lunar_day_*)
    console.log('[ResetService] Step 3: Suppression du cache lunaire...');
    await clearAllLunarCache();
    console.log('[ResetService] ✅ Cache lunaire supprimé');

    // 4. Reset onboarding store (supprime AsyncStorage + state)
    console.log('[ResetService] Step 4: Reset du store onboarding...');
    const onboardingStore = useOnboardingStore.getState();
    await onboardingStore.reset();
    console.log('[ResetService] ✅ Store onboarding reset');

    // 5. Clear cycle store
    console.log('[ResetService] Step 5: Clear du store cycle...');
    const cycleStore = useCycleStore.getState();
    cycleStore.clear();
    console.log('[ResetService] ✅ Store cycle cleared');

    // 6. Clear natal store
    console.log('[ResetService] Step 6: Clear du store natal...');
    const natalStore = useNatalStore.getState();
    natalStore.clearChart();
    console.log('[ResetService] ✅ Store natal cleared');

    // 7. Logout (supprime token + user state)
    console.log('[ResetService] Step 7: Logout (suppression token auth)...');
    const authStore = useAuthStore.getState();
    authStore.logout();
    // Supprimer aussi le token depuis AsyncStorage explicitement
    await AsyncStorage.removeItem(STORAGE_KEYS.AUTH_TOKEN);
    console.log('[ResetService] ✅ Auth cleared (token supprimé)');

    // 8. Supprimer les données de profil restantes (si stockées séparément)
    console.log('[ResetService] Step 8: Suppression des données de profil...');
    const profileKeys = [
      STORAGE_KEYS.BIRTH_DATE,
      STORAGE_KEYS.BIRTH_TIME,
      STORAGE_KEYS.BIRTH_PLACE,
      STORAGE_KEYS.BIRTH_LATITUDE,
      STORAGE_KEYS.BIRTH_LONGITUDE,
      STORAGE_KEYS.LAST_PERIOD_DATE,
      STORAGE_KEYS.AVERAGE_CYCLE_LENGTH,
      STORAGE_KEYS.DAILY_RESONANCE,
      STORAGE_KEYS.NOTIFICATIONS_ENABLED,
      STORAGE_KEYS.NOTIFICATIONS_LAST_SCHEDULED_AT,
      // Ancienne clé pour migration
      'hasSeenWelcome',
    ];
    
    const existingProfileKeys = profileKeys.filter((key) => allKeys.includes(key));
    if (existingProfileKeys.length > 0) {
      await AsyncStorage.multiRemove(existingProfileKeys);
      console.log(`[ResetService] ✅ Données de profil supprimées (${existingProfileKeys.length} clés)`);
    } else {
      console.log('[ResetService] ✅ Aucune donnée de profil à supprimer');
    }

    // 9. Supprimer toutes les clés fantômes (menstrual_*, onboarding_step)
    console.log('[ResetService] Step 9: Suppression des clés fantômes...');
    const ghostKeys = allKeys.filter((key) =>
      key.startsWith('menstrual_') ||
      key === 'onboarding_step' ||
      key === 'menstrual_opt_in' ||
      key === 'menstrual_skipped'
    );
    if (ghostKeys.length > 0) {
      console.warn('[ResetService] 🗑️ Clés fantômes détectées:', ghostKeys);
      await AsyncStorage.multiRemove(ghostKeys);
      console.log(`[ResetService] ✅ Clés fantômes supprimées (${ghostKeys.length})`);
    } else {
      console.log('[ResetService] ✅ Aucune clé fantôme à supprimer');
    }

    console.log('[ResetService] ✅ END: Reset complet terminé avec succès');
  } catch (error) {
    console.error('[ResetService] ❌ ERREUR lors du reset:', error);
    // Même en cas d'erreur, relâcher le flag pour éviter de bloquer l'app
    resetStore.setIsResetting(false);
    throw error;
  }
  
  // Note: isResetting reste à true jusqu'à ce que la navigation soit terminée
  // Il sera relâché dans le composant qui appelle cette fonction après router.replace()
}

