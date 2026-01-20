/**
 * NatalWheelChart - Graphique circulaire du thème natal
 *
 * Affiche un wheel chart astrologique avec:
 * - Les 12 signes zodiacaux en cercle extérieur
 * - Les 12 maisons (lignes radiales)
 * - Les planètes positionnées selon leur degré
 *
 * Conventions:
 * - 0° (début Bélier) est à 9h (gauche du cercle)
 * - Les signes progressent dans le sens anti-horaire
 * - L'Ascendant définit la rotation du chart
 */

import React, { useEffect, useRef } from 'react';
import { View, StyleSheet, Animated, Easing } from 'react-native';
import Svg, { Circle, Line, Text as SvgText, G } from 'react-native-svg';
import { colors } from '../constants/theme';

// Types - Compatible avec le format du store useNatalStore
interface Planet {
  name: string;
  sign: string;
  degree: number;
  house?: number;
  retrograde?: boolean;
}

interface House {
  number: number;
  sign: string;
  degree: number;
}

interface NatalChartData {
  sun_sign?: string;
  moon_sign?: string;
  ascendant?: string;
  planets?: Planet[];
  houses?: House[];
}

interface NatalWheelChartProps {
  chart: NatalChartData;
  size?: number;
  animated?: boolean; // Active l'animation d'apparition
}

// Constantes
const ZODIAC_SIGNS = [
  'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
  'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
];

const ZODIAC_SYMBOLS: Record<string, string> = {
  'Aries': '♈', 'Taurus': '♉', 'Gemini': '♊', 'Cancer': '♋',
  'Leo': '♌', 'Virgo': '♍', 'Libra': '♎', 'Scorpio': '♏',
  'Sagittarius': '♐', 'Capricorn': '♑', 'Aquarius': '♒', 'Pisces': '♓'
};

const PLANET_SYMBOLS: Record<string, string> = {
  'sun': '☉', 'soleil': '☉',
  'moon': '☽', 'lune': '☽',
  'mercury': '☿', 'mercure': '☿',
  'venus': '♀', 'vénus': '♀',
  'mars': '♂',
  'jupiter': '♃',
  'saturn': '♄', 'saturne': '♄',
  'uranus': '♅',
  'neptune': '♆',
  'pluto': '♇', 'pluton': '♇',
  'ascendant': 'AS',
  'medium_coeli': 'MC', 'mc': 'MC', 'milieu_du_ciel': 'MC',
  'mean_node': '☊', 'true_node': '☊', 'nœud nord': '☊',
  'south_node': '☋', 'nœud sud': '☋',
  'chiron': '⚷',
  'lilith': '⚸', 'black_moon_lilith': '⚸',
};

const PLANET_COLORS: Record<string, string> = {
  'sun': '#FFD700',
  'moon': '#C0C0C0',
  'mercury': '#87CEEB',
  'venus': '#FF69B4',
  'mars': '#FF4500',
  'jupiter': '#FFA500',
  'saturn': '#8B4513',
  'uranus': '#00CED1',
  'neptune': '#4169E1',
  'pluto': '#800080',
  'ascendant': '#FFFFFF',
  'medium_coeli': '#FFFFFF',
};

// Couleurs des éléments (Feu, Terre, Air, Eau)
const ELEMENT_COLORS: Record<string, string> = {
  'Aries': '#FF6B6B',     // Feu
  'Leo': '#FF6B6B',
  'Sagittarius': '#FF6B6B',
  'Taurus': '#8B7355',    // Terre
  'Virgo': '#8B7355',
  'Capricorn': '#8B7355',
  'Gemini': '#87CEEB',    // Air
  'Libra': '#87CEEB',
  'Aquarius': '#87CEEB',
  'Cancer': '#4169E1',    // Eau
  'Scorpio': '#4169E1',
  'Pisces': '#4169E1',
};

