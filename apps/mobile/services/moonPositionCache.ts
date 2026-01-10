/**
 * Cache quotidien pour la position lunaire
 * Stocke en AsyncStorage la dernière date + position
 * Évite les refetch multiples le même jour
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { MoonPosition } from './lunarClimate';
import { getCurrentMoonPosition } from './moonPosition';

const CACHE_KEY = 'moonPosition_cache';
const CACHE_DATE_KEY = 'moonPosition_cache_date';

interface MoonPositionCacheData {
  date: string; // YYYY-MM-DD
  position: MoonPosition;
}

/**
 * Obtient la date actuelle au format YYYY-MM-DD
 */
function getCurrentDate(): string {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

/**
 * Récupère la position lunaire avec cache quotidien
 *
 * Logique:
 * - Si même jour (YYYY-MM-DD) => retourne cache
 * - Si jour différent ou pas de cache => fetch API + met à jour cache
 *
 * @param forceRefresh - Force le refetch même si cache valide
 * @returns Position lunaire actuelle
 */
export async function getMoonPositionWithCache(forceRefresh: boolean = false): Promise<MoonPosition> {
  const currentDate = getCurrentDate();

  if (!forceRefresh) {
    try {
      // Vérifier le cache
      const cachedDate = await AsyncStorage.getItem(CACHE_DATE_KEY);
      const cachedData = await AsyncStorage.getItem(CACHE_KEY);

      if (cachedDate === currentDate && cachedData) {
        const cached: MoonPosition = JSON.parse(cachedData);
        console.log(`[MoonPositionCache] ✅ Cache hit (date: ${currentDate}):`, cached);
        return cached;
      }

      // Cache expiré ou date différente
      if (cachedDate && cachedDate !== currentDate) {
        console.log(`[MoonPositionCache] 🔄 Cache expiré (cached: ${cachedDate}, current: ${currentDate})`);
      }
    } catch (error) {
      console.warn('[MoonPositionCache] ⚠️ Erreur lecture cache:', error);
    }
  } else {
    console.log('[MoonPositionCache] 🔄 Force refresh demandé');
  }

  // Cache miss ou force refresh => fetch API
  try {
    const position = await getCurrentMoonPosition();

    // Sauvegarder en cache
    try {
      await AsyncStorage.setItem(CACHE_DATE_KEY, currentDate);
      await AsyncStorage.setItem(CACHE_KEY, JSON.stringify(position));
      console.log(`[MoonPositionCache] 💾 Cache mis à jour (date: ${currentDate}):`, position);
    } catch (error) {
      console.warn('[MoonPositionCache] ⚠️ Erreur sauvegarde cache:', error);
    }

    return position;
  } catch (error) {
    console.error('[MoonPositionCache] ❌ Erreur fetch position lunaire:', error);
    throw error;
  }
}

/**
 * Efface le cache (utile pour les tests ou debug)
 */
export async function clearMoonPositionCache(): Promise<void> {
  try {
    await AsyncStorage.multiRemove([CACHE_KEY, CACHE_DATE_KEY]);
    console.log('[MoonPositionCache] 🗑️ Cache effacé');
  } catch (error) {
    console.warn('[MoonPositionCache] ⚠️ Erreur effacement cache:', error);
  }
}
