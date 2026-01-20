/**
 * Écran Void of Course (Phase 1.3 MVP)
 *
 * Scope strict :
 * - VoC maintenant ? (oui/non + fenêtre active)
 * - Prochaine fenêtre VoC
 * - Liste 2-3 prochaines fenêtres (48h)
 * - UX épurée, zéro pavé
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  RefreshControl,
} from 'react-native';
import { router } from 'expo-router';
import apiClient from '../../services/api';

interface VocWindow {
  start_at: string;
  end_at: string;
}

interface VocStatus {
  now: (VocWindow & { is_active: true }) | null;
  next: VocWindow | null;
  upcoming: VocWindow[];
}

export default function VoidOfCourseScreen() {
  const [status, setStatus] = useState<VocStatus | null>(null);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadVocStatus();
    // Poll toutes les 5 minutes
    const interval = setInterval(loadVocStatus, 5 * 60 * 1000);
    return () => clearInterval(interval);
  }, []);

  const loadVocStatus = async (isRefresh = false) => {
    try {
      if (isRefresh) {
        setRefreshing(true);
      } else {
        setLoading(true);
      }
      setError(null);

      const response = await apiClient.get('/api/lunar/voc/status');
      setStatus(response.data);
    } catch (err: any) {
      console.error('[VoC] Erreur chargement status:', err);
      setError('Erreur lors du chargement des Pauses Lunaires');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const onRefresh = () => loadVocStatus(true);

  const formatDateTime = (isoString: string, showDate = false): string => {
    const date = new Date(isoString);
    const options: Intl.DateTimeFormatOptions = {
      hour: '2-digit',
      minute: '2-digit',
    };

    if (showDate) {
      options.weekday = 'short';
      options.day = 'numeric';
      options.month = 'short';
    }

    return date.toLocaleString('fr-FR', options);
  };

  const formatDuration = (start: string, end: string): string => {
    const startDate = new Date(start);
    const endDate = new Date(end);
    const durationMs = endDate.getTime() - startDate.getTime();
    const hours = Math.floor(durationMs / (1000 * 60 * 60));
    const minutes = Math.floor((durationMs % (1000 * 60 * 60)) / (1000 * 60));

    if (hours > 0) {
      return `${hours}h${minutes > 0 ? minutes.toString().padStart(2, '0') : ''}`;
    }
    return `${minutes}min`;
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#8B7BF7" />
        <Text style={styles.loadingText}>Chargement des Pauses Lunaires...</Text>
      </View>
    );
  }

  if (error || !status) {
    return (
      <View style={styles.errorContainer}>
        <Text style={styles.errorText}>{error || 'Données non disponibles'}</Text>
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

  const isActive = !!status.now;

  return (
    <ScrollView
      style={styles.container}
      contentContainerStyle={styles.scrollContent}
      refreshControl={
        <RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor="#8B7BF7" />
      }
    >
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity
          style={styles.backButtonSmall}
          onPress={() => router.back()}
          hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
        >
          <Text style={styles.backButtonText}>← Retour</Text>
        </TouchableOpacity>

        <Text style={styles.title}>🌑 Pause Lunaire</Text>
        <Text style={styles.subtitle}>Période où la Lune flotte librement</Text>
      </View>

      {/* Status Badge */}
      <View style={[styles.statusBadge, isActive ? styles.statusBadgeActive : styles.statusBadgeInactive]}>
        <View style={[styles.statusDot, isActive ? styles.statusDotActive : styles.statusDotInactive]} />
        <Text style={styles.statusText}>{isActive ? 'PAUSE EN COURS' : 'Pas de pause active'}</Text>
      </View>

      {/* VoC Actif Maintenant */}
      {isActive && status.now && (
        <View style={styles.activeCard}>
          <Text style={styles.cardTitle}>⏰ Fenêtre active</Text>

          <View style={styles.timeRow}>
            <Text style={styles.timeLabel}>Début :</Text>
            <Text style={styles.timeValue}>{formatDateTime(status.now.start_at, true)}</Text>
          </View>

          <View style={styles.timeRow}>
            <Text style={styles.timeLabel}>Fin :</Text>
            <Text style={styles.timeValue}>{formatDateTime(status.now.end_at, true)}</Text>
          </View>

          <View style={styles.durationRow}>
            <Text style={styles.durationLabel}>Durée :</Text>
            <Text style={styles.durationValue}>{formatDuration(status.now.start_at, status.now.end_at)}</Text>
          </View>

          <View style={styles.hintBox}>
            <Text style={styles.hintEmoji}>💡</Text>
            <Text style={styles.hintText}>
              Moment idéal pour l'introspection, le repos et la réflexion.
            </Text>
          </View>
        </View>
      )}

      {/* Prochaine Pause */}
      {status.next && (
        <View style={styles.nextCard}>
          <Text style={styles.cardTitle}>📅 Prochaine pause</Text>

          <View style={styles.timeRow}>
            <Text style={styles.timeLabel}>Début :</Text>
            <Text style={styles.timeValue}>{formatDateTime(status.next.start_at, true)}</Text>
          </View>

          <View style={styles.timeRow}>
            <Text style={styles.timeLabel}>Fin :</Text>
            <Text style={styles.timeValue}>{formatDateTime(status.next.end_at, true)}</Text>
          </View>

          <View style={styles.durationRow}>
            <Text style={styles.durationLabel}>Durée :</Text>
            <Text style={styles.durationValue}>{formatDuration(status.next.start_at, status.next.end_at)}</Text>
          </View>
        </View>
      )}

      {/* Upcoming Windows (48h) */}
      {status.upcoming && status.upcoming.length > 0 && (
        <View style={styles.upcomingCard}>
          <Text style={styles.cardTitle}>🔮 Prochaines pauses (48h)</Text>

          {status.upcoming.map((window, index) => (
            <View key={index} style={styles.upcomingItem}>
              <View style={styles.upcomingDot} />
              <View style={styles.upcomingInfo}>
                <Text style={styles.upcomingTime}>
                  {formatDateTime(window.start_at, true)} → {formatDateTime(window.end_at)}
                </Text>
                <Text style={styles.upcomingDuration}>Durée : {formatDuration(window.start_at, window.end_at)}</Text>
              </View>
            </View>
          ))}
        </View>
      )}

      {/* Info Pause Lunaire */}
      <View style={styles.infoCard}>
        <Text style={styles.infoTitle}>Qu'est-ce que la Pause Lunaire ?</Text>
        <Text style={styles.infoText}>
          Période où la Lune ne forme plus d'aspects majeurs avant de changer de signe. C'est un moment propice à
          l'introspection, au repos et à la consolidation de vos projets.
        </Text>
      </View>

      {/* Last Update */}
      <Text style={styles.lastUpdate}>Dernière mise à jour : {new Date().toLocaleTimeString('fr-FR')}</Text>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0A0E27',
  },
  scrollContent: {
    paddingBottom: 40,
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
  statusBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 16,
    margin: 16,
    borderRadius: 12,
  },
  statusBadgeActive: {
    backgroundColor: 'rgba(248, 113, 113, 0.2)',
  },
  statusBadgeInactive: {
    backgroundColor: 'rgba(74, 222, 128, 0.2)',
  },
  statusDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: 12,
  },
  statusDotActive: {
    backgroundColor: '#F87171',
  },
  statusDotInactive: {
    backgroundColor: '#4ADE80',
  },
  statusText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  activeCard: {
    margin: 16,
    marginTop: 0,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 2,
    borderColor: '#F87171',
  },
  nextCard: {
    margin: 16,
    marginTop: 0,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  upcomingCard: {
    margin: 16,
    marginTop: 0,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#8B7BF7',
    marginBottom: 16,
  },
  timeRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  timeLabel: {
    fontSize: 14,
    color: '#A0A0B0',
  },
  timeValue: {
    fontSize: 14,
    fontWeight: '600',
    color: '#FFFFFF',
  },
  durationRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 8,
    paddingTop: 12,
    borderTopWidth: 1,
    borderTopColor: '#2D3561',
  },
  durationLabel: {
    fontSize: 14,
    color: '#A0A0B0',
  },
  durationValue: {
    fontSize: 14,
    fontWeight: '600',
    color: '#8B7BF7',
  },
  hintBox: {
    flexDirection: 'row',
    backgroundColor: 'rgba(255, 215, 0, 0.1)',
    padding: 12,
    borderRadius: 8,
    marginTop: 16,
  },
  hintEmoji: {
    fontSize: 18,
    marginRight: 8,
  },
  hintText: {
    flex: 1,
    fontSize: 13,
    color: '#FFD700',
    lineHeight: 18,
  },
  upcomingItem: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 12,
  },
  upcomingDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#8B7BF7',
    marginTop: 6,
    marginRight: 12,
  },
  upcomingInfo: {
    flex: 1,
  },
  upcomingTime: {
    fontSize: 14,
    color: '#FFFFFF',
    marginBottom: 4,
  },
  upcomingDuration: {
    fontSize: 12,
    color: '#A0A0B0',
  },
  infoCard: {
    margin: 16,
    marginTop: 0,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  infoTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#8B7BF7',
    marginBottom: 12,
  },
  infoText: {
    fontSize: 14,
    color: '#C0C0D0',
    lineHeight: 22,
  },
  lastUpdate: {
    fontSize: 12,
    color: '#A0A0B0',
    textAlign: 'center',
    marginBottom: 20,
  },
});
