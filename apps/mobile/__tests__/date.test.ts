/**
 * Tests unitaires pour utils/date.ts
 */

import { formatDate, getDaysUntil, formatDaysUntil } from '../utils/date';

describe('date utils', () => {
  describe('formatDate', () => {
    it('should format ISO date to French format', () => {
      const result = formatDate('2025-01-15T14:30:00');
      expect(result).toContain('janvier');
      expect(result).toContain('2025');
      expect(result).toContain('14');
      expect(result).toContain('30');
    });

    it('should handle different months', () => {
      const result = formatDate('2024-12-25T12:00:00');
      expect(result).toContain('décembre');
      expect(result).toContain('2024');
    });
  });

  describe('getDaysUntil', () => {
    it('should return positive days for future dates', () => {
      const tomorrow = new Date();
      tomorrow.setDate(tomorrow.getDate() + 1);
      const result = getDaysUntil(tomorrow.toISOString());
      expect(result).toBeGreaterThanOrEqual(1);
    });

    it('should return negative days for past dates', () => {
      const yesterday = new Date();
      yesterday.setDate(yesterday.getDate() - 1);
      const result = getDaysUntil(yesterday.toISOString());
      expect(result).toBeLessThanOrEqual(-1);
    });

    it('should return 0 or 1 for today', () => {
      const today = new Date();
      const result = getDaysUntil(today.toISOString());
      expect(result).toBeGreaterThanOrEqual(0);
      expect(result).toBeLessThanOrEqual(1);
    });
  });

  describe('formatDaysUntil', () => {
    it('should return "aujourd\'hui" for 0 days', () => {
      expect(formatDaysUntil(0)).toBe("aujourd'hui");
    });

    it('should return "demain" for 1 day', () => {
      expect(formatDaysUntil(1)).toBe('demain');
    });

    it('should return "hier" for -1 day', () => {
      expect(formatDaysUntil(-1)).toBe('hier');
    });

    it('should format positive days correctly', () => {
      expect(formatDaysUntil(5)).toBe('dans 5 jours');
      expect(formatDaysUntil(2)).toBe('dans 2 jours');
    });

    it('should format negative days correctly', () => {
      expect(formatDaysUntil(-5)).toBe('il y a 5 jours');
      expect(formatDaysUntil(-2)).toBe('il y a 2 jours');
    });
  });
});
