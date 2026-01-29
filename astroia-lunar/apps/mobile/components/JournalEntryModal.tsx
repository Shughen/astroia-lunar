/**
 * JournalEntryModal
 * Modal pour créer/éditer une entrée de journal quotidienne
 *
 * Features:
 * - Texte libre illimité (ou limite configurable)
 * - Contexte lunaire affiché (phase + signe)
 * - Save/Delete/Cancel
 * - Feedback utilisateur (saved/deleted)
 */

import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  TextInput,
  StyleSheet,
  Modal,
  Pressable,
  Alert,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
  ActivityIndicator,
} from 'react-native';
import { useTranslation } from 'react-i18next';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { JournalEntry, CreateJournalEntryPayload } from '../types/journal';
import {
  getJournalEntry,
  saveJournalEntry,
  deleteJournalEntry,
} from '../services/journalService';
import { getTodayDateString, getPhaseKey } from '../utils/ritualHelpers';
import { MoonPhase } from '../types/ritual';

interface JournalEntryModalProps {
  visible: boolean;
  onClose: () => void;
  date?: string; // Date YYYY-MM-DD (défaut: aujourd'hui)
  moonContext: {
    phase: MoonPhase;
    sign: string;
  };
}

const MAX_LENGTH = 5000; // Limite caractères (optionnel)

