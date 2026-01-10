/**
 * LunarProvider - Contexte unifié des données lunaires
 * Stratégie: stale-while-revalidate
 * - Retourne cache immédiatement
 * - Rafraîchit en background si stale
 * - Fallback cascade: API → cache → local
 */

import React, { createContext, useContext, useState, useEffect, useCallback, useRef } from 'react';
import { LunarContextValue, LunarDayData, LunarContextStatus, LunarHelpers, LunarDataSource } from '../types/lunar-context';
import { MoonPhase } from '../types/ritual';
import { getLunarCache, setLunarCache, clearAllLunarCache } from '../services/lunarCache';
import { lunaPack } from '../services/api';
import { getTodayDateString, getPhaseEmoji, getPhaseKey, formatTime } from '../utils/ritualHelpers';
import { calculateLocalMoonPhase, calculateLocalMoonSign } from '../utils/moonCalc';

const LunarContext = createContext<LunarContextValue | undefined>(undefined);

interface LunarProviderProps {
  children: React.ReactNode;
}

/**
 * Fetch VoC status from API
 */
async function fetchVocStatus() {
  try {
    const response = await fetch(
      `${process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8000'}/api/lunar/voc/status`
    );

    if (!response.ok) {
      throw new Error(`VoC API error: ${response.status}`);
    }

    return response.json();
  } catch (error) {
    console.log('[LunarProvider] VoC API unavailable:', error);
    return null;
  }
}

/**
 * Convertit phase API (français) vers MoonPhase (anglais)
 */
function convertPhaseToEnglish(phase: string): MoonPhase {
  const phaseMap: Record<string, MoonPhase> = {
    'Nouvelle Lune': 'New Moon',
    'Premier Croissant': 'Waxing Crescent',
    'Premier Quartier': 'First Quarter',
    'Lune Gibbeuse': 'Waxing Gibbous',
    'Pleine Lune': 'Full Moon',
    'Lune Disseminante': 'Waning Gibbous',
    'Dernier Quartier': 'Last Quarter',
    'Dernier Croissant': 'Waning Crescent',
  };

  return phaseMap[phase] || calculateLocalMoonPhase();
}

/**
 * Fetch lunar data from API with fallback
 */
async function fetchLunarDataFromAPI(date: string): Promise<{ data: LunarDayData; source: LunarDataSource }> {
  const today = getTodayDateString();

  // API uniquement pour aujourd'hui
  if (date !== today) {
    throw new Error('API fetch only available for today');
  }

  try {
    // Fetch en parallèle: Daily Climate + VoC
    const [climateResult, vocResult] = await Promise.allSettled([
      lunaPack.getDailyClimate(),
      fetchVocStatus(),
    ]);

    const data: LunarDayData = {
      date,
      moon: {
        phase:
          climateResult.status === 'fulfilled'
            ? convertPhaseToEnglish(climateResult.value.moon.phase)
            : calculateLocalMoonPhase(),
        sign: climateResult.status === 'fulfilled' ? climateResult.value.moon.sign : calculateLocalMoonSign(),
      },
      voc:
        vocResult.status === 'fulfilled' && vocResult.value?.now
          ? {
              is_active: vocResult.value.now.is_active,
              end_at: vocResult.value.now.end_at,
            }
          : undefined,
    };

    return { data, source: 'api' };
  } catch (error) {
    console.error('[LunarProvider] API fetch failed:', error);
    throw error;
  }
}

/**
 * Fallback to local calculation
 * Now provides BOTH phase AND sign (no more 'Unknown')
 */
function calculateLocalLunarData(date: string): LunarDayData {
  // Parse date to ensure consistent calculation (noon UTC to avoid timezone issues)
  const targetDate = new Date(date + 'T12:00:00Z');

  return {
    date,
    moon: {
      phase: calculateLocalMoonPhase(targetDate),
      sign: calculateLocalMoonSign(targetDate),
    },
  };
}

