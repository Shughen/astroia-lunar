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
    message: "L'élan est là. Fais un premier pas concret aujourd'hui.",
    keywords: ['Action', 'Motivation', 'Clarté'],
  },
  first_quarter: {
    message: 'Des obstacles peuvent surgir. Ajuste ta trajectoire avec flexibilité.',
    keywords: ['Décision', 'Persévérance', 'Adaptation'],
  },
  waxing_gibbous: {
    message: 'Tout continue de mûrir. Tu peux affiner, sans forcer.',
    keywords: ['Perfectionnement', 'Patience', 'Détail'],
  },
  full_moon: {
    message: 'Illumination et culmination. Observe ce qui se révèle.',
    keywords: ['Révélation', 'Célébration', 'Gratitude'],
  },
  waning_gibbous: {
    message: 'Temps de partager ce que tu as appris. Transmets.',
    keywords: ['Partage', 'Enseignement', 'Générosité'],
  },
  last_quarter: {
    message: 'Lâche ce qui ne te sert plus. Fais de la place.',
    keywords: ['Libération', 'Lâcher-prise', 'Tri'],
  },
  waning_crescent: {
    message: 'Repos et introspection. Prépare le prochain cycle.',
    keywords: ['Repos', 'Rêves', 'Bilan'],
  },
};
