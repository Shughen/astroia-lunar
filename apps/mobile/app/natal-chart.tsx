/**
 * Écran de calcul et affichage du thème natal
 * Utilise Ephemeris API via /api/natal-chart
 */

import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  TextInput,
  Alert,
  ActivityIndicator,
  Animated,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import { useNatalStore } from '../stores/useNatalStore';
import { natalChart } from '../services/api';
import { geocodePlace } from '../services/geocoding';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Mapping français des signes
const ZODIAC_SIGNS_FR: Record<string, { emoji: string; name: string }> = {
  'Aries': { emoji: '♈', name: 'Bélier' },
  'Taurus': { emoji: '♉', name: 'Taureau' },
  'Gemini': { emoji: '♊', name: 'Gémeaux' },
  'Cancer': { emoji: '♋', name: 'Cancer' },
  'Leo': { emoji: '♌', name: 'Lion' },
  'Virgo': { emoji: '♍', name: 'Vierge' },
  'Libra': { emoji: '♎', name: 'Balance' },
  'Scorpio': { emoji: '♏', name: 'Scorpion' },
  'Sagittarius': { emoji: '♐', name: 'Sagittaire' },
  'Capricorn': { emoji: '♑', name: 'Capricorne' },
  'Aquarius': { emoji: '♒', name: 'Verseau' },
  'Pisces': { emoji: '♓', name: 'Poissons' },
};

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

