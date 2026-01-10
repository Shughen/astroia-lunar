/**
 * Tests pour le service Journal Lunaire
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import {
  getJournalEntry,
  saveJournalEntry,
  deleteJournalEntry,
  hasJournalEntry,
  getAllJournalEntries,
  getJournalEntriesCount,
} from '../services/journalService';
import { CreateJournalEntryPayload } from '../types/journal';

// Mock AsyncStorage
jest.mock('@react-native-async-storage/async-storage', () => ({
  getItem: jest.fn(),
  setItem: jest.fn(),
  removeItem: jest.fn(),
  getAllKeys: jest.fn(),
  multiGet: jest.fn(),
}));

describe('journalService', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('getJournalEntry', () => {
    it('should return null when entry does not exist', async () => {
      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(null);

      const result = await getJournalEntry('2025-12-31');

      expect(result.exists).toBe(false);
      expect(result.entry).toBeNull();
      expect(AsyncStorage.getItem).toHaveBeenCalledWith(
        'journal_entry_2025-12-31'
      );
    });

    it('should return entry when it exists', async () => {
      const mockEntry = {
        date: '2025-12-31',
        text: 'Test entry',
        createdAt: 1735660800000,
        updatedAt: 1735660800000,
        moonContext: {
          phase: 'Full Moon',
          sign: 'Scorpio',
        },
      };

      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(
        JSON.stringify(mockEntry)
      );

      const result = await getJournalEntry('2025-12-31');

      expect(result.exists).toBe(true);
      expect(result.entry).toEqual(mockEntry);
    });
  });

  describe('saveJournalEntry', () => {
    it('should create new entry', async () => {
      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(null);
      (AsyncStorage.setItem as jest.Mock).mockResolvedValue(undefined);

      const payload: CreateJournalEntryPayload = {
        date: '2025-12-31',
        text: 'New entry',
        moonContext: {
          phase: 'New Moon',
          sign: 'Aquarius',
        },
      };

      const result = await saveJournalEntry(payload);

      expect(result.date).toBe('2025-12-31');
      expect(result.text).toBe('New entry');
      expect(result.moonContext).toEqual(payload.moonContext);
      expect(result.createdAt).toBeDefined();
      expect(result.updatedAt).toBeDefined();
      expect(AsyncStorage.setItem).toHaveBeenCalled();
    });

    it('should update existing entry', async () => {
      const existingEntry = {
        date: '2025-12-31',
        text: 'Old text',
        createdAt: 1735660800000,
        updatedAt: 1735660800000,
        moonContext: {
          phase: 'Full Moon',
          sign: 'Scorpio',
        },
      };

      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(
        JSON.stringify(existingEntry)
      );
      (AsyncStorage.setItem as jest.Mock).mockResolvedValue(undefined);

      const payload: CreateJournalEntryPayload = {
        date: '2025-12-31',
        text: 'Updated text',
        moonContext: existingEntry.moonContext,
      };

      const result = await saveJournalEntry(payload);

      expect(result.text).toBe('Updated text');
      expect(result.createdAt).toBe(existingEntry.createdAt); // Preserved
      expect(result.updatedAt).toBeGreaterThan(existingEntry.updatedAt); // Updated
    });
  });

  describe('deleteJournalEntry', () => {
    it('should delete entry', async () => {
      (AsyncStorage.removeItem as jest.Mock).mockResolvedValue(undefined);

      await deleteJournalEntry('2025-12-31');

      expect(AsyncStorage.removeItem).toHaveBeenCalledWith(
        'journal_entry_2025-12-31'
      );
    });
  });

  describe('hasJournalEntry', () => {
    it('should return true if entry exists', async () => {
      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(
        JSON.stringify({ date: '2025-12-31', text: 'Test' })
      );

      const result = await hasJournalEntry('2025-12-31');

      expect(result).toBe(true);
    });

    it('should return false if entry does not exist', async () => {
      (AsyncStorage.getItem as jest.Mock).mockResolvedValue(null);

      const result = await hasJournalEntry('2025-12-31');

      expect(result).toBe(false);
    });
  });

  describe('getAllJournalEntries', () => {
    it('should return empty array when no entries', async () => {
      (AsyncStorage.getAllKeys as jest.Mock).mockResolvedValue([]);

      const result = await getAllJournalEntries();

      expect(result).toEqual([]);
    });

    it('should return all entries sorted by date desc', async () => {
      const entry1 = {
        date: '2025-12-30',
        text: 'Entry 1',
        createdAt: 1735574400000,
        updatedAt: 1735574400000,
        moonContext: { phase: 'New Moon', sign: 'Capricorn' },
      };
      const entry2 = {
        date: '2025-12-31',
        text: 'Entry 2',
        createdAt: 1735660800000,
        updatedAt: 1735660800000,
        moonContext: { phase: 'Full Moon', sign: 'Scorpio' },
      };

      (AsyncStorage.getAllKeys as jest.Mock).mockResolvedValue([
        'journal_entry_2025-12-30',
        'journal_entry_2025-12-31',
        'other_key',
      ]);

      (AsyncStorage.multiGet as jest.Mock).mockResolvedValue([
        ['journal_entry_2025-12-30', JSON.stringify(entry1)],
        ['journal_entry_2025-12-31', JSON.stringify(entry2)],
      ]);

      const result = await getAllJournalEntries();

      expect(result).toHaveLength(2);
      expect(result[0].date).toBe('2025-12-31'); // Most recent first
      expect(result[1].date).toBe('2025-12-30');
    });
  });

  describe('getJournalEntriesCount', () => {
    it('should return count of journal entries', async () => {
      (AsyncStorage.getAllKeys as jest.Mock).mockResolvedValue([
        'journal_entry_2025-12-30',
        'journal_entry_2025-12-31',
        'other_key',
      ]);

      const result = await getJournalEntriesCount();

      expect(result).toBe(2);
    });

    it('should return 0 when no entries', async () => {
      (AsyncStorage.getAllKeys as jest.Mock).mockResolvedValue([]);

      const result = await getJournalEntriesCount();

      expect(result).toBe(0);
    });
  });
});
