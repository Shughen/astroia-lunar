/**
 * HeroLunarCard Component
 * Carte HERO occupant 60% de l'ecran pour la revolution lunaire
 *
 * Features:
 * - Affiche la revolution lunaire en cours en grand format
 * - Elements decoratifs (blur circles)
 * - Section "Themes du mois" avec 3 KeywordChips
 * - CTA bouton gradient
 */

import React, { useRef, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  Pressable,
  Animated,
  Easing,
  Dimensions,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { LunarReturn } from '../services/api';
import { Skeleton } from './Skeleton';
import { translateZodiacSign } from '../utils/astrologyTranslations';
import { haptics } from '../services/haptics';
import { ZodiacBadge } from './icons';
import { KeywordChip } from './KeywordChip';

const { height: SCREEN_HEIGHT } = Dimensions.get('window');

// Keywords based on moon phase for the return date
const PHASE_KEYWORDS: Record<string, string[]> = {
  new_moon: ['Intention', 'Nouveaute', 'Potentiel'],
  waxing_crescent: ['Action', 'Courage', 'Mouvement'],
  first_quarter: ['Decision', 'Perseverance', 'Force'],
  waxing_gibbous: ['Perfectionnement', 'Patience', 'Détail'],
  full_moon: ['Accomplissement', 'Celebration', 'Liberation'],
  waning_gibbous: ['Gratitude', 'Partage', 'Sagesse'],
  last_quarter: ['Lacher-prise', 'Transformation', 'Bilan'],
  waning_crescent: ['Repos', 'Introspection', 'Preparation'],
};

interface HeroLunarCardProps {
  lunarReturn: LunarReturn | null;
  loading?: boolean;
  onPress?: () => void;
}

/**
 * Determine la phase lunaire approximative depuis la date du return
 */
function getPhaseFromDate(returnDate: string): string {
  const date = new Date(returnDate);
  const dayOfMonth = date.getDate();

  // Approximation simple basee sur le jour du mois
  if (dayOfMonth <= 3) return 'new_moon';
  if (dayOfMonth <= 7) return 'waxing_crescent';
  if (dayOfMonth <= 11) return 'first_quarter';
  if (dayOfMonth <= 14) return 'waxing_gibbous';
  if (dayOfMonth <= 17) return 'full_moon';
  if (dayOfMonth <= 21) return 'waning_gibbous';
  if (dayOfMonth <= 25) return 'last_quarter';
  return 'waning_crescent';
}

/**
 * Formate le nom du mois avec l'annee
 */
const formatMonthName = (returnDate: string): string => {
  const date = new Date(returnDate);
  const formatted = date.toLocaleDateString('fr-FR', { month: 'long', year: 'numeric' });
  return formatted.charAt(0).toUpperCase() + formatted.slice(1);
};

/**
 * Formate la plage de dates du cycle lunaire
 */
const formatDateRange = (returnDate: string, endDate?: string): string => {
  const start = new Date(returnDate);
  const end = endDate ? new Date(endDate) : new Date(start.getTime() + 29.5 * 24 * 60 * 60 * 1000);

  const startStr = start.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' }).replace('.', '');
  const endStr = end.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' }).replace('.', '');

  return `${startStr} - ${endStr}`;
};

export function HeroLunarCard({ lunarReturn, loading, onPress }: HeroLunarCardProps) {
  const router = useRouter();
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const scaleAnim = useRef(new Animated.Value(0.95)).current;

  useEffect(() => {
    if (lunarReturn && !loading) {
      Animated.parallel([
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 600,
          easing: Easing.out(Easing.cubic),
          useNativeDriver: true,
        }),
        Animated.timing(scaleAnim, {
          toValue: 1,
          duration: 600,
          easing: Easing.out(Easing.cubic),
          useNativeDriver: true,
        }),
      ]).start();
    } else {
      fadeAnim.setValue(1);
      scaleAnim.setValue(1);
    }
  }, [lunarReturn, loading]);

  const handlePress = () => {
    haptics.light();
    if (onPress) {
      onPress();
    } else {
      router.push('/lunar/report');
    }
  };

  // Loading state
  if (loading && !lunarReturn) {
    return (
      <View style={styles.container}>
        <Skeleton width="100%" height={SCREEN_HEIGHT * 0.45} borderRadius={borderRadius.lg} />
      </View>
    );
  }

  // Pas de donnees
  if (!lunarReturn) {
    return null;
  }

  // Derive display data
  const monthName = formatMonthName(lunarReturn.return_date);
  const dateRange = formatDateRange(lunarReturn.return_date, lunarReturn.end_date);
  const moonSign = lunarReturn.moon_sign ? translateZodiacSign(lunarReturn.moon_sign) : 'Non disponible';
  const lunarAscendant = lunarReturn.lunar_ascendant ? translateZodiacSign(lunarReturn.lunar_ascendant) : 'Non disponible';

  // Get keywords based on return date phase
  const phase = getPhaseFromDate(lunarReturn.return_date);
  const keywords = PHASE_KEYWORDS[phase] || PHASE_KEYWORDS.new_moon;

  return (
    <Animated.View
      style={[
        styles.container,
        {
          opacity: fadeAnim,
          transform: [{ scale: scaleAnim }],
        },
      ]}
    >
      <Pressable
        testID="current-lunar-card"
        onPress={handlePress}
        style={({ pressed }) => [styles.card, pressed && styles.cardPressed]}
      >
        {/* Decorative blur circles */}
        <View style={styles.decorCircle1} />
        <View style={styles.decorCircle2} />

        {/* Question title */}
        <Text style={styles.questionTitle}>Quel est mon cycle actuel ?</Text>

        {/* Month title */}
        <Text style={styles.monthTitle}>{monthName}</Text>

        {/* Date range */}
        <Text style={styles.dateRange}>{dateRange}</Text>

        {/* Meta grid (Lune + Ascendant) */}
        <View style={styles.metaGrid}>
          <View style={styles.metaItem}>
            <View style={styles.metaRow}>
              {lunarReturn.moon_sign && (
                <ZodiacBadge sign={lunarReturn.moon_sign} size={36} />
              )}
              <View style={styles.metaTextContainer}>
                <Text style={styles.metaLabel}>Lune en</Text>
                <Text style={styles.metaValue}>{moonSign}</Text>
              </View>
            </View>
          </View>
          <View style={styles.metaItem}>
            <View style={styles.metaRow}>
              {lunarReturn.lunar_ascendant && (
                <ZodiacBadge sign={lunarReturn.lunar_ascendant} size={36} />
              )}
              <View style={styles.metaTextContainer}>
                <Text style={styles.metaLabel}>Ascendant</Text>
                <Text style={styles.metaValue}>{lunarAscendant}</Text>
              </View>
            </View>
          </View>
        </View>

        {/* Themes du mois */}
        <View style={styles.themesSection}>
          <Text style={styles.themesLabel}>Themes du mois</Text>
          <View style={styles.keywordsRow}>
            {keywords.map((keyword, index) => (
              <KeywordChip
                key={index}
                label={keyword}
                variant={index === 0 ? 'gold' : 'default'}
              />
            ))}
          </View>
        </View>

        {/* CTA Button */}
        <LinearGradient
          colors={[colors.accent, colors.accentDark]}
          start={{ x: 0, y: 0 }}
          end={{ x: 1, y: 0 }}
          style={styles.ctaButton}
        >
          <Text style={styles.ctaButtonText}>Voir le rapport mensuel</Text>
        </LinearGradient>
      </Pressable>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: spacing.md,
    marginVertical: spacing.md,
    zIndex: 1,
  },
  card: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    padding: spacing.xl,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.15)',
    overflow: 'hidden',
  },
  cardPressed: {
    opacity: 0.9,
  },
  decorCircle1: {
    position: 'absolute',
    top: -40,
    right: -40,
    width: 120,
    height: 120,
    borderRadius: 60,
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
  },
  decorCircle2: {
    position: 'absolute',
    bottom: 60,
    left: -30,
    width: 80,
    height: 80,
    borderRadius: 40,
    backgroundColor: 'rgba(255, 215, 0, 0.06)',
  },
  questionTitle: {
    ...fonts.body,
    color: colors.accent,
    marginBottom: spacing.sm,
    fontSize: 15,
    fontWeight: '500',
  },
  monthTitle: {
    fontSize: 32,
    fontWeight: '700',
    color: colors.text,
    marginBottom: spacing.xs,
    letterSpacing: -0.5,
  },
  dateRange: {
    ...fonts.body,
    color: colors.textMuted,
    marginBottom: spacing.xl,
    fontSize: 14,
  },
  metaGrid: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: spacing.xl,
    paddingVertical: spacing.lg,
    borderTopWidth: 1,
    borderBottomWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  metaItem: {
    flex: 1,
  },
  metaRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
  },
  metaTextContainer: {
    alignItems: 'flex-start',
  },
  metaLabel: {
    ...fonts.caption,
    color: colors.textMuted,
    marginBottom: 2,
    fontSize: 11,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  metaValue: {
    ...fonts.body,
    color: colors.text,
    fontSize: 16,
    fontWeight: '600',
  },
  themesSection: {
    marginBottom: spacing.xl,
  },
  themesLabel: {
    ...fonts.caption,
    color: colors.textMuted,
    marginBottom: spacing.sm,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  keywordsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  ctaButton: {
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    alignItems: 'center',
  },
  ctaButtonText: {
    ...fonts.button,
    color: '#000000',
    fontWeight: '600',
  },
});

export default HeroLunarCard;
