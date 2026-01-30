/**
 * Widget Transits Majeurs pour le Home screen (MVP)
 *
 * Affiche:
 * - Top 2-3 transits majeurs du mois (aspects serrés uniquement)
 * - Planètes en transit + aspects + planètes natales
 * - Lien vers l'écran détaillé
 *
 * Optimisé avec SWR pour:
 * - Cache intelligent (60 secondes)
 * - Déduplication des requêtes
 * - Partage du cache entre composants
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';
import { router } from 'expo-router';
import { useMajorTransits } from '../hooks/useLunarData';
import { tPlanet, tAspect } from '../i18n/astro.format';
import { Skeleton } from './Skeleton';
import { haptics } from '../services/haptics';

const ASPECT_COLORS: Record<string, string> = {
  conjunction: '#fbbf24',
  opposition: '#a78bfa',
  square: '#f87171',
  trine: '#4ade80',
};

const ASPECT_SYMBOLS: Record<string, string> = {
  conjunction: '◎',
  opposition: '◉',
  square: '■',
  trine: '▲',
};

export function TransitsWidget() {
  const { data: majorAspects, error, isLoading } = useMajorTransits();

  if (isLoading) {
    return (
      <View style={styles.card}>
        <Skeleton width="60%" height={20} style={{ marginBottom: 16 }} />
        <Skeleton width="100%" height={16} style={{ marginBottom: 8 }} />
        <Skeleton width="90%" height={16} style={{ marginBottom: 8 }} />
        <Skeleton width="85%" height={16} />
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.card}>
        <Text style={styles.errorText}>Transits non disponibles</Text>
      </View>
    );
  }

  // Masquer complètement le widget si pas de transits (UX plus propre)
  if (!majorAspects || majorAspects.length === 0) {
    return null;
  }

  return (
    <TouchableOpacity
      style={styles.card}
      onPress={() => {
        haptics.light();
        router.push('/transits/overview');
      }}
      activeOpacity={0.8}
      testID="transits-widget"
    >
      <View style={styles.header}>
        <Text style={styles.title} testID="transits-title">⭐ Transits Majeurs</Text>
        <Text style={styles.badge} testID="transits-count">{majorAspects.length}</Text>
      </View>

      <View style={styles.content}>
        {majorAspects.map((aspect, index) => {
          const color = ASPECT_COLORS[aspect.aspect] || '#8B7BF7';
          const symbol = ASPECT_SYMBOLS[aspect.aspect] || '●';

          return (
            <View key={index} style={styles.aspectRow}>
              <Text style={[styles.aspectSymbol, { color }]}>{symbol}</Text>
              <View style={styles.aspectInfo}>
                <Text style={styles.aspectText}>
                  {tPlanet(aspect.transit_planet)} {tAspect(aspect.aspect)}{' '}
                  {tPlanet(aspect.natal_planet)}
                </Text>
                {aspect.interpretation && (
                  <Text style={styles.aspectHint} numberOfLines={1}>
                    {aspect.interpretation.split('.')[0]}
                  </Text>
                )}
              </View>
            </View>
          );
        })}
      </View>

      <Text style={styles.ctaText} testID="transits-cta">Voir tous les transits →</Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  badge: {
    backgroundColor: '#8B7BF7',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
    fontSize: 12,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  content: {
    marginBottom: 12,
  },
  aspectRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 10,
  },
  aspectSymbol: {
    fontSize: 18,
    marginRight: 10,
    fontWeight: 'bold',
    width: 24,
  },
  aspectInfo: {
    flex: 1,
  },
  aspectText: {
    fontSize: 15,
    color: '#FFFFFF',
    fontWeight: '600',
    marginBottom: 2,
  },
  aspectHint: {
    fontSize: 13,
    color: '#A0A0B0',
    fontStyle: 'italic',
  },
  emptyText: {
    fontSize: 14,
    color: '#A0A0B0',
    textAlign: 'center',
    marginTop: 8,
  },
  ctaText: {
    fontSize: 14,
    color: '#8B7BF7',
    fontWeight: '600',
  },
  errorText: {
    fontSize: 14,
    color: '#FF6B6B',
    textAlign: 'center',
  },
});
