/**
 * Helpers pour formatage de données astrologiques
 */

import type { Aspect } from '../types/api';

/**
 * Formate une liste d'aspects en texte lisible
 * @param aspects - Liste d'aspects astrologiques
 * @returns Tableau de strings formatés
 */
export function formatAspects(aspects?: Aspect[]): string[] {
  if (!aspects || aspects.length === 0) {
    return [];
  }

  return aspects.map((aspect) => {
    const planet1 = aspect.planet1 || aspect.planet_1 || 'Planet1';
    const planet2 = aspect.planet2 || aspect.planet_2 || 'Planet2';
    const type = aspect.type || aspect.aspect_type || 'aspect';
    const orb = aspect.orb;

    let aspectText = `${planet1} ${type} ${planet2}`;
    if (orb !== undefined && orb !== null) {
      aspectText += `, orb ${orb.toFixed(1)}°`;
    }
    return aspectText;
  });
}

/**
 * Interface pour le formatage React des interprétations
 */
export interface FormattedParagraph {
  type: 'paragraph';
  index: number;
  parts: FormattedPart[];
}

export interface FormattedPart {
  type: 'text' | 'bold';
  content: string;
  key: string;
}

/**
 * Parse une interprétation markdown en structure de données
 * Split par \n\n et supporte **gras**
 * @param text - Texte à formatter
 * @returns Structure de données parsée
 */
export function parseInterpretation(text?: string): FormattedParagraph[] {
  if (!text) {
    return [];
  }

  const paragraphs = text.split('\n\n').filter((p) => p.trim().length > 0);

  return paragraphs.map((paragraph, index) => {
    const parts: FormattedPart[] = [];
    const regex = /\*\*(.*?)\*\*/g;
    let lastIndex = 0;
    let keyCounter = 0;
    let match;

    while ((match = regex.exec(paragraph)) !== null) {
      // Texte avant le gras
      if (match.index > lastIndex) {
        parts.push({
          type: 'text',
          content: paragraph.substring(lastIndex, match.index),
          key: `text-${keyCounter++}`,
        });
      }

      // Texte en gras
      parts.push({
        type: 'bold',
        content: match[1],
        key: `bold-${keyCounter++}`,
      });

      lastIndex = match.index + match[0].length;
    }

    // Texte restant
    if (lastIndex < paragraph.length) {
      parts.push({
        type: 'text',
        content: paragraph.substring(lastIndex),
        key: `text-${keyCounter++}`,
      });
    }

    // Si aucun match, ajouter tout le paragraphe
    if (parts.length === 0) {
      parts.push({
        type: 'text',
        content: paragraph,
        key: `text-${keyCounter++}`,
      });
    }

    return {
      type: 'paragraph',
      index,
      parts,
    };
  });
}
