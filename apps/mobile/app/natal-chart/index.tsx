/**
 * Écran intermédiaire - Résumé des infos profil + bouton "Calculer mon thème natal"
 * Affiche les infos déjà saisies et propose de calculer ou voir le thème
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  Modal,
  TextInput,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { useOnboardingStore } from '../../stores/useOnboardingStore';
import { useNatalStore } from '../../stores/useNatalStore';
import { natalChart } from '../../services/api';
import { geocodePlace } from '../../services/geocoding';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

export default function NatalChartIndexScreen() {
  const router = useRouter();
  const { profileData, setProfileData } = useOnboardingStore();
  const { chart, setChart, setLoading, loading, clearChart } = useNatalStore();
  const [isCalculating, setIsCalculating] = useState(false);
  const [showLoadingModal, setShowLoadingModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  
  // États pour le formulaire d'édition
  const [editName, setEditName] = useState('');
  const [editBirthDate, setEditBirthDate] = useState<Date>(new Date(2000, 0, 1));
  const [editBirthTime, setEditBirthTime] = useState('');
  const [editBirthPlace, setEditBirthPlace] = useState('');
  // birthTimezone supprimé - sera auto-détecté par le backend
  const [showDatePicker, setShowDatePicker] = useState(false);
  const [isSaving, setIsSaving] = useState(false);

  // Vérifier si un thème est déjà calculé
  const hasChart = !!chart;

  // Initialiser les valeurs d'édition depuis profileData
  useEffect(() => {
    if (profileData) {
      setEditName(profileData.name || '');
      setEditBirthDate(profileData.birthDate instanceof Date ? profileData.birthDate : (profileData.birthDate ? new Date(profileData.birthDate) : new Date(2000, 0, 1)));
      setEditBirthTime(profileData.birthTime || '12:00');
      setEditBirthPlace(profileData.birthPlace || '');
      // birthTimezone supprimé - sera auto-détecté par le backend
    }
  }, [profileData, showEditModal]);

  // Helper pour formatter la date de naissance en évitant le décalage de timezone
  const formatBirthDateISO = (value: unknown): string => {
    // Date stockée en Date JS
    if (value instanceof Date) {
      const year = value.getFullYear();
      const month = `${value.getMonth() + 1}`.padStart(2, '0');
      const day = `${value.getDate()}`.padStart(2, '0');
      return `${year}-${month}-${day}`;
    }
    // Date déjà en string YYYY-MM-DD
    if (typeof value === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(value)) {
      return value;
    }
    return 'Non renseigné';
  };

  // Préparer les données d'affichage depuis profileData
  const displayName = profileData?.name || 'Non renseigné';
  const displayDate = profileData?.birthDate
    ? formatBirthDateISO(profileData.birthDate)
    : 'Non renseigné';
  const displayTime = profileData?.birthTime || 'Non renseigné';
  const displayPlace = profileData?.birthPlace || 'Non renseigné';
  // displayTimezone supprimé - timezone auto-détecté par le backend
  const displayCoords =
    profileData?.birthLatitude && profileData?.birthLongitude
      ? `${profileData.birthLatitude.toFixed(4)}, ${profileData.birthLongitude.toFixed(4)}`
      : 'Non renseigné';

  const handleCalculate = async () => {
    // Vérifier que les données minimales sont présentes
    if (!profileData?.birthDate || !profileData?.birthPlace) {
      Alert.alert(
        'Données manquantes',
        'Veuillez compléter votre profil (date de naissance et lieu) avant de calculer votre thème natal. Vous pouvez le faire dans les paramètres.'
      );
      return;
    }

    setIsCalculating(true);
    setShowLoadingModal(true);
    setLoading(true);

    try {
      // Préparer les données pour l'API
      const date =
        profileData.birthDate instanceof Date
          ? profileData.birthDate.toISOString().split('T')[0]
          : typeof profileData.birthDate === 'string'
          ? profileData.birthDate
          : null;

      if (!date) {
        throw new Error('Date de naissance invalide');
      }

      const time = profileData.birthTime || '12:00';
      const birthPlace = profileData.birthPlace || 'Paris, France';

      // Récupérer les coordonnées
      let coords;
      if (
        profileData.birthLatitude &&
        profileData.birthLongitude &&
        profileData.birthPlace === birthPlace.trim()
      ) {
        coords = {
          latitude: profileData.birthLatitude,
          longitude: profileData.birthLongitude,
        };
        console.log('[NATAL-CHART] Utilisation coordonnées depuis profileData');
      } else {
        console.log('[NATAL-CHART] Géocodage du lieu:', birthPlace);
        coords = await geocodePlace(birthPlace);
      }

      // Appel API Ephemeris (timezone auto-détecté par le backend)
      const response = await natalChart.calculate({
        date: date,
        time: time,
        latitude: coords.latitude,
        longitude: coords.longitude,
        place_name: birthPlace,
        // timezone supprimé - sera auto-détecté par le backend
      });

      // Sauvegarder le résultat dans le store
      setChart(response);
      setShowLoadingModal(false);
      setIsCalculating(false);

      // Naviguer vers l'écran résultat
      router.replace('/natal-chart/result');
    } catch (error: any) {
      console.error('[NATAL-CHART] Erreur calcul thème natal:', error);
      setShowLoadingModal(false);
      setIsCalculating(false);
      setLoading(false);

      // Gérer les erreurs
      if (error.message === 'Lieu introuvable') {
        Alert.alert('Lieu introuvable', 'Précise la ville + pays');
      } else if (error.message?.includes('Timeout')) {
        Alert.alert('Erreur', 'Le géocodage a pris trop de temps, réessayez');
      } else if (
        error.message?.includes('connexion') ||
        error.message?.includes('réseau')
      ) {
        Alert.alert('Erreur', 'Erreur de connexion, vérifiez votre réseau');
      } else {
        Alert.alert(
          'Erreur',
          error.response?.data?.detail ||
            error.message ||
            'Impossible de calculer le thème natal'
        );
      }
    }
  };

  const handleViewChart = () => {
    if (hasChart) {
      router.push('/natal-chart/result');
    }
  };

  const handleEditInfo = () => {
    setShowEditModal(true);
  };

  const handleSaveEdit = async () => {
    // Validation
    if (!editName.trim()) {
      Alert.alert('Nom requis', 'Veuillez entrer votre prénom');
      return;
    }

    if (!editBirthPlace.trim()) {
      Alert.alert('Lieu requis', 'Veuillez entrer votre lieu de naissance');
      return;
    }

    if (!editBirthTime.trim()) {
      Alert.alert('Heure requise', 'Veuillez entrer votre heure de naissance (format HH:MM)');
      return;
    }

    setIsSaving(true);

    try {
      // Géocoder le lieu de naissance
      console.log('[NATAL-CHART] Géocodage du lieu:', editBirthPlace);
      const coords = await geocodePlace(editBirthPlace);
      console.log('[NATAL-CHART] Coordonnées:', coords);

      // Sauvegarder le profil mis à jour
      await setProfileData({
        name: editName.trim(),
        birthDate: editBirthDate,
        birthTime: editBirthTime.trim(),
        birthPlace: editBirthPlace.trim(),
        birthLatitude: coords.latitude,
        birthLongitude: coords.longitude,
        // birthTimezone supprimé - sera auto-détecté par le backend
      });

      console.log('[NATAL-CHART] ✅ Profil mis à jour');

      // Effacer le thème calculé car les données ont changé
      clearChart();

      setShowEditModal(false);
      Alert.alert('Succès', 'Informations mises à jour. Tu peux maintenant recalculer ton thème natal.');
    } catch (error: any) {
      console.error('[NATAL-CHART] Erreur mise à jour:', error);
      
      if (error.message === 'Lieu introuvable') {
        Alert.alert('Lieu introuvable', 'Merci de préciser la ville et le pays (ex: Paris, France)');
      } else if (error.message?.includes('Timeout')) {
        Alert.alert('Erreur', 'Le géocodage a pris trop de temps, réessayez');
      } else {
        Alert.alert('Erreur', error.message || 'Impossible de mettre à jour les informations');
      }
    } finally {
      setIsSaving(false);
    }
  };

  const formatDateDisplay = (date: Date) => {
    return date.toLocaleDateString('fr-FR', {
      day: 'numeric',
      month: 'long',
      year: 'numeric',
    });
  };

  const handleDateChange = (type: 'day' | 'month' | 'year', value: number) => {
    const newDate = new Date(editBirthDate);
    if (type === 'day') {
      newDate.setDate(value);
    } else if (type === 'month') {
      newDate.setMonth(value);
    } else if (type === 'year') {
      newDate.setFullYear(value);
    }
    setEditBirthDate(newDate);
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
        {/* Header */}
        <View style={styles.header}>
          <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
            <Text style={styles.backText}>← Retour</Text>
          </TouchableOpacity>
        </View>

        <ScrollView
          contentContainerStyle={styles.scrollContent}
          showsVerticalScrollIndicator={false}
        >
          {/* Titre */}
          <View style={styles.titleSection}>
            <Text style={styles.emoji}>⭐</Text>
            <Text style={styles.title}>Thème Natal</Text>
            <Text style={styles.subtitle}>
              {hasChart
                ? 'Ton thème natal est prêt. Tu peux le consulter ou le mettre à jour si tes informations changent.'
                : 'Calcule ton thème natal complet avec les positions planétaires exactes.'}
            </Text>
          </View>

          {/* Résumé des informations */}
          <View style={styles.infoCard}>
            <View style={styles.infoCardHeader}>
              <Text style={styles.infoCardTitle}>📋 Informations de naissance</Text>
              <TouchableOpacity
                style={styles.editButton}
                onPress={handleEditInfo}
                activeOpacity={0.7}
              >
                <Text style={styles.editButtonText}>✏️ Modifier</Text>
              </TouchableOpacity>
            </View>

            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Nom :</Text>
              <Text style={styles.infoValue}>{displayName}</Text>
            </View>

            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Date :</Text>
              <Text style={styles.infoValue}>{displayDate}</Text>
            </View>

            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Heure :</Text>
              <Text style={styles.infoValue}>{displayTime}</Text>
            </View>

            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Lieu :</Text>
              <Text style={styles.infoValue}>{displayPlace}</Text>
            </View>

            <View style={styles.infoRow}>
              <Text style={styles.infoLabel}>Coordonnées :</Text>
              <Text style={styles.infoValue}>{displayCoords}</Text>
            </View>

            {(!profileData?.birthDate || !profileData?.birthPlace) && (
              <View style={styles.warningBox}>
                <Text style={styles.warningText}>
                  ⚠️ Certaines informations sont manquantes. Complète ton profil dans les paramètres pour un calcul précis.
                </Text>
              </View>
            )}
          </View>

          {/* Badge si déjà calculé */}
          {hasChart && (
            <View style={styles.badgeContainer}>
              <Text style={styles.badgeText}>✅ Thème natal déjà calculé</Text>
            </View>
          )}

          {/* Boutons d'action */}
          <View style={styles.actionsContainer}>
            <TouchableOpacity
              style={[styles.primaryButton, (isCalculating || loading) && styles.buttonDisabled]}
              onPress={handleCalculate}
              disabled={isCalculating || loading}
              activeOpacity={0.8}
            >
              <LinearGradient
                colors={[colors.accent, colors.accentDark || colors.accent]}
                style={styles.buttonGradient}
              >
                {isCalculating || loading ? (
                  <ActivityIndicator color={colors.text} />
                ) : (
                  <Text style={styles.primaryButtonText}>
                    {hasChart ? 'Mettre à jour mon thème natal ✨' : 'Calculer mon thème natal ✨'}
                  </Text>
                )}
              </LinearGradient>
            </TouchableOpacity>

            {hasChart && (
              <TouchableOpacity
                style={styles.secondaryButton}
                onPress={handleViewChart}
                activeOpacity={0.8}
              >
                <Text style={styles.secondaryButtonText}>Voir mon thème natal</Text>
              </TouchableOpacity>
            )}
          </View>
        </ScrollView>

        {/* Modal Loading pendant calcul */}
        <Modal
          visible={showLoadingModal}
          transparent
          animationType="fade"
          onRequestClose={() => {}} // Empêcher fermeture pendant calcul
        >
          <View style={styles.modalOverlay}>
            <View style={styles.modalContent}>
              <ActivityIndicator size="large" color={colors.accent} />
              <Text style={styles.modalText}>Consultation des astres en cours...</Text>
              <Text style={styles.modalSubtext}>
                Calcul des positions planétaires
              </Text>
            </View>
          </View>
        </Modal>

        {/* Modal Édition des informations */}
        <Modal
          visible={showEditModal}
          transparent
          animationType="slide"
          onRequestClose={() => setShowEditModal(false)}
        >
          <KeyboardAvoidingView
            behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
            style={styles.modalOverlay}
          >
            <View style={styles.editModalContent}>
              <View style={styles.editModalHeader}>
                <Text style={styles.editModalTitle}>Modifier les informations</Text>
                <TouchableOpacity
                  onPress={() => setShowEditModal(false)}
                  style={styles.closeButton}
                >
                  <Text style={styles.closeButtonText}>✕</Text>
                </TouchableOpacity>
              </View>

              <ScrollView
                contentContainerStyle={styles.editModalScroll}
                showsVerticalScrollIndicator={false}
                keyboardShouldPersistTaps="handled"
              >
                {/* Nom */}
                <View style={styles.editInputGroup}>
                  <Text style={styles.editLabel}>Prénom</Text>
                  <TextInput
                    style={styles.editInput}
                    placeholder="Ex: Marie"
                    placeholderTextColor="rgba(255,255,255,0.4)"
                    value={editName}
                    onChangeText={setEditName}
                    autoCapitalize="words"
                    autoCorrect={false}
                  />
                </View>

                {/* Date de naissance */}
                <View style={styles.editInputGroup}>
                  <Text style={styles.editLabel}>Date de naissance</Text>
                  <TouchableOpacity
                    style={styles.editDateButton}
                    onPress={() => setShowDatePicker(!showDatePicker)}
                  >
                    <Text style={styles.editDateButtonText}>{formatDateDisplay(editBirthDate)}</Text>
                    <Text style={styles.editDateButtonIcon}>📅</Text>
                  </TouchableOpacity>
                </View>

                {showDatePicker && (
                  <View style={styles.editDatePicker}>
                    <Text style={styles.editDatePickerHint}>
                      Utilisez les flèches pour ajuster la date
                    </Text>
                    <View style={styles.editDatePickerRow}>
                      <Text style={styles.editDatePickerLabel}>Jour:</Text>
                      <TouchableOpacity
                        onPress={() => handleDateChange('day', editBirthDate.getDate() - 1)}
                      >
                        <Text style={styles.editDatePickerButton}>-</Text>
                      </TouchableOpacity>
                      <Text style={styles.editDatePickerValue}>{editBirthDate.getDate()}</Text>
                      <TouchableOpacity
                        onPress={() => handleDateChange('day', editBirthDate.getDate() + 1)}
                      >
                        <Text style={styles.editDatePickerButton}>+</Text>
                      </TouchableOpacity>
                    </View>
                    <View style={styles.editDatePickerRow}>
                      <Text style={styles.editDatePickerLabel}>Mois:</Text>
                      <TouchableOpacity
                        onPress={() => handleDateChange('month', editBirthDate.getMonth() - 1)}
                      >
                        <Text style={styles.editDatePickerButton}>-</Text>
                      </TouchableOpacity>
                      <Text style={styles.editDatePickerValue}>{editBirthDate.getMonth() + 1}</Text>
                      <TouchableOpacity
                        onPress={() => handleDateChange('month', editBirthDate.getMonth() + 1)}
                      >
                        <Text style={styles.editDatePickerButton}>+</Text>
                      </TouchableOpacity>
                    </View>
                    <View style={styles.editDatePickerRow}>
                      <Text style={styles.editDatePickerLabel}>Année:</Text>
                      <TouchableOpacity
                        onPress={() => handleDateChange('year', editBirthDate.getFullYear() - 1)}
                      >
                        <Text style={styles.editDatePickerButton}>-</Text>
                      </TouchableOpacity>
                      <Text style={styles.editDatePickerValue}>{editBirthDate.getFullYear()}</Text>
                      <TouchableOpacity
                        onPress={() => handleDateChange('year', editBirthDate.getFullYear() + 1)}
                      >
                        <Text style={styles.editDatePickerButton}>+</Text>
                      </TouchableOpacity>
                    </View>
                  </View>
                )}

                {/* Heure de naissance */}
                <View style={styles.editInputGroup}>
                  <Text style={styles.editLabel}>Heure de naissance</Text>
                  <TextInput
                    style={styles.editInput}
                    placeholder="Ex: 14:30"
                    placeholderTextColor="rgba(255,255,255,0.4)"
                    value={editBirthTime}
                    onChangeText={setEditBirthTime}
                    keyboardType="numbers-and-punctuation"
                  />
                </View>

                {/* Lieu de naissance */}
                <View style={styles.editInputGroup}>
                  <Text style={styles.editLabel}>Lieu de naissance</Text>
                  <TextInput
                    style={styles.editInput}
                    placeholder="Ex: Paris, France"
                    placeholderTextColor="rgba(255,255,255,0.4)"
                    value={editBirthPlace}
                    onChangeText={setEditBirthPlace}
                    autoCapitalize="words"
                  />
                </View>
              </ScrollView>

              {/* Boutons d'action */}
              <View style={styles.editModalActions}>
                <TouchableOpacity
                  style={styles.editCancelButton}
                  onPress={() => setShowEditModal(false)}
                  activeOpacity={0.8}
                >
                  <Text style={styles.editCancelButtonText}>Annuler</Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={[styles.editSaveButton, isSaving && styles.editSaveButtonDisabled]}
                  onPress={handleSaveEdit}
                  disabled={isSaving}
                  activeOpacity={0.8}
                >
                  <LinearGradient
                    colors={[colors.accent, colors.accentDark || colors.accent]}
                    style={styles.editSaveButtonGradient}
                  >
                    {isSaving ? (
                      <ActivityIndicator color={colors.text} />
                    ) : (
                      <Text style={styles.editSaveButtonText}>Enregistrer</Text>
                    )}
                  </LinearGradient>
                </TouchableOpacity>
              </View>
            </View>
          </KeyboardAvoidingView>
        </Modal>
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
  infoCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.lg,
  },
  infoCardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.md,
  },
  infoCardTitle: {
    ...fonts.h3,
    color: colors.text,
    flex: 1,
  },
  editButton: {
    paddingVertical: spacing.xs,
    paddingHorizontal: spacing.md,
    borderRadius: borderRadius.sm,
    backgroundColor: 'rgba(183, 148, 246, 0.2)',
    borderWidth: 1,
    borderColor: colors.accent,
  },
  editButtonText: {
    ...fonts.bodySmall,
    color: colors.accent,
    fontWeight: '600',
  },
  infoRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: spacing.sm,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255, 255, 255, 0.1)',
  },
  infoLabel: {
    ...fonts.body,
    color: colors.textMuted,
    fontWeight: '600',
  },
  infoValue: {
    ...fonts.body,
    color: colors.text,
    flex: 1,
    textAlign: 'right',
    marginLeft: spacing.md,
  },
  warningBox: {
    backgroundColor: 'rgba(255, 193, 7, 0.15)',
    borderRadius: borderRadius.sm,
    padding: spacing.md,
    marginTop: spacing.md,
  },
  warningText: {
    ...fonts.bodySmall,
    color: 'rgba(255, 193, 7, 0.9)',
    textAlign: 'center',
  },
  badgeContainer: {
    backgroundColor: 'rgba(76, 175, 80, 0.15)',
    borderRadius: borderRadius.sm,
    padding: spacing.md,
    marginBottom: spacing.lg,
    alignItems: 'center',
  },
  badgeText: {
    ...fonts.body,
    color: 'rgba(76, 175, 80, 0.9)',
    fontWeight: '600',
  },
  actionsContainer: {
    gap: spacing.md,
  },
  primaryButton: {
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
    shadowColor: colors.accent,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 4,
  },
  buttonGradient: {
    paddingVertical: spacing.md + 4,
    alignItems: 'center',
    justifyContent: 'center',
  },
  primaryButtonText: {
    ...fonts.button,
    color: colors.text,
    fontSize: fonts.sizes.lg,
    fontWeight: 'bold',
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  secondaryButton: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: colors.accent,
  },
  secondaryButtonText: {
    ...fonts.button,
    color: colors.accent,
    fontSize: fonts.sizes.md,
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalContent: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    padding: spacing.xl,
    alignItems: 'center',
    minWidth: 250,
  },
  modalText: {
    ...fonts.h3,
    color: colors.text,
    marginTop: spacing.lg,
    textAlign: 'center',
  },
  modalSubtext: {
    ...fonts.body,
    color: colors.textMuted,
    marginTop: spacing.sm,
    textAlign: 'center',
  },
  // Styles pour le modal d'édition
  editModalContent: {
    backgroundColor: colors.cardBg,
    borderTopLeftRadius: borderRadius.lg,
    borderTopRightRadius: borderRadius.lg,
    maxHeight: '90%',
    paddingBottom: spacing.lg,
  },
  editModalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255, 255, 255, 0.1)',
  },
  editModalTitle: {
    ...fonts.h2,
    color: colors.text,
  },
  closeButton: {
    width: 32,
    height: 32,
    justifyContent: 'center',
    alignItems: 'center',
    borderRadius: borderRadius.sm,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
  },
  closeButtonText: {
    fontSize: 20,
    color: colors.text,
    fontWeight: 'bold',
  },
  editModalScroll: {
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.md,
  },
  editInputGroup: {
    marginBottom: spacing.lg,
  },
  editLabel: {
    ...fonts.bodySmall,
    color: colors.accent,
    fontWeight: '600',
    marginBottom: spacing.xs,
  },
  editInput: {
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    fontSize: fonts.sizes.md,
    color: colors.text,
    borderWidth: 2,
    borderColor: 'rgba(183, 148, 246, 0.3)',
  },
  editDateButton: {
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
  editDateButtonText: {
    fontSize: fonts.sizes.md,
    color: colors.text,
    fontWeight: '500',
  },
  editDateButtonIcon: {
    fontSize: 20,
  },
  editDatePicker: {
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginTop: spacing.sm,
    gap: spacing.sm,
  },
  editDatePickerHint: {
    fontSize: fonts.sizes.sm,
    color: 'rgba(255, 255, 255, 0.6)',
    textAlign: 'center',
    marginBottom: spacing.xs,
  },
  editDatePickerRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: spacing.xs,
  },
  editDatePickerLabel: {
    fontSize: fonts.sizes.md,
    color: colors.accent,
    fontWeight: '600',
    width: 60,
  },
  editDatePickerButton: {
    fontSize: 24,
    color: colors.accent,
    paddingHorizontal: spacing.md,
  },
  editDatePickerValue: {
    fontSize: fonts.sizes.lg,
    color: colors.text,
    fontWeight: 'bold',
    minWidth: 60,
    textAlign: 'center',
  },
  editModalActions: {
    flexDirection: 'row',
    gap: spacing.md,
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.md,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255, 255, 255, 0.1)',
  },
  editCancelButton: {
    flex: 1,
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.3)',
  },
  editCancelButtonText: {
    ...fonts.button,
    color: colors.textMuted,
  },
  editSaveButton: {
    flex: 1,
    borderRadius: borderRadius.md,
    overflow: 'hidden',
  },
  editSaveButtonDisabled: {
    opacity: 0.6,
  },
  editSaveButtonGradient: {
    paddingVertical: spacing.md,
    alignItems: 'center',
    justifyContent: 'center',
  },
  editSaveButtonText: {
    ...fonts.button,
    color: colors.text,
    fontWeight: 'bold',
  },
});

