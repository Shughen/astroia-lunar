/**
 * Écran principal Luna Pack
 * Interface pour tester les 3 fonctionnalités lunaires avancées
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  ScrollView,
  StyleSheet,
  ActivityIndicator,
} from 'react-native';
import { getLunarReturnReport, getVoidOfCourse, getLunarMansion } from '../../services/api';
import { showNetworkErrorAlert } from '../../utils/errorHandler';
import { isMockResponse, getProviderLabel, cleanInterpretationText } from '../../utils/mockUtils';
import { isDev } from '../../utils/env';

/**
 * Fonction utilitaire pour accéder aux propriétés imbriquées de manière sûre
 * @param obj Objet à parcourir
 * @param path Chemin vers la propriété (ex: 'data.mansion.name')
 * @param defaultValue Valeur par défaut si la propriété n'existe pas
 */
function get(obj: any, path: string, defaultValue: any = undefined): any {
  const keys = path.split('.');
  let result = obj;

  for (const key of keys) {
    if (result == null || typeof result !== 'object') {
      return defaultValue;
    }
    result = result[key];
  }

  return result !== undefined ? result : defaultValue;
}

/**
 * Formate une date ISO en format court lisible
 * Ex: "2025-12-31T10:30:00" -> "31/12 10:30"
 * UI FIX: Retourner "—" au lieu de "N/A" pour valeurs manquantes
 */
function formatShortDateTime(isoString: string | undefined): string {
  if (!isoString) return '—';

  try {
    const date = new Date(isoString);
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');

    return `${day}/${month} ${hours}:${minutes}`;
  } catch {
    return isoString;
  }
}

