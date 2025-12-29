/**
 * Service de gestion de la clôture du soir (résonance quotidienne)
 * Stocke la réponse de l'utilisateur à la question : "Cette énergie a-t-elle résonné aujourd'hui ?"
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import { STORAGE_KEYS } from '../types/storage';

export type ResonanceValue = 'yes' | 'no' | 'maybe';

export interface DailyResonance {
  date: string; // YYYY-MM-DD
  value: ResonanceValue;
}

/**
 * Retourne la date du jour au format YYYY-MM-DD
 */
function getCurrentDate(): string {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

/**
 * Vérifie si la résonance a déjà été enregistrée aujourd'hui
 */
export async function hasRespondedToday(): Promise<boolean> {
  try {
    const stored = await AsyncStorage.getItem(STORAGE_KEYS.DAILY_RESONANCE);
    if (!stored) return false;

    const resonance: DailyResonance = JSON.parse(stored);
    const today = getCurrentDate();

    return resonance.date === today;
  } catch (error) {
    console.error('[DailyResonance] Erreur vérification réponse:', error);
    return false;
  }
}

/**
 * Enregistre la réponse de l'utilisateur
 */
export async function saveDailyResonance(value: ResonanceValue): Promise<void> {
  try {
    const resonance: DailyResonance = {
      date: getCurrentDate(),
      value,
    };

    await AsyncStorage.setItem(STORAGE_KEYS.DAILY_RESONANCE, JSON.stringify(resonance));
    console.log(`[DailyResonance] ✅ Résonance enregistrée: ${value} (${resonance.date})`);
  } catch (error) {
    console.error('[DailyResonance] ❌ Erreur sauvegarde résonance:', error);
    throw error;
  }
}

/**
 * Récupère la réponse du jour (si elle existe)
 */
export async function getTodayResonance(): Promise<DailyResonance | null> {
  try {
    const stored = await AsyncStorage.getItem(STORAGE_KEYS.DAILY_RESONANCE);
    if (!stored) return null;

    const resonance: DailyResonance = JSON.parse(stored);
    const today = getCurrentDate();

    // Retourner seulement si c'est la réponse d'aujourd'hui
    if (resonance.date === today) {
      return resonance;
    }

    return null;
  } catch (error) {
    console.error('[DailyResonance] Erreur lecture résonance:', error);
    return null;
  }
}