/**
 * Convertit un degré zodiacal absolu (0-360) en angle SVG
 * En astrologie: 0° Bélier est à gauche (9h), sens anti-horaire
 * En SVG: 0° est à droite (3h), sens horaire
 * Formule: angle_svg = 180 - degré_astro
 */
function zodiacToSvgAngle(zodiacDegree: number): number {
  return 180 - zodiacDegree;
}

/**
 * Calcule les coordonnées d'un point sur le cercle
 */
function getPointOnCircle(
  centerX: number,
  centerY: number,
  radius: number,
  angleDegrees: number
): { x: number; y: number } {
  const angleRadians = (angleDegrees * Math.PI) / 180;
  return {
    x: centerX + radius * Math.cos(angleRadians),
    y: centerY - radius * Math.sin(angleRadians),
  };
}

/**
 * Obtient le degré absolu d'une planète (0-360)
 */
function getPlanetAbsoluteDegree(planet: Planet): number | null {
  if (planet.degree === undefined || !planet.sign) return null;

  const signIndex = ZODIAC_SIGNS.indexOf(planet.sign);
  if (signIndex === -1) return null;

  return signIndex * 30 + planet.degree;
}

/**
 * Obtient le symbole d'une planète
 */
function getPlanetSymbol(planetName: string): string {
  const key = planetName.toLowerCase();
  return PLANET_SYMBOLS[key] || planetName.charAt(0).toUpperCase();
}

/**
 * Obtient la couleur d'une planète
 */
function getPlanetColor(planetName: string): string {
  const key = planetName.toLowerCase();
  // Cherche une correspondance partielle
  for (const [k, color] of Object.entries(PLANET_COLORS)) {
    if (key.includes(k) || k.includes(key)) {
      return color;
    }
  }
  return colors.accent;
}

