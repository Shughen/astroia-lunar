/**
 * Onboarding - Setup profil (prénom + date de naissance)
 */

import React, { useState, useRef, useEffect, useCallback } from 'react';
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
import { goToNextOnboardingStep } from '../../services/onboardingFlow';
import { getOnboardingFlowState } from '../../utils/onboardingHelpers';

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
  const [showDatePicker, setShowDatePicker] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

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
      setSuggestions(data);
      setShowSuggestions(data.length > 0);
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
      Alert.alert('Nom requis', 'Veuillez entrer votre prénom');
      return;
    }

    if (!placeInput.trim()) {
      Alert.alert('Lieu requis', 'Veuillez entrer votre lieu de naissance');
      return;
    }

    // Validation: l'utilisateur doit avoir sélectionné une suggestion
    if (!selectedPlace) {
      Alert.alert(
        'Ville requise',
        'Veuillez choisir une ville dans la liste de suggestions'
      );
      return;
    }

    if (!birthTime.trim()) {
      Alert.alert('Heure requise', 'Veuillez entrer votre heure de naissance');
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

      // Calculer le thème natal automatiquement (NON BLOQUANT) avec cache + in-flight guard
      try {
        // Guard 1: Vérifier si un calcul est déjà en cours
        if (isNatalCalculating) {
          console.log('[PROFILE-SETUP] 🔒 Calcul natal déjà en cours, skip duplicate request');
        } else if (isCacheFresh()) {
          // Guard 2: Vérifier si le cache est frais (< 10 min)
          console.log('[PROFILE-SETUP] 🎯 Cache natal frais, skip API call');
        } else {
          // Cache MISS ou expiré → appeler l'API
          console.log('[PROFILE-SETUP] Calcul du thème natal (cache MISS)...');
          setIsCalculating(true);

          const response = await natalChart.calculate({
            date: birthDate.toISOString().split('T')[0], // YYYY-MM-DD
            time: birthTime.trim(),
            latitude: selectedPlace.latitude,
            longitude: selectedPlace.longitude,
            place_name: selectedPlace.displayName,
            // timezone supprimé - sera auto-détecté par le backend
          });

          setChart(response); // Stocke le chart + timestamp
          console.log('[PROFILE-SETUP] ✅ Thème natal calculé et mis en cache');
        }
      } catch (natalError: any) {
        // Ne pas bloquer l'onboarding si le calcul échoue
        console.warn('[PROFILE-SETUP] ⚠️ Échec calcul natal (non bloquant):', natalError.message);
        setIsCalculating(false); // Reset flag on error
      }

      // Naviguer vers la prochaine étape avec getOnboardingFlowState
      await goToNextOnboardingStep(router, 'PROFILE-SETUP', getOnboardingFlowState);
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
    router.back();
  };

  const formatDateDisplay = () => {
    return birthDate.toLocaleDateString('fr-FR', {
      day: 'numeric',
      month: 'long',
      year: 'numeric',
    });
  };

  // Sélection de date simplifiée (sans DateTimePicker pour éviter dépendances)
  const handleDateChange = (type: 'day' | 'month' | 'year', value: number) => {
    const newDate = new Date(birthDate);
    if (type === 'day') {
      newDate.setDate(value);
    } else if (type === 'month') {
      newDate.setMonth(value);
    } else if (type === 'year') {
      newDate.setFullYear(value);
    }
    setBirthDate(newDate);
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
            <Text style={styles.headerTitle}>Étape 2/3</Text>
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

            {/* Form */}
            <View style={styles.form}>
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

              {/* Date de naissance */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>Date de naissance</Text>
                <TouchableOpacity
                  style={styles.dateButton}
                  onPress={() => setShowDatePicker(!showDatePicker)}
                >
                  <Text style={styles.dateButtonText}>{formatDateDisplay()}</Text>
                  <Text style={styles.dateButtonIcon}>📅</Text>
                </TouchableOpacity>
              </View>

              {showDatePicker && (
                <View style={styles.datePickerSimple}>
                  <Text style={styles.datePickerHint}>
                    Utilisez les flèches pour ajuster la date
                  </Text>
                  <View style={styles.datePickerRow}>
                    <Text style={styles.datePickerLabel}>Jour:</Text>
                    <TouchableOpacity
                      onPress={() => handleDateChange('day', birthDate.getDate() - 1)}
                    >
                      <Text style={styles.datePickerButton}>-</Text>
                    </TouchableOpacity>
                    <Text style={styles.datePickerValue}>{birthDate.getDate()}</Text>
                    <TouchableOpacity
                      onPress={() => handleDateChange('day', birthDate.getDate() + 1)}
                    >
                      <Text style={styles.datePickerButton}>+</Text>
                    </TouchableOpacity>
                  </View>
                  <View style={styles.datePickerRow}>
                    <Text style={styles.datePickerLabel}>Mois:</Text>
                    <TouchableOpacity
                      onPress={() => handleDateChange('month', birthDate.getMonth() - 1)}
                    >
                      <Text style={styles.datePickerButton}>-</Text>
                    </TouchableOpacity>
                    <Text style={styles.datePickerValue}>{birthDate.getMonth() + 1}</Text>
                    <TouchableOpacity
                      onPress={() => handleDateChange('month', birthDate.getMonth() + 1)}
                    >
                      <Text style={styles.datePickerButton}>+</Text>
                    </TouchableOpacity>
                  </View>
                  <View style={styles.datePickerRow}>
                    <Text style={styles.datePickerLabel}>Année:</Text>
                    <TouchableOpacity
                      onPress={() => handleDateChange('year', birthDate.getFullYear() - 1)}
                    >
                      <Text style={styles.datePickerButton}>-</Text>
                    </TouchableOpacity>
                    <Text style={styles.datePickerValue}>{birthDate.getFullYear()}</Text>
                    <TouchableOpacity
                      onPress={() => handleDateChange('year', birthDate.getFullYear() + 1)}
                    >
                      <Text style={styles.datePickerButton}>+</Text>
                    </TouchableOpacity>
                  </View>
                </View>
              )}

              {/* Heure de naissance */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>Heure de naissance</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Ex: 14:30"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={birthTime}
                  onChangeText={setBirthTime}
                  keyboardType="numbers-and-punctuation"
                />
              </View>

              {/* Lieu de naissance avec autocomplete */}
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
    marginBottom: spacing.xxl,
    lineHeight: 22,
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
  dateButton: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    borderWidth: 2,
    borderColor: 'rgba(183, 148, 246, 0.3)',
  },
  dateButtonText: {
    fontSize: fonts.sizes.lg,
    color: colors.text,
    fontWeight: '500',
  },
  dateButtonIcon: {
    fontSize: 20,
  },
  datePickerSimple: {
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    gap: spacing.sm,
  },
  datePickerHint: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.6)',
    textAlign: 'center',
    marginBottom: spacing.xs,
  },
  datePickerRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: spacing.xs,
  },
  datePickerLabel: {
    fontSize: fonts.sizes.md,
    color: colors.accent,
    fontWeight: '600',
    width: 60,
  },
  datePickerButton: {
    fontSize: 24,
    color: colors.accent,
    paddingHorizontal: spacing.md,
  },
  datePickerValue: {
    fontSize: fonts.sizes.lg,
    color: colors.text,
    fontWeight: 'bold',
    minWidth: 60,
    textAlign: 'center',
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
});
