/**
 * ZodiacIcon - Icônes SVG custom pour les 12 signes zodiacaux
 *
 * Design: Style minimaliste avec lignes fines, adapté au thème sombre de l'app
 * Chaque signe a une couleur d'élément (Feu, Terre, Air, Eau)
 */

import React from 'react';
import { View, StyleSheet } from 'react-native';
import Svg, { Path, Circle, G } from 'react-native-svg';

export type ZodiacSign =
  | 'Aries' | 'Taurus' | 'Gemini' | 'Cancer'
  | 'Leo' | 'Virgo' | 'Libra' | 'Scorpio'
  | 'Sagittarius' | 'Capricorn' | 'Aquarius' | 'Pisces';

interface ZodiacIconProps {
  sign: ZodiacSign | string;
  size?: number;
  color?: string;
  showBackground?: boolean;
}

// Couleurs par élément
const ELEMENT_COLORS: Record<string, string> = {
  // Feu - Rouge/Orange chaud
  'Aries': '#FF6B6B',
  'Leo': '#FF8C42',
  'Sagittarius': '#FF6B6B',
  // Terre - Vert/Brun terreux
  'Taurus': '#7CB342',
  'Virgo': '#8D6E63',
  'Capricorn': '#6D4C41',
  // Air - Bleu/Cyan léger
  'Gemini': '#64B5F6',
  'Libra': '#4FC3F7',
  'Aquarius': '#29B6F6',
  // Eau - Bleu/Violet profond
  'Cancer': '#7986CB',
  'Scorpio': '#9575CD',
  'Pisces': '#7E57C2',
};

// Paths SVG pour chaque signe (viewBox 0 0 24 24)
const ZODIAC_PATHS: Record<string, string> = {
  // Bélier ♈ - Cornes de bélier stylisées
  'Aries': 'M7 4c-1.5 0-3 1.5-3 3.5S5 11 7 12.5V20m10-16c1.5 0 3 1.5 3 3.5S19 11 17 12.5V20M12 4v16',

  // Taureau ♉ - Tête de taureau avec cornes
  'Taurus': 'M12 20c-3.5 0-6-2.5-6-6 0-2 1-4 3-5M12 20c3.5 0 6-2.5 6-6 0-2-1-4-3-5M6 9c-1.5-1.5-2-3-2-4.5C4 3 5 2 6.5 2S9 3 9 4.5M18 9c1.5-1.5 2-3 2-4.5C20 3 19 2 17.5 2S15 3 15 4.5',

  // Gémeaux ♊ - Deux colonnes liées (les jumeaux)
  'Gemini': 'M6 4h12M6 20h12M8 4v16M16 4v16M8 12h8',

  // Cancer ♋ - Pinces de crabe stylisées (69 inversé)
  'Cancer': 'M9 8c2.5 0 4.5 2 4.5 4.5S11.5 17 9 17s-4.5-2-4.5-4.5M15 16c-2.5 0-4.5-2-4.5-4.5S12.5 7 15 7s4.5 2 4.5 4.5',

  // Lion ♌ - Crinière de lion stylisée
  'Leo': 'M6 16c0-2.2 1.8-4 4-4 1.5 0 2.8.8 3.5 2M10 12V7c0-1.7 1.3-3 3-3s3 1.3 3 3c0 2.5-2 4-2 6.5 0 1.4 1.1 2.5 2.5 2.5s2.5-1.1 2.5-2.5',

  // Vierge ♍ - M stylisé avec boucle
  'Virgo': 'M4 16V8l4 8V8l4 8V8M16 8v4c0 2 1 4 3 4M16 12c1 0 2 1 2 2.5S17 17 16 17',

  // Balance ♎ - Balance stylisée
  'Libra': 'M4 18h16M12 18V6M7 10c0-2.8 2.2-5 5-5s5 2.2 5 5',

  // Scorpion ♏ - M avec queue de scorpion
  'Scorpio': 'M4 16V8l4 8V8l4 8V8l4 8v-4l2 2 2-2',

  // Sagittaire ♐ - Flèche de l'archer
  'Sagittarius': 'M4 20L20 4M20 4h-6M20 4v6M4 12l8 8',

  // Capricorne ♑ - Chèvre-poisson stylisée
  'Capricorn': 'M6 12c2-4 4-8 6-8 3 0 3 4 3 8 0 2-1 4-2 5M13 17c1.5 0 3 1 4 0s1.5-3 1-5',

  // Verseau ♒ - Vagues d'eau
  'Aquarius': 'M4 10c2-2 4-2 6 0s4 2 6 0 4-2 6 0M4 16c2-2 4-2 6 0s4 2 6 0 4-2 6 0',

  // Poissons ♓ - Deux poissons reliés
  'Pisces': 'M4 12h16M8 4c-3 0-4 4-4 8s1 8 4 8M16 4c3 0 4 4 4 8s-1 8-4 8',
};

export function ZodiacIcon({
  sign,
  size = 24,
  color,
  showBackground = false,
}: ZodiacIconProps) {
  const normalizedSign = sign as ZodiacSign;
  const path = ZODIAC_PATHS[normalizedSign];
  const defaultColor = ELEMENT_COLORS[normalizedSign] || '#8B7BF7';
  const iconColor = color || defaultColor;

  if (!path) {
    // Fallback: afficher un cercle avec la première lettre
    return (
      <View style={[styles.container, { width: size, height: size }]}>
        <Svg width={size} height={size} viewBox="0 0 24 24">
          <Circle cx="12" cy="12" r="10" stroke={iconColor} strokeWidth="1.5" fill="none" />
        </Svg>
      </View>
    );
  }

  return (
    <View style={[styles.container, { width: size, height: size }]}>
      <Svg width={size} height={size} viewBox="0 0 24 24">
        {showBackground && (
          <Circle
            cx="12"
            cy="12"
            r="11"
            fill="rgba(139, 123, 247, 0.1)"
            stroke={iconColor}
            strokeWidth="0.5"
            opacity={0.3}
          />
        )}
        <Path
          d={path}
          stroke={iconColor}
          strokeWidth="1.5"
          strokeLinecap="round"
          strokeLinejoin="round"
          fill="none"
        />
      </Svg>
    </View>
  );
}

// Composant pour afficher l'icône avec un cercle de fond coloré
export function ZodiacBadge({
  sign,
  size = 40,
}: {
  sign: ZodiacSign | string;
  size?: number;
}) {
  const normalizedSign = sign as ZodiacSign;
  const bgColor = ELEMENT_COLORS[normalizedSign] || '#8B7BF7';

  return (
    <View
      style={[
        styles.badge,
        {
          width: size,
          height: size,
          borderRadius: size / 2,
          backgroundColor: `${bgColor}20`,
          borderColor: bgColor,
        },
      ]}
    >
      <ZodiacIcon sign={sign} size={size * 0.6} color={bgColor} />
    </View>
  );
}

// Export des couleurs pour usage externe
export { ELEMENT_COLORS };

// Helper pour obtenir la couleur d'un signe
export function getZodiacColor(sign: string): string {
  return ELEMENT_COLORS[sign] || '#8B7BF7';
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
  },
  badge: {
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1.5,
  },
});

export default ZodiacIcon;
