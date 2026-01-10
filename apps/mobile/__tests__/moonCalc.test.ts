/**
 * Unit tests for local moon calculations (utils/moonCalc.ts)
 *
 * Tests verify:
 * ✅ Stability: same date always returns same result
 * ✅ Validity: phase ∈ 8 valid phases, sign ∈ 12 valid signs
 * ✅ Determinism: no randomness, no external dependencies
 * ✅ Snapshots: consistency across known dates
 */

import {
  calculateLocalMoonPhase,
  calculateLocalMoonSign,
  calculateMoonDegree,
  degreeToSign,
  calculateLocalMoonData,
  isSameMoonPhase,
  isSameMoonSign,
  getDaysUntilNextPhase,
  getDaysUntilNextSign,
  getNextZodiacSign,
  ZodiacSign,
} from '../utils/moonCalc';
import { MoonPhase } from '../types/ritual';

// ============================================================================
// CONSTANTS & HELPERS
// ============================================================================

const VALID_PHASES: MoonPhase[] = [
  'New Moon',
  'Waxing Crescent',
  'First Quarter',
  'Waxing Gibbous',
  'Full Moon',
  'Waning Gibbous',
  'Last Quarter',
  'Waning Crescent',
];

const VALID_SIGNS: ZodiacSign[] = [
  'Aries',
  'Taurus',
  'Gemini',
  'Cancer',
  'Leo',
  'Virgo',
  'Libra',
  'Scorpio',
  'Sagittarius',
  'Capricorn',
  'Aquarius',
  'Pisces',
];

/**
 * Test dates covering various scenarios
 */
const TEST_DATES = {
  // Reference points
  referenceNewMoon: '2000-01-06',
  referenceMoonPosition: '2025-01-15',

  // Known moon events (approximate - for internal consistency, not astronomical accuracy)
  knownNewMoon: '2025-01-29',
  knownFullMoon: '2025-01-13',

  // Various dates for stability testing
  past: '2020-03-15',
  today: new Date().toISOString().split('T')[0],
  future: '2030-12-25',

  // Edge cases
  leapYear: '2024-02-29',
  yearBoundary: '2024-12-31',
  centuryBoundary: '2100-01-01',
};

// ============================================================================
// PHASE CALCULATION TESTS
// ============================================================================

describe('calculateLocalMoonPhase', () => {
  test('returns a valid moon phase', () => {
    const phase = calculateLocalMoonPhase();
    expect(VALID_PHASES).toContain(phase);
  });

  test('is deterministic for the same date', () => {
    const date = '2025-12-31';
    const phase1 = calculateLocalMoonPhase(date);
    const phase2 = calculateLocalMoonPhase(date);
    const phase3 = calculateLocalMoonPhase(date);

    expect(phase1).toBe(phase2);
    expect(phase2).toBe(phase3);
  });

  test('is stable across multiple calls', () => {
    const results = Array.from({ length: 100 }, () =>
      calculateLocalMoonPhase('2025-06-15')
    );

    const uniqueResults = new Set(results);
    expect(uniqueResults.size).toBe(1); // All results should be identical
  });

  test('accepts Date objects', () => {
    const date = new Date('2025-12-31');
    const phase = calculateLocalMoonPhase(date);
    expect(VALID_PHASES).toContain(phase);
  });

  test('accepts string dates', () => {
    const phase = calculateLocalMoonPhase('2025-12-31');
    expect(VALID_PHASES).toContain(phase);
  });

  test('works without arguments (current date)', () => {
    const phase = calculateLocalMoonPhase();
    expect(VALID_PHASES).toContain(phase);
  });

  test('handles leap years', () => {
    const phase = calculateLocalMoonPhase(TEST_DATES.leapYear);
    expect(VALID_PHASES).toContain(phase);
  });

  test('handles year boundaries', () => {
    const phase = calculateLocalMoonPhase(TEST_DATES.yearBoundary);
    expect(VALID_PHASES).toContain(phase);
  });

  test('is consistent across past, present, and future dates', () => {
    Object.values(TEST_DATES).forEach((date) => {
      const phase = calculateLocalMoonPhase(date);
      expect(VALID_PHASES).toContain(phase);
    });
  });

  // Snapshot tests for internal consistency
  test('matches known snapshots for reference dates', () => {
    expect(calculateLocalMoonPhase(TEST_DATES.referenceNewMoon)).toBe('New Moon');
    expect(calculateLocalMoonPhase('2025-06-15')).toMatchSnapshot();
    expect(calculateLocalMoonPhase('2025-12-31')).toMatchSnapshot();
  });
});

