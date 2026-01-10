/**
 * Types pour le Journal Lunaire
 */

import { MoonPhase } from './ritual';

/**
 * Entrée de journal quotidienne
 */
export interface JournalEntry {
  date: string; // YYYY-MM-DD (date locale)
  text: string; // Texte libre utilisateur
  createdAt: number; // Timestamp de création
  updatedAt: number; // Timestamp dernière modification

  // Contexte lunaire (snapshot du jour)
  moonContext: {
    phase: MoonPhase;
    sign: string; // Ex: "Aquarius" ou "Unknown"
  };
}

/**
 * Payload pour créer/mettre à jour une entrée
 */
export interface CreateJournalEntryPayload {
  date: string; // YYYY-MM-DD
  text: string;
  moonContext: {
    phase: MoonPhase;
    sign: string;
  };
}

/**
 * Résultat de lecture d'entrée
 */
export interface GetJournalEntryResult {
  exists: boolean;
  entry: JournalEntry | null;
}
