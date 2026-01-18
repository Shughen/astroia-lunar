/**
 * Écran Journal Quotidien (MVP - Backend API)
 * Permet un rituel quotidien simple avec sauvegarde backend
 */

import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TextInput,
  TouchableOpacity,
  Alert,
  ActivityIndicator,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useLocalSearchParams, useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { getAllJournalEntries, saveJournalEntry, getJournalEntry } from '../services/journalService';
import { JournalEntry as JournalEntryType } from '../types/journal';

const LinearGradientComponent = LinearGradient || (({ colors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: colors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

// Interface locale pour l'affichage (conversion depuis JournalEntryType)
interface DisplayJournalEntry {
  id: string;
  date: string;
  createdAtISO: string;
  text: string;
}

export default function JournalScreen() {
  const { prefill } = useLocalSearchParams<{ prefill?: string }>();
  const router = useRouter();
  const inputRef = useRef<TextInput | null>(null);
  const scrollRef = useRef<ScrollView | null>(null);
  const inputCardRef = useRef<View | null>(null);
  const savingLockRef = useRef(false);
  const [entries, setEntries] = useState<DisplayJournalEntry[]>([]);
  const [currentText, setCurrentText] = useState('');
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [prefillApplied, setPrefillApplied] = useState(false);
  const [inputCardY, setInputCardY] = useState<number | null>(null);

  // Charger les entrées au mount
  useEffect(() => {
    loadEntries();
  }, []);

  // Appliquer le prefill si disponible et si le champ est vide
  useEffect(() => {
    if (prefill && !prefillApplied && !currentText.trim()) {
      try {
        const decodedPrefill = decodeURIComponent(prefill);
        setCurrentText(decodedPrefill);
        setPrefillApplied(true);
        
        // Focus automatique, positionnement du curseur à la fin et scroll
        setTimeout(() => {
          inputRef.current?.focus();
          inputRef.current?.setNativeProps({
            selection: { start: decodedPrefill.length, end: decodedPrefill.length },
          });
          
          // Scroll automatique pour que l'input soit visible
          if (inputCardY !== null && scrollRef.current) {
            requestAnimationFrame(() => {
              scrollRef.current?.scrollTo({
                y: inputCardY - 24,
                animated: true,
              });
            });
          }
        }, 0);
      } catch (error) {
        console.error('[JOURNAL] Erreur décodage prefill:', error);
      }
    }
  }, [prefill, prefillApplied, currentText, inputCardY]);

  const loadEntries = async () => {
    try {
      setLoading(true);
      // Récupérer toutes les entrées depuis l'API
      const apiEntries = await getAllJournalEntries();

      // Convertir en format d'affichage et garder les 7 dernières
      const displayEntries: DisplayJournalEntry[] = apiEntries
        .slice(0, 7)
        .map((entry) => ({
          id: entry.date, // Utiliser la date comme ID pour la clé React
          date: entry.date,
          createdAtISO: new Date(entry.createdAt).toISOString(),
          text: entry.text,
        }));

      setEntries(displayEntries);
    } catch (error) {
      console.error('[JOURNAL] Erreur chargement:', error);
      Alert.alert('Erreur', 'Impossible de charger vos entrées. Vérifiez votre connexion.');
    } finally {
      setLoading(false);
    }
  };

  const saveEntry = async () => {
    // Protection contre les doubles sauvegardes (lock immédiat)
    if (savingLockRef.current) {
      return;
    }

    if (!currentText.trim()) {
      Alert.alert('Attention', 'Veuillez écrire quelque chose avant de sauvegarder');
      return;
    }

    savingLockRef.current = true;
    setSaving(true);

    try {
      const today = new Date().toISOString().split('T')[0]; // Format YYYY-MM-DD

      // Sauvegarder via l'API (crée ou met à jour)
      await saveJournalEntry({
        date: today,
        text: currentText.trim(),
        moonContext: {
          phase: 'New Moon', // Valeur par défaut, sera calculé côté backend si nécessaire
          sign: 'Unknown',
        },
      });

      // Recharger les entrées
      await loadEntries();
      setCurrentText('');

      Alert.alert(
        '✅ Sauvegardé',
        'Votre entrée a été enregistrée avec succès',
        [
          {
            text: 'Continuer',
            style: 'cancel',
            onPress: () => {
              setTimeout(() => {
                inputRef.current?.focus();
              }, 0);
            },
          },
          {
            text: '🌙 Retour au rituel',
            onPress: () => router.replace('/'),
          },
        ]
      );
    } catch (error) {
      console.error('[JOURNAL] Erreur sauvegarde:', error);
      Alert.alert('Erreur', 'Impossible de sauvegarder votre entrée. Vérifiez votre connexion.');
    } finally {
      savingLockRef.current = false;
      setSaving(false);
    }
  };

  const deleteEntry = async (dateId: string) => {
    Alert.alert(
      'Confirmer la suppression',
      'Voulez-vous vraiment supprimer cette entrée ?',
      [
        {
          text: 'Annuler',
          style: 'cancel',
        },
        {
          text: 'Supprimer',
          style: 'destructive',
          onPress: async () => {
            try {
              // Supprimer via l'API en utilisant la date
              const { deleteJournalEntry } = await import('../services/journalService');
              await deleteJournalEntry(dateId);

              // Recharger les entrées
              await loadEntries();
            } catch (error) {
              console.error('[JOURNAL] Erreur suppression:', error);
              Alert.alert('Erreur', 'Impossible de supprimer cette entrée. Vérifiez votre connexion.');
            }
          },
        },
      ]
    );
  };

  const formatDate = (isoString: string): string => {
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
  };

  const getFirstLine = (text: string): string => {
    const firstLine = text.split('\n')[0];
    return firstLine.length > 50 ? firstLine.substring(0, 50) + '...' : firstLine;
  };

  if (loading) {
    return (
      <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color={colors.accent} />
          <Text style={styles.loadingText}>Chargement...</Text>
        </View>
      </LinearGradientComponent>
    );
  }

  return (
    <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
      <KeyboardAvoidingView
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
        style={{ flex: 1 }}
        keyboardVerticalOffset={80}
      >
        <ScrollView
          ref={scrollRef}
          keyboardShouldPersistTaps="handled"
          contentContainerStyle={styles.scrollContent}
        >
        {/* Header */}
        <View style={styles.header}>
          <View style={styles.headerTop}>
            <TouchableOpacity style={styles.backButton} onPress={() => router.back()}>
              <Text style={styles.backButtonText}>← Retour</Text>
            </TouchableOpacity>
          </View>
          <Text style={styles.title}>📖 Journal Quotidien</Text>
          <Text style={styles.subtitle}>
            Un espace pour votre rituel quotidien
          </Text>
        </View>

        {/* Zone de saisie */}
        <View
          ref={inputCardRef}
          style={styles.inputCard}
          onLayout={(event) => {
            const { y } = event.nativeEvent.layout;
            setInputCardY(y);
          }}
        >
          <Text style={styles.cardTitle}>Nouvelle entrée</Text>
          <TextInput
            ref={inputRef}
            style={styles.textInput}
            value={currentText}
            onChangeText={setCurrentText}
            placeholder="Comment vous sentez-vous aujourd'hui ?"
            placeholderTextColor={colors.textMuted}
            multiline
            numberOfLines={6}
            textAlignVertical="top"
          />

          <TouchableOpacity
            style={[
              styles.saveButton,
              (saving || currentText.trim().length === 0) && styles.saveButtonDisabled,
            ]}
            onPress={saveEntry}
            disabled={saving || currentText.trim().length === 0}
          >
            {saving ? (
              <ActivityIndicator color={colors.text} />
            ) : (
              <Text style={styles.saveButtonText}>💾 Sauvegarder</Text>
            )}
          </TouchableOpacity>
        </View>

        {/* Liste des entrées */}
        <View style={styles.entriesList}>
          <Text style={styles.sectionTitle}>
            Mes 7 dernières entrées
          </Text>

          {entries.length === 0 ? (
            <View style={styles.emptyState}>
              <Text style={styles.emptyEmoji}>📝</Text>
              <Text style={styles.emptyText}>
                Aucune entrée pour le moment
              </Text>
              <Text style={styles.emptyHint}>
                Écrivez votre première entrée pour commencer !
              </Text>
            </View>
          ) : (
            entries.map((entry) => (
              <View key={entry.id} style={styles.entryCard}>
                <View style={styles.entryHeader}>
                  <Text style={styles.entryDate}>
                    {formatDate(entry.createdAtISO)}
                  </Text>
                  <TouchableOpacity
                    onPress={() => deleteEntry(entry.id)}
                    style={styles.deleteButton}
                  >
                    <Text style={styles.deleteButtonText}>🗑️</Text>
                  </TouchableOpacity>
                </View>

                <Text style={styles.entryPreview}>
                  {getFirstLine(entry.text)}
                </Text>

                {entry.text.split('\n').length > 1 && (
                  <Text style={styles.multilineIndicator}>
                    + {entry.text.split('\n').length - 1} ligne(s)
                  </Text>
                )}
              </View>
            ))
          )}
        </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </LinearGradientComponent>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    paddingTop: 60,
    paddingHorizontal: spacing.lg,
    paddingBottom: 140,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    ...fonts.body,
    color: colors.textMuted,
    marginTop: spacing.md,
  },
  header: {
    marginBottom: spacing.xl,
  },
  headerTop: {
    flexDirection: 'row',
    justifyContent: 'flex-start',
    marginBottom: spacing.md,
  },
  backButton: {
    paddingVertical: spacing.xs,
  },
  backButtonText: {
    color: colors.accent,
    fontSize: 16,
    fontWeight: '600',
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  subtitle: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
  },
  inputCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.xl,
    borderWidth: 2,
    borderColor: colors.accent,
  },
  cardTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.md,
  },
  textInput: {
    backgroundColor: 'rgba(0, 0, 0, 0.3)',
    borderRadius: borderRadius.sm,
    padding: spacing.md,
    color: colors.text,
    ...fonts.body,
    minHeight: 120,
    marginBottom: spacing.md,
  },
  saveButton: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    borderRadius: borderRadius.md,
    alignItems: 'center',
  },
  saveButtonDisabled: {
    opacity: 0.5,
  },
  saveButtonText: {
    ...fonts.button,
    color: colors.text,
  },
  sectionTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.md,
  },
  entriesList: {
    marginBottom: spacing.xl,
  },
  emptyState: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.xl,
    alignItems: 'center',
  },
  emptyEmoji: {
    fontSize: 48,
    marginBottom: spacing.md,
  },
  emptyText: {
    ...fonts.body,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  emptyHint: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    textAlign: 'center',
  },
  entryCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.md,
  },
  entryHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.sm,
  },
  entryDate: {
    ...fonts.bodySmall,
    color: colors.accent,
  },
  deleteButton: {
    padding: spacing.xs,
  },
  deleteButtonText: {
    fontSize: 18,
  },
  entryPreview: {
    ...fonts.body,
    color: colors.text,
    lineHeight: 20,
  },
  multilineIndicator: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginTop: spacing.xs,
    fontStyle: 'italic',
  },
});