export function NatalWheelChart({ chart, size = 320, animated = true }: NatalWheelChartProps) {
  // Animations
  const scaleAnim = useRef(new Animated.Value(animated ? 0.5 : 1)).current;
  const opacityAnim = useRef(new Animated.Value(animated ? 0 : 1)).current;
  const rotateAnim = useRef(new Animated.Value(animated ? -0.1 : 0)).current;

  useEffect(() => {
    if (animated) {
      Animated.parallel([
        Animated.spring(scaleAnim, {
          toValue: 1,
          friction: 8,
          tension: 40,
          useNativeDriver: true,
        }),
        Animated.timing(opacityAnim, {
          toValue: 1,
          duration: 600,
          useNativeDriver: true,
        }),
        Animated.timing(rotateAnim, {
          toValue: 0,
          duration: 800,
          easing: Easing.out(Easing.cubic),
          useNativeDriver: true,
        }),
      ]).start();
    }
  }, [animated, scaleAnim, opacityAnim, rotateAnim]);

  const rotate = rotateAnim.interpolate({
    inputRange: [-0.1, 0],
    outputRange: ['-36deg', '0deg'],
  });

  const center = size / 2;
  const outerRadius = size / 2 - 10;
  const zodiacRadius = outerRadius - 25;
  const houseRadius = zodiacRadius - 20;
  const planetRadius = houseRadius - 35;
  const innerRadius = planetRadius - 25;

  // Calcul de l'ascendant pour la rotation du chart
  let ascendantDegree = 0;
  if (chart.planets) {
    const ascPlanet = chart.planets.find(p => p.name.toLowerCase() === 'ascendant');
    if (ascPlanet) {
      const asc = getPlanetAbsoluteDegree(ascPlanet);
      if (asc !== null) ascendantDegree = asc;
    }
  }

  // Collecter les planètes avec leurs positions
  const planetPositions: Array<{
    name: string;
    degree: number;
    symbol: string;
    color: string;
  }> = [];

  if (chart.planets) {
    for (const planet of chart.planets) {
      const degree = getPlanetAbsoluteDegree(planet);
      if (degree !== null) {
        // Exclure l'ascendant et MC du cercle des planètes (ils sont sur les axes)
        const nameLower = planet.name.toLowerCase();
        if (nameLower !== 'ascendant' && nameLower !== 'medium_coeli' && nameLower !== 'mc') {
          planetPositions.push({
            name: planet.name,
            degree,
            symbol: getPlanetSymbol(planet.name),
            color: getPlanetColor(planet.name),
          });
        }
      }
    }
  }

  // Collecter les maisons
  const housePositions: Array<{ number: number; degree: number }> = [];

  if (chart.houses && Array.isArray(chart.houses)) {
    chart.houses.forEach((house, index) => {
      if (house.degree !== undefined && house.sign) {
        const signIndex = ZODIAC_SIGNS.indexOf(house.sign);
        if (signIndex !== -1) {
          housePositions.push({
            number: house.number || index + 1,
            degree: signIndex * 30 + house.degree,
          });
        }
      }
    });
  }

  // Dessiner les segments zodiacaux
  const zodiacSegments = ZODIAC_SIGNS.map((sign, index) => {
    const startAngle = zodiacToSvgAngle(index * 30);
    const endAngle = zodiacToSvgAngle((index + 1) * 30);

    // Position du symbole au milieu du segment
    const midAngle = zodiacToSvgAngle(index * 30 + 15);
    const symbolPos = getPointOnCircle(center, center, zodiacRadius, midAngle);

    const elementColor = ELEMENT_COLORS[sign] || colors.textMuted;

    return (
      <G key={sign}>
        {/* Ligne de séparation des signes */}
        <Line
          x1={center + (zodiacRadius - 15) * Math.cos((startAngle * Math.PI) / 180)}
          y1={center - (zodiacRadius - 15) * Math.sin((startAngle * Math.PI) / 180)}
          x2={center + outerRadius * Math.cos((startAngle * Math.PI) / 180)}
          y2={center - outerRadius * Math.sin((startAngle * Math.PI) / 180)}
          stroke={elementColor}
          strokeWidth={0.5}
          opacity={0.5}
        />
        {/* Symbole du signe */}
        <SvgText
          x={symbolPos.x}
          y={symbolPos.y + 5}
          fontSize={14}
          fill={elementColor}
          textAnchor="middle"
          fontWeight="bold"
        >
          {ZODIAC_SYMBOLS[sign]}
        </SvgText>
      </G>
    );
  });

  // Dessiner les lignes des maisons
  const houseLines = housePositions.map((house) => {
    const angle = zodiacToSvgAngle(house.degree);
    const innerPoint = getPointOnCircle(center, center, innerRadius, angle);
    const outerPoint = getPointOnCircle(center, center, houseRadius, angle);

    // Les maisons angulaires (1, 4, 7, 10) sont plus épaisses
    const isAngular = [1, 4, 7, 10].includes(house.number);

    return (
      <G key={`house-${house.number}`}>
        <Line
          x1={innerPoint.x}
          y1={innerPoint.y}
          x2={outerPoint.x}
          y2={outerPoint.y}
          stroke={isAngular ? colors.accent : colors.textMuted}
          strokeWidth={isAngular ? 2 : 0.5}
          opacity={isAngular ? 0.8 : 0.3}
        />
        {/* Numéro de maison */}
        {isAngular && (
          <SvgText
            x={getPointOnCircle(center, center, innerRadius - 12, angle).x}
            y={getPointOnCircle(center, center, innerRadius - 12, angle).y + 4}
            fontSize={9}
            fill={colors.textMuted}
            textAnchor="middle"
          >
            {house.number}
          </SvgText>
        )}
      </G>
    );
  });

  // Dessiner les planètes (avec gestion des collisions basique)
  const usedAngles: number[] = [];
  const MIN_ANGLE_DIFF = 12; // Minimum 12° entre deux planètes

  const planetElements = planetPositions.map((planet, index) => {
    let displayDegree = planet.degree;

    // Gestion basique des collisions
    for (const usedAngle of usedAngles) {
      const diff = Math.abs(displayDegree - usedAngle);
      if (diff < MIN_ANGLE_DIFF || (360 - diff) < MIN_ANGLE_DIFF) {
        // Décaler légèrement vers l'extérieur
        displayDegree = displayDegree + MIN_ANGLE_DIFF;
      }
    }
    usedAngles.push(displayDegree);

    const angle = zodiacToSvgAngle(displayDegree);
    const pos = getPointOnCircle(center, center, planetRadius, angle);

    return (
      <G key={`planet-${planet.name}-${index}`}>
        {/* Cercle de fond */}
        <Circle
          cx={pos.x}
          cy={pos.y}
          r={11}
          fill={colors.cardBg}
          stroke={planet.color}
          strokeWidth={1.5}
        />
        {/* Symbole de la planète */}
        <SvgText
          x={pos.x}
          y={pos.y + 4}
          fontSize={12}
          fill={planet.color}
          textAnchor="middle"
          fontWeight="bold"
        >
          {planet.symbol}
        </SvgText>
      </G>
    );
  });

  // Lignes des axes (AS-DS et MC-IC)
  const axisLines = (
    <G>
      {/* Axe Ascendant-Descendant (horizontal) */}
      <Line
        x1={center - houseRadius}
        y1={center}
        x2={center + houseRadius}
        y2={center}
        stroke={colors.accent}
        strokeWidth={1}
        opacity={0.6}
      />
      {/* Labels AS et DS */}
      <SvgText
        x={center - houseRadius - 15}
        y={center + 4}
        fontSize={10}
        fill={colors.accent}
        textAnchor="middle"
        fontWeight="bold"
      >
        AS
      </SvgText>
      <SvgText
        x={center + houseRadius + 15}
        y={center + 4}
        fontSize={10}
        fill={colors.textMuted}
        textAnchor="middle"
      >
        DS
      </SvgText>

      {/* Axe MC-IC (vertical) */}
      <Line
        x1={center}
        y1={center - houseRadius}
        x2={center}
        y2={center + houseRadius}
        stroke={colors.accent}
        strokeWidth={1}
        opacity={0.6}
      />
      {/* Labels MC et IC */}
      <SvgText
        x={center}
        y={center - houseRadius - 8}
        fontSize={10}
        fill={colors.accent}
        textAnchor="middle"
        fontWeight="bold"
      >
        MC
      </SvgText>
      <SvgText
        x={center}
        y={center + houseRadius + 14}
        fontSize={10}
        fill={colors.textMuted}
        textAnchor="middle"
      >
        IC
      </SvgText>
    </G>
  );

  return (
    <Animated.View
      style={[
        styles.container,
        { width: size, height: size },
        {
          opacity: opacityAnim,
          transform: [
            { scale: scaleAnim },
            { rotate },
          ],
        },
      ]}
    >
      <Svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        {/* Cercle extérieur */}
        <Circle
          cx={center}
          cy={center}
          r={outerRadius}
          fill="none"
          stroke={colors.accent}
          strokeWidth={2}
          opacity={0.3}
        />

        {/* Cercle zodiacal */}
        <Circle
          cx={center}
          cy={center}
          r={zodiacRadius}
          fill="none"
          stroke={colors.textMuted}
          strokeWidth={1}
          opacity={0.2}
        />

        {/* Cercle des maisons */}
        <Circle
          cx={center}
          cy={center}
          r={houseRadius}
          fill="none"
          stroke={colors.textMuted}
          strokeWidth={1}
          opacity={0.2}
        />

        {/* Cercle intérieur */}
        <Circle
          cx={center}
          cy={center}
          r={innerRadius}
          fill={colors.cardBg}
          stroke={colors.textMuted}
          strokeWidth={0.5}
          opacity={0.8}
        />

        {/* Segments zodiacaux */}
        {zodiacSegments}

        {/* Lignes des maisons */}
        {houseLines}

        {/* Axes */}
        {axisLines}

        {/* Planètes */}
        {planetElements}
      </Svg>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    alignSelf: 'center',
  },
});

export default NatalWheelChart;
