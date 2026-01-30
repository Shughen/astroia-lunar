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
  TouchableOpacity,
} from 'react-native';
import { router, useLocalSearchParams } from 'expo-router';
import apiClient from '../../services/api';
import { AspectDetailSheet } from '../../components/AspectDetailSheet';
import { Skeleton, SkeletonCard } from '../../components/Skeleton';
import { AnimatedCard } from '../../components/AnimatedCard';
import { MarkdownText } from '../../components/MarkdownText';
import LunarInterpretationLoader from '../../components/LunarInterpretationLoader';
import { showNetworkErrorAlert, getHumanErrorMessage } from '../../utils/errorHandler';
import { translateZodiacSign, translateAstrologyText } from '../../utils/astrologyTranslations';
import { tPlanet, tAspect } from '../../i18n/astro.format';
import type { AspectV4 } from '../../types/api';
import { haptics } from '../../services/haptics';

interface LunarReportHeader {
  month: string;
  dates: string;
  moon_sign: string;
  moon_house: number;
  lunar_ascendant: string;
}

interface LunarInterpretation {
  climate: string | null;
  focus: string | null;
  approach: string | null;
  full: string | null;
}

interface LunarReportMetadata {
  source: 'db_temporal' | 'claude' | 'db_template' | 'hardcoded' | 'unknown';
  model_used: string | null;
  version: number;
  generated_at: string;
}

interface LunarReport {
  lunar_return_id: number;  // 🆕 ID pour régénération
  header: LunarReportHeader;
  general_climate: string;
  dominant_axes: string[];
  major_aspects: AspectV4[];
  lunar_interpretation?: LunarInterpretation;
  interpretation_source?: string;
  metadata?: LunarReportMetadata;
}

/**
 * Traduit les sources V2 en labels lisibles
 */
const getSourceLabel = (source: string): string => {
  const labels: Record<string, string> = {
    'db_temporal': 'Cache DB',
    'claude': 'IA Claude',
    'db_template': 'Templates DB',
    'hardcoded': 'Fallback',
    'unknown': 'Inconnu'
  };
  return labels[source] || source;
};

