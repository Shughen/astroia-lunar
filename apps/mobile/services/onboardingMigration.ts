/**
 * Migration one-shot pour nettoyer les flags fantômes d'anciennes versions
 * À appeler AU DÉMARRAGE de l'app (avant hydratation)
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { STORAGE_KEYS } from '../types/storage';

/**
 * Supprime les clés AsyncStorage obsolètes/fantômes (ONE-SHOT)
 * - menstrual_opt_in (cycle-setup supprimé)
 * - menstrual_skipped (cycle-setup supprimé)
 * - onboarding_step (ancienne implémentation)
 * - hasSeenWelcome (migration vers hasSeenWelcomeScreen)
 *
 * Ne s'exécute qu'une seule fois par installation (flag MIGRATION_GHOSTFLAGS_DONE)
 */
export async function cleanupGhostFlags(): Promise<void> {
  try {
    // Vérifier si la migration a déjà été faite
    const migrationDone = await AsyncStorage.getItem(STORAGE_KEYS.MIGRATION_GHOSTFLAGS_DONE);

    if (migrationDone === 'true') {
      // Migration déjà effectuée, skip
      return;
    }

    console.log('[Migration] 🔄 Première exécution : nettoyage des flags fantômes...');

    const allKeys = await AsyncStorage.getAllKeys();

    const ghostKeys = allKeys.filter(
      (key) =>
        key === 'menstrual_opt_in' ||
        key === 'menstrual_skipped' ||
        key === 'onboarding_step' ||
        key === 'hasSeenWelcome' // Ancienne clé (migration vers hasSeenWelcomeScreen)
    );

    if (ghostKeys.length > 0) {
      console.warn('[Migration] 🗑️ Suppression des flags fantômes:', ghostKeys);
      await AsyncStorage.multiRemove(ghostKeys);
      console.log('[Migration] ✅ Flags fantômes supprimés');
    } else {
      console.log('[Migration] ✅ Aucun flag fantôme détecté');
    }

    // Marquer la migration comme effectuée
    await AsyncStorage.setItem(STORAGE_KEYS.MIGRATION_GHOSTFLAGS_DONE, 'true');
    console.log('[Migration] ✅ Migration terminée, marquée comme effectuée');
  } catch (error) {
    console.error('[Migration] ❌ Erreur lors du nettoyage des flags fantômes:', error);
    // Ne pas throw : ne pas bloquer le boot de l'app
  }
}
