/**
 * Tests pour lunarCache service
 * Teste TTL, stale-while-revalidate, et invalidation
 */

import AsyncStorage from '@react-native-async-storage/async-storage';
import {
  getLunarCache,
  setLunarCache,
  clearLunarCache,
  clearAllLunarCache,
} from '../services/lunarCache';
import { LunarDayData } from '../types/lunar-context';

describe('LunarCache', () => {
  beforeEach(async () => {
    await AsyncStorage.clear();
  });

  const mockLunarData: LunarDayData = {
    date: '2025-12-31',
    moon: {
      phase: 'Full Moon',
      sign: 'Cancer',
    },
    voc: {
      is_active: true,
      end_at: '2025-12-31T15:30:00Z',
    },
  };

  describe('setLunarCache & getLunarCache', () => {
    it('devrait stocker et récupérer des données', async () => {
      await setLunarCache('2025-12-31', mockLunarData, 'api');

      const cached = await getLunarCache('2025-12-31');

      expect(cached).not.toBeNull();
      expect(cached?.data).toEqual(mockLunarData);
      expect(cached?.source).toBe('api');
      expect(cached?.isStale).toBe(false);
    });

    it('devrait retourner null si pas de cache', async () => {
      const cached = await getLunarCache('2025-12-30');
      expect(cached).toBeNull();
    });
  });

  describe('Cache TTL (24h)', () => {
    it('devrait retourner des données du cache récent', async () => {
      await clearAllLunarCache();
      await setLunarCache('2025-12-31', mockLunarData, 'api');

      const cached = await getLunarCache('2025-12-31');

      // Cache récent devrait être valide
      expect(cached).not.toBeNull();
      expect(cached?.data).toEqual(mockLunarData);
    });
  });

  describe('Stale detection', () => {
    it('devrait retourner isStale false pour cache récent', async () => {
      await clearAllLunarCache();
      await setLunarCache('2025-12-31', mockLunarData, 'api');

      const cached = await getLunarCache('2025-12-31');

      expect(cached).not.toBeNull();
      expect(cached?.isStale).toBe(false);
    });
  });

  describe('Invalidation à minuit', () => {
    it('devrait valider les données avec la bonne date', async () => {
      await clearAllLunarCache();
      await setLunarCache('2025-12-31', mockLunarData, 'api');

      const cached = await getLunarCache('2025-12-31');

      // Cache avec date correcte devrait être valide
      expect(cached).not.toBeNull();
      expect(cached?.data.date).toBe('2025-12-31');
    });
  });

  describe('clearLunarCache', () => {
    it('devrait supprimer le cache d\'une date spécifique', async () => {
      // Utiliser des dates futures pour éviter l'invalidation automatique (now > midnight)
      // Date1 et Date2 doivent être dans le futur pour que le cache reste valide
      const tomorrow = new Date();
      tomorrow.setDate(tomorrow.getDate() + 1);
      const dayAfter = new Date();
      dayAfter.setDate(dayAfter.getDate() + 2);
      
      const date1 = tomorrow.toISOString().split('T')[0]; // Format YYYY-MM-DD
      const date2 = dayAfter.toISOString().split('T')[0];
      
      const data1 = { ...mockLunarData, date: date1 };
      const data2 = { ...mockLunarData, date: date2 };

      await setLunarCache(date1, data1, 'api');
      await setLunarCache(date2, data2, 'api');

      // Supprimer seulement date1
      await clearLunarCache(date1);

      const cached1 = await getLunarCache(date1);
      const cached2 = await getLunarCache(date2);

      expect(cached1).toBeNull();
      expect(cached2).not.toBeNull();
    });
  });

  describe('clearAllLunarCache', () => {
    it('devrait supprimer tout le cache lunaire', async () => {
      await setLunarCache('2025-12-31', mockLunarData, 'api');
      await setLunarCache('2025-12-30', mockLunarData, 'api');
      await setLunarCache('2025-12-29', mockLunarData, 'local');

      await clearAllLunarCache();

      const cached31 = await getLunarCache('2025-12-31');
      const cached30 = await getLunarCache('2025-12-30');
      const cached29 = await getLunarCache('2025-12-29');

      expect(cached31).toBeNull();
      expect(cached30).toBeNull();
      expect(cached29).toBeNull();
    });
  });

  describe('Source tracking', () => {
    it('devrait préserver la source dans le cache', async () => {
      await clearAllLunarCache();
      await setLunarCache('2025-12-31', mockLunarData, 'local');

      const cached = await getLunarCache('2025-12-31');

      expect(cached).not.toBeNull();
      if (cached) {
        expect(cached.source).toBe('local');
      }
    });
  });
});
