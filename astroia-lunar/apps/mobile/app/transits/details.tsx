import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { tPlanet, tAspect, formatOrb } from '../../i18n/astro.format';

export default function TransitsDetails() {
  const router = useRouter();
  const params = useLocalSearchParams();

  // Récupérer les vraies données depuis les params de navigation
  // Les interprétations reflètent le format factuel + manifestations concrètes
  // Format API backend: "Quoi + Comment ça se manifeste concrètement"
  const aspectDetails = {
    transit_planet: (params.transit_planet as string) || 'Jupiter',
    natal_planet: (params.natal_planet as string) || 'Sun',
    aspect: (params.aspect as string) || 'trine',
    orb: params.orb ? parseFloat(params.orb as string) : 1.2,
    interpretation:
      (params.interpretation as string) ||
      "Jupiter soutient votre identité. Facilité naturelle, opportunités fluides dans les domaines liés à Jupiter. Sentiment d'expansion sans forcer, confiance en soi amplifiée, visibilité accrue.",
    timing: {
      exact_date: (params.exact_date as string) || '2025-11-15T14:30:00',
      orb_range: (params.orb_range as string) || '2025-11-12 → 2025-11-18',
    },
    themes: params.themes
      ? (typeof params.themes === 'string' ? JSON.parse(params.themes) : params.themes)
      : ['expansion', 'opportunités', 'confiance', 'fluidité'],
    recommendations: params.recommendations
      ? (typeof params.recommendations === 'string' ? JSON.parse(params.recommendations) : params.recommendations)
      : [
          'Période propice aux projets à long terme : les démarches se font naturellement',
          'Votre rayonnement personnel attire des opportunités sans effort',
          'Bon moment pour élargir votre champ d\'action (formations, voyages, nouveaux contacts)',
          'Attention à ne pas disperser l\'énergie : choisir 1-2 priorités',
        ],
  };

  return (
    <LinearGradient colors={['#1a0b2e', '#2d1b4e']} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top']}>
        <ScrollView contentContainerStyle={styles.scrollContent}>
          {/* Back Button */}
          <TouchableOpacity
            style={styles.backButton}
            onPress={() => router.back()}
          >
            <Text style={styles.backText}>← Retour</Text>
          </TouchableOpacity>

          {/* Header */}
          <View style={styles.header}>
            <Text style={styles.aspectBadge}>
              {aspectDetails.aspect === 'trine' ? '▲' : '●'}
            </Text>
            <Text style={styles.title}>
              {tPlanet(aspectDetails.transit_planet)} {tAspect(aspectDetails.aspect)}{' '}
              {tPlanet(aspectDetails.natal_planet)}
            </Text>
          </View>

          {/* Orb */}
          <View style={styles.orbContainer}>
            <Text style={styles.orbLabel}>Orbe :</Text>
            <Text style={styles.orbValue}>{formatOrb(aspectDetails.orb)}</Text>
          </View>

          {/* Interpretation */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>🔍 Ce qui se passe</Text>
            <Text style={styles.interpretation}>
              {aspectDetails.interpretation}
            </Text>
          </View>

          {/* Timing */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>⏰ Timing</Text>
            <View style={styles.timingCard}>
              <Text style={styles.timingLabel}>Aspect exact :</Text>
              <Text style={styles.timingValue}>
                {new Date(aspectDetails.timing.exact_date).toLocaleDateString('fr-FR', {
                  weekday: 'long',
                  day: 'numeric',
                  month: 'long',
                  hour: '2-digit',
                  minute: '2-digit',
                })}
              </Text>
              <Text style={styles.timingLabel}>Période d'influence :</Text>
              <Text style={styles.timingValue}>{aspectDetails.timing.orb_range}</Text>
            </View>
          </View>

          {/* Themes */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>🎯 Thèmes</Text>
            <View style={styles.themesContainer}>
              {aspectDetails.themes.map((theme, index) => (
                <View key={index} style={styles.themeBadge}>
                  <Text style={styles.themeText}>{theme}</Text>
                </View>
              ))}
            </View>
          </View>

          {/* Recommendations */}
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>💡 Comment utiliser cette énergie</Text>
            {aspectDetails.recommendations.map((rec, index) => (
              <View key={index} style={styles.recCard}>
                <Text style={styles.recBullet}>•</Text>
                <Text style={styles.recText}>{rec}</Text>
              </View>
            ))}
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
  scrollContent: {
    padding: 20,
  },
  backButton: {
    marginBottom: 16,
  },
  backText: {
    color: '#b794f6',
    fontSize: 16,
  },
  header: {
    alignItems: 'center',
    marginBottom: 24,
  },
  aspectBadge: {
    fontSize: 48,
    marginBottom: 8,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#ffd700',
    textAlign: 'center',
  },
  orbContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 24,
  },
  orbLabel: {
    fontSize: 16,
    color: '#a0a0b0',
    marginRight: 8,
  },
  orbValue: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#ffffff',
  },
  section: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#b794f6',
    marginBottom: 12,
  },
  interpretation: {
    fontSize: 16,
    color: '#ffffff',
    lineHeight: 24,
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    padding: 16,
    borderRadius: 12,
    borderLeftWidth: 4,
    borderLeftColor: '#b794f6',
  },
  timingCard: {
    backgroundColor: 'rgba(42, 26, 78, 0.6)',
    padding: 16,
    borderRadius: 12,
  },
  timingLabel: {
    fontSize: 14,
    color: '#a0a0b0',
    marginBottom: 4,
  },
  timingValue: {
    fontSize: 16,
    color: '#ffffff',
    marginBottom: 12,
  },
  themesContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  themeBadge: {
    backgroundColor: 'rgba(255, 215, 0, 0.2)',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#ffd700',
  },
  themeText: {
    color: '#ffd700',
    fontSize: 14,
    fontWeight: '600',
  },
  recCard: {
    flexDirection: 'row',
    backgroundColor: 'rgba(183, 148, 246, 0.05)',
    padding: 12,
    borderRadius: 8,
    marginBottom: 8,
  },
  recBullet: {
    color: '#ffd700',
    fontSize: 18,
    marginRight: 8,
    lineHeight: 20,
  },
  recText: {
    flex: 1,
    color: '#ffffff',
    fontSize: 14,
    lineHeight: 20,
  },
  loadingText: {
    color: '#ffffff',
    marginTop: 16,
    fontSize: 16,
  },
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  errorEmoji: {
    fontSize: 60,
    marginBottom: 16,
  },
  errorText: {
    color: '#f87171',
    fontSize: 16,
    textAlign: 'center',
  },
});

