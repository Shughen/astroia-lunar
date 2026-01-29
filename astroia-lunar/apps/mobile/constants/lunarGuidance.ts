/**
 * Lunar Guidance Constants
 * Messages et keywords par phase lunaire pour le bottom sheet quotidien
 */

export interface LunarGuidanceData {
  message: string;
  keywords: string[];
}

export const LUNAR_GUIDANCE: Record<string, LunarGuidanceData> = {
  new_moon: {
    message: "Temps de poser tes intentions. Qu'est-ce que tu veux faire grandir ?",
    keywords: ['Intention', 'Commencement', 'Introspection'],
  },
  waxing_crescent: {
    message: "L'elan est la. Fais un premier pas concret aujourd'hui.",
    keywords: ['Action', 'Motivation', 'Clarte'],
  },
  first_quarter: {
    message: 'Des obstacles peuvent surgir. Ajuste ta trajectoire avec flexibilite.',
    keywords: ['Decision', 'Perseverance', 'Adaptation'],
  },
  waxing_gibbous: {
    message: 'Tout continue de murir. Tu peux affiner, sans forcer.',
    keywords: ['Perfectionnement', 'Patience', 'Detail'],
  },
  full_moon: {
    message: 'Illumination et culmination. Observe ce qui se revele.',
    keywords: ['Revelation', 'Celebration', 'Gratitude'],
  },
  waning_gibbous: {
    message: 'Temps de partager ce que tu as appris. Transmets.',
    keywords: ['Partage', 'Enseignement', 'Generosite'],
  },
  last_quarter: {
    message: 'Lache ce qui ne te sert plus. Fais de la place.',
    keywords: ['Liberation', 'Lacher-prise', 'Tri'],
  },
  waning_crescent: {
    message: 'Repos et introspection. Prepare le prochain cycle.',
    keywords: ['Repos', 'Reves', 'Bilan'],
  },
};
