/**
 * Onboarding - Setup profil (prénom + date de naissance)
 */

import React, { useState, useRef, useEffect, useCallback } from 'react';
import { deduplicateLocations } from '../../utils/locationDedup';
import { rankLocationsByRelevance } from '../../utils/locationRanking';
import i18n from '../../i18n';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  TextInput,
  ScrollView,
  Alert,
  KeyboardAvoidingView,
  Platform,
  ActivityIndicator,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useOnboardingStore } from '../../stores/useOnboardingStore';
import { useNatalStore } from '../../stores/useNatalStore';
import { natalChart } from '../../services/api';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { goToNextOnboardingStep, goToPreviousOnboardingStep } from '../../services/onboardingFlow';
import { getOnboardingFlowState } from '../../utils/onboardingHelpers';
import { formatDateLocal } from '../../utils/date';
import { getBig3Preview } from '../../services/localAstroCalc';
import { Big3Preview } from '../../components/onboarding/Big3Preview';
import { DateWheelPicker } from '../../components/onboarding/DateWheelPicker';
import { TimeWheelPicker } from '../../components/onboarding/TimeWheelPicker';

// Type pour une suggestion Nominatim
interface NominatimPlace {
  display_name: string;
  lat: string;
  lon: string;
  address?: {
    city?: string;
    town?: string;
    village?: string;
    municipality?: string;
    hamlet?: string;
    state?: string;
    region?: string;
    county?: string;
    state_district?: string;
    country?: string;
  };
}

// Type pour le lieu sélectionné
interface SelectedPlace {
  displayName: string;
  latitude: number;
  longitude: number;
}