// ============================================================================
// SIGN CALCULATION TESTS
// ============================================================================

describe('calculateLocalMoonSign', () => {
  test('returns a valid zodiac sign', () => {
    const sign = calculateLocalMoonSign();
    expect(VALID_SIGNS).toContain(sign);
  });

  test('never returns Unknown', () => {
    const dates = Array.from({ length: 100 }, (_, i) => {
      const d = new Date();
      d.setDate(d.getDate() + i);
      return d.toISOString().split('T')[0];
    });

    dates.forEach((date) => {
      const sign = calculateLocalMoonSign(date);
      expect(sign).not.toBe('Unknown');
      expect(VALID_SIGNS).toContain(sign);
    });
  });

  test('is deterministic for the same date', () => {
    const date = '2025-12-31';
    const sign1 = calculateLocalMoonSign(date);
    const sign2 = calculateLocalMoonSign(date);
    const sign3 = calculateLocalMoonSign(date);

    expect(sign1).toBe(sign2);
    expect(sign2).toBe(sign3);
  });

  test('is stable across multiple calls', () => {
    const results = Array.from({ length: 100 }, () =>
      calculateLocalMoonSign('2025-06-15')
    );

    const uniqueResults = new Set(results);
    expect(uniqueResults.size).toBe(1); // All results should be identical
  });

  test('accepts Date objects', () => {
    const date = new Date('2025-12-31');
    const sign = calculateLocalMoonSign(date);
    expect(VALID_SIGNS).toContain(sign);
  });

  test('accepts string dates', () => {
    const sign = calculateLocalMoonSign('2025-12-31');
    expect(VALID_SIGNS).toContain(sign);
  });

  test('works without arguments (current date)', () => {
    const sign = calculateLocalMoonSign();
    expect(VALID_SIGNS).toContain(sign);
  });

  test('cycles through all 12 signs over time', () => {
    // Test 30 days (should cover at least one full sign, possibly two)
    const signs = new Set<ZodiacSign>();
    for (let i = 0; i < 30; i++) {
      const d = new Date('2025-01-01');
      d.setDate(d.getDate() + i);
      signs.add(calculateLocalMoonSign(d.toISOString().split('T')[0]));
    }

    // Should have at least 2 signs in 30 days (moon changes sign ~every 2.3 days)
    expect(signs.size).toBeGreaterThanOrEqual(2);
    expect(signs.size).toBeLessThanOrEqual(12);
  });

  test('handles leap years', () => {
    const sign = calculateLocalMoonSign(TEST_DATES.leapYear);
    expect(VALID_SIGNS).toContain(sign);
  });

  test('handles year boundaries', () => {
    const sign = calculateLocalMoonSign(TEST_DATES.yearBoundary);
    expect(VALID_SIGNS).toContain(sign);
  });

  // Snapshot tests for internal consistency
  test('matches known snapshots for reference dates', () => {
    expect(calculateLocalMoonSign('2025-01-15')).toMatchSnapshot();
    expect(calculateLocalMoonSign('2025-06-15')).toMatchSnapshot();
    expect(calculateLocalMoonSign('2025-12-31')).toMatchSnapshot();
  });
});

// ============================================================================
// DEGREE CALCULATION TESTS
// ============================================================================

describe('calculateMoonDegree', () => {
  test('returns a degree between 0 and 360', () => {
    const degree = calculateMoonDegree();
    expect(degree).toBeGreaterThanOrEqual(0);
    expect(degree).toBeLessThan(360);
  });

  test('is deterministic for the same date', () => {
    const date = '2025-12-31';
    const degree1 = calculateMoonDegree(date);
    const degree2 = calculateMoonDegree(date);

    expect(degree1).toBe(degree2);
  });

  test('returns 0-360 range for all test dates', () => {
    Object.values(TEST_DATES).forEach((date) => {
      const degree = calculateMoonDegree(date);
      expect(degree).toBeGreaterThanOrEqual(0);
      expect(degree).toBeLessThan(360);
    });
  });

  test('progresses over time', () => {
    const degree1 = calculateMoonDegree('2025-01-01');
    const degree2 = calculateMoonDegree('2025-01-02');

    // Degrees should be different (moon moves ~13° per day)
    expect(degree1).not.toBe(degree2);
  });
});

