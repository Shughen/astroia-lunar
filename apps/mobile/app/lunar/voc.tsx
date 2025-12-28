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
import { LinearGradient } from 'expo-linear-gradient';
import { lunaPack } from '../../services/api';

export default function VoidOfCourse() {
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [vocData, setVocData] = useState<any>(null);
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

      // Charger le VoC actuel depuis le cache
      const current = await lunaPack.getCurrentVoc();
      setVocData(current);
    } catch (err: any) {
      setError(err.message || 'Erreur lors du chargement du VoC');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const onRefresh = () => loadVocStatus(true);

  if (loading) {
    return (
      <LinearGradient colors={['#1a0b2e', '#2d1b4e']} style={styles.container}>
        <View style={styles.centerContainer}>
          <ActivityIndicator size="large" color="#b794f6" />
          <Text style={styles.loadingText}>Vérification du Void of Course...</Text>
        </View>
      </LinearGradient>
    );
  }

  const isActive = vocData?.is_active || false;

  return (
    <LinearGradient colors={['#1a0b2e', '#2d1b4e']} style={styles.container}>
      <ScrollView
        contentContainerStyle={styles.scrollContent}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor="#b794f6" />
        }
      >
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>🌑 Void of Course</Text>
          <Text style={styles.subtitle}>Période lunaire sans aspects</Text>
        </View>

        {/* Status Badge */}
        <View
          style={[
            styles.statusBadge,
            { backgroundColor: isActive ? 'rgba(248, 113, 113, 0.2)' : 'rgba(74, 222, 128, 0.2)' },
          ]}
        >
          <View
            style={[
              styles.statusDot,
              { backgroundColor: isActive ? '#f87171' : '#4ade80' },
            ]}
          />
          <Text style={styles.statusText}>
            {isActive ? 'VoC EN COURS' : 'Pas de VoC Actif'}
          </Text>
        </View>

        {/* Active VoC Info */}
        {isActive && vocData && (
          <View style={styles.vocCard}>
            <Text style={styles.vocTitle}>⏰ Fenêtre Void of Course Active</Text>
            
            <View style={styles.vocInfo}>
              <View style={styles.vocRow}>
                <Text style={styles.vocLabel}>Début :</Text>
                <Text style={styles.vocValue}>
                  {new Date(vocData.start_at).toLocaleString('fr-FR', {
                    weekday: 'short',
                    hour: '2-digit',
                    minute: '2-digit',
                  })}
                </Text>
              </View>
              
              <View style={styles.vocRow}>
                <Text style={styles.vocLabel}>Fin :</Text>
                <Text style={styles.vocValue}>
                  {new Date(vocData.end_at).toLocaleString('fr-FR', {
                    weekday: 'short',
                    hour: '2-digit',
                    minute: '2-digit',
                  })}
                </Text>
              </View>
            </View>

            <View style={styles.warningBox}>
              <Text style={styles.warningEmoji}>⚠️</Text>
              <Text style={styles.warningText}>
                Période peu propice aux nouvelles initiatives. Privilégier la réflexion et la consolidation.
              </Text>
            </View>
          </View>
        )}

        {/* Not Active Info */}
        {!isActive && (
          <View style={styles.safeCard}>
            <Text style={styles.safeEmoji}>✅</Text>
            <Text style={styles.safeTitle}>Période Favorable</Text>
            <Text style={styles.safeText}>
              La Lune forme des aspects actifs. C'est le bon moment pour lancer de nouveaux projets et prendre des décisions importantes.
            </Text>
          </View>
        )}

        {/* What is VoC? */}
        <View style={styles.infoSection}>
          <Text style={styles.infoTitle}>📚 Qu'est-ce que le Void of Course ?</Text>
          <Text style={styles.infoText}>
            Le Void of Course (VoC) est une période où la Lune ne forme plus d'aspects majeurs avant de changer de signe.
          </Text>
          <Text style={styles.infoText}>
            Pendant cette période, les actions entreprises ont tendance à "ne mener nulle part" ou à nécessiter des ajustements ultérieurs.
          </Text>
          <View style={styles.infoList}>
            <Text style={styles.infoListTitle}>À éviter pendant le VoC :</Text>
            <Text style={styles.infoListItem}>• Signer des contrats importants</Text>
            <Text style={styles.infoListItem}>• Lancer de nouveaux projets</Text>
            <Text style={styles.infoListItem}>• Faire des achats importants</Text>
            <Text style={styles.infoListItem}>• Prendre des décisions majeures</Text>
          </View>
          <View style={styles.infoList}>
            <Text style={styles.infoListTitle}>Favorable pendant le VoC :</Text>
            <Text style={styles.infoListItem}>• Méditation et introspection</Text>
            <Text style={styles.infoListItem}>• Tâches routinières</Text>
            <Text style={styles.infoListItem}>• Repos et relaxation</Text>
            <Text style={styles.infoListItem}>• Créativité sans objectif précis</Text>
          </View>
        </View>

        {/* Last Update */}
        <Text style={styles.lastUpdate}>
          Dernière mise à jour : {new Date().toLocaleTimeString('fr-FR')}
        </Text>
      </ScrollView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  scrollContent: {
    padding: 20,
  },
  header: {
    marginBottom: 24,
    alignItems: 'center',
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
  statusBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 16,
    borderRadius: 12,
    marginBottom: 24,
  },
  statusDot: {
    width: 12,
    height: 12,
    borderRadius: 6,
    marginRight: 12,
  },
  statusText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#ffffff',
  },
  vocCard: {
    backgroundColor: 'rgba(248, 113, 113, 0.1)',
    padding: 20,
    borderRadius: 16,
    marginBottom: 24,
    borderWidth: 2,
    borderColor: 'rgba(248, 113, 113, 0.3)',
  },
  vocTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#f87171',
    marginBottom: 16,
  },
  vocInfo: {
    marginBottom: 16,
  },
  vocRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  vocLabel: {
    fontSize: 14,
    color: '#a0a0b0',
  },
  vocValue: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#ffffff',
  },
  warningBox: {
    flexDirection: 'row',
    backgroundColor: 'rgba(255, 215, 0, 0.1)',
    padding: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: 'rgba(255, 215, 0, 0.3)',
  },
  warningEmoji: {
    fontSize: 20,
    marginRight: 8,
  },
  warningText: {
    flex: 1,
    fontSize: 14,
    color: '#ffd700',
    lineHeight: 20,
  },
  safeCard: {
    backgroundColor: 'rgba(74, 222, 128, 0.1)',
    padding: 20,
    borderRadius: 16,
    marginBottom: 24,
    borderWidth: 2,
    borderColor: 'rgba(74, 222, 128, 0.3)',
    alignItems: 'center',
  },
  safeEmoji: {
    fontSize: 48,
    marginBottom: 12,
  },
  safeTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#4ade80',
    marginBottom: 8,
  },
  safeText: {
    fontSize: 14,
    color: '#ffffff',
    textAlign: 'center',
    lineHeight: 20,
  },
  infoSection: {
    backgroundColor: 'rgba(42, 26, 78, 0.4)',
    padding: 20,
    borderRadius: 12,
    marginBottom: 24,
  },
  infoTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#b794f6',
    marginBottom: 12,
  },
  infoText: {
    fontSize: 14,
    color: '#ffffff',
    lineHeight: 20,
    marginBottom: 12,
  },
  infoList: {
    marginTop: 12,
  },
  infoListTitle: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#ffd700',
    marginBottom: 8,
  },
  infoListItem: {
    fontSize: 13,
    color: '#a0a0b0',
    lineHeight: 20,
  },
  lastUpdate: {
    fontSize: 12,
    color: '#a0a0b0',
    textAlign: 'center',
    marginTop: 8,
  },
  loadingText: {
    color: '#ffffff',
    marginTop: 16,
    fontSize: 16,
  },
});

