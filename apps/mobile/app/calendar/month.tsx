import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { calendar } from '../../services/api';

const MONTH_NAMES = [
  'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
  'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
];

const PHASE_EMOJIS: Record<string, string> = {
  new_moon: '🌑',
  first_quarter: '🌓',
  full_moon: '🌕',
  last_quarter: '🌗',
};

export default function CalendarMonth() {
  // Initialiser avec une date sûre
  const [currentDate, setCurrentDate] = useState<Date>(() => new Date());
  const [loading, setLoading] = useState(false);
  const [calendarData, setCalendarData] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Guard: vérifier que currentDate est valide
    if (!currentDate || !(currentDate instanceof Date) || isNaN(currentDate.getTime())) {
      console.error('[CalendarMonth] Date invalide, réinitialisation');
      setCurrentDate(new Date());
      return;
    }
    loadCalendar();
  }, [currentDate]);

  const loadCalendar = async () => {
    // Guard: vérifier que currentDate existe et est valide avant utilisation
    if (!currentDate || !(currentDate instanceof Date) || isNaN(currentDate.getTime())) {
      console.error('[CalendarMonth] Impossible de charger: date invalide');
      setError('Date invalide');
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const year = currentDate.getFullYear();
      const month = currentDate.getMonth() + 1;

      // Validation des valeurs
      if (isNaN(year) || isNaN(month) || month < 1 || month > 12) {
        throw new Error('Date invalide: année ou mois incorrect');
      }

      const response = await calendar.getMonth(year, month);
      setCalendarData(response);
    } catch (err: any) {
      console.error('[CalendarMonth] Erreur chargement:', err);
      setError(err.message || 'Erreur lors du chargement du calendrier');
    } finally {
      setLoading(false);
    }
  };

  const changeMonth = (delta: number) => {
    // Guard: vérifier que currentDate existe avant modification
    if (!currentDate || !(currentDate instanceof Date) || isNaN(currentDate.getTime())) {
      console.error('[CalendarMonth] Impossible de changer de mois: date invalide');
      setCurrentDate(new Date());
      return;
    }

    const newDate = new Date(currentDate);
    newDate.setMonth(newDate.getMonth() + delta);
    
    // Vérifier que la nouvelle date est valide
    if (isNaN(newDate.getTime())) {
      console.error('[CalendarMonth] Nouvelle date invalide après changement');
      setCurrentDate(new Date());
      return;
    }
    
    setCurrentDate(newDate);
  };

  // Guards pour l'affichage
  if (!currentDate || !(currentDate instanceof Date) || isNaN(currentDate.getTime())) {
    return (
      <LinearGradient colors={['#1a0b2e', '#2d1b4e']} style={styles.container}>
        <View style={styles.errorContainer}>
          <Text style={styles.errorEmoji}>⚠️</Text>
          <Text style={styles.errorText}>Erreur: date invalide</Text>
          <TouchableOpacity style={styles.retryButton} onPress={() => setCurrentDate(new Date())}>
            <Text style={styles.retryText}>Réinitialiser</Text>
          </TouchableOpacity>
        </View>
      </LinearGradient>
    );
  }

  const monthName = MONTH_NAMES[currentDate.getMonth()];
  const year = currentDate.getFullYear();

  return (
    <LinearGradient colors={['#1a0b2e', '#2d1b4e']} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header avec Navigation */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => changeMonth(-1)} style={styles.navButton}>
            <Text style={styles.navText}>←</Text>
          </TouchableOpacity>
          <View style={styles.titleContainer}>
            <Text style={styles.title}>{monthName} {year}</Text>
            <Text style={styles.subtitle}>📅 Calendrier Lunaire</Text>
          </View>
          <TouchableOpacity onPress={() => changeMonth(1)} style={styles.navButton}>
            <Text style={styles.navText}>→</Text>
          </TouchableOpacity>
        </View>

        {loading && (
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#b794f6" />
            <Text style={styles.loadingText}>Chargement...</Text>
          </View>
        )}

        {error && (
          <View style={styles.errorContainer}>
            <Text style={styles.errorEmoji}>⚠️</Text>
            <Text style={styles.errorText}>{error}</Text>
            <TouchableOpacity style={styles.retryButton} onPress={loadCalendar}>
              <Text style={styles.retryText}>Réessayer</Text>
            </TouchableOpacity>
          </View>
        )}

        {!loading && !error && calendarData && (
          <>
            {/* Summary Cards */}
            <View style={styles.summaryContainer}>
              <View style={styles.summaryCard}>
                <Text style={styles.summaryEmoji}>🌑</Text>
                <Text style={styles.summaryValue}>{calendarData.summary?.new_moons || 0}</Text>
                <Text style={styles.summaryLabel}>Nouvelles Lunes</Text>
              </View>
              <View style={styles.summaryCard}>
                <Text style={styles.summaryEmoji}>🌕</Text>
                <Text style={styles.summaryValue}>{calendarData.summary?.full_moons || 0}</Text>
                <Text style={styles.summaryLabel}>Pleines Lunes</Text>
              </View>
              <View style={styles.summaryCard}>
                <Text style={styles.summaryEmoji}>🌒</Text>
                <Text style={styles.summaryValue}>{calendarData.summary?.eclipses || 0}</Text>
                <Text style={styles.summaryLabel}>Éclipses</Text>
              </View>
              <View style={styles.summaryCard}>
                <Text style={styles.summaryEmoji}>✨</Text>
                <Text style={styles.summaryValue}>{calendarData.summary?.special_events || 0}</Text>
                <Text style={styles.summaryLabel}>Événements</Text>
              </View>
            </View>

            {/* Events List */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🌙 Événements du Mois</Text>
              
              {/* Placeholder events */}
              <View style={styles.eventCard}>
                <View style={styles.eventDate}>
                  <Text style={styles.eventDay}>13</Text>
                  <Text style={styles.eventMonth}>Nov</Text>
                </View>
                <View style={styles.eventContent}>
                  <View style={styles.eventHeader}>
                    <Text style={styles.eventEmoji}>🌕</Text>
                    <Text style={styles.eventTitle}>Pleine Lune en Cancer</Text>
                  </View>
                  <Text style={styles.eventTime}>05:27</Text>
                  <Text style={styles.eventDescription}>
                    Culmin émotionnel, introspection, famille
                  </Text>
                </View>
              </View>

              <View style={styles.eventCard}>
                <View style={styles.eventDate}>
                  <Text style={styles.eventDay}>29</Text>
                  <Text style={styles.eventMonth}>Nov</Text>
                </View>
                <View style={styles.eventContent}>
                  <View style={styles.eventHeader}>
                    <Text style={styles.eventEmoji}>🌑</Text>
                    <Text style={styles.eventTitle}>Nouvelle Lune en Verseau</Text>
                  </View>
                  <Text style={styles.eventTime}>12:36</Text>
                  <Text style={styles.eventDescription}>
                    Nouveau départ, innovation, projets futurs
                  </Text>
                </View>
              </View>

              {calendarData.days?.length === 0 && (
                <View style={styles.emptyState}>
                  <Text style={styles.emptyText}>
                    Aucun événement majeur ce mois-ci
                  </Text>
                </View>
              )}
            </View>

            {/* Mansions Quick View */}
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>🏰 Mansions Lunaires</Text>
              <Text style={styles.mansionHint}>
                28 mansions lunaires réparties sur le cycle mensuel
              </Text>
              <TouchableOpacity style={styles.mansionButton}>
                <Text style={styles.mansionButtonText}>Voir la Mansion du Jour</Text>
              </TouchableOpacity>
            </View>
          </>
        )}
      </ScrollView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    padding: 20,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 24,
  },
  navButton: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: 'rgba(183, 148, 246, 0.2)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  navText: {
    color: '#b794f6',
    fontSize: 24,
    fontWeight: 'bold',
  },
  titleContainer: {
    flex: 1,
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#ffd700',
  },
  subtitle: {
    fontSize: 14,
    color: '#b794f6',
    marginTop: 4,
  },
  summaryContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 24,
    gap: 8,
  },
  summaryCard: {
    flex: 1,
    backgroundColor: 'rgba(42, 26, 78, 0.6)',
    padding: 12,
    borderRadius: 12,
    alignItems: 'center',
  },
  summaryEmoji: {
    fontSize: 24,
    marginBottom: 4,
  },
  summaryValue: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#ffd700',
    marginBottom: 2,
  },
  summaryLabel: {
    fontSize: 11,
    color: '#a0a0b0',
    textAlign: 'center',
  },
  section: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#b794f6',
    marginBottom: 12,
  },
  eventCard: {
    flexDirection: 'row',
    backgroundColor: 'rgba(42, 26, 78, 0.8)',
    padding: 16,
    borderRadius: 12,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: 'rgba(255, 215, 0, 0.3)',
  },
  eventDate: {
    width: 60,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 16,
    borderRightWidth: 2,
    borderRightColor: 'rgba(183, 148, 246, 0.3)',
  },
  eventDay: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#ffd700',
  },
  eventMonth: {
    fontSize: 12,
    color: '#a0a0b0',
  },
  eventContent: {
    flex: 1,
  },
  eventHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 4,
  },
  eventEmoji: {
    fontSize: 20,
    marginRight: 8,
  },
  eventTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#ffffff',
    flex: 1,
  },
  eventTime: {
    fontSize: 14,
    color: '#b794f6',
    marginBottom: 4,
  },
  eventDescription: {
    fontSize: 14,
    color: '#a0a0b0',
  },
  mansionHint: {
    fontSize: 14,
    color: '#a0a0b0',
    marginBottom: 12,
  },
  mansionButton: {
    backgroundColor: '#b794f6',
    padding: 12,
    borderRadius: 8,
    alignItems: 'center',
  },
  mansionButtonText: {
    color: '#000000',
    fontWeight: 'bold',
    fontSize: 16,
  },
  emptyState: {
    alignItems: 'center',
    padding: 32,
  },
  emptyText: {
    color: '#a0a0b0',
    fontSize: 14,
    textAlign: 'center',
  },
  loadingContainer: {
    padding: 40,
    alignItems: 'center',
  },
  loadingText: {
    color: '#ffffff',
    marginTop: 16,
    fontSize: 16,
  },
  errorContainer: {
    padding: 40,
    alignItems: 'center',
  },
  errorEmoji: {
    fontSize: 60,
    marginBottom: 16,
  },
  errorText: {
    color: '#f87171',
    fontSize: 16,
    textAlign: 'center',
    marginBottom: 24,
  },
  retryButton: {
    backgroundColor: '#b794f6',
    paddingHorizontal: 24,
    paddingVertical: 12,
    borderRadius: 8,
  },
  retryText: {
    color: '#000000',
    fontWeight: 'bold',
    fontSize: 16,
  },
  backButton: {
    marginBottom: 16,
  },
  backText: {
    color: '#b794f6',
    fontSize: 16,
  },
});