export default function NatalChartScreen() {
  const router = useRouter();
  const { chart, loading, setChart, setLoading } = useNatalStore();
  
  // Formulaire
  const [name, setName] = useState('');
  const [date, setDate] = useState('1990-05-15');
  const [time, setTime] = useState('14:30');
  const [birthPlace, setBirthPlace] = useState('Paris, France');
  const [timezone, setTimezone] = useState('Europe/Paris');

  const handleCalculate = async () => {
    if (!birthPlace || birthPlace.trim().length < 2) {
      Alert.alert('Erreur', 'Merci de saisir un lieu de naissance');
      return;
    }

    setLoading(true);
    try {
      // Géocoder le lieu de naissance
      const coords = await geocodePlace(birthPlace);

      // Utiliser l'endpoint Ephemeris API (pas RapidAPI)
      const response = await natalChart.calculate({
        date: date, // YYYY-MM-DD
        time: time || '12:00', // HH:MM (fallback à midi si manquant)
        latitude: coords.latitude,
        longitude: coords.longitude,
        place_name: birthPlace || 'Lieu inconnu',
        timezone: timezone || 'Europe/Paris',
      });

      // Le format de réponse est différent : {id, sun_sign, moon_sign, ascendant, planets, houses, aspects}
      setChart(response);
      Alert.alert('Succès', 'Thème natal calculé avec succès ! ✨');
    } catch (error: any) {
      console.error('Erreur calcul thème natal:', error);
      // Gérer les erreurs de géocodage
      if (error.message === 'Lieu introuvable') {
        Alert.alert('Lieu introuvable', 'Précise la ville + pays');
      } else if (error.message?.includes('Timeout')) {
        Alert.alert('Erreur', 'Le géocodage a pris trop de temps, réessayez');
      } else if (error.message?.includes('connexion') || error.message?.includes('réseau')) {
        Alert.alert('Erreur', 'Erreur de connexion, vérifiez votre réseau');
      } else {
        Alert.alert(
          'Erreur',
          error.response?.data?.detail || error.message || 'Impossible de calculer le thème natal'
        );
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
          <Text style={styles.backText}>← Retour</Text>
        </TouchableOpacity>

        <View style={styles.header}>
          <Text style={styles.emoji}>⭐</Text>
          <Text style={styles.title}>Thème Natal</Text>
          <Text style={styles.subtitle}>
            Calcule ton thème natal complet via Ephemeris API
          </Text>
        </View>

        {/* Formulaire */}
        {!chart && (
          <View style={styles.form}>
            <Text style={styles.label}>Nom (optionnel)</Text>
            <TextInput
              style={styles.input}
              placeholder="Ton nom"
              placeholderTextColor={colors.textMuted}
              value={name}
              onChangeText={setName}
            />

            <Text style={styles.label}>Date de naissance (AAAA-MM-JJ)</Text>
            <TextInput
              style={styles.input}
              placeholder="1990-05-15"
              placeholderTextColor={colors.textMuted}
              value={date}
              onChangeText={setDate}
            />

            <Text style={styles.label}>Heure de naissance (HH:MM)</Text>
            <TextInput
              style={styles.input}
              placeholder="14:30"
              placeholderTextColor={colors.textMuted}
              value={time}
              onChangeText={setTime}
            />

            <Text style={styles.label}>Lieu de naissance</Text>
            <TextInput
              style={styles.input}
              placeholder="Paris, France"
              placeholderTextColor={colors.textMuted}
              value={birthPlace}
              onChangeText={setBirthPlace}
            />

            <Text style={styles.label}>Timezone</Text>
            <TextInput
              style={styles.input}
              placeholder="Europe/Paris"
              placeholderTextColor={colors.textMuted}
              value={timezone}
              onChangeText={setTimezone}
            />

            <TouchableOpacity
              style={[styles.button, loading && styles.buttonDisabled]}
              onPress={handleCalculate}
              disabled={loading}
            >
              {loading ? (
                <ActivityIndicator color="#fff" />
              ) : (
                <Text style={styles.buttonText}>Calculer mon thème ✨</Text>
              )}
            </TouchableOpacity>
          </View>
        )}

        {/* Résultat */}
        {chart && (
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
                    {chart.sun_sign || 'N/A'}
                  </Text>
                </View>

                <View style={styles.statCard}>
                  <Text style={styles.statLabel}>Lune</Text>
                  <Text style={styles.statEmoji}>
                    {ZODIAC_EMOJI[chart.moon_sign || ''] || '🌙'}
                  </Text>
                  <Text style={styles.statValue}>
                    {chart.moon_sign || 'N/A'}
                  </Text>
                </View>

                <View style={styles.statCard}>
                  <Text style={styles.statLabel}>Ascendant</Text>
                  <Text style={styles.statEmoji}>⬆️</Text>
                  <Text style={styles.statValue}>
                    {chart.ascendant || 'N/A'}
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
                      {planetName}
                    </Text>
                    <Text style={styles.planetInfo}>
                      {planetData.sign ? `${ZODIAC_EMOJI[planetData.sign] || ''} ${planetData.sign}` : 'N/A'}
                      {planetData.degree !== undefined && ` • ${planetData.degree.toFixed(2)}°`}
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
                        {house.sign ? `${ZODIAC_EMOJI[house.sign] || ''} ${house.sign}` : 'N/A'}
                        {house.degree !== undefined && ` • ${house.degree.toFixed(2)}°`}
                      </Text>
                    </View>
                  ))
                ) : typeof chart.houses === 'object' ? (
                  Object.entries(chart.houses).slice(0, 12).map(([houseKey, houseData]: [string, any], index: number) => (
                    <View key={index} style={styles.houseRow}>
                      <Text style={styles.houseNumber}>Maison {houseKey || index + 1}</Text>
                      <Text style={styles.houseInfo}>
                        {houseData.sign ? `${ZODIAC_EMOJI[houseData.sign] || ''} ${houseData.sign}` : 'N/A'}
                        {houseData.degree !== undefined && ` • ${houseData.degree.toFixed(2)}°`}
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
                      {aspect.planet1 || aspect.from_planet || 'Planet1'} {getAspectSymbol(aspect.type || aspect.aspect_type || '')} {aspect.planet2 || aspect.to_planet || 'Planet2'}
                    </Text>
                    <Text style={styles.aspectOrb}>
                      {aspect.orb !== undefined ? `Orb: ${aspect.orb.toFixed(1)}°` : ''}
                      {aspect.angle !== undefined && ` • Angle: ${aspect.angle.toFixed(1)}°`}
                    </Text>
                  </View>
                ))}
              </View>
            )}

            {/* Bouton recalculer */}
            <TouchableOpacity
              style={styles.buttonSecondary}
              onPress={() => setChart(null)}
            >
              <Text style={styles.buttonText}>Recalculer</Text>
            </TouchableOpacity>
          </View>
        )}
      </ScrollView>
    </LinearGradient>
  );
}

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

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    paddingTop: 60,
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.xl,
  },
  backButton: {
    marginBottom: spacing.md,
  },
  backText: {
    ...fonts.body,
    color: colors.accent,
  },
  header: {
    alignItems: 'center',
    marginBottom: spacing.xl,
  },
  emoji: {
    fontSize: 64,
    marginBottom: spacing.sm,
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
  },
  form: {
    width: '100%',
  },
  label: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginBottom: spacing.xs,
    marginTop: spacing.md,
  },
  input: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.sm,
    padding: spacing.md,
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.sm,
  },
  button: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginTop: spacing.lg,
  },
  buttonSecondary: {
    backgroundColor: colors.cardBg,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginTop: spacing.lg,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  buttonText: {
    ...fonts.button,
    color: colors.text,
  },
  resultContainer: {
    width: '100%',
  },
  resultTitle: {
    ...fonts.h2,
    color: colors.gold,
    textAlign: 'center',
    marginBottom: spacing.xl,
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
});