export default function LunaPackScreen() {
  const [loading, setLoading] = useState(false);
  const [selectedFeature, setSelectedFeature] = useState<string | null>(null);
  const [result, setResult] = useState<any>(null);
  const [showRawJson, setShowRawJson] = useState(false);

  // Payload de test hardcodé (Paris, France - date actuelle)
  const testPayload = {
    date: new Date().toISOString().split('T')[0], // YYYY-MM-DD
    time: '12:00',
    latitude: 48.8566,
    longitude: 2.3522,
    timezone: 'Europe/Paris',
  };

  const handleLunarReturnReport = async () => {
    setSelectedFeature('lunar_return_report');
    setLoading(true);
    setResult(null);

    try {
      const payload = {
        ...testPayload,
        birth_date: '1990-01-15',
        birth_time: '14:30',
        month: new Date().toISOString().slice(0, 7), // YYYY-MM
      };

      const response = await getLunarReturnReport(payload);
      setResult(response);
    } catch (error: any) {
      showNetworkErrorAlert(
        error,
        () => handleLunarReturnReport(),
        'Le rapport est temporairement indisponible.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleVoidOfCourse = async () => {
    setSelectedFeature('void_of_course');
    setLoading(true);
    setResult(null);

    try {
      const response = await getVoidOfCourse(testPayload);
      setResult(response);
    } catch (error: any) {
      showNetworkErrorAlert(
        error,
        () => handleVoidOfCourse(),
        'Le Void of Course est temporairement indisponible.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleLunarMansion = async () => {
    setSelectedFeature('lunar_mansion');
    setLoading(true);
    setResult(null);

    try {
      const response = await getLunarMansion(testPayload);
      setResult(response);
    } catch (error: any) {
      showNetworkErrorAlert(
        error,
        () => handleLunarMansion(),
        'La Lunar Mansion est temporairement indisponible.'
      );
    } finally {
      setLoading(false);
    }
  };

  const renderSummary = () => {
    if (!result) return null;

    const { kind, data } = result;
    const isMock = isMockResponse(result);
    const providerLabel = getProviderLabel(result);

    return (
      <View style={styles.resultContainer}>
        <View style={styles.resultHeader}>
          <Text style={styles.resultTitle}>
            {kind === 'lunar_return_report' && '🌙 Lunar Return Report'}
            {kind === 'void_of_course' && '🌑 Void of Course'}
            {kind === 'lunar_mansion' && '🏰 Lunar Mansion'}
          </Text>
          {/* Badge MOCK uniquement en dev */}
          {isDev() && isMock && (
            <View style={styles.mockBadge}>
              <Text style={styles.mockBadgeText}>MOCK</Text>
            </View>
          )}
        </View>

        {/* Provider label uniquement en dev */}
        {isDev() && (
          <Text style={styles.provider}>Provider: {providerLabel}</Text>
        )}

        <View style={styles.summaryBox}>
          <Text style={styles.summaryTitle}>Résumé</Text>

          {/* Lunar Return Report */}
          {kind === 'lunar_return_report' && (
            <>
              {get(data, 'return_date') ? (
                <Text style={styles.summaryText}>
                  📅 Date de retour: {get(data, 'return_date')}
                </Text>
              ) : (
                <Text style={styles.summaryText}>
                  📅 Date de retour: —
                </Text>
              )}
              {get(data, 'moon.sign') ? (
                <Text style={styles.summaryText}>
                  🌙 Lune: {get(data, 'moon.sign')} {get(data, 'moon.degree') ? `(${Math.round(get(data, 'moon.degree'))}°)` : ''}
                </Text>
              ) : (
                <Text style={styles.summaryText}>
                  🌙 Lune: —
                </Text>
              )}
              {get(data, 'moon.house') && (
                <Text style={styles.summaryText}>
                  🏠 Maison: {get(data, 'moon.house')}
                </Text>
              )}
              {(isMock || get(data, 'interpretation')) && (
                <Text style={styles.summaryText} numberOfLines={2}>
                  💬 {cleanInterpretationText(get(data, 'interpretation', ''), isMock)}
                </Text>
              )}
            </>
          )}

          {/* Void of Course */}
          {kind === 'void_of_course' && (
            <>
              <Text style={styles.summaryText}>
                {get(data, 'is_void', false) ? '✅ Actif' : '❌ Inactif'}
              </Text>

              {get(data, 'is_void') && get(data, 'void_of_course') && (
                <>
                  <Text style={styles.summaryText}>
                    🕐 Début: {formatShortDateTime(get(data, 'void_of_course.start'))}
                  </Text>
                  <Text style={styles.summaryText}>
                    🕐 Fin: {formatShortDateTime(get(data, 'void_of_course.end'))}
                  </Text>
                </>
              )}

              {!get(data, 'is_void') && get(data, 'next_void') && (
                <>
                  <Text style={styles.summaryText}>
                    🔮 Prochain VoC:
                  </Text>
                  <Text style={styles.summaryText}>
                    🕐 Début: {formatShortDateTime(get(data, 'next_void.start'))}
                  </Text>
                  <Text style={styles.summaryText}>
                    🕐 Fin: {formatShortDateTime(get(data, 'next_void.end'))}
                  </Text>
                </>
              )}

              {get(data, 'moon_sign') && (
                <Text style={styles.summaryText}>
                  🌙 Signe lunaire: {get(data, 'moon_sign')}
                </Text>
              )}
            </>
          )}

          {/* Lunar Mansion */}
          {kind === 'lunar_mansion' && (
            <>
              {get(data, 'mansion.number') ? (
                <Text style={styles.summaryText}>
                  🏰 Mansion #{get(data, 'mansion.number')}: {get(data, 'mansion.name', '—')}
                </Text>
              ) : (
                <Text style={styles.summaryText}>
                  🏰 Mansion: Indisponible pour le moment
                </Text>
              )}

              {(isMock || get(data, 'mansion.interpretation')) && (
                <Text style={styles.summaryText} numberOfLines={2}>
                  💬 {cleanInterpretationText(get(data, 'mansion.interpretation'), isMock)}
                </Text>
              )}

              {get(data, 'upcoming_changes.0') && (
                <>
                  <Text style={styles.summaryText}>
                    🔄 Prochain changement:
                  </Text>
                  <Text style={styles.summaryText}>
                    🕐 {formatShortDateTime(get(data, 'upcoming_changes.0.change_time'))}
                  </Text>
                  {get(data, 'upcoming_changes.0.to_mansion.number') ? (
                    <Text style={styles.summaryText}>
                      ➡️ Mansion #{get(data, 'upcoming_changes.0.to_mansion.number')}: {get(data, 'upcoming_changes.0.to_mansion.name', '—')}
                    </Text>
                  ) : null}
                </>
              )}
            </>
          )}
        </View>

        {/* Bouton "Voir JSON" uniquement en dev */}
        {isDev() && (
          <>
            <TouchableOpacity
              style={styles.toggleButton}
              onPress={() => setShowRawJson(!showRawJson)}
            >
              <Text style={styles.toggleButtonText}>
                {showRawJson ? '📋 Masquer JSON' : '🔍 Voir JSON complet'}
              </Text>
            </TouchableOpacity>

            {showRawJson && (
              <ScrollView style={styles.jsonContainer}>
                <Text style={styles.jsonText}>
                  {JSON.stringify(result, null, 2)}
                </Text>
              </ScrollView>
            )}
          </>
        )}
      </View>
    );
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>🌙 Luna Pack</Text>
        <Text style={styles.subtitle}>
          Fonctionnalités lunaires avancées (P1)
        </Text>
      </View>

      <View style={styles.buttonsContainer}>
        <TouchableOpacity
          style={[styles.button, styles.buttonPrimary]}
          onPress={handleLunarReturnReport}
          disabled={loading}
        >
          <Text style={styles.buttonText}>🌙 Lunar Return Report</Text>
          <Text style={styles.buttonDescription}>
            Rapport mensuel complet de révolution lunaire
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.button, styles.buttonSecondary]}
          onPress={handleVoidOfCourse}
          disabled={loading}
        >
          <Text style={styles.buttonText}>🌑 Void of Course</Text>
          <Text style={styles.buttonDescription}>
            Période où la Lune ne fait plus d'aspects majeurs
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.button, styles.buttonTertiary]}
          onPress={handleLunarMansion}
          disabled={loading}
        >
          <Text style={styles.buttonText}>🏰 Lunar Mansion</Text>
          <Text style={styles.buttonDescription}>
            Mansion lunaire actuelle (système des 28)
          </Text>
        </TouchableOpacity>
      </View>

      {loading && (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="#8B7BF7" />
          <Text style={styles.loadingText}>Calcul en cours...</Text>
        </View>
      )}

      {renderSummary()}

      <View style={styles.infoBox}>
        <Text style={styles.infoTitle}>ℹ️ Info</Text>
        <Text style={styles.infoText}>
          Payload de test utilisé:
        </Text>
        <Text style={styles.infoText}>
          📍 Paris (48.8566, 2.3522)
        </Text>
        <Text style={styles.infoText}>
          📅 Date: {testPayload.date} à {testPayload.time}
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
  header: {
    padding: 20,
    paddingTop: 60,
    alignItems: 'center',
    backgroundColor: '#1A1F3E',
    borderBottomWidth: 2,
    borderBottomColor: '#8B7BF7',
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: '#A0A0B0',
  },
  buttonsContainer: {
    padding: 20,
    gap: 16,
  },
  button: {
    padding: 20,
    borderRadius: 12,
    borderWidth: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 5,
  },
  buttonPrimary: {
    backgroundColor: '#8B7BF7',
    borderColor: '#6A5AE0',
  },
  buttonSecondary: {
    backgroundColor: '#2D3561',
    borderColor: '#3D4571',
  },
  buttonTertiary: {
    backgroundColor: '#1E2947',
    borderColor: '#2E3957',
  },
  buttonText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 4,
  },
  buttonDescription: {
    fontSize: 13,
    color: '#C0C0D0',
  },
  loadingContainer: {
    alignItems: 'center',
    padding: 30,
  },
  loadingText: {
    marginTop: 12,
    fontSize: 16,
    color: '#8B7BF7',
  },
  resultContainer: {
    margin: 20,
    padding: 20,
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    borderWidth: 2,
    borderColor: '#8B7BF7',
  },
  resultHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  resultTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#FFFFFF',
    flex: 1,
  },
  mockBadge: {
    backgroundColor: 'rgba(139, 123, 247, 0.25)',
    borderWidth: 1,
    borderColor: 'rgba(139, 123, 247, 0.5)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 4,
    marginLeft: 8,
  },
  mockBadgeText: {
    fontSize: 10,
    fontWeight: '600',
    color: '#B794F6',
    letterSpacing: 0.5,
  },
  provider: {
    fontSize: 12,
    color: '#A0A0B0',
    marginBottom: 16,
  },
  summaryBox: {
    backgroundColor: '#0A0E27',
    padding: 16,
    borderRadius: 8,
    marginBottom: 16,
  },
  summaryTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#8B7BF7',
    marginBottom: 8,
  },
  summaryText: {
    fontSize: 14,
    color: '#C0C0D0',
    marginBottom: 6,
    lineHeight: 20,
  },
  toggleButton: {
    backgroundColor: '#2D3561',
    padding: 12,
    borderRadius: 8,
    alignItems: 'center',
    marginBottom: 12,
  },
  toggleButtonText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '600',
  },
  jsonContainer: {
    backgroundColor: '#0A0E27',
    padding: 12,
    borderRadius: 8,
    maxHeight: 300,
  },
  jsonText: {
    fontFamily: 'monospace',
    fontSize: 11,
    color: '#8B7BF7',
  },
  infoBox: {
    margin: 20,
    padding: 16,
    backgroundColor: '#1A1F3E',
    borderRadius: 8,
    borderLeftWidth: 4,
    borderLeftColor: '#8B7BF7',
  },
  infoTitle: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 8,
  },
  infoText: {
    fontSize: 13,
    color: '#A0A0B0',
    marginBottom: 4,
  },
});
