/**
 * Écran détail d'un mois lunaire
 * Route dynamique : /lunar-month/[month]
 *
 * Affiche le rapport enrichi identique à /lunar/report.tsx
 * avec titre dynamique (ex: "Janvier 2026")
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import apiClient, { lunarReturns } from '../../services/api';
import { tPlanet } from '../../i18n/astro.format';
import { MarkdownText } from '../../components/MarkdownText';
import { translateAstrologyText, translateZodiacSign } from '../../utils/astrologyTranslations';
import { trackLunarReturnViewed, trackScreenView } from '../../services/analytics';
import { AspectDetailSheet } from '../../components/AspectDetailSheet';
import { AnimatedCard } from '../../components/AnimatedCard';
import LunarInterpretationLoader from '../../components/LunarInterpretationLoader';
import { haptics } from '../../services/haptics';
import type { AspectV4 } from '../../types/api';

// Interface pour le rapport enrichi (identique à report.tsx)
interface LunarReport {
  lunar_return_id: number;
  header: {
    month: string;
    dates: string;
    moon_sign: string;
    moon_house: number;
    lunar_ascendant: string;
  };
  general_climate: string;
  dominant_axes: string[];
  major_aspects: AspectV4[];
  lunar_interpretation?: {
    climate: string | null;
    focus: string | null;
    approach: string | null;
    full: string | null;
  };
}

export default function LunarMonthScreen() {
  const router = useRouter();
  const { month } = useLocalSearchParams<{ month: string }>();
  const [loading, setLoading] = useState(true);
  const [report, setReport] = useState<LunarReport | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedAspect, setSelectedAspect] = useState<AspectV4 | null>(null);

  useEffect(() => {
    if (month) {
      loadLunarReturn();
      // Track screen view et lunar return viewed
      trackScreenView('lunar_month', { month });
      trackLunarReturnViewed(month);
    }
  }, [month]);

  const loadLunarReturn = async () => {
    try {
      setLoading(true);
      setError(null);

      // Étape 1: Récupérer LunarReturn basique pour avoir l'ID
      const basicData = await lunarReturns.getByMonth(month as string);
      if (!basicData?.id) {
        throw new Error('Cycle lunaire non trouvé');
      }

      // Étape 2: Appeler l'API du rapport enrichi
      const response = await apiClient.get(`/api/lunar-returns/${basicData.id}/report`);
      setReport(response.data);
    } catch (err: any) {
      console.error('[LunarMonth] Erreur chargement:', err);
      setError(err.response?.data?.detail || err.message || 'Erreur lors du chargement');
    } finally {
      setLoading(false);
    }
  };

  // Formatage du mois pour affichage
  const formatMonth = (monthParam: string | undefined) => {
    if (!monthParam) return 'Mois inconnu';

    try {
      const [year, monthNum] = monthParam.split('-');
      const monthNames = [
        'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
        'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
      ];
      const monthIndex = parseInt(monthNum, 10) - 1;
      if (monthIndex >= 0 && monthIndex < 12) {
        return `${monthNames[monthIndex]} ${year}`;
      }
      return monthParam;
    } catch {
      return monthParam;
    }
  };

  // Symbole pour les aspects
  const getAspectSymbol = (type: string): string => {
    const symbols: { [key: string]: string } = {
      conjunction: '☌',
      opposition: '☍',
      square: '□',
      trine: '△',
      sextile: '⚹',
    };
    return symbols[type.toLowerCase()] || type;
  };

  // Header avec infos du cycle
  const renderHeader = () => {
    if (!report) return null;

    const { dates, moon_sign, moon_house, lunar_ascendant } = report.header;
    const translatedMoonSign = translateZodiacSign(moon_sign);
    const translatedAscendant = translateZodiacSign(lunar_ascendant);

    return (
      <AnimatedCard style={styles.headerCard} delay={0} duration={500}>
        <Text style={styles.dates}>{dates}</Text>

        <View style={styles.headerInfoGrid}>
          <View style={styles.headerInfoItem}>
            <Text style={styles.headerLabel}>Lune en</Text>
            <Text style={styles.headerValue}>
              {translatedMoonSign} (Maison {moon_house})
            </Text>
          </View>

          <View style={styles.headerInfoItem}>
            <Text style={styles.headerLabel}>Ascendant lunaire</Text>
            <Text style={styles.headerValue}>{translatedAscendant}</Text>
          </View>
        </View>
      </AnimatedCard>
    );
  };

  // Section climat général
  const renderClimate = () => {
    if (!report) return null;

    // Priorité : lunar_interpretation.full (IA) > general_climate (templates)
    const climateText = report.lunar_interpretation?.full || report.general_climate;
    if (!climateText) return null;

    const translatedClimate = translateAstrologyText(climateText);

    return (
      <AnimatedCard style={styles.card} delay={100} duration={500}>
        <Text style={styles.cardTitle}>🌙 Climat général du mois</Text>
        <MarkdownText style={styles.climateText}>{translatedClimate}</MarkdownText>
      </AnimatedCard>
    );
  };

  // Section aspects majeurs cliquables
  const renderAspects = () => {
    if (!report || !report.major_aspects || report.major_aspects.length === 0) {
      return null;
    }

    return (
      <AnimatedCard style={styles.card} delay={200} duration={500}>
        <Text style={styles.cardTitle}>⭐ Aspects majeurs du cycle</Text>
        <Text style={styles.aspectsSubtitle}>
          {report.major_aspects.length} aspect{report.major_aspects.length > 1 ? 's' : ''} identifié{report.major_aspects.length > 1 ? 's' : ''}
        </Text>

        {report.major_aspects.map((aspect, index) => (
          <TouchableOpacity
            key={aspect.id || index}
            style={styles.aspectRow}
            onPress={() => {
              haptics.light();
              setSelectedAspect(aspect);
            }}
          >
            <View style={styles.aspectHeader}>
              <View style={styles.aspectPlanetsRow}>
                <Text style={styles.aspectPlanets}>
                  {tPlanet(aspect.planet1)} {getAspectSymbol(aspect.type)} {tPlanet(aspect.planet2)}
                </Text>
                {aspect.copy?.shadow && (
                  <Text style={styles.shadowBadge}>⚠️</Text>
                )}
              </View>
              <Text style={styles.aspectOrb}>
                {Math.abs(aspect.orb).toFixed(1)}°
              </Text>
            </View>

            {aspect.copy?.summary && (
              <Text style={styles.aspectSummary} numberOfLines={2}>
                {translateAstrologyText(aspect.copy.summary)}
              </Text>
            )}

            <Text style={styles.aspectCTA}>Voir détails →</Text>
          </TouchableOpacity>
        ))}
      </AnimatedCard>
    );
  };

  if (loading) {
    return (
      <LunarInterpretationLoader message="Chargement de ton cycle lunaire..." />
    );
  }

  if (error) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <ScrollView contentContainerStyle={styles.scrollContent}>
          <TouchableOpacity
            style={styles.backButton}
            onPress={() => router.back()}
            hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
          >
            <Text style={styles.backText}>← Retour</Text>
          </TouchableOpacity>

          <View style={styles.errorContainer}>
            <Text style={styles.errorEmoji}>⚠️</Text>
            <Text style={styles.errorText}>{error}</Text>
            <TouchableOpacity style={styles.retryButton} onPress={loadLunarReturn}>
              <Text style={styles.retryText}>Réessayer</Text>
            </TouchableOpacity>
          </View>
        </ScrollView>
      </LinearGradient>
    );
  }

  if (!report) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <ScrollView contentContainerStyle={styles.scrollContent}>
          <TouchableOpacity
            style={styles.backButton}
            onPress={() => router.back()}
            hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
          >
            <Text style={styles.backText}>← Retour</Text>
          </TouchableOpacity>

          <View style={styles.emptyContainer}>
            <Text style={styles.emptyEmoji}>🌙</Text>
            <Text style={styles.emptyText}>
              Aucune révolution lunaire pour {formatMonth(month)}
            </Text>
            <Text style={styles.emptySubtext}>
              Les révolutions lunaires sont générées automatiquement chaque mois
            </Text>
          </View>
        </ScrollView>
      </LinearGradient>
    );
  }

  return (
    <>
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <ScrollView contentContainerStyle={styles.scrollContent}>
          {/* Header avec titre dynamique */}
          <View style={styles.header}>
            <TouchableOpacity
              style={styles.backButton}
              onPress={() => router.back()}
              hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
            >
              <Text style={styles.backText}>← Retour</Text>
            </TouchableOpacity>

            <View style={styles.titleContainer}>
              <Text style={styles.title}>🌙 Révolution Lunaire</Text>
              <Text style={styles.monthText}>{formatMonth(month)}</Text>
            </View>
          </View>

          {/* Sections enrichies (identiques à report.tsx) */}
          {renderHeader()}
          {renderClimate()}
          {renderAspects()}

          {/* Footer */}
          <View style={styles.footer}>
            <Text style={styles.footerText}>✨ Généré spécialement pour toi</Text>
          </View>
        </ScrollView>
      </LinearGradient>

      {/* Bottom sheet pour détail aspect */}
      <AspectDetailSheet
        aspect={selectedAspect}
        visible={!!selectedAspect}
        onClose={() => setSelectedAspect(null)}
      />
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    padding: spacing.lg,
    paddingTop: 60,
  },
  header: {
    marginBottom: spacing.xl,
  },
  backButton: {
    marginBottom: spacing.md,
  },
  backText: {
    ...fonts.body,
    color: colors.accent,
    fontSize: 16,
  },
  titleContainer: {
    alignItems: 'center',
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    marginBottom: spacing.sm,
  },
  monthText: {
    ...fonts.h2,
    color: colors.gold,
  },
  // Header card (infos cycle)
  headerCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.md,
    borderWidth: 2,
    borderColor: colors.accent,
  },
  dates: {
    fontSize: 16,
    color: colors.textMuted,
    textAlign: 'center',
    marginBottom: spacing.lg,
  },
  headerInfoGrid: {
    gap: spacing.md,
  },
  headerInfoItem: {
    backgroundColor: 'rgba(10, 14, 39, 0.6)',
    padding: spacing.md,
    borderRadius: borderRadius.sm,
  },
  headerLabel: {
    fontSize: 12,
    color: colors.textMuted,
    marginBottom: 4,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  headerValue: {
    fontSize: 16,
    color: colors.text,
    fontWeight: '600',
  },
  // Card générique
  card: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(139, 123, 247, 0.3)',
  },
  cardTitle: {
    ...fonts.h3,
    color: colors.accent,
    marginBottom: spacing.md,
  },
  // Climat
  climateText: {
    fontSize: 15,
    color: colors.text,
    lineHeight: 24,
  },
  // Aspects
  aspectsSubtitle: {
    fontSize: 14,
    color: colors.textMuted,
    marginBottom: spacing.md,
  },
  aspectRow: {
    marginBottom: spacing.md,
    padding: spacing.md,
    backgroundColor: 'rgba(10, 14, 39, 0.6)',
    borderRadius: borderRadius.sm,
    borderWidth: 1,
    borderColor: 'rgba(139, 123, 247, 0.2)',
  },
  aspectHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.sm,
  },
  aspectPlanetsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
    flex: 1,
  },
  aspectPlanets: {
    fontSize: 16,
    color: colors.text,
    fontWeight: '600',
  },
  shadowBadge: {
    fontSize: 16,
    marginLeft: 4,
  },
  aspectOrb: {
    fontSize: 14,
    color: colors.accent,
    fontWeight: '600',
  },
  aspectSummary: {
    fontSize: 14,
    color: colors.textMuted,
    lineHeight: 20,
    marginBottom: spacing.sm,
  },
  aspectCTA: {
    fontSize: 14,
    color: colors.accent,
    fontWeight: '600',
  },
  // Footer
  footer: {
    padding: spacing.lg,
    alignItems: 'center',
    marginTop: spacing.lg,
    borderTopWidth: 1,
    borderTopColor: 'rgba(139, 123, 247, 0.2)',
  },
  footerText: {
    fontSize: 12,
    color: colors.textMuted,
    textAlign: 'center',
  },
  // Empty state
  emptyContainer: {
    alignItems: 'center',
    marginTop: 60,
  },
  emptyEmoji: {
    fontSize: 60,
    marginBottom: spacing.lg,
  },
  emptyText: {
    ...fonts.h3,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  emptySubtext: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    fontStyle: 'italic',
  },
  // Error state
  errorContainer: {
    alignItems: 'center',
    marginTop: 60,
  },
  errorEmoji: {
    fontSize: 60,
    marginBottom: spacing.lg,
  },
  errorText: {
    ...fonts.body,
    color: '#f87171',
    textAlign: 'center',
    marginBottom: spacing.lg,
  },
  retryButton: {
    backgroundColor: colors.accent,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
  },
  retryText: {
    ...fonts.body,
    color: '#000000',
    fontWeight: '600',
  },
});