export default function LunarReportScreen() {
  const params = useLocalSearchParams<{ id?: string }>();
  const [report, setReport] = useState<LunarReport | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [needsGeneration, setNeedsGeneration] = useState(false);
  const [generating, setGenerating] = useState(false);
  const [selectedAspect, setSelectedAspect] = useState<AspectV4 | null>(null);
  const [regenerating, setRegenerating] = useState(false);
  const [needsNatalChart, setNeedsNatalChart] = useState(false);

  useEffect(() => {
    loadReport();
  }, [params.id]);

  const loadReport = async () => {
    try {
      setLoading(true);
      setError(null);
      setNeedsGeneration(false);
      setNeedsNatalChart(false);

      // Si params.id existe, charger le rapport par ID, sinon charger le cycle courant
      const endpoint = params.id
        ? `/api/lunar-returns/${params.id}/report`
        : '/api/lunar-returns/current/report';

      const response = await apiClient.get(endpoint);
      setReport(response.data);
    } catch (err: any) {
      console.error('[LunarReport] Erreur chargement rapport:', err);
      if (err.response?.status === 404) {
        const backendMessage = err.response?.data?.detail;
        if (typeof backendMessage === 'string') {
          // Détecter le cas spécifique : cycles non générés (message contient "generate")
          if (backendMessage.toLowerCase().includes('generate')) {
            setError('Tes cycles lunaires n\'ont pas encore été générés');
            setNeedsGeneration(true);
          } else {
            setError(params.id ? 'Cycle lunaire non trouvé' : 'Aucune révolution lunaire en cours');
            setNeedsGeneration(false);
          }
        } else {
          setError(params.id ? 'Cycle lunaire non trouvé' : 'Aucune révolution lunaire en cours');
          setNeedsGeneration(false);
        }
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

  // Génère les cycles lunaires si non existants
  const generateLunarCycles = async () => {
    try {
      setGenerating(true);
      setNeedsNatalChart(false);
      haptics.light();

      console.log('[LunarReport] 🔄 Génération des cycles lunaires...');
      await apiClient.post('/api/lunar-returns/generate');

      console.log('[LunarReport] ✅ Cycles générés, rechargement du rapport...');
      haptics.success();

      // Recharger le rapport
      await loadReport();
    } catch (err: any) {
      console.error('[LunarReport] ❌ Erreur génération cycles:', err);
      haptics.error();

      // Détecter si le thème natal est requis (404 ou 409 avec message natal)
      const status = err.response?.status;
      const backendDetail = err.response?.data?.detail;
      const detailStr = typeof backendDetail === 'string'
        ? backendDetail
        : backendDetail?.detail || '';

      const isNatalRequired =
        (status === 404 && detailStr.toLowerCase().includes('natal')) ||
        (status === 409 && (
          backendDetail?.error_code === 'NATAL_REQUIRED' ||
          detailStr.toLowerCase().includes('natal')
        ));

      if (isNatalRequired) {
        setError('Tu dois d\'abord créer ton thème natal pour générer tes cycles lunaires.');
        setNeedsNatalChart(true);
      } else {
        const errorMessage = getHumanErrorMessage(err);
        setError(`Impossible de générer les cycles: ${errorMessage}`);
      }
    } finally {
      setGenerating(false);
    }
  };

  // 🆕 Force la régénération de l'interprétation avec Claude Opus 4.5
  const regenerateInterpretation = async () => {
    if (!report?.lunar_return_id) {
      console.error('[LunarReport] Impossible de régénérer : lunar_return_id manquant');
      return;
    }

    try {
      setRegenerating(true);
      haptics.light();

      console.log(`[LunarReport] 🔄 Régénération pour lunar_return_id=${report.lunar_return_id}...`);

      const response = await apiClient.post('/api/lunar/interpretation/regenerate', {
        lunar_return_id: report.lunar_return_id,
        subject: 'full'
      });

      console.log('[LunarReport] ✅ Régénération réussie:', {
        source: response.data.metadata?.source,
        model: response.data.metadata?.model_used,
      });

      haptics.success();

      // Recharger le rapport complet pour voir la nouvelle interprétation
      await loadReport();
    } catch (err: any) {
      console.error('[LunarReport] ❌ Erreur régénération:', err);
      haptics.error();

      const errorMessage = getHumanErrorMessage(err);
      showNetworkErrorAlert(
        err,
        () => regenerateInterpretation(),
        `Impossible de régénérer l'interprétation. ${errorMessage}`
      );
    } finally {
      setRegenerating(false);
    }
  };

  const renderHeader = () => {
    if (!report) return null;

    const { month, dates, moon_sign, moon_house, lunar_ascendant } = report.header;

    // Traduire le mois et les signes
    const translatedMonth = translateAstrologyText(month);
    const translatedMoonSign = translateZodiacSign(moon_sign);
    const translatedAscendant = translateZodiacSign(lunar_ascendant);

    return (
      <AnimatedCard style={styles.headerCard} delay={0} duration={500}>
        <Text style={styles.monthTitle}>{translatedMonth}</Text>
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

  const renderClimate = () => {
    if (!report) return null;

    // Priorité : lunar_interpretation.full (DB) > general_climate (templates)
    const climateText = report.lunar_interpretation?.full || report.general_climate;

    if (!climateText) return null;

    // Traduire tous les signes et mois dans le texte
    const translatedClimate = translateAstrologyText(climateText);

    return (
      <AnimatedCard style={styles.card} delay={100} duration={500}>
        <Text style={styles.cardTitle}>🌙 Climat général du mois</Text>
        <MarkdownText style={styles.climateText}>{translatedClimate}</MarkdownText>
      </AnimatedCard>
    );
  };

  const renderAxes = () => {
    // Ne pas afficher les axes statiques si on a une interprétation IA complète
    // L'interprétation full couvre déjà les domaines de vie activés
    if (report?.lunar_interpretation?.full) {
      return null;
    }

    if (!report || !report.dominant_axes || report.dominant_axes.length === 0) {
      return null;
    }

    return (
      <AnimatedCard style={styles.card} delay={200} duration={500}>
        <Text style={styles.cardTitle}>🎯 Axes dominants du cycle</Text>
        {report.dominant_axes.map((axis, index) => {
          // Traduire les signes dans chaque axe
          const translatedAxis = translateAstrologyText(axis);
          return (
            <View key={index} style={styles.axisItem}>
              <Text style={styles.axisBullet}>•</Text>
              <MarkdownText style={styles.axisText}>{translatedAxis}</MarkdownText>
            </View>
          );
        })}
      </AnimatedCard>
    );
  };

  const renderAspects = () => {
    if (!report || !report.major_aspects || report.major_aspects.length === 0) {
      return null;
    }

    return (
      <AnimatedCard style={styles.card} delay={300} duration={500}>
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

  if (loading || regenerating || generating) {
    return (
      <LunarInterpretationLoader
        message={
          generating
            ? "Génération de tes cycles lunaires..."
            : regenerating
            ? "Régénération en cours..."
            : "Génération de ton interprétation lunaire..."
        }
      />
    );
  }

  if (error || !report) {
    return (
      <View style={styles.errorContainer}>
        <Text style={styles.errorText}>
          {error || 'Rapport non disponible'}
        </Text>

        {/* CTA pour créer le thème natal si requis */}
        {needsNatalChart && (
          <TouchableOpacity
            style={[styles.errorButton, styles.primaryButton]}
            onPress={() => router.push('/natal-chart')}
          >
            <Text style={styles.errorButtonText}>
              Créer mon thème natal
            </Text>
          </TouchableOpacity>
        )}

        {/* CTA pour générer les cycles lunaires si requis (et natal chart existe) */}
        {needsGeneration && !needsNatalChart && (
          <TouchableOpacity
            style={[styles.errorButton, styles.primaryButton]}
            onPress={generateLunarCycles}
            disabled={generating}
          >
            <Text style={styles.errorButtonText}>
              {generating ? 'Génération en cours...' : 'Générer mes cycles lunaires'}
            </Text>
          </TouchableOpacity>
        )}

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
            hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
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
            {__DEV__ && report?.metadata
              ? `📊 V${report.metadata.version} • Source: ${getSourceLabel(report.metadata.source)}${report.metadata.model_used ? ` • ${report.metadata.model_used}` : ''}`
              : '✨ Généré spécialement pour toi'}
          </Text>

          {/* 🧪 Bouton régénération (DEV only) */}
          {__DEV__ && report && (
            <TouchableOpacity
              style={styles.regenerateButton}
              onPress={regenerateInterpretation}
              disabled={regenerating}
            >
              <Text style={styles.regenerateButtonText}>
                {regenerating ? '⏳ Régénération...' : '🔄 Régénérer l\'interprétation'}
              </Text>
            </TouchableOpacity>
          )}
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
  primaryButton: {
    flex: 0,
    backgroundColor: '#8B7BF7',
    width: '100%',
    maxWidth: 300,
    marginBottom: 16,
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
    padding: 8,
    marginLeft: -8,
    marginTop: -8,
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
  aspectPlanetsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    flex: 1,
  },
  aspectPlanets: {
    fontSize: 16,
    color: '#FFFFFF',
    fontWeight: '600',
  },
  shadowBadge: {
    fontSize: 16,
    marginLeft: 4,
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
  regenerateButton: {
    marginTop: 16,
    backgroundColor: '#8B7BF7',
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 8,
    minWidth: 250,
    alignItems: 'center',
  },
  regenerateButtonText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '600',
  },
});
