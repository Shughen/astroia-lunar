/**
 * Écran Journal Quotidien (MVP Local - AsyncStorage)
 * Permet un rituel quotidien simple avec sauvegarde locale
 */

import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TextInput,
  TouchableOpacity,
  Alert,
  ActivityIndicator,
} from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { LinearGradient } from 'expo-linear-gradient';
import { useLocalSearchParams } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

const LinearGradientComponent = LinearGradient || (({ colors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: colors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

interface JournalEntry {
  id: string;
  createdAtISO: string;
  text: string;
}

const STORAGE_KEY = 'journal_entries';

export default function JournalScreen() {
  const { prefill } = useLocalSearchParams<{ prefill?: string }>();
  const [entries, setEntries] = useState<JournalEntry[]>([]);
  const [currentText, setCurrentText] = useState('');
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [prefillApplied, setPrefillApplied] = useState(false);

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
      } catch (error) {
        console.error('[JOURNAL] Erreur décodage prefill:', error);
      }
    }
  }, [prefill, prefillApplied, currentText]);

  const loadEntries = async () => {
    try {
      setLoading(true);
      const stored = await AsyncStorage.getItem(STORAGE_KEY);

      if (stored) {
        const parsed: JournalEntry[] = JSON.parse(stored);
        // Trier par date décroissante et garder les 7 dernières
        const sorted = parsed
          .sort((a, b) => new Date(b.createdAtISO).getTime() - new Date(a.createdAtISO).getTime())
          .slice(0, 7);
        setEntries(sorted);
      }
    } catch (error) {
      console.error('[JOURNAL] Erreur chargement:', error);
      Alert.alert('Erreur', 'Impossible de charger vos entrées');
    } finally {
      setLoading(false);
    }
  };

  const saveEntry = async () => {
    if (!currentText.trim()) {
      Alert.alert('Attention', 'Veuillez écrire quelque chose avant de sauvegarder');
      return;
    }

    try {
      setSaving(true);

      const newEntry: JournalEntry = {
        id: Date.now().toString(),
        createdAtISO: new Date().toISOString(),
        text: currentText.trim(),
      };

      // Ajouter la nouvelle entrée au début
      const updated = [newEntry, ...entries];

      // Garder uniquement les 7 dernières
      const trimmed = updated.slice(0, 7);

      // Sauvegarder
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(trimmed));

      // Mettre à jour l'état
      setEntries(trimmed);
      setCurrentText('');

      Alert.alert('✅ Sauvegardé', 'Votre entrée a été enregistrée avec succès');
    } catch (error) {
      console.error('[JOURNAL] Erreur sauvegarde:', error);
      Alert.alert('Erreur', 'Impossible de sauvegarder votre entrée');
    } finally {
      setSaving(false);
    }
  };

  const deleteEntry = async (id: string) => {
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
              const filtered = entries.filter((e) => e.id !== id);
              await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(filtered));
              setEntries(filtered);
            } catch (error) {
              console.error('[JOURNAL] Erreur suppression:', error);
              Alert.alert('Erreur', 'Impossible de supprimer cette entrée');
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
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>📖 Journal Quotidien</Text>
          <Text style={styles.subtitle}>
            Un espace pour votre rituel quotidien
          </Text>
        </View>

        {/* Zone de saisie */}
        <View style={styles.inputCard}>
          <Text style={styles.cardTitle}>Nouvelle entrée</Text>
          <TextInput
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
            style={[styles.saveButton, saving && styles.saveButtonDisabled]}
            onPress={saveEntry}
            disabled={saving}
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
    paddingBottom: spacing.xl,
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
    alignItems: 'center',
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
