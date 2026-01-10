/**
 * Tests unitaires pour utils/astrology-format.ts
 */

import { formatAspects, parseInterpretation } from '../utils/astrology-format';
import type { Aspect } from '../types/api';

describe('astrology-format utils', () => {
  describe('formatAspects', () => {
    it('should return empty array for undefined aspects', () => {
      const result = formatAspects(undefined);
      expect(result).toEqual([]);
    });

    it('should return empty array for empty aspects', () => {
      const result = formatAspects([]);
      expect(result).toEqual([]);
    });

    it('should format aspect with planet1/planet2', () => {
      const aspects: Aspect[] = [
        {
          planet1: 'Sun',
          planet2: 'Moon',
          type: 'conjunction',
          orb: 2.5,
        },
      ];
      const result = formatAspects(aspects);
      expect(result).toHaveLength(1);
      expect(result[0]).toBe('Sun conjunction Moon, orb 2.5°');
    });

    it('should format aspect with planet_1/planet_2 (alternative naming)', () => {
      const aspects: Aspect[] = [
        {
          planet_1: 'Venus',
          planet_2: 'Mars',
          aspect_type: 'trine',
          orb: 1.2,
        },
      ];
      const result = formatAspects(aspects);
      expect(result).toHaveLength(1);
      expect(result[0]).toBe('Venus trine Mars, orb 1.2°');
    });

    it('should format aspect without orb', () => {
      const aspects: Aspect[] = [
        {
          planet1: 'Jupiter',
          planet2: 'Saturn',
          type: 'square',
        },
      ];
      const result = formatAspects(aspects);
      expect(result).toHaveLength(1);
      expect(result[0]).toBe('Jupiter square Saturn');
    });

    it('should handle multiple aspects', () => {
      const aspects: Aspect[] = [
        { planet1: 'Sun', planet2: 'Moon', type: 'opposition', orb: 3.0 },
        { planet1: 'Venus', planet2: 'Mars', type: 'sextile', orb: 1.5 },
      ];
      const result = formatAspects(aspects);
      expect(result).toHaveLength(2);
      expect(result[0]).toContain('Sun');
      expect(result[1]).toContain('Venus');
    });
  });

  describe('parseInterpretation', () => {
    it('should return empty array for undefined text', () => {
      const result = parseInterpretation(undefined);
      expect(result).toEqual([]);
    });

    it('should return empty array for empty text', () => {
      const result = parseInterpretation('');
      expect(result).toEqual([]);
    });

    it('should parse simple text without markdown', () => {
      const result = parseInterpretation('Simple text paragraph.');
      expect(result).toHaveLength(1);
      expect(result[0].type).toBe('paragraph');
      expect(result[0].parts).toHaveLength(1);
      expect(result[0].parts[0].type).toBe('text');
      expect(result[0].parts[0].content).toBe('Simple text paragraph.');
    });

    it('should parse text with bold markers', () => {
      const result = parseInterpretation('This is **bold** text.');
      expect(result).toHaveLength(1);
      expect(result[0].parts).toHaveLength(3);
      expect(result[0].parts[0].type).toBe('text');
      expect(result[0].parts[0].content).toBe('This is ');
      expect(result[0].parts[1].type).toBe('bold');
      expect(result[0].parts[1].content).toBe('bold');
      expect(result[0].parts[2].type).toBe('text');
      expect(result[0].parts[2].content).toBe(' text.');
    });

    it('should parse multiple paragraphs', () => {
      const text = 'First paragraph.\n\nSecond paragraph.';
      const result = parseInterpretation(text);
      expect(result).toHaveLength(2);
      expect(result[0].parts[0].content).toBe('First paragraph.');
      expect(result[1].parts[0].content).toBe('Second paragraph.');
    });

    it('should parse complex text with multiple bold sections', () => {
      const text = '**Bold start** middle **bold end**.';
      const result = parseInterpretation(text);
      expect(result).toHaveLength(1);
      expect(result[0].parts).toHaveLength(4);
      expect(result[0].parts[0].type).toBe('bold');
      expect(result[0].parts[1].type).toBe('text');
      expect(result[0].parts[2].type).toBe('bold');
      expect(result[0].parts[3].type).toBe('text');
    });

    it('should have unique keys for each part', () => {
      const text = 'Text with **bold** and more **bold**.';
      const result = parseInterpretation(text);
      const keys = result[0].parts.map((p) => p.key);
      const uniqueKeys = new Set(keys);
      expect(uniqueKeys.size).toBe(keys.length);
    });
  });
});
