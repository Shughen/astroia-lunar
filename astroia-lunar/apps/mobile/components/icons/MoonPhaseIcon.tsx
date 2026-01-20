/**
 * MoonPhaseIcon - Icônes SVG pour les phases lunaires
 *
 * Affiche visuellement les 8 phases principales de la Lune
 */

import React from 'react';
import { View, StyleSheet } from 'react-native';
import Svg, { Circle, Path, Defs, ClipPath, Rect } from 'react-native-svg';

export type MoonPhase =
  | 'new_moon'
  | 'waxing_crescent'
  | 'first_quarter'
  | 'waxing_gibbous'
  | 'full_moon'
  | 'waning_gibbous'
  | 'last_quarter'
  | 'waning_crescent';

interface MoonPhaseIconProps {
  phase: MoonPhase | string;
  size?: number;
  lightColor?: string;
  darkColor?: string;
}

// Mapping des noms de phases en français/anglais
const PHASE_MAPPINGS: Record<string, MoonPhase> = {
  'new moon': 'new_moon',
  'nouvelle lune': 'new_moon',
  'new': 'new_moon',
  'waxing crescent': 'waxing_crescent',
  'premier croissant': 'waxing_crescent',
  'first quarter': 'first_quarter',
  'premier quartier': 'first_quarter',
  'waxing gibbous': 'waxing_gibbous',
  'gibbeuse croissante': 'waxing_gibbous',
  'full moon': 'full_moon',
  'pleine lune': 'full_moon',
  'full': 'full_moon',
  'waning gibbous': 'waning_gibbous',
  'gibbeuse décroissante': 'waning_gibbous',
  'last quarter': 'last_quarter',
  'dernier quartier': 'last_quarter',
  'third quarter': 'last_quarter',
  'waning crescent': 'waning_crescent',
  'dernier croissant': 'waning_crescent',
};

// Emojis de fallback pour chaque phase
const PHASE_EMOJIS: Record<MoonPhase, string> = {
  'new_moon': '🌑',
  'waxing_crescent': '🌒',
  'first_quarter': '🌓',
  'waxing_gibbous': '🌔',
  'full_moon': '🌕',
  'waning_gibbous': '🌖',
  'last_quarter': '🌗',
  'waning_crescent': '🌘',
};

function normalizePhase(phase: string): MoonPhase {
  const normalized = phase.toLowerCase().trim().replace(/_/g, ' ');
  return PHASE_MAPPINGS[normalized] || (phase as MoonPhase);
}

export function MoonPhaseIcon({
  phase,
  size = 32,
  lightColor = '#F5F5DC', // Beige lunaire
  darkColor = '#1A1A2E',  // Bleu nuit profond
}: MoonPhaseIconProps) {
  const normalizedPhase = normalizePhase(phase);
  const radius = size / 2 - 2;
  const center = size / 2;

  // Fonction pour créer le path d'illumination selon la phase
  const renderPhase = () => {
    switch (normalizedPhase) {
      case 'new_moon':
        // Lune entièrement sombre
        return (
          <Circle cx={center} cy={center} r={radius} fill={darkColor} />
        );

      case 'full_moon':
        // Lune entièrement éclairée
        return (
          <Circle cx={center} cy={center} r={radius} fill={lightColor} />
        );

      case 'first_quarter':
        // Moitié droite éclairée
        return (
          <>
            <Circle cx={center} cy={center} r={radius} fill={darkColor} />
            <Path
              d={`M${center} ${center - radius} A${radius} ${radius} 0 0 1 ${center} ${center + radius} L${center} ${center - radius}`}
              fill={lightColor}
            />
          </>
        );

      case 'last_quarter':
        // Moitié gauche éclairée
        return (
          <>
            <Circle cx={center} cy={center} r={radius} fill={darkColor} />
            <Path
              d={`M${center} ${center - radius} A${radius} ${radius} 0 0 0 ${center} ${center + radius} L${center} ${center - radius}`}
              fill={lightColor}
            />
          </>
        );

      case 'waxing_crescent':
        // Petit croissant à droite
        return (
          <>
            <Circle cx={center} cy={center} r={radius} fill={darkColor} />
            <Path
              d={`M${center} ${center - radius}
                  A${radius} ${radius} 0 0 1 ${center} ${center + radius}
                  A${radius * 0.6} ${radius} 0 0 0 ${center} ${center - radius}`}
              fill={lightColor}
            />
          </>
        );

      case 'waxing_gibbous':
        // Grande partie droite éclairée
        return (
          <>
            <Circle cx={center} cy={center} r={radius} fill={darkColor} />
            <Path
              d={`M${center} ${center - radius}
                  A${radius} ${radius} 0 0 1 ${center} ${center + radius}
                  A${radius * 0.6} ${radius} 0 0 1 ${center} ${center - radius}`}
              fill={lightColor}
            />
          </>
        );

      case 'waning_gibbous':
        // Grande partie gauche éclairée
        return (
          <>
            <Circle cx={center} cy={center} r={radius} fill={darkColor} />
            <Path
              d={`M${center} ${center - radius}
                  A${radius} ${radius} 0 0 0 ${center} ${center + radius}
                  A${radius * 0.6} ${radius} 0 0 0 ${center} ${center - radius}`}
              fill={lightColor}
            />
          </>
        );

      case 'waning_crescent':
        // Petit croissant à gauche
        return (
          <>
            <Circle cx={center} cy={center} r={radius} fill={darkColor} />
            <Path
              d={`M${center} ${center - radius}
                  A${radius} ${radius} 0 0 0 ${center} ${center + radius}
                  A${radius * 0.6} ${radius} 0 0 1 ${center} ${center - radius}`}
              fill={lightColor}
            />
          </>
        );

      default:
        // Fallback: cercle avec contour
        return (
          <Circle
            cx={center}
            cy={center}
            r={radius}
            fill="none"
            stroke={lightColor}
            strokeWidth={1.5}
          />
        );
    }
  };

  return (
    <View style={[styles.container, { width: size, height: size }]}>
      <Svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        {/* Contour subtil */}
        <Circle
          cx={center}
          cy={center}
          r={radius}
          fill="none"
          stroke="rgba(255,255,255,0.2)"
          strokeWidth={0.5}
        />
        {renderPhase()}
      </Svg>
    </View>
  );
}

// Helper pour obtenir l'emoji de phase
export function getMoonPhaseEmoji(phase: string): string {
  const normalized = normalizePhase(phase);
  return PHASE_EMOJIS[normalized] || '🌙';
}

// Helper pour obtenir le nom français de la phase
export function getMoonPhaseName(phase: string): string {
  const normalized = normalizePhase(phase);
  const names: Record<MoonPhase, string> = {
    'new_moon': 'Nouvelle Lune',
    'waxing_crescent': 'Premier Croissant',
    'first_quarter': 'Premier Quartier',
    'waxing_gibbous': 'Gibbeuse Croissante',
    'full_moon': 'Pleine Lune',
    'waning_gibbous': 'Gibbeuse Décroissante',
    'last_quarter': 'Dernier Quartier',
    'waning_crescent': 'Dernier Croissant',
  };
  return names[normalized] || phase;
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default MoonPhaseIcon;
