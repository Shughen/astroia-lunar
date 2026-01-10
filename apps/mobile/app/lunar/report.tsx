/**
 * Écran Rapport Mensuel de Révolution Lunaire (Phase 1.2)
 *
 * Affiche le rapport généré par lunar_report_builder.py v4 :
 * - Header (mois, dates, lune, ascendant)
 * - Climat général (template-based)
 * - Axes dominants (2-3 domaines de vie)
 * - Aspects majeurs (max 5, enrichis v4)
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  ActivityIndicator,
  TouchableOpacity,
} from 'react-native';
import { router, useLocalSearchParams } from 'expo-router';
import apiClient from '../../services/api';
import { AspectDetailSheet } from '../../components/AspectDetailSheet';
import { Skeleton, SkeletonCard } from '../../components/Skeleton';
import { showNetworkErrorAlert, getHumanErrorMessage } from '../../utils/errorHandler';
import type { AspectV4 } from '../../types/api';

interface LunarReportHeader {
  month: string;
  dates: string;
  moon_sign: string;
  moon_house: number;
  lunar_ascendant: string;
}

interface LunarReport {
  header: LunarReportHeader;
  general_climate: string;
  dominant_axes: string[];
  major_aspects: AspectV4[];
}

export default function LunarReportScreen() {
  const params = useLocalSearchParams<{ id?: string }>();
  const [report, setReport] = useState<LunarReport | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedAspect, setSelectedAspect] = useState<AspectV4 | null>(null);

  useEffect(() => {
    loadReport();
  }, [params.id]);

  const loadReport = async () => {
    try {
      setLoading(true);
      setError(null);

      // Si params.id existe, charger le rapport par ID, sinon charger le cycle courant
      const endpoint = params.id
        ? `/api/lunar-returns/${params.id}/report`
        : '/api/lunar-returns/current/report';

      const response = await apiClient.get(endpoint);
      setReport(response.data);
    } catch (err: any) {
      console.error('[LunarReport] Erreur chargement rapport:', err);
      if (err.response?.status === 404) {
        setError(params.id ? 'Cycle lunaire non trouvé' : 'Aucune révolution lunaire en cours');
      } else {
        // Utiliser le helper pour formater le message d'erreur
        const errorMessage = getHumanErrorMessage(err);
        setError(errorMessage);
        // Afficher aussi un Alert avec option Réessayer
        showNetworkErrorAlert(
          err,
          () => loadReport(),
          'Le rapport est temporairement indisponible.'
        );
      }
    } finally {
      setLoading(false);
    }
  };

  const renderHeader = () => {
    if (!report) return null;

    const { month, dates, moon_sign, moon_house, lunar_ascendant } = report.header;

    return (
      <View style={styles.headerCard}>
        <Text style={styles.monthTitle}>{month}</Text>
        <Text style={styles.dates}>{dates}</Text>

        <View style={styles.headerInfoGrid}>
          <View style={styles.headerInfoItem}>
            <Text style={styles.headerLabel}>Lune en</Text>
            <Text style={styles.headerValue}>
              {moon_sign} (Maison {moon_house})
            </Text>
          </View>

          <View style={styles.headerInfoItem}>
            <Text style={styles.headerLabel}>Ascendant lunaire</Text>
            <Text style={styles.headerValue}>{lunar_ascendant}</Text>
          </View>
        </View>
      </View>
    );
  };

  const renderClimate = () => {
    if (!report || !report.general_climate) return null;

    return (
      <View style={styles.card}>
        <Text style={styles.cardTitle}>🌙 Climat général du mois</Text>
        <Text style={styles.climateText}>{report.general_climate}</Text>
      </View>
    );
  };

  const renderAxes = () => {
    if (!report || !report.dominant_axes || report.dominant_axes.length === 0) {
      return null;
    }

    return (
      <View style={styles.card}>
        <Text style={styles.cardTitle}>🎯 Axes dominants du cycle</Text>
        {report.dominant_axes.map((axis, index) => (
          <View key={index} style={styles.axisItem}>
            <Text style={styles.axisBullet}>•</Text>
            <Text style={styles.axisText}>{axis}</Text>
          </View>
        ))}
      </View>
    );
  };

  const renderAspects = () => {
    if (!report || !report.major_aspects || report.major_aspects.length === 0) {
      return null;
    }

    return (
      <View style={styles.card}>
        <Text style={styles.cardTitle}>⭐ Aspects majeurs du cycle</Text>
        <Text style={styles.aspectsSubtitle}>
          {report.major_aspects.length} aspect{report.major_aspects.length > 1 ? 's' : ''} identifié{report.major_aspects.length > 1 ? 's' : ''}
        </Text>

        {report.major_aspects.map((aspect, index) => (
          <TouchableOpacity
            key={aspect.id || index}
            style={styles.aspectRow}
            onPress={() => setSelectedAspect(aspect)}
          >
            <View style={styles.aspectHeader}>
              <Text style={styles.aspectPlanets}>
                {aspect.planet1} {getAspectSymbol(aspect.type)} {aspect.planet2}
              </Text>
              <Text style={styles.aspectOrb}>
                {Math.abs(aspect.orb).toFixed(1)}°
              </Text>
            </View>

            {aspect.copy?.summary && (
              <Text style={styles.aspectSummary} numberOfLines={2}>
                {aspect.copy.summary}
              </Text>
            )}

            <Text style={styles.aspectCTA}>Voir détails →</Text>
          </TouchableOpacity>
        ))}
      </View>
    );
  };

  // CTA timeline masqué pour MVP (route non implémentée Phase 1.3)
  // const renderCTA = () => {
  //   return (
  //     <View style={styles.ctaSection}>
  //       <TouchableOpacity
  //         style={styles.ctaButton}
  //         onPress={() => router.push('/lunar/timeline')}
  //       >
  //         <Text style={styles.ctaButtonText}>📅 Voir la timeline du cycle</Text>
  //       </TouchableOpacity>
  //     </View>
  //   );
  // };

  const getAspectSymbol = (type: string): string => {
    const symbols: { [key: string]: string } = {
      conjunction: '☌',
      opposition: '☍',
      square: '□',
      trine: '△',
    };
    return symbols[type.toLowerCase()] || type;
  };

  if (loading) {
    return (
      <ScrollView style={styles.container}>
        <View style={styles.header}>
          <TouchableOpacity
            style={styles.backButtonSmall}
            onPress={() => router.back()}
          >
            <Text style={styles.backButtonText}>← Retour</Text>
          </TouchableOpacity>

          <Text style={styles.title}>Rapport Mensuel</Text>
          <Text style={styles.subtitle}>Révolution Lunaire</Text>
        </View>

        <View style={{ margin: 16 }}>
          <SkeletonCard style={{ marginBottom: 16 }} />
          <SkeletonCard style={{ marginBottom: 16 }} />
          <SkeletonCard style={{ marginBottom: 16 }} />
        </View>
      </ScrollView>
    );
  }

  if (error || !report) {
    return (
      <View style={styles.errorContainer}>
        <Text style={styles.errorText}>
          {error || 'Rapport non disponible'}
        </Text>
        <View style={styles.errorActions}>
          <TouchableOpacity
            style={[styles.errorButton, styles.retryButton]}
            onPress={() => loadReport()}
          >
            <Text style={styles.errorButtonText}>Réessayer</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.errorButton, styles.backButton]}
            onPress={() => router.back()}
          >
            <Text style={styles.errorButtonText}>← Retour</Text>
          </TouchableOpacity>
        </View>
      </View>
    );
  }

  return (
    <>
      <ScrollView style={styles.container}>
        <View style={styles.header}>
          <TouchableOpacity
            style={styles.backButtonSmall}
            onPress={() => router.back()}
          >
            <Text style={styles.backButtonText}>← Retour</Text>
          </TouchableOpacity>

          <Text style={styles.title}>Rapport Mensuel</Text>
          <Text style={styles.subtitle}>Révolution Lunaire</Text>
        </View>

        {renderHeader()}
        {renderClimate()}
        {renderAxes()}
        {renderAspects()}
        {/* CTA timeline masqué pour MVP */}

        <View style={styles.footer}>
          <Text style={styles.footerText}>
            Rapport généré par templates v4 (architecture déterministe)
          </Text>
        </View>
      </ScrollView>

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
    backgroundColor: '#0A0E27',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0A0E27',
  },
  loadingText: {
    marginTop: 16,
    fontSize: 16,
    color: '#8B7BF7',
  },
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#0A0E27',
    padding: 20,
  },
  errorText: {
    fontSize: 18,
    color: '#FF6B6B',
    marginBottom: 24,
    textAlign: 'center',
  },
  errorActions: {
    flexDirection: 'row',
    gap: 12,
    width: '100%',
    maxWidth: 300,
  },
  errorButton: {
    flex: 1,
    padding: 16,
    borderRadius: 8,
    alignItems: 'center',
  },
  retryButton: {
    backgroundColor: '#8B7BF7',
  },
  header: {
    padding: 20,
    paddingTop: 60,
    backgroundColor: '#1A1F3E',
    borderBottomWidth: 2,
    borderBottomColor: '#8B7BF7',
    position: 'relative',
  },
  backButtonSmall: {
    position: 'absolute',
    top: 60,
    left: 20,
    zIndex: 10,
  },
  backButton: {
    backgroundColor: '#2D3561',
  },
  errorButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  backButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#FFFFFF',
    textAlign: 'center',
    marginBottom: 4,
    marginTop: 24,
  },
  subtitle: {
    fontSize: 16,
    color: '#A0A0B0',
    textAlign: 'center',
  },
  headerCard: {
    margin: 16,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 2,
    borderColor: '#8B7BF7',
  },
  monthTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#8B7BF7',
    textAlign: 'center',
    marginBottom: 8,
  },
  dates: {
    fontSize: 16,
    color: '#A0A0B0',
    textAlign: 'center',
    marginBottom: 20,
  },
  headerInfoGrid: {
    gap: 16,
  },
  headerInfoItem: {
    backgroundColor: '#0A0E27',
    padding: 12,
    borderRadius: 8,
  },
  headerLabel: {
    fontSize: 12,
    color: '#A0A0B0',
    marginBottom: 4,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  headerValue: {
    fontSize: 16,
    color: '#FFFFFF',
    fontWeight: '600',
  },
  card: {
    margin: 16,
    marginTop: 0,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#8B7BF7',
    marginBottom: 16,
  },
  climateText: {
    fontSize: 15,
    color: '#C0C0D0',
    lineHeight: 24,
  },
  axisItem: {
    flexDirection: 'row',
    marginBottom: 12,
    alignItems: 'flex-start',
  },
  axisBullet: {
    fontSize: 18,
    color: '#8B7BF7',
    marginRight: 8,
    marginTop: 2,
  },
  axisText: {
    fontSize: 15,
    color: '#C0C0D0',
    lineHeight: 22,
    flex: 1,
  },
  aspectsSubtitle: {
    fontSize: 14,
    color: '#A0A0B0',
    marginBottom: 16,
  },
  aspectRow: {
    marginBottom: 16,
    padding: 16,
    backgroundColor: '#0A0E27',
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  aspectHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  aspectPlanets: {
    fontSize: 16,
    color: '#FFFFFF',
    fontWeight: '600',
  },
  aspectOrb: {
    fontSize: 14,
    color: '#8B7BF7',
    fontWeight: '600',
  },
  aspectSummary: {
    fontSize: 14,
    color: '#A0A0B0',
    lineHeight: 20,
    marginBottom: 8,
  },
  aspectCTA: {
    fontSize: 14,
    color: '#8B7BF7',
    fontWeight: '600',
  },
  ctaSection: {
    margin: 16,
    marginTop: 0,
  },
  ctaButton: {
    backgroundColor: '#8B7BF7',
    padding: 18,
    borderRadius: 12,
    alignItems: 'center',
  },
  ctaButtonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '600',
  },
  footer: {
    padding: 20,
    alignItems: 'center',
    marginTop: 20,
    borderTopWidth: 1,
    borderTopColor: '#2D3561',
  },
  footerText: {
    fontSize: 12,
    color: '#A0A0B0',
    textAlign: 'center',
  },
});
