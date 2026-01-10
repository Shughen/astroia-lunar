/**
 * Tests pour les helpers de la carte Rituel Quotidien
 */

import {
  getPhaseEmoji,
  getPhaseKey,
  formatTime,
  formatCacheDate,
  getTodayDateString,
  calculateLocalPhase,
} from '../utils/ritualHelpers';
import { MoonPhase } from '../types/ritual';

describe('ritualHelpers', () => {
  describe('getPhaseEmoji', () => {
    it('should return correct emoji for New Moon', () => {
      expect(getPhaseEmoji('New Moon')).toBe('🌑');
    });

    it('should return correct emoji for Full Moon', () => {
      expect(getPhaseEmoji('Full Moon')).toBe('🌕');
    });

    it('should return correct emoji for First Quarter', () => {
      expect(getPhaseEmoji('First Quarter')).toBe('🌓');
    });

    it('should return default emoji for unknown phase', () => {
      expect(getPhaseEmoji('Unknown Phase' as MoonPhase)).toBe('🌑');
    });
  });

  describe('getPhaseKey', () => {
    it('should convert phase to snake_case key', () => {
      expect(getPhaseKey('New Moon')).toBe('new_moon');
      expect(getPhaseKey('Waxing Crescent')).toBe('waxing_crescent');
      expect(getPhaseKey('Full Moon')).toBe('full_moon');
    });
  });

  describe('formatTime', () => {
    it('should format ISO time to HH:mm', () => {
      const isoString = '2025-12-31T14:32:00Z';
      const result = formatTime(isoString);
      // Note: résultat dépend du timezone local
      expect(result).toMatch(/^\d{1,2}h\d{2}$/);
    });
  });

  describe('formatCacheDate', () => {
    it('should format timestamp to short date (FR)', () => {
      const timestamp = new Date('2025-12-31').getTime();
      const result = formatCacheDate(timestamp, 'fr');
      // Format: "31 déc."
      expect(result).toMatch(/^\d{1,2} .+\.$/);
    });

    it('should format timestamp to short date (EN)', () => {
      const timestamp = new Date('2025-12-31').getTime();
      const result = formatCacheDate(timestamp, 'en');
      // Format: "31 Dec."
      expect(result).toMatch(/^\d{1,2} .+\.$/);
    });
  });

  describe('getTodayDateString', () => {
    it('should return date in YYYY-MM-DD format', () => {
      const result = getTodayDateString();
      expect(result).toMatch(/^\d{4}-\d{2}-\d{2}$/);
    });

    it('should return current date', () => {
      const result = getTodayDateString();
      const today = new Date();
      const expected = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;
      expect(result).toBe(expected);
    });
  });

  describe('calculateLocalPhase', () => {
    it('should return a valid MoonPhase', () => {
      const result = calculateLocalPhase();
      const validPhases: MoonPhase[] = [
        'New Moon',
        'Waxing Crescent',
        'First Quarter',
        'Waxing Gibbous',
        'Full Moon',
        'Waning Gibbous',
        'Last Quarter',
        'Waning Crescent',
      ];
      expect(validPhases).toContain(result);
    });

    it('should be deterministic for same date', () => {
      const phase1 = calculateLocalPhase();
      const phase2 = calculateLocalPhase();
      expect(phase1).toBe(phase2);
    });
  });
});