export default function ProfileSetupScreen() {
  const router = useRouter();
  const onboardingStore = useOnboardingStore();
  const { setProfileData, profileData } = onboardingStore;
  const natalStore = useNatalStore();
  const { setChart, isCacheFresh, isCalculating: isNatalCalculating, setIsCalculating } = natalStore;

  const [name, setName] = useState(profileData?.name || '');
  const [birthDate, setBirthDate] = useState<Date>(
    profileData?.birthDate || new Date(2000, 0, 1)
  );
  const [birthTime, setBirthTime] = useState(profileData?.birthTime || '12:00');
  const [placeInput, setPlaceInput] = useState(profileData?.birthPlace || '');
  const [selectedPlace, setSelectedPlace] = useState<SelectedPlace | null>(
    profileData?.birthLatitude && profileData?.birthLongitude && profileData?.birthPlace
      ? {
          displayName: profileData.birthPlace,
          latitude: profileData.birthLatitude,
          longitude: profileData.birthLongitude,
        }
      : null
  );
  const [suggestions, setSuggestions] = useState<NominatimPlace[]>([]);
  const [isLoadingSuggestions, setIsLoadingSuggestions] = useState(false);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [natalCalculationError, setNatalCalculationError] = useState<string | null>(null);

  // In-flight guard to prevent double submission
  const isSubmittingRef = useRef(false);
  // Ref pour le timer de debounce
  const debounceTimerRef = useRef<NodeJS.Timeout | null>(null);

  // Fonction pour rechercher des suggestions via Nominatim
  const searchPlaces = useCallback(async (query: string) => {
    if (query.length < 3) {
      setSuggestions([]);
      setShowSuggestions(false);
      return;
    }

    setIsLoadingSuggestions(true);
    try {
      const url = `https://nominatim.openstreetmap.org/search?format=json&limit=5&q=${encodeURIComponent(query)}&accept-language=fr&addressdetails=1`;
      
      const response = await fetch(url, {
        headers: {
          'User-Agent': 'AstroiaLunar/1.0 (mobile)',
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const data: NominatimPlace[] = await response.json();
      const deduplicated = deduplicateLocations(data);
      const ranked = rankLocationsByRelevance(deduplicated, i18n.language);
      setSuggestions(ranked);
      setShowSuggestions(ranked.length > 0);
    } catch (error) {
      console.warn('[PROFILE-SETUP] Erreur recherche Nominatim:', error);
      setSuggestions([]);
      setShowSuggestions(false);
    } finally {
      setIsLoadingSuggestions(false);
    }
  }, []);

  // Debounce de la recherche (350ms)
  const handlePlaceInputChange = useCallback((text: string) => {
    setPlaceInput(text);
    // Si l'utilisateur modifie le texte après sélection, réinitialiser selectedPlace
    if (selectedPlace) {
      setSelectedPlace(null);
    }

    // Nettoyer le timer précédent
    if (debounceTimerRef.current) {
      clearTimeout(debounceTimerRef.current);
    }

    // Nouveau timer
    debounceTimerRef.current = setTimeout(() => {
      searchPlaces(text);
    }, 350);
  }, [selectedPlace, searchPlaces]);

  // Nettoyer le timer au unmount
  useEffect(() => {
    return () => {
      if (debounceTimerRef.current) {
        clearTimeout(debounceTimerRef.current);
      }
    };
  }, []);

  // Sélectionner une suggestion
  const handleSelectPlace = (place: NominatimPlace) => {
    const displayName = formatPlaceLabel(place);

    setSelectedPlace({
      displayName,
      latitude: parseFloat(place.lat),
      longitude: parseFloat(place.lon),
    });
    setPlaceInput(displayName);
    setShowSuggestions(false);
    setSuggestions([]);
  };

  const handleNext = async () => {
    // Guard: prevent double submission
    if (isSubmittingRef.current) {
      console.log('[PROFILE-SETUP] ⏸️ Soumission déjà en cours, skip double-click');
      return;
    }

    // Validation
    if (!name.trim()) {
      Alert.alert('Nom requis', "Merci d'entrer ton prénom");
      return;
    }

    if (!placeInput.trim()) {
      Alert.alert('Lieu requis', 'Merci d\'entrer ton lieu de naissance');
      return;
    }

    // Validation: l'utilisateur doit avoir sélectionné une suggestion
    if (!selectedPlace) {
      Alert.alert(
        'Ville requise',
        'Merci de choisir une ville dans la liste de suggestions'
      );
      return;
    }

    if (!birthTime.trim()) {
      Alert.alert('Heure requise', "Merci d'entrer ton heure de naissance");
      return;
    }

    // Mark as submitting
    isSubmittingRef.current = true;
    setIsSubmitting(true);

    try {
      // Sauvegarder le profil complet avec coordonnées (sans timezone)
      await setProfileData({
        name: name.trim(),
        birthDate,
        birthTime: birthTime.trim(),
        birthPlace: selectedPlace.displayName,
        birthLatitude: selectedPlace.latitude,
        birthLongitude: selectedPlace.longitude,
        // birthTimezone supprimé - sera auto-détecté par le backend
      });

      console.log('[PROFILE-SETUP] ✅ Profil sauvegardé (hasCompletedProfile=true)');

      // Calculer le thème natal automatiquement (BLOQUANT avec UI)
      // IMPORTANT: Toujours recalculer car les données de naissance peuvent avoir changé
      try {
        setNatalCalculationError(null); // Reset error state

        // Guard: Vérifier si un calcul est déjà en cours
        if (isNatalCalculating) {
          console.log('[PROFILE-SETUP] 🔒 Calcul natal déjà en cours, skip duplicate request');
        } else {
          // Invalider le cache car les données de profil peuvent avoir changé
          console.log('[PROFILE-SETUP] 🗑️ Invalidation du cache natal (profil modifié)');
          natalStore.clearChart();
          // Cache MISS ou expiré → appeler l'API (BLOQUANT)
          console.log('[PROFILE-SETUP] 🌟 Calcul du thème natal (API réelle)...');
          setIsCalculating(true);

          const formattedDate = formatDateLocal(birthDate);

          const response = await natalChart.calculate({
            date: formattedDate, // YYYY-MM-DD en heure locale (pas UTC!)
            time: birthTime.trim(),
            latitude: selectedPlace.latitude,
            longitude: selectedPlace.longitude,
            place_name: selectedPlace.displayName,
            // timezone supprimé - sera auto-détecté par le backend
          });

          setChart(response); // Stocke le chart + timestamp
          setIsCalculating(false);
          console.log('[PROFILE-SETUP] ✅ Thème natal calculé et mis en cache');
        }

        // Naviguer vers la prochaine étape SEULEMENT si calcul réussi
        await goToNextOnboardingStep(router, 'PROFILE-SETUP', getOnboardingFlowState);
      } catch (natalError: any) {
        // Bloquer l'onboarding ET afficher erreur + bouton retry
        console.error('[PROFILE-SETUP] ❌ Échec calcul natal (BLOQUANT):', natalError.message);
        setIsCalculating(false);
        setNatalCalculationError(
          natalError.message || 'Erreur lors du calcul de ton thème natal. Vérifie ta connexion et réessaie.'
        );
        // NE PAS naviguer - rester sur cet écran pour retry
        return; // Exit early
      }
    } catch (error: any) {
      console.error('[PROFILE-SETUP] Erreur:', error);
      Alert.alert('Erreur', error.message || 'Impossible de sauvegarder le profil');

      // Reset guard on error to allow retry
      isSubmittingRef.current = false;
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleBack = () => {
    goToPreviousOnboardingStep(router, 'PROFILE-SETUP');
  };

  // Formater le label d'une suggestion : "Ville, Région, Pays"
  const formatPlaceLabel = (place: NominatimPlace): string => {
    if (place.address) {
      // Extraire la ville (priorité: city > town > village > municipality > hamlet)
      const cityName =
        place.address.city ||
        place.address.town ||
        place.address.village ||
        place.address.municipality ||
        place.address.hamlet ||
        '';

      // Extraire la région (priorité: state > region > county > state_district)
      const regionName =
        place.address.state ||
        place.address.region ||
        place.address.county ||
        place.address.state_district ||
        '';

      // Extraire le pays
      const countryName = place.address.country || '';

      // Construire le label : "Ville, Région, Pays" (région optionnelle)
      const parts: string[] = [];
      if (cityName) parts.push(cityName);
      if (regionName) parts.push(regionName);
      if (countryName) parts.push(countryName);

      if (parts.length > 0) {
        return parts.join(', ');
      }
    }

    // Fallback : parser display_name si address absent ou non exploitable
    // Format typique : "Ville, Région, Pays, ..."
    const displayParts = place.display_name.split(',').map((s) => s.trim());
    if (displayParts.length >= 2) {
      // Prendre les 2-3 premières parties (Ville, Région?, Pays)
      const fallback = displayParts.slice(0, Math.min(3, displayParts.length)).join(', ');
      // Tronquer à 70 caractères max si trop long
      return fallback.length > 70 ? fallback.substring(0, 67) + '...' : fallback;
    }

    // Dernier fallback : tronquer display_name brut
    const truncated = place.display_name.length > 70
      ? place.display_name.substring(0, 67) + '...'
      : place.display_name;
    return truncated;
  };

  return (
    <LinearGradient
      colors={colors.darkBg}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        <KeyboardAvoidingView
          behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
          style={styles.keyboardView}
        >
          {/* Header */}
          <View style={styles.header}>
            <TouchableOpacity onPress={handleBack} style={styles.backButton}>
              <Text style={styles.backText}>←</Text>
            </TouchableOpacity>
            <View style={styles.progressContainer}>
              <View style={styles.progressBar}>
                <View style={[styles.progressFill, { width: '50%' }]} />
              </View>
              <Text style={styles.headerTitle}>Étape 2/4</Text>
            </View>
            <View style={{ width: 40 }} />
          </View>

          <ScrollView
            contentContainerStyle={styles.scrollContent}
            showsVerticalScrollIndicator={false}
            keyboardShouldPersistTaps="handled"
          >
            {/* Title */}
            <Text style={styles.title}>Créons ton profil</Text>
            <Text style={styles.subtitle}>
              Ces informations nous permettront de personnaliser ton expérience Lunation
            </Text>

            {/* Big 3 Preview - Real-time feedback */}
            {(() => {
              const preview = getBig3Preview(
                birthDate,
                birthTime,
                selectedPlace?.latitude,
                selectedPlace?.longitude
              );
              return (
                <View style={styles.big3PreviewContainer}>
                  <Big3Preview
                    sunSign={preview.sunSign}
                    moonSign={preview.moonSign}
                    ascendant={preview.ascendant}
                    sunPlaceholder={preview.sunPlaceholder}
                    moonPlaceholder={preview.moonPlaceholder}
                    ascendantPlaceholder={preview.ascendantPlaceholder}
                    compact={true}
                  />
                </View>
              );
            })()}

            {/* Form */}
            <View style={styles.form}>
              {/* Date de naissance - EN PREMIER pour voir le Soleil bouger */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>Date de naissance</Text>
                <DateWheelPicker
                  value={birthDate}
                  onChange={setBirthDate}
                  minYear={1920}
                  maxYear={new Date().getFullYear()}
                />
              </View>

              {/* Heure de naissance - pour l'Ascendant */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>Heure de naissance</Text>
                <View style={styles.timePickerContainer}>
                  <TimeWheelPicker
                    value={birthTime}
                    onChange={setBirthTime}
                  />
                  <Text style={styles.timePickerHint}>
                    Nécessaire pour calculer ton Ascendant. Si inconnue, laisse 12:00
                  </Text>
                </View>
              </View>

              {/* Lieu de naissance - pour l'Ascendant */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>Lieu de naissance</Text>
                <View style={styles.autocompleteContainer}>
                  <TextInput
                    style={styles.input}
                    placeholder="Ex: Paris, France"
                    placeholderTextColor="rgba(255,255,255,0.4)"
                    value={placeInput}
                    onChangeText={handlePlaceInputChange}
                    autoCapitalize="words"
                    onFocus={() => {
                      if (suggestions.length > 0) {
                        setShowSuggestions(true);
                      }
                    }}
                  />
                  {isLoadingSuggestions && (
                    <View style={styles.loadingIndicator}>
                      <ActivityIndicator size="small" color={colors.accent} />
                    </View>
                  )}
                  {showSuggestions && suggestions.length > 0 && (
                    <View style={styles.suggestionsContainer}>
                      {suggestions.map((item, index) => (
                        <TouchableOpacity
                          key={`${item.lat}-${item.lon}-${index}`}
                          style={styles.suggestionItem}
                          onPress={() => handleSelectPlace(item)}
                        >
                          <Text style={styles.suggestionLabel}>
                            {formatPlaceLabel(item)}
                          </Text>
                          <Text style={styles.suggestionSubLabel} numberOfLines={1}>
                            {item.display_name}
                          </Text>
                        </TouchableOpacity>
                      ))}
                    </View>
                  )}
                </View>
              </View>

              {/* Prénom */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>Prénom</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Ex: Marie"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={name}
                  onChangeText={setName}
                  autoCapitalize="words"
                  autoCorrect={false}
                />
              </View>

              {/* Info box */}
              <View style={styles.infoBox}>
                <Text style={styles.infoIcon}>ℹ️</Text>
                <Text style={styles.infoText}>
                  Ces informations nous permettent de calculer ton thème natal complet pour des
                  prévisions personnalisées. Le fuseau horaire est détecté automatiquement.
                </Text>
              </View>
            </View>
          </ScrollView>

          {/* Footer */}
          <View style={styles.footer}>
            <TouchableOpacity
              style={[styles.nextButton, isSubmitting && styles.nextButtonDisabled]}
              onPress={handleNext}
              activeOpacity={0.8}
              disabled={isSubmitting}
            >
              <LinearGradient
                colors={[colors.accent, colors.accentDark || colors.accent]}
                style={styles.nextButtonGradient}
                start={{ x: 0, y: 0 }}
                end={{ x: 1, y: 0 }}
              >
                {isSubmitting ? (
                  <ActivityIndicator color={colors.text} />
                ) : (
                  <Text style={styles.nextButtonText}>Suivant</Text>
                )}
              </LinearGradient>
            </TouchableOpacity>
          </View>
        </KeyboardAvoidingView>

        {/* Overlay de chargement pour calcul natal */}
        {isNatalCalculating && (
          <View style={styles.natalLoadingOverlay}>
            <View style={styles.natalLoadingContent}>
              <ActivityIndicator size="large" color={colors.accent} />
              <Text style={styles.natalLoadingTitle}>Calcul de ton thème natal...</Text>
              <Text style={styles.natalLoadingSubtitle}>
                Nous interrogeons les astres pour toi ✨
              </Text>
            </View>
          </View>
        )}

        {/* Modal d'erreur pour calcul natal */}
        {natalCalculationError && !isNatalCalculating && (
          <View style={styles.natalErrorOverlay}>
            <View style={styles.natalErrorContent}>
              <Text style={styles.natalErrorIcon}>⚠️</Text>
              <Text style={styles.natalErrorTitle}>Erreur</Text>
              <Text style={styles.natalErrorMessage}>{natalCalculationError}</Text>
              <TouchableOpacity
                style={styles.natalErrorRetryButton}
                onPress={() => {
                  setNatalCalculationError(null);
                  handleNext(); // Retry submit
                }}
              >
                <Text style={styles.natalErrorRetryText}>Réessayer</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}
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
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  progressContainer: {
    alignItems: 'center',
    gap: spacing.xs,
  },
  progressBar: {
    width: 120,
    height: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    borderRadius: 2,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: colors.accent,
    borderRadius: 2,
  },
  backButton: {
    width: 40,
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
  },
  backText: {
    fontSize: 24,
    color: colors.text,
  },
  headerTitle: {
    color: 'rgba(255, 255, 255, 0.7)',
    fontSize: fonts.sizes.md,
    fontWeight: '600',
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.xl,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.sm,
    marginTop: spacing.lg,
    textShadowColor: 'rgba(183, 148, 246, 0.5)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 10,
  },
  subtitle: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.7)',
    marginBottom: spacing.lg,
    lineHeight: 22,
  },
  big3PreviewContainer: {
    marginBottom: spacing.xl,
  },
  form: {
    gap: spacing.lg,
  },
  inputGroup: {
    gap: spacing.sm,
  },
  label: {
    fontSize: fonts.sizes.md,
    color: colors.accent,
    fontWeight: '600',
  },
  input: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    fontSize: fonts.sizes.lg,
    color: colors.text,
    borderWidth: 2,
    borderColor: 'rgba(183, 148, 246, 0.3)',
  },
  autocompleteContainer: {
    position: 'relative',
    zIndex: 10,
  },
  loadingIndicator: {
    position: 'absolute',
    right: spacing.md,
    top: spacing.md + 2,
  },
  suggestionsContainer: {
    position: 'absolute',
    top: '100%',
    left: 0,
    right: 0,
    marginTop: spacing.xs,
    backgroundColor: 'rgba(20, 20, 30, 0.98)',
    borderRadius: borderRadius.md,
    borderWidth: 2,
    borderColor: 'rgba(183, 148, 246, 0.3)',
    maxHeight: 200,
    zIndex: 1000,
    elevation: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
  },
  suggestionItem: {
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(183, 148, 246, 0.1)',
  },
  suggestionLabel: {
    fontSize: fonts.sizes.md,
    color: colors.text,
    fontWeight: '600',
    marginBottom: spacing.xs,
  },
  suggestionSubLabel: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.6)',
  },
  timePickerContainer: {
    alignItems: 'center',
  },
  timePickerHint: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.5)',
    marginTop: spacing.sm,
    textAlign: 'center',
    fontStyle: 'italic',
  },
  infoBox: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: spacing.sm,
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.3)',
    marginTop: spacing.md,
  },
  infoIcon: {
    fontSize: 20,
  },
  infoText: {
    flex: 1,
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.8)',
    lineHeight: 20,
  },
  footer: {
    paddingHorizontal: spacing.xl,
    paddingBottom: spacing.lg,
  },
  nextButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
  },
  nextButtonGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: spacing.md + 4,
    gap: spacing.sm,
  },
  nextButtonText: {
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
  nextButtonDisabled: {
    opacity: 0.6,
  },
  // Overlay natal calculation
  natalLoadingOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(10, 14, 39, 0.95)',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 9999,
  },
  natalLoadingContent: {
    alignItems: 'center',
    paddingHorizontal: spacing.xl,
  },
  natalLoadingTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: colors.text,
    marginTop: spacing.lg,
    textAlign: 'center',
  },
  natalLoadingSubtitle: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.7)',
    marginTop: spacing.sm,
    textAlign: 'center',
  },
  // Overlay natal error
  natalErrorOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(10, 14, 39, 0.95)',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 9999,
  },
  natalErrorContent: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: borderRadius.lg,
    padding: spacing.xl,
    marginHorizontal: spacing.xl,
    alignItems: 'center',
    borderWidth: 2,
    borderColor: 'rgba(255, 107, 107, 0.5)',
  },
  natalErrorIcon: {
    fontSize: 48,
    marginBottom: spacing.md,
  },
  natalErrorTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.sm,
  },
  natalErrorMessage: {
    fontSize: fonts.sizes.md,
    color: 'rgba(255, 255, 255, 0.8)',
    textAlign: 'center',
    marginBottom: spacing.lg,
    lineHeight: 22,
  },
  natalErrorRetryButton: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.xl,
    borderRadius: borderRadius.md,
  },
  natalErrorRetryText: {
    fontSize: fonts.sizes.lg,
    fontWeight: '700',
    color: colors.text,
  },
});
