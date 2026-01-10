/**
 * Helpers pour la carte Rituel Quotidien
 */

import { MoonPhase } from '../types/ritual';
import { calculateLocalMoonPhase as calculatePhase } from './moonCalc';

/**
 * Retourne l'emoji correspondant à la phase lunaire
 */
export function getPhaseEmoji(phase: MoonPhase): string {
  const emojiMap: Record<MoonPhase, string> = {
    'New Moon': '🌑',
    'Waxing Crescent': '🌒',
    'First Quarter': '🌓',
    'Waxing Gibbous': '🌔',
    'Full Moon': '🌕',
    'Waning Gibbous': '🌖',
    'Last Quarter': '🌗',
    'Waning Crescent': '🌘',
  };
  return emojiMap[phase] || '🌑';
}

/**
 * Convertit la phase lunaire en clé i18n (snake_case)
 */
export function getPhaseKey(phase: MoonPhase): string {
  return phase.toLowerCase().replace(/\s+/g, '_');
}

/**
 * Traduit la phase lunaire anglaise en français
 * Mapping exact des 8 phases définies dans MoonPhase
 */
export function translatePhaseToFrench(phase: MoonPhase): string {
  const translations: Record<MoonPhase, string> = {
    'New Moon': 'Nouvelle Lune',
    'Waxing Crescent': 'Premier Croissant',
    'First Quarter': 'Premier Quartier',
    'Waxing Gibbous': 'Lune Gibbeuse Croissante',
    'Full Moon': 'Pleine Lune',
    'Waning Gibbous': 'Lune Gibbeuse Décroissante',
    'Last Quarter': 'Dernier Quartier',
    'Waning Crescent': 'Dernier Croissant',
  };
  return translations[phase] || phase;
}

/**
 * Formate un timestamp ISO en heure locale (HH:mm)
 */
export function formatTime(isoString: string): string {
  const date = new Date(isoString);
  const hours = date.getHours();
  const minutes = date.getMinutes();
  return `${hours}h${minutes.toString().padStart(2, '0')}`;
}

/**
 * Formate un timestamp en date courte pour cache (ex: "30 déc.")
 */
export function formatCacheDate(timestamp: number, locale: string = 'fr'): string {
  const date = new Date(timestamp);
  const day = date.getDate();
  const monthShort = getMonthShort(date.getMonth(), locale);
  return `${day} ${monthShort}.`;
}

/**
 * Retourne le mois court selon la locale
 */
function getMonthShort(monthIndex: number, locale: string): string {
  const monthsFr = [
    'jan', 'fév', 'mar', 'avr', 'mai', 'juin',
    'juil', 'août', 'sep', 'oct', 'nov', 'déc',
  ];
  const monthsEn = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
  ];
  return locale === 'fr' ? monthsFr[monthIndex] : monthsEn[monthIndex];
}

/**
 * Retourne la date du jour au format YYYY-MM-DD
 */
export function getTodayDateString(): string {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

/**
 * Calcule la phase lunaire locale (fallback si API fail)
 * Utilise algorithme simplifié basé sur le cycle lunaire de ~29.53 jours
 *
 * @deprecated Use calculateLocalMoonPhase from utils/moonCalc.ts instead
 * This wrapper is kept for backward compatibility.
 */
export function calculateLocalPhase(): MoonPhase {
  return calculatePhase();
}
