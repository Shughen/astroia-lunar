import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
} from 'react-native';
import { useRouter } from 'expo-router';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { transits, lunarReturns } from '../../services/api';
import { useAuthStore } from '../../stores/useAuthStore';
import { isDevAuthBypassActive, getDevAuthHeader } from '../../services/api';
import { tPlanet, tAspect, formatOrb } from '../../i18n/astro.format';
import { translateZodiacSign } from '../../utils/astrologyTranslations';

// Aspects majeurs MVP : conjonction, opposition, carré, trigone uniquement
const ASPECT_BADGES: Record<string, { emoji: string; color: string }> = {
  trine: { emoji: '▲', color: '#4ade80' },
  conjunction: { emoji: '◎', color: '#fbbf24' },
  square: { emoji: '■', color: '#f87171' },
  opposition: { emoji: '◉', color: '#a78bfa' },
};

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
const formatDateRange = (startDate: string, endDate: string): string => {
  const start = new Date(startDate);
  const end = new Date(endDate);

  return `${start.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' })} - ${end.toLocaleDateString('fr-FR', { day: 'numeric', month: 'short' })}`;
};

export default function TransitsOverview() {
  const router = useRouter();
  const { user, isAuthenticated } = useAuthStore();
  const [loading, setLoading] = useState(true);
  const [transitsData, setTransitsData] = useState<any>(null);
  const [currentLunarReturn, setCurrentLunarReturn] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Guard: vérifier que l'utilisateur est disponible avant de charger
    if (isAuthenticated && user?.id) {
      loadTransits();
    } else if (isDevAuthBypassActive()) {
      // En mode DEV_AUTH_BYPASS, utiliser le user_id depuis l'env
      loadTransits();
    } else {
      setError('Vous devez être connecté pour voir les transits');
      setLoading(false);
    }
  }, [user, isAuthenticated]);

  const loadTransits = async () => {
    try {
      setLoading(true);
      setError(null);

      // Récupérer userId depuis le store ou DEV_AUTH_BYPASS
      // user_id est maintenant un UUID string (pas un entier)
      let userId: string;
      if (isDevAuthBypassActive()) {
        const devHeader = getDevAuthHeader();
        // En DEV_AUTH_BYPASS, utiliser la valeur du header (peut être ID ou UUID)
        userId = devHeader.value || 'dev-user-id';
      } else if (user?.id) {
        // Convertir en string si nécessaire (peut être number ou string selon le store)
        userId = typeof user.id === 'string' ? user.id : String(user.id);
      } else {
        throw new Error('Utilisateur non authentifié');
      }

      // Construire le mois au format YYYY-MM
      const now = new Date();
      if (isNaN(now.getTime())) {
        throw new Error('Date invalide');
      }
      const month = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`;

      // Le token est géré automatiquement par l'intercepteur axios
      const response = await transits.getOverview(userId, month);

      // Si response est null, c'est un 404 (pas de données) - cas normal, pas une erreur
      if (response === null) {
        setTransitsData(null);
        setError(null); // Pas d'erreur, juste pas de données
      } else {
        // Guard: vérifier que la réponse contient des données valides
        if (!response) {
          throw new Error('Réponse invalide du serveur');
        }
        setTransitsData(response);
      }

      // Charger la révolution lunaire en cours pour afficher le lien
      try {
        const lunarReturnResponse = await lunarReturns.getCurrent();
        if (lunarReturnResponse) {
          setCurrentLunarReturn(lunarReturnResponse);
        }
      } catch (lunarErr) {
        // Ignorer l'erreur si la révolution lunaire n'est pas disponible
        console.warn('[TransitsOverview] Révolution lunaire non disponible:', lunarErr);
      }
    } catch (err: any) {
      console.error('[TransitsOverview] Erreur chargement:', err);
      // Ne pas afficher d'erreur si c'est un 404 (déjà géré ci-dessus)
      if (err.response?.status === 404) {
        setTransitsData(null);
        setError(null);
        return;
      }
      const errorMessage = err.response?.data?.detail || err.message || 'Erreur lors du chargement des transits';
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <LinearGradient colors={['#1a0b2e', '#2d1b4e']} style={styles.container}>
        <SafeAreaView style={styles.safeArea} edges={['top']}>
          <ActivityIndicator size="large" color="#b794f6" />
          <Text style={styles.loadingText}>Chargement des transits...</Text>
        </SafeAreaView>
      </LinearGradient>
    );
  }

  if (error) {
    return (
      <LinearGradient colors={['#1a0b2e', '#2d1b4e']} style={styles.container}>
        <SafeAreaView style={styles.safeArea} edges={['top']}>
          <View style={styles.errorContainer}>
            <Text style={styles.errorEmoji}>⚠️</Text>
            <Text style={styles.errorText}>{error}</Text>
            <TouchableOpacity style={styles.retryButton} onPress={loadTransits}>
              <Text style={styles.retryText}>Réessayer</Text>
            </TouchableOpacity>
          </View>
        </SafeAreaView>
      </LinearGradient>
    );
  }

  // Guards: vérifier que transitsData existe et a la structure attendue
  // Si transitsData est null, c'est un cas normal (pas de données) - afficher un état vide
  if (!transitsData) {
    return (
      <LinearGradient colors={['#1a0b2e', '#2d1b4e']} style={styles.container}>
        <SafeAreaView style={styles.safeArea} edges={['top']}>
          <ScrollView contentContainerStyle={styles.scrollContent}>
            <View style={styles.header}>
              <Text style={styles.title}>🔄 Transits du Mois</Text>
              <Text style={styles.subtitle}>
                Influences planétaires actuelles
              </Text>
            </View>
            <View style={styles.emptyState}>
              <Text style={styles.emptyEmoji}>🌌</Text>
              <Text style={styles.emptyText}>
                Aucun transit disponible pour ce mois
              </Text>
              <Text style={styles.emptySubtext}>
                {isDevAuthBypassActive()
                  ? "Les transits seront calculés automatiquement lors de votre prochaine visite"
                  : "Les transits seront disponibles une fois votre thème natal calculé"}
              </Text>
            </View>
          </ScrollView>
        </SafeAreaView>
      </LinearGradient>
    );
  }

  // Utiliser 'overview' (nouveau nom) avec fallback sur 'summary' pour compatibilité
  const overviewData = transitsData?.overview || transitsData?.summary;
  const insights = overviewData?.insights || {};
  const allAspects = insights?.major_aspects || [];

  // Dériver les infos du mois lunaire pour le header
  const lunarMonthName = currentLunarReturn?.start_date
    ? formatMonthName(currentLunarReturn.start_date)
    : 'Mois en cours';

  const lunarDateRange = currentLunarReturn?.start_date && currentLunarReturn?.end_date
    ? formatDateRange(currentLunarReturn.start_date, currentLunarReturn.end_date)
    : null;

  const moonSign = currentLunarReturn?.moon_sign
    ? translateZodiacSign(currentLunarReturn.moon_sign)
    : null;

  const lunarHouse = currentLunarReturn?.lunar_ascendant_house || null;

  // Filtrer pour ne garder que les 4 aspects majeurs MVP
  const MAJOR_ASPECTS_MVP = ['conjunction', 'opposition', 'square', 'trine'];

  // Planètes réelles uniquement (exclure nœuds, Chiron, etc.)
  const PLANETARY_BODIES = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'];
  const EXCLUDED_KEYWORDS = ['node', 'Node', 'chiron', 'Chiron', 'lilith', 'Lilith', 'Fortune', 'Vertex'];

  const majorAspects = allAspects.filter((aspect: any) => {
    // Filtrer les aspects majeurs
    if (!MAJOR_ASPECTS_MVP.includes(aspect.aspect)) {
      return false;
    }

    // Filtrer les points non-planétaires
    const transitPlanet = aspect.transit_planet || '';
    const natalPlanet = aspect.natal_planet || '';

    // Exclure si contient un mot-clé interdit
    const hasExcludedKeyword = EXCLUDED_KEYWORDS.some(keyword =>
      transitPlanet.includes(keyword) || natalPlanet.includes(keyword)
    );

    if (hasExcludedKeyword) {
      return false;
    }

    // Garder si au moins une des planètes est dans la liste blanche
    const transitIsValid = PLANETARY_BODIES.some(planet => transitPlanet.includes(planet));
    const natalIsValid = PLANETARY_BODIES.some(planet => natalPlanet.includes(planet));

    return transitIsValid && natalIsValid;
  });

  return (
    <LinearGradient colors={['#1a0b2e', '#2d1b4e']} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top']}>
        <ScrollView contentContainerStyle={styles.scrollContent}>
          {/* Header with Lunar Context */}
          <View style={styles.header}>
            <Text style={styles.title}>
              🔄 Transits de {lunarMonthName}
            </Text>
            {lunarDateRange && (
              <Text style={styles.subtitle}>
                {lunarDateRange}
              </Text>
            )}
            {moonSign && (
              <View style={styles.lunarBadgeContainer}>
                <View style={styles.lunarBadge}>
                  <Text style={styles.lunarBadgeText}>
                    🌙 Lune en {moonSign}
                  </Text>
                </View>
                {lunarHouse && (
                  <View style={styles.lunarBadge}>
                    <Text style={styles.lunarBadgeText}>
                      Maison {lunarHouse}
                    </Text>
                  </View>
                )}
              </View>
            )}
          </View>

          {/* Lien vers Révolution Lunaire (optionnel) */}
          {currentLunarReturn && (
            <TouchableOpacity
              style={styles.lunarReturnCard}
              onPress={() => {
                const monthStr = currentLunarReturn.month || currentLunarReturn.start_date?.substring(0, 7);
                if (monthStr) {
                  router.push(`/lunar-month/${monthStr}`);
                }
              }}
            >
              <View style={styles.lunarReturnHeader}>
                <Text style={styles.lunarReturnIcon}>📖</Text>
                <View style={styles.lunarReturnInfo}>
                  <Text style={styles.lunarReturnTitle}>
                    Voir le rapport lunaire complet
                  </Text>
                  <Text style={styles.lunarReturnSubtitle}>
                    Thèmes, défis et opportunités du mois
                  </Text>
                </View>
                <Text style={styles.lunarReturnArrow}>→</Text>
              </View>
            </TouchableOpacity>
          )}

        {/* Energy Level Badge */}
        <View style={styles.energyContainer}>
          <Text style={styles.energyLabel}>Niveau d'énergie :</Text>
          <View
            style={[
              styles.energyBadge,
              {
                backgroundColor:
                  insights.energy_level === 'high'
                    ? '#4ade80'
                    : insights.energy_level === 'low'
                    ? '#f87171'
                    : '#fbbf24',
              },
            ]}
          >
            <Text style={styles.energyText}>
              {insights.energy_level === 'high'
                ? '⚡ Élevé'
                : insights.energy_level === 'low'
                ? '🌙 Calme'
                : '✨ Modéré'}
            </Text>
          </View>
        </View>

        {/* Insights */}
        {insights.insights && insights.insights.length > 0 && (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>💡 Points Clés</Text>
            {insights.insights.slice(0, 5).map((insight: string, index: number) => (
              <View key={index} style={styles.insightCard}>
                <Text style={styles.bullet}>🌙</Text>
                <Text style={styles.insightText}>{insight}</Text>
              </View>
            ))}
          </View>
        )}

        {/* Major Aspects */}
        {majorAspects.length > 0 && (
          <View style={styles.section}>
            <View style={styles.sectionHeader}>
              <Text style={styles.sectionTitle}>⭐ Aspects Majeurs</Text>
              <TouchableOpacity
                onPress={() =>
                  Alert.alert(
                    'ℹ️ Orbe',
                    "L'orbe représente l'écart en degrés entre les planètes. Plus c'est proche de 0°, plus l'aspect est fort et influent.",
                    [{ text: 'OK' }]
                  )
                }
              >
                <Text style={styles.infoIcon}>ℹ️</Text>
              </TouchableOpacity>
            </View>
            <Text style={styles.sectionSubtitle}>
              Orbe = écart en degrés. Plus c'est proche de 0°, plus l'aspect est fort.
            </Text>
            {majorAspects.map((aspect: any, index: number) => {
              const aspectInfo = ASPECT_BADGES[aspect.aspect] || {
                emoji: '●',
                color: '#b794f6',
              };

              return (
                <TouchableOpacity
                  key={index}
                  style={styles.aspectCard}
                  onPress={() =>
                    router.push({
                      pathname: '/transits/details',
                      params: {
                        transit_planet: aspect.transit_planet,
                        natal_planet: aspect.natal_planet,
                        aspect: aspect.aspect,
                        orb: aspect.orb.toString(),
                        interpretation: aspect.interpretation || '',
                        // TODO: Ajouter timing, themes, recommendations depuis l'API
                      },
                    })
                  }
                >
                  <View style={styles.aspectHeader}>
                    <Text
                      style={[
                        styles.aspectBadge,
                        { color: aspectInfo.color },
                      ]}
                    >
                      {aspectInfo.emoji}
                    </Text>
                    <Text style={styles.aspectTitle}>
                      {tPlanet(aspect.transit_planet)} {tAspect(aspect.aspect)} {tPlanet(aspect.natal_planet)}
                    </Text>
                  </View>
                  <Text style={styles.aspectOrb}>Orbe: {formatOrb(aspect.orb)}</Text>
                  {aspect.interpretation && (
                    <Text style={styles.aspectInterpretation}>
                      {aspect.interpretation}
                    </Text>
                  )}
                </TouchableOpacity>
              );
            })}
          </View>
        )}

        {/* Empty State */}
        {!insights.insights?.length && !majorAspects.length && (
          <View style={styles.emptyState}>
            <Text style={styles.emptyEmoji}>🌌</Text>
            <Text style={styles.emptyText}>
              Aucun transit significatif ce mois-ci
            </Text>
          </View>
        )}
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
  header: {
    marginBottom: 24,
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#ffd700',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: '#b794f6',
  },
  energyContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 24,
  },
  energyLabel: {
    fontSize: 16,
    color: '#ffffff',
    marginRight: 12,
  },
  energyBadge: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 20,
  },
  energyText: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#000000',
  },
  section: {
    marginBottom: 24,
  },
  sectionHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#b794f6',
    flex: 1,
  },
  infoIcon: {
    fontSize: 18,
    color: '#b794f6',
    marginLeft: 8,
  },
  sectionSubtitle: {
    fontSize: 12,
    color: '#a0a0b0',
    fontStyle: 'italic',
    marginBottom: 12,
  },
  insightCard: {
    flexDirection: 'row',
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    padding: 12,
    borderRadius: 8,
    marginBottom: 8,
    borderLeftWidth: 3,
    borderLeftColor: '#b794f6',
  },
  bullet: {
    fontSize: 16,
    marginRight: 8,
  },
  insightText: {
    flex: 1,
    fontSize: 14,
    color: '#ffffff',
    lineHeight: 20,
  },
  aspectCard: {
    backgroundColor: 'rgba(42, 26, 78, 0.8)',
    padding: 16,
    borderRadius: 12,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.3)',
  },
  aspectHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  aspectBadge: {
    fontSize: 20,
    marginRight: 8,
    fontWeight: 'bold',
  },
  aspectTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#ffffff',
    flex: 1,
  },
  aspectOrb: {
    fontSize: 12,
    color: '#a0a0b0',
    marginBottom: 4,
  },
  aspectInterpretation: {
    fontSize: 14,
    color: '#b794f6',
    fontStyle: 'italic',
  },
  emptyState: {
    alignItems: 'center',
    marginTop: 60,
  },
  emptyEmoji: {
    fontSize: 60,
    marginBottom: 16,
  },
  emptyText: {
    fontSize: 16,
    color: '#a0a0b0',
    textAlign: 'center',
    marginBottom: 8,
  },
  emptySubtext: {
    fontSize: 14,
    color: '#808080',
    textAlign: 'center',
    fontStyle: 'italic',
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
    marginBottom: 24,
  },
  retryButton: {
    backgroundColor: '#b794f6',
    paddingHorizontal: 24,
    paddingVertical: 12,
    borderRadius: 8,
  },
  retryText: {
    color: '#000000',
    fontWeight: 'bold',
    fontSize: 16,
  },
  lunarReturnCard: {
    backgroundColor: 'rgba(183, 148, 246, 0.15)',
    borderRadius: 12,
    padding: 16,
    marginBottom: 20,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.3)',
  },
  lunarReturnHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  lunarReturnIcon: {
    fontSize: 28,
    marginRight: 12,
  },
  lunarReturnInfo: {
    flex: 1,
  },
  lunarReturnTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#ffffff',
    marginBottom: 4,
  },
  lunarReturnSubtitle: {
    fontSize: 13,
    color: '#b794f6',
  },
  lunarReturnArrow: {
    fontSize: 20,
    color: '#b794f6',
    fontWeight: 'bold',
  },
  lunarReturnDescription: {
    fontSize: 13,
    color: '#a0a0b0',
    fontStyle: 'italic',
    lineHeight: 18,
  },
  lunarBadgeContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 12,
    flexWrap: 'wrap',
    gap: 8,
  },
  lunarBadge: {
    backgroundColor: 'rgba(183, 148, 246, 0.2)',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.3)',
  },
  lunarBadgeText: {
    fontSize: 13,
    color: '#b794f6',
    fontWeight: '600',
  },
});

