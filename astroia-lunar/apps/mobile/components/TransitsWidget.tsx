/**
 * Widget Transits Majeurs pour le Home screen (MVP)
 *
 * Affiche:
 * - Top 2-3 transits majeurs du mois (aspects serrés uniquement)
 * - Planètes en transit + aspects + planètes natales
 * - Lien vers l'écran détaillé
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';
import { router } from 'expo-router';
import { transits } from '../services/api';
import { useAuthStore } from '../stores/useAuthStore';
import { isDevAuthBypassActive, getDevAuthHeader } from '../services/api';
import { tPlanet, tAspect } from '../i18n/astro.format';

interface AspectInfo {
  transit_planet: string;
  natal_planet: string;
  aspect: string;
  orb: number;
  interpretation?: string;
}

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
  const { user, isAuthenticated } = useAuthStore();
  const [majorAspects, setMajorAspects] = useState<AspectInfo[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    if (isAuthenticated || isDevAuthBypassActive()) {
      loadTransits();
    } else {
      setLoading(false);
    }
  }, [user, isAuthenticated]);

  const loadTransits = async () => {
    try {
      setError(false);

      // Récupérer userId
      let userId: string;
      if (isDevAuthBypassActive()) {
        const devHeader = getDevAuthHeader();
        userId = devHeader.value || 'dev-user-id';
      } else if (user?.id) {
        userId = typeof user.id === 'string' ? user.id : String(user.id);
      } else {
        throw new Error('Utilisateur non authentifié');
      }

      // Construire le mois au format YYYY-MM
      const now = new Date();
      const month = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`;

      // Appeler l'API pour récupérer les transits
      const response = await transits.getOverview(userId, month);

      if (response) {
        const overviewData = response?.overview || response?.summary;
        const insights = overviewData?.insights || {};
        const allAspects = insights?.major_aspects || [];

        // Filtrer pour ne garder que les 4 aspects majeurs MVP
        const MAJOR_ASPECTS_MVP = ['conjunction', 'opposition', 'square', 'trine'];

        // Planètes réelles uniquement (exclure nœuds, Chiron, etc.)
        const PLANETARY_BODIES = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'];
        const EXCLUDED_KEYWORDS = ['node', 'Node', 'chiron', 'Chiron', 'lilith', 'Lilith', 'Fortune', 'Vertex'];

        const majorOnlyAspects = allAspects.filter((aspect: any) => {
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

          // Garder si les deux planètes sont dans la liste blanche
          const transitIsValid = PLANETARY_BODIES.some(planet => transitPlanet.includes(planet));
          const natalIsValid = PLANETARY_BODIES.some(planet => natalPlanet.includes(planet));

          return transitIsValid && natalIsValid;
        });

        // Garder uniquement les 3 aspects les plus serrés (orbe le plus petit)
        const sortedAspects = [...majorOnlyAspects]
          .sort((a, b) => Math.abs(a.orb) - Math.abs(b.orb))
          .slice(0, 3);

        setMajorAspects(sortedAspects);
      } else {
        setMajorAspects([]);
      }
    } catch (err) {
      console.error('[TransitsWidget] Erreur chargement transits:', err);
      setError(true);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.card}>
        <ActivityIndicator size="small" color="#8B7BF7" />
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

  if (majorAspects.length === 0) {
    return (
      <View style={styles.card}>
        <View style={styles.header}>
          <Text style={styles.title}>⭐ Transits du Mois</Text>
        </View>
        <Text style={styles.emptyText}>Aucun transit majeur ce mois-ci</Text>
      </View>
    );
  }

  return (
    <TouchableOpacity
      style={styles.card}
      onPress={() => router.push('/transits/overview')}
      activeOpacity={0.8}
    >
      <View style={styles.header}>
        <Text style={styles.title}>⭐ Transits Majeurs</Text>
        <Text style={styles.badge}>{majorAspects.length}</Text>
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

      <Text style={styles.ctaText}>Voir tous les transits →</Text>
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
