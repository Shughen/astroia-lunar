/**
 * Service de génération de Timeline Lunaire V2
 * Utilise LunarContext pour obtenir les données lunaires
 * Simplifié par rapport à V1
 */

import { TimelineDay, TimelineDayType, TimelineConfig } from '../types/timeline';
import { LunarDayData } from '../types/lunar-context';
import { hasJournalEntry } from './journalService';
import { getTodayDateString } from '../utils/ritualHelpers';

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
 * Vérifie si un jour a un VoC actif (simplifié pour V1)
 */
function hasVocForDate(_date: string): boolean {
  // TODO: Intégrer avec l'API VoC si nécessaire
  return false;
}

/**
 * Génère la timeline complète en utilisant getDayData du LunarContext
 * @param getDayData - Fonction du LunarContext pour récupérer données d'un jour
 */
export async function generateTimelineV2(
  getDayData: (date: string) => Promise<LunarDayData>,
  config?: Partial<TimelineConfig>
): Promise<TimelineDay[]> {
  const today = getTodayDateString();
  const daysBefore = config?.daysBefore ?? 14;
  const daysAfter = config?.daysAfter ?? 14;

  const timeline: TimelineDay[] = [];

  // Générer les jours (du plus ancien au plus récent)
  for (let offset = -daysBefore; offset <= daysAfter; offset++) {
    const date = addDays(today, offset);
    const type = getDayType(date, today);

    // Récupérer données lunaires via context
    const lunarData = await getDayData(date);

    // Vérifier si journal existe
    const hasJournal = await hasJournalEntry(date);

    // VoC pour V1 (simplifié)
    const hasVoc = lunarData.voc?.is_active || hasVocForDate(date);

    timeline.push({
      date,
      type,
      moon: lunarData.moon,
      hasVoc,
      hasJournalEntry: hasJournal,
    });
  }

  return timeline;
}

/**
 * Rafraîchit les indicateurs journal pour la timeline
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