/**
 * Generate helpers from lunar data
 */
function generateHelpers(data: LunarDayData | null): LunarHelpers {
  if (!data) {
    return {
      phaseEmoji: '🌑',
      phaseKey: 'new_moon',
      vocActive: false,
    };
  }

  return {
    phaseEmoji: getPhaseEmoji(data.moon.phase),
    phaseKey: getPhaseKey(data.moon.phase),
    vocActive: data.voc?.is_active || false,
    vocEndTime: data.voc?.is_active ? formatTime(data.voc.end_at) : undefined,
  };
}

export function LunarProvider({ children }: LunarProviderProps) {
  // currentDay en ref stable (ne change jamais durant la session)
  const currentDay = useRef(getTodayDateString()).current;

  const [current, setCurrent] = useState<LunarDayData | null>(null);
  const [status, setStatus] = useState<LunarContextStatus>({
    isLoading: true,
    isStale: false,
    source: 'local',
    lastUpdated: Date.now(),
  });

  // Ref pour éviter les fetchs parallèles
  const isFetchingRef = useRef(false);

  // Ref pour accès stable à current sans dépendance dans getDayData
  const currentRef = useRef<LunarDayData | null>(null);

  // Guards pour éviter boucle infinie de refresh
  const refreshInFlight = useRef(false);
  const lastRefreshAt = useRef<number>(0);
  const REFRESH_TTL_MS = 60000; // 60 secondes minimum entre refreshs

  /**
   * Load lunar data with stale-while-revalidate strategy
   * NOTE: Ne dépend PAS de `current` pour éviter re-création à chaque update
   */
  const loadLunarData = useCallback(async (date: string, forceRefresh = false) => {
    // Éviter les fetchs parallèles
    if (isFetchingRef.current && !forceRefresh) {
      return;
    }

    try {
      // 1. Tenter cache d'abord (sauf si forceRefresh)
      if (!forceRefresh) {
        const cached = await getLunarCache(date);

        if (cached) {
          // Cache valide trouvé
          setCurrent(cached.data);
          setStatus({
            isLoading: false,
            isStale: cached.isStale,
            source: cached.source,
            lastUpdated: Date.now(),
          });

          // Si stale, rafraîchir en background (avec guard pour éviter boucle infinie)
          if (cached.isStale) {
            const now = Date.now();
            const timeSinceLastRefresh = now - lastRefreshAt.current;

            if (!refreshInFlight.current && timeSinceLastRefresh > REFRESH_TTL_MS) {
              if (__DEV__) console.log('[LunarProvider] Cache stale, refreshing in background...');
              refreshInFlight.current = true;
              lastRefreshAt.current = now;

              // Refresh sans bloquer, reset inFlight dans finally
              loadLunarData(date, true)
                .catch((err) => {
                  if (__DEV__) console.warn('[LunarProvider] Background refresh error:', err);
                })
                .finally(() => {
                  refreshInFlight.current = false;
                });
            } else if (__DEV__) {
              console.log(
                `[LunarProvider] Skip refresh: inFlight=${refreshInFlight.current}, ` +
                `timeSinceLastRefresh=${Math.round(timeSinceLastRefresh / 1000)}s`
              );
            }
          }

          return;
        }
      }

      // 2. Pas de cache (ou forceRefresh) → fetch API
      isFetchingRef.current = true;
      lastRefreshAt.current = Date.now();

      // Utiliser setter fonctionnel pour éviter dépendance sur `current`
      setStatus((prev) => ({
        ...prev,
        isLoading: !currentRef.current, // Loading si pas de données existantes
        isStale: !!currentRef.current, // Stale si on a déjà des données
      }));

      const { data, source } = await fetchLunarDataFromAPI(date);

      // Mise à jour state
      setCurrent(data);
      setStatus({
        isLoading: false,
        isStale: false,
        source,
        lastUpdated: Date.now(),
      });

      // Cache les données
      await setLunarCache(date, data, source);
    } catch (apiError) {
      if (__DEV__) console.log('[LunarProvider] API failed, trying cache...');

      // 3. API failed → essayer cache même expiré
      const cached = await getLunarCache(date);
      if (cached) {
        setCurrent(cached.data);
        setStatus({
          isLoading: false,
          isStale: true,
          source: cached.source,
          lastUpdated: Date.now(),
          error: 'API unavailable, using cached data',
        });
        return;
      }

      // 4. Fallback total : calcul local
      if (__DEV__) console.log('[LunarProvider] Using local calculation fallback');
      const localData = calculateLocalLunarData(date);

      setCurrent(localData);
      setStatus({
        isLoading: false,
        isStale: false,
        source: 'local',
        lastUpdated: Date.now(),
        error: 'API unavailable, using local calculation',
      });

      // Cache le fallback local
      await setLunarCache(date, localData, 'local');
    } finally {
      isFetchingRef.current = false;
      refreshInFlight.current = false;
    }
  }, []); // ✅ Aucune dépendance - fonction stable

  /**
   * Force refresh depuis API
   * Note: currentDay est stable (ref), loadLunarData est stable (deps [])
   */
  const refresh = useCallback(async () => {
    await loadLunarData(currentDay, true);
  }, [loadLunarData]); // currentDay stable donc pas besoin en deps

  /**
   * Récupère les données d'un jour spécifique
   * Utilisé par Timeline pour générer plusieurs jours
   * Note: utilise currentRef pour éviter de recréer la fonction à chaque changement de current
   */
  const getDayData = useCallback(async (date: string): Promise<LunarDayData> => {
    const today = getTodayDateString();

    // Si aujourd'hui, retourner current ou charger
    if (date === today) {
      // Utiliser currentRef.current au lieu de current pour éviter dependency
      if (currentRef.current) {
        return currentRef.current;
      }
      // Ne pas await ici car ça crée des dépendances, juste trigger le load
      loadLunarData(date).catch(err => {
        if (__DEV__) console.warn('[LunarProvider] getDayData loadLunarData error:', err);
      });
      // Retourner fallback immédiatement
      return calculateLocalLunarData(date);
    }

    // Autre jour : essayer cache puis fallback local
    const cached = await getLunarCache(date);
    if (cached) {
      return cached.data;
    }

    // Fallback local pour dates passées/futures
    const localData = calculateLocalLunarData(date);
    await setLunarCache(date, localData, 'local');
    return localData;
  }, []);

  /**
   * Clear tout le cache
   */
  const clearCache = useCallback(async () => {
    await clearAllLunarCache();
    await loadLunarData(currentDay, true);
  }, [loadLunarData]); // currentDay stable

  /**
   * Sync currentRef with current state
   */
  useEffect(() => {
    currentRef.current = current;
  }, [current]);

  /**
   * Load data au montage uniquement (deps stables)
   */
  useEffect(() => {
    loadLunarData(currentDay);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []); // ✅ Run ONCE au mount - currentDay et loadLunarData stables

  const helpers = generateHelpers(current);

  const value: LunarContextValue = {
    currentDay,
    current,
    status,
    helpers,
    refresh,
    getDayData,
    clearCache,
  };

  return <LunarContext.Provider value={value}>{children}</LunarContext.Provider>;
}

/**
 * Hook pour accéder au contexte lunaire
 */
export function useLunar(): LunarContextValue {
  const context = useContext(LunarContext);
  if (!context) {
    throw new Error('useLunar must be used within LunarProvider');
  }
  return context;
}

/**
 * Hook pour récupérer les données d'un jour spécifique
 */
export function useLunarDay(date: string): LunarDayData | null {
  const { getDayData } = useLunar();
  const [data, setData] = useState<LunarDayData | null>(null);

  useEffect(() => {
    getDayData(date).then(setData);
  }, [date, getDayData]);

  return data;
}
