/**
 * Écran résultat - Affichage du thème natal calculé
 * Affiche les positions planétaires, maisons, aspects
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useNatalStore } from '../../stores/useNatalStore';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { tSign, tPlanet, formatAspectFR, formatDegree } from '../../i18n/astro.format';

// Mapping français des signes
const ZODIAC_EMOJI: Record<string, string> = {
  'Aries': '♈',
  'Taurus': '♉',
  'Gemini': '♊',
  'Cancer': '♋',
  'Leo': '♌',
  'Virgo': '♍',
  'Libra': '♎',
  'Scorpio': '♏',
  'Sagittarius': '♐',
  'Capricorn': '♑',
  'Aquarius': '♒',
  'Pisces': '♓',
};

// Helper pour symboles d'aspects
const getAspectSymbol = (type: string): string => {
  const symbols: Record<string, string> = {
    'conjunction': '☌',
    'opposition': '☍',
    'trine': '△',
    'square': '□',
    'sextile': '⚹',
  };
  return symbols[type.toLowerCase()] || '•';
};

export default function NatalChartResultScreen() {
  const router = useRouter();
  const { chart, clearChart } = useNatalStore();

  // Si pas de chart, rediriger vers l'écran intermédiaire
  React.useEffect(() => {
    if (!chart) {
      router.replace('/natal-chart');
    }
  }, [chart, router]);

  if (!chart) {
    return null; // En attente de redirection
  }

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
            <Text style={styles.backText}>← Retour</Text>
          </TouchableOpacity>
        </View>

        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          <View style={styles.resultContainer}>
            <Text style={styles.resultTitle}>✨ Ton Thème Natal</Text>

            {/* Big 3 */}
            {(chart.sun_sign || chart.moon_sign || chart.ascendant) && (
              <View style={styles.statsRow}>
                <View style={styles.statCard}>
                  <Text style={styles.statLabel}>Soleil</Text>
                  <Text style={styles.statEmoji}>
                    {ZODIAC_EMOJI[chart.sun_sign || ''] || '☀️'}
                  </Text>
                  <Text style={styles.statValue}>
                    {tSign(chart.sun_sign) || 'N/A'}
                  </Text>
                </View>

                <View style={styles.statCard}>
                  <Text style={styles.statLabel}>Lune</Text>
                  <Text style={styles.statEmoji}>
                    {ZODIAC_EMOJI[chart.moon_sign || ''] || '🌙'}
                  </Text>
                  <Text style={styles.statValue}>
                    {tSign(chart.moon_sign) || 'N/A'}
                  </Text>
                </View>

                <View style={styles.statCard}>
                  <Text style={styles.statLabel}>Ascendant</Text>
                  <Text style={styles.statEmoji}>⬆️</Text>
                  <Text style={styles.statValue}>
                    {tSign(chart.ascendant) || 'N/A'}
                  </Text>
                </View>
              </View>
            )}

            {/* Planètes */}
            {chart.planets && typeof chart.planets === 'object' && Object.keys(chart.planets).length > 0 && (
              <View style={styles.section}>
                <Text style={styles.sectionTitle}>🪐 Positions Planétaires</Text>
                {Object.entries(chart.planets).map(([planetName, planetData]: [string, any], index: number) => (
                  <View key={index} style={styles.planetRow}>
                    <Text style={styles.planetName}>
                      {tPlanet(planetName)}
                    </Text>
                    <Text style={styles.planetInfo}>
                      {planetData.sign ? `${ZODIAC_EMOJI[planetData.sign] || ''} ${tSign(planetData.sign)}` : 'N/A'}
                      {planetData.degree !== undefined && ` • ${formatDegree(planetData.degree)}`}
                      {planetData.house !== undefined && ` • Maison ${planetData.house}`}
                    </Text>
                  </View>
                ))}
              </View>
            )}

            {/* Maisons */}
            {chart.houses && (
              <View style={styles.section}>
                <Text style={styles.sectionTitle}>🏠 Maisons Astrologiques</Text>
                {Array.isArray(chart.houses) ? (
                  chart.houses.slice(0, 12).map((house: any, index: number) => (
                    <View key={index} style={styles.houseRow}>
                      <Text style={styles.houseNumber}>Maison {house.number || index + 1}</Text>
                      <Text style={styles.houseInfo}>
                        {house.sign ? `${ZODIAC_EMOJI[house.sign] || ''} ${tSign(house.sign)}` : 'N/A'}
                        {house.degree !== undefined && ` • ${formatDegree(house.degree)}`}
                      </Text>
                    </View>
                  ))
                ) : typeof chart.houses === 'object' ? (
                  Object.entries(chart.houses).slice(0, 12).map(([houseKey, houseData]: [string, any], index: number) => (
                    <View key={index} style={styles.houseRow}>
                      <Text style={styles.houseNumber}>Maison {houseKey || index + 1}</Text>
                      <Text style={styles.houseInfo}>
                        {houseData.sign ? `${ZODIAC_EMOJI[houseData.sign] || ''} ${tSign(houseData.sign)}` : 'N/A'}
                        {houseData.degree !== undefined && ` • ${formatDegree(houseData.degree)}`}
                      </Text>
                    </View>
                  ))
                ) : null}
              </View>
            )}

            {/* Aspects */}
            {chart.aspects && Array.isArray(chart.aspects) && chart.aspects.length > 0 && (
              <View style={styles.section}>
                <Text style={styles.sectionTitle}>✨ Aspects Majeurs</Text>
                {chart.aspects.slice(0, 10).map((aspect: any, index: number) => (
                  <View key={index} style={styles.aspectRow}>
                    <Text style={styles.aspectText}>
                      {formatAspectFR(aspect)}
                    </Text>
                  </View>
                ))}
              </View>
            )}

            {/* Bouton recalculer */}
            <TouchableOpacity
              style={styles.buttonSecondary}
              onPress={() => {
                clearChart();
                router.replace('/natal-chart');
              }}
            >
              <Text style={styles.buttonText}>Recalculer</Text>
            </TouchableOpacity>
          </View>
        </ScrollView>
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  header: {
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.md,
    paddingBottom: spacing.sm,
  },
  backButton: {
    marginBottom: spacing.sm,
  },
  backText: {
    ...fonts.body,
    color: colors.accent,
  },
  scrollContent: {
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.xl,
  },
  resultContainer: {
    width: '100%',
  },
  resultTitle: {
    ...fonts.h2,
    color: colors.gold,
    textAlign: 'center',
    marginBottom: spacing.xl,
    marginTop: spacing.md,
  },
  statsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: spacing.xl,
  },
  statCard: {
    flex: 1,
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.sm,
    padding: spacing.md,
    marginHorizontal: spacing.xs,
    alignItems: 'center',
  },
  statLabel: {
    ...fonts.caption,
    color: colors.textMuted,
    marginBottom: spacing.xs,
  },
  statEmoji: {
    fontSize: 32,
    marginBottom: spacing.xs,
  },
  statValue: {
    ...fonts.h3,
    color: colors.accent,
    textAlign: 'center',
  },
  section: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.lg,
  },
  sectionTitle: {
    ...fonts.h3,
    color: colors.gold,
    marginBottom: spacing.md,
  },
  planetRow: {
    paddingVertical: spacing.sm,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.1)',
  },
  planetName: {
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.xs,
    fontWeight: '600',
  },
  planetInfo: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  houseRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: spacing.sm,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.1)',
  },
  houseNumber: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '600',
  },
  houseInfo: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  aspectRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: spacing.sm,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.1)',
  },
  aspectText: {
    ...fonts.body,
    color: colors.text,
  },
  aspectOrb: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  buttonSecondary: {
    backgroundColor: colors.cardBg,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginTop: spacing.lg,
    borderWidth: 1,
    borderColor: colors.accent,
  },
  buttonText: {
    ...fonts.button,
    color: colors.accent,
  },
});

