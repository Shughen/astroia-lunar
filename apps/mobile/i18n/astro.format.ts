/**
 * Helpers de formatage astrologique FR
 * Traduction robuste avec normalisation + fallback
 */

import { SIGN_FR, PLANET_FR, ASPECT_FR } from './astro.fr';

/**
 * Normalise une chaîne : trim, lowercase, supprime _ et -
 */
function normalize(value: string | undefined | null): string {
  if (!value) return '';
  return value
    .toString()
    .trim()
    .toLowerCase()
    .replace(/[_-\s]+/g, '');
}

/**
 * Traduit un signe zodiacal EN → FR
 * @param value - Nom du signe (ex: "Aries", "aries", "ARIES")
 * @returns Nom FR (ex: "Bélier") ou fallback sur value d'origine
 */
export function tSign(value: string | undefined | null): string {
  if (!value) return '';
  const normalized = normalize(value);
  return SIGN_FR[normalized] || value.toString().trim();
}

/**
 * Traduit une planète EN → FR
 * @param value - Nom de la planète (ex: "Sun", "moon", "MARS")
 * @returns Nom FR (ex: "Soleil") ou fallback sur value d'origine
 */
export function tPlanet(value: string | undefined | null): string {
  if (!value) return '';
  const normalized = normalize(value);
  return PLANET_FR[normalized] || value.toString().trim();
}

/**
 * Traduit un aspect EN → FR
 * @param value - Nom de l'aspect (ex: "trine", "SQUARE", "semi_sextile")
 * @returns Nom FR (ex: "Trigone") ou fallback sur value d'origine
 */
export function tAspect(value: string | undefined | null): string {
  if (!value) return '';
  const normalized = normalize(value);
  return ASPECT_FR[normalized] || value.toString().trim();
}

/**
 * Formate un orbe en degrés avec 1 décimale et virgule FR
 * Affiche la valeur absolue + indicateur séparatif/applicatif optionnel
 * @param orb - Orbe en degrés (number, peut être négatif)
 * @param showDirection - Afficher l'indicateur directionnel (applicatif/séparatif) (défaut: false)
 * @returns String formatée (ex: "2,5°" ou "2,5° (applicatif)")
 */
export function formatOrb(orb: number | undefined | null, showDirection: boolean = false): string {
  if (orb === undefined || orb === null) return '';
  
  // Valeur absolue
  const absOrb = Math.abs(orb);
  const formatted = `${absOrb.toFixed(1).replace('.', ',')}°`;
  
  // Indicateur directionnel optionnel
  if (showDirection) {
    if (orb < 0) {
      return `${formatted} (séparatif)`;
    } else if (orb > 0) {
      return `${formatted} (applicatif)`;
    }
    // orb === 0 : aspect exact, pas besoin d'indicateur
  }
  
  return formatted;
}

/**
 * Formate un aspect complet en français
 * @param aspect - Objet aspect avec fields variés
 * @returns String FR (ex: "Lune trigone Saturne (orbe 2,5°)")
 *
 * Supporte différentes structures d'aspect:
 * - { planet1, aspect, planet2, orb }
 * - { p1, type, p2, orb }
 * - { transit_planet, aspect, natal_planet, orb }
 */
export function formatAspectFR(aspect: any): string {
  if (!aspect || typeof aspect !== 'object') return '';

  // Détecter les noms de champs (variantes)
  const planet1 = aspect.planet1 || aspect.p1 || aspect.transit_planet || aspect.from_planet;
  const planet2 = aspect.planet2 || aspect.p2 || aspect.natal_planet || aspect.to_planet;
  const aspectType = aspect.aspect || aspect.type;
  const orb = aspect.orb;

  // Traduire les planètes et l'aspect
  const p1FR = tPlanet(planet1);
  const p2FR = tPlanet(planet2);
  const aspectFR = tAspect(aspectType);

  // Construire la chaîne
  let result = '';

  if (p1FR && aspectFR && p2FR) {
    result = `${p1FR} ${aspectFR.toLowerCase()} ${p2FR}`;
  } else if (p1FR && p2FR) {
    result = `${p1FR} - ${p2FR}`;
  } else {
    // Fallback: afficher ce qu'on a
    result = [planet1, aspectType, planet2].filter(Boolean).join(' ');
  }

  // Ajouter l'orbe si présent
  if (orb !== undefined && orb !== null) {
    result += ` (orbe ${formatOrb(orb)})`;
  }

  return result;
}

/**
 * Formate un degré avec 1 ou 2 décimales et virgule FR
 * @param degree - Degré (number)
 * @param decimals - Nombre de décimales (défaut: 2)
 * @returns String formatée (ex: "12,34°")
 */
export function formatDegree(degree: number | undefined | null, decimals: number = 2): string {
  if (degree === undefined || degree === null) return '';
  return `${degree.toFixed(decimals).replace('.', ',')}°`;
}
