/**
 * Écran de détail du Lunar Return Report
 * Affichage formaté et lisible du rapport mensuel de révolution lunaire
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
import { useLocalSearchParams, router } from 'expo-router';

interface LunarReturnReport {
  provider: string;
  kind: string;
  data: {
    moon?: {
      sign?: string;
      house?: number;
      degree?: number;
    };
    ascendant?: string;
    interpretation?: string;
    aspects?: any[];
    planets?: any[];
    houses?: any[];
    [key: string]: any;
  };
  cached?: boolean;
}

export default function LunarReportDetailScreen() {
  const params = useLocalSearchParams();
  const [report, setReport] = useState<LunarReturnReport | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // En production, on chargerait les données depuis l'API ou le cache
    // Pour l'instant, simulation avec données de test
    const mockReport: LunarReturnReport = {
      provider: 'rapidapi',
      kind: 'lunar_return_report',
      data: {
        moon: {
          sign: 'Taurus',
          house: 2,
          degree: 15.5,
        },
        ascendant: 'Leo',
        interpretation:
          'Ce mois lunaire met l\'accent sur la stabilité financière et les valeurs personnelles. ' +
          'La Lune en Taureau dans la maison 2 suggère une période favorable pour consolider vos ressources ' +
          'et développer une approche pragmatique de vos finances. L\'ascendant Léon apporte confiance ' +
          'et créativité dans la gestion de vos affaires matérielles.',
        aspects: [
          { planet1: 'Moon', planet2: 'Venus', type: 'trine', orb: 3.2 },
          { planet1: 'Moon', planet2: 'Mars', type: 'square', orb: 2.5 },
        ],
        planets: [
          { name: 'Sun', sign: 'Gemini', house: 11 },
          { name: 'Mercury', sign: 'Cancer', house: 12 },
        ],
      },
      cached: false,
    };

    // Simuler un délai de chargement
    setTimeout(() => {
      setReport(mockReport);
      setLoading(false);
    }, 1000);
  }, [params]);

  const renderMoonInfo = () => {
    if (!report?.data.moon) return null;

    const { sign, house, degree } = report.data.moon;

    return (
      <View style={styles.card}>
        <Text style={styles.cardTitle}>🌙 Position de la Lune</Text>
        
        <View style={styles.infoRow}>
          <Text style={styles.label}>Signe:</Text>
          <Text style={styles.value}>{sign || 'N/A'}</Text>
        </View>

        <View style={styles.infoRow}>
          <Text style={styles.label}>Maison:</Text>
          <Text style={styles.value}>{house || 'N/A'}</Text>
        </View>

        {degree !== undefined && (
          <View style={styles.infoRow}>
            <Text style={styles.label}>Degré:</Text>
            <Text style={styles.value}>{degree.toFixed(2)}°</Text>
          </View>
        )}
      </View>
    );
  };

  const renderInterpretation = () => {
    if (!report?.data.interpretation) return null;

    return (
      <View style={styles.card}>
        <Text style={styles.cardTitle}>📖 Interprétation</Text>
        <Text style={styles.interpretationText}>
          {report.data.interpretation}
        </Text>
      </View>
    );
  };

  const renderAspects = () => {
    if (!report?.data.aspects || report.data.aspects.length === 0) return null;

    return (
      <View style={styles.card}>
        <Text style={styles.cardTitle}>⭐ Aspects Majeurs</Text>
        {report.data.aspects.map((aspect, index) => (
          <View key={index} style={styles.aspectRow}>
            <Text style={styles.aspectText}>
              {aspect.planet1} {aspect.type} {aspect.planet2}
            </Text>
            <Text style={styles.aspectOrb}>
              Orbe: {aspect.orb?.toFixed(1)}°
            </Text>
          </View>
        ))}
      </View>
    );
  };

  const renderKeyPoints = () => {
    const keyPoints = [
      '🔑 Consolidez vos ressources financières',
      '🔑 Période favorable aux investissements stables',
      '🔑 Développez votre confiance en vous',
      '🔑 Attention aux dépenses impulsives (carré Mars)',
    ];

    return (
      <View style={styles.card}>
        <Text style={styles.cardTitle}>🎯 Points Clés du Mois</Text>
        {keyPoints.map((point, index) => (
          <Text key={index} style={styles.keyPoint}>
            {point}
          </Text>
        ))}
      </View>
    );
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#8B7BF7" />
        <Text style={styles.loadingText}>Chargement du rapport...</Text>
      </View>
    );
  }

  if (!report) {
    return (
      <View style={styles.errorContainer}>
        <Text style={styles.errorText}>❌ Rapport non disponible</Text>
        <TouchableOpacity
          style={styles.backButton}
          onPress={() => router.back()}
        >
          <Text style={styles.backButtonText}>Retour</Text>
        </TouchableOpacity>
      </View>
    );
  }

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity
          style={styles.backButtonSmall}
          onPress={() => router.back()}
        >
          <Text style={styles.backButtonText}>← Retour</Text>
        </TouchableOpacity>
        
        <Text style={styles.title}>Rapport Lunaire Mensuel</Text>
        <Text style={styles.subtitle}>
          {new Date().toLocaleDateString('fr-FR', { 
            month: 'long', 
            year: 'numeric' 
          })}
        </Text>

        {report.cached && (
          <View style={styles.cachedBadge}>
            <Text style={styles.cachedText}>📦 Depuis le cache</Text>
          </View>
        )}
      </View>

      {renderMoonInfo()}
      {renderInterpretation()}
      {renderKeyPoints()}
      {renderAspects()}

      <View style={styles.footer}>
        <Text style={styles.footerText}>
          Rapport généré par {report.provider}
        </Text>
        <Text style={styles.footerText}>
          Type: {report.kind}
        </Text>
      </View>
    </ScrollView>
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
    marginBottom: 20,
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
    backgroundColor: '#8B7BF7',
    padding: 16,
    borderRadius: 8,
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
    marginBottom: 8,
    marginTop: 24,
  },
  subtitle: {
    fontSize: 16,
    color: '#A0A0B0',
    textAlign: 'center',
  },
  cachedBadge: {
    marginTop: 12,
    alignSelf: 'center',
    backgroundColor: '#2D3561',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
  },
  cachedText: {
    fontSize: 12,
    color: '#FFFFFF',
  },
  card: {
    margin: 16,
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
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 12,
  },
  label: {
    fontSize: 16,
    color: '#A0A0B0',
  },
  value: {
    fontSize: 16,
    color: '#FFFFFF',
    fontWeight: '600',
  },
  interpretationText: {
    fontSize: 15,
    color: '#C0C0D0',
    lineHeight: 24,
  },
  aspectRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: '#2D3561',
  },
  aspectText: {
    fontSize: 14,
    color: '#FFFFFF',
  },
  aspectOrb: {
    fontSize: 12,
    color: '#A0A0B0',
  },
  keyPoint: {
    fontSize: 15,
    color: '#C0C0D0',
    marginBottom: 12,
    lineHeight: 22,
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
    marginBottom: 4,
  },
});

