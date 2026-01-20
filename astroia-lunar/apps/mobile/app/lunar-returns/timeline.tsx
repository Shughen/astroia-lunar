/**
 * Timeline des 12 cycles lunaires (Phase 1.5 MVP)
 *
 * Scope :
 * - Liste des 12 prochains cycles (mois courant + 11 suivants)
 * - Tap → ouvre rapport mensuel du cycle
 * - Highlight du cycle en cours
 */

import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';
import { router } from 'expo-router';
import apiClient from '../../services/api';
import { SkeletonList } from '../../components/Skeleton';

interface LunarReturnItem {
  id: number;
  return_date: string;
  moon_sign?: string;
  moon_house?: number;
  lunar_ascendant?: string;
}

export default function LunarTimelineScreen() {
  const [cycles, setCycles] = useState<LunarReturnItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadCycles();
  }, []);

  const loadCycles = async () => {
    try {
      setLoading(true);
      setError(null);

      const response = await apiClient.get('/api/lunar-returns/rolling');
      setCycles(response.data);
    } catch (err: any) {
      console.error('[Timeline] Erreur chargement cycles:', err);
      setError('Erreur lors du chargement des cycles');
    } finally {
      setLoading(false);
    }
  };

  const formatMonth = (dateStr: string): string => {
    const date = new Date(dateStr);
    const month = date.toLocaleDateString('fr-FR', { month: 'long' });
    return month.charAt(0).toUpperCase() + month.slice(1);
  };

  const formatDateRange = (dateStr: string): string => {
    const date = new Date(dateStr);
    const day = date.getDate();
    const month = date.toLocaleDateString('fr-FR', { month: 'short' });

    // Calcul fin de cycle (28 jours après)
    const endDate = new Date(date);
    endDate.setDate(endDate.getDate() + 28);
    const endDay = endDate.getDate();
    const endMonth = endDate.toLocaleDateString('fr-FR', { month: 'short' });

    return `${day} ${month} - ${endDay} ${endMonth}`;
  };

  const isCurrentCycle = (index: number): boolean => {
    return index === 0;
  };

  const handleCycleTap = (cycleId: number) => {
    router.push(`/lunar/report?id=${cycleId}` as any);
  };

  if (loading) {
    return (
      <ScrollView style={styles.container}>
        <View style={styles.header}>
          <TouchableOpacity
            style={styles.backButtonSmall}
            onPress={() => router.back()}
            hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
          >
            <Text style={styles.backButtonText}>← Retour</Text>
          </TouchableOpacity>

          <Text style={styles.title}>Timeline des Cycles</Text>
          <Text style={styles.subtitle}>12 prochaines révolutions lunaires</Text>
        </View>

        <View style={styles.cyclesList}>
          <SkeletonList count={12} />
        </View>
      </ScrollView>
    );
  }

  if (error || cycles.length === 0) {
    return (
      <View style={styles.errorContainer}>
        <Text style={styles.errorText}>
          {error || 'Aucun cycle disponible'}
        </Text>
        <TouchableOpacity
          style={styles.backButton}
          onPress={() => router.back()}
          hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
        >
          <Text style={styles.backButtonText}>← Retour</Text>
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
          hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
        >
          <Text style={styles.backButtonText}>← Retour</Text>
        </TouchableOpacity>

        <Text style={styles.title}>Timeline des Cycles</Text>
        <Text style={styles.subtitle}>12 prochaines révolutions lunaires</Text>
      </View>

      <View style={styles.cyclesList}>
        {cycles.map((cycle, index) => (
          <TouchableOpacity
            key={cycle.id}
            style={[
              styles.cycleCard,
              isCurrentCycle(index) && styles.cycleCardCurrent,
            ]}
            onPress={() => handleCycleTap(cycle.id)}
          >
            {isCurrentCycle(index) && (
              <View style={styles.currentBadge}>
                <Text style={styles.currentBadgeText}>Cycle en cours</Text>
              </View>
            )}

            <Text style={styles.cycleMonth}>{formatMonth(cycle.return_date)}</Text>
            <Text style={styles.cycleDates}>{formatDateRange(cycle.return_date)}</Text>

            {cycle.moon_sign && (
              <View style={styles.cycleInfo}>
                <Text style={styles.cycleInfoLabel}>Lune en</Text>
                <Text style={styles.cycleInfoValue}>
                  {cycle.moon_sign}
                  {cycle.moon_house && ` • Maison ${cycle.moon_house}`}
                </Text>
              </View>
            )}

            {cycle.lunar_ascendant && (
              <View style={styles.cycleInfo}>
                <Text style={styles.cycleInfoLabel}>Ascendant</Text>
                <Text style={styles.cycleInfoValue}>{cycle.lunar_ascendant}</Text>
              </View>
            )}

            <Text style={styles.cycleCTA}>Voir le rapport →</Text>
          </TouchableOpacity>
        ))}
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
    textAlign: 'center',
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
    marginBottom: 4,
    marginTop: 24,
  },
  subtitle: {
    fontSize: 16,
    color: '#A0A0B0',
    textAlign: 'center',
  },
  cyclesList: {
    padding: 16,
  },
  cycleCard: {
    marginBottom: 16,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  cycleCardCurrent: {
    borderColor: '#8B7BF7',
    borderWidth: 2,
  },
  currentBadge: {
    position: 'absolute',
    top: 12,
    right: 12,
    backgroundColor: '#8B7BF7',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 6,
  },
  currentBadgeText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  cycleMonth: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#8B7BF7',
    marginBottom: 4,
  },
  cycleDates: {
    fontSize: 14,
    color: '#A0A0B0',
    marginBottom: 16,
  },
  cycleInfo: {
    marginBottom: 12,
  },
  cycleInfoLabel: {
    fontSize: 12,
    color: '#A0A0B0',
    marginBottom: 4,
  },
  cycleInfoValue: {
    fontSize: 15,
    color: '#FFFFFF',
    fontWeight: '600',
  },
  cycleCTA: {
    marginTop: 8,
    fontSize: 14,
    color: '#8B7BF7',
    fontWeight: '600',
  },
});
