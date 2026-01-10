/**
 * Service pour la carte Rituel Quotidien
 * Gestion du fetch API avec fallback cascade et cache
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { DailyRitualData, CachedRitualData, VocStatus } from '../types/ritual';
import { lunaPack } from './api';
import { calculateLocalPhase, getTodayDateString } from '../utils/ritualHelpers';

const CACHE_TTL_MS = 24 * 60 * 60 * 1000; // 24h

/**
 * Récupère les données du rituel quotidien avec fallback cascade
 * 1. Essai cache si valide
 * 2. Essai API (Daily Climate + VoC)
 * 3. Fallback calcul local
 */
export async function fetchRitualData(): Promise<DailyRitualData> {
  const today = getTodayDateString();

  try {
    // 1. Tenter cache d'abord
    const cachedData = await getCachedData(today);
    if (cachedData) {
      return cachedData.data;
    }

    // 2. Fetch API en parallèle (indépendants)
    const [climateResult, vocResult] = await Promise.allSettled([
      lunaPack.getDailyClimate(),
      fetchVocStatus(),
    ]);

    // 3. Construire les données ritual
    const ritualData: DailyRitualData = {
      date: today,
      moon: {
        phase:
          climateResult.status === 'fulfilled'
            ? (climateResult.value.moon.phase as any)
            : calculateLocalPhase(),
        sign:
          climateResult.status === 'fulfilled'
            ? climateResult.value.moon.sign
            : 'Unknown',
      },
      voc:
        vocResult.status === 'fulfilled' && vocResult.value.now
          ? {
              is_active: vocResult.value.now.is_active,
              end_at: vocResult.value.now.end_at,
            }
          : undefined,
    };

    // 4. Cache pour 24h
    await cacheData(today, ritualData);

    return ritualData;
  } catch (error) {
    console.error('[RitualService] Error fetching ritual data:', error);

    // Fallback total : calcul local uniquement
    return {
      date: today,
      moon: {
        phase: calculateLocalPhase(),
        sign: 'Unknown',
      },
    };
  }
}

/**
 * Récupère le statut VoC depuis l'API
 */
async function fetchVocStatus(): Promise<VocStatus> {
  // Utiliser l'endpoint /api/lunar/voc/status pour avoir now + next + upcoming
  const response = await fetch(
    `${process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8000'}/api/lunar/voc/status`
  );

  if (!response.ok) {
    throw new Error(`VoC API error: ${response.status}`);
  }

  return response.json();
}

/**
 * Récupère les données en cache si valides (même jour, < 24h)
 */
async function getCachedData(date: string): Promise<CachedRitualData | null> {
  try {
    const key = `daily_ritual_card_${date}`;
    const cached = await AsyncStorage.getItem(key);

    if (cached) {
      const parsed: CachedRitualData = JSON.parse(cached);

      // Vérifier validité (même date + age < 24h)
      const age = Date.now() - parsed.cached_at;
      if (parsed.data.date === date && age < CACHE_TTL_MS) {
        return parsed;
      }
    }
  } catch (error) {
    console.error('[RitualService] Cache read error:', error);
  }

  return null;
}

/**
 * Cache les données pour 24h
 */
async function cacheData(date: string, data: DailyRitualData): Promise<void> {
  try {
    const key = `daily_ritual_card_${date}`;
    const payload: CachedRitualData = {
      data,
      cached_at: Date.now(),
    };
    await AsyncStorage.setItem(key, JSON.stringify(payload));
  } catch (error) {
    console.error('[RitualService] Cache write error:', error);
  }
}

/**
 * Vérifie si c'est la première vue du jour (pour animation)
 */
export async function isFirstViewToday(): Promise<boolean> {
  try {
    const today = getTodayDateString();
    const key = `ritual_card_last_viewed_${today}`;
    const lastViewed = await AsyncStorage.getItem(key);
    return !lastViewed;
  } catch (error) {
    console.error('[RitualService] isFirstViewToday error:', error);
    return false;
  }
}

/**
 * Marque la carte comme vue aujourd'hui
 */
export async function markAsViewedToday(): Promise<void> {
  try {
    const today = getTodayDateString();
    const key = `ritual_card_last_viewed_${today}`;
    await AsyncStorage.setItem(key, Date.now().toString());
  } catch (error) {
    console.error('[RitualService] markAsViewedToday error:', error);
  }
}
