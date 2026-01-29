/**
 * Service de stockage du Journal Lunaire
 * CRUD via API backend
 */

import {
  JournalEntry,
  CreateJournalEntryPayload,
  GetJournalEntryResult,
} from '../types/journal';
import { journal as journalApi } from './api';

/**
 * Convertit une entrée backend vers le format frontend
 */
function mapBackendEntryToFrontend(backendEntry: any): JournalEntry {
  return {
    id: backendEntry.id, // ID backend pour suppression
    date: backendEntry.date,
    text: backendEntry.note || '',
    createdAt: new Date(backendEntry.created_at).getTime(),
    updatedAt: backendEntry.updated_at ? new Date(backendEntry.updated_at).getTime() : new Date(backendEntry.created_at).getTime(),
    moonContext: {
      phase: 'New Moon', // Valeur par défaut, à recalculer côté frontend si besoin
      sign: 'Unknown',
    },
  };
}

/**
 * Récupère l'entrée de journal pour une date donnée
 */
export async function getJournalEntry(
  date: string
): Promise<GetJournalEntryResult> {
  try {
    // Récupérer toutes les entrées et filtrer par date
    // Note: L'API ne fournit pas d'endpoint GET /entry/{date}, on passe par /entries
    const response = await journalApi.getEntries({ limit: 1000 });
    const entries = response.entries || [];

    const matchingEntry = entries.find((e: any) => e.date === date);

    if (!matchingEntry) {
      return { exists: false, entry: null };
    }

    const entry = mapBackendEntryToFrontend(matchingEntry);
    return { exists: true, entry };
  } catch (error) {
    console.error('[JournalService] Error reading entry:', error);
    return { exists: false, entry: null };
  }
}

/**
 * Crée ou met à jour une entrée de journal
 */
export async function saveJournalEntry(
  payload: CreateJournalEntryPayload
): Promise<JournalEntry> {
  try {
    // Appel API pour créer/mettre à jour
    const backendEntry = await journalApi.createEntry({
      date: payload.date,
      note: payload.text,
      // Le backend peut gérer le champ month si besoin (format YYYY-MM)
      month: payload.date.substring(0, 7), // Ex: "2026-01-16" -> "2026-01"
    });

    // Convertir en format frontend
    return mapBackendEntryToFrontend(backendEntry);
  } catch (error) {
    console.error('[JournalService] Error saving entry:', error);
    throw error;
  }
}

/**
 * Supprime une entrée de journal par son ID
 */
export async function deleteJournalEntry(entryId: number): Promise<void> {
  try {
    await journalApi.deleteEntry(entryId);
  } catch (error) {
    console.error('[JournalService] Error deleting entry:', error);
    throw error;
  }
}

/**
 * Vérifie si une entrée existe pour une date donnée
 */
export async function hasJournalEntry(date: string): Promise<boolean> {
  const result = await getJournalEntry(date);
  return result.exists;
}

/**
 * Récupère toutes les entrées de journal
 */
export async function getAllJournalEntries(): Promise<JournalEntry[]> {
  try {
    const response = await journalApi.getEntries({ limit: 1000 });
    const entries = response.entries || [];

    // Convertir toutes les entrées backend vers format frontend
    const frontendEntries = entries.map(mapBackendEntryToFrontend);

    // Trier par createdAt décroissant (plus récent en premier)
    return frontendEntries.sort((a, b) => b.createdAt - a.createdAt);
  } catch (error) {
    console.error('[JournalService] Error reading all entries:', error);
    return [];
  }
}

/**
 * Compte le nombre total d'entrées
 */
export async function getJournalEntriesCount(): Promise<number> {
  try {
    const response = await journalApi.getEntries({ limit: 1 });
    return response.total || 0;
  } catch (error) {
    console.error('[JournalService] Error counting entries:', error);
    return 0;
  }
}