export function JournalEntryModal({
  visible,
  onClose,
  date,
  moonContext,
}: JournalEntryModalProps) {
  const { t } = useTranslation();
  const [text, setText] = useState('');
  const [existingEntry, setExistingEntry] = useState<JournalEntry | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isSaving, setIsSaving] = useState(false);

  const targetDate = date || getTodayDateString();

  // Charger entrée existante si présente
  useEffect(() => {
    if (visible) {
      loadExistingEntry();
    }
  }, [visible, targetDate]);

  const loadExistingEntry = async () => {
    setIsLoading(true);
    try {
      const result = await getJournalEntry(targetDate);
      if (result.exists && result.entry) {
        setExistingEntry(result.entry);
        setText(result.entry.text);
      } else {
        setExistingEntry(null);
        setText('');
      }
    } catch (error) {
      console.error('[JournalEntryModal] Error loading entry:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSave = async () => {
    if (!text.trim()) {
      Alert.alert(
        t('journal.emptyState'),
        'Écrivez quelque chose avant de sauvegarder.'
      );
      return;
    }

    setIsSaving(true);
    try {
      const payload: CreateJournalEntryPayload = {
        date: targetDate,
        text: text.trim(),
        moonContext,
      };

      await saveJournalEntry(payload);
      Alert.alert('✓', t('journal.saved'));
      onClose();
    } catch (error) {
      console.error('[JournalEntryModal] Error saving entry:', error);
      Alert.alert('Erreur', 'Impossible de sauvegarder l\'entrée.');
    } finally {
      setIsSaving(false);
    }
  };

  const handleDelete = () => {
    if (!existingEntry) return;

    Alert.alert(
      t('journal.delete'),
      t('journal.deleteConfirm'),
      [
        { text: t('journal.cancel'), style: 'cancel' },
        {
          text: t('journal.delete'),
          style: 'destructive',
          onPress: async () => {
            try {
              await deleteJournalEntry(existingEntry.id);
              Alert.alert('✓', t('journal.deleted'));
              onClose();
            } catch (error) {
              console.error('[JournalEntryModal] Error deleting entry:', error);
              Alert.alert('Erreur', 'Impossible de supprimer l\'entrée.');
            }
          },
        },
      ]
    );
  };

  const handleCancel = () => {
    // Réinitialiser texte si modifié
    if (existingEntry) {
      setText(existingEntry.text);
    } else {
      setText('');
    }
    onClose();
  };

  return (
    <Modal
      visible={visible}
      animationType="slide"
      presentationStyle="pageSheet"
      onRequestClose={handleCancel}
    >
      <KeyboardAvoidingView
        style={styles.container}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
      >
        {/* Header */}
        <View style={styles.header}>
          <Pressable onPress={handleCancel} style={styles.headerButton}>
            <Text style={styles.headerButtonText}>{t('journal.cancel')}</Text>
          </Pressable>
          <Text style={styles.headerTitle}>{t('journal.title')}</Text>
          <Pressable
            onPress={handleSave}
            style={styles.headerButton}
            disabled={isSaving}
          >
            {isSaving ? (
              <ActivityIndicator size="small" color={colors.accent} />
            ) : (
              <Text style={[styles.headerButtonText, styles.saveButton]}>
                {t('journal.save')}
              </Text>
            )}
          </Pressable>
        </View>

        <ScrollView
          style={styles.content}
          contentContainerStyle={styles.scrollContent}
          keyboardShouldPersistTaps="handled"
        >
          {/* Contexte lunaire */}
          <View style={styles.moonContextBadge}>
            <Text style={styles.moonContextText}>
              {t('journal.moonContext', {
                phase: moonContext.phase,
                sign: moonContext.sign,
              })}
            </Text>
          </View>

          {/* Titre question dynamique par phase */}
          <Text style={styles.entryTitle}>
            {t(`journal.prompts.${getPhaseKey(moonContext.phase)}`, {
              defaultValue: t('journal.entryTitle'),
            })}
          </Text>

          {/* Loading state */}
          {isLoading ? (
            <View style={styles.loadingContainer}>
              <ActivityIndicator size="large" color={colors.accent} />
            </View>
          ) : (
            <>
              {/* TextInput */}
              <TextInput
                style={styles.textInput}
                placeholder={t('journal.placeholder')}
                placeholderTextColor={colors.textMuted}
                value={text}
                onChangeText={setText}
                multiline
                maxLength={MAX_LENGTH}
                autoFocus={!existingEntry}
                textAlignVertical="top"
              />

              {/* Character count */}
              <Text style={styles.characterCount}>
                {t('journal.characterCount', { count: text.length })}
              </Text>

              {/* Delete button (si entrée existante) */}
              {existingEntry && (
                <Pressable
                  onPress={handleDelete}
                  style={styles.deleteButton}
                >
                  <Text style={styles.deleteButtonText}>
                    {t('journal.delete')}
                  </Text>
                </Pressable>
              )}
            </>
          )}
        </ScrollView>
      </KeyboardAvoidingView>
    </Modal>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: colors.darkBg[0],
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.md,
    paddingTop: spacing.xl + spacing.md, // Safe area top
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(183, 148, 246, 0.1)',
  },
  headerTitle: {
    ...fonts.h3,
    color: colors.text,
  },
  headerButton: {
    padding: spacing.sm,
    minWidth: 60,
  },
  headerButtonText: {
    ...fonts.button,
    color: colors.accent,
    fontSize: 16,
  },
  saveButton: {
    fontWeight: '700',
  },
  content: {
    flex: 1,
  },
  scrollContent: {
    padding: spacing.lg,
  },
  moonContextBadge: {
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    borderRadius: borderRadius.sm,
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
    alignSelf: 'flex-start',
    marginBottom: spacing.lg,
  },
  moonContextText: {
    ...fonts.bodySmall,
    color: colors.accent,
  },
  entryTitle: {
    ...fonts.h2,
    color: colors.text,
    marginBottom: spacing.lg,
  },
  loadingContainer: {
    paddingVertical: spacing.xxl,
    alignItems: 'center',
  },
  textInput: {
    ...fonts.body,
    color: colors.text,
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    minHeight: 200,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.2)',
  },
  characterCount: {
    ...fonts.caption,
    color: colors.textMuted,
    textAlign: 'right',
    marginTop: spacing.sm,
  },
  deleteButton: {
    marginTop: spacing.xl,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.sm,
    borderWidth: 1,
    borderColor: colors.error,
    alignItems: 'center',
  },
  deleteButtonText: {
    ...fonts.button,
    color: colors.error,
  },
});
