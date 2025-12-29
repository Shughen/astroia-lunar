/**
 * Écran résultat - Affichage du thème natal calculé
 * Affiche les positions planétaires, maisons, aspects
 */

import React, { useState } from 'react';
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
import NatalInterpretationModal from '../../components/NatalInterpretationModal';
import { NatalSubject, ChartPayload } from '../../types/natal';
import { planetNameToSubject, buildSubjectPayload } from '../../utils/natalChartUtils';

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

  // State pour le modal d'interprétation
  const [modalVisible, setModalVisible] = useState(false);
  const [selectedSubject, setSelectedSubject] = useState<NatalSubject | null>(null);
  const [selectedPayload, setSelectedPayload] = useState<ChartPayload | null>(null);

  // Générer chart_id stable (simplifié pour V1 - utiliser hash en prod)
  const chartId = chart ? `chart_${chart.sun_sign}_${chart.moon_sign}_${chart.ascendant}` : 'unknown';

  // Handler pour clic sur un placement
  const handlePlacementClick = (subject: NatalSubject) => {
    if (!chart) return;

    const payload = buildSubjectPayload(subject, chart);
    setSelectedSubject(subject);
    setSelectedPayload(payload);
    setModalVisible(true);
  };

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

            {/* Big 3 - Cliquable pour afficher l'interprétation */}
            {(chart.sun_sign || chart.moon_sign || chart.ascendant) && (
              <View style={styles.statsRow}>
                <TouchableOpacity
                  style={styles.statCard}
                  onPress={() => handlePlacementClick('sun')}
                  activeOpacity={0.7}
                >
                  <Text style={styles.statLabel}>Soleil</Text>
                  <Text style={styles.statEmoji}>
                    {ZODIAC_EMOJI[chart.sun_sign || ''] || '☀️'}
                  </Text>
                  <Text style={styles.statValue}>
                    {tSign(chart.sun_sign) || 'N/A'}
                  </Text>
                  <Text style={styles.tapHint}>Tap pour interpréter</Text>
                </TouchableOpacity>

                <TouchableOpacity
                  style={styles.statCard}
                  onPress={() => handlePlacementClick('moon')}
                  activeOpacity={0.7}
                >
                  <Text style={styles.statLabel}>Lune</Text>
                  <Text style={styles.statEmoji}>
                    {ZODIAC_EMOJI[chart.moon_sign || ''] || '🌙'}
                  </Text>
                  <Text style={styles.statValue}>
                    {tSign(chart.moon_sign) || 'N/A'}
                  </Text>
                  <Text style={styles.tapHint}>Tap pour interpréter</Text>
                </TouchableOpacity>

                <TouchableOpacity
                  style={styles.statCard}
                  onPress={() => handlePlacementClick('ascendant')}
                  activeOpacity={0.7}
                >
                  <Text style={styles.statLabel}>Ascendant</Text>
                  <Text style={styles.statEmoji}>⬆️</Text>
                  <Text style={styles.statValue}>
                    {tSign(chart.ascendant) || 'N/A'}
                  </Text>
                  <Text style={styles.tapHint}>Tap pour interpréter</Text>
                </TouchableOpacity>
              </View>
            )}

            {/* Planètes - Ordre spécifique */}
            {chart.planets && typeof chart.planets === 'object' && Object.keys(chart.planets).length > 0 && (
              <View style={styles.section}>
                <Text style={styles.sectionTitle}>🪐 Positions Planétaires</Text>
                {(() => {
                  // Ordre spécifique : Soleil, Lune, Ascendant, Milieu du Ciel, puis les autres
                  // Ordre spécifique : Soleil, Lune, Ascendant, Milieu du Ciel (en 4ème), puis les autres
                  const orderedKeys = [
                    'sun', 'soleil',
                    'moon', 'lune',
                    'ascendant',
                    'medium_coeli', 'milieu_du_ciel', 'mc', 'milieu du ciel',
                    // Planètes classiques (ordre traditionnel)
                    'mercury', 'mercure',
                    'venus', 'vénus',
                    'mars',
                    'jupiter',
                    'saturn', 'saturne',
                    // Planètes extérieures
                    'uranus',
                    'neptune',
                    'pluto', 'pluton',
                    // Points astrologiques
                    'mean_node', 'true_node', 'north_node', 'noeud_nord', 'nœud nord',
                    'south_node', 'noeud_sud', 'nœud sud',
                    'lilith', 'black_moon_lilith', 'blackmoonlilith',
                    'chiron',
                  ];
                  
                  // Créer une liste ordonnée
                  const orderedPlanets: Array<[string, any]> = [];
                  const remainingPlanets: Array<[string, any]> = [];
                  const addedNames = new Set<string>();
                  
                  // D'abord, ajouter dans l'ordre spécifique
                  for (const key of orderedKeys) {
                    const entry = Object.entries(chart.planets).find(([name]) => {
                      const nameLower = name.toLowerCase();
                      const keyLower = key.toLowerCase();
                      
                      // Cas spéciaux pour Milieu du Ciel (en 4ème position)
                      if ((keyLower === 'medium_coeli' || keyLower === 'milieu_du_ciel' || keyLower === 'mc' || keyLower === 'milieu du ciel') &&
                          (nameLower === 'medium_coeli' || nameLower === 'milieu_du_ciel' || nameLower === 'mc' || nameLower === 'milieu du ciel' || name === 'Milieu du Ciel')) {
                        return true;
                      }
                      
                      // Pour les nœuds, prioriser mean_node et éviter les doublons
                      if ((keyLower === 'mean_node' || keyLower === 'true_node' || keyLower === 'north_node' || keyLower === 'noeud_nord' || keyLower === 'nœud nord') && 
                          (nameLower === 'mean_node' || nameLower === 'true_node' || nameLower === 'nœud nord' || name === 'Nœud Nord')) {
                        // Si on a déjà ajouté un nœud, skip
                        if (addedNames.has('mean_node') || addedNames.has('true_node') || addedNames.has('nœud nord') || addedNames.has('Nœud Nord')) {
                          return false;
                        }
                        // Prioriser mean_node
                        return nameLower === 'mean_node' || name === 'Nœud Nord';
                      }
                      
                      // Pour Nœud Sud
                      if ((keyLower === 'south_node' || keyLower === 'noeud_sud' || keyLower === 'nœud sud') &&
                          (nameLower === 'south_node' || nameLower === 'noeud_sud' || nameLower === 'nœud sud' || name === 'Nœud Sud')) {
                        return true;
                      }
                      
                      return nameLower === keyLower;
                    });
                    if (entry) {
                      const nameLower = entry[0].toLowerCase();
                      // Éviter les doublons
                      if (!addedNames.has(nameLower)) {
                        orderedPlanets.push(entry);
                        addedNames.add(nameLower);
                      }
                    }
                  }
                  
                  // Ensuite, ajouter les autres (non encore ajoutés)
                  for (const entry of Object.entries(chart.planets)) {
                    const nameLower = entry[0].toLowerCase();
                    // Éviter mean_node/true_node si déjà ajouté
                    if (nameLower === 'true_node' && addedNames.has('mean_node')) {
                      continue;  // Skip true_node si mean_node déjà présent
                    }
                    if (nameLower === 'mean_node' && addedNames.has('true_node')) {
                      continue;  // Skip mean_node si true_node déjà présent (ne devrait pas arriver)
                    }
                    if (!addedNames.has(nameLower)) {
                      remainingPlanets.push(entry);
                      addedNames.add(nameLower);
                    }
                  }
                  
                  // Fusionner
                  const allPlanets = [...orderedPlanets, ...remainingPlanets];
                  
                  return allPlanets.map(([planetName, planetData]: [string, any], index: number) => {
                    // Traduire les noms pour affichage
                    let displayName: string;
                    const nameLower = planetName.toLowerCase();

                    if (nameLower === 'medium_coeli' || nameLower === 'milieu du ciel' || nameLower === 'mc' || nameLower === 'milieu_du_ciel') {
                      displayName = 'Milieu du Ciel';
                    } else if (nameLower === 'ascendant') {
                      displayName = 'Ascendant';  // Capitalisation
                    } else if (nameLower === 'mean_node' || nameLower === 'true_node' || nameLower === 'nœud nord' || nameLower === 'noeud_nord' || nameLower === 'north_node') {
                      displayName = 'Nœud Nord';  // Unifier mean_node et true_node
                    } else if (nameLower === 'south_node' || nameLower === 'noeud_sud' || nameLower === 'nœud sud') {
                      displayName = 'Nœud Sud';  // N majuscule
                    } else {
                      displayName = tPlanet(planetName);
                    }

                    // Convertir le nom de planète en NatalSubject pour rendre cliquable
                    const subject = planetNameToSubject(planetName);

                    return (
                      <TouchableOpacity
                        key={index}
                        style={styles.planetRow}
                        onPress={() => subject && handlePlacementClick(subject)}
                        disabled={!subject}
                        activeOpacity={subject ? 0.7 : 1}
                      >
                        <Text style={styles.planetName}>
                          {displayName}
                        </Text>
                        <Text style={styles.planetInfo}>
                          {planetData.sign ? `${ZODIAC_EMOJI[planetData.sign] || ''} ${tSign(planetData.sign)}` : 'N/A'}
                          {planetData.degree !== undefined && ` • ${formatDegree(planetData.degree)}`}
                          {planetData.house !== undefined && planetData.house > 0 && ` • Maison ${planetData.house}`}
                        </Text>
                      </TouchableOpacity>
                    );
                  });
                })()}
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
                {chart.aspects.slice(0, 10).map((aspect: any, index: number) => {
                  const aspectText = formatAspectFR(aspect);
                  const orb = aspect.orb !== undefined && aspect.orb !== null ? Math.abs(aspect.orb) : null;
                  
                  return (
                    <View key={index} style={styles.aspectRow}>
                      <View style={styles.aspectContent}>
                        <Text style={styles.aspectText}>
                          {aspectText.replace(/ \(orbe [^)]+\)/, '')}  {/* Enlever l'orbe du texte principal */}
                        </Text>
                        {orb !== null && (
                          <Text style={styles.aspectOrb}>
                            Orbe: {orb.toFixed(1).replace('.', ',')}°  {/* Distance à l'aspect exact */}
                            {' '}
                            <Text style={styles.aspectOrbHint}>
                              ({orb <= 1 ? 'exact' : orb <= 3 ? 'serré' : orb <= 6 ? 'moyen' : 'large'})
                            </Text>
                          </Text>
                        )}
                      </View>
                    </View>
                  );
                })}
                <Text style={styles.aspectExplanation}>
                  L'orbe indique la distance en degrés à l'aspect exact. Plus l'orbe est petit, plus l'aspect est puissant.
                </Text>
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

        {/* Modal d'interprétation */}
        {selectedSubject && selectedPayload && (
          <NatalInterpretationModal
            visible={modalVisible}
            onClose={() => setModalVisible(false)}
            subject={selectedSubject}
            chartId={chartId}
            chartPayload={selectedPayload}
          />
        )}
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
    paddingVertical: spacing.sm,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.1)',
  },
  aspectContent: {
    flexDirection: 'column',
  },
  aspectText: {
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  aspectOrb: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    fontSize: 12,
  },
  aspectOrbHint: {
    ...fonts.bodySmall,
    color: colors.accent,
    fontSize: 11,
    fontStyle: 'italic',
  },
  aspectExplanation: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    fontSize: 12,
    marginTop: spacing.md,
    fontStyle: 'italic',
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
  tapHint: {
    ...fonts.caption,
    color: colors.textMuted,
    fontSize: 10,
    marginTop: spacing.xs,
    fontStyle: 'italic',
  },
});

