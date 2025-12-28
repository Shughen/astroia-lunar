/**
 * Timeline des révolutions lunaires
 * Affiche les 12 prochains retours lunaires triés par date
 */

import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  Modal,
  ScrollView,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import { lunarReturns, LunarReturn } from '../../services/api';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

type BadgeType = 'past' | 'today' | 'upcoming';

interface TimelineItem extends LunarReturn {
  badgeType: BadgeType;
}

export default function LunarReturnsTimelineScreen() {
  const router = useRouter();
  const [items, setItems] = useState<TimelineItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [generating, setGenerating] = useState(false);
  const [selectedItem, setSelectedItem] = useState<LunarReturn | null>(null);
  const [modalVisible, setModalVisible] = useState(false);

  useEffect(() => {
    loadTimeline();
  }, []);

  const loadTimeline = async () => {
    setLoading(true);
    try {
      // Utiliser getRolling() au lieu de getYear() pour les 12 prochains retours
      const returns = await lunarReturns.getRolling();
      
      // Trier par return_date asc et ajouter badges
      const now = new Date();
      const sortedReturns = returns
        .sort((a, b) => new Date(a.return_date).getTime() - new Date(b.return_date).getTime())
        .map((ret): TimelineItem => {
          const returnDate = new Date(ret.return_date);
          const diffDays = Math.floor((returnDate.getTime() - now.getTime()) / (1000 * 60 * 60 * 24));
          
          let badgeType: BadgeType = 'upcoming';
          if (diffDays < 0) {
            badgeType = 'past';
          } else if (diffDays === 0) {
            badgeType = 'today';
          }
          
          return { ...ret, badgeType };
        });
      
      setItems(sortedReturns);
    } catch (error: any) {
      // Si 404, ne pas afficher d'erreur (liste vide est normale)
      if (error.response?.status !== 404) {
        handleApiError(error);
      }
    } finally {
      setLoading(false);
    }
  };

  const handleGenerate = async () => {
    setGenerating(true);
    try {
      await lunarReturns.generate();
      Alert.alert('Succès', 'Retours lunaires générés avec succès ! ✨');
      // Recharger la timeline après génération
      await loadTimeline();
    } catch (error: any) {
      handleApiError(error);
    } finally {
      setGenerating(false);
    }
  };

  const handleApiError = (error: any) => {
    const errorData = error.response?.data;
    if (errorData?.detail && typeof errorData.detail === 'object') {
      const message = errorData.detail.detail || errorData.detail;
      const correlationId = errorData.detail.correlation_id;
      Alert.alert(
        'Erreur',
        `${message}${correlationId ? `\n\nRef: ${correlationId}` : ''}`
      );
    } else {
      Alert.alert('Erreur', error.response?.data?.detail || error.message || 'Une erreur est survenue');
    }
  };

  const formatDate = (dateString: string) => {
    const date = new Date(dateString);
    return date.toLocaleDateString('fr-FR', {
      day: 'numeric',
      month: 'long',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  const getBadgeLabel = (badgeType: BadgeType) => {
    switch (badgeType) {
      case 'past':
        return 'PASSÉ';
      case 'today':
        return 'AUJOURD\'HUI';
      case 'upcoming':
        return 'À VENIR';
    }
  };

  const getBadgeColor = (badgeType: BadgeType) => {
    switch (badgeType) {
      case 'past':
        return colors.textMuted;
      case 'today':
        return colors.accent;
      case 'upcoming':
        return colors.success;
    }
  };

  // Formate les aspects en liste lisible
  const formatAspects = (aspects?: Array<any>): string[] => {
    if (!aspects || aspects.length === 0) {
      return [];
    }
    return aspects.map((aspect) => {
      const planet1 = aspect.planet1 || aspect.planet_1 || 'Planet1';
      const planet2 = aspect.planet2 || aspect.planet_2 || 'Planet2';
      const type = aspect.type || aspect.aspect_type || 'aspect';
      const orb = aspect.orb !== undefined ? aspect.orb : null;
      
      let aspectText = `${planet1} ${type} ${planet2}`;
      if (orb !== null) {
        aspectText += `, orb ${orb.toFixed(1)}°`;
      }
      return aspectText;
    });
  };

  // Formate l'interprétation : split par \n\n et support basique du **gras**
  const formatInterpretation = (text?: string): React.ReactNode[] => {
    if (!text) {
      return [];
    }
    
    // Split par double saut de ligne
    const paragraphs = text.split('\n\n').filter(p => p.trim().length > 0);
    
    return paragraphs.map((paragraph, index) => {
      // Support très simple du **gras** : remplace **texte** par du texte en gras
      const parts: React.ReactNode[] = [];
      const regex = /\*\*(.*?)\*\*/g;
      let lastIndex = 0;
      let match;
      let keyCounter = 0;
      
      while ((match = regex.exec(paragraph)) !== null) {
        // Ajouter le texte avant le match
        if (match.index > lastIndex) {
          parts.push(
            <Text key={`text-${keyCounter++}`} style={styles.interpretationText}>
              {paragraph.substring(lastIndex, match.index)}
            </Text>
          );
        }
        // Ajouter le texte en gras
        parts.push(
          <Text key={`bold-${keyCounter++}`} style={[styles.interpretationText, styles.interpretationBold]}>
            {match[1]}
          </Text>
        );
        lastIndex = match.index + match[0].length;
      }
      
      // Ajouter le reste du texte
      if (lastIndex < paragraph.length) {
        parts.push(
          <Text key={`text-${keyCounter++}`} style={styles.interpretationText}>
            {paragraph.substring(lastIndex)}
          </Text>
        );
      }
      
      // Si aucun match, utiliser le texte tel quel
      if (parts.length === 0) {
        parts.push(
          <Text key={`text-${keyCounter++}`} style={styles.interpretationText}>
            {paragraph}
          </Text>
        );
      }
      
      return (
        <Text key={`para-${index}`} style={styles.interpretationParagraph}>
          {parts}
        </Text>
      );
    });
  };

  // Récupère le badgeType pour l'item sélectionné
  const getSelectedItemBadgeType = (): BadgeType | null => {
    if (!selectedItem) return null;
    const item = items.find(i => i.id === selectedItem.id);
    return item?.badgeType || null;
  };

  const renderItem = ({ item }: { item: TimelineItem }) => (
    <TouchableOpacity
      style={styles.item}
      onPress={() => {
        setSelectedItem(item);
        setModalVisible(true);
      }}
    >
      <View style={styles.itemHeader}>
        <View style={styles.itemLeft}>
          <Text style={styles.itemDate}>{formatDate(item.return_date)}</Text>
          {item.moon_sign && (
            <Text style={styles.itemDetails}>
              Lune en {item.moon_sign}
              {item.moon_house && ` • Maison ${item.moon_house}`}
            </Text>
          )}
        </View>
        <View style={[styles.badge, { backgroundColor: getBadgeColor(item.badgeType) }]}>
          <Text style={styles.badgeText}>{getBadgeLabel(item.badgeType)}</Text>
        </View>
      </View>
      {item.lunar_ascendant && (
        <Text style={styles.itemAscendant}>
          Ascendant: {item.lunar_ascendant}
        </Text>
      )}
    </TouchableOpacity>
  );

  const renderEmpty = () => (
    <View style={styles.emptyContainer}>
      <Text style={styles.emptyEmoji}>🌙</Text>
      <Text style={styles.emptyText}>Aucune révolution lunaire générée</Text>
      <TouchableOpacity
        style={styles.generateButton}
        onPress={handleGenerate}
        disabled={generating}
      >
        {generating ? (
          <ActivityIndicator color={colors.text} />
        ) : (
          <Text style={styles.generateButtonText}>Générer mes révolutions</Text>
        )}
      </TouchableOpacity>
    </View>
  );

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity onPress={() => router.back()} style={styles.backButton}>
          <Text style={styles.backButtonText}>← Retour</Text>
        </TouchableOpacity>
        <Text style={styles.title}>Mes révolutions lunaires</Text>
      </View>

      {loading ? (
        <View style={styles.loadingContainer}>
          <ActivityIndicator color={colors.accent} size="large" />
        </View>
      ) : (
        <FlatList
          data={items}
          renderItem={renderItem}
          keyExtractor={(item) => item.id.toString()}
          contentContainerStyle={styles.listContent}
          ListEmptyComponent={renderEmpty}
        />
      )}

      {/* Modal détail avec fiche structurée */}
      <Modal
        visible={modalVisible}
        transparent
        animationType="fade"
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContent}>
            <View style={styles.modalHeader}>
              <Text style={styles.modalTitle}>Détail révolution lunaire</Text>
              {selectedItem && getSelectedItemBadgeType() && (
                <View style={[styles.modalBadge, { backgroundColor: getBadgeColor(getSelectedItemBadgeType()!) }]}>
                  <Text style={styles.modalBadgeText}>
                    {getBadgeLabel(getSelectedItemBadgeType()!)}
                  </Text>
                </View>
              )}
            </View>
            
            <ScrollView 
              style={styles.modalScrollView}
              contentContainerStyle={styles.modalScrollContent}
              showsVerticalScrollIndicator={false}
            >
              {selectedItem && (
                <>
                  {/* Date/Heure */}
                  <View style={styles.detailSection}>
                    <Text style={styles.detailSectionTitle}>Date et heure</Text>
                    <Text style={styles.detailSectionValue}>
                      {formatDate(selectedItem.return_date)}
                    </Text>
                  </View>

                  {/* Ascendant lunaire, signe lunaire, maison */}
                  <View style={styles.detailSection}>
                    <Text style={styles.detailSectionTitle}>Position lunaire</Text>
                    <View style={styles.detailRow}>
                      {selectedItem.lunar_ascendant && (
                        <Text style={styles.detailValue}>
                          Ascendant: <Text style={styles.detailValueHighlight}>{selectedItem.lunar_ascendant}</Text>
                        </Text>
                      )}
                    </View>
                    <View style={styles.detailRow}>
                      {selectedItem.moon_sign && (
                        <Text style={styles.detailValue}>
                          Signe lunaire: <Text style={styles.detailValueHighlight}>{selectedItem.moon_sign}</Text>
                        </Text>
                      )}
                    </View>
                    {selectedItem.moon_house && (
                      <View style={styles.detailRow}>
                        <Text style={styles.detailValue}>
                          Maison: <Text style={styles.detailValueHighlight}>{selectedItem.moon_house}</Text>
                        </Text>
                      </View>
                    )}
                  </View>

                  {/* Aspects */}
                  {selectedItem.aspects && selectedItem.aspects.length > 0 && (
                    <View style={styles.detailSection}>
                      <Text style={styles.detailSectionTitle}>Aspects</Text>
                      {formatAspects(selectedItem.aspects).map((aspect, index) => (
                        <Text key={index} style={styles.aspectItem}>
                          • {aspect}
                        </Text>
                      ))}
                    </View>
                  )}

                  {/* Interprétation */}
                  {selectedItem.interpretation && (
                    <View style={styles.detailSection}>
                      <Text style={styles.detailSectionTitle}>Interprétation</Text>
                      <View style={styles.interpretationContainer}>
                        {formatInterpretation(selectedItem.interpretation)}
                      </View>
                    </View>
                  )}
                </>
              )}
            </ScrollView>

            <TouchableOpacity
              style={styles.modalCloseButton}
              onPress={() => setModalVisible(false)}
            >
              <Text style={styles.modalCloseButtonText}>Fermer</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  header: {
    paddingTop: 60,
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.md,
  },
  backButton: {
    marginBottom: spacing.sm,
  },
  backButtonText: {
    ...fonts.body,
    color: colors.accent,
  },
  title: {
    ...fonts.h1,
    color: colors.text,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  listContent: {
    padding: spacing.lg,
  },
  item: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.md,
  },
  itemHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'flex-start',
    marginBottom: spacing.xs,
  },
  itemLeft: {
    flex: 1,
    marginRight: spacing.md,
  },
  itemDate: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  itemDetails: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  itemAscendant: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginTop: spacing.xs,
  },
  badge: {
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: borderRadius.sm,
  },
  badgeText: {
    ...fonts.caption,
    color: colors.text,
    fontWeight: '600',
  },
  emptyContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: spacing.xl,
  },
  emptyEmoji: {
    fontSize: 64,
    marginBottom: spacing.md,
  },
  emptyText: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
    marginBottom: spacing.lg,
  },
  generateButton: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.xl,
    borderRadius: borderRadius.md,
  },
  generateButtonText: {
    ...fonts.button,
    color: colors.text,
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.8)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modalContent: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    width: '90%',
    maxHeight: '80%',
    flexDirection: 'column',
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.md,
  },
  modalTitle: {
    ...fonts.h2,
    color: colors.text,
    flex: 1,
  },
  modalBadge: {
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
    borderRadius: borderRadius.sm,
    marginLeft: spacing.md,
  },
  modalBadgeText: {
    ...fonts.caption,
    color: colors.text,
    fontWeight: '600',
  },
  modalScrollView: {
    flexShrink: 1,
    maxHeight: 400,
  },
  modalScrollContent: {
    paddingBottom: spacing.md,
  },
  detailSection: {
    marginBottom: spacing.lg,
  },
  detailSectionTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.sm,
  },
  detailSectionValue: {
    ...fonts.body,
    color: colors.textMuted,
  },
  detailRow: {
    marginBottom: spacing.xs,
  },
  detailValue: {
    ...fonts.body,
    color: colors.textMuted,
  },
  detailValueHighlight: {
    color: colors.text,
    fontWeight: '600',
  },
  aspectItem: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginBottom: spacing.xs,
    marginLeft: spacing.xs,
  },
  interpretationContainer: {
    marginTop: spacing.xs,
  },
  interpretationParagraph: {
    ...fonts.body,
    color: colors.textMuted,
    lineHeight: 24,
    marginBottom: spacing.md,
  },
  interpretationText: {
    ...fonts.body,
    color: colors.textMuted,
  },
  interpretationBold: {
    fontWeight: '600',
    color: colors.text,
  },
  modalCloseButton: {
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginTop: spacing.md,
  },
  modalCloseButtonText: {
    ...fonts.button,
    color: colors.text,
  },
});

