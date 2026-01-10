/**
 * Service de cache intelligent pour les données lunaires
 * Stratégie: stale-while-revalidate
 * - Retourne cache immédiatement si disponible
 * - Rafraîchit en background si stale
 * - Invalidation automatique à minuit local
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { LunarDayData, CachedLunarData, LunarCacheConfig, LunarDataSource } from '../types/lunar-context';

const DEFAULT_CONFIG: LunarCacheConfig = {
  ttl: 24 * 60 * 60 * 1000, // 24h - données valides jusqu'à minuit
  staleTime: 60 * 60 * 1000, // 1h - considéré stale après 1h
  keyPrefix: 'lunar_day_',
};

/**
 * Génère la clé de cache pour une date
 */
function getCacheKey(date: string, config: LunarCacheConfig = DEFAULT_CONFIG): string {
  return `${config.keyPrefix}${date}`;
}

/**
 * Calcule le timestamp de minuit pour une date donnée
 * Utilisé pour l'invalidation automatique
 */
function getMidnightTimestamp(date: string): number {
  const d = new Date(date + 'T00:00:00');
  d.setDate(d.getDate() + 1); // Minuit du lendemain
  return d.getTime();
}

/**
 * Vérifie si le cache est encore valide (avant TTL et avant minuit)
 * Note: la vérification à minuit ne s'applique que pour la date du jour actuel
 */
function isCacheValid(cached: CachedLunarData, date: string, config: LunarCacheConfig = DEFAULT_CONFIG): boolean {
  const now = Date.now();
  const age = now - cached.cached_at;
  
  // Vérifier si la date correspond au jour actuel (format YYYY-MM-DD)
  const today = new Date().toISOString().split('T')[0];
  const isToday = date === today;
  
  // Invalide si:
  // - Date ne correspond pas
  if (cached.data.date !== date) {
    return false;
  }
  
  // Invalide si TTL dépassé
  if (age > config.ttl) {
    return false;
  }
  
  // Pour la date du jour actuel uniquement: invalide si minuit passé (changement de jour)
  if (isToday) {
    const midnight = getMidnightTimestamp(date);
    if (now > midnight) {
      return false;
    }
  }
  
  return true;
}

/**
 * Vérifie si le cache est stale (valide mais ancien)
 */
function isCacheStale(cached: CachedLunarData, config: LunarCacheConfig = DEFAULT_CONFIG): boolean {
  const age = Date.now() - cached.cached_at;
  return age > config.staleTime;
}

/**
 * Récupère les données du cache si disponibles
 * @returns { data, isStale } ou null si pas de cache valide
 */
export async function getLunarCache(
  date: string,
  config: LunarCacheConfig = DEFAULT_CONFIG
): Promise<{ data: LunarDayData; isStale: boolean; source: LunarDataSource } | null> {
  try {
    const key = getCacheKey(date, config);
    const raw = await AsyncStorage.getItem(key);

    if (!raw) {
      return null;
    }

    const cached: CachedLunarData = JSON.parse(raw);

    // Vérifier validité
    if (!isCacheValid(cached, date, config)) {
      // Cache expiré, le supprimer
      await AsyncStorage.removeItem(key);
      return null;
    }

    // Cache valide
    return {
      data: cached.data,
      isStale: isCacheStale(cached, config),
      source: cached.source || 'cache', // fallback si source pas défini
    };
  } catch (error) {
    console.error('[LunarCache] Error reading cache:', error);
    return null;
  }
}

/**
 * Écrit les données dans le cache
 */
export async function setLunarCache(
  date: string,
  data: LunarDayData,
  source: LunarDataSource,
  config: LunarCacheConfig = DEFAULT_CONFIG
): Promise<void> {
  try {
    const key = getCacheKey(date, config);
    const cached: CachedLunarData = {
      data,
      cached_at: Date.now(),
      source,
    };

    await AsyncStorage.setItem(key, JSON.stringify(cached));
    console.log(`[LunarCache] ✅ Cached data for ${date} (source: ${source})`);
  } catch (error) {
    console.error('[LunarCache] Error writing cache:', error);
  }
}

/**
 * Supprime le cache pour une date spécifique
 */
export async function clearLunarCache(date: string, config: LunarCacheConfig = DEFAULT_CONFIG): Promise<void> {
  try {
    const key = getCacheKey(date, config);
    await AsyncStorage.removeItem(key);
    console.log(`[LunarCache] 🗑️ Cleared cache for ${date}`);
  } catch (error) {
    console.error('[LunarCache] Error clearing cache:', error);
  }
}

/**
 * Supprime tout le cache lunaire
 */
export async function clearAllLunarCache(config: LunarCacheConfig = DEFAULT_CONFIG): Promise<void> {
  try {
    const allKeys = await AsyncStorage.getAllKeys();
    const lunarKeys = allKeys.filter((key) => key.startsWith(config.keyPrefix));

    if (lunarKeys.length > 0) {
      await AsyncStorage.multiRemove(lunarKeys);
      console.log(`[LunarCache] 🗑️ Cleared ${lunarKeys.length} cached entries`);
    }
  } catch (error) {
    console.error('[LunarCache] Error clearing all cache:', error);
  }
}

/**
 * Nettoie les caches expirés (maintenance)
 */
export async function cleanExpiredLunarCache(config: LunarCacheConfig = DEFAULT_CONFIG): Promise<void> {
  try {
    const allKeys = await AsyncStorage.getAllKeys();
    const lunarKeys = allKeys.filter((key) => key.startsWith(config.keyPrefix));

    const expiredKeys: string[] = [];

    for (const key of lunarKeys) {
      const raw = await AsyncStorage.getItem(key);
      if (raw) {
        try {
          const cached: CachedLunarData = JSON.parse(raw);
          const date = cached.data.date;

          if (!isCacheValid(cached, date, config)) {
            expiredKeys.push(key);
          }
        } catch {
          // JSON invalide, marquer pour suppression
          expiredKeys.push(key);
        }
      }
    }

    if (expiredKeys.length > 0) {
      await AsyncStorage.multiRemove(expiredKeys);
      console.log(`[LunarCache] 🧹 Cleaned ${expiredKeys.length} expired entries`);
    }
  } catch (error) {
    console.error('[LunarCache] Error cleaning expired cache:', error);
  }
}
