/**
 * Onboarding - Setup profil (prénom + date de naissance)
 */

import React, { useState } from 'react';
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
import { geocodePlace } from '../../services/geocoding';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

export default function ProfileSetupScreen() {
  const router = useRouter();
  const { setProfileData, profileData } = useOnboardingStore();
  const { setChart } = useNatalStore();

  const [name, setName] = useState(profileData?.name || '');
  const [birthDate, setBirthDate] = useState<Date>(
    profileData?.birthDate || new Date(2000, 0, 1)
  );
  const [birthTime, setBirthTime] = useState(profileData?.birthTime || '12:00');
  const [birthPlace, setBirthPlace] = useState(profileData?.birthPlace || '');
  const [birthTimezone, setBirthTimezone] = useState(profileData?.birthTimezone || 'Europe/Paris');
  const [showDatePicker, setShowDatePicker] = useState(false);
  const [isCalculating, setIsCalculating] = useState(false);

  const handleNext = async () => {
    // Validation
    if (!name.trim()) {
      Alert.alert('Nom requis', 'Veuillez entrer votre prénom');
      return;
    }

    if (!birthPlace.trim()) {
      Alert.alert('Lieu requis', 'Veuillez entrer votre lieu de naissance');
      return;
    }

    if (!birthTime.trim()) {
      Alert.alert('Heure requise', 'Veuillez entrer votre heure de naissance');
      return;
    }

    setIsCalculating(true);

    try {
      // 1) Géocoder le lieu de naissance
      console.log('[PROFILE-SETUP] Géocodage du lieu:', birthPlace);
      const coords = await geocodePlace(birthPlace);
      console.log('[PROFILE-SETUP] Coordonnées:', coords);

      // 2) Sauvegarder le profil complet avec coordonnées
      await setProfileData({
        name: name.trim(),
        birthDate,
        birthTime: birthTime.trim(),
        birthPlace: birthPlace.trim(),
        birthLatitude: coords.latitude,
        birthLongitude: coords.longitude,
        birthTimezone: birthTimezone.trim(),
      });

      console.log('[PROFILE-SETUP] Profil sauvegardé →', {
        name: name.trim(),
        birthDate,
        birthTime: birthTime.trim(),
        birthPlace: birthPlace.trim(),
      });

      // 3) Calculer le thème natal automatiquement (NON BLOQUANT)
      try {
        console.log('[PROFILE-SETUP] Calcul du thème natal...');
        const response = await natalChart.calculate({
          date: birthDate.toISOString().split('T')[0], // YYYY-MM-DD
          time: birthTime.trim(),
          latitude: coords.latitude,
          longitude: coords.longitude,
          place_name: birthPlace.trim(),
          timezone: birthTimezone.trim(),
        });

        setChart(response);
        console.log('[PROFILE-SETUP] ✅ Thème natal calculé automatiquement');
      } catch (natalError: any) {
        // Ne pas bloquer l'onboarding si le calcul échoue
        console.warn('[PROFILE-SETUP] ⚠️ Échec calcul natal (non bloquant):', natalError.message);
      }

      // 4) Passer au consentement RGPD
      router.push('/onboarding/consent');
    } catch (error: any) {
      console.error('[PROFILE-SETUP] Erreur:', error);

      // Gérer les erreurs de géocodage
      if (error.message === 'Lieu introuvable') {
        Alert.alert('Lieu introuvable', 'Merci de préciser la ville et le pays (ex: Paris, France)');
      } else if (error.message?.includes('Timeout')) {
        Alert.alert('Erreur', 'Le géocodage a pris trop de temps, réessayez');
      } else {
        Alert.alert('Erreur', error.message || 'Impossible de sauvegarder le profil');
      }
    } finally {
      setIsCalculating(false);
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
            <Text style={styles.headerTitle}>Étape 1/4</Text>
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

              {/* Lieu de naissance */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>Lieu de naissance</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Ex: Paris, France"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={birthPlace}
                  onChangeText={setBirthPlace}
                  autoCapitalize="words"
                />
              </View>

              {/* Timezone (optionnel, masqué par défaut) */}
              <View style={styles.inputGroup}>
                <Text style={styles.label}>Timezone (optionnel)</Text>
                <TextInput
                  style={styles.input}
                  placeholder="Ex: Europe/Paris"
                  placeholderTextColor="rgba(255,255,255,0.4)"
                  value={birthTimezone}
                  onChangeText={setBirthTimezone}
                />
              </View>

              {/* Info box */}
              <View style={styles.infoBox}>
                <Text style={styles.infoIcon}>ℹ️</Text>
                <Text style={styles.infoText}>
                  Ces informations nous permettent de calculer ton thème natal complet pour des
                  prévisions personnalisées
                </Text>
              </View>
            </View>
          </ScrollView>

          {/* Footer */}
          <View style={styles.footer}>
            <TouchableOpacity
              style={[styles.nextButton, isCalculating && styles.nextButtonDisabled]}
              onPress={handleNext}
              activeOpacity={0.8}
              disabled={isCalculating}
            >
              <LinearGradient
                colors={[colors.accent, colors.accentDark || colors.accent]}
                style={styles.nextButtonGradient}
                start={{ x: 0, y: 0 }}
                end={{ x: 1, y: 0 }}
              >
                {isCalculating ? (
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
