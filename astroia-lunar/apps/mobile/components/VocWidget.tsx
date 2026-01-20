/**
 * Widget Void of Course pour le Home screen (MVP)
 *
 * Affiche:
 * - VoC actif maintenant ? (oui/non)
 * - Prochaine fenêtre VoC (date + heure)
 * - Lien vers l'écran détaillé
 *
 * Optimisé avec SWR pour:
 * - Cache intelligent (5 minutes)
 * - Auto-refresh toutes les 5 minutes
 * - Déduplication des requêtes
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';
import { router } from 'expo-router';
import { useVocStatus } from '../hooks/useLunarData';
import { Skeleton } from './Skeleton';
import { haptics } from '../services/haptics';

export function VocWidget() {
  const { data: status, error, isLoading } = useVocStatus();

  const formatDateTime = (isoString: string): string => {
    try {
      const date = new Date(isoString);
      return date.toLocaleString('fr-FR', {
        weekday: 'short',
        day: 'numeric',
        month: 'short',
        hour: '2-digit',
        minute: '2-digit',
      });
    } catch {
      return 'Date invalide';
    }
  };

  if (isLoading) {
    return (
      <View style={styles.card}>
        <Skeleton width="60%" height={20} style={{ marginBottom: 12 }} />
        <Skeleton width="100%" height={16} style={{ marginBottom: 8 }} />
        <Skeleton width="80%" height={14} />
      </View>
    );
  }

  if (error || !status) {
    return (
      <View style={styles.card}>
        <Text style={styles.errorText}>Données non disponibles</Text>
      </View>
    );
  }

  const isActive = status?.now?.is_active === true;
  const hasNext = !!status?.next;

  return (
    <TouchableOpacity
      style={styles.card}
      onPress={() => {
        haptics.light();
        router.push('/lunar/voc');
      }}
      activeOpacity={0.8}
      testID="voc-widget"
    >
      <View style={styles.header}>
        <Text style={styles.title} testID="voc-title">🌑 Pause Lunaire</Text>
        {isActive && <View style={styles.activeBadge}>
          <Text style={styles.activeBadgeText} testID="voc-active-badge">ACTIF</Text>
        </View>}
      </View>

      {isActive ? (
        <View style={styles.content}>
          <Text style={styles.statusText} testID="voc-status-active">La Lune est en pause</Text>
          {status?.now && (
            <Text style={styles.timeText} testID="voc-time">
              Jusqu'à {formatDateTime(status.now.end_at)}
            </Text>
          )}
          <Text style={styles.hintText}>
            Moment idéal pour l'introspection et le repos
          </Text>
        </View>
      ) : (
        <View style={styles.content}>
          <Text style={styles.statusText} testID="voc-status-inactive">Pas de pause actuellement</Text>
          {hasNext ? (
            <Text style={styles.timeText} testID="voc-next">
              Prochaine pause: {formatDateTime(status.next!.start_at)}
            </Text>
          ) : (
            <Text style={styles.timeText}>Aucune fenêtre programmée</Text>
          )}
        </View>
      )}

      <Text style={styles.ctaText} testID="voc-cta">Voir détails →</Text>
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
  activeBadge: {
    backgroundColor: '#FF6B6B',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
  },
  activeBadgeText: {
    color: '#FFFFFF',
    fontSize: 10,
    fontWeight: '700',
    letterSpacing: 0.5,
  },
  content: {
    marginBottom: 12,
  },
  statusText: {
    fontSize: 15,
    color: '#FFFFFF',
    marginBottom: 6,
    fontWeight: '600',
  },
  timeText: {
    fontSize: 14,
    color: '#A0A0B0',
    marginBottom: 6,
  },
  hintText: {
    fontSize: 13,
    color: '#8B7BF7',
    fontStyle: 'italic',
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