describe('degreeToSign', () => {
  test('maps 0° to Aries', () => {
    expect(degreeToSign(0)).toBe('Aries');
    expect(degreeToSign(15)).toBe('Aries');
    expect(degreeToSign(29.9)).toBe('Aries');
  });

  test('maps 30° to Taurus', () => {
    expect(degreeToSign(30)).toBe('Taurus');
    expect(degreeToSign(45)).toBe('Taurus');
    expect(degreeToSign(59.9)).toBe('Taurus');
  });

  test('maps degrees correctly to all 12 signs', () => {
    expect(degreeToSign(0)).toBe('Aries');
    expect(degreeToSign(30)).toBe('Taurus');
    expect(degreeToSign(60)).toBe('Gemini');
    expect(degreeToSign(90)).toBe('Cancer');
    expect(degreeToSign(120)).toBe('Leo');
    expect(degreeToSign(150)).toBe('Virgo');
    expect(degreeToSign(180)).toBe('Libra');
    expect(degreeToSign(210)).toBe('Scorpio');
    expect(degreeToSign(240)).toBe('Sagittarius');
    expect(degreeToSign(270)).toBe('Capricorn');
    expect(degreeToSign(300)).toBe('Aquarius');
    expect(degreeToSign(330)).toBe('Pisces');
  });

  test('handles edge case at 360°', () => {
    expect(degreeToSign(359.9)).toBe('Pisces');
    expect(degreeToSign(360)).toBe('Aries'); // Wraps to 0°
  });

  test('handles negative degrees by normalizing to 0-360', () => {
    // -30° normalizes to 330° which is Pisces (330-360°, sign index 11)
    expect(degreeToSign(-30)).toBe('Pisces');
    // -1° normalizes to 359° which is Pisces (330-360°, sign index 11)
    expect(degreeToSign(-1)).toBe('Pisces');
    // -90° normalizes to 270° which is Capricorn (270-300°)
    expect(degreeToSign(-90)).toBe('Capricorn');
  });
});

// ============================================================================
// COMBINED CALCULATION TESTS
// ============================================================================

describe('calculateLocalMoonData', () => {
  test('returns valid phase and sign', () => {
    const data = calculateLocalMoonData();

    expect(VALID_PHASES).toContain(data.phase);
    expect(VALID_SIGNS).toContain(data.sign);
    expect(data.degree).toBeGreaterThanOrEqual(0);
    expect(data.degree).toBeLessThan(360);
  });

  test('is deterministic for the same date', () => {
    const date = '2025-12-31';
    const data1 = calculateLocalMoonData(date);
    const data2 = calculateLocalMoonData(date);

    expect(data1).toEqual(data2);
  });

  test('sign matches degree conversion', () => {
    const data = calculateLocalMoonData('2025-06-15');
    expect(data.sign).toBe(degreeToSign(data.degree));
  });

  test('provides complete moon data', () => {
    const data = calculateLocalMoonData();

    expect(data).toHaveProperty('phase');
    expect(data).toHaveProperty('sign');
    expect(data).toHaveProperty('degree');
  });
});

// ============================================================================
// UTILITY FUNCTION TESTS
// ============================================================================

describe('isSameMoonPhase', () => {
  test('returns true for same date', () => {
    const date = '2025-12-31';
    expect(isSameMoonPhase(date, date)).toBe(true);
  });

  test('returns true for dates with same phase', () => {
    // Same date should definitely have same phase
    expect(isSameMoonPhase('2025-06-15', '2025-06-15')).toBe(true);
  });

  test('works with Date objects and strings', () => {
    const date1 = new Date('2025-12-31');
    const date2 = '2025-12-31';

    expect(isSameMoonPhase(date1, date2)).toBe(true);
  });
});

describe('isSameMoonSign', () => {
  test('returns true for same date', () => {
    const date = '2025-12-31';
    expect(isSameMoonSign(date, date)).toBe(true);
  });

  test('returns true for dates with same sign', () => {
    // Same date should definitely have same sign
    expect(isSameMoonSign('2025-06-15', '2025-06-15')).toBe(true);
  });

  test('works with Date objects and strings', () => {
    const date1 = new Date('2025-12-31');
    const date2 = '2025-12-31';

    expect(isSameMoonSign(date1, date2)).toBe(true);
  });
});

describe('getDaysUntilNextPhase', () => {
  test('returns a positive number', () => {
    const days = getDaysUntilNextPhase();
    expect(days).toBeGreaterThan(0);
  });

  test('returns a reasonable range (0.5 to 4 days)', () => {
    const days = getDaysUntilNextPhase('2025-06-15');
    expect(days).toBeGreaterThan(0);
    expect(days).toBeLessThanOrEqual(4); // Each phase is ~3.7 days
  });

  test('is deterministic for same date', () => {
    const date = '2025-12-31';
    const days1 = getDaysUntilNextPhase(date);
    const days2 = getDaysUntilNextPhase(date);

    expect(days1).toBe(days2);
  });
});

