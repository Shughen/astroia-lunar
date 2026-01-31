/**
 * Écran détail d'un mois lunaire
 * Route dynamique : /lunar-month/[month]
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { lunarReturns, LunarReturn } from '../../services/api';
import { tPlanet, tSign } from '../../i18n/astro.format';
import { MarkdownText } from '../../components/MarkdownText';
import { translateAstrologyText } from '../../utils/astrologyTranslations';

export default function LunarMonthScreen() {
  const router = useRouter();
  const { month } = useLocalSearchParams<{ month: string }>();
  const [loading, setLoading] = useState(true);
  const [lunarReturn, setLunarReturn] = useState<LunarReturn | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (month) {
      loadLunarReturn();
    }
  }, [month]);

  const loadLunarReturn = async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await lunarReturns.getByMonth(month as string);
      setLunarReturn(data);
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

  const formatDate = (dateString: string) => {
    try {
      const date = new Date(dateString);
      return date.toLocaleDateString('fr-FR', {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
      });
    } catch {
      return dateString;
    }
  };

  if (loading) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color={colors.accent} />
          <Text style={styles.loadingText}>Chargement du mois lunaire...</Text>
        </View>
      </LinearGradient>
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

  if (!lunarReturn) {
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
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
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

        {/* Date précise */}
        {lunarReturn.return_date && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>📅 Date de ta révolution</Text>
            <Text style={styles.dateText}>{formatDate(lunarReturn.return_date)}</Text>
          </View>
        )}

        {/* Position lunaire */}
        {(lunarReturn.moon_sign || lunarReturn.moon_house) && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>🌙 Position de la Lune</Text>
            {lunarReturn.moon_sign && (
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>Signe :</Text>
                <Text style={styles.infoValue}>{tSign(lunarReturn.moon_sign)}</Text>
              </View>
            )}
            {lunarReturn.moon_house && (
              <View style={styles.infoRow}>
                <Text style={styles.infoLabel}>Maison :</Text>
                <Text style={styles.infoValue}>Maison {lunarReturn.moon_house}</Text>
              </View>
            )}
          </View>
        )}

        {/* Ascendant lunaire */}
        {lunarReturn.lunar_ascendant && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>⬆️ Ascendant de ta révolution</Text>
            <Text style={styles.infoValue}>{tSign(lunarReturn.lunar_ascendant)}</Text>
          </View>
        )}

        {/* Aspects principaux */}
        {lunarReturn.aspects && lunarReturn.aspects.length > 0 && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>⭐ Aspects principaux</Text>
            {lunarReturn.aspects.slice(0, 5).map((aspect: any, index: number) => (
              <View key={index} style={styles.aspectRow}>
                <Text style={styles.aspectText}>
                  {aspect.planet1 && tPlanet(aspect.planet1)}
                  {aspect.type && ` ${aspect.type} `}
                  {aspect.planet2 && tPlanet(aspect.planet2)}
                  {aspect.orb !== undefined && ` (orbe: ${Math.abs(aspect.orb).toFixed(1)}°)`}
                </Text>
              </View>
            ))}
          </View>
        )}

        {/* Interprétation */}
        {lunarReturn.interpretation && (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>💡 Interprétation</Text>
            <MarkdownText style={styles.interpretationText}>
              {translateAstrologyText(lunarReturn.interpretation)}
            </MarkdownText>
          </View>
        )}

        {/* Empty state si pas de données */}
        {!lunarReturn.moon_sign && !lunarReturn.aspects?.length && !lunarReturn.interpretation && (
          <View style={styles.emptyDataCard}>
            <Text style={styles.emptyDataText}>
              Les détails de cette révolution lunaire seront disponibles prochainement
            </Text>
          </View>
        )}
      </ScrollView>
    </LinearGradient>
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
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    ...fonts.body,
    color: colors.text,
    marginTop: spacing.md,
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
  card: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.md,
  },
  cardTitle: {
    ...fonts.h3,
    color: colors.accent,
    marginBottom: spacing.md,
  },
  dateText: {
    ...fonts.body,
    color: colors.text,
    fontSize: 16,
  },
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.sm,
  },
  infoLabel: {
    ...fonts.body,
    color: colors.textMuted,
    fontSize: 14,
  },
  infoValue: {
    ...fonts.body,
    color: colors.text,
    fontSize: 16,
    fontWeight: '600',
  },
  aspectRow: {
    backgroundColor: 'rgba(139, 123, 247, 0.1)',
    padding: spacing.sm,
    borderRadius: borderRadius.sm,
    marginBottom: spacing.xs,
  },
  aspectText: {
    ...fonts.body,
    color: colors.text,
    fontSize: 14,
  },
  interpretationText: {
    ...fonts.body,
    color: colors.text,
    fontSize: 15,
    lineHeight: 22,
  },
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
  emptyDataCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.xl,
    alignItems: 'center',
    marginTop: spacing.lg,
  },
  emptyDataText: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    fontStyle: 'italic',
  },
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
