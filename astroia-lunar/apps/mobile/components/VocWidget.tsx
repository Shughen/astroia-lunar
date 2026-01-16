/**
 * Widget Void of Course pour le Home screen (MVP)
 *
 * Affiche:
 * - VoC actif maintenant ? (oui/non)
 * - Prochaine fenêtre VoC (date + heure)
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
import apiClient from '../services/api';

interface VocWindow {
  start_at: string;
  end_at: string;
}

interface VocStatus {
  now: (VocWindow & { is_active: true }) | null;
  next: VocWindow | null;
  upcoming: VocWindow[];
}

export function VocWidget() {
  const [status, setStatus] = useState<VocStatus | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    loadVocStatus();
    // Refresh toutes les 5 minutes
    const interval = setInterval(loadVocStatus, 5 * 60 * 1000);
    return () => clearInterval(interval);
  }, []);

  const loadVocStatus = async () => {
    try {
      setError(false);
      const response = await apiClient.get('/api/lunar/voc/status');
      setStatus(response.data);
    } catch (err) {
      console.error('[VocWidget] Erreur chargement VoC:', err);
      setError(true);
    } finally {
      setLoading(false);
    }
  };

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
        <Text style={styles.errorText}>VoC non disponible</Text>
      </View>
    );
  }

  const isActive = status?.now?.is_active === true;
  const hasNext = !!status?.next;

  return (
    <TouchableOpacity
      style={styles.card}
      onPress={() => router.push('/lunar/voc')}
      activeOpacity={0.8}
    >
      <View style={styles.header}>
        <Text style={styles.title}>🌑 Void of Course</Text>
        {isActive && <View style={styles.activeBadge}>
          <Text style={styles.activeBadgeText}>ACTIF</Text>
        </View>}
      </View>

      {isActive ? (
        <View style={styles.content}>
          <Text style={styles.statusText}>La Lune est Void of Course</Text>
          {status?.now && (
            <Text style={styles.timeText}>
              Jusqu'à {formatDateTime(status.now.end_at)}
            </Text>
          )}
          <Text style={styles.hintText}>
            Période délicate pour débuter des projets importants
          </Text>
        </View>
      ) : (
        <View style={styles.content}>
          <Text style={styles.statusText}>Pas de VoC actuellement</Text>
          {hasNext ? (
            <Text style={styles.timeText}>
              Prochaine fenêtre: {formatDateTime(status.next!.start_at)}
            </Text>
          ) : (
            <Text style={styles.timeText}>Aucune fenêtre programmée</Text>
          )}
        </View>
      )}

      <Text style={styles.ctaText}>Voir détails →</Text>
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
