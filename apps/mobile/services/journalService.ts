/**
 * Service de stockage du Journal Lunaire
 * CRUD simple avec AsyncStorage
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import {
  JournalEntry,
  CreateJournalEntryPayload,
  GetJournalEntryResult,
} from '../types/journal';

const JOURNAL_ENTRY_PREFIX = 'journal_entry_';

/**
 * Génère la clé AsyncStorage pour une date donnée
 */
function getEntryKey(date: string): string {
  return `${JOURNAL_ENTRY_PREFIX}${date}`;
}

/**
 * Récupère l'entrée de journal pour une date donnée
 */
export async function getJournalEntry(
  date: string
): Promise<GetJournalEntryResult> {
  try {
    const key = getEntryKey(date);
    const raw = await AsyncStorage.getItem(key);

    if (!raw) {
      return { exists: false, entry: null };
    }

    const entry: JournalEntry = JSON.parse(raw);
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
    const key = getEntryKey(payload.date);
    const now = Date.now();

    // Vérifier si entrée existe déjà
    const existing = await getJournalEntry(payload.date);

    const entry: JournalEntry = {
      date: payload.date,
      text: payload.text,
      moonContext: payload.moonContext,
      createdAt: existing.entry?.createdAt || now,
      updatedAt: now,
    };

    await AsyncStorage.setItem(key, JSON.stringify(entry));
    return entry;
  } catch (error) {
    console.error('[JournalService] Error saving entry:', error);
    throw error;
  }
}

/**
 * Supprime une entrée de journal
 */
export async function deleteJournalEntry(date: string): Promise<void> {
  try {
    const key = getEntryKey(date);
    await AsyncStorage.removeItem(key);
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
 * Récupère toutes les entrées de journal (Phase 2)
 * Note: Scan toutes les clés AsyncStorage avec prefix
 * Performance acceptable pour < 1000 entrées
 */
export async function getAllJournalEntries(): Promise<JournalEntry[]> {
  try {
    const allKeys = await AsyncStorage.getAllKeys();
    const journalKeys = allKeys.filter((key) =>
      key.startsWith(JOURNAL_ENTRY_PREFIX)
    );

    if (journalKeys.length === 0) {
      return [];
    }

    const entries = await AsyncStorage.multiGet(journalKeys);
    const parsed: JournalEntry[] = entries
      .map(([_, value]) => {
        if (value) {
          try {
            return JSON.parse(value) as JournalEntry;
          } catch {
            return null;
          }
        }
        return null;
      })
      .filter((entry): entry is JournalEntry => entry !== null);

    // Trier par date décroissante (plus récent en premier)
    return parsed.sort((a, b) => b.date.localeCompare(a.date));
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
    const allKeys = await AsyncStorage.getAllKeys();
    const journalKeys = allKeys.filter((key) =>
      key.startsWith(JOURNAL_ENTRY_PREFIX)
    );
    return journalKeys.length;
  } catch (error) {
    console.error('[JournalService] Error counting entries:', error);
    return 0;
  }
}
