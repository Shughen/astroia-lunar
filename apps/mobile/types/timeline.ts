/**
 * Types pour la Timeline Lunaire
 */

import { MoonPhase } from './ritual';

/**
 * Type de jour dans la timeline (passé, présent, futur)
 */
export type TimelineDayType = 'past' | 'today' | 'future';

/**
 * Jour de la timeline avec contexte lunaire et journal
 */
export interface TimelineDay {
  date: string; // YYYY-MM-DD
  type: TimelineDayType;

  // Contexte lunaire
  moon: {
    phase: MoonPhase;
    sign: string; // "Aquarius", "Taurus", etc.
  };

  // VoC actif ce jour-là
  hasVoc: boolean;

  // Indicateur d'entrée journal
  hasJournalEntry: boolean;

  // Label relatif (Aujourd'hui, Hier, Demain, etc.)
  relativeLabel?: string;
}

/**
 * Configuration pour la génération de timeline
 */
export interface TimelineConfig {
  centerDate: string; // YYYY-MM-DD - Date centrale (généralement aujourd'hui)
  daysBefore: number; // Nombre de jours avant
  daysAfter: number; // Nombre de jours après
}
