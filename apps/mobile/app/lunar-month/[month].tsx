/**
 * Écran détail d'un mois lunaire
 * Route dynamique : /lunar-month/[month]
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter, useLocalSearchParams } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

export default function LunarMonthScreen() {
  const router = useRouter();
  const { month } = useLocalSearchParams<{ month: string }>();

  // Formatage du mois pour affichage
  const formatMonth = (monthParam: string | undefined) => {
    if (!monthParam) return 'Mois inconnu';
    
    // Format attendu : YYYY-MM ou similaire
    try {
      const [year, monthNum] = monthParam.split('-');
      const monthNames = [
        'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
        'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
      ];
      const monthIndex = parseInt(monthNum, 10) - 1;
      if (monthIndex >= 0 && monthIndex < 12) {
        return `${monthNames[monthIndex]} ${year}`;
      }
      return monthParam;
    } catch {
      return monthParam;
    }
  };

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <TouchableOpacity
            style={styles.backButton}
            onPress={() => router.back()}
          >
            <Text style={styles.backText}>← Retour</Text>
          </TouchableOpacity>
          
          <View style={styles.titleContainer}>
            <Text style={styles.title}>🌙 Mois Lunaire</Text>
            <Text style={styles.monthText}>{formatMonth(month)}</Text>
          </View>
        </View>

        {/* Contenu placeholder */}
        <View style={styles.content}>
          <Text style={styles.placeholderText}>
            Détails du mois lunaire à venir
          </Text>
          <Text style={styles.placeholderSubtext}>
            Cette fonctionnalité sera implémentée prochainement
          </Text>
        </View>
      </ScrollView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    padding: spacing.lg,
    paddingTop: 60,
  },
  header: {
    marginBottom: spacing.xl,
  },
  backButton: {
    marginBottom: spacing.md,
  },
  backText: {
    ...fonts.body,
    color: colors.accent,
    fontSize: 16,
  },
  titleContainer: {
    alignItems: 'center',
  },
  title: {
    ...fonts.h1,
    color: colors.text,
    marginBottom: spacing.sm,
  },
  monthText: {
    ...fonts.h2,
    color: colors.gold,
  },
  content: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.xl,
    alignItems: 'center',
    marginTop: spacing.lg,
  },
  placeholderText: {
    ...fonts.h3,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  placeholderSubtext: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
  },
});

