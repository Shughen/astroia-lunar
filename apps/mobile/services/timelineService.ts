/**
 * Service de génération de Timeline Lunaire
 * Génère une liste de jours avec contexte lunaire et indicateurs journal
 */

import { TimelineDay, TimelineDayType, TimelineConfig } from '../types/timeline';
import { MoonPhase } from '../types/ritual';
import { hasJournalEntry } from './journalService';
import { getTodayDateString } from '../utils/ritualHelpers';
import { calculateLocalMoonPhase, calculateLocalMoonSign } from '../utils/moonCalc';
import { lunaPack } from './api';

/**
 * Ajoute ou soustrait des jours à une date YYYY-MM-DD
 */
function addDays(dateString: string, days: number): string {
  const date = new Date(dateString);
  date.setDate(date.getDate() + days);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

/**
 * Détermine le type de jour (passé, aujourd'hui, futur)
 */
function getDayType(date: string, today: string): TimelineDayType {
  if (date === today) return 'today';
  if (date < today) return 'past';
  return 'future';
}

/**
 * Calcule approximativement la phase et le signe lunaire pour une date donnée
 * Utilise les fonctions centralisées de utils/moonCalc.ts
 */
function calculateMoonDataForDate(date: string): { phase: MoonPhase; sign: string } {
  // Parse date to ensure consistent calculation (noon UTC to avoid timezone issues)
  const targetDate = new Date(date + 'T12:00:00Z');

  return {
    phase: calculateLocalMoonPhase(targetDate),
    sign: calculateLocalMoonSign(targetDate),
  };
}

/**
 * Récupère les données lunaires pour une date via API (aujourd'hui uniquement)
 * Fallback sur calcul local si API indisponible
 */
async function getMoonDataForDate(date: string): Promise<{ phase: MoonPhase; sign: string }> {
  const today = getTodayDateString();

  // API uniquement pour aujourd'hui
  if (date === today) {
    try {
      const result = await lunaPack.getCurrentMoonPosition();
      // Convertir la phase de l'API (format français) vers MoonPhase (format anglais)
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

      const phase = phaseMap[result.phase] || calculateMoonDataForDate(date).phase;

      return {
        phase,
        sign: result.sign,
      };
    } catch (error) {
      // Fallback sur calcul local
      console.log('[Timeline] API unavailable for today, using local calculation');
      return calculateMoonDataForDate(date);
    }
  }

  // Pour les autres dates : calcul local uniquement
  return calculateMoonDataForDate(date);
}

/**
 * Vérifie si un jour a un VoC actif (simplifié pour V1)
 * Pour l'instant retourne false, peut être enrichi plus tard avec API VoC
 */
function hasVocForDate(_date: string): boolean {
  // TODO: Intégrer avec l'API VoC si nécessaire
  // Pour V1, on simplifie en retournant false
  return false;
}

/**
 * Génère la timeline complète avec tous les jours
 * Version optimisée : appel API uniquement pour aujourd'hui, calcul local pour le reste
 */
export async function generateTimeline(config?: Partial<TimelineConfig>): Promise<TimelineDay[]> {
  const today = getTodayDateString();
  const daysBefore = config?.daysBefore ?? 14;
  const daysAfter = config?.daysAfter ?? 14;

  const timeline: TimelineDay[] = [];

  // Récupérer les données lunaires pour aujourd'hui via API (avec fallback)
  const todayMoonData = await getMoonDataForDate(today);

  // Générer les jours (du plus ancien au plus récent)
  for (let offset = -daysBefore; offset <= daysAfter; offset++) {
    const date = addDays(today, offset);
    const type = getDayType(date, today);

    // Pour aujourd'hui, utiliser les données de l'API
    // Pour les autres jours, calculer localement pour éviter trop d'appels API
    const moonData = offset === 0 ? todayMoonData : calculateMoonDataForDate(date);

    // Vérifier si journal existe (async)
    const hasJournal = await hasJournalEntry(date);

    // VoC pour V1 (simplifié)
    const hasVoc = hasVocForDate(date);

    timeline.push({
      date,
      type,
      moon: moonData,
      hasVoc,
      hasJournalEntry: hasJournal,
    });
  }

  return timeline;
}

/**
 * Génère uniquement les dates de la timeline (sans appels async)
 * Utile pour FlatList initialData
 */
export function generateTimelineDates(config?: Partial<TimelineConfig>): string[] {
  const today = getTodayDateString();
  const daysBefore = config?.daysBefore ?? 14;
  const daysAfter = config?.daysAfter ?? 14;

  const dates: string[] = [];
  for (let offset = -daysBefore; offset <= daysAfter; offset++) {
    dates.push(addDays(today, offset));
  }
  return dates;
}

/**
 * Rafraîchit les indicateurs journal pour la timeline
 * (utile après création/suppression d'une entrée)
 */
export async function refreshTimelineJournalIndicators(
  timeline: TimelineDay[]
): Promise<TimelineDay[]> {
  const refreshed = await Promise.all(
    timeline.map(async (day) => ({
      ...day,
      hasJournalEntry: await hasJournalEntry(day.date),
    }))
  );
  return refreshed;
}