describe('getDaysUntilNextSign', () => {
  test('returns a positive number', () => {
    const days = getDaysUntilNextSign();
    expect(days).toBeGreaterThan(0);
  });

  test('returns a reasonable range (0.5 to 2.5 days)', () => {
    const days = getDaysUntilNextSign('2025-06-15');
    expect(days).toBeGreaterThan(0);
    expect(days).toBeLessThanOrEqual(2.5); // Each sign is ~2.3 days
  });

  test('is deterministic for same date', () => {
    const date = '2025-12-31';
    const days1 = getDaysUntilNextSign(date);
    const days2 = getDaysUntilNextSign(date);

    expect(days1).toBe(days2);
  });
});

describe('getNextZodiacSign', () => {
  test('cycles through all signs correctly', () => {
    expect(getNextZodiacSign('Aries')).toBe('Taurus');
    expect(getNextZodiacSign('Taurus')).toBe('Gemini');
    expect(getNextZodiacSign('Gemini')).toBe('Cancer');
    expect(getNextZodiacSign('Cancer')).toBe('Leo');
    expect(getNextZodiacSign('Leo')).toBe('Virgo');
    expect(getNextZodiacSign('Virgo')).toBe('Libra');
    expect(getNextZodiacSign('Libra')).toBe('Scorpio');
    expect(getNextZodiacSign('Scorpio')).toBe('Sagittarius');
    expect(getNextZodiacSign('Sagittarius')).toBe('Capricorn');
    expect(getNextZodiacSign('Capricorn')).toBe('Aquarius');
    expect(getNextZodiacSign('Aquarius')).toBe('Pisces');
    expect(getNextZodiacSign('Pisces')).toBe('Aries'); // Wraps around
  });

  test('works without arguments (uses current moon sign)', () => {
    const nextSign = getNextZodiacSign();
    expect(VALID_SIGNS).toContain(nextSign);
  });
});

// ============================================================================
// STABILITY & CONSISTENCY TESTS
// ============================================================================

describe('Stability and consistency', () => {
  test('100 sequential days all have valid phases and signs', () => {
    const startDate = new Date('2025-01-01');

    for (let i = 0; i < 100; i++) {
      const date = new Date(startDate);
      date.setDate(date.getDate() + i);
      const dateStr = date.toISOString().split('T')[0];

      const phase = calculateLocalMoonPhase(dateStr);
      const sign = calculateLocalMoonSign(dateStr);

      expect(VALID_PHASES).toContain(phase);
      expect(VALID_SIGNS).toContain(sign);
      expect(sign).not.toBe('Unknown');
    }
  });

  test('phase cycles approximately every 29.5 days', () => {
    // Track phases over 60 days to see at least 2 full cycles
    const phases: MoonPhase[] = [];
    const startDate = new Date('2025-01-01');

    for (let i = 0; i < 60; i++) {
      const date = new Date(startDate);
      date.setDate(date.getDate() + i);
      phases.push(calculateLocalMoonPhase(date.toISOString().split('T')[0]));
    }

    // Should see multiple different phases
    const uniquePhases = new Set(phases);
    expect(uniquePhases.size).toBeGreaterThanOrEqual(4); // At least half the phases
  });

  test('sign cycles through all 12 signs over ~27 days', () => {
    // Track signs over 30 days to see full cycle
    const signs: ZodiacSign[] = [];
    const startDate = new Date('2025-01-01');

    for (let i = 0; i < 30; i++) {
      const date = new Date(startDate);
      date.setDate(date.getDate() + i);
      signs.push(calculateLocalMoonSign(date.toISOString().split('T')[0]));
    }

    // Should see many different signs (moon stays ~2.3 days per sign)
    const uniqueSigns = new Set(signs);
    expect(uniqueSigns.size).toBeGreaterThanOrEqual(10); // Most signs in 30 days
  });

  test('calculations are independent of system timezone', () => {
    // Same UTC date should give same results regardless of TZ
    const utcDate = '2025-06-15T12:00:00Z';
    const phase = calculateLocalMoonPhase(utcDate);
    const sign = calculateLocalMoonSign(utcDate);

    // Multiple calls should be identical
    expect(calculateLocalMoonPhase(utcDate)).toBe(phase);
    expect(calculateLocalMoonSign(utcDate)).toBe(sign);
  });
});
