/**
 * Types pour le LunarContext unifié
 * Centralise les données lunaires pour éviter fetchs redondants
 */

import { MoonPhase } from './ritual';

/**
 * Source des données lunaires
 */
export type LunarDataSource = 'api' | 'cache' | 'local';

/**
 * Données lunaires d'un jour spécifique
 */
export interface LunarDayData {
  date: string; // YYYY-MM-DD
  moon: {
    phase: MoonPhase;
    sign: string; // "Aquarius", "Taurus", etc.
  };
  voc?: {
    is_active: boolean;
    end_at: string; // ISO timestamp
  };
}

/**
 * Statut du contexte lunaire
 */
export interface LunarContextStatus {
  isLoading: boolean;
  isStale: boolean; // true si données en cache mais refresh en cours
  source: LunarDataSource;
  lastUpdated: number; // timestamp
  error?: string;
}

/**
 * Helpers dérivés pour l'affichage
 */
export interface LunarHelpers {
  phaseEmoji: string; // 🌑, 🌒, etc.
  phaseKey: string; // "new_moon", "waxing_crescent", etc. (pour i18n)
  vocActive: boolean;
  vocEndTime?: string; // Format HH:mm si VoC actif
}

/**
 * Données en cache avec TTL
 */
export interface CachedLunarData {
  data: LunarDayData;
  cached_at: number; // timestamp
  source: LunarDataSource;
}

/**
 * Configuration du cache
 */
export interface LunarCacheConfig {
  ttl: number; // Time to live en ms (défaut: 24h)
  staleTime: number; // Temps avant de considérer stale en ms (défaut: 1h)
  keyPrefix: string; // Préfixe des clés AsyncStorage
}

/**
 * Interface du contexte lunaire
 */
export interface LunarContextValue {
  // Données actuelles (aujourd'hui)
  currentDay: string; // YYYY-MM-DD
  current: LunarDayData | null;

  // Statut
  status: LunarContextStatus;

  // Helpers
  helpers: LunarHelpers;

  // Actions
  refresh: () => Promise<void>; // Force refresh depuis API
  getDayData: (date: string) => Promise<LunarDayData>; // Récupère données d'un jour spécifique

  // Cache management (optionnel, pour debug/admin)
  clearCache: () => Promise<void>;
}
