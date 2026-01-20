/**
 * Icônes astrologiques custom pour Lunation
 *
 * Ce module exporte des composants SVG pour:
 * - Les 12 signes zodiacaux
 * - Les planètes principales
 * - Les phases lunaires
 */

// Zodiac Icons
export {
  ZodiacIcon,
  ZodiacBadge,
  getZodiacColor,
  ELEMENT_COLORS,
  type ZodiacSign,
} from './ZodiacIcon';

// Planet Icons
export {
  PlanetIcon,
  PlanetBadge,
  getPlanetColor,
  PLANET_COLORS,
  type PlanetName,
} from './PlanetIcon';

// Moon Phase Icons
export {
  MoonPhaseIcon,
  getMoonPhaseEmoji,
  getMoonPhaseName,
  type MoonPhase,
} from './MoonPhaseIcon';
