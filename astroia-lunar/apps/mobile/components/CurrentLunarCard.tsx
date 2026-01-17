/**
 * CurrentLunarCard Component
 * Carte HERO "Quel est mon cycle actuel ?" pour le dashboard Home
 *
 * Features:
 * - Affiche la révolution lunaire en cours
 * - Format imposant, position 1 dans la hiérarchie
 * - Animation fade-in au premier affichage
 * - CTA vers /lunar/report
 */

import React, { useState, useRef, useEffect } from 'react';
import {
  View,
  Text,
  Pressable,
  StyleSheet,
  Animated,
  Easing,
} from 'react-native';
import { useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { LunarReturn } from '../services/api';
import { Skeleton } from './Skeleton';
import { translateZodiacSign } from '../utils/astrologyTranslations';

interface CurrentLunarCardProps {
  lunarReturn: LunarReturn | null;
  loading?: boolean;
  onRefresh?: () => void;
}

/**
 * Formate le nom du mois avec l'année
 * Ex: "Janvier 2026"
 */
const formatMonthName = (returnDate: string): string => {
  const date = new Date(returnDate);
  const formatted = date.toLocaleDateString('fr-FR', { month: 'long', year: 'numeric' });
  // Capitaliser la première lettre
  return formatted.charAt(0).toUpperCase() + formatted.slice(1);
};

/**
 * Formate la plage de dates du cycle lunaire
 * Ex: "20 janv. - 18 fév." (cycle ~29.5 jours)
 */
const formatDateRange = (returnDate: string): string => {
  const start = new Date(returnDate);
  const end = new Date(start.getTime() + 29.5 * 24 * 60 * 60 * 1000);

  return `${start.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' })} - ${end.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' })}`;
};

export function CurrentLunarCard({ lunarReturn, loading, onRefresh }: CurrentLunarCardProps) {
  const router = useRouter();

  // State local
  const [isFirstView] = useState(false);
  const fadeAnim = useRef(new Animated.Value(0)).current;

  // Animate on mount
  useEffect(() => {
    if (lunarReturn && !loading) {
      Animated.timing(fadeAnim, {
        toValue: 1,
        duration: 600,
        easing: Easing.out(Easing.cubic),
        useNativeDriver: true,
      }).start();
    } else if (lunarReturn && !loading) {
      // Pas d'animation, affichage direct
      fadeAnim.setValue(1);
    }
  }, [lunarReturn, loading]);

  const handlePress = () => {
    router.push('/lunar/report');
  };

  // Render loading
  if (loading && !lunarReturn) {
    return (
      <View style={styles.container}>
        <Skeleton width="100%" height={200} borderRadius={borderRadius.md} />
      </View>
    );
  }

  // Pas de données
  if (!lunarReturn) {
    return null;
  }

  // Derive display data
  const monthName = formatMonthName(lunarReturn.return_date);
  const dateRange = formatDateRange(lunarReturn.return_date);
  const moonSign = lunarReturn.moon_sign ? translateZodiacSign(lunarReturn.moon_sign) : 'Non disponible';
  const lunarAscendant = lunarReturn.lunar_ascendant ? translateZodiacSign(lunarReturn.lunar_ascendant) : 'Non disponible';

  return (
    <Animated.View
      style={[
        styles.container,
        {
          opacity: fadeAnim,
        },
      ]}
    >
      <Pressable
        onPress={handlePress}
        style={({ pressed }) => [styles.card, pressed && styles.cardPressed]}
        testID="current-lunar-card"
      >
        {/* Question title */}
        <Text style={styles.questionTitle} testID="lunar-question">Quel est mon cycle actuel ?</Text>

        {/* Month title */}
        <Text style={styles.monthTitle} testID="lunar-month">{monthName}</Text>

        {/* Date range */}
        <Text style={styles.dateRange} testID="lunar-date-range">{dateRange}</Text>

        {/* Meta grid (Lune + Ascendant) */}
        <View style={styles.metaGrid}>
          <View style={styles.metaItem}>
            <Text style={styles.metaLabel}>Lune en</Text>
            <Text style={styles.metaValue} testID="lunar-moon-sign">{moonSign}</Text>
          </View>
          <View style={styles.metaItem}>
            <Text style={styles.metaLabel} testID="lunar-ascendant-label">Ascendant</Text>
            <Text style={styles.metaValue} testID="lunar-ascendant">{lunarAscendant}</Text>
          </View>
        </View>

        {/* CTA */}
        <Text style={styles.ctaText} testID="lunar-cta">→ Voir le rapport mensuel</Text>
      </Pressable>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: spacing.md,
    marginVertical: spacing.sm,
  },
  card: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  cardPressed: {
    opacity: 0.8,
  },
  questionTitle: {
    ...fonts.h3,
    color: colors.accent,
    marginBottom: spacing.md,
    fontSize: 16,
    fontWeight: '500',
  },
  monthTitle: {
    ...fonts.h2,
    color: colors.text,
    marginBottom: spacing.sm,
    fontSize: 28,
    fontWeight: 'bold',
  },
  dateRange: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginBottom: spacing.lg,
    fontSize: 14,
  },
  metaGrid: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: spacing.lg,
    paddingVertical: spacing.md,
    borderTopWidth: 1,
    borderBottomWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  metaItem: {
    alignItems: 'center',
  },
  metaLabel: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginBottom: spacing.xs,
    fontSize: 12,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  metaValue: {
    ...fonts.body,
    color: colors.text,
    fontSize: 16,
    fontWeight: '600',
  },
  ctaText: {
    ...fonts.button,
    color: colors.accent,
    fontSize: 15,
    textAlign: 'center',
  },
});
