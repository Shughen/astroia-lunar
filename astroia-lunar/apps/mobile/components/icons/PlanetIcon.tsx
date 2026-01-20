/**
 * PlanetIcon - Icônes SVG custom pour les planètes astrologiques
 *
 * Design: Style minimaliste avec symboles astronomiques traditionnels
 * revisités pour un look moderne et cohérent avec l'app
 */

import React from 'react';
import { View, StyleSheet } from 'react-native';
import Svg, { Path, Circle, G, Line } from 'react-native-svg';

export type PlanetName =
  | 'sun' | 'moon' | 'mercury' | 'venus' | 'mars'
  | 'jupiter' | 'saturn' | 'uranus' | 'neptune' | 'pluto'
  | 'ascendant' | 'mc' | 'north_node' | 'south_node' | 'chiron' | 'lilith';

interface PlanetIconProps {
  planet: PlanetName | string;
  size?: number;
  color?: string;
  showGlow?: boolean;
}

// Couleurs traditionnelles des planètes
const PLANET_COLORS: Record<string, string> = {
  'sun': '#FFD700',        // Or solaire
  'soleil': '#FFD700',
  'moon': '#E8E8E8',       // Argent lunaire
  'lune': '#E8E8E8',
  'mercury': '#87CEEB',    // Bleu clair vif
  'mercure': '#87CEEB',
  'venus': '#FF69B4',      // Rose Vénus
  'vénus': '#FF69B4',
  'mars': '#FF4500',       // Rouge Mars
  'jupiter': '#FFA500',    // Orange Jupiter
  'saturn': '#DAA520',     // Or vieilli Saturne
  'saturne': '#DAA520',
  'uranus': '#00CED1',     // Turquoise Uranus
  'neptune': '#4169E1',    // Bleu royal Neptune
  'pluto': '#9370DB',      // Violet Pluton
  'pluton': '#9370DB',
  'ascendant': '#FFFFFF',  // Blanc pur
  'mc': '#FFFFFF',
  'north_node': '#7CB342', // Vert croissance
  'south_node': '#8D6E63', // Brun passé
  'chiron': '#9C27B0',     // Violet guérison
  'lilith': '#212121',     // Noir mystère
};

// Paths SVG pour chaque planète (viewBox 0 0 24 24)
const PLANET_PATHS: Record<string, { path: string; hasCircle?: boolean; circleRadius?: number }> = {
  // Soleil ☉ - Cercle avec point central
  'sun': {
    path: '',
    hasCircle: true,
    circleRadius: 8,
  },

  // Lune ☽ - Croissant
  'moon': {
    path: 'M12 3a9 9 0 0 0 0 18c1.5 0 3-.4 4.2-1A7 7 0 0 1 12 3z',
  },

  // Mercure ☿ - Cercle avec croix et cornes
  'mercury': {
    path: 'M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM12 16v5M9 19h6M8 5h8M12 5v3',
  },

  // Vénus ♀ - Cercle avec croix
  'venus': {
    path: 'M12 5a5 5 0 1 0 0 10 5 5 0 0 0 0-10zM12 15v6M9 18h6',
  },

  // Mars ♂ - Cercle avec flèche
  'mars': {
    path: 'M12 10a5 5 0 1 0 0 10 5 5 0 0 0 0-10zM16 4l4 4M20 4h-4v4M16 8l-3 3',
  },

  // Jupiter ♃ - Symbole de Jupiter
  'jupiter': {
    path: 'M4 12h10M10 6v12c3 0 6-2 6-6s-3-6-6-6',
  },

  // Saturne ♄ - Symbole avec croix et croissant
  'saturn': {
    path: 'M8 4h6M11 4v6M6 10c2 0 4 2 4 5 0 2-1 4-3 5M10 15c2 0 4 1 6 1',
  },

  // Uranus ♅ - Cercle avec antennes
  'uranus': {
    path: 'M12 9a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM12 4v5M8 7l4-3 4 3',
  },

  // Neptune ♆ - Trident
  'neptune': {
    path: 'M12 4v16M6 6l6-2 6 2M6 6v4M18 6v4M12 8v-2',
  },

  // Pluton ♇ - Cercle avec arc et croix
  'pluto': {
    path: 'M12 7a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM8 4h8M12 4v3M12 15v5',
  },

  // Ascendant - Flèche montante stylisée
  'ascendant': {
    path: 'M12 4v16M8 8l4-4 4 4M6 12h12',
  },

  // MC (Milieu du Ciel) - Angle supérieur
  'mc': {
    path: 'M4 20l8-16 8 16M8 12h8',
  },

  // Nœud Nord ☊ - Fer à cheval vers le haut
  'north_node': {
    path: 'M6 8c0-2.2 2.7-4 6-4s6 1.8 6 4M6 8v8M18 8v8',
  },

  // Nœud Sud ☋ - Fer à cheval vers le bas
  'south_node': {
    path: 'M6 16c0 2.2 2.7 4 6 4s6-1.8 6-4M6 16V8M18 16V8',
  },

  // Chiron ⚷ - Clé
  'chiron': {
    path: 'M12 4v12M8 8l4 4 4-4M12 16a3 3 0 1 0 0 6 3 3 0 0 0 0-6z',
  },

  // Lilith ⚸ - Lune noire
  'lilith': {
    path: 'M12 4c4 0 6 3 6 8s-2 8-6 8c-2 0-4-1-5-3M7 17V7',
  },
};

