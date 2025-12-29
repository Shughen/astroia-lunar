/**
 * Cache quotidien pour le Daily Lunar Climate
 * Stocke en AsyncStorage la dernière date + climate complet
 * Évite les refetch multiples le même jour
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { lunaPack } from './api';
import { MoonPosition } from './lunarClimate';
import { getCurrentMoonPosition } from './moonPosition';

const CACHE_KEY = 'dailyClimate_cache';
const CACHE_DATE_KEY = 'dailyClimate_cache_date';

export interface DailyInsight {
  title: string;
  text: string;
  keywords: string[];
  version: string;
}

export interface DailyClimate {
  date: string; // YYYY-MM-DD
  moon: MoonPosition;
  insight: DailyInsight;
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
 * Récupère le Daily Lunar Climate avec cache quotidien
 *
 * Logique:
 * - Si même jour (YYYY-MM-DD) => retourne cache
 * - Si jour différent ou pas de cache => fetch API + met à jour cache
 * - Si API fail => fallback sur moonPosition uniquement (sans insight)
 *
 * @param forceRefresh - Force le refetch même si cache valide
 * @returns Daily Climate avec insight (ou null si API fail)
 */
export async function getDailyClimateWithCache(forceRefresh: boolean = false): Promise<DailyClimate | null> {
  const currentDate = getCurrentDate();

  if (!forceRefresh) {
    try {
      // Vérifier le cache
      const cachedDate = await AsyncStorage.getItem(CACHE_DATE_KEY);
      const cachedData = await AsyncStorage.getItem(CACHE_KEY);

      if (cachedDate === currentDate && cachedData) {
        const cached: DailyClimate = JSON.parse(cachedData);
        console.log(`[DailyClimateCache] ✅ Cache hit (date: ${currentDate}):`, cached.insight.title);
        return cached;
      }

      // Cache expiré ou date différente
      if (cachedDate && cachedDate !== currentDate) {
        console.log(`[DailyClimateCache] 🔄 Cache expiré (cached: ${cachedDate}, current: ${currentDate})`);
      }
    } catch (error) {
      console.warn('[DailyClimateCache] ⚠️ Erreur lecture cache:', error);
    }
  } else {
    console.log('[DailyClimateCache] 🔄 Force refresh demandé');
  }

  // Cache miss ou force refresh => fetch API
  try {
    const climate = await lunaPack.getDailyClimate();

    // Sauvegarder en cache
    try {
      await AsyncStorage.setItem(CACHE_DATE_KEY, currentDate);
      await AsyncStorage.setItem(CACHE_KEY, JSON.stringify(climate));
      console.log(`[DailyClimateCache] 💾 Cache mis à jour (date: ${currentDate}, insight: ${climate.insight.title})`);
    } catch (error) {
      console.warn('[DailyClimateCache] ⚠️ Erreur sauvegarde cache:', error);
    }

    return climate;
  } catch (error) {
    console.error('[DailyClimateCache] ❌ Erreur fetch daily climate depuis API:', error);

    // Fallback: Retourner null (le composant utilisera moonPosition seul)
    return null;
  }
}

/**
 * Efface le cache (utile pour les tests ou debug)
 */
export async function clearDailyClimateCache(): Promise<void> {
  try {
    await AsyncStorage.multiRemove([CACHE_KEY, CACHE_DATE_KEY]);
    console.log('[DailyClimateCache] 🗑️ Cache effacé');
  } catch (error) {
    console.warn('[DailyClimateCache] ⚠️ Erreur effacement cache:', error);
  }
}
