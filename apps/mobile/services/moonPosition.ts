/**
 * Service pour récupérer la position actuelle de la Lune
 * Appelle l'API backend /api/lunar/current (Swiss Ephemeris)
 * Fallback sur calcul client si API offline
 */

import { MoonPosition } from './lunarClimate';
import { lunaPack } from './api';

// Approximation des phases lunaires (cycle ~ 29.5 jours)
const LUNAR_CYCLE_DAYS = 29.530588;

// Date de référence d'une Nouvelle Lune (2025-01-29 12:00 UTC)
const NEW_MOON_REFERENCE = new Date('2025-01-29T12:00:00Z').getTime();

/**
 * Calcule la phase lunaire actuelle
 */
function calculateMoonPhase(now: Date): string {
  const daysSinceNewMoon = (now.getTime() - NEW_MOON_REFERENCE) / (1000 * 60 * 60 * 24);
  const phaseInCycle = ((daysSinceNewMoon % LUNAR_CYCLE_DAYS) + LUNAR_CYCLE_DAYS) % LUNAR_CYCLE_DAYS;

  if (phaseInCycle < 1.85) return 'Nouvelle Lune';
  if (phaseInCycle < 7.4) return 'Premier Croissant';
  if (phaseInCycle < 9.2) return 'Premier Quartier';
  if (phaseInCycle < 14.75) return 'Lune Gibbeuse';
  if (phaseInCycle < 16.6) return 'Pleine Lune';
  if (phaseInCycle < 22.15) return 'Lune Disseminante';
  if (phaseInCycle < 23.95) return 'Dernier Quartier';
  return 'Dernier Croissant';
}

/**
 * Calcule approximativement le degré zodiacal de la Lune
 * La Lune fait 360° en ~27.3 jours (cycle sidéral)
 */
function calculateMoonDegree(now: Date): number {
  const SIDEREAL_CYCLE_DAYS = 27.321661;
  // Date de référence où la Lune était à 0° Bélier (exemple arbitraire)
  const MOON_REFERENCE = new Date('2025-01-15T00:00:00Z').getTime();

  const daysSinceReference = (now.getTime() - MOON_REFERENCE) / (1000 * 60 * 60 * 24);
  const degreesPerDay = 360 / SIDEREAL_CYCLE_DAYS;
  const degree = (daysSinceReference * degreesPerDay) % 360;

  return degree < 0 ? degree + 360 : degree;
}

/**
 * Convertit un degré zodiacal en signe
 */
function degreeToSign(degree: number): string {
  const signs = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
  ];
  const signIndex = Math.floor(degree / 30);
  return signs[signIndex] || 'Aries';
}

/**
 * Fallback: Calcul client-side (approximatif) si l'API est offline
 */
function calculateMockMoonPosition(): MoonPosition {
  const now = new Date();
  const degree = calculateMoonDegree(now);
  const sign = degreeToSign(degree);
  const phase = calculateMoonPhase(now);

  return {
    sign,
    degree,
    phase,
  };
}

/**
 * Récupère la position actuelle de la Lune
 * Appelle l'API backend /api/lunar/current (Swiss Ephemeris)
 * Fallback sur calcul client si API indisponible
 */
export async function getCurrentMoonPosition(): Promise<MoonPosition> {
  try {
    // Appel API backend avec Swiss Ephemeris
    const result = await lunaPack.getCurrentMoonPosition();
    console.log('[MoonPosition] ✅ Position depuis API backend (Swiss Ephemeris):', result);
    return result;
  } catch (error: any) {
    // Fallback sur calcul client si API offline
    console.warn(
      '[MoonPosition] ⚠️ API backend indisponible, fallback sur calcul client (approximatif):',
      error.message || error
    );
    const mockResult = calculateMockMoonPosition();
    console.log('[MoonPosition] 📊 Position calculée client-side:', mockResult);
    return mockResult;
  }
}