// Normaliser le nom de la planète
function normalizePlanetName(name: string): string {
  const normalized = name.toLowerCase().trim();
  const mappings: Record<string, string> = {
    'soleil': 'sun',
    'lune': 'moon',
    'mercure': 'mercury',
    'vénus': 'venus',
    'saturne': 'saturn',
    'pluton': 'pluto',
    'medium_coeli': 'mc',
    'milieu_du_ciel': 'mc',
    'mean_node': 'north_node',
    'true_node': 'north_node',
    'nœud nord': 'north_node',
    'nœud sud': 'south_node',
    'black_moon_lilith': 'lilith',
  };
  return mappings[normalized] || normalized;
}

export function PlanetIcon({
  planet,
  size = 24,
  color,
  showGlow = false,
}: PlanetIconProps) {
  const normalizedPlanet = normalizePlanetName(planet);
  const planetData = PLANET_PATHS[normalizedPlanet];
  const defaultColor = PLANET_COLORS[normalizedPlanet] || PLANET_COLORS[planet] || '#8B7BF7';
  const iconColor = color || defaultColor;

  if (!planetData) {
    // Fallback: cercle simple
    return (
      <View style={[styles.container, { width: size, height: size }]}>
        <Svg width={size} height={size} viewBox="0 0 24 24">
          <Circle cx="12" cy="12" r="8" stroke={iconColor} strokeWidth="1.5" fill="none" />
        </Svg>
      </View>
    );
  }

  // Cas spécial pour le Soleil (cercle avec point)
  if (normalizedPlanet === 'sun') {
    return (
      <View style={[styles.container, { width: size, height: size }]}>
        <Svg width={size} height={size} viewBox="0 0 24 24">
          {showGlow && (
            <Circle cx="12" cy="12" r="11" fill={`${iconColor}30`} />
          )}
          <Circle cx="12" cy="12" r="8" stroke={iconColor} strokeWidth="1.5" fill="none" />
          <Circle cx="12" cy="12" r="2" fill={iconColor} />
        </Svg>
      </View>
    );
  }

  return (
    <View style={[styles.container, { width: size, height: size }]}>
      <Svg width={size} height={size} viewBox="0 0 24 24">
        {showGlow && (
          <Circle cx="12" cy="12" r="11" fill={`${iconColor}20`} />
        )}
        <Path
          d={planetData.path}
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

// Composant badge avec fond coloré
export function PlanetBadge({
  planet,
  size = 40,
}: {
  planet: PlanetName | string;
  size?: number;
}) {
  const normalizedPlanet = normalizePlanetName(planet);
  const bgColor = PLANET_COLORS[normalizedPlanet] || '#8B7BF7';

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
      <PlanetIcon planet={planet} size={size * 0.6} color={bgColor} />
    </View>
  );
}

// Export des couleurs
export { PLANET_COLORS };

// Helper pour obtenir la couleur d'une planète
export function getPlanetColor(planet: string): string {
  const normalized = normalizePlanetName(planet);
  return PLANET_COLORS[normalized] || PLANET_COLORS[planet] || '#8B7BF7';
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

export default PlanetIcon;
