/**
 * Composant Daily Lunar Climate - Card Hero
 * Affiche l'énergie du jour selon la Lune et le thème natal
 */

import React, { useMemo, useEffect, useRef, useState } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Animated } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import { useNatalStore } from '../stores/useNatalStore';
import { calculateDailyLunarClimate, MoonPosition } from '../services/lunarClimate';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { saveDailyResonance, hasRespondedToday, ResonanceValue } from '../services/dailyResonance';

interface DailyInsight {
  title: string;
  text: string;
  keywords: string[];
  version: string;
}

interface DailyLunarClimateProps {
  moonPosition: MoonPosition;
  insight?: DailyInsight | null; // Insight depuis le backend (optionnel)
}

// Emoji selon la phase lunaire
const getMoonPhaseEmoji = (phase: string): string => {
  const phaseEmojis: Record<string, string> = {
    'Nouvelle Lune': '🌑',
    'Premier Croissant': '🌒',
    'Premier Quartier': '🌓',
    'Lune Gibbeuse': '🌔',
    'Pleine Lune': '🌕',
    'Lune Disseminante': '🌖',
    'Dernier Quartier': '🌗',
    'Dernier Croissant': '🌘',
  };
  return phaseEmojis[phase] || '🌙';
};

export default function DailyLunarClimate({ moonPosition, insight }: DailyLunarClimateProps) {
  const { chart } = useNatalStore();
  const router = useRouter();

  // État pour la clôture du soir
  const [hasResponded, setHasResponded] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  // Animation d'entrée (fade-in + translation verticale)
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const translateYAnim = useRef(new Animated.Value(20)).current;

  useEffect(() => {
    // Animation douce au montage
    Animated.parallel([
      Animated.timing(fadeAnim, {
        toValue: 1,
        duration: 400,
        useNativeDriver: true,
      }),
      Animated.timing(translateYAnim, {
        toValue: 0,
        duration: 400,
        useNativeDriver: true,
      }),
    ]).start();

    // Vérifier si l'utilisateur a déjà répondu aujourd'hui
    checkIfResponded();
  }, []);

  const checkIfResponded = async () => {
    const responded = await hasRespondedToday();
    setHasResponded(responded);
  };

  // Calculer le climat du jour (fallback si pas d'insight backend)
  const climate = useMemo(() => {
    return calculateDailyLunarClimate(moonPosition, chart);
  }, [moonPosition, chart]);

  // Si pas de chart complet, afficher un CTA discret
  const handlePress = () => {
    if (!climate.hasFullChart) {
      router.push('/natal-chart');
    }
  };

  // Gestion de la clôture du soir
  const handleResonanceResponse = async (value: ResonanceValue) => {
    if (isSubmitting) return;

    setIsSubmitting(true);
    try {
      await saveDailyResonance(value);
      setHasResponded(true);

      // Fade out subtil des boutons
      setTimeout(() => {
        setIsSubmitting(false);
      }, 1000);
    } catch (error) {
      console.error('[DailyLunarClimate] Erreur enregistrement résonance:', error);
      setIsSubmitting(false);
    }
  };

  // Priorité: insight backend > climat calculé
  const displayTitle = insight ? insight.title : `Climat du jour : ${climate.theme}`;
  const displayMessage = insight ? insight.text : climate.message;

  // Conditions temporelles
  const currentHour = new Date().getHours();
  const isEvening = currentHour >= 20; // Anticipation pour demain
  const isReflectionTime = currentHour >= 19 && currentHour < 24; // Clôture du soir

  return (
    <Animated.View
      style={{
        opacity: fadeAnim,
        transform: [{ translateY: translateYAnim }],
      }}
    >
      <TouchableOpacity
        onPress={handlePress}
        activeOpacity={climate.hasFullChart ? 1 : 0.7}
        disabled={climate.hasFullChart}
      >
        <LinearGradient
          colors={['rgba(183, 148, 246, 0.15)', 'rgba(183, 148, 246, 0.05)']}
          start={{ x: 0, y: 0 }}
          end={{ x: 1, y: 1 }}
          style={styles.card}
        >
        {/* Header */}
        <View style={styles.header}>
          <View style={styles.headerLeft}>
            <Text style={styles.headerTitle}>🌙 Ton Climat Lunaire</Text>
            {!climate.hasFullChart && (
              <View style={styles.badge}>
                <Text style={styles.badgeText}>Basique</Text>
              </View>
            )}
          </View>
          <Text style={styles.todayIndicator}>Aujourd'hui</Text>
        </View>

        {/* Titre (insight backend ou climat calculé) */}
        <Text style={styles.title}>{displayTitle}</Text>

        {/* Message (insight backend ou climat calculé) */}
        <Text style={styles.message}>{displayMessage}</Text>

        {/* Keywords si insight backend disponible */}
        {insight && insight.keywords && insight.keywords.length > 0 && (
          <View style={styles.keywordsContainer}>
            {insight.keywords.slice(0, 4).map((keyword, index) => (
              <View key={index} style={styles.keywordBadge}>
                <Text style={styles.keywordText}>{keyword}</Text>
              </View>
            ))}
          </View>
        )}

        {/* Phase lunaire */}
        <View style={styles.phaseContainer}>
          <Text style={styles.phaseText}>
            {getMoonPhaseEmoji(climate.phase)} {climate.phase}
          </Text>
        </View>

        {/* Anticipation du soir (après 20h) */}
        {isEvening && (
          <View style={styles.anticipationContainer}>
            <Text style={styles.anticipationText}>Demain, une nouvelle énergie.</Text>
          </View>
        )}

        {/* Clôture du soir (après 19h, avant minuit) */}
        {isReflectionTime && !hasResponded && (
          <View style={styles.reflectionContainer}>
            <Text style={styles.reflectionQuestion}>Cette énergie a-t-elle résonné aujourd'hui ?</Text>
            <View style={styles.reflectionButtons}>
              <TouchableOpacity
                style={[styles.reflectionButton, isSubmitting && styles.reflectionButtonDisabled]}
                onPress={() => handleResonanceResponse('yes')}
                disabled={isSubmitting}
              >
                <Text style={styles.reflectionButtonText}>Oui</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.reflectionButton, isSubmitting && styles.reflectionButtonDisabled]}
                onPress={() => handleResonanceResponse('no')}
                disabled={isSubmitting}
              >
                <Text style={styles.reflectionButtonText}>Non</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.reflectionButton, isSubmitting && styles.reflectionButtonDisabled]}
                onPress={() => handleResonanceResponse('maybe')}
                disabled={isSubmitting}
              >
                <Text style={styles.reflectionButtonText}>Peut-être</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}

        {/* CTA si pas de chart complet */}
        {!climate.hasFullChart && (
          <View style={styles.ctaContainer}>
            <Text style={styles.ctaText}>
              💫 Calcule ton thème natal pour un climat ultra-personnalisé
            </Text>
          </View>
        )}
      </LinearGradient>
    </TouchableOpacity>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  card: {
    borderRadius: borderRadius.lg,
    padding: spacing.lg,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.3)',
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 8,
    elevation: 4,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.md,
  },
  headerLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
  },
  headerTitle: {
    fontSize: fonts.sizes.md,
    fontWeight: '700',
    color: colors.accent,
  },
  todayIndicator: {
    fontSize: 11,
    fontWeight: '400',
    color: 'rgba(255, 255, 255, 0.5)',
    fontStyle: 'italic',
  },
  badge: {
    backgroundColor: 'rgba(255, 193, 7, 0.2)',
    paddingHorizontal: spacing.sm,
    paddingVertical: 4,
    borderRadius: borderRadius.sm,
    borderWidth: 1,
    borderColor: 'rgba(255, 193, 7, 0.4)',
  },
  badgeText: {
    fontSize: 10,
    fontWeight: '600',
    color: '#FFC107',
    textTransform: 'uppercase',
  },
  title: {
    fontSize: fonts.sizes.lg,
    fontWeight: '700',
    color: colors.text,
    marginBottom: spacing.sm,
  },
  message: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.85)',
    lineHeight: 22,
    marginBottom: spacing.md,
  },
  keywordsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: spacing.xs,
    marginBottom: spacing.md,
  },
  keywordBadge: {
    backgroundColor: 'rgba(183, 148, 246, 0.2)',
    paddingHorizontal: spacing.sm,
    paddingVertical: 4,
    borderRadius: borderRadius.sm,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.4)',
  },
  keywordText: {
    fontSize: 11,
    fontWeight: '600',
    color: colors.accent,
  },
  phaseContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingTop: spacing.sm,
    borderTopWidth: 1,
    borderTopColor: 'rgba(183, 148, 246, 0.2)',
  },
  phaseText: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.7)',
    fontWeight: '600',
  },
  anticipationContainer: {
    marginTop: spacing.sm,
    paddingTop: spacing.sm,
  },
  anticipationText: {
    fontSize: 12,
    color: 'rgba(183, 148, 246, 0.7)',
    fontStyle: 'italic',
    fontWeight: '400',
  },
  reflectionContainer: {
    marginTop: spacing.md,
    paddingTop: spacing.md,
    borderTopWidth: 1,
    borderTopColor: 'rgba(183, 148, 246, 0.1)',
  },
  reflectionQuestion: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.8)',
    marginBottom: spacing.sm,
    textAlign: 'center',
    fontWeight: '500',
  },
  reflectionButtons: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: spacing.sm,
  },
  reflectionButton: {
    paddingVertical: 8,
    paddingHorizontal: spacing.md,
    borderRadius: borderRadius.sm,
    backgroundColor: 'rgba(183, 148, 246, 0.15)',
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.3)',
  },
  reflectionButtonDisabled: {
    opacity: 0.5,
  },
  reflectionButtonText: {
    fontSize: 12,
    color: colors.accent,
    fontWeight: '600',
  },
  ctaContainer: {
    marginTop: spacing.md,
    padding: spacing.sm,
    backgroundColor: 'rgba(255, 193, 7, 0.1)',
    borderRadius: borderRadius.sm,
    borderWidth: 1,
    borderColor: 'rgba(255, 193, 7, 0.3)',
  },
  ctaText: {
    fontSize: fonts.sizes.sm,
    color: '#FFC107',
    textAlign: 'center',
    fontWeight: '600',
  },
});
