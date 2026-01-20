/**
 * Écran Thème Natal - MVP
 * 
 * Flow:
 * 1. Au chargement → GET /api/natal-chart (avec RequestGuard)
 * 2. Si 404 → afficher formulaire minimal "Créer mon thème natal"
 * 3. Si 200/201 → naviguer vers /natal-chart/result
 * 4. Si 502/503 → afficher message + bouton retry
 * 5. Sur submit formulaire → POST /api/natal-chart
 */

import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  TextInput,
  KeyboardAvoidingView,
  Platform,
  Alert,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useNatalStore } from '../../stores/useNatalStore';
import { natalChart } from '../../services/api';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { guardedRequest } from '../../utils/requestGuard';

export default function NatalChartIndexScreen() {
  const router = useRouter();
  const { chart, setChart, setLoading, loading } = useNatalStore();
  
  // États pour le chargement initial
  const [isCheckingChart, setIsCheckingChart] = useState(true);
  const [hasExistingChart, setHasExistingChart] = useState(false);
  const [networkError, setNetworkError] = useState<{ status?: number; message: string } | null>(null);
  
  // États pour le formulaire
  const [showForm, setShowForm] = useState(false);
  const [formDate, setFormDate] = useState('');
  const [formTime, setFormTime] = useState('');
  const [formPlaceName, setFormPlaceName] = useState('');
  const [formLat, setFormLat] = useState('');
  const [formLon, setFormLon] = useState('');
  const [formTimezone, setFormTimezone] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  
  // Guard anti-boucle pour le chargement initial
  const hasCheckedRef = useRef(false);

  // Chargement initial: GET /api/natal-chart
  useEffect(() => {
    if (hasCheckedRef.current) {
      console.log('[NATAL-CHART] ⏸️ Chargement déjà effectué, skip');
      return;
    }

    const loadExistingChart = async () => {
      console.log('[NATAL-CHART] 🔍 Vérification thème natal existant...');
      hasCheckedRef.current = true;
      setIsCheckingChart(true);
      setNetworkError(null);

      try {
        // Utiliser RequestGuard pour éviter les doublons et les boucles
        const response = await guardedRequest(
          'natal-chart/get',
          async () => {
            console.log('[NATAL-CHART] 📡 GET /api/natal-chart');
            return await natalChart.get();
          },
          { ttl: 60000 } // Cache 60s
        );

        console.log('[NATAL-CHART] ✅ Thème natal trouvé, navigation vers result');
        setChart(response);
        setHasExistingChart(true);
        
        // Naviguer vers l'écran résultat
        router.replace('/natal-chart/result');
      } catch (error: any) {
        const status = error.response?.status;
        console.log(`[NATAL-CHART] 📭 GET /api/natal-chart → ${status || 'error'}`);

        if (status === 404) {
          // 404 = pas de thème natal, afficher le formulaire
          console.log('[NATAL-CHART] 📝 Aucun thème natal, affichage formulaire');
          setShowForm(true);
        } else if (status === 502 || status === 503) {
          // Erreur réseau (502 Bad Gateway, 503 Service Unavailable)
          console.error('[NATAL-CHART] ❌ Erreur réseau:', status);
          setNetworkError({
            status,
            message: 'Le serveur n\'est pas disponible pour le moment. Veuillez réessayer.',
          });
        } else {
          // Autre erreur
          console.error('[NATAL-CHART] ❌ Erreur:', error.message);
          setNetworkError({
            message: error.response?.data?.detail || error.message || 'Erreur lors du chargement',
          });
        }
      } finally {
        setIsCheckingChart(false);
      }
    };

    loadExistingChart();
  }, [router, setChart]);

  // Handler pour retry après erreur réseau
  const handleRetry = () => {
    console.log('[NATAL-CHART] 🔄 Retry après erreur réseau');
    hasCheckedRef.current = false;
    setNetworkError(null);
    setIsCheckingChart(true);
    
    // Relancer le chargement
    const loadExistingChart = async () => {
      try {
        const response = await guardedRequest(
          'natal-chart/get',
          async () => {
            console.log('[NATAL-CHART] 📡 GET /api/natal-chart (retry)');
            return await natalChart.get();
          },
          { ttl: 60000, forceRefresh: true } // Force refresh pour bypass cache
        );

        console.log('[NATAL-CHART] ✅ Thème natal trouvé (retry)');
        setChart(response);
        setHasExistingChart(true);
        router.replace('/natal-chart/result');
      } catch (error: any) {
        const status = error.response?.status;
        if (status === 404) {
          setShowForm(true);
        } else if (status === 502 || status === 503) {
          setNetworkError({
            status,
            message: 'Le serveur n\'est pas disponible pour le moment. Veuillez réessayer.',
          });
        } else {
          setNetworkError({
            message: error.response?.data?.detail || error.message || 'Erreur lors du chargement',
          });
        }
      } finally {
        setIsCheckingChart(false);
      }
    };

    loadExistingChart();
  };

  // Handler pour submit du formulaire
  const handleSubmit = async () => {
    // Validation
    if (!formDate.trim()) {
      Alert.alert('Erreur', 'Veuillez entrer une date de naissance (YYYY-MM-DD)');
      return;
    }
    if (!formTime.trim()) {
      Alert.alert('Erreur', 'Veuillez entrer une heure de naissance (HH:MM)');
      return;
    }
    if (!formPlaceName.trim()) {
      Alert.alert('Erreur', 'Veuillez entrer un lieu de naissance');
      return;
    }
    if (!formLat.trim() || !formLon.trim()) {
      Alert.alert('Erreur', 'Veuillez entrer les coordonnées (latitude et longitude)');
      return;
    }

    const latitude = parseFloat(formLat);
    const longitude = parseFloat(formLon);

    if (isNaN(latitude) || isNaN(longitude)) {
      Alert.alert('Erreur', 'Coordonnées invalides. Utilisez des nombres décimaux.');
      return;
    }

    setIsSubmitting(true);
    setLoading(true);
    setNetworkError(null);

    try {
      console.log('[NATAL-CHART] 📤 POST /api/natal-chart');
      const payload: {
        date: string;
        time: string;
        latitude: number;
        longitude: number;
        place_name: string;
        timezone?: string;
      } = {
        date: formDate.trim(),
        time: formTime.trim(),
        latitude,
        longitude,
        place_name: formPlaceName.trim(),
      };

      // Ajouter timezone si fourni (optionnel)
      if (formTimezone.trim()) {
        payload.timezone = formTimezone.trim();
      }

      const response = await natalChart.calculate(payload);

      console.log('[NATAL-CHART] ✅ Thème natal calculé avec succès');
      setChart(response);

      // Naviguer vers l'écran résultat
      router.replace('/natal-chart/result');
    } catch (error: any) {
      console.error('[NATAL-CHART] ❌ Erreur calcul thème natal:', error);
      const status = error.response?.status;

      if (status === 502 || status === 503) {
        setNetworkError({
          status,
          message: 'Le serveur n\'est pas disponible pour le moment. Veuillez réessayer.',
        });
      } else {
        const errorMessage = error.response?.data?.detail || error.message || 'Impossible de calculer le thème natal';
        Alert.alert('Erreur', errorMessage);
      }
    } finally {
      setIsSubmitting(false);
      setLoading(false);
    }
  };

  // Écran de chargement initial
  if (isCheckingChart) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
          <View style={styles.centerContainer}>
            <ActivityIndicator size="large" color={colors.accent} />
            <Text style={styles.loadingText}>Chargement...</Text>
          </View>
        </SafeAreaView>
      </LinearGradient>
    );
  }

  // Écran d'erreur réseau avec retry
  if (networkError && !showForm) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
          <View style={styles.header}>
            <TouchableOpacity
              onPress={() => router.back()}
              style={styles.backButton}
              hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
            >
              <Text style={styles.backText}>← Retour</Text>
            </TouchableOpacity>
          </View>
          <View style={styles.centerContainer}>
            <Text style={styles.errorEmoji}>⚠️</Text>
            <Text style={styles.errorTitle}>Erreur de connexion</Text>
            <Text style={styles.errorMessage}>{networkError.message}</Text>
            <TouchableOpacity
              style={styles.retryButton}
              onPress={handleRetry}
              activeOpacity={0.8}
            >
              <LinearGradient
                colors={[colors.accent, colors.accentDark || colors.accent]}
                style={styles.retryButtonGradient}
              >
                <Text style={styles.retryButtonText}>Réessayer</Text>
              </LinearGradient>
            </TouchableOpacity>
          </View>
        </SafeAreaView>
      </LinearGradient>
    );
  }

  // Formulaire "Créer mon thème natal"
  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        <KeyboardAvoidingView
          behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
          style={styles.keyboardView}
        >
          <View style={styles.header}>
            <TouchableOpacity
              onPress={() => router.back()}
              style={styles.backButton}
              hitSlop={{ top: 20, bottom: 20, left: 20, right: 20 }}
            >
              <Text style={styles.backText}>← Retour</Text>
            </TouchableOpacity>
          </View>

          <ScrollView
            contentContainerStyle={styles.scrollContent}
            showsVerticalScrollIndicator={false}
            keyboardShouldPersistTaps="handled"
          >
            {/* Titre */}
            <View style={styles.titleSection}>
              <Text style={styles.emoji}>⭐</Text>
              <Text style={styles.title}>Créer mon thème natal</Text>
              <Text style={styles.subtitle}>
                Remplis les informations suivantes pour calculer ton thème natal
              </Text>
            </View>

            {/* Message d'erreur réseau dans le formulaire */}
            {networkError && (
              <View style={styles.errorBox}>
                <Text style={styles.errorBoxText}>{networkError.message}</Text>
                <TouchableOpacity onPress={handleRetry} style={styles.errorRetryButton}>
                  <Text style={styles.errorRetryText}>Réessayer</Text>
                </TouchableOpacity>
              </View>
            )}

            {/* Formulaire */}
            <View style={styles.formCard}>
              {/* Date */}
              <View style={styles.inputGroup}>
                <Text style={styles.inputLabel}>Date de naissance *</Text>
                <TextInput
                  style={styles.input}
                  placeholder="YYYY-MM-DD (ex: 1990-01-15)"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={formDate}
                  onChangeText={setFormDate}
                  autoCapitalize="none"
                  keyboardType="default"
                />
                <Text style={styles.inputHint}>Format: YYYY-MM-DD</Text>
              </View>

              {/* Heure */}
              <View style={styles.inputGroup}>
                <Text style={styles.inputLabel}>Heure de naissance *</Text>
                <TextInput
                  style={styles.input}
                  placeholder="HH:MM (ex: 14:30)"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={formTime}
                  onChangeText={setFormTime}
                  autoCapitalize="none"
                  keyboardType="numbers-and-punctuation"
                />
                <Text style={styles.inputHint}>Format: HH:MM (24h)</Text>
              </View>

              {/* Lieu */}
              <View style={styles.inputGroup}>
                <Text style={styles.inputLabel}>Lieu de naissance *</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Ex: Paris, France"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={formPlaceName}
                  onChangeText={setFormPlaceName}
                  autoCapitalize="words"
                />
                <Text style={styles.inputHint}>Ville, Pays</Text>
              </View>

              {/* Latitude */}
              <View style={styles.inputGroup}>
                <Text style={styles.inputLabel}>Latitude *</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Ex: 48.8566"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={formLat}
                  onChangeText={setFormLat}
                  autoCapitalize="none"
                  keyboardType="decimal-pad"
                />
              </View>

              {/* Longitude */}
              <View style={styles.inputGroup}>
                <Text style={styles.inputLabel}>Longitude *</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Ex: 2.3522"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={formLon}
                  onChangeText={setFormLon}
                  autoCapitalize="none"
                  keyboardType="decimal-pad"
                />
              </View>

              {/* Timezone (optionnel) */}
              <View style={styles.inputGroup}>
                <Text style={styles.inputLabel}>Timezone (optionnel)</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Ex: Europe/Paris"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={formTimezone}
                  onChangeText={setFormTimezone}
                  autoCapitalize="none"
                />
                <Text style={styles.inputHint}>Laissé vide pour auto-détection</Text>
              </View>

              {/* Bouton Submit */}
              <TouchableOpacity
                style={[styles.submitButton, (isSubmitting || loading) && styles.submitButtonDisabled]}
                onPress={handleSubmit}
                disabled={isSubmitting || loading}
                activeOpacity={0.8}
              >
                <LinearGradient
                  colors={[colors.accent, colors.accentDark || colors.accent]}
                  style={styles.submitButtonGradient}
                >
                  {isSubmitting || loading ? (
                    <ActivityIndicator color={colors.text} />
                  ) : (
                    <Text style={styles.submitButtonText}>Calculer mon thème natal ✨</Text>
                  )}
                </LinearGradient>
              </TouchableOpacity>
            </View>
          </ScrollView>
        </KeyboardAvoidingView>
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  keyboardView: {
    flex: 1,
  },
  header: {
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.md,
    paddingBottom: spacing.sm,
  },
  backButton: {
    marginBottom: spacing.sm,
  },
  backText: {
    ...fonts.body,
    color: colors.accent,
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: spacing.xl,
  },
  loadingText: {
    ...fonts.body,
    color: colors.textMuted,
    marginTop: spacing.md,
  },
  errorEmoji: {
    fontSize: 64,
    marginBottom: spacing.md,
  },
  errorTitle: {
    ...fonts.h2,
    color: colors.text,
    marginBottom: spacing.md,
    textAlign: 'center',
  },
  errorMessage: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    marginBottom: spacing.xl,
  },
  retryButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
  },
  retryButtonGradient: {
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.xl,
    alignItems: 'center',
    justifyContent: 'center',
  },
  retryButtonText: {
    ...fonts.button,
    color: colors.text,
    fontWeight: 'bold',
  },
  scrollContent: {
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.xl,
  },
  titleSection: {
    alignItems: 'center',
    marginBottom: spacing.xl,
    marginTop: spacing.md,
  },
  emoji: {
    fontSize: 64,
    marginBottom: spacing.sm,
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    marginBottom: spacing.xs,
    textAlign: 'center',
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    paddingHorizontal: spacing.md,
  },
  errorBox: {
    backgroundColor: 'rgba(255, 193, 7, 0.15)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(255, 193, 7, 0.3)',
  },
  errorBoxText: {
    ...fonts.bodySmall,
    color: 'rgba(255, 193, 7, 0.9)',
    marginBottom: spacing.sm,
  },
  errorRetryButton: {
    alignSelf: 'flex-start',
    paddingVertical: spacing.xs,
    paddingHorizontal: spacing.md,
  },
  errorRetryText: {
    ...fonts.bodySmall,
    color: 'rgba(255, 193, 7, 0.9)',
    fontWeight: '600',
  },
  formCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
  },
  inputGroup: {
    marginBottom: spacing.lg,
  },
  inputLabel: {
    ...fonts.bodySmall,
    color: colors.accent,
    fontWeight: '600',
    marginBottom: spacing.xs,
  },
  input: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    fontSize: fonts.sizes.md,
    color: colors.text,
    borderWidth: 2,
    borderColor: 'rgba(183, 148, 246, 0.3)',
  },
  inputHint: {
    ...fonts.caption,
    color: colors.textMuted,
    marginTop: spacing.xs,
    fontSize: 12,
  },
  submitButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    marginTop: spacing.md,
  },
  submitButtonDisabled: {
    opacity: 0.6,
  },
  submitButtonGradient: {
    paddingVertical: spacing.md + 4,
    alignItems: 'center',
    justifyContent: 'center',
  },
  submitButtonText: {
    ...fonts.button,
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
});
